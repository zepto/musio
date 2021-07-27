#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of agw files.
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


"""A module for reading agws."""

import os
from sys import stderr as sys_stderr
from sys import stdout as sys_stdout
# from tempfile import mktemp
from typing import BinaryIO

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import silence

_agw = LazyImport('audiality.audiality', globals(), locals(),
                  ['audiality'], 1)

__supported_dict = {
    'ext': ['.agw'],
    'handler': 'AgwFile',
    'dependencies': {
        'ctypes': ['audiality'],
        'python': []
    }
}


class AgwFile(AudioIO):
    """A file like object for reading agws."""

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, quality: int = 4, latency: int = 50, **_):
        """Initialize the playback settings of the player."""
        super(AgwFile, self).__init__(filename, 'r', depth, rate, channels)

        self._quality = quality
        self._latency = latency
        self._depth = 16

        self._raw_file, self._raw_filename = self._open(filename)

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'depth={self._depth}, rate={self._rate}, '
                f'channels={self._channels}, quality={self._quality}, '
                f'latency={self._latency})')

    def _open(self, filename: str) -> tuple[BinaryIO, str]:
        """Load the specified file."""
        filename_b = filename.encode("utf-8", "surrogateescape")

        # Stop the audiality library from printing information.
        # redirect_cstd()

        name = os.path.basename(filename_b)
        path = os.path.dirname(filename_b)

        # Create a temporary fifo in the current directory.
        raw_filename = "musio.raw"
        try:
            if not os.path.isfile(raw_filename):
                os.mkfifo(raw_filename)
        except OSError as err:
            print(f"Failed to create FIFO: {err}")

        output = f"disk:{raw_filename}"

        # Silence stdout and stderr.
        with silence(sys_stdout), silence(sys_stderr):
            # Open the audio engine and start it.
            _agw.ady_open()
            _agw.ady_set_interface(1, output.encode())
            _agw.ady_start(self._rate, self._latency, 0)

        # Set playback quality.
        _agw.ady_quality(self._quality)

        # Set the path to load data from.
        _agw.ady_set_path(path)

        # Load the file
        agw_id = _agw.ady_wave_load(0, name, -1)

        if agw_id:
            raise IOError(f"Error loading {name}, {agw_id}")

        # Start playing.
        _agw.music_play(1, agw_id)
        # _agw.ady_channel_control(0, -2, 2, agw_id)
        # _agw.ady_channel_play(0, 0, _agw.c_float(60.0), _agw.c_float(1.0))

        self._agw_id = agw_id

        self._closed = False

        # Open the raw file that is written to.
        return open(raw_filename, "rb", buffering=0), raw_filename

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it.

        If size is None then read a buffer size.
        """
        return self._raw_file.read(size)

    def close(self):
        """Close and clean up."""
        if not self.closed:
            # Change the interface to an empty string to disconnect it
            # so it can be stopped.
            # _agw.ady_set_interface(1, b'')

            # _agw.ady_channel_stop(-1, -1)
            # _agw.ady_close()
            _agw.ady_wave_free(self._agw_id)

            if self._raw_file:
                self._raw_file.close()
                os.remove(self._raw_filename)

            self._closed = True
