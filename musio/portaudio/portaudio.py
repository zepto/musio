#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Portaudio module.
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


"""Portaudio module."""

from typing import Any, Callable, Union
# from ._portaudio import *
from . import _portaudio

class Info(dict[Any, Any]):
    """An info class."""

    def __init__(self, info_struct: _portaudio.Structure):
        """Wrap a struct in a dict to make it easier to access."""
        for key, val in info_struct.contents._fields_:
            setattr(self, key, getattr(info_struct.contents, key))


class Portaudio(object):
    """Portaudio class.

    A portaudio object that can be used with the 'with' statement
    to initialize and terminate portaudio.  Portaudio has to be initialized
    before any portaudio functions are called.
    """

    def initialize(self) -> int:
        """Initialize portaudio.  Has to be called first."""
        return _portaudio.Pa_Initialize()

    def terminate(self) -> int:
        """Terminate portaudio."""
        return _portaudio.Pa_Terminate()

    @property
    def device_count(self) -> int:
        """The number of valid devices available."""
        return _portaudio.Pa_GetDeviceCount()

    def device_name(self, devindex: int) -> str:
        """The name if the device at index 'devindex.'"""
        try:
            return _portaudio.Pa_GetDeviceInfo(devindex).contents.name.decode()
        except Exception as err:
            return f'{err}'

    @property
    def default_output_device(self) -> int:
        """The index of the default output device."""
        return _portaudio.Pa_GetDefaultOutputDevice()

    @property
    def default_input_device(self) -> int:
        """The index of the default input device."""
        return _portaudio.Pa_GetDefaultInputDevice()

    @property
    def api_count(self) -> int:
        """The number of valid host apis."""
        return _portaudio.Pa_GetHostApiCount()

    @property
    def default_api(self) -> int:
        """The index of the default host api."""
        return _portaudio.Pa_GetDefaultHostApi()

    def __enter__(self) -> object:
        """Provides the ability to use pythons with statement."""
        try:
            self.initialize()
            return self
        except Exception as err:
            print(err)
            return object

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Close the pcm when finished."""
        try:
            self.terminate()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False


class StreamParams(_portaudio.PaStreamParameters):
    """Portaudio stream parameters wrapper class."""

    def __init__(self, device_index: int = 0, channels: int = 2,
                 samp_format: _portaudio.c_ulong = _portaudio.paInt16,
                 latency: float = 500000):
        """Create a parameter object.  Use when creating a stream."""
        max_dev_index = _portaudio.Pa_GetDeviceCount()
        if device_index not in range(max_dev_index):
            print(f"Invalid device, should be 0-{max_dev_index-1}. "
                  f" Using default.")
            device_index = _portaudio.Pa_GetDefaultOutputDevice()

        super(StreamParams, self).__init__()

        self.device = device_index
        self.channelCount = channels
        self.sampleFormat = samp_format
        self.suggestedLatency = latency
        self.hostApiSpecificStreamInfo = None

        if samp_format in (_portaudio.paFloat32, _portaudio.paInt32):
            depth = 32
        elif samp_format == _portaudio.paInt24:
            depth = 24
        elif samp_format == _portaudio.paInt16:
            depth = 16
        elif samp_format in (_portaudio.paInt8, _portaudio.paUInt8):
            depth = 8
        else:
            depth = 16

        self._depth = depth

        self._multiplier = channels * (depth >> 3)

    @property
    def multiplier(self) -> int:
        """Buffer multiplier.

        The number to multiply the frame count by to get the actual size of the
        buffer.
        """
        return self._multiplier

    @property
    def device_info(self) -> dict:
        """The info on the selected device."""
        return Info(_portaudio.Pa_GetDeviceInfo(self.device))

    def check(self, direction: str = 'output', rate: int = 0) -> int:
        """Check the parameters."""
        dev_info = self.device_info
        if not rate:
            rate = dev_info.defaultSampleRate
        if direction == 'output':
            result = _portaudio.Pa_IsFormatSupported(None, self, rate)
        else:
            result = _portaudio.Pa_IsFormatSupported(self, None, rate)
        if result != _portaudio.paFormatIsSupported:
            raise ValueError(f"Invalid {direction} parameters: "
                             f"{_portaudio.Pa_GetErrorText(result)}")

        return rate


class Stream(object):
    """A Portaudio stream."""

    def __init__(self, input_params: StreamParams = None,
                 output_params: StreamParams = None,
                 callback: Callable = None, flags: int = 0,
                 rate: int = 0, buffer_size: int = 0):
        """ Open a new portaudio stream.

        """

        if not input_params and not output_params:
            raise ValueError("Specify either input parameters or output "
                             "parameters or both.")

        if input_params:
            rate = input_params.check('input', rate)

        if output_params:
            rate = output_params.check('output', rate)

        if callback:
            self._pa_stream_callback = _portaudio.PaStreamCallback(
                self._pa_stream_callback_f
            )
        else:
            self._pa_stream_callback = None

        self._input_params = input_params
        self._output_params = output_params
        self._callback = callback
        self._rate = rate
        self._buffer_size = buffer_size
        self._flags = flags

        self._input_multiplier = getattr(input_params, 'multiplier', 1)

        self._stream = (_portaudio.POINTER(_portaudio.PaStream))()

    @property
    def buffer_size(self) -> int:
        """The optimal buffer size for this stream."""
        return self._buffer_size

    def open(self) -> int:
        """Opens a portaudio stream."""
        if self._pa_stream_callback:
            buffer_size = self._buffer_size
        else:
            # Jack will segfault unless this is zero.
            buffer_size = 0

        return _portaudio.Pa_OpenStream(
            _portaudio.byref(self._stream),
            self._input_params,
            self._output_params,
            self._rate,
            buffer_size,
            self._flags,
            self._pa_stream_callback,
            None
        )

    def close(self) -> int:
        """Close a portaudio stream."""
        return _portaudio.Pa_CloseStream(self._stream)

    def _pa_stream_callback_f(self, in_data: Any, out_buffer: Any,
                              frame_count: int, time_info: Any,
                              status_flags: int, user_data: Any) -> int:
        """Callback function for portaudio."""
        if in_data:
            in_str = _portaudio.string_at(
                in_data,
                frame_count * (self._input_multiplier)
            )
        else:
            in_str = b''

        data = self._callback(frame_count, in_str)

        if out_buffer and not data:
            print("Done.")
            return _portaudio.paComplete
        elif out_buffer:
            _portaudio.memmove(
                out_buffer,
                _portaudio.c_buffer(data),
                len(data)
            )

        return _portaudio.paContinue

    @property
    def active(self) -> bool:
        """Return a boolean value indecating whether the stream is active."""
        return bool(_portaudio.Pa_IsStreamActive(self._stream))

    @property
    def stopped(self) -> bool:
        """Return a boolean indecating whether the stream is stopped."""
        return bool(_portaudio.Pa_IsStreamStopped(self._stream))

    def start(self) -> Union[int, bool]:
        """Start the stream."""
        if not self.active:
            ret_val = _portaudio.Pa_StartStream(self._stream)
            if not self._callback:
                if self._output_params:
                    buffer_size = _portaudio.Pa_GetStreamWriteAvailable(
                        self._stream
                    )
                    if buffer_size < self._buffer_size:
                        self._buffer_size = buffer_size - (buffer_size % 2)
                elif self._input_params:
                    buffer_size = _portaudio.Pa_GetStreamReadAvailable(
                        self._stream
                    )
            return ret_val
        else:
            return False

    def stop(self) -> Union[int, bool]:
        """Stop an active stream."""
        if not self.stopped:
            return _portaudio.Pa_StopStream(self._stream)

        return False

    def abort(self) -> Union[int, bool]:
        """Abort the stream and drops any pending buffers."""
        if self.active:
            return _portaudio.Pa_AbortStream(self._stream)
        else:
            return False

    def write(self, data: bytes, length: int = 0) -> int:
        """Write a 'length' size buffer of data to the stream."""
        if not length:
            length = self._buffer_size

        return _portaudio.Pa_WriteStream(self._stream, data, length)

    def read(self, length: int) -> bytes:
        """Read a 'length' size buffer from the stream and returns it."""
        if not length:
            length = self._buffer_size

        read_length = length // self._input_multiplier

        data_buffer = _portaudio.create_string_buffer(length)
        _portaudio.Pa_ReadStream(self._stream, data_buffer, read_length)

        return data_buffer.raw

    def __enter__(self) -> Any:
        """Provide the ability to use pythons with statement."""
        try:
            self.open()
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Close the pcm when finished."""
        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False
