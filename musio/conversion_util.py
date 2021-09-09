#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Audio conversion utilities.
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


"""Audio conversion utilities."""

import audioop
import math
from array import array

from .io_base import AudioIO, io_wrapper


def swap_endian(data: bytes) -> bytes:
    """Swap the endianness of the data."""
    data_array = array('h', data)
    data_array.byteswap()

    return data_array.tobytes()


class AudioConvert():
    """Audio conversion utilities."""

    def __init__(self, depth: int, channels: int, samplerate: int,
                 unsigned: bool = False):
        """Convert audio data.

        Resample audio data with the given values to any other type.
        """
        # Store the resample state for the next resample.
        self._state = None

        # Setup source values.
        self._depth = depth
        self._rate = samplerate
        self._channels = channels
        self._unsigned = unsigned
        self._width = depth // 8

    def convert_to(self, data: bytes, to_depth: int, to_channels: int,
                   to_rate: int, to_unsigned: bool = False) -> bytes:
        """Convert audio data."""
        dest_width = to_depth // 8

        print(to_depth, self._depth)
        if self._depth != to_depth:
            if self._depth == 8:
                data = audioop.bias(data, 1, 128)
            data = audioop.lin2lin(
                data,
                self._width,
                dest_width
            )
            if to_depth == 8:
                data = audioop(data, 1, 128)

        if self._unsigned != to_unsigned:
            data = audioop.bias(data, dest_width, 128)

        # Make it stereo
        if self._channels < to_channels:
            data = audioop.tostereo(data, dest_width, 1, 1)
        # Make it mono
        elif self._channels > to_channels:
            data = audioop.tomono(data, dest_width, 1, 1)

        # print(dest_width)
        # Convert the sample rate of the data to the requested rate.
        if self._rate != to_rate and data:
            data, self._state = audioop.ratecv(
                data,
                dest_width,
                to_channels,
                self._rate,
                to_rate,
                self._state,
                2,
                1
            )

        return data


class ConvertReader(AudioIO):
    """Audio data reader that converts it."""

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Only reading
    _supported_modes = 'r'

    def __init__(self, source: AudioIO, depth: int = 16, rate: int = 44100,
                 channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, floatp: bool = False, **_):
        """Set up the format to convert read data to."""
        super(ConvertReader, self).__init__("", 'r', depth, rate, channels)

        self._source = source

        self._bigendian = bigendian
        self._unsigned = unsigned
        self._floatp = floatp

        self._state = None

        self._buffer = b''

        self._closed = False

    def close(self):
        """Close."""
        self._closed = True

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Convert audio.

        Convert the samples to the given rate and makes it mono or stereo
        depending on the channels value.
        """
        data = self._buffer

        while len(data) < size:
            temp_data = self._source.read()
            if not temp_data:
                if len(data) != 0:
                    data += b'\x00' * (size - len(data))
                break

            if self._source._floatp and not self._floatp:
                in_array = array('f', temp_data)
                out_array = array(f"{'h' if self._depth <= 16 else 'i'}")
                for i in in_array:
                    if i >= 1.0:
                        out_array.append(32767)
                    elif i <= -1.0:
                        out_array.append(-32768)
                    else:
                        out_array.append(math.floor(i * 32768.0))
                temp_data = out_array.tobytes()

            # Convert audio data from source width to self._width.
            if self._depth != self._source.depth:
                temp_data = audioop.lin2lin(
                    temp_data,
                    self._source._width,
                    self._width
                )

            if self._unsigned != self._source.unsigned:
                temp_data = audioop.bias(temp_data, self._source._width, 128)

            # Make it stereo
            if self._source.channels < self._channels:
                temp_data = audioop.tostereo(temp_data, self._width, 1, 1)
            # Make it mono
            elif self._source.channels > self._channels:
                temp_data = audioop.tomono(temp_data, self._width, 1, 1)

            # Convert the sample rate of the data to the requested rate.
            if self._rate != self._source.rate and temp_data:
                temp_data, self._state = audioop.ratecv(
                    temp_data,
                    self._width,
                    self._channels,
                    self._source.rate,
                    self._rate,
                    self._state
                )

            data += temp_data

        self._buffer = data[size:]

        return data[:size]
