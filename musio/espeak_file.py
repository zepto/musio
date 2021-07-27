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


"""A TTS module using the espeak library."""

from sys import stderr as sys_stderr
from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

_espeak = LazyImport('espeak._espeak', globals(), locals(), ['_espeak'], 1)


def issupported(filename, *_):
    """Return True if file is supported else False."""
    import mimetypes

    # Initialize mimetypes.
    mimetypes.init()

    # Get the mime type of filename.
    mimetype, _ = mimetypes.guess_type(filename)

    # If no mimtype was found then filename is not supported.
    if not mimetype:
        return False

    # File containing text are supported.
    return True if 'text' in mimetype else False


__supported_dict = {
    'ext': ['.txt'],
    'issupported': issupported,
    'handler': 'EspeakFile',
    # 'default': True,
    'dependencies': {
        'ctypes': ['espeak'],
        'python': []
    }
}


class EspeakFile(AudioIO):
    """Espeak wrapper for text to speech synthesis."""

    # Valid bit depths.
    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, mode: str = 'r', voice: str = 'en-us',
                 **_):
        """Espeak tts object."""
        # Initialize espeak and get the sample rate.
        output = _espeak.AUDIO_OUTPUT_RETRIEVAL
        rate = self._err_check(_espeak.espeak_Initialize(output, 0, None, 0))

        super(EspeakFile, self).__init__(filename, 'r', 16, rate, 1)

        # Make the buffer big to avoid underruns.
        self._buffer_size = 16384

        self._voice = voice
        self.voice = voice

        self._position = 0
        self._data_buffer = b''
        self._speaking = False
        self._done = False

        # Set the retrieval callback
        self._espeak_synth_callback = _espeak.t_espeak_callback(self)
        _espeak.espeak_SetSynthCallback(self._espeak_synth_callback)

        self._closed = False

    def _open(self):
        """Open the classes file and set it up for read/write access."""
        # Get the file and length
        text = ''
        with open(self._filename, 'r') as txt_file:
            text = txt_file.read()

            text = text.strip().encode() + b'\0'
            text_length = len(text)

            # Speak the file
            self._err_check(
                _espeak.espeak_Synth(
                    text,
                    text_length,
                    0,
                    _espeak.POS_CHARACTER,
                    0,
                    _espeak.espeakCHARS_UTF8,
                    None,
                    None
                )
            )

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'mode="{self._mode}", voice="{self._voice}")')

    def __call__(self, wav: Any, numsamples: int, _: Any) -> int:
        """Make the class callable.

        Make this class callable so it can be called as the espeak synth
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

    def _err_check(self, ret_val: int) -> int:
        """Check for errors.

        Check the 'ret_val' for error status (<0) and prints and error message.
        Returns 'ret_val' for the calling function to use.
        """
        try:
            assert(ret_val >= 0)
        except Exception as err:
            msg_out(f"There was and error {err} {ret_val}", file=sys_stderr)

        return ret_val

    def _get_position(self) -> int:
        """Return the current position."""
        return self._position

    def _set_position(self, position: int):
        """Change the position of playback."""
        if position <= self._length:
            self._position = position

    @property
    def range(self) -> int:
        """Return the current inflection range."""
        return _espeak.espeak_GetParameter(_espeak.espeakRANGE, 1)

    @range.setter
    def range(self, value: int):
        """Set the inflection range."""
        self._err_check(
            _espeak.espeak_SetParameter(_espeak.espeakRANGE, int(value), 0)
        )

    @property
    def pitch(self) -> int:
        """Return the current pitch."""
        return _espeak.espeak_GetParameter(_espeak.espeakPITCH, 1)

    @pitch.setter
    def pitch(self, value: int):
        """Set the pitch."""
        self._err_check(
            _espeak.espeak_SetParameter(_espeak.espeakPITCH, int(value), 0)
        )

    @property
    def volume(self) -> int:
        """Return the current volume."""
        return _espeak.espeak_GetParameter(_espeak.espeakVOLUME, 1)

    @volume.setter
    def volume(self, value: int):
        """Set the pitch."""
        self._err_check(
            _espeak.espeak_SetParameter(_espeak.espeakVOLUME, int(value), 0)
        )

    @property
    def speed(self) -> int:
        """Return the current rate."""
        return _espeak.espeak_GetParameter(_espeak.espeakRATE, 1)

    @speed.setter
    def speed(self, value: int):
        """Set the rate."""
        self._err_check(
            _espeak.espeak_SetParameter(_espeak.espeakRATE, int(value), 0)
        )

    @property
    def voice(self) -> str:
        """Return the current voice."""
        voice = _espeak.espeak_GetCurrentVoice()
        return voice.contents.languages[1:].decode()

    @voice.setter
    def voice(self, value: str):
        """Set the espeak voice."""
        self._voice = value

        voice_b = value.encode()

        self._err_check(_espeak.espeak_SetVoiceByName(voice_b))

    @property
    def isspeaking(self) -> bool:
        """Is it speaking."""
        return self._speaking

    def list_voices(self):
        """Print a list of available voices."""
        voices = _espeak.espeak_ListVoices(None)
        print(f'{"Language":21} {"Name":22} Identifier')
        print(f'{"-":->55}')
        for voice in voices:
            if not voice:
                break
            voice = voice.contents
            lang = voice.languages.decode()
            name = voice.name.decode()
            ident = voice.identifier.decode()
            print(f'{lang:22} {name:22} {ident}')

    def close(self):
        """Stop speaking."""
        if not self.closed:
            self._speaking = False

            self._err_check(_espeak.espeak_Cancel())
            self._err_check(_espeak.espeak_Terminate())

            self._closed = True

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read from the data buffer."""
        # Start speaking
        if not self._done and not self._speaking:
            self._speaking = True
            self._open()

        # Data buffer for
        data = b''

        while len(data) < size:
            size -= len(data)
            data += self._data_buffer[self._position:self._position + size]
            self._position += len(data)

            # Check if the file is finished
            if self._position == self._length and self._done:
                # Loop if necessary
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        # Fill data buffer until it is the requested
                        # size.
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    # Increment the loop counter and seek to the start
                    self._loop_count += 1
                    self.seek(0)
                    continue

        return data
