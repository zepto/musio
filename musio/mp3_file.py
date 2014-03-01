#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading and writing of mp3 files.
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


""" A module for reading and writing mp3s.

"""

from sys import stderr as sys_stderr
from array import array

from .io_util import silence, msg_out
from .io_base import AudioIO, io_wrapper
from .io_util import slice_buffer
# from .mpg123 import _mpg123
from .import_util import LazyImport

_mpg123 = LazyImport('mpg123._mpg123', globals(), locals(),
                     ['_mpg123'], 1)
_lame = LazyImport('lame.lame', globals(), locals(),
                     ['lame'], 1)

__supported_dict = {
    'ext': ['.mp3'],
    'handler': 'MP3File',
    'dependencies': {
        'ctypes': ['mpg123', 'mp3lame'],
        'python': []
    }
}

SEEK_SET = 0 # Seek from beginning of file.
SEEK_CUR = 1 # Seek from current position.
SEEK_END = 2 # Seek from end of file.

def get_genre_list():
    """ Returns a list of valid id3 genres.

    """

    genre_list = [''] * 255

    def _make_genre_list(genre_id, genre, cookie):
        """ Make a list of id3 tags and their id's.

        """

        try:
            genre_list[genre_id] = genre.decode()
        except:
            print(genre_id)

    _callback = _lame.CFUNCTYPE(None, _lame.c_int, _lame.STRING, _lame.c_void_p)
    _lame.id3tag_genre_list(_callback(_make_genre_list), None)

    return genre_list

def _check(err):
    """ Check if there was an error and print the result.

    """

    if not err: return err

    if hasattr(err, 'value'):
        err = err.value

    if err != _mpg123.MPG123_OK:
        err_str = _mpg123.mpg123_plain_strerror(err).decode('cp437', 'replace')
        msg_out("Error in %s: %s" % (__file__, err_str))

    return err


