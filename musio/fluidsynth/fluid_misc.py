#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth misc.
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


""" Fluidsynth misc.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

#
# @file misc.h
# @brief Miscellaneous utility functions and defines
#

#
# Value that indicates success, used by most libfluidsynth functions.
# @since 1.1.0
#
# NOTE: This was not publicly defined prior to libfluidsynth 1.1.0.  When
# writing code which should also be compatible with older versions, something
# like the following can be used:
#
# @code
#   #include <fluidsynth.h>
#
#   #ifndef FLUID_OK
#   #define FLUID_OK      (0)
#   #define FLUID_FAILED  (-1)
#   #endif
# @endcode
#
FLUID_OK = 0

#
# Value that indicates failure, used by most libfluidsynth functions.
# @since 1.1.0
#
# NOTE: See #FLUID_OK for more details.
#
FLUID_FAILED = -1


#FLUIDSYNTH_API int fluid_is_soundfont (const char *filename);
fluid_is_soundfont = _fluid_lib.fluid_is_soundfont
fluid_is_soundfont.argtypes = [c_char_p]
fluid_is_soundfont.restype = c_int

#FLUIDSYNTH_API int fluid_is_midifile (const char *filename);
fluid_is_midifile = _fluid_lib.fluid_is_midifile
fluid_is_midifile.argtypes = [c_char_p]
fluid_is_midifile.restype = c_int
