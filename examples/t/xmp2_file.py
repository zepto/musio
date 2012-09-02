#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of media files using xmp.
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


""" A module for reading media files using xmp.

"""

from musio.io_base import AudioIO, io_wrapper
from .xmp import _xmp

__supported_dict = {
        'ext': ['.669', '.alm', '.amd', '.amf', '.arch', '.asylum', '.coco',
                '.dbm', '.digi', '.dmf', '.dt', '.dtt', '.emod', '.far',
                '.flt', '.fnk', '.ftm', '.gal4', '.gal5', '.gdm', '.gtk',
                '.hsc', '.ice', '.imf', '.ims', '.it', '.liq', '.masi', '.mdl',
                '.med2', '.med3', '.med4', '.mfp', '.mgt', '.mmd1', '.mmd3',
                '.mod', '.mtm', '.no', '.okt', '.polly', '.psm', '.pt3',
                '.ptm', '.pw', '.rad', '.rtm', '.s3m', '.sfx', '.ssmt', '.stc',
                '.stim', '.st', '.stm', '.stx', '.sym', '.tcb', '.ult', '.umx',
                '.xm'],
        'handler': 'XMPFile',
        'dependencies': {
            'ctypes': ['xmp'],
            'python': []
            }
        }


class XMPFile(AudioIO):
    """ A file like object for reading media files with ffmpeg.

    """

    # Valid bit depths
    _valid_depth = (16, 8)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2,
                 unsigned=False, **kwargs):
        """ XMPFile(filename, depth=16, rate=44100, channels=2, unsigned=False)
        -> Initialize the playback settings of the player.

        """

        super(XMPFile, self).__init__(filename, 'r', depth, rate, channels)

        self._flags = 0

        if depth == 8:
            print('8bit')
            self._flags = _xmp.XMP_MIX_8BIT

        if channels == 1:
            print('mono')
            self._flags |= _xmp.XMP_MIX_MONO

        if unsigned:
            self._flags |= _xmp.XMP_MIX_UNSIGNED

        self.__module_info = None

        self.__xmp_context = self._open(filename)

        self._length = self.__module_info.mod.contents.len

        self._data = b''

        self._load_info()

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _xmp.xmp_seek_time(self.__xmp_context, position)

    def _get_position(self):
        """ Updates the position variable.

        """

        return self.__module_info.order

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        filename = filename.encode()

        xmp_context = _xmp.xmp_create_context() #(_xmp.c_char * 4096)()

        if _xmp.xmp_load_module(xmp_context, filename) != 0:
            raise IOError("Can't load module: %s" % filename)

        self.__module_info = _xmp.xmp_module_info()
        _xmp.xmp_player_get_info(xmp_context, _xmp.byref(self.__module_info))

        # The file is now open.
        self._closed = False

        _xmp.xmp_player_start(xmp_context, self._rate, self._flags)

        return xmp_context

    def _load_info(self):
        """ Load the module music info.

        """

        def load_list(key: str, index: str, count: int) -> list:
            """ _load_list(key, index, count) -> Load a list of names and
            filenames into a list.

            """

            fill_list = []

            for i in range(count):
                tmp = getattr(self.__module_info.mod.contents, index)[i]
                name = tmp.name.decode('cp437', 'replace')
                if name:
                    key_str = '%-8s %02d:' % (key.capitalize(), i)
                    fill_list.append('%s %s' % (key_str, name))

            return fill_list

        # Load instrument info.
        num_inst = self.__module_info.mod.contents.ins
        if num_inst > 0:
            tmp_list = load_list('instrument', 'xxi', num_inst)
            if tmp_list:
                self._info_dict['instruments'] = tmp_list

        # Load sample info.
        num_smp = self.__module_info.mod.contents.smp
        if num_smp > 0:
            tmp_list = load_list('sample', 'xxs', num_smp)
            if tmp_list:
                self._info_dict['samples'] = tmp_list

        # Get the module name.
        name = self.__module_info.mod.contents.name.decode('cp437', 'replace')
        self._info_dict['name'] = name

        # Get the mod type.
        mod_type = self.__module_info.mod.contents.type
        self._info_dict['type'] = mod_type.decode('cp437', 'replace')

        # Get any comment.
        comment = self.__module_info.comment
        if comment:
            self._info_dict['comment'] = comment.decode('cp437', 'replace')

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None read buffer_size of data.

        """

        # Only update the global data buffer.
        data = self._data
        old_count = 0

        while not data or len(data) < size:
            # Get the next data block.
            _xmp.xmp_player_get_info(self.__xmp_context,
                                     _xmp.byref(self.__module_info))

            if self.__module_info.loop_count > old_count or \
                    _xmp.xmp_player_frame(self.__xmp_context) != 0:
                old_count = self.__module_info.loop_count
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                else:
                    # self.seek(0)
                    _xmp.xmp_player_end(self.__xmp_context)
                    _xmp.xmp_player_start(self.__xmp_context, self._rate, 0)

                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1

                break

            # Append the decoded data to the buffer.
            data += _xmp.string_at(self.__module_info.buffer,
                                   self.__module_info.buffer_size)

        # Store extra data for next time.
        self._data = data[size:]

        # Make sure we return only the number of bytes requested.
        return data[:size]

    def close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            _xmp.xmp_player_end(self.__xmp_context)
            _xmp.xmp_release_module(self.__xmp_context)
            _xmp.xmp_free_context(self.__xmp_context)

            # This file is closed.
            self._closed = True
