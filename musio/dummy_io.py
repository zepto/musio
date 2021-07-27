#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A Dummy io device.
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


"""A Dummy io device."""

from .io_base import DevIO, io_wrapper

__supported_dict = {
    'output': [bytes, str],
    'input': [bytes, str],
    'handler': 'Dummy',
    # 'default': True
}


class Dummy(DevIO):
    """A class that provides a file like object to write to a dummy pcm."""

    # Valid bit depths.
    _valid_depth = (32, 24, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode: str = 'w', depth: int = 16, rate: int = 44100,
                 channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, buffer_size: int = 0,
                 latency: float = 500000, **kwargs):
        """Initialize the dummy pcm device."""
        super(Dummy, self).__init__(
            mode,
            depth,
            rate,
            channels,
            bigendian,
            unsigned,
            buffer_size
        )

        self._dummy = self._open()

    def __repr__(self):
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(mode="{self._mode}", '
                f'depth={self._depth}, rate={self._rate}, '
                f'channels={self._channels}, bigendian={self._bigendian}, '
                f'unsigned={self._unsigned}, buffer_size={self._buffer_size})'
                f'latency={self._latency}')

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write to the pcm device."""
        return len(data)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """Read length bytes from input."""
        return b'\x00' * size

    def _open(self):
        """Open the pcm audio output."""
        self._closed = False

        return True

    def close(self):
        """Close the pcm."""
        if not self.closed:
            self._dummy = None

            self._closed = True
