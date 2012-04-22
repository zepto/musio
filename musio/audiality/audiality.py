#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Audiality module.
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

""" Audiality module.

"""

from ctypes import *
from ctypes.util import find_library

from .enums import *
from .wave import *
from .commands import *

audiality_name = find_library('audiality')
if not audiality_name:
    raise Exception("libaudiality could not be found")

_audiality_lib = cdll.LoadLibrary(audiality_name)


# Get the version of the library linked. (Should match
# A_COMPILED_VERSION short of the snapshot field, if
# you're linking statically, but dynamic linking or
# loading as a module (dlopen()) gives you the version
# of the library actually loaded.

#extern AEXP Uint32 ACALL ady_lib_version(void);
ady_lib_version = _audiality_lib.ady_lib_version
ady_lib_version.argtypes = []
ady_lib_version.restype = c_int32


# Define this to get range checking in the API entry calls. 
#define	ADY_SAFE

# Limits - exceed these and things may blow up! 
ADY_MIN_OUTPUT_RATE	= 8000
ADY_MAX_OUTPUT_RATE	= 48000
ADY_MAX_MIX_RATE	= 128000
ADY_MAX_OVERSAMPLING =	16

# Sounds 
ADY_MAX_WAVES	=	128
ADY_MAX_PATCHES	=	128

# Control 
# Grous and channels; virtually no per-unit overhead. 
ADY_MAX_GROUPS	 =	8
ADY_MAX_CHANNELS =	32


#----------------------------------------------------------
	#Init/close
#----------------------------------------------------------

# Initialize audio engine. Will do nothing if called when
# the engine is already open.
#
# Returns 0 on success, or a negative value in the case
# of failure.
 
#extern AEXP int ACALL ady_open(void);
ady_open = _audiality_lib.ady_open
ady_open.argtypes = []
ady_open.restype = c_int



# Select an I/O interface.
#
# 'iface' denotes the interface to set, and 'desc' is a
# string of the format
#	"<driver>[:<arguments>]"
# where <driver> is the name of the driver to use, and
# <arguments> is a device dependent argument string for
# the driver.
#
# Mode of operation (input/output, blocking or not) is
# decided by the host, and requested through the flags
# passed to the open() call of the driver.
#
# Available drivers as of Audiality 0.1.1:
#	ossmidi		OSS(/Free) rawmidi I/O
#	osspcm		OSS(/Free) PCM audio I/O
#	alsamidi	ALSA rawmidi I/O
#	alsapcm		ALSA PCM I/O
#	sdlpcm		SDL audio output
#
# TODO for 0.1.2:
#	alsaseq		ALSA sequencer I/O
#	jackpcm		JACK audio I/O
#	directmidi	For plugin wrappers and off-line
#	directpcm	For plugin wrappers and off-line
#
# Some examples:
#	SDL audio out:	"sdlaudio"
#	OSS raw MIDI:	"ossmidi:/dev/midi00"
#	ALSA raw MIDI:	"alsamidi:hw:0,0"
#	ALSA sequencer:	"alsaseq:Audiality"
#	OSS audio:	"ossaudio:/dev/dsp"
#	Disconnected:	"" (Empty string) or NULL (no string)
#
# Defualts:
#	AI_AUDIO_IN:	NULL
#	AI_AUDIO_OUT:	"ossaudio:/dev/dsp"
#	AI_CONTROL_IN:	"ossmidi:/dev/midi00"
#	AI_CONTROL_OUT:	NULL
#
# If called while the engine is running, the affected interface
# will be closed or (re)opened as required. Note that in the
# case of audio interfaces, this may require that the engine is
# restarted, possibly with different parameters.
#
# Returns 0 on success, or a negative value in the case
# of failure.
 
#extern AEXP int ACALL ady_set_interface(ADY_interfaces iface, const char *desc);
ady_set_interface = _audiality_lib.ady_set_interface
ady_set_interface.argtypes = [ADY_interfaces, c_char_p]
ady_set_interface.restype = c_int




