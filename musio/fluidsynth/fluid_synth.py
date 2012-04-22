#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth synth.
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


""" Fluidsynth synth.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

from .fluid_types import *

#
# @file synth.h
# @brief Embeddable SoundFont synthesizer
#  
# You create a new synthesizer with new_fluid_synth() and you destroy
# if with delete_fluid_synth(). Use the settings structure to specify
# the synthesizer characteristics. 
#
# You have to load a SoundFont in order to hear any sound. For that
# you use the fluid_synth_sfload() function.
#
# You can use the audio driver functions described below to open
# the audio device and create a background audio thread.
#  
# The API for sending MIDI events is probably what you expect:
# fluid_synth_noteon(), fluid_synth_noteoff(), ...
#

FLUID_SYNTH_CHANNEL_INFO_NAME_SIZE = 32    # *< Length of channel info name field (including zero terminator) 

#
# Channel information structure for fluid_synth_get_channel_info().
# @since 1.1.1
#
class _fluid_synth_channel_info_t(Structure):
    _fields_ = [
            ('assigned', c_int), # *< TRUE if a preset is assigned, FALSE otherwise 
# Reserved flag bits (at the least 31) 
            ('sfont_id', c_int), # *< ID of parent SoundFont 
            ('bank', c_int), # *< MIDI bank number (0-16383) 
            ('program', c_int), # *< MIDI program number (0-127) 
            ('name', c_char * FLUID_SYNTH_CHANNEL_INFO_NAME_SIZE), # *< Channel preset name 
            ('reserved', c_char * 32) # *< Reserved data for future expansion 
            ]

#FLUIDSYNTH_API fluid_synth_t* new_fluid_synth(fluid_settings_t* settings);
new_fluid_synth = _fluid_lib.new_fluid_synth
new_fluid_synth.argtypes = [POINTER(fluid_settings_t)]
new_fluid_synth.restype = POINTER(fluid_synth_t)

#FLUIDSYNTH_API int delete_fluid_synth(fluid_synth_t* synth);
delete_fluid_synth = _fluid_lib.delete_fluid_synth
delete_fluid_synth.argtypes = [POINTER(fluid_synth_t)]
delete_fluid_synth.restype = c_int

#FLUIDSYNTH_API fluid_settings_t* fluid_synth_get_settings(fluid_synth_t* synth);
fluid_synth_get_settings = _fluid_lib.fluid_synth_get_settings
fluid_synth_get_settings.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_settings.restype = POINTER(fluid_settings_t)



# MIDI channel messages 

#FLUIDSYNTH_API int fluid_synth_noteon(fluid_synth_t* synth, int chan, int key, int vel);
fluid_synth_noteon = _fluid_lib.fluid_synth_noteon
fluid_synth_noteon.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_int]
fluid_synth_noteon.restype = c_int

#FLUIDSYNTH_API int fluid_synth_noteoff(fluid_synth_t* synth, int chan, int key);
fluid_synth_noteoff = _fluid_lib.fluid_synth_noteoff
fluid_synth_noteoff.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_noteoff.restype = c_int

#FLUIDSYNTH_API int fluid_synth_cc(fluid_synth_t* synth, int chan, int ctrl, int val);
fluid_synth_cc = _fluid_lib.fluid_synth_cc
fluid_synth_cc.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_int]
fluid_synth_cc.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_cc(fluid_synth_t* synth, int chan, int ctrl, int* pval);
fluid_synth_get_cc = _fluid_lib.fluid_synth_get_cc
fluid_synth_get_cc.argtypes = [POINTER(fluid_synth_t), c_int, c_int, POINTER(c_int)]
fluid_synth_get_cc.restype = c_int

#FLUIDSYNTH_API int fluid_synth_sysex(fluid_synth_t *synth, const char *data, int len,
#char *response, int *response_len, int *handled, int dryrun);
fluid_synth_sysex = _fluid_lib.fluid_synth_sysex
fluid_synth_sysex.argtypes = [POINTER(fluid_synth_t), c_char_p, c_int, c_char_p, POINTER(c_int), POINTER(c_int), c_int]
fluid_synth_sysex.restype = c_int

#FLUIDSYNTH_API int fluid_synth_pitch_bend(fluid_synth_t* synth, int chan, int val);
fluid_synth_pitch_bend = _fluid_lib.fluid_synth_pitch_bend
fluid_synth_pitch_bend.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_pitch_bend.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_pitch_bend(fluid_synth_t* synth, int chan, int* ppitch_bend);
fluid_synth_get_pitch_bend = _fluid_lib.fluid_synth_get_pitch_bend
fluid_synth_get_pitch_bend.argtypes = [POINTER(fluid_synth_t), c_int, POINTER(c_int)]
fluid_synth_get_pitch_bend.restype = c_int

#FLUIDSYNTH_API int fluid_synth_pitch_wheel_sens(fluid_synth_t* synth, int chan, int val);
fluid_synth_pitch_wheel_sens = _fluid_lib.fluid_synth_pitch_wheel_sens
fluid_synth_pitch_wheel_sens.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_pitch_wheel_sens.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_pitch_wheel_sens(fluid_synth_t* synth, int chan, int* pval);
fluid_synth_get_pitch_wheel_sens = _fluid_lib.fluid_synth_get_pitch_wheel_sens
fluid_synth_get_pitch_wheel_sens.argtypes = [POINTER(fluid_synth_t), c_int, POINTER(c_int)]
fluid_synth_get_pitch_wheel_sens.restype = c_int

#FLUIDSYNTH_API int fluid_synth_program_change(fluid_synth_t* synth, int chan, int program);
fluid_synth_program_change = _fluid_lib.fluid_synth_program_change
fluid_synth_program_change.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_program_change.restype = c_int

#FLUIDSYNTH_API int fluid_synth_channel_pressure(fluid_synth_t* synth, int chan, int val);
fluid_synth_channel_pressure = _fluid_lib.fluid_synth_channel_pressure
fluid_synth_channel_pressure.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_channel_pressure.restype = c_int

#FLUIDSYNTH_API int fluid_synth_bank_select(fluid_synth_t* synth, int chan, unsigned int bank);
fluid_synth_bank_select = _fluid_lib.fluid_synth_bank_select
fluid_synth_bank_select.argtypes = [POINTER(fluid_synth_t), c_int, c_uint]
fluid_synth_bank_select.restype = c_int

#FLUIDSYNTH_API int fluid_synth_sfont_select(fluid_synth_t* synth, int chan, unsigned int sfont_id);
fluid_synth_sfont_select = _fluid_lib.fluid_synth_sfont_select
fluid_synth_sfont_select.argtypes = [POINTER(fluid_synth_t), c_int, c_uint]
fluid_synth_sfont_select.restype = c_int

#FLUIDSYNTH_API
#int fluid_synth_program_select(fluid_synth_t* synth, int chan, unsigned int sfont_id,
#unsigned int bank_num, unsigned int preset_num);
fluid_synth_program_select = _fluid_lib.fluid_synth_program_select
fluid_synth_program_select.argtypes = [POINTER(fluid_synth_t), c_int, c_uint, c_uint, c_uint]
fluid_synth_program_select.restype = c_int

#FLUIDSYNTH_API int
#fluid_synth_program_select_by_sfont_name (fluid_synth_t* synth, int chan,
#const char *sfont_name, unsigned int bank_num,
#unsigned int preset_num);
fluid_synth_program_select_by_sfont_name = _fluid_lib.fluid_synth_program_select_by_sfont_name
fluid_synth_program_select_by_sfont_name.argtypes = [POINTER(fluid_synth_t), c_int, c_char_p, c_uint, c_uint]
fluid_synth_program_select_by_sfont_name.restype = c_int

#FLUIDSYNTH_API 
#int fluid_synth_get_program(fluid_synth_t* synth, int chan, unsigned int* sfont_id, 
#unsigned int* bank_num, unsigned int* preset_num);
fluid_synth_get_program = _fluid_lib.fluid_synth_get_program
fluid_synth_get_program.argtypes = [POINTER(fluid_synth_t), c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
fluid_synth_get_program.restype = c_int

#FLUIDSYNTH_API int fluid_synth_unset_program (fluid_synth_t *synth, int chan);
fluid_synth_unset_program = _fluid_lib.fluid_synth_unset_program
fluid_synth_unset_program.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_unset_program.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_channel_info (fluid_synth_t *synth, int chan,
#fluid_synth_channel_info_t *info);
fluid_synth_get_channel_info = _fluid_lib.fluid_synth_get_channel_info
fluid_synth_get_channel_info.argtypes = [POINTER(fluid_synth_t), c_int, POINTER(fluid_synth_channel_info_t)]
fluid_synth_get_channel_info.restype = c_int

#FLUIDSYNTH_API int fluid_synth_program_reset(fluid_synth_t* synth);
fluid_synth_program_reset = _fluid_lib.fluid_synth_program_reset
fluid_synth_program_reset.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_program_reset.restype = c_int

#FLUIDSYNTH_API int fluid_synth_system_reset(fluid_synth_t* synth);
fluid_synth_system_reset = _fluid_lib.fluid_synth_system_reset
fluid_synth_system_reset.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_system_reset.restype = c_int



# Low level access 
#FLUIDSYNTH_API fluid_preset_t* fluid_synth_get_channel_preset(fluid_synth_t* synth, int chan);
fluid_synth_get_channel_preset = _fluid_lib.fluid_synth_get_channel_preset
fluid_synth_get_channel_preset.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_get_channel_preset.restype = POINTER(fluid_preset_t)

#FLUIDSYNTH_API int fluid_synth_start(fluid_synth_t* synth, unsigned int id, 
					 #fluid_preset_t* preset, int audio_chan, 
					 #int midi_chan, int key, int vel);
fluid_synth_start = _fluid_lib.fluid_synth_start
fluid_synth_start.argtypes = [POINTER(fluid_synth_t), c_uint, POINTER(fluid_preset_t), c_int, c_int, c_int, c_int]
fluid_synth_start.restype = c_int

#FLUIDSYNTH_API int fluid_synth_stop(fluid_synth_t* synth, unsigned int id);
fluid_synth_stop = _fluid_lib.fluid_synth_stop
fluid_synth_stop.argtypes = [POINTER(fluid_synth_t), c_uint]
fluid_synth_stop.restype = c_int



# SoundFont management 

#FLUIDSYNTH_API 
#int fluid_synth_sfload(fluid_synth_t* synth, const char* filename, int reset_presets);
fluid_synth_sfload = _fluid_lib.fluid_synth_sfload
fluid_synth_sfload.argtypes = [POINTER(fluid_synth_t), POINTER(c_char), c_int]
fluid_synth_sfload.restype = c_int

#FLUIDSYNTH_API int fluid_synth_sfreload(fluid_synth_t* synth, unsigned int id);
fluid_synth_sfreload = _fluid_lib.fluid_synth_sfreload
fluid_synth_sfreload.argtypes = [POINTER(fluid_synth_t), c_uint]
fluid_synth_sfreload.restype = c_int

#FLUIDSYNTH_API int fluid_synth_sfunload(fluid_synth_t* synth, unsigned int id, int reset_presets);
fluid_synth_sfunload = _fluid_lib.fluid_synth_sfunload
fluid_synth_sfunload.argtypes = [POINTER(fluid_synth_t), c_uint, c_int]
fluid_synth_sfunload.restype = c_int

#FLUIDSYNTH_API int fluid_synth_add_sfont(fluid_synth_t* synth, fluid_sfont_t* sfont);
fluid_synth_add_sfont = _fluid_lib.fluid_synth_add_sfont
fluid_synth_add_sfont.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_sfont_t)]
fluid_synth_add_sfont.restype = c_int

#FLUIDSYNTH_API void fluid_synth_remove_sfont(fluid_synth_t* synth, fluid_sfont_t* sfont);
fluid_synth_remove_sfont = _fluid_lib.fluid_synth_remove_sfont
fluid_synth_remove_sfont.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_sfont_t)]
fluid_synth_remove_sfont.restype = None

#FLUIDSYNTH_API int fluid_synth_sfcount(fluid_synth_t* synth);
fluid_synth_sfcount = _fluid_lib.fluid_synth_sfcount
fluid_synth_sfcount.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_sfcount.restype = c_int

#FLUIDSYNTH_API fluid_sfont_t* fluid_synth_get_sfont(fluid_synth_t* synth, unsigned int num);
fluid_synth_get_sfont = _fluid_lib.fluid_synth_get_sfont
fluid_synth_get_sfont.argtypes = [POINTER(fluid_synth_t), c_uint]
fluid_synth_get_sfont.restype = POINTER(fluid_sfont_t)

#FLUIDSYNTH_API fluid_sfont_t* fluid_synth_get_sfont_by_id(fluid_synth_t* synth, unsigned int id);
fluid_synth_get_sfont_by_id = _fluid_lib.fluid_synth_get_sfont_by_id
fluid_synth_get_sfont_by_id.argtypes = [POINTER(fluid_synth_t), c_uint]
fluid_synth_get_sfont_by_id.restype = POINTER(fluid_sfont_t)

#FLUIDSYNTH_API fluid_sfont_t *fluid_synth_get_sfont_by_name (fluid_synth_t* synth,
#const char *name);
fluid_synth_get_sfont_by_name = _fluid_lib.fluid_synth_get_sfont_by_name
fluid_synth_get_sfont_by_name.argtypes = [POINTER(fluid_synth_t), c_char_p]
fluid_synth_get_sfont_by_name.restype = POINTER(fluid_sfont_t)

#FLUIDSYNTH_API int fluid_synth_set_bank_offset(fluid_synth_t* synth, int sfont_id, int offset);
fluid_synth_set_bank_offset = _fluid_lib.fluid_synth_set_bank_offset
fluid_synth_set_bank_offset.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_set_bank_offset.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_bank_offset(fluid_synth_t* synth, int sfont_id);
fluid_synth_get_bank_offset = _fluid_lib.fluid_synth_get_bank_offset
fluid_synth_get_bank_offset.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_get_bank_offset.restype = c_int



# Reverb  

#FLUIDSYNTH_API void fluid_synth_set_reverb(fluid_synth_t* synth, double roomsize, 
					   #double damping, double width, double level);
fluid_synth_set_reverb = _fluid_lib.fluid_synth_set_reverb
fluid_synth_set_reverb.argtypes = [POINTER(fluid_synth_t), c_double, c_double, c_double, c_double]
fluid_synth_set_reverb.restype = None

#FLUIDSYNTH_API void fluid_synth_set_reverb_on(fluid_synth_t* synth, int on);
fluid_synth_set_reverb_on = _fluid_lib.fluid_synth_set_reverb_on
fluid_synth_set_reverb_on.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_set_reverb_on.restype = None

#FLUIDSYNTH_API double fluid_synth_get_reverb_roomsize(fluid_synth_t* synth);
fluid_synth_get_reverb_roomsize = _fluid_lib.fluid_synth_get_reverb_roomsize
fluid_synth_get_reverb_roomsize.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_reverb_roomsize.restype = c_double

#FLUIDSYNTH_API double fluid_synth_get_reverb_damp(fluid_synth_t* synth);
fluid_synth_get_reverb_damp = _fluid_lib.fluid_synth_get_reverb_damp
fluid_synth_get_reverb_damp.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_reverb_damp.restype = c_double

#FLUIDSYNTH_API double fluid_synth_get_reverb_level(fluid_synth_t* synth);
fluid_synth_get_reverb_level = _fluid_lib.fluid_synth_get_reverb_level
fluid_synth_get_reverb_level.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_reverb_level.restype = c_double

#FLUIDSYNTH_API double fluid_synth_get_reverb_width(fluid_synth_t* synth);
fluid_synth_get_reverb_width = _fluid_lib.fluid_synth_get_reverb_width
fluid_synth_get_reverb_width.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_reverb_width.restype = c_double


FLUID_REVERB_DEFAULT_ROOMSIZE = 0.2      # *< Default reverb room size 
FLUID_REVERB_DEFAULT_DAMP = 0.0          # *< Default reverb damping 
FLUID_REVERB_DEFAULT_WIDTH = 0.5         # *< Default reverb width 
FLUID_REVERB_DEFAULT_LEVEL = 0.9         # *< Default reverb level 



# Chorus 

#
# Chorus modulation waveform type.
#
fluid_chorus_mod = c_int
FLUID_CHORUS_MOD_SINE = 0            # *< Sine wave chorus modulation 
FLUID_CHORUS_MOD_TRIANGLE = 1        # *< Triangle wave chorus modulation 


#FLUIDSYNTH_API void fluid_synth_set_chorus(fluid_synth_t* synth, int nr, double level, 
					 #double speed, double depth_ms, int type);
fluid_synth_set_chorus = _fluid_lib.fluid_synth_set_chorus
fluid_synth_set_chorus.argtypes = [POINTER(fluid_synth_t), c_int, c_double, c_double, c_double, c_int]
fluid_synth_set_chorus.restype = None

#FLUIDSYNTH_API void fluid_synth_set_chorus_on(fluid_synth_t* synth, int on);
fluid_synth_set_chorus_on = _fluid_lib.fluid_synth_set_chorus_on
fluid_synth_set_chorus_on.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_set_chorus_on.restype = None

#FLUIDSYNTH_API int fluid_synth_get_chorus_nr(fluid_synth_t* synth);
fluid_synth_get_chorus_nr = _fluid_lib.fluid_synth_get_chorus_nr
fluid_synth_get_chorus_nr.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_chorus_nr.restype = c_int

#FLUIDSYNTH_API double fluid_synth_get_chorus_level(fluid_synth_t* synth);
fluid_synth_get_chorus_level = _fluid_lib.fluid_synth_get_chorus_level
fluid_synth_get_chorus_level.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_chorus_level.restype = c_double

#FLUIDSYNTH_API double fluid_synth_get_chorus_speed_Hz(fluid_synth_t* synth);
fluid_synth_get_chorus_speed_Hz = _fluid_lib.fluid_synth_get_chorus_speed_Hz
fluid_synth_get_chorus_speed_Hz.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_chorus_speed_Hz.restype = c_double

#FLUIDSYNTH_API double fluid_synth_get_chorus_depth_ms(fluid_synth_t* synth);
fluid_synth_get_chorus_depth_ms = _fluid_lib.fluid_synth_get_chorus_depth_ms
fluid_synth_get_chorus_depth_ms.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_chorus_depth_ms.restype = c_double

#FLUIDSYNTH_API int fluid_synth_get_chorus_type(fluid_synth_t* synth);  see fluid_chorus_mod 
fluid_synth_get_chorus_type = _fluid_lib.fluid_synth_get_chorus_type
fluid_synth_get_chorus_type.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_chorus_type.restype = c_int


FLUID_CHORUS_DEFAULT_N = 3                             #   *< Default chorus voice count 
FLUID_CHORUS_DEFAULT_LEVEL = 2.0                       #  *< Default chorus level 
FLUID_CHORUS_DEFAULT_SPEED = 0.3                       #  *< Default chorus speed 
FLUID_CHORUS_DEFAULT_DEPTH = 8.0                       #  *< Default chorus depth 
FLUID_CHORUS_DEFAULT_TYPE = FLUID_CHORUS_MOD_SINE      #   *< Default chorus waveform type 


# Audio and MIDI channels 

#FLUIDSYNTH_API int fluid_synth_count_midi_channels(fluid_synth_t* synth);
fluid_synth_count_midi_channels = _fluid_lib.fluid_synth_count_midi_channels
fluid_synth_count_midi_channels.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_count_midi_channels.restype = c_int

#FLUIDSYNTH_API int fluid_synth_count_audio_channels(fluid_synth_t* synth);
fluid_synth_count_audio_channels = _fluid_lib.fluid_synth_count_audio_channels
fluid_synth_count_audio_channels.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_count_audio_channels.restype = c_int

#FLUIDSYNTH_API int fluid_synth_count_audio_groups(fluid_synth_t* synth);
fluid_synth_count_audio_groups = _fluid_lib.fluid_synth_count_audio_groups
fluid_synth_count_audio_groups.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_count_audio_groups.restype = c_int

#FLUIDSYNTH_API int fluid_synth_count_effects_channels(fluid_synth_t* synth);
fluid_synth_count_effects_channels = _fluid_lib.fluid_synth_count_effects_channels
fluid_synth_count_effects_channels.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_count_effects_channels.restype = c_int



# Synthesis parameters 

#FLUIDSYNTH_API void fluid_synth_set_sample_rate(fluid_synth_t* synth, float sample_rate);
fluid_synth_set_sample_rate = _fluid_lib.fluid_synth_set_sample_rate
fluid_synth_set_sample_rate.argtypes = [POINTER(fluid_synth_t), c_float]
fluid_synth_set_sample_rate.restype = None

#FLUIDSYNTH_API void fluid_synth_set_gain(fluid_synth_t* synth, float gain);
fluid_synth_set_gain = _fluid_lib.fluid_synth_set_gain
fluid_synth_set_gain.argtypes = [POINTER(fluid_synth_t), c_float]
fluid_synth_set_gain.restype = None

#FLUIDSYNTH_API float fluid_synth_get_gain(fluid_synth_t* synth);
fluid_synth_get_gain = _fluid_lib.fluid_synth_get_gain
fluid_synth_get_gain.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_gain.restype = c_float

#FLUIDSYNTH_API int fluid_synth_set_polyphony(fluid_synth_t* synth, int polyphony);
fluid_synth_set_polyphony = _fluid_lib.fluid_synth_set_polyphony
fluid_synth_set_polyphony.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_set_polyphony.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_polyphony(fluid_synth_t* synth);
fluid_synth_get_polyphony = _fluid_lib.fluid_synth_get_polyphony
fluid_synth_get_polyphony.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_polyphony.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_active_voice_count(fluid_synth_t* synth);
fluid_synth_get_active_voice_count = _fluid_lib.fluid_synth_get_active_voice_count
fluid_synth_get_active_voice_count.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_active_voice_count.restype = c_int

#FLUIDSYNTH_API int fluid_synth_get_internal_bufsize(fluid_synth_t* synth);
fluid_synth_get_internal_bufsize = _fluid_lib.fluid_synth_get_internal_bufsize
fluid_synth_get_internal_bufsize.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_internal_bufsize.restype = c_int


#FLUIDSYNTH_API 
#int fluid_synth_set_interp_method(fluid_synth_t* synth, int chan, int interp_method);
fluid_synth_set_interp_method = _fluid_lib.fluid_synth_set_interp_method
fluid_synth_set_interp_method.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_set_interp_method.restype = c_int


#
# Synthesis interpolation method.
#
fluid_interp = c_int
FLUID_INTERP_NONE = 0      #  *< No interpolation: Fastest, but questionable audio quality 
FLUID_INTERP_LINEAR = 1    #  *< Straight-line interpolation: A bit slower, reasonable audio quality 
FLUID_INTERP_4THORDER = 4  #  *< Fourth-order interpolation, good quality, the default 
FLUID_INTERP_7THORDER = 7  #  *< Seventh-order interpolation 

FLUID_INTERP_DEFAULT =  FLUID_INTERP_4THORDER  # *< Default interpolation method from #fluid_interp. 
FLUID_INTERP_HIGHEST =  FLUID_INTERP_7THORDER  # *< Highest interpolation method from #fluid_interp. 


# Generator interface 

#FLUIDSYNTH_API 
#int fluid_synth_set_gen(fluid_synth_t* synth, int chan, int param, float value);
fluid_synth_set_gen = _fluid_lib.fluid_synth_set_gen
fluid_synth_set_gen.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_float]
fluid_synth_set_gen.restype = c_int

#FLUIDSYNTH_API int fluid_synth_set_gen2 (fluid_synth_t* synth, int chan,
#int param, float value,
#int absolute, int normalized);
fluid_synth_set_gen2 = _fluid_lib.fluid_synth_set_gen2
fluid_synth_set_gen2.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_float, c_int, c_int]
fluid_synth_set_gen2.restype = c_int

#FLUIDSYNTH_API float fluid_synth_get_gen(fluid_synth_t* synth, int chan, int param);
fluid_synth_get_gen = _fluid_lib.fluid_synth_get_gen
fluid_synth_get_gen.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_get_gen.restype = c_float



# Tuning 

#FLUIDSYNTH_API 
#int fluid_synth_create_key_tuning(fluid_synth_t* synth, int bank, int prog,
				  #const char* name, const double* pitch);
fluid_synth_create_key_tuning = _fluid_lib.fluid_synth_create_key_tuning
fluid_synth_create_key_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_char_p, POINTER(c_double)]
fluid_synth_create_key_tuning.restype = c_int

#FLUIDSYNTH_API
#int fluid_synth_activate_key_tuning(fluid_synth_t* synth, int bank, int prog,
#const char* name, const double* pitch, int apply);
fluid_synth_activate_key_tuning = _fluid_lib.fluid_synth_activate_key_tuning
fluid_synth_activate_key_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_char_p, POINTER(c_double), c_int]
fluid_synth_activate_key_tuning.restype = c_int

#FLUIDSYNTH_API 
#int fluid_synth_create_octave_tuning(fluid_synth_t* synth, int bank, int prog,
#const char* name, const double* pitch);
fluid_synth_create_octave_tuning = _fluid_lib.fluid_synth_create_octave_tuning
fluid_synth_create_octave_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_char_p, POINTER(c_double)]
fluid_synth_create_octave_tuning.restype = c_int

#FLUIDSYNTH_API
#int fluid_synth_activate_octave_tuning(fluid_synth_t* synth, int bank, int prog,
#const char* name, const double* pitch, int apply);
fluid_synth_activate_octave_tuning = _fluid_lib.fluid_synth_activate_octave_tuning
fluid_synth_activate_octave_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_char_p, POINTER(c_double), c_int]
fluid_synth_activate_octave_tuning.restype = c_int

#FLUIDSYNTH_API 
#int fluid_synth_tune_notes(fluid_synth_t* synth, int bank, int prog,
			   #int len, const int *keys, const double* pitch, int apply);
fluid_synth_tune_notes = _fluid_lib.fluid_synth_tune_notes
fluid_synth_tune_notes.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_int, c_char_p, POINTER(c_double), c_int]
fluid_synth_tune_notes.restype = c_int

#FLUIDSYNTH_API 
#int fluid_synth_select_tuning(fluid_synth_t* synth, int chan, int bank, int prog);
fluid_synth_select_tuning = _fluid_lib.fluid_synth_select_tuning
fluid_synth_select_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_int]
fluid_synth_select_tuning.restype = c_int

#FLUIDSYNTH_API
#int fluid_synth_activate_tuning(fluid_synth_t* synth, int chan, int bank, int prog,
#int apply);
fluid_synth_activate_tuning = _fluid_lib.fluid_synth_activate_tuning
fluid_synth_activate_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_int, c_int]
fluid_synth_activate_tuning.restype = c_int

#FLUIDSYNTH_API int fluid_synth_reset_tuning(fluid_synth_t* synth, int chan);
fluid_synth_reset_tuning = _fluid_lib.fluid_synth_reset_tuning
fluid_synth_reset_tuning.argtypes = [POINTER(fluid_synth_t), c_int]
fluid_synth_reset_tuning.restype = c_int

#FLUIDSYNTH_API
#int fluid_synth_deactivate_tuning(fluid_synth_t* synth, int chan, int apply);
fluid_synth_deactivate_tuning = _fluid_lib.fluid_synth_deactivate_tuning
fluid_synth_deactivate_tuning.argtypes = [POINTER(fluid_synth_t), c_int, c_int]
fluid_synth_deactivate_tuning.restype = c_int

#FLUIDSYNTH_API void fluid_synth_tuning_iteration_start(fluid_synth_t* synth);
fluid_synth_tuning_iteration_start = _fluid_lib.fluid_synth_tuning_iteration_start
fluid_synth_tuning_iteration_start.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_tuning_iteration_start.restype = None

#FLUIDSYNTH_API 
#int fluid_synth_tuning_iteration_next(fluid_synth_t* synth, int* bank, int* prog);
fluid_synth_tuning_iteration_next = _fluid_lib.fluid_synth_tuning_iteration_next
fluid_synth_tuning_iteration_next.argtypes = [POINTER(fluid_synth_t), POINTER(c_int), POINTER(c_int)]
fluid_synth_tuning_iteration_next.restype = c_int

#FLUIDSYNTH_API int fluid_synth_tuning_dump(fluid_synth_t* synth, int bank, int prog, 
					   #char* name, int len, double* pitch);
fluid_synth_tuning_dump = _fluid_lib.fluid_synth_tuning_dump
fluid_synth_tuning_dump.argtypes = [POINTER(fluid_synth_t), c_int, c_int, c_char_p, c_int, POINTER(c_double)]
fluid_synth_tuning_dump.restype = c_int


# Misc 

#FLUIDSYNTH_API double fluid_synth_get_cpu_load(fluid_synth_t* synth);
fluid_synth_get_cpu_load = _fluid_lib.fluid_synth_get_cpu_load
fluid_synth_get_cpu_load.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_get_cpu_load.restype = c_double

#FLUIDSYNTH_API char* fluid_synth_error(fluid_synth_t* synth);
fluid_synth_error = _fluid_lib.fluid_synth_error
fluid_synth_error.argtypes = [POINTER(fluid_synth_t)]
fluid_synth_error.restype = c_char_p



#
# Synthesizer plugin
#
# To create a synthesizer plugin, create the synthesizer as
# explained above. Once the synthesizer is created you can call
# any of the functions below to get the audio. 
#

#FLUIDSYNTH_API int fluid_synth_write_s16(fluid_synth_t* synth, int len, 
					   #void* lout, int loff, int lincr, 
					   #void* rout, int roff, int rincr);
fluid_synth_write_s16 = _fluid_lib.fluid_synth_write_s16
fluid_synth_write_s16.argtypes = [POINTER(fluid_synth_t), c_int, c_void_p, c_int, c_int, c_void_p, c_int, c_int]
fluid_synth_write_s16.restype = c_int

#FLUIDSYNTH_API int fluid_synth_write_float(fluid_synth_t* synth, int len, 
					 #void* lout, int loff, int lincr, 
					 #void* rout, int roff, int rincr);
fluid_synth_write_float = _fluid_lib.fluid_synth_write_float
fluid_synth_write_float.argtypes = [POINTER(fluid_synth_t), c_int, c_void_p, c_int, c_int, c_void_p, c_int, c_int]
fluid_synth_write_float.restype = c_int

#FLUIDSYNTH_API int fluid_synth_nwrite_float(fluid_synth_t* synth, int len, 
					  #float** left, float** right, 
					  #float** fx_left, float** fx_right);
fluid_synth_nwrite_float = _fluid_lib.fluid_synth_nwrite_float
fluid_synth_nwrite_float.argtypes = [POINTER(fluid_synth_t), c_int, POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]
fluid_synth_nwrite_float.restype = c_int

#FLUIDSYNTH_API int fluid_synth_process(fluid_synth_t* synth, int len,
					 #int nin, float** in, 
					 #int nout, float** out);
fluid_synth_process = _fluid_lib.fluid_synth_process
fluid_synth_process.argtypes = [POINTER(fluid_synth_t), c_int, c_int, POINTER(POINTER(c_float)), c_int, POINTER(POINTER(c_float))]
fluid_synth_process.restype = c_int


#
# Type definition of the synthesizer's audio callback function.
# @param synth FluidSynth instance
# @param len Count of audio frames to synthesize
# @param out1 Array to store left channel of audio to
# @param loff Offset index in 'out1' for first sample
# @param lincr Increment between samples stored to 'out1'
# @param out2 Array to store right channel of audio to
# @param roff Offset index in 'out2' for first sample
# @param rincr Increment between samples stored to 'out2'
#
#typedef int (*fluid_audio_callback_t)(fluid_synth_t* synth, int len, 
					 #void* out1, int loff, int lincr, 
					 #void* out2, int roff, int rincr);
fluid_audio_callback_t = CFUNCTYPE(c_int, POINTER(fluid_synth_t), c_int, c_void_p, c_int, c_int, c_void_p, c_int, c_int)


# Synthesizer's interface to handle SoundFont loaders 

#FLUIDSYNTH_API void fluid_synth_add_sfloader(fluid_synth_t* synth, fluid_sfloader_t* loader);
fluid_synth_add_sfloader = _fluid_lib.fluid_synth_add_sfloader
fluid_synth_add_sfloader.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_sfloader_t)]
fluid_synth_add_sfloader.restype = None

#FLUIDSYNTH_API fluid_voice_t* fluid_synth_alloc_voice(fluid_synth_t* synth, fluid_sample_t* sample,
#int channum, int key, int vel);
fluid_synth_alloc_voice = _fluid_lib.fluid_synth_alloc_voice
fluid_synth_alloc_voice.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_sfloader_t), c_int, c_int, c_int]
fluid_synth_alloc_voice.restype = POINTER(fluid_voice_t)

#FLUIDSYNTH_API void fluid_synth_start_voice(fluid_synth_t* synth, fluid_voice_t* voice);
fluid_synth_start_voice = _fluid_lib.fluid_synth_start_voice
fluid_synth_start_voice.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_voice_t)]
fluid_synth_start_voice.restype = None

#FLUIDSYNTH_API void fluid_synth_get_voicelist(fluid_synth_t* synth,
#fluid_voice_t* buf[], int bufsize, int ID);
fluid_synth_get_voicelist = _fluid_lib.fluid_synth_get_voicelist
fluid_synth_get_voicelist.argtypes = [POINTER(fluid_synth_t), POINTER(POINTER(fluid_voice_t)), c_int, c_int]
fluid_synth_get_voicelist.restype = None

#FLUIDSYNTH_API int fluid_synth_handle_midi_event(void* data, fluid_midi_event_t* event);
fluid_synth_handle_midi_event = _fluid_lib.fluid_synth_handle_midi_event
fluid_synth_handle_midi_event.argtypes = [c_void_p, POINTER(fluid_midi_event_t)]
fluid_synth_handle_midi_event.restype = c_int

#FLUIDSYNTH_API void fluid_synth_set_midi_router(fluid_synth_t* synth,
#fluid_midi_router_t* router);
fluid_synth_set_midi_router = _fluid_lib.fluid_synth_set_midi_router
fluid_synth_set_midi_router.argtypes = [POINTER(fluid_synth_t), POINTER(fluid_midi_router_t)]
fluid_synth_set_midi_router.restype = None
