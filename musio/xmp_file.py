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


"""A module for reading media files using xmp."""

from typing import Any

from musio.io_base import AudioIO, io_wrapper

from .import_util import LazyImport
from .io_util import bytes_to_str

_xmp = LazyImport('xmp._xmp', globals(), locals(), ['_xmp'], 1)

__supported_dict = {
    'ext': ['.669', '.alm', '.amd', '.amf', '.arch', '.asylum', '.coco',
            '.dbm', '.digi', '.dmf', '.dt', '.dtt', '.emod', '.far',
            '.flt', '.fnk', '.ftm', '.gal4', '.gal5', '.gdm', '.gtk',
            '.hsc', '.ice', '.imf', '.ims', '.it', '.itz', '.liq', '.masi',
            '.mdl', '.med2', '.med3', '.med4', '.mfp', '.mgt', '.mmd1',
            '.mmd3', '.mod', '.mtm', '.no', '.okt', '.polly', '.psm', '.pt3',
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
    """A file like object for reading media files with ffmpeg."""

    # Valid bit depths
    _valid_depth = (16, 8)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, unsigned: bool = False, **kwargs):
        """Initialize the playback settings of the player."""
        super(XMPFile, self).__init__(filename, 'r', depth, rate, channels)

        self._flags = 0
        self._seek_pos = -1

        if depth == 8:
            self._flags = _xmp.XMP_FORMAT_8BIT

        if channels == 1:
            self._flags |= _xmp.XMP_FORMAT_MONO

        if unsigned:
            self._flags |= _xmp.XMP_FORMAT_UNSIGNED

        self.__module_info, self.__frame_info, self.__xmp_context = \
            self._open(filename)

        self._length = self.__frame_info.total_time

        self._data = b''

        self._load_info()

    def to_seconds(self, position: int) -> float:
        """Convert the provided position/length to seconds."""
        return position / 1000

    def _set_position(self, position: int):
        """Change the position of playback."""
        if position > self.position:
            position += self._length // self.__module_info.mod.contents.len
        else:
            position -= self._length // self.__module_info.mod.contents.len

        _xmp.xmp_seek_time(self.__xmp_context, position)

    def _get_position(self) -> int:
        """Update the position variable."""
        return self.__frame_info.time

    def _open(self, filename: str) -> tuple[Any, Any, Any]:
        """Load the specified file."""
        filename_b = filename.encode('utf-8', 'surrogateescape')

        xmp_context = _xmp.xmp_create_context()  # (_xmp.c_char * 4096)()

        ret = _xmp.xmp_load_module(xmp_context, filename_b)
        if ret != 0:
            raise IOError(
                f"Can't load module: {filename} error number {ret}"
            )

        module_info = _xmp.xmp_module_info()
        _xmp.xmp_get_module_info(xmp_context, _xmp.byref(module_info))

        frame_info = _xmp.xmp_frame_info()
        _xmp.xmp_get_frame_info(xmp_context, _xmp.byref(frame_info))

        _xmp.xmp_set_player(xmp_context, _xmp.XMP_PLAYER_INTERP,
                            _xmp.XMP_INTERP_SPLINE)
        _xmp.xmp_set_player(xmp_context, _xmp.XMP_PLAYER_DSP, _xmp.XMP_DSP_ALL)
        _xmp.xmp_set_player(xmp_context, _xmp.XMP_PLAYER_MIX, 1000)

        # The file is now open.
        self._closed = False

        _xmp.xmp_start_player(xmp_context, self._rate, self._flags)

        return module_info, frame_info, xmp_context

    def _load_info(self):
        """Load the module music info."""
        def load_list(key: str, index: str, count: int) -> list[str]:
            """Load a list of names and filenames into a list."""
            fill_list = []

            for i in range(count):
                tmp = getattr(self.__module_info.mod.contents, index)[i]
                name = bytes_to_str(tmp.name)
                if name:
                    fill_list.append(f"{key.capitalize():8} {i:02} {name}")

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
        name = bytes_to_str(self.__module_info.mod.contents.name)
        self._info_dict['name'] = name

        # Get the mod type.
        mod_type = self.__module_info.mod.contents.type
        self._info_dict['type'] = bytes_to_str(mod_type)

        # Get any comment.
        comment = self.__module_info.comment
        if comment:
            self._info_dict['comment'] = bytes_to_str(comment)

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None read buffer_size of data.
        """
        # Only update the global data buffer.
        data = self._data
        old_count = 0

        while not data or len(data) < size:
            # Get the next data block.
            _xmp.xmp_get_frame_info(self.__xmp_context,
                                    _xmp.byref(self.__frame_info))

            if self.__frame_info.loop_count > old_count or \
                    _xmp.xmp_play_frame(self.__xmp_context) != 0:
                old_count = self.__frame_info.loop_count
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                else:
                    # self.seek(0)
                    _xmp.xmp_end_player(self.__xmp_context)
                    _xmp.xmp_start_player(self.__xmp_context, self._rate, 0)

                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1

                break

            # Append the decoded data to the buffer.
            data += _xmp.string_at(self.__frame_info.buffer,
                                   self.__frame_info.buffer_size)

        # Store extra data for next time.
        self._data = data[size:]

        # Make sure we return only the number of bytes requested.
        return data[:size]

    def close(self):
        """Close and cleans up."""
        if not self.closed:
            _xmp.xmp_end_player(self.__xmp_context)
            _xmp.xmp_release_module(self.__xmp_context)
            _xmp.xmp_free_context(self.__xmp_context)

            # This file is closed.
            self._closed = True
