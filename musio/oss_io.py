#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Provides a thin wrapper for ossaudiodev to allow for easy access, and
# using with the 'with' statement.
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


"""OSS wrapper.

A thin ossaudiodev wrapper that allows it to be used with the with statement.
"""

from typing import Any

from .import_util import LazyImport
from .io_base import DevIO, io_wrapper

ossaudiodev = LazyImport('ossaudiodev', globals(), locals(), [], 0)

__supported_dict = {
    'output': [bytes],
    'input': [bytes],
    'handler': 'Oss',
    # 'default': True
}


class Oss(DevIO):
    """OSS file object for reading and writing.

    A class that provides a file like object to write to an oss pcm object.
    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode: str = 'w', depth: int = 16, rate: int = 44100,
                 channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, buffer_size: int = 0,
                 device: str = 'default', **kwargs):
        """Initialize the alsa pcm device."""
        super(Oss, self).__init__(mode, depth, rate,
                                  channels, bigendian, unsigned, buffer_size)

        if depth == 8:
            audio_format = getattr(
                ossaudiodev, f"AFMT_{'U' if unsigned else 'S'}8")
        else:
            audio_format = getattr(
                ossaudiodev,
                f"AFMT_{'U' if unsigned else 'S'}16_"
                f"{'BE' if bigendian else 'LE'}"
            )

        self._format = audio_format
        self._device = '/dev/dsp' if device == 'default' else device

        self._dsp = self._open()

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write to the pcm device."""
        return self._dsp.write(data)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """Read length bytes from input."""
        return self._dsp.read(size)

    def _open(self) -> Any:
        """Open the pcm audio output."""
        dsp = ossaudiodev.open(self._device, self._mode)
        try:
            dsp.setparameters(self._format, self._channels, self._rate, True)
        except OSSAudioError as err:
            print(f"Error opening dsp: {err}")

        self._closed = False

        return dsp

    def close(self):
        """Close the pcm."""
        if not self.closed:
            self._dsp.close()

            self._closed = True
