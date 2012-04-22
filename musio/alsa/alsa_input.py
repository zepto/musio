#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa input.
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


""" Alsa input.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *

#
#  \defgroup Input Input Interface
#
#  The input functions present an interface similar to the stdio functions
#  on top of different underlying input sources.
#
#  The #snd_config_load function uses such an input handle to be able to
#  load configurations not only from standard files but also from other
#  sources, e.g. from memory buffers.
#
#  \{
#

#
# \brief Internal structure for an input object.
#
# The ALSA library uses a pointer to this structure as a handle to an
# input object. Applications don't access its contents directly.
#
class _snd_input(Structure):
    _fields_ = [
            ]
snd_input_t = _snd_input 

# Input type. 
_snd_input_type = c_int
# Input from a stdio stream. 
SND_INPUT_STDIO = 0
# Input from a memory buffer. 
SND_INPUT_BUFFER = 1
snd_input_type_t = _snd_input_type 

#int snd_input_stdio_open(snd_input_t **inputp, const char *file, const char *mode);
snd_input_stdio_open = _alsa_lib.snd_input_stdio_open
snd_input_stdio_open.argtypes = [POINTER(POINTER(snd_input_t)), c_char_p, c_char_p]
snd_input_stdio_open.restype = c_int

#int snd_input_stdio_attach(snd_input_t **inputp, FILE *fp, int _close);
snd_input_stdio_attach = _alsa_lib.snd_input_stdio_attach
snd_input_stdio_attach.argtypes = [POINTER(POINTER(snd_input_t)), POINTER(FILE), c_int]
snd_input_stdio_attach.restype = c_int

#int snd_input_buffer_open(snd_input_t **inputp, const char *buffer, ssize_t size);
snd_input_buffer_open = _alsa_lib.snd_input_buffer_open
snd_input_buffer_open.argtypes = [POINTER(POINTER(snd_input_t)), c_char_p, c_size_t]
snd_input_buffer_open.restype = c_int

#int snd_input_close(snd_input_t *input);
snd_input_close = _alsa_lib.snd_input_close
snd_input_close.argtypes = [POINTER(snd_input_t)]
snd_input_close.restype = c_int

#int snd_input_scanf(snd_input_t *input, const char *format, ...)
snd_input_scanf = _alsa_lib.snd_input_scanf
snd_input_scanf.argtypes = [POINTER(snd_input_t), c_char_p]
snd_input_scanf.restype = c_int

#ifndef DOC_HIDDEN
	#__attribute__ ((format (scanf, 2, 3)))
#endif
	#;
#char *snd_input_gets(snd_input_t *input, char *str, size_t size);
snd_input_gets = _alsa_lib.snd_input_gets
snd_input_gets.argtypes = [POINTER(snd_input_t), c_char_p, c_size_t]
snd_input_gets.restype = c_char_p

#int snd_input_getc(snd_input_t *input);
snd_input_getc = _alsa_lib.snd_input_getc
snd_input_getc.argtypes = [POINTER(snd_input_t)]
snd_input_getc.restype = c_int

#int snd_input_ungetc(snd_input_t *input, int c);
snd_input_ungetc = _alsa_lib.snd_input_ungetc
snd_input_ungetc.argtypes = [POINTER(snd_input_t), c_int]
snd_input_ungetc.restype = c_int
