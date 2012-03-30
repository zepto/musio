#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa output.
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


""" Alsa output.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *

#
#  \defgroup Output Output Interface
#
#  The output functions present an interface similar to the stdio functions
#  on top of different underlying output destinations.
#
#  Many PCM debugging functions (\c snd_pcm_xxx_dump_xxx) use such an output
#  handle to be able to write not only to the screen but also to other
#  destinations, e.g. to files or to memory buffers.
#
#  \{
#

#
# \brief Internal structure for an output object.
#
# The ALSA library uses a pointer to this structure as a handle to an
# output object. Applications don't access its contents directly.
#
class _snd_output(Structure):
    _fields_ = [
            ]
snd_output_t = _snd_output 

# Output type. 
_snd_output_type = c_int
# Output to a stdio stream. 
SND_OUTPUT_STDIO = 0
# Output to a memory buffer. 
SND_OUTPUT_BUFFER = 1
snd_output_type_t = _snd_output_type

#int snd_output_stdio_open(snd_output_t **outputp, const char *file, const char *mode);
snd_output_stdio_open = _alsa_lib.snd_output_stdio_open
snd_output_stdio_open.argtypes = [POINTER(POINTER(snd_output_t)), c_char_p, c_char_p]
snd_output_stdio_open.restype = c_int

#int snd_output_stdio_attach(snd_output_t **outputp, FILE *fp, int _close);
snd_output_stdio_attach = _alsa_lib.snd_output_stdio_attach
snd_output_stdio_attach.argtypes = [POINTER(POINTER(snd_output_t)), POINTER(FILE), c_int]
snd_output_stdio_attach.restype = c_int

#int snd_output_buffer_open(snd_output_t **outputp);
snd_output_buffer_open = _alsa_lib.snd_output_buffer_open
snd_output_buffer_open.argtypes = [POINTER(POINTER(snd_output_t))]
snd_output_buffer_open.restype = c_int

#size_t snd_output_buffer_string(snd_output_t *output, char **buf);
snd_output_buffer_string = _alsa_lib.snd_output_buffer_string
snd_output_buffer_string.argtypes = [POINTER(snd_output_t), POINTER(c_char_p)]
snd_output_buffer_string.restype = c_size_t

#int snd_output_close(snd_output_t *output);
snd_output_close = _alsa_lib.snd_output_close
snd_output_close.argtypes = [POINTER(snd_output_t)]
snd_output_close.restype = c_int

#int snd_output_printf(snd_output_t *output, const char *format, ...)
snd_output_printf = _alsa_lib.snd_output_printf
snd_output_printf.argtypes = [POINTER(snd_output_t), c_char_p]
snd_output_printf.restype = c_int

#ifndef DOC_HIDDEN
	#__attribute__ ((format (printf, 2, 3)))
#endif
	#;
#int snd_output_vprintf(snd_output_t *output, const char *format, va_list args);
snd_output_vprintf = _alsa_lib.snd_output_vprintf
snd_output_vprintf.argtypes = [POINTER(snd_output_t), c_char_p, va_list]
snd_output_vprintf.restype = c_int

#int snd_output_puts(snd_output_t *output, const char *str);
snd_output_puts = _alsa_lib.snd_output_puts
snd_output_puts.argtypes = [POINTER(snd_output_t), c_char_p]
snd_output_puts.restype = c_int

#int snd_output_putc(snd_output_t *output, int c);
snd_output_putc = _alsa_lib.snd_output_putc
snd_output_putc.argtypes = [POINTER(snd_output_t), c_int]
snd_output_putc.restype = c_int

#int snd_output_flush(snd_output_t *output);
snd_output_flush = _alsa_lib.snd_output_flush
snd_output_flush.argtypes = [POINTER(snd_output_t)]
snd_output_flush.restype = c_int
