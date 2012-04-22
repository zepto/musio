#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa conf.
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


""" Alsa conf.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_input import *
from .alsa_output import *

#
#  \defgroup Config Configuration Interface
#  The configuration functions and types allow you to read, enumerate,
#  modify and write the contents of ALSA configuration files.
#  \{
#

# \brief \c dlsym version for the config evaluate callback. 
#define SND_CONFIG_DLSYM_VERSION_EVALUATE	_dlsym_config_evaluate_001
# \brief \c dlsym version for the config hook callback. 
#define SND_CONFIG_DLSYM_VERSION_HOOK		_dlsym_config_hook_001

# \brief Configuration node type. 
_snd_config_type = c_int
# Integer number. 
SND_CONFIG_TYPE_INTEGER = 0
# 64-bit integer number. 
SND_CONFIG_TYPE_INTEGER64 = 1
# Real number. 
SND_CONFIG_TYPE_REAL = 2
# Character string. 
SND_CONFIG_TYPE_STRING = 3
# Pointer (runtime only, cannot be saved). 
SND_CONFIG_TYPE_POINTER = 4 
# Compound node. 
SND_CONFIG_TYPE_COMPOUND = 1024
snd_config_type_t = _snd_config_type 

#
# \brief Internal structure for a configuration node object.
#
# The ALSA library uses a pointer to this structure as a handle to a
# configuration node. Applications don't access its contents directly.
#
class _snd_config(Structure):
    _fields_ = [
            ]
snd_config_t = _snd_config 

#
# \brief Type for a configuration compound iterator.
#
# The ALSA library uses this pointer type as a handle to a configuration
# compound iterator. Applications don't directly access the contents of
# the structure pointed to by this type.
#
class _snd_config_iterator(Structure):
    _fields_ = [
            ]
snd_config_iterator_t = _snd_config_iterator

#
# \brief Internal structure for a configuration private update object.
#
# The ALSA library uses this structure to save private update information.
#
class _snd_config_update(Structure):
    _fields_ = [
            ]
snd_config_update_t = _snd_config_update 

class _snd_config(Structure):
    _fields_ = [
            ]
snd_config_t = _snd_config

#int snd_config_top(snd_config_t **config);
snd_config_top = _alsa_lib.snd_config_top
snd_config_top.argtypes = [POINTER(POINTER(snd_config_t))]
snd_config_top.restype = c_int


#int snd_config_load(snd_config_t *config, snd_input_t *in);
snd_config_load = _alsa_lib.snd_config_load
snd_config_load.argtypes = [POINTER(snd_config_t), POINTER(snd_input_t)]
snd_config_load.restype = c_int

#int snd_config_load_override(snd_config_t *config, snd_input_t *in);
snd_config_load_override = _alsa_lib.snd_config_load_override
snd_config_load_override.argtypes = [POINTER(snd_config_t), POINTER(snd_input_t)]
snd_config_load_override.restype = c_int

#int snd_config_save(snd_config_t *config, snd_output_t *out);
snd_config_save = _alsa_lib.snd_config_save
snd_config_save.argtypes = [POINTER(snd_config_t), POINTER(snd_output_t)]
snd_config_save.restype = c_int

#int snd_config_update(void);
snd_config_update = _alsa_lib.snd_config_update
snd_config_update.argtypes = []
snd_config_update.restype = c_int

#int snd_config_update_r(snd_config_t **top, snd_config_update_t **update, const char *path);
snd_config_update_r = _alsa_lib.snd_config_update_r
snd_config_update_r.argtypes = [POINTER(POINTER(snd_config_t)), POINTER(POINTER(snd_config_update_t)), c_char_p]
snd_config_update_r.restype = c_int

#int snd_config_update_free(snd_config_update_t *update);
snd_config_update_free = _alsa_lib.snd_config_update_free
snd_config_update_free.argtypes = [POINTER(snd_config_update_t)]
snd_config_update_free.restype = c_int

#int snd_config_update_free_global(void);
snd_config_update_free_global = _alsa_lib.snd_config_update_free_global
snd_config_update_free_global.argtypes = []
snd_config_update_free_global.restype = c_int


#int snd_config_search(snd_config_t *config, const char *key,
			  #snd_config_t **result);
snd_config_search = _alsa_lib.snd_config_search
snd_config_search.argtypes = [POINTER(snd_config_t), c_char_p, POINTER(POINTER(snd_config_t))]
snd_config_search.restype = c_int

#int snd_config_searchv(snd_config_t *config, 
			   #snd_config_t **result, ...);
snd_config_searchv = _alsa_lib.snd_config_searchv
snd_config_searchv.argtypes = [POINTER(snd_config_t), POINTER(POINTER(snd_config_t))]
snd_config_searchv.restype = c_int

#int snd_config_search_definition(snd_config_t *config,
				 #const char *base, const char *key,
				 #snd_config_t **result);
snd_config_search_definition = _alsa_lib.snd_config_search_definition
snd_config_search_definition.argtypes = [POINTER(snd_config_t), c_char_p, c_char_p, POINTER(POINTER(snd_config_t))]
snd_config_search_definition.restype = c_int

#int snd_config_expand(snd_config_t *config, snd_config_t *root,
			  #const char *args, snd_config_t *private_data,
			  #snd_config_t **result);
snd_config_expand = _alsa_lib.snd_config_expand
snd_config_expand.argtypes = [POINTER(snd_config_t), POINTER(snd_config_t), c_char_p, POINTER(snd_config_t), POINTER(POINTER(snd_config_t))]
snd_config_expand.restype = c_int

#int snd_config_evaluate(snd_config_t *config, snd_config_t *root,
			#snd_config_t *private_data, snd_config_t **result);
snd_config_evaluate = _alsa_lib.snd_config_evaluate
snd_config_evaluate.argtypes = [POINTER(snd_config_t), POINTER(snd_config_t), POINTER(snd_config_t), POINTER(POINTER(snd_config_t))]
snd_config_evaluate.restype = c_int


#int snd_config_add(snd_config_t *config, snd_config_t *leaf);
snd_config_add = _alsa_lib.snd_config_add
snd_config_add.argtypes = [POINTER(snd_config_t), POINTER(snd_config_t)]
snd_config_add.restype = c_int

#int snd_config_delete(snd_config_t *config);
snd_config_delete = _alsa_lib.snd_config_delete
snd_config_delete.argtypes = [POINTER(snd_config_t)]
snd_config_delete.restype = c_int

#int snd_config_delete_compound_members(const snd_config_t *config);
snd_config_delete_compound_members = _alsa_lib.snd_config_delete_compound_members
snd_config_delete_compound_members.argtypes = [POINTER(snd_config_t)]
snd_config_delete_compound_members.restype = c_int

#int snd_config_copy(snd_config_t **dst, snd_config_t *src);
snd_config_copy = _alsa_lib.snd_config_copy
snd_config_copy.argtypes = [POINTER(POINTER(snd_config_t)), POINTER(snd_config_t)]
snd_config_copy.restype = c_int


#int snd_config_make(snd_config_t **config, const char *key,
			#snd_config_type_t type);
snd_config_make = _alsa_lib.snd_config_make
snd_config_make.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, snd_config_type_t]
snd_config_make.restype = c_int

#int snd_config_make_integer(snd_config_t **config, const char *key);
snd_config_make_integer = _alsa_lib.snd_config_make_integer
snd_config_make_integer.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p]
snd_config_make_integer.restype = c_int

#int snd_config_make_integer64(snd_config_t **config, const char *key);
snd_config_make_integer64 = _alsa_lib.snd_config_make_integer64
snd_config_make_integer64.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p]
snd_config_make_integer64.restype = c_int

#int snd_config_make_real(snd_config_t **config, const char *key);
snd_config_make_real = _alsa_lib.snd_config_make_real
snd_config_make_real.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p]
snd_config_make_real.restype = c_int

#int snd_config_make_string(snd_config_t **config, const char *key);
snd_config_make_string = _alsa_lib.snd_config_make_string
snd_config_make_string.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p]
snd_config_make_string.restype = c_int

#int snd_config_make_pointer(snd_config_t **config, const char *key);
snd_config_make_pointer = _alsa_lib.snd_config_make_pointer
snd_config_make_pointer.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p]
snd_config_make_pointer.restype = c_int

#int snd_config_make_compound(snd_config_t **config, const char *key, int join);
snd_config_make_compound = _alsa_lib.snd_config_make_compound
snd_config_make_compound.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_int]
snd_config_make_compound.restype = c_int


#int snd_config_imake_integer(snd_config_t **config, const char *key, const long value);
snd_config_imake_integer = _alsa_lib.snd_config_imake_integer
snd_config_imake_integer.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_long]
snd_config_imake_integer.restype = c_int

#int snd_config_imake_integer64(snd_config_t **config, const char *key, const long long value);
snd_config_imake_integer64 = _alsa_lib.snd_config_imake_integer64
snd_config_imake_integer64.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_longlong]
snd_config_imake_integer64.restype = c_int

#int snd_config_imake_real(snd_config_t **config, const char *key, const double value);
snd_config_imake_real = _alsa_lib.snd_config_imake_real
snd_config_imake_real.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_double]
snd_config_imake_real.restype = c_int

#int snd_config_imake_string(snd_config_t **config, const char *key, const char *ascii);
snd_config_imake_string = _alsa_lib.snd_config_imake_string
snd_config_imake_string.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_char_p]
snd_config_imake_string.restype = c_int

#int snd_config_imake_pointer(snd_config_t **config, const char *key, const void *ptr);
snd_config_imake_pointer = _alsa_lib.snd_config_imake_pointer
snd_config_imake_pointer.argtypes = [POINTER(POINTER(snd_config_t)), c_char_p, c_void_p]
snd_config_imake_pointer.restype = c_int


#snd_config_type_t snd_config_get_type(const snd_config_t *config);
snd_config_get_type = _alsa_lib.snd_config_get_type
snd_config_get_type.argtypes = [POINTER(snd_config_t)]
snd_config_get_type.restype = snd_config_type_t


#int snd_config_set_id(snd_config_t *config, const char *id);
snd_config_set_id = _alsa_lib.snd_config_set_id
snd_config_set_id.argtypes = [POINTER(snd_config_t), c_char_p]
snd_config_set_id.restype = c_int

#int snd_config_set_integer(snd_config_t *config, long value);
snd_config_set_integer = _alsa_lib.snd_config_set_integer
snd_config_set_integer.argtypes = [POINTER(snd_config_t), c_long]
snd_config_set_integer.restype = c_int

#int snd_config_set_integer64(snd_config_t *config, long long value);
snd_config_set_integer64 = _alsa_lib.snd_config_set_integer64
snd_config_set_integer64.argtypes = [POINTER(snd_config_t), c_longlong]
snd_config_set_integer64.restype = c_int

#int snd_config_set_real(snd_config_t *config, double value);
snd_config_set_real = _alsa_lib.snd_config_set_real
snd_config_set_real.argtypes = [POINTER(snd_config_t), c_double]
snd_config_set_real.restype = c_int

#int snd_config_set_string(snd_config_t *config, const char *value);
snd_config_set_string = _alsa_lib.snd_config_set_string
snd_config_set_string.argtypes = [POINTER(snd_config_t), c_char_p]
snd_config_set_string.restype = c_int

#int snd_config_set_ascii(snd_config_t *config, const char *ascii);
snd_config_set_ascii = _alsa_lib.snd_config_set_ascii
snd_config_set_ascii.argtypes = [POINTER(snd_config_t), c_char_p]
snd_config_set_ascii.restype = c_int

#int snd_config_set_pointer(snd_config_t *config, const void *ptr);
snd_config_set_pointer = _alsa_lib.snd_config_set_pointer
snd_config_set_pointer.argtypes = [POINTER(snd_config_t), c_void_p]
snd_config_set_pointer.restype = c_int

#int snd_config_get_id(const snd_config_t *config, const char **value);
snd_config_get_id = _alsa_lib.snd_config_get_id
snd_config_get_id.argtypes = [POINTER(snd_config_t), POINTER(c_char_p)]
snd_config_get_id.restype = c_int

#int snd_config_get_integer(const snd_config_t *config, long *value);
snd_config_get_integer = _alsa_lib.snd_config_get_integer
snd_config_get_integer.argtypes = [POINTER(snd_config_t), POINTER(c_long)]
snd_config_get_integer.restype = c_int

#int snd_config_get_integer64(const snd_config_t *config, long long *value);
snd_config_get_integer64 = _alsa_lib.snd_config_get_integer64
snd_config_get_integer64.argtypes = [POINTER(snd_config_t), POINTER(c_longlong)]
snd_config_get_integer64.restype = c_int

#int snd_config_get_real(const snd_config_t *config, double *value);
snd_config_get_real = _alsa_lib.snd_config_get_real
snd_config_get_real.argtypes = [POINTER(snd_config_t), POINTER(c_double)]
snd_config_get_real.restype = c_int

#int snd_config_get_ireal(const snd_config_t *config, double *value);
snd_config_get_ireal = _alsa_lib.snd_config_get_ireal
snd_config_get_ireal.argtypes = [POINTER(snd_config_t), POINTER(c_double)]
snd_config_get_ireal.restype = c_int

#int snd_config_get_string(const snd_config_t *config, const char **value);
snd_config_get_string = _alsa_lib.snd_config_get_string
snd_config_get_string.argtypes = [POINTER(snd_config_t), POINTER(c_char_p)]
snd_config_get_string.restype = c_int

#int snd_config_get_ascii(const snd_config_t *config, char **value);
snd_config_get_ascii = _alsa_lib.snd_config_get_ascii
snd_config_get_ascii.argtypes = [POINTER(snd_config_t), POINTER(c_char_p)]
snd_config_get_ascii.restype = c_int

#int snd_config_get_pointer(const snd_config_t *config, const void **value);
snd_config_get_pointer = _alsa_lib.snd_config_get_pointer
snd_config_get_pointer.argtypes = [POINTER(snd_config_t), POINTER(c_void_p)]
snd_config_get_pointer.restype = c_int

#int snd_config_test_id(const snd_config_t *config, const char *id);
snd_config_test_id = _alsa_lib.snd_config_test_id
snd_config_test_id.argtypes = [POINTER(snd_config_t), c_char_p]
snd_config_test_id.restype = c_int


#snd_config_iterator_t snd_config_iterator_first(const snd_config_t *node);
snd_config_iterator_first = _alsa_lib.snd_config_iterator_first
snd_config_iterator_first.argtypes = [POINTER(snd_config_t)]
snd_config_iterator_first.restype = snd_config_iterator_t

#snd_config_iterator_t snd_config_iterator_next(const snd_config_iterator_t iterator);
snd_config_iterator_next = _alsa_lib.snd_config_iterator_next
snd_config_iterator_next.argtypes = [snd_config_iterator_t]
snd_config_iterator_next.restype = snd_config_iterator_t

#snd_config_iterator_t snd_config_iterator_end(const snd_config_t *node);
snd_config_iterator_end = _alsa_lib.snd_config_iterator_end
snd_config_iterator_end.argtypes = [POINTER(snd_config_t)]
snd_config_iterator_end.restype = snd_config_iterator_t

#snd_config_t *snd_config_iterator_entry(const snd_config_iterator_t iterator);
snd_config_iterator_entry = _alsa_lib.snd_config_iterator_entry
snd_config_iterator_entry.argtypes = [snd_config_iterator_t]
snd_config_iterator_entry.restype = POINTER(snd_config_t)


#
# \brief Helper macro to iterate over the children of a compound node.
# \param[in,out] pos Iterator variable for the current node.
# \param[in,out] next Temporary iterator variable for the next node.
# \param[in] node Handle to the compound configuration node to iterate over.
#
# Use this macro like a \c for statement, e.g.:
# \code
# snd_config_iterator_t pos, next;
# snd_config_for_each(pos, next, node) {
#     snd_config_t *entry = snd_config_iterator_entry(pos);
#     ...
# }
# \endcode
#
# This macro allows deleting or removing the current node.
#
#define snd_config_for_each(pos, next, node) \
	#for (pos = snd_config_iterator_first(node), next = snd_config_iterator_next(pos); pos != snd_config_iterator_end(node); pos = next, next = snd_config_iterator_next(pos))

# Misc functions 

#int snd_config_get_bool_ascii(const char *ascii);
snd_config_get_bool_ascii = _alsa_lib.snd_config_get_bool_ascii
snd_config_get_bool_ascii.argtypes = [c_char_p]
snd_config_get_bool_ascii.restype = c_int

#int snd_config_get_bool(const snd_config_t *conf);
snd_config_get_bool = _alsa_lib.snd_config_get_bool
snd_config_get_bool.argtypes = [POINTER(snd_config_t)]
snd_config_get_bool.restype = c_int

#int snd_config_get_ctl_iface_ascii(const char *ascii);
snd_config_get_ctl_iface_ascii = _alsa_lib.snd_config_get_ctl_iface_ascii
snd_config_get_ctl_iface_ascii.argtypes = [c_char_p]
snd_config_get_ctl_iface_ascii.restype = c_int

#int snd_config_get_ctl_iface(const snd_config_t *conf);
snd_config_get_ctl_iface = _alsa_lib.snd_config_get_ctl_iface
snd_config_get_ctl_iface.argtypes = [POINTER(snd_config_t)]
snd_config_get_ctl_iface.restype = c_int


# Names functions 

#
# Device-name list element
#
class snd_devname(Structure):
    _fields_ = [
            ]
snd_devname_t = snd_devname 

#
# Device-name list element (definition)
#
class snd_devname(Structure):
    _fields_ = [
            ('name', c_char_p), # *< Device name string 
            ('comment', c_char_p), # *< Comments 
            ('next', POINTER(snd_devname_t)) # *< Next pointer 
            ]

#int snd_names_list(const char *iface, snd_devname_t **list);
snd_names_list = _alsa_lib.snd_names_list
snd_names_list.argtypes = [c_char_p, POINTER(POINTER(snd_devname_t))]
snd_names_list.restype = c_int

#void snd_names_list_free(snd_devname_t *list);
snd_names_list_free = _alsa_lib.snd_names_list_free
snd_names_list_free.argtypes = [POINTER(snd_devname_t)]
snd_names_list_free.restype = None
