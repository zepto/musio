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

from time import sleep as time_sleep
from sys import stderr as sys_stderr

from .io_base import DevIO, io_wrapper
from .io_util import silence
from .espeak import espeak as _espeak
# from .import_util import LazyImport
# 
# _espeak = LazyImport('espeak.espeak', globals(), locals(), ['_espeak'], 0)

__supported_dict = {
        'output': [str],
        'input': [None],
        'handler': 'Espeak',
        'default': True
        }


class Espeak(DevIO):
    """ Provide write access to espeak.

    """

    # Only supports writing
    _supported_modes = 'w'

    # Only supports depth 16
    _valid_depth = (16,)

    def __init__(self, mode='w', voice='en-us', **kwargs):
        """ Espeak(mode='w', voice='en-us') -> Open espeak and set it up for
        writing.

        """

        rate = _espeak.init()

        super(Espeak, self).__init__(mode='w', depth=16,  rate=rate,
                                     channels=1)

        self._voice = voice
        _espeak.set_voice(voice)

        self._closed = False

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='%(_mode)s', voice='%(_voice)s'" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    @property
    def range(self):
        """ The current inflection range.

        """

        return _espeak.get_range()

    @range.setter
    def range(self, value):
        """ Set the inflection range.

        """

        _espeak.set_range(int(value))

    @property
    def pitch(self):
        """ The current pitch.

        """

        return _espeak.get_pitch()

    @pitch.setter
    def pitch(self, value):
        """ Set the pitch.

        """

        _espeak.set_pitch(int(value))

    @property
    def volume(self):
        """ The current volume.

        """

        return _espeak.get_volume()

    @volume.setter
    def volume(self, value):
        """ Set the pitch.

        """

        _espeak.set_volume(int(value))

    @property
    def speed(self):
        """ The current rate.

        """

        return _espeak.get_speed()

    @speed.setter
    def speed(self, value):
        """ Set the rate.

        """

        _espeak.set_speed(int(value))

    @property
    def voice(self):
        """ The current voice.

        """

        return _espeak.get_voice()

    @voice.setter
    def voice(self, value):
        """ Set the espeak voice.

        """

        self._voice = value
        _espeak.set_voice(value)

    def list_voices(self):
        """ Print a list of available voices.

        """

        _espeak.list_voices()

    def close(self):
        """ Stop speaking.

        """

        if not self.closed:
            _espeak.close()

            self._closed = True

    def flush(self):
        """ Wait for playing to stop.

        """

        while _espeak.isplaying():
            time_sleep(0.02)

    @io_wrapper
    def write(self, data: str) -> int:
        """ write(data) -> Make espeak say data if it is printable.

        """

        # Convert data to type str.
        if type(data) is int:
            data = str(data)
        elif type(data) is bytes:
            data = data.decode()
        elif type(data) in (list, tuple, range):
            data = ' '.join([str(i) for i in data])
        elif type(data) is not str:
            return 0

        # Silence stderr
        with silence(sys_stderr):
            return_val = _espeak.speak_text(data)

            # Flush output buffer before returning
            self.flush()

        return return_val
