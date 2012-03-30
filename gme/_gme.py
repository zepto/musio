#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Game music emulator library python wrapper.
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


""" Game music emulator library python wrapper.

"""

from ctypes import *
from ctypes.util import find_library

gmelib_name = find_library('gme')
if not gmelib_name:
    raise Exception("libgme could not be found")

_gme_lib = cdll.LoadLibrary(gmelib_name)

# Game music emulator library C interface (also usable from C++) 

# Error string returned by library functions, or NULL if no error (success) 
#typedef const char* gme_err_t;
gme_err_t = c_char_p

# First parameter of most gme_ functions is a pointer to the Music_Emu 
#typedef struct Music_Emu Music_Emu;
class Music_Emu_t(Structure):
    _fields_ = [
            ]
Music_Emu = Music_Emu_t


#******* Basic operations *******

# Create emulator and load game music file/data into it. Sets *out to new emulator. 
#gme_err_t gme_open_file( const char path [], Music_Emu** out, int sample_rate );
gme_open_file = _gme_lib.gme_open_file
gme_open_file.argtypes = [c_char_p, POINTER(POINTER(Music_Emu)), c_int]
gme_open_file.restype = gme_err_t

# Number of tracks available 
#int gme_track_count( Music_Emu const* );
gme_track_count = _gme_lib.gme_track_count
gme_track_count.argtypes = [POINTER(Music_Emu)]
gme_track_count.restype = c_int

# Start a track, where 0 is the first track 
#gme_err_t gme_start_track( Music_Emu*, int index );
gme_start_track = _gme_lib.gme_start_track
gme_start_track.argtypes = [POINTER(Music_Emu), c_int]
gme_start_track.restype = gme_err_t

# Generate 'count' 16-bit signed samples info 'out'. Output is in stereo. 
#gme_err_t gme_play( Music_Emu*, int count, short out [] );
gme_play = _gme_lib.gme_play
gme_play.argtypes = [POINTER(Music_Emu), c_int, POINTER(c_short)]
gme_play.restype = gme_err_t

# Finish using emulator and free memory 
#void gme_delete( Music_Emu* );
gme_delete = _gme_lib.gme_delete
gme_delete.argtypes = [POINTER(Music_Emu)]
gme_delete.restype = None


#******* Track position/length *******

# Set time to start fading track out. Once fade ends track_ended() returns true.
#Fade time can be changed while track is playing. 
#void gme_set_fade( Music_Emu*, int start_msec );
gme_set_fade = _gme_lib.gme_set_fade
gme_set_fade.argtypes = [POINTER(Music_Emu), c_int]
gme_set_fade.restype = None

# True if a track has reached its end 
#int gme_track_ended( Music_Emu const* );
gme_track_ended = _gme_lib.gme_track_ended
gme_track_ended.argtypes = [POINTER(Music_Emu)]
gme_track_ended.restype = c_int

# Number of milliseconds (1000 = one second) played since beginning of track 
#int gme_tell( Music_Emu const* );
gme_tell = _gme_lib.gme_tell
gme_tell.argtypes = [POINTER(Music_Emu)]
gme_tell.restype = c_int

# Seek to new time in track. Seeking backwards or far forward can take a while. 
#gme_err_t gme_seek( Music_Emu*, int msec );
gme_seek = _gme_lib.gme_seek
gme_seek.argtypes = [POINTER(Music_Emu), c_int]
gme_seek.restype = gme_err_t


#******* Informational *******

# If you only need track information from a music file, pass gme_info_only for
#sample_rate to open/load. 
#enum { gme_info_only = -1 };
gme_info_only = -1

# Most recent warning string, or NULL if none. Clears current warning after returning.
#Warning is also cleared when loading a file and starting a track. 
#const char* gme_warning( Music_Emu* );
gme_warning = _gme_lib.gme_warning
gme_warning.argtypes = [POINTER(Music_Emu)]
gme_warning.restype = c_char_p

# Load m3u playlist file (must be done after loading music) 
#gme_err_t gme_load_m3u( Music_Emu*, const char path [] );
gme_load_m3u = _gme_lib.gme_load_m3u
gme_load_m3u.argtypes = [POINTER(Music_Emu), c_char_p]
gme_load_m3u.restype = gme_err_t

