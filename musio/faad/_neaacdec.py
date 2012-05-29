# -*- coding: UTF8 -*-
#
# python faad wrapper library.
# Generated with h2xml and xml2py then modified.
# Copyright (C) 2011 Josiah Gordon <josiahg@gmail.com>
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


""" python faad wrapper module.

"""

from ctypes import *
from ctypes.util import find_library

faadlib_name = find_library('faad')
if not faadlib_name:
    raise Exception("libfaad not be found")
_faad_lib = cdll.LoadLibrary(faadlib_name)

_libraries = {}
_libraries['libfaad.so.2'] = _faad_lib

# _libraries = {}
# _libraries['libfaad.so.2'] = CDLL('libfaad.so.2')
STRING = c_char_p


# faacDecInitDRM = NeAACDecInitDRM # alias
NeAACDecHandle = c_void_p
NeAACDecInit2 = _libraries['libfaad.so.2'].NeAACDecInit2
NeAACDecInit2.restype = c_char
NeAACDecInit2.argtypes = [NeAACDecHandle, POINTER(c_ubyte), c_ulong, POINTER(c_ulong), POINTER(c_ubyte)]
faacDecInit2 = NeAACDecInit2 # alias
class NeAACDecConfiguration(Structure):
    pass
NeAACDecConfigurationPtr = POINTER(NeAACDecConfiguration)
NeAACDecSetConfiguration = _libraries['libfaad.so.2'].NeAACDecSetConfiguration
NeAACDecSetConfiguration.restype = c_ubyte
NeAACDecSetConfiguration.argtypes = [NeAACDecHandle, NeAACDecConfigurationPtr]
faacDecSetConfiguration = NeAACDecSetConfiguration # alias
NeAACDecClose = _libraries['libfaad.so.2'].NeAACDecClose
NeAACDecClose.restype = None
NeAACDecClose.argtypes = [NeAACDecHandle]
faacDecClose = NeAACDecClose # alias
class NeAACDecFrameInfo(Structure):
    pass
faacDecFrameInfo = NeAACDecFrameInfo # alias
NeAACDecGetErrorMessage = _libraries['libfaad.so.2'].NeAACDecGetErrorMessage
NeAACDecGetErrorMessage.restype = STRING
NeAACDecGetErrorMessage.argtypes = [c_ubyte]
faacDecGetErrorMessage = NeAACDecGetErrorMessage # alias
faacDecConfigurationPtr = NeAACDecConfigurationPtr # alias
faacDecConfiguration = NeAACDecConfiguration # alias
NeAACDecInit = _libraries['libfaad.so.2'].NeAACDecInit
NeAACDecInit.restype = c_long
NeAACDecInit.argtypes = [NeAACDecHandle, POINTER(c_ubyte), c_ulong, POINTER(c_ulong), POINTER(c_ubyte)]
faacDecInit = NeAACDecInit # alias
class mp4AudioSpecificConfig(Structure):
    pass
