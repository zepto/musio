#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides access to alsa seq.
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


""" An alsa seq module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .seq_event import *
from .alsa_timer import *

#
#  \defgroup Sequencer MIDI Sequencer
#  MIDI Sequencer Interface.
#  See \ref seq page for more details.
#  \{
#

# dlsym version for interface entry callback 
#define SND_SEQ_DLSYM_VERSION		_dlsym_seq_001

# Sequencer handle 
class _snd_seq(Structure):
    _fields_ = [
            ]
snd_seq_t = _snd_seq

#
# sequencer opening stream types
#
SND_SEQ_OPEN_OUTPUT	= 1	# *< open for output (write) 
SND_SEQ_OPEN_INPUT  = 2	# *< open for input (read) 
SND_SEQ_OPEN_DUPLEX = (SND_SEQ_OPEN_OUTPUT|SND_SEQ_OPEN_INPUT) # *< open for both input and output (read/write) 

#
# sequencer opening mode
#
SND_SEQ_NONBLOCK = 0x0001 # *< non-blocking mode (flag to open mode) 

# sequencer handle type 
_snd_seq_type = c_int
SND_SEQ_TYPE_HW   = 0 # *< hardware 
SND_SEQ_TYPE_SHM  = 1 # *< shared memory (NYI) 
SND_SEQ_TYPE_INET = 2 # *< network (NYI) 
snd_seq_type_t = _snd_seq_type

# special client (port) ids 
SND_SEQ_ADDRESS_UNKNOWN		= 253 # *< unknown source 
SND_SEQ_ADDRESS_SUBSCRIBERS	= 254 # *< send event to all subscribed ports 
SND_SEQ_ADDRESS_BROADCAST	= 255 # *< send event to all queues/clients/ports/channels 

# known client numbers 
SND_SEQ_CLIENT_SYSTEM = 0 # *< system client 

#
#
#int snd_seq_open(snd_seq_t **handle, const char *name, int streams, int mode);
snd_seq_open = _alsa_lib.snd_seq_open
snd_seq_open.argtypes = [POINTER(POINTER(snd_seq_t)), POINTER(c_char), c_int, c_int]
snd_seq_open.restype = c_int

#int snd_seq_open_lconf(snd_seq_t **handle, const char *name, int streams, int mode, snd_config_t *lconf);
snd_seq_open_lconf = _alsa_lib.snd_seq_open_lconf
snd_seq_open_lconf.argtypes = [POINTER(POINTER(snd_seq_t)), POINTER(c_char), c_int, c_int, POINTER(snd_config_t)]
snd_seq_open_lconf.restype = c_int

#const char *snd_seq_name(snd_seq_t *seq);
snd_seq_name = _alsa_lib.snd_seq_name
snd_seq_name.argtypes = [POINTER(snd_seq_t)]
snd_seq_name.restype = c_char_p

#snd_seq_type_t snd_seq_type(snd_seq_t *seq);
snd_seq_type = _alsa_lib.snd_seq_type
snd_seq_type.argtypes = [POINTER(snd_seq_t)]
snd_seq_type.restype = snd_seq_type_t

#int snd_seq_close(snd_seq_t *handle);
snd_seq_close = _alsa_lib.snd_seq_close
snd_seq_close.argtypes = [POINTER(snd_seq_t)]
snd_seq_close.restype = c_int

#int snd_seq_poll_descriptors_count(snd_seq_t *handle, short events);
snd_seq_poll_descriptors_count = _alsa_lib.snd_seq_poll_descriptors_count
snd_seq_poll_descriptors_count.argtypes = [POINTER(snd_seq_t), c_short]
snd_seq_poll_descriptors_count.restype = c_int

#int snd_seq_poll_descriptors(snd_seq_t *handle, struct pollfd *pfds, unsigned int space, short events);
snd_seq_poll_descriptors = _alsa_lib.snd_seq_poll_descriptors
snd_seq_poll_descriptors.argtypes = [POINTER(snd_seq_t), POINTER(pollfd), c_uint, c_short]
snd_seq_poll_descriptors.restype = c_int

#int snd_seq_poll_descriptors_revents(snd_seq_t *seq, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_seq_poll_descriptors_revents = _alsa_lib.snd_seq_poll_descriptors_revents
snd_seq_poll_descriptors_revents.argtypes = [POINTER(snd_seq_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_seq_poll_descriptors_revents.restype = c_int

#int snd_seq_nonblock(snd_seq_t *handle, int nonblock);
snd_seq_nonblock = _alsa_lib.snd_seq_nonblock
snd_seq_nonblock.argtypes = [POINTER(snd_seq_t), c_int]
snd_seq_nonblock.restype = c_int

#int snd_seq_client_id(snd_seq_t *handle);
snd_seq_client_id = _alsa_lib.snd_seq_client_id
snd_seq_client_id.argtypes = [POINTER(snd_seq_t)]
snd_seq_client_id.restype = c_int


#size_t snd_seq_get_output_buffer_size(snd_seq_t *handle);
snd_seq_get_output_buffer_size = _alsa_lib.snd_seq_get_output_buffer_size
snd_seq_get_output_buffer_size.argtypes = [POINTER(snd_seq_t)]
snd_seq_get_output_buffer_size.restype = c_size_t

#size_t snd_seq_get_input_buffer_size(snd_seq_t *handle);
snd_seq_get_input_buffer_size = _alsa_lib.snd_seq_get_input_buffer_size
snd_seq_get_input_buffer_size.argtypes = [POINTER(snd_seq_t)]
snd_seq_get_input_buffer_size.restype = c_size_t

#int snd_seq_set_output_buffer_size(snd_seq_t *handle, size_t size);
snd_seq_set_output_buffer_size = _alsa_lib.snd_seq_set_output_buffer_size
snd_seq_set_output_buffer_size.argtypes = [POINTER(snd_seq_t), c_size_t]
snd_seq_set_output_buffer_size.restype = c_int

#int snd_seq_set_input_buffer_size(snd_seq_t *handle, size_t size);
snd_seq_set_input_buffer_size = _alsa_lib.snd_seq_set_input_buffer_size
snd_seq_set_input_buffer_size.argtypes = [POINTER(snd_seq_t), c_size_t]
snd_seq_set_input_buffer_size.restype = c_int


# system information container 
class _snd_seq_system_info(Structure):
    _fields_ = [
            ]
snd_seq_system_info_t = _snd_seq_system_info

#size_t snd_seq_system_info_sizeof(void);
snd_seq_system_info_sizeof = _alsa_lib.snd_seq_system_info_sizeof
snd_seq_system_info_sizeof.argtypes = []
snd_seq_system_info_sizeof.restype = c_size_t

# allocate a #snd_seq_system_info_t container on stack 
#define snd_seq_system_info_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_system_info)
#int snd_seq_system_info_malloc(snd_seq_system_info_t **ptr);
snd_seq_system_info_malloc = _alsa_lib.snd_seq_system_info_malloc
snd_seq_system_info_malloc.argtypes = [POINTER(POINTER(snd_seq_system_info_t))]
snd_seq_system_info_malloc.restype = c_int

#void snd_seq_system_info_free(snd_seq_system_info_t *ptr);
snd_seq_system_info_free = _alsa_lib.snd_seq_system_info_free
snd_seq_system_info_free.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_free.restype = None

#void snd_seq_system_info_copy(snd_seq_system_info_t *dst, const snd_seq_system_info_t *src);
snd_seq_system_info_copy = _alsa_lib.snd_seq_system_info_copy
snd_seq_system_info_copy.argtypes = [POINTER(snd_seq_system_info_t), POINTER(snd_seq_system_info_t)]
snd_seq_system_info_copy.restype = None


#int snd_seq_system_info_get_queues(const snd_seq_system_info_t *info);
snd_seq_system_info_get_queues = _alsa_lib.snd_seq_system_info_get_queues
snd_seq_system_info_get_queues.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_queues.restype = c_int

#int snd_seq_system_info_get_clients(const snd_seq_system_info_t *info);
snd_seq_system_info_get_clients = _alsa_lib.snd_seq_system_info_get_clients
snd_seq_system_info_get_clients.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_clients.restype = c_int

#int snd_seq_system_info_get_ports(const snd_seq_system_info_t *info);
snd_seq_system_info_get_ports = _alsa_lib.snd_seq_system_info_get_ports
snd_seq_system_info_get_ports.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_ports.restype = c_int

#int snd_seq_system_info_get_channels(const snd_seq_system_info_t *info);
snd_seq_system_info_get_channels = _alsa_lib.snd_seq_system_info_get_channels
snd_seq_system_info_get_channels.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_channels.restype = c_int

#int snd_seq_system_info_get_cur_clients(const snd_seq_system_info_t *info);
snd_seq_system_info_get_cur_clients = _alsa_lib.snd_seq_system_info_get_cur_clients
snd_seq_system_info_get_cur_clients.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_cur_clients.restype = c_int

#int snd_seq_system_info_get_cur_queues(const snd_seq_system_info_t *info);
snd_seq_system_info_get_cur_queues = _alsa_lib.snd_seq_system_info_get_cur_queues
snd_seq_system_info_get_cur_queues.argtypes = [POINTER(snd_seq_system_info_t)]
snd_seq_system_info_get_cur_queues.restype = c_int


#int snd_seq_system_info(snd_seq_t *handle, snd_seq_system_info_t *info);
snd_seq_system_info = _alsa_lib.snd_seq_system_info
snd_seq_system_info.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_system_info_t)]
snd_seq_system_info.restype = c_int


# \} 


#
#  \defgroup SeqClient Sequencer Client Interface
#  Sequencer Client Interface
#  \ingroup Sequencer
#  \{
#

# client information container 
class _snd_seq_client_info(Structure):
    _fields_ = [
            ]
snd_seq_client_info_t = _snd_seq_client_info

# client types 
snd_seq_client_type = c_int
SND_SEQ_USER_CLIENT     = 1 # *< user client 
SND_SEQ_KERNEL_CLIENT   = 2	# *< kernel client 
snd_seq_client_type_t = snd_seq_client_type 
                        
#size_t snd_seq_client_info_sizeof(void);
snd_seq_client_info_sizeof = _alsa_lib.snd_seq_client_info_sizeof
snd_seq_client_info_sizeof.argtypes = []
snd_seq_client_info_sizeof.restype = c_size_t

# allocate a #snd_seq_client_info_t container on stack 
#define snd_seq_client_info_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_client_info)
#int snd_seq_client_info_malloc(snd_seq_client_info_t **ptr);
snd_seq_client_info_malloc = _alsa_lib.snd_seq_client_info_malloc
snd_seq_client_info_malloc.argtypes = [POINTER(POINTER(snd_seq_client_info_t))]
snd_seq_client_info_malloc.restype = c_int

#void snd_seq_client_info_free(snd_seq_client_info_t *ptr);
snd_seq_client_info_free = _alsa_lib.snd_seq_client_info_free
snd_seq_client_info_free.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_free.restype = None

#void snd_seq_client_info_copy(snd_seq_client_info_t *dst, const snd_seq_client_info_t *src);
snd_seq_client_info_copy = _alsa_lib.snd_seq_client_info_copy
snd_seq_client_info_copy.argtypes = [POINTER(snd_seq_client_info_t), POINTER(snd_seq_client_info_t)]
snd_seq_client_info_copy.restype = None


#int snd_seq_client_info_get_client(const snd_seq_client_info_t *info);
snd_seq_client_info_get_client = _alsa_lib.snd_seq_client_info_get_client
snd_seq_client_info_get_client.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_client.restype = c_int

#snd_seq_client_type_t snd_seq_client_info_get_type(const snd_seq_client_info_t *info);
snd_seq_client_info_get_type = _alsa_lib.snd_seq_client_info_get_type
snd_seq_client_info_get_type.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_type.restype = snd_seq_client_type_t

#const char *snd_seq_client_info_get_name(snd_seq_client_info_t *info);
snd_seq_client_info_get_name = _alsa_lib.snd_seq_client_info_get_name
snd_seq_client_info_get_name.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_name.restype = c_char_p

#int snd_seq_client_info_get_broadcast_filter(const snd_seq_client_info_t *info);
snd_seq_client_info_get_broadcast_filter = _alsa_lib.snd_seq_client_info_get_broadcast_filter
snd_seq_client_info_get_broadcast_filter.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_broadcast_filter.restype = c_int

#int snd_seq_client_info_get_error_bounce(const snd_seq_client_info_t *info);
snd_seq_client_info_get_error_bounce = _alsa_lib.snd_seq_client_info_get_error_bounce
snd_seq_client_info_get_error_bounce.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_error_bounce.restype = c_int

#const unsigned char *snd_seq_client_info_get_event_filter(const snd_seq_client_info_t *info);
snd_seq_client_info_get_event_filter = _alsa_lib.snd_seq_client_info_get_event_filter
snd_seq_client_info_get_event_filter.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_event_filter.restype = POINTER(c_ubyte)

#int snd_seq_client_info_get_num_ports(const snd_seq_client_info_t *info);
snd_seq_client_info_get_num_ports = _alsa_lib.snd_seq_client_info_get_num_ports
snd_seq_client_info_get_num_ports.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_num_ports.restype = c_int

#int snd_seq_client_info_get_event_lost(const snd_seq_client_info_t *info);
snd_seq_client_info_get_event_lost = _alsa_lib.snd_seq_client_info_get_event_lost
snd_seq_client_info_get_event_lost.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_get_event_lost.restype = c_int


#void snd_seq_client_info_set_client(snd_seq_client_info_t *info, int client);
snd_seq_client_info_set_client = _alsa_lib.snd_seq_client_info_set_client
snd_seq_client_info_set_client.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_set_client.restype = None

#void snd_seq_client_info_set_name(snd_seq_client_info_t *info, const char *name);
snd_seq_client_info_set_name = _alsa_lib.snd_seq_client_info_set_name
snd_seq_client_info_set_name.argtypes = [POINTER(snd_seq_client_info_t), c_char_p]
snd_seq_client_info_set_name.restype = None

#void snd_seq_client_info_set_broadcast_filter(snd_seq_client_info_t *info, int val);
snd_seq_client_info_set_broadcast_filter = _alsa_lib.snd_seq_client_info_set_broadcast_filter
snd_seq_client_info_set_broadcast_filter.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_set_broadcast_filter.restype = None

#void snd_seq_client_info_set_error_bounce(snd_seq_client_info_t *info, int val);
snd_seq_client_info_set_error_bounce = _alsa_lib.snd_seq_client_info_set_error_bounce
snd_seq_client_info_set_error_bounce.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_set_error_bounce.restype = None

#void snd_seq_client_info_set_event_filter(snd_seq_client_info_t *info, unsigned char *filter);
snd_seq_client_info_set_event_filter = _alsa_lib.snd_seq_client_info_set_event_filter
snd_seq_client_info_set_event_filter.argtypes = [POINTER(snd_seq_client_info_t), POINTER(c_ubyte)]
snd_seq_client_info_set_event_filter.restype = None


#void snd_seq_client_info_event_filter_clear(snd_seq_client_info_t *info);
snd_seq_client_info_event_filter_clear = _alsa_lib.snd_seq_client_info_event_filter_clear
snd_seq_client_info_event_filter_clear.argtypes = [POINTER(snd_seq_client_info_t)]
snd_seq_client_info_event_filter_clear.restype = None

#void snd_seq_client_info_event_filter_add(snd_seq_client_info_t *info, int event_type);
snd_seq_client_info_event_filter_add = _alsa_lib.snd_seq_client_info_event_filter_add
snd_seq_client_info_event_filter_add.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_event_filter_add.restype = None

#void snd_seq_client_info_event_filter_del(snd_seq_client_info_t *info, int event_type);
snd_seq_client_info_event_filter_del = _alsa_lib.snd_seq_client_info_event_filter_del
snd_seq_client_info_event_filter_del.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_event_filter_del.restype = None

#int snd_seq_client_info_event_filter_check(snd_seq_client_info_t *info, int event_type);
snd_seq_client_info_event_filter_check = _alsa_lib.snd_seq_client_info_event_filter_check
snd_seq_client_info_event_filter_check.argtypes = [POINTER(snd_seq_client_info_t), c_int]
snd_seq_client_info_event_filter_check.restype = c_int


#int snd_seq_get_client_info(snd_seq_t *handle, snd_seq_client_info_t *info);
snd_seq_get_client_info = _alsa_lib.snd_seq_get_client_info
snd_seq_get_client_info.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_client_info_t)]
snd_seq_get_client_info.restype = c_int

#int snd_seq_get_any_client_info(snd_seq_t *handle, int client, snd_seq_client_info_t *info);
snd_seq_get_any_client_info = _alsa_lib.snd_seq_get_any_client_info
snd_seq_get_any_client_info.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_client_info_t)]
snd_seq_get_any_client_info.restype = c_int

#int snd_seq_set_client_info(snd_seq_t *handle, snd_seq_client_info_t *info);
snd_seq_set_client_info = _alsa_lib.snd_seq_set_client_info
snd_seq_set_client_info.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_client_info_t)]
snd_seq_set_client_info.restype = c_int

#int snd_seq_query_next_client(snd_seq_t *handle, snd_seq_client_info_t *info);
snd_seq_query_next_client = _alsa_lib.snd_seq_query_next_client
snd_seq_query_next_client.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_client_info_t)]
snd_seq_query_next_client.restype = c_int


#
#

# client pool information container 
class _snd_seq_client_pool(Structure):
    _fields_ = [
            ]
snd_seq_client_pool_t = _snd_seq_client_pool

#size_t snd_seq_client_pool_sizeof(void);
snd_seq_client_pool_sizeof = _alsa_lib.snd_seq_client_pool_sizeof
snd_seq_client_pool_sizeof.argtypes = []
snd_seq_client_pool_sizeof.restype = c_size_t

# allocate a #snd_seq_client_pool_t container on stack 
#define snd_seq_client_pool_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_client_pool)
#int snd_seq_client_pool_malloc(snd_seq_client_pool_t **ptr);
snd_seq_client_pool_malloc = _alsa_lib.snd_seq_client_pool_malloc
snd_seq_client_pool_malloc.argtypes = [POINTER(POINTER(snd_seq_client_pool_t))]
snd_seq_client_pool_malloc.restype = c_int

#void snd_seq_client_pool_free(snd_seq_client_pool_t *ptr);
snd_seq_client_pool_free = _alsa_lib.snd_seq_client_pool_free
snd_seq_client_pool_free.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_free.restype = None

#void snd_seq_client_pool_copy(snd_seq_client_pool_t *dst, const snd_seq_client_pool_t *src);
snd_seq_client_pool_copy = _alsa_lib.snd_seq_client_pool_copy
snd_seq_client_pool_copy.argtypes = [POINTER(snd_seq_client_pool_t), POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_copy.restype = None


#int snd_seq_client_pool_get_client(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_client = _alsa_lib.snd_seq_client_pool_get_client
snd_seq_client_pool_get_client.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_client.restype = c_int

#size_t snd_seq_client_pool_get_output_pool(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_output_pool = _alsa_lib.snd_seq_client_pool_get_output_pool
snd_seq_client_pool_get_output_pool.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_output_pool.restype = c_size_t

#size_t snd_seq_client_pool_get_input_pool(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_input_pool = _alsa_lib.snd_seq_client_pool_get_input_pool
snd_seq_client_pool_get_input_pool.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_input_pool.restype = c_size_t

#size_t snd_seq_client_pool_get_output_room(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_output_room = _alsa_lib.snd_seq_client_pool_get_output_room
snd_seq_client_pool_get_output_room.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_output_room.restype = c_size_t

#size_t snd_seq_client_pool_get_output_free(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_output_free = _alsa_lib.snd_seq_client_pool_get_output_free
snd_seq_client_pool_get_output_free.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_output_free.restype = c_size_t

#size_t snd_seq_client_pool_get_input_free(const snd_seq_client_pool_t *info);
snd_seq_client_pool_get_input_free = _alsa_lib.snd_seq_client_pool_get_input_free
snd_seq_client_pool_get_input_free.argtypes = [POINTER(snd_seq_client_pool_t)]
snd_seq_client_pool_get_input_free.restype = c_size_t

#void snd_seq_client_pool_set_output_pool(snd_seq_client_pool_t *info, size_t size);
snd_seq_client_pool_set_output_pool = _alsa_lib.snd_seq_client_pool_set_output_pool
snd_seq_client_pool_set_output_pool.argtypes = [POINTER(snd_seq_client_pool_t), c_size_t]
snd_seq_client_pool_set_output_pool.restype = None

#void snd_seq_client_pool_set_input_pool(snd_seq_client_pool_t *info, size_t size);
snd_seq_client_pool_set_input_pool = _alsa_lib.snd_seq_client_pool_set_input_pool
snd_seq_client_pool_set_input_pool.argtypes = [POINTER(snd_seq_client_pool_t), c_size_t]
snd_seq_client_pool_set_input_pool.restype = None

#void snd_seq_client_pool_set_output_room(snd_seq_client_pool_t *info, size_t size);
snd_seq_client_pool_set_output_room = _alsa_lib.snd_seq_client_pool_set_output_room
snd_seq_client_pool_set_output_room.argtypes = [POINTER(snd_seq_client_pool_t), c_size_t]
snd_seq_client_pool_set_output_room.restype = None


#int snd_seq_get_client_pool(snd_seq_t *handle, snd_seq_client_pool_t *info);
snd_seq_get_client_pool = _alsa_lib.snd_seq_get_client_pool
snd_seq_get_client_pool.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_client_pool_t)]
snd_seq_get_client_pool.restype = c_int

#int snd_seq_set_client_pool(snd_seq_t *handle, snd_seq_client_pool_t *info);
snd_seq_set_client_pool = _alsa_lib.snd_seq_set_client_pool
snd_seq_set_client_pool.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_client_pool_t)]
snd_seq_set_client_pool.restype = c_int



# \} 


#
#  \defgroup SeqPort Sequencer Port Interface
#  Sequencer Port Interface
#  \ingroup Sequencer
#  \{
#

# port information container 
class _snd_seq_port_info(Structure):
    _fields_ = [
            ]
snd_seq_port_info_t = _snd_seq_port_info 

# known port numbers 
SND_SEQ_PORT_SYSTEM_TIMER = 0	 # *< system timer port 
SND_SEQ_PORT_SYSTEM_ANNOUNCE = 1 # *< system announce port 

# port capabilities (32 bits) 
SND_SEQ_PORT_CAP_READ	=	(1<<0)	# *< readable from this port 
SND_SEQ_PORT_CAP_WRITE	=	(1<<1)	# *< writable to this port 

SND_SEQ_PORT_CAP_SYNC_READ	= (1<<2)	# *< allow read subscriptions 
SND_SEQ_PORT_CAP_SYNC_WRITE	= (1<<3)	# *< allow write subscriptions 

SND_SEQ_PORT_CAP_DUPLEX = (1<<4) # *< allow read/write duplex 

SND_SEQ_PORT_CAP_SUBS_READ	= (1<<5)	# *< allow read subscription 
SND_SEQ_PORT_CAP_SUBS_WRITE	= (1<<6)	# *< allow write subscription 
SND_SEQ_PORT_CAP_NO_EXPORT	= (1<<7)	# *< routing not allowed 

# port type 
# Messages sent from/to this port have device-specific semantics. 
SND_SEQ_PORT_TYPE_SPECIFIC = (1<<0)
# This port understands MIDI messages. 
SND_SEQ_PORT_TYPE_MIDI_GENERIC = (1<<1)
# This port is compatible with the General MIDI specification. 
SND_SEQ_PORT_TYPE_MIDI_GM = (1<<2)
# This port is compatible with the Roland GS standard. 
SND_SEQ_PORT_TYPE_MIDI_GS = (1<<3)
# This port is compatible with the Yamaha XG specification. 
SND_SEQ_PORT_TYPE_MIDI_XG = (1<<4)
# This port is compatible with the Roland MT-32. 
SND_SEQ_PORT_TYPE_MIDI_MT32 = (1<<5)
# This port is compatible with the General MIDI 2 specification. 
SND_SEQ_PORT_TYPE_MIDI_GM2 = (1<<6)
# This port understands SND_SEQ_EVENT_SAMPLE_xxx messages
#(these are not MIDI messages). 
SND_SEQ_PORT_TYPE_SYNTH = (1<<10)
# Instruments can be downloaded to this port
#(with SND_SEQ_EVENT_INSTR_xxx messages sent directly). 
SND_SEQ_PORT_TYPE_DIRECT_SAMPLE = (1<<11)
# Instruments can be downloaded to this port
#(with SND_SEQ_EVENT_INSTR_xxx messages sent directly or through a queue). 
SND_SEQ_PORT_TYPE_SAMPLE = (1<<12)
# This port is implemented in hardware. 
SND_SEQ_PORT_TYPE_HARDWARE = (1<<16)
# This port is implemented in software. 
SND_SEQ_PORT_TYPE_SOFTWARE = (1<<17)
# Messages sent to this port will generate sounds. 
SND_SEQ_PORT_TYPE_SYNTHESIZER = (1<<18)
# This port may connect to other devices
#(whose characteristics are not known). 
SND_SEQ_PORT_TYPE_PORT = (1<<19)
# This port belongs to an application, such as a sequencer or editor. 
SND_SEQ_PORT_TYPE_APPLICATION = (1<<20)


#size_t snd_seq_port_info_sizeof(void);
snd_seq_port_info_sizeof = _alsa_lib.snd_seq_port_info_sizeof
snd_seq_port_info_sizeof.argtypes = []
snd_seq_port_info_sizeof.restype = c_size_t

# allocate a #snd_seq_port_info_t container on stack 
#define snd_seq_port_info_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_port_info)
#int snd_seq_port_info_malloc(snd_seq_port_info_t **ptr);
snd_seq_port_info_malloc = _alsa_lib.snd_seq_port_info_malloc
snd_seq_port_info_malloc.argtypes = [POINTER(POINTER(snd_seq_port_info_t))]
snd_seq_port_info_malloc.restype = c_int

#void snd_seq_port_info_free(snd_seq_port_info_t *ptr);
snd_seq_port_info_free = _alsa_lib.snd_seq_port_info_free
snd_seq_port_info_free.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_free.restype = None

#void snd_seq_port_info_copy(snd_seq_port_info_t *dst, const snd_seq_port_info_t *src);
snd_seq_port_info_copy = _alsa_lib.snd_seq_port_info_copy
snd_seq_port_info_copy.argtypes = [POINTER(snd_seq_port_info_t), POINTER(snd_seq_port_info_t)]
snd_seq_port_info_copy.restype = None


#int snd_seq_port_info_get_client(const snd_seq_port_info_t *info);
snd_seq_port_info_get_client = _alsa_lib.snd_seq_port_info_get_client
snd_seq_port_info_get_client.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_client.restype = c_int

#int snd_seq_port_info_get_port(const snd_seq_port_info_t *info);
snd_seq_port_info_get_port = _alsa_lib.snd_seq_port_info_get_port
snd_seq_port_info_get_port.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_port.restype = c_int

#const snd_seq_addr_t *snd_seq_port_info_get_addr(const snd_seq_port_info_t *info);
snd_seq_port_info_get_addr = _alsa_lib.snd_seq_port_info_get_addr
snd_seq_port_info_get_addr.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_addr.restype = POINTER(snd_seq_addr_t)

#const char *snd_seq_port_info_get_name(const snd_seq_port_info_t *info);
snd_seq_port_info_get_name = _alsa_lib.snd_seq_port_info_get_name
snd_seq_port_info_get_name.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_name.restype = c_char_p

#unsigned int snd_seq_port_info_get_capability(const snd_seq_port_info_t *info);
snd_seq_port_info_get_capability = _alsa_lib.snd_seq_port_info_get_capability
snd_seq_port_info_get_capability.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_capability.restype = c_uint

#unsigned int snd_seq_port_info_get_type(const snd_seq_port_info_t *info);
snd_seq_port_info_get_type = _alsa_lib.snd_seq_port_info_get_type
snd_seq_port_info_get_type.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_type.restype = c_uint

#int snd_seq_port_info_get_midi_channels(const snd_seq_port_info_t *info);
snd_seq_port_info_get_midi_channels = _alsa_lib.snd_seq_port_info_get_midi_channels
snd_seq_port_info_get_midi_channels.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_midi_channels.restype = c_int

#int snd_seq_port_info_get_midi_voices(const snd_seq_port_info_t *info);
snd_seq_port_info_get_midi_voices = _alsa_lib.snd_seq_port_info_get_midi_voices
snd_seq_port_info_get_midi_voices.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_midi_voices.restype = c_int

#int snd_seq_port_info_get_synth_voices(const snd_seq_port_info_t *info);
snd_seq_port_info_get_synth_voices = _alsa_lib.snd_seq_port_info_get_synth_voices
snd_seq_port_info_get_synth_voices.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_synth_voices.restype = c_int

#int snd_seq_port_info_get_read_use(const snd_seq_port_info_t *info);
snd_seq_port_info_get_read_use = _alsa_lib.snd_seq_port_info_get_read_use
snd_seq_port_info_get_read_use.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_read_use.restype = c_int

#int snd_seq_port_info_get_write_use(const snd_seq_port_info_t *info);
snd_seq_port_info_get_write_use = _alsa_lib.snd_seq_port_info_get_write_use
snd_seq_port_info_get_write_use.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_write_use.restype = c_int

#int snd_seq_port_info_get_port_specified(const snd_seq_port_info_t *info);
snd_seq_port_info_get_port_specified = _alsa_lib.snd_seq_port_info_get_port_specified
snd_seq_port_info_get_port_specified.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_port_specified.restype = c_int

#int snd_seq_port_info_get_timestamping(const snd_seq_port_info_t *info);
snd_seq_port_info_get_timestamping = _alsa_lib.snd_seq_port_info_get_timestamping
snd_seq_port_info_get_timestamping.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_timestamping.restype = c_int

#int snd_seq_port_info_get_timestamp_real(const snd_seq_port_info_t *info);
snd_seq_port_info_get_timestamp_real = _alsa_lib.snd_seq_port_info_get_timestamp_real
snd_seq_port_info_get_timestamp_real.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_timestamp_real.restype = c_int

#int snd_seq_port_info_get_timestamp_queue(const snd_seq_port_info_t *info);
snd_seq_port_info_get_timestamp_queue = _alsa_lib.snd_seq_port_info_get_timestamp_queue
snd_seq_port_info_get_timestamp_queue.argtypes = [POINTER(snd_seq_port_info_t)]
snd_seq_port_info_get_timestamp_queue.restype = c_int


#void snd_seq_port_info_set_client(snd_seq_port_info_t *info, int client);
snd_seq_port_info_set_client = _alsa_lib.snd_seq_port_info_set_client
snd_seq_port_info_set_client.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_client.restype = None

#void snd_seq_port_info_set_port(snd_seq_port_info_t *info, int port);
snd_seq_port_info_set_port = _alsa_lib.snd_seq_port_info_set_port
snd_seq_port_info_set_port.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_port.restype = None

#void snd_seq_port_info_set_addr(snd_seq_port_info_t *info, const snd_seq_addr_t *addr);
snd_seq_port_info_set_addr = _alsa_lib.snd_seq_port_info_set_addr
snd_seq_port_info_set_addr.argtypes = [POINTER(snd_seq_port_info_t), POINTER(snd_seq_addr_t)]
snd_seq_port_info_set_addr.restype = None

#void snd_seq_port_info_set_name(snd_seq_port_info_t *info, const char *name);
snd_seq_port_info_set_name = _alsa_lib.snd_seq_port_info_set_name
snd_seq_port_info_set_name.argtypes = [POINTER(snd_seq_port_info_t), c_char_p]
snd_seq_port_info_set_name.restype = None

#void snd_seq_port_info_set_capability(snd_seq_port_info_t *info, unsigned int capability);
snd_seq_port_info_set_capability = _alsa_lib.snd_seq_port_info_set_capability
snd_seq_port_info_set_capability.argtypes = [POINTER(snd_seq_port_info_t), c_uint]
snd_seq_port_info_set_capability.restype = None

#void snd_seq_port_info_set_type(snd_seq_port_info_t *info, unsigned int type);
snd_seq_port_info_set_type = _alsa_lib.snd_seq_port_info_set_type
snd_seq_port_info_set_type.argtypes = [POINTER(snd_seq_port_info_t), c_uint]
snd_seq_port_info_set_type.restype = None

#void snd_seq_port_info_set_midi_channels(snd_seq_port_info_t *info, int channels);
snd_seq_port_info_set_midi_channels = _alsa_lib.snd_seq_port_info_set_midi_channels
snd_seq_port_info_set_midi_channels.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_midi_channels.restype = None

#void snd_seq_port_info_set_midi_voices(snd_seq_port_info_t *info, int voices);
snd_seq_port_info_set_midi_voices = _alsa_lib.snd_seq_port_info_set_midi_voices
snd_seq_port_info_set_midi_voices.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_midi_voices.restype = None

#void snd_seq_port_info_set_synth_voices(snd_seq_port_info_t *info, int voices);
snd_seq_port_info_set_synth_voices = _alsa_lib.snd_seq_port_info_set_synth_voices
snd_seq_port_info_set_synth_voices.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_synth_voices.restype = None

#void snd_seq_port_info_set_port_specified(snd_seq_port_info_t *info, int val);
snd_seq_port_info_set_port_specified = _alsa_lib.snd_seq_port_info_set_port_specified
snd_seq_port_info_set_port_specified.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_port_specified.restype = None

#void snd_seq_port_info_set_timestamping(snd_seq_port_info_t *info, int enable);
snd_seq_port_info_set_timestamping = _alsa_lib.snd_seq_port_info_set_timestamping
snd_seq_port_info_set_timestamping.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_timestamping.restype = None

#void snd_seq_port_info_set_timestamp_real(snd_seq_port_info_t *info, int realtime);
snd_seq_port_info_set_timestamp_real = _alsa_lib.snd_seq_port_info_set_timestamp_real
snd_seq_port_info_set_timestamp_real.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_timestamp_real.restype = None

#void snd_seq_port_info_set_timestamp_queue(snd_seq_port_info_t *info, int queue);
snd_seq_port_info_set_timestamp_queue = _alsa_lib.snd_seq_port_info_set_timestamp_queue
snd_seq_port_info_set_timestamp_queue.argtypes = [POINTER(snd_seq_port_info_t), c_int]
snd_seq_port_info_set_timestamp_queue.restype = None


#int snd_seq_create_port(snd_seq_t *handle, snd_seq_port_info_t *info);
snd_seq_create_port = _alsa_lib.snd_seq_create_port
snd_seq_create_port.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_port_info_t)]
snd_seq_create_port.restype = c_int

#int snd_seq_delete_port(snd_seq_t *handle, int port);
snd_seq_delete_port = _alsa_lib.snd_seq_delete_port
snd_seq_delete_port.argtypes = [POINTER(snd_seq_t), c_int]
snd_seq_delete_port.restype = c_int

#int snd_seq_get_port_info(snd_seq_t *handle, int port, snd_seq_port_info_t *info);
snd_seq_get_port_info = _alsa_lib.snd_seq_get_port_info
snd_seq_get_port_info.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_port_info_t)]
snd_seq_get_port_info.restype = c_int

#int snd_seq_get_any_port_info(snd_seq_t *handle, int client, int port, snd_seq_port_info_t *info);
snd_seq_get_any_port_info = _alsa_lib.snd_seq_get_any_port_info
snd_seq_get_any_port_info.argtypes = [POINTER(snd_seq_t), c_int, c_int, POINTER(snd_seq_port_info_t)]
snd_seq_get_any_port_info.restype = c_int

#int snd_seq_set_port_info(snd_seq_t *handle, int port, snd_seq_port_info_t *info);
snd_seq_set_port_info = _alsa_lib.snd_seq_set_port_info
snd_seq_set_port_info.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_port_info_t)]
snd_seq_set_port_info.restype = c_int

#int snd_seq_query_next_port(snd_seq_t *handle, snd_seq_port_info_t *info);
snd_seq_query_next_port = _alsa_lib.snd_seq_query_next_port
snd_seq_query_next_port.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_port_info_t)]
snd_seq_query_next_port.restype = c_int


# \} 


#
#  \defgroup SeqSubscribe Sequencer Port Subscription
#  Sequencer Port Subscription
#  \ingroup Sequencer
#  \{
#

# port subscription container 
class _snd_seq_port_subscribe(Structure):
    _fields_ = [
            ]
snd_seq_port_subscribe_t = _snd_seq_port_subscribe

#size_t snd_seq_port_subscribe_sizeof(void);
snd_seq_port_subscribe_sizeof = _alsa_lib.snd_seq_port_subscribe_sizeof
snd_seq_port_subscribe_sizeof.argtypes = []
snd_seq_port_subscribe_sizeof.restype = c_size_t

# allocate a #snd_seq_port_subscribe_t container on stack 
#define snd_seq_port_subscribe_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_port_subscribe)
#int snd_seq_port_subscribe_malloc(snd_seq_port_subscribe_t **ptr);
snd_seq_port_subscribe_malloc = _alsa_lib.snd_seq_port_subscribe_malloc
snd_seq_port_subscribe_malloc.argtypes = [POINTER(POINTER(snd_seq_port_subscribe_t))]
snd_seq_port_subscribe_malloc.restype = c_int

#void snd_seq_port_subscribe_free(snd_seq_port_subscribe_t *ptr);
snd_seq_port_subscribe_free = _alsa_lib.snd_seq_port_subscribe_free
snd_seq_port_subscribe_free.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_free.restype = None

#void snd_seq_port_subscribe_copy(snd_seq_port_subscribe_t *dst, const snd_seq_port_subscribe_t *src);
snd_seq_port_subscribe_copy = _alsa_lib.snd_seq_port_subscribe_copy
snd_seq_port_subscribe_copy.argtypes = [POINTER(snd_seq_port_subscribe_t), POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_copy.restype = None


#const snd_seq_addr_t *snd_seq_port_subscribe_get_sender(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_sender = _alsa_lib.snd_seq_port_subscribe_get_sender
snd_seq_port_subscribe_get_sender.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_sender.restype = POINTER(snd_seq_addr_t)

#const snd_seq_addr_t *snd_seq_port_subscribe_get_dest(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_dest = _alsa_lib.snd_seq_port_subscribe_get_dest
snd_seq_port_subscribe_get_dest.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_dest.restype = POINTER(snd_seq_addr_t)

#int snd_seq_port_subscribe_get_queue(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_queue = _alsa_lib.snd_seq_port_subscribe_get_queue
snd_seq_port_subscribe_get_queue.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_queue.restype = c_int

#int snd_seq_port_subscribe_get_exclusive(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_exclusive = _alsa_lib.snd_seq_port_subscribe_get_exclusive
snd_seq_port_subscribe_get_exclusive.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_exclusive.restype = c_int

#int snd_seq_port_subscribe_get_time_update(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_time_update = _alsa_lib.snd_seq_port_subscribe_get_time_update
snd_seq_port_subscribe_get_time_update.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_time_update.restype = c_int

#int snd_seq_port_subscribe_get_time_real(const snd_seq_port_subscribe_t *info);
snd_seq_port_subscribe_get_time_real = _alsa_lib.snd_seq_port_subscribe_get_time_real
snd_seq_port_subscribe_get_time_real.argtypes = [POINTER(snd_seq_port_subscribe_t)]
snd_seq_port_subscribe_get_time_real.restype = c_int


#void snd_seq_port_subscribe_set_sender(snd_seq_port_subscribe_t *info, const snd_seq_addr_t *addr);
snd_seq_port_subscribe_set_sender = _alsa_lib.snd_seq_port_subscribe_set_sender
snd_seq_port_subscribe_set_sender.argtypes = [POINTER(snd_seq_port_subscribe_t), POINTER(snd_seq_addr_t)]
snd_seq_port_subscribe_set_sender.restype = None

#void snd_seq_port_subscribe_set_dest(snd_seq_port_subscribe_t *info, const snd_seq_addr_t *addr);
snd_seq_port_subscribe_set_dest = _alsa_lib.snd_seq_port_subscribe_set_dest
snd_seq_port_subscribe_set_dest.argtypes = [POINTER(snd_seq_port_subscribe_t), POINTER(snd_seq_addr_t)]
snd_seq_port_subscribe_set_dest.restype = None

#void snd_seq_port_subscribe_set_queue(snd_seq_port_subscribe_t *info, int q);
snd_seq_port_subscribe_set_queue = _alsa_lib.snd_seq_port_subscribe_set_queue
snd_seq_port_subscribe_set_queue.argtypes = [POINTER(snd_seq_port_subscribe_t), c_int]
snd_seq_port_subscribe_set_queue.restype = None

#void snd_seq_port_subscribe_set_exclusive(snd_seq_port_subscribe_t *info, int val);
snd_seq_port_subscribe_set_exclusive = _alsa_lib.snd_seq_port_subscribe_set_exclusive
snd_seq_port_subscribe_set_exclusive.argtypes = [POINTER(snd_seq_port_subscribe_t), c_int]
snd_seq_port_subscribe_set_exclusive.restype = None

#void snd_seq_port_subscribe_set_time_update(snd_seq_port_subscribe_t *info, int val);
snd_seq_port_subscribe_set_time_update = _alsa_lib.snd_seq_port_subscribe_set_time_update
snd_seq_port_subscribe_set_time_update.argtypes = [POINTER(snd_seq_port_subscribe_t), c_int]
snd_seq_port_subscribe_set_time_update.restype = None

#void snd_seq_port_subscribe_set_time_real(snd_seq_port_subscribe_t *info, int val);
snd_seq_port_subscribe_set_time_real = _alsa_lib.snd_seq_port_subscribe_set_time_real
snd_seq_port_subscribe_set_time_real.argtypes = [POINTER(snd_seq_port_subscribe_t), c_int]
snd_seq_port_subscribe_set_time_real.restype = None


#int snd_seq_get_port_subscription(snd_seq_t *handle, snd_seq_port_subscribe_t *sub);
snd_seq_get_port_subscription = _alsa_lib.snd_seq_get_port_subscription
snd_seq_get_port_subscription.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_port_subscribe_t)]
snd_seq_get_port_subscription.restype = c_int

#int snd_seq_subscribe_port(snd_seq_t *handle, snd_seq_port_subscribe_t *sub);
snd_seq_subscribe_port = _alsa_lib.snd_seq_subscribe_port
snd_seq_subscribe_port.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_port_subscribe_t)]
snd_seq_subscribe_port.restype = c_int

#int snd_seq_unsubscribe_port(snd_seq_t *handle, snd_seq_port_subscribe_t *sub);
snd_seq_unsubscribe_port = _alsa_lib.snd_seq_unsubscribe_port
snd_seq_unsubscribe_port.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_port_subscribe_t)]
snd_seq_unsubscribe_port.restype = c_int


#
#

# subscription query container 
class _snd_seq_query_subscribe(Structure):
    _fields_ = [
            ]
snd_seq_query_subscribe_t = _snd_seq_query_subscribe

# type of query subscription 
SND_SEQ_QUERY_SUBS_READ = 0 # *< query read subscriptions 
SND_SEQ_QUERY_SUBS_WRITE = 1 # *< query write subscriptions 
snd_seq_query_subs_type_t = c_int

#size_t snd_seq_query_subscribe_sizeof(void);
snd_seq_query_subscribe_sizeof = _alsa_lib.snd_seq_query_subscribe_sizeof
snd_seq_query_subscribe_sizeof.argtypes = []
snd_seq_query_subscribe_sizeof.restype = c_size_t

# allocate a #snd_seq_query_subscribe_t container on stack 
#define snd_seq_query_subscribe_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_query_subscribe)
#int snd_seq_query_subscribe_malloc(snd_seq_query_subscribe_t **ptr);
snd_seq_query_subscribe_malloc = _alsa_lib.snd_seq_query_subscribe_malloc
snd_seq_query_subscribe_malloc.argtypes = [POINTER(POINTER(snd_seq_query_subscribe_t))]
snd_seq_query_subscribe_malloc.restype = c_int

#void snd_seq_query_subscribe_free(snd_seq_query_subscribe_t *ptr);
snd_seq_query_subscribe_free = _alsa_lib.snd_seq_query_subscribe_free
snd_seq_query_subscribe_free.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_free.restype = None

#void snd_seq_query_subscribe_copy(snd_seq_query_subscribe_t *dst, const snd_seq_query_subscribe_t *src);
snd_seq_query_subscribe_copy = _alsa_lib.snd_seq_query_subscribe_copy
snd_seq_query_subscribe_copy.argtypes = [POINTER(snd_seq_query_subscribe_t), POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_copy.restype = None


#int snd_seq_query_subscribe_get_client(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_client = _alsa_lib.snd_seq_query_subscribe_get_client
snd_seq_query_subscribe_get_client.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_client.restype = c_int

#int snd_seq_query_subscribe_get_port(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_port = _alsa_lib.snd_seq_query_subscribe_get_port
snd_seq_query_subscribe_get_port.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_port.restype = c_int

#const snd_seq_addr_t *snd_seq_query_subscribe_get_root(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_root = _alsa_lib.snd_seq_query_subscribe_get_root
snd_seq_query_subscribe_get_root.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_root.restype = POINTER(snd_seq_addr_t)

#snd_seq_query_subs_type_t snd_seq_query_subscribe_get_type(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_type = _alsa_lib.snd_seq_query_subscribe_get_type
snd_seq_query_subscribe_get_type.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_type.restype = snd_seq_query_subs_type_t

#int snd_seq_query_subscribe_get_index(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_index = _alsa_lib.snd_seq_query_subscribe_get_index
snd_seq_query_subscribe_get_index.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_index.restype = c_int

#int snd_seq_query_subscribe_get_num_subs(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_num_subs = _alsa_lib.snd_seq_query_subscribe_get_num_subs
snd_seq_query_subscribe_get_num_subs.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_num_subs.restype = c_int

#const snd_seq_addr_t *snd_seq_query_subscribe_get_addr(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_addr = _alsa_lib.snd_seq_query_subscribe_get_addr
snd_seq_query_subscribe_get_addr.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_addr.restype = POINTER(snd_seq_addr_t)

#int snd_seq_query_subscribe_get_queue(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_queue = _alsa_lib.snd_seq_query_subscribe_get_queue
snd_seq_query_subscribe_get_queue.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_queue.restype = c_int

#int snd_seq_query_subscribe_get_exclusive(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_exclusive = _alsa_lib.snd_seq_query_subscribe_get_exclusive
snd_seq_query_subscribe_get_exclusive.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_exclusive.restype = c_int

#int snd_seq_query_subscribe_get_time_update(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_time_update = _alsa_lib.snd_seq_query_subscribe_get_time_update
snd_seq_query_subscribe_get_time_update.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_time_update.restype = c_int

#int snd_seq_query_subscribe_get_time_real(const snd_seq_query_subscribe_t *info);
snd_seq_query_subscribe_get_time_real = _alsa_lib.snd_seq_query_subscribe_get_time_real
snd_seq_query_subscribe_get_time_real.argtypes = [POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_subscribe_get_time_real.restype = c_int


#void snd_seq_query_subscribe_set_client(snd_seq_query_subscribe_t *info, int client);
snd_seq_query_subscribe_set_client = _alsa_lib.snd_seq_query_subscribe_set_client
snd_seq_query_subscribe_set_client.argtypes = [POINTER(snd_seq_query_subscribe_t), c_int]
snd_seq_query_subscribe_set_client.restype = None

#void snd_seq_query_subscribe_set_port(snd_seq_query_subscribe_t *info, int port);
snd_seq_query_subscribe_set_port = _alsa_lib.snd_seq_query_subscribe_set_port
snd_seq_query_subscribe_set_port.argtypes = [POINTER(snd_seq_query_subscribe_t), c_int]
snd_seq_query_subscribe_set_port.restype = None

#void snd_seq_query_subscribe_set_root(snd_seq_query_subscribe_t *info, const snd_seq_addr_t *addr);
snd_seq_query_subscribe_set_root = _alsa_lib.snd_seq_query_subscribe_set_root
snd_seq_query_subscribe_set_root.argtypes = [POINTER(snd_seq_query_subscribe_t), POINTER(snd_seq_addr_t)]
snd_seq_query_subscribe_set_root.restype = None

#void snd_seq_query_subscribe_set_type(snd_seq_query_subscribe_t *info, snd_seq_query_subs_type_t type);
snd_seq_query_subscribe_set_type = _alsa_lib.snd_seq_query_subscribe_set_type
snd_seq_query_subscribe_set_type.argtypes = [POINTER(snd_seq_query_subscribe_t), snd_seq_query_subs_type_t]
snd_seq_query_subscribe_set_type.restype = None

#void snd_seq_query_subscribe_set_index(snd_seq_query_subscribe_t *info, int _index);
snd_seq_query_subscribe_set_index = _alsa_lib.snd_seq_query_subscribe_set_index
snd_seq_query_subscribe_set_index.argtypes = [POINTER(snd_seq_query_subscribe_t), c_int]
snd_seq_query_subscribe_set_index.restype = None


#int snd_seq_query_port_subscribers(snd_seq_t *seq, snd_seq_query_subscribe_t * subs);
snd_seq_query_port_subscribers = _alsa_lib.snd_seq_query_port_subscribers
snd_seq_query_port_subscribers.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_query_subscribe_t)]
snd_seq_query_port_subscribers.restype = c_int


# \} 


#
#  \defgroup SeqQueue Sequencer Queue Interface
#  Sequencer Queue Interface
#  \ingroup Sequencer
#  \{
#

# queue information container 
class _snd_seq_queue_info(Structure):
    _fields_ = [
            ]
snd_seq_queue_info_t = _snd_seq_queue_info
# queue status container 
class _snd_seq_queue_status(Structure):
    _fields_ = [
            ]
snd_seq_queue_status_t = _snd_seq_queue_status 
# queue tempo container 
class _snd_seq_queue_tempo(Structure):
    _fields_ = [
            ]
snd_seq_queue_tempo_t = _snd_seq_queue_tempo 
# queue timer information container 
class _snd_seq_queue_timer(Structure):
    _fields_ = [
            ]
snd_seq_queue_timer_t = _snd_seq_queue_timer 

# special queue ids 
SND_SEQ_QUEUE_DIRECT = 253 # *< direct dispatch 

#size_t snd_seq_queue_info_sizeof(void);
snd_seq_queue_info_sizeof = _alsa_lib.snd_seq_queue_info_sizeof
snd_seq_queue_info_sizeof.argtypes = []
snd_seq_queue_info_sizeof.restype = c_size_t

# allocate a #snd_seq_queue_info_t container on stack 
#define snd_seq_queue_info_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_queue_info)
#int snd_seq_queue_info_malloc(snd_seq_queue_info_t **ptr);
snd_seq_queue_info_malloc = _alsa_lib.snd_seq_queue_info_malloc
snd_seq_queue_info_malloc.argtypes = [POINTER(POINTER(snd_seq_queue_info_t))]
snd_seq_queue_info_malloc.restype = c_int

#void snd_seq_queue_info_free(snd_seq_queue_info_t *ptr);
snd_seq_queue_info_free = _alsa_lib.snd_seq_queue_info_free
snd_seq_queue_info_free.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_free.restype = None

#void snd_seq_queue_info_copy(snd_seq_queue_info_t *dst, const snd_seq_queue_info_t *src);
snd_seq_queue_info_copy = _alsa_lib.snd_seq_queue_info_copy
snd_seq_queue_info_copy.argtypes = [POINTER(snd_seq_queue_info_t), POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_copy.restype = None


#int snd_seq_queue_info_get_queue(const snd_seq_queue_info_t *info);
snd_seq_queue_info_get_queue = _alsa_lib.snd_seq_queue_info_get_queue
snd_seq_queue_info_get_queue.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_get_queue.restype = c_int

#const char *snd_seq_queue_info_get_name(const snd_seq_queue_info_t *info);
snd_seq_queue_info_get_name = _alsa_lib.snd_seq_queue_info_get_name
snd_seq_queue_info_get_name.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_get_name.restype = c_char_p

#int snd_seq_queue_info_get_owner(const snd_seq_queue_info_t *info);
snd_seq_queue_info_get_owner = _alsa_lib.snd_seq_queue_info_get_owner
snd_seq_queue_info_get_owner.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_get_owner.restype = c_int

#int snd_seq_queue_info_get_locked(const snd_seq_queue_info_t *info);
snd_seq_queue_info_get_locked = _alsa_lib.snd_seq_queue_info_get_locked
snd_seq_queue_info_get_locked.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_get_locked.restype = c_int

#unsigned int snd_seq_queue_info_get_flags(const snd_seq_queue_info_t *info);
snd_seq_queue_info_get_flags = _alsa_lib.snd_seq_queue_info_get_flags
snd_seq_queue_info_get_flags.argtypes = [POINTER(snd_seq_queue_info_t)]
snd_seq_queue_info_get_flags.restype = c_uint


#void snd_seq_queue_info_set_name(snd_seq_queue_info_t *info, const char *name);
snd_seq_queue_info_set_name = _alsa_lib.snd_seq_queue_info_set_name
snd_seq_queue_info_set_name.argtypes = [POINTER(snd_seq_queue_info_t), c_char_p]
snd_seq_queue_info_set_name.restype = None

#void snd_seq_queue_info_set_owner(snd_seq_queue_info_t *info, int owner);
snd_seq_queue_info_set_owner = _alsa_lib.snd_seq_queue_info_set_owner
snd_seq_queue_info_set_owner.argtypes = [POINTER(snd_seq_queue_info_t), c_int]
snd_seq_queue_info_set_owner.restype = None

#void snd_seq_queue_info_set_locked(snd_seq_queue_info_t *info, int locked);
snd_seq_queue_info_set_locked = _alsa_lib.snd_seq_queue_info_set_locked
snd_seq_queue_info_set_locked.argtypes = [POINTER(snd_seq_queue_info_t), c_int]
snd_seq_queue_info_set_locked.restype = None

#void snd_seq_queue_info_set_flags(snd_seq_queue_info_t *info, unsigned int flags);
snd_seq_queue_info_set_flags = _alsa_lib.snd_seq_queue_info_set_flags
snd_seq_queue_info_set_flags.argtypes = [POINTER(snd_seq_queue_info_t), c_uint]
snd_seq_queue_info_set_flags.restype = None


#int snd_seq_create_queue(snd_seq_t *seq, snd_seq_queue_info_t *info);
snd_seq_create_queue = _alsa_lib.snd_seq_create_queue
snd_seq_create_queue.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_queue_info_t)]
snd_seq_create_queue.restype = c_int

#int snd_seq_alloc_named_queue(snd_seq_t *seq, const char *name);
snd_seq_alloc_named_queue = _alsa_lib.snd_seq_alloc_named_queue
snd_seq_alloc_named_queue.argtypes = [POINTER(snd_seq_t), c_char_p]
snd_seq_alloc_named_queue.restype = c_int

#int snd_seq_alloc_queue(snd_seq_t *handle);
snd_seq_alloc_queue = _alsa_lib.snd_seq_alloc_queue
snd_seq_alloc_queue.argtypes = [POINTER(snd_seq_t)]
snd_seq_alloc_queue.restype = c_int

#int snd_seq_free_queue(snd_seq_t *handle, int q);
snd_seq_free_queue = _alsa_lib.snd_seq_free_queue
snd_seq_free_queue.argtypes = [POINTER(snd_seq_t), c_int]
snd_seq_free_queue.restype = c_int

#int snd_seq_get_queue_info(snd_seq_t *seq, int q, snd_seq_queue_info_t *info);
snd_seq_get_queue_info = _alsa_lib.snd_seq_get_queue_info
snd_seq_get_queue_info.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_info_t)]
snd_seq_get_queue_info.restype = c_int

#int snd_seq_set_queue_info(snd_seq_t *seq, int q, snd_seq_queue_info_t *info);
snd_seq_set_queue_info = _alsa_lib.snd_seq_set_queue_info
snd_seq_set_queue_info.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_info_t)]
snd_seq_set_queue_info.restype = c_int

#int snd_seq_query_named_queue(snd_seq_t *seq, const char *name);
snd_seq_query_named_queue = _alsa_lib.snd_seq_query_named_queue
snd_seq_query_named_queue.argtypes = [POINTER(snd_seq_t), c_char_p]
snd_seq_query_named_queue.restype = c_int


#int snd_seq_get_queue_usage(snd_seq_t *handle, int q);
snd_seq_get_queue_usage = _alsa_lib.snd_seq_get_queue_usage
snd_seq_get_queue_usage.argtypes = [POINTER(snd_seq_t), c_int]
snd_seq_get_queue_usage.restype = c_int

#int snd_seq_set_queue_usage(snd_seq_t *handle, int q, int used);
snd_seq_set_queue_usage = _alsa_lib.snd_seq_set_queue_usage
snd_seq_set_queue_usage.argtypes = [POINTER(snd_seq_t), c_int, c_int]
snd_seq_set_queue_usage.restype = c_int


#
#
#size_t snd_seq_queue_status_sizeof(void);
snd_seq_queue_status_sizeof = _alsa_lib.snd_seq_queue_status_sizeof
snd_seq_queue_status_sizeof.argtypes = []
snd_seq_queue_status_sizeof.restype = c_size_t

# allocate a #snd_seq_queue_status_t container on stack 
#define snd_seq_queue_status_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_queue_status)
#int snd_seq_queue_status_malloc(snd_seq_queue_status_t **ptr);
snd_seq_queue_status_malloc = _alsa_lib.snd_seq_queue_status_malloc
snd_seq_queue_status_malloc.argtypes = [POINTER(POINTER(snd_seq_queue_status_t))]
snd_seq_queue_status_malloc.restype = c_int

#void snd_seq_queue_status_free(snd_seq_queue_status_t *ptr);
snd_seq_queue_status_free = _alsa_lib.snd_seq_queue_status_free
snd_seq_queue_status_free.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_free.restype = None

#void snd_seq_queue_status_copy(snd_seq_queue_status_t *dst, const snd_seq_queue_status_t *src);
snd_seq_queue_status_copy = _alsa_lib.snd_seq_queue_status_copy
snd_seq_queue_status_copy.argtypes = [POINTER(snd_seq_queue_status_t), POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_copy.restype = None


#int snd_seq_queue_status_get_queue(const snd_seq_queue_status_t *info);
snd_seq_queue_status_get_queue = _alsa_lib.snd_seq_queue_status_get_queue
snd_seq_queue_status_get_queue.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_get_queue.restype = c_int

#int snd_seq_queue_status_get_events(const snd_seq_queue_status_t *info);
snd_seq_queue_status_get_events = _alsa_lib.snd_seq_queue_status_get_events
snd_seq_queue_status_get_events.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_get_events.restype = c_int

#snd_seq_tick_time_t snd_seq_queue_status_get_tick_time(const snd_seq_queue_status_t *info);
snd_seq_queue_status_get_tick_time = _alsa_lib.snd_seq_queue_status_get_tick_time
snd_seq_queue_status_get_tick_time.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_get_tick_time.restype = snd_seq_tick_time_t

#const snd_seq_real_time_t *snd_seq_queue_status_get_real_time(const snd_seq_queue_status_t *info);
snd_seq_queue_status_get_real_time = _alsa_lib.snd_seq_queue_status_get_real_time
snd_seq_queue_status_get_real_time.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_get_real_time.restype = POINTER(snd_seq_real_time_t)

#unsigned int snd_seq_queue_status_get_status(const snd_seq_queue_status_t *info);
snd_seq_queue_status_get_status = _alsa_lib.snd_seq_queue_status_get_status
snd_seq_queue_status_get_status.argtypes = [POINTER(snd_seq_queue_status_t)]
snd_seq_queue_status_get_status.restype = c_uint


#int snd_seq_get_queue_status(snd_seq_t *handle, int q, snd_seq_queue_status_t *status);
snd_seq_get_queue_status = _alsa_lib.snd_seq_get_queue_status
snd_seq_get_queue_status.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_status_t)]
snd_seq_get_queue_status.restype = c_int


#
#
#size_t snd_seq_queue_tempo_sizeof(void);
snd_seq_queue_tempo_sizeof = _alsa_lib.snd_seq_queue_tempo_sizeof
snd_seq_queue_tempo_sizeof.argtypes = []
snd_seq_queue_tempo_sizeof.restype = c_size_t

# allocate a #snd_seq_queue_tempo_t container on stack 
#define snd_seq_queue_tempo_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_queue_tempo)
#int snd_seq_queue_tempo_malloc(snd_seq_queue_tempo_t **ptr);
snd_seq_queue_tempo_malloc = _alsa_lib.snd_seq_queue_tempo_malloc
snd_seq_queue_tempo_malloc.argtypes = [POINTER(POINTER(snd_seq_queue_tempo_t))]
snd_seq_queue_tempo_malloc.restype = c_int

#void snd_seq_queue_tempo_free(snd_seq_queue_tempo_t *ptr);
snd_seq_queue_tempo_free = _alsa_lib.snd_seq_queue_tempo_free
snd_seq_queue_tempo_free.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_free.restype = None

#void snd_seq_queue_tempo_copy(snd_seq_queue_tempo_t *dst, const snd_seq_queue_tempo_t *src);
snd_seq_queue_tempo_copy = _alsa_lib.snd_seq_queue_tempo_copy
snd_seq_queue_tempo_copy.argtypes = [POINTER(snd_seq_queue_tempo_t), POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_copy.restype = None


#int snd_seq_queue_tempo_get_queue(const snd_seq_queue_tempo_t *info);
snd_seq_queue_tempo_get_queue = _alsa_lib.snd_seq_queue_tempo_get_queue
snd_seq_queue_tempo_get_queue.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_get_queue.restype = c_int

#unsigned int snd_seq_queue_tempo_get_tempo(const snd_seq_queue_tempo_t *info);
snd_seq_queue_tempo_get_tempo = _alsa_lib.snd_seq_queue_tempo_get_tempo
snd_seq_queue_tempo_get_tempo.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_get_tempo.restype = c_uint

#int snd_seq_queue_tempo_get_ppq(const snd_seq_queue_tempo_t *info);
snd_seq_queue_tempo_get_ppq = _alsa_lib.snd_seq_queue_tempo_get_ppq
snd_seq_queue_tempo_get_ppq.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_get_ppq.restype = c_int

#unsigned int snd_seq_queue_tempo_get_skew(const snd_seq_queue_tempo_t *info);
snd_seq_queue_tempo_get_skew = _alsa_lib.snd_seq_queue_tempo_get_skew
snd_seq_queue_tempo_get_skew.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_get_skew.restype = c_uint

#unsigned int snd_seq_queue_tempo_get_skew_base(const snd_seq_queue_tempo_t *info);
snd_seq_queue_tempo_get_skew_base = _alsa_lib.snd_seq_queue_tempo_get_skew_base
snd_seq_queue_tempo_get_skew_base.argtypes = [POINTER(snd_seq_queue_tempo_t)]
snd_seq_queue_tempo_get_skew_base.restype = c_uint

#void snd_seq_queue_tempo_set_tempo(snd_seq_queue_tempo_t *info, unsigned int tempo);
snd_seq_queue_tempo_set_tempo = _alsa_lib.snd_seq_queue_tempo_set_tempo
snd_seq_queue_tempo_set_tempo.argtypes = [POINTER(snd_seq_queue_tempo_t), c_uint]
snd_seq_queue_tempo_set_tempo.restype = None

#void snd_seq_queue_tempo_set_ppq(snd_seq_queue_tempo_t *info, int ppq);
snd_seq_queue_tempo_set_ppq = _alsa_lib.snd_seq_queue_tempo_set_ppq
snd_seq_queue_tempo_set_ppq.argtypes = [POINTER(snd_seq_queue_tempo_t), c_int]
snd_seq_queue_tempo_set_ppq.restype = None

#void snd_seq_queue_tempo_set_skew(snd_seq_queue_tempo_t *info, unsigned int skew);
snd_seq_queue_tempo_set_skew = _alsa_lib.snd_seq_queue_tempo_set_skew
snd_seq_queue_tempo_set_skew.argtypes = [POINTER(snd_seq_queue_tempo_t), c_uint]
snd_seq_queue_tempo_set_skew.restype = None

#void snd_seq_queue_tempo_set_skew_base(snd_seq_queue_tempo_t *info, unsigned int base);
snd_seq_queue_tempo_set_skew_base = _alsa_lib.snd_seq_queue_tempo_set_skew_base
snd_seq_queue_tempo_set_skew_base.argtypes = [POINTER(snd_seq_queue_tempo_t), c_uint]
snd_seq_queue_tempo_set_skew_base.restype = None


#int snd_seq_get_queue_tempo(snd_seq_t *handle, int q, snd_seq_queue_tempo_t *tempo);
snd_seq_get_queue_tempo = _alsa_lib.snd_seq_get_queue_tempo
snd_seq_get_queue_tempo.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_tempo_t)]
snd_seq_get_queue_tempo.restype = c_int

#int snd_seq_set_queue_tempo(snd_seq_t *handle, int q, snd_seq_queue_tempo_t *tempo);
snd_seq_set_queue_tempo = _alsa_lib.snd_seq_set_queue_tempo
snd_seq_set_queue_tempo.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_tempo_t)]
snd_seq_set_queue_tempo.restype = c_int


#
#

# sequencer timer sources 
SND_SEQ_TIMER_ALSA = 0		   #  ALSA timer 
SND_SEQ_TIMER_MIDI_CLOCK = 1   #  Midi Clock (CLOCK event) 
SND_SEQ_TIMER_MIDI_TICK = 2	   #  Midi Timer Tick (TICK event 
snd_seq_queue_timer_type_t = c_int

#size_t snd_seq_queue_timer_sizeof(void);
snd_seq_queue_timer_sizeof = _alsa_lib.snd_seq_queue_timer_sizeof
snd_seq_queue_timer_sizeof.argtypes = []
snd_seq_queue_timer_sizeof.restype = c_size_t

# allocate a #snd_seq_queue_timer_t container on stack 
#define snd_seq_queue_timer_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_queue_timer)
#int snd_seq_queue_timer_malloc(snd_seq_queue_timer_t **ptr);
snd_seq_queue_timer_malloc = _alsa_lib.snd_seq_queue_timer_malloc
snd_seq_queue_timer_malloc.argtypes = [POINTER(POINTER(snd_seq_queue_timer_t))]
snd_seq_queue_timer_malloc.restype = c_int

#void snd_seq_queue_timer_free(snd_seq_queue_timer_t *ptr);
snd_seq_queue_timer_free = _alsa_lib.snd_seq_queue_timer_free
snd_seq_queue_timer_free.argtypes = [POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_free.restype = None

#void snd_seq_queue_timer_copy(snd_seq_queue_timer_t *dst, const snd_seq_queue_timer_t *src);
snd_seq_queue_timer_copy = _alsa_lib.snd_seq_queue_timer_copy
snd_seq_queue_timer_copy.argtypes = [POINTER(snd_seq_queue_timer_t), POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_copy.restype = None


#int snd_seq_queue_timer_get_queue(const snd_seq_queue_timer_t *info);
snd_seq_queue_timer_get_queue = _alsa_lib.snd_seq_queue_timer_get_queue
snd_seq_queue_timer_get_queue.argtypes = [POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_get_queue.restype = c_int

#snd_seq_queue_timer_type_t snd_seq_queue_timer_get_type(const snd_seq_queue_timer_t *info);
snd_seq_queue_timer_get_type = _alsa_lib.snd_seq_queue_timer_get_type
snd_seq_queue_timer_get_type.argtypes = [POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_get_type.restype = snd_seq_queue_timer_type_t

#const snd_timer_id_t *snd_seq_queue_timer_get_id(const snd_seq_queue_timer_t *info);
snd_seq_queue_timer_get_id = _alsa_lib.snd_seq_queue_timer_get_id
snd_seq_queue_timer_get_id.argtypes = [POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_get_id.restype = POINTER(snd_timer_id_t)

#unsigned int snd_seq_queue_timer_get_resolution(const snd_seq_queue_timer_t *info);
snd_seq_queue_timer_get_resolution = _alsa_lib.snd_seq_queue_timer_get_resolution
snd_seq_queue_timer_get_resolution.argtypes = [POINTER(snd_seq_queue_timer_t)]
snd_seq_queue_timer_get_resolution.restype = c_uint


#void snd_seq_queue_timer_set_type(snd_seq_queue_timer_t *info, snd_seq_queue_timer_type_t type);
snd_seq_queue_timer_set_type = _alsa_lib.snd_seq_queue_timer_set_type
snd_seq_queue_timer_set_type.argtypes = [POINTER(snd_seq_queue_timer_t), snd_seq_queue_timer_type_t]
snd_seq_queue_timer_set_type.restype = None

#void snd_seq_queue_timer_set_id(snd_seq_queue_timer_t *info, const snd_timer_id_t *id);
snd_seq_queue_timer_set_id = _alsa_lib.snd_seq_queue_timer_set_id
snd_seq_queue_timer_set_id.argtypes = [POINTER(snd_seq_queue_timer_t), POINTER(snd_timer_id_t)]
snd_seq_queue_timer_set_id.restype = None

#void snd_seq_queue_timer_set_resolution(snd_seq_queue_timer_t *info, unsigned int resolution);
snd_seq_queue_timer_set_resolution = _alsa_lib.snd_seq_queue_timer_set_resolution
snd_seq_queue_timer_set_resolution.argtypes = [POINTER(snd_seq_queue_timer_t), c_uint]
snd_seq_queue_timer_set_resolution.restype = None


#int snd_seq_get_queue_timer(snd_seq_t *handle, int q, snd_seq_queue_timer_t *timer);
snd_seq_get_queue_timer = _alsa_lib.snd_seq_get_queue_timer
snd_seq_get_queue_timer.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_timer_t)]
snd_seq_get_queue_timer.restype = c_int

#int snd_seq_set_queue_timer(snd_seq_t *handle, int q, snd_seq_queue_timer_t *timer);
snd_seq_set_queue_timer = _alsa_lib.snd_seq_set_queue_timer
snd_seq_set_queue_timer.argtypes = [POINTER(snd_seq_t), c_int, POINTER(snd_seq_queue_timer_t)]
snd_seq_set_queue_timer.restype = c_int


# \} 

#
#  \defgroup SeqEvent Sequencer Event API
#  Sequencer Event API
#  \ingroup Sequencer
#  \{
#

#int snd_seq_free_event(snd_seq_event_t *ev);
snd_seq_free_event = _alsa_lib.snd_seq_free_event
snd_seq_free_event.argtypes = [POINTER(snd_seq_event_t)]
snd_seq_free_event.restype = c_int

#ssize_t snd_seq_event_length(snd_seq_event_t *ev);
snd_seq_event_length = _alsa_lib.snd_seq_event_length
snd_seq_event_length.argtypes = [POINTER(snd_seq_event_t)]
snd_seq_event_length.restype = c_size_t

#int snd_seq_event_output(snd_seq_t *handle, snd_seq_event_t *ev);
snd_seq_event_output = _alsa_lib.snd_seq_event_output
snd_seq_event_output.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_event_t)]
snd_seq_event_output.restype = c_int

#int snd_seq_event_output_buffer(snd_seq_t *handle, snd_seq_event_t *ev);
snd_seq_event_output_buffer = _alsa_lib.snd_seq_event_output_buffer
snd_seq_event_output_buffer.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_event_t)]
snd_seq_event_output_buffer.restype = c_int

#int snd_seq_event_output_direct(snd_seq_t *handle, snd_seq_event_t *ev);
snd_seq_event_output_direct = _alsa_lib.snd_seq_event_output_direct
snd_seq_event_output_direct.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_event_t)]
snd_seq_event_output_direct.restype = c_int

#int snd_seq_event_input(snd_seq_t *handle, snd_seq_event_t **ev);
snd_seq_event_input = _alsa_lib.snd_seq_event_input
snd_seq_event_input.argtypes = [POINTER(snd_seq_t), POINTER(POINTER(snd_seq_event_t))]
snd_seq_event_input.restype = c_int

#int snd_seq_event_input_pending(snd_seq_t *seq, int fetch_sequencer);
snd_seq_event_input_pending = _alsa_lib.snd_seq_event_input_pending
snd_seq_event_input_pending.argtypes = [POINTER(snd_seq_t), c_int]
snd_seq_event_input_pending.restype = c_int

#int snd_seq_drain_output(snd_seq_t *handle);
snd_seq_drain_output = _alsa_lib.snd_seq_drain_output
snd_seq_drain_output.argtypes = [POINTER(snd_seq_t)]
snd_seq_drain_output.restype = c_int

#int snd_seq_event_output_pending(snd_seq_t *seq);
snd_seq_event_output_pending = _alsa_lib.snd_seq_event_output_pending
snd_seq_event_output_pending.argtypes = [POINTER(snd_seq_t)]
snd_seq_event_output_pending.restype = c_int

#int snd_seq_extract_output(snd_seq_t *handle, snd_seq_event_t **ev);
snd_seq_extract_output = _alsa_lib.snd_seq_extract_output
snd_seq_extract_output.argtypes = [POINTER(snd_seq_t), POINTER(POINTER(snd_seq_event_t))]
snd_seq_extract_output.restype = c_int

#int snd_seq_drop_output(snd_seq_t *handle);
snd_seq_drop_output = _alsa_lib.snd_seq_drop_output
snd_seq_drop_output.argtypes = [POINTER(snd_seq_t)]
snd_seq_drop_output.restype = c_int

#int snd_seq_drop_output_buffer(snd_seq_t *handle);
snd_seq_drop_output_buffer = _alsa_lib.snd_seq_drop_output_buffer
snd_seq_drop_output_buffer.argtypes = [POINTER(snd_seq_t)]
snd_seq_drop_output_buffer.restype = c_int

#int snd_seq_drop_input(snd_seq_t *handle);
snd_seq_drop_input = _alsa_lib.snd_seq_drop_input
snd_seq_drop_input.argtypes = [POINTER(snd_seq_t)]
snd_seq_drop_input.restype = c_int

#int snd_seq_drop_input_buffer(snd_seq_t *handle);
snd_seq_drop_input_buffer = _alsa_lib.snd_seq_drop_input_buffer
snd_seq_drop_input_buffer.argtypes = [POINTER(snd_seq_t)]
snd_seq_drop_input_buffer.restype = c_int


# event removal conditionals 
class _snd_seq_remove_events(Structure):
    _fields_ = [
            ]
snd_seq_remove_events_t = _snd_seq_remove_events 

# Remove conditional flags 
SND_SEQ_REMOVE_INPUT		 = (1<<0)	# *< Flush input queues 
SND_SEQ_REMOVE_OUTPUT		 = (1<<1)	# *< Flush output queues 
SND_SEQ_REMOVE_DEST		 = (1<<2)	# *< Restrict by destination q:client:port 
SND_SEQ_REMOVE_DEST_CHANNEL	 = (1<<3)	# *< Restrict by channel 
SND_SEQ_REMOVE_TIME_BEFORE	 = (1<<4)	# *< Restrict to before time 
SND_SEQ_REMOVE_TIME_AFTER	 = (1<<5)	# *< Restrict to time or after 
SND_SEQ_REMOVE_TIME_TICK	 = (1<<6)	# *< Time is in ticks 
SND_SEQ_REMOVE_EVENT_TYPE	 = (1<<7)	# *< Restrict to event type 
SND_SEQ_REMOVE_IGNORE_OFF 	 = (1<<8)	# *< Do not flush off events 
SND_SEQ_REMOVE_TAG_MATCH 	 = (1<<9)	# *< Restrict to events with given tag 

#size_t snd_seq_remove_events_sizeof(void);
snd_seq_remove_events_sizeof = _alsa_lib.snd_seq_remove_events_sizeof
snd_seq_remove_events_sizeof.argtypes = []
snd_seq_remove_events_sizeof.restype = c_size_t

# allocate a #snd_seq_remove_events_t container on stack 
#define snd_seq_remove_events_alloca(ptr) \
	#__snd_alloca(ptr, snd_seq_remove_events)
#int snd_seq_remove_events_malloc(snd_seq_remove_events_t **ptr);
snd_seq_remove_events_malloc = _alsa_lib.snd_seq_remove_events_malloc
snd_seq_remove_events_malloc.argtypes = [POINTER(POINTER(snd_seq_remove_events_t))]
snd_seq_remove_events_malloc.restype = c_int

#void snd_seq_remove_events_free(snd_seq_remove_events_t *ptr);
snd_seq_remove_events_free = _alsa_lib.snd_seq_remove_events_free
snd_seq_remove_events_free.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_free.restype = None

#void snd_seq_remove_events_copy(snd_seq_remove_events_t *dst, const snd_seq_remove_events_t *src);
snd_seq_remove_events_copy = _alsa_lib.snd_seq_remove_events_copy
snd_seq_remove_events_copy.argtypes = [POINTER(snd_seq_remove_events_t), POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_copy.restype = None


#unsigned int snd_seq_remove_events_get_condition(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_condition = _alsa_lib.snd_seq_remove_events_get_condition
snd_seq_remove_events_get_condition.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_condition.restype = c_uint

#int snd_seq_remove_events_get_queue(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_queue = _alsa_lib.snd_seq_remove_events_get_queue
snd_seq_remove_events_get_queue.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_queue.restype = c_int

#const snd_seq_timestamp_t *snd_seq_remove_events_get_time(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_time = _alsa_lib.snd_seq_remove_events_get_time
snd_seq_remove_events_get_time.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_time.restype = POINTER(snd_seq_timestamp_t)

#const snd_seq_addr_t *snd_seq_remove_events_get_dest(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_dest = _alsa_lib.snd_seq_remove_events_get_dest
snd_seq_remove_events_get_dest.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_dest.restype = POINTER(snd_seq_addr_t)

#int snd_seq_remove_events_get_channel(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_channel = _alsa_lib.snd_seq_remove_events_get_channel
snd_seq_remove_events_get_channel.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_channel.restype = c_int

#int snd_seq_remove_events_get_event_type(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_event_type = _alsa_lib.snd_seq_remove_events_get_event_type
snd_seq_remove_events_get_event_type.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_event_type.restype = c_int

#int snd_seq_remove_events_get_tag(const snd_seq_remove_events_t *info);
snd_seq_remove_events_get_tag = _alsa_lib.snd_seq_remove_events_get_tag
snd_seq_remove_events_get_tag.argtypes = [POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events_get_tag.restype = c_int


#void snd_seq_remove_events_set_condition(snd_seq_remove_events_t *info, unsigned int flags);
snd_seq_remove_events_set_condition = _alsa_lib.snd_seq_remove_events_set_condition
snd_seq_remove_events_set_condition.argtypes = [POINTER(snd_seq_remove_events_t), c_uint]
snd_seq_remove_events_set_condition.restype = None

#void snd_seq_remove_events_set_queue(snd_seq_remove_events_t *info, int queue);
snd_seq_remove_events_set_queue = _alsa_lib.snd_seq_remove_events_set_queue
snd_seq_remove_events_set_queue.argtypes = [POINTER(snd_seq_remove_events_t), c_int]
snd_seq_remove_events_set_queue.restype = None

#void snd_seq_remove_events_set_time(snd_seq_remove_events_t *info, const snd_seq_timestamp_t *time);
snd_seq_remove_events_set_time = _alsa_lib.snd_seq_remove_events_set_time
snd_seq_remove_events_set_time.argtypes = [POINTER(snd_seq_remove_events_t), POINTER(snd_seq_timestamp_t)]
snd_seq_remove_events_set_time.restype = None

#void snd_seq_remove_events_set_dest(snd_seq_remove_events_t *info, const snd_seq_addr_t *addr);
snd_seq_remove_events_set_dest = _alsa_lib.snd_seq_remove_events_set_dest
snd_seq_remove_events_set_dest.argtypes = [POINTER(snd_seq_remove_events_t), POINTER(snd_seq_addr_t)]
snd_seq_remove_events_set_dest.restype = None

#void snd_seq_remove_events_set_channel(snd_seq_remove_events_t *info, int channel);
snd_seq_remove_events_set_channel = _alsa_lib.snd_seq_remove_events_set_channel
snd_seq_remove_events_set_channel.argtypes = [POINTER(snd_seq_remove_events_t), c_int]
snd_seq_remove_events_set_channel.restype = None

#void snd_seq_remove_events_set_event_type(snd_seq_remove_events_t *info, int type);
snd_seq_remove_events_set_event_type = _alsa_lib.snd_seq_remove_events_set_event_type
snd_seq_remove_events_set_event_type.argtypes = [POINTER(snd_seq_remove_events_t), c_int]
snd_seq_remove_events_set_event_type.restype = None

#void snd_seq_remove_events_set_tag(snd_seq_remove_events_t *info, int tag);
snd_seq_remove_events_set_tag = _alsa_lib.snd_seq_remove_events_set_tag
snd_seq_remove_events_set_tag.argtypes = [POINTER(snd_seq_remove_events_t), c_int]
snd_seq_remove_events_set_tag.restype = None


#int snd_seq_remove_events(snd_seq_t *handle, snd_seq_remove_events_t *info);
snd_seq_remove_events = _alsa_lib.snd_seq_remove_events
snd_seq_remove_events.argtypes = [POINTER(snd_seq_t), POINTER(snd_seq_remove_events_t)]
snd_seq_remove_events.restype = c_int


# \} 

#
#  \defgroup SeqMisc Sequencer Miscellaneous
#  Sequencer Miscellaneous
#  \ingroup Sequencer
#  \{
#

#void snd_seq_set_bit(int nr, void *array);
snd_seq_set_bit = _alsa_lib.snd_seq_set_bit
snd_seq_set_bit.argtypes = [c_int, c_void_p]
snd_seq_set_bit.restype = None

#void snd_seq_unset_bit(int nr, void *array);
snd_seq_unset_bit = _alsa_lib.snd_seq_unset_bit
snd_seq_unset_bit.argtypes = [c_int, c_void_p]
snd_seq_unset_bit.restype = None

#int snd_seq_change_bit(int nr, void *array);
snd_seq_change_bit = _alsa_lib.snd_seq_change_bit
snd_seq_change_bit.argtypes = [c_int, c_void_p]
snd_seq_change_bit.restype = c_int

#int snd_seq_get_bit(int nr, void *array);
snd_seq_get_bit = _alsa_lib.snd_seq_get_bit
snd_seq_get_bit.argtypes = [c_int, c_void_p]
snd_seq_get_bit.restype = c_int


# \} 


#
#  \defgroup SeqEvType Sequencer Event Type Checks
#  Sequencer Event Type Checks
#  \ingroup Sequencer
#  \{
#

# event type macros 
SND_SEQ_EVFLG_RESULT = 0
SND_SEQ_EVFLG_NOTE = 1
SND_SEQ_EVFLG_CONTROL = 2 
SND_SEQ_EVFLG_QUEUE = 3
SND_SEQ_EVFLG_SYSTEM = 4
SND_SEQ_EVFLG_MESSAGE = 5
SND_SEQ_EVFLG_CONNECTION = 6
SND_SEQ_EVFLG_SAMPLE = 7
SND_SEQ_EVFLG_USERS = 8
SND_SEQ_EVFLG_INSTR = 9
SND_SEQ_EVFLG_QUOTE = 10
SND_SEQ_EVFLG_NONE = 11
SND_SEQ_EVFLG_RAW = 12
SND_SEQ_EVFLG_FIXED = 13
SND_SEQ_EVFLG_VARIABLE = 14
SND_SEQ_EVFLG_VARUSR = 15

SND_SEQ_EVFLG_NOTE_ONEARG = 0
SND_SEQ_EVFLG_NOTE_TWOARG = 1

SND_SEQ_EVFLG_QUEUE_NOARG = 0
SND_SEQ_EVFLG_QUEUE_TICK = 1
SND_SEQ_EVFLG_QUEUE_TIME = 2
SND_SEQ_EVFLG_QUEUE_VALUE = 3

#
# Exported event type table
#
# This table is referred by snd_seq_ev_is_xxx.
#
#extern const unsigned int snd_seq_event_types[];

#define _SND_SEQ_TYPE(x)	(1<<(x))	*< master type - 24bit 
#define _SND_SEQ_TYPE_OPT(x)	((x)<<24)	*< optional type - 8bit 

# check the event type 
#define snd_seq_type_check(ev,x) (snd_seq_event_types[(ev)->type] & _SND_SEQ_TYPE(x))

# event type check: result events 
#define snd_seq_ev_is_result_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_RESULT)
# event type check: note events 
#define snd_seq_ev_is_note_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_NOTE)
# event type check: control events 
#define snd_seq_ev_is_control_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_CONTROL)
# event type check: channel specific events 
#define snd_seq_ev_is_channel_type(ev) \
	#(snd_seq_event_types[(ev)->type] & (_SND_SEQ_TYPE(SND_SEQ_EVFLG_NOTE) | _SND_SEQ_TYPE(SND_SEQ_EVFLG_CONTROL)))

# event type check: queue control events 
#define snd_seq_ev_is_queue_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_QUEUE)
# event type check: system status messages 
#define snd_seq_ev_is_message_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_MESSAGE)
# event type check: system status messages 
#define snd_seq_ev_is_subscribe_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_CONNECTION)
# event type check: sample messages 
#define snd_seq_ev_is_sample_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_SAMPLE)
# event type check: user-defined messages 
#define snd_seq_ev_is_user_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_USERS)
# event type check: instrument layer events 
#define snd_seq_ev_is_instr_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_INSTR)
# event type check: fixed length events 
#define snd_seq_ev_is_fixed_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_FIXED)
# event type check: variable length events 
#define snd_seq_ev_is_variable_type(ev)	\
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_VARIABLE)
# event type check: user pointer events 
#define snd_seq_ev_is_varusr_type(ev) \
	#snd_seq_type_check(ev, SND_SEQ_EVFLG_VARUSR)
# event type check: reserved for kernel 
#define snd_seq_ev_is_reserved(ev) \
	#(! snd_seq_event_types[(ev)->type])

#
# macros to check event flags
#
# prior events 
#define snd_seq_ev_is_prior(ev)	\
	#(((ev)->flags & SND_SEQ_PRIORITY_MASK) == SND_SEQ_PRIORITY_HIGH)

# get the data length type 
#define snd_seq_ev_length_type(ev) \
	#((ev)->flags & SND_SEQ_EVENT_LENGTH_MASK)
# fixed length events 
#define snd_seq_ev_is_fixed(ev)	\
	#(snd_seq_ev_length_type(ev) == SND_SEQ_EVENT_LENGTH_FIXED)
# variable length events 
#define snd_seq_ev_is_variable(ev) \
	#(snd_seq_ev_length_type(ev) == SND_SEQ_EVENT_LENGTH_VARIABLE)
# variable length on user-space 
#define snd_seq_ev_is_varusr(ev) \
	#(snd_seq_ev_length_type(ev) == SND_SEQ_EVENT_LENGTH_VARUSR)

# time-stamp type 
#define snd_seq_ev_timestamp_type(ev) \
	#((ev)->flags & SND_SEQ_TIME_STAMP_MASK)
# event is in tick time 
#define snd_seq_ev_is_tick(ev) \
	#(snd_seq_ev_timestamp_type(ev) == SND_SEQ_TIME_STAMP_TICK)
# event is in real-time 
#define snd_seq_ev_is_real(ev) \
	#(snd_seq_ev_timestamp_type(ev) == SND_SEQ_TIME_STAMP_REAL)

# time-mode type 
#define snd_seq_ev_timemode_type(ev) \
	#((ev)->flags & SND_SEQ_TIME_MODE_MASK)
# scheduled in absolute time 
#define snd_seq_ev_is_abstime(ev) \
	#(snd_seq_ev_timemode_type(ev) == SND_SEQ_TIME_MODE_ABS)
# scheduled in relative time 
#define snd_seq_ev_is_reltime(ev) \
	#(snd_seq_ev_timemode_type(ev) == SND_SEQ_TIME_MODE_REL)

# direct dispatched events 
#define snd_seq_ev_is_direct(ev) \
	#((ev)->queue == SND_SEQ_QUEUE_DIRECT)
