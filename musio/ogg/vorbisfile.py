#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# vorbisfile module.
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


""" vorbisfile module.

"""

from ctypes import *
from ctypes.util import find_library

from .codec import *

vorbisfilelib_name = find_library('vorbisfile')
if not vorbisfilelib_name:
    raise Exception("libvorbisfile could not be found")

_vorbisfile_lib = cdll.LoadLibrary(vorbisfilelib_name)

# The function prototypes for the callbacks are basically the same as for
# the stdio functions fread, fseek, fclose, ftell.
# The one difference is that the FILE * arguments have been replaced with
# a void * - this is to be used as a pointer to whatever internal data these
# functions might need. In the stdio case, it's just a FILE * cast to a void *
#
# If you use other functions, check the docs for these functions and return
# the right values. For seek_func(), you *MUST* return -1 if the stream is
# unseekable
#
class _ov_callbacks(Structure):
    _fields_ = [
            ('read_func', CFUNCTYPE(c_size_t, c_void_p, c_size_t, c_size_t, c_void_p)),
            ('seek_func', CFUNCTYPE(c_int, c_void_p, ogg_int64_t, c_int)),
            ('close_func', CFUNCTYPE(c_int, c_void_p)),
            ('tell_func', CFUNCTYPE(c_long, c_void_p))
            ]
ov_callbacks = _ov_callbacks

#ifndef OV_EXCLUDE_STATIC_CALLBACKS

# a few sets of convenient callbacks, especially for use under
# Windows where ov_open_callbacks() should always be used instead of
# ov_open() to avoid problems with incompatible crt.o version linking
# issues. 

#static int _ov_header_fseek_wrap(FILE *f,ogg_int64_t off,int whence){
  #if(f==NULL)return(-1);

#ifdef __MINGW32__
  #return fseeko64(f,off,whence);
#elif defined (_WIN32)
  #return _fseeki64(f,off,whence);
#else
  #return fseek(f,off,whence);
#endif
#}

# These structs below (OV_CALLBACKS_DEFAULT etc) are defined here as
# static data. That means that every file which includes this header
# will get its own copy of these structs whether it uses them or
# not unless it #defines OV_EXCLUDE_STATIC_CALLBACKS.
# These static symbols are essential on platforms such as Windows on
# which several different versions of stdio support may be linked to
# by different DLLs, and we need to be certain we know which one
# we're using (the same one as the main application).
#

#static ov_callbacks OV_CALLBACKS_DEFAULT = {
  #(size_t (*)(void *, size_t, size_t, void *))  fread,
  #(int (*)(void *, ogg_int64_t, int))           _ov_header_fseek_wrap,
  #(int (*)(void *))                             fclose,
  #(long (*)(void *))                            ftell
#};

#static ov_callbacks OV_CALLBACKS_NOCLOSE = {
  #(size_t (*)(void *, size_t, size_t, void *))  fread,
  #(int (*)(void *, ogg_int64_t, int))           _ov_header_fseek_wrap,
  #(int (*)(void *))                             NULL,
  #(long (*)(void *))                            ftell
#};

#static ov_callbacks OV_CALLBACKS_STREAMONLY = {
  #(size_t (*)(void *, size_t, size_t, void *))  fread,
  #(int (*)(void *, ogg_int64_t, int))           NULL,
  #(int (*)(void *))                             fclose,
  #(long (*)(void *))                            NULL
#};

#static ov_callbacks OV_CALLBACKS_STREAMONLY_NOCLOSE = {
  #(size_t (*)(void *, size_t, size_t, void *))  fread,
  #(int (*)(void *, ogg_int64_t, int))           NULL,
  #(int (*)(void *))                             NULL,
  #(long (*)(void *))                            NULL
#};

#endif

NOTOPEN   = 0
PARTOPEN  = 1
OPENED    = 2
STREAMSET = 3
INITSET   = 4

