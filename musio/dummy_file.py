#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A Dummy file.
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


""" A Dummy file.

"""

from .io_base import AudioIO, io_wrapper

__supported_dict = {
    'ext': ['.*'],
    'handler': 'DummyFile',
}


class DummyFile(AudioIO):
    """ Handles all files with read and write.

    """

    # Valid bit depths.
    _valid_depth = (32, 16, 8)

    # Only reading is supported
    _supported_modes = 'rw'

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, **kwargs):
        """ AllFile(self, filename, mode='r', depth=16, rate=44100, channels=2,
                    bigendian=False, unsigned=False, **kwargs) -> Loads the
        correct codec for the file and acts as a wrapper providing additional
        funcionality.

        """

        super(DummyFile, self).__init__(filename, mode, depth, rate, channels)

        self._bigendian = bigendian
        self._unsigned = unsigned

        self.write = lambda data: len(data)
        self.write.__doc__ = """ write(data) -> Write data to dummy file. """
        self.write.__annotations__ = {'data': bytes, 'return': int}

        self ._closed = False

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def close(self):
        """ Close.

        """

        if not self.closed:
            self._closed = True

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Returns audio data with its format converted if
        necessary.

        """

        return b'\x00' * size
