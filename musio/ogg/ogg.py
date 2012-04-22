#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# ogg module.
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


""" ogg module.

"""

from ctypes import *
from ctypes.util import find_library

from .config_types import *

ogglib_name = find_library('ogg')
if not ogglib_name:
    raise Exception("libogg could not be found")

_ogg_lib = cdll.LoadLibrary(ogglib_name)

class _ogg_iovec_t(Structure):
    _fields_ = [
            ('iov_base', c_void_p),
            ('iov_len', c_size_t)
            ]
ogg_iovec_t = _ogg_iovec_t

class _oggpack_buffer(Structure):
    _fields_ = [
            ('endbyte', c_long),
            ('endbit', c_int),

            ('buffer', POINTER(c_ubyte)),
            ('ptr', POINTER(c_ubyte)),
            ('storage', c_long)
            ]
oggpack_buffer = _oggpack_buffer

# ogg_page is used to encapsulate the data in one Ogg bitstream page ****

class _ogg_page(Structure):
    _fields_ = [
            ('header', POINTER(c_ubyte)), 
            ('header_len', c_long),
            ('body', POINTER(c_ubyte)),
            ('body_len', c_long)
            ]
ogg_page = _ogg_page

# ogg_stream_state contains the current encode/decode state of a logical
#Ogg bitstream *********************************************************

class _ogg_stream_state(Structure):
    _fields_ = [
            ('body_data', POINTER(c_ubyte)), #  bytes from packet bodies 
            ('body_storage', c_long), #  storage elements allocated 
            ('body_fill', c_long), #  elements stored; fill mark 
            ('body_returned', c_long), #  elements of fill returned 


            ('lacing_vals', POINTER(c_int)), #  The values that will go to the segment table 
            ('granule_vals', POINTER(ogg_int64_t)), #  granulepos values for headers. Not compact
#this way, but it is simple coupled to the
#lacing fifo 
            ('lacing_storage', c_long),
            ('lacing_fill', c_long),
            ('lacing_packet', c_long),
            ('lacing_returned', c_long),

            ('header', c_ubyte * 282), #  working space for header encode 
            ('header_fill', c_int),

            ('e_o_s', c_int), #  set when we have buffered the last packet in the
#logical bitstream 
            ('b_o_s', c_int), #  set after we've written the initial page
#of a logical bitstream 
            ('serialno', c_long),
            ('pageno', c_long),
            ('packetno', ogg_int64_t), #  sequence number for decode; the framing
#knows where there's a hole in the data,
#but we need coupling so that the codec
#(which is in a seperate abstraction
#layer) also knows about the gap 
            ('granulepos', ogg_int64_t)
            ]

ogg_stream_state = _ogg_stream_state

# ogg_packet is used to encapsulate the data and metadata belonging
#to a single raw Ogg/Vorbis packet ************************************

class _ogg_packet(Structure):
    _fields_ = [
            ('packet', POINTER(c_ubyte)),
            ('bytes', c_long),
            ('b_o_s', c_long),
            ('e_o_s', c_long),

            ('granulepos', ogg_int64_t),

            ('packetno', ogg_int64_t), #  sequence number for decode; the framing
# knows where there's a hole in the data,
# but we need coupling so that the codec
# (which is in a seperate abstraction
# layer) also knows about the gap 
            ]
ogg_packet = _ogg_packet

class _ogg_sync_state(Structure):
    _fields_ = [
            ('data', POINTER(c_ubyte)),
            ('storage', c_int),
            ('fill', c_int),
            ('returned', c_int),

            ('unsynced', c_int),
            ('headerbytes', c_int),
            ('bodybytes', c_int)
            ]
ogg_sync_state = _ogg_sync_state

# Ogg BITSTREAM PRIMITIVES: bitstream ***********************

#extern void  oggpack_writeinit(oggpack_buffer *b);
oggpack_writeinit = _ogg_lib.oggpack_writeinit
oggpack_writeinit.argtypes = [POINTER(oggpack_buffer)]
oggpack_writeinit.restype = None

#extern int   oggpack_writecheck(oggpack_buffer *b);
oggpack_writecheck = _ogg_lib.oggpack_writecheck
oggpack_writecheck.argtypes = [POINTER(oggpack_buffer)]
oggpack_writecheck.restype = c_int

#extern void  oggpack_writetrunc(oggpack_buffer *b,long bits);
oggpack_writetrunc = _ogg_lib.oggpack_writetrunc
oggpack_writetrunc.argtypes = [POINTER(oggpack_buffer), c_long]
oggpack_writetrunc.restype = None

