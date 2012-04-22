#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# vorbis codec module.
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


""" vorbis codec module.

"""

from ctypes import *
from ctypes.util import find_library

from .ogg import *

vorbislib_name = find_library('vorbis')
if not vorbislib_name:
    raise Exception("libvorbis could not be found")

_vorbis_lib = cdll.LoadLibrary(vorbislib_name)

class _vorbis_info(Structure):
    _fields_ = [
            ('version', c_int),
            ('channels', c_int), 
            ('rate', c_long), 

            # The below bitrate declarations are *hints*.
             #Combinations of the three values carry the following implications:

             #all three set to the same value:
               #implies a fixed rate bitstream
             #only nominal set:
               #implies a VBR stream that averages the nominal bitrate.  No hard
               #upper/lower limit
             #upper and or lower set:
               #implies a VBR bitstream that obeys the bitrate limits. nominal
               #may also be set to give a nominal rate.
             #none set:
               #the coder does not care to speculate.
            #

            ('bitrate_upper', c_long),
            ('bitrate_nominal', c_long), 
            ('bitrate_lower', c_long),
            ('bitrate_window', c_long),

            ('codec_setup', c_void_p)
            ]
vorbis_info = _vorbis_info

# vorbis_dsp_state buffers the current vorbis audio
   #analysis/synthesis state.  The DSP state belongs to a specific
   #logical bitstream ***************************************************
class _vorbis_dsp_state(Structure):
    _fields_ = [
            ('analysisp', c_int),
            ('vi', POINTER(vorbis_info)),

            ('pcm', POINTER(POINTER(c_float))),
            ('pcmret', POINTER(POINTER(c_float))),
            ('pcm_storage', c_int),
            ('pcm_current', c_int),
            ('pcm_returned', c_int),

            ('preextrapolate', c_int),
            ('eofflat', c_int),

            ('lW', c_long),
            ('W', c_long),
            ('nW', c_long),
            ('centerW', c_long),

            ('granulepos', ogg_int64_t),
            ('sequence', ogg_int64_t),

            ('glue_bits', ogg_int64_t),
            ('time_bits', ogg_int64_t),
            ('floor_bits', ogg_int64_t),
            ('res_bits', ogg_int64_t),

            ('backend_state', c_void_p)
            ]
vorbis_dsp_state = _vorbis_dsp_state

class alloc_chain(Structure):
    pass

class _vorbis_block(Structure):
    _fields_ = [
            # necessary stream state for linking to the framing abstraction 
            ('pcm', POINTER(POINTER(c_float))), #  this is a pointer into local storage 
            ('opb', oggpack_buffer),

            ('lW', c_long),
            ('W', c_long),
            ('nW', c_long),
            ('pcmend', c_int),
            ('mode', c_int),

            ('eofflat', c_int),
            ('granulepos', ogg_int64_t),
            ('sequence', ogg_int64_t),
            ('vd', POINTER(vorbis_dsp_state)), #  For read-only access of configuration 

            # local storage to avoid remallocing; it's up to the mapping to
             #structure it 
            ('localstore', c_void_p),
            ('localtop', c_long),
            ('localalloc', c_long),
            ('totaluse', c_long),
            ('reap', POINTER(alloc_chain)),

            # bitmetrics for the frame 
            ('glue_bits', c_long),
            ('time_bits', c_long),
            ('floor_bits', c_long),
            ('res_bits', c_long),

            ('internal', c_void_p)
            ]

vorbis_block = _vorbis_block

# vorbis_block is a single block of data to be processed as part of
#the analysis/synthesis stream; it belongs to a specific logical
#bitstream, but is independent from other vorbis_blocks belonging to
#that logical bitstream. ************************************************

alloc_chain._fields_ = [
        ('ptr', c_void_p),
        ('next', POINTER(alloc_chain))
        ]

# vorbis_info contains all the setup information specific to the
   #specific compression/decompression mode in progress (eg,
   #psychoacoustic settings, channel setup, options, codebook
   #etc). vorbis_info and substructures are in backends.h.
#*******************************************************************

# the comments are not part of vorbis_info so that vorbis_info can be
   #static storage 
class _vorbis_comment(Structure):
    _fields_ = [
            # unlimited user comment fields.  libvorbis writes 'libvorbis'
             #whatever vendor is set to in encode 
            ('user_comments', POINTER(c_char_p)),
            ('comment_lengths', POINTER(c_int)),
            ('comments', c_int),
            ('vendor', c_char_p)
            ]

