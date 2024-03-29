#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Thin wrapper on the text file object.
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


"""Thin wrapper on the text file object."""

import re
from mmap import ACCESS_READ, mmap
from os.path import getsize

from .io_base import AudioIO, io_wrapper


def issupported(filename: str, *_) -> bool:
    """Return True if file is supported else False."""
    import mimetypes

    # Initialize mimetypes.
    mimetypes.init()

    # Get the mime type of filename.
    mimetype, _ = mimetypes.guess_type(filename)

    # If no mimtype was found then filename is not supported.
    if not mimetype:
        return False

    # File containing text are supported.
    return True if 'text' in mimetype else False

__supported_dict = {
    'ext': ['.txt'],
    'issupported': issupported,
    'handler': 'TextFile',
    'default': True
}


class TextFile(AudioIO):
    """Wrap text file objects."""

    def __init__(self, filename: str, mode: str = 'r',
                 sentence_endings: str = '.!?', **kwargs):
        """Just a regular file object."""
        super(TextFile, self).__init__(filename, mode)

        # Rate is 0 since this is a text file.
        self._rate = 0

        # Only read one line/sentence at a time.
        self._buffer_size = 1

        # Regex to match sentences.
        sentence_endings = f'.*?[{re.escape(sentence_endings)}]'
        re_flags = re.DOTALL | re.IGNORECASE | re.MULTILINE

        # Compile the sentence regex.
        sentence_regex = re.compile(sentence_endings.encode(), re_flags)

        # Open the file with the correct mode.
        self._fileobj = open(filename, mode)

        # Memory mapped file for quick searching.
        mmapobj = mmap(self._fileobj.fileno(), 0, access=ACCESS_READ)

        # List of sentences in file
        sentence_list = sentence_regex.findall(mmapobj[:])

        # No need for the mmap to be open anymore
        mmapobj.close()

        # Check for sentence endings.
        if 'r' in mode and sentence_list:
            self._line_list = [sentence.decode() for sentence in sentence_list]
        elif 'r' in mode:
            self._line_list = self._fileobj.readlines()
        else:
            # Not reading the file so line_list is empty and length is zero.
            self._line_list = []

        if self._line_list:
            # The length is the length of the line list.
            self._length = len(self._line_list)
        else:
            self._length = getsize(filename)

        # Current index.
        self._index = 0

        self._closed = False

    def __repr__(self):
        """Return a python expression to recreate this instance."""
        return (f"{self.__class__.__name__}(filename='{self._filename}', "
                f"mode='{self._mode}')")

    def _set_position(self, position: int):
        """Change the position of playback."""
        if 'w' in self._mode:
            self._fileobj.seek(position)
        else:
            self._index = int(position)

    def _get_position(self) -> int:
        """Return the current position."""
        if 'w' in self._mode:
            return self._fileobj.tell()
        else:
            return self._index

    @io_wrapper
    def write(self, data: str) -> int:
        """Write data to file."""
        return self._fileobj.write(data)

    @io_wrapper
    def readline(self, size: int = -1) -> str:
        """Return the next line or size bytes."""
        if size == -1:
            return self.read(self._buffer_size)
        else:
            return self.read(self._buffer_size)[:size]

    @io_wrapper
    def readlines(self, count: int = -1) -> str:
        """Return count lines/sentences if it can."""
        # Start index.
        slice_start = self._index

        # Return all the lines if count is -1.
        if count == -1:
            self._index = self._length
            return ' '.join(self._line_list[slice_start:])

        # Calculate the last index to read to.
        slice_end = slice_start + count

        # Read count number of sentences if available.
        lines = ' '.join(self._line_list[slice_start:slice_end])

        # Increment the sentence index.
        self._index += count % ((self._length - slice_start) + count)

        return lines.replace('\n', ' ')

    @io_wrapper
    def read(self, size: int = -1) -> str:
        """Return size or less ammount of text."""
        data = self.readlines(size)

        if not data:
            if self._loops == -1 or self._loop_count < self._loops:
                self._loop_count += 1
                self.position = 0
                data = self.read(size)

        return data

    def close(self):
        """Close file."""
        if not self.closed:
            self._fileobj.close()
            self._line_list = []
            self._closed = True
