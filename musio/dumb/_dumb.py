#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Dumb module.
# Copyright (C) 2012 Josiah Gordon <josiahg@gmail.com>
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


""" Dumb module.

"""

from ctypes import *
from ctypes.util import find_library


dumblib_name = find_library('dumb')
if not dumblib_name:
    raise Exception("libdumb could not be found")

_dumb_lib = cdll.LoadLibrary(dumblib_name)

def MIN(x,y):
    return min((x, y))
def MAX(x,y):
    return max((x, y))
def MID(x,y,z):
    return MAX(x, MIN(y, z))

def ABS(x):
    return abs(x)



def DUMB_ID(a,b,c,d):
    return ((ord(a) << 24) | (ord(b) << 16) | (ord(c) << 8) | (ord(d)))


#/* Basic Sample Type. Normal range is -0x800000 to 0x7FFFFF. */

#typedef int sample_t;
sample_t = c_int


#/* Library Clean-up Management */

#int dumb_atexit(void (*proc)(void));
dumb_atexit = _dumb_lib.dumb_atexit
dumb_atexit.argtypes = [CFUNCTYPE(None)]
dumb_atexit.restype = c_int

#void dumb_exit(void);
dumb_exit = _dumb_lib.dumb_exit
dumb_exit.argtypes = []
dumb_exit.restype = None


#/* File Input Functions */

class DUMBFILE_SYSTEM(Structure):
    _fields_ = [
            # void *(*open)(const char *filename); 
            ('open', CFUNCTYPE(c_void_p, c_char_p)),
            # int (*skip)(void *f, long n);
            ('skip', CFUNCTYPE(c_int, c_void_p, c_long)), 
            # int (*getc)(void *f);
            ('getc', CFUNCTYPE(c_int, c_void_p)),
            # long (*getnc)(char *ptr, long n, void *f);
            ('getnc', CFUNCTYPE(c_long, c_char_p, c_long, c_void_p)),
            # void (*close)(void *f);
            ('close', CFUNCTYPE(None, c_void_p))
            ]

class DUMBFILE(Structure):
    _fields_ = [
            ]

#void register_dumbfile_system(DUMBFILE_SYSTEM *dfs);
register_dumbfile_system = _dumb_lib.register_dumbfile_system
register_dumbfile_system.argtypes = [POINTER(DUMBFILE_SYSTEM)]
register_dumbfile_system.restype = None


#DUMBFILE *dumbfile_open(const char *filename);
dumbfile_open = _dumb_lib.dumbfile_open
dumbfile_open.argtypes = [c_char_p]
dumbfile_open.restype = POINTER(DUMBFILE)

#DUMBFILE *dumbfile_open_ex(void *file, DUMBFILE_SYSTEM *dfs);
dumbfile_open_ex = _dumb_lib.dumbfile_open_ex
dumbfile_open_ex.argtypes = [c_void_p, POINTER(DUMBFILE_SYSTEM)]
dumbfile_open_ex.restype = POINTER(DUMBFILE)


#long dumbfile_pos(DUMBFILE *f);
dumbfile_pos = _dumb_lib.dumbfile_pos
dumbfile_pos.argtypes = [POINTER(DUMBFILE)]
dumbfile_pos.restype = c_long

#int dumbfile_skip(DUMBFILE *f, long n);
dumbfile_skip = _dumb_lib.dumbfile_skip
dumbfile_skip.argtypes = [POINTER(DUMBFILE), c_long]
dumbfile_skip.restype = c_int


#int dumbfile_getc(DUMBFILE *f);
dumbfile_getc = _dumb_lib.dumbfile_getc
dumbfile_getc.argtypes = [POINTER(DUMBFILE)]
dumbfile_getc.restype = c_int


#int dumbfile_igetw(DUMBFILE *f);
dumbfile_igetw = _dumb_lib.dumbfile_igetw
dumbfile_igetw.argtypes = [POINTER(DUMBFILE)]
dumbfile_igetw.restype = c_int

#int dumbfile_mgetw(DUMBFILE *f);
dumbfile_mgetw = _dumb_lib.dumbfile_mgetw
dumbfile_mgetw.argtypes = [POINTER(DUMBFILE)]
dumbfile_mgetw.restype = c_int


#long dumbfile_igetl(DUMBFILE *f);
dumbfile_igetl = _dumb_lib.dumbfile_igetl
dumbfile_igetl.argtypes = [POINTER(DUMBFILE)]
dumbfile_igetl.restype = c_long

#long dumbfile_mgetl(DUMBFILE *f);
dumbfile_mgetl = _dumb_lib.dumbfile_mgetl
dumbfile_mgetl.argtypes = [POINTER(DUMBFILE)]
dumbfile_mgetl.restype = c_long


#unsigned long dumbfile_cgetul(DUMBFILE *f);
dumbfile_cgetul = _dumb_lib.dumbfile_cgetul
dumbfile_cgetul.argtypes = [POINTER(DUMBFILE)]
dumbfile_cgetul.restype = c_ulong

#signed long dumbfile_cgetsl(DUMBFILE *f);
dumbfile_cgetsl = _dumb_lib.dumbfile_cgetsl
dumbfile_cgetsl.argtypes = [POINTER(DUMBFILE)]
dumbfile_cgetsl.restype = c_long


#long dumbfile_getnc(char *ptr, long n, DUMBFILE *f);
dumbfile_getnc = _dumb_lib.dumbfile_getnc
dumbfile_getnc.argtypes = [c_char_p, c_long, POINTER(DUMBFILE)]
dumbfile_getnc.restype = c_long


#int dumbfile_error(DUMBFILE *f);
dumbfile_error = _dumb_lib.dumbfile_error
dumbfile_error.argtypes = [POINTER(DUMBFILE)]
dumbfile_error.restype = c_int

#int dumbfile_close(DUMBFILE *f);
dumbfile_close = _dumb_lib.dumbfile_close
dumbfile_close.argtypes = [POINTER(DUMBFILE)]
dumbfile_close.restype = c_int



#/* stdio File Input Module */

#void dumb_register_stdfiles(void);
dumb_register_stdfiles = _dumb_lib.dumb_register_stdfiles
dumb_register_stdfiles.argtypes = []
dumb_register_stdfiles.restype = None

class FILE(Structure):
    _fields_ = [
            ]

#DUMBFILE *dumbfile_open_stdfile(FILE *p);
dumbfile_open_stdfile = _dumb_lib.dumbfile_open_stdfile
dumbfile_open_stdfile.argtypes = [POINTER(FILE)]
dumbfile_open_stdfile.restype = POINTER(DUMBFILE)



#/* Memory File Input Module */

#DUMBFILE *dumbfile_open_memory(const char *data, long size);
dumbfile_open_memory = _dumb_lib.dumbfile_open_memory
dumbfile_open_memory.argtypes = [c_char_p, c_long]
dumbfile_open_memory.restype = POINTER(DUMBFILE)



#/* DUH Management */

#typedef struct DUH DUH;
class _DUH(Structure):
    _fields_ = [
            ]
DUH = _DUH


DUH_SIGNATURE = DUMB_ID('D','U','H','!')

#void unload_duh(DUH *duh);
unload_duh = _dumb_lib.unload_duh
unload_duh.argtypes = [POINTER(DUH)]
unload_duh.restype = None


#DUH *load_duh(const char *filename);
load_duh = _dumb_lib.load_duh
load_duh.argtypes = [c_char_p]
load_duh.restype = POINTER(DUH)

#DUH *read_duh(DUMBFILE *f);
read_duh = _dumb_lib.read_duh
read_duh.argtypes = [POINTER(DUMBFILE)]
read_duh.restype = POINTER(DUH)


#long duh_get_length(DUH *duh);
duh_get_length = _dumb_lib.duh_get_length
duh_get_length.argtypes = [POINTER(DUH)]
duh_get_length.restype = c_long


#const char *duh_get_tag(DUH *duh, const char *key);
duh_get_tag = _dumb_lib.duh_get_tag
duh_get_tag.argtypes = [POINTER(DUH), c_char_p]
duh_get_tag.restype = c_char_p



#/* Signal Rendering Functions */

#typedef struct DUH_SIGRENDERER DUH_SIGRENDERER;
class _DUH_SIGRENDERER(Structure):
    _fields_ = [
            ]