class _OggVorbis_File(Structure):
    _fields_ = [
            ('datasource', c_void_p), #  Pointer to a FILE *, etc. 
            ('seekable', c_int),
            ('offset', ogg_int64_t),
            ('end', ogg_int64_t),
            ('oy', ogg_sync_state),

            # If the FILE handle isn't seekable (eg, a pipe), only the current
             #stream appears 
            ('links', c_int),
            ('offsets', POINTER(ogg_int64_t)),
            ('dataoffsets', POINTER(ogg_int64_t)),
            ('serialnos', POINTER(c_long)),
            ('pcmlengths', POINTER(ogg_int64_t)), #  overloaded to maintain binary
                                          #compatibility; x2 size, stores both
                                          #beginning and end values 
            ('vi', POINTER(vorbis_info)),
            ('vc', POINTER(vorbis_comment)),

            # Decoding working state local storage 
            ('pcm_offset', ogg_int64_t),
            ('ready_state', c_int),
            ('current_serialno', c_long), 
            ('current_link', c_int),

            ('bittrack', c_double), 
            ('samptrack', c_double),

            ('os', ogg_stream_state), #  take physical pages, weld into a logical
                                  #stream of packets 
            ('vd', vorbis_dsp_state), #  central working state for the packet->PCM decoder 
            ('vb', vorbis_block), #  local working space for packet->PCM decode 

            ('callbacks', ov_callbacks)
            ]

OggVorbis_File = _OggVorbis_File


#extern int ov_clear(OggVorbis_File *vf);
ov_clear = _vorbisfile_lib.ov_clear
ov_clear.argtypes = [POINTER(OggVorbis_File)]
ov_clear.restype = c_int

#extern int ov_fopen(char *path,OggVorbis_File *vf);
ov_fopen = _vorbisfile_lib.ov_fopen
ov_fopen.argtypes = [c_char_p, POINTER(OggVorbis_File)]
ov_fopen.restype = c_int

#extern int ov_open(FILE *f,OggVorbis_File *vf,char *initial,long ibytes);
ov_open = _vorbisfile_lib.ov_open
ov_open.argtypes = [POINTER(FILE), POINTER(OggVorbis_File), c_char_p, c_long]
ov_open.restype = c_int

#extern int ov_open_callbacks(void *datasource, OggVorbis_File *vf,
                #char *initial, long ibytes, ov_callbacks callbacks);
ov_open_callbacks = _vorbisfile_lib.ov_open_callbacks
ov_open_callbacks.argtypes = [c_void_p, POINTER(OggVorbis_File), c_char_p, c_long, ov_callbacks]
ov_open_callbacks.restype = c_int


#extern int ov_test(FILE *f,OggVorbis_File *vf,char *initial,long ibytes);
ov_test = _vorbisfile_lib.ov_test
ov_test.argtypes = [POINTER(FILE), POINTER(OggVorbis_File), c_char_p, c_long]
ov_test.restype = c_int

#extern int ov_test_callbacks(void *datasource, OggVorbis_File *vf,
                #char *initial, long ibytes, ov_callbacks callbacks);
ov_test_callbacks = _vorbisfile_lib.ov_test_callbacks
ov_test_callbacks.argtypes = [c_void_p, POINTER(OggVorbis_File), c_char_p, c_long, ov_callbacks]
ov_test_callbacks.restype = c_int

#extern int ov_test_open(OggVorbis_File *vf);
ov_test_open = _vorbisfile_lib.ov_test_open
ov_test_open.argtypes = [POINTER(OggVorbis_File)]
ov_test_open.restype = c_int


#extern long ov_bitrate(OggVorbis_File *vf,int i);
ov_bitrate = _vorbisfile_lib.ov_bitrate
ov_bitrate.argtypes = [POINTER(OggVorbis_File), c_int]
ov_bitrate.restype = c_long

#extern long ov_bitrate_instant(OggVorbis_File *vf);
ov_bitrate_instant = _vorbisfile_lib.ov_bitrate_instant
ov_bitrate_instant.argtypes = [POINTER(OggVorbis_File)]
ov_bitrate_instant.restype = c_long

