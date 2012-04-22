#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa lisp.
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


""" Alsa lisp.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *

class alisp_cfg(Structure):
    _fields_ = [
            ('verbose', c_int), #int verbose: 1,
            ('warning', c_int), # warning: 1,
            ('debug', c_int), # debug: 1;
            ('in', POINTER(snd_input_t)), #  program code 
            ('out', POINTER(snd_output_t)), #  program output 
            ('eout', POINTER(snd_output_t)), #  error output 
            ('vout', POINTER(snd_output_t)), #  verbose output 
            ('wout', POINTER(snd_output_t)), #  warning output 
            ('dout', POINTER(snd_output_t)), #  debug output 
            ]

class alisp_instance(Structure):
    _fields_ = [
            ]
class alisp_object(Structure):
    _fields_ = [
            ]
class alisp_seq_iterator(Structure):
    _fields_ = [
            ]

#struct alisp_cfg *alsa_lisp_default_cfg(snd_input_t *input);
alsa_lisp_default_cfg = _alsa_lib.alsa_lisp_default_cfg
alsa_lisp_default_cfg.argtypes = [POINTER(snd_input_t)]
alsa_lisp_default_cfg.restype = POINTER(alisp_cfg)

#void alsa_lisp_default_cfg_free(struct alisp_cfg *cfg);
alsa_lisp_default_cfg_free = _alsa_lib.alsa_lisp_default_cfg_free
alsa_lisp_default_cfg_free.argtypes = [POINTER(alisp_cfg)]
alsa_lisp_default_cfg_free.restype = None

#int alsa_lisp(struct alisp_cfg *cfg, struct alisp_instance **instance);
alsa_lisp = _alsa_lib.alsa_lisp
alsa_lisp.argtypes = [POINTER(alisp_cfg), POINTER(POINTER(alisp_instance))]
alsa_lisp.restype = c_int

#void alsa_lisp_free(struct alisp_instance *instance);
alsa_lisp_free = _alsa_lib.alsa_lisp_free
alsa_lisp_free.argtypes = [POINTER(alisp_instance)]
alsa_lisp_free.restype = None

#int alsa_lisp_function(struct alisp_instance *instance, struct alisp_seq_iterator **result,
			   #const char *id, const char *args, ...)
alsa_lisp_function = _alsa_lib.alsa_lisp_function
alsa_lisp_function.argtypes = [POINTER(alisp_instance), POINTER(POINTER(alisp_seq_iterator))]
alsa_lisp_function.restype = c_int

#ifndef DOC_HIDDEN
			   #__attribute__ ((format (printf, 4, 5)))
#endif
			   #;
#void alsa_lisp_result_free(struct alisp_instance *instance,
			   #struct alisp_seq_iterator *result);
alsa_lisp_result_free = _alsa_lib.alsa_lisp_result_free
alsa_lisp_result_free.argtypes = [POINTER(alisp_instance), POINTER(alisp_seq_iterator)]
alsa_lisp_result_free.restype = None

#int alsa_lisp_seq_first(struct alisp_instance *instance, const char *id,
			#struct alisp_seq_iterator **seq);
alsa_lisp_seq_first = _alsa_lib.alsa_lisp_seq_first
alsa_lisp_seq_first.argtypes = [POINTER(alisp_instance), c_char_p, POINTER(POINTER(alisp_seq_iterator))]
alsa_lisp_seq_first.restype = c_int

#int alsa_lisp_seq_next(struct alisp_seq_iterator **seq);
alsa_lisp_seq_next = _alsa_lib.alsa_lisp_seq_next
alsa_lisp_seq_next.argtypes = [POINTER(POINTER(alisp_seq_iterator))]
alsa_lisp_seq_next.restype = c_int

#int alsa_lisp_seq_count(struct alisp_seq_iterator *seq);
alsa_lisp_seq_count = _alsa_lib.alsa_lisp_seq_count
alsa_lisp_seq_count.argtypes = [POINTER(alisp_seq_iterator)]
alsa_lisp_seq_count.restype = c_int

#int alsa_lisp_seq_integer(struct alisp_seq_iterator *seq, long *val);
alsa_lisp_seq_integer = _alsa_lib.alsa_lisp_seq_integer
alsa_lisp_seq_integer.argtypes = [POINTER(alisp_seq_iterator), POINTER(c_long)]
alsa_lisp_seq_integer.restype = c_int

#int alsa_lisp_seq_pointer(struct alisp_seq_iterator *seq, const char *ptr_id, void **ptr);
alsa_lisp_seq_pointer = _alsa_lib.alsa_lisp_seq_pointer
alsa_lisp_seq_pointer.argtypes = [POINTER(alisp_seq_iterator), c_char_p, POINTER(c_void_p)]
alsa_lisp_seq_pointer.restype = c_int

