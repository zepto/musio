#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of wave audio.
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


"""A class to handle wave audio like python files."""

import wave
from typing import Any

from .io_base import AudioIO, io_wrapper

__supported_dict = {
    'ext': ['.wav'],
    'handler': 'WaveFile'
}


class WaveFile(AudioIO):
    """A class for wav file access."""

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Both reading and writing are supported
    _supported_modes = 'rw'

    def __init__(self, filename: str, mode: str = 'r', depth: int = 16,
                 rate: int = 44100, channels: int = 2, **_):
        """Initialize the playback settings of the player."""
        self._mode = mode

        self._wave = self._open(filename)

        if 'r' in mode:
            super(WaveFile, self).__init__(
                filename,
                mode,
                self._wave.getsampwidth() * 8,
                self._wave.getframerate(),
                self._wave.getnchannels()
            )
            self._length = self._wave.getnframes()
            self._width = self._wave.getsampwidth()
        elif 'w' in mode:
            super(WaveFile, self).__init__(
                filename,
                mode,
                depth,
                rate,
                channels
            )
            self._wave.setnchannels(channels)
            self._wave.setsampwidth(depth // 8)
            self._wave.setframerate(rate)

        self._closed = False

        if self._depth == 8:
            self._unsigned = True

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'mode={self._mode}, depth={self._depth}, rate={self._rate}, '
                f'channels={self._channels}')

    def _set_position(self, position: int):
        """Change the position of playback."""
        self._wave.setpos(position)

    def _get_position(self) -> int:
        """Get position."""
        return self._wave.tell()

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write data to wave file."""
        # Do this so it doesn't return None which is not an int.
        return self._wave.writeframes(data) or 0

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it."""
        size //= self._channels * (self._depth >> 3)

        if self.position >= self._length:
            if self._loops == -1 or self._loop_count < self._loops:
                self._loop_count += 1
                self.seek(0)

        return self._wave.readframes(size)

    def _open(self, filename: str) -> Any:
        """Load the specified file."""
        wave_file = wave.open(filename, self._mode)

        return wave_file

    def close(self):
        """Close and clean up."""
        if not self.closed:
            self._wave.close()

            self._closed = True
