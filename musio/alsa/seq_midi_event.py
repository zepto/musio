#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides access to alsa seq midi event.
# Copyright (C) 2010 Josiah Gordon <josiahg@gmail.com>
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


""" An alsa seq midi event module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .seq_event import *

#
#  \defgroup MIDI_Event Sequencer event <-> MIDI byte stream coder
#  \ingroup Sequencer
#  Sequencer event <-> MIDI byte stream coder
#  \{
#

# container for sequencer midi event parsers 
class snd_midi_event(Structure):
    _fields_ = [
            ]
snd_midi_event_t = snd_midi_event 

#int snd_midi_event_new(size_t bufsize, snd_midi_event_t **rdev);
snd_midi_event_new = _alsa_lib.snd_midi_event_new
snd_midi_event_new.argtypes = [c_size_t, POINTER(POINTER(snd_midi_event_t))]
snd_midi_event_new.restype = c_int

#int snd_midi_event_resize_buffer(snd_midi_event_t *dev, size_t bufsize);
snd_midi_event_resize_buffer = _alsa_lib.snd_midi_event_resize_buffer
snd_midi_event_resize_buffer.argtypes = [POINTER(snd_midi_event_t), c_size_t]
snd_midi_event_resize_buffer.restype = c_int

#void snd_midi_event_free(snd_midi_event_t *dev);
snd_midi_event_free = _alsa_lib.snd_midi_event_free
snd_midi_event_free.argtypes = [POINTER(snd_midi_event_t)]
snd_midi_event_free.restype = None

#void snd_midi_event_init(snd_midi_event_t *dev);
snd_midi_event_init = _alsa_lib.snd_midi_event_init
snd_midi_event_init.argtypes = [POINTER(snd_midi_event_t)]
snd_midi_event_init.restype = None

#void snd_midi_event_reset_encode(snd_midi_event_t *dev);
snd_midi_event_reset_encode = _alsa_lib.snd_midi_event_reset_encode
snd_midi_event_reset_encode.argtypes = [POINTER(snd_midi_event_t)]
snd_midi_event_reset_encode.restype = None

#void snd_midi_event_reset_decode(snd_midi_event_t *dev);
snd_midi_event_reset_decode = _alsa_lib.snd_midi_event_reset_decode
snd_midi_event_reset_decode.argtypes = [POINTER(snd_midi_event_t)]
snd_midi_event_reset_decode.restype = None

#void snd_midi_event_no_status(snd_midi_event_t *dev, int on);
snd_midi_event_no_status = _alsa_lib.snd_midi_event_no_status
snd_midi_event_no_status.argtypes = [POINTER(snd_midi_event_t), c_int]
snd_midi_event_no_status.restype = None

# encode from byte stream - return number of written bytes if success 
#long snd_midi_event_encode(snd_midi_event_t *dev, const unsigned char *buf, long count, snd_seq_event_t *ev);
snd_midi_event_encode = _alsa_lib.snd_midi_event_encode
snd_midi_event_encode.argtypes = [POINTER(snd_midi_event_t), POINTER(c_ubyte), c_long, POINTER(snd_seq_event_t)]
snd_midi_event_encode.restype = c_long

#int snd_midi_event_encode_byte(snd_midi_event_t *dev, int c, snd_seq_event_t *ev);
snd_midi_event_encode_byte = _alsa_lib.snd_midi_event_encode_byte
snd_midi_event_encode_byte.argtypes = [POINTER(snd_midi_event_t), c_int, POINTER(snd_seq_event_t)]
snd_midi_event_encode_byte.restype = c_int

# decode from event to bytes - return number of written bytes if success 
#long snd_midi_event_decode(snd_midi_event_t *dev, unsigned char *buf, long count, const snd_seq_event_t *ev);
snd_midi_event_decode = _alsa_lib.snd_midi_event_decode
snd_midi_event_decode.argtypes = [POINTER(snd_midi_event_t), POINTER(c_ubyte), c_long, POINTER(snd_seq_event_t)]
snd_midi_event_decode.restype = c_long
