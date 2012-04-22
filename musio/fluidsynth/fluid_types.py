#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth types.
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


""" Fluidsynth types.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))


#
# @file types.h
# @brief Type declarations
#

#typedef struct _fluid_hashtable_t fluid_settings_t;             *< Configuration settings instance 
class _fluid_hashtable_t(Structure):
    _fields_ = [
            ]
fluid_settings_t = _fluid_hashtable_t

#typedef struct _fluid_synth_t fluid_synth_t;                    *< Synthesizer instance 
class _fluid_synth_t(Structure):
    _fields_ = [
            ]
fluid_synth_t = _fluid_synth_t

#typedef struct _fluid_synth_channel_info_t fluid_synth_channel_info_t;  *< SoundFont channel info 
class _fluid_synth_channel_info_t(Structure):
    _fields_ = [
            ]
fluid_synth_channel_info_t = _fluid_synth_channel_info_t 

#typedef struct _fluid_voice_t fluid_voice_t;                    *< Synthesis voice instance 
class _fluid_voice_t(Structure):
    _fields_ = [
            ]
fluid_voice_t = _fluid_voice_t 

#typedef struct _fluid_sfloader_t fluid_sfloader_t;              *< SoundFont loader plugin 
class _fluid_sfloader_t(Structure):
    _fields_ = [
            ]
fluid_sfloader_t = _fluid_sfloader_t 

#typedef struct _fluid_sfont_t fluid_sfont_t;                    *< SoundFont 
class _fluid_sfont_t(Structure):
    _fields_ = [
            ]
fluid_sfont_t = _fluid_sfont_t 

#typedef struct _fluid_preset_t fluid_preset_t;                  *< SoundFont preset 
class _fluid_preset_t(Structure):
    _fields_ = [
            ]
fluid_preset_t = _fluid_preset_t 

#typedef struct _fluid_sample_t fluid_sample_t;                  *< SoundFont sample 
class _fluid_sample_t(Structure):
    _fields_ = [
            ]
fluid_sample_t = _fluid_sample_t 

#typedef struct _fluid_mod_t fluid_mod_t;                        *< SoundFont modulator 
class _fluid_mod_t(Structure):
    _fields_ = [
            ]
fluid_mod_t = _fluid_mod_t 

#typedef struct _fluid_audio_driver_t fluid_audio_driver_t;      *< Audio driver instance 
class _fluid_audio_driver_t(Structure):
    _fields_ = [
            ]
fluid_audio_driver_t = _fluid_audio_driver_t 

#typedef struct _fluid_file_renderer_t fluid_file_renderer_t;    *< Audio file renderer instance 
class _fluid_file_renderer_t(Structure):
    _fields_ = [
            ]
fluid_file_renderer_t = _fluid_file_renderer_t 

#typedef struct _fluid_player_t fluid_player_t;                  *< MIDI player instance 
class _fluid_player_t(Structure):
    _fields_ = [
            ]
fluid_player_t = _fluid_player_t

#typedef struct _fluid_midi_event_t fluid_midi_event_t;          *< MIDI event 
class _fluid_midi_event_t(Structure):
    _fields_ = [
            ]
fluid_midi_event_t = _fluid_midi_event_t 

#typedef struct _fluid_midi_driver_t fluid_midi_driver_t;        *< MIDI driver instance 
class _fluid_midi_driver_t(Structure):
    _fields_ = [
            ]
fluid_midi_driver_t = _fluid_midi_driver_t 

#typedef struct _fluid_midi_router_t fluid_midi_router_t;        *< MIDI router instance 
class _fluid_midi_router_t(Structure):
    _fields_ = [
            ]
fluid_midi_router_t = _fluid_midi_router_t 

#typedef struct _fluid_midi_router_rule_t fluid_midi_router_rule_t;      *< MIDI router rule 
class _fluid_midi_router_rule_t(Structure):
    _fields_ = [
            ]
fluid_midi_router_rule_t = _fluid_midi_router_rule_t 

#typedef struct _fluid_hashtable_t fluid_cmd_handler_t;          *< Command handler 
fluid_cmd_handler_t = _fluid_hashtable_t

#typedef struct _fluid_shell_t fluid_shell_t;                    *< Command shell 
class _fluid_shell_t(Structure):
    _fields_ = [
            ]
fluid_shell_t = _fluid_shell_t 

#typedef struct _fluid_server_t fluid_server_t;                  *< TCP/IP shell server instance 
class _fluid_server_t(Structure):
    _fields_ = [
            ]
fluid_server_t = _fluid_server_t 

#typedef struct _fluid_event_t fluid_event_t;                    *< Sequencer event 
class _fluid_event_t(Structure):
    _fields_ = [
            ]
fluid_event_t = _fluid_event_t 

#typedef struct _fluid_sequencer_t fluid_sequencer_t;            *< Sequencer instance 
class _fluid_sequencer_t(Structure):
    _fields_ = [
            ]
fluid_sequencer_t = _fluid_sequencer_t 

#typedef struct _fluid_ramsfont_t fluid_ramsfont_t;              *< RAM SoundFont 
class _fluid_ramsfont_t(Structure):
    _fields_ = [
            ]
fluid_ramsfont_t = _fluid_ramsfont_t 

#typedef struct _fluid_rampreset_t fluid_rampreset_t;            *< RAM SoundFont preset 
class _fluid_rampreset_t(Structure):
    _fields_ = [
            ]
fluid_rampreset_t = _fluid_rampreset_t 


#typedef int fluid_istream_t;    *< Input stream descriptor 
fluid_istream_t = c_int
#typedef int fluid_ostream_t;    *< Output stream descriptor 
fluid_ostream_t = c_int