# Start audio engine. Can also be used for restarting
# the engine with new parameters. Will open the engine
# first if required. Any loaded sounds and patches (if
# the engine is open, that is) are unaffected.
#
# Returns 0 on success, or a negative value in the case
# of failure.
 
#extern AEXP int ACALL ady_start(int rate, int latency, int flags);
ady_start = _audiality_lib.ady_start
ady_start.argtypes = [c_int, c_int, c_int]
ady_start.restype = c_int



# "Driver" call for engine low priority housekeeping
# work. Call this "frequently" - at least ten times per
# second if possible.
#
#	Note that while this call may not do anything
#	at all on some platforms, it could provide
#	CRITICAL SERVICES to the engine on others!
#
# (Mac OS Classic would be an example of the latter;
# since the engine is running in interrupt context,
# plugins must be instantiated and destroyed in the
# context of audio_run() instead.)
#
# With "pollaudio" enabled:
#	Fills up the driver's audio buffer, calling the
#	engine callback as needed to generate data. In
#	this mode, audio_run() must be called rather
#	frequently to avoid drop-outs. (The exact
#	requirement depends on the configured latency.)
 
#extern AEXP void ACALL ady_run(void);
#ady_run = _audiality_lib.ady_run
#ady_run.argtypes = []
#ady_run.restype = None 



# Stop the audio engine. Does not unload sounds or
# patches.
 
#extern AEXP void ACALL ady_stop(void);
ady_stop = _audiality_lib.ady_stop
ady_stop.argtypes = []
ady_stop.restype = None



# Stops the audio engine if running, and then unloads
# all waves & patches.
 
#extern AEXP void ACALL ady_close(void);
ady_close = _audiality_lib.ady_close
ady_close.argtypes = []
ady_close.restype = None


#extern AEXP void ACALL ady_quality(ADY_quality quality);
ady_quality = _audiality_lib.ady_quality
ady_quality.argtypes = [ADY_quality]
ady_quality.restype = None

#extern AEXP void ACALL ady_set_limiter(float thres, float rels);
#ady_set_limiter = _audiality_lib.ady_set_limiter
#ady_set_limiter.argtypes = [c_float, c_float]
#ady_set_limiter.restype = None



# Patch Construction (low level)
 
#extern AEXP void ACALL ady_patch_param(int pid, int param, int arg);
ady_patch_param = _audiality_lib.ady_patch_param
ady_patch_param.argtypes = [c_int, c_int, c_int]
ady_patch_param.restype = None

#extern AEXP void ACALL ady_patch_paramf(int pid, int param, float arg);
#ady_patch_paramf = _audiality_lib.ady_patch_paramf
#ady_patch_paramf.argtypes = [c_int, c_int, c_float]
#ady_patch_paramf.restype = None

#extern AEXP void ACALL ady_patch_control(int pid, int layer, int ctl, int arg);
#ady_patch_control = _audiality_lib.ady_patch_control
#ady_patch_control.argtypes = [c_int, c_int, c_int, c_int]
#ady_patch_control.restype = None 

#extern AEXP void ACALL ady_patch_controlf(int pid, int layer, int ctl, float arg);
#ady_patch_controlf = _audiality_lib.ady_patch_controlf
#ady_patch_controlf.argtypes = [c_int, c_int, c_int, c_float]
#ady_patch_controlf.restype = None



# Debugging functions implemented only in debug builds.
 
#extern AEXP void ACALL ady_print_info(void);
ady_print_info = _audiality_lib.ady_print_info
ady_print_info.argtypes = []
ady_print_info.restype = None



# Old or temporary crap that will probably go away.
 
#extern AEXP void ACALL ady_sleep(int ms);
ady_sleep = _audiality_lib.ady_sleep
ady_sleep.argtypes = [c_int]
ady_sleep.restype = None

