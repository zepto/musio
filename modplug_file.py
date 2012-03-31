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


""" ModPlug is a class to handle module music using the modplug library.

"""

from array import array

from io_base import AudioIO, OnDemand, io_wrapper
from au_resample import to_bigendian

_modplug = OnDemand('modplug._modplug', globals(), locals(),
                    ['_modplug'], 0)

__supported_dict = {
        'ext': ['.mod', '.xm', '.s3m', '.it'],
        'handler': 'ModPlugFile',
        'default': True
        }

modplug_flags = [
        _modplug.MODPLUG_ENABLE_OVERSAMPLING,
        _modplug.MODPLUG_ENABLE_NOISE_REDUCTION,
        _modplug.MODPLUG_ENABLE_REVERB,
        _modplug.MODPLUG_ENABLE_MEGABASS,
        _modplug.MODPLUG_ENABLE_SURROUND
        ]


class ModPlugFile(AudioIO):
    """ A file like interface to module music files (it, xm, s3m, mod) using 
    the modplug library.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False):
        """ ModPlugFile(filename, depth=16, rate=44100, channels=2) ->
        Initialize the playback settings of the player.

        """

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

        # Loop forever.
        self._modplug_settings.mLoopCount = -1
        self._modplug_settings.mStereoSeparation = 256
        self._modplug_settings.mMaxMixChannels = 256
        self._modplug_settings.mResamplingMode = _modplug.MODPLUG_RESAMPLE_FIR

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
            self._proc_func = to_bigendian
        else:
            self._proc_func = lambda data_list: data_list

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _modplug.ModPlug_Seek(self._modplug_file, position)

    def _open(self, filename):
        """ _load_file(filename) -> Load the specified file.

        """

        with open(filename, 'rb') as mod_file:
            mod_data = mod_file.read()

        modplug_file = _modplug.ModPlug_Load(mod_data, len(mod_data))
        if not modplug_file:
            raise OSError("Error loading file: %s" % filename)

        self._closed = False

        return modplug_file

    def _load_info(self, modplug_file):
        """ _load_info(duh) -> Load the information such as the module name 
        and message and the sample and instrument names.

        """

        def load_list(key, name_func, modplug_file, count):
            """ _load_list(fill_list, name_func, modplug_file, count) -> 
            Load a list of names and filenames from sig_data into fill_list.

            """

            fill_list = []

            name_buffer = _modplug.create_string_buffer(256)
            for i in range(count):
                name_func(modplug_file, i, name_buffer)
                if name_buffer:
                    name = name_buffer.value.decode('cp437', 'replace')
                    key_str = '%-8s %3d:' % (key.capitalize(), i)
                    value_str = '%s %s' % (name, '')
                    fill_list.append("%s %s" % (key_str, value_str))

            return fill_list

        num_smp = _modplug.ModPlug_NumSamples(modplug_file)
        if num_smp > 0:
            tmp_list = load_list('sample', _modplug.ModPlug_SampleName,
                                 modplug_file, num_smp)
            if tmp_list:
                self._info_dict['samples'] = tmp_list

        num_ins = _modplug.ModPlug_NumInstruments(modplug_file)
        if num_ins > 0:
            tmp_list = load_list('instrument',
                                 _modplug.ModPlug_InstrumentName, modplug_file,
                                 num_ins)
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
        """ _update_settings -> Reload and apply the settings.

        """

        _modplug.ModPlug_SetSettings(_modplug.byref(self._modplug_settings))

    @io_wrapper
    def read(self, size=None):
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        str_buffer = _modplug.create_string_buffer(size)

        if _modplug.ModPlug_Read(self._modplug_file, str_buffer, size) != 0:
            return self._proc_func(str_buffer.raw)
        else:
            return ''

    def close(self):
        """ close -> Closes and cleans up.

        """

        try:
            _modplug.ModPlug_Unload(self._modplug_file)
            self._modplug_file = None
            self._closed = True
            return True
        except:
            return False

    def _wrap_settings(func):
        """ A wrapper function to update the settings.

        """

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
    def loops(self):
        """ How many times the module should play.

        """

        return self._modplug_settings.mLoopCount

    @loops.setter
    @_wrap_settings
    def loops(self, value):
        """ Set how many times the module should play.

        To play forever use a value of -1.

        """

        self._modplug_settings.mLoopCount = int(value)

    @property
    def oversampling(self):
        """ Whether oversampling is enabled.

        """

        return (self.flags & _modplug.MODPLUG_ENABLE_OVERSAMPLING) == 1

    @oversampling.setter
    @_wrap_settings
    def oversampling(self, value):
        """ Enable/Disable oversampling.  bool

        """

        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
            return
        if value:
            self.flags |= _modplug.MODPLUG_ENABLE_OVERSAMPLING
        else:
            self.flags &= ~_modplug.MODPLUG_ENABLE_OVERSAMPLING

    @property
    def noise_reduction(self):
        """ Whether noise reduction is enabled.

        """

        return (self.flags & _modplug.MODPLUG_ENABLE_NOISE_REDUCTION) != 0

    @noise_reduction.setter
    @_wrap_settings
    def noise_reduction(self, value):
        """ Enable/Disable noise reduction.  bool

        """

        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
            return
        if value:
            self.flags |= _modplug.MODPLUG_ENABLE_NOISE_REDUCTION
        else:
            self.flags &= ~_modplug.MODPLUG_ENABLE_NOISE_REDUCTION

    @property
    def resampling(self):
        """ The current resample mode.

        """

        return self._modplug_settings.mResamplingMode

    @resampling.setter
    @_wrap_settings
    def resampling(self, value):
        """ resampling(mode) -> Set the resampling mode.

        """

        if value not in range(3):
            raise Exception('Invalid value')
        else:
            self._modplug_settings.mResamplingMode = value

    @property
    def flags(self):
        """ The current modplug flags.

        """

        return self._modplug_settings.mFlags

    @flags.setter
    @_wrap_settings
    def flags(self, flags):
        """ Set the modplug flags.

        """

        self._modplug_settings.mFlags = flags

    @property
    def volume(self):
        """ Get the current volume.

        """

        return _modplug.ModPlug_GetMasterVolume(self._modplug_file)

    @volume.setter
    def volume(self, value):
        """ Set the volume.

        """

        _modplug.ModPlug_SetMasterVolume(self._modplug_file, int(value))

    @property
    def reverb_depth(self):
        """ Get the current reverb delay.

        """

        return self._modplug_settings.mReverbDepth

    @reverb_depth.setter
    @_wrap_settings
    def reverb_depth(self, value):
        """ Set the reverb depth.

        """

        self._modplug_settings.mReverbDepth = int(value)

    @property
    def reverb_delay(self):
        """ Get the current reverb delay.

        """

        return self._modplug_settings.mReverbDelay

    @reverb_delay.setter
    @_wrap_settings
    def reverb_delay(self, value):
        """ Set the reverb delay.

        """

        if value ==  0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_REVERB
        else:
            self.flags |=  _modplug.MODPLUG_ENABLE_REVERB
        self._modplug_settings.mReverbDelay = int(value)

    @property
    def surround_depth(self):
        """ Get the current surround delay.

        """

        return self._modplug_settings.mSurroundDepth

    @surround_depth.setter
    @_wrap_settings
    def surround_depth(self, value):
        """ Set the surround depth.

        """

        if value ==  0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_SURROUND
        else:
            self.flags |=  _modplug.MODPLUG_ENABLE_SURROUND
        self._modplug_settings.mSurroundDepth = int(value)

    @property
    def surround_delay(self):
        """ Get the current surround delay.

        """

        return self._modplug_settings.mSurroundDelay

    @surround_delay.setter
    @_wrap_settings
    def surround_delay(self, value):
        """ Set the surround delay.

        """

        self._modplug_settings.mSurroundDelay = int(value)

    @property
    def bass_amount(self):
        """ Get the current bass amount.

        """

        return self._modplug_settings.mBassAmount

    @bass_amount.setter
    @_wrap_settings
    def bass_amount(self, value):
        """ Set the bass amount.

        """

        if value ==  0:
            self.flags &= ~ _modplug.MODPLUG_ENABLE_MEGABASS
        else:
            self.flags |=  _modplug.MODPLUG_ENABLE_MEGABASS
        self._modplug_settings.mBassAmount = int(value)

    @property
    def bass_range(self):
        """ Get the current bass range.

        """

        return self._modplug_settings.mBassRange

    @bass_range.setter
    @_wrap_settings
    def bass_range(self, value):
        """ Set the bass range.

        """

        self._modplug_settings.mBassRange = int(value)

    @property
    def stereo_separation(self):
        """ Get the current stereo separation.

        """

        return self._modplug_settings.mStereoSeparation

    @stereo_separation.setter
    @_wrap_settings
    def stereo_separation(self, value):
        """ Set the stereo separation 1-256.

        """

        if value in range(1, 257):
            self._modplug_settings.mStereoSeparation = int(value)
        else:
            print("Value out of range should be 1-256.")

    @property
    def maxmix_channels(self):
        """ Get the number of mixing channels.

        """

        return self._modplug_settings.mMaxMixChannels

    @maxmix_channels.setter
    @_wrap_settings
    def maxmix_channels(self, value):
        """ Get the number of mixing channels. (32-256)

        """

        if value in range(32, 257):
            self._modplug_settings.mMaxMixChannels = int(value)
        else:
            print("Value out of range should be 32-256.")
