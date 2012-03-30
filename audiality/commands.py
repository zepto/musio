#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Audiality commands module.
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

""" Audiality commands module.

"""

from ctypes import *
from ctypes.util import find_library

from .enums import *

audiality_name = find_library('audiality')
if not audiality_name:
    raise Exception("libaudiality could not be found")

_audiality_lib = cdll.LoadLibrary(audiality_name)


#----------------------------------------------------------
#   Mixer Control
#----------------------------------------------------------
#extern AEXP void ACALL ady_mixer_stage(unsigned bus, unsigned stage,
		#ADY_stagetypes type);
ady_mixer_stage = _audiality_lib.ady_mixer_stage
ady_mixer_stage.argtypes = [c_uint, c_uint, ADY_stagetypes]
ady_mixer_stage.restype = None

#extern AEXP void ACALL ady_mixer_control(unsigned bus, unsigned stage,
		#unsigned ctl, float arg);
ady_mixer_control = _audiality_lib.ady_mixer_control
ady_mixer_control.argtypes = [c_uint, c_uint, c_uint, c_float]
ady_mixer_control.restype = None


# Connect MIDI CC 'cc' on 'channel' to mixer control 'ctrl'
# of bus stage 'stage' of bus 'bus', using transform type
# 'transform'.

#extern AEXP void ACALL ady_mixer_connect_cc(
		#unsigned bus, unsigned stage, unsigned ctl,
		#unsigned channel, unsigned cc, unsigned transform);
ady_mixer_connect_cc = _audiality_lib.ady_mixer_connect_cc
ady_mixer_connect_cc.argtypes = [c_uint, c_uint, c_uint, c_uint, c_uint, c_uint]
ady_mixer_connect_cc.restype = None


#----------------------------------------------------------
	#Group Control
#----------------------------------------------------------
#extern AEXP void ACALL ady_group_stop(unsigned gid);
ady_group_stop = _audiality_lib.ady_group_stop
ady_group_stop.argtypes = [c_uint]
ady_group_stop.restype = None

#extern AEXP void ACALL ady_group_control(unsigned gid, unsigned ctl, float arg);
ady_group_control = _audiality_lib.ady_group_control
ady_group_control.argtypes = [c_uint, c_uint, c_float]
ady_group_control.restype = None



#----------------------------------------------------------
	#Channel Control
#----------------------------------------------------------
#extern AEXP void ACALL ady_channel_play(int cid, int tag,
		#float pitch, float velocity);
ady_channel_play = _audiality_lib.ady_channel_play
ady_channel_play.argtypes = [c_int, c_int, c_float, c_float]
ady_channel_play.restype = None

#extern AEXP void ACALL ady_channel_control(int cid, int tag,
		#int ctl, float arg);
ady_channel_control = _audiality_lib.ady_channel_control
ady_channel_control.argtypes = [c_int, c_int, c_int, c_float]
ady_channel_control.restype = None

#extern AEXP void ACALL ady_channel_stop(int cid, int tag);	 -1 to stop all 
ady_channel_stop = _audiality_lib.ady_channel_stop
ady_channel_stop.argtypes = [c_int, c_int]
ady_channel_stop.restype = None



#FIXME: Broken API. Broken implementation. It just "seems" to work.

#extern AEXP int ACALL ady_channel_playing(int cid);
ady_channel_playing = _audiality_lib.ady_channel_playing
ady_channel_playing.argtypes = [c_int]
ady_channel_playing.restype = c_int



# Some hacks for soft real time user feedback or similar.

#extern AEXP float ACALL ady_channel_read_control(int cid, int tag, int ctl);
ady_channel_read_control = _audiality_lib.ady_channel_read_control
ady_channel_read_control.argtypes = [c_int, c_int, c_int]
ady_channel_read_control.restype = c_float



#----------------------------------------------------------
	#Simple Wrapper for Sound Effects
#----------------------------------------------------------

#FIXME: This probably belongs somewhere else.

#extern AEXP void ACALL play_init(void);
play_init = _audiality_lib.play_init
play_init.argtypes = []
play_init.restype = None

#extern AEXP void ACALL music_play(int channel, int wid);
music_play = _audiality_lib.music_play
music_play.argtypes = [c_int, c_int]
music_play.restype = None


# Set listener position 
#extern AEXP void ACALL sound_position(int x, int y);
sound_position = _audiality_lib.sound_position
sound_position.argtypes = [c_int, c_int]
sound_position.restype = None


# Set world size for wrapping 
#extern AEXP void ACALL sound_wrap(int w, int h);
sound_wrap = _audiality_lib.sound_wrap
sound_wrap.argtypes = [c_int, c_int]
sound_wrap.restype = None



# Set world scale. 'maxrange' is the distance where
# a sound is out of the audible range.

#extern AEXP void ACALL sound_scale(int maxrange, int pan_maxrange);
sound_scale = _audiality_lib.sound_scale
sound_scale.argtypes = [c_int, c_int]
sound_scale.restype = None



# Play a sound at world coordinates (x, y), using
# default pitch (60<<16) and velocity (65536).

#extern AEXP void ACALL sound_play(int wid, int x, int y);
sound_play = _audiality_lib.sound_play
sound_play.argtypes = [c_int, c_int, c_int]
sound_play.restype = None


# Play a sound right where the listener is. 
#extern AEXP void ACALL sound_play0(int wid);
sound_play0 = _audiality_lib.sound_play0
sound_play0.argtypes = [c_int]
sound_play0.restype = None
