#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Mikmod module.
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


"""Mikmod module."""

import ctypes
import sys
from ctypes.util import find_library

miklib_name = find_library("mikmod")
if not miklib_name:
    raise Exception("libmikmod could not be found")

_mikmod_lib = ctypes.cdll.LoadLibrary(miklib_name)

# /*
# *	========== Library version
# */

LIBMIKMOD_VERSION_MAJOR = 3
LIBMIKMOD_VERSION_MINOR = 1
LIBMIKMOD_REVISION = 10


def LIBMIKMOD_VERSION():
    return (
        (LIBMIKMOD_VERSION_MAJOR << 16)
        | (LIBMIKMOD_VERSION_MINOR << 8)
        | (LIBMIKMOD_REVISION)
    )


# MIKMODAPI extern long MikMod_GetVersion(void);
MikMod_GetVersion = _mikmod_lib.MikMod_GetVersion
MikMod_GetVersion.argtypes = []
MikMod_GetVersion.restype = ctypes.c_long

# /*
# *	========== Platform independent-type definitions
# */

CHAR = ctypes.c_char_p


# if defined(__arch64__) || defined(__alpha) || defined(__x86_64) || defined(_LP64)
if sys.maxsize >> 31:
    # /* 64 bit architectures */

    SBYTE = ctypes.c_byte  # /* 1 byte, signed */
    UBYTE = ctypes.c_ubyte  # /* 1 byte, unsigned */
    SWORD = ctypes.c_short  # /* 2 bytes, signed */
    UWORD = ctypes.c_ushort  # /* 2 bytes, unsigned */
    SLONG = ctypes.c_long  # /* 4 bytes, signed */
    ULONG = ctypes.c_uint  # /* 4 bytes, unsigned */
    BOOL = ctypes.c_int  # /* 0=false, <>0 true */

# else
else:
    # /* 32 bit architectures */

    SBYTE = ctypes.c_byte  # /* 1 byte, signed */
    UBYTE = ctypes.c_ubyte  # /* 1 byte, unsigned */
    SWORD = ctypes.c_short  # /* 2 bytes, signed */
    UWORD = ctypes.c_ushort  # /* 2 bytes, unsigned */
    SLONG = ctypes.c_long  # /* 4 bytes, signed */
    # if !defined(__OS2__)&&!defined(__EMX__)&&!defined(WIN32)
    if sys.platform not in ["os2", "win32"]:
        ULONG = ctypes.c_uint  # /* 4 bytes, unsigned */
        BOOL = ctypes.c_int  # /* 0=false, <>0 true */
# endif
# endif

# /*
# *	========== Error codes
# */

MMERR_OPENING_FILE = 1
MMERR_OUT_OF_MEMORY = 2
MMERR_DYNAMIC_LINKING = 3

MMERR_SAMPLE_TOO_BIG = 4
MMERR_OUT_OF_HANDLES = 5
MMERR_UNKNOWN_WAVE_TYPE = 6

MMERR_LOADING_PATTERN = 7
MMERR_LOADING_TRACK = 8
MMERR_LOADING_HEADER = 9
MMERR_LOADING_SAMPLEINFO = 10
MMERR_NOT_A_MODULE = 11
MMERR_NOT_A_STREAM = 12
MMERR_MED_SYNTHSAMPLES = 13
MMERR_ITPACK_INVALID_DATA = 14

MMERR_DETECTING_DEVICE = 15
MMERR_INVALID_DEVICE = 16
MMERR_INITIALIZING_MIXER = 17
MMERR_OPENING_AUDIO = 18
MMERR_8BIT_ONLY = 19
MMERR_16BIT_ONLY = 20
MMERR_STEREO_ONLY = 21
MMERR_ULAW = 22
MMERR_NON_BLOCK = 23

MMERR_AF_AUDIO_PORT = 24

MMERR_AIX_CONFIG_INIT = 25
MMERR_AIX_CONFIG_CONTROL = 26
MMERR_AIX_CONFIG_START = 27

MMERR_GUS_SETTINGS = 28
MMERR_GUS_RESET = 29
MMERR_GUS_TIMER = 30

MMERR_HP_SETSAMPLESIZE = 31
MMERR_HP_SETSPEED = 32
MMERR_HP_CHANNELS = 33
MMERR_HP_AUDIO_OUTPUT = 34
MMERR_HP_AUDIO_DESC = 35
MMERR_HP_BUFFERSIZE = 36

MMERR_OSS_SETFRAGMENT = 37
MMERR_OSS_SETSAMPLESIZE = 38
MMERR_OSS_SETSTEREO = 39
MMERR_OSS_SETSPEED = 40

MMERR_SGI_SPEED = 41
MMERR_SGI_16BIT = 42
MMERR_SGI_8BIT = 43
MMERR_SGI_STEREO = 44
MMERR_SGI_MONO = 45

MMERR_SUN_INIT = 46

MMERR_OS2_MIXSETUP = 47
MMERR_OS2_SEMAPHORE = 48
MMERR_OS2_TIMER = 49
MMERR_OS2_THREAD = 50

MMERR_DS_PRIORITY = 51
MMERR_DS_BUFFER = 52
MMERR_DS_FORMAT = 53
MMERR_DS_NOTIFY = 54
MMERR_DS_EVENT = 55
MMERR_DS_THREAD = 56
MMERR_DS_UPDATE = 57

MMERR_WINMM_HANDLE = 58
MMERR_WINMM_ALLOCATED = 59
MMERR_WINMM_DEVICEID = 60
MMERR_WINMM_FORMAT = 61
MMERR_WINMM_UNKNOWN = 62

MMERR_MAC_SPEED = 63
MMERR_MAC_START = 64

MMERR_MAX = 65

# /*
# *	========== Error handling
# */

# typedef void (MikMod_handler)(void);
MikMod_handler = ctypes.CFUNCTYPE(None)

# typedef MikMod_handler *MikMod_handler_t;
MikMod_handler_t = ctypes.POINTER(MikMod_handler)

# MIKMODAPI extern int  MikMod_errno;
MikMod_errno = ctypes.c_int.in_dll(_mikmod_lib, "MikMod_errno")

# MIKMODAPI extern BOOL MikMod_critical;
MikMod_critical = ctypes.c_int.in_dll(_mikmod_lib, "MikMod_critical")

# MIKMODAPI extern char *MikMod_strerror(int);
MikMod_strerror = _mikmod_lib.MikMod_strerror
MikMod_strerror.argtypes = [ctypes.c_int]
MikMod_strerror.restype = ctypes.c_char_p