class MP3File(AudioIO):
    """ A file like object for reading mp3s.

    """

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Only reading is supported
    _supported_modes = 'rw'

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2,
                 unsigned=False, quality=2, comment_dict={}, **kwargs):
        """ MP3File(filename, mode='r', depth=16, rate=44100, channels=2,
        unsigned=False, quality=2, comment_dict={}) -> Initialize the playback
        settings of the player.

        """

        super(MP3File, self).__init__(filename, mode, depth, rate, channels)

        self._unsigned = unsigned

        if mode == 'r':
            if depth in [8, 16, 32]:
                encoding = getattr(_mpg123, 'MPG123_ENC_%s_%s' %
                                ('UNSIGNED' if unsigned else 'SIGNED',
                                    depth))
            else:
                encoding = _mpg123.MPG123_ENC_SIGNED_16

            self._encoding = encoding

            self._id3_dict = {}

            _check(_mpg123.mpg123_init())
            self._mpg123_handle = self._read_open(filename)
            self._length = _mpg123.mpg123_length(self._mpg123_handle)

            self._update_info()

            self._data = b''
        else:
            if quality not in range(0, 10):
                quality = 2

            self._quality = quality
            self._comment_dict = comment_dict
            if not self._comment_dict['comment']:
                self._comment_dict['comment'] = 'Encoded with musio.mp3_file'

            self._global_flags = _lame.lame_init()

            _lame.lame_set_quality(self._global_flags, quality)

            # Disable auto id3 tag write.
            _lame.lame_set_write_id3tag_automatic(self._global_flags, 0);

            if not self._global_flags:
                raise(Exception("Error creating lame global structure"))
            if _lame.lame_init_params(self._global_flags) < 0:
                raise(Exception("Error initializing lame"))

            self._out_file = self._write_open(filename)
            self._write_id3v2tags()

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', mode=%(_mode)s, depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, unsigned=%(_unsigned)s, quality=%(_quality)s, comment_dict=%(_comment_dict)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def to_seconds(self, position):
        """ Convert the provided position/length to seconds.

        """

        return position / self._rate

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _check(_mpg123.mpg123_seek(self._mpg123_handle, position,
                                   SEEK_SET))

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return _mpg123.mpg123_tell(self._mpg123_handle)

    def _read_open(self, filename: str):
        """ _read_open(filename) -> Load the specified file.

        """

        # Create a mpg123 handle.
        err = _mpg123.c_int()
        mpg123_handle = _mpg123.mpg123_new(None, _mpg123.byref(err))
        _check(err)

        if _check(_mpg123.mpg123_open(mpg123_handle, filename.encode())):
            raise IOError("There was an error opening %s" % filename)

        with silence(sys_stderr):
            _check(_mpg123.mpg123_scan(mpg123_handle))

        _check(_mpg123.mpg123_format_none(mpg123_handle))

        err = _check(_mpg123.mpg123_format(mpg123_handle,
                                           self._rate, self._channels,
                                           self._encoding))

        rate = _mpg123.c_long()
        channels = _mpg123.c_int()
        encoding = _mpg123.c_int()

        _check(_mpg123.mpg123_getformat(mpg123_handle,
                                        _mpg123.byref(rate),
                                        _mpg123.byref(channels),
                                        _mpg123.byref(encoding)))

        self._rate = rate.value
        self._channels = channels.value
        self._encoding = encoding.value

        # Grab the depth from the encoding.
        for k, i in vars(_mpg123).items():
            if i == encoding.value:
                k_split = k.split('_')
                self._depth = int(k_split[-1])
                self._unsigned = k_split[-2] != 'SIGNED'

        self._closed = False

        return mpg123_handle

    def _write_open(self, filename: str):
        """ _write_open(filename) -> Load the specified file.

        """

        self._closed = False

        return open(filename, 'wb')

    def _update_info(self):
        """ Updates the id3 info for the opened mp3.

        """

        id3v1 = _mpg123.POINTER(_mpg123.mpg123_id3v1)()
        id3v2 = _mpg123.POINTER(_mpg123.mpg123_id3v2)()
        _check(_mpg123.mpg123_id3(self._mpg123_handle,
                                  _mpg123.byref(id3v1),
                                  _mpg123.byref(id3v2)))

        id3_dict = self._info_dict
        for i in ['tag', 'title', 'artist', 'album', 'year', 'comment',
                  'genre']:
            try:
                id3_dict[i] = getattr(id3v1.contents, i)
            except:
                pass
            try:
                id3_dict[i] = getattr(id3v2.contents, i).contents.p
            except:
                continue
        try:
            id3_dict['version'] = id3v2.contents.version
        except:
            pass

        try:
            if id3v2.contents.extras > 0:
                tag_type = id3v2.contents.extra.contents.description.p.decode()
                id3_dict[tag_type] = id3v2.contents.extra.contents.text.p
        except:
            pass

        try:
            if id3v2.contents.texts > 0:
                id3_dict['texts'] = id3v2.contents.text.contents.text.p
        except:
            pass

        for key, value in dict(id3_dict.items()).items():
            if type(value) is not int:
                if not value.strip():
                    id3_dict.pop(key)
                elif type(value) is bytes:
                    id3_dict.pop(key)
                    id3_dict[key.lower()] = value.decode()
            else:
                id3_dict.pop(key)
                id3_dict[key.lower()] = value

        album = id3_dict.get('album', '')
        artist = id3_dict.get('artist', '')
        title = id3_dict.get('title', '')

        if album and title:
            id3_dict['name'] = '%(album)s - %(title)s' % id3_dict
        elif artist and title:
            id3_dict['name'] = '%(artist)s - %(title)s' % id3_dict
        elif title:
            id3_dict['name'] = title.strip()

        self._id3_dict = self._info_dict = id3_dict

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        byte_buffer = (_mpg123.c_ubyte * size)()
        bytes_read = _mpg123.c_size_t(-1)
        data = self._data
        while len(data) < size:
            with silence(sys_stderr):
                err = _check(_mpg123.mpg123_read(self._mpg123_handle,
                                                 byte_buffer, size,
                                                 _mpg123.byref(bytes_read)))

            if bytes_read.value == 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    self._loop_count += 1
                    self.seek(0)
                    continue

            data += byte_buffer

        # Make sure we return only the number of bytes requested.
        self._data = data[size:]

        return data[:size]

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(str) -> Encodes and writes str to an mp3 file.

        """

        # Number of samples = bytes / ((bits per sample) / 8)
        num_samples = len(data) // (self._depth // 8)
        samples_per_chan = num_samples // self._channels

        # Create a buffer to hold the encoded data.
        encoded_data = (_lame.c_ubyte * len(data))()

        # Split the data into samples.
        if self._depth == 16:
            # Two bytes per sample.
            data_bytes = array('h', data)
        elif self._depth == 8:
            # One byte per sample.
            data_bytes = array('b', data)

        # in_buffer_l = (_lame.c_short * samples_per_chan)(*data_bytes[::2])
        # in_buffer_r = (_lame.c_short * samples_per_chan)(*data_bytes[1::2])
        # bytes_encoded = _lame.lame_encode_buffer(self._global_flags,
        #                                             in_buffer_l,
        #                                             in_buffer_r,
        #                                             samples_per_chan,
        #                                             encoded_data,
        #                                             0)

        in_buffer = (_lame.c_short * num_samples)(*data_bytes)
        bytes_encoded = _lame.lame_encode_buffer_interleaved(self._global_flags,
                                                    in_buffer,
                                                    samples_per_chan,
                                                    encoded_data,
                                                    0)

        # Retrieve the encoded audio data from buffer.
        out_data = _lame.string_at(encoded_data, bytes_encoded)

        # Write it to the file.
        return self._out_file.write(out_data)

    def _write_id3v2tags(self):
        """ Write id3tags to the mp3 file.

        """

        # Initialize the id3tags and add v2 tags.
        _lame.id3tag_init(self._global_flags)
        _lame.id3tag_add_v2(self._global_flags)

        # Add the tags in comment_dict.
        for tag_type, tag in self._comment_dict.items():
            # Make sure tag is of type bytes.
            tag = tag.encode() if type(tag) is str else tag
            if type(tag) is not bytes:
                tag = str(tag).encode()
            tag_func = getattr(_lame, 'id3tag_set_%s' % tag_type, None)
            if tag_func:
                if tag_func(self._global_flags, tag) == -1:
                    err_str = '%s %s out of range' % (tag_type, tag)
                    msg_out("Error in %s: %s" % (__file__, err_str))

        # Write the v2 tag.
        id3v2_size = _lame.lame_get_id3v2_tag(self._global_flags,
                                              _lame.c_ubyte(0), 0)
        id3v2_tag = (_lame.c_ubyte * id3v2_size)()
        id3v2_len = _lame.lame_get_id3v2_tag(self._global_flags, id3v2_tag,
                                             id3v2_size)
        out_data = _lame.string_at(id3v2_tag, id3v2_len)
        self._out_file.write(out_data)

    def close(self) -> bool:
        """ close -> Closes and cleans up.

        """

        if self._mode == 'r':
            self._read_close()
        else:
            self._write_close()

    def _read_close(self) -> bool:
        """ close -> Closes reading file.

        """

        if not self.closed:
            try:
                _check(_mpg123.mpg123_close(self._mpg123_handle))
                _check(_mpg123.mpg123_delete(self._mpg123_handle))
                _check(_mpg123.mpg123_exit())

                self._mpg123_handle = None

                self._closed = True
            except Exception as err:
                msg_out("(%s.close) Error: %s" % (self.__class__.__name__, err))

    def _write_close(self) -> bool:
        """ close -> Closes writing file.

        """

        if self._out_file:
            # Create a buffer to hold the encoded data.
            encoded_data = (_lame.c_ubyte * 7200)()

            # Flush the buffer and get the last buffer to write.
            ret = _lame.lame_encode_flush(self._global_flags, encoded_data, 0)

            # Retrieve the encoded audio data from buffer.
            out_data = _lame.string_at(encoded_data, ret)

            # Write it to the file.
            self._out_file.write(out_data)

            # Write the v1 tag.
            id3v1_tag = (_lame.c_ubyte * 128)()
            id3v1_len = _lame.lame_get_id3v1_tag(self._global_flags, id3v1_tag,
                                                _lame.sizeof(id3v1_tag))
            out_data = _lame.string_at(id3v1_tag, id3v1_len)
            self._out_file.write(out_data)

            self._out_file.close()
