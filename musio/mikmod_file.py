#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of module music using mikmod.
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


"""Mikmod is a class to handle module music using libmikmod."""

from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper

_mikmod = LazyImport('mikmod._mikmod', globals(), locals(), ['_mikmod'], 1)
_mikmod_drv = LazyImport('mikmod.driver', globals(), locals(), ['driver'], 1)

__supported_dict = {
    'ext': ['.669', '.amf', '.dsm', '.far', '.gdm', '.imf', '.it', '.med',
            '.mod', '.mtm', '.s3m', '.stm', '.stx', '.ult', '.uni',
            '.apun', '.xm'],
    'handler': 'MikModFile',
    'dependencies': {
        'ctypes': ['mikmod'],
        'python': []
    }
}


class MikModFile(AudioIO):
    """A class to use mikmod to play modules.

    After loading a file start needs to be called to start the module.  Then
    update needs to be called until the module is done.
    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, **_):
        """Initialize the playback settings of the player."""
        super(MikModFile, self).__init__(filename, 'r', depth, rate, channels)

        if depth == 8:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_16BITS
            self._unsigned = True
        else:
            _mikmod.md_mode.value |= _mikmod.DMODE_16BITS

        if channels == 1:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_STEREO
        else:
            _mikmod.md_mode.value |= _mikmod.DMODE_STEREO \
                | _mikmod.DMODE_HQMIXER

        _mikmod.md_mixfreq.value = rate

        # Use custom driver.
        _mikmod.md_device.value = 0

        self._module = self._open(filename)
        self._length = self._module.contents.numpos
        self._volume = self._module.contents.volume
        self._speed = self._module.contents.bpm

        self._module.contents.loop = True
        self._module.contents.wrap = True

        self._near_end = 0
        self._data_buffer = b''

        _mikmod.Player_Start(self._module)

    def _set_position(self, position: int):
        """Change the position of playback."""
        position += -1 if position < self.position else 1
        if position < self.length and position >= 0:
            _mikmod.Player_SetPosition(position)

    def _get_position(self) -> int:
        """Update the position variable."""
        return self._module.contents.sngpos

    @property
    def surround(self) -> bool:
        """Whether surround is enabled."""
        return (_mikmod.md_mode.value & _mikmod.DMODE_SURROUND) != 0

    @surround.setter
    def surround(self, value: bool):
        """Enable/Disable surround.  bool."""
        if value:
            _mikmod.md_mode.value |= _mikmod.DMODE_SURROUND
        else:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_SURROUND

    @property
    def interp(self) -> bool:
        """Whether interpolation is enabled."""
        return (_mikmod.md_mode.value & _mikmod.DMODE_INTERP) != 0

    @interp.setter
    def interp(self, value: bool):
        """Enable/Disable interpolation."""
        if value:
            _mikmod.md_mode.value |= _mikmod.DMODE_INTERP
        else:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_INTERP

    @property
    def speed(self) -> int:
        """Get the current speed."""
        return self._speed

    @speed.setter
    def speed(self, value: int):
        """Set the speed."""
        try:
            self._speed = int(value)
            _mikmod.Player_SetTempo(self._speed)
        except ValueError:
            print(f"Invalid value for speed {value} should be an number.")

    @property
    def volume(self) -> int:
        """Get the current volume."""
        return self._volume

    @volume.setter
    def volume(self, value: int):
        """Set the volume."""
        try:
            self._volume = int(value)
            _mikmod.Player_SetVolume(self._volume)
        except ValueError:
            print(f"Invalid value for volume {value} should be an number.")

    @property
    def reverb(self) -> int:
        """Return the amount of reverb 0 = none;  15 = chaos."""
        return _mikmod.md_reverb.value

    @reverb.setter
    def reverb(self, value: int):
        """Set the volume.  0 = none;  15 = chaos."""
        try:
            _mikmod.md_reverb.value = int(value)
        except ValueError:
            print(f"Invalid value for reverb {value} should be a number.")

    def _open(self, filename: str) -> Any:
        """Load the specified file."""
        try:
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename

        # _mikmod.MikMod_RegisterAllDrivers()
        _mikmod.MikMod_RegisterDriver(
            _mikmod.ctypes.byref(_mikmod_drv.drv_musio))
        _mikmod.MikMod_RegisterAllLoaders()
        # print(_mikmod.MikMod_InfoDriver().decode())

        err_int = _mikmod.MikMod_Init(b"")
        if err_int:
            raise Exception(_mikmod.MikMod_strerror(err_int).decode())

        if _mikmod.MikMod_InitThreads() == 0:
            print("Not thread safe")

        module = _mikmod.Player_Load(filename_b, 64, 1)

        try:
            self._load_info(module)
        except ValueError:
            self.close()
            raise IOError(
                f"Can't load module: {filename}"
            )

        self._closed = False

        return module

    def close(self):
        """Stop playback and unloads the module."""
        if not self.closed:
            _mikmod.Player_Stop()
            _mikmod.Player_Free(self._module)
            _mikmod.MikMod_Exit()
            self._closed = True

    @io_wrapper
    def read(self, size: int) -> bytes:
        """Continue playing the module."""
        # If there was extra data from the last read put it in data before
        # reading again.
        data = self._data_buffer

        # When the position equals the length then the playback has reached the
        # end and is not going to loop.
        if self.position == self.length:
            if len(data) > 0:
                data += b'\x00' * (size - len(data))
            return data

        # When nearing the end keep track so we can tell when the song has
        # looped.
        if self.position == (self.length - 1):
            self._near_end = self.position

        # Position has gone back down so increase loop_count, and reset
        # near_end to 0.
        if self.position < self._near_end:
            self._loop_count += 1
            self._near_end = 0

        # Disable wrapping and looping, so the position can reach the length,
        # and the song can end properly.
        if self._loops != -1 and self._loop_count >= self._loops:
            self._module.contents.loop = False
            self._module.contents.wrap = False

        # We need a ctypes.c_byte data buffer to hold the data from mikmod
        # VC_WriteBytes.
        byte_buffer = (_mikmod.ctypes.c_byte * size)()

        while len(data) < size:
            try:
                read_size = _mikmod.VC_WriteBytes(byte_buffer, size)
                data += _mikmod.ctypes.string_at(byte_buffer, read_size)
            except Exception as err:
                print(f"Error reading: ({err})", flush=True)
        # Put any data greater than size in data_buffer to be used next read.
        self._data_buffer = data[size:]
        # Only return the data upto the requested size.
        return data[:size]

    def _load_info(self, module: Any):
        """Load module info into info_dict.

        Load the information such as the module name and message and the sample
        and instrument names.
        """
        num_smp = module.contents.numsmp
        if num_smp > 0:
            tmp_list = []
            for i in range(num_smp):
                try:
                    name = module.contents.samples[i].samplename
                    name = name.decode('cp437', 'replace')
                except Exception:
                    continue
                if name:
                    key_str = f'{"Sample":8} {i:3}'
                    value_str = f'{name} {""}'
                    tmp_list.append(f"{key_str} {value_str}")
            if any(tmp_list):
                self._info_dict['samples'] = tmp_list

        num_ins = module.contents.numins
        if num_ins > 0:
            tmp_list = []
            for i in range(num_ins):
                try:
                    name = module.contents.instruments[i].insname
                    name = name.decode('cp437', 'replace')
                except Exception:
                    continue
                if name:
                    key_str = f'{"Instrument":8} {i:3}'
                    value_str = f'{name} {""}'
                    tmp_list.append(f"{key_str} {value_str}")
            if any(tmp_list):
                self._info_dict['instruments'] = tmp_list

        mod_type = module.contents.modtype.decode('cp437', 'replace')
        self._info_dict['type'] = mod_type

        name = module.contents.songname
        self._info_dict['name'] = name.decode('cp437', 'replace')

        comment = module.contents.comment
        if comment:
            message = comment.decode('cp437', 'replace')
            self._info_dict['message'] = message.replace('\n', '\n')
