#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# An object for accessing espeak synthesised audio data.
# Copyright (C) 2013 Josiah Gordon <josiahg@gmail.com>
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


""" An object for accessing espeak synthesised audio data.

"""

from functools import wraps as functools_wraps
from sys import stderr as sys_stderr

from .io_base import AudioIO, io_wrapper
from .io_util import silence, msg_out
from .import_util import LazyImport

_espeak = LazyImport('espeak._espeak', globals(), locals(), ['_espeak'], 1)
# from .espeak import _espeak

_espeak = LazyImport('espeak._espeak', globals(), locals(), ['_espeak'], 1)


__supported_dict = {
    'output': [str],
    'input': [bytes],
    'handler': 'EspeakText',
    'default': True,
    'dependencies': {'ctypes': ['espeak'], 'python': []}
}


class EspeakText(AudioIO):
    """ Espeak wrapper for text to speech synthesis

    """

    # Only supports depth 16
    _valid_depth = (16,)

    def __init__(self, text: str, voice: str='en-us', **kwargs):
        """ Espeak tts object.

        """

        # Initialize espeak and get the sample rate.
        output = _espeak.AUDIO_OUTPUT_RETRIEVAL
        rate = self._err_check(_espeak.espeak_Initialize(output, 0, None,
                                                         0))

        super(EspeakText, self).__init__(filename='', mode='rw', depth=16,
                                         rate=rate, channels=1)

        self._text = text

        self._voice = voice
        self.voice = voice

        self._position = 0
        self._data_buffer = b''
        self._speaking = False
        self._done = False
        self._buffer_size = 8192

        # Set the retrieval callback
        self._espeak_synth_callback = _espeak.t_espeak_callback(self)
        _espeak.espeak_SetSynthCallback(self._espeak_synth_callback)

        self._closed = False

        self._speak(text)

    def _speak(self, text):
        """ _open() -> Open the classes file and set it up for read/write
        access.

        """

        self._speaking = True

        text = text.strip().encode() + b'\0'
        text_length = len(text)

        # Speak the file
        self._err_check(_espeak.espeak_Synth(text, text_length, 0,
                                             _espeak.POS_CHARACTER, 0,
                                             _espeak.espeakCHARS_UTF8,
                                             None, None))

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "text='%(_text)s', voice='%(_voice)s'" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def __getitem__(self, item):
        """ Return the attribute.

        """

        return getattr(self, item)

    def __call__(self, wav, numsamples, events):
        """ Make the class callable so it can be called as the espeak synth
        callback.

        """

        # Stop if the end of the synthesis is reached.
        if not wav:
            self._done = True
            self._speaking = False
            return 1

        # Append the data to the buffer.
        self._data_buffer += _espeak.string_at(wav, numsamples *
                                               _espeak.sizeof(_espeak.c_short))

        # Update length
        self._length = len(self._data_buffer)

        # Return value 0 means to keep playing 1 means to stop.
        return 0 if self._speaking else 1

    def _err_check(self, ret_val):
        """ Checks the 'ret_val' for error status (<0) and prints and error
        message.  Returns 'ret_val' for the calling function to use.

        """
        try:
            assert(ret_val >= 0)
        except Exception as err:
            print("There was and error %s %s" % (err, ret_val),
                  file=sys_stderr)

        return ret_val

    def _get_position(self) -> int:
        """ Returns the current position.

        """

        return self._position

    def _set_position(self, position: int):
        """ Change the position of playback.

        """

        if position <= self._length:
            self._position = position

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

    @property
    def isspeaking(self):
        """ Is it speaking.

        """

        return self._speaking

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
            self._speaking = False

            self._err_check(_espeak.espeak_Cancel())
            self._err_check(_espeak.espeak_Terminate())

            self._closed = True

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

        self._text = data

        # Silence stderr
        with silence(sys_stderr):
            # Speak the text.
            self._speak(data)

        return len(data)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ Read from the data buffer.

        """

        # Data buffer for
        data = b''

        while len(data) < size:
            size -= len(data)
            data += self._data_buffer[self._position:self._position + size]
            self._position += len(data)

            # Check if the file is finished
            if self._position == self._length and self._done:
                if data:
                    # Fill data buffer until it is the requested
                    # size.
                    data += b'\x00' * (size - len(data))
                break

        return data