#extern long ov_streams(OggVorbis_File *vf);
ov_streams = _vorbisfile_lib.ov_streams
ov_streams.argtypes = [POINTER(OggVorbis_File)]
ov_streams.restype = c_long

#extern long ov_seekable(OggVorbis_File *vf);
ov_seekable = _vorbisfile_lib.ov_seekable
ov_seekable.argtypes = [POINTER(OggVorbis_File)]
ov_seekable.restype = c_long

#extern long ov_serialnumber(OggVorbis_File *vf,int i);
ov_serialnumber = _vorbisfile_lib.ov_serialnumber
ov_serialnumber.argtypes = [POINTER(OggVorbis_File), c_int]
ov_serialnumber.restype = c_long


#extern ogg_int64_t ov_raw_total(OggVorbis_File *vf,int i);
ov_raw_total = _vorbisfile_lib.ov_raw_total
ov_raw_total.argtypes = [POINTER(OggVorbis_File), c_int]
ov_raw_total.restype = ogg_int64_t

#extern ogg_int64_t ov_pcm_total(OggVorbis_File *vf,int i);
ov_pcm_total = _vorbisfile_lib.ov_pcm_total
ov_pcm_total.argtypes = [POINTER(OggVorbis_File), c_int]
ov_pcm_total.restype = ogg_int64_t

#extern double ov_time_total(OggVorbis_File *vf,int i);
ov_time_total = _vorbisfile_lib.ov_time_total
ov_time_total.argtypes = [POINTER(OggVorbis_File), c_int]
ov_time_total.restype = c_double


#extern int ov_raw_seek(OggVorbis_File *vf,ogg_int64_t pos);
ov_raw_seek = _vorbisfile_lib.ov_raw_seek
ov_raw_seek.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_raw_seek.restype = c_int

#extern int ov_pcm_seek(OggVorbis_File *vf,ogg_int64_t pos);
ov_pcm_seek = _vorbisfile_lib.ov_pcm_seek
ov_pcm_seek.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_pcm_seek.restype = c_int

#extern int ov_pcm_seek_page(OggVorbis_File *vf,ogg_int64_t pos);
ov_pcm_seek_page = _vorbisfile_lib.ov_pcm_seek_page
ov_pcm_seek_page.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_pcm_seek_page.restype = c_int

#extern int ov_time_seek(OggVorbis_File *vf,double pos);
ov_time_seek = _vorbisfile_lib.ov_time_seek
ov_time_seek.argtypes = [POINTER(OggVorbis_File), c_double]
ov_time_seek.restype = c_int

#extern int ov_time_seek_page(OggVorbis_File *vf,double pos);
ov_time_seek_page = _vorbisfile_lib.ov_time_seek_page
ov_time_seek_page.argtypes = [POINTER(OggVorbis_File), c_double]
ov_time_seek_page.restype = c_int


#extern int ov_raw_seek_lap(OggVorbis_File *vf,ogg_int64_t pos);
ov_raw_seek_lap = _vorbisfile_lib.ov_raw_seek_lap
ov_raw_seek_lap.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_raw_seek_lap.restype = c_int

#extern int ov_pcm_seek_lap(OggVorbis_File *vf,ogg_int64_t pos);
ov_pcm_seek_lap = _vorbisfile_lib.ov_pcm_seek_lap
ov_pcm_seek_lap.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_pcm_seek_lap.restype = c_int

#extern int ov_pcm_seek_page_lap(OggVorbis_File *vf,ogg_int64_t pos);
ov_pcm_seek_page_lap = _vorbisfile_lib.ov_pcm_seek_page_lap
ov_pcm_seek_page_lap.argtypes = [POINTER(OggVorbis_File), ogg_int64_t]
ov_pcm_seek_page_lap.restype = c_int

#extern int ov_time_seek_lap(OggVorbis_File *vf,double pos);
ov_time_seek_lap = _vorbisfile_lib.ov_time_seek_lap
ov_time_seek_lap.argtypes = [POINTER(OggVorbis_File), c_double]
ov_time_seek_lap.restype = c_int

