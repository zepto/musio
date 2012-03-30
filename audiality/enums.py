#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Audiality enums module.
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

""" Audiality enums module.

"""


from ctypes import *

# Builtin patch drivers 
PD_NONE = -1  #  No driver! 
PD_MONO = 0	  #  Basic monophonic 
PD_POLY = 1	  #  Basic polyphonic 
PD_MIDI = 2	  #  Basic MIDI player 
PD_EEL = 3	  #  User EEL code driver 
ADY_patch_drivers = c_int


# Voice tag special codes 
AVT_FUTURE = -2
AVT_ALL = -1
ADY_voice_tags = c_int


#
# DAHDSR envelope generator parameters:
#
#   Level
#     ^
#     |         __L1__
#     |        /|    |\
#     |       / |    | \
#     |__L0__/  |    |  \__L2__
#     |     |   |    |   |    |\
#     |  D  | A | H  | D | S  |R\
#     |_____|___|____|___|____|__\____\
#     |     |   |    |   |    |   |   / Time
#      DELAY T1  HOLD T2   T3  T4
#
# State by state description:
#
#	D: Set to L0, and hold for DELAY seconds.
#	A: Ramp to L1 over T1 seconds.
#	H: Hold at L1 for HOLD seconds.
#	D: Ramp to L2 over T2 seconds.
#	S: if T3 < 0
#		Hold at L2 until CE_STOP is received.
#	   else
#		Hold at L2 for T3 seconds.
#	R: Ramp to 0 over T3 seconds.
#
# If T3 is set to a negative value, sustain lasts until
# a CE_STOP event is received. If T3 is 0 of higher,
# sustain lasts for T3 seconds.
#
# The EG will *always* load L0, but from then on, if a
# phase has a zero duration, that phase is skipped.
# Note that skipping any of the A, D and R phases will
# produce clicks, unless the adjacent levels are
# identical.
#
# In some cases, it's desirable that the EG immediately
# skips to the release phase when a CE_STOP event is
# received, whereas in other cases, this would result
# in problems with very short notes. Therefore, there is
# a boolean control 'ENV_SKIP' that make it possible to
# specify which behavior is desired.
# '1' will make the EG skip to release upon receiving
# CE_STOP. '0' will result in the EG taking no action
# on CE_STOP until the sustain phase is reached the
# normal way.
# 'ENV_SKIP' has no effect if "timed sustain" is used;
# T3 must be < 0, or CE_STOP is entirely ignored.
#
#

# Audio Patch Parameters 
APP_FIRST = 0
# Patch Driver Plugin 
APP_DRIVER = 0	#  (int) Patch driver index 

# Oscillator 
APP_WAVE = 1    #  (int) Waveform index 

# "Special" features 
APP_RANDPITCH = 2   #   (fixp) Random pitch depth 
APP_RANDVOL = 3	    #   (fixp) Random volume depth 

# Envelope Generator 
APP_ENV_SKIP = 4    #	(bool) skip to sustain on CE_STOP 
APP_ENV_L0 = 5      #	(fixp) envelope level 0 (initial) 
APP_ENV_DELAY = 6   #	(fixp) envelope delay-to-attack 
APP_ENV_T1 = 7      #   (fixp) envelope attack time 
APP_ENV_L1 = 8      #   (fixp) envelope hold level 
APP_ENV_HOLD = 9    #   (fixp) envelope hold time 
APP_ENV_T2 = 10     #   (fixp) envelope decay time 
APP_ENV_L2 = 11     #   (fixp) envelope sustain level 
APP_ENV_T3 = 12     #   (fixp) envelope sustain time 
APP_ENV_T4 = 13     #   (fixp) envelope release time 

# LFO Generator 
APP_LFO_DELAY = 14  #   (fixp) LFO delay-to-start 
APP_LFO_ATTACK = 15 #   (fixp) LFO attack time-to-full 
APP_LFO_DECAY = 16  #   (fixp) LFO decay time-to-zero 
APP_LFO_RATE = 17   #   (fixp) LFO frequency 
APP_LFO_SHAPE = 18  #   (int) LFO modulation waveform 

# Modulation Matrix 
APP_ENV2PITCH = 19  #   (fixp) 
APP_ENV2VOL = 20    #   (fixp) 
APP_LFO2PITCH = 21  #   (fixp) 
APP_LFO2VOL = 22    #   (fixp) 
#if 0
APP_ENV2CUT = 23    #   (fixp) 
APP_LFO2CUT = 24    #   (fixp) 
#TODO:
#
# Controls for the resonant filter
# (Setting CUT to 0 disables the filter.)
#
APP_FILT_CUT = 25   #   (fixp) Filter cutoff 
APP_FILT_RES = 26   #   (fixp) Filter resonance 

