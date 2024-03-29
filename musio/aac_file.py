#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading aac audio files.
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


"""A module for reading aac audio files."""

from os.path import getsize
from typing import Any, BinaryIO

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper

_neaacdec = LazyImport('faad._neaacdec', globals(), locals(), ['_neaacdec'], 1)

__supported_dict = {
    'ext': ['.aac'],
    'handler': 'AACFile',
    'dependencies': {
        'ctypes': ['faad'],
        'python': []
    }
}


def bytes_to_pointer(data_type: Any, data: bytes) -> Any:
    """Return a ctypes pointer to a copy of data."""
    # Create a len(data) length pointer of type data_type.
    c_pointer = data_type * len(data)
    # Return a copy of cata in c_pointer.
    return c_pointer.from_buffer_copy(data)


class AACDecoder:
    """An object to decode AAC audio data."""

    def __init__(self, init_buf: Any, init_size: int, depth: int = 16,
                 stereo: bool = True, mp4: bool = False):
        """Initialize class variables."""
        # Use different init for mp4 files and aac files.
        if mp4:
            self._init = _neaacdec.NeAACDecInit2
        else:
            self._init = _neaacdec.NeAACDecInit

        if depth in [16, 24, 32]:
            out_format = getattr(_neaacdec, f'FAAD_FMT_{depth}BIT')
            self._depth = depth
        else:
            out_format = _neaacdec.FAAD_FMT_16BIT
            self._depth = 16

        self._out_format = out_format

        self._channels = 2
        self._rate = 44100
        self._stereo = stereo

        self._frame_info = _neaacdec.NeAACDecFrameInfo()

        self._min_stream_size = _neaacdec.FAAD_MIN_STREAMSIZE

        # Open the file.
        self._decoder = self._open(init_buf, init_size)

    @property
    def bytesconsumed(self) -> int:
        """Return the number of bytes consumed."""
        if not self._frame_info:
            return 0

        return self._frame_info.bytesconsumed

    @property
    def min_stream_size(self) -> int:
        """Return the minimum size of a stream."""
        return self._min_stream_size

    @property
    def rate(self) -> int:
        """Return the sample rate of the aac."""
        return self._rate

    @property
    def channels(self) -> int:
        """Return the number of channels."""
        return self._channels

    @property
    def depth(self) -> int:
        """Return the bit depth the aac."""
        return self._depth

    def _open(self, init_buf: Any, init_size: int) -> Any:
        """Open and configure the aac decoder."""
        # Open the decoder.
        decoder = _neaacdec.NeAACDecOpen()

        # Get the current configuration.
        decoder_conf = _neaacdec.NeAACDecGetCurrentConfiguration(decoder)

        # Set the requested output format.
        decoder_conf.contents.outputFormat = self._out_format

        # If stereo is set set downMatrix to 1 else 0
        decoder_conf.contents.downMatrix = int(self._stereo)

        # Upsample Implicit SBR?
        decoder_conf.contents.dontUpSampleImplicitSBR = 0

        # Setup the configuration we want.
        _neaacdec.NeAACDecSetConfiguration(decoder, decoder_conf)

        rate = _neaacdec.c_ulong(0)
        channels = _neaacdec.c_ubyte(0)

        # Initialize the decoder and get the sample rate and channel
        # count.
        _ = self._init(decoder, init_buf, init_size,
                       _neaacdec.byref(rate), _neaacdec.byref(channels))

        self._rate = rate.value
        self._channels = channels.value

        return decoder

    def close(self):
        """Close the aac decoder."""
        if self._decoder:
            _neaacdec.NeAACDecClose(self._decoder)

        self._decoder = None
        del(self._frame_info)

    def decode(self, data: bytes, data_size: int) -> bytes:
        """Return raw audio data decoded from 'data'.

        data must be of type _neaacdec.POINTER(ctypes._neaacdec.c_ubyte)
        data_size must be of type ctypes.c_uint32
        """
        frame_info = self._frame_info

        try:
            # Try to decode the next frame.
            sample_buffer = _neaacdec.NeAACDecDecode(
                self._decoder, _neaacdec.byref(frame_info), data, data_size
            )

            # Check for errors.
            err = _neaacdec.NeAACDecGetErrorMessage(frame_info.error)

            # Raise an error if no data was consumed.
            if not sample_buffer or frame_info.bytesconsumed <= 0:
                raise BufferError(err.decode())
            elif frame_info.error != 0:
                raise BufferError(err.decode())
            elif frame_info.samples <= 0:
                return b''
            else:
                # Process the decoded data.

                # Calculate the number of bytes read.
                bytes_read = frame_info.samples * \
                    _neaacdec.sizeof(_neaacdec.c_short)

                # Put the data in a buffer and return it.
                byte_buffer = _neaacdec.string_at(sample_buffer, bytes_read)
                return byte_buffer

        except BufferError as err:
            # Catch the errors that we raised and print a message about
            # them.
            print(f"Error decoding data: {err}")
            return b''


