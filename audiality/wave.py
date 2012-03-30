#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Audiality wave module.
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

""" Audiality wave module.

"""

from ctypes import *
from ctypes.util import find_library

from .enums import *

audiality_name = find_library('audiality')
if not audiality_name:
    raise Exception("libaudiality could not be found")

_audiality_lib = cdll.LoadLibrary(audiality_name)


# Note on sample formats and clipping:
#	* Operations on integer waveforms will saturate if the
#	  respective integer range is exceeded.

#	* Operations on floating point waveforms will *not*
#	  saturate at all, under any circumstances.

#	* Converting from floating point to integer formats,
#	  as well as mixing floating point waveforms into
#	  integer waveforms will saturate if the respective
#	  integer range is exceeded.
 

A_PATCH_MAP_SIZE = 128


#----------------------------------------------------------
#   Basic Wave API
#----------------------------------------------------------*/


# Allocate a new wave for later use.
# If 'id' is -1, a wave id will be allocated automatically.

# Returns your wave id, or a negative value in the case of
# failure.
 
#extern AEXP int ACALL ady_wave_alloc(int wid);
ady_wave_alloc = _audiality_lib.ady_wave_alloc
ady_wave_alloc.argtypes = [c_int]
ady_wave_alloc.restype = c_int



# Allocate a range of waves for later use, to prevent the from
# being stolen by the dynamic allocation system.

# Returns your first wave id, or a negative value in the case of
# failure.
 
#extern AEXP int ACALL ady_wave_alloc_range(int first_wid, int last_wid);
ady_wave_alloc_range = _audiality_lib.ady_wave_alloc_range
ady_wave_alloc_range.argtypes = [c_int, c_int]
ady_wave_alloc_range.restype = c_int



# Set the path to data files.

# This must be a valid path, terminated by a
# '/', '\', ':' or whatever "directory separator"
# the current platform is using, and will be
# prepended to any external file names used in
# other calls.
 
#extern AEXP void ACALL ady_set_path(const char *path);
ady_set_path = _audiality_lib.ady_set_path
ady_set_path.argtypes = [c_char_p]
ady_set_path.restype = None


# Returns the current path. */
#extern AEXP const char *ACALL ady_path(void);
ady_path = _audiality_lib.ady_path
ady_path.argtypes = []
ady_path.restype = c_char_p



# Loads a waveform from disk.

# If 'id' is -1, a new waveform will be allocated automatically.

# The file name can be the path to an audio file of any supported
# format.

# If the file format cannot be identified, the file is assumed to
# be raw data, and the audio format is assumed to be of the
# format specified for the waveform. You should set the proper
# format (using a_wave_format()) *before* loading a raw audio
# file, to minimize the risk of extra work for the engine.

# Returns the id of the new wave, or a negative value in the
# case of failure.
 
#extern AEXP int ACALL ady_wave_load(int wid, const char *name, int looped);
ady_wave_load = _audiality_lib.ady_wave_load
ady_wave_load.argtypes = [c_int, c_char_p, c_int]
ady_wave_load.restype = c_int



# "Loads" a waveform from a raw data buffer in memory.
# The audio engine will *not* free the memory you pass here, but
# will copy it into a private buffer internally, so your buffer
# does not have to be static. (The internal copy is often needed
# anyway due to the need for preprocessing.)

# The data is assumed to be of the format specified with
# a_wave_format().

# Returns the id of the new wave, or a negative value in the
# case of failure.
 
#extern AEXP int ACALL ady_wave_load_mem(int wid, void *data, unsigned size, int looped);
ady_wave_load_mem = _audiality_lib.ady_wave_load_mem
ady_wave_load_mem.argtypes = [c_int, c_void_p, c_uint, c_int]
ady_wave_load_mem.restype = c_int



# Removes a waveform from memory, and frees the wave id.
 
#extern AEXP void ACALL ady_wave_free(int wid);	 -1 to free all */
ady_wave_free = _audiality_lib.ady_wave_free
ady_wave_free.argtypes = [c_int]
ady_wave_free.restype = None



# Specify the data format and sample rate of a waveform.

# If 'id' is -1, a new waveform will be allocated automatically.

# Note that this call *will not* convert any data! This call
# should normally not be used except when loading raw audio
# files.

# Returns the id of the new wave, or a negative value in the
# case of failure. (Yes, it *can* fail, as it may have to
# reallocate the wave data buffer!)
 
#extern AEXP int ACALL ady_wave_format(int wid, ADY_formats fmt, int fs);
ady_wave_format = _audiality_lib.ady_wave_format
ady_wave_format.argtypes = [c_int, ADY_formats, c_int]
ady_wave_format.restype = c_int



# Creates a silent wave of the specified size in *samples*.

# The data will be of the format specified with
# a_wave_format().

# Returns the id of the new wave, or a negative value in the
# case of failure.
 
#extern AEXP int ACALL ady_wave_blank(int wid, unsigned samples, int looped);
ady_wave_blank = _audiality_lib.ady_wave_blank
ady_wave_blank.argtypes = [c_int, c_uint, c_int]
ady_wave_blank.restype = c_int



# Convert a waveform from it's current format into the specified
# format. If there is no data, you just get a new empty wave of
# the specified format, or if new_vwid == wid, the format is
# changed into the one you specify.

# If new_wid is -1, a new wave will be allocated automatically.
# new_wid may equal wid, for "in-place" conversion.

# By setting either 'fmt' to -1 or 'fs' to 0, the respective
# parameter is copied from the original wave. Setting both to
# -1 respectively 0 is equivalent to calling a_wave_clone().

# 'resamp' is the resampling method to use, if resampling is
# needed.

# Returns the new wave id, or a negative value in the case of
# failure.
 
#extern AEXP int ACALL ady_wave_convert(int wid, int new_wid, ADY_formats fmt,
		#int fs, ADY_resample resamp);
ady_wave_convert = _audiality_lib.ady_wave_convert
ady_wave_convert.argtypes = [c_int, c_int, ADY_formats, c_int, ADY_resample]
ady_wave_convert.restype = c_int


# Copy a waveform.

# If new_wid is -1, a new wave will be allocated automatically.

# Returns the clone wave id, or a negative value in the case of
# failure.
 
#extern AEXP int ACALL ady_wave_clone(int wid, int new_wid);
ady_wave_clone = _audiality_lib.ady_wave_clone
ady_wave_clone.argtypes = [c_int, c_int]
ady_wave_clone.restype = c_int



# Converts a waveform (if needed) and prepares it for playback
# by the real time synth engine. Passing -1 for 'wid' will
# prepare *all* waveforms that aren't ready for playback
# already.
 
#extern AEXP void ACALL ady_wave_prepare(int wid);
ady_wave_prepare = _audiality_lib.ady_wave_prepare
ady_wave_prepare.argtypes = [c_int]
ady_wave_prepare.restype = None



# Change the default patch mapping, so that when
# sequence <wid> selects patch <from>, patch <to>
# is selected instead.

# If <wid> is -1, the mapping of all waveforms are affected.
# If <from> is -1, all mappings of the affected waveforms are
# changed. If <to> is -1, any mappings affected will be set
# to the default 1:1 mapping.
 
#extern AEXP void ACALL ady_wave_map(int wid, int from, int to);
ady_wave_map = _audiality_lib.ady_wave_map
ady_wave_map.argtypes = [c_int, c_int, c_int]
ady_wave_map.restype = None
