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


""" A module for reading agws.

"""

import os
from time import sleep
from tempfile import mktemp

from io_base import AudioIO, OnDemand, io_wrapper

_agw = OnDemand('audiality.audiality', globals(), locals(),
                ['audiality'], 0)

__supported_dict = {
        'ext': ['.agw'],
        'handler': 'AgwFile'
        }


def redirect_cstd():
    """ Redirect ctypes stdout/stderr.

    """

    import sys
    sys.stdout.flush()
    oldstdout = os.dup(1)
    oldstderr = os.dup(2)
    r, w = os.pipe()
    os.dup2(w, 1)
    os.dup2(w, 2)
    os.close(w)
    os.close(r)
    sys.stdout = os.fdopen(oldstdout, 'w')
    sys.stderr = os.fdopen(oldstderr, 'w')


class AgwFile(AudioIO):
    """ A file like object for reading agws.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, quality=4,
                 latency=50, **kwargs):
        """ AgwFile(filename, depth=16, rate=44100, channels=2, quality=4,
        latency=50) -> Initialize
        the playback settings of the player.

        """

        super(AgwFile, self).__init__(filename, 'r', depth, rate, channels)

        self._raw_filename = None
        self._raw_file = None
        self._quality = quality
        self._latency = latency
        self._depth = 16

        self._raw_file = self._open(filename)

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='{_filename}', depth={_depth}, rate={_rate}, channels={_channels}, quality={_quality}, latency={_latency}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        filename = filename.encode()

        # Stop the audiality library from printing information.
        redirect_cstd()

        name = os.path.basename(filename)
        path = os.path.dirname(filename)

        # Create a temporary fifo in the current directory.
        self._raw_filename = os.path.basename(mktemp())
        try:
            if not os.path.isfile(self._raw_filename):
                os.mkfifo(self._raw_filename)
        except OSError as err:
            print("Failed to create FIFO: %s" % err)

        output = 'disk:%s' % self._raw_filename

        _agw.ady_set_path(path)

        agw_id = _agw.ady_wave_load(0, name, -1)
        if agw_id:
            raise IOError("Error loading %s, %s" % (name, agw_id))

        _agw.ady_set_interface(1, output.encode())
        _agw.ady_start(self._rate, self._latency, 0)
        _agw.ady_quality(self._quality)
        _agw.ady_channel_control(0, -2, 2, agw_id)
        _agw.ady_channel_play(0, 0, _agw.c_float(60.0), _agw.c_float(1.0))

        self._closed = False

        self._agw_id = agw_id

        return open(self._raw_filename, 'rb', buffering=0)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        return self._raw_file.read(size)

    def close(self):
        """ close -> Closes and cleans up.

        """

        try:
            # Change the interface to an empty string to disconnect it
            # so it can be stopped.
            _agw.ady_set_interface(1, '')

            _agw.ady_channel_stop(-1, -1)
            _agw.ady_close()
            _agw.ady_wave_free(self._agw_id)

            if self._raw_file:
                self._raw_file.close()
                os.remove(self._raw_filename)

            self._closed = True

            return True
        except Exception as err:
            return False
