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
from .io_util import silence, msg_out
# from .espeak import _espeak
from .import_util import LazyImport

_espeak = LazyImport('espeak._espeak', globals(), locals(), ['_espeak'], 1)

__supported_dict = {
    'output': [str],
    'input': [None],
    'handler': 'Espeak',
    'default': True,
    'dependencies': {'ctypes': ['espeak'], 'python': []}
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

        output = _espeak.AUDIO_OUTPUT_PLAYBACK
        rate = self._err_check(_espeak.espeak_Initialize(output, 0, None, 0))

        super(Espeak, self).__init__(mode='w', depth=16,  rate=rate,
                                     channels=1)

        self._voice = voice
        self.voice = voice

        self._closed = False

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='%(_mode)s', voice='%(_voice)s'" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def _err_check(self, ret_val):
        """ Checks the 'ret_val' for error status (<0) and prints and error
        message.  Returns 'ret_val' for the calling function to use.

        """
        try:
            assert(ret_val >= 0)
        except Exception as err:
            msg_out("There was and error %s %s" % (err, ret_val), file=sys_stderr)

        return ret_val

    @property
    def range(self):
        """ The current inflection range.

        """

        return _espeak.espeak_GetParameter(_espeak.espeakRANGE, 1)

    @range.setter
    def range(self, value):
        """ Set the inflection range.

        """

        self._err_check(_espeak.espeak_SetParameter(_espeak.espeakRANGE,
                                                    int(value), 0))

    @property
    def pitch(self):
        """ The current pitch.

        """

        return _espeak.espeak_GetParameter(_espeak.espeakPITCH, 1)

    @pitch.setter
    def pitch(self, value):
        """ Set the pitch.

        """

        self._err_check(_espeak.espeak_SetParameter(_espeak.espeakPITCH,
                                                    int(value), 0))

    @property
    def volume(self):
        """ The current volume.

        """

        return _espeak.espeak_GetParameter(_espeak.espeakVOLUME, 1)

    @volume.setter
    def volume(self, value):
        """ Set the pitch.

        """

        self._err_check(_espeak.espeak_SetParameter(_espeak.espeakVOLUME,
                                                    int(value), 0))

    @property
    def speed(self):
        """ The current rate.

        """

        return _espeak.espeak_GetParameter(_espeak.espeakRATE, 1)

    @speed.setter
    def speed(self, value):
        """ Set the rate.

        """

        self._err_check(_espeak.espeak_SetParameter(_espeak.espeakRATE,
                                                    int(value), 0))

    @property
    def voice(self):
        """ The current voice.

        """

        voice = _espeak.espeak_GetCurrentVoice()
        return voice.contents.languages[1:].decode()

    @voice.setter
    def voice(self, value):
        """ Set the espeak voice.

        """

        self._voice = value

        if not isinstance(value, bytes):
            value = value.encode()

        self._err_check(_espeak.espeak_SetVoiceByName(value))

    def list_voices(self):
        """ Print a list of available voices.

        """

        voices = _espeak.espeak_ListVoices(None)
        print("%-21s %-22s %s" % ("Language", "Name", "Identifier"))
        print('-'*55)
        for voice in voices:
            if not voice:
                break
            voice = voice.contents
            lang = voice.languages.decode()
            name = voice.name.decode()
            ident = voice.identifier.decode()
            print("%-22s %-22s %s" % (lang, name, ident))

    def close(self):
        """ Stop speaking.

        """

        if not self.closed:
            self._err_check(_espeak.espeak_Cancel())
            self._err_check(_espeak.espeak_Terminate())

            self._closed = True

    def flush(self):
        """ Wait for playing to stop.

        """

        while bool(_espeak.espeak_IsPlaying()):
            time_sleep(0.02)

    @io_wrapper
    def write(self, data: str) -> int:
        """ write(data) -> Make espeak say data if it is printable.

        """

        # Return 0 if no data was given.
        if not data: return 0

        # Convert data to type str.
        if type(data) is int:
            data = str(data)
        elif type(data) is bytes:
            data = data.decode()
        elif type(data) in (list, tuple, range):
            data = ' '.join([str(i) for i in data])
        elif type(data) is not str:
            return 0

        # Cleanup the input and get its length.
        text = data.strip().encode() + b'\0'
        text_length = len(text)

        # Silence stderr
        with silence(sys_stderr):
            # Speak the text.
            self._err_check(_espeak.espeak_Synth(text, text_length, 0,
                                                 _espeak.POS_CHARACTER, 0,
                                                 _espeak.espeakCHARS_UTF8,
                                                 None, None))

            # Flush output buffer before returning
            self.flush()

        return text_length
