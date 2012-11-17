#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Provides a wrapper for portaudio to allow for easy access, and
# using with the 'with' statement.
# Copyright (C) 2010 Josiah Gordon <josiahg@gmail.com>
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


""" A wrapper for portaudio to allow it to be used with the 'with' statement.

"""

from sys import stderr as sys_stderr

from .io_base import DevIO, io_wrapper
from .io_util import silence
# from .portaudio import portaudio as _portaudio
from import_util import LazyImport

_portaudio = LazyImport('portaudio.portaudio', globals(), locals(),
                        ['portaudio'], 1)

__supported_dict = {
        'output': [bytes],
        'input': [bytes],
        'handler': 'Portaudio',
        'default': True,
        'dependencies': {
            'ctypes': ['portaudio'],
            'python': []
            }
        }


class Portaudio(DevIO):
    """ A class that provides a file like object to write to a portaudio
    stream.

    """

    # Valid bit depths
    _valid_depth = (32, 24, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
                 unsigned=False, floatp=False, buffer_size=None,
                 latency=0.0500000, devindex='default', callback=None,
                 **kwargs):
        """ Portaudio(mode='w', depth=16, rate=44100, channels=2,
        unsigned=False, floatp=False, buffer_size=4092, latency=500000,
        devindex=1, callback=None) -> Initialize the portaudio device.

        """

        super(Portaudio, self).__init__(mode, depth, rate, channels, False,
                                        unsigned, buffer_size, latency)

        if depth in [8, 16, 24, 32]:
            if floatp:
                self._format = _portaudio.paFloat32
            elif unsigned:
                self._format = _portaudio.paUInt8
            else:
                self._format = getattr(_portaudio, 'paInt%s' % depth)
        else:
            self._format = _portaudio.paInt16

        self._rate = float(rate)
        self._floatp = floatp
        self._devindex = devindex
        self._callback = callback

        self._devname = ''

        self._stream = None
        self._portaudio = None

        self._open()

        self._buffer_size = self._stream.buffer_size

        # Buffer to hold extra data.
        self._data = b''

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, unsigned=%(_unsigned)s, floatp=%(_floatp)s, buffer_size=%(_buffer_size)s, latency=%(_latency)s, devindex=%(_devindex)s, callback=%(_callback)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def device_list(self):
        """ A list of the devices with thier names.

        """

        dev_count = self._portaudio.device_count
        name_func = self._portaudio.device_name

        return [name_func(i) for i in range(dev_count)]

    @property
    def rate(self):
        """ The sample current sample rate.

        """

        return int(self._rate)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        # Calculate how many bytes are needed before it can write.
        write_size = self._buffer_size * self._channels * (self._depth >> 3)

        # Append the data to the data buffer.
        self._data += data

        datalen = len(self._data)

        # Don't write anything if there is not enough to fill the buffer,
        # otherwise nothing will play.
        if datalen < write_size:
            if len(data) == 0 and datalen > 0:
                # Just write the last fiew bytes.
                self._stream.write(self._data, datalen)
                # self._data = b''
                return datalen
            else:
                return 0

        # Loop through the collected data and write it out.
        while len(self._data) >= write_size:
            try:
                self._stream.write(self._data[:write_size], self._buffer_size)
            except IOError as err:
                class_name = self.__class__.__name__
                print("(%s.write) %s" % (class_name, err))
                continue
            self._data = self._data[write_size:]

        return datalen

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size) -> Read length data from stream.

        """

        data = b''
        while len(data) < size:
            try:
                data += self._stream.read(size)
            except IOError as err:
                class_name = self.__class__.__name__
                print("(%s.read) %s" % (class_name, err))
        return data[:size]

    def _open(self):
        """ open -> Open the pcm audio output.

        """

        self._portaudio = _portaudio.Portaudio()

        # Silence stderr
        with silence(sys_stderr):
            self._portaudio.initialize()

        dev_list = self.device_list()
        dev_index = self._devindex

        # Get the correct device index.
        if type(dev_index) is str:
            if dev_index in dev_list:
                dev_index = dev_list.index(dev_index)
            else:
                dev_index = 0

        self._devindex = dev_index
        self._devname = dev_list[dev_index]

        if 'w' in self._mode:
            # Setup the output stream parameters.
            out_params = _portaudio.StreamParams(device_index=self._devindex,
                                                 samp_format=self._format,
                                                 channels=self._channels,
                                                 latency=self._latency)
        else:
            out_params = None

        if 'r' in self._mode:
            # Setup the input stream parameters.
            in_params = _portaudio.StreamParams(device_index=self._devindex,
                                                samp_format=self._format,
                                                channels=self._channels,
                                                latency=self._latency)
        else:
            in_params = None

        # Open a stream.
        self._stream = _portaudio.Stream(rate=self._rate,
                                         buffer_size=self._buffer_size,
                                         input_params=in_params,
                                         output_params=out_params,
                                         callback=self._callback)

        self._stream.open()
        self._stream.start()

        self._closed = False

    def close(self):
        """ close -> Close the pcm.

        """

        if not self.closed:
            self._stream.stop()
            # Wait for the stream to stop.
            while not self._stream.stopped:
                pass

            self._stream.close()
            self._portaudio.terminate()

            self._closed = True
