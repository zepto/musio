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


""" A module for reading aac audio files.

"""

from os.path import getsize as os_getsize

from io_base import AudioIO, OnDemand, io_wrapper

_neaacdec = OnDemand('faad._neaacdec', globals(), locals(), ['_neaacdec'], 0)

__supported_dict= {
        'ext': ['.aac'],
        'handler': 'AACFile'
        }


class AACDecoder(object):
    """ An object to decode AAC audio data.

    """

    def __init__(self, init_buf, init_size, depth=16, stereo=True):
        """ Initialize class variables.

        """

        if depth in [16, 24, 32]:
            out_format = getattr(_neaacdec, 'FAAD_FMT_%sBIT' % depth)
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
    def bytesconsumed(self):
        """ The number of bytes consumed in the last decoding operation.

        """

        if not self._frame_info:
            return 0

        return self._frame_info.bytesconsumed

    @property
    def min_stream_size(self):
        """ The minimum size of a stream.

        """

        return self._min_stream_size

    @property
    def rate(self):
        """ The sample rate of the aac.

        """

        return self._rate

    @property
    def channels(self):
        """ The number of channels.

        """

        return self._channels

    @property
    def depth(self):
        """ The bit depth the aac.

        """

        return self._depth

    def _open(self, init_buf, init_size):
        """ Open and configure the aac decoder.

        """

        # Only send ctypes type POINTER(c_ubyte) to the method.
        if type(init_buf) == bytes:
            # Cast the data to a C pointer to use in the decoder.
            init_buf = _neaacdec.cast(init_buf,
                                      _neaacdec.POINTER(_neaacdec.c_ubyte))

        # Make init_size a ctypes c_ulong.
        if type(init_size) == int:
                init_size = _neaacdec.c_ulong(init_size)

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
        ret = _neaacdec.NeAACDecInit(decoder, init_buf, init_size,
                                     _neaacdec.byref(rate),
                                     _neaacdec.byref(channels))

        self._rate = rate.value
        self._channels = channels.value

        return decoder

    def close(self):
        """ Close the aac decoder.

        """

        if self._decoder:
            _neaacdec.NeAACDecClose(self._decoder)

        self._decoder = None
        self._frame_info = None

    def decode(self, data, data_size):
        """ Return raw audio data decoded from 'data.'

        data must be of type _neaacdec.POINTER(ctypes._neaacdec.c_ubyte)
        data_size must be of type ctypes.c_uint32

        """

        frame_info = self._frame_info

        data_size = data_size if type(data_size) == int else data_size.value

        try:
            # Try to decode the next frame.
            sample_buffer = _neaacdec.NeAACDecDecode(self._decoder,
                                                     _neaacdec.byref(frame_info),
                                                     data, data_size)

            # Check for errors.
            err = _neaacdec.NeAACDecGetErrorMessage(frame_info.error)

            # Raise an error if not data was consumed.
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
            print("Error decoding data: %s" % err)
            return b''


class AACFile(AudioIO):
    """ A file like object for reading aacs.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, **kwargs):
        """ AACFile(filename, depth=16, rate=44100, channels=2) -> Initialize
        the playback settings of the player.

        """

        super(AACFile, self).__init__(filename, 'r', depth, rate, channels)

        self._info_dict['name'] = filename

        self._aac_file = None
        self._aac_decoder = self._open(filename)

        self._data = b''

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._aac_file.seek(position)

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return self._aac_file.tell()

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        self._aac_file = open(filename, 'rb', buffering=0)

        self._length = os_getsize(filename.encode())

        # Read the first 4 bytes from the file, so we can get the
        # channel count, depth, and sample rate of the file.
        data_size = 4
        data = self._aac_file.read(data_size)

        # Seek back to the start.
        self._aac_file.seek(0)

        aac_decoder = AACDecoder(data, data_size)

        self._channels = aac_decoder.channels
        self._rate = aac_decoder.rate
        self._depth = aac_decoder.depth

        self._closed = False

        return aac_decoder

    @io_wrapper
    def read(self, size):
        """ read(size) -> Reads size amount of data and returns it.

        """

        # Start with any leftover data from the last read.
        data = self._data

        encoded_data = b''

        r_size = self._aac_decoder.min_stream_size

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
                    continue

            # Cast the bytes object to a type POINTER(ctypes.c_ubyte).
            encoded_ubytes = _neaacdec.cast(encoded_data,
                                  _neaacdec.POINTER(_neaacdec.c_ubyte))

            # Decode into a temporary buffer.
            temp_data = self._aac_decoder.decode(encoded_ubytes,
                                                 len(encoded_data))

            # Remove the number of bytes not used.
            encoded_data = encoded_data[self._aac_decoder.bytesconsumed:]

            # Only read the number of bytes used so we keep the buffer at one
            # size.
            r_size = self._aac_decoder.bytesconsumed

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
        """ close -> Closes and cleans up.

        """

        try:
            self._aac_file.close()
            self._aac_decoder.close()

            self._aac_file = None

            self._closed = True

            return True
        except:
            return False

