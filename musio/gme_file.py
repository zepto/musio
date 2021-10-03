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


"""A file like object to play libgme supported chip music."""

from functools import partial
from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper

_gme = LazyImport('gme._gme', globals(), locals(), ['_gme'], 1)

__supported_dict = {
    'ext': ['.ay', '.gps', '.gym', '.hes', '.kss', '.nsf', '.nsfe',
            '.sap', '.spc', '.vgm', '.vgz'],
    'handler': 'GMEFile',
    'dependencies': {
        'ctypes': ['gme'],
        'python': []
    }
}


def _err(func_out: bytes) -> bytes:
    """Verify function output.

    Check the function output and if it is not empty raise an error.
    """
    if func_out:
        raise Exception(func_out.decode('cp437', 'replace'))

    return func_out


class GMEFile(AudioIO):
    """An object for accessing files supported by libgme."""

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, track: int = 0, rate: int = 44100, **_):
        """Initialize the playback settings of the player."""
        super(GMEFile, self).__init__(filename, 'r', 16, rate, 2)

        self._track = track
        self._tempo = 1
        self._track_count = 0
        self._stereo_depth = 0.0

        # Open the file.
        self._music_emu = self._open(filename)

        # Start the track playing.
        self.track = track

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f"{self.__class__.__name__}(filename='{self._filename}', "
                f"track={self._track}, rate={self._rate})")

    def _set_position(self, position: int):
        """Change the position of playback."""
        _err(_gme.gme_seek(self._music_emu, position))

    def _get_position(self) -> int:
        """Get the playback position."""
        return _gme.gme_tell(self._music_emu)

    @property
    def stereo_depth(self) -> float:
        """Get the current stereo depth."""
        return self._stereo_depth

    @stereo_depth.setter
    def stereo_depth(self, value: float):
        """Set the stereo depth."""
        if value < 0.0 or value > 1.0:
            print(f"Invalid value {value}: must in range 0.0-1.0")
        else:
            self._stereo_depth = value
            _gme.gme_set_stereo_depth(self._music_emu, value)

    @property
    def tempo(self) -> int:
        """Get the current tempo."""
        return self._tempo

    @tempo.setter
    def tempo(self, tempo: int):
        """Set the tempo."""
        self._tempo = tempo
        _gme.gme_set_tempo(self._music_emu, tempo)

    @property
    def track(self) -> int:
        """Get the current track."""
        return self._track

    @track.setter
    def track(self, track: int):
        """Set the track."""
        # Only set track to a value between 0 and self._track_count.
        self._track = max(min(self._track_count - 1, track - 1), 0)
        _err(_gme.gme_start_track(self._music_emu, self._track))
        self._info_dict = self._update_info()

    def _open(self, filename: str) -> object:
        """Load the specified file."""
        music_emu = _gme.ctypes.POINTER(_gme.Music_Emu)()

        filename_b = filename.encode('utf-8', 'surrogateescape')
        _err(_gme.gme_open_file(
            filename_b,
            _gme.ctypes.byref(music_emu),
            self._rate
        ))

        self._track_count = _gme.gme_track_count(music_emu)

        self._closed = False

        return music_emu

    def _update_info(self) -> dict:
        """Load song information into dict.

        Load the information such as the module name and message and the sample
        and instrument names.
        """
        info_t = _gme.ctypes.POINTER(_gme.gme_info_t)()
        _ = _gme.gme_track_info(
            self._music_emu,
            _gme.ctypes.byref(info_t),
            self._track
        )

        self._length = info_t.contents.play_length

        info_dict = {"track": f"{self._track + 1}/{self._track_count}"}
        info_dict['name'] = info_t.contents.game.decode('cp437', 'replace')

        for i in ('system', 'song', 'copyright', 'author',
                  'comment', 'dumper', 'game'):
            data = getattr(info_t.contents, i).decode('cp437', 'replace')
            if data:
                info_dict[i] = data

        _gme.gme_free_info(info_t)

        return info_dict

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and return it."""
        size //= self._channels

        c_buffer = (_gme.ctypes.c_short * size)()

        _gme.gme_play(self._music_emu, size, c_buffer)

        data = _gme.ctypes.string_at(c_buffer, _gme.ctypes.sizeof(c_buffer))

        if _gme.gme_track_ended(self._music_emu) or (self.position >
                                                     self.length):
            if self._loops == -1 or self._loops > self._loop_count:
                self._loop_count += 1
                self.seek(0)
            else:
                data = b''

        return data

    def close(self):
        """Close and clean up."""
        if not self.closed:
            _gme.gme_delete(self._music_emu)

            self._closed = True


class MusicEmu:
    """GME wrapper. libgme music emu wrapper."""

    def __init__(self, filename: str, rate: int = 44100):
        """Create new music emu object."""
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

        self._equalizer = _gme.ctypes.POINTER(_gme.gme_equalizer_t)()
        self.equalizer = partial(_gme.gme_equalizer, self._music_emu,
                                 self._equalizer)
        self.set_equalizer = partial(_gme.gme_set_equalizer, self._equalizer)

        self._track_info = {}
        self._track = 0

        self._closed = False

    @property
    def length(self) -> int:
        """Get the current track length."""
        return self._length

    def start_track(self, track: int):
        """Start playing track."""
        self._track = track % self.track_count()

        self._start_track(self._track)

        self._track_info[track] = self._update_track_info(track)

    def _update_track_info(self, track: int) -> dict:
        """Update the track info dictionary."""
        info_t = _gme.ctypes.POINTER(_gme.gme_info_t)()
        _ = _gme.gme_track_info(
            self._music_emu,
            _gme.ctypes.byref(info_t),
            track
        )

        self._length = info_t.contents.play_length

        info_dict = {}
        info_dict['name'] = info_t.contents.game.decode('cp437', 'replace')

        for i in ('system', 'song', 'copyright', 'author',
                  'comment', 'dumper'):
            data = getattr(info_t.contents, i).decode('ascii', 'ignore')
            if data:
                info_dict[i] = data

        _gme.gme_free_info(info_t)

        return info_dict

    def track_info(self, track: int) -> dict:
        """Return the info about the track."""
        return self._track_info[track]

    def read(self, size: int = -1) -> bytes:
        """Read size bytes and return a bytes object."""
        if self._closed:
            raise IOError("Can't read from closed file.")

        if self.track_ended():
            return b''

        c_buffer = (_gme.ctypes.c_short * size)()

        self.play(size, c_buffer)

        return _gme.string_at(c_buffer, _gme.sizeof(c_buffer))

    def _open(self, filename: str, sample_rate: int) -> Any:
        """Wrap the _gme.gme_open_file function."""
        filename_b = filename.encode('utf-8', 'surrogateescape')

        music_emu = _gme.ctypes.POINTER(_gme.Music_Emu)()

        _err(_gme.gme_open_file(
            filename_b,
            _gme.ctypes.byref(music_emu),
            sample_rate
        ))

        return music_emu

    def close(self):
        """Cleanup."""
        self.delete()
        self._closed = True
