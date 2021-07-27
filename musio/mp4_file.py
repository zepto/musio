#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading aac audio from mp4 files.
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


"""A module for reading aac audio from mp4s."""

from sys import stdout as sys_stdout
from typing import Any

from .aac_file import AACDecoder
from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import silence

_mp4v2_wrapper = LazyImport('mp4v2._mp4v2_wrapper', globals(), locals(),
                            ['mp4v2._mp4v2_wrapper'], 1)

__supported_dict = {
    'ext': ['.mp4', '.m4v', '.m4a'],
    'handler': 'Mp4File',
    'dependencies': {
        'ctypes': ['mp4v2', 'faad'],
        'python': []
    }
}


class Mp4File(AudioIO):
    """A file like object for reading aac audio from mp4s."""

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, **_):
        """Initialize the playback settings of the player."""
        super(Mp4File, self).__init__(filename, 'r', depth, rate, channels)

        self._mp4_handle, self._aac_decoder = self._open(filename)

        self._info_dict |= self._update_info()

        self._length = self._mp4_handle.sample_count

        self._data_buffer = b''

    def to_seconds(self, position: int) -> float:
        """Convert the provided position/length to seconds."""
        return (position * 1024) / self._rate

    def _set_position(self, position: int):
        """Change the position of playback."""
        self._mp4_handle.current_sample = position

    def _get_position(self) -> int:
        """Get the position."""
        # Update the position.
        return self._mp4_handle.current_sample

    def _open(self, filename: str) -> tuple[Any, Any]:
        """Load the specified file."""
        try:
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()

        with silence(sys_stdout):
            mp4_handle = _mp4v2_wrapper.Mp4(filename_b)

        # Get the aac decoder.
        aac_decoder = AACDecoder(*mp4_handle.get_configuration(), mp4=True)

        self._rate = aac_decoder.rate
        self._channels = aac_decoder.channels
        self._depth = aac_decoder.depth

        self._closed = False

        return mp4_handle, aac_decoder

    def _update_info(self) -> dict:
        """Return the information dictionary."""
        tags_dict = self._mp4_handle.get_tag_dict()

        info_dict = {}

        for i in ['name', 'artist', 'albumArtist', 'album', 'composer',
                  'comments', 'genre', 'releaseDate', 'track', 'disk',
                  'description', 'longDescription', 'lyrics', 'copyright',
                  'encodedBy']:
            value = getattr(tags_dict, i, None)
            if value:
                info_dict[i] = value
            elif hasattr(value, 'value'):
                info_dict[i] = value.value

        return info_dict

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it.

        If size is None then read a buffer size.
        """
        data = self._data_buffer

        while len(data) < size:
            # Read the next sample.
            sample = self._mp4_handle.read()

            if sample.size.value == 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        # Fill data buffer until it is the requested
                        # size.
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    self._loop_count += 1
                    self.seek(1)
                    continue

            # Decode data into a temporary buffer.
            temp_data = self._aac_decoder.decode(sample.data,
                                                 sample.size.value)

            # Append decoded data to the data buffer.
            data += temp_data

        # Store extra data for next read.
        self._data_buffer = data[size:]

        # Only return the requested amount of data.
        return data[:size]

    def close(self):
        """Close and clean up."""
        if not self.closed:
            self._mp4_handle.close()
            self._aac_decoder.close()

            self._closed = True
