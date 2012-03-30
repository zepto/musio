#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth event.
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


""" Fluidsynth event.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

from .fluid_types import *

#
# @file event.h
# @brief Sequencer event functions and defines.
#
# Functions and constants for creating/processing sequencer events.
#

#
# Sequencer event type enumeration.
#
fluid_seq_event_type = c_int
FLUID_SEQ_NOTE = 0		# *< Note event with duration 
FLUID_SEQ_NOTEON = 1		# *< Note on event 
FLUID_SEQ_NOTEOFF = 2		# *< Note off event 
FLUID_SEQ_ALLSOUNDSOFF = 3	# *< All sounds off event 
FLUID_SEQ_ALLNOTESOFF = 4	# *< All notes off event 
FLUID_SEQ_BANKSELECT = 5		# *< Bank select message 
FLUID_SEQ_PROGRAMCHANGE = 6	# *< Program change message 
FLUID_SEQ_PROGRAMSELECT = 7	# *< Program select message (DOCME) 
FLUID_SEQ_PITCHBEND = 8		# *< Pitch bend message 
FLUID_SEQ_PITCHWHEELSENS = 9	# *< Pitch wheel sensitivity set message @since 1.1.0 was mispelled previously 
FLUID_SEQ_MODULATION = 10		# *< Modulation controller event 
FLUID_SEQ_SUSTAIN = 11		# *< Sustain controller event 
FLUID_SEQ_CONTROLCHANGE = 12	# *< MIDI control change event 
FLUID_SEQ_PAN = 13		# *< Stereo pan set event 
FLUID_SEQ_VOLUME = 14		# *< Volume set event 
FLUID_SEQ_REVERBSEND = 15		# *< Reverb send set event 
FLUID_SEQ_CHORUSSEND = 16		# *< Chorus send set event 
FLUID_SEQ_TIMER = 17		# *< Timer event (DOCME) 
FLUID_SEQ_ANYCONTROLCHANGE = 18	# *< DOCME (used for remove_events only) 
FLUID_SEQ_CHANNELPRESSURE = 19    # *< Channel aftertouch event @since 1.1.0 
FLUID_SEQ_SYSTEMRESET = 20        # *< System reset event @since 1.1.0 
FLUID_SEQ_UNREGISTERING = 21      # *< Called when a sequencer client is being unregistered. @since 1.1.0 
FLUID_SEQ_LASTEVENT = 22	# *< Defines the count of event enums 


FLUID_SEQ_PITCHWHHELSENS =      FLUID_SEQ_PITCHWHEELSENS       # *< Old deprecated misspelling of #FLUID_SEQ_PITCHWHEELSENS 

# Event alloc/free 
#FLUIDSYNTH_API fluid_event_t* new_fluid_event(void);
new_fluid_event = _fluid_lib.new_fluid_event
new_fluid_event.argtypes = []
new_fluid_event.restype = POINTER(fluid_event_t)

#FLUIDSYNTH_API void delete_fluid_event(fluid_event_t* evt);
delete_fluid_event = _fluid_lib.delete_fluid_event
delete_fluid_event.argtypes = [POINTER(fluid_event_t)]
delete_fluid_event.restype = None


# Initializing events 
#FLUIDSYNTH_API void fluid_event_set_source(fluid_event_t* evt, short src);
fluid_event_set_source = _fluid_lib.fluid_event_set_source
fluid_event_set_source.argtypes = [POINTER(fluid_event_t), c_short]
fluid_event_set_source.restype = None

#FLUIDSYNTH_API void fluid_event_set_dest(fluid_event_t* evt, short dest);
fluid_event_set_dest = _fluid_lib.fluid_event_set_dest
fluid_event_set_dest.argtypes = [POINTER(fluid_event_t), c_short]
fluid_event_set_dest.restype = None


# Timer events 
#FLUIDSYNTH_API void fluid_event_timer(fluid_event_t* evt, void* data);
fluid_event_timer = _fluid_lib.fluid_event_timer
fluid_event_timer.argtypes = [POINTER(fluid_event_t), c_void_p]
fluid_event_timer.restype = None


# Note events 
#FLUIDSYNTH_API void fluid_event_note(fluid_event_t* evt, int channel, 
				   #short key, short vel, 
				   #unsigned int duration);
fluid_event_note = _fluid_lib.fluid_event_note
fluid_event_note.argtypes = [POINTER(fluid_event_t), c_int, c_short, c_short, c_uint]
fluid_event_note.restype = None


#FLUIDSYNTH_API void fluid_event_noteon(fluid_event_t* evt, int channel, short key, short vel);
fluid_event_noteon = _fluid_lib.fluid_event_noteon
fluid_event_noteon.argtypes = [POINTER(fluid_event_t), c_int, c_short, c_short]
fluid_event_noteon.restype = None

#FLUIDSYNTH_API void fluid_event_noteoff(fluid_event_t* evt, int channel, short key);
fluid_event_noteoff = _fluid_lib.fluid_event_noteoff
fluid_event_noteoff.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_noteoff.restype = None

#FLUIDSYNTH_API void fluid_event_all_sounds_off(fluid_event_t* evt, int channel);
fluid_event_all_sounds_off = _fluid_lib.fluid_event_all_sounds_off
fluid_event_all_sounds_off.argtypes = [POINTER(fluid_event_t), c_int]
fluid_event_all_sounds_off.restype = None

#FLUIDSYNTH_API void fluid_event_all_notes_off(fluid_event_t* evt, int channel);
fluid_event_all_notes_off = _fluid_lib.fluid_event_all_notes_off
fluid_event_all_notes_off.argtypes = [POINTER(fluid_event_t), c_int]
fluid_event_all_notes_off.restype = None


# Instrument selection 
#FLUIDSYNTH_API void fluid_event_bank_select(fluid_event_t* evt, int channel, short bank_num);
fluid_event_bank_select = _fluid_lib.fluid_event_bank_select
fluid_event_bank_select.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_bank_select.restype = None

#FLUIDSYNTH_API void fluid_event_program_change(fluid_event_t* evt, int channel, short preset_num);
fluid_event_program_change = _fluid_lib.fluid_event_program_change
fluid_event_program_change.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_program_change.restype = None

#FLUIDSYNTH_API void fluid_event_program_select(fluid_event_t* evt, int channel, unsigned int sfont_id, short bank_num, short preset_num);
fluid_event_program_select = _fluid_lib.fluid_event_program_select
fluid_event_program_select.argtypes = [POINTER(fluid_event_t), c_int, c_uint, c_short, c_short]
fluid_event_program_select.restype = None


# Real-time generic instrument controllers 
#FLUIDSYNTH_API 
#void fluid_event_control_change(fluid_event_t* evt, int channel, short control, short val);
fluid_event_control_change = _fluid_lib.fluid_event_control_change
fluid_event_control_change.argtypes = [POINTER(fluid_event_t), c_int, c_short, c_short]
fluid_event_control_change.restype = None


# Real-time instrument controllers shortcuts 
#FLUIDSYNTH_API void fluid_event_pitch_bend(fluid_event_t* evt, int channel, int val);
fluid_event_pitch_bend = _fluid_lib.fluid_event_pitch_bend
fluid_event_pitch_bend.argtypes = [POINTER(fluid_event_t), c_int, c_int]
fluid_event_pitch_bend.restype = None

#FLUIDSYNTH_API void fluid_event_pitch_wheelsens(fluid_event_t* evt, int channel, short val);
fluid_event_pitch_wheelsens = _fluid_lib.fluid_event_pitch_wheelsens
fluid_event_pitch_wheelsens.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_pitch_wheelsens.restype = None

#FLUIDSYNTH_API void fluid_event_modulation(fluid_event_t* evt, int channel, short val);
fluid_event_modulation = _fluid_lib.fluid_event_modulation
fluid_event_modulation.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_modulation.restype = None

#FLUIDSYNTH_API void fluid_event_sustain(fluid_event_t* evt, int channel, short val);
fluid_event_sustain = _fluid_lib.fluid_event_sustain
fluid_event_sustain.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_sustain.restype = None

#FLUIDSYNTH_API void fluid_event_pan(fluid_event_t* evt, int channel, short val);
fluid_event_pan = _fluid_lib.fluid_event_pan
fluid_event_pan.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_pan.restype = None

#FLUIDSYNTH_API void fluid_event_volume(fluid_event_t* evt, int channel, short val);
fluid_event_volume = _fluid_lib.fluid_event_volume
fluid_event_volume.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_volume.restype = None

#FLUIDSYNTH_API void fluid_event_reverb_send(fluid_event_t* evt, int channel, short val);
fluid_event_reverb_send = _fluid_lib.fluid_event_reverb_send
fluid_event_reverb_send.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_reverb_send.restype = None

#FLUIDSYNTH_API void fluid_event_chorus_send(fluid_event_t* evt, int channel, short val);
fluid_event_chorus_send = _fluid_lib.fluid_event_chorus_send
fluid_event_chorus_send.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_chorus_send.restype = None


#FLUIDSYNTH_API void fluid_event_channel_pressure(fluid_event_t* evt, int channel, short val);
fluid_event_channel_pressure = _fluid_lib.fluid_event_channel_pressure
fluid_event_channel_pressure.argtypes = [POINTER(fluid_event_t), c_int, c_short]
fluid_event_channel_pressure.restype = None

#FLUIDSYNTH_API void fluid_event_system_reset(fluid_event_t* evt);
fluid_event_system_reset = _fluid_lib.fluid_event_system_reset
fluid_event_system_reset.argtypes = [POINTER(fluid_event_t)]
fluid_event_system_reset.restype = None



# Only for removing events 
#FLUIDSYNTH_API void fluid_event_any_control_change(fluid_event_t* evt, int channel);
fluid_event_any_control_change = _fluid_lib.fluid_event_any_control_change
fluid_event_any_control_change.argtypes = [POINTER(fluid_event_t), c_int]
fluid_event_any_control_change.restype = None


# Only when unregistering clients 
#FLUIDSYNTH_API void fluid_event_unregistering(fluid_event_t* evt);
fluid_event_unregistering = _fluid_lib.fluid_event_unregistering
fluid_event_unregistering.argtypes = [POINTER(fluid_event_t)]
fluid_event_unregistering.restype = None


# Accessing event data 
#FLUIDSYNTH_API int fluid_event_get_type(fluid_event_t* evt);
fluid_event_get_type = _fluid_lib.fluid_event_get_type
fluid_event_get_type.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_type.restype = c_int

#FLUIDSYNTH_API short fluid_event_get_source(fluid_event_t* evt);
fluid_event_get_source = _fluid_lib.fluid_event_get_source
fluid_event_get_source.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_source.restype = c_short

#FLUIDSYNTH_API short fluid_event_get_dest(fluid_event_t* evt);
fluid_event_get_dest = _fluid_lib.fluid_event_get_dest
fluid_event_get_dest.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_dest.restype = c_short

#FLUIDSYNTH_API int fluid_event_get_channel(fluid_event_t* evt);
fluid_event_get_channel = _fluid_lib.fluid_event_get_channel
fluid_event_get_channel.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_channel.restype = c_int

#FLUIDSYNTH_API short fluid_event_get_key(fluid_event_t* evt);
fluid_event_get_key = _fluid_lib.fluid_event_get_key
fluid_event_get_key.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_key.restype = c_short

#FLUIDSYNTH_API short fluid_event_get_velocity(fluid_event_t* evt);
fluid_event_get_velocity = _fluid_lib.fluid_event_get_velocity
fluid_event_get_velocity.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_velocity.restype = c_short

#FLUIDSYNTH_API short fluid_event_get_control(fluid_event_t* evt);
fluid_event_get_control = _fluid_lib.fluid_event_get_control
fluid_event_get_control.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_control.restype = c_short

#FLUIDSYNTH_API short fluid_event_get_value(fluid_event_t* evt);
fluid_event_get_value = _fluid_lib.fluid_event_get_value
fluid_event_get_value.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_value.restype = c_short

#FLUIDSYNTH_API short fluid_event_get_program(fluid_event_t* evt);
fluid_event_get_program = _fluid_lib.fluid_event_get_program
fluid_event_get_program.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_program.restype = c_short

#FLUIDSYNTH_API void* fluid_event_get_data(fluid_event_t* evt);
fluid_event_get_data = _fluid_lib.fluid_event_get_data
fluid_event_get_data.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_data.restype = c_void_p

#FLUIDSYNTH_API unsigned int fluid_event_get_duration(fluid_event_t* evt);
fluid_event_get_duration = _fluid_lib.fluid_event_get_duration
fluid_event_get_duration.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_duration.restype = c_uint

#FLUIDSYNTH_API short fluid_event_get_bank(fluid_event_t* evt);
fluid_event_get_bank = _fluid_lib.fluid_event_get_bank
fluid_event_get_bank.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_bank.restype = c_short

#FLUIDSYNTH_API int fluid_event_get_pitch(fluid_event_t* evt);
fluid_event_get_pitch = _fluid_lib.fluid_event_get_pitch
fluid_event_get_pitch.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_pitch.restype = c_int

#FLUIDSYNTH_API unsigned int fluid_event_get_sfont_id(fluid_event_t* evt);
fluid_event_get_sfont_id = _fluid_lib.fluid_event_get_sfont_id
fluid_event_get_sfont_id.argtypes = [POINTER(fluid_event_t)]
fluid_event_get_sfont_id.restype = c_uint

