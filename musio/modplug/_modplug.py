#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Modplug module.
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


""" Modplug module.

"""

from ctypes import *
from ctypes.util import find_library

mplib_name = find_library('modplug')
if not mplib_name:
    raise Exception("libmodplug could not be found")

_modplug_lib = cdll.LoadLibrary(mplib_name)

#/*
 #* This source code is public domain.
 #*
 #* Authors: Kenton Varda <temporal@gauge3d.org> (C interface wrapper)
 #*/

class _ModPlugFile(Structure):
    _fields_ = [
            ]
ModPlugFile = _ModPlugFile 

class _ModPlugNote(Structure):
    _fields_ = [
            ('Note', c_ubyte),
            ('Instrument', c_ubyte),
            ('VolumeEffect', c_ubyte),
            ('Effect', c_ubyte),
            ('Volume', c_ubyte),
            ('Parameter', c_ubyte)
            ]
ModPlugNote = _ModPlugNote 

#typedef void (*ModPlugMixerProc)(int*, unsigned long, unsigned long);
ModPlugMixerProc = CFUNCTYPE(None, POINTER(c_int), c_ulong, c_ulong)


#/* Load a mod file.  [data] should point to a block of memory containing the complete
 #* file, and [size] should be the size of that block.
 #* Return the loaded mod file on success, or NULL on failure. */
#ModPlugFile* ModPlug_Load(const void* data, int size);
ModPlug_Load = _modplug_lib.ModPlug_Load
ModPlug_Load.argtypes = [c_void_p, c_int]
ModPlug_Load.restype = POINTER(ModPlugFile)

#/* Unload a mod file. */
#void ModPlug_Unload(ModPlugFile* file);
ModPlug_Unload = _modplug_lib.ModPlug_Unload
ModPlug_Unload.argtypes = [POINTER(ModPlugFile)]
ModPlug_Unload.restype = None


#/* Read sample data into the buffer.  Returns the number of bytes read.  If the end
 #* of the mod has been reached, zero is returned. */
#int  ModPlug_Read(ModPlugFile* file, void* buffer, int size);
ModPlug_Read = _modplug_lib.ModPlug_Read
ModPlug_Read.argtypes = [POINTER(ModPlugFile), c_void_p, c_int]
ModPlug_Read.restype = c_int


#/* Get the name of the mod.  The returned buffer is stored within the ModPlugFile
 #* structure and will remain valid until you unload the file. */
#const char* ModPlug_GetName(ModPlugFile* file);
ModPlug_GetName = _modplug_lib.ModPlug_GetName
ModPlug_GetName.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetName.restype = c_char_p


#/* Get the length of the mod, in milliseconds.  Note that this result is not always
 #* accurate, especially in the case of mods with loops. */
#int ModPlug_GetLength(ModPlugFile* file);
ModPlug_GetLength = _modplug_lib.ModPlug_GetLength
ModPlug_GetLength.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetLength.restype = c_int


#/* Seek to a particular position in the song.  Note that seeking and MODs don't mix very
 #* well.  Some mods will be missing instruments for a short time after a seek, as ModPlug
 #* does not scan the sequence backwards to find out which instruments were supposed to be
 #* playing at that time.  (Doing so would be difficult and not very reliable.)  Also,
 #* note that seeking is not very exact in some mods -- especially those for which
 #* ModPlug_GetLength() does not report the full length. */
#void ModPlug_Seek(ModPlugFile* file, int millisecond);
ModPlug_Seek = _modplug_lib.ModPlug_Seek
ModPlug_Seek.argtypes = [POINTER(ModPlugFile), c_int]
ModPlug_Seek.restype = None


