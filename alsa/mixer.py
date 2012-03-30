#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa mixer.
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


""" Alsa mixer.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .control import *

#
#  \defgroup Mixer Mixer Interface
#  The mixer interface.
#  \{
#

# Mixer handle 
class _snd_mixer(Structure):
    _fields_ = [
            ]
snd_mixer_t = _snd_mixer 
# Mixer elements class handle 
class _snd_mixer_class(Structure):
    _fields_ = [
            ]
snd_mixer_class_t = _snd_mixer_class 
# Mixer element handle 
class _snd_mixer_elem(Structure):
    _fields_ = [
            ]
snd_mixer_elem_t = _snd_mixer_elem 

# 
# \brief Mixer callback function
# \param mixer Mixer handle
# \param mask event mask
# \param elem related mixer element (if any)
# \return 0 on success otherwise a negative error code
#
#typedef int (*snd_mixer_callback_t)(snd_mixer_t *ctl,
					#unsigned int mask,
					#snd_mixer_elem_t *elem);
snd_mixer_callback_t = CFUNCTYPE(c_int, POINTER(snd_mixer_t), c_uint, POINTER(snd_mixer_elem_t))

# 
# \brief Mixer element callback function
# \param elem Mixer element
# \param mask event mask
# \return 0 on success otherwise a negative error code
#
#typedef int (*snd_mixer_elem_callback_t)(snd_mixer_elem_t *elem,
					 #unsigned int mask);
snd_mixer_elem_callback_t = CFUNCTYPE(c_int, POINTER(snd_mixer_elem_t), c_uint)

#
# \brief Compare function for sorting mixer elements
# \param e1 First element
# \param e2 Second element
# \return -1 if e1 < e2, 0 if e1 == e2, 1 if e1 > e2
#
#typedef int (*snd_mixer_compare_t)(const snd_mixer_elem_t *e1,
				   #const snd_mixer_elem_t *e2);
snd_mixer_compare_t = CFUNCTYPE(c_int, POINTER(snd_mixer_elem_t), POINTER(snd_mixer_elem_t))

#
# \brief Event callback for the mixer class
# \param class_ Mixer class
# \param mask Event mask (SND_CTL_EVENT_*)
# \param helem HCTL element which invoked the event
# \param melem Mixer element associated to HCTL element
# \return zero if success, otherwise a negative error value
#
#typedef int (*snd_mixer_event_t)(snd_mixer_class_t *class_, unsigned int mask,
				 #snd_hctl_elem_t *helem, snd_mixer_elem_t *melem);
snd_mixer_event_t = CFUNCTYPE(c_int, POINTER(snd_mixer_class_t), c_uint, POINTER(snd_hctl_elem_t), POINTER(snd_mixer_elem_t))


# Mixer element type 
_snd_mixer_elem_type = c_int
# Simple mixer elements 
SND_MIXER_ELEM_SIMPLE = 0
SND_MIXER_ELEM_LAST = SND_MIXER_ELEM_SIMPLE
snd_mixer_elem_type_t = _snd_mixer_elem_type 

#int snd_mixer_open(snd_mixer_t **mixer, int mode);
snd_mixer_open = _alsa_lib.snd_mixer_open
snd_mixer_open.argtypes = [POINTER(POINTER(snd_mixer_t)), c_int]
snd_mixer_open.restype = c_int

#int snd_mixer_close(snd_mixer_t *mixer);
snd_mixer_close = _alsa_lib.snd_mixer_close
snd_mixer_close.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_close.restype = c_int

#snd_mixer_elem_t *snd_mixer_first_elem(snd_mixer_t *mixer);
snd_mixer_first_elem = _alsa_lib.snd_mixer_first_elem
snd_mixer_first_elem.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_first_elem.restype = POINTER(snd_mixer_elem_t)

#snd_mixer_elem_t *snd_mixer_last_elem(snd_mixer_t *mixer);
snd_mixer_last_elem = _alsa_lib.snd_mixer_last_elem
snd_mixer_last_elem.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_last_elem.restype = POINTER(snd_mixer_elem_t)

#int snd_mixer_handle_events(snd_mixer_t *mixer);
snd_mixer_handle_events = _alsa_lib.snd_mixer_handle_events
snd_mixer_handle_events.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_handle_events.restype = c_int

#int snd_mixer_attach(snd_mixer_t *mixer, const char *name);
snd_mixer_attach = _alsa_lib.snd_mixer_attach
snd_mixer_attach.argtypes = [POINTER(snd_mixer_t), c_char_p]
snd_mixer_attach.restype = c_int

#int snd_mixer_attach_hctl(snd_mixer_t *mixer, snd_hctl_t *hctl);
snd_mixer_attach_hctl = _alsa_lib.snd_mixer_attach_hctl
snd_mixer_attach_hctl.argtypes = [POINTER(snd_mixer_t), POINTER(snd_hctl_t)]
snd_mixer_attach_hctl.restype = c_int

#int snd_mixer_detach(snd_mixer_t *mixer, const char *name);
snd_mixer_detach = _alsa_lib.snd_mixer_detach
snd_mixer_detach.argtypes = [POINTER(snd_mixer_t), c_char_p]
snd_mixer_detach.restype = c_int

#int snd_mixer_detach_hctl(snd_mixer_t *mixer, snd_hctl_t *hctl);
snd_mixer_detach_hctl = _alsa_lib.snd_mixer_detach_hctl
snd_mixer_detach_hctl.argtypes = [POINTER(snd_mixer_t), POINTER(snd_hctl_t)]
snd_mixer_detach_hctl.restype = c_int

#int snd_mixer_get_hctl(snd_mixer_t *mixer, const char *name, snd_hctl_t **hctl);
snd_mixer_get_hctl = _alsa_lib.snd_mixer_get_hctl
snd_mixer_get_hctl.argtypes = [POINTER(snd_mixer_t), c_char_p, POINTER(POINTER(snd_hctl_t))]
snd_mixer_get_hctl.restype = c_int

#int snd_mixer_poll_descriptors_count(snd_mixer_t *mixer);
snd_mixer_poll_descriptors_count = _alsa_lib.snd_mixer_poll_descriptors_count
snd_mixer_poll_descriptors_count.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_poll_descriptors_count.restype = c_int

#int snd_mixer_poll_descriptors(snd_mixer_t *mixer, struct pollfd *pfds, unsigned int space);
snd_mixer_poll_descriptors = _alsa_lib.snd_mixer_poll_descriptors
snd_mixer_poll_descriptors.argtypes = [POINTER(snd_mixer_t), POINTER(pollfd), c_uint]
snd_mixer_poll_descriptors.restype = c_int

#int snd_mixer_poll_descriptors_revents(snd_mixer_t *mixer, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_mixer_poll_descriptors_revents = _alsa_lib.snd_mixer_poll_descriptors_revents
snd_mixer_poll_descriptors_revents.argtypes = [POINTER(snd_mixer_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_mixer_poll_descriptors_revents.restype = c_int

#int snd_mixer_load(snd_mixer_t *mixer);
snd_mixer_load = _alsa_lib.snd_mixer_load
snd_mixer_load.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_load.restype = c_int

#void snd_mixer_free(snd_mixer_t *mixer);
snd_mixer_free = _alsa_lib.snd_mixer_free
snd_mixer_free.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_free.restype = None

#int snd_mixer_wait(snd_mixer_t *mixer, int timeout);
snd_mixer_wait = _alsa_lib.snd_mixer_wait
snd_mixer_wait.argtypes = [POINTER(snd_mixer_t), c_int]
snd_mixer_wait.restype = c_int

#int snd_mixer_set_compare(snd_mixer_t *mixer, snd_mixer_compare_t msort);
snd_mixer_set_compare = _alsa_lib.snd_mixer_set_compare
snd_mixer_set_compare.argtypes = [POINTER(snd_mixer_t), snd_mixer_compare_t]
snd_mixer_set_compare.restype = c_int

#void snd_mixer_set_callback(snd_mixer_t *obj, snd_mixer_callback_t val);
snd_mixer_set_callback = _alsa_lib.snd_mixer_set_callback
snd_mixer_set_callback.argtypes = [POINTER(snd_mixer_t), snd_mixer_callback_t]
snd_mixer_set_callback.restype = None

#void * snd_mixer_get_callback_private(const snd_mixer_t *obj);
snd_mixer_get_callback_private = _alsa_lib.snd_mixer_get_callback_private
snd_mixer_get_callback_private.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_get_callback_private.restype = c_void_p

#void snd_mixer_set_callback_private(snd_mixer_t *obj, void * val);
snd_mixer_set_callback_private = _alsa_lib.snd_mixer_set_callback_private
snd_mixer_set_callback_private.argtypes = [POINTER(snd_mixer_t), c_void_p]
snd_mixer_set_callback_private.restype = None

#unsigned int snd_mixer_get_count(const snd_mixer_t *obj);
snd_mixer_get_count = _alsa_lib.snd_mixer_get_count
snd_mixer_get_count.argtypes = [POINTER(snd_mixer_t)]
snd_mixer_get_count.restype = c_uint

#int snd_mixer_class_unregister(snd_mixer_class_t *clss);
snd_mixer_class_unregister = _alsa_lib.snd_mixer_class_unregister
snd_mixer_class_unregister.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_unregister.restype = c_int


#snd_mixer_elem_t *snd_mixer_elem_next(snd_mixer_elem_t *elem);
snd_mixer_elem_next = _alsa_lib.snd_mixer_elem_next
snd_mixer_elem_next.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_next.restype = POINTER(snd_mixer_elem_t)

#snd_mixer_elem_t *snd_mixer_elem_prev(snd_mixer_elem_t *elem);
snd_mixer_elem_prev = _alsa_lib.snd_mixer_elem_prev
snd_mixer_elem_prev.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_prev.restype = POINTER(snd_mixer_elem_t)

#void snd_mixer_elem_set_callback(snd_mixer_elem_t *obj, snd_mixer_elem_callback_t val);
snd_mixer_elem_set_callback = _alsa_lib.snd_mixer_elem_set_callback
snd_mixer_elem_set_callback.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_elem_callback_t]
snd_mixer_elem_set_callback.restype = None

#void * snd_mixer_elem_get_callback_private(const snd_mixer_elem_t *obj);
snd_mixer_elem_get_callback_private = _alsa_lib.snd_mixer_elem_get_callback_private
snd_mixer_elem_get_callback_private.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_get_callback_private.restype = c_void_p

#void snd_mixer_elem_set_callback_private(snd_mixer_elem_t *obj, void * val);
snd_mixer_elem_set_callback_private = _alsa_lib.snd_mixer_elem_set_callback_private
snd_mixer_elem_set_callback_private.argtypes = [POINTER(snd_mixer_elem_t), c_void_p]
snd_mixer_elem_set_callback_private.restype = None

#snd_mixer_elem_type_t snd_mixer_elem_get_type(const snd_mixer_elem_t *obj);
snd_mixer_elem_get_type = _alsa_lib.snd_mixer_elem_get_type
snd_mixer_elem_get_type.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_get_type.restype = snd_mixer_elem_type_t


#int snd_mixer_class_register(snd_mixer_class_t *class_, snd_mixer_t *mixer);
snd_mixer_class_register = _alsa_lib.snd_mixer_class_register
snd_mixer_class_register.argtypes = [POINTER(snd_mixer_class_t), POINTER(snd_mixer_t)]
snd_mixer_class_register.restype = c_int

#int snd_mixer_elem_new(snd_mixer_elem_t **elem,
			   #snd_mixer_elem_type_t type,
			   #int compare_weight,
			   #void *private_data,
			   #void (*private_free)(snd_mixer_elem_t *elem));
snd_mixer_elem_new = _alsa_lib.snd_mixer_elem_new
snd_mixer_elem_new.argtypes = [POINTER(POINTER(snd_mixer_elem_t)), snd_mixer_elem_type_t, c_int, c_void_p, CFUNCTYPE(None, POINTER(snd_mixer_elem_t))]
snd_mixer_elem_new.restype = c_int

#int snd_mixer_elem_add(snd_mixer_elem_t *elem, snd_mixer_class_t *class_);
snd_mixer_elem_add = _alsa_lib.snd_mixer_elem_add
snd_mixer_elem_add.argtypes = [POINTER(snd_mixer_elem_t), POINTER(snd_mixer_class_t)]
snd_mixer_elem_add.restype = c_int

#int snd_mixer_elem_remove(snd_mixer_elem_t *elem);
snd_mixer_elem_remove = _alsa_lib.snd_mixer_elem_remove
snd_mixer_elem_remove.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_remove.restype = c_int

#void snd_mixer_elem_free(snd_mixer_elem_t *elem);
snd_mixer_elem_free = _alsa_lib.snd_mixer_elem_free
snd_mixer_elem_free.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_free.restype = None

#int snd_mixer_elem_info(snd_mixer_elem_t *elem);
snd_mixer_elem_info = _alsa_lib.snd_mixer_elem_info
snd_mixer_elem_info.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_info.restype = c_int

#int snd_mixer_elem_value(snd_mixer_elem_t *elem);
snd_mixer_elem_value = _alsa_lib.snd_mixer_elem_value
snd_mixer_elem_value.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_value.restype = c_int

#int snd_mixer_elem_attach(snd_mixer_elem_t *melem, snd_hctl_elem_t *helem);
snd_mixer_elem_attach = _alsa_lib.snd_mixer_elem_attach
snd_mixer_elem_attach.argtypes = [POINTER(snd_mixer_elem_t), POINTER(snd_hctl_elem_t)]
snd_mixer_elem_attach.restype = c_int

#int snd_mixer_elem_detach(snd_mixer_elem_t *melem, snd_hctl_elem_t *helem);
snd_mixer_elem_detach = _alsa_lib.snd_mixer_elem_detach
snd_mixer_elem_detach.argtypes = [POINTER(snd_mixer_elem_t), POINTER(snd_hctl_elem_t)]
snd_mixer_elem_detach.restype = c_int

#int snd_mixer_elem_empty(snd_mixer_elem_t *melem);
snd_mixer_elem_empty = _alsa_lib.snd_mixer_elem_empty
snd_mixer_elem_empty.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_empty.restype = c_int

#void *snd_mixer_elem_get_private(const snd_mixer_elem_t *melem);
snd_mixer_elem_get_private = _alsa_lib.snd_mixer_elem_get_private
snd_mixer_elem_get_private.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_elem_get_private.restype = c_void_p


#size_t snd_mixer_class_sizeof(void);
snd_mixer_class_sizeof = _alsa_lib.snd_mixer_class_sizeof
snd_mixer_class_sizeof.argtypes = []
snd_mixer_class_sizeof.restype = c_size_t


# \hideinitializer
# \brief allocate an invalid #snd_mixer_class_t using standard alloca
# \param ptr returned pointer
#
#define snd_mixer_class_alloca(ptr) __snd_alloca(ptr, snd_mixer_class)
#int snd_mixer_class_malloc(snd_mixer_class_t **ptr);
snd_mixer_class_malloc = _alsa_lib.snd_mixer_class_malloc
snd_mixer_class_malloc.argtypes = [POINTER(POINTER(snd_mixer_class_t))]
snd_mixer_class_malloc.restype = c_int

#void snd_mixer_class_free(snd_mixer_class_t *obj);
snd_mixer_class_free = _alsa_lib.snd_mixer_class_free
snd_mixer_class_free.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_free.restype = None

#void snd_mixer_class_copy(snd_mixer_class_t *dst, const snd_mixer_class_t *src);
snd_mixer_class_copy = _alsa_lib.snd_mixer_class_copy
snd_mixer_class_copy.argtypes = [POINTER(snd_mixer_class_t), POINTER(snd_mixer_class_t)]
snd_mixer_class_copy.restype = None

#snd_mixer_t *snd_mixer_class_get_mixer(const snd_mixer_class_t *class_);
snd_mixer_class_get_mixer = _alsa_lib.snd_mixer_class_get_mixer
snd_mixer_class_get_mixer.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_get_mixer.restype = POINTER(snd_mixer_t)

#snd_mixer_event_t snd_mixer_class_get_event(const snd_mixer_class_t *class_);
snd_mixer_class_get_event = _alsa_lib.snd_mixer_class_get_event
snd_mixer_class_get_event.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_get_event.restype = snd_mixer_event_t

#void *snd_mixer_class_get_private(const snd_mixer_class_t *class_);
snd_mixer_class_get_private = _alsa_lib.snd_mixer_class_get_private
snd_mixer_class_get_private.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_get_private.restype = c_void_p

#snd_mixer_compare_t snd_mixer_class_get_compare(const snd_mixer_class_t *class_);
snd_mixer_class_get_compare = _alsa_lib.snd_mixer_class_get_compare
snd_mixer_class_get_compare.argtypes = [POINTER(snd_mixer_class_t)]
snd_mixer_class_get_compare.restype = snd_mixer_compare_t

#int snd_mixer_class_set_event(snd_mixer_class_t *class_, snd_mixer_event_t event);
snd_mixer_class_set_event = _alsa_lib.snd_mixer_class_set_event
snd_mixer_class_set_event.argtypes = [POINTER(snd_mixer_class_t), snd_mixer_event_t]
snd_mixer_class_set_event.restype = c_int

#int snd_mixer_class_set_private(snd_mixer_class_t *class_, void *private_data);
snd_mixer_class_set_private = _alsa_lib.snd_mixer_class_set_private
snd_mixer_class_set_private.argtypes = [POINTER(snd_mixer_class_t), c_void_p]
snd_mixer_class_set_private.restype = c_int

#int snd_mixer_class_set_private_free(snd_mixer_class_t *class_, void (*private_free)(snd_mixer_class_t *class_));
snd_mixer_class_set_private_free = _alsa_lib.snd_mixer_class_set_private_free
snd_mixer_class_set_private_free.argtypes = [POINTER(snd_mixer_class_t), CFUNCTYPE(None, POINTER(snd_mixer_class_t))]
snd_mixer_class_set_private_free.restype = c_int

#int snd_mixer_class_set_compare(snd_mixer_class_t *class_, snd_mixer_compare_t compare);
snd_mixer_class_set_compare = _alsa_lib.snd_mixer_class_set_compare
snd_mixer_class_set_compare.argtypes = [POINTER(snd_mixer_class_t), snd_mixer_compare_t]
snd_mixer_class_set_compare.restype = c_int


#
#  \defgroup SimpleMixer Simple Mixer Interface
#  \ingroup Mixer
#  The simple mixer interface.
#  \{
#

# Simple mixer elements API 

# Mixer simple element channel identifier 
_snd_mixer_selem_channel_id = c_int
# Unknown 
SND_MIXER_SCHN_UNKNOWN = -1
# Front left 
SND_MIXER_SCHN_FRONT_LEFT = 0
# Front right 
SND_MIXER_SCHN_FRONT_RIGHT = 1
# Rear left 
SND_MIXER_SCHN_REAR_LEFT = 2
# Rear right 
SND_MIXER_SCHN_REAR_RIGHT = 3
# Front center 
SND_MIXER_SCHN_FRONT_CENTER = 4
# Woofer 
SND_MIXER_SCHN_WOOFER = 5
# Side Left 
SND_MIXER_SCHN_SIDE_LEFT = 6
# Side Right 
SND_MIXER_SCHN_SIDE_RIGHT = 7
# Rear Center 
SND_MIXER_SCHN_REAR_CENTER = 8
SND_MIXER_SCHN_LAST = 31
# Mono (Front left alias) 
SND_MIXER_SCHN_MONO = SND_MIXER_SCHN_FRONT_LEFT
snd_mixer_selem_channel_id_t = _snd_mixer_selem_channel_id

# Mixer simple element - register options - abstraction level 
snd_mixer_selem_regopt_abstract = c_int
# no abstraction - try use all universal controls from driver 
SND_MIXER_SABSTRACT_NONE = 0
# basic abstraction - Master,PCM,CD,Aux,Record-Gain etc. 
SND_MIXER_SABSTRACT_BASIC = 1

# Mixer simple element - register options 
class snd_mixer_selem_regopt(Structure):
    _fields_ = [
# structure version 
            ('ver', c_int),
# v1: abstract layer selection 
            ('abstract', snd_mixer_selem_regopt_abstract),
# v1: device name (must be NULL when playback_pcm or capture_pcm != NULL) 
            ('device', c_char_p),
# v1: playback PCM connected to mixer device (NULL == none) 
            ('playback_pcm', POINTER(snd_pcm_t)),
# v1: capture PCM connected to mixer device (NULL == none) 
            ('capture_pcm', POINTER(snd_pcm_t))
            ]

# Mixer simple element identifier 
class _snd_mixer_selem_id(Structure):
    _fields_ = [
            ]
snd_mixer_selem_id_t = _snd_mixer_selem_id 

#const char *snd_mixer_selem_channel_name(snd_mixer_selem_channel_id_t channel);
snd_mixer_selem_channel_name = _alsa_lib.snd_mixer_selem_channel_name
snd_mixer_selem_channel_name.argtypes = [snd_mixer_selem_channel_id_t]
snd_mixer_selem_channel_name.restype = c_char_p


#int snd_mixer_selem_register(snd_mixer_t *mixer,
				 #struct snd_mixer_selem_regopt *options,
				 #snd_mixer_class_t **classp);
snd_mixer_selem_register = _alsa_lib.snd_mixer_selem_register
snd_mixer_selem_register.argtypes = [POINTER(snd_mixer_t), POINTER(snd_mixer_selem_regopt), POINTER(POINTER(snd_mixer_class_t))]
snd_mixer_selem_register.restype = c_int

#void snd_mixer_selem_get_id(snd_mixer_elem_t *element,
				#snd_mixer_selem_id_t *id);
snd_mixer_selem_get_id = _alsa_lib.snd_mixer_selem_get_id
snd_mixer_selem_get_id.argtypes = [POINTER(snd_mixer_elem_t), POINTER(snd_mixer_selem_id_t)]
snd_mixer_selem_get_id.restype = None

#const char *snd_mixer_selem_get_name(snd_mixer_elem_t *elem);
snd_mixer_selem_get_name = _alsa_lib.snd_mixer_selem_get_name
snd_mixer_selem_get_name.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_get_name.restype = c_char_p

#unsigned int snd_mixer_selem_get_index(snd_mixer_elem_t *elem);
snd_mixer_selem_get_index = _alsa_lib.snd_mixer_selem_get_index
snd_mixer_selem_get_index.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_get_index.restype = c_uint

#snd_mixer_elem_t *snd_mixer_find_selem(snd_mixer_t *mixer,
					   #const snd_mixer_selem_id_t *id);
snd_mixer_find_selem = _alsa_lib.snd_mixer_find_selem
snd_mixer_find_selem.argtypes = [POINTER(snd_mixer_t), POINTER(snd_mixer_selem_id_t)]
snd_mixer_find_selem.restype = POINTER(snd_mixer_elem_t)


#int snd_mixer_selem_is_active(snd_mixer_elem_t *elem);
snd_mixer_selem_is_active = _alsa_lib.snd_mixer_selem_is_active
snd_mixer_selem_is_active.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_active.restype = c_int

#int snd_mixer_selem_is_playback_mono(snd_mixer_elem_t *elem);
snd_mixer_selem_is_playback_mono = _alsa_lib.snd_mixer_selem_is_playback_mono
snd_mixer_selem_is_playback_mono.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_playback_mono.restype = c_int

#int snd_mixer_selem_has_playback_channel(snd_mixer_elem_t *obj, snd_mixer_selem_channel_id_t channel);
snd_mixer_selem_has_playback_channel = _alsa_lib.snd_mixer_selem_has_playback_channel
snd_mixer_selem_has_playback_channel.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t]
snd_mixer_selem_has_playback_channel.restype = c_int

#int snd_mixer_selem_is_capture_mono(snd_mixer_elem_t *elem);
snd_mixer_selem_is_capture_mono = _alsa_lib.snd_mixer_selem_is_capture_mono
snd_mixer_selem_is_capture_mono.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_capture_mono.restype = c_int

#int snd_mixer_selem_has_capture_channel(snd_mixer_elem_t *obj, snd_mixer_selem_channel_id_t channel);
snd_mixer_selem_has_capture_channel = _alsa_lib.snd_mixer_selem_has_capture_channel
snd_mixer_selem_has_capture_channel.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t]
snd_mixer_selem_has_capture_channel.restype = c_int

#int snd_mixer_selem_get_capture_group(snd_mixer_elem_t *elem);
snd_mixer_selem_get_capture_group = _alsa_lib.snd_mixer_selem_get_capture_group
snd_mixer_selem_get_capture_group.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_get_capture_group.restype = c_int

#int snd_mixer_selem_has_common_volume(snd_mixer_elem_t *elem);
snd_mixer_selem_has_common_volume = _alsa_lib.snd_mixer_selem_has_common_volume
snd_mixer_selem_has_common_volume.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_common_volume.restype = c_int

#int snd_mixer_selem_has_playback_volume(snd_mixer_elem_t *elem);
snd_mixer_selem_has_playback_volume = _alsa_lib.snd_mixer_selem_has_playback_volume
snd_mixer_selem_has_playback_volume.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_playback_volume.restype = c_int

#int snd_mixer_selem_has_playback_volume_joined(snd_mixer_elem_t *elem);
snd_mixer_selem_has_playback_volume_joined = _alsa_lib.snd_mixer_selem_has_playback_volume_joined
snd_mixer_selem_has_playback_volume_joined.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_playback_volume_joined.restype = c_int

#int snd_mixer_selem_has_capture_volume(snd_mixer_elem_t *elem);
snd_mixer_selem_has_capture_volume = _alsa_lib.snd_mixer_selem_has_capture_volume
snd_mixer_selem_has_capture_volume.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_capture_volume.restype = c_int

#int snd_mixer_selem_has_capture_volume_joined(snd_mixer_elem_t *elem);
snd_mixer_selem_has_capture_volume_joined = _alsa_lib.snd_mixer_selem_has_capture_volume_joined
snd_mixer_selem_has_capture_volume_joined.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_capture_volume_joined.restype = c_int

#int snd_mixer_selem_has_common_switch(snd_mixer_elem_t *elem);
snd_mixer_selem_has_common_switch = _alsa_lib.snd_mixer_selem_has_common_switch
snd_mixer_selem_has_common_switch.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_common_switch.restype = c_int

#int snd_mixer_selem_has_playback_switch(snd_mixer_elem_t *elem);
snd_mixer_selem_has_playback_switch = _alsa_lib.snd_mixer_selem_has_playback_switch
snd_mixer_selem_has_playback_switch.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_playback_switch.restype = c_int

#int snd_mixer_selem_has_playback_switch_joined(snd_mixer_elem_t *elem);
snd_mixer_selem_has_playback_switch_joined = _alsa_lib.snd_mixer_selem_has_playback_switch_joined
snd_mixer_selem_has_playback_switch_joined.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_playback_switch_joined.restype = c_int

#int snd_mixer_selem_has_capture_switch(snd_mixer_elem_t *elem);
snd_mixer_selem_has_capture_switch = _alsa_lib.snd_mixer_selem_has_capture_switch
snd_mixer_selem_has_capture_switch.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_capture_switch.restype = c_int

#int snd_mixer_selem_has_capture_switch_joined(snd_mixer_elem_t *elem);
snd_mixer_selem_has_capture_switch_joined = _alsa_lib.snd_mixer_selem_has_capture_switch_joined
snd_mixer_selem_has_capture_switch_joined.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_capture_switch_joined.restype = c_int

#int snd_mixer_selem_has_capture_switch_exclusive(snd_mixer_elem_t *elem);
snd_mixer_selem_has_capture_switch_exclusive = _alsa_lib.snd_mixer_selem_has_capture_switch_exclusive
snd_mixer_selem_has_capture_switch_exclusive.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_has_capture_switch_exclusive.restype = c_int


#int snd_mixer_selem_ask_playback_vol_dB(snd_mixer_elem_t *elem, long value, long *dBvalue);
snd_mixer_selem_ask_playback_vol_dB = _alsa_lib.snd_mixer_selem_ask_playback_vol_dB
snd_mixer_selem_ask_playback_vol_dB.argtypes = [POINTER(snd_mixer_elem_t), c_long, POINTER(c_long)]
snd_mixer_selem_ask_playback_vol_dB.restype = c_int

#int snd_mixer_selem_ask_capture_vol_dB(snd_mixer_elem_t *elem, long value, long *dBvalue);
snd_mixer_selem_ask_capture_vol_dB = _alsa_lib.snd_mixer_selem_ask_capture_vol_dB
snd_mixer_selem_ask_capture_vol_dB.argtypes = [POINTER(snd_mixer_elem_t), c_long, POINTER(c_long)]
snd_mixer_selem_ask_capture_vol_dB.restype = c_int

#int snd_mixer_selem_ask_playback_dB_vol(snd_mixer_elem_t *elem, long dBvalue, int dir, long *value);
snd_mixer_selem_ask_playback_dB_vol = _alsa_lib.snd_mixer_selem_ask_playback_dB_vol
snd_mixer_selem_ask_playback_dB_vol.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_int, POINTER(c_long)]
snd_mixer_selem_ask_playback_dB_vol.restype = c_int

#int snd_mixer_selem_ask_capture_dB_vol(snd_mixer_elem_t *elem, long dBvalue, int dir, long *value);
snd_mixer_selem_ask_capture_dB_vol = _alsa_lib.snd_mixer_selem_ask_capture_dB_vol
snd_mixer_selem_ask_capture_dB_vol.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_int, POINTER(c_long)]
snd_mixer_selem_ask_capture_dB_vol.restype = c_int

#int snd_mixer_selem_get_playback_volume(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long *value);
snd_mixer_selem_get_playback_volume = _alsa_lib.snd_mixer_selem_get_playback_volume
snd_mixer_selem_get_playback_volume.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_long)]
snd_mixer_selem_get_playback_volume.restype = c_int

#int snd_mixer_selem_get_capture_volume(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long *value);
snd_mixer_selem_get_capture_volume = _alsa_lib.snd_mixer_selem_get_capture_volume
snd_mixer_selem_get_capture_volume.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_long)]
snd_mixer_selem_get_capture_volume.restype = c_int

#int snd_mixer_selem_get_playback_dB(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long *value);
snd_mixer_selem_get_playback_dB = _alsa_lib.snd_mixer_selem_get_playback_dB
snd_mixer_selem_get_playback_dB.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_long)]
snd_mixer_selem_get_playback_dB.restype = c_int

#int snd_mixer_selem_get_capture_dB(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long *value);
snd_mixer_selem_get_capture_dB = _alsa_lib.snd_mixer_selem_get_capture_dB
snd_mixer_selem_get_capture_dB.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_long)]
snd_mixer_selem_get_capture_dB.restype = c_int

#int snd_mixer_selem_get_playback_switch(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, int *value);
snd_mixer_selem_get_playback_switch = _alsa_lib.snd_mixer_selem_get_playback_switch
snd_mixer_selem_get_playback_switch.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_int)]
snd_mixer_selem_get_playback_switch.restype = c_int

#int snd_mixer_selem_get_capture_switch(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, int *value);
snd_mixer_selem_get_capture_switch = _alsa_lib.snd_mixer_selem_get_capture_switch
snd_mixer_selem_get_capture_switch.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_int)]
snd_mixer_selem_get_capture_switch.restype = c_int

#int snd_mixer_selem_set_playback_volume(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long value);
snd_mixer_selem_set_playback_volume = _alsa_lib.snd_mixer_selem_set_playback_volume
snd_mixer_selem_set_playback_volume.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_long]
snd_mixer_selem_set_playback_volume.restype = c_int

#int snd_mixer_selem_set_capture_volume(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long value);
snd_mixer_selem_set_capture_volume = _alsa_lib.snd_mixer_selem_set_capture_volume
snd_mixer_selem_set_capture_volume.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_long]
snd_mixer_selem_set_capture_volume.restype = c_int

#int snd_mixer_selem_set_playback_dB(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long value, int dir);
snd_mixer_selem_set_playback_dB = _alsa_lib.snd_mixer_selem_set_playback_dB
snd_mixer_selem_set_playback_dB.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_long, c_int]
snd_mixer_selem_set_playback_dB.restype = c_int

#int snd_mixer_selem_set_capture_dB(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, long value, int dir);
snd_mixer_selem_set_capture_dB = _alsa_lib.snd_mixer_selem_set_capture_dB
snd_mixer_selem_set_capture_dB.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_long, c_int]
snd_mixer_selem_set_capture_dB.restype = c_int

#int snd_mixer_selem_set_playback_volume_all(snd_mixer_elem_t *elem, long value);
snd_mixer_selem_set_playback_volume_all = _alsa_lib.snd_mixer_selem_set_playback_volume_all
snd_mixer_selem_set_playback_volume_all.argtypes = [POINTER(snd_mixer_elem_t), c_long]
snd_mixer_selem_set_playback_volume_all.restype = c_int

#int snd_mixer_selem_set_capture_volume_all(snd_mixer_elem_t *elem, long value);
snd_mixer_selem_set_capture_volume_all = _alsa_lib.snd_mixer_selem_set_capture_volume_all
snd_mixer_selem_set_capture_volume_all.argtypes = [POINTER(snd_mixer_elem_t), c_long]
snd_mixer_selem_set_capture_volume_all.restype = c_int

#int snd_mixer_selem_set_playback_dB_all(snd_mixer_elem_t *elem, long value, int dir);
snd_mixer_selem_set_playback_dB_all = _alsa_lib.snd_mixer_selem_set_playback_dB_all
snd_mixer_selem_set_playback_dB_all.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_int]
snd_mixer_selem_set_playback_dB_all.restype = c_int

#int snd_mixer_selem_set_capture_dB_all(snd_mixer_elem_t *elem, long value, int dir);
snd_mixer_selem_set_capture_dB_all = _alsa_lib.snd_mixer_selem_set_capture_dB_all
snd_mixer_selem_set_capture_dB_all.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_int]
snd_mixer_selem_set_capture_dB_all.restype = c_int

#int snd_mixer_selem_set_playback_switch(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, int value);
snd_mixer_selem_set_playback_switch = _alsa_lib.snd_mixer_selem_set_playback_switch
snd_mixer_selem_set_playback_switch.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_int]
snd_mixer_selem_set_playback_switch.restype = c_int

#int snd_mixer_selem_set_capture_switch(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, int value);
snd_mixer_selem_set_capture_switch = _alsa_lib.snd_mixer_selem_set_capture_switch
snd_mixer_selem_set_capture_switch.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_int]
snd_mixer_selem_set_capture_switch.restype = c_int

#int snd_mixer_selem_set_playback_switch_all(snd_mixer_elem_t *elem, int value);
snd_mixer_selem_set_playback_switch_all = _alsa_lib.snd_mixer_selem_set_playback_switch_all
snd_mixer_selem_set_playback_switch_all.argtypes = [POINTER(snd_mixer_elem_t), c_int]
snd_mixer_selem_set_playback_switch_all.restype = c_int

#int snd_mixer_selem_set_capture_switch_all(snd_mixer_elem_t *elem, int value);
snd_mixer_selem_set_capture_switch_all = _alsa_lib.snd_mixer_selem_set_capture_switch_all
snd_mixer_selem_set_capture_switch_all.argtypes = [POINTER(snd_mixer_elem_t), c_int]
snd_mixer_selem_set_capture_switch_all.restype = c_int

#int snd_mixer_selem_get_playback_volume_range(snd_mixer_elem_t *elem, 
						  #long *min, long *max);
snd_mixer_selem_get_playback_volume_range = _alsa_lib.snd_mixer_selem_get_playback_volume_range
snd_mixer_selem_get_playback_volume_range.argtypes = [POINTER(snd_mixer_elem_t), POINTER(c_long), POINTER(c_long)]
snd_mixer_selem_get_playback_volume_range.restype = c_int

#int snd_mixer_selem_get_playback_dB_range(snd_mixer_elem_t *elem, 
					  #long *min, long *max);
snd_mixer_selem_get_playback_dB_range = _alsa_lib.snd_mixer_selem_get_playback_dB_range
snd_mixer_selem_get_playback_dB_range.argtypes = [POINTER(snd_mixer_elem_t), POINTER(c_long), POINTER(c_long)]
snd_mixer_selem_get_playback_dB_range.restype = c_int

#int snd_mixer_selem_set_playback_volume_range(snd_mixer_elem_t *elem, 
						  #long min, long max);
snd_mixer_selem_set_playback_volume_range = _alsa_lib.snd_mixer_selem_set_playback_volume_range
snd_mixer_selem_set_playback_volume_range.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_long]
snd_mixer_selem_set_playback_volume_range.restype = c_int

#int snd_mixer_selem_get_capture_volume_range(snd_mixer_elem_t *elem, 
						 #long *min, long *max);
snd_mixer_selem_get_capture_volume_range = _alsa_lib.snd_mixer_selem_get_capture_volume_range
snd_mixer_selem_get_capture_volume_range.argtypes = [POINTER(snd_mixer_elem_t), POINTER(c_long), POINTER(c_long)]
snd_mixer_selem_get_capture_volume_range.restype = c_int

#int snd_mixer_selem_get_capture_dB_range(snd_mixer_elem_t *elem, 
					 #long *min, long *max);
snd_mixer_selem_get_capture_dB_range = _alsa_lib.snd_mixer_selem_get_capture_dB_range
snd_mixer_selem_get_capture_dB_range.argtypes = [POINTER(snd_mixer_elem_t), POINTER(c_long), POINTER(c_long)]
snd_mixer_selem_get_capture_dB_range.restype = c_int

#int snd_mixer_selem_set_capture_volume_range(snd_mixer_elem_t *elem, 
						 #long min, long max);
snd_mixer_selem_set_capture_volume_range = _alsa_lib.snd_mixer_selem_set_capture_volume_range
snd_mixer_selem_set_capture_volume_range.argtypes = [POINTER(snd_mixer_elem_t), c_long, c_long]
snd_mixer_selem_set_capture_volume_range.restype = c_int


#int snd_mixer_selem_is_enumerated(snd_mixer_elem_t *elem);
snd_mixer_selem_is_enumerated = _alsa_lib.snd_mixer_selem_is_enumerated
snd_mixer_selem_is_enumerated.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_enumerated.restype = c_int

#int snd_mixer_selem_is_enum_playback(snd_mixer_elem_t *elem);
snd_mixer_selem_is_enum_playback = _alsa_lib.snd_mixer_selem_is_enum_playback
snd_mixer_selem_is_enum_playback.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_enum_playback.restype = c_int

#int snd_mixer_selem_is_enum_capture(snd_mixer_elem_t *elem);
snd_mixer_selem_is_enum_capture = _alsa_lib.snd_mixer_selem_is_enum_capture
snd_mixer_selem_is_enum_capture.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_is_enum_capture.restype = c_int

#int snd_mixer_selem_get_enum_items(snd_mixer_elem_t *elem);
snd_mixer_selem_get_enum_items = _alsa_lib.snd_mixer_selem_get_enum_items
snd_mixer_selem_get_enum_items.argtypes = [POINTER(snd_mixer_elem_t)]
snd_mixer_selem_get_enum_items.restype = c_int

#int snd_mixer_selem_get_enum_item_name(snd_mixer_elem_t *elem, unsigned int idx, size_t maxlen, char *str);
snd_mixer_selem_get_enum_item_name = _alsa_lib.snd_mixer_selem_get_enum_item_name
snd_mixer_selem_get_enum_item_name.argtypes = [POINTER(snd_mixer_elem_t), c_uint, c_size_t, c_char_p]
snd_mixer_selem_get_enum_item_name.restype = c_int

#int snd_mixer_selem_get_enum_item(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, unsigned int *idxp);
snd_mixer_selem_get_enum_item = _alsa_lib.snd_mixer_selem_get_enum_item
snd_mixer_selem_get_enum_item.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, POINTER(c_uint)]
snd_mixer_selem_get_enum_item.restype = c_int

#int snd_mixer_selem_set_enum_item(snd_mixer_elem_t *elem, snd_mixer_selem_channel_id_t channel, unsigned int idx);
snd_mixer_selem_set_enum_item = _alsa_lib.snd_mixer_selem_set_enum_item
snd_mixer_selem_set_enum_item.argtypes = [POINTER(snd_mixer_elem_t), snd_mixer_selem_channel_id_t, c_uint]
snd_mixer_selem_set_enum_item.restype = c_int


#size_t snd_mixer_selem_id_sizeof(void);
snd_mixer_selem_id_sizeof = _alsa_lib.snd_mixer_selem_id_sizeof
snd_mixer_selem_id_sizeof.argtypes = []
snd_mixer_selem_id_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_mixer_selem_id_t using standard alloca
# \param ptr returned pointer
#
#define snd_mixer_selem_id_alloca(ptr) __snd_alloca(ptr, snd_mixer_selem_id)
#int snd_mixer_selem_id_malloc(snd_mixer_selem_id_t **ptr);
snd_mixer_selem_id_malloc = _alsa_lib.snd_mixer_selem_id_malloc
snd_mixer_selem_id_malloc.argtypes = [POINTER(POINTER(snd_mixer_selem_id_t))]
snd_mixer_selem_id_malloc.restype = c_int

#void snd_mixer_selem_id_free(snd_mixer_selem_id_t *obj);
snd_mixer_selem_id_free = _alsa_lib.snd_mixer_selem_id_free
snd_mixer_selem_id_free.argtypes = [POINTER(snd_mixer_selem_id_t)]
snd_mixer_selem_id_free.restype = None

#void snd_mixer_selem_id_copy(snd_mixer_selem_id_t *dst, const snd_mixer_selem_id_t *src);
snd_mixer_selem_id_copy = _alsa_lib.snd_mixer_selem_id_copy
snd_mixer_selem_id_copy.argtypes = [POINTER(snd_mixer_selem_id_t), POINTER(snd_mixer_selem_id_t)]
snd_mixer_selem_id_copy.restype = None

#const char *snd_mixer_selem_id_get_name(const snd_mixer_selem_id_t *obj);
snd_mixer_selem_id_get_name = _alsa_lib.snd_mixer_selem_id_get_name
snd_mixer_selem_id_get_name.argtypes = [POINTER(snd_mixer_selem_id_t)]
snd_mixer_selem_id_get_name.restype = c_char_p

#unsigned int snd_mixer_selem_id_get_index(const snd_mixer_selem_id_t *obj);
snd_mixer_selem_id_get_index = _alsa_lib.snd_mixer_selem_id_get_index
snd_mixer_selem_id_get_index.argtypes = [POINTER(snd_mixer_selem_id_t)]
snd_mixer_selem_id_get_index.restype = c_uint

#void snd_mixer_selem_id_set_name(snd_mixer_selem_id_t *obj, const char *val);
snd_mixer_selem_id_set_name = _alsa_lib.snd_mixer_selem_id_set_name
snd_mixer_selem_id_set_name.argtypes = [POINTER(snd_mixer_selem_id_t), c_char_p]
snd_mixer_selem_id_set_name.restype = None

#void snd_mixer_selem_id_set_index(snd_mixer_selem_id_t *obj, unsigned int val);
snd_mixer_selem_id_set_index = _alsa_lib.snd_mixer_selem_id_set_index
snd_mixer_selem_id_set_index.argtypes = [POINTER(snd_mixer_selem_id_t), c_uint]
snd_mixer_selem_id_set_index.restype = None
