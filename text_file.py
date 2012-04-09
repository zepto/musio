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


""" Thin wrapper on the text file object.

"""

from os.path import getsize as os_getsize

from io_base import AudioIO, io_wrapper

def issupported(filename, *args):
    """ issupported(filename) -> Returns True if file is supported else False.

    """

    import mimetypes

    mimetypes.init()

    mimetype, encoding = mimetypes.guess_type(filename)

    if not mimetype:
        return False

    return True if 'text' in mimetype else False

__supported_dict = {
        'ext': ['.txt'],
        'issupported': issupported,
        'handler': 'TextFile',
        'default': True
        }


class TextFile(AudioIO):
    """ Wrap text file objects.

    """

    def __init__(self, filename, mode='r', **kwargs):
        """ TextFile(filename, mode='r') -> Just a regular file
        object.

        """

        super(TextFile, self).__init__(filename, mode)

        self._buffer_size = 1

        self._file = open(filename, mode)

        self._length = os_getsize(filename)

        self.seek = self._file.seek
        self.tell = self._file.tell
        self.readline = self._file.readline

        self._closed = False

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', mode='%(_mode)s'" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _set_position(self, position: int):
        """ Change the position of playback.

        """

        self._file.seek(position)

    def _get_position(self) -> int:
        """ Returns the current position.

        """

        return self._file.tell()

    @io_wrapper
    def write(self, data: str) -> int:
        """ Write data to file.

        """

        return self._file.write(data)

    def sreadlines(self, size: int) -> str:
        """ Returns size number of lines concatenated into a string.

        """

        return ''.join([self._file.readline() for i in range(size)])

    @io_wrapper
    def read(self, size: int) -> str:
        """ Return size or less ammount of text.

        """

        data = self.sreadlines(size)

        if not data:
            if self._loops == -1 or self._loop_count < self._loops:
                self._loop_count += 1
                self._file.seek(0)
                data = self.sreadlines(size)

        return data

    def close(self):
        """ Close file.

        """

        if not self.closed:
            self._file.close()
            self._closed = True