_ModPlug_Flags = c_int
MODPLUG_ENABLE_OVERSAMPLING     = 1 << 0  # /* Enable oversampling (*highly* recommended) */
MODPLUG_ENABLE_NOISE_REDUCTION  = 1 << 1  # /* Enable noise reduction */
MODPLUG_ENABLE_REVERB           = 1 << 2  # /* Enable reverb */
MODPLUG_ENABLE_MEGABASS         = 1 << 3  # /* Enable megabass */
MODPLUG_ENABLE_SURROUND         = 1 << 4  # /* Enable surround sound. */


_ModPlug_ResamplingMode = c_int
MODPLUG_RESAMPLE_NEAREST = 0  # No interpolation (very fast, extremely bad sound quality)
MODPLUG_RESAMPLE_LINEAR  = 1  # Linear interpolation (fast, good quality)
MODPLUG_RESAMPLE_SPLINE  = 2  # Cubic spline interpolation (high quality)
MODPLUG_RESAMPLE_FIR     = 3  # 8-tap fir filter (extremely high quality)

class _ModPlug_Settings(Structure):
    _fields_ = [
            ('mFlags', c_int),           # One or more of the MODPLUG_ENABLE_* flags above, bitwise-OR'ed
            
            # Note that ModPlug always decodes sound at 44100kHz, 32 bit, stereo and then
            # down-mixes to the settings you choose.
	        ('mChannels', c_int),        # Number of channels - 1 for mono or 2 for stereo
	        ('mBits', c_int),            # Bits per sample - 8, 16, or 32
	        ('mFrequency', c_int),       # Sampling rate - 11025, 22050, or 44100
	        ('mResamplingMode', c_int),  # One of MODPLUG_RESAMPLE_*, above

            ('mStereoSeparation', c_int),# Stereo separation, 1 - 256
            ('mMaxMixChannels', c_int),  # Maximum number of mixing channels (polyphony), 32 - 256

	        ('mReverbDepth', c_int),     # Reverb level 0(quiet)-100(loud)

	        ('mReverbDelay', c_int),     # Reverb delay in ms, usually 40-200ms
	        ('mBassAmount', c_int),      # XBass level 0(quiet)-100(loud)
	        ('mBassRange', c_int),       # XBass cutoff in Hz 10-100
	        ('mSurroundDepth', c_int),   # Surround level 0(quiet)-100(heavy)
	        ('mSurroundDelay', c_int),   # Surround delay in ms, usually 5-40ms
	        ('mLoopCount', c_int)        # Number of times to loop.  Zero prevents looping.
                                                # -1 loops forever.
            ]
ModPlug_Settings = _ModPlug_Settings

#/* Get and set the mod decoder settings.  All options, except for channels, bits-per-sample,
 #* sampling rate, and loop count, will take effect immediately.  Those options which don't
 #* take effect immediately will take effect the next time you load a mod. */
#void ModPlug_GetSettings(ModPlug_Settings* settings);
ModPlug_GetSettings = _modplug_lib.ModPlug_GetSettings
ModPlug_GetSettings.argtypes = [POINTER(ModPlug_Settings)]
ModPlug_GetSettings.restype = None

#void ModPlug_SetSettings(const ModPlug_Settings* settings);
ModPlug_SetSettings = _modplug_lib.ModPlug_SetSettings
ModPlug_SetSettings.argtypes = [POINTER(ModPlug_Settings)]
ModPlug_SetSettings.restype = None


#/* New ModPlug API Functions */
#/* NOTE: Master Volume (1-512) */
#unsigned int ModPlug_GetMasterVolume(ModPlugFile* file) ;
ModPlug_GetMasterVolume = _modplug_lib.ModPlug_GetMasterVolume
ModPlug_GetMasterVolume.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetMasterVolume.restype = c_uint

#void ModPlug_SetMasterVolume(ModPlugFile* file,unsigned int cvol) ;
ModPlug_SetMasterVolume = _modplug_lib.ModPlug_SetMasterVolume
ModPlug_SetMasterVolume.argtypes = [POINTER(ModPlugFile), c_uint]
ModPlug_SetMasterVolume.restype = None