#extern void  oggpack_writealign(oggpack_buffer *b);
oggpack_writealign = _ogg_lib.oggpack_writealign
oggpack_writealign.argtypes = [POINTER(oggpack_buffer)]
oggpack_writealign.restype = None

#extern void  oggpack_writecopy(oggpack_buffer *b,void *source,long bits);
oggpack_writecopy = _ogg_lib.oggpack_writecopy
oggpack_writecopy.argtypes = [POINTER(oggpack_buffer), c_void_p, c_long]
oggpack_writecopy.restype = None

#extern void  oggpack_reset(oggpack_buffer *b);
oggpack_reset = _ogg_lib.oggpack_reset
oggpack_reset.argtypes = [POINTER(oggpack_buffer)]
oggpack_reset.restype = None

#extern void  oggpack_writeclear(oggpack_buffer *b);
oggpack_writeclear = _ogg_lib.oggpack_writeclear
oggpack_writeclear.argtypes = [POINTER(oggpack_buffer)]
oggpack_writeclear.restype = None

#extern void  oggpack_readinit(oggpack_buffer *b,unsigned char *buf,int bytes);
oggpack_readinit = _ogg_lib.oggpack_readinit
oggpack_readinit.argtypes = [POINTER(oggpack_buffer), POINTER(c_ubyte), c_int]
oggpack_readinit.restype = None

#extern void  oggpack_write(oggpack_buffer *b,unsigned long value,int bits);
oggpack_write = _ogg_lib.oggpack_write
oggpack_write.argtypes = [POINTER(oggpack_buffer), c_ulong, c_int]
oggpack_write.restype = None

#extern long  oggpack_look(oggpack_buffer *b,int bits);
oggpack_look = _ogg_lib.oggpack_look
oggpack_look.argtypes = [POINTER(oggpack_buffer), c_int]
oggpack_look.restype = c_long

#extern long  oggpack_look1(oggpack_buffer *b);
oggpack_look1 = _ogg_lib.oggpack_look1
oggpack_look1.argtypes = [POINTER(oggpack_buffer)]
oggpack_look1.restype = c_long

#extern void  oggpack_adv(oggpack_buffer *b,int bits);
oggpack_adv = _ogg_lib.oggpack_adv
oggpack_adv.argtypes = [POINTER(oggpack_buffer), c_int]
oggpack_adv.restype = None

#extern void  oggpack_adv1(oggpack_buffer *b);
oggpack_adv1 = _ogg_lib.oggpack_adv1
oggpack_adv1.argtypes = [POINTER(oggpack_buffer)]
oggpack_adv1.restype = None

#extern long  oggpack_read(oggpack_buffer *b,int bits);
oggpack_read = _ogg_lib.oggpack_read
oggpack_read.argtypes = [POINTER(oggpack_buffer), c_int]
oggpack_read.restype = c_long

#extern long  oggpack_read1(oggpack_buffer *b);
oggpack_read1 = _ogg_lib.oggpack_read1
oggpack_read1.argtypes = [POINTER(oggpack_buffer)]
oggpack_read1.restype = c_long

#extern long  oggpack_bytes(oggpack_buffer *b);
oggpack_bytes = _ogg_lib.oggpack_bytes
oggpack_bytes.argtypes = [POINTER(oggpack_buffer)]
oggpack_bytes.restype = c_long

#extern long  oggpack_bits(oggpack_buffer *b);
oggpack_bits = _ogg_lib.oggpack_bits
oggpack_bits.argtypes = [POINTER(oggpack_buffer)]
oggpack_bits.restype = c_long

#extern unsigned char *oggpack_get_buffer(oggpack_buffer *b);
oggpack_get_buffer = _ogg_lib.oggpack_get_buffer
oggpack_get_buffer.argtypes = [POINTER(oggpack_buffer)]
oggpack_get_buffer.restype = POINTER(c_ubyte)


#extern void  oggpackB_writeinit(oggpack_buffer *b);
oggpackB_writeinit = _ogg_lib.oggpackB_writeinit
oggpackB_writeinit.argtypes = [POINTER(oggpack_buffer)]
oggpackB_writeinit.restype = None

#extern int   oggpackB_writecheck(oggpack_buffer *b);
oggpackB_writecheck = _ogg_lib.oggpackB_writecheck
oggpackB_writecheck.argtypes = [POINTER(oggpack_buffer)]
oggpackB_writecheck.restype = c_int