DUH_SIGRENDERER = _DUH_SIGRENDERER

#DUH_SIGRENDERER *duh_start_sigrenderer(DUH *duh, int sig, int n_channels, long pos);
duh_start_sigrenderer = _dumb_lib.duh_start_sigrenderer
duh_start_sigrenderer.argtypes = [POINTER(DUH), c_int, c_int, c_long]
duh_start_sigrenderer.restype = POINTER(DUH_SIGRENDERER)


#ifdef DUMB_DECLARE_DEPRECATED
#typedef void (*DUH_SIGRENDERER_CALLBACK)(void *data, sample_t **samples, int n_channels, long length);
DUH_SIGRENDERER_CALLBACK = CFUNCTYPE(None, c_void_p, POINTER(POINTER(sample_t)), c_int, c_long)

#/* This is deprecated, but is not marked as such because GCC tends to
 #* complain spuriously when the typedef is used later. See comments below.
 #*/

#void duh_sigrenderer_set_callback(
	#DUH_SIGRENDERER *sigrenderer,
	#DUH_SIGRENDERER_CALLBACK callback, void *data
#) DUMB_DEPRECATED;
duh_sigrenderer_set_callback = _dumb_lib.duh_sigrenderer_set_callback
duh_sigrenderer_set_callback.argtypes = [POINTER(DUH_SIGRENDERER), DUH_SIGRENDERER_CALLBACK, c_void_p]
duh_sigrenderer_set_callback.restype = None

#/* The 'callback' argument's type has changed for const-correctness. See the
 #* DUH_SIGRENDERER_CALLBACK definition just above. Also note that the samples
 #* in the buffer are now 256 times as large; the normal range is -0x800000 to
 #* 0x7FFFFF. The function has been renamed partly because its functionality
 #* has changed slightly and partly so that its name is more meaningful. The
 #* new one is duh_sigrenderer_set_analyser_callback(), and the typedef for
 #* the function pointer has also changed, from DUH_SIGRENDERER_CALLBACK to
 #* DUH_SIGRENDERER_ANALYSER_CALLBACK. (If you wanted to use this callback to
 #* apply a DSP effect, don't worry; there is a better way of doing this. It
 #* is undocumented, so contact me and I shall try to help. Contact details
 #* are in readme.txt.)
 #*/

#typedef void (*DUH_SIGRENDERER_ANALYSER_CALLBACK)(void *data, const sample_t *const *samples, int n_channels, long length);
DUH_SIGRENDERER_ANALYSER_CALLBACK = CFUNCTYPE(None, c_void_p, POINTER(POINTER(sample_t)), c_int, c_long)

#/* This is deprecated, but is not marked as such because GCC tends to
 #* complain spuriously when the typedef is used later. See comments below.
 #*/

#void duh_sigrenderer_set_analyser_callback(
	#DUH_SIGRENDERER *sigrenderer,
	#DUH_SIGRENDERER_ANALYSER_CALLBACK callback, void *data
#) DUMB_DEPRECATED;
duh_sigrenderer_set_analyser_callback = _dumb_lib.duh_sigrenderer_set_analyser_callback
duh_sigrenderer_set_analyser_callback.argtypes = [POINTER(DUH_SIGRENDERER), DUH_SIGRENDERER_ANALYSER_CALLBACK, c_void_p]
duh_sigrenderer_set_analyser_callback.restype = None

#/* This is deprecated because the meaning of the 'samples' parameter in the
 #* callback needed to change. For stereo applications, the array used to be
 #* indexed with samples[channel][pos]. It is now indexed with
 #* samples[0][pos*2+channel]. Mono sample data are still indexed with
 #* samples[0][pos]. The array is still 2D because samples will probably only
 #* ever be interleaved in twos. In order to fix your code, adapt it to the
 #* new sample layout and then call
 #* duh_sigrenderer_set_sample_analyser_callback below instead of this
 #* function.
 #*/
#endif

#typedef void (*DUH_SIGRENDERER_SAMPLE_ANALYSER_CALLBACK)(void *data, const sample_t *const *samples, int n_channels, long length);
DUH_SIGRENDERER_SAMPLE_ANALYSER_CALLBACK = CFUNCTYPE(None, c_void_p, POINTER(POINTER(sample_t)), c_int, c_long)

#void duh_sigrenderer_set_sample_analyser_callback(
	#DUH_SIGRENDERER *sigrenderer,
	#DUH_SIGRENDERER_SAMPLE_ANALYSER_CALLBACK callback, void *data
#);
duh_sigrenderer_set_sample_analyser_callback = _dumb_lib.duh_sigrenderer_set_sample_analyser_callback
duh_sigrenderer_set_sample_analyser_callback.argtypes = [POINTER(DUH_SIGRENDERER), DUH_SIGRENDERER_SAMPLE_ANALYSER_CALLBACK, c_void_p]
duh_sigrenderer_set_sample_analyser_callback.restype = None


#int duh_sigrenderer_get_n_channels(DUH_SIGRENDERER *sigrenderer);
duh_sigrenderer_get_n_channels = _dumb_lib.duh_sigrenderer_get_n_channels
duh_sigrenderer_get_n_channels.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_sigrenderer_get_n_channels.restype = c_int

#long duh_sigrenderer_get_position(DUH_SIGRENDERER *sigrenderer);
duh_sigrenderer_get_position = _dumb_lib.duh_sigrenderer_get_position
duh_sigrenderer_get_position.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_sigrenderer_get_position.restype = c_long


#void duh_sigrenderer_set_sigparam(DUH_SIGRENDERER *sigrenderer, unsigned char id, long value);
duh_sigrenderer_set_sigparam = _dumb_lib.duh_sigrenderer_set_sigparam
duh_sigrenderer_set_sigparam.argtypes = [POINTER(DUH_SIGRENDERER), c_ubyte, c_long]
duh_sigrenderer_set_sigparam.restype = None


#ifdef DUMB_DECLARE_DEPRECATED
#long duh_sigrenderer_get_samples(
	#DUH_SIGRENDERER *sigrenderer,
	#float volume, float delta,
	#long size, sample_t **samples
#) DUMB_DEPRECATED;
duh_sigrenderer_get_samples = _dumb_lib.duh_sigrenderer_get_samples
duh_sigrenderer_get_samples.argtypes = [POINTER(DUH_SIGRENDERER), c_float, c_float, c_long, POINTER(POINTER(sample_t))]
duh_sigrenderer_get_samples.restype = c_long

#/* The sample format has changed, so if you were using this function,
 #* you should switch to duh_sigrenderer_generate_samples() and change
 #* how you interpret the samples array. See the comments for
 #* duh_sigrenderer_set_analyser_callback().
 #*/
#endif

#long duh_sigrenderer_generate_samples(
	#DUH_SIGRENDERER *sigrenderer,
	#float volume, float delta,
	#long size, sample_t **samples
#);
duh_sigrenderer_generate_samples = _dumb_lib.duh_sigrenderer_generate_samples
duh_sigrenderer_generate_samples.argtypes = [POINTER(DUH_SIGRENDERER), c_float, c_float, c_long, POINTER(POINTER(sample_t))]
duh_sigrenderer_generate_samples.restype = c_long


#void duh_sigrenderer_get_current_sample(DUH_SIGRENDERER *sigrenderer, float volume, sample_t *samples);
duh_sigrenderer_get_current_sample = _dumb_lib.duh_sigrenderer_get_current_sample
duh_sigrenderer_get_current_sample.argtypes = [POINTER(DUH_SIGRENDERER), c_float, POINTER(sample_t)]
duh_sigrenderer_get_current_sample.restype = None


#void duh_end_sigrenderer(DUH_SIGRENDERER *sigrenderer);
duh_end_sigrenderer = _dumb_lib.duh_end_sigrenderer
duh_end_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_end_sigrenderer.restype = None



#/* DUH Rendering Functions */

#long duh_render(
	#DUH_SIGRENDERER *sigrenderer,
	#int bits, int unsign,
	#float volume, float delta,
	#long size, void *sptr
#);
duh_render = _dumb_lib.duh_render
duh_render.argtypes = [POINTER(DUH_SIGRENDERER), c_int, c_int, c_float, c_float, c_long, c_void_p]
duh_render.restype = c_long


