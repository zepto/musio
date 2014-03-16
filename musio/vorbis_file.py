#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of ogg vorbis files.
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


""" A module for reading ogg vorbis files.

"""

from os.path import isfile as os_isfile
from array import array

from .io_base import AudioIO, io_wrapper
from .io_util import slice_buffer
# from .ogg import vorbisfile as _vorbisfile
# from .ogg import vorbisenc as _vorbisenc
from .import_util import LazyImport

_vorbisfile = LazyImport('ogg.vorbisfile', globals(), locals(),
                         ['_vorbisfile'], 1)
_vorbisenc = LazyImport('ogg.vorbisenc_wrapper', globals(), locals(),
                        ['vorbisenc_wrapper'], 1)

__supported_dict = {
    'ext': ['.ogg', '.ogv'],
    'handler': 'VorbisFile',
    'dependencies': {
        'ctypes': ['vorbis', 'vorbisenc', 'vorbisfile', 'ogg'],
        'python': []
    }
}


class VorbisFile(AudioIO):
    """ Read and write ogg vorbis files.

    """

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Both reading and writing are supported
    _supported_modes = 'rw'

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, quality=.5, comment_dict={},
                 **kwargs):
        """ VorbisFile(filename, mode='r', depth=16, channels=2,
        bigendian=False, unsigned=False,) -> Initialize the file object for
        reading and writing.

        """

        super(VorbisFile, self).__init__(filename=filename, mode=mode,
                                         depth=depth, rate=rate,
                                         channels=channels)

        self._signed = not unsigned
        self._unsigned = unsigned
        self._bigendian = bigendian

        if mode == 'r':
            if not os_isfile(filename):
                raise OSError("File not found: %s" % filename)

            self._vorbis_file = self._read_open(filename)

            file_pointer = _vorbisfile.pointer(self._vorbis_file)
            self._length = _vorbisfile.ov_pcm_total(file_pointer, -1)

            self._data = b''
        else:
            self._quality = quality
            self._comment_dict = comment_dict
            self._info_dict.update(self._comment_dict)

            self._stream_state = _vorbisenc.OggStreamState()
            self._page = _vorbisenc.OggPage()
            self._packet = _vorbisenc.OggPacket()

            self._info = _vorbisenc.VorbisInfo()
            self._comment = _vorbisenc.VorbisComment()

            self._comment.update(comment_dict)

            self._dsp_state = _vorbisenc.DspState()
            self._block = _vorbisenc.VorbisBlock()

            self._vorbis_file = self._write_open(filename)

    def close(self):
        """ close -> Closes and cleans up.

        """

        if self._mode == 'r':
            self._read_close()
        else:
            self._write_close()

    def to_seconds(self, position):
        """ Convert the provided position/length to seconds.

        """

        return position / self._rate

    def _set_position(self, position):
        """ Change the position of playback.

        """

        file_pointer = _vorbisfile.pointer(self._vorbis_file)

        if _vorbisfile.ov_seekable(file_pointer):
            _vorbisfile.ov_pcm_seek_lap(file_pointer, position)

    def _get_position(self):
        """ Updates the position variable.

        """

        file_pointer = _vorbisfile.pointer(self._vorbis_file)

        # Update the position.
        return _vorbisfile.ov_pcm_tell(file_pointer)

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        if self._mode == 'r':
            repr_str = "filename='%(_filename)s', mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s" % self
        else:
            repr_str = "filename='%(_filename)s', mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, quality=%(_quality)s, comment_dict=%(_comment_dict)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _read_open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        vorbis_file = _vorbisfile.OggVorbis_File()

        filename = filename.encode('utf-8', 'surrogateescape')

        if _vorbisfile.ov_fopen(filename, _vorbisfile.byref(vorbis_file)) < 0:
            raise IOError('Error opening file: %s' % filename)

        comments = _vorbisfile.ov_comment(_vorbisfile.byref(vorbis_file), -1)
        info = _vorbisfile.ov_info(_vorbisfile.byref(vorbis_file), -1)

        self._channels = info.contents.channels
        self._rate = info.contents.rate

        vendor = comments.contents.vendor.decode('ascii', 'ignore')
        self._info_dict['Vendor'] = vendor

        # Get comments from file.
        comments = _vorbisfile.ov_comment(_vorbisfile.byref(vorbis_file), -1)
        comments = comments.contents.user_comments

        # Build info dict.
        for comment in comments:
            # Exit loop after the last comment.
            if not comment: break

            comment_list = comment.decode('utf8', 'replace').split('=')

            # Handle invalid comments (without '=')
            if b'=' not in comment:
                comment_list.insert(0, 'misc')

            comment_list[0] = comment_list[0].lower()

            self._info_dict.update(dict((comment_list,)))

        if not self._info_dict.get('name', ''):
            album = self._info_dict.get('album', '')
            title = self._info_dict.get('title', '')
            if album and title:
                name = ('%s - %s' % (album.strip(), title.strip()))
            else:
                name = self._filename

            self._info_dict['name'] = name

        # The file is now open.
        self._closed = False

        return vorbis_file

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        bytesread = -1

        bitstream = _vorbisfile.pointer(_vorbisfile.c_int())

        # Create the read buffer.
        str_buf = _vorbisfile.create_string_buffer(size)

        # Start with any unused data from the last read.
        data = self._data

        file_pointer = _vorbisfile.pointer(self._vorbis_file)

        while len(data) < size:
            # Read the data from the file.
            bytesread = _vorbisfile.ov_read(file_pointer, str_buf, size,
                                            int(self._bigendian), self._width,
                                            int(self._signed), bitstream)

            # Check how many bytes were read.
            if bytesread == 0:
                # Check if we should loop.
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the rest of the buffer with blank data and
                    # exit.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    # Increment the loop counter.
                    self._loop_count += 1

                    # Seek to the start and continue reading.
                    self.seek(0)
                    continue

            # append the data read to the buffer.
            data += _vorbisfile.string_at(str_buf, bytesread)

        # Store extra data for the next read.
        self._data = data[size:]

        # Only return the amount asked for.
        return data[:size]

    def _read_close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            _vorbisfile.ov_clear(_vorbisfile.byref(self._vorbis_file))
            self._vorbis_file = None

            self._closed = True

    def _write_open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        ret = self._info.encode_init_vbr(self._channels, self._rate,
                                         _vorbisfile.c_float(self._quality))

        if ret != 0:
            raise IOError("Error initializing vorbis info")

        self._comment["ENCODER"] = __name__
        self._info_dict['encoder'] = __name__

        self._dsp_state.analysis_init(self._info)
        self._dsp_state.block_init(self._block)

        header = _vorbisenc.OggPacket()
        header_comm = _vorbisenc.OggPacket()
        header_code = _vorbisenc.OggPacket()

        self._dsp_state.headerout(self._comment, header, header_comm,
                                  header_code)
        self._stream_state.packetin(header)
        self._stream_state.packetin(header_comm)
        self._stream_state.packetin(header_code)

        vorbis_file = open(filename, 'wb')

        # Initialize the file.
        while self._stream_state.flush(self._page):
            vorbis_file.write(bytes(self._page))

        # The file is now open.
        self._closed = False

        return vorbis_file

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(str) -> Encodes and writes str to an ogg file.

        """

        written = 0

        for data_buffer in slice_buffer(data, self._buffer_size):
            written += self._vorbis_file.write(self._encode(data_buffer))

        return written

    def _fill_buffer(self, data):
        """ fill_buffer(data) -> Fill the dsp buffer with data.
        De-interleaves the data in 'data', and puts it in the dsps two
        dimensional floating point array.

        """

        data_size = len(data) // (self._depth // (8 // self._channels))

        dsp_buffer = self._dsp_state.get_buffer(data_size)

        bytebuffer = array('h', data)

        for i in range(data_size):
            for j in range(self._channels):
                dsp_buffer[j][i] = bytebuffer[i * self._channels + j] / 32768.0
            # dsp_buffer[0][i] = (bytebuffer[i * self._channels] |
            #                     (bytebuffer[i] % 255)) / 32768.0
            # if self._channels != 1:
            #     dsp_buffer[1][i] = (bytebuffer[i * 2 + 1] |
            #                         (bytebuffer[i + 1] % 255)) / 32768.0

        return data_size

    def _encode(self, data):
        """ _encode(str) -> Returns the vorbis encoded str.

        """

        data_size = self._fill_buffer(data) if data else 0

        self._dsp_state.wrote(data_size)

        # Vorbis data buffer
        page_buffer = b''

        while self._dsp_state.blockout(self._block) == 1:
            self._block.analysis(None)
            self._block.bitrate_addblock()
            while self._dsp_state.bitrate_flushpacket(self._packet):
                self._stream_state.packetin(self._packet)
                while not self._page.eos:
                    if not self._stream_state.pageout(self._page): break
                    page_buffer += bytes(self._page)

        return page_buffer

    def _write_close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            # Finalize the file.
            self._vorbis_file.write(self._encode(None))

            # Close and clear everything.
            self._vorbis_file.close()
            self._stream_state.clear()
            self._block.clear()
            self._comment.clear()
            self._info.clear()

            self._vorbis_file = None

            # The file is closed.
            self._closed = True