#extern void  oggpackB_writetrunc(oggpack_buffer *b,long bits);
oggpackB_writetrunc = _ogg_lib.oggpackB_writetrunc
oggpackB_writetrunc.argtypes = [POINTER(oggpack_buffer), c_long]
oggpackB_writetrunc.restype = None

#extern void  oggpackB_writealign(oggpack_buffer *b);
oggpackB_writealign = _ogg_lib.oggpackB_writealign
oggpackB_writealign.argtypes = [POINTER(oggpack_buffer)]
oggpackB_writealign.restype = None

#extern void  oggpackB_writecopy(oggpack_buffer *b,void *source,long bits);
oggpackB_writecopy = _ogg_lib.oggpackB_writecopy
oggpackB_writecopy.argtypes = [POINTER(oggpack_buffer), c_void_p, c_long]
oggpackB_writecopy.restype = None

#extern void  oggpackB_reset(oggpack_buffer *b);
oggpackB_reset = _ogg_lib.oggpackB_reset
oggpackB_reset.argtypes = [POINTER(oggpack_buffer)]
oggpackB_reset.restype = None

#extern void  oggpackB_writeclear(oggpack_buffer *b);
oggpackB_writeclear = _ogg_lib.oggpackB_writeclear
oggpackB_writeclear.argtypes = [POINTER(oggpack_buffer)]
oggpackB_writeclear.restype = None

#extern void  oggpackB_readinit(oggpack_buffer *b,unsigned char *buf,int bytes);
oggpackB_readinit = _ogg_lib.oggpackB_readinit
oggpackB_readinit.argtypes = [POINTER(oggpack_buffer), POINTER(c_ubyte), c_int]
oggpackB_readinit.restype = None

#extern void  oggpackB_write(oggpack_buffer *b,unsigned long value,int bits);
oggpackB_write = _ogg_lib.oggpackB_write
oggpackB_write.argtypes = [POINTER(oggpack_buffer), c_ulong, c_int]
oggpackB_write.restype = None

#extern long  oggpackB_look(oggpack_buffer *b,int bits);
oggpackB_look = _ogg_lib.oggpackB_look
oggpackB_look.argtypes = [POINTER(oggpack_buffer), c_int]
oggpackB_look.restype = c_long

#extern long  oggpackB_look1(oggpack_buffer *b);
oggpackB_look1 = _ogg_lib.oggpackB_look1
oggpackB_look1.argtypes = [POINTER(oggpack_buffer)]
oggpackB_look1.restype = c_long

#extern void  oggpackB_adv(oggpack_buffer *b,int bits);
oggpackB_adv = _ogg_lib.oggpackB_adv
oggpackB_adv.argtypes = [POINTER(oggpack_buffer), c_int]
oggpackB_adv.restype = None

#extern void  oggpackB_adv1(oggpack_buffer *b);
oggpackB_adv1 = _ogg_lib.oggpackB_adv1
oggpackB_adv1.argtypes = [POINTER(oggpack_buffer)]
oggpackB_adv1.restype = None

#extern long  oggpackB_read(oggpack_buffer *b,int bits);
oggpackB_read = _ogg_lib.oggpackB_read
oggpackB_read.argtypes = [POINTER(oggpack_buffer), c_int]
oggpackB_read.restype = c_long

#extern long  oggpackB_read1(oggpack_buffer *b);
oggpackB_read1 = _ogg_lib.oggpackB_read1
oggpackB_read1.argtypes = [POINTER(oggpack_buffer)]
oggpackB_read1.restype = c_long

#extern long  oggpackB_bytes(oggpack_buffer *b);
oggpackB_bytes = _ogg_lib.oggpackB_bytes
oggpackB_bytes.argtypes = [POINTER(oggpack_buffer)]
oggpackB_bytes.restype = c_long

#extern long  oggpackB_bits(oggpack_buffer *b);
oggpackB_bits = _ogg_lib.oggpackB_bits
oggpackB_bits.argtypes = [POINTER(oggpack_buffer)]
oggpackB_bits.restype = c_long

#extern unsigned char *oggpackB_get_buffer(oggpack_buffer *b);
oggpackB_get_buffer = _ogg_lib.oggpackB_get_buffer
oggpackB_get_buffer.argtypes = [POINTER(oggpack_buffer)]
oggpackB_get_buffer.restype = POINTER(c_ubyte)


# Ogg BITSTREAM PRIMITIVES: encoding *************************

