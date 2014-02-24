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


""" A module for reading aac audio from mp4s.

"""

from sys import stdout as sys_stdout

from .aac_file import AACDecoder
from .io_base import AudioIO, io_wrapper
from .io_util import silence
# from .mp4v2 import _mp4v2

from .import_util import LazyImport

_mp4v2 = LazyImport('mp4v2._mp4v2', globals(), locals(),
                    ['_mp4v2'], 1)
_mp4v2_wrapper = LazyImport('mp4v2._mp4v2_wrapper', globals(), locals(),
                        ['mp4v2._mp4v2_wrapper'], 1)

__supported_dict = {
    'ext': ['.mp4', '.m4v'],
    'handler': 'Mp4File',
    'dependencies': {
        'ctypes': ['mp4v2', 'faad'],
        'python': []
    }
}


class Mp4File(AudioIO):
    """ A file like object for reading aac audio from mp4s.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, **kwargs):
        """ Mpg4File(filename, depth=16, rate=44100, channels=2) -> Initialize
        the playback settings of the player.

        """

        super(Mp4File, self).__init__(filename, 'r', depth, rate, channels)

        self._tags_dict = {}

        self._aac_decoder = None
        self._mp4_handle = self._open(filename)

        self._update_info()

        self._length = self._mp4_handle.sample_count

        self._data = b''

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._mp4_handle.current_sample = position

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return self._mp4_handle.current_sample

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        with silence(sys_stdout):
            mp4_handle = _mp4v2_wrapper.Mp4(filename.encode())

        # Get the aac decoder.
        self._aac_decoder = AACDecoder(*mp4_handle.get_configuration())

        self._rate = self._aac_decoder.rate
        self._channels = self._aac_decoder.channels
        self._depth = self._aac_decoder.depth

        self._closed = False

        return mp4_handle

    def _update_info(self):
        """ Updates the id3 info for the opened mp3.

        """

        tags_dict = self._mp4_handle.get_tag_dict()

        info_dict = self._info_dict

        for i in ['name', 'artist', 'albumArtist', 'album', 'composer',
                  'comments', 'genre', 'releaseDate', 'track', 'disk',
                  'description', 'longDescription', 'lyrics', 'copyright',
                  'encodedBy']:
            value = getattr(tags_dict, i, None)
            if value:
                info_dict[i] = value
            elif hasattr(value, 'value'):
                info_dict[i] = value.value

        self._tags_dict = self._info_dict = info_dict

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        data = self._data

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
        self._data = data[size:]

        # Only return the requested amount of data.
        return data[:size]

    def close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            self._mp4_handle.close()
            self._aac_decoder.close()

            self._closed = True
