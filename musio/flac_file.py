#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of FLAC files.
# Copyright (C) 2015 Josiah Gordon <josiahg@gmail.com>
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


""" A module for reading FLAC files.

"""

from itertools import compress, cycle
from array import array

from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

from .import_util import LazyImport

_flac = LazyImport('flac.flac', globals(), locals(), ['flac'], 1)

__supported_dict = {
    'ext': ['.flac'],
    'handler': 'FlacFile',
    'dependencies': {
        'ctypes': ['FLAC'],
        'python': []
    }
}

class FlacFile(AudioIO):
    """ A file like object for reading media files with ffmpeg.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, **kwargs):
        """ FlacFile(filename, depth=16, rate=44100, channels=2) ->
        Initialize the playback settings of the player.

        """

        super(FlacFile, self).__init__(filename, 'r', depth, rate, channels)

        self._total_samples = 0
        self._decoder = None
        self._data_buffer = b''
        self._position = 0

        self._info_dict.update(self._update_info(filename))

        # Setup the decoder callbacks.
        self._write_callback = _flac.FLAC__StreamDecoderWriteCallback(self._write_status)
        self._metadata_callback = _flac.FLAC__StreamDecoderMetadataCallback(self._metadata_status)
        self._error_callback = _flac.FLAC__StreamDecoderErrorCallback(self._error_status)

        self._decoder = self._open(filename)
        if self._decoder:
            self._closed = False
        else:
            raise(OSError("Failed to open FLAC: %s." % filename))

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return self._position

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _flac.FLAC__stream_decoder_seek_absolute(self._decoder, position)

    def _update_info(self, filename):
        """ Updates the id3 info for the opened flac.

        """

        info_dict = {}
        metadata = _flac.POINTER(_flac.FLAC__StreamMetadata)()
        filename_b = filename.encode('utf-8', 'surrogateescape')
        if _flac.FLAC__metadata_get_tags(filename_b, _flac.byref(metadata)):
            for i in metadata.contents.data.vorbis_comment.comments:
                length = i.length
                entry = i.entry
                entry_s = _flac.string_at(entry, length)
                if not entry_s: break
                name, value = entry_s.decode('utf-8', 'replace').split('=')
                info_dict[name.lower()] = value

        return info_dict

    def _open(self, filename):
        """ Open a flac file.

        """

        try:
            # Convert filename to bytes.
            filename = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            pass

        decoder = _flac.FLAC__stream_decoder_new()

        init = _flac.FLAC__stream_decoder_init_file(decoder, filename,
                                                    self._write_callback,
                                                    self._metadata_callback,
                                                    self._error_callback,
                                                    None)

        if init != _flac.FLAC__STREAM_DECODER_INIT_STATUS_OK:
            msg_out(_flac.FLAC__StreamDecoderInitStatusString(init))
            return None

        # Decode the first sample to get the metadata
        _flac.FLAC__stream_decoder_process_single(decoder)

        return decoder

    def close(self):
        """ Close and finish the flac decoder.

        """

        if not self.closed and self._decoder:
            _flac.FLAC__stream_decoder_finish(self._decoder)
            _flac.FLAC__stream_decoder_delete(self._decoder)

            self._closed = True
            self._decoder = None

    def _write_status(self, decoder, frame, buf, client_data):
        """ write_status callback function  Called when the decoder has decoded
        a sample from the flac file.

        """

        channels = frame.contents.header.channels
        size = frame.contents.header.blocksize
        depth = frame.contents.header.bits_per_sample
        rate = frame.contents.header.sample_rate
        size = frame.contents.header.blocksize

        # Only 1 and 2 channels are supported.
        if channels > 2:
            return _flac.FLAC__STREAM_DECODER_WRITE_STATUS_ABORT

        if depth == 16:
            data = array('h', bytearray((size * channels) * 2))
        elif depth == 24:
            data = array('i', bytearray((size * channels) * 4))
        elif depth == 8:
            data = array('b', bytearray(size * channels))
        else:
            return _flac.FLAC__STREAM_DECODER_WRITE_STATUS_ABORT

        # Compute the sample size
        sample_size = size * channels

        # Interleave the data.
        for i in range(size):
            for j in range(channels):
                data[i * channels + j] = buf[j][i]

        data = bytearray(data)

        if depth == 24:
            # Discard every 4th byte to make 3-byte 24-bit.
            data = compress(data, cycle([1,1,1,0]))
            data = bytes(data)[:sample_size * 3]
        else:
            data = bytes(data)

        # Update the position
        self._position = frame.contents.header.number.sample_number

        self._data_buffer += data

        return _flac.FLAC__STREAM_DECODER_WRITE_STATUS_CONTINUE

    def _metadata_status(self, decoder, metadata, client_data):
        """ metadata callback  Called when the decoder is initialized.

        """

        self._channels = metadata.contents.data.stream_info.channels
        self._rate = metadata.contents.data.stream_info.sample_rate
        self._total_samples = metadata.contents.data.stream_info.total_samples
        self._depth = metadata.contents.data.stream_info.bits_per_sample
        self._length = self._total_samples

        if self._depth == 24:
            self.three_byte = True

    def _error_status(self, decoder, error_status, client_data):
        """ Error callback  Called when the decoder encounters an error.

        """

        msg_out('An error occured in flac_file: %s' % error_status)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        while len(self._data_buffer) < size:
            # Get the current decoder state.
            decode_state = _flac.FLAC__stream_decoder_get_state(self._decoder)

            # Check for the end of the stream.
            if decode_state == _flac.FLAC__STREAM_DECODER_END_OF_STREAM:
                # Get the last sample so we can pad it for output.
                data = self._data_buffer
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                else:
                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1
                    self.seek(0)
                break
            else:
                # Decode the next sample.
                _flac.FLAC__stream_decoder_process_single(self._decoder)


        data = self._data_buffer[:size]
        self._data_buffer =  self._data_buffer[size:]

        return data
