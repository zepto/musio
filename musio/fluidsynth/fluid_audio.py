#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth audio.
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


""" Fluidsynth audio.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

from .fluid_types import *

#
# @file audio.h
# @brief Functions for audio driver output.
# @defgroup AudioFunctions Functions for audio output
#
# Defines functions for creating audio driver output.  Use
# new_fluid_audio_driver() to create a new audio driver for a given synth
# and configuration settings.  The function new_fluid_audio_driver2() can be
# used if custom audio processing is desired before the audio is sent to the
# audio driver (although it is not as efficient).
#
# @sa @ref CreatingAudioDriver
#

#
# Callback function type used with new_fluid_audio_driver2() to allow for
# custom user audio processing before the audio is sent to the driver.  This
# function is responsible for rendering the audio to the buffers.
# @param data The user data parameter as passed to new_fluid_audio_driver2().
# @param len Length of the audio in frames.
# @param nin Count of buffers in 'in'
# @param in Not used currently
# @param nout Count of arrays in 'out' (i.e., channel count)
# @param out Output buffers, one for each channel
# @return Should return 0 on success, non-zero if an error occured.
#
#typedef int (*fluid_audio_func_t)(void* data, int len,
				 #int nin, float** in,
				 #int nout, float** out);
fluid_audio_func_t = CFUNCTYPE(c_int, c_void_p, c_int, c_int, POINTER(POINTER(c_float)), c_int, POINTER(POINTER(c_float)))

#FLUIDSYNTH_API fluid_audio_driver_t* new_fluid_audio_driver(fluid_settings_t* settings,
							 #fluid_synth_t* synth);
new_fluid_audio_driver = _fluid_lib.new_fluid_audio_driver
new_fluid_audio_driver.argtypes = [POINTER(fluid_settings_t), POINTER(fluid_synth_t)]
new_fluid_audio_driver.restype = POINTER(fluid_audio_driver_t)

#FLUIDSYNTH_API fluid_audio_driver_t* new_fluid_audio_driver2(fluid_settings_t* settings,
							  #fluid_audio_func_t func,
							  #void* data);
new_fluid_audio_driver2 = _fluid_lib.new_fluid_audio_driver2
new_fluid_audio_driver2.argtypes = [POINTER(fluid_settings_t), fluid_audio_func_t, c_void_p]
new_fluid_audio_driver2.restype = POINTER(fluid_audio_driver_t)

#FLUIDSYNTH_API void delete_fluid_audio_driver(fluid_audio_driver_t* driver);
delete_fluid_audio_driver = _fluid_lib.delete_fluid_audio_driver
delete_fluid_audio_driver.argtypes = [POINTER(fluid_audio_driver_t)]
delete_fluid_audio_driver.restype = None

#FLUIDSYNTH_API fluid_file_renderer_t *new_fluid_file_renderer(fluid_synth_t* synth);
new_fluid_file_renderer = _fluid_lib.new_fluid_file_renderer
new_fluid_file_renderer.argtypes = [POINTER(fluid_synth_t)]
new_fluid_file_renderer.restype = fluid_file_renderer_t

#FLUIDSYNTH_API int fluid_file_renderer_process_block(fluid_file_renderer_t* dev);
fluid_file_renderer_process_block = _fluid_lib.fluid_file_renderer_process_block
fluid_file_renderer_process_block.argtypes = [POINTER(fluid_file_renderer_t)]
fluid_file_renderer_process_block.restype = c_int

#FLUIDSYNTH_API void delete_fluid_file_renderer(fluid_file_renderer_t* dev);
delete_fluid_file_renderer = _fluid_lib.delete_fluid_file_renderer
delete_fluid_file_renderer.argtypes = [POINTER(fluid_file_renderer_t)]
delete_fluid_file_renderer.restype = None