#extern int      ogg_stream_packetin(ogg_stream_state *os, ogg_packet *op);
ogg_stream_packetin = _ogg_lib.ogg_stream_packetin
ogg_stream_packetin.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_packet)]
ogg_stream_packetin.restype = c_int

#extern int      ogg_stream_iovecin(ogg_stream_state *os, ogg_iovec_t *iov,
#int count, long e_o_s, ogg_int64_t granulepos);
ogg_stream_iovecin = _ogg_lib.ogg_stream_iovecin
ogg_stream_iovecin.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_iovec_t), c_int, c_long, ogg_int64_t]
ogg_stream_iovecin.restype = c_int

#extern int      ogg_stream_pageout(ogg_stream_state *os, ogg_page *og);
ogg_stream_pageout = _ogg_lib.ogg_stream_pageout
ogg_stream_pageout.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_page)]
ogg_stream_pageout.restype = c_int

#extern int      ogg_stream_flush(ogg_stream_state *os, ogg_page *og);
ogg_stream_flush = _ogg_lib.ogg_stream_flush
ogg_stream_flush.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_page)]
ogg_stream_flush.restype = c_int


# Ogg BITSTREAM PRIMITIVES: decoding *************************

#extern int      ogg_sync_init(ogg_sync_state *oy);
ogg_sync_init = _ogg_lib.ogg_sync_init
ogg_sync_init.argtypes = [POINTER(ogg_sync_state)]
ogg_sync_init.restype = c_int

#extern int      ogg_sync_clear(ogg_sync_state *oy);
ogg_sync_clear = _ogg_lib.ogg_sync_clear
ogg_sync_clear.argtypes = [POINTER(ogg_sync_state)]
ogg_sync_clear.restype = c_int

#extern int      ogg_sync_reset(ogg_sync_state *oy);
ogg_sync_reset = _ogg_lib.ogg_sync_reset
ogg_sync_reset.argtypes = [POINTER(ogg_sync_state)]
ogg_sync_reset.restype = c_int

#extern int      ogg_sync_destroy(ogg_sync_state *oy);
ogg_sync_destroy = _ogg_lib.ogg_sync_destroy
ogg_sync_destroy.argtypes = [POINTER(ogg_sync_state)]
ogg_sync_destroy.restype = c_int

#extern int      ogg_sync_check(ogg_sync_state *oy);
ogg_sync_check = _ogg_lib.ogg_sync_check
ogg_sync_check.argtypes = [POINTER(ogg_sync_state)]
ogg_sync_check.restype = c_int


#extern char    *ogg_sync_buffer(ogg_sync_state *oy, long size);
ogg_sync_buffer = _ogg_lib.ogg_sync_buffer
ogg_sync_buffer.argtypes = [POINTER(ogg_sync_state), c_long]
ogg_sync_buffer.restype = c_char_p

#extern int      ogg_sync_wrote(ogg_sync_state *oy, long bytes);
ogg_sync_wrote = _ogg_lib.ogg_sync_wrote
ogg_sync_wrote.argtypes = [POINTER(ogg_sync_state), c_long]
ogg_sync_wrote.restype = c_int

#extern long     ogg_sync_pageseek(ogg_sync_state *oy,ogg_page *og);
ogg_sync_pageseek = _ogg_lib.ogg_sync_pageseek
ogg_sync_pageseek.argtypes = [POINTER(ogg_sync_state), POINTER(ogg_page)]
ogg_sync_pageseek.restype = c_long

#extern int      ogg_sync_pageout(ogg_sync_state *oy, ogg_page *og);
ogg_sync_pageout = _ogg_lib.ogg_sync_pageout
ogg_sync_pageout.argtypes = [POINTER(ogg_sync_state), POINTER(ogg_page)]
ogg_sync_pageout.restype = c_int

#extern int      ogg_stream_pagein(ogg_stream_state *os, ogg_page *og);
ogg_stream_pagein = _ogg_lib.ogg_stream_pagein
ogg_stream_pagein.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_page)]
ogg_stream_pagein.restype = c_int

#extern int      ogg_stream_packetout(ogg_stream_state *os,ogg_packet *op);
ogg_stream_packetout = _ogg_lib.ogg_stream_packetout
ogg_stream_packetout.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_packet)]
ogg_stream_packetout.restype = c_int

#extern int      ogg_stream_packetpeek(ogg_stream_state *os,ogg_packet *op);
ogg_stream_packetpeek = _ogg_lib.ogg_stream_packetpeek
ogg_stream_packetpeek.argtypes = [POINTER(ogg_stream_state), POINTER(ogg_packet)]
ogg_stream_packetpeek.restype = c_int


