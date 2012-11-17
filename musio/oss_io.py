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


""" A thin ossaudiodev wrapper that allows it to be used with the with 
statement.

"""

from .io_base import DevIO, io_wrapper
# import ossaudiodev

from .import_util import LazyImport
ossaudiodev = LazyImport('ossaudiodev', globals(), locals(), [], 1)

__supported_dict = {
        'output': [bytes],
        'input': [bytes],
        'handler': 'Oss',
        # 'default': True
        }


class Oss(DevIO):
    """ A class that provides a file like object to write to an oss pcm
    object.

    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, buffer_size=None, **kwargs):
        """ Oss(depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None) -> Initialize the alsa pcm device.

        """

        super(Oss, self).__init__(mode, depth, rate, channels, bigendian,
                                  unsigned, buffer_size)

        if depth == 8:
            audio_format = getattr(ossaudiodev, "AFMT_%s8" % \
                                   ('U' if unsigned else 'S'))
        else:
            audio_format = getattr(ossaudiodev, "AFMT_%s16_%s" % \
                                   ('U' if unsigned else 'S',
                                    'BE' if bigendian else 'LE'))

        self._format = audio_format

        self._dsp = self._open()

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        return self._dsp.write(data)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=0) -> Read length bytes from input.

        """

        return self._dsp.read(size)

    def _open(self):
        """ open -> Open the pcm audio output.

        """

        dsp = ossaudiodev.open(self._mode)
        try:
            dsp.setparameters(self._format, self._channels, self._rate, True)
        except OSSAudioError as err:
            print("Error opening dsp: %s" % err)

        self._closed = False

        return dsp

    def close(self):
        """ close -> Close the pcm.

        """

        if not self.closed:
            self._dsp.close()
            self._dsp = None

            self._closed = True