# Clear any loaded m3u playlist and any internal playlist that the music format
#supports (NSFE for example). 
#void gme_clear_playlist( Music_Emu* );
#gme_clear_playlist = _gme_lib.gme_clear_playlist
#gme_clear_playlist.argtypes = [POINTER(Music_Emu)]
#gme_clear_playlist.restype = None

# Gets information for a particular track (length, name, author, etc.).
#Must be freed after use. 
#typedef struct gme_info_t gme_info_t;
class gme_info_t(Structure):
    pass

#gme_err_t gme_track_info( Music_Emu const*, gme_info_t** out, int track );
gme_track_info = _gme_lib.gme_track_info
gme_track_info.argtypes = [POINTER(Music_Emu), POINTER(POINTER(gme_info_t)), c_int]
gme_track_info.restype = gme_err_t

# Frees track information 
#void gme_free_info( gme_info_t* );
gme_free_info = _gme_lib.gme_free_info
gme_free_info.argtypes = [POINTER(gme_info_t)]
gme_free_info.restype = None

gme_info_t._fields_ = [
	# times in milliseconds; -1 if unknown 
    ('length', c_int),  # total length, if file specifies it 
	('intro_length', c_int), #	 length of song up to looping section 
	('loop_length', c_int), #	 length of looping section 
	
	# Length if available, otherwise intro_length+loop_length*2 if available,
	#otherwise a default of 150000 (2.5 minutes). 
	('play_length', c_int),
	
    # reserved 
	('i4', c_int),
	('i5', c_int),
	('i6', c_int),
	('i7', c_int),
	('i8', c_int),
	('i9', c_int),
	('i10', c_int),
	('i11', c_int),
	('i12', c_int),
	('i13', c_int),
	('i14', c_int),
    ('i15', c_int),
	
	# empty string ("") if not available 
	('system', c_char_p),
	('game', c_char_p),
	('song', c_char_p),
	('author', c_char_p),
	('copyright', c_char_p),
	('comment', c_char_p),
	('dumper', c_char_p),
	
    # reserved 
	('s7', c_char_p),
	('s8', c_char_p),
	('s9', c_char_p),
	('s10', c_char_p),
	('s11', c_char_p),
	('s12', c_char_p),
	('s13', c_char_p),
	('s14', c_char_p),
	('s15', c_char_p)
    ]


#******* Advanced playback *******

# Adjust stereo echo depth, where 0.0 = off and 1.0 = maximum. Has no effect for
#GYM, SPC, and Sega Genesis VGM music 
#void gme_set_stereo_depth( Music_Emu*, double depth );
gme_set_stereo_depth = _gme_lib.gme_set_stereo_depth
gme_set_stereo_depth.argtypes = [POINTER(Music_Emu), c_double]
gme_set_stereo_depth.restype = None

# Disable automatic end-of-track detection and skipping of silence at beginning
#if ignore is true 
#void gme_ignore_silence( Music_Emu*, int ignore );
gme_ignore_silence = _gme_lib.gme_ignore_silence
gme_ignore_silence.argtypes = [POINTER(Music_Emu), c_int]
gme_ignore_silence.restype = None

# Adjust song tempo, where 1.0 = normal, 0.5 = half speed, 2.0 = double speed.
#Track length as returned by track_info() assumes a tempo of 1.0. 
#void gme_set_tempo( Music_Emu*, double tempo );
gme_set_tempo = _gme_lib.gme_set_tempo
gme_set_tempo.argtypes = [POINTER(Music_Emu), c_double]
gme_set_tempo.restype = None

# Number of voices used by currently loaded file 
#int gme_voice_count( Music_Emu const* );
gme_voice_count = _gme_lib.gme_voice_count
gme_voice_count.argtypes = [POINTER(Music_Emu)]
gme_voice_count.restype = c_int

# Name of voice i, from 0 to gme_voice_count() - 1 
#const char* gme_voice_name( Music_Emu const*, int i );
gme_voice_name = _gme_lib.gme_voice_name
gme_voice_name.argtypes = [POINTER(Music_Emu), c_int]
gme_voice_name.restype = c_char_p