#ifdef DUMB_DECLARE_DEPRECATED

#long duh_render_signal(
	#DUH_SIGRENDERER *sigrenderer,
	#float volume, float delta,
	#long size, sample_t **samples
#) DUMB_DEPRECATED;
duh_render_signal = _dumb_lib.duh_render_signal
duh_render_signal.argtypes = [POINTER(DUH_SIGRENDERER), c_float, c_float, c_long, POINTER(POINTER(sample_t))]
duh_render_signal.restype = c_long

#/* Please use duh_sigrenderer_generate_samples(), and see the
 #* comments for the deprecated duh_sigrenderer_get_samples() too.
 #*/

#typedef DUH_SIGRENDERER DUH_RENDERER DUMB_DEPRECATED;
DUH_RENDERER = DUH_SIGRENDERER

#/* Please use DUH_SIGRENDERER instead of DUH_RENDERER. */

#DUH_SIGRENDERER *duh_start_renderer(DUH *duh, int n_channels, long pos) DUMB_DEPRECATED;
duh_start_renderer = _dumb_lib.duh_start_renderer
duh_start_renderer.argtypes = [POINTER(DUH), c_int, c_long]
duh_start_renderer.restype = POINTER(DUH_SIGRENDERER)

#/* Please use duh_start_sigrenderer() instead. Pass 0 for 'sig'. */

#int duh_renderer_get_n_channels(DUH_SIGRENDERER *dr) DUMB_DEPRECATED;
duh_renderer_get_n_channels = _dumb_lib.duh_renderer_get_n_channels
duh_renderer_get_n_channels.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_renderer_get_n_channels.restype = c_int

#long duh_renderer_get_position(DUH_SIGRENDERER *dr) DUMB_DEPRECATED;
duh_renderer_get_position = _dumb_lib.duh_renderer_get_position
duh_renderer_get_position.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_renderer_get_position.restype = c_long

#/* Please use the duh_sigrenderer_*() equivalents of these two functions. */

#void duh_end_renderer(DUH_SIGRENDERER *dr) DUMB_DEPRECATED;
duh_end_renderer = _dumb_lib.duh_end_renderer
duh_end_renderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_end_renderer.restype = None

#/* Please use duh_end_sigrenderer() instead. */

#DUH_SIGRENDERER *duh_renderer_encapsulate_sigrenderer(DUH_SIGRENDERER *sigrenderer) DUMB_DEPRECATED;
duh_renderer_encapsulate_sigrenderer = _dumb_lib.duh_renderer_encapsulate_sigrenderer
duh_renderer_encapsulate_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_renderer_encapsulate_sigrenderer.restype = POINTER(DUH_SIGRENDERER)

#DUH_SIGRENDERER *duh_renderer_get_sigrenderer(DUH_SIGRENDERER *dr) DUMB_DEPRECATED;
duh_renderer_get_sigrenderer = _dumb_lib.duh_renderer_get_sigrenderer
duh_renderer_get_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_renderer_get_sigrenderer.restype = POINTER(DUH_SIGRENDERER)

#DUH_SIGRENDERER *duh_renderer_decompose_to_sigrenderer(DUH_SIGRENDERER *dr) DUMB_DEPRECATED;
duh_renderer_decompose_to_sigrenderer = _dumb_lib.duh_renderer_decompose_to_sigrenderer
duh_renderer_decompose_to_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_renderer_decompose_to_sigrenderer.restype = POINTER(DUH_SIGRENDERER)

#/* These functions have become no-ops that just return the parameter.
 #* So, for instance, replace
 #*   duh_renderer_encapsulate_sigrenderer(my_sigrenderer)
 #* with
 #*   my_sigrenderer
 #*/

#endif


#/* Impulse Tracker Support */

#extern int dumb_it_max_to_mix;
dumb_it_max_to_mix = c_int.in_dll(_dumb_lib, 'dumb_it_max_to_mix')

#typedef struct DUMB_IT_SIGDATA DUMB_IT_SIGDATA;
class DUMB_IT_SIGDATA(Structure):
    _fields_ = [
            ]
#typedef struct DUMB_IT_SIGRENDERER DUMB_IT_SIGRENDERER;
class DUMB_IT_SIGRENDERER(Structure):
    _fields_ = [
            ]

#DUMB_IT_SIGDATA *duh_get_it_sigdata(DUH *duh);
duh_get_it_sigdata = _dumb_lib.duh_get_it_sigdata
duh_get_it_sigdata.argtypes = [POINTER(DUH)]
duh_get_it_sigdata.restype = POINTER(DUMB_IT_SIGDATA)

#DUH_SIGRENDERER *duh_encapsulate_it_sigrenderer(DUMB_IT_SIGRENDERER *it_sigrenderer, int n_channels, long pos);
duh_encapsulate_it_sigrenderer = _dumb_lib.duh_encapsulate_it_sigrenderer
duh_encapsulate_it_sigrenderer.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int, c_long]
duh_encapsulate_it_sigrenderer.restype = POINTER(DUH_SIGRENDERER)

#DUMB_IT_SIGRENDERER *duh_get_it_sigrenderer(DUH_SIGRENDERER *sigrenderer);
duh_get_it_sigrenderer = _dumb_lib.duh_get_it_sigrenderer
duh_get_it_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER)]
duh_get_it_sigrenderer.restype = POINTER(DUMB_IT_SIGRENDERER)


#DUH_SIGRENDERER *dumb_it_start_at_order(DUH *duh, int n_channels, int startorder);
dumb_it_start_at_order = _dumb_lib.dumb_it_start_at_order
dumb_it_start_at_order.argtypes = [POINTER(DUH), c_int, c_int]
dumb_it_start_at_order.restype = POINTER(DUH_SIGRENDERER)


#void dumb_it_set_loop_callback(DUMB_IT_SIGRENDERER *sigrenderer, int (*callback)(void *data), void *data);
dumb_it_set_loop_callback = _dumb_lib.dumb_it_set_loop_callback
dumb_it_set_loop_callback.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_void_p, c_void_p]
dumb_it_set_loop_callback.restype = None

#void dumb_it_set_xm_speed_zero_callback(DUMB_IT_SIGRENDERER *sigrenderer, int (*callback)(void *data), void *data);
dumb_it_set_xm_speed_zero_callback = _dumb_lib.dumb_it_set_xm_speed_zero_callback
dumb_it_set_xm_speed_zero_callback.argtypes = [POINTER(DUMB_IT_SIGRENDERER), CFUNCTYPE(c_int, c_void_p), c_void_p]
dumb_it_set_xm_speed_zero_callback.restype = None

#void dumb_it_set_midi_callback(DUMB_IT_SIGRENDERER *sigrenderer, int (*callback)(void *data, int channel, unsigned char midi_byte), void *data);
dumb_it_set_midi_callback = _dumb_lib.dumb_it_set_midi_callback
dumb_it_set_midi_callback.argtypes = [POINTER(DUMB_IT_SIGRENDERER), CFUNCTYPE(c_int, c_void_p, c_int, c_uint), c_void_p]
dumb_it_set_midi_callback.restype = None


#int dumb_it_callback_terminate(void *data);
dumb_it_callback_terminate = _dumb_lib.dumb_it_callback_terminate
dumb_it_callback_terminate.argtypes = [c_void_p]
dumb_it_callback_terminate.restype = c_int

#int dumb_it_callback_midi_block(void *data, int channel, unsigned char midi_byte);
dumb_it_callback_midi_block = _dumb_lib.dumb_it_callback_midi_block
dumb_it_callback_midi_block.argtypes = [c_void_p, c_int, c_ubyte]
dumb_it_callback_midi_block.restype = c_int


#DUH *dumb_load_it(const char *filename);
dumb_load_it = _dumb_lib.dumb_load_it
dumb_load_it.argtypes = [c_char_p]
dumb_load_it.restype = POINTER(DUH)

#DUH *dumb_load_xm(const char *filename);
dumb_load_xm = _dumb_lib.dumb_load_xm
dumb_load_xm.argtypes = [c_char_p]
dumb_load_xm.restype = POINTER(DUH)