class AACFile(AudioIO):
    """File like object for reading aacs."""

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, depth: int = 16, rate: int = 44100,
                 channels: int = 2, **kwargs):
        """Initialize the playback settings of the player."""
        super(AACFile, self).__init__(filename, 'r', depth, rate, channels)

        self._info_dict['name'] = filename

        self._aac_file, self._aac_decoder = self._open(filename)

        self._data = b''

    def _set_position(self, position: int):
        """Change the position of playback."""
        r_size = self._aac_decoder.min_stream_size
        position += -r_size if position > self.position else r_size
        self._aac_file.seek(position)

    def _get_position(self) -> int:
        """Update the position variable."""
        # Update the position.
        return self._aac_file.tell()

    def _open(self, filename: str) -> tuple[BinaryIO, AACDecoder]:
        """Load the specified file."""
        aac_file = open(filename, 'rb', buffering=0)

        self._length = getsize(filename.encode('utf-8', 'surrogateescape'))

        # Read the first 4 bytes from the file, so we can get the
        # channel count, depth, and sample rate of the file.
        data_size = 4
        data = aac_file.read(data_size)

        # Make init_size a ctypes c_ulong.
        data_size = _neaacdec.c_ulong(data_size)

        # Cast the data to a C pointer to use in the decoder.
        data_p = bytes_to_pointer(_neaacdec.c_ubyte, data)

        # Seek back to the start.
        aac_file.seek(0)

        aac_decoder = AACDecoder(data_p, data_size)

        self._channels = aac_decoder.channels
        self._rate = aac_decoder.rate
        self._depth = aac_decoder.depth

        self._closed = False

        return aac_file, aac_decoder

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it."""
        # Start with any leftover data from the last read.
        data = self._data

        encoded_data = b''

        r_size = (size + 1) + self._aac_decoder.min_stream_size

        while len(data) < size:
            # Read aac encoded data from the file.
            encoded_data += self._aac_file.read(r_size)

            if len(encoded_data) == 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    self._loop_count += 1
                    self.seek(0)

                    # Reset the read size
                    r_size = (size + 1) + self._aac_decoder.min_stream_size

                    continue

            # Decode into a temporary buffer.
            temp_data = self._aac_decoder.decode(
                # Cast the bytes object to a type POINTER(ctypes.c_ubyte).
                bytes_to_pointer(_neaacdec.c_ubyte, encoded_data),
                len(encoded_data)
            )

            # Only read the number of bytes used so we keep the buffer at one
            # size.
            r_size = self._aac_decoder.bytesconsumed

            # Remove the number of bytes not used.
            encoded_data = encoded_data[r_size:]

            # Append the data to the buffer.
            data += temp_data

        if len(encoded_data) > 0:
            # Seek back the bytes that were not used so we can read them again
            # the next time.
            self._aac_file.seek(-len(encoded_data), 1)

        # Store extra data for next read.
        self._data = data[size:]

        # Make sure we return only the number of bytes requested.
        return data[:size]

    def close(self):
        """Close and cleans up."""
        if not self.closed:
            self._aac_file.close()
            self._aac_decoder.close()

            del(self._aac_file)

            self._closed = True