#extern int ov_time_seek_page_lap(OggVorbis_File *vf,double pos);
ov_time_seek_page_lap = _vorbisfile_lib.ov_time_seek_page_lap
ov_time_seek_page_lap.argtypes = [POINTER(OggVorbis_File), c_double]
ov_time_seek_page_lap.restype = c_int


#extern ogg_int64_t ov_raw_tell(OggVorbis_File *vf);
ov_raw_tell = _vorbisfile_lib.ov_raw_tell
ov_raw_tell.argtypes = [POINTER(OggVorbis_File)]
ov_raw_tell.restype = ogg_int64_t

#extern ogg_int64_t ov_pcm_tell(OggVorbis_File *vf);
ov_pcm_tell = _vorbisfile_lib.ov_pcm_tell
ov_pcm_tell.argtypes = [POINTER(OggVorbis_File)]
ov_pcm_tell.restype = ogg_int64_t

#extern double ov_time_tell(OggVorbis_File *vf);
ov_time_tell = _vorbisfile_lib.ov_time_tell
ov_time_tell.argtypes = [POINTER(OggVorbis_File)]
ov_time_tell.restype = c_double


#extern vorbis_info *ov_info(OggVorbis_File *vf,int link);
ov_info = _vorbisfile_lib.ov_info
ov_info.argtypes = [POINTER(OggVorbis_File), c_int]
ov_info.restype = POINTER(vorbis_info)

#extern vorbis_comment *ov_comment(OggVorbis_File *vf,int link);
ov_comment = _vorbisfile_lib.ov_comment
ov_comment.argtypes = [POINTER(OggVorbis_File), c_int]
ov_comment.restype = POINTER(vorbis_comment)


#extern long ov_read_float(OggVorbis_File *vf,float ***pcm_channels,int samples,
                          #int *bitstream);
ov_read_float = _vorbisfile_lib.ov_read_float
ov_read_float.argtypes = [POINTER(OggVorbis_File), POINTER(POINTER(POINTER(c_float))), c_int, POINTER(c_int)]
ov_read_float.restype = c_long

#extern long ov_read_filter(OggVorbis_File *vf,char *buffer,int length,
                          #int bigendianp,int word,int sgned,int *bitstream,
                          #void (*filter)(float **pcm,long channels,long samples,void *filter_param),void *filter_param);
ov_read_filter = _vorbisfile_lib.ov_read_filter
ov_read_filter.argtypes = [POINTER(OggVorbis_File), c_char_p, c_int, c_int, c_int, c_int, POINTER(c_int), CFUNCTYPE(None, POINTER(POINTER(c_float)), c_long, c_long, c_void_p), c_void_p]
ov_read_filter.restype = c_long

#extern long ov_read(OggVorbis_File *vf,char *buffer,int length,
                    #int bigendianp,int word,int sgned,int *bitstream);
ov_read = _vorbisfile_lib.ov_read
ov_read.argtypes = [POINTER(OggVorbis_File), c_char_p, c_int, c_int, c_int, c_int, POINTER(c_int)]
ov_read.restype = c_long

#extern int ov_crosslap(OggVorbis_File *vf1,OggVorbis_File *vf2);
ov_crosslap = _vorbisfile_lib.ov_crosslap
ov_crosslap.argtypes = [POINTER(OggVorbis_File), POINTER(OggVorbis_File)]
ov_crosslap.restype = c_int


#extern int ov_halfrate(OggVorbis_File *vf,int flag);
ov_halfrate = _vorbisfile_lib.ov_halfrate
ov_halfrate.argtypes = [POINTER(OggVorbis_File), c_int]
ov_halfrate.restype = c_int

#extern int ov_halfrate_p(OggVorbis_File *vf);
ov_halfrate_p = _vorbisfile_lib.ov_halfrate_p
ov_halfrate_p.argtypes = [POINTER(OggVorbis_File)]
ov_halfrate_p.restype = c_int