#DUH *dumb_load_s3m(const char *filename);
dumb_load_s3m = _dumb_lib.dumb_load_s3m
dumb_load_s3m.argtypes = [c_char_p]
dumb_load_s3m.restype = POINTER(DUH)

#DUH *dumb_load_mod(const char *filename);
dumb_load_mod = _dumb_lib.dumb_load_mod
dumb_load_mod.argtypes = [c_char_p]
dumb_load_mod.restype = POINTER(DUH)


#DUH *dumb_read_it(DUMBFILE *f);
dumb_read_it = _dumb_lib.dumb_read_it
dumb_read_it.argtypes = [POINTER(DUMBFILE)]
dumb_read_it.restype = POINTER(DUH)

#DUH *dumb_read_xm(DUMBFILE *f);
dumb_read_xm = _dumb_lib.dumb_read_xm
dumb_read_xm.argtypes = [POINTER(DUMBFILE)]
dumb_read_xm.restype = POINTER(DUH)

#DUH *dumb_read_s3m(DUMBFILE *f);
dumb_read_s3m = _dumb_lib.dumb_read_s3m
dumb_read_s3m.argtypes = [POINTER(DUMBFILE)]
dumb_read_s3m.restype = POINTER(DUH)

#DUH *dumb_read_mod(DUMBFILE *f);
dumb_read_mod = _dumb_lib.dumb_read_mod
dumb_read_mod.argtypes = [POINTER(DUMBFILE)]
dumb_read_mod.restype = POINTER(DUH)


#DUH *dumb_load_it_quick(const char *filename);
dumb_load_it_quick = _dumb_lib.dumb_load_it_quick
dumb_load_it_quick.argtypes = [c_char_p]
dumb_load_it_quick.restype = POINTER(DUH)

#DUH *dumb_load_xm_quick(const char *filename);
dumb_load_xm_quick = _dumb_lib.dumb_load_xm_quick
dumb_load_xm_quick.argtypes = [c_char_p]
dumb_load_xm_quick.restype = POINTER(DUH)

#DUH *dumb_load_s3m_quick(const char *filename);
dumb_load_s3m_quick = _dumb_lib.dumb_load_s3m_quick
dumb_load_s3m_quick.argtypes = [c_char_p]
dumb_load_s3m_quick.restype = POINTER(DUH)

#DUH *dumb_load_mod_quick(const char *filename);
dumb_load_mod_quick = _dumb_lib.dumb_load_mod_quick
dumb_load_mod_quick.argtypes = [c_char_p]
dumb_load_mod_quick.restype = POINTER(DUH)


#DUH *dumb_read_it_quick(DUMBFILE *f);
dumb_read_it_quick = _dumb_lib.dumb_read_it_quick
dumb_read_it_quick.argtypes = [POINTER(DUMBFILE)]
dumb_read_it_quick.restype = POINTER(DUH)

#DUH *dumb_read_xm_quick(DUMBFILE *f);
dumb_read_xm_quick = _dumb_lib.dumb_read_xm_quick
dumb_read_xm_quick.argtypes = [POINTER(DUMBFILE)]
dumb_read_xm_quick.restype = POINTER(DUH)

#DUH *dumb_read_s3m_quick(DUMBFILE *f);
dumb_read_s3m_quick = _dumb_lib.dumb_read_s3m_quick
dumb_read_s3m_quick.argtypes = [POINTER(DUMBFILE)]
dumb_read_s3m_quick.restype = POINTER(DUH)

#DUH *dumb_read_mod_quick(DUMBFILE *f);
dumb_read_mod_quick = _dumb_lib.dumb_read_mod_quick
dumb_read_mod_quick.argtypes = [POINTER(DUMBFILE)]
dumb_read_mod_quick.restype = POINTER(DUH)


#long dumb_it_build_checkpoints(DUMB_IT_SIGDATA *sigdata);
dumb_it_build_checkpoints = _dumb_lib.dumb_it_build_checkpoints
dumb_it_build_checkpoints.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_build_checkpoints.restype = c_long

#void dumb_it_do_initial_runthrough(DUH *duh);
dumb_it_do_initial_runthrough = _dumb_lib.dumb_it_do_initial_runthrough
dumb_it_do_initial_runthrough.argtypes = [POINTER(DUH)]
dumb_it_do_initial_runthrough.restype = None


#const unsigned char *dumb_it_sd_get_song_message(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_song_message = _dumb_lib.dumb_it_sd_get_song_message
dumb_it_sd_get_song_message.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_song_message.restype = c_char_p


#int dumb_it_sd_get_n_orders(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_n_orders = _dumb_lib.dumb_it_sd_get_n_orders
dumb_it_sd_get_n_orders.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_n_orders.restype = c_int

#int dumb_it_sd_get_n_samples(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_n_samples = _dumb_lib.dumb_it_sd_get_n_samples
dumb_it_sd_get_n_samples.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_n_samples.restype = c_int

#int dumb_it_sd_get_n_instruments(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_n_instruments = _dumb_lib.dumb_it_sd_get_n_instruments
dumb_it_sd_get_n_instruments.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_n_instruments.restype = c_int


#const unsigned char *dumb_it_sd_get_sample_name(DUMB_IT_SIGDATA *sd, int i);
dumb_it_sd_get_sample_name = _dumb_lib.dumb_it_sd_get_sample_name
dumb_it_sd_get_sample_name.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_get_sample_name.restype = c_char_p

#const unsigned char *dumb_it_sd_get_sample_filename(DUMB_IT_SIGDATA *sd, int i);
dumb_it_sd_get_sample_filename = _dumb_lib.dumb_it_sd_get_sample_filename
dumb_it_sd_get_sample_filename.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_get_sample_filename.restype = c_char_p

#const unsigned char *dumb_it_sd_get_instrument_name(DUMB_IT_SIGDATA *sd, int i);
dumb_it_sd_get_instrument_name = _dumb_lib.dumb_it_sd_get_instrument_name
dumb_it_sd_get_instrument_name.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_get_instrument_name.restype = c_char_p

#const unsigned char *dumb_it_sd_get_instrument_filename(DUMB_IT_SIGDATA *sd, int i);
dumb_it_sd_get_instrument_filename = _dumb_lib.dumb_it_sd_get_instrument_filename
dumb_it_sd_get_instrument_filename.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_get_instrument_filename.restype = c_char_p


#int dumb_it_sd_get_initial_global_volume(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_initial_global_volume = _dumb_lib.dumb_it_sd_get_initial_global_volume
dumb_it_sd_get_initial_global_volume.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_initial_global_volume.restype = c_int

#void dumb_it_sd_set_initial_global_volume(DUMB_IT_SIGDATA *sd, int gv);
dumb_it_sd_set_initial_global_volume = _dumb_lib.dumb_it_sd_set_initial_global_volume
dumb_it_sd_set_initial_global_volume.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_set_initial_global_volume.restype = None


#int dumb_it_sd_get_mixing_volume(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_mixing_volume = _dumb_lib.dumb_it_sd_get_mixing_volume
dumb_it_sd_get_mixing_volume.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_mixing_volume.restype = c_int

#void dumb_it_sd_set_mixing_volume(DUMB_IT_SIGDATA *sd, int mv);
dumb_it_sd_set_mixing_volume = _dumb_lib.dumb_it_sd_set_mixing_volume
dumb_it_sd_set_mixing_volume.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_set_mixing_volume.restype = None


#int dumb_it_sd_get_initial_speed(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_initial_speed = _dumb_lib.dumb_it_sd_get_initial_speed
dumb_it_sd_get_initial_speed.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_initial_speed.restype = c_int

#void dumb_it_sd_set_initial_speed(DUMB_IT_SIGDATA *sd, int speed);
dumb_it_sd_set_initial_speed = _dumb_lib.dumb_it_sd_set_initial_speed
dumb_it_sd_set_initial_speed.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_set_initial_speed.restype = None


#int dumb_it_sd_get_initial_tempo(DUMB_IT_SIGDATA *sd);
dumb_it_sd_get_initial_tempo = _dumb_lib.dumb_it_sd_get_initial_tempo
dumb_it_sd_get_initial_tempo.argtypes = [POINTER(DUMB_IT_SIGDATA)]
dumb_it_sd_get_initial_tempo.restype = c_int

