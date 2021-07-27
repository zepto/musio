#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of module music using modplug.
# Copyright (C) 2012 Josiah Gordon <josiahg@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""ModPlug is a class to handle module music using the modplug library."""

from typing import Any, Callable

from .conversion_util import swap_endian
from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper

_modplug = LazyImport('modplug._modplug', globals(), locals(),
                      ['_modplug'], 1)

__supported_dict = {
    'ext': ['.mod', '.xm', '.s3m', '.it'],
    'handler': 'ModPlugFile',
    'default': True,
    'dependencies': {
        'ctypes': ['modplug'],
        'python': []
    }
}


class ModPlugFile(AudioIO):
    """Modplug module file.

    A file like interface to module music files (it, xm, s3m, mod) using the
    modplug library.
    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, **kwargs):
        """Initialize the playback settings of the player."""
        super(ModPlugFile, self).__init__(filename, 'r', depth, rate, channels)

        self._unsigned = unsigned
        self._bigendian = bigendian

        if depth == 8:
            self._unsigned = True

        # Create modplug settings object.
        self._modplug_settings = _modplug.ModPlug_Settings()

        # Get the default settings.
        _modplug.ModPlug_GetSettings(_modplug.byref(self._modplug_settings))

        # Set the settings to the values we want.
        self._modplug_settings.mBits = depth
        self._modplug_settings.mChannels = channels
        self._modplug_settings.mFrequency = rate
        self._modplug_settings.mStereoSeparation = 256
        self._modplug_settings.mMaxMixChannels = 256
        self._modplug_settings.mResamplingMode = _modplug.MODPLUG_RESAMPLE_FIR

        # Loop forever.
        self._modplug_settings.mLoopCount = -1

        # Set the settings.
        _modplug.ModPlug_SetSettings(_modplug.byref(self._modplug_settings))

        # Open mod file.
        self._modplug_file = self._open(filename)

        # Load module info.
        self._load_info(self._modplug_file)

        # Get the length.
        self._length = _modplug.ModPlug_GetLength(self._modplug_file)

        # Define the conversion function.
        if depth == 16 and bigendian:
            self._proc_func = swap_endian
        else:
            self._proc_func = lambda data_list: data_list

        self._pos = 0

    def to_seconds(self, position: int) -> float:
        """Convert the provided position/length to seconds."""
        return position / 1000

    def _get_position(self) -> int:
        """Return the current playback position in milliseconds."""
        return self._pos

    def _set_position(self, position: int):
        """Change the position of playback."""
        self._pos = position
        _modplug.ModPlug_Seek(self._modplug_file, position)

    def _open(self, filename: str) -> Any:
        """Load the specified file."""
        with open(filename, 'rb') as mod_file:
            mod_data = mod_file.read()

        modplug_file = _modplug.ModPlug_Load(mod_data, len(mod_data))
        if not modplug_file:
            raise OSError(f"Error loading file: {filename}")

        self._closed = False

        return modplug_file

    def _load_info(self, modplug_file: Any):
        """Load module info.

        Load the information such as the module name and message and the sample
        and instrument names.
        """
        def load_list(key: str, name_func: Callable, modplug_file: Any,
                      count: int) -> list[str]:
            """Fill list with data.

            Load a list of names and filenames from sig_data into fill_list.
            """
            fill_list = []

            name_buffer = _modplug.create_string_buffer(256)
            for i in range(count):
                name_func(modplug_file, i, name_buffer)
                if name_buffer:
                    name = name_buffer.value.decode('cp437', 'replace')
                    fill_list.append(f"{key.capitalize():8} {i:03} {name}")

            return fill_list

        num_smp = _modplug.ModPlug_NumSamples(modplug_file)
        if num_smp > 0:
            tmp_list = load_list(
                'sample',
                _modplug.ModPlug_SampleName,
                modplug_file,
                num_smp
            )
            if tmp_list:
                self._info_dict['samples'] = tmp_list

        num_ins = _modplug.ModPlug_NumInstruments(modplug_file)
        if num_ins > 0:
            tmp_list = load_list(
                'instrument',
                _modplug.ModPlug_InstrumentName,
                modplug_file,
                num_ins
            )
            if tmp_list:
                self._info_dict['instruments'] = tmp_list

        name = _modplug.ModPlug_GetName(modplug_file)
        name = name.decode('cp437', 'replace')
        self._info_dict['name'] = name

        mod_type = _modplug.ModPlug_GetModuleType(modplug_file)
        self._info_dict['type'] = mod_type

        message = _modplug.ModPlug_GetMessage(modplug_file)
        if message:
            message = message.decode('cp437', 'replace').replace('\r', '\n')
            self._info_dict['message'] = message

    def _update_settings(self):
        """Reload and apply the settings."""
        _modplug.ModPlug_SetSettings(_modplug.byref(self._modplug_settings))

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it."""
        str_buffer = _modplug.create_string_buffer(size)
        data = b''

        # Don't loop past .01% of length.
        if self.position > (self.length + (.001 * self.length)):
            self._loop_count = self.position / self.length
            if self._loops != -1 and self._loop_count > self._loops:
                return b''

        if _modplug.ModPlug_Read(self._modplug_file, str_buffer, size) != 0:
            samples_read = len(str_buffer.raw) / (self._channels * self._depth >> 3)
            # Calculate the position in milliseconds.
            self._pos += int(samples_read // (self._rate / 1000))
            data = self._proc_func(str_buffer.raw)
        else:
            # If no data was read then we have reached the end of the
            # file so restart or exit.
            if self._loops == -1 or self._loop_count < self._loops:
                # Fill the buffer so we return the requested size.
                data += b'\x00' * (size - len(data))

                # Update the loop count and seek to the start.
                self._loop_count += 1
                self.seek(0)

        # Return the data if data = b'' then the player will exit.
        return data

    def close(self):
        """Close and clean up."""
        if not self.closed:
            _modplug.ModPlug_Unload(self._modplug_file)
            self._modplug_file = None
            self._closed = True

    def _wrap_settings(func: Callable) -> Callable:
        """Update the settings."""
        def wrap_func(self, *args):
            try:
                retval = func(self, *args)
                self._update_settings()
                return retval
            except Exception as err:
                print("Error %s" % err)
                return None

        return wrap_func

    @property
    def loops(self) -> int:
        """How many times the module should play."""
        return self._modplug_settings.mLoopCount

    @loops.setter
    @_wrap_settings
    def loops(self, value: int):
        """Set how many times the module should play.

        To play forever use a value of -1.
        """
        self._loops = value
        self._modplug_settings.mLoopCount = int(value)

    @property
    def oversampling(self) -> bool:
        """Whether oversampling is enabled."""
        return (self.flags & _modplug.MODPLUG_ENABLE_OVERSAMPLING) == 1

    @oversampling.setter
    @_wrap_settings
    def oversampling(self, value: bool):
        """Enable/Disable oversampling."""
        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
            return
        if value:
            self.flags |= _modplug.MODPLUG_ENABLE_OVERSAMPLING
        else:
            self.flags &= ~_modplug.MODPLUG_ENABLE_OVERSAMPLING

    @property
    def noise_reduction(self) -> bool:
        """Whether noise reduction is enabled."""
        return (self.flags & _modplug.MODPLUG_ENABLE_NOISE_REDUCTION) != 0

    @noise_reduction.setter
    @_wrap_settings
    def noise_reduction(self, value: bool):
        """Enable/Disable noise reduction."""
        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
            return
        if value:
            self.flags |= _modplug.MODPLUG_ENABLE_NOISE_REDUCTION
        else:
            self.flags &= ~_modplug.MODPLUG_ENABLE_NOISE_REDUCTION

    @property
    def resampling(self) -> int:
        """Return the current resample mode."""
        return self._modplug_settings.mResamplingMode

    @resampling.setter
    @_wrap_settings
    def resampling(self, value: int):
        """Set the resampling mode."""
        if value not in range(3):
            raise Exception('Invalid value')
        else:
            self._modplug_settings.mResamplingMode = value

    @property
    def flags(self) -> int:
        """Return the current modplug flags."""
        return self._modplug_settings.mFlags

    @flags.setter
    @_wrap_settings
    def flags(self, flags: int):
        """Set the modplug flags."""
        self._modplug_settings.mFlags = flags

    @property
    def volume(self) -> int:
        """Get the current volume."""
        return _modplug.ModPlug_GetMasterVolume(self._modplug_file)

    @volume.setter
    def volume(self, value: int):
        """Set the volume."""
        _modplug.ModPlug_SetMasterVolume(self._modplug_file, int(value))

    @property
    def reverb_depth(self) -> int:
        """Get the current reverb delay."""
        return self._modplug_settings.mReverbDepth

    @reverb_depth.setter
    @_wrap_settings
    def reverb_depth(self, value: int):
        """Set the reverb depth."""
        self._modplug_settings.mReverbDepth = int(value)

    @property
    def reverb_delay(self) -> int:
        """Get the current reverb delay."""
        return self._modplug_settings.mReverbDelay

    @reverb_delay.setter
    @_wrap_settings
    def reverb_delay(self, value: int):
        """Set the reverb delay."""
        if value == 0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_REVERB
        else:
            self.flags |= _modplug.MODPLUG_ENABLE_REVERB
        self._modplug_settings.mReverbDelay = int(value)

    @property
    def surround_depth(self) -> int:
        """Get the current surround delay."""
        return self._modplug_settings.mSurroundDepth

    @surround_depth.setter
    @_wrap_settings
    def surround_depth(self, value: int):
        """Set the surround depth."""
        if value == 0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_SURROUND
        else:
            self.flags |= _modplug.MODPLUG_ENABLE_SURROUND
        self._modplug_settings.mSurroundDepth = int(value)

    @property
    def surround_delay(self) -> int:
        """Get the current surround delay."""
        return self._modplug_settings.mSurroundDelay

    @surround_delay.setter
    @_wrap_settings
    def surround_delay(self, value: int):
        """Set the surround delay."""
        self._modplug_settings.mSurroundDelay = int(value)

    @property
    def bass_amount(self) -> int:
        """Get the current bass amount."""
        return self._modplug_settings.mBassAmount

    @bass_amount.setter
    @_wrap_settings
    def bass_amount(self, value: int):
        """Set the bass amount."""
        if value == 0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_MEGABASS
        else:
            self.flags |= _modplug.MODPLUG_ENABLE_MEGABASS
        self._modplug_settings.mBassAmount = int(value)

    @property
    def bass_range(self) -> int:
        """Get the current bass range."""
        return self._modplug_settings.mBassRange

    @bass_range.setter
    @_wrap_settings
    def bass_range(self, value: int):
        """Set the bass range."""
        self._modplug_settings.mBassRange = int(value)

    @property
    def stereo_separation(self) -> int:
        """Get the current stereo separation."""
        return self._modplug_settings.mStereoSeparation

    @stereo_separation.setter
    @_wrap_settings
    def stereo_separation(self, value: int):
        """Set the stereo separation 1-256."""
        if value in range(1, 257):
            self._modplug_settings.mStereoSeparation = int(value)
        else:
            print("Value out of range should be 1-256.")

    @property
    def maxmix_channels(self) -> int:
        """Get the number of mixing channels."""
        return self._modplug_settings.mMaxMixChannels

    @maxmix_channels.setter
    @_wrap_settings
    def maxmix_channels(self, value: int):
        """Get the number of mixing channels (32-256)."""
        if value in range(32, 257):
            self._modplug_settings.mMaxMixChannels = int(value)
        else:
            print("Value out of range should be 32-256.")
