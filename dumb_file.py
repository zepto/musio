#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of module music using dumb. 
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


""" Dumb is a class to handle module music using the dumb library.

"""

from io_base import AudioIO, OnDemand, io_wrapper
from conversion_util import swap_endian

_dumb = OnDemand('dumb._dumb', globals(), locals(), ['_dumb'], 0)

__supported_dict = {
        'ext': ['.xm', '.s3m', '.it', '.mod'],
        'handler': 'DumbFile',
        'default': True
        }


class Buffer(_dumb.Union):
    """ A union for taking the samples from duh_render.

    """

    _fields_ = [
            ("s16", _dumb.c_short * 8192),
            ("s8", _dumb.c_ubyte * 16384)
            ]


class DumbFile(AudioIO):
    """ File like object to access module music supported by dumb.

    """

    # Valid bit depths.
    _valid_depth = (16, 8)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, **kwargs):
        """ DumbFile(filename, depth=16, rate=44100, channels=2) -> Initialize
        the playback settings of the player.

        """

        super(DumbFile, self).__init__(filename, 'r', depth, rate, channels)

        # Set the volume to half, so it doesn't overdrive the speakers.
        self._volume = 0.5

        self._delta = 0
        self.speed = 1.0

        self._unsigned = unsigned
        self._bigendian = bigendian

        self._buffer = Buffer()
        self._buffer_ref = _dumb.pointer(self._buffer)

        # Set data_list to buffer.s8 or buffer.s16 depending on bit depth.
        self._data_list = getattr(self._buffer, 's%s' % self._depth)

        # Define the conversion function.
        if depth == 16 and bigendian:
            self._convert_func = swap_endian
        else:
            self._convert_func = lambda data_list: data_list

        self._max_read_size = _dumb.sizeof(self._data_list)

        self._duh = self._open()
        if not self._duh:
            raise IOError("Error loading %s" % filename)

        # Start the renderer.
        self._sig_r = _dumb.duh_start_sigrenderer(self._duh, 0, channels, 0)
        self._length = _dumb.duh_get_length(self._duh)

        # Setup the loop callback
        self._it_sig_r = _dumb.duh_get_it_sigrenderer(self._sig_r)
        loop_callback = _dumb.CFUNCTYPE(_dumb.c_long, _dumb.c_void_p)
        self._loop_callback_f = loop_callback(self._loop_callback)
        _dumb.dumb_it_set_loop_callback(self._it_sig_r, self._loop_callback_f,
                                        None)

        # Load info into the info dict.
        self._load_info()

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _loop_callback(self, data):
        """ _loop_callback(data) -> Called everytime the module loops.

        """

        # Increment the loop counter.
        self._loop_count += 1

        return int(self._loops != -1 and self._loop_count > self._loops)

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._sig_r = _dumb.duh_start_sigrenderer(self._duh, 0, self._channels,
                                                  position)

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return _dumb.duh_sigrenderer_get_position(self._sig_r)

    @property
    def convert_func(self):
        """ The function used to convert the module data to the correct
        format.

        """

        return self._convert_func

    @convert_func.setter
    def convert_func(self, function):
        """ Set the function used to convert the module data to the correct
        format.  The function should take a string and return a string.

        """

        self._convert_func = function

    @property
    def volume(self):
        """ Get the current volume.

        """

        return self._volume

    @volume.setter
    def volume(self, value):
        """ Set the volume.

        """

        self._volume = value

    @property
    def speed(self):
        """ Get the current speed.

        """

        return self._delta * (self._rate / 65536.0)

    @speed.setter
    def speed(self, speed):
        """ Set the speed.

        """

        self._delta = (65536.0 * speed) / self._rate

    @property
    def resampling(self):
        """ The current resample mode.

        """

        return _dumb.dumb_resampling_quality.value

    @resampling.setter
    def resampling(self, value):
        """ resampling(mode) -> Set the resampling mode.

        """

        if value not in range(3):
            raise ValueError('Invalid value, has to be in range 0-2')
        else:
            _dumb.dumb_resampling_quality.value = int(value)

    @property
    def max_to_mix(self):
        """ Maximum number of samples to mix at a time.

        """

        return _dumb.dumb_it_max_to_mix.value

    @max_to_mix.setter
    def max_to_mix(self, value):
        """ Set the maximum number of samples to mix at a time.

        """

        _dumb.dumb_it_max_to_mix.value = value

    def _load_info(self):
        """ Load the module music info.

        """

        def load_list(key, name_func, filename_func, sig_data, count):
            """ _load_list(fill_list, name_func, filename_func, sig_data,
            count) -> Load a list of names and filenames from sig_data into
            fill_list.

            """

            fill_list = []

            for i in range(count):
                try:
                    name = name_func(sig_data, i).decode('cp437', 'replace')
                except:
                    pass
                if name:
                    name = name.replace('\r', '\n')
                    filename = filename_func(sig_data, i)
                    filename = filename.decode('cp437', 'replace')
                    filename = filename.replace('\r', '\n')
                    key_str = '%-8s %03d:' % (key.capitalize(), i)
                    value_str = '%s %s' % (name, filename)
                    fill_list.append("%s %s" % (key_str, value_str))

            return fill_list

        sig_data = _dumb.duh_get_it_sigdata(self._duh)
        num_smp = _dumb.dumb_it_sd_get_n_samples(sig_data)
        if num_smp > 0:
            tmp_list = load_list('sample', _dumb.dumb_it_sd_get_sample_name,
                      _dumb.dumb_it_sd_get_sample_filename,
                      sig_data, num_smp)
            if tmp_list:
                self._info_dict['samples'] = tmp_list

        num_inst = _dumb.dumb_it_sd_get_n_instruments(sig_data)
        if num_inst > 0:
            tmp_list = load_list('instrument',
                    _dumb.dumb_it_sd_get_instrument_name,
                    _dumb.dumb_it_sd_get_instrument_filename, sig_data,
                    num_inst)
            if tmp_list:
                self._info_dict['instruments'] = tmp_list

        name = _dumb.duh_get_tag(self._duh, b'TITLE')
        name = name.decode('cp437', 'replace')
        self._info_dict['name'] = name

        message = _dumb.dumb_it_sd_get_song_message(sig_data)
        if message:
            message = message.decode('cp437', 'replace').replace('\r', '\n')
            self._info_dict['message'] = message

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        c_size = size

        # Don't over fill the buffer or it will crash.
        if c_size > self._max_read_size:
            c_size = self._max_read_size

        # Render size will render c_size bytes.
        read_size = c_size // (self._channels * (self._depth >> 3))

        # Data buffer to fill.
        data = b''

        while len(data) < size:
            # When size - len(data) is less than c_size, c_size can be
            # smaller so we don't return too much data.
            if size - len(data) < c_size:
                c_size = size - len(data)
                read_size = c_size // (self._channels * (self._depth >> 3))

            # Render read_size amount of data.
            render_size = _dumb.duh_render(self._sig_r, self._depth,
                                           self._unsigned, self._volume,
                                           self._delta, read_size,
                                           self._buffer_ref)

            # Nothing rendered so exit loop.
            if render_size < 1:
                break

            # Get the bytes data from the c buffer.
            temp_data = _dumb.string_at(self._data_list, c_size)

            # Convert the data to the correct format.
            data += self._convert_func(temp_data)

        return data

    def _open(self):
        """ _open(filename) -> Load the specified file.

        """

        _dumb.dumb_register_stdfiles()

        func_tup = (_dumb.load_duh, _dumb.dumb_load_xm, _dumb.dumb_load_s3m,
                    _dumb.dumb_load_it, _dumb.dumb_load_mod)

        # Convert the filename to a bytes object.
        bytes_filename = self._filename.encode('utf8', 'replace')

        for loader in func_tup:
            duh = loader(bytes_filename)
            if duh:
                break
        else:
            raise IOError("Error unable to load %s" % self._filename)
            return None

        self.resampling = _dumb.DUMB_RQ_CUBIC
        self.max_to_mix = 256

        self._closed = False

        return duh

    def close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            _dumb.duh_end_sigrenderer(self._sig_r)
            _dumb.unload_duh(self._duh)
            _dumb.dumb_exit()

            self._duh = None
            self._closed = True
