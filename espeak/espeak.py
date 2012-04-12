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
from sys import stderr as sys_stderr

from . import _espeak

speaking = False
done = False
data_buffer = b''
pos = 0

def _espeak_callback(wav, numsamples, events):
    """ Callback for espeak wav data retrieval.

    """

    global speaking, data_buffer, done

    if wav:
        data_buffer += _espeak.string_at(wav, numsamples *
                                         _espeak.sizeof(_espeak.c_short))
    else:
        speaking = False
        done = True

    # Return value 0 means to keep playing 1 means to stop.
    return 0 if speaking and wav else 1

def init(output=_espeak.AUDIO_OUTPUT_PLAYBACK, callback=_espeak_callback):
    """ init(output=_espeak.AUDIO_OUTPUT_PLAYBACK) -> Initialize espeak and
    return the sample rate.

    """

    rate = _err_check(_espeak.espeak_Initialize(output, 0, None, 0))

    if output == _espeak.AUDIO_OUTPUT_RETRIEVAL:
        espeak_synth_callback = _espeak.t_espeak_callback(callback)
        _espeak.espeak_SetSynthCallback(espeak_synth_callback)

    return rate

def _err_check(ret_val):
    """ Checks the 'ret_val' for error status (<0) and prints and error
    message.  Returns 'ret_val' for the calling function to use.

    """

    try:
        assert(ret_val >= 0)
    except Exception as err:
        print("There was and error %s %s" % (err, ret_val), file=sys_stderr)

    return ret_val

def get_range():
    """ The current inflection range.

    """

    return _espeak.espeak_GetParameter(_espeak.espeakRANGE, 1)

def set_range(value):
    """ Set the inflection range.

    """

    value = int(value)
    _err_check(_espeak.espeak_SetParameter(_espeak.espeakRANGE, value, 0))

def get_pitch():
    """ The current pitch.

    """

    return _espeak.espeak_GetParameter(_espeak.espeakPITCH, 1)

def set_pitch(value):
    """ Set the pitch.

    """

    value = int(value)
    _err_check(_espeak.espeak_SetParameter(_espeak.espeakPITCH, value, 0))

def get_volume():
    """ The current volume.

    """

    return _espeak.espeak_GetParameter(_espeak.espeakVOLUME, 1)

def set_volume(value):
    """ Set the pitch.

    """

    value = int(value)
    _err_check(_espeak.espeak_SetParameter(_espeak.espeakVOLUME, value, 0))

def get_speed():
    """ The current rate.

    """

    return _espeak.espeak_GetParameter(_espeak.espeakRATE, 1)

def set_speed(value):
    """ Set the rate.

    """

    value = int(value)
    _err_check(_espeak.espeak_SetParameter(_espeak.espeakRATE, value, 0))

def get_voice():
    """ The current voice.

    """

    voice = _espeak.espeak_GetCurrentVoice()
    return voice.contents.languages[1:].decode()

def set_voice(value):
    """ Set the espeak voice.

    """

    if type(value) is not bytes:
        value = value.encode()

    _err_check(_espeak.espeak_SetVoiceByName(value))

def isplaying():
    """ Is it speaking.

    """

    return bool(_espeak.espeak_IsPlaying())

def list_voices():
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

def _update_speaking(func):
    """ Update the speaking variable.

    """

    @functools_wraps(func)
    def wrapper(*args):
        """ Wraps the function.

        """

        global speaking

        if func.__name__ != 'close':
            speaking = True
        else:
            speaking = False

        ret_val = func(*args)

        return ret_val

    return wrapper

@_update_speaking
def speak_text(text):
    """ Speak the text to the audio buffer.

    """

    text = text.strip().encode() + b'\0'
    text_length = len(text)
    _err_check(_espeak.espeak_Synth(text, text_length, 0,
                                            _espeak.POS_CHARACTER, 0,
                                            _espeak.espeakCHARS_UTF8, None,
                                            None))

    return text_length

@_update_speaking
def close():
    """ Stop speaking.

    """

    _err_check(_espeak.espeak_Cancel())
    _err_check(_espeak.espeak_Terminate())

def read(size=None):
    """ Read from the global data buffer.

    """

    global data_buffer, pos

    if not size: size = len(data_buffer)

    data = data_buffer[pos:pos+size]
    pos += len(data)

    # data_buffer = data_buffer[len(data):]

    return data
