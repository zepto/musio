#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa control.
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


""" Alsa control.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *
from .hwdep import *
from .pcm import *
from .rawmidi import *

#
#  \defgroup Control Control Interface
#  The control interface.
#  See \ref control page for more details.
#  \{
#

# dlsym version for interface entry callback 
#define SND_CONTROL_DLSYM_VERSION	_dlsym_control_001

# IEC958 structure 
class snd_aes_iec958(Structure):
    _fields_ = [
            ('status', c_ubyte * 24), # *< AES/IEC958 channel status bits 
            ('subcode', c_ubyte * 147), # *< AES/IEC958 subcode bits 
            ('pad', c_ubyte), # *< nothing 
            ('dig_subframe', c_ubyte * 4) # *< AES/IEC958 subframe bits 
            ]
snd_aes_iec958_t = snd_aes_iec958

# CTL card info container 
class _snd_ctl_card_info(Structure):
    _fields_ = [
            ]
snd_ctl_card_info_t = _snd_ctl_card_info 

# CTL element identifier container 
class _snd_ctl_elem_id(Structure):
    _fields_ = [
            ]
snd_ctl_elem_id_t = _snd_ctl_elem_id 

# CTL element identifier list container 
class _snd_ctl_elem_list(Structure):
    _fields_ = [
            ]
snd_ctl_elem_list_t = _snd_ctl_elem_list 

# CTL element info container 
class _snd_ctl_elem_info(Structure):
    _fields_ = [
            ]
snd_ctl_elem_info_t = _snd_ctl_elem_info 

# CTL element value container 
class _snd_ctl_elem_value(Structure):
    _fields_ = [
            ]
snd_ctl_elem_value_t = _snd_ctl_elem_value 

# CTL event container 
class _snd_ctl_event(Structure):
    _fields_ = [
            ]
snd_ctl_event_t = _snd_ctl_event 

# CTL element type 
_snd_ctl_elem_type = c_int
# Invalid type 
SND_CTL_ELEM_TYPE_NONE = 0
# Boolean contents 
SND_CTL_ELEM_TYPE_BOOLEAN = 1
# Integer contents 
SND_CTL_ELEM_TYPE_INTEGER = 2
# Enumerated contents 
SND_CTL_ELEM_TYPE_ENUMERATED = 3
# Bytes contents 
SND_CTL_ELEM_TYPE_BYTES = 4
# IEC958 (S/PDIF) setting content 
SND_CTL_ELEM_TYPE_IEC958 = 5
# 64-bit integer contents 
SND_CTL_ELEM_TYPE_INTEGER64 = 6
SND_CTL_ELEM_TYPE_LAST = SND_CTL_ELEM_TYPE_INTEGER64
snd_ctl_elem_type_t = _snd_ctl_elem_type 

# CTL related interface 
_snd_ctl_elem_iface = c_int
# Card level 
SND_CTL_ELEM_IFACE_CARD = 0
# Hardware dependent device 
SND_CTL_ELEM_IFACE_HWDEP = 1
# Mixer 
SND_CTL_ELEM_IFACE_MIXER = 2
# PCM 
SND_CTL_ELEM_IFACE_PCM = 3
# RawMidi 
SND_CTL_ELEM_IFACE_RAWMIDI = 4
# Timer 
SND_CTL_ELEM_IFACE_TIMER = 5
# Sequencer 
SND_CTL_ELEM_IFACE_SEQUENCER = 6
SND_CTL_ELEM_IFACE_LAST = SND_CTL_ELEM_IFACE_SEQUENCER
snd_ctl_elem_iface_t = _snd_ctl_elem_iface

# Event class 
_snd_ctl_event_type = c_int
# Elements related event 
SND_CTL_EVENT_ELEM = 0
SND_CTL_EVENT_LAST = SND_CTL_EVENT_ELEM
snd_ctl_event_type_t = _snd_ctl_event_type 

# Element has been removed (Warning: test this first and if set don't
# test the other masks) \hideinitializer 
SND_CTL_EVENT_MASK_REMOVE = (~0)
# Element value has been changed \hideinitializer 
SND_CTL_EVENT_MASK_VALUE = (1<<0)
# Element info has been changed \hideinitializer 
SND_CTL_EVENT_MASK_INFO	= (1<<1)
# Element has been added \hideinitializer 
SND_CTL_EVENT_MASK_ADD = (1<<2)
# Element's TLV value has been changed \hideinitializer 
SND_CTL_EVENT_MASK_TLV = (1<<3)

# CTL name helper 
SND_CTL_NAME_NONE =	""
# CTL name helper 
SND_CTL_NAME_PLAYBACK =	"Playback "
# CTL name helper 
SND_CTL_NAME_CAPTURE = "Capture "

# CTL name helper 
SND_CTL_NAME_IEC958_NONE = ""
# CTL name helper 
SND_CTL_NAME_IEC958_SWITCH = "Switch"
# CTL name helper 
SND_CTL_NAME_IEC958_VOLUME = "Volume"
# CTL name helper 
SND_CTL_NAME_IEC958_DEFAULT = "Default"
# CTL name helper 
SND_CTL_NAME_IEC958_MASK = "Mask"
# CTL name helper 
SND_CTL_NAME_IEC958_CON_MASK = "Con Mask"
# CTL name helper 
SND_CTL_NAME_IEC958_PRO_MASK = "Pro Mask"
# CTL name helper 
SND_CTL_NAME_IEC958_PCM_STREAM = "PCM Stream"
# Element name for IEC958 (S/PDIF) 
#SND_CTL_NAME_IEC958(expl,direction,what) = "IEC958 " expl SND_CTL_NAME_##direction SND_CTL_NAME_IEC958_##what

# Mask for the major Power State identifier 
SND_CTL_POWER_MASK = 0xff00
# ACPI/PCI Power State D0 
SND_CTL_POWER_D0 = 0x0000
# ACPI/PCI Power State D1 
SND_CTL_POWER_D1 = 0x0100
# ACPI/PCI Power State D2 
SND_CTL_POWER_D2 = 0x0200
# ACPI/PCI Power State D3 
SND_CTL_POWER_D3 = 0x0300
# ACPI/PCI Power State D3hot 
SND_CTL_POWER_D3hot = (SND_CTL_POWER_D3|0x0000)
# ACPI/PCI Power State D3cold 
SND_CTL_POWER_D3cold = (SND_CTL_POWER_D3|0x0001)

# TLV type - Container 
SND_CTL_TLVT_CONTAINER = 0x0000
# TLV type - basic dB scale 
SND_CTL_TLVT_DB_SCALE = 0x0001
# TLV type - linear volume 
SND_CTL_TLVT_DB_LINEAR = 0x0002
# TLV type - dB range container 
SND_CTL_TLVT_DB_RANGE = 0x0003
# TLV type - dB scale specified by min/max values 
SND_CTL_TLVT_DB_MINMAX = 0x0004
# TLV type - dB scale specified by min/max values (with mute) 
SND_CTL_TLVT_DB_MINMAX_MUTE = 0x0005

# Mute state 
SND_CTL_TLV_DB_GAIN_MUTE = -9999999

# CTL type 
_snd_ctl_type = c_int
# Kernel level CTL 
SND_CTL_TYPE_HW = 0
# Shared memory client CTL 
SND_CTL_TYPE_SHM = 1
# INET client CTL (not yet implemented) 
SND_CTL_TYPE_INET = 2
# External control plugin 
SND_CTL_TYPE_EXT = 3
snd_ctl_type_t = _snd_ctl_type 

# Non blocking mode (flag for open mode) \hideinitializer 
SND_CTL_NONBLOCK = 0x0001

# Async notification (flag for open mode) \hideinitializer 
SND_CTL_ASYNC =	0x0002

# Read only (flag for open mode) \hideinitializer 
SND_CTL_READONLY = 0x0004

# CTL handle 
class _snd_ctl(Structure):
    _fields_ = [
            ]
snd_ctl_t = _snd_ctl 

# Don't destroy the ctl handle when close 
SND_SCTL_NOFREE	= 0x0001

# SCTL type 
class _snd_sctl(Structure):
    _fields_ = [
            ]
snd_sctl_t = _snd_sctl 

#int snd_card_load(int card);
snd_card_load = _alsa_lib.snd_card_load
snd_card_load.argtypes = [c_int]
snd_card_load.restype = c_int

#int snd_card_next(int *card);
snd_card_next = _alsa_lib.snd_card_next
snd_card_next.argtypes = [POINTER(c_int)]
snd_card_next.restype = c_int

#int snd_card_get_index(const char *name);
snd_card_get_index = _alsa_lib.snd_card_get_index
snd_card_get_index.argtypes = [c_char_p]
snd_card_get_index.restype = c_int

#int snd_card_get_name(int card, char **name);
snd_card_get_name = _alsa_lib.snd_card_get_name
snd_card_get_name.argtypes = [c_int, POINTER(c_char_p)]
snd_card_get_name.restype = c_int

#int snd_card_get_longname(int card, char **name);
snd_card_get_longname = _alsa_lib.snd_card_get_longname
snd_card_get_longname.argtypes = [c_int, POINTER(c_char_p)]
snd_card_get_longname.restype = c_int


#int snd_device_name_hint(int card, const char *iface, void ***hints);
snd_device_name_hint = _alsa_lib.snd_device_name_hint
snd_device_name_hint.argtypes = [c_int, c_char_p, POINTER(POINTER(c_void_p))]
snd_device_name_hint.restype = c_int

#int snd_device_name_free_hint(void **hints);
snd_device_name_free_hint = _alsa_lib.snd_device_name_free_hint
snd_device_name_free_hint.argtypes = [POINTER(c_void_p)]
snd_device_name_free_hint.restype = c_int

#char *snd_device_name_get_hint(const void *hint, const char *id);
snd_device_name_get_hint = _alsa_lib.snd_device_name_get_hint
snd_device_name_get_hint.argtypes = [c_void_p, c_char_p]
snd_device_name_get_hint.restype = c_char_p


#int snd_ctl_open(snd_ctl_t **ctl, const char *name, int mode);
snd_ctl_open = _alsa_lib.snd_ctl_open
snd_ctl_open.argtypes = [POINTER(POINTER(snd_ctl_t)), c_char_p, c_int]
snd_ctl_open.restype = c_int

#int snd_ctl_open_lconf(snd_ctl_t **ctl, const char *name, int mode, snd_config_t *lconf);
snd_ctl_open_lconf = _alsa_lib.snd_ctl_open_lconf
snd_ctl_open_lconf.argtypes = [POINTER(POINTER(snd_ctl_t)), c_char_p, c_int, POINTER(snd_config_t)]
snd_ctl_open_lconf.restype = c_int

#int snd_ctl_close(snd_ctl_t *ctl);
snd_ctl_close = _alsa_lib.snd_ctl_close
snd_ctl_close.argtypes = [POINTER(snd_ctl_t)]
snd_ctl_close.restype = c_int

#int snd_ctl_nonblock(snd_ctl_t *ctl, int nonblock);
snd_ctl_nonblock = _alsa_lib.snd_ctl_nonblock
snd_ctl_nonblock.argtypes = [POINTER(snd_ctl_t), c_int]
snd_ctl_nonblock.restype = c_int

#int snd_async_add_ctl_handler(snd_async_handler_t **handler, snd_ctl_t *ctl, 
				  #snd_async_callback_t callback, void *private_data);
snd_async_add_ctl_handler = _alsa_lib.snd_async_add_ctl_handler
snd_async_add_ctl_handler.argtypes = [POINTER(POINTER(snd_async_handler_t)), POINTER(snd_ctl_t), snd_async_callback_t, c_void_p]
snd_async_add_ctl_handler.restype = c_int

#snd_ctl_t *snd_async_handler_get_ctl(snd_async_handler_t *handler);
snd_async_handler_get_ctl = _alsa_lib.snd_async_handler_get_ctl
snd_async_handler_get_ctl.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_ctl.restype = POINTER(snd_ctl_t)

#int snd_ctl_poll_descriptors_count(snd_ctl_t *ctl);
snd_ctl_poll_descriptors_count = _alsa_lib.snd_ctl_poll_descriptors_count
snd_ctl_poll_descriptors_count.argtypes = [POINTER(snd_ctl_t)]
snd_ctl_poll_descriptors_count.restype = c_int

#int snd_ctl_poll_descriptors(snd_ctl_t *ctl, struct pollfd *pfds, unsigned int space);
snd_ctl_poll_descriptors = _alsa_lib.snd_ctl_poll_descriptors
snd_ctl_poll_descriptors.argtypes = [POINTER(snd_ctl_t), POINTER(pollfd), c_uint]
snd_ctl_poll_descriptors.restype = c_int

#int snd_ctl_poll_descriptors_revents(snd_ctl_t *ctl, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_ctl_poll_descriptors_revents = _alsa_lib.snd_ctl_poll_descriptors_revents
snd_ctl_poll_descriptors_revents.argtypes = [POINTER(snd_ctl_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_ctl_poll_descriptors_revents.restype = c_int

#int snd_ctl_subscribe_events(snd_ctl_t *ctl, int subscribe);
snd_ctl_subscribe_events = _alsa_lib.snd_ctl_subscribe_events
snd_ctl_subscribe_events.argtypes = [POINTER(snd_ctl_t), c_int]
snd_ctl_subscribe_events.restype = c_int

#int snd_ctl_card_info(snd_ctl_t *ctl, snd_ctl_card_info_t *info);
snd_ctl_card_info = _alsa_lib.snd_ctl_card_info
snd_ctl_card_info.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info.restype = c_int

#int snd_ctl_elem_list(snd_ctl_t *ctl, snd_ctl_elem_list_t *list);
snd_ctl_elem_list = _alsa_lib.snd_ctl_elem_list
snd_ctl_elem_list.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list.restype = c_int

#int snd_ctl_elem_info(snd_ctl_t *ctl, snd_ctl_elem_info_t *info);
snd_ctl_elem_info = _alsa_lib.snd_ctl_elem_info
snd_ctl_elem_info.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info.restype = c_int

#int snd_ctl_elem_read(snd_ctl_t *ctl, snd_ctl_elem_value_t *value);
snd_ctl_elem_read = _alsa_lib.snd_ctl_elem_read
snd_ctl_elem_read.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_read.restype = c_int

#int snd_ctl_elem_write(snd_ctl_t *ctl, snd_ctl_elem_value_t *value);
snd_ctl_elem_write = _alsa_lib.snd_ctl_elem_write
snd_ctl_elem_write.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_write.restype = c_int

#int snd_ctl_elem_lock(snd_ctl_t *ctl, snd_ctl_elem_id_t *id);
snd_ctl_elem_lock = _alsa_lib.snd_ctl_elem_lock
snd_ctl_elem_lock.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_lock.restype = c_int

#int snd_ctl_elem_unlock(snd_ctl_t *ctl, snd_ctl_elem_id_t *id);
snd_ctl_elem_unlock = _alsa_lib.snd_ctl_elem_unlock
snd_ctl_elem_unlock.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_unlock.restype = c_int

#int snd_ctl_elem_tlv_read(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
			  #unsigned int *tlv, unsigned int tlv_size);
snd_ctl_elem_tlv_read = _alsa_lib.snd_ctl_elem_tlv_read
snd_ctl_elem_tlv_read.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), POINTER(c_uint), c_uint]
snd_ctl_elem_tlv_read.restype = c_int

#int snd_ctl_elem_tlv_write(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
			   #const unsigned int *tlv);
snd_ctl_elem_tlv_write = _alsa_lib.snd_ctl_elem_tlv_write
snd_ctl_elem_tlv_write.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), POINTER(c_uint)]
snd_ctl_elem_tlv_write.restype = c_int

#int snd_ctl_elem_tlv_command(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
				 #const unsigned int *tlv);
snd_ctl_elem_tlv_command = _alsa_lib.snd_ctl_elem_tlv_command
snd_ctl_elem_tlv_command.argtype = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), POINTER(c_uint)]
snd_ctl_elem_tlv_command.restype = c_int

#ifdef __ALSA_HWDEP_H
#int snd_ctl_hwdep_next_device(snd_ctl_t *ctl, int * device);
snd_ctl_hwdep_next_device = _alsa_lib.snd_ctl_hwdep_next_device
snd_ctl_hwdep_next_device.argtypes = [POINTER(snd_ctl_t), POINTER(c_int)]
snd_ctl_hwdep_next_device.restype = c_int

#int snd_ctl_hwdep_info(snd_ctl_t *ctl, snd_hwdep_info_t * info);
snd_ctl_hwdep_info = _alsa_lib.snd_ctl_hwdep_info
snd_ctl_hwdep_info.argtypes = [POINTER(snd_ctl_t), POINTER(snd_hwdep_info_t)]
snd_ctl_hwdep_info.restype = c_int

#endif
#ifdef __ALSA_PCM_H
#int snd_ctl_pcm_next_device(snd_ctl_t *ctl, int *device);
snd_ctl_pcm_next_device = _alsa_lib.snd_ctl_pcm_next_device
snd_ctl_pcm_next_device.argtypes = [POINTER(snd_ctl_t), POINTER(c_int)]
snd_ctl_pcm_next_device.restype = c_int

#int snd_ctl_pcm_info(snd_ctl_t *ctl, snd_pcm_info_t * info);
snd_ctl_pcm_info = _alsa_lib.snd_ctl_pcm_info
snd_ctl_pcm_info.argtypes = [POINTER(snd_ctl_t), POINTER(snd_pcm_info_t)]
snd_ctl_pcm_info.restype = c_int

#int snd_ctl_pcm_prefer_subdevice(snd_ctl_t *ctl, int subdev);
snd_ctl_pcm_prefer_subdevice = _alsa_lib.snd_ctl_pcm_prefer_subdevice
snd_ctl_pcm_prefer_subdevice.argtypes = [POINTER(snd_ctl_t), c_int]
snd_ctl_pcm_prefer_subdevice.restype = c_int

#endif
#ifdef __ALSA_RAWMIDI_H
#int snd_ctl_rawmidi_next_device(snd_ctl_t *ctl, int * device);
snd_ctl_rawmidi_next_device = _alsa_lib.snd_ctl_rawmidi_next_device
snd_ctl_rawmidi_next_device.argtypes = [POINTER(snd_ctl_t), POINTER(c_int)]
snd_ctl_rawmidi_next_device.restype = c_int

#int snd_ctl_rawmidi_info(snd_ctl_t *ctl, snd_rawmidi_info_t * info);
snd_ctl_rawmidi_info = _alsa_lib.snd_ctl_rawmidi_info
snd_ctl_rawmidi_info.argtypes = [POINTER(snd_ctl_t), POINTER(snd_rawmidi_info_t)]
snd_ctl_rawmidi_info.restype = c_int

#int snd_ctl_rawmidi_prefer_subdevice(snd_ctl_t *ctl, int subdev);
snd_ctl_rawmidi_prefer_subdevice = _alsa_lib.snd_ctl_rawmidi_prefer_subdevice
snd_ctl_rawmidi_prefer_subdevice.argtypes = [POINTER(snd_ctl_t), c_int]
snd_ctl_rawmidi_prefer_subdevice.restype = c_int

#endif
#int snd_ctl_set_power_state(snd_ctl_t *ctl, unsigned int state);
snd_ctl_set_power_state = _alsa_lib.snd_ctl_set_power_state
snd_ctl_set_power_state.argtypes = [POINTER(snd_ctl_t), c_uint]
snd_ctl_set_power_state.restype = c_int

#int snd_ctl_get_power_state(snd_ctl_t *ctl, unsigned int *state);
snd_ctl_get_power_state = _alsa_lib.snd_ctl_get_power_state
snd_ctl_get_power_state.argtypes = [POINTER(snd_ctl_t), POINTER(c_uint)]
snd_ctl_get_power_state.restype = c_int


#int snd_ctl_read(snd_ctl_t *ctl, snd_ctl_event_t *event);
snd_ctl_read = _alsa_lib.snd_ctl_read
snd_ctl_read.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_event_t)]
snd_ctl_read.restype = c_int

#int snd_ctl_wait(snd_ctl_t *ctl, int timeout);
snd_ctl_wait = _alsa_lib.snd_ctl_wait
snd_ctl_wait.argtypes = [POINTER(snd_ctl_t), c_int]
snd_ctl_wait.restype = c_int

#const char *snd_ctl_name(snd_ctl_t *ctl);
snd_ctl_name = _alsa_lib.snd_ctl_name
snd_ctl_name.argtypes = [POINTER(snd_ctl_t)]
snd_ctl_name.restype = c_char_p

#snd_ctl_type_t snd_ctl_type(snd_ctl_t *ctl);
snd_ctl_type = _alsa_lib.snd_ctl_type
snd_ctl_type.argtypes = [POINTER(snd_ctl_t)]
snd_ctl_type.restype = snd_ctl_type_t


#const char *snd_ctl_elem_type_name(snd_ctl_elem_type_t type);
snd_ctl_elem_type_name = _alsa_lib.snd_ctl_elem_type_name
snd_ctl_elem_type_name.argtypes = [snd_ctl_elem_type_t]
snd_ctl_elem_type_name.restype = c_char_p

#const char *snd_ctl_elem_iface_name(snd_ctl_elem_iface_t iface);
snd_ctl_elem_iface_name = _alsa_lib.snd_ctl_elem_iface_name
snd_ctl_elem_iface_name.argtypes = [snd_ctl_elem_iface_t]
snd_ctl_elem_iface_name.restype = c_char_p

#const char *snd_ctl_event_type_name(snd_ctl_event_type_t type);
snd_ctl_event_type_name = _alsa_lib.snd_ctl_event_type_name
snd_ctl_event_type_name.argtypes = [snd_ctl_event_type_t]
snd_ctl_event_type_name.restype = c_char_p


#unsigned int snd_ctl_event_elem_get_mask(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_mask = _alsa_lib.snd_ctl_event_elem_get_mask
snd_ctl_event_elem_get_mask.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_mask.restype = c_uint

#unsigned int snd_ctl_event_elem_get_numid(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_numid = _alsa_lib.snd_ctl_event_elem_get_numid
snd_ctl_event_elem_get_numid.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_numid.restype = c_uint

#void snd_ctl_event_elem_get_id(const snd_ctl_event_t *obj, snd_ctl_elem_id_t *ptr);
snd_ctl_event_elem_get_id = _alsa_lib.snd_ctl_event_elem_get_id
snd_ctl_event_elem_get_id.argtypes = [POINTER(snd_ctl_event_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_event_elem_get_id.restype = None

#snd_ctl_elem_iface_t snd_ctl_event_elem_get_interface(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_interface = _alsa_lib.snd_ctl_event_elem_get_interface
snd_ctl_event_elem_get_interface.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_ctl_event_elem_get_device(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_device = _alsa_lib.snd_ctl_event_elem_get_device
snd_ctl_event_elem_get_device.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_device.restype = c_uint

#unsigned int snd_ctl_event_elem_get_subdevice(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_subdevice = _alsa_lib.snd_ctl_event_elem_get_subdevice
snd_ctl_event_elem_get_subdevice.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_subdevice.restype = c_uint

#const char *snd_ctl_event_elem_get_name(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_name = _alsa_lib.snd_ctl_event_elem_get_name
snd_ctl_event_elem_get_name.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_name.restype = c_char_p

#unsigned int snd_ctl_event_elem_get_index(const snd_ctl_event_t *obj);
snd_ctl_event_elem_get_index = _alsa_lib.snd_ctl_event_elem_get_index
snd_ctl_event_elem_get_index.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_elem_get_index.restype = c_uint


#int snd_ctl_elem_list_alloc_space(snd_ctl_elem_list_t *obj, unsigned int entries);
snd_ctl_elem_list_alloc_space = _alsa_lib.snd_ctl_elem_list_alloc_space
snd_ctl_elem_list_alloc_space.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_alloc_space.restype = c_int

#void snd_ctl_elem_list_free_space(snd_ctl_elem_list_t *obj);
snd_ctl_elem_list_free_space = _alsa_lib.snd_ctl_elem_list_free_space
snd_ctl_elem_list_free_space.argtypes = [POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_free_space.restype = None


#size_t snd_ctl_elem_id_sizeof(void);
snd_ctl_elem_id_sizeof = _alsa_lib.snd_ctl_elem_id_sizeof
snd_ctl_elem_id_sizeof.argtypes = []
snd_ctl_elem_id_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_elem_id_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_elem_id_alloca(ptr) __snd_alloca(ptr, snd_ctl_elem_id)
#int snd_ctl_elem_id_malloc(snd_ctl_elem_id_t **ptr);
snd_ctl_elem_id_malloc = _alsa_lib.snd_ctl_elem_id_malloc
snd_ctl_elem_id_malloc.argtypes = [POINTER(POINTER(snd_ctl_elem_id_t))]
snd_ctl_elem_id_malloc.restype = c_int

#void snd_ctl_elem_id_free(snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_free = _alsa_lib.snd_ctl_elem_id_free
snd_ctl_elem_id_free.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_free.restype = None

#void snd_ctl_elem_id_clear(snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_clear = _alsa_lib.snd_ctl_elem_id_clear
snd_ctl_elem_id_clear.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_clear.restype = None

#void snd_ctl_elem_id_copy(snd_ctl_elem_id_t *dst, const snd_ctl_elem_id_t *src);
snd_ctl_elem_id_copy = _alsa_lib.snd_ctl_elem_id_copy
snd_ctl_elem_id_copy.argtypes = [POINTER(snd_ctl_elem_id_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_copy.restype = None

#unsigned int snd_ctl_elem_id_get_numid(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_numid = _alsa_lib.snd_ctl_elem_id_get_numid
snd_ctl_elem_id_get_numid.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_numid.restype = c_uint

#snd_ctl_elem_iface_t snd_ctl_elem_id_get_interface(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_interface = _alsa_lib.snd_ctl_elem_id_get_interface
snd_ctl_elem_id_get_interface.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_ctl_elem_id_get_device(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_device = _alsa_lib.snd_ctl_elem_id_get_device
snd_ctl_elem_id_get_device.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_device.restype = c_uint

#unsigned int snd_ctl_elem_id_get_subdevice(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_subdevice = _alsa_lib.snd_ctl_elem_id_get_subdevice
snd_ctl_elem_id_get_subdevice.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_subdevice.restype = c_uint

#const char *snd_ctl_elem_id_get_name(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_name = _alsa_lib.snd_ctl_elem_id_get_name
snd_ctl_elem_id_get_name.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_name.restype = c_char_p

#unsigned int snd_ctl_elem_id_get_index(const snd_ctl_elem_id_t *obj);
snd_ctl_elem_id_get_index = _alsa_lib.snd_ctl_elem_id_get_index
snd_ctl_elem_id_get_index.argtypes = [POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_id_get_index.restype = c_uint

#void snd_ctl_elem_id_set_numid(snd_ctl_elem_id_t *obj, unsigned int val);
snd_ctl_elem_id_set_numid = _alsa_lib.snd_ctl_elem_id_set_numid
snd_ctl_elem_id_set_numid.argtypes = [POINTER(snd_ctl_elem_id_t), c_uint]
snd_ctl_elem_id_set_numid.restype = None

#void snd_ctl_elem_id_set_interface(snd_ctl_elem_id_t *obj, snd_ctl_elem_iface_t val);
snd_ctl_elem_id_set_interface = _alsa_lib.snd_ctl_elem_id_set_interface
snd_ctl_elem_id_set_interface.argtypes = [POINTER(snd_ctl_elem_id_t), snd_ctl_elem_iface_t]
snd_ctl_elem_id_set_interface.restype = None

#void snd_ctl_elem_id_set_device(snd_ctl_elem_id_t *obj, unsigned int val);
snd_ctl_elem_id_set_device = _alsa_lib.snd_ctl_elem_id_set_device
snd_ctl_elem_id_set_device.argtypes = [POINTER(snd_ctl_elem_id_t), c_uint]
snd_ctl_elem_id_set_device.restype = None

#void snd_ctl_elem_id_set_subdevice(snd_ctl_elem_id_t *obj, unsigned int val);
snd_ctl_elem_id_set_subdevice = _alsa_lib.snd_ctl_elem_id_set_subdevice
snd_ctl_elem_id_set_subdevice.argtypes = [POINTER(snd_ctl_elem_id_t), c_uint]
snd_ctl_elem_id_set_subdevice.restype = None

#void snd_ctl_elem_id_set_name(snd_ctl_elem_id_t *obj, const char *val);
snd_ctl_elem_id_set_name = _alsa_lib.snd_ctl_elem_id_set_name
snd_ctl_elem_id_set_name.argtypes = [POINTER(snd_ctl_elem_id_t), c_char_p]
snd_ctl_elem_id_set_name.restype = None

#void snd_ctl_elem_id_set_index(snd_ctl_elem_id_t *obj, unsigned int val);
snd_ctl_elem_id_set_index = _alsa_lib.snd_ctl_elem_id_set_index
snd_ctl_elem_id_set_index.argtypes = [POINTER(snd_ctl_elem_id_t), c_uint]
snd_ctl_elem_id_set_index.restype = None


#size_t snd_ctl_card_info_sizeof(void);
snd_ctl_card_info_sizeof = _alsa_lib.snd_ctl_card_info_sizeof
snd_ctl_card_info_sizeof.argtypes = []
snd_ctl_card_info_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_card_info_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_card_info_alloca(ptr) __snd_alloca(ptr, snd_ctl_card_info)
#int snd_ctl_card_info_malloc(snd_ctl_card_info_t **ptr);
snd_ctl_card_info_malloc = _alsa_lib.snd_ctl_card_info_malloc
snd_ctl_card_info_malloc.argtypes = [POINTER(POINTER(snd_ctl_card_info_t))]
snd_ctl_card_info_malloc.restype = c_int

#void snd_ctl_card_info_free(snd_ctl_card_info_t *obj);
snd_ctl_card_info_free = _alsa_lib.snd_ctl_card_info_free
snd_ctl_card_info_free.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_free.restype = None

#void snd_ctl_card_info_clear(snd_ctl_card_info_t *obj);
snd_ctl_card_info_clear = _alsa_lib.snd_ctl_card_info_clear
snd_ctl_card_info_clear.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_clear.restype = None

#void snd_ctl_card_info_copy(snd_ctl_card_info_t *dst, const snd_ctl_card_info_t *src);
snd_ctl_card_info_copy = _alsa_lib.snd_ctl_card_info_copy
snd_ctl_card_info_copy.argtypes = [POINTER(snd_ctl_card_info_t), POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_copy.restype = None

#int snd_ctl_card_info_get_card(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_card = _alsa_lib.snd_ctl_card_info_get_card
snd_ctl_card_info_get_card.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_card.restype = c_int

#const char *snd_ctl_card_info_get_id(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_id = _alsa_lib.snd_ctl_card_info_get_id
snd_ctl_card_info_get_id.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_id.restype = c_char_p

#const char *snd_ctl_card_info_get_driver(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_driver = _alsa_lib.snd_ctl_card_info_get_driver
snd_ctl_card_info_get_driver.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_driver.restype = c_char_p

#const char *snd_ctl_card_info_get_name(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_name = _alsa_lib.snd_ctl_card_info_get_name
snd_ctl_card_info_get_name.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_name.restype = c_char_p

#const char *snd_ctl_card_info_get_longname(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_longname = _alsa_lib.snd_ctl_card_info_get_longname
snd_ctl_card_info_get_longname.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_longname.restype = c_char_p

#const char *snd_ctl_card_info_get_mixername(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_mixername = _alsa_lib.snd_ctl_card_info_get_mixername
snd_ctl_card_info_get_mixername.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_mixername.restype = c_char_p

#const char *snd_ctl_card_info_get_components(const snd_ctl_card_info_t *obj);
snd_ctl_card_info_get_components = _alsa_lib.snd_ctl_card_info_get_components
snd_ctl_card_info_get_components.argtypes = [POINTER(snd_ctl_card_info_t)]
snd_ctl_card_info_get_components.restype = c_char_p


#size_t snd_ctl_event_sizeof(void);
snd_ctl_event_sizeof = _alsa_lib.snd_ctl_event_sizeof
snd_ctl_event_sizeof.argtypes = []
snd_ctl_event_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_event_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_event_alloca(ptr) __snd_alloca(ptr, snd_ctl_event)
#int snd_ctl_event_malloc(snd_ctl_event_t **ptr);
snd_ctl_event_malloc = _alsa_lib.snd_ctl_event_malloc
snd_ctl_event_malloc.argtypes = [POINTER(POINTER(snd_ctl_event_t))]
snd_ctl_event_malloc.restype = c_int

#void snd_ctl_event_free(snd_ctl_event_t *obj);
snd_ctl_event_free = _alsa_lib.snd_ctl_event_free
snd_ctl_event_free.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_free.restype = None

#void snd_ctl_event_clear(snd_ctl_event_t *obj);
snd_ctl_event_clear = _alsa_lib.snd_ctl_event_clear
snd_ctl_event_clear.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_clear.restype = None

#void snd_ctl_event_copy(snd_ctl_event_t *dst, const snd_ctl_event_t *src);
snd_ctl_event_copy = _alsa_lib.snd_ctl_event_copy
snd_ctl_event_copy.argtypes = [POINTER(snd_ctl_event_t), POINTER(snd_ctl_event_t)]
snd_ctl_event_copy.restype = None

#snd_ctl_event_type_t snd_ctl_event_get_type(const snd_ctl_event_t *obj);
snd_ctl_event_get_type = _alsa_lib.snd_ctl_event_get_type
snd_ctl_event_get_type.argtypes = [POINTER(snd_ctl_event_t)]
snd_ctl_event_get_type.restype = snd_ctl_event_type_t


#size_t snd_ctl_elem_list_sizeof(void);
snd_ctl_elem_list_sizeof = _alsa_lib.snd_ctl_elem_list_sizeof
snd_ctl_elem_list_sizeof.argtypes = []
snd_ctl_elem_list_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_elem_list_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_elem_list_alloca(ptr) __snd_alloca(ptr, snd_ctl_elem_list)
#int snd_ctl_elem_list_malloc(snd_ctl_elem_list_t **ptr);
snd_ctl_elem_list_malloc = _alsa_lib.snd_ctl_elem_list_malloc
snd_ctl_elem_list_malloc.argtypes = [POINTER(POINTER(snd_ctl_elem_list_t))]
snd_ctl_elem_list_malloc.restype = c_int

#void snd_ctl_elem_list_free(snd_ctl_elem_list_t *obj);
snd_ctl_elem_list_free = _alsa_lib.snd_ctl_elem_list_free
snd_ctl_elem_list_free.argtypes = [POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_free.restype = None

#void snd_ctl_elem_list_clear(snd_ctl_elem_list_t *obj);
snd_ctl_elem_list_clear = _alsa_lib.snd_ctl_elem_list_clear
snd_ctl_elem_list_clear.argtypes = [POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_clear.restype = None

#void snd_ctl_elem_list_copy(snd_ctl_elem_list_t *dst, const snd_ctl_elem_list_t *src);
snd_ctl_elem_list_copy = _alsa_lib.snd_ctl_elem_list_copy
snd_ctl_elem_list_copy.argtypes = [POINTER(snd_ctl_elem_list_t), POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_copy.restype = None

#void snd_ctl_elem_list_set_offset(snd_ctl_elem_list_t *obj, unsigned int val);
snd_ctl_elem_list_set_offset = _alsa_lib.snd_ctl_elem_list_set_offset
snd_ctl_elem_list_set_offset.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_set_offset.restype = None

#unsigned int snd_ctl_elem_list_get_used(const snd_ctl_elem_list_t *obj);
snd_ctl_elem_list_get_used = _alsa_lib.snd_ctl_elem_list_get_used
snd_ctl_elem_list_get_used.argtypes = [POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_get_used.restype = c_uint

#unsigned int snd_ctl_elem_list_get_count(const snd_ctl_elem_list_t *obj);
snd_ctl_elem_list_get_count = _alsa_lib.snd_ctl_elem_list_get_count
snd_ctl_elem_list_get_count.argtypes = [POINTER(snd_ctl_elem_list_t)]
snd_ctl_elem_list_get_count.restype = c_uint

#void snd_ctl_elem_list_get_id(const snd_ctl_elem_list_t *obj, unsigned int idx, snd_ctl_elem_id_t *ptr);
snd_ctl_elem_list_get_id = _alsa_lib.snd_ctl_elem_list_get_id
snd_ctl_elem_list_get_id.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint, POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_list_get_id.restype = None

#unsigned int snd_ctl_elem_list_get_numid(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_numid = _alsa_lib.snd_ctl_elem_list_get_numid
snd_ctl_elem_list_get_numid.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_numid.restype = c_uint

#snd_ctl_elem_iface_t snd_ctl_elem_list_get_interface(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_interface = _alsa_lib.snd_ctl_elem_list_get_interface
snd_ctl_elem_list_get_interface.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_ctl_elem_list_get_device(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_device = _alsa_lib.snd_ctl_elem_list_get_device
snd_ctl_elem_list_get_device.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_device.restype = c_uint

#unsigned int snd_ctl_elem_list_get_subdevice(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_subdevice = _alsa_lib.snd_ctl_elem_list_get_subdevice
snd_ctl_elem_list_get_subdevice.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_subdevice.restype = c_uint

#const char *snd_ctl_elem_list_get_name(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_name = _alsa_lib.snd_ctl_elem_list_get_name
snd_ctl_elem_list_get_name.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_name.restype = c_char_p

#unsigned int snd_ctl_elem_list_get_index(const snd_ctl_elem_list_t *obj, unsigned int idx);
snd_ctl_elem_list_get_index = _alsa_lib.snd_ctl_elem_list_get_index
snd_ctl_elem_list_get_index.argtypes = [POINTER(snd_ctl_elem_list_t), c_uint]
snd_ctl_elem_list_get_index.restype = c_uint


#size_t snd_ctl_elem_info_sizeof(void);
snd_ctl_elem_info_sizeof = _alsa_lib.snd_ctl_elem_info_sizeof
snd_ctl_elem_info_sizeof.argtypes = []
snd_ctl_elem_info_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_elem_info_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_elem_info_alloca(ptr) __snd_alloca(ptr, snd_ctl_elem_info)
#int snd_ctl_elem_info_malloc(snd_ctl_elem_info_t **ptr);
snd_ctl_elem_info_malloc = _alsa_lib.snd_ctl_elem_info_malloc
snd_ctl_elem_info_malloc.argtypes = [POINTER(POINTER(snd_ctl_elem_info_t))]
snd_ctl_elem_info_malloc.restype = c_int

#void snd_ctl_elem_info_free(snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_free = _alsa_lib.snd_ctl_elem_info_free
snd_ctl_elem_info_free.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_free.restype = None

#void snd_ctl_elem_info_clear(snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_clear = _alsa_lib.snd_ctl_elem_info_clear
snd_ctl_elem_info_clear.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_clear.restype = None

#void snd_ctl_elem_info_copy(snd_ctl_elem_info_t *dst, const snd_ctl_elem_info_t *src);
snd_ctl_elem_info_copy = _alsa_lib.snd_ctl_elem_info_copy
snd_ctl_elem_info_copy.argtypes = [POINTER(snd_ctl_elem_info_t), POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_copy.restype = None

#snd_ctl_elem_type_t snd_ctl_elem_info_get_type(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_type = _alsa_lib.snd_ctl_elem_info_get_type
snd_ctl_elem_info_get_type.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_type.restype = snd_ctl_elem_type_t

#int snd_ctl_elem_info_is_readable(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_readable = _alsa_lib.snd_ctl_elem_info_is_readable
snd_ctl_elem_info_is_readable.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_readable.restype = c_int

#int snd_ctl_elem_info_is_writable(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_writable = _alsa_lib.snd_ctl_elem_info_is_writable
snd_ctl_elem_info_is_writable.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_writable.restype = c_int

#int snd_ctl_elem_info_is_volatile(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_volatile = _alsa_lib.snd_ctl_elem_info_is_volatile
snd_ctl_elem_info_is_volatile.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_volatile.restype = c_int

#int snd_ctl_elem_info_is_inactive(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_inactive = _alsa_lib.snd_ctl_elem_info_is_inactive
snd_ctl_elem_info_is_inactive.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_inactive.restype = c_int

#int snd_ctl_elem_info_is_locked(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_locked = _alsa_lib.snd_ctl_elem_info_is_locked
snd_ctl_elem_info_is_locked.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_locked.restype = c_int

#int snd_ctl_elem_info_is_tlv_readable(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_tlv_readable = _alsa_lib.snd_ctl_elem_info_is_tlv_readable
snd_ctl_elem_info_is_tlv_readable.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_tlv_readable.restype = c_int

#int snd_ctl_elem_info_is_tlv_writable(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_tlv_writable = _alsa_lib.snd_ctl_elem_info_is_tlv_writable
snd_ctl_elem_info_is_tlv_writable.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_tlv_writable.restype = c_int

#int snd_ctl_elem_info_is_tlv_commandable(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_tlv_commandable = _alsa_lib.snd_ctl_elem_info_is_tlv_commandable
snd_ctl_elem_info_is_tlv_commandable.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_tlv_commandable.restype = c_int

#int snd_ctl_elem_info_is_owner(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_owner = _alsa_lib.snd_ctl_elem_info_is_owner
snd_ctl_elem_info_is_owner.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_owner.restype = c_int

#int snd_ctl_elem_info_is_user(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_is_user = _alsa_lib.snd_ctl_elem_info_is_user
snd_ctl_elem_info_is_user.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_is_user.restype = c_int

#pid_t snd_ctl_elem_info_get_owner(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_owner = _alsa_lib.snd_ctl_elem_info_get_owner
snd_ctl_elem_info_get_owner.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_owner.restype = pid_t

#unsigned int snd_ctl_elem_info_get_count(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_count = _alsa_lib.snd_ctl_elem_info_get_count
snd_ctl_elem_info_get_count.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_count.restype = c_uint

#long snd_ctl_elem_info_get_min(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_min = _alsa_lib.snd_ctl_elem_info_get_min
snd_ctl_elem_info_get_min.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_min.restype = c_long

#long snd_ctl_elem_info_get_max(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_max = _alsa_lib.snd_ctl_elem_info_get_max
snd_ctl_elem_info_get_max.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_max.restype = c_long

#long snd_ctl_elem_info_get_step(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_step = _alsa_lib.snd_ctl_elem_info_get_step
snd_ctl_elem_info_get_step.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_step.restype = c_long

#long long snd_ctl_elem_info_get_min64(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_min64 = _alsa_lib.snd_ctl_elem_info_get_min64
snd_ctl_elem_info_get_min64.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_min64.restype = c_longlong

#long long snd_ctl_elem_info_get_max64(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_max64 = _alsa_lib.snd_ctl_elem_info_get_max64
snd_ctl_elem_info_get_max64.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_max64.restype = c_longlong

#long long snd_ctl_elem_info_get_step64(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_step64 = _alsa_lib.snd_ctl_elem_info_get_step64
snd_ctl_elem_info_get_step64.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_step64.restype = c_longlong

#unsigned int snd_ctl_elem_info_get_items(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_items = _alsa_lib.snd_ctl_elem_info_get_items
snd_ctl_elem_info_get_items.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_items.restype = c_uint

#void snd_ctl_elem_info_set_item(snd_ctl_elem_info_t *obj, unsigned int val);
snd_ctl_elem_info_set_item = _alsa_lib.snd_ctl_elem_info_set_item
snd_ctl_elem_info_set_item.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_set_item.restype = None

#const char *snd_ctl_elem_info_get_item_name(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_item_name = _alsa_lib.snd_ctl_elem_info_get_item_name
snd_ctl_elem_info_get_item_name.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_item_name.restype = c_char_p

#int snd_ctl_elem_info_get_dimensions(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_dimensions = _alsa_lib.snd_ctl_elem_info_get_dimensions
snd_ctl_elem_info_get_dimensions.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_dimensions.restype = c_int

#int snd_ctl_elem_info_get_dimension(const snd_ctl_elem_info_t *obj, unsigned int idx);
snd_ctl_elem_info_get_dimension = _alsa_lib.snd_ctl_elem_info_get_dimension
snd_ctl_elem_info_get_dimension.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_get_dimension.restype = c_int

#void snd_ctl_elem_info_get_id(const snd_ctl_elem_info_t *obj, snd_ctl_elem_id_t *ptr);
snd_ctl_elem_info_get_id = _alsa_lib.snd_ctl_elem_info_get_id
snd_ctl_elem_info_get_id.argtypes = [POINTER(snd_ctl_elem_info_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_info_get_id.restype = None

#unsigned int snd_ctl_elem_info_get_numid(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_numid = _alsa_lib.snd_ctl_elem_info_get_numid
snd_ctl_elem_info_get_numid.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_numid.restype = c_uint

#snd_ctl_elem_iface_t snd_ctl_elem_info_get_interface(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_interface = _alsa_lib.snd_ctl_elem_info_get_interface
snd_ctl_elem_info_get_interface.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_ctl_elem_info_get_device(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_device = _alsa_lib.snd_ctl_elem_info_get_device
snd_ctl_elem_info_get_device.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_device.restype = c_uint

#unsigned int snd_ctl_elem_info_get_subdevice(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_subdevice = _alsa_lib.snd_ctl_elem_info_get_subdevice
snd_ctl_elem_info_get_subdevice.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_subdevice.restype = c_uint

#const char *snd_ctl_elem_info_get_name(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_name = _alsa_lib.snd_ctl_elem_info_get_name
snd_ctl_elem_info_get_name.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_name.restype = c_char_p

#unsigned int snd_ctl_elem_info_get_index(const snd_ctl_elem_info_t *obj);
snd_ctl_elem_info_get_index = _alsa_lib.snd_ctl_elem_info_get_index
snd_ctl_elem_info_get_index.argtypes = [POINTER(snd_ctl_elem_info_t)]
snd_ctl_elem_info_get_index.restype = c_uint

#void snd_ctl_elem_info_set_id(snd_ctl_elem_info_t *obj, const snd_ctl_elem_id_t *ptr);
snd_ctl_elem_info_set_id = _alsa_lib.snd_ctl_elem_info_set_id
snd_ctl_elem_info_set_id.argtypes = [POINTER(snd_ctl_elem_info_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_info_set_id.restype = None

#void snd_ctl_elem_info_set_numid(snd_ctl_elem_info_t *obj, unsigned int val);
snd_ctl_elem_info_set_numid = _alsa_lib.snd_ctl_elem_info_set_numid
snd_ctl_elem_info_set_numid.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_set_numid.restype = None

#void snd_ctl_elem_info_set_interface(snd_ctl_elem_info_t *obj, snd_ctl_elem_iface_t val);
snd_ctl_elem_info_set_interface = _alsa_lib.snd_ctl_elem_info_set_interface
snd_ctl_elem_info_set_interface.argtypes = [POINTER(snd_ctl_elem_info_t), snd_ctl_elem_iface_t]
snd_ctl_elem_info_set_interface.restype = None

#void snd_ctl_elem_info_set_device(snd_ctl_elem_info_t *obj, unsigned int val);
snd_ctl_elem_info_set_device = _alsa_lib.snd_ctl_elem_info_set_device
snd_ctl_elem_info_set_device.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_set_device.restype = None

#void snd_ctl_elem_info_set_subdevice(snd_ctl_elem_info_t *obj, unsigned int val);
snd_ctl_elem_info_set_subdevice = _alsa_lib.snd_ctl_elem_info_set_subdevice
snd_ctl_elem_info_set_subdevice.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_set_subdevice.restype = None

#void snd_ctl_elem_info_set_name(snd_ctl_elem_info_t *obj, const char *val);
snd_ctl_elem_info_set_name = _alsa_lib.snd_ctl_elem_info_set_name
snd_ctl_elem_info_set_name.argtypes = [POINTER(snd_ctl_elem_info_t), c_char_p]
snd_ctl_elem_info_set_name.restype = None

#void snd_ctl_elem_info_set_index(snd_ctl_elem_info_t *obj, unsigned int val);
snd_ctl_elem_info_set_index = _alsa_lib.snd_ctl_elem_info_set_index
snd_ctl_elem_info_set_index.argtypes = [POINTER(snd_ctl_elem_info_t), c_uint]
snd_ctl_elem_info_set_index.restype = None


#int snd_ctl_elem_add_integer(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id, unsigned int count, long imin, long imax, long istep);
snd_ctl_elem_add_integer = _alsa_lib.snd_ctl_elem_add_integer
snd_ctl_elem_add_integer.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), c_uint, c_long, c_long, c_long]
snd_ctl_elem_add_integer.restype = c_int

#int snd_ctl_elem_add_integer64(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id, unsigned int count, long long imin, long long imax, long long istep);
snd_ctl_elem_add_integer64 = _alsa_lib.snd_ctl_elem_add_integer64
snd_ctl_elem_add_integer64.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), c_uint, c_longlong, c_longlong, c_longlong]
snd_ctl_elem_add_integer64.restype = c_int

#int snd_ctl_elem_add_boolean(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id, unsigned int count);
snd_ctl_elem_add_boolean = _alsa_lib.snd_ctl_elem_add_boolean
snd_ctl_elem_add_boolean.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), c_uint]
snd_ctl_elem_add_boolean.restype = c_int

#int snd_ctl_elem_add_iec958(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id);
snd_ctl_elem_add_iec958 = _alsa_lib.snd_ctl_elem_add_iec958
snd_ctl_elem_add_iec958.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_add_iec958.restype = c_int

#int snd_ctl_elem_remove(snd_ctl_t *ctl, snd_ctl_elem_id_t *id);
snd_ctl_elem_remove = _alsa_lib.snd_ctl_elem_remove
snd_ctl_elem_remove.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_remove.restype = c_int


#size_t snd_ctl_elem_value_sizeof(void);
snd_ctl_elem_value_sizeof = _alsa_lib.snd_ctl_elem_value_sizeof
snd_ctl_elem_value_sizeof.argtypes = []
snd_ctl_elem_value_sizeof.restype = c_size_t

# \hideinitializer
# \brief allocate an invalid #snd_ctl_elem_value_t using standard alloca
# \param ptr returned pointer
#
#define snd_ctl_elem_value_alloca(ptr) __snd_alloca(ptr, snd_ctl_elem_value)
#int snd_ctl_elem_value_malloc(snd_ctl_elem_value_t **ptr);
snd_ctl_elem_value_malloc = _alsa_lib.snd_ctl_elem_value_malloc
snd_ctl_elem_value_malloc.argtypes = [POINTER(POINTER(snd_ctl_elem_value_t))]
snd_ctl_elem_value_malloc.restype = c_int

#void snd_ctl_elem_value_free(snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_free = _alsa_lib.snd_ctl_elem_value_free
snd_ctl_elem_value_free.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_free.restype = None

#void snd_ctl_elem_value_clear(snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_clear = _alsa_lib.snd_ctl_elem_value_clear
snd_ctl_elem_value_clear.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_clear.restype = None

#void snd_ctl_elem_value_copy(snd_ctl_elem_value_t *dst, const snd_ctl_elem_value_t *src);
snd_ctl_elem_value_copy = _alsa_lib.snd_ctl_elem_value_copy
snd_ctl_elem_value_copy.argtypes = [POINTER(snd_ctl_elem_value_t), POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_copy.restype = None

#void snd_ctl_elem_value_get_id(const snd_ctl_elem_value_t *obj, snd_ctl_elem_id_t *ptr);
snd_ctl_elem_value_get_id = _alsa_lib.snd_ctl_elem_value_get_id
snd_ctl_elem_value_get_id.argtypes = [POINTER(snd_ctl_elem_value_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_value_get_id.restype = None

#unsigned int snd_ctl_elem_value_get_numid(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_numid = _alsa_lib.snd_ctl_elem_value_get_numid
snd_ctl_elem_value_get_numid.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_numid.restype = c_uint

#snd_ctl_elem_iface_t snd_ctl_elem_value_get_interface(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_interface = _alsa_lib.snd_ctl_elem_value_get_interface
snd_ctl_elem_value_get_interface.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_ctl_elem_value_get_device(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_device = _alsa_lib.snd_ctl_elem_value_get_device
snd_ctl_elem_value_get_device.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_device.restype = c_uint

#unsigned int snd_ctl_elem_value_get_subdevice(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_subdevice = _alsa_lib.snd_ctl_elem_value_get_subdevice
snd_ctl_elem_value_get_subdevice.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_subdevice.restype = c_uint

#const char *snd_ctl_elem_value_get_name(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_name = _alsa_lib.snd_ctl_elem_value_get_name
snd_ctl_elem_value_get_name.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_name.restype = c_char_p

#unsigned int snd_ctl_elem_value_get_index(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_index = _alsa_lib.snd_ctl_elem_value_get_index
snd_ctl_elem_value_get_index.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_index.restype = c_uint

#void snd_ctl_elem_value_set_id(snd_ctl_elem_value_t *obj, const snd_ctl_elem_id_t *ptr);
snd_ctl_elem_value_set_id = _alsa_lib.snd_ctl_elem_value_set_id
snd_ctl_elem_value_set_id.argtypes = [POINTER(snd_ctl_elem_value_t), POINTER(snd_ctl_elem_id_t)]
snd_ctl_elem_value_set_id.restype = None

#void snd_ctl_elem_value_set_numid(snd_ctl_elem_value_t *obj, unsigned int val);
snd_ctl_elem_value_set_numid = _alsa_lib.snd_ctl_elem_value_set_numid
snd_ctl_elem_value_set_numid.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_set_numid.restype = None

#void snd_ctl_elem_value_set_interface(snd_ctl_elem_value_t *obj, snd_ctl_elem_iface_t val);
snd_ctl_elem_value_set_interface = _alsa_lib.snd_ctl_elem_value_set_interface
snd_ctl_elem_value_set_interface.argtypes = [POINTER(snd_ctl_elem_value_t), snd_ctl_elem_iface_t]
snd_ctl_elem_value_set_interface.restype = None

#void snd_ctl_elem_value_set_device(snd_ctl_elem_value_t *obj, unsigned int val);
snd_ctl_elem_value_set_device = _alsa_lib.snd_ctl_elem_value_set_device
snd_ctl_elem_value_set_device.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_set_device.restype = None

#void snd_ctl_elem_value_set_subdevice(snd_ctl_elem_value_t *obj, unsigned int val);
snd_ctl_elem_value_set_subdevice = _alsa_lib.snd_ctl_elem_value_set_subdevice
snd_ctl_elem_value_set_subdevice.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_set_subdevice.restype = None

#void snd_ctl_elem_value_set_name(snd_ctl_elem_value_t *obj, const char *val);
snd_ctl_elem_value_set_name = _alsa_lib.snd_ctl_elem_value_set_name
snd_ctl_elem_value_set_name.argtypes = [POINTER(snd_ctl_elem_value_t), c_char_p]
snd_ctl_elem_value_set_name.restype = None

#void snd_ctl_elem_value_set_index(snd_ctl_elem_value_t *obj, unsigned int val);
snd_ctl_elem_value_set_index = _alsa_lib.snd_ctl_elem_value_set_index
snd_ctl_elem_value_set_index.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_set_index.restype = None

#int snd_ctl_elem_value_get_boolean(const snd_ctl_elem_value_t *obj, unsigned int idx);
snd_ctl_elem_value_get_boolean = _alsa_lib.snd_ctl_elem_value_get_boolean
snd_ctl_elem_value_get_boolean.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_get_boolean.restype = c_int

#long snd_ctl_elem_value_get_integer(const snd_ctl_elem_value_t *obj, unsigned int idx);
snd_ctl_elem_value_get_integer = _alsa_lib.snd_ctl_elem_value_get_integer
snd_ctl_elem_value_get_integer.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_get_integer.restype = c_long

#long long snd_ctl_elem_value_get_integer64(const snd_ctl_elem_value_t *obj, unsigned int idx);
snd_ctl_elem_value_get_integer64 = _alsa_lib.snd_ctl_elem_value_get_integer64
snd_ctl_elem_value_get_integer64.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_get_integer64.restype = c_longlong

#unsigned int snd_ctl_elem_value_get_enumerated(const snd_ctl_elem_value_t *obj, unsigned int idx);
snd_ctl_elem_value_get_enumerated = _alsa_lib.snd_ctl_elem_value_get_enumerated
snd_ctl_elem_value_get_enumerated.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_get_enumerated.restype = c_uint

#unsigned char snd_ctl_elem_value_get_byte(const snd_ctl_elem_value_t *obj, unsigned int idx);
snd_ctl_elem_value_get_byte = _alsa_lib.snd_ctl_elem_value_get_byte
snd_ctl_elem_value_get_byte.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint]
snd_ctl_elem_value_get_byte.restype = c_ubyte

#void snd_ctl_elem_value_set_boolean(snd_ctl_elem_value_t *obj, unsigned int idx, long val);
snd_ctl_elem_value_set_boolean = _alsa_lib.snd_ctl_elem_value_set_boolean
snd_ctl_elem_value_set_boolean.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint, c_long]
snd_ctl_elem_value_set_boolean.restype = None

#void snd_ctl_elem_value_set_integer(snd_ctl_elem_value_t *obj, unsigned int idx, long val);
snd_ctl_elem_value_set_integer = _alsa_lib.snd_ctl_elem_value_set_integer
snd_ctl_elem_value_set_integer.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint, c_long]
snd_ctl_elem_value_set_integer.restype = None

#void snd_ctl_elem_value_set_integer64(snd_ctl_elem_value_t *obj, unsigned int idx, long long val);
snd_ctl_elem_value_set_integer64 = _alsa_lib.snd_ctl_elem_value_set_integer64
snd_ctl_elem_value_set_integer64.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint, c_longlong]
snd_ctl_elem_value_set_integer64.restype = None

#void snd_ctl_elem_value_set_enumerated(snd_ctl_elem_value_t *obj, unsigned int idx, unsigned int val);
snd_ctl_elem_value_set_enumerated = _alsa_lib.snd_ctl_elem_value_set_enumerated
snd_ctl_elem_value_set_enumerated.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint, c_uint]
snd_ctl_elem_value_set_enumerated.restype = None

#void snd_ctl_elem_value_set_byte(snd_ctl_elem_value_t *obj, unsigned int idx, unsigned char val);
snd_ctl_elem_value_set_byte = _alsa_lib.snd_ctl_elem_value_set_byte
snd_ctl_elem_value_set_byte.argtypes = [POINTER(snd_ctl_elem_value_t), c_uint, c_ubyte]
snd_ctl_elem_value_set_byte.restype = None

#void snd_ctl_elem_set_bytes(snd_ctl_elem_value_t *obj, void *data, size_t size);
snd_ctl_elem_set_bytes = _alsa_lib.snd_ctl_elem_set_bytes
snd_ctl_elem_set_bytes.argtypes = [POINTER(snd_ctl_elem_value_t), c_void_p, c_size_t]
snd_ctl_elem_set_bytes.restype = None

#const void * snd_ctl_elem_value_get_bytes(const snd_ctl_elem_value_t *obj);
snd_ctl_elem_value_get_bytes = _alsa_lib.snd_ctl_elem_value_get_bytes
snd_ctl_elem_value_get_bytes.argtypes = [POINTER(snd_ctl_elem_value_t)]
snd_ctl_elem_value_get_bytes.restype = c_void_p

#void snd_ctl_elem_value_get_iec958(const snd_ctl_elem_value_t *obj, snd_aes_iec958_t *ptr);
snd_ctl_elem_value_get_iec958 = _alsa_lib.snd_ctl_elem_value_get_iec958
snd_ctl_elem_value_get_iec958.argtypes = [POINTER(snd_ctl_elem_value_t), POINTER(snd_aes_iec958_t)]
snd_ctl_elem_value_get_iec958.restype = None

#void snd_ctl_elem_value_set_iec958(snd_ctl_elem_value_t *obj, const snd_aes_iec958_t *ptr);
snd_ctl_elem_value_set_iec958 = _alsa_lib.snd_ctl_elem_value_set_iec958
snd_ctl_elem_value_set_iec958.argtypes = [POINTER(snd_ctl_elem_value_t), POINTER(snd_aes_iec958_t)]
snd_ctl_elem_value_set_iec958.restype = None


#int snd_tlv_parse_dB_info(unsigned int *tlv, unsigned int tlv_size,
			  #unsigned int **db_tlvp);
snd_tlv_parse_dB_info = _alsa_lib.snd_tlv_parse_dB_info
snd_tlv_parse_dB_info.argtypes = [POINTER(c_uint), c_uint, POINTER(POINTER(c_uint))]
snd_tlv_parse_dB_info.restype = c_int

#int snd_tlv_get_dB_range(unsigned int *tlv, long rangemin, long rangemax,
			 #long *min, long *max);
snd_tlv_get_dB_range = _alsa_lib.snd_tlv_get_dB_range
snd_tlv_get_dB_range.argtypes = [POINTER(c_uint), c_long, c_long, POINTER(c_long), POINTER(c_long)]
snd_tlv_get_dB_range.restype = c_int

#int snd_tlv_convert_to_dB(unsigned int *tlv, long rangemin, long rangemax,
			  #long volume, long *db_gain);
snd_tlv_convert_to_dB = _alsa_lib.snd_tlv_convert_to_dB
snd_tlv_convert_to_dB.argtypes = [POINTER(c_uint), c_long, c_long, c_long, POINTER(c_long)]
snd_tlv_convert_to_dB.restype = c_int

#int snd_tlv_convert_from_dB(unsigned int *tlv, long rangemin, long rangemax,
				#long db_gain, long *value, int xdir);
snd_tlv_convert_from_dB = _alsa_lib.snd_tlv_convert_from_dB
snd_tlv_convert_from_dB.argtypes = [POINTER(c_uint), c_long, c_long, c_long, POINTER(c_long), c_int]
snd_tlv_convert_from_dB.restype = c_int

#int snd_ctl_get_dB_range(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
			 #long *min, long *max);
snd_ctl_get_dB_range = _alsa_lib.snd_ctl_get_dB_range
snd_ctl_get_dB_range.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), POINTER(c_long), POINTER(c_long)]
snd_ctl_get_dB_range.restype = c_int

#int snd_ctl_convert_to_dB(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
			  #long volume, long *db_gain);
snd_ctl_convert_to_dB = _alsa_lib.snd_ctl_convert_to_dB
snd_ctl_convert_to_dB.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), c_long, POINTER(c_long)]
snd_ctl_convert_to_dB.restype = c_int

#int snd_ctl_convert_from_dB(snd_ctl_t *ctl, const snd_ctl_elem_id_t *id,
				#long db_gain, long *value, int xdir);
snd_ctl_convert_from_dB = _alsa_lib.snd_ctl_convert_from_dB
snd_ctl_convert_from_dB.argtypes = [POINTER(snd_ctl_t), POINTER(snd_ctl_elem_id_t), c_long, POINTER(c_long), c_int]
snd_ctl_convert_from_dB.restype = c_int


#
#  \defgroup HControl High level Control Interface
#  \ingroup Control
#  The high level control interface.
#  See \ref hcontrol page for more details.
#  \{
#

# HCTL element handle 
class _snd_hctl_elem(Structure):
    _fields_ = [
            ]
snd_hctl_elem_t = _snd_hctl_elem 

# HCTL handle 
class _snd_hctl(Structure):
    _fields_ = [
            ]
snd_hctl_t = _snd_hctl 

#
# \brief Compare function for sorting HCTL elements
# \param e1 First element
# \param e2 Second element
# \return -1 if e1 < e2, 0 if e1 == e2, 1 if e1 > e2
#
#typedef int (*snd_hctl_compare_t)(const snd_hctl_elem_t *e1,
				  #const snd_hctl_elem_t *e2);
snd_hctl_compare_t = CFUNCTYPE(c_int, POINTER(snd_hctl_elem_t), POINTER(snd_hctl_elem_t))

#int snd_hctl_compare_fast(const snd_hctl_elem_t *c1,
			  #const snd_hctl_elem_t *c2);
snd_hctl_compare_fast = _alsa_lib.snd_hctl_compare_fast
snd_hctl_compare_fast.argtypes = [POINTER(snd_hctl_elem_t), POINTER(snd_hctl_elem_t)]
snd_hctl_compare_fast.restype = c_int

# 
# \brief HCTL callback function
# \param hctl HCTL handle
# \param mask event mask
# \param elem related HCTL element (if any)
# \return 0 on success otherwise a negative error code
#
#typedef int (*snd_hctl_callback_t)(snd_hctl_t *hctl,
				   #unsigned int mask,
				   #snd_hctl_elem_t *elem);
snd_hctl_callback_t = CFUNCTYPE(c_int, POINTER(snd_hctl_t), c_uint, POINTER(snd_hctl_elem_t))

# 
# \brief HCTL element callback function
# \param elem HCTL element
# \param mask event mask
# \return 0 on success otherwise a negative error code
#
#typedef int (*snd_hctl_elem_callback_t)(snd_hctl_elem_t *elem,
					#unsigned int mask);
snd_hctl_elem_callback_t = CFUNCTYPE(c_int, POINTER(snd_hctl_elem_t), c_uint)


#int snd_hctl_open(snd_hctl_t **hctl, const char *name, int mode);
snd_hctl_open = _alsa_lib.snd_hctl_open
snd_hctl_open.argtypes = [POINTER(POINTER(snd_hctl_t)), c_char_p, c_int]
snd_hctl_open.restype = c_int

#int snd_hctl_open_ctl(snd_hctl_t **hctlp, snd_ctl_t *ctl);
snd_hctl_open_ctl = _alsa_lib.snd_hctl_open_ctl
snd_hctl_open_ctl.argtypes = [POINTER(POINTER(snd_hctl_t)), POINTER(snd_ctl_t)]
snd_hctl_open_ctl.restype = c_int

#int snd_hctl_close(snd_hctl_t *hctl);
snd_hctl_close = _alsa_lib.snd_hctl_close
snd_hctl_close.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_close.restype = c_int

#int snd_hctl_nonblock(snd_hctl_t *hctl, int nonblock);
snd_hctl_nonblock = _alsa_lib.snd_hctl_nonblock
snd_hctl_nonblock.argtypes = [POINTER(snd_hctl_t), c_int]
snd_hctl_nonblock.restype = c_int

#int snd_hctl_poll_descriptors_count(snd_hctl_t *hctl);
snd_hctl_poll_descriptors_count = _alsa_lib.snd_hctl_poll_descriptors_count
snd_hctl_poll_descriptors_count.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_poll_descriptors_count.restype = c_int

#int snd_hctl_poll_descriptors(snd_hctl_t *hctl, struct pollfd *pfds, unsigned int space);
snd_hctl_poll_descriptors = _alsa_lib.snd_hctl_poll_descriptors
snd_hctl_poll_descriptors.argtypes = [POINTER(snd_hctl_t), POINTER(pollfd), c_uint]
snd_hctl_poll_descriptors.restype = c_int

#int snd_hctl_poll_descriptors_revents(snd_hctl_t *ctl, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_hctl_poll_descriptors_revents = _alsa_lib.snd_hctl_poll_descriptors_revents
snd_hctl_poll_descriptors_revents.argtypes = [POINTER(snd_hctl_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_hctl_poll_descriptors_revents.restype = c_int

#unsigned int snd_hctl_get_count(snd_hctl_t *hctl);
snd_hctl_get_count = _alsa_lib.snd_hctl_get_count
snd_hctl_get_count.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_get_count.restype = c_uint

#int snd_hctl_set_compare(snd_hctl_t *hctl, snd_hctl_compare_t hsort);
snd_hctl_set_compare = _alsa_lib.snd_hctl_set_compare
snd_hctl_set_compare.argtypes = [POINTER(snd_hctl_t), snd_hctl_compare_t]
snd_hctl_set_compare.restype = c_int

#snd_hctl_elem_t *snd_hctl_first_elem(snd_hctl_t *hctl);
snd_hctl_first_elem = _alsa_lib.snd_hctl_first_elem
snd_hctl_first_elem.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_first_elem.restype = POINTER(snd_hctl_elem_t)

#snd_hctl_elem_t *snd_hctl_last_elem(snd_hctl_t *hctl);
snd_hctl_last_elem = _alsa_lib.snd_hctl_last_elem
snd_hctl_last_elem.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_last_elem.restype = POINTER(snd_hctl_elem_t)

#snd_hctl_elem_t *snd_hctl_find_elem(snd_hctl_t *hctl, const snd_ctl_elem_id_t *id);
snd_hctl_find_elem = _alsa_lib.snd_hctl_find_elem
snd_hctl_find_elem.argtypes = [POINTER(snd_hctl_t), POINTER(snd_ctl_elem_id_t)]
snd_hctl_find_elem.restype = POINTER(snd_hctl_elem_t)

#void snd_hctl_set_callback(snd_hctl_t *hctl, snd_hctl_callback_t callback);
snd_hctl_set_callback = _alsa_lib.snd_hctl_set_callback
snd_hctl_set_callback.argtypes = [POINTER(snd_hctl_t), snd_hctl_callback_t]
snd_hctl_set_callback.restype = None

#void snd_hctl_set_callback_private(snd_hctl_t *hctl, void *data);
snd_hctl_set_callback_private = _alsa_lib.snd_hctl_set_callback_private
snd_hctl_set_callback_private.argtypes = [POINTER(snd_hctl_t), c_void_p]
snd_hctl_set_callback_private.restype = None

#void *snd_hctl_get_callback_private(snd_hctl_t *hctl);
snd_hctl_get_callback_private = _alsa_lib.snd_hctl_get_callback_private
snd_hctl_get_callback_private.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_get_callback_private.restype = c_void_p

#int snd_hctl_load(snd_hctl_t *hctl);
snd_hctl_load = _alsa_lib.snd_hctl_load
snd_hctl_load.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_load.restype = c_int

#int snd_hctl_free(snd_hctl_t *hctl);
snd_hctl_free = _alsa_lib.snd_hctl_free
snd_hctl_free.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_free.restype = c_int

#int snd_hctl_handle_events(snd_hctl_t *hctl);
snd_hctl_handle_events = _alsa_lib.snd_hctl_handle_events
snd_hctl_handle_events.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_handle_events.restype = c_int

#const char *snd_hctl_name(snd_hctl_t *hctl);
snd_hctl_name = _alsa_lib.snd_hctl_name
snd_hctl_name.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_name.restype = c_char_p

#int snd_hctl_wait(snd_hctl_t *hctl, int timeout);
snd_hctl_wait = _alsa_lib.snd_hctl_wait
snd_hctl_wait.argtypes = [POINTER(snd_hctl_t), c_int]
snd_hctl_wait.restype = c_int

#snd_ctl_t *snd_hctl_ctl(snd_hctl_t *hctl);
snd_hctl_ctl = _alsa_lib.snd_hctl_ctl
snd_hctl_ctl.argtypes = [POINTER(snd_hctl_t)]
snd_hctl_ctl.restype = POINTER(snd_ctl_t)


#snd_hctl_elem_t *snd_hctl_elem_next(snd_hctl_elem_t *elem);
snd_hctl_elem_next = _alsa_lib.snd_hctl_elem_next
snd_hctl_elem_next.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_next.restype = POINTER(snd_hctl_elem_t)

#snd_hctl_elem_t *snd_hctl_elem_prev(snd_hctl_elem_t *elem);
snd_hctl_elem_prev = _alsa_lib.snd_hctl_elem_prev
snd_hctl_elem_prev.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_prev.restype = POINTER(snd_hctl_elem_t)

#int snd_hctl_elem_info(snd_hctl_elem_t *elem, snd_ctl_elem_info_t * info);
snd_hctl_elem_info = _alsa_lib.snd_hctl_elem_info
snd_hctl_elem_info.argtypes = [POINTER(snd_hctl_elem_t), POINTER(snd_ctl_elem_info_t)]
snd_hctl_elem_info.restype = c_int

#int snd_hctl_elem_read(snd_hctl_elem_t *elem, snd_ctl_elem_value_t * value);
snd_hctl_elem_read = _alsa_lib.snd_hctl_elem_read
snd_hctl_elem_read.argtypes = [POINTER(snd_hctl_elem_t), POINTER(snd_ctl_elem_value_t)]
snd_hctl_elem_read.restype = c_int

#int snd_hctl_elem_write(snd_hctl_elem_t *elem, snd_ctl_elem_value_t * value);
snd_hctl_elem_write = _alsa_lib.snd_hctl_elem_write
snd_hctl_elem_write.argtypes = [POINTER(snd_hctl_elem_t), POINTER(snd_ctl_elem_value_t)]
snd_hctl_elem_write.restype = c_int

#int snd_hctl_elem_tlv_read(snd_hctl_elem_t *elem, unsigned int *tlv, unsigned int tlv_size);
snd_hctl_elem_tlv_read = _alsa_lib.snd_hctl_elem_tlv_read
snd_hctl_elem_tlv_read.argtypes = [POINTER(snd_hctl_elem_t), POINTER(c_uint), c_uint]
snd_hctl_elem_tlv_read.restype = c_int

#int snd_hctl_elem_tlv_write(snd_hctl_elem_t *elem, const unsigned int *tlv);
snd_hctl_elem_tlv_write = _alsa_lib.snd_hctl_elem_tlv_write
snd_hctl_elem_tlv_write.argtypes = [POINTER(snd_hctl_elem_t), POINTER(c_uint)]
snd_hctl_elem_tlv_write.restype = c_int

#int snd_hctl_elem_tlv_command(snd_hctl_elem_t *elem, const unsigned int *tlv);
snd_hctl_elem_tlv_command = _alsa_lib.snd_hctl_elem_tlv_command
snd_hctl_elem_tlv_command.argtypes = [POINTER(snd_hctl_elem_t), POINTER(c_uint)]
snd_hctl_elem_tlv_command.restype = c_int


#snd_hctl_t *snd_hctl_elem_get_hctl(snd_hctl_elem_t *elem);
snd_hctl_elem_get_hctl = _alsa_lib.snd_hctl_elem_get_hctl
snd_hctl_elem_get_hctl.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_hctl.restype = POINTER(snd_hctl_t)


#void snd_hctl_elem_get_id(const snd_hctl_elem_t *obj, snd_ctl_elem_id_t *ptr);
snd_hctl_elem_get_id = _alsa_lib.snd_hctl_elem_get_id
snd_hctl_elem_get_id.argtypes = [POINTER(snd_hctl_elem_t), POINTER(snd_ctl_elem_id_t)]
snd_hctl_elem_get_id.restype = None

#unsigned int snd_hctl_elem_get_numid(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_numid = _alsa_lib.snd_hctl_elem_get_numid
snd_hctl_elem_get_numid.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_numid.restype = c_uint

#snd_ctl_elem_iface_t snd_hctl_elem_get_interface(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_interface = _alsa_lib.snd_hctl_elem_get_interface
snd_hctl_elem_get_interface.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_interface.restype = snd_ctl_elem_iface_t

#unsigned int snd_hctl_elem_get_device(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_device = _alsa_lib.snd_hctl_elem_get_device
snd_hctl_elem_get_device.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_device.restype = c_uint

#unsigned int snd_hctl_elem_get_subdevice(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_subdevice = _alsa_lib.snd_hctl_elem_get_subdevice
snd_hctl_elem_get_subdevice.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_subdevice.restype = c_uint

#const char *snd_hctl_elem_get_name(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_name = _alsa_lib.snd_hctl_elem_get_name
snd_hctl_elem_get_name.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_name.restype = c_char_p

#unsigned int snd_hctl_elem_get_index(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_index = _alsa_lib.snd_hctl_elem_get_index
snd_hctl_elem_get_index.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_index.restype = c_uint

#void snd_hctl_elem_set_callback(snd_hctl_elem_t *obj, snd_hctl_elem_callback_t val);
snd_hctl_elem_set_callback = _alsa_lib.snd_hctl_elem_set_callback
snd_hctl_elem_set_callback.argtypes = [POINTER(snd_hctl_elem_t), snd_hctl_elem_callback_t]
snd_hctl_elem_set_callback.restype = None

#void * snd_hctl_elem_get_callback_private(const snd_hctl_elem_t *obj);
snd_hctl_elem_get_callback_private = _alsa_lib.snd_hctl_elem_get_callback_private
snd_hctl_elem_get_callback_private.argtypes = [POINTER(snd_hctl_elem_t)]
snd_hctl_elem_get_callback_private.restype = c_void_p

#void snd_hctl_elem_set_callback_private(snd_hctl_elem_t *obj, void * val);
snd_hctl_elem_set_callback_private = _alsa_lib.snd_hctl_elem_set_callback_private
snd_hctl_elem_set_callback_private.argtypes = [POINTER(snd_hctl_elem_t), c_void_p]
snd_hctl_elem_set_callback_private.restype = None


# \} 

# \} 

#
#  \defgroup SControl Setup Control Interface
#  \ingroup Control
#  The setup control interface - set or modify control elements from a configuration file.
#  \{
#

#int snd_sctl_build(snd_sctl_t **ctl, snd_ctl_t *handle, snd_config_t *config,
		   #snd_config_t *private_data, int mode);
snd_sctl_build = _alsa_lib.snd_sctl_build
snd_sctl_build.argtypes = [POINTER(POINTER(snd_sctl_t)), POINTER(snd_ctl_t), POINTER(snd_config_t), POINTER(snd_config_t), c_int]
snd_sctl_build.restype = c_int

#int snd_sctl_free(snd_sctl_t *handle);
snd_sctl_free = _alsa_lib.snd_sctl_free
snd_sctl_free.argtypes = [POINTER(snd_sctl_t)]
snd_sctl_free.restype = c_int

#int snd_sctl_install(snd_sctl_t *handle);
snd_sctl_install = _alsa_lib.snd_sctl_install
snd_sctl_install.argtypes = [POINTER(snd_sctl_t)]
snd_sctl_install.restype = c_int

#int snd_sctl_remove(snd_sctl_t *handle);
snd_sctl_remove = _alsa_lib.snd_sctl_remove
snd_sctl_remove.argtypes = [POINTER(snd_sctl_t)]
snd_sctl_remove.restype = c_int
