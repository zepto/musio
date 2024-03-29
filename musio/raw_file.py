#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of raw files.
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


"""A module for reading raws."""

from os.path import getsize as os_getsize
from typing import IO, Any

from .io_base import AudioIO, io_wrapper

__supported_dict = {
    'ext': ['.raw'],
    'handler': 'RawFile'
}


class RawFile(AudioIO):
    """A file like object for reading raws."""

    # Both reading and writing are supported
    _supported_modes = 'rw'

    def __init__(self, filename: str, mode: str = 'r', depth: int = 16,
                 rate: int = 44100, channels: int = 2, **_):
        """Initialize the playback settings of the player."""
        super(RawFile, self).__init__(filename, mode, depth, rate, channels)

        if 'r' in mode:
            self._length = os_getsize(filename)

        self._file = self._open(filename)

        self.seek = self._file.seek
        self.tell = self._file.tell

    def _set_position(self, position: int):
        """Change the position of playback."""
        self._file.seek(position)

    def _get_position(self) -> int:
        """Get position."""
        return self._file.tell()

    def _open(self, filename: str) -> IO[Any]:
        """Load the specified file."""
        self._closed = False

        return open(filename, '%sb' % self._mode, buffering=0)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write data to raw audio file."""
        return self._file.write(data)

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it.

        If size is None then read a buffer size.
        """
        if self.position >= self._length:
            if self._loops == -1 or self._loop_count < self._loops:
                self._loop_count += 1
                self.seek(0)

        return self._file.read(size)

    def close(self):
        """Close and clean up."""
        if not self.closed:
            self._file.close()
            self._closed = True
