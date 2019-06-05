#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Fluidsynth settings.
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


""" Fluidsynth settings.

"""
from ctypes.util import find_library
from ctypes import *

_fluid_lib = cdll.LoadLibrary(find_library('fluidsynth'))

from .fluid_types import *

#
# @file settings.h
# @brief Synthesizer settings
# @defgroup SettingsFunctions Functions for settings management
#
# To create a synthesizer object you will have to specify its
# settings. These settings are stored in a fluid_settings_t object.
# @code
#     void
#     my_synthesizer ()
#     {
#       fluid_settings_t *settings;
#       fluid_synth_t *synth;
#       fluid_audio_driver_t *adriver;
#
#       settings = new_fluid_settings ();
#       fluid_settings_setstr(settings, "audio.driver", "alsa");
#       // ... change settings ...
#       synth = new_fluid_synth (settings);
#       adriver = new_fluid_audio_driver (settings, synth);
#       // ...
#     }
# @endcode
# @sa @ref CreatingSettings
#

#
# Hint FLUID_HINT_BOUNDED_BELOW indicates that the LowerBound field
# of the FLUID_PortRangeHint should be considered meaningful. The
# value in this field should be considered the (inclusive) lower
# bound of the valid range. If FLUID_HINT_SAMPLE_RATE is also
# specified then the value of LowerBound should be multiplied by the
# sample rate.
#
FLUID_HINT_BOUNDED_BELOW = 0x1

# Hint FLUID_HINT_BOUNDED_ABOVE indicates that the UpperBound field
#of the FLUID_PortRangeHint should be considered meaningful. The
#value in this field should be considered the (inclusive) upper
#bound of the valid range. If FLUID_HINT_SAMPLE_RATE is also
#specified then the value of UpperBound should be multiplied by the
#sample rate. 
FLUID_HINT_BOUNDED_ABOVE = 0x2

#
# Hint FLUID_HINT_TOGGLED indicates that the data item should be
# considered a Boolean toggle. Data less than or equal to zero should
# be considered `off' or `false,' and data above zero should be
# considered `on' or `true.' FLUID_HINT_TOGGLED may not be used in
# conjunction with any other hint.
#
FLUID_HINT_TOGGLED = 0x4

#
# Hint FLUID_HINT_SAMPLE_RATE indicates that any bounds specified
# should be interpreted as multiples of the sample rate. For
# instance, a frequency range from 0Hz to the Nyquist frequency (half
# the sample rate) could be requested by this hint in conjunction
# with LowerBound = 0 and UpperBound = 0.5. Hosts that support bounds
# at all must support this hint to retain meaning.
#
FLUID_HINT_SAMPLE_RATE = 0x8

#
# Hint FLUID_HINT_LOGARITHMIC indicates that it is likely that the
# user will find it more intuitive to view values using a logarithmic
# scale. This is particularly useful for frequencies and gains.
#
FLUID_HINT_LOGARITHMIC = 0x10

#
# Hint FLUID_HINT_INTEGER indicates that a user interface would
# probably wish to provide a stepped control taking only integer
# values.
# @deprecated
#
# As there is an integer setting type, this hint is not used.
#
FLUID_HINT_INTEGER = 0x20


FLUID_HINT_FILENAME = 0x01        # *< String setting is a file name 
FLUID_HINT_OPTIONLIST = 0x02        # *< Setting is a list of string options 


#
# Settings type
#
# Each setting has a defined type: numeric (double), integer, string or a
# set of values. The type of each setting can be retrieved using the
# function fluid_settings_get_type()
#
fluid_types_enum = c_int
FLUID_NO_TYPE = -1  # *< Undefined type 
FLUID_NUM_TYPE = 0  # *< Numeric (double) 
FLUID_INT_TYPE = 1  # *< Integer 
FLUID_STR_TYPE = 2  # *< String 
FLUID_SET_TYPE = 3  # *< Set of values 


