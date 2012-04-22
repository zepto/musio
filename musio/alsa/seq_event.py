#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Provides access to alsa seq event.
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


""" An alsa seq event module.

"""

from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))

from .alsa_global import *

#
#  \defgroup SeqEvents Sequencer Event Definitions
#  Sequencer Event Definitions
#  \ingroup Sequencer
#  \{
#

#
# Sequencer event data type
#
snd_seq_event_type_t = c_ubyte

# Sequencer event type 
snd_seq_event_type = c_int
# system status; event data type = #snd_seq_result_t 
SND_SEQ_EVENT_SYSTEM = 0
# returned result status; event data type = #snd_seq_result_t 
SND_SEQ_EVENT_RESULT = 1

# note on and off with duration; event data type = #snd_seq_ev_note_t 
SND_SEQ_EVENT_NOTE = 5
# note on; event data type = #snd_seq_ev_note_t 
SND_SEQ_EVENT_NOTEON = 6
# note off; event data type = #snd_seq_ev_note_t 
SND_SEQ_EVENT_NOTEOFF = 7
# key pressure change (aftertouch); event data type = #snd_seq_ev_note_t 
SND_SEQ_EVENT_KEYPRESS = 8

# controller; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_CONTROLLER = 10
# program change; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_PGMCHANGE = 11
# channel pressure; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_CHANPRESS = 12
# pitchwheel; event data type = #snd_seq_ev_ctrl_t; data is from -8192 to 8191) 
SND_SEQ_EVENT_PITCHBEND = 13
# 14 bit controller value; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_CONTROL14 = 14
# 14 bit NRPN;  event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_NONREGPARAM = 15
# 14 bit RPN; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_REGPARAM = 16

# SPP with LSB and MSB values; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_SONGPOS = 20
# Song Select with song ID number; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_SONGSEL = 21
# midi time code quarter frame; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_QFRAME = 22
# SMF Time Signature event; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_TIMESIGN = 23
# SMF Key Signature event; event data type = #snd_seq_ev_ctrl_t 
SND_SEQ_EVENT_KEYSIGN = 24
        
# MIDI Real Time Start message; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_START = 30
# MIDI Real Time Continue message; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_CONTINUE = 31
# MIDI Real Time Stop message; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_STOP = 32
# Set tick queue position; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_SETPOS_TICK = 33
# Set real-time queue position; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_SETPOS_TIME = 34
# (SMF) Tempo event; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_TEMPO = 35
# MIDI Real Time Clock message; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_CLOCK = 36
# MIDI Real Time Tick message; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_TICK = 37
# Queue timer skew; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_QUEUE_SKEW = 38
# Sync position changed; event data type = #snd_seq_ev_queue_control_t 
SND_SEQ_EVENT_SYNC_POS = 39

# Tune request; event data type = none 
SND_SEQ_EVENT_TUNE_REQUEST = 40
# Reset to power-on state; event data type = none 
SND_SEQ_EVENT_RESET = 41
# Active sensing event; event data type = none 
SND_SEQ_EVENT_SENSING = 42

# Echo-back event; event data type = any type 
SND_SEQ_EVENT_ECHO = 50
# OSS emulation raw event; event data type = any type 
SND_SEQ_EVENT_OSS = 51

# New client has connected; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_CLIENT_START = 60
# Client has left the system; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_CLIENT_EXIT = 61
# Client status/info has changed; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_CLIENT_CHANGE = 62
# New port was created; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_PORT_START = 63
# Port was deleted from system; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_PORT_EXIT = 64
# Port status/info has changed; event data type = #snd_seq_addr_t 
SND_SEQ_EVENT_PORT_CHANGE = 65

# Ports connected; event data type = #snd_seq_connect_t 
SND_SEQ_EVENT_PORT_SUBSCRIBED = 66
# Ports disconnected; event data type = #snd_seq_connect_t 
SND_SEQ_EVENT_PORT_UNSUBSCRIBED = 67

# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR0 = 90
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR1 = 91
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR2 = 92
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR3 = 93
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR4 = 94
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR5 = 95
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR6 = 96
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR7 = 97
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR8 = 98
# user-defined event; event data type = any (fixed size) 
SND_SEQ_EVENT_USR9 = 99

# system exclusive data (variable length);  event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_SYSEX = 130
# error event;  event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_BOUNCE = 131
# reserved for user apps;  event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_USR_VAR0 = 135
# reserved for user apps; event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_USR_VAR1 = 136
# reserved for user apps; event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_USR_VAR2 = 137
# reserved for user apps; event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_USR_VAR3 = 138
# reserved for user apps; event data type = #snd_seq_ev_ext_t 
SND_SEQ_EVENT_USR_VAR4 = 139

# NOP; ignored in any case 
SND_SEQ_EVENT_NONE = 255


# Sequencer event address 
class snd_seq_addr(Structure):
    _fields_ = [
            ('client', c_ubyte), # *< Client id 
            ('port', c_ubyte) # *< Port id 
            ]
snd_seq_addr_t = snd_seq_addr

# Connection (subscription) between ports 
class snd_seq_connect(Structure):
    _fields_ = [
            ('sender', snd_seq_addr_t), # *< sender address 
            ('dest', snd_seq_addr_t) # *< destination address 
            ]
snd_seq_connect_t = snd_seq_connect


# Real-time data record 
class snd_seq_real_time(Structure):
    _fields_ = [
            ('tv_sec', c_uint),	# *< seconds 
            ('tv_nsec', c_uint)	# *< nanoseconds 
            ]
snd_seq_real_time_t = snd_seq_real_time

# (MIDI) Tick-time data record 
snd_seq_tick_time_t = c_uint

# unioned time stamp 
class snd_seq_timestamp(Union):
    _fields_ = [
            ('tick', snd_seq_tick_time_t), # *< tick-time 
            ('time', snd_seq_real_time) # *< real-time 
            ]
snd_seq_timestamp_t = snd_seq_timestamp


#
# Event mode flags
#
# NOTE: only 8 bits available!
#
SND_SEQ_TIME_STAMP_TICK		 = (0<<0)	# *< timestamp in clock ticks 
SND_SEQ_TIME_STAMP_REAL		 = (1<<0)	# *< timestamp in real time 
SND_SEQ_TIME_STAMP_MASK		 = (1<<0)	# *< mask for timestamp bits 

SND_SEQ_TIME_MODE_ABS		 = (0<<1)	# *< absolute timestamp 
SND_SEQ_TIME_MODE_REL		 = (1<<1)	# *< relative to current time 
SND_SEQ_TIME_MODE_MASK		 = (1<<1)	# *< mask for time mode bits 

SND_SEQ_EVENT_LENGTH_FIXED	 = (0<<2)	# *< fixed event size 
SND_SEQ_EVENT_LENGTH_VARIABLE = (1<<2)	# *< variable event size 
SND_SEQ_EVENT_LENGTH_VARUSR	 = (2<<2)	# *< variable event size - user memory space 
SND_SEQ_EVENT_LENGTH_MASK	 = (3<<2)	# *< mask for event length bits 

SND_SEQ_PRIORITY_NORMAL		 = (0<<4)	# *< normal priority 
SND_SEQ_PRIORITY_HIGH		 = (1<<4)	# *< event should be processed before others 
SND_SEQ_PRIORITY_MASK		 = (1<<4)	# *< mask for priority bits 


# Note event 
class snd_seq_ev_note(Structure):
    _fields_ = [
            ('channel', c_ubyte), #	*< channel number 
            ('note', c_ubyte),	# *< note 
            ('velocity', c_ubyte),	# *< velocity 
            ('off_velocity', c_ubyte), # *< note-off velocity; only for #SND_SEQ_EVENT_NOTE 
            ('duration', c_uint)	 # *< duration until note-off; only for #SND_SEQ_EVENT_NOTE 
            ]
