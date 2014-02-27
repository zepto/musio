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


""" Mikmod is a class to handle module music using libmikmod.

"""

from os import remove as os_remove
from time import sleep as time_sleep
from threading import Thread

from .io_base import AudioIO, io_wrapper

# from .mikmod import _mikmod

from .import_util import LazyImport

_mikmod = LazyImport('mikmod._mikmod', globals(), locals(),
                     ['_mikmod'], 1)
_mikmod_drv = LazyImport('mikmod.driver', globals(), locals(),
                     ['driver'], 1)

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
    """ A class to use mikmod to play modules.
    After loading a file start needs to be called to start the module.  Then
    update needs to be called until the module is done.

    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, **kwargs):
        """ MikModFile(filename, depth=16, rate=44100, channels=2) ->
        Initialize the playback settings of the player.

        """

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

        # Set the device to a raw file.
        # _mikmod.md_device.value = 6
        # Use custom driver.
        _mikmod.md_device.value = 0

        self._out_filename = 'music.raw'

        self._module = self._open(filename)
        self._length = self._module.contents.numpos
        self._volume = self._module.contents.volume
        self._speed = self._module.contents.bpm

        self._module.contents.loop = True
        self._module.contents.wrap = True

        self._near_end = 0

        _mikmod.Player_Start(self._module)

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _mikmod.Player_SetPosition(position + 1)

    def _get_position(self):
        """ Updates the position variable.

        """

        # print(self._module.contents.sngpos, self._module.contents.numpos)
        return self._module.contents.sngpos

    @property
    def surround(self):
        """ Whether surround is enabled.

        """

        return (_mikmod.md_mode.value & _mikmod.DMODE_SURROUND) != 0

    @surround.setter
    def surround(self, value):
        """ Enable/Disable surround.  bool

        """

        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
        elif value:
            _mikmod.md_mode.value |= _mikmod.DMODE_SURROUND
        else:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_SURROUND

    @property
    def interp(self):
        """ Whether interpolation is enabled.

        """

        return (_mikmod.md_mode.value & _mikmod.DMODE_INTERP) != 0

    @interp.setter
    def interp(self, value):
        """ Enable/Disable interpolation.  bool

        """

        if type(value) is not bool:
            print("Invalid value.  Should be True or False.")
        elif value:
            _mikmod.md_mode.value |= _mikmod.DMODE_INTERP
        else:
            _mikmod.md_mode.value &= ~_mikmod.DMODE_INTERP

    @property
    def speed(self):
        """ Get the current speed.

        """

        return self._speed

    @speed.setter
    def speed(self, value):
        """ Set the speed.

        """

        self._speed = int(value)
        _mikmod.Player_SetTempo(self._speed)

    @property
    def volume(self):
        """ Get the current volume.

        """

        return self._volume

    @volume.setter
    def volume(self, value):
        """ Set the volume.

        """

        self._volume = int(value)
        _mikmod.Player_SetVolume(self._volume)

    @property
    def reverb(self):
        """ The amount of reverb
        0 = none;  15 = chaos

        """

        return _mikmod.md_reverb.value

    @reverb.setter
    def reverb(self, value):
        """ Set the volume.
        0 = none;  15 = chaos

        """

        _mikmod.md_reverb.value = int(value)

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        filename = filename.encode('utf8', 'replace')

        # _mikmod.MikMod_RegisterAllDrivers()
        _mikmod.MikMod_RegisterDriver(_mikmod.byref(_mikmod_drv.drv_musio))
        _mikmod.MikMod_RegisterAllLoaders()
        # print(_mikmod.MikMod_InfoDriver().decode())

        err_int = _mikmod.MikMod_Init(b"")
        if err_int:
            raise Exception(_mikmod.MikMod_strerror(err_int).decode())

        if _mikmod.MikMod_InitThreads() == 0:
            print("Not thread safe")

        module = _mikmod.Player_Load(filename, 64, 1)

        self._load_info(module)

        self._closed = False

        return module

    def close(self):
        """ Stops playback and unloads the module.

        """

        if not self.closed:
            _mikmod.Player_Stop()
            _mikmod.Player_Free(self._module)
            _mikmod.MikMod_Exit()
            self._closed = True

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ Continue playing the module.

        """

        try:
            if self.position >= self.length - 1:
                self._near_end = self.position

            if self.position < self._near_end:
                if self._loops != -1 and self._loop_count >= self._loops:
                    return b''
                self._loop_count += 1
                self._near_end = 0

            byte_buffer = (_mikmod.c_byte * size)()

            data = b''
            while len(data) < size:
                read_size = _mikmod.VC_WriteBytes(byte_buffer, size)
                data += byte_buffer

            return data
        except Exception as err:
            print("Error reading: (%s)" % err, flush=True)
            return b''

    def _load_info(self, module):
        """ _load_info(module) -> Load the information such as the module name
        and message and the sample and instrument names.

        """

        num_smp = module.contents.numsmp
        if num_smp > 0:
            tmp_list = []
            for i in range(num_smp):
                name = module.contents.samples[i].samplename
                name = name.decode('cp437', 'replace')
                if name:
                    key_str = '%-8s %3d:' % ('Sample', i)
                    value_str = '%s %s' % (name, '')
                    tmp_list.append("%s %s" % (key_str, value_str))
            if any(tmp_list):
                self._info_dict['samples'] = tmp_list

        num_ins = module.contents.numins
        if num_ins > 0:
            tmp_list = []
            for i in range(num_ins):
                try:
                    name = module.contents.instruments[i].insname
                except:
                    pass
                if name:
                    name = name.decode('cp437', 'replace')
                    key_str = '%-8s %3d:' % ('Instrument', i)
                    value_str = '%s %s' % (name, '')
                    tmp_list.append("%s %s" % (key_str, value_str))
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