#
# Distortion control
#
APP_DIST_GAIN = 27  #   (fixp) Pre-limiter gain 
APP_DIST_CLIP = 28  #   (fixp) Limiter clip threshold 
APP_DIST_DRIVE = 29 #   (fixp) Feedback from the clipped peaks 
#endif
APP_COUNT = 30
APP_LAST = APP_COUNT - 1
ADY_pparams = c_int
#typedef int ADY_ppbank[APP_COUNT];
ADY_ppbank = c_int * APP_COUNT


#
# The voice structure:
#      OSC -> VOL/PAN/SEND
#                |   |
#                | : '-> o-> FX BUS 0
#                '-----> o-> FX BUS 1
#                  :  :  ...    ...
#                  :  :  o-> FX BUS N-1
#
#	That's it! No filters, and just one oscillator. The
#	interesting part is the output section.
#
#	Every voice has two output bus selectors, each one
#	referencing a stereo bus, on which further
#	processing may be applied. By setting either bus
#	selector to -1, or by pointing both at the same bus,
#	only the Primary Output will be used, and some some
#	CPU power is saved during mixing. :-)
#
#	As opposed to most MIDI synths, this engine allows
#	you to select one or two output busses for each
#	voice, using one as the Primary Output (level set
#	by CC7: Volume) and the other as the Secondary
#	Output (level set by CC91: Reverb Depth, multiplied
#	by CC7.)
#
#	The MIDI implementation uses CC88 and CC89 to select
#	Primary and Secondary Output busses, respectively.
#

#
# The Priority System:
#	Set ACC_PRIORITY to 0 to have a channel grab a
#	voice, and have it excluded from the dynamic
#	voice allocation system.
#
#	Other values specify channel priority for voice
#	stealing - higher values mean lower priority.
#	Higher priority channels win when fighting for
#	voices. Priority 0 voices cannot be stolen.
#

ACC_FIRST = 0
#--- Controls that are NOT transformed ---
ACC_GROUP = 0		#	 mixer group 
ACC_PRIORITY = 1	#	 Voice Allocation Priority 
ACC_PATCH = 2		#  (int) Patch index 

ACC_PRIM_BUS = 3	# (int) target bus for ACC_VOLUME 
ACC_SEND_BUS = 4	#  (int) target bus for ACC_SEND 

#--- Controls that are transformed by adding ---
ACC_PAN = 5 	#	 (fixp[-1, 1]) pre-send pan 
ACC_PITCH = 5 	#	 (fixp) linear frequency; int <==> MIDI 

#--- Controls that are transformed by multiplying ---
ACC_VOLUME = 6 	#	 (fixp) primary "send" level 
ACC_SEND = 7 	#	 (fixp) secondary send level 

#--- Patch Controls (Not transformed) ---
ACC_MOD1 = 8 	#	 (fixp) Modulation 1 depth 
ACC_MOD2 = 9 	#	 (fixp) Modulation 2 depth 
ACC_MOD3 = 10 	#	 (fixp) Modulation 3 depth 

ACC_X = 11 		#		 (fixp) X position 
ACC_Y = 12 		#		 (fixp) Y position 
ACC_Z = 13		#		 (fixp) Z position 

ACC_COUNT = 14
ACC_LAST = ACC_COUNT - 1
ADY_ctls = c_int
#typedef int ADY_ccbank[ACC_COUNT];
ADY_ccbank = c_int * ACC_COUNT


#
# Bus Stage Types
#
ABST_NONE = 0
ABST_AUDIO_INPUT = 1
ABST_AUDIO_OUTPUT = 2
ABST_BUS_TAP = 3
ABST_BUS_SEND = 4
ABST_IFX = 5
ABST_LADSPA = 6

ABST_COUNT = 7
ABST_LAST = ABST_COUNT -1
ADY_stagetypes = c_int


#
# Insert Effect Types (for IFX stages)
#
AFX_NONE = 0
AFX_DELAY = 1   #	 1: Tap 1	2: Tap 2
         # 3: Gain 1	4: Gain 2
         # 5: Feedback Level
         #
AFX_ECHO = 2    #	 1: Ldelay	2: Rdelay
         # 3: Lgain	4: Rgain
         # 5: Feedback Delay
         #
