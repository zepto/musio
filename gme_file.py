#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of some chip music. 
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


""" A file like object to play libgme supported chip music. 

"""

from functools import partial

from io_base import AudioIO, OnDemand, io_wrapper

_gme = OnDemand('gme._gme', globals(), locals(), ['_gme'], 0)

__supported_dict = {
        'ext': ['.ay', '.gps', '.gym', '.hes', '.kss', '.nsf', '.nsfe', 
                '.sap', '.spc', '.vgm', '.vgz'],
        'handler': 'GMEFile'
        }

def _err(func_out):
    """ _err(func_out) -> Check the function output and if it is not
    empty raise an error.

    """

    if func_out:
        raise Exception(func_out.decode('cp437', 'replace'))

    return func_out


class GMEFile(AudioIO):
    """ An object for accessing files supported by libgme.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, track=0, depth=16, rate=44100, channels=2):
        """ GMEFile(filename, depth=16, rate=44100, channels=2) -> Initialize
        the playback settings of the player.

        """

        super(GMEFile, self).__init__(filename, 'r', 16, rate, 2)

        self._track = track
        self._tempo = 1
        self._track_count = 0
        self._stereo_depth = 0.0

        # Open the file.
        self._music_emu = self._open(filename)

        # Start the track playing.
        self.track = track

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='{_filename}', track={_track}, rate={_rate}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _set_position(self, position):
        """ Change the position of playback.

        """

        _err(_gme.gme_seek(self._music_emu, position))

    def _get_position(self):
        """ Updates the position variable.

        """

        return _gme.gme_tell(self._music_emu)

    @property
    def stereo_depth(self):
        """ Get the current stereo depth

        """

        return self._stereo_depth

    @stereo_depth.setter
    def stereo_depth(self, value):
        """ Set the stereo depth.

        """

        if value < 0.0 or value > 1.0:
            print("Invalid value %s: must in range 0.0-1.0" % value)
        else:
            self._stereo_depth = value
            _gme.gme_set_stereo_depth(self._music_emu, value)

    @property
    def tempo(self):
        """ Get the current tempo.

        """

        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        """ Set the tempo.

        """

        self._tempo = tempo
        _gme.gme_set_tempo(self._music_emu, tempo)

    @property
    def track(self):
        """ Get the current track

        """

        return self._track

    @track.setter
    def track(self, track):
        """ Set the track

        """

        self._track = track % self._track_count

        _err(_gme.gme_start_track(self._music_emu, self._track))

        self._update_info()

    def _open(self, filename):
        """ _load(filename) -> Load the specified file.

        """

        music_emu = _gme.POINTER(_gme.Music_Emu)()

        filename = filename.encode()
        _err(_gme.gme_open_file(filename, _gme.byref(music_emu), self._rate))

        self._track_count = _gme.gme_track_count(music_emu)

        self._closed = False

        return music_emu

    def _update_info(self):
        """ _load_info() -> Load the information such as the module name
        and message and the sample and instrument names.

        """

        info_t = _gme.POINTER(_gme.gme_info_t)()
        track_info = _gme.gme_track_info(self._music_emu, _gme.byref(info_t),
                                         self._track)

        self._length = info_t.contents.play_length

        info_dict = {'track': '%s/%s' % (self._track, self._track_count)}

        for i in ('system', 'song', 'copyright', 'author',
                  'comment', 'dumper', 'game'):
            data = getattr(info_t.contents, i).decode('cp437', 'replace')
            if data:
                info_dict[i] = data

        _gme.gme_free_info(info_t)

        self._info_dict = info_dict

    @io_wrapper
    def read(self, size=None):
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        size //= self._channels

        c_buffer = (_gme.c_short * size)()

        _gme.gme_play(self._music_emu, size, c_buffer)

        data = _gme.string_at(c_buffer, _gme.sizeof(c_buffer))

        if _gme.gme_track_ended(self._music_emu):
            if self._loops == -1 or self._loops > self._loop_count:
                self._loop_count += 1
                self.seek(0)
            else:
                data = b''

        return data

    def close(self):
        """ close -> Closes and cleans up.

        """

        _gme.gme_delete(self._music_emu)

        self._closed = True


class MusicEmu(object):
    """ libgme music emu wrapper.

    """

    def __init__(self, filename, rate=44100):
        """ Create new music emu object.

        """

        super(MusicEmu, self).__init__()

        self._music_emu = self._open(filename, rate)

        self.delete = partial(_gme.gme_delete, self._music_emu)

        self.track_count = partial(_gme.gme_track_count, self._music_emu)
        self._start_track = partial(_gme.gme_start_track, self._music_emu)
        self.track_ended = partial(_gme.gme_track_ended, self._music_emu)

        self.play = partial(_gme.gme_play, self._music_emu)

        self.set_fade = partial(_gme.gme_set_fade, self._music_emu)

        self.tell = partial(_gme.gme_tell, self._music_emu)
        self.seek = partial(_gme.gme_seek, self._music_emu)

        self.warning = partial(_gme.gme_warning, self._music_emu)
        self.load_m3u = partial(_gme.gme_load_m3u, self._music_emu)

        self.set_stereo_depth = partial(_gme.gme_set_stereo_depth,
                                        self._music_emu)
        self.ignore_silence = partial(_gme.gme_ignore_silence,
                                      self._music_emu)
        self.set_tempo = partial(_gme.gme_set_tempo, self._music_emu)

        self.voice_count = partial(_gme.gme_voice_count, self._music_emu)
        self.voice_name = partial(_gme.gme_voice_name, self._music_emu)
        self.mute_voice = partial(_gme.gme_mute_voice, self._music_emu)
        self.mute_voices = partial(_gme.gme_mute_voices, self._music_emu)

        self._equalizer = _gme.POINTER(_gme.gme_equalizer_t)()
        self.equalizer = partial(_gme.gme_equalizer, self._music_emu,
                                 self._equalizer)
        self.set_equalizer = partial(_gme.gme_set_equalizer, self._equalizer)

        self._track_info = {}
        self._track = 0

        self._closed = False

    @property
    def length(self):
        """ Current track length.

        """

        return self._length

    def start_track(self, track):
        """ start_track(track) -> Start playing track.

        """

        self._track = track % self.track_count()

        self._start_track(self._track)

        self._update_track_info()

    def _update_track_info(self):
        """ _update_track_info() -> Update the track info dictionary.

        """

        info_t = _gme.POINTER(_gme.gme_info_t)()
        track_info = _gme.gme_track_info(self._music_emu, _gme.byref(info_t),
                                         track)

        self._length = info_t.contents.play_length

        info_dict = {}
        info_dict['name'] = info_t.contents.game.decode('cp437', 'replace')

        for i in ('system', 'song', 'copyright', 'author',
                  'comment', 'dumper'):
            data = getattr(info_t.contents, i).decode('ascii', 'ignore')
            if data:
                info_dict[i] = data

        _gme.gme_free_info(info_t)

        self._track_info = info_dict

    def track_info(self, track):
        """ track_info(track) -> Return the info about the track.

        """

        return self._track_info

    def read(self, size):
        """ read(size) -> Read size bytes and return a bytes object.

        """

        if self._closed:
            raise IOError("Can't read from closed file.")

        if self.track_ended():
            return b''

        c_buffer = (_gme.c_short * size)()

        self.play(size, c_buffer)

        return _gme.string_at(c_buffer, _gme.sizeof(c_buffer))

    def _open(self, filename, sample_rate):
        """ _open(filename, sample_rate) -> Wrap the _gme.gme_open_file 
        function.

        """

        filename = filename.encode()

        music_emu = _gme.POINTER(_gme.Music_Emu)()

        _err(_gme.gme_open_file(filename, _gme.byref(music_emu), sample_rate))

        return music_emu

    def close(self):
        """ Cleanup.

        """

        self.delete()
        self._closed = True