vorbis_comment = _vorbis_comment


# libvorbis encodes in two abstraction layers; first we perform DSP
   #and produce a packet (see docs/analysis.txt).  The packet is then
   #coded into a framed OggSquish bitstream by the second layer (see
   #docs/framing.txt).  Decode is the reverse process; we sync/frame
   #the bitstream and extract individual packets, then decode the
   #packet back into PCM audio.

   #The extra framing/packetizing is used in streaming formats, such as
   #files.  Over the net (such as with UDP), the framing and
   #packetization aren't necessary as they're provided by the transport
   #and the streaming layer is not used 

# Vorbis PRIMITIVES: general **************************************

#extern void     vorbis_info_init(vorbis_info *vi);
vorbis_info_init = _vorbis_lib.vorbis_info_init
vorbis_info_init.argtypes = [POINTER(vorbis_info)]
vorbis_info_init.restype = None

#extern void     vorbis_info_clear(vorbis_info *vi);
vorbis_info_clear = _vorbis_lib.vorbis_info_clear
vorbis_info_clear.argtypes = [POINTER(vorbis_info)]
vorbis_info_clear.restype = None

#extern int      vorbis_info_blocksize(vorbis_info *vi,int zo);
vorbis_info_blocksize = _vorbis_lib.vorbis_info_blocksize
vorbis_info_blocksize.argtypes = [POINTER(vorbis_info), c_int]
vorbis_info_blocksize.restype = c_int

#extern void     vorbis_comment_init(vorbis_comment *vc);
vorbis_comment_init = _vorbis_lib.vorbis_comment_init
vorbis_comment_init.argtypes = [POINTER(vorbis_comment)]
vorbis_comment_init.restype = None

#extern void     vorbis_comment_add(vorbis_comment *vc, const char *comment);
vorbis_comment_add = _vorbis_lib.vorbis_comment_add
vorbis_comment_add.argtypes = [POINTER(vorbis_comment), c_char_p]
vorbis_comment_add.restype = None

#extern void     vorbis_comment_add_tag(vorbis_comment *vc,
                                       #const char *tag, const char *contents);
vorbis_comment_add_tag = _vorbis_lib.vorbis_comment_add_tag
vorbis_comment_add_tag.argtypes = [POINTER(vorbis_comment), c_char_p, c_char_p]
vorbis_comment_add_tag.restype = None

#extern char    *vorbis_comment_query(vorbis_comment *vc, const char *tag, int count);
vorbis_comment_query = _vorbis_lib.vorbis_comment_query
vorbis_comment_query.argtypes = [POINTER(vorbis_comment), c_char_p, c_int]
vorbis_comment_query.restype = c_char_p

#extern int      vorbis_comment_query_count(vorbis_comment *vc, const char *tag);
vorbis_comment_query_count = _vorbis_lib.vorbis_comment_query_count
vorbis_comment_query_count.argtypes = [POINTER(vorbis_comment), c_char_p]
vorbis_comment_query_count.restype = c_int

#extern void     vorbis_comment_clear(vorbis_comment *vc);
vorbis_comment_clear = _vorbis_lib.vorbis_comment_clear
vorbis_comment_clear.argtypes = [POINTER(vorbis_comment)]
vorbis_comment_clear.restype = None


#extern int      vorbis_block_init(vorbis_dsp_state *v, vorbis_block *vb);
vorbis_block_init = _vorbis_lib.vorbis_block_init
vorbis_block_init.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_block)]
vorbis_block_init.restype = c_int

#extern int      vorbis_block_clear(vorbis_block *vb);
vorbis_block_clear = _vorbis_lib.vorbis_block_clear
vorbis_block_clear.argtypes = [POINTER(vorbis_block)]
vorbis_block_clear.restype = c_int

#extern void     vorbis_dsp_clear(vorbis_dsp_state *v);
vorbis_dsp_clear = _vorbis_lib.vorbis_dsp_clear
vorbis_dsp_clear.argtypes = [POINTER(vorbis_dsp_state)]
vorbis_dsp_clear.restype = None

#extern double   vorbis_granule_time(vorbis_dsp_state *v,
                                    #ogg_int64_t granulepos);
