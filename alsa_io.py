#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Provides a thin wrapper for alsaaudio to allow for easy access, and
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


""" A wrapper for alsaaudio to allow it to be used with the 'with' statement.

"""

import alsa.pcm as alsapcm

from io_base import DevIO, io_wrapper, OnDemand

alsapcm = OnDemand('alsa.pcm', globals(), locals(), ['pcm'], 0)

__supported_dict = {
        'output': [bytes],
        'input': [bytes],
        'handler': 'Alsa',
        # 'default': True
        }


class Alsa(DevIO):
    """ A class that provides a file like object to write to an alsa pcm
    object.

    """

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, buffer_size=None,
                 latency=500000, device=b'default', **kwargs):
        """ Alsa(mode='w', depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None, latency=500000, device=b'default',
        **kwargs) -> Initialize the alsa pcm device.

        """

        super(Alsa, self).__init__(mode, depth, rate, channels, bigendian,
                                   unsigned, buffer_size, latency)

        if depth in (32, 16):
            pcm_format = getattr(alsapcm, 'SND_PCM_FORMAT_%s%s_%s' % \
                                       ('U' if unsigned else 'S',
                                        depth, 
                                        'BE' if bigendian else 'LE'))
        elif depth == 8:
            pcm_format = getattr(alsapcm, 'SND_PCM_FORMAT_%s%s' % \
                                       ('U' if unsigned else 'S', depth))
        else:
            pcm_format = alsapcm.SND_PCM_FORMAT_U16_LE

        self._pcm_format = pcm_format
        self._soft_resample = 1
        self._frame_size = 0
        self._device = device

        self._multiplier = channels * (depth >> 3)

        self._pcm = self._open()

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s, buffer_size=%(_buffer_size)s, latency=%(_latency)s, device=%(_device)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        datalen = len(data)

        # Calculate the frame size.
        frame_size = datalen // (self._depth // (8 // self._channels))

        # print(alsapcm.snd_pcm_state_name(alsapcm.snd_pcm_state(self._pcm)))
        rc = alsapcm.snd_pcm_writei(self._pcm, data,
                                    alsapcm.c_ulong(frame_size))

        if rc == -alsapcm.EPIPE:
            # EPIPE means underrun
            # Try to correct for the underrun.
            err = alsapcm.snd_pcm_prepare(self._pcm)
            if err < 0:
                print("Can't recover from underrun prepare failed: %s\n",
                        alsapcm.snd_strerror(err).decode('utf8'))
            return err
        elif rc < 0:
            print(alsapcm.snd_strerror(rc).decode('utf8'))
        elif rc != frame_size:
            print("Write %d frames" % rc)

        # Return the length of the data written.
        return datalen

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=0) -> Read length bytes from input.

        """

        # Corrected size based on frame_size.
        read_size = size // self._frame_size

        # Create buffer to hold data.
        read_buffer = alsapcm.create_string_buffer(size)

        # Read data.
        rc = alsapcm.snd_pcm_readi(self._pcm, read_buffer, read_size)

        if rc == -alsapcm.EPIPE:
            # EPIPE means underrun
            err_text = alsapcm.snd_strerror(rc).decode('utf8')
            print('%s: %s' % (__name__, err_text))

            # Correct for underrun.
            err = alsapcm.snd_pcm_prepare(self._pcm)

            if err < 0:
                # Correcting failed.
                raise IOError(
                        "Can't recover from underrun prepare failed: %s\n",
                        alsapcm.snd_strerror(err).decode('utf8')
                        )
            else:
                rc = 0
        elif rc < 0:
            raise IOError(alsapcm.snd_strerror(rc).decode('utf8'))

        return alsapcm.string_at(read_buffer, rc * self._frame_size)

    def _open(self):
        """ open -> Open the pcm audio output.

        """

        if 'r' in self._mode:
            stream_io = alsapcm.SND_PCM_STREAM_CAPTURE
            pcm_mode = 0 #alsapcm.SND_PCM_NONBLOCK
        else:
            stream_io = alsapcm.SND_PCM_STREAM_PLAYBACK
            pcm_mode = 0

        pcm = alsapcm.POINTER(alsapcm.snd_pcm_t)()

        # Open PCM device.
        rc = alsapcm.snd_pcm_open(alsapcm.byref(pcm), self._device,
                                  stream_io, pcm_mode)

        if rc < 0:
            raise IOError(alsapcm.snd_strerror(rc).decode('utf8'))
            return None

        if 'w' in self._mode:
            alsapcm.snd_pcm_set_params(pcm, self._pcm_format,
                                    alsapcm.SND_PCM_ACCESS_RW_INTERLEAVED,
                                    self._channels,
                                    self._rate,
                                    self._soft_resample, self._latency)
        else:
            self._update_params(pcm)

        self._closed = False

        return pcm

    def close(self):
        """ close -> Close the pcm.

        """

        if not self.closed:
            alsapcm.snd_pcm_hw_free(self._pcm)
            alsapcm.snd_pcm_close(self._pcm)

            self._closed = True

    def _update_params(self, pcm):
        """ _set_params(pcm) -> Set the alsa pcm hardware parameters.

        """

        params = alsapcm.POINTER(alsapcm.snd_pcm_hw_params_t)()
        alsapcm.snd_pcm_hw_params_malloc(alsapcm.byref(params))

        res = alsapcm.snd_pcm_hw_params_any(pcm, params)
        if res < 0:
            raise ValueError(alsapcm.snd_strerror(res).decode('utf8'))

        alsapcm.snd_pcm_hw_params_set_access(pcm, params,
                alsapcm.SND_PCM_ACCESS_RW_INTERLEAVED)

        alsapcm.snd_pcm_hw_params_set_format(pcm, params, self._pcm_format)
        alsapcm.snd_pcm_hw_params_set_channels(pcm, params, self._channels)
        alsapcm.snd_pcm_hw_params_set_rate(pcm, params, self._rate, 0)
        alsapcm.snd_pcm_hw_params_set_period_size(pcm, params,
                                                  self._buffer_size, 0)
        alsapcm.snd_pcm_hw_params_set_periods(pcm, params, 4, 0)

        alsapcm.snd_pcm_hw_params(pcm, params)

        alsapcm.snd_pcm_hw_params_current(pcm, params)

        val = alsapcm.c_uint()

        alsapcm.snd_pcm_hw_params_get_channels(params, alsapcm.byref(val))
        self._channels = val.value

        alsapcm.snd_pcm_hw_params_get_rate(params, alsapcm.byref(val),
                                           alsapcm.c_long(0))
        self._rate = val.value

        alsapcm.snd_pcm_hw_params_get_period_size(params, alsapcm.byref(val),
                                                  alsapcm.c_long(0))
        self._period_size = val.value

        fmt = alsapcm.snd_pcm_format_t()
        alsapcm.snd_pcm_hw_params_get_format(params, alsapcm.byref(fmt))
        self._format = fmt.value

        self._frame_size = self._channels * \
                alsapcm.snd_pcm_hw_params_get_sbits(params) // 8

        alsapcm.snd_pcm_hw_params_free(params)