#FLUIDSYNTH_API fluid_settings_t* new_fluid_settings(void);
new_fluid_settings = _fluid_lib.new_fluid_settings
new_fluid_settings.argtypes = []
new_fluid_settings.restype = POINTER(fluid_settings_t)

#FLUIDSYNTH_API void delete_fluid_settings(fluid_settings_t* settings);
delete_fluid_settings = _fluid_lib.delete_fluid_settings
delete_fluid_settings.argtypes = [POINTER(fluid_settings_t)]
delete_fluid_settings.restype = None

#FLUIDSYNTH_API
#int fluid_settings_get_type(fluid_settings_t* settings, const char *name);
fluid_settings_get_type = _fluid_lib.fluid_settings_get_type
fluid_settings_get_type.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_get_type.restype = c_int

#FLUIDSYNTH_API
#int fluid_settings_get_hints(fluid_settings_t* settings, const char *name);
fluid_settings_get_hints = _fluid_lib.fluid_settings_get_hints
fluid_settings_get_hints.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_get_hints.restype = c_int

#FLUIDSYNTH_API
#int fluid_settings_is_realtime(fluid_settings_t* settings, const char *name);
fluid_settings_is_realtime = _fluid_lib.fluid_settings_is_realtime
fluid_settings_is_realtime.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_is_realtime.restype = c_int

#FLUIDSYNTH_API
#int fluid_settings_setstr(fluid_settings_t* settings, const char *name, const char *str);
fluid_settings_setstr = _fluid_lib.fluid_settings_setstr
fluid_settings_setstr.argtypes = [POINTER(fluid_settings_t), c_char_p, c_char_p]
fluid_settings_setstr.restype = c_int

#FLUIDSYNTH_API
#int fluid_settings_copystr(fluid_settings_t* settings, const char *name, char *str, int len);
fluid_settings_copystr = _fluid_lib.fluid_settings_copystr
fluid_settings_copystr.argtypes = [POINTER(fluid_settings_t), c_char_p, c_char_p, c_int]
fluid_settings_copystr.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_dupstr(fluid_settings_t* settings, const char *name, char** str);
fluid_settings_dupstr = _fluid_lib.fluid_settings_dupstr
fluid_settings_dupstr.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_char_p)]
fluid_settings_dupstr.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_getstr(fluid_settings_t* settings, const char *name, char** str);
fluid_settings_getstr = _fluid_lib.fluid_settings_getstr
fluid_settings_getstr.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_char_p)]
fluid_settings_getstr.restype = c_int


#FLUIDSYNTH_API
#char* fluid_settings_getstr_default(fluid_settings_t* settings, const char *name);
fluid_settings_getstr_default = _fluid_lib.fluid_settings_getstr_default
fluid_settings_getstr_default.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_getstr_default.restype = c_char_p


#FLUIDSYNTH_API
#int fluid_settings_str_equal(fluid_settings_t* settings, const char *name, const char *value);
fluid_settings_str_equal = _fluid_lib.fluid_settings_str_equal
fluid_settings_str_equal.argtypes = [POINTER(fluid_settings_t), c_char_p, c_char_p]
fluid_settings_str_equal.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_setnum(fluid_settings_t* settings, const char *name, double val);
fluid_settings_setnum = _fluid_lib.fluid_settings_setnum
fluid_settings_setnum.argtypes = [POINTER(fluid_settings_t), c_char_p, c_double]
fluid_settings_setnum.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_getnum(fluid_settings_t* settings, const char *name, double* val);
fluid_settings_getnum = _fluid_lib.fluid_settings_getnum
fluid_settings_getnum.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_double)]
fluid_settings_getnum.restype = c_int


#FLUIDSYNTH_API
#double fluid_settings_getnum_default(fluid_settings_t* settings, const char *name);
fluid_settings_getnum_default = _fluid_lib.fluid_settings_getnum_default
fluid_settings_getnum_default.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_getnum_default.restype = c_double


