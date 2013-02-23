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


""" Portaudio module.

"""

from ._portaudio import *

class Info(object):
    """ An info class.

    """

    def __init__(self, info_struct):
        """ Info(info_struct) -> Wrap a struct to make it easier to access.

        """

        for key, val in info_struct.contents._fields_:
            setattr(self, key, getattr(info_struct.contents, key))


class Portaudio(object):
    """ A portaudio object that can be used with the 'with' statement
    to initialize and terminate portaudio.  Portaudio has to be initialized
    before any portaudio functions are called.

    """

    def initialize(self):
        """ Initialize portaudio.  Has to be called first.

        """

        return Pa_Initialize()

    def terminate(self):
        """ Terminate portaudio.

        """

        return Pa_Terminate()

    @property
    def device_count(self):
        """ The number of valid devices available.

        """

        return Pa_GetDeviceCount()

    def device_name(self, devindex):
        """ The name if the device at index 'devindex.'

        """

        try:
            return Pa_GetDeviceInfo(devindex).contents.name.decode()
        except Exception as err:
            return None

    @property
    def default_output_device(self):
        """ The index of the default output device.

        """

        return Pa_GetDefaultOutputDevice()

    @property
    def default_input_device(self):
        """ The index of the default input device.

        """

        return Pa_GetDefaultInputDevice()

    @property
    def api_count(self):
        """ The number of valid host apis.

        """

        return Pa_GetHostApiCount()

    @property
    def default_api(self):
        """ The index of the default host api.

        """

        return Pa_GetDefaultHostApi()

    def __enter__(self):
        """ Provides the ability to use pythons with statement.

        """

        try:
            self.initialize()
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """ Close the pcm when finished.

        """

        try:
            self.terminate()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False


class StreamParams(PaStreamParameters):
    """ Portaudio stream parameters wrapper class.

    """

    def __init__(self, device_index=0, channels=2, samp_format=paInt16,
            latency=500000):
        """ StreamParams(device_index=1, channels=2, samp_format=paInt16,
        latency=500000) -> Create a parameter object.  Use when creating
        a stream.

        """

        max_dev_index = Pa_GetDeviceCount()
        if device_index not in range(max_dev_index):
            print("Invalid device, should be 0-%s.  Using default." % \
                    (max_dev_index - 1))
            device_index = Pa_GetDefaultOutputDevice()

        super(StreamParams, self).__init__()

        self.device = device_index
        self.channelCount = channels
        self.sampleFormat = samp_format
        self.suggestedLatency = latency
        self.hostApiSpecificStreamInfo = None

        if samp_format in (paFloat32, paInt32):
            depth = 32
        elif samp_format == paInt24:
            depth = 24
        elif samp_format == paInt16:
            depth = 16
        elif samp_format in (paInt8, paUInt8):
            depth = 8
        else:
            depth = 16

        self._depth = depth

        self._multiplier = channels * (depth >> 3)

    @property
    def multiplier(self):
        """ The number to multiplay the frame count by to get the
        actual size of the buffer.

        """

        return self._multiplier

    @property
    def device_info(self):
        """ The info on the selected device.

        """

        return Info(Pa_GetDeviceInfo(self.device))

    def check(self, direction='output', rate=None):
        """ check(direction='output', rate=None) -> Check the parameters.

        """

        dev_info = self.device_info
        if not rate:
            rate = dev_info.defaultSampleRate
        if direction == 'output':
            result = Pa_IsFormatSupported(None, self, rate)
        else:
            result = Pa_IsFormatSupported(self, None, rate)
        if result != paFormatIsSupported:
            raise ValueError("Invalid %s parameters: %s" % (direction, Pa_GetErrorText(result)))

        return rate


class Stream(object):
    """ A Portaudio stream.

    """

    def __init__(self, input_params=None, output_params=None, callback=None, 
            flags=0, rate=None, buffer_size=0):
        """ Open a new portaudio stream.

        """

        if not input_params and not output_params:
            raise ValueError("Specify either input parameters or output parameters or both.")

        if input_params:
            rate = input_params.check('input', rate)

        if output_params:
            rate = output_params.check('output', rate)

        if callback:
            self._pa_stream_callback = PaStreamCallback(self._pa_stream_callback_f)
        else:
            self._pa_stream_callback = None

        self._input_params = input_params
        self._output_params = output_params
        self._callback = callback
        self._rate = rate
        self._buffer_size = buffer_size
        self._flags = flags

        self._input_multiplier = getattr(input_params, 'multiplier', 1)

        self._stream = (POINTER(PaStream))()

    @property
    def buffer_size(self):
        """ The optimal buffer size for this stream

        """

        return self._buffer_size

    def open(self):
        """ Opens a portaudio stream.

        """

        if self._pa_stream_callback:
            buffer_size = self._buffer_size
        else:
            # Jack will segfault unless this is zero.
            buffer_size = 0

        return Pa_OpenStream(byref(self._stream), self._input_params,
                             self._output_params, self._rate,
                             buffer_size, self._flags,
                             self._pa_stream_callback, None)

    def close(self):
        """ Closes a portaudio stream.

        """

        return Pa_CloseStream(self._stream)

    def _pa_stream_callback_f(self, in_data, out_buffer, frame_count,
                              time_info, status_flags, user_data):
        """ The stream callback.

        """

        if in_data:
            in_str = string_at(in_data, frame_count * (self._input_multiplier))
        else:
            in_str = b''

        data = self._callback(frame_count, in_str)

        if out_buffer and not data:
            print("Done.")
            return paComplete
        elif out_buffer:
            memmove(out_buffer, c_buffer(data), len(data))

        return paContinue

    @property
    def active(self):
        """ Returns a boolean value indecating whether the stream is active.

        """

        return bool(Pa_IsStreamActive(self._stream))

    @property
    def stopped(self):
        """ Returns a boolean indecating whether the stream is stopped.

        """

        return bool(Pa_IsStreamStopped(self._stream))

    def start(self):
        """ Starts the stream.

        """

        if not self.active:
            ret_val = Pa_StartStream(self._stream)
            if not self._callback:
                if self._output_params:
                    buffer_size = Pa_GetStreamWriteAvailable(self._stream)
                    if buffer_size < self._buffer_size:
                        self._buffer_size = buffer_size - (buffer_size % 2)
                elif self._input_params:
                    buffer_size = Pa_GetStreamReadAvailable(self._stream)
            return ret_val
        else:
            return False

    def stop(self):
        """ Stops an active stream.

        """

        if not self.stopped:
            return Pa_StopStream(self._stream)

        return False

    def abort(self):
        """ Aborts the stream and drops any pending buffers.

        """

        if self.active:
            return Pa_AbortStream(self._stream)
        else:
            return False

    def write(self, data, length=None):
        """ write(data, length) -> Write a 'length' size buffer of data to
        the stream.

        """

        if not length:
            length = self._buffer_size

        return Pa_WriteStream(self._stream, data, length)

    def read(self, length):
        """ read(length) -> Read a 'length' size buffer from the stream
        and returns it.

        """

        if not length:
            length = self._buffer_size

        read_length = length // self._input_multiplier

        data_buffer = create_string_buffer(length)
        Pa_ReadStream(self._stream, data_buffer, read_length)

        return data_buffer.raw

    def __enter__(self):
        """ Provides the ability to use pythons with statement.

        """

        try:
            self.open()
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """ Close the pcm when finished.

        """

        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False
