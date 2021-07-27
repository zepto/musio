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


"""A wrapper for alsaaudio to allow it to be used with the 'with' statement."""

from typing import Any

from .import_util import LazyImport
from .io_base import DevIO, io_wrapper

alsapcm = LazyImport('alsa.pcm', globals(), locals(), ['pcm'], 1)

__supported_dict = {
    'output': [bytes],
    'input': [bytes],
    'handler': 'Alsa',
    # 'default': True
    'dependencies': {
        'ctypes': ['asound'],
        'python': []
    }
}


class Alsa(DevIO):
    """File like access to Alsa devices for read and write.

    A class that provides a file like object to write to an alsa pcm object.
    """

    # Valid bit depths
    _valid_depth = (32, 24, 20, 18, 16, 8)

    # Supports reading and writing.
    _supported_modes = 'rw'

    def __init__(self, mode: str = 'w', depth: int = 16, rate: int = 44100,
                 channels: int = 2, bigendian: bool = False,
                 unsigned: bool = False, floatp: bool = False,
                 buffer_size: int = 0, latency: float = 500000,
                 device: str = 'default', three_byte: bool = False, **kwargs):
        """Initialize the alsa pcm device."""
        super(Alsa, self).__init__(mode, depth, rate, channels,
                                   bigendian, unsigned, buffer_size, latency)

        if floatp:
            pcm_format = getattr(
                alsapcm,
                f"SND_PCM_FORMAT_FLOAT_{'BE' if bigendian else 'LE'}"
            )
        elif depth in (32, 24, 16) and not three_byte:
            pcm_format = getattr(
                alsapcm,
                f"SND_PCM_FORMAT_{'U' if unsigned else 'S'}"
                f"{depth}_{'BE' if bigendian else 'LE'}"
            )
        elif depth in (24, 20, 18) and three_byte:
            pcm_format = getattr(
                alsapcm,
                f"SND_PCM_FORMAT_{'U' if unsigned else 'S'}"
                f"{depth}_{'3BE' if bigendian else '3LE'}"
            )
        elif depth == 8:
            pcm_format = getattr(
                alsapcm,
                f"SND_PCM_FORMAT_{'U' if unsigned else 'S'}{depth}"
            )
        else:
            pcm_format = alsapcm.SND_PCM_FORMAT_U16_LE

        self._three_byte = three_byte
        self._pcm_format = pcm_format
        self._soft_resample = 1
        self._frame_size = 0
        self._device = device.encode() if isinstance(device, str) else device

        self._multiplier = channels * (depth >> 3)

        self._in_pcm, self._out_pcm = self._open()

    def __repr__(self):
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(mode="{self._mode}", '
                f'depth={self._depth}, rate={self._rate}, '
                f'channels={self._channels}, bigendian={self._bigendian}, '
                f'unsigned={self._unsigned}, buffer_size={self._buffer_size}, '
                f'latency={self._latency}, device={self._device}, '
                f'three_byte={self._three_byte})')

    def _check_rc(self, rc: int, func_name: str):
        """Check the rc and handle the errors."""
        # Set the pcm based on the function name.
        pcm = self._out_pcm if func_name == 'write' else self._in_pcm

        # Get the class name for error information.
        class_name = self.__class__.__name__

        # Check for underruns
        if rc == -alsapcm.EPIPE:
            # EPIPE means underrun
            err_text = alsapcm.snd_strerror(rc).decode('utf8')
            print(f"({class_name}.{func_name}): {err_text}")

            # Try to correct for the underrun.
            # err = alsapcm.snd_pcm_prepare(pcm)
            err = alsapcm.snd_pcm_recover(pcm, rc, 1)
            if err < 0:
                # Recovery failed so raise IOError.
                raise IOError(f"({class_name}.{func_name}) Underrun recovery "
                              f"failed: "
                              f"{alsapcm.snd_strerror(err).decode('utf8')}")
            else:
                # Recovery succeeded so return 0.
                rc = 0
        elif rc < 0:
            # Raise IOError on any other error.
            raise IOError(f"({class_name}.{func_name}): "
                          f"{alsapcm.snd_strerror(rc).decode('utf8')}")

        return rc

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Write to the pcm device."""
        # The length of data.
        datalen = len(data)

        # Calculate the frame size so writei will write datalen number
        # of bytes.
        frame_size = datalen // (self._depth // (8 // self._channels))

        # Number of bytes written.
        rc = 0

        # Loop until all the data is written.
        while rc != frame_size:
            # Write the data.
            rc = alsapcm.snd_pcm_writei(
                self._out_pcm,
                data,
                alsapcm.c_ulong(frame_size)
            )

            # Check the output.
            rc = self._check_rc(rc, 'write')

            # Check that frame_size bytes were written.
            if rc > 0 and rc != frame_size:
                print(f"Write {rc} frames")

        # Return the length of the data written.
        return datalen

    @io_wrapper
    def read(self, size: int) -> bytes:
        """Read length bytes from input."""
        # Calculate the size to pass to readi so it will read size
        # number of bytes.
        read_size = size // self._frame_size

        # Create buffer to hold data.
        read_buffer = alsapcm.create_string_buffer(size)

        # The return data buffer.
        data = b''

        # Read up to size number of bytes into data.
        while len(data) < size:
            # Read data.
            rc = alsapcm.snd_pcm_readi(
                self._in_pcm,
                read_buffer,
                read_size
            )

            # Check the output.
            rc = self._check_rc(rc, 'read')

            # Append the data read to the data buffer.
            data += alsapcm.string_at(read_buffer, rc * self._frame_size)

        # Only return size number of bytes.
        return data[:size]

    def _open_pcm(self, mode: str) -> Any:
        """Return an open pcm device opened with mode."""
        # Open in blocking mode.
        pcm_mode = 0

        if 'r' in mode:
            stream_io = alsapcm.SND_PCM_STREAM_CAPTURE
        else:
            stream_io = alsapcm.SND_PCM_STREAM_PLAYBACK

        pcm = alsapcm.POINTER(alsapcm.snd_pcm_t)()

        # Open PCM device.
        rc = alsapcm.snd_pcm_open(
            alsapcm.byref(pcm),
            self._device,
            stream_io,
            pcm_mode
        )

        if rc < 0:
            raise IOError(
                f"({self.__class__.__name__}.open): "
                f"{alsapcm.snd_strerror(rc).decode('utf8')}"
            )

        if 'r' in mode:
            self._update_params(pcm)
        else:
            alsapcm.snd_pcm_set_params(
                pcm,
                self._pcm_format,
                alsapcm.SND_PCM_ACCESS_RW_INTERLEAVED,
                self._channels,
                self._rate,
                self._soft_resample,
                self._latency
            )

        return pcm

    def _open(self) -> tuple[Any, Any]:
        """Open the pcm audio output."""
        # Open the input pcm.
        in_pcm = self._open_pcm('r') if 'r' in self._mode else ()

        # Open the output pcm.
        out_pcm = self._open_pcm('w') if 'w' in self._mode else ()

        self._closed = False

        return in_pcm, out_pcm

    def close(self):
        """Close the pcm."""
        if not self.closed:
            # Let the pcm finish writing out all its data.
            alsapcm.snd_pcm_drain(self._out_pcm)

            # Close all open pcms.
            for pcm in (self._in_pcm, self._out_pcm):
                if pcm:
                    alsapcm.snd_pcm_hw_free(pcm)
                    alsapcm.snd_pcm_close(pcm)

            self._closed = True

    def _update_params(self, pcm: Any):
        """Update the alsa pcm hardware parameters."""
        params = alsapcm.POINTER(alsapcm.snd_pcm_hw_params_t)()
        alsapcm.snd_pcm_hw_params_malloc(alsapcm.byref(params))

        res = alsapcm.snd_pcm_hw_params_any(pcm, params)
        if res < 0:
            raise ValueError(alsapcm.snd_strerror(res).decode('utf8'))

        alsapcm.snd_pcm_hw_params_set_access(
            pcm, params, alsapcm.SND_PCM_ACCESS_RW_INTERLEAVED)

        alsapcm.snd_pcm_hw_params_set_format(pcm, params, self._pcm_format)
        alsapcm.snd_pcm_hw_params_set_channels(pcm, params, self._channels)
        alsapcm.snd_pcm_hw_params_set_rate(pcm, params, self._rate, 0)
        alsapcm.snd_pcm_hw_params_set_period_size(
            pcm, params, self._buffer_size, 0)
        alsapcm.snd_pcm_hw_params_set_periods(pcm, params, 4, 0)

        alsapcm.snd_pcm_hw_params(pcm, params)

        alsapcm.snd_pcm_hw_params_current(pcm, params)

        val = alsapcm.c_uint()

        alsapcm.snd_pcm_hw_params_get_channels(params, alsapcm.byref(val))
        self._channels = val.value

        alsapcm.snd_pcm_hw_params_get_rate(
            params, alsapcm.byref(val), alsapcm.c_int(0))
        self._rate = val.value

        val = alsapcm.c_ulong()

        alsapcm.snd_pcm_hw_params_get_period_size(
            params, alsapcm.byref(val), alsapcm.c_int(0))
        self._period_size = val.value

        fmt = alsapcm.snd_pcm_format_t()
        alsapcm.snd_pcm_hw_params_get_format(params, alsapcm.byref(fmt))
        self._format = fmt.value

        self._frame_size = self._channels * \
            alsapcm.snd_pcm_hw_params_get_sbits(params) // 8

        alsapcm.snd_pcm_hw_params_free(params)
