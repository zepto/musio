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


"""A module for reading and writing mp3s."""

import audioop
from array import array
from os import getenv
from sys import stderr
from typing import Any

from .id3_util import ID3Tags
from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import Magic, msg_out, silence

_mpg123 = LazyImport('mpg123._mpg123', globals(), locals(), ['_mpg123'], 1)
_lame = LazyImport('lame.lame', globals(), locals(), ['lame'], 1)

__supported_dict = {
    'ext': ['.mp3'],
    'handler': 'MP3File',
    'dependencies': {
        'ctypes': ['mpg123', 'mp3lame'],
        'python': []
    }
}

SEEK_SET = 0  # Seek from beginning of file.
SEEK_CUR = 1  # Seek from current position.
SEEK_END = 2  # Seek from end of file.


def get_genre_list() -> list[str]:
    """Return a list of valid id3 genres."""
    genre_list = [''] * 255

    def _make_genre_list(genre_id: int, genre: bytes, _):
        """Make a list of id3 tags and their id's."""
        try:
            genre_list[genre_id] = genre.decode('utf8', 'replace')
        except Exception:
            print(genre_id)

    _callback = _lame.CFUNCTYPE(
        None,
        _lame.c_int,
        _lame.STRING,
        _lame.c_void_p
    )
    _lame.id3tag_genre_list(_callback(_make_genre_list), None)

    return genre_list


def _check(err: Any) -> Any:
    """Check if there was an error and print the result."""
    if not err:
        return err

    if hasattr(err, 'value'):
        err = err.value

    if err != _mpg123.MPG123_OK:
        err_str = _mpg123.mpg123_plain_strerror(err).decode('cp437', 'replace')
        msg_out(f"Error in {__file__}: {err_str}")

    return err


