#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Handles opening all supported files.
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


""" Handles opening all supported files.

"""

import audioop
from os.path import basename as os_basename

from .io_base import AudioIO, io_wrapper
from .io_util import get_codec
from .conversion_util import swap_endian

__supported_dict = {
    'ext': ['.*'],
    'handler': 'AllFile',
    'default': True
}


class AllFile(AudioIO):
    """ Handles all files get_codec can open.

    """

    # Valid bit depths.
    _valid_depth = (32, 16, 8)

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, **kwargs):
        """ AllFile(self, filename, mode='r', depth=16, rate=44100, channels=2,
                    bigendian=False, unsigned=False, **kwargs) -> Loads the
        correct codec for the file and acts as a wrapper providing additional
        funcionality.

        """

        codec = get_codec(filename, blacklist=[os_basename(__file__)])

        self._supported_modes = getattr(codec, '_supported_modes', 'r')

        super(AllFile, self).__init__(filename, mode, depth, rate, channels)

        self._bigendian = bigendian
        self._unsigned = unsigned

        self._state = None

        self._source = codec(filename, mode=mode, **kwargs)

        annotations = getattr(codec.read, '__annotations__')
        self.read.__annotations__.update(annotations)

        self._buffer = annotations.get('return', bytes)()
        self._buffer_size = self._source.buffer_size

        self._length = self._source.length
        self._info_dict = self._source._info_dict
        self.write = self._source.write

        self._closed = False

        if self._depth != self._source.depth:
            self._convert_depth = lambda data: \
                    audioop.lin2lin(data, self._source._width, self._width)
        else:
            self._convert_depth = lambda data: data

        if self._unsigned != self._source.unsigned:
            self._convert_unsigned = lambda data: \
                    audioop.bias(data, self._source._width, 128)
        else:
            self._convert_unsigned = lambda data: data

        # Make it stereo
        if self._source.channels < self._channels:
            self._convert_channels = lambda data: audioop.tostereo(data,
                                                                   self._width,
                                                                   1, 1)
        # Make it mono
        elif self._source.channels > self._channels:
            self._convert_channels = lambda data: audioop.tomono(data,
                                                                 self._width,
                                                                 1, 1)
        else:
            self._convert_channels = lambda data: data

        # Convert the sample rate of the data to the requested rate.
        if self._rate != self._source.rate:
            self._convert_rate = lambda data: audioop.ratecv(data, self._width,
                                                             self._channels,
                                                             self._source.rate,
                                                             self._rate,
                                                             self._state)
        else:
            self._convert_rate = lambda data: (data, self._state)

        if self._bigendian != self._source.bigendian:
            self._convert_endian = swap_endian
        else:
            self._convert_endian = lambda data: data

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def close(self):
        """ Close.

        """

        if not self.closed:
            self._source.close()

            self._closed = True

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._source.position = position

    def _get_position(self):
        """ Returns the current position.

        """

        return self._source.position

    @property
    def loops(self):
        """ How many times the file should loop.

        """

        return self._source.loops

    @loops.setter
    def loops(self, value):
        """ Set how many times the file should loop.

        To play forever use a value of -1.

        """

        self._source.loops = value

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Returns audio data with its format converted if
        necessary.

        """

        data = self._buffer

        while len(data) < size:
            temp_data = self._source.read(size)
            if type(temp_data) is not bytes:
                return temp_data

            if not temp_data:
                if len(data) != 0:
                    data += b'\x00' * (size - len(data))
                break

            temp_data = self._convert_depth(temp_data)

            temp_data = self._convert_unsigned(temp_data)

            temp_data = self._convert_channels(temp_data)

            temp_data, self._state = self._convert_rate(temp_data)

            temp_data = self._convert_endian(temp_data)

            data += temp_data

        self._buffer = data[size:]

        return data[:size]