#void dumb_it_sd_set_initial_tempo(DUMB_IT_SIGDATA *sd, int tempo);
dumb_it_sd_set_initial_tempo = _dumb_lib.dumb_it_sd_set_initial_tempo
dumb_it_sd_set_initial_tempo.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_set_initial_tempo.restype = None


#int dumb_it_sd_get_initial_channel_volume(DUMB_IT_SIGDATA *sd, int channel);
dumb_it_sd_get_initial_channel_volume = _dumb_lib.dumb_it_sd_get_initial_channel_volume
dumb_it_sd_get_initial_channel_volume.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int]
dumb_it_sd_get_initial_channel_volume.restype = c_int

#void dumb_it_sd_set_initial_channel_volume(DUMB_IT_SIGDATA *sd, int channel, int volume);
dumb_it_sd_set_initial_channel_volume = _dumb_lib.dumb_it_sd_set_initial_channel_volume
dumb_it_sd_set_initial_channel_volume.argtypes = [POINTER(DUMB_IT_SIGDATA), c_int, c_int]
dumb_it_sd_set_initial_channel_volume.restype = None


#int dumb_it_sr_get_current_order(DUMB_IT_SIGRENDERER *sr);
dumb_it_sr_get_current_order = _dumb_lib.dumb_it_sr_get_current_order
dumb_it_sr_get_current_order.argtypes = [POINTER(DUMB_IT_SIGRENDERER)]
dumb_it_sr_get_current_order.restype = c_int

#int dumb_it_sr_get_current_row(DUMB_IT_SIGRENDERER *sr);
dumb_it_sr_get_current_row = _dumb_lib.dumb_it_sr_get_current_row
dumb_it_sr_get_current_row.argtypes = [POINTER(DUMB_IT_SIGRENDERER)]
dumb_it_sr_get_current_row.restype = c_int


#int dumb_it_sr_get_global_volume(DUMB_IT_SIGRENDERER *sr);
dumb_it_sr_get_global_volume = _dumb_lib.dumb_it_sr_get_global_volume
dumb_it_sr_get_global_volume.argtypes = [POINTER(DUMB_IT_SIGRENDERER)]
dumb_it_sr_get_global_volume.restype = c_int

#void dumb_it_sr_set_global_volume(DUMB_IT_SIGRENDERER *sr, int gv);
dumb_it_sr_set_global_volume = _dumb_lib.dumb_it_sr_set_global_volume
dumb_it_sr_set_global_volume.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int]
dumb_it_sr_set_global_volume.restype = None


#int dumb_it_sr_get_tempo(DUMB_IT_SIGRENDERER *sr);
dumb_it_sr_get_tempo = _dumb_lib.dumb_it_sr_get_tempo
dumb_it_sr_get_tempo.argtypes = [POINTER(DUMB_IT_SIGRENDERER)]
dumb_it_sr_get_tempo.restype = c_int

#void dumb_it_sr_set_tempo(DUMB_IT_SIGRENDERER *sr, int tempo);
dumb_it_sr_set_tempo = _dumb_lib.dumb_it_sr_set_tempo
dumb_it_sr_set_tempo.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int]
dumb_it_sr_set_tempo.restype = None


#int dumb_it_sr_get_speed(DUMB_IT_SIGRENDERER *sr);
dumb_it_sr_get_speed = _dumb_lib.dumb_it_sr_get_speed
dumb_it_sr_get_speed.argtypes = [POINTER(DUMB_IT_SIGRENDERER)]
dumb_it_sr_get_speed.restype = c_int

#void dumb_it_sr_set_speed(DUMB_IT_SIGRENDERER *sr, int speed);
dumb_it_sr_set_speed = _dumb_lib.dumb_it_sr_set_speed
dumb_it_sr_set_speed.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int]
dumb_it_sr_set_speed.restype = None


DUMB_IT_N_CHANNELS = 64
DUMB_IT_N_NNA_CHANNELS = 192
DUMB_IT_TOTAL_CHANNELS = (DUMB_IT_N_CHANNELS + DUMB_IT_N_NNA_CHANNELS)

#/* Channels passed to any of these functions are 0-based */
#int dumb_it_sr_get_channel_volume(DUMB_IT_SIGRENDERER *sr, int channel);
dumb_it_sr_get_channel_volume = _dumb_lib.dumb_it_sr_get_channel_volume
dumb_it_sr_get_channel_volume.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int]
dumb_it_sr_get_channel_volume.restype = c_int

#void dumb_it_sr_set_channel_volume(DUMB_IT_SIGRENDERER *sr, int channel, int volume);
dumb_it_sr_set_channel_volume = _dumb_lib.dumb_it_sr_set_channel_volume
dumb_it_sr_set_channel_volume.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int, c_int]
dumb_it_sr_set_channel_volume.restype = None


#int dumb_it_sr_get_channel_muted(DUMB_IT_SIGRENDERER *sr, int channel);
dumb_it_sr_get_channel_muted = _dumb_lib.dumb_it_sr_get_channel_muted
dumb_it_sr_get_channel_muted.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int]
dumb_it_sr_get_channel_muted.restype = c_int

#void dumb_it_sr_set_channel_muted(DUMB_IT_SIGRENDERER *sr, int channel, int muted);
dumb_it_sr_set_channel_muted = _dumb_lib.dumb_it_sr_set_channel_muted
dumb_it_sr_set_channel_muted.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int, c_int]
dumb_it_sr_set_channel_muted.restype = None


#typedef struct DUMB_IT_CHANNEL_STATE DUMB_IT_CHANNEL_STATE;
class DUMB_IT_CHANNEL_STATE(Structure):
    _fields_ = [
            ]

class DUMB_IT_CHANNEL_STATE(Structure):
    _fields_ = [
            ('channel', c_int), # /* 0-based; meaningful for NNA channels */
            ('sample', c_int), # /* 1-based; 0 if nothing playing, then other fields undef */
            ('freq', c_int), # /* in Hz */
            ('volume', c_float), # /* 1.0 maximum; affected by ALL factors, inc. mixing vol */
            ('pan', c_ubyte), # /* 0-64, 100 for surround */
            ('subpan', c_char), # /* use (pan + subpan/256.0f) or ((pan<<8)+subpan) */
            ('filter_cutoff', c_ubyte), # /* 0-127    cutoff=127 AND resonance=0 */
            ('filter_subcutoff', c_ubyte), # /* 0-255      -> no filters (subcutoff */
            ('filter_resonance', c_ubyte), # /* 0-127        always 0 in this case) */
            #/* subcutoff only changes from zero if filter envelopes are in use. The
             #* calculation (filter_cutoff + filter_subcutoff/256.0f) gives a more
             #* accurate filter cutoff measurement as a float. It would often be more
             #* useful to use a scaled int such as ((cutoff<<8) + subcutoff).
             #*/
             ]

#/* Values of 64 or more will access NNA channels here. */
#void dumb_it_sr_get_channel_state(DUMB_IT_SIGRENDERER *sr, int channel, DUMB_IT_CHANNEL_STATE *state);
dumb_it_sr_get_channel_state = _dumb_lib.dumb_it_sr_get_channel_state
dumb_it_sr_get_channel_state.argtypes = [POINTER(DUMB_IT_SIGRENDERER), c_int, POINTER(DUMB_IT_CHANNEL_STATE)]
dumb_it_sr_get_channel_state.restype = None



#/* Signal Design Helper Values */

#/* Use pow(DUMB_SEMITONE_BASE, n) to get the 'delta' value to transpose up by
 #* n semitones. To transpose down, use negative n.
 #*/
DUMB_SEMITONE_BASE = 1.059463094359295309843105314939748495817

#/* Use pow(DUMB_QUARTERTONE_BASE, n) to get the 'delta' value to transpose up
 #* by n quartertones. To transpose down, use negative n.
 #*/
DUMB_QUARTERTONE_BASE = 1.029302236643492074463779317738953977823

#/* Use pow(DUMB_PITCH_BASE, n) to get the 'delta' value to transpose up by n
 #* units. In this case, 256 units represent one semitone; 3072 units
 #* represent one octave. These units are used by the sequence signal (SEQU).
 #*/
