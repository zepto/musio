#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Alsa hwdep.
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


""" Alsa hwdep.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *

#
#  \defgroup HwDep Hardware Dependant Interface
#  The Hardware Dependant Interface.
#  \{
#

# dlsym version for interface entry callback 
#define SND_HWDEP_DLSYM_VERSION		_dlsym_hwdep_001

# HwDep information container 
class _snd_hwdep_info(Structure):
    _fields_ = [
            ]
snd_hwdep_info_t = _snd_hwdep_info 

# HwDep DSP status container 
class _snd_hwdep_dsp_status(Structure):
    _fields_ = [
            ]
snd_hwdep_dsp_status_t = _snd_hwdep_dsp_status 

# HwDep DSP image container 
class _snd_hwdep_dsp_image(Structure):
    _fields_ = [
            ]
snd_hwdep_dsp_image_t = _snd_hwdep_dsp_image 

# HwDep interface 
_snd_hwdep_iface = c_int
SND_HWDEP_IFACE_OPL2 = 0	# *< OPL2 raw driver 
SND_HWDEP_IFACE_OPL3 = 1	# *< OPL3 raw driver 
SND_HWDEP_IFACE_OPL4 = 2	# *< OPL4 raw driver 
SND_HWDEP_IFACE_SB16CSP = 3	# *< SB16CSP driver 
SND_HWDEP_IFACE_EMU10K1 = 4	# *< EMU10K1 driver 
SND_HWDEP_IFACE_YSS225 = 5	# *< YSS225 driver 
SND_HWDEP_IFACE_ICS2115	= 6 # *< ICS2115 driver 
SND_HWDEP_IFACE_SSCAPE = 7	# *< Ensoniq SoundScape ISA card (MC68EC000) 
SND_HWDEP_IFACE_VX = 8		# *< Digigram VX cards 
SND_HWDEP_IFACE_MIXART = 9	# *< Digigram miXart cards 
SND_HWDEP_IFACE_USX2Y = 10	# *< Tascam US122, US224 & US428 usb 
SND_HWDEP_IFACE_EMUX_WAVETABLE = 11 # *< EmuX wavetable 
SND_HWDEP_IFACE_BLUETOOTH = 12 # *< Bluetooth audio 
SND_HWDEP_IFACE_USX2Y_PCM = 13 # *< Tascam US122, US224 & US428 raw USB PCM 
SND_HWDEP_IFACE_PCXHR = 14 	# *< Digigram PCXHR 
SND_HWDEP_IFACE_SB_RC = 15	# *< SB Extigy/Audigy2NX remote control 
            
SND_HWDEP_IFACE_LAST = SND_HWDEP_IFACE_SB_RC # *< last known hwdep interface 
snd_hwdep_iface_t = _snd_hwdep_iface 

# open for reading 
SND_HWDEP_OPEN_READ = 0 # (O_RDONLY)
# open for writing 
SND_HWDEP_OPEN_WRITE = 1 # (O_WRONLY)
# open for reading and writing 
SND_HWDEP_OPEN_DUPLEX = 2 # (O_RDWR)
# open mode flag: open in nonblock mode 
SND_HWDEP_OPEN_NONBLOCK = 2048 # (O_NONBLOCK)

# HwDep handle type 
_snd_hwdep_type = c_int
# Kernel level HwDep 
SND_HWDEP_TYPE_HW = 0
# Shared memory client HwDep (not yet implemented) 
SND_HWDEP_TYPE_SHM = 1
# INET client HwDep (not yet implemented) 
SND_HWDEP_TYPE_INET = 2
snd_hwdep_type_t = _snd_hwdep_type 

# HwDep handle 
class _snd_hwdep(Structure):
    _fields_ = [
            ]
snd_hwdep_t = _snd_hwdep 

#int snd_hwdep_open(snd_hwdep_t **hwdep, const char *name, int mode);
snd_hwdep_open = _alsa_lib.snd_hwdep_open
snd_hwdep_open.argtypes = [POINTER(POINTER(snd_hwdep_t)), c_char_p, c_int]
snd_hwdep_open.restype = c_int

#int snd_hwdep_close(snd_hwdep_t *hwdep);
snd_hwdep_close = _alsa_lib.snd_hwdep_close
snd_hwdep_close.argtypes = [POINTER(snd_hwdep_t)]
snd_hwdep_close.restype = c_int

#int snd_hwdep_poll_descriptors(snd_hwdep_t *hwdep, struct pollfd *pfds, unsigned int space);
snd_hwdep_poll_descriptors = _alsa_lib.snd_hwdep_poll_descriptors
snd_hwdep_poll_descriptors.argtypes = [POINTER(snd_hwdep_t), POINTER(pollfd), c_uint]
snd_hwdep_poll_descriptors.restype = c_int

#int snd_hwdep_poll_descriptors_revents(snd_hwdep_t *hwdep, struct pollfd *pfds, unsigned int nfds, unsigned short *revents);
snd_hwdep_poll_descriptors_revents = _alsa_lib.snd_hwdep_poll_descriptors_revents
snd_hwdep_poll_descriptors_revents.argtypes = [POINTER(snd_hwdep_t), POINTER(pollfd), c_uint, POINTER(c_ushort)]
snd_hwdep_poll_descriptors_revents.restype = c_int

#int snd_hwdep_nonblock(snd_hwdep_t *hwdep, int nonblock);
snd_hwdep_nonblock = _alsa_lib.snd_hwdep_nonblock
snd_hwdep_nonblock.argtypes = [POINTER(snd_hwdep_t), c_int]
snd_hwdep_nonblock.restype = c_int

#int snd_hwdep_info(snd_hwdep_t *hwdep, snd_hwdep_info_t * info);
snd_hwdep_info = _alsa_lib.snd_hwdep_info
snd_hwdep_info.argtypes = [POINTER(snd_hwdep_t), POINTER(snd_hwdep_info_t)]
snd_hwdep_info.restype = c_int

#int snd_hwdep_dsp_status(snd_hwdep_t *hwdep, snd_hwdep_dsp_status_t *status);
snd_hwdep_dsp_status = _alsa_lib.snd_hwdep_dsp_status
snd_hwdep_dsp_status.argtypes = [POINTER(snd_hwdep_t), POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status.restype = c_int

#int snd_hwdep_dsp_load(snd_hwdep_t *hwdep, snd_hwdep_dsp_image_t *block);
snd_hwdep_dsp_load = _alsa_lib.snd_hwdep_dsp_load
snd_hwdep_dsp_load.argtypes = [POINTER(snd_hwdep_t), POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_load.restype = c_int

#int snd_hwdep_ioctl(snd_hwdep_t *hwdep, unsigned int request, void * arg);
snd_hwdep_ioctl = _alsa_lib.snd_hwdep_ioctl
snd_hwdep_ioctl.argtypes = [POINTER(snd_hwdep_t), c_uint, c_void_p]
snd_hwdep_ioctl.restype = c_int

#ssize_t snd_hwdep_write(snd_hwdep_t *hwdep, const void *buffer, size_t size);
snd_hwdep_write = _alsa_lib.snd_hwdep_write
snd_hwdep_write.argtypes = [POINTER(snd_hwdep_t), c_void_p, c_size_t]
snd_hwdep_write.restype = c_size_t

#ssize_t snd_hwdep_read(snd_hwdep_t *hwdep, void *buffer, size_t size);
snd_hwdep_read = _alsa_lib.snd_hwdep_read
snd_hwdep_read.argtypes = [POINTER(snd_hwdep_t), c_void_p, c_size_t]
snd_hwdep_read.restype = c_size_t


#size_t snd_hwdep_info_sizeof(void);
snd_hwdep_info_sizeof = _alsa_lib.snd_hwdep_info_sizeof
snd_hwdep_info_sizeof.argtypes = []
snd_hwdep_info_sizeof.restype = c_size_t

# allocate #snd_hwdep_info_t container on stack 
#define snd_hwdep_info_alloca(ptr) __snd_alloca(ptr, snd_hwdep_info)
#int snd_hwdep_info_malloc(snd_hwdep_info_t **ptr);
snd_hwdep_info_malloc = _alsa_lib.snd_hwdep_info_malloc
snd_hwdep_info_malloc.argtypes = [POINTER(POINTER(snd_hwdep_info_t))]
snd_hwdep_info_malloc.restype = c_int

#void snd_hwdep_info_free(snd_hwdep_info_t *obj);
snd_hwdep_info_free = _alsa_lib.snd_hwdep_info_free
snd_hwdep_info_free.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_free.restype = None

#void snd_hwdep_info_copy(snd_hwdep_info_t *dst, const snd_hwdep_info_t *src);
snd_hwdep_info_copy = _alsa_lib.snd_hwdep_info_copy
snd_hwdep_info_copy.argtypes = [POINTER(snd_hwdep_info_t), POINTER(snd_hwdep_info_t)]
snd_hwdep_info_copy.restype = None


#unsigned int snd_hwdep_info_get_device(const snd_hwdep_info_t *obj);
snd_hwdep_info_get_device = _alsa_lib.snd_hwdep_info_get_device
snd_hwdep_info_get_device.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_get_device.restype = c_uint

#int snd_hwdep_info_get_card(const snd_hwdep_info_t *obj);
snd_hwdep_info_get_card = _alsa_lib.snd_hwdep_info_get_card
snd_hwdep_info_get_card.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_get_card.restype = c_int

#const char *snd_hwdep_info_get_id(const snd_hwdep_info_t *obj);
snd_hwdep_info_get_id = _alsa_lib.snd_hwdep_info_get_id
snd_hwdep_info_get_id.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_get_id.restype = c_char_p

#const char *snd_hwdep_info_get_name(const snd_hwdep_info_t *obj);
snd_hwdep_info_get_name = _alsa_lib.snd_hwdep_info_get_name
snd_hwdep_info_get_name.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_get_name.restype = c_char_p

#snd_hwdep_iface_t snd_hwdep_info_get_iface(const snd_hwdep_info_t *obj);
snd_hwdep_info_get_iface = _alsa_lib.snd_hwdep_info_get_iface
snd_hwdep_info_get_iface.argtypes = [POINTER(snd_hwdep_info_t)]
snd_hwdep_info_get_iface.restype = snd_hwdep_iface_t

#void snd_hwdep_info_set_device(snd_hwdep_info_t *obj, unsigned int val);
snd_hwdep_info_set_device = _alsa_lib.snd_hwdep_info_set_device
snd_hwdep_info_set_device.argtypes = [POINTER(snd_hwdep_info_t), c_uint]
snd_hwdep_info_set_device.restype = None


#size_t snd_hwdep_dsp_status_sizeof(void);
snd_hwdep_dsp_status_sizeof = _alsa_lib.snd_hwdep_dsp_status_sizeof
snd_hwdep_dsp_status_sizeof.argtypes = []
snd_hwdep_dsp_status_sizeof.restype = c_size_t

# allocate #snd_hwdep_dsp_status_t container on stack 
#define snd_hwdep_dsp_status_alloca(ptr) __snd_alloca(ptr, snd_hwdep_dsp_status)
#int snd_hwdep_dsp_status_malloc(snd_hwdep_dsp_status_t **ptr);
snd_hwdep_dsp_status_malloc = _alsa_lib.snd_hwdep_dsp_status_malloc
snd_hwdep_dsp_status_malloc.argtypes = [POINTER(POINTER(snd_hwdep_dsp_status_t))]
snd_hwdep_dsp_status_malloc.restype = c_int

#void snd_hwdep_dsp_status_free(snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_free = _alsa_lib.snd_hwdep_dsp_status_free
snd_hwdep_dsp_status_free.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_free.restype = None

#void snd_hwdep_dsp_status_copy(snd_hwdep_dsp_status_t *dst, const snd_hwdep_dsp_status_t *src);
snd_hwdep_dsp_status_copy = _alsa_lib.snd_hwdep_dsp_status_copy
snd_hwdep_dsp_status_copy.argtypes = [POINTER(snd_hwdep_dsp_status_t), POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_copy.restype = None


#unsigned int snd_hwdep_dsp_status_get_version(const snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_get_version = _alsa_lib.snd_hwdep_dsp_status_get_version
snd_hwdep_dsp_status_get_version.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_get_version.restype = c_uint

#const char *snd_hwdep_dsp_status_get_id(const snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_get_id = _alsa_lib.snd_hwdep_dsp_status_get_id
snd_hwdep_dsp_status_get_id.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_get_id.restype = c_char_p

#unsigned int snd_hwdep_dsp_status_get_num_dsps(const snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_get_num_dsps = _alsa_lib.snd_hwdep_dsp_status_get_num_dsps
snd_hwdep_dsp_status_get_num_dsps.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_get_num_dsps.restype = c_uint

#unsigned int snd_hwdep_dsp_status_get_dsp_loaded(const snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_get_dsp_loaded = _alsa_lib.snd_hwdep_dsp_status_get_dsp_loaded
snd_hwdep_dsp_status_get_dsp_loaded.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_get_dsp_loaded.restype = c_uint

#unsigned int snd_hwdep_dsp_status_get_chip_ready(const snd_hwdep_dsp_status_t *obj);
snd_hwdep_dsp_status_get_chip_ready = _alsa_lib.snd_hwdep_dsp_status_get_chip_ready
snd_hwdep_dsp_status_get_chip_ready.argtypes = [POINTER(snd_hwdep_dsp_status_t)]
snd_hwdep_dsp_status_get_chip_ready.restype = c_uint


#size_t snd_hwdep_dsp_image_sizeof(void);
snd_hwdep_dsp_image_sizeof = _alsa_lib.snd_hwdep_dsp_image_sizeof
snd_hwdep_dsp_image_sizeof.argtypes = []
snd_hwdep_dsp_image_sizeof.restype = c_size_t

# allocate #snd_hwdep_dsp_image_t container on stack 
#define snd_hwdep_dsp_image_alloca(ptr) __snd_alloca(ptr, snd_hwdep_dsp_image)
#int snd_hwdep_dsp_image_malloc(snd_hwdep_dsp_image_t **ptr);
snd_hwdep_dsp_image_malloc = _alsa_lib.snd_hwdep_dsp_image_malloc
snd_hwdep_dsp_image_malloc.argtypes = [POINTER(POINTER(snd_hwdep_dsp_image_t))]
snd_hwdep_dsp_image_malloc.restype = c_int

#void snd_hwdep_dsp_image_free(snd_hwdep_dsp_image_t *obj);
snd_hwdep_dsp_image_free = _alsa_lib.snd_hwdep_dsp_image_free
snd_hwdep_dsp_image_free.argtypes = [POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_free.restype = None

#void snd_hwdep_dsp_image_copy(snd_hwdep_dsp_image_t *dst, const snd_hwdep_dsp_image_t *src);
snd_hwdep_dsp_image_copy = _alsa_lib.snd_hwdep_dsp_image_copy
snd_hwdep_dsp_image_copy.argtypes = [POINTER(snd_hwdep_dsp_image_t), POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_copy.restype = None


#unsigned int snd_hwdep_dsp_image_get_index(const snd_hwdep_dsp_image_t *obj);
snd_hwdep_dsp_image_get_index = _alsa_lib.snd_hwdep_dsp_image_get_index
snd_hwdep_dsp_image_get_index.argtypes = [POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_get_index.restype = c_uint

#const char *snd_hwdep_dsp_image_get_name(const snd_hwdep_dsp_image_t *obj);
snd_hwdep_dsp_image_get_name = _alsa_lib.snd_hwdep_dsp_image_get_name
snd_hwdep_dsp_image_get_name.argtypes = [POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_get_name.restype = c_char_p

#const void *snd_hwdep_dsp_image_get_image(const snd_hwdep_dsp_image_t *obj);
snd_hwdep_dsp_image_get_image = _alsa_lib.snd_hwdep_dsp_image_get_image
snd_hwdep_dsp_image_get_image.argtypes = [POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_get_image.restype = c_void_p

#size_t snd_hwdep_dsp_image_get_length(const snd_hwdep_dsp_image_t *obj);
snd_hwdep_dsp_image_get_length = _alsa_lib.snd_hwdep_dsp_image_get_length
snd_hwdep_dsp_image_get_length.argtypes = [POINTER(snd_hwdep_dsp_image_t)]
snd_hwdep_dsp_image_get_length.restype = c_size_t


#void snd_hwdep_dsp_image_set_index(snd_hwdep_dsp_image_t *obj, unsigned int _index);
snd_hwdep_dsp_image_set_index = _alsa_lib.snd_hwdep_dsp_image_set_index
snd_hwdep_dsp_image_set_index.argtypes = [POINTER(snd_hwdep_dsp_image_t), c_uint]
snd_hwdep_dsp_image_set_index.restype = None

#void snd_hwdep_dsp_image_set_name(snd_hwdep_dsp_image_t *obj, const char *name);
snd_hwdep_dsp_image_set_name = _alsa_lib.snd_hwdep_dsp_image_set_name
snd_hwdep_dsp_image_set_name.argtypes = [POINTER(snd_hwdep_dsp_image_t), c_char_p]
snd_hwdep_dsp_image_set_name.restype = None

#void snd_hwdep_dsp_image_set_image(snd_hwdep_dsp_image_t *obj, void *buffer);
snd_hwdep_dsp_image_set_image = _alsa_lib.snd_hwdep_dsp_image_set_image
snd_hwdep_dsp_image_set_image.argtypes = [POINTER(snd_hwdep_dsp_image_t), c_void_p]
snd_hwdep_dsp_image_set_image.restype = None

#void snd_hwdep_dsp_image_set_length(snd_hwdep_dsp_image_t *obj, size_t length);
snd_hwdep_dsp_image_set_length = _alsa_lib.snd_hwdep_dsp_image_set_length
snd_hwdep_dsp_image_set_length.argtypes = [POINTER(snd_hwdep_dsp_image_t), c_size_t]
snd_hwdep_dsp_image_set_length.restype = None
