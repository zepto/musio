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


""" A class to handle wave audio like python files.

"""

import ctypes as _ctypes
import wave

from io_base import AudioIO, io_wrapper

__supported_dict = {
        'ext': ['.wav'],
        'handler': 'WaveFile'
        }


class WaveFile(AudioIO):
    """ A class for wav file access.

    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Both reading and writing are supported
    _supported_modes = 'rw'

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2,
                 **kwargs):
        """ WaveFile(filename, mode='r', depth=16, rate=44100, channels=2) ->
        Initialize the playback settings of the player.

        """

        self._mode = mode

        self._wave = self._open(filename)

        if 'r' in mode:
            super(WaveFile, self).__init__(filename, mode,
                                           self._wave.getsampwidth() * 8,
                                           self._wave.getframerate(),
                                           self._wave.getnchannels())
            self._length = self._wave.getnframes()
            self._width = self._wave.getsampwidth()
        elif 'w' in mode:
            super(WaveFile, self).__init__(filename, mode, depth, rate,
                                           channels)
            self._wave.setnchannels(channels)
            self._wave.setsampwidth(depth // 8)
            self._wave.setframerate(rate)

        self._closed = False

        if self._depth == 8:
            self._unsigned = True

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='{_filename}', mode='{_mode}', depth={_depth}, rate={_rate}, channels={_channels}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._wave.setpos(position)

    def _get_position(self):
        """ Updates the position variable.

        """

        return self._wave.tell()

    @io_wrapper
    def write(self, data):
        """ write(data) -> Write data to wave file.

        """

        return self._wave.writeframes(data)

    @io_wrapper
    def read(self, size=None):
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        size //= self._channels * (self._depth >> 3)

        if self.position >= self._length:
            if self._loops == -1 or self._loop_count < self._loops:
                self._loop_count += 1
                self.seek(0)

        return self._wave.readframes(size)

    def _open(self, filename):
        """ _load(filename) -> Load the specified file.

        """

        wave_file = wave.open(filename, self._mode)

        return wave_file

    def close(self):
        """ close -> Closes and cleans up.

        """

        self._wave.close()

        self._closed = True

        return self._closed
