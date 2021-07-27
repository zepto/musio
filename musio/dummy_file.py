#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A Dummy file.
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


"""A Dummy file."""

from .io_base import AudioIO, io_wrapper

__supported_dict = {
    'ext': ['.*'],
    'handler': 'DummyFile',
}


class DummyFile(AudioIO):
    """Handles all files with read and write."""

    # Valid bit depths.
    _valid_depth = (32, 16, 8)

    # Only reading is supported
    _supported_modes = 'rw'

    def __init__(self, filename: str, mode: str = 'r', depth: int = 16,
                 rate: int = 44100, channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, **_):
        """Fake file."""
        super(DummyFile, self).__init__(filename, mode, depth, rate, channels)

        self._bigendian = bigendian
        self._unsigned = unsigned

        self.write = lambda data: len(data)
        self.write.__doc__ = """ write(data) -> Write data to dummy file. """
        self.write.__annotations__ = {'data': bytes, 'return': int}

        self ._closed = False

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'mode="{self._mode}", depth={self._depth}, '
                f'rate={self._rate}, channels={self._channels}, '
                f'bigendian={self._bigendian}, unsigned={self._unsigned})')

    def close(self):
        """Close."""
        if not self.closed:
            self._closed = True

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Return audio data with its format converted if necessary."""
        return b'\x00' * size
