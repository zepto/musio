#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides alsa error.
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


""" An alsa error module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .alsa_conf import *

#
#  \defgroup Error Error handling
#  Error handling macros and functions.
#  \{
#

SND_ERROR_BEGIN = 500000 # *< Lower boundary of sound error codes. 
SND_ERROR_INCOMPATIBLE_VERSION = (SND_ERROR_BEGIN+0) # *< Kernel/library protocols are not compatible. 
SND_ERROR_ALISP_NIL = (SND_ERROR_BEGIN+1)	# *< Lisp encountered an error during acall. 

#const char *snd_strerror(int errnum);
snd_strerror = _alsa_lib.snd_strerror
snd_strerror.argtypes = [c_int]
snd_strerror.restype = c_char_p


#
# \brief Error handler callback.
# \param file Source file name.
# \param line Line number.
# \param function Function name.
# \param err Value of \c errno, or 0 if not relevant.
# \param fmt \c printf(3) format.
# \param ... \c printf(3) arguments.
#
# A function of this type is called by the ALSA library when an error occurs.
# This function usually shows the message on the screen, and/or logs it.
#
#typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...)  __attribute__ ((format (printf, 5, 6))) ;
snd_lib_error_handler_t = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

#extern snd_lib_error_handler_t snd_lib_error;
snd_lib_error = snd_lib_error_handler_t.in_dll(_alsa_lib, 'snd_lib_error')

#extern int snd_lib_error_set_handler(snd_lib_error_handler_t handler);
snd_lib_error_set_handler = _alsa_lib.snd_lib_error_set_handler
snd_lib_error_set_handler.argtypes = [snd_lib_error_handler_t]
snd_lib_error_set_handler.restype = c_int
