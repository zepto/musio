#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides global alsa functions and structs.
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


""" Global alsa data.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

pid_t = c_int

class va_list(Structure):
    _fields_ = [
            ]

class FILE(Structure):
    _fields_ = [
            ]

class pollfd(Structure):
    _fields_ = [
            ]

class snd_shm_area(Structure):
    _fields_ = [
            ]

#
#  \defgroup Global Global defines and functions
#  Global defines and functions.
#  \par
#  The ALSA library implementation uses these macros and functions.
#  Most applications probably do not need them.
#  \{
#

#const char *snd_asoundlib_version(void);
snd_asoundlib_version = _alsa_lib.snd_asoundlib_version
snd_asoundlib_version.argtypes = []
snd_asoundlib_version.restype = c_char_p


#ifndef ATTRIBUTE_UNUSED
# do not print warning (gcc) when function parameter is not used 
#define ATTRIBUTE_UNUSED __attribute__ ((__unused__))
#endif

#ifdef PIC  dynamic build 

# \hideinitializer \brief Helper macro for #SND_DLSYM_BUILD_VERSION. 
#define __SND_DLSYM_VERSION(name, version) _ ## name ## version
#
# \hideinitializer
# \brief Appends the build version to the name of a versioned dynamic symbol.
#
#define SND_DLSYM_BUILD_VERSION(name, version) char __SND_DLSYM_VERSION(name, version);

#else  static build 

class snd_dlsym_link(Structure):
    pass
snd_dlsym_link._fields = [
        ('next', POINTER(snd_dlsym_link)),
        ('dlsym_name', c_char_p),
        ('dlsym_ptr', c_void_p)
        ]

snd_dlsym_start = POINTER(snd_dlsym_link)

# \hideinitializer \brief Helper macro for #SND_DLSYM_BUILD_VERSION. 
#define __SND_DLSYM_VERSION(prefix, name, version) _ ## prefix ## name ## version
#
# \hideinitializer
# \brief Appends the build version to the name of a versioned dynamic symbol.
#
#define SND_DLSYM_BUILD_VERSION(name, version) \
#static struct snd_dlsym_link __SND_DLSYM_VERSION(snd_dlsym_, name, version); \
#void __SND_DLSYM_VERSION(snd_dlsym_constructor_, name, version) (void) __attribute__ ((constructor)); \
#void __SND_DLSYM_VERSION(snd_dlsym_constructor_, name, version) (void) { \
#__SND_DLSYM_VERSION(snd_dlsym_, name, version).next = snd_dlsym_start; \
#__SND_DLSYM_VERSION(snd_dlsym_, name, version).dlsym_name = # name; \
#__SND_DLSYM_VERSION(snd_dlsym_, name, version).dlsym_ptr = (void *)&name; \
#snd_dlsym_start = &__SND_DLSYM_VERSION(snd_dlsym_, name, version); \
#}

#endif

#ifndef __STRING
# \brief Return 'x' argument as string 
#define __STRING(x)     #x
#endif

# \brief Returns the version of a dynamic symbol as a string. 
#define SND_DLSYM_VERSION(version) __STRING(version)

#void *snd_dlopen(const char *file, int mode);
snd_dlopen = _alsa_lib.snd_dlopen
snd_dlopen.argtypes = [c_char_p, c_int]
snd_dlopen.restype = c_void_p

#void *snd_dlsym(void *handle, const char *name, const char *version);
snd_dlsym = _alsa_lib.snd_dlsym
snd_dlsym.argtypes = [c_void_p, c_char_p, c_char_p]
snd_dlsym.restype = c_void_p

#int snd_dlclose(void *handle);
snd_dlclose = _alsa_lib.snd_dlclose
snd_dlclose.argtypes = [c_void_p]
snd_dlclose.restype = c_int



# \brief alloca helper macro. 
#define __snd_alloca(ptr,type) do { *ptr = (type##_t *) alloca(type##_sizeof()); memset(*ptr, 0, type##_sizeof()); } while (0)

#
# \brief Internal structure for an async notification client handler.
#
# The ALSA library uses a pointer to this structure as a handle to an async
# notification object. Applications don't access its contents directly.
#
class _snd_async_handler(Structure):
    _fields_ = [
            ]
snd_async_handler_t = _snd_async_handler


#
# \brief Async notification callback.
#
# See the #snd_async_add_handler function for details.
#
#typedef void (*snd_async_callback_t)(snd_async_handler_t *handler);
snd_async_callback_t = CFUNCTYPE(None, POINTER(snd_async_handler_t))

#int snd_async_add_handler(snd_async_handler_t **handler, int fd, 
			  #snd_async_callback_t callback, void *private_data);
snd_async_add_handler = _alsa_lib.snd_async_add_handler
snd_async_add_handler.argtypes = [POINTER(POINTER(snd_async_handler_t)), c_int, snd_async_callback_t, c_void_p]
snd_async_add_handler.restype = c_int

#int snd_async_del_handler(snd_async_handler_t *handler);
snd_async_del_handler = _alsa_lib.snd_async_del_handler
snd_async_del_handler.argtypes = [POINTER(snd_async_handler_t)]
snd_async_del_handler.restype = c_int

#int snd_async_handler_get_fd(snd_async_handler_t *handler);
snd_async_handler_get_fd = _alsa_lib.snd_async_handler_get_fd
snd_async_handler_get_fd.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_fd.restype = c_int

#int snd_async_handler_get_signo(snd_async_handler_t *handler);
snd_async_handler_get_signo = _alsa_lib.snd_async_handler_get_signo
snd_async_handler_get_signo.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_signo.restype = c_int

#void *snd_async_handler_get_callback_private(snd_async_handler_t *handler);
snd_async_handler_get_callback_private = _alsa_lib.snd_async_handler_get_callback_private
snd_async_handler_get_callback_private.argtypes = [POINTER(snd_async_handler_t)]
snd_async_handler_get_callback_private.restype = c_void_p


#struct snd_shm_area *snd_shm_area_create(int shmid, void *ptr);
snd_shm_area_create = _alsa_lib.snd_shm_area_create
snd_shm_area_create.argtypes = [c_int, c_void_p]
snd_shm_area_create.restype = POINTER(snd_shm_area)

#struct snd_shm_area *snd_shm_area_share(struct snd_shm_area *area);
snd_shm_area_share = _alsa_lib.snd_shm_area_share
snd_shm_area_share.argtypes = [POINTER(snd_shm_area)]
snd_shm_area_share.restype = POINTER(snd_shm_area)

#int snd_shm_area_destroy(struct snd_shm_area *area);
snd_shm_area_destroy = _alsa_lib.snd_shm_area_destroy
snd_shm_area_destroy.argtypes = [POINTER(snd_shm_area)]
snd_shm_area_destroy.restype = c_int


#int snd_user_file(const char *file, char **result);
snd_user_file = _alsa_lib.snd_user_file
snd_user_file.argtypes = [c_char_p, POINTER(c_char_p)]
snd_user_file.restype = c_int


#if !defined(_POSIX_C_SOURCE) && !defined(_POSIX_SOURCE)
class timeval(Structure):
    _fields_ = [
#time_t		tv_sec;		 seconds 
            ('tv_sec', c_long),
#long		tv_usec;	 microseconds 
            ('tv_usec', c_long)
            ]

class timespec(Structure):
    _fields_ = [
#time_t		tv_sec;		 seconds 
            ('tv_sec', c_long),
#long		tv_nsec;	 nanoseconds 
            ('tv_nsec', c_long)
            ]

# Timestamp 
snd_timestamp_t = timeval
# Hi-res timestamp 
snd_htimestamp_t = timespec