DUMB_PITCH_BASE = 1.000225659305069791926712241547647863626


#/* Signal Design Function Types */

#typedef void sigdata_t;
sigdata_t = None

#typedef void sigrenderer_t;
sigrenderer_t = None

#typedef sigdata_t *(*DUH_LOAD_SIGDATA)(DUH *duh, DUMBFILE *file);
DUH_LOAD_SIGDATA = CFUNCTYPE(POINTER(sigdata_t), POINTER(DUH), POINTER(DUMBFILE))


#typedef sigrenderer_t *(*DUH_START_SIGRENDERER)(
	#DUH *duh,
	#sigdata_t *sigdata,
	#int n_channels,
	#long pos
#);
DUH_START_SIGRENDERER = CFUNCTYPE(POINTER(sigrenderer_t), POINTER(DUH), POINTER(sigdata_t), c_int, c_long)


#typedef void (*DUH_SIGRENDERER_SET_SIGPARAM)(
	#sigrenderer_t *sigrenderer,
	#unsigned char id, long value
#);
DUH_SIGRENDERER_SET_SIGPARAM = CFUNCTYPE(None, POINTER(sigrenderer_t), c_ubyte, c_long)


#typedef long (*DUH_SIGRENDERER_GENERATE_SAMPLES)(
	#sigrenderer_t *sigrenderer,
	#float volume, float delta,
	#long size, sample_t **samples
#);
DUH_SIGRENDERER_GENERATE_SAMPLES = CFUNCTYPE(c_long, POINTER(sigrenderer_t), c_float, c_float, c_long, POINTER(POINTER(sample_t)))


#typedef void (*DUH_SIGRENDERER_GET_CURRENT_SAMPLE)(
	#sigrenderer_t *sigrenderer,
	#float volume,
	#sample_t *samples
#);
DUH_SIGRENDERER_GET_CURRENT_SAMPLE = CFUNCTYPE(None, POINTER(sigrenderer_t), c_float, POINTER(sample_t))


#typedef void (*DUH_END_SIGRENDERER)(sigrenderer_t *sigrenderer);
DUH_END_SIGRENDERER = CFUNCTYPE(None, POINTER(sigrenderer_t))


#typedef void (*DUH_UNLOAD_SIGDATA)(sigdata_t *sigdata);
DUH_UNLOAD_SIGDATA = CFUNCTYPE(None, POINTER(sigdata_t))



#/* Signal Design Function Registration */

class DUH_SIGTYPE_DESC(Structure):
    _fields_ = [
            ('type', c_long),
            ('load_sigdata', DUH_LOAD_SIGDATA),
            ('start_sigrenderer', DUH_START_SIGRENDERER), 
            ('sigrenderer_set_sigparam', DUH_SIGRENDERER_SET_SIGPARAM),
            ('sigrenderer_generate_samples', DUH_SIGRENDERER_GENERATE_SAMPLES),
            ('sigrenderer_get_current_sample', DUH_SIGRENDERER_GET_CURRENT_SAMPLE),
            ('end_sigrenderer', DUH_END_SIGRENDERER),
            ('unload_sigdata', DUH_UNLOAD_SIGDATA)
            ]

#void dumb_register_sigtype(DUH_SIGTYPE_DESC *desc);
dumb_register_sigtype = _dumb_lib.dumb_register_sigtype
dumb_register_sigtype.argtypes = [POINTER(DUH_SIGTYPE_DESC)]
dumb_register_sigtype.restype = None



#// Decide where to put these functions; new heading?

#sigdata_t *duh_get_raw_sigdata(DUH *duh, int sig, long type);
duh_get_raw_sigdata = _dumb_lib.duh_get_raw_sigdata
duh_get_raw_sigdata.argtypes = [POINTER(DUH), c_int, c_long]
duh_get_raw_sigdata.restype = POINTER(sigdata_t)


#DUH_SIGRENDERER *duh_encapsulate_raw_sigrenderer(sigrenderer_t *vsigrenderer, DUH_SIGTYPE_DESC *desc, int n_channels, long pos);
duh_encapsulate_raw_sigrenderer = _dumb_lib.duh_encapsulate_raw_sigrenderer
duh_encapsulate_raw_sigrenderer.argtypes = [POINTER(sigrenderer_t), POINTER(DUH_SIGTYPE_DESC), c_int, c_long]
duh_encapsulate_raw_sigrenderer.restype = POINTER(DUH_SIGRENDERER)

#sigrenderer_t *duh_get_raw_sigrenderer(DUH_SIGRENDERER *sigrenderer, long type);
duh_get_raw_sigrenderer = _dumb_lib.duh_get_raw_sigrenderer
duh_get_raw_sigrenderer.argtypes = [POINTER(DUH_SIGRENDERER), c_long]
duh_get_raw_sigrenderer.restype = POINTER(sigrenderer_t)



#/* Standard Signal Types */

#//void dumb_register_sigtype_sample(void);


#/* Sample Buffer Allocation Helpers */

#ifdef DUMB_DECLARE_DEPRECATED
#sample_t **create_sample_buffer(int n_channels, long length) DUMB_DEPRECATED;
create_sample_buffer = _dumb_lib.create_sample_buffer
create_sample_buffer.argtypes = [c_int, c_long]
create_sample_buffer.restype = POINTER(POINTER(sample_t))

#/* DUMB has been changed to interleave stereo samples. Use
 #* allocate_sample_buffer() instead, and see the comments for
 #* duh_sigrenderer_set_analyser_callback().
 #*/
#endif
#sample_t **allocate_sample_buffer(int n_channels, long length);
allocate_sample_buffer = _dumb_lib.allocate_sample_buffer
allocate_sample_buffer.argtypes = [c_int, c_long]
allocate_sample_buffer.restype = POINTER(POINTER(sample_t))

#void destroy_sample_buffer(sample_t **samples);
destroy_sample_buffer = _dumb_lib.destroy_sample_buffer
destroy_sample_buffer.argtypes = [POINTER(POINTER(sample_t))]
destroy_sample_buffer.restype = None



#/* Silencing Helper */

#void dumb_silence(sample_t *samples, long length);
dumb_silence = _dumb_lib.dumb_silence
dumb_silence.argtypes = [POINTER(sample_t), c_long]
dumb_silence.restype = None



#/* Click Removal Helpers */

#typedef struct DUMB_CLICK_REMOVER DUMB_CLICK_REMOVER;
class DUMB_CLICK_REMOVER(Structure):
    _fields_ = [
            ]

#DUMB_CLICK_REMOVER *dumb_create_click_remover(void);
dumb_create_click_remover = _dumb_lib.dumb_create_click_remover
dumb_create_click_remover.argtypes = []
dumb_create_click_remover.restype = POINTER(DUMB_CLICK_REMOVER)

#void dumb_record_click(DUMB_CLICK_REMOVER *cr, long pos, sample_t step);
dumb_record_click = _dumb_lib.dumb_record_click
dumb_record_click.argtypes = [POINTER(DUMB_CLICK_REMOVER), c_long, sample_t]
dumb_record_click.restype = None

#void dumb_remove_clicks(DUMB_CLICK_REMOVER *cr, sample_t *samples, long length, int step, float halflife);
dumb_remove_clicks = _dumb_lib.dumb_remove_clicks
dumb_remove_clicks.argtypes = [POINTER(DUMB_CLICK_REMOVER), POINTER(sample_t), c_long, c_int, c_float]
dumb_remove_clicks.restype = None

#sample_t dumb_click_remover_get_offset(DUMB_CLICK_REMOVER *cr);
dumb_click_remover_get_offset = _dumb_lib.dumb_click_remover_get_offset
dumb_click_remover_get_offset.argtypes = [POINTER(DUMB_CLICK_REMOVER)]
dumb_click_remover_get_offset.restype = sample_t

#void dumb_destroy_click_remover(DUMB_CLICK_REMOVER *cr);
dumb_destroy_click_remover = _dumb_lib.dumb_destroy_click_remover
dumb_destroy_click_remover.argtypes = [POINTER(DUMB_CLICK_REMOVER)]
dumb_destroy_click_remover.restype = None