#int ModPlug_GetCurrentSpeed(ModPlugFile* file);
ModPlug_GetCurrentSpeed = _modplug_lib.ModPlug_GetCurrentSpeed
ModPlug_GetCurrentSpeed.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetCurrentSpeed.restype = c_int

#int ModPlug_GetCurrentTempo(ModPlugFile* file);
ModPlug_GetCurrentTempo = _modplug_lib.ModPlug_GetCurrentTempo
ModPlug_GetCurrentTempo.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetCurrentTempo.restype = c_int

#int ModPlug_GetCurrentOrder(ModPlugFile* file);
ModPlug_GetCurrentOrder = _modplug_lib.ModPlug_GetCurrentOrder
ModPlug_GetCurrentOrder.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetCurrentOrder.restype = c_int

#int ModPlug_GetCurrentPattern(ModPlugFile* file);
ModPlug_GetCurrentPattern = _modplug_lib.ModPlug_GetCurrentPattern
ModPlug_GetCurrentPattern.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetCurrentPattern.restype = c_int

#int ModPlug_GetCurrentRow(ModPlugFile* file);
ModPlug_GetCurrentRow = _modplug_lib.ModPlug_GetCurrentRow
ModPlug_GetCurrentRow.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetCurrentRow.restype = c_int

#int ModPlug_GetPlayingChannels(ModPlugFile* file);
ModPlug_GetPlayingChannels = _modplug_lib.ModPlug_GetPlayingChannels
ModPlug_GetPlayingChannels.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetPlayingChannels.restype = c_int


#void ModPlug_SeekOrder(ModPlugFile* file,int order);
ModPlug_SeekOrder = _modplug_lib.ModPlug_SeekOrder
ModPlug_SeekOrder.argtypes = [POINTER(ModPlugFile), c_int]
ModPlug_SeekOrder.restype = None

#int ModPlug_GetModuleType(ModPlugFile* file);
ModPlug_GetModuleType = _modplug_lib.ModPlug_GetModuleType
ModPlug_GetModuleType.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetModuleType.restype = c_int

#char* ModPlug_GetMessage(ModPlugFile* file);
ModPlug_GetMessage = _modplug_lib.ModPlug_GetMessage
ModPlug_GetMessage.argtypes = [POINTER(ModPlugFile)]
ModPlug_GetMessage.restype = c_char_p



#ifndef MODPLUG_NO_FILESAVE
#/*
 #* EXPERIMENTAL Export Functions
 #*/
#/*Export to a Scream Tracker 3 S3M module. EXPERIMENTAL (only works on Little-Endian platforms)*/
#char ModPlug_ExportS3M(ModPlugFile* file, const char* filepath);
#ModPlug_ExportS3M = _modplug_lib.ModPlug_ExportS3M
#ModPlug_ExportS3M.argtypes = [POINTER(ModPlugFile), POINTER(c_char)]
#ModPlug_ExportS3M.restype = c_char


#/*Export to a Extended Module (XM). EXPERIMENTAL (only works on Little-Endian platforms)*/
#char ModPlug_ExportXM(ModPlugFile* file, const char* filepath);
#ModPlug_ExportXM = _modplug_lib.ModPlug_ExportXM
#ModPlug_ExportXM.argtypes = [POINTER(ModPlugFile), POINTER(c_char)]
#ModPlug_ExportXM.restype = c_char


#/*Export to a Amiga MOD file. EXPERIMENTAL.*/
#char ModPlug_ExportMOD(ModPlugFile* file, const char* filepath);
#ModPlug_ExportMOD = _modplug_lib.ModPlug_ExportMOD
#ModPlug_ExportMOD.argtypes = [POINTER(ModPlugFile), POINTER(c_char)]
#ModPlug_ExportMOD.restype = c_char


