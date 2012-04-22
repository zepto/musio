#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides alsa rawmidi.
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


""" An alsa rawmidi module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .alsa_conf import *

#
#  \defgroup RawMidi RawMidi Interface
#  The RawMidi Interface. See \ref rawmidi page for more details.
#  \{
#

# dlsym version for interface entry callback 
#define SND_RAWMIDI_DLSYM_VERSION	_dlsym_rawmidi_001

# RawMidi information container 
class _snd_rawmidi_info(Structure):
    _fields_ = [
            ]
snd_rawmidi_info_t = _snd_rawmidi_info 
# RawMidi settings container 
class _snd_rawmidi_params(Structure):
    _fields_ = [
            ]
snd_rawmidi_params_t = _snd_rawmidi_params 
# RawMidi status container 
class _snd_rawmidi_status(Structure):
    _fields_ = [
            ]
snd_rawmidi_status_t = _snd_rawmidi_status 

# RawMidi stream (direction) 
_snd_rawmidi_stream = c_int
# Output stream 
SND_RAWMIDI_STREAM_OUTPUT = 0
# Input stream 
SND_RAWMIDI_STREAM_INPUT = 1
SND_RAWMIDI_STREAM_LAST = SND_RAWMIDI_STREAM_INPUT
snd_rawmidi_stream_t = _snd_rawmidi_stream

# Append (flag to open mode) \hideinitializer 
SND_RAWMIDI_APPEND = 0x0001
# Non blocking mode (flag to open mode) \hideinitializer 
SND_RAWMIDI_NONBLOCK = 0x0002
# Write sync mode (Flag to open mode) \hideinitializer 
SND_RAWMIDI_SYNC = 0x0004

# RawMidi handle 
class _snd_rawmidi(Structure):
    _fields = [
            ]
snd_rawmidi_t = _snd_rawmidi 

# RawMidi type 
_snd_rawmidi_type = c_int
# Kernel level RawMidi 
SND_RAWMIDI_TYPE_HW = 0
# Shared memory client RawMidi (not yet implemented) 
SND_RAWMIDI_TYPE_SHM = 1
# INET client RawMidi (not yet implemented) 
SND_RAWMIDI_TYPE_INET = 2
# Virtual (sequencer) RawMidi 
SND_RAWMIDI_TYPE_VIRTUAL = 3
snd_rawmidi_type_t = _snd_rawmidi_type 

#int snd_rawmidi_open(snd_rawmidi_t **in_rmidi, snd_rawmidi_t **out_rmidi,
			 #const char *name, int mode);
snd_rawmidi_open = _alsa_lib.snd_rawmidi_open
snd_rawmidi_open.argtypes = [POINTER(POINTER(snd_rawmidi_t)), POINTER(POINTER(snd_rawmidi_t)), c_char_p, c_int]
snd_rawmidi_open.restype = c_int

#int snd_rawmidi_open_lconf(snd_rawmidi_t **in_rmidi, snd_rawmidi_t **out_rmidi,
			   #const char *name, int mode, snd_config_t *lconf);
snd_rawmidi_open_lconf = _alsa_lib.snd_rawmidi_open_lconf
snd_rawmidi_open_lconf.argtypes = [POINTER(POINTER(snd_rawmidi_t)), POINTER(POINTER(snd_rawmidi_t)), c_char_p, c_int, POINTER(snd_config_t)]
snd_rawmidi_open_lconf.restype = c_int

#int snd_rawmidi_close(snd_rawmidi_t *rmidi);
snd_rawmidi_close = _alsa_lib.snd_rawmidi_close
snd_rawmidi_close.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_close.restype = c_int

#int snd_rawmidi_poll_descriptors_count(snd_rawmidi_t *rmidi);
snd_rawmidi_poll_descriptors_count = _alsa_lib.snd_rawmidi_poll_descriptors_count
snd_rawmidi_poll_descriptors_count.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_poll_descriptors_count.restype = c_int

#int snd_rawmidi_poll_descriptors(snd_rawmidi_t *rmidi, struct pollfd *pfds, unsigned int space);
snd_rawmidi_poll_descriptors = _alsa_lib.snd_rawmidi_poll_descriptors
snd_rawmidi_poll_descriptors.argtypes = [POINTER(snd_rawmidi_t), POINTER(pollfd), c_uint]
snd_rawmidi_poll_descriptors.restype = c_int

#int snd_rawmidi_poll_descriptors_revents(snd_rawmidi_t *rawmidi, struct pollfd *pfds, unsigned int nfds, unsigned short *revent);
snd_rawmidi_poll_descriptors_revents = _alsa_lib.snd_rawmidi_poll_descriptors_revents
snd_rawmidi_poll_descriptors_revents.argtypes = [POINTER(snd_rawmidi_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_rawmidi_poll_descriptors_revents.restype = c_int

#int snd_rawmidi_nonblock(snd_rawmidi_t *rmidi, int nonblock);
snd_rawmidi_nonblock = _alsa_lib.snd_rawmidi_nonblock
snd_rawmidi_nonblock.argtypes = [POINTER(snd_rawmidi_t), c_int]
snd_rawmidi_nonblock.restype = c_int

#size_t snd_rawmidi_info_sizeof(void);
snd_rawmidi_info_sizeof = _alsa_lib.snd_rawmidi_info_sizeof
snd_rawmidi_info_sizeof.argtypes = []
snd_rawmidi_info_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_rawmidi_info_t using standard alloca
# \param ptr returned pointer
#
#define snd_rawmidi_info_alloca(ptr) __snd_alloca(ptr, snd_rawmidi_info)
#int snd_rawmidi_info_malloc(snd_rawmidi_info_t **ptr);
snd_rawmidi_info_malloc = _alsa_lib.snd_rawmidi_info_malloc
snd_rawmidi_info_malloc.argtypes = [POINTER(POINTER(snd_rawmidi_info_t))]
snd_rawmidi_info_malloc.restype = c_int

#void snd_rawmidi_info_free(snd_rawmidi_info_t *obj);
snd_rawmidi_info_free = _alsa_lib.snd_rawmidi_info_free
snd_rawmidi_info_free.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_free.restype = None

#void snd_rawmidi_info_copy(snd_rawmidi_info_t *dst, const snd_rawmidi_info_t *src);
snd_rawmidi_info_copy = _alsa_lib.snd_rawmidi_info_copy
snd_rawmidi_info_copy.argtypes = [POINTER(snd_rawmidi_info_t), POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_copy.restype = None

#unsigned int snd_rawmidi_info_get_device(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_device = _alsa_lib.snd_rawmidi_info_get_device
snd_rawmidi_info_get_device.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_device.restype = c_uint

#unsigned int snd_rawmidi_info_get_subdevice(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_subdevice = _alsa_lib.snd_rawmidi_info_get_subdevice
snd_rawmidi_info_get_subdevice.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_subdevice.restype = c_uint

#snd_rawmidi_stream_t snd_rawmidi_info_get_stream(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_stream = _alsa_lib.snd_rawmidi_info_get_stream
snd_rawmidi_info_get_stream.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_stream.restype = snd_rawmidi_stream_t

#int snd_rawmidi_info_get_card(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_card = _alsa_lib.snd_rawmidi_info_get_card
snd_rawmidi_info_get_card.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_card.restype = c_int

#unsigned int snd_rawmidi_info_get_flags(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_flags = _alsa_lib.snd_rawmidi_info_get_flags
snd_rawmidi_info_get_flags.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_flags.restype = c_uint

#const char *snd_rawmidi_info_get_id(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_id = _alsa_lib.snd_rawmidi_info_get_id
snd_rawmidi_info_get_id.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_id.restype = c_char_p

#const char *snd_rawmidi_info_get_name(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_name = _alsa_lib.snd_rawmidi_info_get_name
snd_rawmidi_info_get_name.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_name.restype = c_char_p

#const char *snd_rawmidi_info_get_subdevice_name(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_subdevice_name = _alsa_lib.snd_rawmidi_info_get_subdevice_name
snd_rawmidi_info_get_subdevice_name.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_subdevice_name.restype = c_char_p

#unsigned int snd_rawmidi_info_get_subdevices_count(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_subdevices_count = _alsa_lib.snd_rawmidi_info_get_subdevices_count
snd_rawmidi_info_get_subdevices_count.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_subdevices_count.restype = c_uint

#unsigned int snd_rawmidi_info_get_subdevices_avail(const snd_rawmidi_info_t *obj);
snd_rawmidi_info_get_subdevices_avail = _alsa_lib.snd_rawmidi_info_get_subdevices_avail
snd_rawmidi_info_get_subdevices_avail.argtypes = [POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info_get_subdevices_avail.restype = c_uint

#void snd_rawmidi_info_set_device(snd_rawmidi_info_t *obj, unsigned int val);
snd_rawmidi_info_set_device = _alsa_lib.snd_rawmidi_info_set_device
snd_rawmidi_info_set_device.argtypes = [POINTER(snd_rawmidi_info_t), c_uint]
snd_rawmidi_info_set_device.restype = None

#void snd_rawmidi_info_set_subdevice(snd_rawmidi_info_t *obj, unsigned int val);
snd_rawmidi_info_set_subdevice = _alsa_lib.snd_rawmidi_info_set_subdevice
snd_rawmidi_info_set_subdevice.argtypes = [POINTER(snd_rawmidi_info_t), c_uint]
snd_rawmidi_info_set_subdevice.restype = None

#void snd_rawmidi_info_set_stream(snd_rawmidi_info_t *obj, snd_rawmidi_stream_t val);
snd_rawmidi_info_set_stream = _alsa_lib.snd_rawmidi_info_set_stream
snd_rawmidi_info_set_stream.argtypes = [POINTER(snd_rawmidi_info_t), snd_rawmidi_stream_t]
snd_rawmidi_info_set_stream.restype = None

#int snd_rawmidi_info(snd_rawmidi_t *rmidi, snd_rawmidi_info_t * info);
snd_rawmidi_info = _alsa_lib.snd_rawmidi_info
snd_rawmidi_info.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_info_t)]
snd_rawmidi_info.restype = c_int

#size_t snd_rawmidi_params_sizeof(void);
snd_rawmidi_params_sizeof = _alsa_lib.snd_rawmidi_params_sizeof
snd_rawmidi_params_sizeof.argtypes = []
snd_rawmidi_params_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_rawmidi_params_t using standard alloca
# \param ptr returned pointer
#
#define snd_rawmidi_params_alloca(ptr) __snd_alloca(ptr, snd_rawmidi_params)
#int snd_rawmidi_params_malloc(snd_rawmidi_params_t **ptr);
snd_rawmidi_params_malloc = _alsa_lib.snd_rawmidi_params_malloc
snd_rawmidi_params_malloc.argtypes = [POINTER(POINTER(snd_rawmidi_params_t))]
snd_rawmidi_params_malloc.restype = c_int

#void snd_rawmidi_params_free(snd_rawmidi_params_t *obj);
snd_rawmidi_params_free = _alsa_lib.snd_rawmidi_params_free
snd_rawmidi_params_free.argtypes = [POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_free.restype = None

#void snd_rawmidi_params_copy(snd_rawmidi_params_t *dst, const snd_rawmidi_params_t *src);
snd_rawmidi_params_copy = _alsa_lib.snd_rawmidi_params_copy
snd_rawmidi_params_copy.argtypes = [POINTER(snd_rawmidi_params_t), POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_copy.restype = None

#int snd_rawmidi_params_set_buffer_size(snd_rawmidi_t *rmidi, snd_rawmidi_params_t *params, size_t val);
snd_rawmidi_params_set_buffer_size = _alsa_lib.snd_rawmidi_params_set_buffer_size
snd_rawmidi_params_set_buffer_size.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_params_t), c_size_t]
snd_rawmidi_params_set_buffer_size.restype = c_int

#size_t snd_rawmidi_params_get_buffer_size(const snd_rawmidi_params_t *params);
snd_rawmidi_params_get_buffer_size = _alsa_lib.snd_rawmidi_params_get_buffer_size
snd_rawmidi_params_get_buffer_size.argtypes = [POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_get_buffer_size.restype = c_size_t

#int snd_rawmidi_params_set_avail_min(snd_rawmidi_t *rmidi, snd_rawmidi_params_t *params, size_t val);
snd_rawmidi_params_set_avail_min = _alsa_lib.snd_rawmidi_params_set_avail_min
snd_rawmidi_params_set_avail_min.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_params_t), c_size_t]
snd_rawmidi_params_set_avail_min.restype = c_int

#size_t snd_rawmidi_params_get_avail_min(const snd_rawmidi_params_t *params);
snd_rawmidi_params_get_avail_min = _alsa_lib.snd_rawmidi_params_get_avail_min
snd_rawmidi_params_get_avail_min.argtypes = [POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_get_avail_min.restype = c_size_t

#int snd_rawmidi_params_set_no_active_sensing(snd_rawmidi_t *rmidi, snd_rawmidi_params_t *params, int val);
snd_rawmidi_params_set_no_active_sensing = _alsa_lib.snd_rawmidi_params_set_no_active_sensing
snd_rawmidi_params_set_no_active_sensing.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_params_t), c_int]
snd_rawmidi_params_set_no_active_sensing.restype = c_int

#int snd_rawmidi_params_get_no_active_sensing(const snd_rawmidi_params_t *params);
snd_rawmidi_params_get_no_active_sensing = _alsa_lib.snd_rawmidi_params_get_no_active_sensing
snd_rawmidi_params_get_no_active_sensing.argtypes = [POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_get_no_active_sensing.restype = c_int

#int snd_rawmidi_params(snd_rawmidi_t *rmidi, snd_rawmidi_params_t * params);
snd_rawmidi_params = _alsa_lib.snd_rawmidi_params
snd_rawmidi_params.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params.restype = c_int

#int snd_rawmidi_params_current(snd_rawmidi_t *rmidi, snd_rawmidi_params_t *params);
snd_rawmidi_params_current = _alsa_lib.snd_rawmidi_params_current
snd_rawmidi_params_current.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_params_t)]
snd_rawmidi_params_current.restype = c_int

#size_t snd_rawmidi_status_sizeof(void);
snd_rawmidi_status_sizeof = _alsa_lib.snd_rawmidi_status_sizeof
snd_rawmidi_status_sizeof.argtypes = []
snd_rawmidi_status_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_rawmidi_status_t using standard alloca
# \param ptr returned pointer
#
#define snd_rawmidi_status_alloca(ptr) __snd_alloca(ptr, snd_rawmidi_status)
#int snd_rawmidi_status_malloc(snd_rawmidi_status_t **ptr);
snd_rawmidi_status_malloc = _alsa_lib.snd_rawmidi_status_malloc
snd_rawmidi_status_malloc.argtypes = [POINTER(POINTER(snd_rawmidi_status_t))]
snd_rawmidi_status_malloc.restype = c_int

#void snd_rawmidi_status_free(snd_rawmidi_status_t *obj);
snd_rawmidi_status_free = _alsa_lib.snd_rawmidi_status_free
snd_rawmidi_status_free.argtypes = [POINTER(snd_rawmidi_status_t)]
snd_rawmidi_status_free.restype = None

#void snd_rawmidi_status_copy(snd_rawmidi_status_t *dst, const snd_rawmidi_status_t *src);
snd_rawmidi_status_copy = _alsa_lib.snd_rawmidi_status_copy
snd_rawmidi_status_copy.argtypes = [POINTER(snd_rawmidi_status_t), POINTER(snd_rawmidi_status_t)]
snd_rawmidi_status_copy.restype = None

#void snd_rawmidi_status_get_tstamp(const snd_rawmidi_status_t *obj, snd_htimestamp_t *ptr);
snd_rawmidi_status_get_tstamp = _alsa_lib.snd_rawmidi_status_get_tstamp
snd_rawmidi_status_get_tstamp.argtypes = [POINTER(snd_rawmidi_status_t), POINTER(snd_htimestamp_t)]
snd_rawmidi_status_get_tstamp.restype = None

#size_t snd_rawmidi_status_get_avail(const snd_rawmidi_status_t *obj);
snd_rawmidi_status_get_avail = _alsa_lib.snd_rawmidi_status_get_avail
snd_rawmidi_status_get_avail.argtypes = [POINTER(snd_rawmidi_status_t)]
snd_rawmidi_status_get_avail.restype = c_size_t

#size_t snd_rawmidi_status_get_xruns(const snd_rawmidi_status_t *obj);
snd_rawmidi_status_get_xruns = _alsa_lib.snd_rawmidi_status_get_xruns
snd_rawmidi_status_get_xruns.argtypes = [POINTER(snd_rawmidi_status_t)]
snd_rawmidi_status_get_xruns.restype = c_size_t

#int snd_rawmidi_status(snd_rawmidi_t *rmidi, snd_rawmidi_status_t * status);
snd_rawmidi_status = _alsa_lib.snd_rawmidi_status
snd_rawmidi_status.argtypes = [POINTER(snd_rawmidi_t), POINTER(snd_rawmidi_status_t)]
snd_rawmidi_status.restype = c_int

#int snd_rawmidi_drain(snd_rawmidi_t *rmidi);
snd_rawmidi_drain = _alsa_lib.snd_rawmidi_drain
snd_rawmidi_drain.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_drain.restype = c_int

#int snd_rawmidi_drop(snd_rawmidi_t *rmidi);
snd_rawmidi_drop = _alsa_lib.snd_rawmidi_drop
snd_rawmidi_drop.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_drop.restype = c_int

#ssize_t snd_rawmidi_write(snd_rawmidi_t *rmidi, const void *buffer, size_t size);
snd_rawmidi_write = _alsa_lib.snd_rawmidi_write
snd_rawmidi_write.argtypes = [POINTER(snd_rawmidi_t), c_void_p, c_size_t]
snd_rawmidi_write.restype = c_size_t

#ssize_t snd_rawmidi_read(snd_rawmidi_t *rmidi, void *buffer, size_t size);
snd_rawmidi_read = _alsa_lib.snd_rawmidi_read
snd_rawmidi_read.argtypes = [POINTER(snd_rawmidi_t), c_void_p, c_size_t]
snd_rawmidi_read.restype = c_size_t

#const char *snd_rawmidi_name(snd_rawmidi_t *rmidi);
snd_rawmidi_name = _alsa_lib.snd_rawmidi_name
snd_rawmidi_name.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_name.restype = c_char_p

#snd_rawmidi_type_t snd_rawmidi_type(snd_rawmidi_t *rmidi);
snd_rawmidi_type = _alsa_lib.snd_rawmidi_type
snd_rawmidi_type.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_type.restype = snd_rawmidi_type_t

#snd_rawmidi_stream_t snd_rawmidi_stream(snd_rawmidi_t *rawmidi);
snd_rawmidi_stream = _alsa_lib.snd_rawmidi_stream
snd_rawmidi_stream.argtypes = [POINTER(snd_rawmidi_t)]
snd_rawmidi_stream.restype = snd_rawmidi_stream_t
