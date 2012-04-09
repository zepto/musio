#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of mp3 files.
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


""" A module for reading mp3s.

"""

from io_base import AudioIO, OnDemand, io_wrapper

_mpg123 = OnDemand('mpg123._mpg123', globals(), locals(),
                   ['_mpg123'], 0)

__supported_dict = {
        'ext': ['.mp3'],
        'handler': 'Mpg123File'
        }


def _check(err):
    """ Check if there was an error and print the result.

    """

    if not err: return err

    if hasattr(err, 'value'):
        err = err.value

    if err != _mpg123.MPG123_OK:
        print(_mpg123.mpg123_plain_strerror(err).decode('cp437', 'replace'))

    return err


class Mpg123File(AudioIO):
    """ A file like object for reading mp3s.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2,
                 unsigned=False, **kwargs):
        """ Mpg123File(filename, depth=16, rate=44100, channels=2,
        unsigned=False) -> Initialize the playback settings of the player.

        """

        super(Mpg123File, self).__init__(filename, 'r', depth, rate, channels)

        if depth in [8, 16, 32]:
            encoding = getattr(_mpg123, 'MPG123_ENC_%s_%s' % \
                                     ('UNSIGNED' if unsigned else 'SIGNED',
                                      depth))
        else:
            encoding = _mpg123.MPG123_ENC_SIGNED_16

        self._encoding = encoding
        self._unsigned = unsigned

        self._id3_dict = {}

        _check(_mpg123.mpg123_init())

        self._mpg123_handle = self._open(filename)

        self._length = _mpg123.mpg123_length(self._mpg123_handle)

        self._update_info()

        self._data = b''

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, unsigned=%(_unsigned)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _check(_mpg123.mpg123_seek(self._mpg123_handle, position,
                                        _mpg123.SEEK_SET))

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return _mpg123.mpg123_tell(self._mpg123_handle)

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        # Create a mpg123 handle.
        err = _mpg123.c_int()
        mpg123_handle = _mpg123.mpg123_new(None, _mpg123.byref(err))
        _check(err)

        if _check(_mpg123.mpg123_open(mpg123_handle, filename.encode())):
            raise IOError("There was an error opening %s" % filename)


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

    def _update_info(self):
        """ Updates the id3 info for the opened mp3.

        """

        id3v1 = _mpg123.POINTER(_mpg123.mpg123_id3v1)()
        id3v2 = _mpg123.POINTER(_mpg123.mpg123_id3v2)()
        _check(_mpg123.mpg123_id3(self._mpg123_handle,
                                       _mpg123.byref(id3v1),
                                       _mpg123.byref(id3v2)))

        id3_dict = {}
        for i in ['tag', 'title', 'artist', 'album', 'year', 'comment', 
                  'genre']:
            try:
                id3_dict[i] = getattr(id3v1.contents, i)
                id3_dict[i] = getattr(id3v2.contents, i).contents.p
            except:
                continue
        try:
            id3_dict['version'] = id3v2.contents.version
        except:
            pass

        try:
            if id3v2.contents.extras > 0:
                id3_dict['extra'] = id3v2.contents.extra.contents.text.p
        except:
            pass

        try:
            if id3v2.contents.texts > 0:
                id3_dict['texts'] = id3v2.contents.text.contents.text.p
        except:
            pass

        temp_dict = {}
        temp_dict.update(id3_dict)
        for key, value in temp_dict.items():
            if type(value) is not int:
                if not i.strip():
                    id3_dict.pop(key)
                elif type(value) is bytes:
                    id3_dict[key.lower()] = value.decode()

        album = id3_dict.get('album', '')
        artist = id3_dict.get('artist', '')
        title = id3_dict.get('title', '')

        if album and title:
            name = ('%s - %s' % (album.strip(), title.strip()))
        elif artist and title:
            name = ('%s - %s' % (artist.strip(), title.strip()))
        else:
            name = self._filename

        id3_dict['name'] = name

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

    def close(self) -> bool:
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            try:
                _check(_mpg123.mpg123_close(self._mpg123_handle))
                _check(_mpg123.mpg123_delete(self._mpg123_handle))
                _check(_mpg123.mpg123_exit())

                self._mpg123_handle = None

                self._closed = True
            except Exception as err:
                print("(%s.close) Error: %s" % (self.__class__.__name__, err))