#/*Export to a Impulse Tracker IT file. Should work OK in Little-Endian & Big-Endian platforms :-) */
#char ModPlug_ExportIT(ModPlugFile* file, const char* filepath);
#ModPlug_ExportIT = _modplug_lib.ModPlug_ExportIT
#ModPlug_ExportIT.argtypes = [POINTER(ModPlugFile), POINTER(c_char)]
#ModPlug_ExportIT.restype = c_char

#endif // MODPLUG_NO_FILESAVE

#unsigned int ModPlug_NumInstruments(ModPlugFile* file);
ModPlug_NumInstruments = _modplug_lib.ModPlug_NumInstruments
ModPlug_NumInstruments.argtypes = [POINTER(ModPlugFile)]
ModPlug_NumInstruments.restype = c_uint

#unsigned int ModPlug_NumSamples(ModPlugFile* file);
ModPlug_NumSamples = _modplug_lib.ModPlug_NumSamples
ModPlug_NumSamples.argtypes = [POINTER(ModPlugFile)]
ModPlug_NumSamples.restype = c_uint

#unsigned int ModPlug_NumPatterns(ModPlugFile* file);
ModPlug_NumPatterns = _modplug_lib.ModPlug_NumPatterns
ModPlug_NumPatterns.argtypes = [POINTER(ModPlugFile)]
ModPlug_NumPatterns.restype = c_uint

#unsigned int ModPlug_NumChannels(ModPlugFile* file);
ModPlug_NumChannels = _modplug_lib.ModPlug_NumChannels
ModPlug_NumChannels.argtypes = [POINTER(ModPlugFile)]
ModPlug_NumChannels.restype = c_uint

#unsigned int ModPlug_SampleName(ModPlugFile* file, unsigned int qual, char* buff);
ModPlug_SampleName = _modplug_lib.ModPlug_SampleName
ModPlug_SampleName.argtypes = [POINTER(ModPlugFile), c_uint, POINTER(c_char)]
ModPlug_SampleName.restype = c_uint

#unsigned int ModPlug_InstrumentName(ModPlugFile* file, unsigned int qual, char* buff);
ModPlug_InstrumentName = _modplug_lib.ModPlug_InstrumentName
ModPlug_InstrumentName.argtypes = [POINTER(ModPlugFile), c_uint, POINTER(c_char)]
ModPlug_InstrumentName.restype = c_uint


#/*
 #* Retrieve pattern note-data
 #*/
#ModPlugNote* ModPlug_GetPattern(ModPlugFile* file, int pattern, unsigned int* numrows);
ModPlug_GetPattern = _modplug_lib.ModPlug_GetPattern
ModPlug_GetPattern.argtypes = [POINTER(ModPlugFile), c_int, POINTER(c_uint)]
ModPlug_GetPattern.restype = POINTER(ModPlugNote)


#/*
 #* =================
 #* Mixer callback
 #* =================
 #*
 #* Use this callback if you want to 'modify' the mixed data of LibModPlug.
 #* 
 #* void proc(int* buffer,unsigned long channels,unsigned long nsamples) ;
 #*
 #* 'buffer': A buffer of mixed samples
 #* 'channels': N. of channels in the buffer
 #* 'nsamples': N. of samples in the buffeer (without taking care of n.channels)
 #*
 #* (Samples are signed 32-bit integers)
 #*/
#void ModPlug_InitMixerCallback(ModPlugFile* file,ModPlugMixerProc proc) ;
ModPlug_InitMixerCallback = _modplug_lib.ModPlug_InitMixerCallback
ModPlug_InitMixerCallback.argtypes = [POINTER(ModPlugFile), ModPlugMixerProc]
ModPlug_InitMixerCallback.restype = None

#void ModPlug_UnloadMixerCallback(ModPlugFile* file) ;
ModPlug_UnloadMixerCallback = _modplug_lib.ModPlug_UnloadMixerCallback
ModPlug_UnloadMixerCallback.argtypes = [POINTER(ModPlugFile)]
ModPlug_UnloadMixerCallback.restype = None