snd_seq_ev_note_t = snd_seq_ev_note

# Controller event 
class snd_seq_ev_ctrl(Structure):
    _fields_ = [
            ('channel', c_ubyte), #	*< channel number 
            ('unused', c_ubyte * 3), # 	*< reserved 
            ('param', c_uint), # *< control parameter 
            ('value', c_int)	# *< control value 
            ]
snd_seq_ev_ctrl_t = snd_seq_ev_ctrl

# generic set of bytes (12x8 bit) 
class snd_seq_ev_raw8(Structure):
    _fields_ = [
	        ('d', c_ubyte * 12) # *< 8 bit value 
            ]
snd_seq_ev_raw8_t = snd_seq_ev_raw8

# generic set of integers (3x32 bit) 
class snd_seq_ev_raw32(Structure):
    _fields_ = [
            ('d', c_uint * 3) #	*< 32 bit value 
            ]
snd_seq_ev_raw32_t = snd_seq_ev_raw32

# external stored data 
class snd_seq_ev_ext(Structure):
    _fields_ = [
            ('len', c_uint), # *< length of data 
            ('ptr', c_void_p) # *< pointer to data (note: can be 64-bit) 
            ]
snd_seq_ev_ext_t = snd_seq_ev_ext

# Result events 
class snd_seq_result(Structure):
    _fields_ = [
            ('event', c_int), #	*< processed event type 
            ('result', c_int) #	*< status 
            ]
snd_seq_result_t = snd_seq_result

# Queue skew values 
class snd_seq_queue_skew(Structure):
    _fields_ = [
            ('value', c_uint), # *< skew value 
            ('base', c_uint) # *< skew base 
            ]
snd_seq_queue_skew_t = snd_seq_queue_skew

# queue timer control 
class _param(Union):
    _fields_ = [
            ('value', c_int), # *< affected value (e.g. tempo) 
            ('time', snd_seq_timestamp_t), # *< time 
            ('position', c_uint), #	*< sync position 
            ('skew', snd_seq_queue_skew_t), # *< queue skew 
            ('d32', c_uint * 2), # *< any data 
            ('d8', c_ubyte * 8), # *< any data 
            ]
param = _param

class snd_seq_ev_queue_control(Structure):
    _fields_ = [
            ('queue', c_ubyte), # *< affected queue 
            ('unused', c_ubyte * 3), # *< reserved 
            ('param', param)  # *< data value union 
            ]
snd_seq_ev_queue_control_t = snd_seq_ev_queue_control

class _data(Union):
    _fields_ = [
            ('note', snd_seq_ev_note_t), # *< note information 
            ('control', snd_seq_ev_ctrl_t), # *< MIDI control information 
            ('raw8', snd_seq_ev_raw8_t), # *< raw8 data 
            ('raw32', snd_seq_ev_raw32_t), # *< raw32 data 
            ('ext', snd_seq_ev_ext_t), # *< external data 
            ('queue', snd_seq_ev_queue_control_t), # *< queue control 
            ('time', snd_seq_timestamp_t), # *< timestamp 
            ('addr', snd_seq_addr_t), # *< address 
            ('connect', snd_seq_connect_t), # *< connect information 
            ('result', snd_seq_result_t) # *< operation result code 
            ]
data = _data

# Sequencer event 
class snd_seq_event(Structure):
    _fields_ = [
            ('type', snd_seq_event_type_t), # *< event type 
            ('flags', c_ubyte), # *< event flags 
            ('tag', c_ubyte), # *< tag 
            
            ('queue', c_ubyte), # *< schedule queue 
            ('time', snd_seq_timestamp_t), # *< schedule time 

            ('source', snd_seq_addr_t), # *< source address 
            ('dest', snd_seq_addr_t), # *< destination address 

            ('data', data) # *< event data... 
            ]
snd_seq_event_t = snd_seq_event