vorbis_granule_time = _vorbis_lib.vorbis_granule_time
vorbis_granule_time.argtypes = [POINTER(vorbis_dsp_state), ogg_int64_t]
vorbis_granule_time.restype = c_double


#extern const char *vorbis_version_string(void);
vorbis_version_string = _vorbis_lib.vorbis_version_string
vorbis_version_string.argtypes = []
vorbis_version_string.restype = c_char_p


# Vorbis PRIMITIVES: analysis/DSP layer ***************************

#extern int      vorbis_analysis_init(vorbis_dsp_state *v,vorbis_info *vi);
vorbis_analysis_init = _vorbis_lib.vorbis_analysis_init
vorbis_analysis_init.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_info)]
vorbis_analysis_init.restype = c_int

#extern int      vorbis_commentheader_out(vorbis_comment *vc, ogg_packet *op);
vorbis_commentheader_out = _vorbis_lib.vorbis_commentheader_out
vorbis_commentheader_out.argtypes = [POINTER(vorbis_comment), POINTER(ogg_packet)]
vorbis_commentheader_out.restype = c_int

#extern int      vorbis_analysis_headerout(vorbis_dsp_state *v,
                                          #vorbis_comment *vc,
                                          #ogg_packet *op,
                                          #ogg_packet *op_comm,
                                          #ogg_packet *op_code);
vorbis_analysis_headerout = _vorbis_lib.vorbis_analysis_headerout
vorbis_analysis_headerout.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_comment), POINTER(ogg_packet), POINTER(ogg_packet), POINTER(ogg_packet)]
vorbis_analysis_headerout.restype = c_int

#extern float  **vorbis_analysis_buffer(vorbis_dsp_state *v,int vals);
vorbis_analysis_buffer = _vorbis_lib.vorbis_analysis_buffer
vorbis_analysis_buffer.argtypes = [POINTER(vorbis_dsp_state), c_int]
vorbis_analysis_buffer.restype = POINTER(POINTER(c_float))

#extern int      vorbis_analysis_wrote(vorbis_dsp_state *v,int vals);
vorbis_analysis_wrote = _vorbis_lib.vorbis_analysis_wrote
vorbis_analysis_wrote.argtypes = [POINTER(vorbis_dsp_state), c_int]
vorbis_analysis_wrote.restype = c_int

#extern int      vorbis_analysis_blockout(vorbis_dsp_state *v,vorbis_block *vb);
vorbis_analysis_blockout = _vorbis_lib.vorbis_analysis_blockout
vorbis_analysis_blockout.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_block)]
vorbis_analysis_blockout.restype = c_int

#extern int      vorbis_analysis(vorbis_block *vb,ogg_packet *op);
vorbis_analysis = _vorbis_lib.vorbis_analysis
vorbis_analysis.argtypes = [POINTER(vorbis_block), POINTER(ogg_packet)]
vorbis_analysis.restype = c_int


#extern int      vorbis_bitrate_addblock(vorbis_block *vb);
vorbis_bitrate_addblock = _vorbis_lib.vorbis_bitrate_addblock
vorbis_bitrate_addblock.argtypes = [POINTER(vorbis_block)]
vorbis_bitrate_addblock.restype = c_int

#extern int      vorbis_bitrate_flushpacket(vorbis_dsp_state *vd,
                                           #ogg_packet *op);
vorbis_bitrate_flushpacket = _vorbis_lib.vorbis_bitrate_flushpacket
vorbis_bitrate_flushpacket.argtypes = [POINTER(vorbis_dsp_state), POINTER(ogg_packet)]
vorbis_bitrate_flushpacket.restype = c_int


# Vorbis PRIMITIVES: synthesis layer ******************************
#extern int      vorbis_synthesis_idheader(ogg_packet *op);
vorbis_synthesis_idheader = _vorbis_lib.vorbis_synthesis_idheader
vorbis_synthesis_idheader.argtypes = [POINTER(ogg_packet)]
vorbis_synthesis_idheader.restype = c_int

#extern int      vorbis_synthesis_headerin(vorbis_info *vi,vorbis_comment *vc,
                                          #ogg_packet *op);
vorbis_synthesis_headerin = _vorbis_lib.vorbis_synthesis_headerin
vorbis_synthesis_headerin.argtypes = [POINTER(vorbis_info), POINTER(vorbis_comment), POINTER(ogg_packet)]
vorbis_synthesis_headerin.restype = c_int


