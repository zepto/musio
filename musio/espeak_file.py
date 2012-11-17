#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A TTS module using the espeak library.
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


""" A TTS module using the espeak library.

"""

from functools import wraps as functools_wraps

from .io_base import AudioIO, io_wrapper
# from .espeak import espeak as  _espeak
from .import_util import LazyImport

_espeak = LazyImport('espeak.espeak', globals(), locals(), ['_espeak'], 1)

__supported_dict = {
        'ext': ['.txt'],
        'handler': 'EspeakFile',
        # 'default': True
        'dependencies': {
            'ctypes': ['espeak'],
            'python': []
            }
        }


class EspeakFile(AudioIO):
    """ Espeak wrapper for text to speech synthesis

    """

    # Valid bit depths.
    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, **kwargs):
        """ Espeak tts object.

        """

        rate = _espeak.init(_espeak._espeak.AUDIO_OUTPUT_RETRIEVAL)

        super(EspeakFile, self).__init__(filename, 'r', 16, rate, 1)

        with open(self._filename, 'r') as txt_file:
            self._txt = txt_file.read()

        self._closed = False

    @property
    def range(self):
        """ The current inflection range.

        """

        return _espeak.get_range()

    @range.setter
    def range(self, value):
        """ Set the inflection range.

        """

        _espeak.set_range(value)

    @property
    def pitch(self):
        """ The current pitch.

        """

        return _espeak.get_pitch()

    @pitch.setter
    def pitch(self, value):
        """ Set the pitch.

        """

        _espeak.set_pitch(value)

    @property
    def volume(self):
        """ The current volume.

        """

        return _espeak.get_volume()

    @volume.setter
    def volume(self, value):
        """ Set the pitch.

        """

        _espeak.set_volume(value)

    @property
    def speed(self):
        """ The current rate.

        """

        return _espeak.get_speed()

    @speed.setter
    def speed(self, value):
        """ Set the rate.

        """

        _espeak.set_speed(value)

    @property
    def voice(self):
        """ The current voice.

        """

        return _espeak.get_voice()

    @voice.setter
    def voice(self, value):
        """ Set the espeak voice.

        """

        _espeak.set_voice(value)

    @property
    def isplaying(self):
        """ Is it speaking.

        """

        return _espeak.speaking #isplaying()

    def list_voices(self):
        """ Print a list of available voices.

        """

        _espeak.list_voices()

    def close(self):
        """ Stop speaking.

        """

        _espeak.close()

        self._closed = True

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ Read from the global data buffer.

        """

        if not _espeak.speaking and not _espeak.done:
            _espeak.speak_text(self._txt)

        data = b''
        size = 4096

        while len(data) < size:
            size -= len(data)
            data = _espeak.read(size)

            if not data:
                if self._loops == -1 or self._loop_count < self._loops:
                    self._loop_count += 1
                    _espeak.speak_text(self._txt)
                    continue
                else:
                    break

        return data