# Mute/unmute voice i, where voice 0 is first voice 
#void gme_mute_voice( Music_Emu*, int index, int mute );
gme_mute_voice = _gme_lib.gme_mute_voice
gme_mute_voice.argtypes = [POINTER(Music_Emu), c_int, c_int]
gme_mute_voice.restype = None

# Set muting state of all voices at once using a bit mask, where -1 mutes all
#voices, 0 unmutes them all, 0x01 mutes just the first voice, etc. 
#void gme_mute_voices( Music_Emu*, int muting_mask );
gme_mute_voices = _gme_lib.gme_mute_voices
gme_mute_voices.argtypes = [POINTER(Music_Emu), c_int]
gme_mute_voices.restype = None

# Frequency equalizer parameters (see gme.txt) 
class gme_equalizer_t(Structure):
    _fields_ = [
        ('treble', c_double), # -50.0 = muffled, 0 = flat, +5.0 = extra-crisp 
        ('bass', c_double),   # 1 = full bass, 90 = average, 
                              # 16000 = almost no bass 
        
        # reserved 
        ('d2', c_double),
        ('d3', c_double),
        ('d4', c_double),
        ('d5', c_double),
        ('d6', c_double),
        ('d7', c_double),
        ('d8', c_double),
        ('d9', c_double)
    ]

# Get current frequency equalizater parameters 
#void gme_equalizer( Music_Emu const*, gme_equalizer_t* out );
gme_equalizer = _gme_lib.gme_equalizer
gme_equalizer.argtypes = [POINTER(Music_Emu), POINTER(gme_equalizer_t)]
gme_equalizer.restype = None

# Change frequency equalizer parameters 
#void gme_set_equalizer( Music_Emu*, gme_equalizer_t const* eq );
gme_set_equalizer = _gme_lib.gme_set_equalizer
gme_set_equalizer.argtypes = [POINTER(Music_Emu), POINTER(gme_equalizer_t)]
gme_set_equalizer.restype = None



#******* Game music types *******

# Music file type identifier. Can also hold NULL. 
#typedef const struct gme_type_t_* gme_type_t;
class gme_type_t_(Structure):
    _fields_ = [
            ]
gme_type_t = POINTER(gme_type_t_)

# Emulator type constants for each supported file type 
gme_ay_type = gme_type_t
gme_gbs_type = gme_type_t
gme_gym_type = gme_type_t
gme_hes_type = gme_type_t
gme_kss_type = gme_type_t
gme_nsf_type = gme_type_t
gme_nsfe_type = gme_type_t
gme_sap_type = gme_type_t
gme_spc_type = gme_type_t
gme_vgm_type = gme_type_t
gme_vgz_type = gme_type_t

# Type of this emulator 
#gme_type_t gme_type( Music_Emu const* );
gme_type = _gme_lib.gme_type
gme_type.argtypes = [POINTER(Music_Emu)]
gme_type.restype = gme_type_t

# Pointer to array of all music types, with NULL entry at end. Allows a player linked
#to this library to support new music types without having to be updated. 
#gme_type_t const* gme_type_list();
gme_type_list = _gme_lib.gme_type_list
gme_type_list.argtypes = []
gme_type_list.restype = POINTER(gme_type_t)

# Name of game system for this music file type 
#const char* gme_type_system( gme_type_t );
gme_type_system = _gme_lib.gme_type_system
gme_type_system.argtypes = [gme_type_t]
gme_type_system.restype = c_char_p

# True if this music file type supports multiple tracks 
#int gme_type_multitrack( gme_type_t );
#gme_type_multitrack = _gme_lib.gme_type_multitrack
#gme_type_multitrack.argtypes = [gme_type_t]
#gme_type_multitrack.restype = c_int


#******* Advanced file loading *******

# Error returned if file type is not supported 
#extern const char* const gme_wrong_file_type;

# Same as gme_open_file(), but uses file data already in memory. Makes copy of data. 
#gme_err_t gme_open_data( void const* data, long size, Music_Emu** out, int sample_rate );
gme_open_data = _gme_lib.gme_open_data
gme_open_data.argtypes = [c_void_p, c_long, POINTER(POINTER(Music_Emu)), c_int]
gme_open_data.restype = gme_err_t

