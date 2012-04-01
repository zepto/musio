#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Re-sampling and data conversion functions.
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


""" Re-sampling and data conversion functions.

"""

from array import array

def swap_endian(data):
    """ swap_endian(data) -> Swap the endianness of the data.

    """

    data_array = array('h', data)
    data_array.byteswap()

    return data_array.tostring()

def convert_read(self, rate, channels, depth, unsigned, size=None):
    """ Convert the samples to the given rate and makes it mono or stereo
    depending on the channels value. The data is buffered so 

    """

    if not size:
        size = self._buffer_size

    read_size = size * channels * (depth >> 3)
    width = depth // 8

    data = self._convert_buffer
    while len(data) < read_size:
        temp_data = self.read()
        if not temp_data:
            if self._loops != -1 and self._loop_count >= (self._loops -1):
                if len(data) != 0:
                    data += b'\x00' * (read_size - len(data))
                break
            else:
                self._loop_count += 1
                self.seek(0)
                continue

        if unsigned != self.unsigned:
            temp_data = bias(temp_data, self._width, 128)

        if depth > 8 and self._depth == 8:
            temp_data = lin2lin(temp_data, self._width, width)
        elif depth == 8 and self._depth > 8:
            temp_data = lin2lin(temp_data, self._width, width)
            if unsigned:
                temp_data = bias(temp_data, width, 128)

        # Make it stereo
        if self._channels < channels:
            temp_data = tostereo(temp_data, width, 1, 1)
        # Make it mono
        elif self._channels > channels:
            temp_data = tomono(temp_data, width, 1, 1)

        # Convert the sample rate of the data to the requested rate.
        if rate != self._rate and temp_data:
            temp_data, self._state = ratecv(temp_data, width,
                                            channels, self._rate, rate,
                                            self._state)
        data += temp_data

    self._convert_buffer = data[read_size:]

    return data[:read_size]
