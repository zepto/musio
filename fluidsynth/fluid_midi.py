#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth midi.
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


""" Fluidsynth midi.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

from .fluid_types import *

#
# @file midi.h
# @brief Functions for MIDI events, drivers and MIDI file playback.
#

#FLUIDSYNTH_API fluid_midi_event_t* new_fluid_midi_event(void);
new_fluid_midi_event = _fluid_lib.new_fluid_midi_event
new_fluid_midi_event.argtypes = []
new_fluid_midi_event.restype = POINTER(fluid_midi_event_t)

#FLUIDSYNTH_API int delete_fluid_midi_event(fluid_midi_event_t* event);
delete_fluid_midi_event = _fluid_lib.delete_fluid_midi_event
delete_fluid_midi_event.argtypes = [POINTER(fluid_midi_event_t)]
delete_fluid_midi_event.restype = c_int


#FLUIDSYNTH_API int fluid_midi_event_set_type(fluid_midi_event_t* evt, int type);
fluid_midi_event_set_type = _fluid_lib.fluid_midi_event_set_type
fluid_midi_event_set_type.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_type.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_type(fluid_midi_event_t* evt);
fluid_midi_event_get_type = _fluid_lib.fluid_midi_event_get_type
fluid_midi_event_get_type.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_type.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_channel(fluid_midi_event_t* evt, int chan);
fluid_midi_event_set_channel = _fluid_lib.fluid_midi_event_set_channel
fluid_midi_event_set_channel.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_channel.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_channel(fluid_midi_event_t* evt);
fluid_midi_event_get_channel = _fluid_lib.fluid_midi_event_get_channel
fluid_midi_event_get_channel.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_channel.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_key(fluid_midi_event_t* evt);
fluid_midi_event_get_key = _fluid_lib.fluid_midi_event_get_key
fluid_midi_event_get_key.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_key.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_key(fluid_midi_event_t* evt, int key);
fluid_midi_event_set_key = _fluid_lib.fluid_midi_event_set_key
fluid_midi_event_set_key.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_key.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_velocity(fluid_midi_event_t* evt);
fluid_midi_event_get_velocity = _fluid_lib.fluid_midi_event_get_velocity
fluid_midi_event_get_velocity.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_velocity.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_velocity(fluid_midi_event_t* evt, int vel);
fluid_midi_event_set_velocity = _fluid_lib.fluid_midi_event_set_velocity
fluid_midi_event_set_velocity.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_velocity.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_control(fluid_midi_event_t* evt);
fluid_midi_event_get_control = _fluid_lib.fluid_midi_event_get_control
fluid_midi_event_get_control.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_control.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_control(fluid_midi_event_t* evt, int ctrl);
fluid_midi_event_set_control = _fluid_lib.fluid_midi_event_set_control
fluid_midi_event_set_control.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_control.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_value(fluid_midi_event_t* evt);
fluid_midi_event_get_value = _fluid_lib.fluid_midi_event_get_value
fluid_midi_event_get_value.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_value.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_value(fluid_midi_event_t* evt, int val);
fluid_midi_event_set_value = _fluid_lib.fluid_midi_event_set_value
fluid_midi_event_set_value.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_value.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_program(fluid_midi_event_t* evt);
fluid_midi_event_get_program = _fluid_lib.fluid_midi_event_get_program
fluid_midi_event_get_program.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_program.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_program(fluid_midi_event_t* evt, int val);
fluid_midi_event_set_program = _fluid_lib.fluid_midi_event_set_program
fluid_midi_event_set_program.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_program.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_get_pitch(fluid_midi_event_t* evt);
fluid_midi_event_get_pitch = _fluid_lib.fluid_midi_event_get_pitch
fluid_midi_event_get_pitch.argtypes = [POINTER(fluid_midi_event_t)]
fluid_midi_event_get_pitch.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_pitch(fluid_midi_event_t* evt, int val);
fluid_midi_event_set_pitch = _fluid_lib.fluid_midi_event_set_pitch
fluid_midi_event_set_pitch.argtypes = [POINTER(fluid_midi_event_t), c_int]
fluid_midi_event_set_pitch.restype = c_int

#FLUIDSYNTH_API int fluid_midi_event_set_sysex(fluid_midi_event_t* evt, void *data,
#int size, int dynamic);
fluid_midi_event_set_sysex = _fluid_lib.fluid_midi_event_set_sysex
fluid_midi_event_set_sysex.argtypes = [POINTER(fluid_midi_event_t), c_void_p, c_int, c_int]
fluid_midi_event_set_sysex.restype = c_int


#
# MIDI router rule type.
# @since 1.1.0
#
FLUID_MIDI_ROUTER_RULE_NOTE = 0                  # *< MIDI note rule 
FLUID_MIDI_ROUTER_RULE_CC = 1                    # *< MIDI controller rule 
FLUID_MIDI_ROUTER_RULE_PROG_CHANGE = 2           # *< MIDI program change rule 
FLUID_MIDI_ROUTER_RULE_PITCH_BEND = 3            # *< MIDI pitch bend rule 
FLUID_MIDI_ROUTER_RULE_CHANNEL_PRESSURE = 4      # *< MIDI channel pressure rule 
FLUID_MIDI_ROUTER_RULE_KEY_PRESSURE = 5          # *< MIDI key pressure rule 
FLUID_MIDI_ROUTER_RULE_COUNT = 6                 # *< Total count of rule types 
fluid_midi_router_rule_type = c_int

#
# Generic callback function for MIDI events.
# @param data User defined data pointer
# @param event The MIDI event
# @return Should return #FLUID_OK on success, #FLUID_FAILED otherwise
#
# Will be used between
# - MIDI driver and MIDI router
# - MIDI router and synth
# to communicate events.
# In the not-so-far future...
#
#typedef int (*handle_midi_event_func_t)(void* data, fluid_midi_event_t* event);
handle_midi_event_func_t = CFUNCTYPE(c_int, c_void_p, POINTER(fluid_midi_event_t))

#FLUIDSYNTH_API fluid_midi_router_t* new_fluid_midi_router(fluid_settings_t* settings,
							   #handle_midi_event_func_t handler, 
							   #void* event_handler_data); 
new_fluid_midi_router = _fluid_lib.new_fluid_midi_router
new_fluid_midi_router.argtypes = [POINTER(fluid_settings_t), handle_midi_event_func_t, c_void_p]
new_fluid_midi_router.restype = POINTER(fluid_midi_router_t)

#FLUIDSYNTH_API int delete_fluid_midi_router(fluid_midi_router_t* handler); 
delete_fluid_midi_router = _fluid_lib.delete_fluid_midi_router
delete_fluid_midi_router.argtypes = [POINTER(fluid_midi_router_t)]
delete_fluid_midi_router.restype = c_int

#FLUIDSYNTH_API int fluid_midi_router_set_default_rules (fluid_midi_router_t *router);
fluid_midi_router_set_default_rules = _fluid_lib.fluid_midi_router_set_default_rules
fluid_midi_router_set_default_rules.argtypes = [POINTER(fluid_midi_router_t)]
fluid_midi_router_set_default_rules.restype = c_int

#FLUIDSYNTH_API int fluid_midi_router_clear_rules (fluid_midi_router_t *router);
fluid_midi_router_clear_rules = _fluid_lib.fluid_midi_router_clear_rules
fluid_midi_router_clear_rules.argtypes = [POINTER(fluid_midi_router_t)]
fluid_midi_router_clear_rules.restype = c_int

#FLUIDSYNTH_API int fluid_midi_router_add_rule (fluid_midi_router_t *router,
#fluid_midi_router_rule_t *rule, int type);
fluid_midi_router_add_rule = _fluid_lib.fluid_midi_router_add_rule
fluid_midi_router_add_rule.argtypes = [POINTER(fluid_midi_router_t), POINTER(fluid_midi_router_rule_t), c_int]
fluid_midi_router_add_rule.restype = c_int

#FLUIDSYNTH_API fluid_midi_router_rule_t *new_fluid_midi_router_rule (void);
new_fluid_midi_router_rule = _fluid_lib.new_fluid_midi_router_rule
new_fluid_midi_router_rule.argtypes = []
new_fluid_midi_router_rule.restype = POINTER( fluid_midi_router_rule_t)

#FLUIDSYNTH_API void delete_fluid_midi_router_rule (fluid_midi_router_rule_t *rule);
delete_fluid_midi_router_rule = _fluid_lib.delete_fluid_midi_router_rule
delete_fluid_midi_router_rule.argtypes = [POINTER(fluid_midi_router_rule_t)]
delete_fluid_midi_router_rule.restype = None

#FLUIDSYNTH_API void fluid_midi_router_rule_set_chan (fluid_midi_router_rule_t *rule,
#int min, int max, float mul, int add);
fluid_midi_router_rule_set_chan = _fluid_lib.fluid_midi_router_rule_set_chan
fluid_midi_router_rule_set_chan.argtypes = [POINTER(fluid_midi_router_rule_t), c_int, c_int, c_float, c_int]
fluid_midi_router_rule_set_chan.restype = None

#FLUIDSYNTH_API void fluid_midi_router_rule_set_param1 (fluid_midi_router_rule_t *rule,
#int min, int max, float mul, int add);
fluid_midi_router_rule_set_param1 = _fluid_lib.fluid_midi_router_rule_set_param1
fluid_midi_router_rule_set_param1.argtypes = [POINTER(fluid_midi_router_rule_t), c_int, c_int, c_float, c_int]
fluid_midi_router_rule_set_param1.restype = None

#FLUIDSYNTH_API void fluid_midi_router_rule_set_param2 (fluid_midi_router_rule_t *rule,
#int min, int max, float mul, int add);
fluid_midi_router_rule_set_param2 = _fluid_lib.fluid_midi_router_rule_set_param2
fluid_midi_router_rule_set_param2.argtypes = [POINTER(fluid_midi_router_rule_t), c_int, c_int, c_float, c_int]
fluid_midi_router_rule_set_param2.restype = None

#FLUIDSYNTH_API int fluid_midi_router_handle_midi_event(void* data, fluid_midi_event_t* event);
fluid_midi_router_handle_midi_event = _fluid_lib.fluid_midi_router_handle_midi_event
fluid_midi_router_handle_midi_event.argtypes = [c_void_p, POINTER(fluid_midi_event_t)]
fluid_midi_router_handle_midi_event.restype = c_int

#FLUIDSYNTH_API int fluid_midi_dump_prerouter(void* data, fluid_midi_event_t* event); 
fluid_midi_dump_prerouter = _fluid_lib.fluid_midi_dump_prerouter
fluid_midi_dump_prerouter.argtypes = [c_void_p, POINTER(fluid_midi_event_t)]
fluid_midi_dump_prerouter.restype = c_int

#FLUIDSYNTH_API int fluid_midi_dump_postrouter(void* data, fluid_midi_event_t* event); 
fluid_midi_dump_postrouter = _fluid_lib.fluid_midi_dump_postrouter
fluid_midi_dump_postrouter.argtypes = [c_void_p, POINTER(fluid_midi_event_t)]
fluid_midi_dump_postrouter.restype = c_int



#FLUIDSYNTH_API 
#fluid_midi_driver_t* new_fluid_midi_driver(fluid_settings_t* settings, 
					 #handle_midi_event_func_t handler, 
					 #void* event_handler_data);
new_fluid_midi_driver = _fluid_lib.new_fluid_midi_driver
new_fluid_midi_driver.argtypes = [POINTER(fluid_settings_t), handle_midi_event_func_t, c_void_p]
new_fluid_midi_driver.restype = POINTER(fluid_midi_driver_t)


#FLUIDSYNTH_API void delete_fluid_midi_driver(fluid_midi_driver_t* driver);
delete_fluid_midi_driver = _fluid_lib.delete_fluid_midi_driver
delete_fluid_midi_driver.argtypes = [POINTER(fluid_midi_driver_t)]
delete_fluid_midi_driver.restype = None


#
# MIDI player status enum.
# @since 1.1.0
#
fluid_player_status = c_int
FLUID_PLAYER_READY = 0           # *< Player is ready 
FLUID_PLAYER_PLAYING = 1         # *< Player is currently playing 
FLUID_PLAYER_DONE = 2            # *< Player is finished playing 

#FLUIDSYNTH_API fluid_player_t* new_fluid_player(fluid_synth_t* synth);
new_fluid_player = _fluid_lib.new_fluid_player
new_fluid_player.argtypes = [POINTER(fluid_synth_t)]
new_fluid_player.restype = POINTER(fluid_player_t)

#FLUIDSYNTH_API int delete_fluid_player(fluid_player_t* player);
delete_fluid_player = _fluid_lib.delete_fluid_player
delete_fluid_player.argtypes = [POINTER(fluid_player_t)]
delete_fluid_player.restype = c_int

#FLUIDSYNTH_API int fluid_player_add(fluid_player_t* player, const char *midifile);
fluid_player_add = _fluid_lib.fluid_player_add
fluid_player_add.argtypes = [POINTER(fluid_player_t), c_char_p]
fluid_player_add.restype = c_int

#FLUIDSYNTH_API int fluid_player_play(fluid_player_t* player);
fluid_player_play = _fluid_lib.fluid_player_play
fluid_player_play.argtypes = [POINTER(fluid_player_t)]
fluid_player_play.restype = c_int

#FLUIDSYNTH_API int fluid_player_stop(fluid_player_t* player);
fluid_player_stop = _fluid_lib.fluid_player_stop
fluid_player_stop.argtypes = [POINTER(fluid_player_t)]
fluid_player_stop.restype = c_int

#FLUIDSYNTH_API int fluid_player_join(fluid_player_t* player);
fluid_player_join = _fluid_lib.fluid_player_join
fluid_player_join.argtypes = [POINTER(fluid_player_t)]
fluid_player_join.restype = c_int

#FLUIDSYNTH_API int fluid_player_set_loop(fluid_player_t* player, int loop);
fluid_player_set_loop = _fluid_lib.fluid_player_set_loop
fluid_player_set_loop.argtypes = [POINTER(fluid_player_t), c_int]
fluid_player_set_loop.restype = c_int

#FLUIDSYNTH_API int fluid_player_set_midi_tempo(fluid_player_t* player, int tempo);
fluid_player_set_midi_tempo = _fluid_lib.fluid_player_set_midi_tempo
fluid_player_set_midi_tempo.argtypes = [POINTER(fluid_player_t), c_int]
fluid_player_set_midi_tempo.restype = c_int

#FLUIDSYNTH_API int fluid_player_set_bpm(fluid_player_t* player, int bpm);
fluid_player_set_bpm = _fluid_lib.fluid_player_set_bpm
fluid_player_set_bpm.argtypes = [POINTER(fluid_player_t), c_int]
fluid_player_set_bpm.restype = c_int

#FLUIDSYNTH_API int fluid_player_get_status(fluid_player_t* player);
fluid_player_get_status = _fluid_lib.fluid_player_get_status
fluid_player_get_status.argtypes = [POINTER(fluid_player_t)]
fluid_player_get_status.restype = c_int