# MIKMODAPI extern MikMod_handler_t MikMod_RegisterErrorHandler(MikMod_handler_t);
MikMod_RegisterErrorHandler = _mikmod_lib.MikMod_RegisterErrorHandler
MikMod_RegisterErrorHandler.argtypes = [MikMod_handler_t]
MikMod_RegisterErrorHandler.restype = MikMod_handler_t


# /*
# *	========== Library initialization and core functions
# */

# struct MDRIVER;
class MDRIVER(ctypes.Structure):
    pass


# MIKMODAPI extern void   MikMod_RegisterAllDrivers(void);
MikMod_RegisterAllDrivers = _mikmod_lib.MikMod_RegisterAllDrivers
MikMod_RegisterAllDrivers.argtypes = []
MikMod_RegisterAllDrivers.restype = None


# MIKMODAPI extern CHAR*  MikMod_InfoDriver(void);
MikMod_InfoDriver = _mikmod_lib.MikMod_InfoDriver
MikMod_InfoDriver.argtypes = []
MikMod_InfoDriver.restype = CHAR

# MIKMODAPI extern void   MikMod_RegisterDriver(struct MDRIVER*);
MikMod_RegisterDriver = _mikmod_lib.MikMod_RegisterDriver
MikMod_RegisterDriver.argtypes = [ctypes.POINTER(MDRIVER)]
MikMod_RegisterDriver.restype = None

# MIKMODAPI extern int    MikMod_DriverFromAlias(CHAR*);
MikMod_DriverFromAlias = _mikmod_lib.MikMod_DriverFromAlias
MikMod_DriverFromAlias.argtypes = [CHAR]
MikMod_DriverFromAlias.restype = ctypes.c_int


# MIKMODAPI extern BOOL   MikMod_Init(CHAR*);
MikMod_Init = _mikmod_lib.MikMod_Init
MikMod_Init.argtypes = [CHAR]
MikMod_Init.restype = BOOL

# MIKMODAPI extern void   MikMod_Exit(void);
MikMod_Exit = _mikmod_lib.MikMod_Exit
MikMod_Exit.argtypes = []
MikMod_Exit.restype = None

# MIKMODAPI extern BOOL   MikMod_Reset(CHAR*);
MikMod_Reset = _mikmod_lib.MikMod_Reset
MikMod_Reset.argtypes = [CHAR]
MikMod_Reset.restype = BOOL

# MIKMODAPI extern BOOL   MikMod_SetNumVoices(int,int);
MikMod_SetNumVoices = _mikmod_lib.MikMod_SetNumVoices
MikMod_SetNumVoices.argtypes = [ctypes.c_int, ctypes.c_int]
MikMod_SetNumVoices.restype = BOOL

# MIKMODAPI extern BOOL   MikMod_Active(void);
MikMod_Active = _mikmod_lib.MikMod_Active
MikMod_Active.argtypes = []
MikMod_Active.restype = BOOL

# MIKMODAPI extern BOOL   MikMod_EnableOutput(void);
MikMod_EnableOutput = _mikmod_lib.MikMod_EnableOutput
MikMod_EnableOutput.argtypes = []
MikMod_EnableOutput.restype = BOOL

# MIKMODAPI extern void   MikMod_DisableOutput(void);
MikMod_DisableOutput = _mikmod_lib.MikMod_DisableOutput
MikMod_DisableOutput.argtypes = []
MikMod_DisableOutput.restype = None

# MIKMODAPI extern void   MikMod_Update(void);
MikMod_Update = _mikmod_lib.MikMod_Update
MikMod_Update.argtypes = []
MikMod_Update.restype = None


# MIKMODAPI extern BOOL   MikMod_InitThreads(void);
MikMod_InitThreads = _mikmod_lib.MikMod_InitThreads
MikMod_InitThreads.argtypes = []
MikMod_InitThreads.restype = BOOL

# MIKMODAPI extern void   MikMod_Lock(void);
MikMod_Lock = _mikmod_lib.MikMod_Lock
MikMod_Lock.argtypes = []
MikMod_Lock.restype = None

# MIKMODAPI extern void   MikMod_Unlock(void);
MikMod_Unlock = _mikmod_lib.MikMod_Unlock
MikMod_Unlock.argtypes = []
MikMod_Unlock.restype = None


# /*
# *	========== Reader, Writer
# */

# typedef struct MREADER {
class MREADER(ctypes.Structure):
    pass


MREADER._fields_ = [
    (
        "Seek",
        ctypes.CFUNCTYPE(BOOL, ctypes.POINTER(MREADER), ctypes.c_long, ctypes.c_int),
    ),
    ("Tell", ctypes.CFUNCTYPE(ctypes.c_long, ctypes.POINTER(MREADER))),
    (
        "Read",
        ctypes.CFUNCTYPE(
            BOOL, ctypes.POINTER(MREADER), ctypes.c_void_p, ctypes.c_size_t
        ),
    ),
    ("Get", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(MREADER))),
    ("Eof", ctypes.CFUNCTYPE(BOOL, ctypes.POINTER(MREADER))),
]


class MWRITER(ctypes.Structure):
    pass


MWRITER._fields_ = [
    (
        "Seek",
        ctypes.CFUNCTYPE(BOOL, ctypes.POINTER(MWRITER), ctypes.c_long, ctypes.c_int),
    ),
    ("Tell", ctypes.CFUNCTYPE(ctypes.c_long, ctypes.POINTER(MWRITER))),
    (
        "Write",
        ctypes.CFUNCTYPE(
            BOOL, ctypes.POINTER(MWRITER), ctypes.c_void_p, ctypes.c_size_t
        ),
    ),
    ("Put", ctypes.CFUNCTYPE(BOOL, ctypes.POINTER(MWRITER), ctypes.c_int)),
]

# /*
# *	========== Samples
# */

# /* Sample playback should not be interrupted */
SFX_CRITICAL = 1

# /* Sample format [loading and in-memory] flags: */
SF_16BITS = 0x0001
SF_STEREO = 0x0002
SF_SIGNED = 0x0004
SF_BIG_ENDIAN = 0x0008
SF_DELTA = 0x0010
SF_ITPACKED = 0x0020

SF_FORMATMASK = 0x003F

# /* General Playback flags */

SF_LOOP = 0x0100
SF_BIDI = 0x0200
SF_REVERSE = 0x0400
SF_SUSTAIN = 0x0800

SF_PLAYBACKMASK = 0x0C00

# /* Module-only Playback Flags */

SF_OWNPAN = 0x1000
SF_UST_LOOP = 0x2000

SF_EXTRAPLAYBACKMASK = 0x3000

# /* Panning constants */
PAN_LEFT = 0
PAN_HALFLEFT = 64
PAN_CENTER = 128
PAN_HALFRIGHT = 192
PAN_RIGHT = 255
PAN_SURROUND = 512  # /* panning value for Dolby Surround */