NeAACDecAudioSpecificConfig = _libraries['libfaad.so.2'].NeAACDecAudioSpecificConfig
NeAACDecAudioSpecificConfig.restype = c_char
NeAACDecAudioSpecificConfig.argtypes = [POINTER(c_ubyte), c_ulong, POINTER(mp4AudioSpecificConfig)]
AudioSpecificConfig = NeAACDecAudioSpecificConfig # alias
NeAACDecGetCurrentConfiguration = _libraries['libfaad.so.2'].NeAACDecGetCurrentConfiguration
NeAACDecGetCurrentConfiguration.restype = NeAACDecConfigurationPtr
NeAACDecGetCurrentConfiguration.argtypes = [NeAACDecHandle]
faacDecGetCurrentConfiguration = NeAACDecGetCurrentConfiguration # alias
faacDecHandle = NeAACDecHandle # alias
NeAACDecOpen = _libraries['libfaad.so.2'].NeAACDecOpen
NeAACDecOpen.restype = NeAACDecHandle
NeAACDecOpen.argtypes = []
faacDecOpen = NeAACDecOpen # alias
NeAACDecDecode = _libraries['libfaad.so.2'].NeAACDecDecode
NeAACDecDecode.restype = c_void_p
NeAACDecDecode.argtypes = [NeAACDecHandle, POINTER(NeAACDecFrameInfo), POINTER(c_ubyte), c_ulong]
faacDecDecode = NeAACDecDecode # alias
NeAACDecPostSeekReset = _libraries['libfaad.so.2'].NeAACDecPostSeekReset
NeAACDecPostSeekReset.restype = None
NeAACDecPostSeekReset.argtypes = [NeAACDecHandle, c_long]
faacDecPostSeekReset = NeAACDecPostSeekReset # alias
FAAD_FMT_FLOAT = 4 # Variable c_int '4'
FAAD_FMT_FIXED = FAAD_FMT_FLOAT # alias
FAAD_FMT_DOUBLE = 5 # Variable c_int '5'
NO_SBR_UPSAMPLED = 3 # Variable c_int '3'
DRM_ER_LC = 27 # Variable c_int '27'
LC_DEC_CAP = 1 # Variable c_int '1'
DRMCH_SBR_MONO = 3 # Variable c_int '3'
FAAD_FMT_24BIT = 2 # Variable c_int '2'
HE_AAC = 5 # Variable c_int '5'
BACK_CHANNEL_CENTER = 8 # Variable c_int '8'
LD = 23 # Variable c_int '23'
FAAD_FMT_32BIT = 3 # Variable c_int '3'
LC = 2 # Variable c_int '2'
FRONT_CHANNEL_RIGHT = 3 # Variable c_int '3'
FRONT_CHANNEL_CENTER = 1 # Variable c_int '1'
DRMCH_SBR_PS_STEREO = 5 # Variable c_int '5'
ER_LTP = 19 # Variable c_int '19'
RAW = 0 # Variable c_int '0'
NO_SBR = 0 # Variable c_int '0'
ER_LC = 17 # Variable c_int '17'
LFE_CHANNEL = 9 # Variable c_int '9'
FAAD2_VERSION = '2.7' # Variable STRING '(const char*)"2.7"'
FRONT_CHANNEL_LEFT = 2 # Variable c_int '2'
LTP = 4 # Variable c_int '4'
BACK_CHANNEL_RIGHT = 7 # Variable c_int '7'
SIDE_CHANNEL_LEFT = 4 # Variable c_int '4'
DRMCH_SBR_STEREO = 4 # Variable c_int '4'
FAAD_MIN_STREAMSIZE = 768 # Variable c_int '768'
ADTS = 2 # Variable c_int '2'
ADIF = 1 # Variable c_int '1'
ERROR_RESILIENCE_CAP = 16 # Variable c_int '16'
LD_DEC_CAP = 8 # Variable c_int '8'
FIXED_POINT_CAP = 32 # Variable c_int '32'
FAAD_FMT_16BIT = 1 # Variable c_int '1'
MAIN = 1 # Variable c_int '1'
SBR_UPSAMPLED = 1 # Variable c_int '1'
SBR_DOWNSAMPLED = 2 # Variable c_int '2'
SSR = 3 # Variable c_int '3'
UNKNOWN_CHANNEL = 0 # Variable c_int '0'
DRMCH_MONO = 1 # Variable c_int '1'
DRMCH_STEREO = 2 # Variable c_int '2'
LATM = 3 # Variable c_int '3'
SIDE_CHANNEL_RIGHT = 5 # Variable c_int '5'
BACK_CHANNEL_LEFT = 6 # Variable c_int '6'
MAIN_DEC_CAP = 2 # Variable c_int '2'
LTP_DEC_CAP = 4 # Variable c_int '4'
mp4AudioSpecificConfig._fields_ = [
    ('objectTypeIndex', c_ubyte),
    ('samplingFrequencyIndex', c_ubyte),
    ('samplingFrequency', c_ulong),
    ('channelsConfiguration', c_ubyte),
    ('frameLengthFlag', c_ubyte),
    ('dependsOnCoreCoder', c_ubyte),
    ('coreCoderDelay', c_ushort),
    ('extensionFlag', c_ubyte),
    ('aacSectionDataResilienceFlag', c_ubyte),
    ('aacScalefactorDataResilienceFlag', c_ubyte),
    ('aacSpectralDataResilienceFlag', c_ubyte),
    ('epConfig', c_ubyte),
    ('sbr_present_flag', c_char),
    ('forceUpSampling', c_char),
    ('downSampledSBR', c_char),
]
NeAACDecConfiguration._fields_ = [
    ('defObjectType', c_ubyte),
    ('defSampleRate', c_ulong),
    ('outputFormat', c_ubyte),
    ('downMatrix', c_ubyte),
    ('useOldADTSFormat', c_ubyte),
    ('dontUpSampleImplicitSBR', c_ubyte),
]
NeAACDecFrameInfo._fields_ = [
    ('bytesconsumed', c_ulong),
    ('samples', c_ulong),
    ('channels', c_ubyte),
    ('error', c_ubyte),
    ('samplerate', c_ulong),
    ('sbr', c_ubyte),
    ('object_type', c_ubyte),
    ('header_type', c_ubyte),
    ('num_front_channels', c_ubyte),
    ('num_side_channels', c_ubyte),
    ('num_back_channels', c_ubyte),
    ('num_lfe_channels', c_ubyte),
    ('channel_position', c_ubyte * 64),
    ('ps', c_ubyte),
]
NeAACDecGetCapabilities = _libraries['libfaad.so.2'].NeAACDecGetCapabilities
NeAACDecGetCapabilities.restype = c_ulong
NeAACDecGetCapabilities.argtypes = []
NeAACDecDecode2 = _libraries['libfaad.so.2'].NeAACDecDecode2
NeAACDecDecode2.restype = c_void_p
#NeAACDecDecode2.argtypes = [NeAACDecHandle, POINTER(NeAACDecFrameInfo), POINTER(c_ubyte), c_ulong, POINTER(c_void_p), c_ulong]
__all__ = ['FRONT_CHANNEL_CENTER', 'SBR_UPSAMPLED', 'faacDecDecode',
           'AudioSpecificConfig', 'NO_SBR_UPSAMPLED',
           'NeAACDecDecode2', 'faacDecSetConfiguration',
           'faacDecOpen', 'DRM_ER_LC', 'LC_DEC_CAP', 'ER_LTP',
           'DRMCH_SBR_MONO', 'NeAACDecClose',
           'faacDecConfigurationPtr', 'FAAD_FMT_24BIT',
           'faacDecConfiguration', 'HE_AAC', 'BACK_CHANNEL_CENTER',
           'NeAACDecGetErrorMessage', 'LD', 'faacDecClose',
           'NeAACDecDecode', 'LC', 'NeAACDecPostSeekReset',
           'FRONT_CHANNEL_RIGHT', 'FAAD_FMT_DOUBLE',
           'DRMCH_SBR_PS_STEREO', 'NeAACDecInit', 'faacDecFrameInfo',
           'RAW', 'NeAACDecFrameInfo', 'NO_SBR', 'ER_LC',
           'LFE_CHANNEL', 'SIDE_CHANNEL_LEFT', 'FAAD2_VERSION',
           'faacDecInit2', 'NeAACDecHandle', 'NeAACDecOpen',
           'faacDecGetCurrentConfiguration', 'LTP',
           'BACK_CHANNEL_RIGHT', 'NeAACDecGetCapabilities',
           'faacDecGetErrorMessage', 'NeAACDecAudioSpecificConfig',
           'FAAD_MIN_STREAMSIZE', 'mp4AudioSpecificConfig',
           'FAAD_FMT_FLOAT', 'NeAACDecConfigurationPtr', 'LATM',
           'FAAD_FMT_32BIT', 'ADTS', 'ADIF', 'NeAACDecInit2',
           'ERROR_RESILIENCE_CAP', 'NeAACDecGetCurrentConfiguration',
           'BACK_CHANNEL_LEFT', 'faacDecHandle', 'FIXED_POINT_CAP',
           'faacDecInit', 'FAAD_FMT_16BIT', 'faacDecPostSeekReset',
           'LTP_DEC_CAP', 'SIDE_CHANNEL_RIGHT', 'SBR_DOWNSAMPLED',
           'MAIN_DEC_CAP', 'SSR', 'UNKNOWN_CHANNEL',
           'FRONT_CHANNEL_LEFT', 'DRMCH_MONO', 'DRMCH_STEREO',
           'LD_DEC_CAP', 'FAAD_FMT_FIXED', 'NeAACDecSetConfiguration',
           'MAIN', 'DRMCH_SBR_STEREO', 'NeAACDecConfiguration']
