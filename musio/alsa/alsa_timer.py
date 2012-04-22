#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa timer structs.
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


""" Alsa timer structs

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .alsa_conf import *

#
#  \defgroup Timer Timer Interface
#  Timer Interface. See \ref timer page for more details.
#  \{
#

# dlsym version for interface entry callback 
#define SND_TIMER_DLSYM_VERSION		_dlsym_timer_001
# dlsym version for interface entry callback 
#define SND_TIMER_QUERY_DLSYM_VERSION	_dlsym_timer_query_001

# timer identification structure 
class _snd_timer_id(Structure):
    _fields_ = [
            ]
snd_timer_id_t = _snd_timer_id 
# timer global info structure 
class _snd_timer_ginfo(Structure):
    _fields_ = [
            ]
snd_timer_ginfo_t = _snd_timer_ginfo 
# timer global params structure 
class _snd_timer_gparams(Structure):
    _fields_ = [
            ]
snd_timer_gparams_t = _snd_timer_gparams 
# timer global status structure 
class _snd_timer_gstatus(Structure):
    _fields_ = [
            ]
snd_timer_gstatus_t = _snd_timer_gstatus 
# timer info structure 
class _snd_timer_info(Structure):
    _fields_ = [
            ]
snd_timer_info_t = _snd_timer_info 
# timer params structure 
class _snd_timer_params(Structure):
    _fields_ = [
            ]
snd_timer_params_t = _snd_timer_params 
# timer status structure 
class _snd_timer_status(Structure):
    _fields_ = [
            ]
snd_timer_status_t = _snd_timer_status 
# timer master class 
_snd_timer_class = c_int
SND_TIMER_CLASS_NONE = -1	 # *< invalid 
SND_TIMER_CLASS_SLAVE = 0	 # *< slave timer 
SND_TIMER_CLASS_GLOBAL = 1	 # *< global timer 
SND_TIMER_CLASS_CARD = 2	 # *< card timer 
SND_TIMER_CLASS_PCM = 3		 # *< PCM timer 
SND_TIMER_CLASS_LAST = SND_TIMER_CLASS_PCM	# *< last timer 
snd_timer_class_t = _snd_timer_class 

# timer slave class 
_snd_timer_slave_class = c_int
SND_TIMER_SCLASS_NONE = 0		# *< none 
SND_TIMER_SCLASS_APPLICATION = 1	# 	*< for internal use 
SND_TIMER_SCLASS_SEQUENCER = 2		# *< sequencer timer 
SND_TIMER_SCLASS_OSS_SEQUENCER = 3	# 	*< OSS sequencer timer 
SND_TIMER_SCLASS_LAST = SND_TIMER_SCLASS_OSS_SEQUENCER	# *< last slave timer 
snd_timer_slave_class_t = _snd_timer_slave_class 

# timer read event identification 
_snd_timer_event = c_int
SND_TIMER_EVENT_RESOLUTION = 0 #  val = resolution in ns 
SND_TIMER_EVENT_TICK = 1	 #  val = ticks 
SND_TIMER_EVENT_START = 2	 #  val = resolution in ns 
SND_TIMER_EVENT_STOP = 3	 #  val = 0 
SND_TIMER_EVENT_CONTINUE = 4 #  val = resolution in ns 
SND_TIMER_EVENT_PAUSE = 5	 #  val = 0 
SND_TIMER_EVENT_EARLY = 6	 #  val = 0 
SND_TIMER_EVENT_SUSPEND = 7	 #  val = 0 
SND_TIMER_EVENT_RESUME = 8	 #  val = resolution in ns 
# master timer events for slave timer instances 
SND_TIMER_EVENT_MSTART = SND_TIMER_EVENT_START + 10
SND_TIMER_EVENT_MSTOP = SND_TIMER_EVENT_STOP + 10
SND_TIMER_EVENT_MCONTINUE = SND_TIMER_EVENT_CONTINUE + 10
SND_TIMER_EVENT_MPAUSE = SND_TIMER_EVENT_PAUSE + 10
SND_TIMER_EVENT_MSUSPEND = SND_TIMER_EVENT_SUSPEND + 10
SND_TIMER_EVENT_MRESUME = SND_TIMER_EVENT_RESUME + 10	
snd_timer_event_t = _snd_timer_event 

# timer read structure 
class _snd_timer_read(Structure):
    _fields_ = [
            ('resolution', c_uint), # *< tick resolution in nanoseconds 
            ('ticks', c_uint) # *< count of happened ticks 
            ]
snd_timer_read_t = _snd_timer_read

# timer tstamp + event read structure 
class _snd_timer_tread(Structure):
    _fields_ = [
            ('event', snd_timer_event_t), # *< Timer event 
            ('tstamp', snd_htimestamp_t), # *< Time stamp of each event 
            ('val', c_uint) # *< Event value 
            ]
snd_timer_tread_t = _snd_timer_tread

# global timer - system 
SND_TIMER_GLOBAL_SYSTEM = 0
# global timer - RTC 
SND_TIMER_GLOBAL_RTC 	= 1
# global timer - HPET 
SND_TIMER_GLOBAL_HPET	= 2
# global timer - HRTIMER 
SND_TIMER_GLOBAL_HRTIMER = 3

# timer open mode flag - non-blocking behaviour 
SND_TIMER_OPEN_NONBLOCK	= (1<<0)
# use timestamps and event notification - enhanced read 
SND_TIMER_OPEN_TREAD = (1<<1)

# timer handle type 
_snd_timer_type = c_int
# Kernel level HwDep 
SND_TIMER_TYPE_HW = 0
# Shared memory client timer (not yet implemented) 
SND_TIMER_TYPE_SHM = 1
# INET client timer (not yet implemented) 
SND_TIMER_TYPE_INET = 2
snd_timer_type_t = _snd_timer_type 

# timer query handle 
class _snd_timer_query(Structure):
    _fields_ = [
            ]
snd_timer_query_t = _snd_timer_query 
# timer handle 
class _snd_timer(Structure):
    _fields_ = [
            ]
snd_timer_t = _snd_timer 


#int snd_timer_query_open(snd_timer_query_t **handle, const char *name, int mode);
snd_timer_query_open = _alsa_lib.snd_timer_query_open
snd_timer_query_open.argtypes = [POINTER(POINTER(snd_timer_query_t)), c_char_p, c_int]
snd_timer_query_open.restype = c_int

#int snd_timer_query_open_lconf(snd_timer_query_t **handle, const char *name, int mode, snd_config_t *lconf);
snd_timer_query_open_lconf = _alsa_lib.snd_timer_query_open_lconf
snd_timer_query_open_lconf.argtypes = [POINTER(POINTER(snd_timer_query_t)), c_char_p, c_int, POINTER(snd_config_t)]
snd_timer_query_open_lconf.restype = c_int

#int snd_timer_query_close(snd_timer_query_t *handle);
snd_timer_query_close = _alsa_lib.snd_timer_query_close
snd_timer_query_close.argtypes = [POINTER(snd_timer_query_t)]
snd_timer_query_close.restype = c_int

#int snd_timer_query_next_device(snd_timer_query_t *handle, snd_timer_id_t *tid);
snd_timer_query_next_device = _alsa_lib.snd_timer_query_next_device
snd_timer_query_next_device.argtypes = [POINTER(snd_timer_query_t), POINTER(snd_timer_id_t)]
snd_timer_query_next_device.restype = c_int

#int snd_timer_query_info(snd_timer_query_t *handle, snd_timer_ginfo_t *info);
snd_timer_query_info = _alsa_lib.snd_timer_query_info
snd_timer_query_info.argtypes = [POINTER(snd_timer_query_t), POINTER(snd_timer_ginfo_t)]
snd_timer_query_info.restype = c_int

#int snd_timer_query_params(snd_timer_query_t *handle, snd_timer_gparams_t *params);
snd_timer_query_params = _alsa_lib.snd_timer_query_params
snd_timer_query_params.argtypes = [POINTER(snd_timer_query_t), POINTER(snd_timer_gparams_t)]
snd_timer_query_params.restype = c_int

#int snd_timer_query_status(snd_timer_query_t *handle, snd_timer_gstatus_t *status);
snd_timer_query_status = _alsa_lib.snd_timer_query_status
snd_timer_query_status.argtypes = [POINTER(snd_timer_query_t), POINTER(snd_timer_gstatus_t)]
snd_timer_query_status.restype = c_int


#int snd_timer_open(snd_timer_t **handle, const char *name, int mode);
snd_timer_open = _alsa_lib.snd_timer_open
snd_timer_open.argtypes = [POINTER(POINTER(snd_timer_t)), c_char_p, c_int]
snd_timer_open.restype = c_int

#int snd_timer_open_lconf(snd_timer_t **handle, const char *name, int mode, snd_config_t *lconf);
snd_timer_open_lconf = _alsa_lib.snd_timer_open_lconf
snd_timer_open_lconf.argtypes = [POINTER(POINTER(snd_timer_t)), c_char_p, c_int, POINTER(snd_config_t)]
snd_timer_open_lconf.restype = c_int

#int snd_timer_close(snd_timer_t *handle);
snd_timer_close = _alsa_lib.snd_timer_close
snd_timer_close.argtypes = [POINTER(snd_timer_t)]
snd_timer_close.restype = c_int

#int snd_async_add_timer_handler(snd_async_handler_t **handler, snd_timer_t *timer,
				#snd_async_callback_t callback, void *private_data);
snd_async_add_timer_handler = _alsa_lib.snd_async_add_timer_handler
snd_async_add_timer_handler.argtypes = [POINTER(POINTER(snd_async_handler_t)), POINTER(snd_timer_t), snd_async_callback_t, c_void_p]
snd_async_add_timer_handler.restype = c_int

#snd_timer_t *snd_async_handler_get_timer(snd_async_handler_t *handler);
snd_async_handler_get_timer = _alsa_lib.snd_async_handler_get_timer
snd_async_handler_get_timer.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_timer.restype = POINTER(snd_timer_t)

#int snd_timer_poll_descriptors_count(snd_timer_t *handle);
snd_timer_poll_descriptors_count = _alsa_lib.snd_timer_poll_descriptors_count
snd_timer_poll_descriptors_count.argtypes = [POINTER(snd_timer_t)]
snd_timer_poll_descriptors_count.restype = c_int

#int snd_timer_poll_descriptors(snd_timer_t *handle, struct pollfd *pfds, unsigned int space);
snd_timer_poll_descriptors = _alsa_lib.snd_timer_poll_descriptors
snd_timer_poll_descriptors.argtypes = [POINTER(snd_timer_t), POINTER(pollfd), c_uint]
snd_timer_poll_descriptors.restype = c_int

#int snd_timer_poll_descriptors_revents(snd_timer_t *timer, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_timer_poll_descriptors_revents = _alsa_lib.snd_timer_poll_descriptors_revents
snd_timer_poll_descriptors_revents.argtypes = [POINTER(snd_timer_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_timer_poll_descriptors_revents.restype = c_int

#int snd_timer_info(snd_timer_t *handle, snd_timer_info_t *timer);
snd_timer_info = _alsa_lib.snd_timer_info
snd_timer_info.argtypes = [POINTER(snd_timer_t), POINTER(snd_timer_info_t)]
snd_timer_info.restype = c_int

#int snd_timer_params(snd_timer_t *handle, snd_timer_params_t *params);
snd_timer_params = _alsa_lib.snd_timer_params
snd_timer_params.argtypes = [POINTER(snd_timer_t), POINTER(snd_timer_params_t)]
snd_timer_params.restype = c_int

#int snd_timer_status(snd_timer_t *handle, snd_timer_status_t *status);
snd_timer_status = _alsa_lib.snd_timer_status
snd_timer_status.argtypes = [POINTER(snd_timer_t), POINTER(snd_timer_status_t)]
snd_timer_status.restype = c_int

#int snd_timer_start(snd_timer_t *handle);
snd_timer_start = _alsa_lib.snd_timer_start
snd_timer_start.argtypes = [POINTER(snd_timer_t)]
snd_timer_start.restype = c_int

#int snd_timer_stop(snd_timer_t *handle);
snd_timer_stop = _alsa_lib.snd_timer_stop
snd_timer_stop.argtypes = [POINTER(snd_timer_t)]
snd_timer_stop.restype = c_int

#int snd_timer_continue(snd_timer_t *handle);
snd_timer_continue = _alsa_lib.snd_timer_continue
snd_timer_continue.argtypes = [POINTER(snd_timer_t)]
snd_timer_continue.restype = c_int

#ssize_t snd_timer_read(snd_timer_t *handle, void *buffer, size_t size);
snd_timer_read = _alsa_lib.snd_timer_read
snd_timer_read.argtypes = [POINTER(snd_timer_t), c_void_p, c_size_t]
snd_timer_read.restype = c_size_t


#size_t snd_timer_id_sizeof(void);
snd_timer_id_sizeof = _alsa_lib.snd_timer_id_sizeof
snd_timer_id_sizeof.argtypes = []
snd_timer_id_sizeof.restype = c_size_t

# allocate #snd_timer_id_t container on stack 
#define snd_timer_id_alloca(ptr) __snd_alloca(ptr, snd_timer_id)
#int snd_timer_id_malloc(snd_timer_id_t **ptr);
snd_timer_id_malloc = _alsa_lib.snd_timer_id_malloc
snd_timer_id_malloc.argtypes = [POINTER(POINTER(snd_timer_id_t))]
snd_timer_id_malloc.restype = c_int

#void snd_timer_id_free(snd_timer_id_t *obj);
snd_timer_id_free = _alsa_lib.snd_timer_id_free
snd_timer_id_free.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_free.restype = None

#void snd_timer_id_copy(snd_timer_id_t *dst, const snd_timer_id_t *src);
snd_timer_id_copy = _alsa_lib.snd_timer_id_copy
snd_timer_id_copy.argtypes = [POINTER(snd_timer_id_t), POINTER(snd_timer_id_t)]
snd_timer_id_copy.restype = None


#void snd_timer_id_set_class(snd_timer_id_t *id, int dev_class);
snd_timer_id_set_class = _alsa_lib.snd_timer_id_set_class
snd_timer_id_set_class.argtypes = [POINTER(snd_timer_id_t), c_int]
snd_timer_id_set_class.restype = None

#int snd_timer_id_get_class(snd_timer_id_t *id);
snd_timer_id_get_class = _alsa_lib.snd_timer_id_get_class
snd_timer_id_get_class.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_get_class.restype = c_int

#void snd_timer_id_set_sclass(snd_timer_id_t *id, int dev_sclass);
snd_timer_id_set_sclass = _alsa_lib.snd_timer_id_set_sclass
snd_timer_id_set_sclass.argtypes = [POINTER(snd_timer_id_t), c_int]
snd_timer_id_set_sclass.restype = None

#int snd_timer_id_get_sclass(snd_timer_id_t *id);
snd_timer_id_get_sclass = _alsa_lib.snd_timer_id_get_sclass
snd_timer_id_get_sclass.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_get_sclass.restype = c_int

#void snd_timer_id_set_card(snd_timer_id_t *id, int card);
snd_timer_id_set_card = _alsa_lib.snd_timer_id_set_card
snd_timer_id_set_card.argtypes = [POINTER(snd_timer_id_t), c_int]
snd_timer_id_set_card.restype = None

#int snd_timer_id_get_card(snd_timer_id_t *id);
snd_timer_id_get_card = _alsa_lib.snd_timer_id_get_card
snd_timer_id_get_card.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_get_card.restype = c_int

#void snd_timer_id_set_device(snd_timer_id_t *id, int device);
snd_timer_id_set_device = _alsa_lib.snd_timer_id_set_device
snd_timer_id_set_device.argtypes = [POINTER(snd_timer_id_t), c_int]
snd_timer_id_set_device.restype = None

#int snd_timer_id_get_device(snd_timer_id_t *id);
snd_timer_id_get_device = _alsa_lib.snd_timer_id_get_device
snd_timer_id_get_device.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_get_device.restype = c_int

#void snd_timer_id_set_subdevice(snd_timer_id_t *id, int subdevice);
snd_timer_id_set_subdevice = _alsa_lib.snd_timer_id_set_subdevice
snd_timer_id_set_subdevice.argtypes = [POINTER(snd_timer_id_t), c_int]
snd_timer_id_set_subdevice.restype = None

#int snd_timer_id_get_subdevice(snd_timer_id_t *id);
snd_timer_id_get_subdevice = _alsa_lib.snd_timer_id_get_subdevice
snd_timer_id_get_subdevice.argtypes = [POINTER(snd_timer_id_t)]
snd_timer_id_get_subdevice.restype = c_int


#size_t snd_timer_ginfo_sizeof(void);
snd_timer_ginfo_sizeof = _alsa_lib.snd_timer_ginfo_sizeof
snd_timer_ginfo_sizeof.argtypes = []
snd_timer_ginfo_sizeof.restype = c_size_t

# allocate #snd_timer_ginfo_t container on stack 
#define snd_timer_ginfo_alloca(ptr) __snd_alloca(ptr, snd_timer_ginfo)
#int snd_timer_ginfo_malloc(snd_timer_ginfo_t **ptr);
snd_timer_ginfo_malloc = _alsa_lib.snd_timer_ginfo_malloc
snd_timer_ginfo_malloc.argtypes = [POINTER(POINTER(snd_timer_ginfo_t))]
snd_timer_ginfo_malloc.restype = c_int

#void snd_timer_ginfo_free(snd_timer_ginfo_t *obj);
snd_timer_ginfo_free = _alsa_lib.snd_timer_ginfo_free
snd_timer_ginfo_free.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_free.restype = None

#void snd_timer_ginfo_copy(snd_timer_ginfo_t *dst, const snd_timer_ginfo_t *src);
snd_timer_ginfo_copy = _alsa_lib.snd_timer_ginfo_copy
snd_timer_ginfo_copy.argtypes = [POINTER(snd_timer_ginfo_t), POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_copy.restype = None


#int snd_timer_ginfo_set_tid(snd_timer_ginfo_t *obj, snd_timer_id_t *tid);
snd_timer_ginfo_set_tid = _alsa_lib.snd_timer_ginfo_set_tid
snd_timer_ginfo_set_tid.argtypes = [POINTER(snd_timer_ginfo_t), POINTER(snd_timer_id_t)]
snd_timer_ginfo_set_tid.restype = c_int

#snd_timer_id_t *snd_timer_ginfo_get_tid(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_tid = _alsa_lib.snd_timer_ginfo_get_tid
snd_timer_ginfo_get_tid.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_tid.restype = POINTER(snd_timer_id_t)

#unsigned int snd_timer_ginfo_get_flags(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_flags = _alsa_lib.snd_timer_ginfo_get_flags
snd_timer_ginfo_get_flags.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_flags.restype = c_uint

#int snd_timer_ginfo_get_card(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_card = _alsa_lib.snd_timer_ginfo_get_card
snd_timer_ginfo_get_card.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_card.restype = c_int

#char *snd_timer_ginfo_get_id(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_id = _alsa_lib.snd_timer_ginfo_get_id
snd_timer_ginfo_get_id.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_id.restype = c_char_p

#char *snd_timer_ginfo_get_name(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_name = _alsa_lib.snd_timer_ginfo_get_name
snd_timer_ginfo_get_name.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_name.restype = c_char_p

#unsigned long snd_timer_ginfo_get_resolution(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_resolution = _alsa_lib.snd_timer_ginfo_get_resolution
snd_timer_ginfo_get_resolution.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_resolution.restype = c_ulong

#unsigned long snd_timer_ginfo_get_resolution_min(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_resolution_min = _alsa_lib.snd_timer_ginfo_get_resolution_min
snd_timer_ginfo_get_resolution_min.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_resolution_min.restype = c_ulong

#unsigned long snd_timer_ginfo_get_resolution_max(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_resolution_max = _alsa_lib.snd_timer_ginfo_get_resolution_max
snd_timer_ginfo_get_resolution_max.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_resolution_max.restype = c_ulong

#unsigned int snd_timer_ginfo_get_clients(snd_timer_ginfo_t *obj);
snd_timer_ginfo_get_clients = _alsa_lib.snd_timer_ginfo_get_clients
snd_timer_ginfo_get_clients.argtypes = [POINTER(snd_timer_ginfo_t)]
snd_timer_ginfo_get_clients.restype = c_uint


#size_t snd_timer_info_sizeof(void);
snd_timer_info_sizeof = _alsa_lib.snd_timer_info_sizeof
snd_timer_info_sizeof.argtypes = []
snd_timer_info_sizeof.restype = c_size_t

# allocate #snd_timer_info_t container on stack 
#define snd_timer_info_alloca(ptr) __snd_alloca(ptr, snd_timer_info)
#int snd_timer_info_malloc(snd_timer_info_t **ptr);
snd_timer_info_malloc = _alsa_lib.snd_timer_info_malloc
snd_timer_info_malloc.argtypes = [POINTER(POINTER(snd_timer_info_t))]
snd_timer_info_malloc.restype = c_int

#void snd_timer_info_free(snd_timer_info_t *obj);
snd_timer_info_free = _alsa_lib.snd_timer_info_free
snd_timer_info_free.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_free.restype = None

#void snd_timer_info_copy(snd_timer_info_t *dst, const snd_timer_info_t *src);
snd_timer_info_copy = _alsa_lib.snd_timer_info_copy
snd_timer_info_copy.argtypes = [POINTER(snd_timer_info_t), POINTER(snd_timer_info_t)]
snd_timer_info_copy.restype = None


#int snd_timer_info_is_slave(snd_timer_info_t * info);
snd_timer_info_is_slave = _alsa_lib.snd_timer_info_is_slave
snd_timer_info_is_slave.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_is_slave.restype = c_int

#int snd_timer_info_get_card(snd_timer_info_t * info);
snd_timer_info_get_card = _alsa_lib.snd_timer_info_get_card
snd_timer_info_get_card.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_get_card.restype = c_int

#const char *snd_timer_info_get_id(snd_timer_info_t * info);
snd_timer_info_get_id = _alsa_lib.snd_timer_info_get_id
snd_timer_info_get_id.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_get_id.restype = c_char_p

#const char *snd_timer_info_get_name(snd_timer_info_t * info);
snd_timer_info_get_name = _alsa_lib.snd_timer_info_get_name
snd_timer_info_get_name.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_get_name.restype = c_char_p

#long snd_timer_info_get_resolution(snd_timer_info_t * info);
snd_timer_info_get_resolution = _alsa_lib.snd_timer_info_get_resolution
snd_timer_info_get_resolution.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_get_resolution.restype = c_long


#size_t snd_timer_params_sizeof(void);
snd_timer_params_sizeof = _alsa_lib.snd_timer_params_sizeof
snd_timer_params_sizeof.argtypes = []
snd_timer_params_sizeof.restype = c_size_t

# allocate #snd_timer_params_t container on stack 
#define snd_timer_params_alloca(ptr) __snd_alloca(ptr, snd_timer_params)
#int snd_timer_params_malloc(snd_timer_params_t **ptr);
snd_timer_params_malloc = _alsa_lib.snd_timer_params_malloc
snd_timer_params_malloc.argtypes = [POINTER(POINTER(snd_timer_params_t))]
snd_timer_params_malloc.restype = c_int

#void snd_timer_params_free(snd_timer_params_t *obj);
snd_timer_params_free = _alsa_lib.snd_timer_params_free
snd_timer_params_free.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_free.restype = None

#void snd_timer_params_copy(snd_timer_params_t *dst, const snd_timer_params_t *src);
snd_timer_params_copy = _alsa_lib.snd_timer_params_copy
snd_timer_params_copy.argtypes = [POINTER(snd_timer_params_t), POINTER(snd_timer_params_t)]
snd_timer_params_copy.restype = None


#int snd_timer_params_set_auto_start(snd_timer_params_t * params, int auto_start);
snd_timer_params_set_auto_start = _alsa_lib.snd_timer_params_set_auto_start
snd_timer_params_set_auto_start.argtypes = [POINTER(snd_timer_params_t), c_int]
snd_timer_params_set_auto_start.restype = c_int

#int snd_timer_params_get_auto_start(snd_timer_params_t * params);
snd_timer_params_get_auto_start = _alsa_lib.snd_timer_params_get_auto_start
snd_timer_params_get_auto_start.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_auto_start.restype = c_int

#int snd_timer_params_set_exclusive(snd_timer_params_t * params, int exclusive);
snd_timer_params_set_exclusive = _alsa_lib.snd_timer_params_set_exclusive
snd_timer_params_set_exclusive.argtypes = [POINTER(snd_timer_params_t), c_int]
snd_timer_params_set_exclusive.restype = c_int

#int snd_timer_params_get_exclusive(snd_timer_params_t * params);
snd_timer_params_get_exclusive = _alsa_lib.snd_timer_params_get_exclusive
snd_timer_params_get_exclusive.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_exclusive.restype = c_int

#int snd_timer_params_set_early_event(snd_timer_params_t * params, int early_event);
snd_timer_params_set_early_event = _alsa_lib.snd_timer_params_set_early_event
snd_timer_params_set_early_event.argtypes = [POINTER(snd_timer_params_t), c_int]
snd_timer_params_set_early_event.restype = c_int

#int snd_timer_params_get_early_event(snd_timer_params_t * params);
snd_timer_params_get_early_event = _alsa_lib.snd_timer_params_get_early_event
snd_timer_params_get_early_event.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_early_event.restype = c_int

#void snd_timer_params_set_ticks(snd_timer_params_t * params, long ticks);
snd_timer_params_set_ticks = _alsa_lib.snd_timer_params_set_ticks
snd_timer_params_set_ticks.argtypes = [POINTER(snd_timer_params_t), c_long]
snd_timer_params_set_ticks.restype = None

#long snd_timer_params_get_ticks(snd_timer_params_t * params);
snd_timer_params_get_ticks = _alsa_lib.snd_timer_params_get_ticks
snd_timer_params_get_ticks.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_ticks.restype = c_long

#void snd_timer_params_set_queue_size(snd_timer_params_t * params, long queue_size);
snd_timer_params_set_queue_size = _alsa_lib.snd_timer_params_set_queue_size
snd_timer_params_set_queue_size.argtypes = [POINTER(snd_timer_params_t), c_long]
snd_timer_params_set_queue_size.restype = None

#long snd_timer_params_get_queue_size(snd_timer_params_t * params);
snd_timer_params_get_queue_size = _alsa_lib.snd_timer_params_get_queue_size
snd_timer_params_get_queue_size.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_queue_size.restype = c_long

#void snd_timer_params_set_filter(snd_timer_params_t * params, unsigned int filter);
snd_timer_params_set_filter = _alsa_lib.snd_timer_params_set_filter
snd_timer_params_set_filter.argtypes = [POINTER(snd_timer_params_t), c_uint]
snd_timer_params_set_filter.restype = None

#unsigned int snd_timer_params_get_filter(snd_timer_params_t * params);
snd_timer_params_get_filter = _alsa_lib.snd_timer_params_get_filter
snd_timer_params_get_filter.argtypes = [POINTER(snd_timer_params_t)]
snd_timer_params_get_filter.restype = c_uint


#size_t snd_timer_status_sizeof(void);
snd_timer_status_sizeof = _alsa_lib.snd_timer_status_sizeof
snd_timer_status_sizeof.argtypes = []
snd_timer_status_sizeof.restype = c_size_t

# allocate #snd_timer_status_t container on stack 
#define snd_timer_status_alloca(ptr) __snd_alloca(ptr, snd_timer_status)
#int snd_timer_status_malloc(snd_timer_status_t **ptr);
snd_timer_status_malloc = _alsa_lib.snd_timer_status_malloc
snd_timer_status_malloc.argtypes = [POINTER(POINTER(snd_timer_status_t))]
snd_timer_status_malloc.restype = c_int

#void snd_timer_status_free(snd_timer_status_t *obj);
snd_timer_status_free = _alsa_lib.snd_timer_status_free
snd_timer_status_free.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_free.restype = None

#void snd_timer_status_copy(snd_timer_status_t *dst, const snd_timer_status_t *src);
snd_timer_status_copy = _alsa_lib.snd_timer_status_copy
snd_timer_status_copy.argtypes = [POINTER(snd_timer_status_t), POINTER(snd_timer_status_t)]
snd_timer_status_copy.restype = None


#snd_htimestamp_t snd_timer_status_get_timestamp(snd_timer_status_t * status);
snd_timer_status_get_timestamp = _alsa_lib.snd_timer_status_get_timestamp
snd_timer_status_get_timestamp.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_get_timestamp.restype = snd_htimestamp_t

#long snd_timer_status_get_resolution(snd_timer_status_t * status);
snd_timer_status_get_resolution = _alsa_lib.snd_timer_status_get_resolution
snd_timer_status_get_resolution.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_get_resolution.restype = c_long

#long snd_timer_status_get_lost(snd_timer_status_t * status);
snd_timer_status_get_lost = _alsa_lib.snd_timer_status_get_lost
snd_timer_status_get_lost.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_get_lost.restype = c_long

#long snd_timer_status_get_overrun(snd_timer_status_t * status);
snd_timer_status_get_overrun = _alsa_lib.snd_timer_status_get_overrun
snd_timer_status_get_overrun.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_get_overrun.restype = c_long

#long snd_timer_status_get_queue(snd_timer_status_t * status);
snd_timer_status_get_queue = _alsa_lib.snd_timer_status_get_queue
snd_timer_status_get_queue.argtypes = [POINTER(snd_timer_status_t)]
snd_timer_status_get_queue.restype = c_long


# deprecated functions, for compatibility 
#long snd_timer_info_get_ticks(snd_timer_info_t * info);
snd_timer_info_get_ticks = _alsa_lib.snd_timer_info_get_ticks
snd_timer_info_get_ticks.argtypes = [POINTER(snd_timer_info_t)]
snd_timer_info_get_ticks.restype = c_long