class _SAMPLE(ctypes.Structure):
    _fields_ = [
        ("panning", SWORD),  # panning (0-255 or PAN_SURROUND)
        ("speed", ULONG),  # Base playing speed/frequency of note
        ("volume", UBYTE),  # volume 0-64
        ("inflags", SWORD),  # sample format on disk
        ("flags", SWORD),  # sample format in memory
        ("length", ULONG),  # length of sample (in samples!)
        # repeat position (relative to start, in samples)
        ("loopstart", ULONG),
        ("loopend", ULONG),  # repeat end
        # sustain loop begin (in samples) \  Not Supported
        ("susbegin", ULONG),
        # sustain loop end                /      Yet!
        ("susend", ULONG),
        # Variables used by the module player only! (ignored for sound effects)
        ("globvol", UBYTE),  # global volume
        ("vibflags", UBYTE),  # autovibrato flag stuffs
        # Vibratos moved from INSTRUMENT to SAMPLE
        ("vibtype", UBYTE),
        ("vibsweep", UBYTE),
        ("vibdepth", UBYTE),
        ("vibrate", UBYTE),
        ("samplename", CHAR),  # name of the sample
        # Values used internally only
        ("avibpos", UWORD),  # autovibrato pos [player use]
        # for sample scaling, maintains proper period slides
        ("divfactor", UBYTE),
        ("seekpos", ULONG),  # seek position in file
        # sample handle used by individual drivers
        ("handle", SWORD),
        ("onfree", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
        ("ctx", ctypes.c_void_p),
    ]


SAMPLE = _SAMPLE


class FILE(ctypes.Structure):
    _fields_ = []


# /* Sample functions */


# MIKMODAPI extern SAMPLE *Sample_Load(CHAR*);
Sample_Load = _mikmod_lib.Sample_Load
Sample_Load.argtypes = [CHAR]
Sample_Load.restype = ctypes.POINTER(SAMPLE)

# MIKMODAPI extern SAMPLE *Sample_LoadFP(FILE*);
Sample_LoadFP = _mikmod_lib.Sample_LoadFP
Sample_LoadFP.argtypes = [ctypes.POINTER(FILE)]
Sample_LoadFP.restype = ctypes.POINTER(SAMPLE)

# MIKMODAPI extern SAMPLE *Sample_LoadGeneric(MREADER*);
Sample_LoadGeneric = _mikmod_lib.Sample_LoadGeneric
Sample_LoadGeneric.argtypes = [ctypes.POINTER(MREADER)]
Sample_LoadGeneric.restype = ctypes.POINTER(SAMPLE)

# MIKMODAPI extern void   Sample_Free(SAMPLE*);
Sample_Free = _mikmod_lib.Sample_Free
Sample_Free.argtypes = [ctypes.POINTER(SAMPLE)]
Sample_Free.restype = None

# MIKMODAPI extern SBYTE  Sample_Play(SAMPLE*,ULONG,UBYTE);
Sample_Play = _mikmod_lib.Sample_Play
Sample_Play.argtypes = [ctypes.POINTER(SAMPLE), ULONG, UBYTE]
Sample_Play.restype = SBYTE


# MIKMODAPI extern void   Voice_SetVolume(SBYTE,UWORD);
Voice_SetVolume = _mikmod_lib.Voice_SetVolume
Voice_SetVolume.argtypes = [SBYTE, UWORD]
Voice_SetVolume.restype = None

# MIKMODAPI extern UWORD  Voice_GetVolume(SBYTE);
Voice_GetVolume = _mikmod_lib.Voice_GetVolume
Voice_GetVolume.argtypes = [SBYTE]
Voice_GetVolume.restype = UWORD

# MIKMODAPI extern void   Voice_SetFrequency(SBYTE,ULONG);
Voice_SetFrequency = _mikmod_lib.Voice_SetFrequency
Voice_SetFrequency.argtypes = [SBYTE, ULONG]
Voice_SetFrequency.restype = None

# MIKMODAPI extern ULONG  Voice_GetFrequency(SBYTE);
Voice_GetFrequency = _mikmod_lib.Voice_GetFrequency
Voice_GetFrequency.argtypes = [SBYTE]
Voice_GetFrequency.restype = ULONG

# MIKMODAPI extern void   Voice_SetPanning(SBYTE,ULONG);
Voice_SetPanning = _mikmod_lib.Voice_SetPanning
Voice_SetPanning.argtypes = [SBYTE, ULONG]
Voice_SetPanning.restype = None

# MIKMODAPI extern ULONG  Voice_GetPanning(SBYTE);
Voice_GetPanning = _mikmod_lib.Voice_GetPanning
Voice_GetPanning.argtypes = [SBYTE]
Voice_GetPanning.restype = ULONG

# MIKMODAPI extern void   Voice_Play(SBYTE,SAMPLE*,ULONG);
Voice_Play = _mikmod_lib.Voice_Play
Voice_Play.argtypes = [SBYTE, ctypes.POINTER(SAMPLE), ULONG]
Voice_Play.restype = None

# MIKMODAPI extern void   Voice_Stop(SBYTE);
Voice_Stop = _mikmod_lib.Voice_Stop
Voice_Stop.argtypes = [SBYTE]
Voice_Stop.restype = None

# MIKMODAPI extern BOOL   Voice_Stopped(SBYTE);
Voice_Stopped = _mikmod_lib.Voice_Stopped
Voice_Stopped.argtypes = [SBYTE]
Voice_Stopped.restype = BOOL

# MIKMODAPI extern SLONG  Voice_GetPosition(SBYTE);
Voice_GetPosition = _mikmod_lib.Voice_GetPosition
Voice_GetPosition.argtypes = [SBYTE]
Voice_GetPosition.restype = SLONG

# MIKMODAPI extern ULONG  Voice_RealVolume(SBYTE);
Voice_RealVolume = _mikmod_lib.Voice_RealVolume
Voice_RealVolume.argtypes = [SBYTE]
Voice_RealVolume.restype = ULONG


# /*
# *	========== Internal module representation (UniMod)
# */

# /*
# Instrument definition - for information only, the only field which may be
# of use in user programs is the name field
# */

# /* Instrument note count */
INSTNOTES = 120

# /* Envelope point */


class _ENVPT(ctypes.Structure):
    _fields_ = [("pos", SWORD), ("val", SWORD)]


ENVPT = _ENVPT

# /* Envelope point count */
ENVPOINTS = 32

# /* Instrument structure */


class _INSTRUMENT(ctypes.Structure):
    _fields_ = [
        ("insname", CHAR),
        ("flags", UBYTE),
        ("samplenumber", UWORD * INSTNOTES),
        ("samplenote", UBYTE * INSTNOTES),
        ("nnatype", UBYTE),
        ("dca", UBYTE),  # duplicate check action
        ("dct", UBYTE),  # duplicate check type
        ("globvol", UBYTE),
        ("volfade", UWORD),
        ("panning", SWORD),  # instrument-based panning var
        ("pitpansep", UBYTE),  # pitch pan separation (0 to 255)
        ("pitpancenter", UBYTE),  # pitch pan center (0 to 119)
        ("rvolver", UBYTE),  # random volume varations (0 - 100%)
        ("rpanver", UBYTE),  # random panning varations (0 - 100%)
        # volume envelope
        ("volflg", UBYTE),  # bit 0: on 1: sustain 2: loop
        ("volpts", UBYTE),
        ("volsusbeg", UBYTE),
        ("volsusend", UBYTE),
        ("volbeg", UBYTE),
        ("volend", UBYTE),
        ("volenv", ENVPT * ENVPOINTS),
        # panning envelope
        ("panflg", UBYTE),  # bit 0: on 1: sustain 2: loop
        ("panpts", UBYTE),
        ("pansusbeg", UBYTE),
        ("pansusend", UBYTE),
        ("panbeg", UBYTE),
        ("panend", UBYTE),
        ("panenv", ENVPT * ENVPOINTS),
        # pitch envelope
        ("pitflg", UBYTE),  # bit 0: on 1: sustain 2: loop
        ("pitpts", UBYTE),
        ("pitsusbeg", UBYTE),
        ("pitsusend", UBYTE),
        ("pitbeg", UBYTE),
        ("pitend", UBYTE),
        ("pitenv", ENVPT * ENVPOINTS),
    ]


INSTRUMENT = _INSTRUMENT


class _MP_CONTROL(ctypes.Structure):
    pass


MP_CONTROL = _MP_CONTROL


class _MP_VOICE(ctypes.Structure):
    pass


MP_VOICE = _MP_VOICE

# /*
# Module definition
# */

# /* maximum master channels supported */
UF_MAXCHAN = 64

# /* Module flags */
UF_XMPERIODS = 0x0001  # /* XM periods / finetuning */
UF_LINEAR = 0x0002  # /* LINEAR periods (UF_XMPERIODS must be set) */
UF_INST = 0x0004  # /* Instruments are used */
UF_NNA = 0x0008  # /* IT: NNA used, set numvoices rather
#  than numchn */
UF_S3MSLIDES = 0x0010  # /* uses old S3M volume slides */
UF_BGSLIDES = 0x0020  # /* continue volume slides in the background */
UF_HIGHBPM = 0x0040  # /* MED: can use >255 bpm */
UF_NOWRAP = 0x0080  # /* XM-type (i.e. illogical) pattern break
#  semantics */
UF_ARPMEM = 0x0100  # /* IT: need arpeggio memory */
UF_FT2QUIRKS = 0x0200  # /* emulate some FT2 replay quirks */
UF_PANNING = 0x0400  # /* module uses panning effects or have
# 		  non-tracker default initial panning */


class _MODULE(ctypes.Structure):
    # general module information
    _fields_ = [
        ("songname", CHAR),  # name of the song
        ("modtype", CHAR),  # string type of module loaded
        ("comment", CHAR),  # module comments
        #
        ("flags", UWORD),  # See module flags above
        ("numchn", UBYTE),  # number of module channels
        # max # voices used for full NNA playback
        ("numvoices", UBYTE),
        # number of positions in this song
        ("numpos", UWORD),
        ("numpat", UWORD),  # number of patterns in this so
        ("numins", UWORD),  # number of instruments
        ("numsmp", UWORD),  # number of samples
        ("instruments", ctypes.POINTER(INSTRUMENT)),  # all instruments
        ("samples", ctypes.POINTER(SAMPLE)),  # all samples
        ("realchn", UBYTE),  # real number of channels used
        # total number of channels used (incl NNAs)
        ("totalchn", UBYTE),
        # playback settings
        ("reppos", UWORD),  # restart position
        ("initspeed", UBYTE),  # initial song speed
        ("inittempo", UWORD),  # initial song tempo
        # initial global volume (0 - 128)
        ("initvolume", UBYTE),
        ("panning", UWORD * UF_MAXCHAN),  # panning positions
        ("chanvol", UBYTE * UF_MAXCHAN),  # channel positions
        ("bpm", UWORD),  # current beats-per-minute speed
        ("sngspd", UWORD),  # current song speed
        # song volume (0-128) (or user volume)
        ("volume", SWORD),
        # extended speed flag (default enabled)
        ("extspd", BOOL),
        # panning flag (default enabled)
        ("panflag", BOOL),
        # wrap module ? (default disabled)
        ("wrap", BOOL),
        # allow module to loop ? (default enabled)
        ("loop", BOOL),
        # volume fade out during last pattern
        ("fadeout", BOOL),
        ("patpos", UWORD),  # current row number
        ("sngpos", SWORD),  # current song position
        # current song time in 2^-10 seconds
        ("sngtime", ULONG),
        ("relspd", SWORD),  # relative speed factor
        # internal module representation
        ("numtrk", UWORD),  # number of tracks
        # array of numtrk pointers to tracks
        ("tracks", ctypes.POINTER(ctypes.POINTER(UBYTE))),
        ("patterns", ctypes.POINTER(UWORD)),  # array of Patterns
        # array of number of rows for each pattern
        ("pattrows", ctypes.POINTER(UWORD)),
        ("positions", ctypes.POINTER(UWORD)),  # all positions
        ("forbid", BOOL),  # if true, no player update!
        # number of rows on current pattern
        ("numrow", UWORD),
        # tick counter (counts from 0 to sngspd)
        ("vbtick", UWORD),
        # used for song time computation
        ("sngremainder", UWORD),
        # Effects Channel info (size pf->numchn)
        ("control", ctypes.POINTER(MP_CONTROL)),
        # Audio Voice information (size md_numchn)
        ("voice", ctypes.POINTER(MP_VOICE)),
        ("globalslide", UBYTE),  # global volume slide rate
        # module has just looped to position -1
        ("pat_repcrazy", UBYTE),
        # position where to start a new pattern
        ("patbrk", UWORD),
        # patterndelay counter (command memory)
        ("patdly", UBYTE),
        # patterndelay counter (real one)
        ("patdly2", UBYTE),
        # flag to indicate a jump is needed...
        ("posjmp", SWORD),
        # threshold to detect bpm or speed values
        ("bmplimit", UWORD),
    ]


MODULE = _MODULE

# /*
# *	========== Module loaders
# */

# struct MLOADER;


class MLOADER(ctypes.Structure):
    pass


# MIKMODAPI extern CHAR*   MikMod_InfoLoader(void);
MikMod_InfoLoader = _mikmod_lib.MikMod_InfoLoader
MikMod_InfoLoader.argtypes = []
MikMod_InfoLoader.restype = CHAR

# MIKMODAPI extern void    MikMod_RegisterAllLoaders(void);
MikMod_RegisterAllLoaders = _mikmod_lib.MikMod_RegisterAllLoaders
MikMod_RegisterAllLoaders.argtypes = []
MikMod_RegisterAllLoaders.restype = None

# MIKMODAPI extern void    MikMod_RegisterLoader(struct MLOADER*);
MikMod_RegisterLoader = _mikmod_lib.MikMod_RegisterLoader
MikMod_RegisterLoader.argtypes = [ctypes.POINTER(MLOADER)]
MikMod_RegisterLoader.restype = None

# MIKMODAPI extern struct MLOADER load_669; /* 669 and Extended-669 (by Tran/Renaissance) */
load_669 = MLOADER.in_dll(_mikmod_lib, "load_669")
# MIKMODAPI extern struct MLOADER load_amf; /* DMP Advanced Module Format (by Otto Chrons) */
load_amf = MLOADER.in_dll(_mikmod_lib, "load_amf")
# MIKMODAPI extern struct MLOADER load_dsm; /* DSIK internal module format */
load_dsm = MLOADER.in_dll(_mikmod_lib, "load_dsm")
# MIKMODAPI extern struct MLOADER load_far; /* Farandole Composer (by Daniel Potter) */
load_far = MLOADER.in_dll(_mikmod_lib, "load_far")
# MIKMODAPI extern struct MLOADER load_gdm; /* General DigiMusic (by Edward Schlunder) */
load_gdm = MLOADER.in_dll(_mikmod_lib, "load_gdm")
# MIKMODAPI extern struct MLOADER load_it;  /* Impulse Tracker (by Jeffrey Lim) */
load_it = MLOADER.in_dll(_mikmod_lib, "load_it")
# MIKMODAPI extern struct MLOADER load_imf; /* Imago Orpheus (by Lutz Roeder) */
load_imf = MLOADER.in_dll(_mikmod_lib, "load_imf")
# MIKMODAPI extern struct MLOADER load_med; /* Amiga MED modules (by Teijo Kinnunen) */
load_med = MLOADER.in_dll(_mikmod_lib, "load_med")
# MIKMODAPI extern struct MLOADER load_m15; /* Soundtracker 15-instrument */
load_m15 = MLOADER.in_dll(_mikmod_lib, "load_m15")
# MIKMODAPI extern struct MLOADER load_mod; /* Standard 31-instrument Module loader */
load_mod = MLOADER.in_dll(_mikmod_lib, "load_mod")
# MIKMODAPI extern struct MLOADER load_mtm; /* Multi-Tracker Module (by Renaissance) */
load_mtm = MLOADER.in_dll(_mikmod_lib, "load_mtm")
# MIKMODAPI extern struct MLOADER load_okt; /* Amiga Oktalyzer */
load_okt = MLOADER.in_dll(_mikmod_lib, "load_okt")
# MIKMODAPI extern struct MLOADER load_stm; /* ScreamTracker 2 (by Future Crew) */
load_stm = MLOADER.in_dll(_mikmod_lib, "load_stm")
# MIKMODAPI extern struct MLOADER load_stx; /* STMIK 0.2 (by Future Crew) */
load_stx = MLOADER.in_dll(_mikmod_lib, "load_stx")
# MIKMODAPI extern struct MLOADER load_s3m; /* ScreamTracker 3 (by Future Crew) */
load_s3m = MLOADER.in_dll(_mikmod_lib, "load_s3m")
# MIKMODAPI extern struct MLOADER load_ult; /* UltraTracker (by MAS) */
load_ult = MLOADER.in_dll(_mikmod_lib, "load_ult")
# MIKMODAPI extern struct MLOADER load_uni; /* MikMod and APlayer internal module format */
load_uni = MLOADER.in_dll(_mikmod_lib, "load_uni")
# MIKMODAPI extern struct MLOADER load_xm;  /* FastTracker 2 (by Triton) */
load_xm = MLOADER.in_dll(_mikmod_lib, "load_xm")

# /*
# *	========== Module player
# */

# MIKMODAPI extern MODULE* Player_Load(CHAR*,int,BOOL);
Player_Load = _mikmod_lib.Player_Load
Player_Load.argtypes = [CHAR, ctypes.c_int, BOOL]
Player_Load.restype = ctypes.POINTER(MODULE)

# MIKMODAPI extern MODULE* Player_LoadFP(FILE*,int,BOOL);
Player_LoadFP = _mikmod_lib.Player_LoadFP
Player_LoadFP.argtypes = [ctypes.POINTER(FILE), ctypes.c_int, BOOL]
Player_LoadFP.restype = ctypes.POINTER(MODULE)

# MIKMODAPI extern MODULE* Player_LoadGeneric(MREADER*,int,BOOL);
Player_LoadGeneric = _mikmod_lib.Player_LoadGeneric
Player_LoadGeneric.argtypes = [ctypes.POINTER(MREADER), ctypes.c_int, BOOL]
Player_LoadGeneric.restype = ctypes.POINTER(MODULE)

# MIKMODAPI extern CHAR*   Player_LoadTitle(CHAR*);
Player_LoadTitle = _mikmod_lib.Player_LoadTitle
Player_LoadTitle.argtypes = [CHAR]
Player_LoadTitle.restype = CHAR

# MIKMODAPI extern CHAR*   Player_LoadTitleFP(FILE*);
Player_LoadTitleFP = _mikmod_lib.Player_LoadTitleFP
Player_LoadTitleFP.argtypes = [ctypes.POINTER(FILE)]
Player_LoadTitleFP.restype = CHAR

# MIKMODAPI extern void    Player_Free(MODULE*);
Player_Free = _mikmod_lib.Player_Free
Player_Free.argtypes = [ctypes.POINTER(MODULE)]
Player_Free.restype = None

# MIKMODAPI extern void    Player_Start(MODULE*);
Player_Start = _mikmod_lib.Player_Start
Player_Start.argtypes = [ctypes.POINTER(MODULE)]
Player_Start.restype = None

# MIKMODAPI extern BOOL    Player_Active(void);
Player_Active = _mikmod_lib.Player_Active
Player_Active.argtypes = []
Player_Active.restype = BOOL

# MIKMODAPI extern void    Player_Stop(void);
Player_Stop = _mikmod_lib.Player_Stop
Player_Stop.argtypes = []
Player_Stop.restype = None

# MIKMODAPI extern void    Player_TogglePause(void);
Player_TogglePause = _mikmod_lib.Player_TogglePause
Player_TogglePause.argtypes = []
Player_TogglePause.restype = None

# MIKMODAPI extern BOOL    Player_Paused(void);
Player_Paused = _mikmod_lib.Player_Paused
Player_Paused.argtypes = []
Player_Paused.restype = BOOL

# MIKMODAPI extern void    Player_NextPosition(void);
Player_NextPosition = _mikmod_lib.Player_NextPosition
Player_NextPosition.argtypes = []
Player_NextPosition.restype = None

# MIKMODAPI extern void    Player_PrevPosition(void);
Player_PrevPosition = _mikmod_lib.Player_PrevPosition
Player_PrevPosition.argtypes = []
Player_PrevPosition.restype = None

# MIKMODAPI extern void    Player_SetPosition(UWORD);
Player_SetPosition = _mikmod_lib.Player_SetPosition
Player_SetPosition.argtypes = [UWORD]
Player_SetPosition.restype = None

# MIKMODAPI extern BOOL    Player_Muted(UBYTE);
Player_Muted = _mikmod_lib.Player_Muted
Player_Muted.argtypes = [UBYTE]
Player_Muted.restype = BOOL

# MIKMODAPI extern void    Player_SetVolume(SWORD);
Player_SetVolume = _mikmod_lib.Player_SetVolume
Player_SetVolume.argtypes = [SWORD]
Player_SetVolume.restype = None

# MIKMODAPI extern MODULE* Player_GetModule(void);
Player_GetModule = _mikmod_lib.Player_GetModule
Player_GetModule.argtypes = []
Player_GetModule.restype = ctypes.POINTER(MODULE)

# MIKMODAPI extern void    Player_SetSpeed(UWORD);
Player_SetSpeed = _mikmod_lib.Player_SetSpeed
Player_SetSpeed.argtypes = [UWORD]
Player_SetSpeed.restype = None

# MIKMODAPI extern void    Player_SetTempo(UWORD);
Player_SetTempo = _mikmod_lib.Player_SetTempo
Player_SetTempo.argtypes = [UWORD]
Player_SetTempo.restype = None

# MIKMODAPI extern void    Player_Unmute(SLONG,...);
Player_Unmute = _mikmod_lib.Player_Unmute
Player_Unmute.argtypes = [SLONG]
Player_Unmute.restype = None

# MIKMODAPI extern void    Player_Mute(SLONG,...);
Player_Mute = _mikmod_lib.Player_Mute
Player_Mute.argtypes = [SLONG]
Player_Mute.restype = None

# MIKMODAPI extern void    Player_ToggleMute(SLONG,...);
Player_ToggleMute = _mikmod_lib.Player_ToggleMute
Player_ToggleMute.argtypes = [SLONG]
Player_ToggleMute.restype = None

# MIKMODAPI extern int     Player_GetChannelVoice(UBYTE);
Player_GetChannelVoice = _mikmod_lib.Player_GetChannelVoice
Player_GetChannelVoice.argtypes = [UBYTE]
Player_GetChannelVoice.restype = ctypes.c_int

# MIKMODAPI extern UWORD   Player_GetChannelPeriod(UBYTE);
Player_GetChannelPeriod = _mikmod_lib.Player_GetChannelPeriod
Player_GetChannelPeriod.argtypes = [UBYTE]
Player_GetChannelPeriod.restype = UWORD


# typedef void (MikMod_player)(void);
MikMod_player = ctypes.CFUNCTYPE(None)
# typedef MikMod_player *MikMod_player_t;
MikMod_player_t = ctypes.POINTER(MikMod_player)

# MIKMODAPI extern MikMod_player_t MikMod_RegisterPlayer(MikMod_player_t);
MikMod_RegisterPlayer = _mikmod_lib.MikMod_RegisterPlayer
MikMod_RegisterPlayer.argtypes = [MikMod_player_t]
MikMod_RegisterPlayer.restype = MikMod_player_t


MUTE_EXCLUSIVE = 32000
MUTE_INCLUSIVE = 32001

# /*
# *	========== Drivers
# */

MD_MUSIC = 0
MD_SNDFX = 1

MD_HARDWARE = 0
MD_SOFTWARE = 1


# /* Mixing flags */

# /* These ones take effect only after MikMod_Init or MikMod_Reset */
DMODE_16BITS = 0x0001  # /* enable 16 bit output */
DMODE_STEREO = 0x0002  # /* enable stereo output */
DMODE_SOFT_SNDFX = 0x0004  # /* Process sound effects via software mixer */
DMODE_SOFT_MUSIC = 0x0008  # /* Process music via software mixer */
DMODE_HQMIXER = 0x0010  # /* Use high-quality (slower) software mixer */
# /* These take effect immediately. */
DMODE_SURROUND = 0x0100  # /* enable surround sound */
DMODE_INTERP = 0x0200  # /* enable interpolation */
DMODE_REVERSE = 0x0400  # /* reverse stereo */

# struct SAMPLOAD;


class SAMPLOAD(ctypes.Structure):
    pass


MDRIVER._fields_ = [
    ("next", ctypes.POINTER(MDRIVER)),
    ("Name", CHAR),
    ("Version", CHAR),
    ("HardVoiceLimit", UBYTE),
    ("SoftVoiceLimit", UBYTE),
    ("Alias", CHAR),
    ("CmdLineHelp", CHAR),
    ("CommandLine", ctypes.CFUNCTYPE(None, CHAR)),
    ("IsPresent", ctypes.CFUNCTYPE(BOOL)),
    ("SampleLoad", ctypes.CFUNCTYPE(SWORD, ctypes.POINTER(SAMPLOAD), ctypes.c_int)),
    ("SampleUnload", ctypes.CFUNCTYPE(None, SWORD)),
    ("FreeSampleSpace", ctypes.CFUNCTYPE(ULONG, ctypes.c_int)),
    ("RealSampleLength", ctypes.CFUNCTYPE(ULONG, ctypes.c_int, ctypes.POINTER(SAMPLE))),
    ("Init", ctypes.CFUNCTYPE(ctypes.c_int)),
    ("Exit", ctypes.CFUNCTYPE(None)),
    ("Reset", ctypes.CFUNCTYPE(ctypes.c_int)),
    ("SetNumVoices", ctypes.CFUNCTYPE(ctypes.c_int)),
    ("PlayStart", ctypes.CFUNCTYPE(ctypes.c_int)),
    ("PlayStop", ctypes.CFUNCTYPE(None)),
    ("Update", ctypes.CFUNCTYPE(None)),
    ("Pause", ctypes.CFUNCTYPE(None)),
    ("VoiceSetVolume", ctypes.CFUNCTYPE(None, UBYTE, UWORD)),
    ("VoiceGetVolume", ctypes.CFUNCTYPE(UWORD, UBYTE)),
    ("VoiceSetFrequency", ctypes.CFUNCTYPE(None, UBYTE, ULONG)),
    ("VoiceGetFrequency", ctypes.CFUNCTYPE(ULONG, UBYTE)),
    ("VoiceSetPanning", ctypes.CFUNCTYPE(None, UBYTE, ULONG)),
    ("VoiceGetPanning", ctypes.CFUNCTYPE(ULONG, UBYTE)),
    (
        "VoicePlay",
        ctypes.CFUNCTYPE(None, UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD),
    ),
    ("VoiceStop", ctypes.CFUNCTYPE(None, UBYTE)),
    ("VoiceStopped", ctypes.CFUNCTYPE(BOOL, UBYTE)),
    ("VoiceGetPosition", ctypes.CFUNCTYPE(SLONG, UBYTE)),
    ("VoiceRealVolume", ctypes.CFUNCTYPE(ULONG, UBYTE)),
]

# /* These variables can be changed at ANY time and results will be immediate */
# MIKMODAPI extern UBYTE md_volume;      /* global sound volume (0-128) */
md_volume = UBYTE.in_dll(_mikmod_lib, "md_volume")
# MIKMODAPI extern UBYTE md_musicvolume; /* volume of song */
md_musicvolume = UBYTE.in_dll(_mikmod_lib, "md_musicvolume")
# MIKMODAPI extern UBYTE md_sndfxvolume; /* volume of sound effects */
md_sndfxvolume = UBYTE.in_dll(_mikmod_lib, "md_sndfxvolume")
# MIKMODAPI extern UBYTE md_reverb;      /* 0 = none;  15 = chaos */
md_reverb = UBYTE.in_dll(_mikmod_lib, "md_reverb")
# MIKMODAPI extern UBYTE md_pansep;      /* 0 = mono;  128 == 100% (full left/right) */
md_pansep = UBYTE.in_dll(_mikmod_lib, "md_pansep")

# /* The variables below can be changed at any time, but changes will not be
# implemented until MikMod_Reset is called. A call to MikMod_Reset may result
# in a skip or pop in audio (depending on the soundcard driver and the settings
# changed). */
# MIKMODAPI extern UWORD md_device;      /* device */
md_device = UWORD.in_dll(_mikmod_lib, "md_device")
# MIKMODAPI extern UWORD md_mixfreq;     /* mixing frequency */
md_mixfreq = UWORD.in_dll(_mikmod_lib, "md_mixfreq")
# MIKMODAPI extern UWORD md_mode;        /* mode. See DMODE_? flags above */
md_mode = UWORD.in_dll(_mikmod_lib, "md_mode")

# /* The following variable should not be changed! */
# MIKMODAPI extern MDRIVER* md_driver;   /* Current driver in use. */
md_driver = ctypes.POINTER(MDRIVER).in_dll(_mikmod_lib, "md_driver")

# /* Known drivers list */

# MIKMODAPI extern struct MDRIVER drv_nos;    /* no sound */
drv_nos = MDRIVER.in_dll(_mikmod_lib, "drv_nos")
# MIKMODAPI extern struct MDRIVER drv_pipe;   /* piped output */
drv_pipe = MDRIVER.in_dll(_mikmod_lib, "drv_pipe")
# MIKMODAPI extern struct MDRIVER drv_raw;    /* raw file disk writer [music.raw] */
drv_raw = MDRIVER.in_dll(_mikmod_lib, "drv_raw")
# MIKMODAPI extern struct MDRIVER drv_stdout; /* output to stdout */
drv_stdout = MDRIVER.in_dll(_mikmod_lib, "drv_stdout")
# MIKMODAPI extern struct MDRIVER drv_wav;    /* RIFF WAVE file disk writer [music.wav] */
drv_wav = MDRIVER.in_dll(_mikmod_lib, "drv_wav")

# MIKMODAPI extern struct MDRIVER drv_ultra;  /* Linux Ultrasound driver */
drv_ultra = MDRIVER.in_dll(_mikmod_lib, "drv_ultra")
# MIKMODAPI extern struct MDRIVER drv_sam9407;	/* Linux sam9407 driver */
drv_sam9407 = MDRIVER.in_dll(_mikmod_lib, "drv_sam9407")

# MIKMODAPI extern struct MDRIVER drv_AF;     /* Dec Alpha AudioFile */
drv_AF = MDRIVER.in_dll(_mikmod_lib, "drv_AF")
# MIKMODAPI extern struct MDRIVER drv_aix;    /* AIX audio device */
drv_aix = MDRIVER.in_dll(_mikmod_lib, "drv_aix")
# MIKMODAPI extern struct MDRIVER drv_alsa;   /* Advanced Linux Sound Architecture (ALSA) */
drv_alsa = MDRIVER.in_dll(_mikmod_lib, "drv_alsa")
# MIKMODAPI extern struct MDRIVER drv_esd;    /* Enlightened sound daemon (EsounD) */
drv_esd = MDRIVER.in_dll(_mikmod_lib, "drv_esd")
# MIKMODAPI extern struct MDRIVER drv_hp;     /* HP-UX audio device */
drv_hp = MDRIVER.in_dll(_mikmod_lib, "drv_hp")
# MIKMODAPI extern struct MDRIVER drv_oss;    /* OpenSound System (Linux,FreeBSD...) */
drv_oss = MDRIVER.in_dll(_mikmod_lib, "drv_oss")
# MIKMODAPI extern struct MDRIVER drv_sgi;    /* SGI audio library */
drv_sgi = MDRIVER.in_dll(_mikmod_lib, "drv_sgi")
# MIKMODAPI extern struct MDRIVER drv_sun;    /* Sun/NetBSD/OpenBSD audio device */
drv_sun = MDRIVER.in_dll(_mikmod_lib, "drv_sun")

# MIKMODAPI extern struct MDRIVER drv_dart;   /* OS/2 Direct Audio RealTime */
# drv_dart = MDRIVER.in_dll(_mikmod_lib, 'drv_dart')
if sys.platform == "os2":
    # MIKMODAPI extern struct MDRIVER drv_os2;    /* OS/2 MMPM/2 */
    drv_os2 = MDRIVER.in_dll(_mikmod_lib, "drv_os2")

# MIKMODAPI extern struct MDRIVER drv_ds;     /* Win32 DirectSound driver */
# drv_ds = MDRIVER.in_dll(_mikmod_lib, 'drv_ds')
if sys.platform == "win32":
    # MIKMODAPI extern struct MDRIVER drv_win;    /* Win32 multimedia API driver */
    drv_win = MDRIVER.in_dll(_mikmod_lib, "drv_win")

if sys.platform == "darwin":
    # MIKMODAPI extern struct MDRIVER drv_mac;    /* Macintosh Sound Manager driver */
    drv_mac = MDRIVER.in_dll(_mikmod_lib, "drv_mac")

# /*========== Virtual channel mixer interface (for user-supplied drivers only) */

# MIKMODAPI extern BOOL  VC_Init(void);
VC_Init = _mikmod_lib.VC_Init
VC_Init.argtypes = []
VC_Init.restype = BOOL

# MIKMODAPI extern void  VC_Exit(void);
VC_Exit = _mikmod_lib.VC_Exit
VC_Exit.argtypes = []
VC_Exit.restype = None

# MIKMODAPI extern BOOL  VC_SetNumVoices(void);
VC_SetNumVoices = _mikmod_lib.VC_SetNumVoices
VC_SetNumVoices.argtypes = []
VC_SetNumVoices.restype = BOOL

# MIKMODAPI extern ULONG VC_SampleSpace(int);
VC_SampleSpace = _mikmod_lib.VC_SampleSpace
VC_SampleSpace.argtypes = [ctypes.c_int]
VC_SampleSpace.restype = ULONG

# MIKMODAPI extern ULONG VC_SampleLength(int,SAMPLE*);
VC_SampleLength = _mikmod_lib.VC_SampleLength
VC_SampleLength.argtypes = [ctypes.c_int, ctypes.POINTER(SAMPLE)]
VC_SampleLength.restype = ULONG


# MIKMODAPI extern BOOL  VC_PlayStart(void);
VC_PlayStart = _mikmod_lib.VC_PlayStart
VC_PlayStart.argtypes = []
VC_PlayStart.restype = BOOL

# MIKMODAPI extern void  VC_PlayStop(void);
VC_PlayStop = _mikmod_lib.VC_PlayStop
VC_PlayStop.argtypes = []
VC_PlayStop.restype = None


# MIKMODAPI extern SWORD VC_SampleLoad(struct SAMPLOAD*,int);
VC_SampleLoad = _mikmod_lib.VC_SampleLoad
VC_SampleLoad.argtypes = [ctypes.POINTER(SAMPLOAD), ctypes.c_int]
VC_SampleLoad.restype = SWORD

# MIKMODAPI extern void  VC_SampleUnload(SWORD);
VC_SampleUnload = _mikmod_lib.VC_SampleUnload
VC_SampleUnload.argtypes = [SWORD]
VC_SampleUnload.restype = None


# MIKMODAPI extern ULONG VC_WriteBytes(SBYTE*,ULONG);
VC_WriteBytes = _mikmod_lib.VC_WriteBytes
VC_WriteBytes.argtypes = [ctypes.POINTER(SBYTE), ULONG]
VC_WriteBytes.restype = ULONG
VC_WriteBytes = _mikmod_lib.VC_WriteBytes
VC_WriteBytes.restype = ULONG
VC_WriteBytes.argtypes = [ctypes.POINTER(SBYTE), ULONG]

# MIKMODAPI extern ULONG VC_SilenceBytes(SBYTE*,ULONG);
VC_SilenceBytes = _mikmod_lib.VC_SilenceBytes
VC_SilenceBytes.argtypes = [ctypes.POINTER(SBYTE), ULONG]
VC_SilenceBytes.restype = ULONG


# MIKMODAPI extern void  VC_VoiceSetVolume(UBYTE,UWORD);
VC_VoiceSetVolume = _mikmod_lib.VC_VoiceSetVolume
VC_VoiceSetVolume.argtypes = [UBYTE, UWORD]
VC_VoiceSetVolume.restype = None

# MIKMODAPI extern UWORD VC_VoiceGetVolume(UBYTE);
VC_VoiceGetVolume = _mikmod_lib.VC_VoiceGetVolume
VC_VoiceGetVolume.argtypes = [UBYTE]
VC_VoiceGetVolume.restype = UWORD

# MIKMODAPI extern void  VC_VoiceSetFrequency(UBYTE,ULONG);
VC_VoiceSetFrequency = _mikmod_lib.VC_VoiceSetFrequency
VC_VoiceSetFrequency.argtypes = [UBYTE, ULONG]
VC_VoiceSetFrequency.restype = None

# MIKMODAPI extern ULONG VC_VoiceGetFrequency(UBYTE);
VC_VoiceGetFrequency = _mikmod_lib.VC_VoiceGetFrequency
VC_VoiceGetFrequency.argtypes = [UBYTE]
VC_VoiceGetFrequency.restype = ULONG

# MIKMODAPI extern void  VC_VoiceSetPanning(UBYTE,ULONG);
VC_VoiceSetPanning = _mikmod_lib.VC_VoiceSetPanning
VC_VoiceSetPanning.argtypes = [UBYTE, ULONG]
VC_VoiceSetPanning.restype = None

# MIKMODAPI extern ULONG VC_VoiceGetPanning(UBYTE);
VC_VoiceGetPanning = _mikmod_lib.VC_VoiceGetPanning
VC_VoiceGetPanning.argtypes = [UBYTE]
VC_VoiceGetPanning.restype = ULONG

# MIKMODAPI extern void  VC_VoicePlay(UBYTE,SWORD,ULONG,ULONG,ULONG,ULONG,UWORD);
VC_VoicePlay = _mikmod_lib.VC_VoicePlay
VC_VoicePlay.argtypes = [UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD]
VC_VoicePlay.restype = None


# MIKMODAPI extern void  VC_VoiceStop(UBYTE);
VC_VoiceStop = _mikmod_lib.VC_VoiceStop
VC_VoiceStop.argtypes = [UBYTE]
VC_VoiceStop.restype = None

# MIKMODAPI extern BOOL  VC_VoiceStopped(UBYTE);
VC_VoiceStopped = _mikmod_lib.VC_VoiceStopped
VC_VoiceStopped.argtypes = [UBYTE]
VC_VoiceStopped.restype = BOOL

# MIKMODAPI extern SLONG VC_VoiceGetPosition(UBYTE);
VC_VoiceGetPosition = _mikmod_lib.VC_VoiceGetPosition
VC_VoiceGetPosition.argtypes = [UBYTE]
VC_VoiceGetPosition.restype = SLONG

# MIKMODAPI extern ULONG VC_VoiceRealVolume(UBYTE);
VC_VoiceRealVolume = _mikmod_lib.VC_VoiceRealVolume
VC_VoiceRealVolume.argtypes = [UBYTE]
VC_VoiceRealVolume.restype = ULONG


# ex:set ts=4:
