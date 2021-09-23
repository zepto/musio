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


"""A wrapper for portaudio to allow it to be used with the 'with' statement."""

from sys import stderr as sys_stderr
from typing import Any, Callable, Union

from .import_util import LazyImport
from .io_base import DevIO, io_wrapper
from .io_util import silence

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
    """Provide a file like object to write to a portaudio stream."""

    # Valid bit depths
    _valid_depth = (32, 24, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode: str = 'w', depth: int = 16, rate: int = 44100,
                 channels: int = 2, unsigned: bool = False,
                 floatp: bool = False, buffer_size: int = 0,
                 latency: float = 0.0500000, device: Any = 'default',
                 callback: Callable = None, callback_data: Any = None,
                 **_):
        """Initialize the portaudio device."""
        super(Portaudio, self).__init__(
            mode,
            depth,
            rate,
            channels,
            False,
            unsigned,
            buffer_size,
            latency
        )

        if depth in [8, 16, 24, 32]:
            if floatp:
                self._format = _portaudio._portaudio.paFloat32
            elif unsigned:
                self._format = _portaudio._portaudio.paUInt8
            else:
                self._format = getattr(_portaudio._portaudio, f'paInt{depth}')
        else:
            self._format = _portaudio._portaudio.paInt16

        self._rate = float(rate)
        self._floatp = floatp

        try:
            device = int(device)
        except ValueError:
            pass

        self._devindex = device

        self._callback = callback
        self._user_data = callback_data

        self._devname = ''

        self._stream, self._portaudio = self._open()

        self._buffer_size = self._stream.buffer_size

        # Buffer to hold extra data.
        self._data = b''

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(mode="{self._mode}", '
                f'depth={self._depth}, rate={self._rate}, '
                f'channels={self._channels}, unsigned={self._unsigned}, '
                f'floatp={self._floatp}, buffer_size={self._buffer_size}, '
                f'latency={self._latency}, devindex={self._devindex}, '
                f'callback={self._callback}, callback_data={self._user_data})')

    def device_list(self, device: Any = None) -> list[str]:
        """Return a list of the devices with thier names."""
        device = self._portaudio if not device else device
        dev_count = device.device_count
        name_func = device.device_name

        return [name_func(i) for i in range(dev_count)]

    @property
    @io_wrapper
    def is_stream_active(self) -> bool:
        """Return whether or not the stream is active."""
        return self._stream.active

    @property
    @io_wrapper
    def is_stream_stopped(self) -> bool:
        """Return whether or not the stream is stopped."""
        return self._stream.stopped

    @io_wrapper
    def abort_stream(self) -> Union[int, bool]:
        """Abort the stream.

        Stops the stream and drops all buffers.
        """
        return self._stream.abort()

    @io_wrapper
    def stop_stream(self) -> Union[int, bool]:
        """Temporaraly stop the stream.

        Use after a write if there won't be another for a while.  Instead of
        using this write silence until there is something else to
        write.
        """
        return self._stream.stop()

    @io_wrapper
    def start_stream(self) -> Union[int, bool]:
        """Start the stream.

        Use before writing and after calling stop_stream.
        """
        return self._stream.start()

    @property
    def rate(self) -> int:
        """Return the sample current sample rate."""
        return int(self._rate)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write to the pcm device."""
        # Calculate how many bytes are needed before it can write.
        write_size = self._buffer_size * self._channels * (self._depth >> 3)

        # Append the data to the data buffer.
        self._data += data

        datalen = len(self._data)

        # Don't write anything if there is not enough to fill the buffer,
        # otherwise nothing will play.
        if datalen < write_size:
            if len(data) == 0 and datalen > 0:
                # Just write the last few bytes.
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
        """Read length data from stream."""
        data = b''
        while len(data) < size:
            try:
                data += self._stream.read(size)
            except IOError as err:
                class_name = self.__class__.__name__
                print("(%s.read) %s" % (class_name, err))
        return data[:size]

    def _open(self) -> tuple[Any, Any]:
        """Open the pcm audio output."""
        portaudio = _portaudio.Portaudio()

        # Silence stderr
        with silence(sys_stderr):
            portaudio.initialize()

        dev_list = self.device_list(portaudio)
        dev_index = self._devindex

        if type(dev_index) is bytes:
            dev_index = dev_index.decode()

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
        stream = _portaudio.Stream(
            rate=self._rate,
            buffer_size=self._buffer_size,
            input_params=in_params,
            output_params=out_params,
            callback=self._callback,
            user_data=self._user_data
        )

        stream.open()
        stream.start()

        self._closed = False

        return stream, portaudio

    @io_wrapper
    def close(self) -> None:
        """Close the pcm."""
        if not self._closed:
            self._stream.stop()
            # Wait for the stream to stop.
            while not self._stream.stopped:
                pass

            self._stream.close()
            self._portaudio.terminate()

            self._closed = True
