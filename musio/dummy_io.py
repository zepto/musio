#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A Dummy io device.
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


""" A Dummy io device.

"""

from .io_base import DevIO, io_wrapper

__supported_dict = {
        'output': [bytes, str],
        'input': [bytes, str],
        'handler': 'Dummy',
        # 'default': True
        }


class Dummy(DevIO):
    """ A class that provides a file like object to write to a dummy pcm.

    """

    # Valid bit depths.
    _valid_depth = (32, 24, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, buffer_size=None,
                 latency=500000, **kwargs):
        """ Dummy(mode='w', depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None, latency=500000, **kwargs) ->
        Initialize the dummy pcm device.

        """

        super(Dummy, self).__init__(mode, depth, rate, channels, bigendian,
                                    unsigned, buffer_size)

        self._dummy = self._open()

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='{_mode}', depth={_depth}, rate={_rate}, channels={_channels}, bigendian={_bigendian}, unsigned={_unsigned}, buffer_size={_buffer_size}, latency={_latency}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        return len(data)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=0) -> Read length bytes from input.

        """

        return b'\x00' * size

    def _open(self):
        """ open -> Open the pcm audio output.

        """

        self._closed = False

        return True

    def close(self):
        """ close -> Close the pcm.

        """

        if not self.closed:
            self._dummy = None

            self._closed = True