#extern int      vorbis_synthesis_init(vorbis_dsp_state *v,vorbis_info *vi);
vorbis_synthesis_init = _vorbis_lib.vorbis_synthesis_init
vorbis_synthesis_init.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_info)]
vorbis_synthesis_init.restype = c_int

#extern int      vorbis_synthesis_restart(vorbis_dsp_state *v);
vorbis_synthesis_restart = _vorbis_lib.vorbis_synthesis_restart
vorbis_synthesis_restart.argtypes = [POINTER(vorbis_dsp_state)]
vorbis_synthesis_restart.restype = c_int

#extern int      vorbis_synthesis(vorbis_block *vb,ogg_packet *op);
vorbis_synthesis = _vorbis_lib.vorbis_synthesis
vorbis_synthesis.argtypes = [POINTER(vorbis_block), POINTER(ogg_packet)]
vorbis_synthesis.restype = c_int

#extern int      vorbis_synthesis_trackonly(vorbis_block *vb,ogg_packet *op);
vorbis_synthesis_trackonly = _vorbis_lib.vorbis_synthesis_trackonly
vorbis_synthesis_trackonly.argtypes = [POINTER(vorbis_block), POINTER(ogg_packet)]
vorbis_synthesis_trackonly.restype = c_int

#extern int      vorbis_synthesis_blockin(vorbis_dsp_state *v,vorbis_block *vb);
vorbis_synthesis_blockin = _vorbis_lib.vorbis_synthesis_blockin
vorbis_synthesis_blockin.argtypes = [POINTER(vorbis_dsp_state), POINTER(vorbis_block)]
vorbis_synthesis_blockin.restype = c_int

#extern int      vorbis_synthesis_pcmout(vorbis_dsp_state *v,float ***pcm);
vorbis_synthesis_pcmout = _vorbis_lib.vorbis_synthesis_pcmout
vorbis_synthesis_pcmout.argtypes = [POINTER(vorbis_dsp_state), POINTER(POINTER(POINTER(c_float)))]
vorbis_synthesis_pcmout.restype = c_int

#extern int      vorbis_synthesis_lapout(vorbis_dsp_state *v,float ***pcm);
vorbis_synthesis_lapout = _vorbis_lib.vorbis_synthesis_lapout
vorbis_synthesis_lapout.argtypes = [POINTER(vorbis_dsp_state), POINTER(POINTER(POINTER(c_float)))]
vorbis_synthesis_lapout.restype = c_int

#extern int      vorbis_synthesis_read(vorbis_dsp_state *v,int samples);
vorbis_synthesis_read = _vorbis_lib.vorbis_synthesis_read
vorbis_synthesis_read.argtypes = [POINTER(vorbis_dsp_state), c_int]
vorbis_synthesis_read.restype = c_int

#extern long     vorbis_packet_blocksize(vorbis_info *vi,ogg_packet *op);
vorbis_packet_blocksize = _vorbis_lib.vorbis_packet_blocksize
vorbis_packet_blocksize.argtypes = [POINTER(vorbis_info), POINTER(ogg_packet)]
vorbis_packet_blocksize.restype = c_long


#extern int      vorbis_synthesis_halfrate(vorbis_info *v,int flag);
vorbis_synthesis_halfrate = _vorbis_lib.vorbis_synthesis_halfrate
vorbis_synthesis_halfrate.argtypes = [POINTER(vorbis_info), c_int]
vorbis_synthesis_halfrate.restype = c_int

#extern int      vorbis_synthesis_halfrate_p(vorbis_info *v);
vorbis_synthesis_halfrate_p = _vorbis_lib.vorbis_synthesis_halfrate_p
vorbis_synthesis_halfrate_p.argtypes = [POINTER(vorbis_info)]
vorbis_synthesis_halfrate_p.restype = c_int


# Vorbis ERRORS and return codes **********************************

OV_FALSE      = -1
OV_EOF        = -2
OV_HOLE       = -3

OV_EREAD      = -128
OV_EFAULT     = -129
OV_EIMPL      = -130
OV_EINVAL     = -131
OV_ENOTVORBIS = -132
OV_EBADHEADER = -133
OV_EVERSION   = -134
OV_ENOTAUDIO  = -135
OV_EBADPACKET = -136
OV_EBADLINK   = -137
OV_ENOSEEK    = -138