# Determine likely game music type based on first four bytes of file. Returns
#string containing proper file suffix (i.e. "NSF", "SPC", etc.) or "" if
#file header is not recognized. 
#const char* gme_identify_header( void const* header );
gme_identify_header = _gme_lib.gme_identify_header
gme_identify_header.argtypes = [c_void_p]
gme_identify_header.restype = c_char_p

# Get corresponding music type for file path or extension passed in. 
#gme_type_t gme_identify_extension( const char path_or_extension [] );
gme_identify_extension = _gme_lib.gme_identify_extension
gme_identify_extension.argtypes = [c_char_p]
gme_identify_extension.restype = gme_type_t

# Determine file type based on file's extension or header (if extension isn't recognized).
#Sets *type_out to type, or 0 if unrecognized or error. 
#gme_err_t gme_identify_file( const char path [], gme_type_t* type_out );
gme_identify_file = _gme_lib.gme_identify_file
gme_identify_file.argtypes = [c_char_p, POINTER(gme_type_t)]
gme_identify_file.restype = gme_err_t

# Create new emulator and set sample rate. Returns NULL if out of memory. If you only need
#track information, pass gme_info_only for sample_rate. 
#Music_Emu* gme_new_emu( gme_type_t, int sample_rate );
gme_new_emu = _gme_lib.gme_new_emu
gme_new_emu.argtypes = [gme_type_t, c_int]
gme_new_emu.restype = POINTER(Music_Emu)

# Load music file into emulator 
#gme_err_t gme_load_file( Music_Emu*, const char path [] );
gme_load_file = _gme_lib.gme_load_file
gme_load_file.argtypes = [POINTER(Music_Emu), c_char_p]
gme_load_file.restype = gme_err_t

# Load music file from memory into emulator. Makes a copy of data passed. 
#gme_err_t gme_load_data( Music_Emu*, void const* data, long size );
gme_load_data = _gme_lib.gme_load_data
gme_load_data.argtypes = [POINTER(Music_Emu), c_void_p, c_long]
gme_load_data.restype = gme_err_t

# Load music file using custom data reader function that will be called to
#read file data. Most emulators load the entire file in one read call. 
#typedef gme_err_t (*gme_reader_t)( void* your_data, void* out, int count );
gme_reader_t = CFUNCTYPE(gme_err_t, c_void_p, c_void_p, c_int)

#gme_err_t gme_load_custom( Music_Emu*, gme_reader_t, long file_size, void* your_data );
gme_load_custom = _gme_lib.gme_load_custom
gme_load_custom.argtypes = [POINTER(Music_Emu), gme_reader_t, c_long, c_void_p]
gme_load_custom.restype = gme_err_t

# Load m3u playlist file from memory (must be done after loading music) 
#gme_err_t gme_load_m3u_data( Music_Emu*, void const* data, long size );
gme_load_m3u_data = _gme_lib.gme_load_m3u_data
gme_load_m3u_data.argtypes = [POINTER(Music_Emu), c_void_p, c_long]
gme_load_m3u_data.restype = gme_err_t


#******* User data *******

# Set/get pointer to data you want to associate with this emulator.
#You can use this for whatever you want. 
#void  gme_set_user_data( Music_Emu*, void* new_user_data );
gme_set_user_data = _gme_lib.gme_set_user_data
gme_set_user_data.argtypes = [POINTER(Music_Emu), c_void_p]
gme_set_user_data.restype = None

#void* gme_user_data( Music_Emu const* );
gme_user_data = _gme_lib.gme_user_data
gme_user_data.argtypes = [POINTER(Music_Emu)]
gme_user_data.restype = c_void_p

# Register cleanup function to be called when deleting emulator, or NULL to
#clear it. Passes user_data to cleanup function. 
#typedef void (*gme_user_cleanup_t)( void* user_data );
gme_user_cleanup_t = CFUNCTYPE(c_void_p, c_void_p)

#void gme_set_user_cleanup( Music_Emu*, gme_user_cleanup_t func );
gme_set_user_cleanup = _gme_lib.gme_set_user_cleanup
gme_set_user_cleanup.argtypes = [POINTER(Music_Emu), gme_user_cleanup_t]
gme_set_user_cleanup.restype = None