#FLUIDSYNTH_API
#void fluid_settings_getnum_range(fluid_settings_t* settings, const char *name,
				#double* min, double* max);
fluid_settings_getnum_range = _fluid_lib.fluid_settings_getnum_range
fluid_settings_getnum_range.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_double), POINTER(c_double)]
fluid_settings_getnum_range.restype = None

#FLUIDSYNTH_API
#int fluid_settings_setint(fluid_settings_t* settings, const char *name, int val);
fluid_settings_setint = _fluid_lib.fluid_settings_setint
fluid_settings_setint.argtypes = [POINTER(fluid_settings_t), c_char_p, c_int]
fluid_settings_setint.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_getint(fluid_settings_t* settings, const char *name, int* val);
fluid_settings_getint = _fluid_lib.fluid_settings_getint
fluid_settings_getint.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_int)]
fluid_settings_getint.restype = c_int


#FLUIDSYNTH_API
#int fluid_settings_getint_default(fluid_settings_t* settings, const char *name);
fluid_settings_getint_default = _fluid_lib.fluid_settings_getint_default
fluid_settings_getint_default.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_getint_default.restype = c_int


#FLUIDSYNTH_API
#void fluid_settings_getint_range(fluid_settings_t* settings, const char *name,
				#int* min, int* max);
fluid_settings_getint_range = _fluid_lib.fluid_settings_getint_range
fluid_settings_getint_range.argtypes = [POINTER(fluid_settings_t), c_char_p, POINTER(c_int), POINTER(c_int)]
fluid_settings_getint_range.restype = None


#
# Callback function type used with fluid_settings_foreach_option()
# @param data User defined data pointer
# @param name Setting name
# @param option A string option for this setting (iterates through the list)
#
#typedef void (*fluid_settings_foreach_option_t)(void *data, char *name, char *option);
fluid_settings_foreach_option_t = CFUNCTYPE(None, c_void_p, c_char_p, c_char_p)

#FLUIDSYNTH_API
#void fluid_settings_foreach_option(fluid_settings_t* settings,
				  #const char* name, void* data,
				  #fluid_settings_foreach_option_t func);
fluid_settings_foreach_option = _fluid_lib.fluid_settings_foreach_option
fluid_settings_foreach_option.argtypes = [POINTER(fluid_settings_t), c_char_p, c_void_p, fluid_settings_foreach_option_t]
fluid_settings_foreach_option.restype = None

#FLUIDSYNTH_API
#int fluid_settings_option_count (fluid_settings_t* settings, const char* name);
fluid_settings_option_count = _fluid_lib.fluid_settings_option_count
fluid_settings_option_count.argtypes = [POINTER(fluid_settings_t), c_char_p]
fluid_settings_option_count.restype = c_int

#FLUIDSYNTH_API char *fluid_settings_option_concat (fluid_settings_t* settings,
#const char* name,
#const char* separator);
fluid_settings_option_concat = _fluid_lib.fluid_settings_option_concat 
fluid_settings_option_concat.argtypes = [POINTER(fluid_settings_t), c_char_p, c_char_p]
fluid_settings_option_concat.restype = c_char_p

#
# Callback function type used with fluid_settings_foreach()
# @param data User defined data pointer
# @param name Setting name
# @param type Setting type (#fluid_types_enum)
#
#typedef void (*fluid_settings_foreach_t)(void *data, char *name, int type);
fluid_settings_foreach_t = CFUNCTYPE(None, c_void_p, c_char_p, c_int)

#FLUIDSYNTH_API
#void fluid_settings_foreach(fluid_settings_t* settings, void* data,
			   #fluid_settings_foreach_t func);
fluid_settings_foreach = _fluid_lib.fluid_settings_foreach
fluid_settings_foreach.argtypes = [POINTER(fluid_settings_t), c_void_p, fluid_settings_foreach_t]
fluid_settings_foreach.restype = None