#DUMB_CLICK_REMOVER **dumb_create_click_remover_array(int n);
dumb_create_click_remover_array = _dumb_lib.dumb_create_click_remover_array
dumb_create_click_remover_array.argtypes = [c_int]
dumb_create_click_remover_array.restype = POINTER(POINTER(DUMB_CLICK_REMOVER))

#void dumb_record_click_array(int n, DUMB_CLICK_REMOVER **cr, long pos, sample_t *step);
dumb_record_click_array = _dumb_lib.dumb_record_click_array
dumb_record_click_array.argtypes = [c_int, POINTER(POINTER(DUMB_CLICK_REMOVER)), c_long, POINTER(sample_t)]
dumb_record_click_array.restype = None

#void dumb_record_click_negative_array(int n, DUMB_CLICK_REMOVER **cr, long pos, sample_t *step);
dumb_record_click_negative_array = _dumb_lib.dumb_record_click_negative_array
dumb_record_click_negative_array.argtypes = [c_int, POINTER(POINTER(DUMB_CLICK_REMOVER)), c_long, POINTER(sample_t)]
dumb_record_click_negative_array.restype = None

#void dumb_remove_clicks_array(int n, DUMB_CLICK_REMOVER **cr, sample_t **samples, long length, float halflife);
dumb_remove_clicks_array = _dumb_lib.dumb_remove_clicks_array
dumb_remove_clicks_array.argtypes = [c_int, POINTER(POINTER(DUMB_CLICK_REMOVER)), POINTER(POINTER(sample_t)), c_long, c_float]
dumb_remove_clicks_array.restype = None

#void dumb_click_remover_get_offset_array(int n, DUMB_CLICK_REMOVER **cr, sample_t *offset);
dumb_click_remover_get_offset_array = _dumb_lib.dumb_click_remover_get_offset_array
dumb_click_remover_get_offset_array.argtypes = [c_int, POINTER(POINTER(DUMB_CLICK_REMOVER)), POINTER(sample_t)]
dumb_click_remover_get_offset_array.restype = None

#void dumb_destroy_click_remover_array(int n, DUMB_CLICK_REMOVER **cr);
dumb_destroy_click_remover_array = _dumb_lib.dumb_destroy_click_remover_array
dumb_destroy_click_remover_array.argtypes = [c_int, POINTER(POINTER(DUMB_CLICK_REMOVER))]
dumb_destroy_click_remover_array.restype = None



#/* Resampling Helpers */

DUMB_RQ_ALIASING = 0
DUMB_RQ_LINEAR   = 1
DUMB_RQ_CUBIC    = 2
DUMB_RQ_N_LEVELS = 3
#extern int dumb_resampling_quality;
dumb_resampling_quality = c_int.in_dll(_dumb_lib, 'dumb_resampling_quality')


#typedef struct DUMB_RESAMPLER DUMB_RESAMPLER;
class DUMB_RESAMPLER(Structure):
    pass

#typedef void (*DUMB_RESAMPLE_PICKUP)(DUMB_RESAMPLER *resampler, void *data);
DUMB_RESAMPLE_PICKUP = CFUNCTYPE(None, POINTER(DUMB_RESAMPLER), c_void_p)

class x(Union):
    _fields_ = [
            ('x24', sample_t * (3*2)),
            ('x16', c_short * (3*2)),
            ('x8', c_char * (3*2))
            ]
DUMB_RESAMPLER._fields_ = [
        ('src', c_void_p),
        ('pos', c_long),
        ('subpos', c_int),
        ('start', c_long),
        ('end', c_long),
        ('dir', c_int),
        ('pickup', DUMB_RESAMPLE_PICKUP),
        ('pickup_data', c_void_p),
        ('min_quality', c_int),
        ('max_quality', c_int),
        #/* Everything below this point is internal: do not use. */
        ('x', x),
        ('overshot', c_int)
        ]

#void dumb_reset_resampler(DUMB_RESAMPLER *resampler, sample_t *src, int src_channels, long pos, long start, long end);
dumb_reset_resampler = _dumb_lib.dumb_reset_resampler
dumb_reset_resampler.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_int, c_long, c_long, c_long]
dumb_reset_resampler.restype = None

#DUMB_RESAMPLER *dumb_start_resampler(sample_t *src, int src_channels, long pos, long start, long end);
dumb_start_resampler = _dumb_lib.dumb_start_resampler
dumb_start_resampler.argtypes = [POINTER(sample_t), c_int, c_long, c_long, c_long]
dumb_start_resampler.restype = POINTER(DUMB_RESAMPLER)

#long dumb_resample_1_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume, float delta);
dumb_resample_1_1 = _dumb_lib.dumb_resample_1_1
dumb_resample_1_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float]
dumb_resample_1_1.restype = c_long

#long dumb_resample_1_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_1_2 = _dumb_lib.dumb_resample_1_2
dumb_resample_1_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_1_2.restype = c_long

#long dumb_resample_2_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_2_1 = _dumb_lib.dumb_resample_2_1
dumb_resample_2_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_2_1.restype = c_long

#long dumb_resample_2_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_2_2 = _dumb_lib.dumb_resample_2_2
dumb_resample_2_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_2_2.restype = c_long

#void dumb_resample_get_current_sample_1_1(DUMB_RESAMPLER *resampler, float volume, sample_t *dst);
dumb_resample_get_current_sample_1_1 = _dumb_lib.dumb_resample_get_current_sample_1_1
dumb_resample_get_current_sample_1_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_1_1.restype = None

#void dumb_resample_get_current_sample_1_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_1_2 = _dumb_lib.dumb_resample_get_current_sample_1_2
dumb_resample_get_current_sample_1_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_1_2.restype = None

#void dumb_resample_get_current_sample_2_1(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_2_1 = _dumb_lib.dumb_resample_get_current_sample_2_1
dumb_resample_get_current_sample_2_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_2_1.restype = None

#void dumb_resample_get_current_sample_2_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_2_2 = _dumb_lib.dumb_resample_get_current_sample_2_2
dumb_resample_get_current_sample_2_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_2_2.restype = None

#void dumb_end_resampler(DUMB_RESAMPLER *resampler);
dumb_end_resampler = _dumb_lib.dumb_end_resampler
dumb_end_resampler.argtypes = [POINTER(DUMB_RESAMPLER)]
dumb_end_resampler.restype = None


#void dumb_reset_resampler_16(DUMB_RESAMPLER *resampler, short *src, int src_channels, long pos, long start, long end);
dumb_reset_resampler_16 = _dumb_lib.dumb_reset_resampler_16
dumb_reset_resampler_16.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(c_short), c_int, c_long, c_long, c_long]
dumb_reset_resampler_16.restype = None

#DUMB_RESAMPLER *dumb_start_resampler_16(short *src, int src_channels, long pos, long start, long end);
dumb_start_resampler_16 = _dumb_lib.dumb_start_resampler_16
dumb_start_resampler_16.argtypes = [POINTER(c_short), c_int, c_long, c_long, c_long]
dumb_start_resampler_16.restype = POINTER(DUMB_RESAMPLER)

#long dumb_resample_16_1_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume, float delta);
dumb_resample_16_1_1 = _dumb_lib.dumb_resample_16_1_1
dumb_resample_16_1_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float]
dumb_resample_16_1_1.restype = c_long

#long dumb_resample_16_1_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_16_1_2 = _dumb_lib.dumb_resample_16_1_2
dumb_resample_16_1_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_16_1_2.restype = c_long

#long dumb_resample_16_2_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_16_2_1 = _dumb_lib.dumb_resample_16_2_1
dumb_resample_16_2_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_16_2_1.restype = c_long

#long dumb_resample_16_2_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_16_2_2 = _dumb_lib.dumb_resample_16_2_2
dumb_resample_16_2_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_16_2_2.restype = c_long

#void dumb_resample_get_current_sample_16_1_1(DUMB_RESAMPLER *resampler, float volume, sample_t *dst);
dumb_resample_get_current_sample_16_1_1 = _dumb_lib.dumb_resample_get_current_sample_16_1_1
dumb_resample_get_current_sample_16_1_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_16_1_1.restype = None

#void dumb_resample_get_current_sample_16_1_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_16_1_2 = _dumb_lib.dumb_resample_get_current_sample_16_1_2
dumb_resample_get_current_sample_16_1_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_16_1_2.restype = None

