#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides access to alsa pcm.
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


""" An alsa pcm module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .alsa_conf import *
from .alsa_error import *

EINTR = 4
EPIPE = 32
EBADFD = 77
ESTRPIPE = 86

# PCM generic info container 
class _snd_pcm_info(Structure):
    _fields_ = [
            ]
snd_pcm_info_t = _snd_pcm_info

# PCM hardware configuration space container 
class _snd_pcm_hw_params(Structure):
    _fields_ = [
            ]
snd_pcm_hw_params_t = _snd_pcm_hw_params 

# PCM software configuration container 
class _snd_pcm_sw_params(Structure):
    _fields_ = [
            ]
snd_pcm_sw_params_t = _snd_pcm_sw_params

# PCM status container 
class _snd_pcm_status(Structure):
    _fields_ = [
            ]
snd_pcm_status_t = _snd_pcm_status

# PCM access types mask 
class _snd_pcm_access_mask(Structure):
    _fields_ = [
            ]
snd_pcm_access_mask_t = _snd_pcm_access_mask

# PCM formats mask 
class _snd_pcm_format_mask(Structure):
    _fields_ = [
            ]
snd_pcm_format_mask_t = _snd_pcm_format_mask

# PCM subformats mask 
class _snd_pcm_subformat_mask(Structure):
    _fields_ = [
            ]
snd_pcm_subformat_mask_t = _snd_pcm_subformat_mask

# PCM class 
_snd_pcm_class = c_int
# standard device 

SND_PCM_CLASS_GENERIC = 0
# multichannel device 
SND_PCM_CLASS_MULTI = 1
# software modem device 
SND_PCM_CLASS_MODEM = 2
# digitizer device 
SND_PCM_CLASS_DIGITIZER = 3
SND_PCM_CLASS_LAST = SND_PCM_CLASS_DIGITIZER
snd_pcm_class_t = _snd_pcm_class

# PCM subclass 
_snd_pcm_subclass = c_int
# subdevices are mixed together 
SND_PCM_SUBCLASS_GENERIC_MIX = 0
# multichannel subdevices are mixed together 
SND_PCM_SUBCLASS_MULTI_MIX = 1
SND_PCM_SUBCLASS_LAST = SND_PCM_SUBCLASS_MULTI_MIX
snd_pcm_subclass_t = _snd_pcm_subclass

# PCM stream (direction) 
_snd_pcm_stream = c_int 
# Playback stream 
SND_PCM_STREAM_PLAYBACK = 0
# Capture stream 
SND_PCM_STREAM_CAPTURE = 1
SND_PCM_STREAM_LAST = SND_PCM_STREAM_CAPTURE
snd_pcm_stream_t = _snd_pcm_stream

# PCM access type 
_snd_pcm_access = c_int
# PCM access type 
# mmap access with simple interleaved channels 
SND_PCM_ACCESS_MMAP_INTERLEAVED = 0
# mmap access with simple non interleaved channels 
SND_PCM_ACCESS_MMAP_NONINTERLEAVED = 1
# mmap access with complex placement 
SND_PCM_ACCESS_MMAP_COMPLEX = 2
# snd_pcm_readi/snd_pcm_writei access 
SND_PCM_ACCESS_RW_INTERLEAVED = 3
# snd_pcm_readn/snd_pcm_writen access 
SND_PCM_ACCESS_RW_NONINTERLEAVED = 4
SND_PCM_ACCESS_LAST = SND_PCM_ACCESS_RW_NONINTERLEAVED
snd_pcm_access_t = _snd_pcm_access

# PCM sample format 
_snd_pcm_format = c_int
# Unknown 
SND_PCM_FORMAT_UNKNOWN = -1
# Signed 8 bit 
SND_PCM_FORMAT_S8 = 0
# Unsigned 8 bit 
SND_PCM_FORMAT_U8 = 1
# Signed 16 bit Little Endian 
SND_PCM_FORMAT_S16_LE = 2
# Signed 16 bit Big Endian 
SND_PCM_FORMAT_S16_BE = 3
# Unsigned 16 bit Little Endian 
SND_PCM_FORMAT_U16_LE = 4
# Unsigned 16 bit Big Endian 
SND_PCM_FORMAT_U16_BE = 5
# Signed 24 bit Little Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_S24_LE = 6
# Signed 24 bit Big Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_S24_BE = 7
# Unsigned 24 bit Little Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_U24_LE = 8
# Unsigned 24 bit Big Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_U24_BE = 9
# Signed 32 bit Little Endian 
SND_PCM_FORMAT_S32_LE = 10
# Signed 32 bit Big Endian 
SND_PCM_FORMAT_S32_BE = 11
# Unsigned 32 bit Little Endian 
SND_PCM_FORMAT_U32_LE = 12
# Unsigned 32 bit Big Endian 
SND_PCM_FORMAT_U32_BE = 13
# Float 32 bit Little Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT_LE = 14
# Float 32 bit Big Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT_BE = 15
# Float 64 bit Little Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT64_LE = 16
# Float 64 bit Big Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT64_BE = 17
# IEC-958 Little Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME_LE = 18
# IEC-958 Big Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME_BE = 19
# Mu-Law 
SND_PCM_FORMAT_MU_LAW = 20
# A-Law 
SND_PCM_FORMAT_A_LAW = 21
# Ima-ADPCM 
SND_PCM_FORMAT_IMA_ADPCM = 22
# MPEG 
SND_PCM_FORMAT_MPEG = 23
# GSM 
SND_PCM_FORMAT_GSM = 24
# Special 
SND_PCM_FORMAT_SPECIAL = 31
# Signed 24bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S24_3LE = 32
# Signed 24bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S24_3BE = 33
# Unsigned 24bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U24_3LE = 34
# Unsigned 24bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U24_3BE = 35
# Signed 20bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S20_3LE = 36
# Signed 20bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S20_3BE = 37
# Unsigned 20bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U20_3LE = 38
# Unsigned 20bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U20_3BE = 39
# Signed 18bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S18_3LE = 40
# Signed 18bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S18_3BE = 41
# Unsigned 18bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U18_3LE = 42
# Unsigned 18bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U18_3BE = 43
SND_PCM_FORMAT_LAST = SND_PCM_FORMAT_U18_3BE

#if __BYTE_ORDER == __LITTLE_ENDIAN
# Signed 16 bit CPU endian 
SND_PCM_FORMAT_S16 = SND_PCM_FORMAT_S16_LE
# Unsigned 16 bit CPU endian 
SND_PCM_FORMAT_U16 = SND_PCM_FORMAT_U16_LE
# Signed 24 bit CPU endian 
SND_PCM_FORMAT_S24 = SND_PCM_FORMAT_S24_LE
# Unsigned 24 bit CPU endian 
SND_PCM_FORMAT_U24 = SND_PCM_FORMAT_U24_LE
# Signed 32 bit CPU endian 
SND_PCM_FORMAT_S32 = SND_PCM_FORMAT_S32_LE
# Unsigned 32 bit CPU endian 
SND_PCM_FORMAT_U32 = SND_PCM_FORMAT_U32_LE
# Float 32 bit CPU endian 
SND_PCM_FORMAT_FLOAT = SND_PCM_FORMAT_FLOAT_LE
# Float 64 bit CPU endian 
SND_PCM_FORMAT_FLOAT64 = SND_PCM_FORMAT_FLOAT64_LE
# IEC-958 CPU Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME = SND_PCM_FORMAT_IEC958_SUBFRAME_LE
#elif __BYTE_ORDER == __BIG_ENDIAN
# Signed 16 bit CPU endian 
SND_PCM_FORMAT_S16 = SND_PCM_FORMAT_S16_BE
# Unsigned 16 bit CPU endian 
SND_PCM_FORMAT_U16 = SND_PCM_FORMAT_U16_BE
# Signed 24 bit CPU endian 
SND_PCM_FORMAT_S24 = SND_PCM_FORMAT_S24_BE
# Unsigned 24 bit CPU endian 
SND_PCM_FORMAT_U24 = SND_PCM_FORMAT_U24_BE
# Signed 32 bit CPU endian 
SND_PCM_FORMAT_S32 = SND_PCM_FORMAT_S32_BE
# Unsigned 32 bit CPU endian 
SND_PCM_FORMAT_U32 = SND_PCM_FORMAT_U32_BE
# Float 32 bit CPU endian 
SND_PCM_FORMAT_FLOAT = SND_PCM_FORMAT_FLOAT_BE
# Float 64 bit CPU endian 
SND_PCM_FORMAT_FLOAT64 = SND_PCM_FORMAT_FLOAT64_BE
# IEC-958 CPU Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME = SND_PCM_FORMAT_IEC958_SUBFRAME_BE
snd_pcm_format_t = _snd_pcm_format

# PCM sample subformat 
_snd_pcm_subformat = c_int
# Standard 
SND_PCM_SUBFORMAT_STD = 0
SND_PCM_SUBFORMAT_LAST = SND_PCM_SUBFORMAT_STD
snd_pcm_subformat_t = _snd_pcm_subformat

# PCM state 
_snd_pcm_state = c_int
# Open 
SND_PCM_STATE_OPEN = 0
# Setup installed  
SND_PCM_STATE_SETUP = 1
# Ready to start 
SND_PCM_STATE_PREPARED = 2
# Running 
SND_PCM_STATE_RUNNING = 3
# Stopped: underrun (playback) or overrun (capture) detected 
SND_PCM_STATE_XRUN = 4
# Draining: running (playback) or stopped (capture) 
SND_PCM_STATE_DRAINING = 5
# Paused 
SND_PCM_STATE_PAUSED = 6
# Hardware is suspended 
SND_PCM_STATE_SUSPENDED = 7
# Hardware is disconnected 
SND_PCM_STATE_DISCONNECTED = 8
SND_PCM_STATE_LAST = SND_PCM_STATE_DISCONNECTED
snd_pcm_state_t = _snd_pcm_state

# PCM start mode 
_snd_pcm_start = c_int
# Automatic start on data read/write 
SND_PCM_START_DATA = 0
# Explicit start 
SND_PCM_START_EXPLICIT = 1
SND_PCM_START_LAST = SND_PCM_START_EXPLICIT
snd_pcm_start_t = _snd_pcm_start

# PCM xrun mode 
_snd_pcm_xrun = c_int
# Xrun detection disabled 
SND_PCM_XRUN_NONE = 0
# Stop on xrun detection 
SND_PCM_XRUN_STOP = 1
SND_PCM_XRUN_LAST = SND_PCM_XRUN_STOP
snd_pcm_xrun_t = _snd_pcm_xrun

# PCM timestamp mode 
_snd_pcm_tstamp = c_int
# No timestamp 
SND_PCM_TSTAMP_NONE = 0
# Update timestamp at every hardware position update 
SND_PCM_TSTAMP_ENABLE = 1
# Equivalent with #SND_PCM_TSTAMP_ENABLE,
# just for compatibility with older versions
#
SND_PCM_TSTAMP_MMAP = SND_PCM_TSTAMP_ENABLE
SND_PCM_TSTAMP_LAST = SND_PCM_TSTAMP_ENABLE
snd_pcm_tstamp_t = _snd_pcm_tstamp

# Unsigned frames quantity 
snd_pcm_uframes_t = c_ulong
# Signed frames quantity 
snd_pcm_sframes_t = c_long

# Non blocking mode (flag for open mode) \hideinitializer 
SND_PCM_NONBLOCK = 0x00000001
# Async notification (flag for open mode) \hideinitializer 
SND_PCM_ASYNC =	0x00000002
# Disable automatic (but not forced!) rate resamplinig 
SND_PCM_NO_AUTO_RESAMPLE = 0x00010000
# Disable automatic (but not forced!) channel conversion 
SND_PCM_NO_AUTO_CHANNELS = 0x00020000
# Disable automatic (but not forced!) format conversion 
SND_PCM_NO_AUTO_FORMAT = 0x00040000
# Disable soft volume control 
SND_PCM_NO_SOFTVOL = 0x00080000

# PCM handle 
class _snd_pcm(Structure):
    _fields_ = [
            ]
snd_pcm_t = _snd_pcm

# PCM type 
_snd_pcm_type = c_int
# Kernel level PCM 
SND_PCM_TYPE_HW = 0
# Hooked PCM 
SND_PCM_TYPE_HOOKS = 1
# One or more linked PCM with exclusive access to selected
#channels 
SND_PCM_TYPE_MULTI = 2
# File writing plugin 
SND_PCM_TYPE_FILE = 3
# Null endpoint PCM 
SND_PCM_TYPE_NULL = 4
# Shared memory client PCM 
SND_PCM_TYPE_SHM = 5
# INET client PCM (not yet implemented) 
SND_PCM_TYPE_INET = 6
# Copying plugin 
SND_PCM_TYPE_COPY = 7
# Linear format conversion PCM 
SND_PCM_TYPE_LINEAR = 8
# A-Law format conversion PCM 
SND_PCM_TYPE_ALAW = 9
# Mu-Law format conversion PCM 
SND_PCM_TYPE_MULAW = 10
# IMA-ADPCM format conversion PCM 
SND_PCM_TYPE_ADPCM = 11
# Rate conversion PCM 
SND_PCM_TYPE_RATE = 12
# Attenuated static route PCM 
SND_PCM_TYPE_ROUTE = 13
# Format adjusted PCM 
SND_PCM_TYPE_PLUG = 14
# Sharing PCM 
SND_PCM_TYPE_SHARE = 15
# Meter plugin 
SND_PCM_TYPE_METER = 16
# Mixing PCM 
SND_PCM_TYPE_MIX = 17
# Attenuated dynamic route PCM (not yet implemented) 
SND_PCM_TYPE_DROUTE = 18
# Loopback server plugin (not yet implemented) 
SND_PCM_TYPE_LBSERVER = 19
# Linear Integer <-> Linear Float format conversion PCM 
SND_PCM_TYPE_LINEAR_FLOAT = 20
# LADSPA integration plugin 
SND_PCM_TYPE_LADSPA = 21
# Direct Mixing plugin 
SND_PCM_TYPE_DMIX = 22
# Jack Audio Connection Kit plugin 
SND_PCM_TYPE_JACK = 23
# Direct Snooping plugin 
SND_PCM_TYPE_DSNOOP = 24
# Direct Sharing plugin 
SND_PCM_TYPE_DSHARE = 25
# IEC958 subframe plugin 
SND_PCM_TYPE_IEC958 = 26
# Soft volume plugin 
SND_PCM_TYPE_SOFTVOL = 27
# External I/O plugin 
SND_PCM_TYPE_IOPLUG = 28
# External filter plugin 
SND_PCM_TYPE_EXTPLUG = 29
# Mmap-emulation plugin 
SND_PCM_TYPE_MMAP_EMUL = 30
SND_PCM_TYPE_LAST = SND_PCM_TYPE_MMAP_EMUL

# PCM type 
snd_pcm_type_t = _snd_pcm_type

# PCM area specification 
class _snd_pcm_channel_area(Structure):
    _fields_ = [
			# base address of channel samples 
            ('addr', c_void_p),
			# offset to first sample in bits 
            ('first', c_uint),
			# samples distance in bits 
            ('step', c_uint)
            ]
snd_pcm_channel_area_t = _snd_pcm_channel_area

# PCM synchronization ID 
class _snd_pcm_sync_id(Union):
    _fields_ = [
# 8-bit ID 
        	('id', c_ubyte * 16),
	        # 16-bit ID 
	        ('id16', c_ushort * 8),
	        # 32-bit ID 
	        ('id32', c_uint * 4),
            ]
snd_pcm_sync_id_t = _snd_pcm_sync_id

# #SND_PCM_TYPE_METER scope handle 
class _snd_pcm_scope(Structure):
    _fields_ = [
            ]
snd_pcm_scope_t = _snd_pcm_scope


#int snd_pcm_open(snd_pcm_t **pcm, const char *name, 
		 #snd_pcm_stream_t stream, int mode);
snd_pcm_open = _alsa_lib.snd_pcm_open
snd_pcm_open.argtypes = [POINTER(POINTER(snd_pcm_t)), c_char_p, snd_pcm_stream_t, c_int]
snd_pcm_open.restype = c_int

#int snd_pcm_open_lconf(snd_pcm_t **pcm, const char *name, 
			   #snd_pcm_stream_t stream, int mode,
			   #snd_config_t *lconf);
snd_pcm_open_lconf = _alsa_lib.snd_pcm_open_lconf
snd_pcm_open_lconf.argtypes = [POINTER(POINTER(snd_pcm_t)), c_char_p, snd_pcm_stream_t, c_int, POINTER(snd_config_t)]
snd_pcm_open_lconf.restype = c_int

#int snd_pcm_close(snd_pcm_t *pcm);
snd_pcm_close = _alsa_lib.snd_pcm_close
snd_pcm_close.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_close.restype = c_int

#const char *snd_pcm_name(snd_pcm_t *pcm);
snd_pcm_name = _alsa_lib.snd_pcm_name
snd_pcm_name.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_name.restype = c_char_p

#snd_pcm_type_t snd_pcm_type(snd_pcm_t *pcm);
snd_pcm_type = _alsa_lib.snd_pcm_type
snd_pcm_type.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_type.restype = snd_pcm_type_t

#snd_pcm_stream_t snd_pcm_stream(snd_pcm_t *pcm);
snd_pcm_stream = _alsa_lib.snd_pcm_stream
snd_pcm_stream.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_stream.restype = snd_pcm_stream_t

#int snd_pcm_poll_descriptors_count(snd_pcm_t *pcm);
snd_pcm_poll_descriptors_count = _alsa_lib.snd_pcm_poll_descriptors_count
snd_pcm_poll_descriptors_count.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_poll_descriptors_count.restype = c_int

#int snd_pcm_poll_descriptors(snd_pcm_t *pcm, struct pollfd *pfds, unsigned int space);
snd_pcm_poll_descriptors = _alsa_lib.snd_pcm_poll_descriptors
snd_pcm_poll_descriptors.argtypes = [POINTER(snd_pcm_t), POINTER(pollfd), c_uint]
snd_pcm_poll_descriptors.restype = c_int

#int snd_pcm_poll_descriptors_revents(snd_pcm_t *pcm, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_pcm_poll_descriptors_revents = _alsa_lib.snd_pcm_poll_descriptors_revents
snd_pcm_poll_descriptors_revents.argtypes = [POINTER(snd_pcm_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_pcm_poll_descriptors_revents.restype = c_int

#int snd_pcm_nonblock(snd_pcm_t *pcm, int nonblock);
snd_pcm_nonblock = _alsa_lib.snd_pcm_nonblock
snd_pcm_nonblock.argtypes = [POINTER(snd_pcm_t), c_int]
snd_pcm_nonblock.restype = c_int

#int snd_async_add_pcm_handler(snd_async_handler_t **handler, snd_pcm_t *pcm, 
				  #snd_async_callback_t callback, void *private_data);
snd_async_add_pcm_handler = _alsa_lib.snd_async_add_pcm_handler
snd_async_add_pcm_handler.argtypes = [POINTER(POINTER(snd_async_handler_t)), POINTER(snd_pcm_t), snd_async_callback_t, c_void_p]
snd_async_add_pcm_handler.restype = c_int

#snd_pcm_t *snd_async_handler_get_pcm(snd_async_handler_t *handler);
snd_async_handler_get_pcm = _alsa_lib.snd_async_handler_get_pcm
snd_async_handler_get_pcm.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_pcm.restype = POINTER(snd_pcm_t)

#int snd_pcm_info(snd_pcm_t *pcm, snd_pcm_info_t *info);
snd_pcm_info = _alsa_lib.snd_pcm_info
snd_pcm_info.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_info_t)]
snd_pcm_info.restype = c_int

#int snd_pcm_hw_params_current(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params_current = _alsa_lib.snd_pcm_hw_params_current
snd_pcm_hw_params_current.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_current.restype = c_int

#int snd_pcm_hw_params(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params = _alsa_lib.snd_pcm_hw_params
snd_pcm_hw_params.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params.restype = c_int

#int snd_pcm_hw_free(snd_pcm_t *pcm);
snd_pcm_hw_free = _alsa_lib.snd_pcm_hw_free
snd_pcm_hw_free.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_hw_free.restype = c_int

#int snd_pcm_sw_params_current(snd_pcm_t *pcm, snd_pcm_sw_params_t *params);
snd_pcm_sw_params_current = _alsa_lib.snd_pcm_sw_params_current
snd_pcm_sw_params_current.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params_current.restype = c_int

#int snd_pcm_sw_params(snd_pcm_t *pcm, snd_pcm_sw_params_t *params);
snd_pcm_sw_params = _alsa_lib.snd_pcm_sw_params
snd_pcm_sw_params.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params.restype = c_int

#int snd_pcm_prepare(snd_pcm_t *pcm);
snd_pcm_prepare = _alsa_lib.snd_pcm_prepare
snd_pcm_prepare.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_prepare.restype = c_int

#int snd_pcm_reset(snd_pcm_t *pcm);
snd_pcm_reset = _alsa_lib.snd_pcm_reset
snd_pcm_reset.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_reset.restype = c_int

#int snd_pcm_status(snd_pcm_t *pcm, snd_pcm_status_t *status);
snd_pcm_status = _alsa_lib.snd_pcm_status
snd_pcm_status.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_status_t)]
snd_pcm_status.restype = c_int

#int snd_pcm_start(snd_pcm_t *pcm);
snd_pcm_start = _alsa_lib.snd_pcm_start
snd_pcm_start.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_start.restype = c_int

#int snd_pcm_drop(snd_pcm_t *pcm);
snd_pcm_drop = _alsa_lib.snd_pcm_drop
snd_pcm_drop.artypes = [POINTER(snd_pcm_t)]
snd_pcm_drop.restype = c_int

#int snd_pcm_drain(snd_pcm_t *pcm);
snd_pcm_drain = _alsa_lib.snd_pcm_drain
snd_pcm_drain.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_drain.restype = c_int

#int snd_pcm_pause(snd_pcm_t *pcm, int enable);
snd_pcm_pause = _alsa_lib.snd_pcm_pause
snd_pcm_pause.argtypes = [POINTER(snd_pcm_t), c_int]
snd_pcm_pause.restype = c_int

#snd_pcm_state_t snd_pcm_state(snd_pcm_t *pcm);
snd_pcm_state = _alsa_lib.snd_pcm_state
snd_pcm_state.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_state.restype = snd_pcm_state_t

#int snd_pcm_hwsync(snd_pcm_t *pcm);
snd_pcm_hwsync = _alsa_lib.snd_pcm_hwsync
snd_pcm_hwsync.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_hwsync.restype = c_int

#int snd_pcm_delay(snd_pcm_t *pcm, snd_pcm_sframes_t *delayp);
snd_pcm_delay = _alsa_lib.snd_pcm_delay
snd_pcm_delay.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sframes_t)]
snd_pcm_delay.restype = c_int

#int snd_pcm_resume(snd_pcm_t *pcm);
snd_pcm_resume = _alsa_lib.snd_pcm_resume
snd_pcm_resume.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_resume.restype = c_int

#int snd_pcm_htimestamp(snd_pcm_t *pcm, snd_pcm_uframes_t *avail, snd_htimestamp_t *tstamp);
snd_pcm_htimestamp = _alsa_lib.snd_pcm_htimestamp
snd_pcm_htimestamp.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_uframes_t), POINTER(snd_htimestamp_t)]
snd_pcm_htimestamp.restype = c_int

#snd_pcm_sframes_t snd_pcm_avail(snd_pcm_t *pcm);
snd_pcm_avail = _alsa_lib.snd_pcm_avail
snd_pcm_avail.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_avail.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_avail_update(snd_pcm_t *pcm);
snd_pcm_avail_update = _alsa_lib.snd_pcm_avail_update
snd_pcm_avail_update.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_avail_update.restype = snd_pcm_sframes_t

#int snd_pcm_avail_delay(snd_pcm_t *pcm, snd_pcm_sframes_t *availp, snd_pcm_sframes_t *delayp);
snd_pcm_avail_delay = _alsa_lib.snd_pcm_avail_delay
snd_pcm_avail_delay.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sframes_t), POINTER(snd_pcm_sframes_t)]
snd_pcm_avail_delay.restype = c_int

#snd_pcm_sframes_t snd_pcm_rewindable(snd_pcm_t *pcm);
snd_pcm_rewindable = _alsa_lib.snd_pcm_rewindable
snd_pcm_rewindable.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_rewindable.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_rewind(snd_pcm_t *pcm, snd_pcm_uframes_t frames);
snd_pcm_rewind = _alsa_lib.snd_pcm_rewind
snd_pcm_rewind.argtypes = [POINTER(snd_pcm_t), snd_pcm_uframes_t]
snd_pcm_rewind.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_forwardable(snd_pcm_t *pcm);
snd_pcm_forwardable = _alsa_lib.snd_pcm_forwardable
snd_pcm_forwardable.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_forwardable.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_forward(snd_pcm_t *pcm, snd_pcm_uframes_t frames);
snd_pcm_forward = _alsa_lib.snd_pcm_forward
snd_pcm_forward.argtypes = [POINTER(snd_pcm_t), snd_pcm_uframes_t]
snd_pcm_forward.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_writei(snd_pcm_t *pcm, const void *buffer, snd_pcm_uframes_t size);
snd_pcm_writei = _alsa_lib.snd_pcm_writei
snd_pcm_writei.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_writei.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_readi(snd_pcm_t *pcm, void *buffer, snd_pcm_uframes_t size);
snd_pcm_readi = _alsa_lib.snd_pcm_readi
snd_pcm_readi.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_readi.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_writen(snd_pcm_t *pcm, void **bufs, snd_pcm_uframes_t size);
snd_pcm_writen = _alsa_lib.snd_pcm_writen
snd_pcm_writen.argtypes = [POINTER(snd_pcm_t), POINTER(c_void_p), snd_pcm_uframes_t]
snd_pcm_writen.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_readn(snd_pcm_t *pcm, void **bufs, snd_pcm_uframes_t size);
snd_pcm_readn = _alsa_lib.snd_pcm_readn
snd_pcm_readn.argtypes = [POINTER(snd_pcm_t), POINTER(c_void_p), snd_pcm_uframes_t]
snd_pcm_readn.restype = snd_pcm_sframes_t

#int snd_pcm_wait(snd_pcm_t *pcm, int timeout);
snd_pcm_wait = _alsa_lib.snd_pcm_wait
snd_pcm_wait.argtypes = [POINTER(snd_pcm_t), c_int]
snd_pcm_wait.restype = c_int


#int snd_pcm_link(snd_pcm_t *pcm1, snd_pcm_t *pcm2);
snd_pcm_link = _alsa_lib.snd_pcm_link
snd_pcm_link.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_t)]
snd_pcm_link.restype = c_int

#int snd_pcm_unlink(snd_pcm_t *pcm);
snd_pcm_unlink = _alsa_lib.snd_pcm_unlink
snd_pcm_unlink.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_unlink.restype = c_int


#//int snd_pcm_mixer_element(snd_pcm_t *pcm, snd_mixer_t *mixer, snd_mixer_elem_t **elem);

#
# application helpers - these functions are implemented on top
# of the basic API
#

#int snd_pcm_recover(snd_pcm_t *pcm, int err, int silent);
snd_pcm_recover = _alsa_lib.snd_pcm_recover
snd_pcm_recover.argtypes = [POINTER(snd_pcm_t), c_int, c_int]
snd_pcm_recover.restype = c_int

#int snd_pcm_set_params(snd_pcm_t *pcm,
#snd_pcm_format_t format,
#snd_pcm_access_t access,
#unsigned int channels,
#unsigned int rate,
#int soft_resample,
#unsigned int latency);
snd_pcm_set_params = _alsa_lib.snd_pcm_set_params
snd_pcm_set_params.argtypes = [POINTER(snd_pcm_t), snd_pcm_format_t, snd_pcm_access_t, c_uint, c_uint, c_int, c_uint]
snd_pcm_set_params.restype = c_int

#int snd_pcm_get_params(snd_pcm_t *pcm,
#snd_pcm_uframes_t *buffer_size,
#snd_pcm_uframes_t *period_size);
snd_pcm_get_params = _alsa_lib.snd_pcm_get_params
snd_pcm_get_params.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_uframes_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_get_params.restype = c_int

# \} 

#
# \defgroup PCM_Info Stream Information
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_info_sizeof(void);
snd_pcm_info_sizeof = _alsa_lib.snd_pcm_info_sizeof
snd_pcm_info_sizeof.argtypes = []
snd_pcm_info_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_pcm_info_t using standard alloca
# \param ptr returned pointer
#
#int snd_pcm_info_malloc(snd_pcm_info_t **ptr);
snd_pcm_info_malloc = _alsa_lib.snd_pcm_info_malloc
snd_pcm_info_malloc.argtypes = [POINTER(POINTER(snd_pcm_info_t))]
snd_pcm_info_malloc.restype = c_int

#void snd_pcm_info_free(snd_pcm_info_t *obj);
snd_pcm_info_free = _alsa_lib.snd_pcm_info_free
snd_pcm_info_free.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_free.restype = None

#void snd_pcm_info_copy(snd_pcm_info_t *dst, const snd_pcm_info_t *src);
snd_pcm_info_copy = _alsa_lib.snd_pcm_info_copy
snd_pcm_info_copy.argtypes = [POINTER(snd_pcm_info_t), POINTER(snd_pcm_info_t)]
snd_pcm_info_copy.restype = None

#unsigned int snd_pcm_info_get_device(const snd_pcm_info_t *obj);
snd_pcm_info_get_device = _alsa_lib.snd_pcm_info_get_device
snd_pcm_info_get_device.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_device.restype = c_uint

#unsigned int snd_pcm_info_get_subdevice(const snd_pcm_info_t *obj);
snd_pcm_info_get_subdevice = _alsa_lib.snd_pcm_info_get_subdevice
snd_pcm_info_get_subdevice.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_subdevice.restype = c_uint

#snd_pcm_stream_t snd_pcm_info_get_stream(const snd_pcm_info_t *obj);
snd_pcm_info_get_stream = _alsa_lib.snd_pcm_info_get_stream
snd_pcm_info_get_stream.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_stream.restype = snd_pcm_stream_t

#int snd_pcm_info_get_card(const snd_pcm_info_t *obj);
snd_pcm_info_get_card = _alsa_lib.snd_pcm_info_get_card
snd_pcm_info_get_card.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_card.restype = c_int

#const char *snd_pcm_info_get_id(const snd_pcm_info_t *obj);
snd_pcm_info_get_id = _alsa_lib.snd_pcm_info_get_id
snd_pcm_info_get_id.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_id.restype = c_char_p

#const char *snd_pcm_info_get_name(const snd_pcm_info_t *obj);
snd_pcm_info_get_name = _alsa_lib.snd_pcm_info_get_name
snd_pcm_info_get_name.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_name.restype = c_char_p

#const char *snd_pcm_info_get_subdevice_name(const snd_pcm_info_t *obj);
snd_pcm_info_get_subdevice_name = _alsa_lib.snd_pcm_info_get_subdevice_name
snd_pcm_info_get_subdevice_name.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_subdevice_name.restype = c_char_p

#snd_pcm_class_t snd_pcm_info_get_class(const snd_pcm_info_t *obj);
snd_pcm_info_get_class = _alsa_lib.snd_pcm_info_get_class
snd_pcm_info_get_class.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_class.restype = snd_pcm_class_t

#snd_pcm_subclass_t snd_pcm_info_get_subclass(const snd_pcm_info_t *obj);
snd_pcm_info_get_subclass = _alsa_lib.snd_pcm_info_get_subclass
snd_pcm_info_get_subclass.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_subclass.restype = snd_pcm_subclass_t

#unsigned int snd_pcm_info_get_subdevices_count(const snd_pcm_info_t *obj);
snd_pcm_info_get_subdevices_count = _alsa_lib.snd_pcm_info_get_subdevices_count
snd_pcm_info_get_subdevices_count.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_subdevices_count.restype = c_uint

#unsigned int snd_pcm_info_get_subdevices_avail(const snd_pcm_info_t *obj);
snd_pcm_info_get_subdevices_avail = _alsa_lib.snd_pcm_info_get_subdevices_avail
snd_pcm_info_get_subdevices_avail.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_subdevices_avail.restype = c_uint

#snd_pcm_sync_id_t snd_pcm_info_get_sync(const snd_pcm_info_t *obj);
snd_pcm_info_get_sync = _alsa_lib.snd_pcm_info_get_sync
snd_pcm_info_get_sync.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_sync.restype = snd_pcm_sync_id_t

#void snd_pcm_info_set_device(snd_pcm_info_t *obj, unsigned int val);
snd_pcm_info_set_device = _alsa_lib.snd_pcm_info_set_device
snd_pcm_info_set_device.argtypes = [POINTER(snd_pcm_info_t), c_uint]
snd_pcm_info_set_device.restype = None

#void snd_pcm_info_set_subdevice(snd_pcm_info_t *obj, unsigned int val);
snd_pcm_info_set_subdevice = _alsa_lib.snd_pcm_info_set_subdevice
snd_pcm_info_set_subdevice.argtypes = [POINTER(snd_pcm_info_t), c_uint]
snd_pcm_info_set_subdevice.restype = None

#void snd_pcm_info_set_stream(snd_pcm_info_t *obj, snd_pcm_stream_t val);
snd_pcm_info_set_stream = _alsa_lib.snd_pcm_info_set_stream
snd_pcm_info_set_stream.argtypes = [POINTER(snd_pcm_info_t), snd_pcm_stream_t]
snd_pcm_info_set_stream.restype = None


# \} 

#
# \defgroup PCM_HW_Params Hardware Parameters
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#int snd_pcm_hw_params_any(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params_any = _alsa_lib.snd_pcm_hw_params_any
snd_pcm_hw_params_any.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_any.restype = c_int

#int snd_pcm_hw_params_can_mmap_sample_resolution(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_can_mmap_sample_resolution = _alsa_lib.snd_pcm_hw_params_can_mmap_sample_resolution
snd_pcm_hw_params_can_mmap_sample_resolution.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_can_mmap_sample_resolution.restype = c_int

#int snd_pcm_hw_params_is_double(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_double = _alsa_lib.snd_pcm_hw_params_is_double
snd_pcm_hw_params_is_double.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_double.restype = c_int

#int snd_pcm_hw_params_is_batch(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_batch = _alsa_lib.snd_pcm_hw_params_is_batch
snd_pcm_hw_params_is_batch.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_batch.restype = c_int

#int snd_pcm_hw_params_is_block_transfer(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_block_transfer = _alsa_lib.snd_pcm_hw_params_is_block_transfer
snd_pcm_hw_params_is_block_transfer.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_block_transfer.restype = c_int

#int snd_pcm_hw_params_is_monotonic(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_monotonic = _alsa_lib.snd_pcm_hw_params_is_monotonic
snd_pcm_hw_params_is_monotonic.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_monotonic.restype = c_int

#int snd_pcm_hw_params_can_overrange(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_can_overrange = _alsa_lib.snd_pcm_hw_params_can_overrange
snd_pcm_hw_params_can_overrange.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_can_overrange.restype = c_int

#int snd_pcm_hw_params_can_pause(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_can_pause = _alsa_lib.snd_pcm_hw_params_can_pause
snd_pcm_hw_params_can_pause.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_can_pause.restype = c_int

#int snd_pcm_hw_params_can_resume(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_can_resume = _alsa_lib.snd_pcm_hw_params_can_resume
snd_pcm_hw_params_can_resume.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_can_resume.restype = c_int

#int snd_pcm_hw_params_is_half_duplex(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_half_duplex = _alsa_lib.snd_pcm_hw_params_is_half_duplex
snd_pcm_hw_params_is_half_duplex.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_half_duplex.restype = c_int

#int snd_pcm_hw_params_is_joint_duplex(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_is_joint_duplex = _alsa_lib.snd_pcm_hw_params_is_joint_duplex
snd_pcm_hw_params_is_joint_duplex.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_is_joint_duplex.restype = c_int

#int snd_pcm_hw_params_can_sync_start(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_can_sync_start = _alsa_lib.snd_pcm_hw_params_can_sync_start
snd_pcm_hw_params_can_sync_start.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_can_sync_start.restype = c_int

#int snd_pcm_hw_params_get_rate_numden(const snd_pcm_hw_params_t *params,
					  #unsigned int *rate_num,
					  #unsigned int *rate_den);
snd_pcm_hw_params_get_rate_numden = _alsa_lib.snd_pcm_hw_params_get_rate_numden
snd_pcm_hw_params_get_rate_numden.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_uint)]
snd_pcm_hw_params_get_rate_numden.restype = c_int

#int snd_pcm_hw_params_get_sbits(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_get_sbits = _alsa_lib.snd_pcm_hw_params_get_sbits
snd_pcm_hw_params_get_sbits.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_get_sbits.restype = c_int

#int snd_pcm_hw_params_get_fifo_size(const snd_pcm_hw_params_t *params);
snd_pcm_hw_params_get_fifo_size = _alsa_lib.snd_pcm_hw_params_get_fifo_size
snd_pcm_hw_params_get_fifo_size.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_get_fifo_size.restype = c_int

#if 0
class _snd_pcm_hw_strategy(Structure):
    _fields_ = [
            ]
snd_pcm_hw_strategy_t = _snd_pcm_hw_strategy

# choices need to be sorted on ascending badness 
class _snd_pcm_hw_strategy_simple_choices_list(Structure):
    _fields_ = [
            ('value', c_uint),
            ('badness', c_uint)
            ]
snd_pcm_hw_strategy_simple_choices_list_t = _snd_pcm_hw_strategy_simple_choices_list

#int snd_pcm_hw_params_strategy(snd_pcm_t *pcm, snd_pcm_hw_params_t *params,
				   #const snd_pcm_hw_strategy_t *strategy,
				   #unsigned int badness_min,
				   #unsigned int badness_max);
#snd_pcm_hw_params_strategy = _alsa_lib.snd_pcm_hw_params_strategy
#snd_pcm_hw_params_strategy.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_hw_strategy_t), c_uint, c_uint]
#snd_pcm_hw_params_strategy.restype = c_int


#void snd_pcm_hw_strategy_free(snd_pcm_hw_strategy_t *strategy);
#snd_pcm_hw_strategy_free = _alsa_lib.snd_pcm_hw_strategy_free
#snd_pcm_hw_strategy_free.argtypes = [POINTER(snd_pcm_hw_strategy)]
#snd_pcm_hw_strategy_free.restype = None

#int snd_pcm_hw_strategy_simple(snd_pcm_hw_strategy_t **strategyp,
				   #unsigned int badness_min,
				   #unsigned int badness_max);
#snd_pcm_hw_strategy_simple = _alsa_lib.snd_pcm_hw_strategy_simple
#snd_pcm_hw_strategy_simple.argtypes = [POINTER(POINTER(snd_pcm_hw_strategy_t)), c_uint, c_uint]
#snd_pcm_hw_strategy_simple.restype = c_int


class _snd_output(Structure):
    _fields_ = [
            ]
snd_output_t = _snd_output

#int snd_pcm_hw_params_try_explain_failure(snd_pcm_t *pcm,
					  #snd_pcm_hw_params_t *fail,
					  #snd_pcm_hw_params_t *success,
					  #unsigned int depth,
					  #snd_output_t *out);
#snd_pcm_hw_params_try_explain_failure = _alsa_lib.snd_pcm_hw_params_try_explain_failure
#snd_pcm_hw_params_try_explain_failure.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_hw_params_t), c_uint, POINTER(snd_output_t)]
#snd_pcm_hw_params_try_explain_failure.restype = c_int

#endif

#size_t snd_pcm_hw_params_sizeof(void);
snd_pcm_hw_params_sizeof = _alsa_lib.snd_pcm_hw_params_sizeof
snd_pcm_hw_params_sizeof.argtypes = []
snd_pcm_hw_params_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_pcm_hw_params_t using standard alloca
# \param ptr returned pointer
#
#int snd_pcm_hw_params_malloc(snd_pcm_hw_params_t **ptr);
snd_pcm_hw_params_malloc = _alsa_lib.snd_pcm_hw_params_malloc
snd_pcm_hw_params_malloc.argtypes = [POINTER(POINTER(snd_pcm_hw_params_t))]
snd_pcm_hw_params_malloc.restype = c_int

#void snd_pcm_hw_params_free(snd_pcm_hw_params_t *obj);
snd_pcm_hw_params_free = _alsa_lib.snd_pcm_hw_params_free
snd_pcm_hw_params_free.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_free.restype = None

#void snd_pcm_hw_params_copy(snd_pcm_hw_params_t *dst, const snd_pcm_hw_params_t *src);
snd_pcm_hw_params_copy = _alsa_lib.snd_pcm_hw_params_copy
snd_pcm_hw_params_copy.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_copy.restype = None


#if !defined(ALSA_LIBRARY_BUILD) && !defined(ALSA_PCM_OLD_HW_PARAMS_API)

#int snd_pcm_hw_params_get_access(const snd_pcm_hw_params_t *params, snd_pcm_access_t *_access);
snd_pcm_hw_params_get_access = _alsa_lib.snd_pcm_hw_params_get_access
snd_pcm_hw_params_get_access.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_access_t)]
snd_pcm_hw_params_get_access.restype = c_int

#int snd_pcm_hw_params_test_access(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_t _access);
snd_pcm_hw_params_test_access = _alsa_lib.snd_pcm_hw_params_test_access
snd_pcm_hw_params_test_access.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_access_t]
snd_pcm_hw_params_test_access.restype = c_int

#int snd_pcm_hw_params_set_access(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_t _access);
snd_pcm_hw_params_set_access = _alsa_lib.snd_pcm_hw_params_set_access
snd_pcm_hw_params_set_access.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_access_t]
snd_pcm_hw_params_set_access.restype = c_int

#int snd_pcm_hw_params_set_access_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_t *_access);
snd_pcm_hw_params_set_access_first = _alsa_lib.snd_pcm_hw_params_set_access_first
snd_pcm_hw_params_set_access_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_access_t)]
snd_pcm_hw_params_set_access_first.restype = c_int

#int snd_pcm_hw_params_set_access_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_t *_access);
snd_pcm_hw_params_set_access_last = _alsa_lib.snd_pcm_hw_params_set_access_last
snd_pcm_hw_params_set_access_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_access_t)]
snd_pcm_hw_params_set_access_last.restype = c_int

#int snd_pcm_hw_params_set_access_mask(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_mask_t *mask);
snd_pcm_hw_params_set_access_mask = _alsa_lib.snd_pcm_hw_params_set_access_mask
snd_pcm_hw_params_set_access_mask.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_access_mask_t)]
snd_pcm_hw_params_set_access_mask.restype = c_int

#int snd_pcm_hw_params_get_access_mask(snd_pcm_hw_params_t *params, snd_pcm_access_mask_t *mask);
snd_pcm_hw_params_get_access_mask = _alsa_lib.snd_pcm_hw_params_get_access_mask
snd_pcm_hw_params_get_access_mask.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_access_mask_t)]
snd_pcm_hw_params_get_access_mask.restype = c_int


#int snd_pcm_hw_params_get_format(const snd_pcm_hw_params_t *params, snd_pcm_format_t *val);
snd_pcm_hw_params_get_format = _alsa_lib.snd_pcm_hw_params_get_format
snd_pcm_hw_params_get_format.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_format_t)]
snd_pcm_hw_params_get_format.restype = c_int

#int snd_pcm_hw_params_test_format(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_t val);
snd_pcm_hw_params_test_format = _alsa_lib.snd_pcm_hw_params_test_format
snd_pcm_hw_params_test_format.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_format_t]
snd_pcm_hw_params_test_format.restype = c_int

#int snd_pcm_hw_params_set_format(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_t val);
snd_pcm_hw_params_set_format = _alsa_lib.snd_pcm_hw_params_set_format
snd_pcm_hw_params_set_format.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_format_t]
snd_pcm_hw_params_set_format.restype = c_int

#int snd_pcm_hw_params_set_format_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_t *format);
snd_pcm_hw_params_set_format_first = _alsa_lib.snd_pcm_hw_params_set_format_first
snd_pcm_hw_params_set_format_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_format_t)]
snd_pcm_hw_params_set_format_first.restype = c_int

#int snd_pcm_hw_params_set_format_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_t *format);
snd_pcm_hw_params_set_format_last = _alsa_lib.snd_pcm_hw_params_set_format_last
snd_pcm_hw_params_set_format_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_format_t)]
snd_pcm_hw_params_set_format_last.restype = c_int

#int snd_pcm_hw_params_set_format_mask(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_mask_t *mask);
snd_pcm_hw_params_set_format_mask = _alsa_lib.snd_pcm_hw_params_set_format_mask
snd_pcm_hw_params_set_format_mask.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_format_mask_t)]
snd_pcm_hw_params_set_format_mask.restype = c_int

#void snd_pcm_hw_params_get_format_mask(snd_pcm_hw_params_t *params, snd_pcm_format_mask_t *mask);
snd_pcm_hw_params_get_format_mask = _alsa_lib.snd_pcm_hw_params_get_format_mask
snd_pcm_hw_params_get_format_mask.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_format_mask_t)]
snd_pcm_hw_params_get_format_mask.restype = None


#int snd_pcm_hw_params_get_subformat(const snd_pcm_hw_params_t *params, snd_pcm_subformat_t *subformat);
snd_pcm_hw_params_get_subformat = _alsa_lib.snd_pcm_hw_params_get_subformat
snd_pcm_hw_params_get_subformat.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_subformat_t)]
snd_pcm_hw_params_get_subformat.restype = c_int

#int snd_pcm_hw_params_test_subformat(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_subformat_t subformat);
snd_pcm_hw_params_test_subformat = _alsa_lib.snd_pcm_hw_params_test_subformat
snd_pcm_hw_params_test_subformat.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_subformat_t]
snd_pcm_hw_params_test_subformat.restype = c_int

#int snd_pcm_hw_params_set_subformat(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_subformat_t subformat);
snd_pcm_hw_params_set_subformat = _alsa_lib.snd_pcm_hw_params_set_subformat
snd_pcm_hw_params_set_subformat.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_subformat_t]
snd_pcm_hw_params_set_subformat.restype = c_int

#int snd_pcm_hw_params_set_subformat_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_subformat_t *subformat);
snd_pcm_hw_params_set_subformat_first = _alsa_lib.snd_pcm_hw_params_set_subformat_first
snd_pcm_hw_params_set_subformat_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_subformat_t)]
snd_pcm_hw_params_set_subformat_first.restype = c_int

#int snd_pcm_hw_params_set_subformat_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_subformat_t *subformat);
snd_pcm_hw_params_set_subformat_last = _alsa_lib.snd_pcm_hw_params_set_subformat_last
snd_pcm_hw_params_set_subformat_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_subformat_t)]
snd_pcm_hw_params_set_subformat_last.restype = c_int

#int snd_pcm_hw_params_set_subformat_mask(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_subformat_mask_t *mask);
snd_pcm_hw_params_set_subformat_mask = _alsa_lib.snd_pcm_hw_params_set_subformat_mask
snd_pcm_hw_params_set_subformat_mask.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_hw_params_set_subformat_mask.restype = c_int

#void snd_pcm_hw_params_get_subformat_mask(snd_pcm_hw_params_t *params, snd_pcm_subformat_mask_t *mask);
snd_pcm_hw_params_get_subformat_mask = _alsa_lib.snd_pcm_hw_params_get_subformat_mask
snd_pcm_hw_params_get_subformat_mask.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_hw_params_get_subformat_mask.restype = None


#int snd_pcm_hw_params_get_channels(const snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_get_channels = _alsa_lib.snd_pcm_hw_params_get_channels
snd_pcm_hw_params_get_channels.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_get_channels.restype = c_int

#int snd_pcm_hw_params_get_channels_min(const snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_get_channels_min = _alsa_lib.snd_pcm_hw_params_get_channels_min
snd_pcm_hw_params_get_channels_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_get_channels_min.restype = c_int

#int snd_pcm_hw_params_get_channels_max(const snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_get_channels_max = _alsa_lib.snd_pcm_hw_params_get_channels_max
snd_pcm_hw_params_get_channels_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_get_channels_max.restype = c_int

#int snd_pcm_hw_params_test_channels(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val);
snd_pcm_hw_params_test_channels = _alsa_lib.snd_pcm_hw_params_test_channels
snd_pcm_hw_params_test_channels.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint]
snd_pcm_hw_params_test_channels.restype = c_int

#int snd_pcm_hw_params_set_channels(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val);
snd_pcm_hw_params_set_channels = _alsa_lib.snd_pcm_hw_params_set_channels
snd_pcm_hw_params_set_channels.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint]
snd_pcm_hw_params_set_channels.restype = c_int

#int snd_pcm_hw_params_set_channels_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_set_channels_min = _alsa_lib.snd_pcm_hw_params_set_channels_min
snd_pcm_hw_params_set_channels_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_set_channels_min.restype = c_int

#int snd_pcm_hw_params_set_channels_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_set_channels_max = _alsa_lib.snd_pcm_hw_params_set_channels_max
snd_pcm_hw_params_set_channels_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t),  POINTER(c_uint)]
snd_pcm_hw_params_set_channels_max.restype = c_int

#int snd_pcm_hw_params_set_channels_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, unsigned int *max);
snd_pcm_hw_params_set_channels_minmax = _alsa_lib.snd_pcm_hw_params_set_channels_minmax
snd_pcm_hw_params_set_channels_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_uint)]
snd_pcm_hw_params_set_channels_minmax.restype = c_int

#int snd_pcm_hw_params_set_channels_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_set_channels_near = _alsa_lib.snd_pcm_hw_params_set_channels_near
snd_pcm_hw_params_set_channels_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_set_channels_near.restype = c_int

#int snd_pcm_hw_params_set_channels_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_set_channels_first = _alsa_lib.snd_pcm_hw_params_set_channels_first
snd_pcm_hw_params_set_channels_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_set_channels_first.restype = c_int

#int snd_pcm_hw_params_set_channels_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_set_channels_last = _alsa_lib.snd_pcm_hw_params_set_channels_last
snd_pcm_hw_params_set_channels_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_set_channels_last.restype = c_int


#int snd_pcm_hw_params_get_rate(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_rate = _alsa_lib.snd_pcm_hw_params_get_rate
snd_pcm_hw_params_get_rate.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_rate.restype = c_int

#int snd_pcm_hw_params_get_rate_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_rate_min = _alsa_lib.snd_pcm_hw_params_get_rate_min
snd_pcm_hw_params_get_rate_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_rate_min.restype = c_int

#int snd_pcm_hw_params_get_rate_max(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_rate_max = _alsa_lib.snd_pcm_hw_params_get_rate_max
snd_pcm_hw_params_get_rate_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_rate_max.restype = c_int

#int snd_pcm_hw_params_test_rate(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_test_rate = _alsa_lib.snd_pcm_hw_params_test_rate
snd_pcm_hw_params_test_rate.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_test_rate.restype = c_int

#int snd_pcm_hw_params_set_rate(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_set_rate = _alsa_lib.snd_pcm_hw_params_set_rate
snd_pcm_hw_params_set_rate.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_rate.restype = c_int

#int snd_pcm_hw_params_set_rate_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_min = _alsa_lib.snd_pcm_hw_params_set_rate_min
snd_pcm_hw_params_set_rate_min.argtypes = [POINTER(snd_pcm_t),  POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_min.restype = c_int

#int snd_pcm_hw_params_set_rate_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_max = _alsa_lib.snd_pcm_hw_params_set_rate_max
snd_pcm_hw_params_set_rate_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_max.restype = c_int

#int snd_pcm_hw_params_set_rate_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, int *mindir, unsigned int *max, int *maxdir);
snd_pcm_hw_params_set_rate_minmax = _alsa_lib.snd_pcm_hw_params_set_rate_minmax
snd_pcm_hw_params_set_rate_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_minmax.restype = c_int

#int snd_pcm_hw_params_set_rate_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_near = _alsa_lib.snd_pcm_hw_params_set_rate_near
snd_pcm_hw_params_set_rate_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_near.restype = c_int

#int snd_pcm_hw_params_set_rate_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_first = _alsa_lib.snd_pcm_hw_params_set_rate_first
snd_pcm_hw_params_set_rate_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_first.restype = c_int

#int snd_pcm_hw_params_set_rate_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_last = _alsa_lib.snd_pcm_hw_params_set_rate_last
snd_pcm_hw_params_set_rate_last.argtypes = [POINTER(snd_pcm_t),  POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_last.restype = c_int

#int snd_pcm_hw_params_set_rate_resample(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val);
snd_pcm_hw_params_set_rate_resample = _alsa_lib.snd_pcm_hw_params_set_rate_resample
snd_pcm_hw_params_set_rate_resample.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint]
snd_pcm_hw_params_set_rate_resample.restype = c_int

#int snd_pcm_hw_params_get_rate_resample(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_get_rate_resample = _alsa_lib.snd_pcm_hw_params_get_rate_resample
snd_pcm_hw_params_get_rate_resample.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_get_rate_resample.restype = c_int

#int snd_pcm_hw_params_set_export_buffer(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val);
snd_pcm_hw_params_set_export_buffer = _alsa_lib.snd_pcm_hw_params_set_export_buffer
snd_pcm_hw_params_set_export_buffer.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint]
snd_pcm_hw_params_set_export_buffer.restype = c_int

#int snd_pcm_hw_params_get_export_buffer(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val);
snd_pcm_hw_params_get_export_buffer = _alsa_lib.snd_pcm_hw_params_get_export_buffer
snd_pcm_hw_params_get_export_buffer.argtypes = [POINTER(snd_pcm_t),  POINTER(snd_pcm_hw_params_t), POINTER(c_uint)]
snd_pcm_hw_params_get_export_buffer.restype = c_int


#int snd_pcm_hw_params_get_period_time(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_period_time = _alsa_lib.snd_pcm_hw_params_get_period_time
snd_pcm_hw_params_get_period_time.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_period_time.restype = c_int

#int snd_pcm_hw_params_get_period_time_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_period_time_min = _alsa_lib.snd_pcm_hw_params_get_period_time_min
snd_pcm_hw_params_get_period_time_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_period_time_min.restype = c_int

#int snd_pcm_hw_params_get_period_time_max(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_period_time_max = _alsa_lib.snd_pcm_hw_params_get_period_time_max
snd_pcm_hw_params_get_period_time_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_period_time_max.restype = c_int

#int snd_pcm_hw_params_test_period_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_test_period_time = _alsa_lib.snd_pcm_hw_params_test_period_time
snd_pcm_hw_params_test_period_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_test_period_time.restype = c_int

#int snd_pcm_hw_params_set_period_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_set_period_time = _alsa_lib.snd_pcm_hw_params_set_period_time
snd_pcm_hw_params_set_period_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_period_time.restype = c_int

#int snd_pcm_hw_params_set_period_time_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_period_time_min = _alsa_lib.snd_pcm_hw_params_set_period_time_min
snd_pcm_hw_params_set_period_time_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_min.restype = c_int

#int snd_pcm_hw_params_set_period_time_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_period_time_max = _alsa_lib.snd_pcm_hw_params_set_period_time_max
snd_pcm_hw_params_set_period_time_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t),  POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_max.restype = c_int

#int snd_pcm_hw_params_set_period_time_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, int *mindir, unsigned int *max, int *maxdir);
snd_pcm_hw_params_set_period_time_minmax = _alsa_lib.snd_pcm_hw_params_set_period_time_minmax
snd_pcm_hw_params_set_period_time_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_minmax.restype = c_int

#int snd_pcm_hw_params_set_period_time_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_period_time_near = _alsa_lib.snd_pcm_hw_params_set_period_time_near
snd_pcm_hw_params_set_period_time_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_near.restype = c_int

#int snd_pcm_hw_params_set_period_time_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_period_time_first = _alsa_lib.snd_pcm_hw_params_set_period_time_first
snd_pcm_hw_params_set_period_time_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t),  POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_first.restype = c_int

#int snd_pcm_hw_params_set_period_time_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_period_time_last = _alsa_lib.snd_pcm_hw_params_set_period_time_last
snd_pcm_hw_params_set_period_time_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_period_time_last.restype = c_int


#int snd_pcm_hw_params_get_period_size(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *frames, int *dir);
snd_pcm_hw_params_get_period_size = _alsa_lib.snd_pcm_hw_params_get_period_size
snd_pcm_hw_params_get_period_size.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_get_period_size.restype = c_int

#int snd_pcm_hw_params_get_period_size_min(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *frames, int *dir);
snd_pcm_hw_params_get_period_size_min = _alsa_lib.snd_pcm_hw_params_get_period_size_min
snd_pcm_hw_params_get_period_size_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_get_period_size_min.restype = c_int

#int snd_pcm_hw_params_get_period_size_max(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *frames, int *dir);
snd_pcm_hw_params_get_period_size_max = _alsa_lib.snd_pcm_hw_params_get_period_size_max
snd_pcm_hw_params_get_period_size_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_get_period_size_max.restype = c_int

#int snd_pcm_hw_params_test_period_size(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t val, int dir);
snd_pcm_hw_params_test_period_size = _alsa_lib.snd_pcm_hw_params_test_period_size
snd_pcm_hw_params_test_period_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_uframes_t, c_int]
snd_pcm_hw_params_test_period_size.restype = c_int

#int snd_pcm_hw_params_set_period_size(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t val, int dir);
snd_pcm_hw_params_set_period_size = _alsa_lib.snd_pcm_hw_params_set_period_size
snd_pcm_hw_params_set_period_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_uframes_t, c_int]
snd_pcm_hw_params_set_period_size.restype = c_int

#int snd_pcm_hw_params_set_period_size_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val, int *dir);
snd_pcm_hw_params_set_period_size_min = _alsa_lib.snd_pcm_hw_params_set_period_size_min
snd_pcm_hw_params_set_period_size_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_min.restype = c_int

#int snd_pcm_hw_params_set_period_size_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val, int *dir);
snd_pcm_hw_params_set_period_size_max = _alsa_lib.snd_pcm_hw_params_set_period_size_max
snd_pcm_hw_params_set_period_size_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_max.restype = c_int

#int snd_pcm_hw_params_set_period_size_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *min, int *mindir, snd_pcm_uframes_t *max, int *maxdir);
snd_pcm_hw_params_set_period_size_minmax = _alsa_lib.snd_pcm_hw_params_set_period_size_minmax
snd_pcm_hw_params_set_period_size_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_minmax.restype = c_int

#int snd_pcm_hw_params_set_period_size_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val, int *dir);
snd_pcm_hw_params_set_period_size_near = _alsa_lib.snd_pcm_hw_params_set_period_size_near
snd_pcm_hw_params_set_period_size_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_near.restype = c_int

#int snd_pcm_hw_params_set_period_size_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val, int *dir);
snd_pcm_hw_params_set_period_size_first = _alsa_lib.snd_pcm_hw_params_set_period_size_first
snd_pcm_hw_params_set_period_size_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_first.restype = c_int

#int snd_pcm_hw_params_set_period_size_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val, int *dir);
snd_pcm_hw_params_set_period_size_last = _alsa_lib.snd_pcm_hw_params_set_period_size_last
snd_pcm_hw_params_set_period_size_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_set_period_size_last.restype = c_int

#int snd_pcm_hw_params_set_period_size_integer(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params_set_period_size_integer = _alsa_lib.snd_pcm_hw_params_set_period_size_integer
snd_pcm_hw_params_set_period_size_integer.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_set_period_size_integer.restype = c_int


#int snd_pcm_hw_params_get_periods(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_periods = _alsa_lib.snd_pcm_hw_params_get_periods
snd_pcm_hw_params_get_periods.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_periods.restype = c_int

#int snd_pcm_hw_params_get_periods_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_periods_min = _alsa_lib.snd_pcm_hw_params_get_periods_min
snd_pcm_hw_params_get_periods_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_periods_min.restype = c_int

#int snd_pcm_hw_params_get_periods_max(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_periods_max = _alsa_lib.snd_pcm_hw_params_get_periods_max
snd_pcm_hw_params_get_periods_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_periods_max.restype = c_int

#int snd_pcm_hw_params_test_periods(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_test_periods = _alsa_lib.snd_pcm_hw_params_test_periods
snd_pcm_hw_params_test_periods.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_test_periods.restype = c_int

#int snd_pcm_hw_params_set_periods(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_set_periods = _alsa_lib.snd_pcm_hw_params_set_periods
snd_pcm_hw_params_set_periods.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_periods.restype = c_int

#int snd_pcm_hw_params_set_periods_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_periods_min = _alsa_lib.snd_pcm_hw_params_set_periods_min
snd_pcm_hw_params_set_periods_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_min.restype = c_int

#int snd_pcm_hw_params_set_periods_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_periods_max = _alsa_lib.snd_pcm_hw_params_set_periods_max
snd_pcm_hw_params_set_periods_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_max.restype = c_int

#int snd_pcm_hw_params_set_periods_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, int *mindir, unsigned int *max, int *maxdir);
snd_pcm_hw_params_set_periods_minmax = _alsa_lib.snd_pcm_hw_params_set_periods_minmax
snd_pcm_hw_params_set_periods_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_minmax.restype = c_int

#int snd_pcm_hw_params_set_periods_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_periods_near = _alsa_lib.snd_pcm_hw_params_set_periods_near
snd_pcm_hw_params_set_periods_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_near.restype = c_int

#int snd_pcm_hw_params_set_periods_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_periods_first = _alsa_lib.snd_pcm_hw_params_set_periods_first
snd_pcm_hw_params_set_periods_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_first.restype = c_int

#int snd_pcm_hw_params_set_periods_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_periods_last = _alsa_lib.snd_pcm_hw_params_set_periods_last
snd_pcm_hw_params_set_periods_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_periods_last.restype = c_int

#int snd_pcm_hw_params_set_periods_integer(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params_set_periods_integer = _alsa_lib.snd_pcm_hw_params_set_periods_integer
snd_pcm_hw_params_set_periods_integer.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_set_periods_integer.restype = c_int


#int snd_pcm_hw_params_get_buffer_time(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_buffer_time = _alsa_lib.snd_pcm_hw_params_get_buffer_time
snd_pcm_hw_params_get_buffer_time.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_buffer_time.restype = c_int

#int snd_pcm_hw_params_get_buffer_time_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_buffer_time_min = _alsa_lib.snd_pcm_hw_params_get_buffer_time_min
snd_pcm_hw_params_get_buffer_time_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_buffer_time_min.restype = c_int

#int snd_pcm_hw_params_get_buffer_time_max(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_get_buffer_time_max = _alsa_lib.snd_pcm_hw_params_get_buffer_time_max
snd_pcm_hw_params_get_buffer_time_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_buffer_time_max.restype = c_int

#int snd_pcm_hw_params_test_buffer_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_test_buffer_time = _alsa_lib.snd_pcm_hw_params_test_buffer_time
snd_pcm_hw_params_test_buffer_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_test_buffer_time.restype = c_int

#int snd_pcm_hw_params_set_buffer_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_set_buffer_time = _alsa_lib.snd_pcm_hw_params_set_buffer_time
snd_pcm_hw_params_set_buffer_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_buffer_time.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_buffer_time_min = _alsa_lib.snd_pcm_hw_params_set_buffer_time_min
snd_pcm_hw_params_set_buffer_time_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_min.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_buffer_time_max = _alsa_lib.snd_pcm_hw_params_set_buffer_time_max
snd_pcm_hw_params_set_buffer_time_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_max.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, int *mindir, unsigned int *max, int *maxdir);
snd_pcm_hw_params_set_buffer_time_minmax = _alsa_lib.snd_pcm_hw_params_set_buffer_time_minmax
snd_pcm_hw_params_set_buffer_time_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_minmax.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_buffer_time_near = _alsa_lib.snd_pcm_hw_params_set_buffer_time_near
snd_pcm_hw_params_set_buffer_time_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_near.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_buffer_time_first = _alsa_lib.snd_pcm_hw_params_set_buffer_time_first
snd_pcm_hw_params_set_buffer_time_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_first.restype = c_int

#int snd_pcm_hw_params_set_buffer_time_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_buffer_time_last = _alsa_lib.snd_pcm_hw_params_set_buffer_time_last
snd_pcm_hw_params_set_buffer_time_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_buffer_time_last.restype = c_int


#int snd_pcm_hw_params_get_buffer_size(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_get_buffer_size = _alsa_lib.snd_pcm_hw_params_get_buffer_size
snd_pcm_hw_params_get_buffer_size.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_get_buffer_size.restype = c_int

#int snd_pcm_hw_params_get_buffer_size_min(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_get_buffer_size_min = _alsa_lib.snd_pcm_hw_params_get_buffer_size_min
snd_pcm_hw_params_get_buffer_size_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_get_buffer_size_min.restype = c_int

#int snd_pcm_hw_params_get_buffer_size_max(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_get_buffer_size_max = _alsa_lib.snd_pcm_hw_params_get_buffer_size_max
snd_pcm_hw_params_get_buffer_size_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_get_buffer_size_max.restype = c_int

#int snd_pcm_hw_params_test_buffer_size(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_hw_params_test_buffer_size = _alsa_lib.snd_pcm_hw_params_test_buffer_size
snd_pcm_hw_params_test_buffer_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_uframes_t]
snd_pcm_hw_params_test_buffer_size.restype = c_int

#int snd_pcm_hw_params_set_buffer_size(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_hw_params_set_buffer_size = _alsa_lib.snd_pcm_hw_params_set_buffer_size
snd_pcm_hw_params_set_buffer_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_uframes_t]
snd_pcm_hw_params_set_buffer_size.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_set_buffer_size_min = _alsa_lib.snd_pcm_hw_params_set_buffer_size_min
snd_pcm_hw_params_set_buffer_size_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_min.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_set_buffer_size_max = _alsa_lib.snd_pcm_hw_params_set_buffer_size_max
snd_pcm_hw_params_set_buffer_size_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_max.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *min, snd_pcm_uframes_t *max);
snd_pcm_hw_params_set_buffer_size_minmax = _alsa_lib.snd_pcm_hw_params_set_buffer_size_minmax
snd_pcm_hw_params_set_buffer_size_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_minmax.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_set_buffer_size_near = _alsa_lib.snd_pcm_hw_params_set_buffer_size_near
snd_pcm_hw_params_set_buffer_size_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_near.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_set_buffer_size_first = _alsa_lib.snd_pcm_hw_params_set_buffer_size_first
snd_pcm_hw_params_set_buffer_size_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_first.restype = c_int

#int snd_pcm_hw_params_set_buffer_size_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_set_buffer_size_last = _alsa_lib.snd_pcm_hw_params_set_buffer_size_last
snd_pcm_hw_params_set_buffer_size_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_set_buffer_size_last.restype = c_int


#endif  !ALSA_LIBRARY_BUILD && !ALSA_PCM_OLD_HW_PARAMS_API 

#int snd_pcm_hw_params_get_min_align(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_hw_params_get_min_align = _alsa_lib.snd_pcm_hw_params_get_min_align
snd_pcm_hw_params_get_min_align.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_hw_params_get_min_align.restype = c_int


# \} 

#
# \defgroup PCM_SW_Params Software Parameters
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_sw_params_sizeof(void);
snd_pcm_sw_params_sizeof = _alsa_lib.snd_pcm_sw_params_sizeof
snd_pcm_sw_params_sizeof.argtypes = []
snd_pcm_sw_params_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_pcm_sw_params_t using standard alloca
# \param ptr returned pointer
#
#define snd_pcm_sw_params_alloca(ptr) __snd_alloca(ptr, snd_pcm_sw_params)
#int snd_pcm_sw_params_malloc(snd_pcm_sw_params_t **ptr);
snd_pcm_sw_params_malloc = _alsa_lib.snd_pcm_sw_params_malloc
snd_pcm_sw_params_malloc.argtypes = [POINTER(POINTER(snd_pcm_sw_params_t))]
snd_pcm_sw_params_malloc.restype = c_int

#void snd_pcm_sw_params_free(snd_pcm_sw_params_t *obj);
snd_pcm_sw_params_free = _alsa_lib.snd_pcm_sw_params_free
snd_pcm_sw_params_free.argtypes = [POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params_free.restype = None

#void snd_pcm_sw_params_copy(snd_pcm_sw_params_t *dst, const snd_pcm_sw_params_t *src);
snd_pcm_sw_params_copy = _alsa_lib.snd_pcm_sw_params_copy
snd_pcm_sw_params_copy.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params_copy.restype = None

#int snd_pcm_sw_params_get_boundary(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_boundary = _alsa_lib.snd_pcm_sw_params_get_boundary
snd_pcm_sw_params_get_boundary.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_boundary.restype = c_int


#if !defined(ALSA_LIBRARY_BUILD) && !defined(ALSA_PCM_OLD_SW_PARAMS_API)

#int snd_pcm_sw_params_set_tstamp_mode(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_tstamp_t val);
snd_pcm_sw_params_set_tstamp_mode = _alsa_lib.snd_pcm_sw_params_set_tstamp_mode
snd_pcm_sw_params_set_tstamp_mode.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_tstamp_t]
snd_pcm_sw_params_set_tstamp_mode.restype = c_int

#int snd_pcm_sw_params_get_tstamp_mode(const snd_pcm_sw_params_t *params, snd_pcm_tstamp_t *val);
snd_pcm_sw_params_get_tstamp_mode = _alsa_lib.snd_pcm_sw_params_get_tstamp_mode
snd_pcm_sw_params_get_tstamp_mode.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_tstamp_t)]
snd_pcm_sw_params_get_tstamp_mode.restype = c_int

#int snd_pcm_sw_params_set_avail_min(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_sw_params_set_avail_min = _alsa_lib.snd_pcm_sw_params_set_avail_min
snd_pcm_sw_params_set_avail_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_avail_min.restype = c_int

#int snd_pcm_sw_params_get_avail_min(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_avail_min = _alsa_lib.snd_pcm_sw_params_get_avail_min
snd_pcm_sw_params_get_avail_min.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_avail_min.restype = c_int

#int snd_pcm_sw_params_set_period_event(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, int val);
snd_pcm_sw_params_set_period_event = _alsa_lib.snd_pcm_sw_params_set_period_event
snd_pcm_sw_params_set_period_event.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), c_int]
snd_pcm_sw_params_set_period_event.restype = c_int

#int snd_pcm_sw_params_get_period_event(const snd_pcm_sw_params_t *params, int *val);
snd_pcm_sw_params_get_period_event = _alsa_lib.snd_pcm_sw_params_get_period_event
snd_pcm_sw_params_get_period_event.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(c_int)]
snd_pcm_sw_params_get_period_event.restype = c_int

#int snd_pcm_sw_params_set_start_threshold(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_sw_params_set_start_threshold = _alsa_lib.snd_pcm_sw_params_set_start_threshold
snd_pcm_sw_params_set_start_threshold.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_start_threshold.restype = c_int

#int snd_pcm_sw_params_get_start_threshold(const snd_pcm_sw_params_t *paramsm, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_start_threshold = _alsa_lib.snd_pcm_sw_params_get_start_threshold
snd_pcm_sw_params_get_start_threshold.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_start_threshold.restype = c_int

#int snd_pcm_sw_params_set_stop_threshold(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_sw_params_set_stop_threshold = _alsa_lib.snd_pcm_sw_params_set_stop_threshold
snd_pcm_sw_params_set_stop_threshold.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_stop_threshold.restype = c_int

#int snd_pcm_sw_params_get_stop_threshold(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_stop_threshold = _alsa_lib.snd_pcm_sw_params_get_stop_threshold
snd_pcm_sw_params_get_stop_threshold.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_stop_threshold.restype = c_int

#int snd_pcm_sw_params_set_silence_threshold(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_sw_params_set_silence_threshold = _alsa_lib.snd_pcm_sw_params_set_silence_threshold
snd_pcm_sw_params_set_silence_threshold.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_silence_threshold.restype = c_int

#int snd_pcm_sw_params_get_silence_threshold(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_silence_threshold = _alsa_lib.snd_pcm_sw_params_get_silence_threshold
snd_pcm_sw_params_get_silence_threshold.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_silence_threshold.restype = c_int

#int snd_pcm_sw_params_set_silence_size(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val);
snd_pcm_sw_params_set_silence_size = _alsa_lib.snd_pcm_sw_params_set_silence_size
snd_pcm_sw_params_set_silence_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_silence_size.restype = c_int

#int snd_pcm_sw_params_get_silence_size(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val);
snd_pcm_sw_params_get_silence_size = _alsa_lib.snd_pcm_sw_params_get_silence_size
snd_pcm_sw_params_get_silence_size.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_silence_size.restype = c_int


#endif  !ALSA_LIBRARY_BUILD && !ALSA_PCM_OLD_SW_PARAMS_API 

# \} 

# include old API 
#ifndef ALSA_LIBRARY_BUILD
#if defined(ALSA_PCM_OLD_HW_PARAMS_API) || defined(ALSA_PCM_OLD_SW_PARAMS_API)
#include "pcm_old.h"
#endif
#endif

#
# \defgroup PCM_Access Access Mask Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_access_mask_sizeof(void);
snd_pcm_access_mask_sizeof = _alsa_lib.snd_pcm_access_mask_sizeof
snd_pcm_access_mask_sizeof.argtypes = []
snd_pcm_access_mask_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an empty #snd_pcm_access_mask_t using standard alloca
# \param ptr returned pointer
#
#define snd_pcm_access_mask_alloca(ptr) __snd_alloca(ptr, snd_pcm_access_mask)
#int snd_pcm_access_mask_malloc(snd_pcm_access_mask_t **ptr);
snd_pcm_access_mask_malloc = _alsa_lib.snd_pcm_access_mask_malloc
snd_pcm_access_mask_malloc.argtypes = [POINTER(POINTER(snd_pcm_access_mask_t))]
snd_pcm_access_mask_malloc.restype = c_int

#void snd_pcm_access_mask_free(snd_pcm_access_mask_t *obj);
snd_pcm_access_mask_free = _alsa_lib.snd_pcm_access_mask_free
snd_pcm_access_mask_free.argtypes = [POINTER(snd_pcm_access_mask_t)]
snd_pcm_access_mask_free.restype = None

#void snd_pcm_access_mask_copy(snd_pcm_access_mask_t *dst, const snd_pcm_access_mask_t *src);
snd_pcm_access_mask_copy = _alsa_lib.snd_pcm_access_mask_copy
snd_pcm_access_mask_copy.argtypes = [POINTER(snd_pcm_access_mask_t), POINTER(snd_pcm_access_mask_t)]
snd_pcm_access_mask_copy.restype = None

#void snd_pcm_access_mask_none(snd_pcm_access_mask_t *mask);
snd_pcm_access_mask_none = _alsa_lib.snd_pcm_access_mask_none
snd_pcm_access_mask_none.argtypes = [POINTER(snd_pcm_access_mask_t)]
snd_pcm_access_mask_none.restype = None

#void snd_pcm_access_mask_any(snd_pcm_access_mask_t *mask);
snd_pcm_access_mask_any = _alsa_lib.snd_pcm_access_mask_any
snd_pcm_access_mask_any.argtypes = [POINTER(snd_pcm_access_mask_t)]
snd_pcm_access_mask_any.restype = None

#int snd_pcm_access_mask_test(const snd_pcm_access_mask_t *mask, snd_pcm_access_t val);
snd_pcm_access_mask_test = _alsa_lib.snd_pcm_access_mask_test
snd_pcm_access_mask_test.argtypes = [POINTER(snd_pcm_access_mask_t), snd_pcm_access_t]
snd_pcm_access_mask_test.restype = c_int

#int snd_pcm_access_mask_empty(const snd_pcm_access_mask_t *mask);
snd_pcm_access_mask_empty = _alsa_lib.snd_pcm_access_mask_empty
snd_pcm_access_mask_empty.argtypes = [POINTER(snd_pcm_access_mask_t)]
snd_pcm_access_mask_empty.restype = c_int

#void snd_pcm_access_mask_set(snd_pcm_access_mask_t *mask, snd_pcm_access_t val);
snd_pcm_access_mask_set = _alsa_lib.snd_pcm_access_mask_set
snd_pcm_access_mask_set.argtypes = [POINTER(snd_pcm_access_mask_t), snd_pcm_access_t]
snd_pcm_access_mask_set.restype = None

#void snd_pcm_access_mask_reset(snd_pcm_access_mask_t *mask, snd_pcm_access_t val);
snd_pcm_access_mask_reset = _alsa_lib.snd_pcm_access_mask_reset
snd_pcm_access_mask_reset.argtypes = [POINTER(snd_pcm_access_mask_t), snd_pcm_access_t]
snd_pcm_access_mask_reset.restype = None


# \} 

#
# \defgroup PCM_Format Format Mask Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_format_mask_sizeof(void);
snd_pcm_format_mask_sizeof = _alsa_lib.snd_pcm_format_mask_sizeof
snd_pcm_format_mask_sizeof.argtypes = []
snd_pcm_format_mask_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an empty #snd_pcm_format_mask_t using standard alloca
# \param ptr returned pointer
#
#define snd_pcm_format_mask_alloca(ptr) __snd_alloca(ptr, snd_pcm_format_mask)
#int snd_pcm_format_mask_malloc(snd_pcm_format_mask_t **ptr);
snd_pcm_format_mask_malloc = _alsa_lib.snd_pcm_format_mask_malloc
snd_pcm_format_mask_malloc.argtypes = [POINTER(POINTER(snd_pcm_format_mask_t))]
snd_pcm_format_mask_malloc.restype = c_int

#void snd_pcm_format_mask_free(snd_pcm_format_mask_t *obj);
snd_pcm_format_mask_free = _alsa_lib.snd_pcm_format_mask_free
snd_pcm_format_mask_free.argtypes = [POINTER(snd_pcm_format_mask_t)]
snd_pcm_format_mask_free.restype = None

#void snd_pcm_format_mask_copy(snd_pcm_format_mask_t *dst, const snd_pcm_format_mask_t *src);
snd_pcm_format_mask_copy = _alsa_lib.snd_pcm_format_mask_copy
snd_pcm_format_mask_copy.argtypes = [POINTER(snd_pcm_format_mask_t), POINTER(snd_pcm_format_mask_t)]
snd_pcm_format_mask_copy.restype = None

#void snd_pcm_format_mask_none(snd_pcm_format_mask_t *mask);
snd_pcm_format_mask_none = _alsa_lib.snd_pcm_format_mask_none
snd_pcm_format_mask_none.argtypes = [POINTER(snd_pcm_format_mask_t)]
snd_pcm_format_mask_none.restype = None

#void snd_pcm_format_mask_any(snd_pcm_format_mask_t *mask);
snd_pcm_format_mask_any = _alsa_lib.snd_pcm_format_mask_any
snd_pcm_format_mask_any.argtypes = [POINTER(snd_pcm_format_mask_t)]
snd_pcm_format_mask_any.restype = None

#int snd_pcm_format_mask_test(const snd_pcm_format_mask_t *mask, snd_pcm_format_t val);
snd_pcm_format_mask_test = _alsa_lib.snd_pcm_format_mask_test
snd_pcm_format_mask_test.argtypes = [POINTER(snd_pcm_format_mask_t), snd_pcm_format_t]
snd_pcm_format_mask_test.restype = c_int

#int snd_pcm_format_mask_empty(const snd_pcm_format_mask_t *mask);
snd_pcm_format_mask_empty = _alsa_lib.snd_pcm_format_mask_empty
snd_pcm_format_mask_empty.argtypes = [POINTER(snd_pcm_format_mask_t)]
snd_pcm_format_mask_empty.restype = c_int

#void snd_pcm_format_mask_set(snd_pcm_format_mask_t *mask, snd_pcm_format_t val);
snd_pcm_format_mask_set = _alsa_lib.snd_pcm_format_mask_set
snd_pcm_format_mask_set.argtypes = [POINTER(snd_pcm_format_mask_t), snd_pcm_format_t]
snd_pcm_format_mask_set.restype = None

#void snd_pcm_format_mask_reset(snd_pcm_format_mask_t *mask, snd_pcm_format_t val);
snd_pcm_format_mask_reset = _alsa_lib.snd_pcm_format_mask_reset
snd_pcm_format_mask_reset.argtypes = [POINTER(snd_pcm_format_mask_t), snd_pcm_format_t]
snd_pcm_format_mask_reset.restype = None


# \} 

#
# \defgroup PCM_SubFormat Subformat Mask Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_subformat_mask_sizeof(void);
snd_pcm_subformat_mask_sizeof = _alsa_lib.snd_pcm_subformat_mask_sizeof
snd_pcm_subformat_mask_sizeof.argtypes = []
snd_pcm_subformat_mask_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an empty #snd_pcm_subformat_mask_t using standard alloca
# \param ptr returned pointer
#
#define snd_pcm_subformat_mask_alloca(ptr) __snd_alloca(ptr, snd_pcm_subformat_mask)
#int snd_pcm_subformat_mask_malloc(snd_pcm_subformat_mask_t **ptr);
snd_pcm_subformat_mask_malloc = _alsa_lib.snd_pcm_subformat_mask_malloc
snd_pcm_subformat_mask_malloc.argtypes = [POINTER(POINTER(snd_pcm_subformat_mask_t))]
snd_pcm_subformat_mask_malloc.restype = c_int

#void snd_pcm_subformat_mask_free(snd_pcm_subformat_mask_t *obj);
snd_pcm_subformat_mask_free = _alsa_lib.snd_pcm_subformat_mask_free
snd_pcm_subformat_mask_free.argtypes = [POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_subformat_mask_free.restype = None

#void snd_pcm_subformat_mask_copy(snd_pcm_subformat_mask_t *dst, const snd_pcm_subformat_mask_t *src);
snd_pcm_subformat_mask_copy = _alsa_lib.snd_pcm_subformat_mask_copy
snd_pcm_subformat_mask_copy.argtypes = [POINTER(snd_pcm_subformat_mask_t), POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_subformat_mask_copy.restype = None

#void snd_pcm_subformat_mask_none(snd_pcm_subformat_mask_t *mask);
snd_pcm_subformat_mask_none = _alsa_lib.snd_pcm_subformat_mask_none
snd_pcm_subformat_mask_none.argtypes = [POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_subformat_mask_none.restype = None

#void snd_pcm_subformat_mask_any(snd_pcm_subformat_mask_t *mask);
snd_pcm_subformat_mask_any = _alsa_lib.snd_pcm_subformat_mask_any
snd_pcm_subformat_mask_any.argtypes = [POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_subformat_mask_any.restype = None

#int snd_pcm_subformat_mask_test(const snd_pcm_subformat_mask_t *mask, snd_pcm_subformat_t val);
snd_pcm_subformat_mask_test = _alsa_lib.snd_pcm_subformat_mask_test
snd_pcm_subformat_mask_test.argtypes = [POINTER(snd_pcm_subformat_mask_t), snd_pcm_subformat_t]
snd_pcm_subformat_mask_test.restype = c_int

#int snd_pcm_subformat_mask_empty(const snd_pcm_subformat_mask_t *mask);
snd_pcm_subformat_mask_empty = _alsa_lib.snd_pcm_subformat_mask_empty
snd_pcm_subformat_mask_empty.argtypes = [POINTER(snd_pcm_subformat_mask_t)]
snd_pcm_subformat_mask_empty.restype = c_int

#void snd_pcm_subformat_mask_set(snd_pcm_subformat_mask_t *mask, snd_pcm_subformat_t val);
snd_pcm_subformat_mask_set = _alsa_lib.snd_pcm_subformat_mask_set
snd_pcm_subformat_mask_set.argtypes = [POINTER(snd_pcm_subformat_mask_t), snd_pcm_subformat_t]
snd_pcm_subformat_mask_set.restype = None

#void snd_pcm_subformat_mask_reset(snd_pcm_subformat_mask_t *mask, snd_pcm_subformat_t val);
snd_pcm_subformat_mask_reset = _alsa_lib.snd_pcm_subformat_mask_reset
snd_pcm_subformat_mask_reset.argtypes = [POINTER(snd_pcm_subformat_mask_t), snd_pcm_subformat_t]
snd_pcm_subformat_mask_reset.restype = None


# \} 

#
# \defgroup PCM_Status Status Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#size_t snd_pcm_status_sizeof(void);
snd_pcm_status_sizeof = _alsa_lib.snd_pcm_status_sizeof
snd_pcm_status_sizeof.argtypes = []
snd_pcm_status_sizeof.restype = c_size_t


# \hideinitializer
# \brief allocate an invalid #snd_pcm_status_t using standard alloca
# \param ptr returned pointer
#
#define snd_pcm_status_alloca(ptr) __snd_alloca(ptr, snd_pcm_status)
#int snd_pcm_status_malloc(snd_pcm_status_t **ptr);
snd_pcm_status_malloc = _alsa_lib.snd_pcm_status_malloc
snd_pcm_status_malloc.argtypes = [POINTER(POINTER(snd_pcm_status_t))]
snd_pcm_status_malloc.restype = c_int

#void snd_pcm_status_free(snd_pcm_status_t *obj);
snd_pcm_status_free = _alsa_lib.snd_pcm_status_free
snd_pcm_status_free.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_free.restype = None

#void snd_pcm_status_copy(snd_pcm_status_t *dst, const snd_pcm_status_t *src);
snd_pcm_status_copy = _alsa_lib.snd_pcm_status_copy
snd_pcm_status_copy.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_pcm_status_t)]
snd_pcm_status_copy.restype = None

#snd_pcm_state_t snd_pcm_status_get_state(const snd_pcm_status_t *obj);
snd_pcm_status_get_state = _alsa_lib.snd_pcm_status_get_state
snd_pcm_status_get_state.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_get_state.restype = snd_pcm_state_t

#void snd_pcm_status_get_trigger_tstamp(const snd_pcm_status_t *obj, snd_timestamp_t *ptr);
snd_pcm_status_get_trigger_tstamp = _alsa_lib.snd_pcm_status_get_trigger_tstamp
snd_pcm_status_get_trigger_tstamp.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_timestamp_t)]
snd_pcm_status_get_trigger_tstamp.restype = None

#void snd_pcm_status_get_trigger_htstamp(const snd_pcm_status_t *obj, snd_htimestamp_t *ptr);
snd_pcm_status_get_trigger_htstamp = _alsa_lib.snd_pcm_status_get_trigger_htstamp
snd_pcm_status_get_trigger_htstamp.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_htimestamp_t)]
snd_pcm_status_get_trigger_htstamp.restype = None

#void snd_pcm_status_get_tstamp(const snd_pcm_status_t *obj, snd_timestamp_t *ptr);
snd_pcm_status_get_tstamp = _alsa_lib.snd_pcm_status_get_tstamp
snd_pcm_status_get_tstamp.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_timestamp_t)]
snd_pcm_status_get_tstamp.restype = None

#void snd_pcm_status_get_htstamp(const snd_pcm_status_t *obj, snd_htimestamp_t *ptr);
snd_pcm_status_get_htstamp = _alsa_lib.snd_pcm_status_get_htstamp
snd_pcm_status_get_htstamp.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_htimestamp_t)]
snd_pcm_status_get_htstamp.restype = None

#snd_pcm_sframes_t snd_pcm_status_get_delay(const snd_pcm_status_t *obj);
snd_pcm_status_get_delay = _alsa_lib.snd_pcm_status_get_delay
snd_pcm_status_get_delay.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_get_delay.restype = snd_pcm_sframes_t

#snd_pcm_uframes_t snd_pcm_status_get_avail(const snd_pcm_status_t *obj);
snd_pcm_status_get_avail = _alsa_lib.snd_pcm_status_get_avail
snd_pcm_status_get_avail.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_get_avail.restype = snd_pcm_uframes_t

#snd_pcm_uframes_t snd_pcm_status_get_avail_max(const snd_pcm_status_t *obj);
snd_pcm_status_get_avail_max = _alsa_lib.snd_pcm_status_get_avail_max
snd_pcm_status_get_avail_max.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_get_avail_max.restype = snd_pcm_uframes_t

#snd_pcm_uframes_t snd_pcm_status_get_overrange(const snd_pcm_status_t *obj);
snd_pcm_status_get_overrange = _alsa_lib.snd_pcm_status_get_overrange
snd_pcm_status_get_overrange.argtypes = [POINTER(snd_pcm_status_t)]
snd_pcm_status_get_overrange.restype = snd_pcm_uframes_t


# \} 

#
# \defgroup PCM_Description Description Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#const char *snd_pcm_type_name(snd_pcm_type_t type);
snd_pcm_type_name = _alsa_lib.snd_pcm_type_name
snd_pcm_type_name.argtypes = [snd_pcm_type_t]
snd_pcm_type_name.restype = c_char_p

#const char *snd_pcm_stream_name(const snd_pcm_stream_t stream);
snd_pcm_stream_name = _alsa_lib.snd_pcm_stream_name
snd_pcm_stream_name.argtypes = [snd_pcm_stream_t]
snd_pcm_stream_name.restype = c_char_p

#const char *snd_pcm_access_name(const snd_pcm_access_t _access);
snd_pcm_access_name = _alsa_lib.snd_pcm_access_name
snd_pcm_access_name.argtypes = [snd_pcm_access_t]
snd_pcm_access_name.restype = c_char_p

#const char *snd_pcm_format_name(const snd_pcm_format_t format);
snd_pcm_format_name = _alsa_lib.snd_pcm_format_name
snd_pcm_format_name.argtypes = [snd_pcm_format_t]
snd_pcm_format_name.restype = c_char_p

#const char *snd_pcm_format_description(const snd_pcm_format_t format);
snd_pcm_format_description = _alsa_lib.snd_pcm_format_description
snd_pcm_format_description.argtypes = [snd_pcm_format_t]
snd_pcm_format_description.restype = c_char_p

#const char *snd_pcm_subformat_name(const snd_pcm_subformat_t subformat);
snd_pcm_subformat_name = _alsa_lib.snd_pcm_subformat_name
snd_pcm_subformat_name.argtypes = [snd_pcm_subformat_t]
snd_pcm_subformat_name.restype = c_char_p

#const char *snd_pcm_subformat_description(const snd_pcm_subformat_t subformat);
snd_pcm_subformat_description = _alsa_lib.snd_pcm_subformat_description
snd_pcm_subformat_description.argtypes = [snd_pcm_subformat_t]
snd_pcm_subformat_description.restype = c_char_p

#snd_pcm_format_t snd_pcm_format_value(const char* name);
snd_pcm_format_value = _alsa_lib.snd_pcm_format_value
snd_pcm_format_value.argtypes = [c_char_p]
snd_pcm_format_value.restype = snd_pcm_format_t

#const char *snd_pcm_tstamp_mode_name(const snd_pcm_tstamp_t mode);
snd_pcm_tstamp_mode_name = _alsa_lib.snd_pcm_tstamp_mode_name
snd_pcm_tstamp_mode_name.argtypes = [snd_pcm_tstamp_t]
snd_pcm_tstamp_mode_name.restype = c_char_p

#const char *snd_pcm_state_name(const snd_pcm_state_t state);
snd_pcm_state_name = _alsa_lib.snd_pcm_state_name
snd_pcm_state_name.argtypes = [snd_pcm_state_t]
snd_pcm_state_name.restype = c_char_p


# \} 

#
# \defgroup PCM_Dump Debug Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#int snd_pcm_dump(snd_pcm_t *pcm, snd_output_t *out);
snd_pcm_dump = _alsa_lib.snd_pcm_dump
snd_pcm_dump.argtypes = [POINTER(snd_pcm_t), POINTER(snd_output_t)]
snd_pcm_dump.restype = c_int

#int snd_pcm_dump_hw_setup(snd_pcm_t *pcm, snd_output_t *out);
snd_pcm_dump_hw_setup = _alsa_lib.snd_pcm_dump_hw_setup
snd_pcm_dump_hw_setup.argtypes = [POINTER(snd_pcm_t), POINTER(snd_output_t)]
snd_pcm_dump_hw_setup.restype = c_int

#int snd_pcm_dump_sw_setup(snd_pcm_t *pcm, snd_output_t *out);
snd_pcm_dump_sw_setup = _alsa_lib.snd_pcm_dump_sw_setup
snd_pcm_dump_sw_setup.argtypes = [POINTER(snd_pcm_t), POINTER(snd_output_t)]
snd_pcm_dump_sw_setup.restype = c_int

#int snd_pcm_dump_setup(snd_pcm_t *pcm, snd_output_t *out);
snd_pcm_dump_setup = _alsa_lib.snd_pcm_dump_setup
snd_pcm_dump_setup.argtypes = [POINTER(snd_pcm_t), POINTER(snd_output_t)]
snd_pcm_dump_setup.restype = c_int

#int snd_pcm_hw_params_dump(snd_pcm_hw_params_t *params, snd_output_t *out);
snd_pcm_hw_params_dump = _alsa_lib.snd_pcm_hw_params_dump
snd_pcm_hw_params_dump.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_output_t)]
snd_pcm_hw_params_dump.restype = c_int

#int snd_pcm_sw_params_dump(snd_pcm_sw_params_t *params, snd_output_t *out);
snd_pcm_sw_params_dump = _alsa_lib.snd_pcm_sw_params_dump
snd_pcm_sw_params_dump.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_output_t)]
snd_pcm_sw_params_dump.restype = c_int

#int snd_pcm_status_dump(snd_pcm_status_t *status, snd_output_t *out);
snd_pcm_status_dump = _alsa_lib.snd_pcm_status_dump
snd_pcm_status_dump.argtypes = [POINTER(snd_pcm_status_t), POINTER(snd_output_t)]
snd_pcm_status_dump.restype = c_int


# \} 

#
# \defgroup PCM_Direct Direct Access (MMAP) Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#int snd_pcm_mmap_begin(snd_pcm_t *pcm,
			   #const snd_pcm_channel_area_t **areas,
			   #snd_pcm_uframes_t *offset,
			   #snd_pcm_uframes_t *frames);
snd_pcm_mmap_begin = _alsa_lib.snd_pcm_mmap_begin
snd_pcm_mmap_begin.argtypes = [POINTER(snd_pcm_t), POINTER(POINTER(snd_pcm_channel_area_t)), POINTER(snd_pcm_uframes_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_mmap_begin.restype = c_int

#snd_pcm_sframes_t snd_pcm_mmap_commit(snd_pcm_t *pcm,
					  #snd_pcm_uframes_t offset,
					  #snd_pcm_uframes_t frames);
snd_pcm_mmap_commit = _alsa_lib.snd_pcm_mmap_commit
snd_pcm_mmap_commit.argtypes = [POINTER(snd_pcm_t), snd_pcm_uframes_t, snd_pcm_uframes_t]
snd_pcm_mmap_commit.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_mmap_writei(snd_pcm_t *pcm, const void *buffer, snd_pcm_uframes_t size);
snd_pcm_mmap_writei = _alsa_lib.snd_pcm_mmap_writei
snd_pcm_mmap_writei.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_mmap_writei.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_mmap_readi(snd_pcm_t *pcm, void *buffer, snd_pcm_uframes_t size);
snd_pcm_mmap_readi = _alsa_lib.snd_pcm_mmap_readi
snd_pcm_mmap_readi.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_mmap_readi.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_mmap_writen(snd_pcm_t *pcm, void **bufs, snd_pcm_uframes_t size);
snd_pcm_mmap_writen = _alsa_lib.snd_pcm_mmap_writen
snd_pcm_mmap_writen.argtypes = [POINTER(snd_pcm_t), POINTER(c_void_p), snd_pcm_uframes_t]
snd_pcm_mmap_writen.restype = snd_pcm_sframes_t

#snd_pcm_sframes_t snd_pcm_mmap_readn(snd_pcm_t *pcm, void **bufs, snd_pcm_uframes_t size);                                                                
snd_pcm_mmap_readn = _alsa_lib.snd_pcm_mmap_readn
snd_pcm_mmap_readn.argtypes = [POINTER(snd_pcm_t), POINTER(c_void_p), snd_pcm_uframes_t]
snd_pcm_mmap_readn.restype = snd_pcm_sframes_t


# \} 

#
# \defgroup PCM_Helpers Helper Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

#int snd_pcm_format_signed(snd_pcm_format_t format);
snd_pcm_format_signed = _alsa_lib.snd_pcm_format_signed
snd_pcm_format_signed.argtypes = [snd_pcm_format_t]
snd_pcm_format_signed.restype = c_int

#int snd_pcm_format_unsigned(snd_pcm_format_t format);
snd_pcm_format_unsigned = _alsa_lib.snd_pcm_format_unsigned
snd_pcm_format_unsigned.argtypes = [snd_pcm_format_t]
snd_pcm_format_unsigned.restype = c_int

#int snd_pcm_format_linear(snd_pcm_format_t format);
snd_pcm_format_linear = _alsa_lib.snd_pcm_format_linear
snd_pcm_format_linear.argtypes = [snd_pcm_format_t]
snd_pcm_format_linear.restype = c_int

#int snd_pcm_format_float(snd_pcm_format_t format);
snd_pcm_format_float = _alsa_lib.snd_pcm_format_float
snd_pcm_format_float.argtypes = [snd_pcm_format_t]
snd_pcm_format_float.restype = c_int

#int snd_pcm_format_little_endian(snd_pcm_format_t format);
snd_pcm_format_little_endian = _alsa_lib.snd_pcm_format_little_endian
snd_pcm_format_little_endian.argtypes = [snd_pcm_format_t]
snd_pcm_format_little_endian.restype = c_int

#int snd_pcm_format_big_endian(snd_pcm_format_t format);
snd_pcm_format_big_endian = _alsa_lib.snd_pcm_format_big_endian
snd_pcm_format_big_endian.argtypes = [snd_pcm_format_t]
snd_pcm_format_big_endian.restype = c_int

#int snd_pcm_format_cpu_endian(snd_pcm_format_t format);
snd_pcm_format_cpu_endian = _alsa_lib.snd_pcm_format_cpu_endian
snd_pcm_format_cpu_endian.argtypes = [snd_pcm_format_t]
snd_pcm_format_cpu_endian.restype = c_int

#int snd_pcm_format_width(snd_pcm_format_t format);			 in bits 
snd_pcm_format_width = _alsa_lib.snd_pcm_format_width
snd_pcm_format_width.argtypes = [snd_pcm_format_t]
snd_pcm_format_width.restype = c_int

#int snd_pcm_format_physical_width(snd_pcm_format_t format);		 in bits 
snd_pcm_format_physical_width = _alsa_lib.snd_pcm_format_physical_width
snd_pcm_format_physical_width.argtypes = [snd_pcm_format_t]
snd_pcm_format_physical_width.restype = c_int

#snd_pcm_format_t snd_pcm_build_linear_format(int width, int pwidth, int unsignd, int big_endian);
snd_pcm_build_linear_format = _alsa_lib.snd_pcm_build_linear_format
snd_pcm_build_linear_format.argtypes = [c_int, c_int, c_int, c_int]
snd_pcm_build_linear_format.restype = snd_pcm_format_t

#ssize_t snd_pcm_format_size(snd_pcm_format_t format, size_t samples);
snd_pcm_format_size = _alsa_lib.snd_pcm_format_size
snd_pcm_format_size.argtypes = [snd_pcm_format_t, c_size_t]
snd_pcm_format_size.restype = c_size_t

#u_int8_t snd_pcm_format_silence(snd_pcm_format_t format);
snd_pcm_format_silence = _alsa_lib.snd_pcm_format_silence
snd_pcm_format_silence.argtypes = [snd_pcm_format_t]
snd_pcm_format_silence.restype = c_uint8

#u_int16_t snd_pcm_format_silence_16(snd_pcm_format_t format);
snd_pcm_format_silence_16 = _alsa_lib.snd_pcm_format_silence_16
snd_pcm_format_silence_16.argtypes = [snd_pcm_format_t]
snd_pcm_format_silence_16.restype = c_uint16

#u_int32_t snd_pcm_format_silence_32(snd_pcm_format_t format);
snd_pcm_format_silence_32 = _alsa_lib.snd_pcm_format_silence_32
snd_pcm_format_silence_32.argtypes = [snd_pcm_format_t]
snd_pcm_format_silence_32.restype = c_uint32

#u_int64_t snd_pcm_format_silence_64(snd_pcm_format_t format);
snd_pcm_format_silence_64 = _alsa_lib.snd_pcm_format_silence_64
snd_pcm_format_silence_64.argtypes = [snd_pcm_format_t]
snd_pcm_format_silence_64.restype = c_uint64

#int snd_pcm_format_set_silence(snd_pcm_format_t format, void *buf, unsigned int samples);
snd_pcm_format_set_silence = _alsa_lib.snd_pcm_format_set_silence
snd_pcm_format_set_silence.argtypes = [snd_pcm_format_t, c_void_p, c_uint]
snd_pcm_format_set_silence.restype = c_int


#snd_pcm_sframes_t snd_pcm_bytes_to_frames(snd_pcm_t *pcm, ssize_t bytes);
snd_pcm_bytes_to_frames = _alsa_lib.snd_pcm_bytes_to_frames
snd_pcm_bytes_to_frames.argtypes = [POINTER(snd_pcm_t), c_size_t]
snd_pcm_bytes_to_frames.restype = snd_pcm_sframes_t

#ssize_t snd_pcm_frames_to_bytes(snd_pcm_t *pcm, snd_pcm_sframes_t frames);
snd_pcm_frames_to_bytes = _alsa_lib.snd_pcm_frames_to_bytes
snd_pcm_frames_to_bytes.argtypes = [POINTER(snd_pcm_t), snd_pcm_sframes_t]
snd_pcm_frames_to_bytes.restype = c_size_t

#long snd_pcm_bytes_to_samples(snd_pcm_t *pcm, ssize_t bytes);
snd_pcm_bytes_to_samples = _alsa_lib.snd_pcm_bytes_to_samples
snd_pcm_bytes_to_samples.argtypes = [POINTER(snd_pcm_t), c_size_t]
snd_pcm_bytes_to_samples.restype = c_long

#ssize_t snd_pcm_samples_to_bytes(snd_pcm_t *pcm, long samples);
snd_pcm_samples_to_bytes = _alsa_lib.snd_pcm_samples_to_bytes
snd_pcm_samples_to_bytes.argtypes = [POINTER(snd_pcm_t), c_long]
snd_pcm_samples_to_bytes.restype = c_size_t


#int snd_pcm_area_silence(const snd_pcm_channel_area_t *dst_channel, snd_pcm_uframes_t dst_offset,
			 #unsigned int samples, snd_pcm_format_t format);
snd_pcm_area_silence = _alsa_lib.snd_pcm_area_silence
snd_pcm_area_silence.argtypes = [POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, c_uint, snd_pcm_format_t]
snd_pcm_area_silence.restype = c_int

#int snd_pcm_areas_silence(const snd_pcm_channel_area_t *dst_channels, snd_pcm_uframes_t dst_offset,
			  #unsigned int channels, snd_pcm_uframes_t frames, snd_pcm_format_t format);
snd_pcm_areas_silence = _alsa_lib.snd_pcm_areas_silence
snd_pcm_areas_silence.argtypes = [POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, c_uint, snd_pcm_uframes_t, snd_pcm_format_t]
snd_pcm_areas_silence.restype = c_int

#int snd_pcm_area_copy(const snd_pcm_channel_area_t *dst_channel, snd_pcm_uframes_t dst_offset,
			  #const snd_pcm_channel_area_t *src_channel, snd_pcm_uframes_t src_offset,
			  #unsigned int samples, snd_pcm_format_t format);
snd_pcm_area_copy = _alsa_lib.snd_pcm_area_copy
snd_pcm_area_copy.argtypes = [POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, c_uint, snd_pcm_format_t]
snd_pcm_area_copy.restype = c_int

#int snd_pcm_areas_copy(const snd_pcm_channel_area_t *dst_channels, snd_pcm_uframes_t dst_offset,
			   #const snd_pcm_channel_area_t *src_channels, snd_pcm_uframes_t src_offset,
			   #unsigned int channels, snd_pcm_uframes_t frames, snd_pcm_format_t format);
snd_pcm_areas_copy = _alsa_lib.snd_pcm_areas_copy
snd_pcm_areas_copy.argtypes = [POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, POINTER(snd_pcm_channel_area_t), snd_pcm_uframes_t, c_uint, snd_pcm_uframes_t, snd_pcm_format_t]
snd_pcm_areas_copy.restype = c_int


# \} 

#
# \defgroup PCM_Hook Hook Extension
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

# type of pcm hook 
_snd_pcm_hook_type = c_int
SND_PCM_HOOK_TYPE_HW_PARAMS = 0
SND_PCM_HOOK_TYPE_HW_FREE = 1
SND_PCM_HOOK_TYPE_CLOSE = 2
SND_PCM_HOOK_TYPE_LAST = SND_PCM_HOOK_TYPE_CLOSE
snd_pcm_hook_type_t = _snd_pcm_hook_type

# PCM hook container 
class _snd_pcm_hook(Structure):
    _fields_ = [
            ]
snd_pcm_hook_t = _snd_pcm_hook 
# PCM hook callback function 
#typedef int (*snd_pcm_hook_func_t)(snd_pcm_hook_t *hook);
snd_pcm_hook_func_t = CFUNCTYPE(c_int, POINTER(snd_pcm_hook_t))

#snd_pcm_t *snd_pcm_hook_get_pcm(snd_pcm_hook_t *hook);
snd_pcm_hook_get_pcm = _alsa_lib.snd_pcm_hook_get_pcm
snd_pcm_hook_get_pcm.argtypes = [POINTER(snd_pcm_hook_t)]
snd_pcm_hook_get_pcm.restype = POINTER(snd_pcm_t)

#void *snd_pcm_hook_get_private(snd_pcm_hook_t *hook);
snd_pcm_hook_get_private = _alsa_lib.snd_pcm_hook_get_private
snd_pcm_hook_get_private.argtypes = [POINTER(snd_pcm_hook_t)]
snd_pcm_hook_get_private.restype = c_void_p

#void snd_pcm_hook_set_private(snd_pcm_hook_t *hook, void *private_data);
snd_pcm_hook_set_private = _alsa_lib.snd_pcm_hook_set_private
snd_pcm_hook_set_private.argtypes = [POINTER(snd_pcm_hook_t), c_void_p]
snd_pcm_hook_set_private.restype = None

#int snd_pcm_hook_add(snd_pcm_hook_t **hookp, snd_pcm_t *pcm,
#snd_pcm_hook_type_t type,
#snd_pcm_hook_func_t func, void *private_data);
snd_pcm_hook_add = _alsa_lib.snd_pcm_hook_add
snd_pcm_hook_add.argtypes = [POINTER(POINTER(snd_pcm_hook_t)), POINTER(snd_pcm_t), snd_pcm_hook_type_t, snd_pcm_hook_func_t, c_void_p]
snd_pcm_hook_add.restype = c_int

#int snd_pcm_hook_remove(snd_pcm_hook_t *hook);
snd_pcm_hook_remove = _alsa_lib.snd_pcm_hook_remove
snd_pcm_hook_remove.argtypes = [POINTER(snd_pcm_hook_t)]
snd_pcm_hook_remove.restype = c_int


# \} 

#
# \defgroup PCM_Scope Scope Plugin Extension
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

# #SND_PCM_TYPE_METER scope functions 
class _snd_pcm_scope_ops(Structure):
    _fields_ = [
# \brief Enable and prepare it using current params
# \param scope scope handle
#
#int (*enable)(snd_pcm_scope_t *scope);
            ('enable', CFUNCTYPE(c_int, POINTER(snd_pcm_scope_t))),
# \brief Disable
# \param scope scope handle
#
#void (*disable)(snd_pcm_scope_t *scope);
            ('disable', CFUNCTYPE(None, POINTER(snd_pcm_scope_t))),
# \brief PCM has been started
# \param scope scope handle
#
#void (*start)(snd_pcm_scope_t *scope);
            ('start', CFUNCTYPE(None, POINTER(snd_pcm_scope_t))),
# \brief PCM has been stopped
# \param scope scope handle
#
#void (*stop)(snd_pcm_scope_t *scope);
            ('stop', CFUNCTYPE(None, POINTER(snd_pcm_scope_t))),
# \brief New frames are present
# \param scope scope handle
#
#void (*update)(snd_pcm_scope_t *scope);
            ('update', CFUNCTYPE(None, POINTER(snd_pcm_scope_t))),
# \brief Reset status
# \param scope scope handle
#
#void (*reset)(snd_pcm_scope_t *scope);
            ('reset', CFUNCTYPE(None, POINTER(snd_pcm_scope_t))),
# \brief PCM is closing
# \param scope scope handle
#
#void (*close)(snd_pcm_scope_t *scope);
            ('close', CFUNCTYPE(None, POINTER(snd_pcm_scope_t)))
            ]
snd_pcm_scope_ops_t = _snd_pcm_scope_ops

#snd_pcm_uframes_t snd_pcm_meter_get_bufsize(snd_pcm_t *pcm);
snd_pcm_meter_get_bufsize = _alsa_lib.snd_pcm_meter_get_bufsize
snd_pcm_meter_get_bufsize.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_meter_get_bufsize.restype = snd_pcm_uframes_t

#unsigned int snd_pcm_meter_get_channels(snd_pcm_t *pcm);
snd_pcm_meter_get_channels = _alsa_lib.snd_pcm_meter_get_channels
snd_pcm_meter_get_channels.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_meter_get_channels.restype = c_uint

#unsigned int snd_pcm_meter_get_rate(snd_pcm_t *pcm);
snd_pcm_meter_get_rate = _alsa_lib.snd_pcm_meter_get_rate
snd_pcm_meter_get_rate.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_meter_get_rate.restype = c_uint

#snd_pcm_uframes_t snd_pcm_meter_get_now(snd_pcm_t *pcm);
snd_pcm_meter_get_now = _alsa_lib.snd_pcm_meter_get_now
snd_pcm_meter_get_now.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_meter_get_now.restype = snd_pcm_uframes_t

#snd_pcm_uframes_t snd_pcm_meter_get_boundary(snd_pcm_t *pcm);
snd_pcm_meter_get_boundary = _alsa_lib.snd_pcm_meter_get_boundary
snd_pcm_meter_get_boundary.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_meter_get_boundary.restype = snd_pcm_uframes_t

#int snd_pcm_meter_add_scope(snd_pcm_t *pcm, snd_pcm_scope_t *scope);
snd_pcm_meter_add_scope = _alsa_lib.snd_pcm_meter_add_scope
snd_pcm_meter_add_scope.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_scope_t)]
snd_pcm_meter_add_scope.restype = c_int

#snd_pcm_scope_t *snd_pcm_meter_search_scope(snd_pcm_t *pcm, const char *name);
snd_pcm_meter_search_scope = _alsa_lib.snd_pcm_meter_search_scope
snd_pcm_meter_search_scope.argtypes = [POINTER(snd_pcm_t), c_char_p]
snd_pcm_meter_search_scope.restype = POINTER(snd_pcm_scope_t)

#int snd_pcm_scope_malloc(snd_pcm_scope_t **ptr);
snd_pcm_scope_malloc = _alsa_lib.snd_pcm_scope_malloc
snd_pcm_scope_malloc.argtypes = [POINTER(POINTER(snd_pcm_scope_t))]
snd_pcm_scope_malloc.restype = c_int

#void snd_pcm_scope_set_ops(snd_pcm_scope_t *scope,
			   #const snd_pcm_scope_ops_t *val);
snd_pcm_scope_set_ops = _alsa_lib.snd_pcm_scope_set_ops
snd_pcm_scope_set_ops.argtypes = [POINTER(snd_pcm_scope_t), POINTER(snd_pcm_scope_ops_t)]
snd_pcm_scope_set_ops.restype = None

#void snd_pcm_scope_set_name(snd_pcm_scope_t *scope, const char *val);
snd_pcm_scope_set_name = _alsa_lib.snd_pcm_scope_set_name
snd_pcm_scope_set_name.argtypes = [POINTER(snd_pcm_scope_t), c_char_p]
snd_pcm_scope_set_name.restype = None

#const char *snd_pcm_scope_get_name(snd_pcm_scope_t *scope);
snd_pcm_scope_get_name = _alsa_lib.snd_pcm_scope_get_name
snd_pcm_scope_get_name.argtypes = [POINTER(snd_pcm_scope_t)]
snd_pcm_scope_get_name.restype = c_char_p

#void *snd_pcm_scope_get_callback_private(snd_pcm_scope_t *scope);
snd_pcm_scope_get_callback_private = _alsa_lib.snd_pcm_scope_get_callback_private
snd_pcm_scope_get_callback_private.argtypes = [POINTER(snd_pcm_scope_t)]
snd_pcm_scope_get_callback_private.restype = c_void_p

#void snd_pcm_scope_set_callback_private(snd_pcm_scope_t *scope, void *val);
snd_pcm_scope_set_callback_private = _alsa_lib.snd_pcm_scope_set_callback_private
snd_pcm_scope_set_callback_private.argtypes = [POINTER(snd_pcm_scope_t), c_void_p]
snd_pcm_scope_set_callback_private.restype = None

#int snd_pcm_scope_s16_open(snd_pcm_t *pcm, const char *name,
			   #snd_pcm_scope_t **scopep);
snd_pcm_scope_s16_open = _alsa_lib.snd_pcm_scope_s16_open
snd_pcm_scope_s16_open.argtypes = [POINTER(snd_pcm_t), c_char_p, POINTER(POINTER(snd_pcm_scope_t))]
snd_pcm_scope_s16_open.restype = c_int

#int16_t *snd_pcm_scope_s16_get_channel_buffer(snd_pcm_scope_t *scope,
						  #unsigned int channel);
snd_pcm_scope_s16_get_channel_buffer = _alsa_lib.snd_pcm_scope_s16_get_channel_buffer
snd_pcm_scope_s16_get_channel_buffer.argtypes = [POINTER(snd_pcm_scope_t), c_uint]
snd_pcm_scope_s16_get_channel_buffer.restype = POINTER(c_int16)


# \} 

#
# \defgroup PCM_Simple Simple setup functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

# Simple PCM latency type 
_snd_spcm_latency = c_int
# standard latency - for standard playback or capture
#(estimated latency in one direction 350ms) 
SND_SPCM_LATENCY_STANDARD = 0
# medium latency - software phones etc.
#(estimated latency in one direction maximally 25ms 
SND_SPCM_LATENCY_MEDIUM = 1
# realtime latency - realtime applications (effect processors etc.)
#(estimated latency in one direction 5ms and better) 
SND_SPCM_LATENCY_REALTIME = 2
snd_spcm_latency_t = _snd_spcm_latency

# Simple PCM xrun type 
_snd_spcm_xrun_type = c_int
# driver / library will ignore all xruns, the stream runs forever 
SND_SPCM_XRUN_IGNORE = 0
# driver / library stops the stream when an xrun occurs 
SND_SPCM_XRUN_STOP = 1
snd_spcm_xrun_type_t = _snd_spcm_xrun_type

# Simple PCM duplex type 
_snd_spcm_duplex_type = c_int
# liberal duplex - the buffer and period sizes might not match 
SND_SPCM_DUPLEX_LIBERAL = 0
# pedantic duplex - the buffer and period sizes MUST match 
SND_SPCM_DUPLEX_PEDANTIC = 1
snd_spcm_duplex_type_t = _snd_spcm_duplex_type

#int snd_spcm_init(snd_pcm_t *pcm,
		  #unsigned int rate,
		  #unsigned int channels,
		  #snd_pcm_format_t format,
		  #snd_pcm_subformat_t subformat,
		  #snd_spcm_latency_t latency,
		  #snd_pcm_access_t _access,
		  #snd_spcm_xrun_type_t xrun_type);
snd_spcm_init = _alsa_lib.snd_spcm_init
snd_spcm_init.argtypes = [POINTER(snd_pcm_t), c_uint, c_uint, snd_pcm_format_t, snd_pcm_subformat_t, snd_spcm_latency_t, snd_pcm_access_t, snd_spcm_xrun_type_t]
snd_spcm_init.restype = c_int

#int snd_spcm_init_duplex(snd_pcm_t *playback_pcm,
			 #snd_pcm_t *capture_pcm,
			 #unsigned int rate,
			 #unsigned int channels,
			 #snd_pcm_format_t format,
			 #snd_pcm_subformat_t subformat,
			 #snd_spcm_latency_t latency,
			 #snd_pcm_access_t _access,
			 #snd_spcm_xrun_type_t xrun_type,
			 #snd_spcm_duplex_type_t duplex_type);
snd_spcm_init_duplex = _alsa_lib.snd_spcm_init_duplex
snd_spcm_init_duplex.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_t), c_uint, c_uint, snd_pcm_format_t, snd_pcm_subformat_t, snd_spcm_latency_t, snd_pcm_access_t, snd_spcm_xrun_type_t, snd_spcm_duplex_type_t]
snd_spcm_init_duplex.restype = c_int


#int snd_spcm_init_get_params(snd_pcm_t *pcm,
				 #unsigned int *rate,
				 #snd_pcm_uframes_t *buffer_size,
				 #snd_pcm_uframes_t *period_size);
snd_spcm_init_get_params = _alsa_lib.snd_spcm_init_get_params
snd_spcm_init_get_params.argtypes = [POINTER(snd_pcm_t), POINTER(c_uint), POINTER(snd_pcm_uframes_t), POINTER(snd_pcm_uframes_t)]
snd_spcm_init_get_params.restype = c_int


# \} 

#
# \defgroup PCM_Deprecated Deprecated Functions
# \ingroup PCM
# See the \ref pcm page for more details.
# \{
#

# Deprecated functions, for compatibility 
#const char *snd_pcm_start_mode_name(snd_pcm_start_t mode) __attribute__((deprecated));
snd_pcm_start_mode_name = _alsa_lib.snd_pcm_start_mode_name
snd_pcm_start_mode_name.argtypes = [snd_pcm_start_t]
snd_pcm_start_mode_name.restype = c_char_p

#const char *snd_pcm_xrun_mode_name(snd_pcm_xrun_t mode) __attribute__((deprecated));
snd_pcm_xrun_mode_name = _alsa_lib.snd_pcm_xrun_mode_name
snd_pcm_xrun_mode_name.argtypes = [snd_pcm_xrun_t]
snd_pcm_xrun_mode_name.restype = c_char_p

#int snd_pcm_sw_params_set_start_mode(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_start_t val) __attribute__((deprecated));
snd_pcm_sw_params_set_start_mode = _alsa_lib.snd_pcm_sw_params_set_start_mode
snd_pcm_sw_params_set_start_mode.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_start_t]
snd_pcm_sw_params_set_start_mode.restype = c_int

#snd_pcm_start_t snd_pcm_sw_params_get_start_mode(const snd_pcm_sw_params_t *params) __attribute__((deprecated));
snd_pcm_sw_params_get_start_mode = _alsa_lib.snd_pcm_sw_params_get_start_mode
snd_pcm_sw_params_get_start_mode.argtypes = [POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params_get_start_mode.restype = snd_pcm_start_t

#int snd_pcm_sw_params_set_xrun_mode(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_xrun_t val) __attribute__((deprecated));
snd_pcm_sw_params_set_xrun_mode = _alsa_lib.snd_pcm_sw_params_set_xrun_mode
snd_pcm_sw_params_set_xrun_mode.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_xrun_t]
snd_pcm_sw_params_set_xrun_mode.restype = c_int

#snd_pcm_xrun_t snd_pcm_sw_params_get_xrun_mode(const snd_pcm_sw_params_t *params) __attribute__((deprecated));
snd_pcm_sw_params_get_xrun_mode = _alsa_lib.snd_pcm_sw_params_get_xrun_mode
snd_pcm_sw_params_get_xrun_mode.argtypes = [POINTER(snd_pcm_sw_params_t)]
snd_pcm_sw_params_get_xrun_mode.restype = snd_pcm_xrun_t

#if !defined(ALSA_LIBRARY_BUILD) && !defined(ALSA_PCM_OLD_SW_PARAMS_API)
#int snd_pcm_sw_params_set_xfer_align(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, snd_pcm_uframes_t val) __attribute__((deprecated));
snd_pcm_sw_params_set_xfer_align = _alsa_lib.snd_pcm_sw_params_set_xfer_align
snd_pcm_sw_params_set_xfer_align.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), snd_pcm_uframes_t]
snd_pcm_sw_params_set_xfer_align.restype = c_int

#int snd_pcm_sw_params_get_xfer_align(const snd_pcm_sw_params_t *params, snd_pcm_uframes_t *val) __attribute__((deprecated));
snd_pcm_sw_params_get_xfer_align = _alsa_lib.snd_pcm_sw_params_get_xfer_align
snd_pcm_sw_params_get_xfer_align.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_sw_params_get_xfer_align.restype = c_int

#int snd_pcm_sw_params_set_sleep_min(snd_pcm_t *pcm, snd_pcm_sw_params_t *params, unsigned int val) __attribute__((deprecated));
snd_pcm_sw_params_set_sleep_min = _alsa_lib.snd_pcm_sw_params_set_sleep_min
snd_pcm_sw_params_set_sleep_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_sw_params_t), c_uint]
snd_pcm_sw_params_set_sleep_min.restype = c_int

#int snd_pcm_sw_params_get_sleep_min(const snd_pcm_sw_params_t *params, unsigned int *val) __attribute__((deprecated));
snd_pcm_sw_params_get_sleep_min = _alsa_lib.snd_pcm_sw_params_get_sleep_min
snd_pcm_sw_params_get_sleep_min.argtypes = [POINTER(snd_pcm_sw_params_t), POINTER(c_uint)]
snd_pcm_sw_params_get_sleep_min.restype = c_int

#endif  !ALSA_LIBRARY_BUILD && !ALSA_PCM_OLD_SW_PARAMS_API 
#if !defined(ALSA_LIBRARY_BUILD) && !defined(ALSA_PCM_OLD_HW_PARAMS_API)
#int snd_pcm_hw_params_get_tick_time(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_get_tick_time = _alsa_lib.snd_pcm_hw_params_get_tick_time
snd_pcm_hw_params_get_tick_time.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_tick_time.restype = c_int

#int snd_pcm_hw_params_get_tick_time_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_get_tick_time_min = _alsa_lib.snd_pcm_hw_params_get_tick_time_min
snd_pcm_hw_params_get_tick_time_min.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_tick_time_min.restype = c_int

#int snd_pcm_hw_params_get_tick_time_max(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_get_tick_time_max = _alsa_lib.snd_pcm_hw_params_get_tick_time_max
snd_pcm_hw_params_get_tick_time_max.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_get_tick_time_max.restype = c_int

#int snd_pcm_hw_params_test_tick_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir) __attribute__((deprecated));
snd_pcm_hw_params_test_tick_time = _alsa_lib.snd_pcm_hw_params_test_tick_time
snd_pcm_hw_params_test_tick_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_test_tick_time.restype = c_int

#int snd_pcm_hw_params_set_tick_time(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time = _alsa_lib.snd_pcm_hw_params_set_tick_time
snd_pcm_hw_params_set_tick_time.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_tick_time.restype = c_int

#int snd_pcm_hw_params_set_tick_time_min(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_min = _alsa_lib.snd_pcm_hw_params_set_tick_time_min
snd_pcm_hw_params_set_tick_time_min.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_min.restype = c_int

#int snd_pcm_hw_params_set_tick_time_max(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_max = _alsa_lib.snd_pcm_hw_params_set_tick_time_max
snd_pcm_hw_params_set_tick_time_max.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_max.restype = c_int

#int snd_pcm_hw_params_set_tick_time_minmax(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *min, int *mindir, unsigned int *max, int *maxdir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_minmax = _alsa_lib.snd_pcm_hw_params_set_tick_time_minmax
snd_pcm_hw_params_set_tick_time_minmax.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_minmax.restype = c_int

#int snd_pcm_hw_params_set_tick_time_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_near = _alsa_lib.snd_pcm_hw_params_set_tick_time_near
snd_pcm_hw_params_set_tick_time_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_near.restype = c_int

#int snd_pcm_hw_params_set_tick_time_first(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_first = _alsa_lib.snd_pcm_hw_params_set_tick_time_first
snd_pcm_hw_params_set_tick_time_first.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_first.restype = c_int

#int snd_pcm_hw_params_set_tick_time_last(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir) __attribute__((deprecated));
snd_pcm_hw_params_set_tick_time_last = _alsa_lib.snd_pcm_hw_params_set_tick_time_last
snd_pcm_hw_params_set_tick_time_last.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_tick_time_last.restype = c_int