# Ogg BITSTREAM PRIMITIVES: general **************************

#extern int      ogg_stream_init(ogg_stream_state *os,int serialno);
ogg_stream_init = _ogg_lib.ogg_stream_init
ogg_stream_init.argtypes = [POINTER(ogg_stream_state), c_int]
ogg_stream_init.restype = c_int

#extern int      ogg_stream_clear(ogg_stream_state *os);
ogg_stream_clear = _ogg_lib.ogg_stream_clear
ogg_stream_clear.argtypes = [POINTER(ogg_stream_state)]
ogg_stream_clear.restype = c_int

#extern int      ogg_stream_reset(ogg_stream_state *os);
ogg_stream_reset = _ogg_lib.ogg_stream_reset
ogg_stream_reset.argtypes = [POINTER(ogg_stream_state)]
ogg_stream_reset.restype = c_int

#extern int      ogg_stream_reset_serialno(ogg_stream_state *os,int serialno);
ogg_stream_reset_serialno = _ogg_lib.ogg_stream_reset_serialno
ogg_stream_reset_serialno.argtypes = [POINTER(ogg_stream_state), c_int]
ogg_stream_reset_serialno.restype = c_int

#extern int      ogg_stream_destroy(ogg_stream_state *os);
ogg_stream_destroy = _ogg_lib.ogg_stream_destroy
ogg_stream_destroy.argtypes = [POINTER(ogg_stream_state)]
ogg_stream_destroy.restype = c_int

#extern int      ogg_stream_check(ogg_stream_state *os);
ogg_stream_check = _ogg_lib.ogg_stream_check
ogg_stream_check.argtypes = [POINTER(ogg_stream_state)]
ogg_stream_check.restype = c_int

#extern int      ogg_stream_eos(ogg_stream_state *os);
ogg_stream_eos = _ogg_lib.ogg_stream_eos
ogg_stream_eos.argtypes = [POINTER(ogg_stream_state)]
ogg_stream_eos.restype = c_int


#extern void     ogg_page_checksum_set(ogg_page *og);
ogg_page_checksum_set = _ogg_lib.ogg_page_checksum_set
ogg_page_checksum_set.argtypes = [POINTER(ogg_page)]
ogg_page_checksum_set.restype = None


#extern int      ogg_page_version(const ogg_page *og);
ogg_page_version = _ogg_lib.ogg_page_version
ogg_page_version.argtypes = [POINTER(ogg_page)]
ogg_page_version.restype = c_int

#extern int      ogg_page_continued(const ogg_page *og);
ogg_page_continued = _ogg_lib.ogg_page_continued
ogg_page_continued.argtypes = [POINTER(ogg_page)]
ogg_page_continued.restype = c_int

#extern int      ogg_page_bos(const ogg_page *og);
ogg_page_bos = _ogg_lib.ogg_page_bos
ogg_page_bos.argtypes = [POINTER(ogg_page)]
ogg_page_bos.restype = c_int

#extern int      ogg_page_eos(const ogg_page *og);
ogg_page_eos = _ogg_lib.ogg_page_eos
ogg_page_eos.argtypes = [POINTER(ogg_page)]
ogg_page_eos.restype = c_int

#extern ogg_int64_t  ogg_page_granulepos(const ogg_page *og);
ogg_page_granulepos = _ogg_lib.ogg_page_granulepos
ogg_page_granulepos.argtypes = [POINTER(ogg_page)]
ogg_page_granulepos.restype = ogg_int64_t

#extern int      ogg_page_serialno(const ogg_page *og);
ogg_page_serialno = _ogg_lib.ogg_page_serialno
ogg_page_serialno.argtypes = [POINTER(ogg_page)]
ogg_page_serialno.restype = c_int

#extern long     ogg_page_pageno(const ogg_page *og);
ogg_page_pageno = _ogg_lib.ogg_page_pageno
ogg_page_pageno.argtypes = [POINTER(ogg_page)]
ogg_page_pageno.restype = c_long

#extern int      ogg_page_packets(const ogg_page *og);
ogg_page_packets = _ogg_lib.ogg_page_packets
ogg_page_packets.argtypes = [POINTER(ogg_page)]
ogg_page_packets.restype = c_int


#extern void     ogg_packet_clear(ogg_packet *op);
ogg_packet_clear = _ogg_lib.ogg_packet_clear
ogg_packet_clear.argtypes = [POINTER(ogg_packet)]
ogg_packet_clear.restype = None