#void dumb_resample_get_current_sample_16_2_1(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_16_2_1 = _dumb_lib.dumb_resample_get_current_sample_16_2_1
dumb_resample_get_current_sample_16_2_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_16_2_1.restype = None

#void dumb_resample_get_current_sample_16_2_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_16_2_2 = _dumb_lib.dumb_resample_get_current_sample_16_2_2
dumb_resample_get_current_sample_16_2_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_16_2_2.restype = None

#void dumb_end_resampler_16(DUMB_RESAMPLER *resampler);
dumb_end_resampler_16 = _dumb_lib.dumb_end_resampler_16
dumb_end_resampler_16.argtypes = [POINTER(DUMB_RESAMPLER)]
dumb_end_resampler_16.restype = None


#void dumb_reset_resampler_8(DUMB_RESAMPLER *resampler, signed char *src, int src_channels, long pos, long start, long end);
dumb_reset_resampler_8 = _dumb_lib.dumb_reset_resampler_8
dumb_reset_resampler_8.argtypes = [POINTER(DUMB_RESAMPLER), c_char_p, c_int, c_long, c_long, c_long]
dumb_reset_resampler_8.restype = None

#DUMB_RESAMPLER *dumb_start_resampler_8(signed char *src, int src_channels, long pos, long start, long end);
dumb_start_resampler_8 = _dumb_lib.dumb_start_resampler_8
dumb_start_resampler_8.argtypes = [c_char_p, c_int, c_long, c_long, c_long]
dumb_start_resampler_8.restype = POINTER(DUMB_RESAMPLER)

#long dumb_resample_8_1_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume, float delta);
dumb_resample_8_1_1 = _dumb_lib.dumb_resample_8_1_1
dumb_resample_8_1_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float]
dumb_resample_8_1_1.restype = c_long

#long dumb_resample_8_1_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_8_1_2 = _dumb_lib.dumb_resample_8_1_2
dumb_resample_8_1_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_8_1_2.restype = c_long

#long dumb_resample_8_2_1(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_8_2_1 = _dumb_lib.dumb_resample_8_2_1
dumb_resample_8_2_1.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_8_2_1.restype = c_long

#long dumb_resample_8_2_2(DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_8_2_2 = _dumb_lib.dumb_resample_8_2_2
dumb_resample_8_2_2.argtypes = [POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_8_2_2.restype = c_long

#void dumb_resample_get_current_sample_8_1_1(DUMB_RESAMPLER *resampler, float volume, sample_t *dst);
dumb_resample_get_current_sample_8_1_1 = _dumb_lib.dumb_resample_get_current_sample_8_1_1
dumb_resample_get_current_sample_8_1_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_8_1_1.restype = None

#void dumb_resample_get_current_sample_8_1_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_8_1_2 = _dumb_lib.dumb_resample_get_current_sample_8_1_2
dumb_resample_get_current_sample_8_1_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_8_1_2.restype = None

#void dumb_resample_get_current_sample_8_2_1(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_8_2_1 = _dumb_lib.dumb_resample_get_current_sample_8_2_1
dumb_resample_get_current_sample_8_2_1.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_8_2_1.restype = None

#void dumb_resample_get_current_sample_8_2_2(DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_8_2_2 = _dumb_lib.dumb_resample_get_current_sample_8_2_2
dumb_resample_get_current_sample_8_2_2.argtypes = [POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_8_2_2.restype = None

#void dumb_end_resampler_8(DUMB_RESAMPLER *resampler);
dumb_end_resampler_8 = _dumb_lib.dumb_end_resampler_8
dumb_end_resampler_8.argtypes = [POINTER(DUMB_RESAMPLER)]
dumb_end_resampler_8.restype = None


#void dumb_reset_resampler_n(int n, DUMB_RESAMPLER *resampler, void *src, int src_channels, long pos, long start, long end);
dumb_reset_resampler_n = _dumb_lib.dumb_reset_resampler_n
dumb_reset_resampler_n.argtypes = [c_int, POINTER(DUMB_RESAMPLER), c_void_p, c_int, c_long, c_long, c_long]
dumb_reset_resampler_n.restype = None

#DUMB_RESAMPLER *dumb_start_resampler_n(int n, void *src, int src_channels, long pos, long start, long end);
dumb_start_resampler_n = _dumb_lib.dumb_start_resampler_n
dumb_start_resampler_n.argtypes = [c_int, c_void_p, c_int, c_long, c_long, c_long]
dumb_start_resampler_n.restype = POINTER(DUMB_RESAMPLER)

#long dumb_resample_n_1_1(int n, DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume, float delta);
dumb_resample_n_1_1 = _dumb_lib.dumb_resample_n_1_1
dumb_resample_n_1_1.argtypes = [c_int, POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float]
dumb_resample_n_1_1.restype = c_long

#long dumb_resample_n_1_2(int n, DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_n_1_2 = _dumb_lib.dumb_resample_n_1_2
dumb_resample_n_1_2.argtypes = [c_int, POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_n_1_2.restype = c_long

#long dumb_resample_n_2_1(int n, DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_n_2_1 = _dumb_lib.dumb_resample_n_2_1
dumb_resample_n_2_1.argtypes = [c_int, POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_n_2_1.restype = c_long

#long dumb_resample_n_2_2(int n, DUMB_RESAMPLER *resampler, sample_t *dst, long dst_size, float volume_left, float volume_right, float delta);
dumb_resample_n_2_2 = _dumb_lib.dumb_resample_n_2_2
dumb_resample_n_2_2.argtypes = [c_int, POINTER(DUMB_RESAMPLER), POINTER(sample_t), c_long, c_float, c_float, c_float]
dumb_resample_n_2_2.restype = c_long

#void dumb_resample_get_current_sample_n_1_1(int n, DUMB_RESAMPLER *resampler, float volume, sample_t *dst);
dumb_resample_get_current_sample_n_1_1 = _dumb_lib.dumb_resample_get_current_sample_n_1_1
dumb_resample_get_current_sample_n_1_1.argtypes = [c_int, POINTER(DUMB_RESAMPLER), c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_n_1_1.restype = None

#void dumb_resample_get_current_sample_n_1_2(int n, DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_n_1_2 = _dumb_lib.dumb_resample_get_current_sample_n_1_2
dumb_resample_get_current_sample_n_1_2.argtypes = [c_int, POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_n_1_2.restype = None

#void dumb_resample_get_current_sample_n_2_1(int n, DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_n_2_1 = _dumb_lib.dumb_resample_get_current_sample_n_2_1
dumb_resample_get_current_sample_n_2_1.argtypes = [c_int, POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_n_2_1.restype = None

#void dumb_resample_get_current_sample_n_2_2(int n, DUMB_RESAMPLER *resampler, float volume_left, float volume_right, sample_t *dst);
dumb_resample_get_current_sample_n_2_2 = _dumb_lib.dumb_resample_get_current_sample_n_2_2
dumb_resample_get_current_sample_n_2_2.argtypes = [c_int, POINTER(DUMB_RESAMPLER), c_float, c_float, POINTER(sample_t)]
dumb_resample_get_current_sample_n_2_2.restype = None

#void dumb_end_resampler_n(int n, DUMB_RESAMPLER *resampler);
dumb_end_resampler_n = _dumb_lib.dumb_end_resampler_n
dumb_end_resampler_n.argtypes = [c_int, POINTER(DUMB_RESAMPLER)]
dumb_end_resampler_n.restype = None



#/* DUH Construction */

#DUH *make_duh(
	#long length,
	#int n_tags,
	#const char *const tag[][2],
	#int n_signals,
	#DUH_SIGTYPE_DESC *desc[],
	#sigdata_t *sigdata[]
#);
make_duh = _dumb_lib.make_duh
make_duh.argtypes = [c_long, c_int, c_char_p * 2, c_int, POINTER(POINTER(DUH_SIGTYPE_DESC)), POINTER(POINTER(sigdata_t))]
make_duh.restype = POINTER(DUH)

#void duh_set_length(DUH *duh, long length);
duh_set_length = _dumb_lib.duh_set_length
duh_set_length.argtypes = [POINTER(DUH), c_long]
duh_set_length.restype = None


