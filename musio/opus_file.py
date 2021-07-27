#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of Opus files.
# Copyright (C) 2015 Josiah Gordon <josiahg@gmail.com>
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


"""A module for reading Opus files."""

from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

_opus = LazyImport('opus.opus', globals(), locals(), ['opus'], 1)


__supported_dict = {
    'ext': ['.opus'],
    'handler': 'OpusFile',
    'dependencies': {
        'ctypes': ['opus', 'opusfile'],
        'python': []
    }
}


class OpusFile(AudioIO):
    """A file like object for reading media files with opus."""

    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, **_):
        """Initialize the playback settings of the player."""
        super(OpusFile, self).__init__(filename, 'r', 16, 48000, 2)

        self._rate = 48000
        self._data_buffer = b''
        self._position = 0
        self._length = 0

        self._opus_file = self._open(filename)

        if self._opus_file:
            self._length = _opus.op_pcm_total(self._opus_file, -1)
            self._closed = False
            self._info_dict.update(self._update_info())
        else:
            raise(OSError(f"Failed to open opus: {filename}."))

    def _get_position(self) -> int:
        """Update the position variable."""
        # Update the position.
        self._position = _opus.op_pcm_tell(self._opus_file)
        return self._position

    def _set_position(self, position: int):
        """Change the position of playback."""
        _opus.op_pcm_seek(self._opus_file, position)

    def _update_info(self) -> dict:
        """Update the id3 info for the opened flac."""
        info_dict = {}

        self._channels = _opus.op_channel_count(self._opus_file, -1)

        tags = _opus.op_tags(self._opus_file, -1)
        for i in range(tags.contents.comments):
            try:
                comment = tags.contents.user_comments[i]
                comment_len = tags.contents.comment_lengths[i]
                comment_str = _opus.string_at(comment, comment_len)
                if b'METADATA_BLOCK_PICTURE' not in comment_str:
                    name, value = comment_str.decode(
                        'utf-8',
                        'replace'
                    ).split('=')
                    info_dict[name] = value
            except Exception:
                continue

        return info_dict

    def _open(self, filename: str) -> Any:
        """Open a opus file."""
        try:
            # Convert filename to bytes.
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()

        err = _opus.c_int()
        opus_file = _opus.op_open_file(filename_b, _opus.byref(err))

        if err.value != _opus.OPUS_OK:
            msg_out(_opus.opus_strerror(err))
            return None

        return opus_file

    def close(self):
        """Close and finish the flac decoder."""
        if not self.closed and self._opus_file:
            _opus.op_free(self._opus_file)

            self._closed = True
            del(self._opus_file)

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        buf_size = 960
        byte_buffer = (_opus.opus_int16 * buf_size)()

        data = self._data_buffer[:size]

        while len(data) < size:
            bytes_read = _opus.op_read_stereo(
                self._opus_file,
                byte_buffer,
                buf_size
            )

            if bytes_read < 0:
                msg_out(_opus.opus_strerror(bytes_read))

            # Check for the end of the stream.
            if bytes_read == 0:
                # Get the last sample so we can pad it for output.
                data = self._data_buffer
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1
                    self.seek(0)
                    continue

            data += _opus.string_at(
                byte_buffer,
                bytes_read * (self._channels * _opus.sizeof(_opus.opus_int16))
            )

        self._data_buffer = data[size:]

        return data[:size]