class MP3File(AudioIO):
    """A file like object for reading and writing mp3s."""

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Only reading is supported
    _supported_modes = 'rw'

    def __init__(self, filename: str, mode: str = 'r', depth: int = 16,
                 rate: int = 44100, channels: int = 2,
                 unsigned: bool = False, quality: int = 2,
                 comment_dict: dict = {}, **kwargs):
        """Initialize the playback settings of the player."""
        if depth in [32, 24]:
            self._from_width = depth // 8
            depth = 16
        else:
            self._from_width = None

        self._state = None

        super(MP3File, self).__init__(filename, mode, depth, rate, channels)

        self._unsigned = unsigned

        if mode == 'r':
            if depth in [8, 16, 32]:
                encoding = getattr(
                    _mpg123,
                    f"MPG123_ENC_{'UNSIGNED' if unsigned else 'SIGNED'}_"
                    f"{depth}"
                )
            else:
                encoding = _mpg123.MPG123_ENC_SIGNED_16

            self._encoding = encoding

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
            if not self._comment_dict.get('comment', ''):
                self._comment_dict['comment'] = f"Encoded with {__name__}"

            self._global_flags = _lame.lame_init()

            _lame.lame_set_quality(self._global_flags, quality)

            # Disable auto id3 tag write.
            _lame.lame_set_write_id3tag_automatic(self._global_flags, 0)

            if not self._global_flags:
                raise(Exception("Error creating lame global structure"))
            if _lame.lame_init_params(self._global_flags) < 0:
                raise(Exception("Error initializing lame"))

            self._out_file = self._write_open(filename)

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        if self._mode == 'r':
            repr_str = (f"filename='{self._filename}', mode={self._mode}, "
                        f"depth={self._depth}, rate={self._rate}, "
                        f"channels={self._channels}, "
                        f"unsigned={self._unsigned}")
        else:
            repr_str = (f"filename='{self._filename}', mode={self._mode}, "
                        f"depth={self._depth}, rate={self._rate}, "
                        f"channels={self._channels}, "
                        f"unsigned={self._unsigned}, quality={self._quality}, "
                        f"comment_dict={self._comment_dict}")

        return f"{self.__class__.__name__}({repr_str})"

    def to_seconds(self, position: int) -> float:
        """Convert the provided position/length to seconds."""
        return position / self._rate

    def _set_position(self, position: int):
        """Change the position of playback."""
        _check(_mpg123.mpg123_seek(self._mpg123_handle, position, SEEK_SET))

    def _get_position(self) -> int:
        """Update the position variable."""
        # Update the position.
        return _mpg123.mpg123_tell(self._mpg123_handle)

    def _read_open(self, filename: str) -> Any:
        """Load the specified file."""
        # Create a mpg123 handle.
        err = _mpg123.c_int()
        mpg123_handle = _mpg123.mpg123_new(None, _mpg123.byref(err))
        _check(err)

        try:
            bytes_filename = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            bytes_filename = filename

        if _check(_mpg123.mpg123_open(mpg123_handle, bytes_filename)):
            raise IOError(f"There was an error opening {filename}")

        with silence(stderr):
            _check(_mpg123.mpg123_scan(mpg123_handle))

        _check(_mpg123.mpg123_format_none(mpg123_handle))

        err = _check(_mpg123.mpg123_format(
            mpg123_handle, self._rate, self._channels, self._encoding))

        rate = _mpg123.c_long()
        channels = _mpg123.c_int()
        encoding = _mpg123.c_int()

        _check(_mpg123.mpg123_getformat(
            mpg123_handle,
            _mpg123.byref(rate),
            _mpg123.byref(channels),
            _mpg123.byref(encoding)
        ))

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

    def _write_open(self, filename: str) -> Any:
        """Load the specified file."""
        # Initialize the id3tags and add v2 tags.
        _lame.id3tag_init(self._global_flags)
        _lame.id3tag_add_v2(self._global_flags)

        type_dict = {
            'title': b'TIT2',
            'artist': b'TPE1',
            'album': b'TALB',
            'year': b'TYER',
            'track': b'TRCK',
            'genre': b'TCON',
            'date': b'TYER',
            'tracknumber': b'TRCK'
        }

        tag_type_dict = {
            'title': 'title',
            'artist': 'artist',
            'album': 'album',
            'year': 'year',
            'track': 'track',
            'genre': 'genre',
            'date': 'year',
            'tracknumber': 'track',
            'comment': 'comment'
        }

        # Add the tags in comment_dict.
        for tag_type, tag in self._comment_dict.items():
            # Cleanup the tag before encoding.
            tag = str(tag).strip()
            tag_enc = ''

            # Detect the tag encoding.
            for tag_enc in ['ascii', 'latin-1', 'utf16']:
                try:
                    tag = tag.encode(tag_enc) if type(tag) is str else tag
                    break
                except UnicodeEncodeError:
                    continue

            # Add all id3 tags.
            tag_type = tag_type_dict.get(tag_type, '')
            tag_func = getattr(_lame, f"id3tag_set_{tag_type}", None)
            if tag_func:
                if tag_func(self._global_flags, tag):
                    err_str = f"{tag_type} {tag} out of range"
                    msg_out(f"Error in {__file__}: {err_str}")
                _lame.id3tag_set_pad(self._global_flags, 128000)

            # Add the utf16 tags.
            if tag_enc == 'utf16':
                tag_id = type_dict.get(tag_type, None)

                # Convert the tag to a unsigned short array.
                data_bytes = array('h', tag)
                in_buffer = (_lame.c_ushort * len(data_bytes))(*data_bytes)

                if tag_type == 'comment':
                    _ = _lame.id3tag_set_comment_utf16(
                        self._global_flags,
                        _lame.c_char_p(0),
                        _lame.c_ushort(0),
                        in_buffer
                    )
                if tag_id:
                    _ = _lame.id3tag_set_textinfo_utf16(
                        self._global_flags,
                        _lame.c_char_p(tag_id),
                        in_buffer
                    )

        # Write the v2 tag.
        id3v2_size = _lame.lame_get_id3v2_tag(
            self._global_flags, _lame.c_ubyte(0), 0)
        id3v2_tag = (_lame.c_ubyte * id3v2_size)()
        id3v2_len = _lame.lame_get_id3v2_tag(
            self._global_flags, id3v2_tag, id3v2_size)
        out_data = _lame.string_at(id3v2_tag, id3v2_len)

        out_file = open(filename, 'wb')

        # Write out the id3v2 tags.
        out_file.write(out_data)

        self._closed = False

        return out_file

    def _get_mpg123_tags(self) -> dict:
        """Use mpg123 to get the id3tags."""
        id3v1 = _mpg123.POINTER(_mpg123.mpg123_id3v1)()
        id3v2 = _mpg123.POINTER(_mpg123.mpg123_id3v2)()
        _check(_mpg123.mpg123_id3(self._mpg123_handle,
               _mpg123.byref(id3v1), _mpg123.byref(id3v2)))

        id3_dict = self._info_dict
        for i in ['tag', 'title', 'artist', 'album', 'year', 'comment',
                  'genre']:
            id3_dict[i] = ''
            try:
                id3_dict[i] = getattr(id3v2.contents, i).contents.p
            except Exception:
                pass
            try:
                temp = getattr(id3v1.contents, i)
                current_i = id3_dict.get(i, b'')
                id3_dict[i] = temp if len(temp) > len(current_i) else current_i
            except Exception:
                pass

        try:
            id3_dict['version'] = id3v2.contents.version
        except Exception:
            pass

        try:
            if id3v2.contents.extras > 0:
                tag_type = id3v2.contents.extra.contents.description.p
                tag_type = tag_type.decode('utf8', 'replace')
                id3_dict[tag_type] = id3v2.contents.extra.contents.text.p
        except Exception:
            pass

        try:
            if id3v2.contents.texts > 0:
                id3_dict['texts'] = id3v2.contents.text.contents.text.p
        except Exception:
            pass

        magic = Magic()
        for key, value in dict(id3_dict.items()).items():
            if type(value) is not int:
                if not value.strip():
                    id3_dict.pop(key)
                elif type(value) is bytes:
                    id3_dict.pop(key)
                    enc = magic.check(value).decode()
                    enc = getenv('MUSIO_LANG', enc)
                    try:
                        id3_dict[key.lower()] = value.decode(enc, 'ignore')
                    except LookupError:
                        id3_dict[key.lower()] = value.decode('utf8', 'ignore')

            else:
                id3_dict.pop(key)
                id3_dict[key.lower()] = value

        return id3_dict

    def _get_id3tags(self) -> dict:
        """Use libid3tag to read the id3tags."""
        try:
            import id3tag.id3tag as _id3tag
        except Exception:
            return self._get_mpg123_tags()

        bytes_filename = self._filename.encode('utf-8', 'surrogateescape')
        id3_file = _id3tag.id3_file_open(bytes_filename, 0)
        id3_tag = _id3tag.id3_file_tag(id3_file)
        fields_dict = {
            'title': b'TIT2',
            'artist': b'TPE1',
            'album': b'TALB',
            'track': b'TRCK',
            'year': b'TDRC',
            'genre': b'TCON',
            'subtitle': b'TIT3',
            'copyright': b'TCOP',
            'produced': b'TPRO',
            'orchestra': b'TPE2',
            'conductor': b'TPE3',
            'lyricist': b'TEXT',
            'publisher': b'TPUB',
            'station': b'TRSN',
            'encoder': b'TENC',
        }

        id3_dict = self._info_dict

        for tag_name, tag_id in fields_dict.items():
            id3_frame = _id3tag.id3_tag_findframe(id3_tag, tag_id, 0)
            try:
                assert(id3_frame.contents)
            except ValueError:
                continue
            field = id3_frame.contents.fields[1]
            try:
                ucs4 = field.stringlist.strings.contents
            except ValueError:
                continue
            if tag_name == 'genre':
                ucs4 = _id3tag.id3_genre_name(ucs4)
            field_val = _id3tag.id3_ucs4_utf8duplicate(ucs4)
            tag_val = _id3tag.string_at(field_val).decode('utf8', 'replace')
            id3_dict[tag_name] = tag_val

        i = 0
        while True:
            frame = _id3tag.id3_tag_findframe(id3_tag, b'COMM', i)
            try:
                assert(frame.contents)
            except ValueError:
                break
            i += 1
            # ucs4 = _id3tag.id3_field_getstring(
            #   _id3tag.id3_frame_field(frame, 2))
            ucs4 = _id3tag.id3_field_getfullstring(
                _id3tag.id3_frame_field(frame, 3))
            field_val = _id3tag.id3_ucs4_utf8duplicate(ucs4)
            tag_val = _id3tag.string_at(field_val).decode('utf8', 'replace')
            id3_dict['comment'] = tag_val
            break

        _id3tag.id3_file_close(id3_file)

        return id3_dict

    def _update_info(self):
        """Update the id3 info for the opened mp3."""
        # id3_dict = self._get_id3tags()
        id3_dict = ID3Tags(self._filename)

        album = id3_dict.get('album', '')
        artist = id3_dict.get('artist', '')
        title = id3_dict.get('title', '')

        if album and title:
            id3_dict['name'] = f"{album} - {title}"
        elif artist and title:
            id3_dict['name'] = f"{artist} - {title}"
        elif title:
            id3_dict['name'] = title.strip()

        self._info_dict |= id3_dict

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        byte_buffer = (_mpg123.c_ubyte * size)()
        bytes_read = _mpg123.c_size_t(-1)
        data = self._data
        while len(data) < size:
            with silence(stderr):
                _ = _check(_mpg123.mpg123_read(
                    self._mpg123_handle,
                    byte_buffer,
                    size,
                    _mpg123.byref(bytes_read)
                ))

            if bytes_read.value == 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    self._loop_count += 1
                    self.seek(0)
                    continue

            data += _mpg123.string_at(byte_buffer, bytes_read.value)

        # Make sure we return only the number of bytes requested.
        self._data = data[size:]

        return data[:size]

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Encode and writes str to an mp3 file."""
        # Scale all bit-width data above 16-bit down to 16-bit.
        if self._from_width:
            data = audioop.lin2lin(data, self._from_width, self._depth // 8)

        # Resample all audio data above 44100 down to 44100.
        if self._rate > 44100:
            data, self._state = audioop.ratecv(
                data,
                self._depth // 8,
                self._channels,
                self._rate,
                44100,
                self._state
            )

        # Number of samples = bytes / ((bits per sample) / 8)
        num_samples = len(data) // (self._depth // 8)
        samples_per_chan = num_samples // self._channels

        # Create a buffer to hold the encoded data.
        encoded_data = (_lame.c_ubyte * _lame.LAME_MAXMP3BUFFER)()

        data_bytes = b''

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
        bytes_encoded = _lame.lame_encode_buffer_interleaved(
            self._global_flags,
            in_buffer,
            samples_per_chan,
            encoded_data,
            _lame.sizeof(encoded_data)
        )

        # Retrieve the encoded audio data from buffer.
        out_data = _lame.string_at(encoded_data, bytes_encoded)

        # Write data to the file.
        return self._out_file.write(out_data)

    def close(self) -> bool:
        """Close and cleans up."""
        if self._mode == 'r':
            return self._read_close()
        else:
            return self._write_close()

    def _read_close(self) -> bool:
        """Close reading file."""
        if not self.closed:
            try:
                _check(_mpg123.mpg123_close(self._mpg123_handle))
                _check(_mpg123.mpg123_delete(self._mpg123_handle))
                _check(_mpg123.mpg123_exit())

                self._mpg123_handle = None

                self._closed = True
            except Exception as err:
                msg_out(f"({self.__class__.__name__}.close) Error: {err}")

        return self._closed

    def _write_close(self) -> bool:
        """Close writing file."""
        if self._out_file and not self._closed:
            # Create a buffer to hold the encoded data.
            encoded_data = (_lame.c_ubyte * _lame.LAME_MAXMP3BUFFER)()

            # Flush the buffer and get the last buffer to write.
            ret = _lame.lame_encode_flush(
                self._global_flags, encoded_data, _lame.sizeof(encoded_data))

            # Retrieve the encoded audio data from buffer.
            out_data = _lame.string_at(encoded_data, ret)

            # Write it to the file.
            self._out_file.write(out_data)

            # Write the v1 tag.
            id3v1_tag = (_lame.c_ubyte * 128)()
            id3v1_len = _lame.lame_get_id3v1_tag(
                self._global_flags, id3v1_tag, _lame.sizeof(id3v1_tag))
            out_data = _lame.string_at(id3v1_tag, id3v1_len)
            self._out_file.write(out_data)

            # Write lametag.
            lametag = (_lame.c_ubyte * _lame.LAME_MAXMP3BUFFER)()
            lametag_len = _lame.lame_get_lametag_frame(
                self._global_flags,
                lametag,
                _lame.sizeof(lametag)
            )
            out_data = _lame.string_at(lametag, lametag_len)
            self._out_file.write(out_data)

            self._out_file.close()
            _lame.lame_close(self._global_flags)

        return self._closed