AFX_XDELAY = 3  #	 1: Early reflections duration
         # 2: Tail duration
         # 3: Early reflections level
         # 4: Tail Feedback Level
         # 5: Feedback LPF Cutoff
         #
AFX_REVERB = 4  #	 1: Reflection density
         # 2: Tail feedback
         # 3:
         # 4:
         # 5: Feedback LPF Cutoff
         #
AFX_CHORUS = 5  #	 1: Left Vibrato Speed
         # 2: Right Vibrato Speed
         # 3: Left Vibrato Depth
         # 4: Right Vibrato Depth
         # 5: Feedback Level
         #
AFX_FLANGER = 6 # Same as chorus; only different scale. 
AFX_FILTER = 7  #	 1: Left Cut	2: Right Cut
         # 3: Left Reso	4: Right Resonance
         # 5: <unused>
         #
AFX_DIST = 8    #	 1: Bass	2: Treble
         # 3: Pre Gain	4: Post Gain
         # 4: Drive
         #
AFX_WAH = 9     #	 1: Cutoff		2: Resonance
         # 3: Cutoff Depth	4: Attack
         # 5: Release
         #
AFX_EQ = 10     #	 1: Bass f	2: Treble f
         # 3: Bass Gain	4: Treble Gain
         # 4: Mid Gain
         #
AFX_ENHANCER = 11
         # 1: Mid f	2: High f
         # 3: Mid Sens.	4: High Sensitivity
         # 5: Artificial Treble Strength
         #
AFX_COMPRESSOR = 12
         # 1: Attack	2: Release
         # 3: Gain	4: Threshold
         # 5: Knee Softness
         #
AFX_LIMITER = 13
         # 1: Attack	2: Release
         # 3: Gain	4: Threshold
         # 5: Knee Softness
         #
AFX_MAXIMIZER = 14
         # 1: Low Split	2: High Split
         # 3: Low Boost	4: High Boost
         # 5: Mid Boost
         #
AFX_COUNT = 15
AFX_LAST = AFX_COUNT -1
ADY_fxtypes = c_int


#
# Voice resampling algorithms.
#
AR_WORST = -3
AR_MEDIUM = -2
AR_BEST = -1

AR_NEAREST = 0	    #  Nearest sample ("useless") 
AR_NEAREST_4X = 1 	# 	 Nearest with 4x oversampling 
AR_LINEAR = 2 		# 	 Linear Interpolation 
AR_LINEAR_2X_R = 3 	# 	 LI w/ 2x oversampling + ramp smoothing 
AR_LINEAR_4X_R = 4 	# 	 LI w/ 4x oversampling + ramp smoothing 
AR_LINEAR_8X_R = 5 	# 	 LI w/ 8x oversampling + ramp smoothing 
AR_LINEAR_16X_R = 6 #  LI w/ 16x oversampling + ramp smoothing 
AR_CUBIC_R = 7		#	 Cubic interpolation + ramp smoothing 
ADY_resample = c_int


#
# Data formats.
#
AF_MONO8 = 0	#	 Mono Sint8 
AF_STEREO8 = 1 	# 	 Stereo Sint8 
AF_MONO16 = 2 	# 	 Mono Sint16 
AF_STEREO16 = 3 # 	 Stereo Sint16 
AF_MONO32 = 4 	# 	 Mono float32 
AF_STEREO32 = 5 # 	 Stereo float32 
AF_MIDI = 6		#	 Midi sequence 
ADY_formats = c_int


#
# General quality levels.
#
AQ_VERY_LOW = 0	 # Nearest, no oversampling 
AQ_LOW = 1 		 # Nearest, 4x oversampling 
AQ_NORMAL = 2 	 # Linear interpolation 
AQ_HIGH = 3 	 # Cub or lin interpol. + 2x..8x ovsmpl 
AQ_VERY_HIGH = 4 # Cub or lin interpol. + 4x..16x ovsmpl 
ADY_quality = c_int


#
# Interface types.
#
ADY_IF_AUDIO_IN = 0
ADY_IF_AUDIO_OUT = 1
ADY_IF_CONTROL_IN = 2 
ADY_IF_CONTROL_OUT = 3 

ADY_IF_COUNT = 4
ADY_interfaces = c_int


#
# Bits for the 'flags' argument of a_start(),
# and A_settings::flags.
#
ADY_USE_POLLING = 0x00000001
ADY_REALTIME = 0x00000002
