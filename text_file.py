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

from io_base import AudioIO, io_wrapper

__supported_dict = {
        'ext': ['.txt'],
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

        self.seek = self._file.seek
        self.tell = self._file.tell

        self._closed = False

    @io_wrapper
    def write(self, data: str) -> int:
        """ Write data to file.

        """

        return self._file.write(data)

    @io_wrapper
    def read(self, size: int) -> str:
        """ Return size or less ammount of text.

        """

        return self._file.readlines(size)

    def close(self):
        """ Close file.

        """

        self._file.close()
        self._closed = True
