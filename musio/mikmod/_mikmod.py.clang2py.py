# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I/usr/lib/clang/12.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


class FunctionFactoryStub:
    def __getattr__(self, _):
        return ctypes.CFUNCTYPE(lambda y: y)


# libraries['FIXME_STUB'] explanation
# As you did not list (-l libraryname.so) a library that exports this function
# This is a non-working stub instead.
# You can either re-run clan2py with -l /path/to/library.so
# Or manually fix this by comment the ctypes.CDLL loading
_libraries = {}
_libraries["FIXME_STUB"] = ctypes.CDLL("/usr/lib/libmikmod.so")
c_int128 = ctypes.c_ubyte * 16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte * 16


def string_cast(char_pointer, encoding="utf-8", errors="strict"):
    value = ctypes.cast(char_pointer, ctypes.c_char_p).value
    if value is not None and encoding is not None:
        value = value.decode(encoding, errors=errors)
    return value


def char_pointer_cast(string, encoding="utf-8"):
    if encoding is not None:
        try:
            string = string.encode(encoding)
        except AttributeError:
            # In Python3, bytes has no encode attribute
            pass
    string = ctypes.c_char_p(string)
    return ctypes.cast(string, ctypes.POINTER(ctypes.c_char))


class AsDictMixin:
    @classmethod
    def as_dict(cls, self):
        result = {}
        if not isinstance(self, AsDictMixin):
            # not a structure, assume it's already a python object
            return self
        if not hasattr(cls, "_fields_"):
            return result
        # sys.version_info >= (3, 5)
        # for (field, *_) in cls._fields_:  # noqa
        for field_tuple in cls._fields_:  # noqa
            field = field_tuple[0]
            if field.startswith("PADDING_"):
                continue
            value = getattr(self, field)
            type_ = type(value)
            if hasattr(value, "_length_") and hasattr(value, "_type_"):
                # array
                if not hasattr(type_, "as_dict"):
                    value = [v for v in value]
                else:
                    type_ = type_._type_
                    value = [type_.as_dict(v) for v in value]
            elif hasattr(value, "contents") and hasattr(value, "_type_"):
                # pointer
                try:
                    if not hasattr(type_, "as_dict"):
                        value = value.contents
                    else:
                        type_ = type_._type_
                        value = type_.as_dict(value.contents)
                except ValueError:
                    # nullptr
                    value = None
            elif isinstance(value, AsDictMixin):
                # other structure
                value = type_.as_dict(value)
            result[field] = value
        return result


class Structure(ctypes.Structure, AsDictMixin):
    def __init__(self, *args, **kwds):
        # We don't want to use positional arguments fill PADDING_* fields

        args = dict(zip(self.__class__._field_names_(), args))
        args.update(kwds)
        super(Structure, self).__init__(**args)

    @classmethod
    def _field_names_(cls):
        if hasattr(cls, "_fields_"):
            return (f[0] for f in cls._fields_ if not f[0].startswith("PADDING"))
        else:
            return ()

    @classmethod
    def get_type(cls, field):
        for f in cls._fields_:
            if f[0] == field:
                return f[1]
        return None

    @classmethod
    def bind(cls, bound_fields):
        fields = {}
        for name, type_ in cls._fields_:
            if hasattr(type_, "restype"):
                if name in bound_fields:
                    if bound_fields[name] is None:
                        fields[name] = type_()
                    else:
                        # use a closure to capture the callback from the loop scope
                        fields[name] = type_(
                            (lambda callback: lambda *args: callback(*args))(
                                bound_fields[name]
                            )
                        )
                    del bound_fields[name]
                else:
                    # default callback implementation (does nothing)
                    try:
                        default_ = type_(0).restype().value
                    except TypeError:
                        default_ = None
                    fields[name] = type_(
                        (lambda default_: lambda *args: default_)(default_)
                    )
            else:
                # not a callback function, use default initialization
                if name in bound_fields:
                    fields[name] = bound_fields[name]
                    del bound_fields[name]
                else:
                    fields[name] = type_()
        if len(bound_fields) != 0:
            raise ValueError(
                "Cannot bind the following unknown callback(s) {}.{}".format(
                    cls.__name__, bound_fields.keys()
                )
            )
        return cls(**fields)


class Union(ctypes.Union, AsDictMixin):
    pass


_MIKMOD_H_ = True  # macro
MIKMODAPI = True  # macro
LIBMIKMOD_VERSION_MAJOR = 3  # macro
LIBMIKMOD_VERSION_MINOR = 3  # macro
LIBMIKMOD_REVISION = 11  # macro
# def LIBMIKMOD_VERSION((3<<16):  # macro
#    return |(3<<8)|(11))
SFX_CRITICAL = 1  # macro
SF_16BITS = 0x0001  # macro
SF_STEREO = 0x0002  # macro
SF_SIGNED = 0x0004  # macro
SF_BIG_ENDIAN = 0x0008  # macro
SF_DELTA = 0x0010  # macro
SF_ITPACKED = 0x0020  # macro
SF_FORMATMASK = 0x003F  # macro
SF_LOOP = 0x0100  # macro
SF_BIDI = 0x0200  # macro
SF_REVERSE = 0x0400  # macro
SF_SUSTAIN = 0x0800  # macro
SF_PLAYBACKMASK = 0x0C00  # macro
SF_OWNPAN = 0x1000  # macro
SF_UST_LOOP = 0x2000  # macro
SF_EXTRAPLAYBACKMASK = 0x3000  # macro
PAN_LEFT = 0  # macro
PAN_HALFLEFT = 64  # macro
PAN_CENTER = 128  # macro
PAN_HALFRIGHT = 192  # macro
PAN_RIGHT = 255  # macro
PAN_SURROUND = 512  # macro
INSTNOTES = 120  # macro
ENVPOINTS = 32  # macro
UF_MAXCHAN = 64  # macro
UF_XMPERIODS = 0x0001  # macro
UF_LINEAR = 0x0002  # macro
UF_INST = 0x0004  # macro
UF_NNA = 0x0008  # macro
UF_S3MSLIDES = 0x0010  # macro
UF_BGSLIDES = 0x0020  # macro
UF_HIGHBPM = 0x0040  # macro
UF_NOWRAP = 0x0080  # macro
UF_ARPMEM = 0x0100  # macro
UF_FT2QUIRKS = 0x0200  # macro
UF_PANNING = 0x0400  # macro
MUTE_EXCLUSIVE = 32000  # macro
MUTE_INCLUSIVE = 32001  # macro
DMODE_16BITS = 0x0001  # macro
DMODE_STEREO = 0x0002  # macro
DMODE_SOFT_SNDFX = 0x0004  # macro
DMODE_SOFT_MUSIC = 0x0008  # macro
DMODE_HQMIXER = 0x0010  # macro
DMODE_FLOAT = 0x0020  # macro
DMODE_SURROUND = 0x0100  # macro
DMODE_INTERP = 0x0200  # macro
DMODE_REVERSE = 0x0400  # macro
DMODE_SIMDMIXER = 0x0800  # macro
DMODE_NOISEREDUCTION = 0x1000  # macro
MikMod_GetVersion = _libraries["FIXME_STUB"].MikMod_GetVersion
MikMod_GetVersion.restype = ctypes.c_int64
MikMod_GetVersion.argtypes = []
CHAR = ctypes.c_char
BOOL = ctypes.c_int32
SBYTE = ctypes.c_byte
UBYTE = ctypes.c_ubyte
SWORD = ctypes.c_int16
UWORD = ctypes.c_uint16
SLONG = ctypes.c_int32
ULONG = ctypes.c_uint32
__mikmod_typetest = ctypes.c_int32 * 1

# values for enumeration 'c__Ea_MMERR_OPENING_FILE'
c__Ea_MMERR_OPENING_FILE__enumvalues = {
    1: "MMERR_OPENING_FILE",
    2: "MMERR_OUT_OF_MEMORY",
    3: "MMERR_DYNAMIC_LINKING",
    4: "MMERR_SAMPLE_TOO_BIG",
    5: "MMERR_OUT_OF_HANDLES",
    6: "MMERR_UNKNOWN_WAVE_TYPE",
    7: "MMERR_LOADING_PATTERN",
    8: "MMERR_LOADING_TRACK",
    9: "MMERR_LOADING_HEADER",
    10: "MMERR_LOADING_SAMPLEINFO",
    11: "MMERR_NOT_A_MODULE",
    12: "MMERR_NOT_A_STREAM",
    13: "MMERR_MED_SYNTHSAMPLES",
    14: "MMERR_ITPACK_INVALID_DATA",
    15: "MMERR_DETECTING_DEVICE",
    16: "MMERR_INVALID_DEVICE",
    17: "MMERR_INITIALIZING_MIXER",
    18: "MMERR_OPENING_AUDIO",
    19: "MMERR_8BIT_ONLY",
    20: "MMERR_16BIT_ONLY",
    21: "MMERR_STEREO_ONLY",
    22: "MMERR_ULAW",
    23: "MMERR_NON_BLOCK",
    24: "MMERR_AF_AUDIO_PORT",
    25: "MMERR_AIX_CONFIG_INIT",
    26: "MMERR_AIX_CONFIG_CONTROL",
    27: "MMERR_AIX_CONFIG_START",
    28: "MMERR_GUS_SETTINGS",
    29: "MMERR_GUS_RESET",
    30: "MMERR_GUS_TIMER",
    31: "MMERR_HP_SETSAMPLESIZE",
    32: "MMERR_HP_SETSPEED",
    33: "MMERR_HP_CHANNELS",
    34: "MMERR_HP_AUDIO_OUTPUT",
    35: "MMERR_HP_AUDIO_DESC",
    36: "MMERR_HP_BUFFERSIZE",
    37: "MMERR_OSS_SETFRAGMENT",
    38: "MMERR_OSS_SETSAMPLESIZE",
    39: "MMERR_OSS_SETSTEREO",
    40: "MMERR_OSS_SETSPEED",
    41: "MMERR_SGI_SPEED",
    42: "MMERR_SGI_16BIT",
    43: "MMERR_SGI_8BIT",
    44: "MMERR_SGI_STEREO",
    45: "MMERR_SGI_MONO",
    46: "MMERR_SUN_INIT",
    47: "MMERR_OS2_MIXSETUP",
    48: "MMERR_OS2_SEMAPHORE",
    49: "MMERR_OS2_TIMER",
    50: "MMERR_OS2_THREAD",
    51: "MMERR_DS_PRIORITY",
    52: "MMERR_DS_BUFFER",
    53: "MMERR_DS_FORMAT",
    54: "MMERR_DS_NOTIFY",
    55: "MMERR_DS_EVENT",
    56: "MMERR_DS_THREAD",
    57: "MMERR_DS_UPDATE",
    58: "MMERR_WINMM_HANDLE",
    59: "MMERR_WINMM_ALLOCATED",
    60: "MMERR_WINMM_DEVICEID",
    61: "MMERR_WINMM_FORMAT",
    62: "MMERR_WINMM_UNKNOWN",
    63: "MMERR_MAC_SPEED",
    64: "MMERR_MAC_START",
    65: "MMERR_OSX_UNKNOWN_DEVICE",
    66: "MMERR_OSX_BAD_PROPERTY",
    67: "MMERR_OSX_UNSUPPORTED_FORMAT",
    68: "MMERR_OSX_SET_STEREO",
    69: "MMERR_OSX_BUFFER_ALLOC",
    70: "MMERR_OSX_ADD_IO_PROC",
    71: "MMERR_OSX_DEVICE_START",
    72: "MMERR_OSX_PTHREAD",
    73: "MMERR_DOSWSS_STARTDMA",
    74: "MMERR_DOSSB_STARTDMA",
    75: "MMERR_NO_FLOAT32",
    76: "MMERR_OPENAL_CREATECTX",
    77: "MMERR_OPENAL_CTXCURRENT",
    78: "MMERR_OPENAL_GENBUFFERS",
    79: "MMERR_OPENAL_GENSOURCES",
    80: "MMERR_OPENAL_SOURCE",
    81: "MMERR_OPENAL_QUEUEBUFFERS",
    82: "MMERR_OPENAL_UNQUEUEBUFFERS",
    83: "MMERR_OPENAL_BUFFERDATA",
    84: "MMERR_OPENAL_GETSOURCE",
    85: "MMERR_OPENAL_SOURCEPLAY",
    86: "MMERR_OPENAL_SOURCESTOP",
    87: "MMERR_ALSA_NOCONFIG",
    88: "MMERR_ALSA_SETPARAMS",
    89: "MMERR_ALSA_SETFORMAT",
    90: "MMERR_ALSA_SETRATE",
    91: "MMERR_ALSA_SETCHANNELS",
    92: "MMERR_ALSA_BUFFERSIZE",
    93: "MMERR_ALSA_PCM_START",
    94: "MMERR_ALSA_PCM_WRITE",
    95: "MMERR_ALSA_PCM_RECOVER",
    96: "MMERR_SNDIO_SETPARAMS",
    97: "MMERR_SNDIO_BADPARAMS",
    98: "MMERR_MAX",
}
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
MMERR_OSX_UNKNOWN_DEVICE = 65
MMERR_OSX_BAD_PROPERTY = 66
MMERR_OSX_UNSUPPORTED_FORMAT = 67
MMERR_OSX_SET_STEREO = 68
MMERR_OSX_BUFFER_ALLOC = 69
MMERR_OSX_ADD_IO_PROC = 70
MMERR_OSX_DEVICE_START = 71
MMERR_OSX_PTHREAD = 72
MMERR_DOSWSS_STARTDMA = 73
MMERR_DOSSB_STARTDMA = 74
MMERR_NO_FLOAT32 = 75
MMERR_OPENAL_CREATECTX = 76
MMERR_OPENAL_CTXCURRENT = 77
MMERR_OPENAL_GENBUFFERS = 78
MMERR_OPENAL_GENSOURCES = 79
MMERR_OPENAL_SOURCE = 80
MMERR_OPENAL_QUEUEBUFFERS = 81
MMERR_OPENAL_UNQUEUEBUFFERS = 82
MMERR_OPENAL_BUFFERDATA = 83
MMERR_OPENAL_GETSOURCE = 84
MMERR_OPENAL_SOURCEPLAY = 85
MMERR_OPENAL_SOURCESTOP = 86
MMERR_ALSA_NOCONFIG = 87
MMERR_ALSA_SETPARAMS = 88
MMERR_ALSA_SETFORMAT = 89
MMERR_ALSA_SETRATE = 90
MMERR_ALSA_SETCHANNELS = 91
MMERR_ALSA_BUFFERSIZE = 92
MMERR_ALSA_PCM_START = 93
MMERR_ALSA_PCM_WRITE = 94
MMERR_ALSA_PCM_RECOVER = 95
MMERR_SNDIO_SETPARAMS = 96
MMERR_SNDIO_BADPARAMS = 97
MMERR_MAX = 98
c__Ea_MMERR_OPENING_FILE = ctypes.c_uint32  # enum
MikMod_handler = ctypes.CFUNCTYPE(None)
MikMod_handler_t = ctypes.CFUNCTYPE(None)
MikMod_errno = 0  # Variable ctypes.c_int32
MikMod_critical = 0  # Variable ctypes.c_int32
MikMod_strerror = _libraries["FIXME_STUB"].MikMod_strerror
MikMod_strerror.restype = ctypes.POINTER(ctypes.c_char)
MikMod_strerror.argtypes = [ctypes.c_int32]
MikMod_RegisterErrorHandler = _libraries["FIXME_STUB"].MikMod_RegisterErrorHandler
MikMod_RegisterErrorHandler.restype = MikMod_handler_t
MikMod_RegisterErrorHandler.argtypes = [MikMod_handler_t]
MikMod_RegisterAllDrivers = _libraries["FIXME_STUB"].MikMod_RegisterAllDrivers
MikMod_RegisterAllDrivers.restype = None
MikMod_RegisterAllDrivers.argtypes = []
MikMod_InfoDriver = _libraries["FIXME_STUB"].MikMod_InfoDriver
MikMod_InfoDriver.restype = ctypes.POINTER(ctypes.c_char)
MikMod_InfoDriver.argtypes = []


class struct_MDRIVER(Structure):
    pass


MikMod_RegisterDriver = _libraries["FIXME_STUB"].MikMod_RegisterDriver
MikMod_RegisterDriver.restype = None
MikMod_RegisterDriver.argtypes = [ctypes.POINTER(struct_MDRIVER)]
MikMod_DriverFromAlias = _libraries["FIXME_STUB"].MikMod_DriverFromAlias
MikMod_DriverFromAlias.restype = ctypes.c_int32
MikMod_DriverFromAlias.argtypes = [ctypes.POINTER(ctypes.c_char)]
MikMod_DriverByOrdinal = _libraries["FIXME_STUB"].MikMod_DriverByOrdinal
MikMod_DriverByOrdinal.restype = ctypes.POINTER(struct_MDRIVER)
MikMod_DriverByOrdinal.argtypes = [ctypes.c_int32]
MikMod_Init = _libraries["FIXME_STUB"].MikMod_Init
MikMod_Init.restype = ctypes.c_int32
MikMod_Init.argtypes = [ctypes.POINTER(ctypes.c_char)]
MikMod_Exit = _libraries["FIXME_STUB"].MikMod_Exit
MikMod_Exit.restype = None
MikMod_Exit.argtypes = []
MikMod_Reset = _libraries["FIXME_STUB"].MikMod_Reset
MikMod_Reset.restype = ctypes.c_int32
MikMod_Reset.argtypes = [ctypes.POINTER(ctypes.c_char)]
MikMod_SetNumVoices = _libraries["FIXME_STUB"].MikMod_SetNumVoices
MikMod_SetNumVoices.restype = ctypes.c_int32
MikMod_SetNumVoices.argtypes = [ctypes.c_int32, ctypes.c_int32]
MikMod_Active = _libraries["FIXME_STUB"].MikMod_Active
MikMod_Active.restype = BOOL
MikMod_Active.argtypes = []
MikMod_EnableOutput = _libraries["FIXME_STUB"].MikMod_EnableOutput
MikMod_EnableOutput.restype = ctypes.c_int32
MikMod_EnableOutput.argtypes = []
MikMod_DisableOutput = _libraries["FIXME_STUB"].MikMod_DisableOutput
MikMod_DisableOutput.restype = None
MikMod_DisableOutput.argtypes = []
MikMod_Update = _libraries["FIXME_STUB"].MikMod_Update
MikMod_Update.restype = None
MikMod_Update.argtypes = []
MikMod_InitThreads = _libraries["FIXME_STUB"].MikMod_InitThreads
MikMod_InitThreads.restype = BOOL
MikMod_InitThreads.argtypes = []
MikMod_Lock = _libraries["FIXME_STUB"].MikMod_Lock
MikMod_Lock.restype = None
MikMod_Lock.argtypes = []
MikMod_Unlock = _libraries["FIXME_STUB"].MikMod_Unlock
MikMod_Unlock.restype = None
MikMod_Unlock.argtypes = []
size_t = ctypes.c_uint64
MikMod_malloc = _libraries["FIXME_STUB"].MikMod_malloc
MikMod_malloc.restype = ctypes.POINTER(None)
MikMod_malloc.argtypes = [size_t]
MikMod_calloc = _libraries["FIXME_STUB"].MikMod_calloc
MikMod_calloc.restype = ctypes.POINTER(None)
MikMod_calloc.argtypes = [size_t, size_t]
MikMod_realloc = _libraries["FIXME_STUB"].MikMod_realloc
MikMod_realloc.restype = ctypes.POINTER(None)
MikMod_realloc.argtypes = [ctypes.POINTER(None), size_t]
MikMod_strdup = _libraries["FIXME_STUB"].MikMod_strdup
MikMod_strdup.restype = ctypes.POINTER(ctypes.c_char)
MikMod_strdup.argtypes = [ctypes.POINTER(ctypes.c_char)]
MikMod_free = _libraries["FIXME_STUB"].MikMod_free
MikMod_free.restype = None
MikMod_free.argtypes = [ctypes.POINTER(None)]


class struct_MREADER(Structure):
    pass


struct_MREADER._pack_ = 1  # source:False
struct_MREADER._fields_ = [
    (
        "Seek",
        ctypes.CFUNCTYPE(
            ctypes.c_int32,
            ctypes.POINTER(struct_MREADER),
            ctypes.c_int64,
            ctypes.c_int32,
        ),
    ),
    ("Tell", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.POINTER(struct_MREADER))),
    (
        "Read",
        ctypes.CFUNCTYPE(
            ctypes.c_int32,
            ctypes.POINTER(struct_MREADER),
            ctypes.POINTER(None),
            ctypes.c_uint64,
        ),
    ),
    ("Get", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(struct_MREADER))),
    ("Eof", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(struct_MREADER))),
    ("iobase", ctypes.c_int64),
    ("prev_iobase", ctypes.c_int64),
]

MREADER = struct_MREADER


class struct_MWRITER(Structure):
    pass


struct_MWRITER._pack_ = 1  # source:False
struct_MWRITER._fields_ = [
    (
        "Seek",
        ctypes.CFUNCTYPE(
            ctypes.c_int32,
            ctypes.POINTER(struct_MWRITER),
            ctypes.c_int64,
            ctypes.c_int32,
        ),
    ),
    ("Tell", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.POINTER(struct_MWRITER))),
    (
        "Write",
        ctypes.CFUNCTYPE(
            ctypes.c_int32,
            ctypes.POINTER(struct_MWRITER),
            ctypes.POINTER(None),
            ctypes.c_uint64,
        ),
    ),
    (
        "Put",
        ctypes.CFUNCTYPE(
            ctypes.c_int32, ctypes.POINTER(struct_MWRITER), ctypes.c_int32
        ),
    ),
]

MWRITER = struct_MWRITER


class struct_SAMPLE(Structure):
    pass


struct_SAMPLE._pack_ = 1  # source:False
struct_SAMPLE._fields_ = [
    ("panning", ctypes.c_int16),
    ("PADDING_0", ctypes.c_ubyte * 2),
    ("speed", ctypes.c_uint32),
    ("volume", ctypes.c_ubyte),
    ("PADDING_1", ctypes.c_ubyte),
    ("inflags", ctypes.c_uint16),
    ("flags", ctypes.c_uint16),
    ("PADDING_2", ctypes.c_ubyte * 2),
    ("length", ctypes.c_uint32),
    ("loopstart", ctypes.c_uint32),
    ("loopend", ctypes.c_uint32),
    ("susbegin", ctypes.c_uint32),
    ("susend", ctypes.c_uint32),
    ("globvol", ctypes.c_ubyte),
    ("vibflags", ctypes.c_ubyte),
    ("vibtype", ctypes.c_ubyte),
    ("vibsweep", ctypes.c_ubyte),
    ("vibdepth", ctypes.c_ubyte),
    ("vibrate", ctypes.c_ubyte),
    ("PADDING_3", ctypes.c_ubyte * 6),
    ("samplename", ctypes.POINTER(ctypes.c_char)),
    ("avibpos", ctypes.c_uint16),
    ("divfactor", ctypes.c_ubyte),
    ("PADDING_4", ctypes.c_ubyte),
    ("seekpos", ctypes.c_uint32),
    ("handle", ctypes.c_int16),
    ("PADDING_5", ctypes.c_ubyte * 6),
    ("onfree", ctypes.CFUNCTYPE(None, ctypes.POINTER(None))),
    ("ctx", ctypes.POINTER(None)),
]

SAMPLE = struct_SAMPLE
Sample_LoadRaw = _libraries["FIXME_STUB"].Sample_LoadRaw
Sample_LoadRaw.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadRaw.argtypes = [ctypes.POINTER(ctypes.c_char), ULONG, ULONG, ULONG]


class struct__IO_FILE(Structure):
    pass


class struct__IO_marker(Structure):
    pass


class struct__IO_wide_data(Structure):
    pass


class struct__IO_codecvt(Structure):
    pass


struct__IO_FILE._pack_ = 1  # source:False
struct__IO_FILE._fields_ = [
    ("_flags", ctypes.c_int32),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("_IO_read_ptr", ctypes.POINTER(ctypes.c_char)),
    ("_IO_read_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_read_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_ptr", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_buf_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_buf_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_save_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_backup_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_save_end", ctypes.POINTER(ctypes.c_char)),
    ("_markers", ctypes.POINTER(struct__IO_marker)),
    ("_chain", ctypes.POINTER(struct__IO_FILE)),
    ("_fileno", ctypes.c_int32),
    ("_flags2", ctypes.c_int32),
    ("_old_offset", ctypes.c_int64),
    ("_cur_column", ctypes.c_uint16),
    ("_vtable_offset", ctypes.c_byte),
    ("_shortbuf", ctypes.c_char * 1),
    ("PADDING_1", ctypes.c_ubyte * 4),
    ("_lock", ctypes.POINTER(None)),
    ("_offset", ctypes.c_int64),
    ("_codecvt", ctypes.POINTER(struct__IO_codecvt)),
    ("_wide_data", ctypes.POINTER(struct__IO_wide_data)),
    ("_freeres_list", ctypes.POINTER(struct__IO_FILE)),
    ("_freeres_buf", ctypes.POINTER(None)),
    ("__pad5", ctypes.c_uint64),
    ("_mode", ctypes.c_int32),
    ("_unused2", ctypes.c_char * 20),
]

Sample_LoadRawFP = _libraries["FIXME_STUB"].Sample_LoadRawFP
Sample_LoadRawFP.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadRawFP.argtypes = [ctypes.POINTER(struct__IO_FILE), ULONG, ULONG, ULONG]
Sample_LoadRawMem = _libraries["FIXME_STUB"].Sample_LoadRawMem
Sample_LoadRawMem.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadRawMem.argtypes = [
    ctypes.POINTER(ctypes.c_char),
    ctypes.c_int32,
    ULONG,
    ULONG,
    ULONG,
]
Sample_LoadRawGeneric = _libraries["FIXME_STUB"].Sample_LoadRawGeneric
Sample_LoadRawGeneric.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadRawGeneric.argtypes = [ctypes.POINTER(struct_MREADER), ULONG, ULONG, ULONG]
Sample_Load = _libraries["FIXME_STUB"].Sample_Load
Sample_Load.restype = ctypes.POINTER(struct_SAMPLE)
Sample_Load.argtypes = [ctypes.POINTER(ctypes.c_char)]
Sample_LoadFP = _libraries["FIXME_STUB"].Sample_LoadFP
Sample_LoadFP.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadFP.argtypes = [ctypes.POINTER(struct__IO_FILE)]
Sample_LoadMem = _libraries["FIXME_STUB"].Sample_LoadMem
Sample_LoadMem.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadMem.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int32]
Sample_LoadGeneric = _libraries["FIXME_STUB"].Sample_LoadGeneric
Sample_LoadGeneric.restype = ctypes.POINTER(struct_SAMPLE)
Sample_LoadGeneric.argtypes = [ctypes.POINTER(struct_MREADER)]
Sample_Free = _libraries["FIXME_STUB"].Sample_Free
Sample_Free.restype = None
Sample_Free.argtypes = [ctypes.POINTER(struct_SAMPLE)]
Sample_Play = _libraries["FIXME_STUB"].Sample_Play
Sample_Play.restype = SBYTE
Sample_Play.argtypes = [ctypes.POINTER(struct_SAMPLE), ULONG, UBYTE]
Voice_SetVolume = _libraries["FIXME_STUB"].Voice_SetVolume
Voice_SetVolume.restype = None
Voice_SetVolume.argtypes = [SBYTE, UWORD]
Voice_GetVolume = _libraries["FIXME_STUB"].Voice_GetVolume
Voice_GetVolume.restype = UWORD
Voice_GetVolume.argtypes = [SBYTE]
Voice_SetFrequency = _libraries["FIXME_STUB"].Voice_SetFrequency
Voice_SetFrequency.restype = None
Voice_SetFrequency.argtypes = [SBYTE, ULONG]
Voice_GetFrequency = _libraries["FIXME_STUB"].Voice_GetFrequency
Voice_GetFrequency.restype = ULONG
Voice_GetFrequency.argtypes = [SBYTE]
Voice_SetPanning = _libraries["FIXME_STUB"].Voice_SetPanning
Voice_SetPanning.restype = None
Voice_SetPanning.argtypes = [SBYTE, ULONG]
Voice_GetPanning = _libraries["FIXME_STUB"].Voice_GetPanning
Voice_GetPanning.restype = ULONG
Voice_GetPanning.argtypes = [SBYTE]
Voice_Play = _libraries["FIXME_STUB"].Voice_Play
Voice_Play.restype = None
Voice_Play.argtypes = [SBYTE, ctypes.POINTER(struct_SAMPLE), ULONG]
Voice_Stop = _libraries["FIXME_STUB"].Voice_Stop
Voice_Stop.restype = None
Voice_Stop.argtypes = [SBYTE]
Voice_Stopped = _libraries["FIXME_STUB"].Voice_Stopped
Voice_Stopped.restype = BOOL
Voice_Stopped.argtypes = [SBYTE]
Voice_GetPosition = _libraries["FIXME_STUB"].Voice_GetPosition
Voice_GetPosition.restype = SLONG
Voice_GetPosition.argtypes = [SBYTE]
Voice_RealVolume = _libraries["FIXME_STUB"].Voice_RealVolume
Voice_RealVolume.restype = ULONG
Voice_RealVolume.argtypes = [SBYTE]


class struct_ENVPT(Structure):
    pass


struct_ENVPT._pack_ = 1  # source:False
struct_ENVPT._fields_ = [
    ("pos", ctypes.c_int16),
    ("val", ctypes.c_int16),
]

ENVPT = struct_ENVPT


class struct_INSTRUMENT(Structure):
    pass


struct_INSTRUMENT._pack_ = 1  # source:False
struct_INSTRUMENT._fields_ = [
    ("insname", ctypes.POINTER(ctypes.c_char)),
    ("flags", ctypes.c_ubyte),
    ("PADDING_0", ctypes.c_ubyte),
    ("samplenumber", ctypes.c_uint16 * 120),
    ("samplenote", ctypes.c_ubyte * 120),
    ("nnatype", ctypes.c_ubyte),
    ("dca", ctypes.c_ubyte),
    ("dct", ctypes.c_ubyte),
    ("globvol", ctypes.c_ubyte),
    ("volfade", ctypes.c_uint16),
    ("panning", ctypes.c_int16),
    ("pitpansep", ctypes.c_ubyte),
    ("pitpancenter", ctypes.c_ubyte),
    ("rvolvar", ctypes.c_ubyte),
    ("rpanvar", ctypes.c_ubyte),
    ("volflg", ctypes.c_ubyte),
    ("volpts", ctypes.c_ubyte),
    ("volsusbeg", ctypes.c_ubyte),
    ("volsusend", ctypes.c_ubyte),
    ("volbeg", ctypes.c_ubyte),
    ("volend", ctypes.c_ubyte),
    ("volenv", struct_ENVPT * 32),
    ("panflg", ctypes.c_ubyte),
    ("panpts", ctypes.c_ubyte),
    ("pansusbeg", ctypes.c_ubyte),
    ("pansusend", ctypes.c_ubyte),
    ("panbeg", ctypes.c_ubyte),
    ("panend", ctypes.c_ubyte),
    ("panenv", struct_ENVPT * 32),
    ("pitflg", ctypes.c_ubyte),
    ("pitpts", ctypes.c_ubyte),
    ("pitsusbeg", ctypes.c_ubyte),
    ("pitsusend", ctypes.c_ubyte),
    ("pitbeg", ctypes.c_ubyte),
    ("pitend", ctypes.c_ubyte),
    ("pitenv", struct_ENVPT * 32),
]

INSTRUMENT = struct_INSTRUMENT


class struct_MP_CONTROL(Structure):
    pass


class struct_MP_VOICE(Structure):
    pass


class struct_MODULE(Structure):
    pass


struct_MODULE._pack_ = 1  # source:False
struct_MODULE._fields_ = [
    ("songname", ctypes.POINTER(ctypes.c_char)),
    ("modtype", ctypes.POINTER(ctypes.c_char)),
    ("comment", ctypes.POINTER(ctypes.c_char)),
    ("flags", ctypes.c_uint16),
    ("numchn", ctypes.c_ubyte),
    ("numvoices", ctypes.c_ubyte),
    ("numpos", ctypes.c_uint16),
    ("numpat", ctypes.c_uint16),
    ("numins", ctypes.c_uint16),
    ("numsmp", ctypes.c_uint16),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("instruments", ctypes.POINTER(struct_INSTRUMENT)),
    ("samples", ctypes.POINTER(struct_SAMPLE)),
    ("realchn", ctypes.c_ubyte),
    ("totalchn", ctypes.c_ubyte),
    ("reppos", ctypes.c_uint16),
    ("initspeed", ctypes.c_ubyte),
    ("PADDING_1", ctypes.c_ubyte),
    ("inittempo", ctypes.c_uint16),
    ("initvolume", ctypes.c_ubyte),
    ("PADDING_2", ctypes.c_ubyte),
    ("panning", ctypes.c_uint16 * 64),
    ("chanvol", ctypes.c_ubyte * 64),
    ("bpm", ctypes.c_uint16),
    ("sngspd", ctypes.c_uint16),
    ("volume", ctypes.c_int16),
    ("extspd", ctypes.c_int32),
    ("panflag", ctypes.c_int32),
    ("wrap", ctypes.c_int32),
    ("loop", ctypes.c_int32),
    ("fadeout", ctypes.c_int32),
    ("patpos", ctypes.c_uint16),
    ("sngpos", ctypes.c_int16),
    ("sngtime", ctypes.c_uint32),
    ("relspd", ctypes.c_int16),
    ("numtrk", ctypes.c_uint16),
    ("tracks", ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte))),
    ("patterns", ctypes.POINTER(ctypes.c_uint16)),
    ("pattrows", ctypes.POINTER(ctypes.c_uint16)),
    ("positions", ctypes.POINTER(ctypes.c_uint16)),
    ("forbid", ctypes.c_int32),
    ("numrow", ctypes.c_uint16),
    ("vbtick", ctypes.c_uint16),
    ("sngremainder", ctypes.c_uint16),
    ("PADDING_3", ctypes.c_ubyte * 6),
    ("control", ctypes.POINTER(struct_MP_CONTROL)),
    ("voice", ctypes.POINTER(struct_MP_VOICE)),
    ("globalslide", ctypes.c_ubyte),
    ("pat_repcrazy", ctypes.c_ubyte),
    ("patbrk", ctypes.c_uint16),
    ("patdly", ctypes.c_ubyte),
    ("patdly2", ctypes.c_ubyte),
    ("posjmp", ctypes.c_int16),
    ("bpmlimit", ctypes.c_uint16),
    ("PADDING_4", ctypes.c_ubyte * 6),
]

MODULE = struct_MODULE


class struct_VOICEINFO(Structure):
    pass


struct_VOICEINFO._pack_ = 1  # source:False
struct_VOICEINFO._fields_ = [
    ("i", ctypes.POINTER(struct_INSTRUMENT)),
    ("s", ctypes.POINTER(struct_SAMPLE)),
    ("panning", ctypes.c_int16),
    ("volume", ctypes.c_byte),
    ("PADDING_0", ctypes.c_ubyte),
    ("period", ctypes.c_uint16),
    ("kick", ctypes.c_ubyte),
    ("PADDING_1", ctypes.c_ubyte),
]

VOICEINFO = struct_VOICEINFO


class struct_MLOADER(Structure):
    pass


MikMod_InfoLoader = _libraries["FIXME_STUB"].MikMod_InfoLoader
MikMod_InfoLoader.restype = ctypes.POINTER(ctypes.c_char)
MikMod_InfoLoader.argtypes = []
MikMod_RegisterAllLoaders = _libraries["FIXME_STUB"].MikMod_RegisterAllLoaders
MikMod_RegisterAllLoaders.restype = None
MikMod_RegisterAllLoaders.argtypes = []
MikMod_RegisterLoader = _libraries["FIXME_STUB"].MikMod_RegisterLoader
MikMod_RegisterLoader.restype = None
MikMod_RegisterLoader.argtypes = [ctypes.POINTER(struct_MLOADER)]
load_669 = struct_MLOADER  # Variable struct_MLOADER
load_amf = struct_MLOADER  # Variable struct_MLOADER
load_asy = struct_MLOADER  # Variable struct_MLOADER
load_dsm = struct_MLOADER  # Variable struct_MLOADER
load_far = struct_MLOADER  # Variable struct_MLOADER
load_gdm = struct_MLOADER  # Variable struct_MLOADER
load_gt2 = struct_MLOADER  # Variable struct_MLOADER
load_it = struct_MLOADER  # Variable struct_MLOADER
load_imf = struct_MLOADER  # Variable struct_MLOADER
load_med = struct_MLOADER  # Variable struct_MLOADER
load_m15 = struct_MLOADER  # Variable struct_MLOADER
load_mod = struct_MLOADER  # Variable struct_MLOADER
load_mtm = struct_MLOADER  # Variable struct_MLOADER
load_okt = struct_MLOADER  # Variable struct_MLOADER
load_stm = struct_MLOADER  # Variable struct_MLOADER
load_stx = struct_MLOADER  # Variable struct_MLOADER
load_s3m = struct_MLOADER  # Variable struct_MLOADER
load_ult = struct_MLOADER  # Variable struct_MLOADER
load_umx = struct_MLOADER  # Variable struct_MLOADER
load_uni = struct_MLOADER  # Variable struct_MLOADER
load_xm = struct_MLOADER  # Variable struct_MLOADER
Player_Load = _libraries["FIXME_STUB"].Player_Load
Player_Load.restype = ctypes.POINTER(struct_MODULE)
Player_Load.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int32, BOOL]
Player_LoadFP = _libraries["FIXME_STUB"].Player_LoadFP
Player_LoadFP.restype = ctypes.POINTER(struct_MODULE)
Player_LoadFP.argtypes = [ctypes.POINTER(struct__IO_FILE), ctypes.c_int32, BOOL]
Player_LoadMem = _libraries["FIXME_STUB"].Player_LoadMem
Player_LoadMem.restype = ctypes.POINTER(struct_MODULE)
Player_LoadMem.argtypes = [
    ctypes.POINTER(ctypes.c_char),
    ctypes.c_int32,
    ctypes.c_int32,
    BOOL,
]
Player_LoadGeneric = _libraries["FIXME_STUB"].Player_LoadGeneric
Player_LoadGeneric.restype = ctypes.POINTER(struct_MODULE)
Player_LoadGeneric.argtypes = [ctypes.POINTER(struct_MREADER), ctypes.c_int32, BOOL]
Player_LoadTitle = _libraries["FIXME_STUB"].Player_LoadTitle
Player_LoadTitle.restype = ctypes.POINTER(ctypes.c_char)
Player_LoadTitle.argtypes = [ctypes.POINTER(ctypes.c_char)]
Player_LoadTitleFP = _libraries["FIXME_STUB"].Player_LoadTitleFP
Player_LoadTitleFP.restype = ctypes.POINTER(ctypes.c_char)
Player_LoadTitleFP.argtypes = [ctypes.POINTER(struct__IO_FILE)]
Player_LoadTitleMem = _libraries["FIXME_STUB"].Player_LoadTitleMem
Player_LoadTitleMem.restype = ctypes.POINTER(ctypes.c_char)
Player_LoadTitleMem.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int32]
Player_LoadTitleGeneric = _libraries["FIXME_STUB"].Player_LoadTitleGeneric
Player_LoadTitleGeneric.restype = ctypes.POINTER(ctypes.c_char)
Player_LoadTitleGeneric.argtypes = [ctypes.POINTER(struct_MREADER)]
Player_Free = _libraries["FIXME_STUB"].Player_Free
Player_Free.restype = None
Player_Free.argtypes = [ctypes.POINTER(struct_MODULE)]
Player_Start = _libraries["FIXME_STUB"].Player_Start
Player_Start.restype = None
Player_Start.argtypes = [ctypes.POINTER(struct_MODULE)]
Player_Active = _libraries["FIXME_STUB"].Player_Active
Player_Active.restype = BOOL
Player_Active.argtypes = []
Player_Stop = _libraries["FIXME_STUB"].Player_Stop
Player_Stop.restype = None
Player_Stop.argtypes = []
Player_TogglePause = _libraries["FIXME_STUB"].Player_TogglePause
Player_TogglePause.restype = None
Player_TogglePause.argtypes = []
Player_Paused = _libraries["FIXME_STUB"].Player_Paused
Player_Paused.restype = BOOL
Player_Paused.argtypes = []
Player_NextPosition = _libraries["FIXME_STUB"].Player_NextPosition
Player_NextPosition.restype = None
Player_NextPosition.argtypes = []
Player_PrevPosition = _libraries["FIXME_STUB"].Player_PrevPosition
Player_PrevPosition.restype = None
Player_PrevPosition.argtypes = []
Player_SetPosition = _libraries["FIXME_STUB"].Player_SetPosition
Player_SetPosition.restype = None
Player_SetPosition.argtypes = [UWORD]
Player_Muted = _libraries["FIXME_STUB"].Player_Muted
Player_Muted.restype = BOOL
Player_Muted.argtypes = [UBYTE]
Player_SetVolume = _libraries["FIXME_STUB"].Player_SetVolume
Player_SetVolume.restype = None
Player_SetVolume.argtypes = [SWORD]
Player_GetModule = _libraries["FIXME_STUB"].Player_GetModule
Player_GetModule.restype = ctypes.POINTER(struct_MODULE)
Player_GetModule.argtypes = []
Player_SetSpeed = _libraries["FIXME_STUB"].Player_SetSpeed
Player_SetSpeed.restype = None
Player_SetSpeed.argtypes = [UWORD]
Player_SetTempo = _libraries["FIXME_STUB"].Player_SetTempo
Player_SetTempo.restype = None
Player_SetTempo.argtypes = [UWORD]
Player_Unmute = _libraries["FIXME_STUB"].Player_Unmute
Player_Unmute.restype = None
Player_Unmute.argtypes = [SLONG]
Player_Mute = _libraries["FIXME_STUB"].Player_Mute
Player_Mute.restype = None
Player_Mute.argtypes = [SLONG]
Player_ToggleMute = _libraries["FIXME_STUB"].Player_ToggleMute
Player_ToggleMute.restype = None
Player_ToggleMute.argtypes = [SLONG]
Player_GetChannelVoice = _libraries["FIXME_STUB"].Player_GetChannelVoice
Player_GetChannelVoice.restype = ctypes.c_int32
Player_GetChannelVoice.argtypes = [UBYTE]
Player_GetChannelPeriod = _libraries["FIXME_STUB"].Player_GetChannelPeriod
Player_GetChannelPeriod.restype = UWORD
Player_GetChannelPeriod.argtypes = [UBYTE]
Player_QueryVoices = _libraries["FIXME_STUB"].Player_QueryVoices
Player_QueryVoices.restype = ctypes.c_int32
Player_QueryVoices.argtypes = [UWORD, ctypes.POINTER(struct_VOICEINFO)]
Player_GetRow = _libraries["FIXME_STUB"].Player_GetRow
Player_GetRow.restype = ctypes.c_int32
Player_GetRow.argtypes = []
Player_GetOrder = _libraries["FIXME_STUB"].Player_GetOrder
Player_GetOrder.restype = ctypes.c_int32
Player_GetOrder.argtypes = []
MikMod_player_t = ctypes.CFUNCTYPE(None)
MikMod_callback_t = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint64
)
MikMod_RegisterPlayer = _libraries["FIXME_STUB"].MikMod_RegisterPlayer
MikMod_RegisterPlayer.restype = MikMod_player_t
MikMod_RegisterPlayer.argtypes = [MikMod_player_t]

# values for enumeration 'c__Ea_MD_MUSIC'
c__Ea_MD_MUSIC__enumvalues = {
    0: "MD_MUSIC",
    1: "MD_SNDFX",
}
MD_MUSIC = 0
MD_SNDFX = 1
c__Ea_MD_MUSIC = ctypes.c_uint32  # enum

# values for enumeration 'c__Ea_MD_HARDWARE'
c__Ea_MD_HARDWARE__enumvalues = {
    0: "MD_HARDWARE",
    1: "MD_SOFTWARE",
}
MD_HARDWARE = 0
MD_SOFTWARE = 1
c__Ea_MD_HARDWARE = ctypes.c_uint32  # enum


class struct_SAMPLOAD(Structure):
    pass


struct_MDRIVER._pack_ = 1  # source:False
struct_MDRIVER._fields_ = [
    ("next", ctypes.POINTER(struct_MDRIVER)),
    ("Name", ctypes.POINTER(ctypes.c_char)),
    ("Version", ctypes.POINTER(ctypes.c_char)),
    ("HardVoiceLimit", ctypes.c_ubyte),
    ("SoftVoiceLimit", ctypes.c_ubyte),
    ("PADDING_0", ctypes.c_ubyte * 6),
    ("Alias", ctypes.POINTER(ctypes.c_char)),
    ("CmdLineHelp", ctypes.POINTER(ctypes.c_char)),
    ("CommandLine", ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_char))),
    ("IsPresent", ctypes.CFUNCTYPE(ctypes.c_int32)),
    (
        "SampleLoad",
        ctypes.CFUNCTYPE(
            ctypes.c_int16, ctypes.POINTER(struct_SAMPLOAD), ctypes.c_int32
        ),
    ),
    ("SampleUnload", ctypes.CFUNCTYPE(None, ctypes.c_int16)),
    ("FreeSampleSpace", ctypes.CFUNCTYPE(ctypes.c_uint32, ctypes.c_int32)),
    (
        "RealSampleLength",
        ctypes.CFUNCTYPE(
            ctypes.c_uint32, ctypes.c_int32, ctypes.POINTER(struct_SAMPLE)
        ),
    ),
    ("Init", ctypes.CFUNCTYPE(ctypes.c_int32)),
    ("Exit", ctypes.CFUNCTYPE(None)),
    ("Reset", ctypes.CFUNCTYPE(ctypes.c_int32)),
    ("SetNumVoices", ctypes.CFUNCTYPE(ctypes.c_int32)),
    ("PlayStart", ctypes.CFUNCTYPE(ctypes.c_int32)),
    ("PlayStop", ctypes.CFUNCTYPE(None)),
    ("Update", ctypes.CFUNCTYPE(None)),
    ("Pause", ctypes.CFUNCTYPE(None)),
    ("VoiceSetVolume", ctypes.CFUNCTYPE(None, ctypes.c_ubyte, ctypes.c_uint16)),
    ("VoiceGetVolume", ctypes.CFUNCTYPE(ctypes.c_uint16, ctypes.c_ubyte)),
    ("VoiceSetFrequency", ctypes.CFUNCTYPE(None, ctypes.c_ubyte, ctypes.c_uint32)),
    ("VoiceGetFrequency", ctypes.CFUNCTYPE(ctypes.c_uint32, ctypes.c_ubyte)),
    ("VoiceSetPanning", ctypes.CFUNCTYPE(None, ctypes.c_ubyte, ctypes.c_uint32)),
    ("VoiceGetPanning", ctypes.CFUNCTYPE(ctypes.c_uint32, ctypes.c_ubyte)),
    (
        "VoicePlay",
        ctypes.CFUNCTYPE(
            None,
            ctypes.c_ubyte,
            ctypes.c_int16,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint16,
        ),
    ),
    ("VoiceStop", ctypes.CFUNCTYPE(None, ctypes.c_ubyte)),
    ("VoiceStopped", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_ubyte)),
    ("VoiceGetPosition", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_ubyte)),
    ("VoiceRealVolume", ctypes.CFUNCTYPE(ctypes.c_uint32, ctypes.c_ubyte)),
]

MDRIVER = struct_MDRIVER
md_volume = "\x00"  # Variable ctypes.c_ubyte
md_musicvolume = "\x00"  # Variable ctypes.c_ubyte
md_sndfxvolume = "\x00"  # Variable ctypes.c_ubyte
md_reverb = "\x00"  # Variable ctypes.c_ubyte
md_pansep = "\x00"  # Variable ctypes.c_ubyte
md_device = 0  # Variable ctypes.c_uint16
md_mixfreq = 0  # Variable ctypes.c_uint16
md_mode = 0  # Variable ctypes.c_uint16
# Variable ctypes.POINTER(struct_MDRIVER)
md_driver = ctypes.POINTER(struct_MDRIVER)()
drv_nos = struct_MDRIVER  # Variable struct_MDRIVER
drv_pipe = struct_MDRIVER  # Variable struct_MDRIVER
drv_raw = struct_MDRIVER  # Variable struct_MDRIVER
drv_stdout = struct_MDRIVER  # Variable struct_MDRIVER
drv_wav = struct_MDRIVER  # Variable struct_MDRIVER
drv_aiff = struct_MDRIVER  # Variable struct_MDRIVER
drv_ultra = struct_MDRIVER  # Variable struct_MDRIVER
drv_sam9407 = struct_MDRIVER  # Variable struct_MDRIVER
drv_AF = struct_MDRIVER  # Variable struct_MDRIVER
drv_ahi = struct_MDRIVER  # Variable struct_MDRIVER
drv_aix = struct_MDRIVER  # Variable struct_MDRIVER
drv_alsa = struct_MDRIVER  # Variable struct_MDRIVER
drv_esd = struct_MDRIVER  # Variable struct_MDRIVER
drv_pulseaudio = struct_MDRIVER  # Variable struct_MDRIVER
drv_hp = struct_MDRIVER  # Variable struct_MDRIVER
drv_nas = struct_MDRIVER  # Variable struct_MDRIVER
drv_oss = struct_MDRIVER  # Variable struct_MDRIVER
drv_openal = struct_MDRIVER  # Variable struct_MDRIVER
drv_sdl = struct_MDRIVER  # Variable struct_MDRIVER
drv_sgi = struct_MDRIVER  # Variable struct_MDRIVER
drv_sndio = struct_MDRIVER  # Variable struct_MDRIVER
drv_sun = struct_MDRIVER  # Variable struct_MDRIVER
drv_dart = struct_MDRIVER  # Variable struct_MDRIVER
drv_os2 = struct_MDRIVER  # Variable struct_MDRIVER
drv_ds = struct_MDRIVER  # Variable struct_MDRIVER
drv_xaudio2 = struct_MDRIVER  # Variable struct_MDRIVER
drv_win = struct_MDRIVER  # Variable struct_MDRIVER
drv_mac = struct_MDRIVER  # Variable struct_MDRIVER
drv_osx = struct_MDRIVER  # Variable struct_MDRIVER
drv_dc = struct_MDRIVER  # Variable struct_MDRIVER
drv_gp32 = struct_MDRIVER  # Variable struct_MDRIVER
drv_psp = struct_MDRIVER  # Variable struct_MDRIVER
drv_wss = struct_MDRIVER  # Variable struct_MDRIVER
drv_sb = struct_MDRIVER  # Variable struct_MDRIVER
drv_osles = struct_MDRIVER  # Variable struct_MDRIVER
VC_Init = _libraries["FIXME_STUB"].VC_Init
VC_Init.restype = ctypes.c_int32
VC_Init.argtypes = []
VC_Exit = _libraries["FIXME_STUB"].VC_Exit
VC_Exit.restype = None
VC_Exit.argtypes = []
VC_SetCallback = _libraries["FIXME_STUB"].VC_SetCallback
VC_SetCallback.restype = None
VC_SetCallback.argtypes = [MikMod_callback_t]
VC_SetNumVoices = _libraries["FIXME_STUB"].VC_SetNumVoices
VC_SetNumVoices.restype = ctypes.c_int32
VC_SetNumVoices.argtypes = []
VC_SampleSpace = _libraries["FIXME_STUB"].VC_SampleSpace
VC_SampleSpace.restype = ULONG
VC_SampleSpace.argtypes = [ctypes.c_int32]
VC_SampleLength = _libraries["FIXME_STUB"].VC_SampleLength
VC_SampleLength.restype = ULONG
VC_SampleLength.argtypes = [ctypes.c_int32, ctypes.POINTER(struct_SAMPLE)]
VC_PlayStart = _libraries["FIXME_STUB"].VC_PlayStart
VC_PlayStart.restype = ctypes.c_int32
VC_PlayStart.argtypes = []
VC_PlayStop = _libraries["FIXME_STUB"].VC_PlayStop
VC_PlayStop.restype = None
VC_PlayStop.argtypes = []
VC_SampleLoad = _libraries["FIXME_STUB"].VC_SampleLoad
VC_SampleLoad.restype = SWORD
VC_SampleLoad.argtypes = [ctypes.POINTER(struct_SAMPLOAD), ctypes.c_int32]
VC_SampleUnload = _libraries["FIXME_STUB"].VC_SampleUnload
VC_SampleUnload.restype = None
VC_SampleUnload.argtypes = [SWORD]
VC_WriteBytes = _libraries["FIXME_STUB"].VC_WriteBytes
VC_WriteBytes.restype = ULONG
VC_WriteBytes.argtypes = [ctypes.POINTER(ctypes.c_byte), ULONG]
VC_SilenceBytes = _libraries["FIXME_STUB"].VC_SilenceBytes
VC_SilenceBytes.restype = ULONG
VC_SilenceBytes.argtypes = [ctypes.POINTER(ctypes.c_byte), ULONG]
VC_VoiceSetVolume = _libraries["FIXME_STUB"].VC_VoiceSetVolume
VC_VoiceSetVolume.restype = None
VC_VoiceSetVolume.argtypes = [UBYTE, UWORD]
VC_VoiceGetVolume = _libraries["FIXME_STUB"].VC_VoiceGetVolume
VC_VoiceGetVolume.restype = UWORD
VC_VoiceGetVolume.argtypes = [UBYTE]
VC_VoiceSetFrequency = _libraries["FIXME_STUB"].VC_VoiceSetFrequency
VC_VoiceSetFrequency.restype = None
VC_VoiceSetFrequency.argtypes = [UBYTE, ULONG]
VC_VoiceGetFrequency = _libraries["FIXME_STUB"].VC_VoiceGetFrequency
VC_VoiceGetFrequency.restype = ULONG
VC_VoiceGetFrequency.argtypes = [UBYTE]
VC_VoiceSetPanning = _libraries["FIXME_STUB"].VC_VoiceSetPanning
VC_VoiceSetPanning.restype = None
VC_VoiceSetPanning.argtypes = [UBYTE, ULONG]
VC_VoiceGetPanning = _libraries["FIXME_STUB"].VC_VoiceGetPanning
VC_VoiceGetPanning.restype = ULONG
VC_VoiceGetPanning.argtypes = [UBYTE]
VC_VoicePlay = _libraries["FIXME_STUB"].VC_VoicePlay
VC_VoicePlay.restype = None
VC_VoicePlay.argtypes = [UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD]
VC_VoiceStop = _libraries["FIXME_STUB"].VC_VoiceStop
VC_VoiceStop.restype = None
VC_VoiceStop.argtypes = [UBYTE]
VC_VoiceStopped = _libraries["FIXME_STUB"].VC_VoiceStopped
VC_VoiceStopped.restype = BOOL
VC_VoiceStopped.argtypes = [UBYTE]
VC_VoiceGetPosition = _libraries["FIXME_STUB"].VC_VoiceGetPosition
VC_VoiceGetPosition.restype = SLONG
VC_VoiceGetPosition.argtypes = [UBYTE]
VC_VoiceRealVolume = _libraries["FIXME_STUB"].VC_VoiceRealVolume
VC_VoiceRealVolume.restype = ULONG
VC_VoiceRealVolume.argtypes = [UBYTE]
__all__ = [
    "BOOL",
    "CHAR",
    "DMODE_16BITS",
    "DMODE_FLOAT",
    "DMODE_HQMIXER",
    "DMODE_INTERP",
    "DMODE_NOISEREDUCTION",
    "DMODE_REVERSE",
    "DMODE_SIMDMIXER",
    "DMODE_SOFT_MUSIC",
    "DMODE_SOFT_SNDFX",
    "DMODE_STEREO",
    "DMODE_SURROUND",
    "ENVPOINTS",
    "ENVPT",
    "INSTNOTES",
    "INSTRUMENT",
    "LIBMIKMOD_REVISION",
    "LIBMIKMOD_VERSION_MAJOR",
    "LIBMIKMOD_VERSION_MINOR",
    "MDRIVER",
    "MD_HARDWARE",
    "MD_MUSIC",
    "MD_SNDFX",
    "MD_SOFTWARE",
    "MIKMODAPI",
    "MMERR_16BIT_ONLY",
    "MMERR_8BIT_ONLY",
    "MMERR_AF_AUDIO_PORT",
    "MMERR_AIX_CONFIG_CONTROL",
    "MMERR_AIX_CONFIG_INIT",
    "MMERR_AIX_CONFIG_START",
    "MMERR_ALSA_BUFFERSIZE",
    "MMERR_ALSA_NOCONFIG",
    "MMERR_ALSA_PCM_RECOVER",
    "MMERR_ALSA_PCM_START",
    "MMERR_ALSA_PCM_WRITE",
    "MMERR_ALSA_SETCHANNELS",
    "MMERR_ALSA_SETFORMAT",
    "MMERR_ALSA_SETPARAMS",
    "MMERR_ALSA_SETRATE",
    "MMERR_DETECTING_DEVICE",
    "MMERR_DOSSB_STARTDMA",
    "MMERR_DOSWSS_STARTDMA",
    "MMERR_DS_BUFFER",
    "MMERR_DS_EVENT",
    "MMERR_DS_FORMAT",
    "MMERR_DS_NOTIFY",
    "MMERR_DS_PRIORITY",
    "MMERR_DS_THREAD",
    "MMERR_DS_UPDATE",
    "MMERR_DYNAMIC_LINKING",
    "MMERR_GUS_RESET",
    "MMERR_GUS_SETTINGS",
    "MMERR_GUS_TIMER",
    "MMERR_HP_AUDIO_DESC",
    "MMERR_HP_AUDIO_OUTPUT",
    "MMERR_HP_BUFFERSIZE",
    "MMERR_HP_CHANNELS",
    "MMERR_HP_SETSAMPLESIZE",
    "MMERR_HP_SETSPEED",
    "MMERR_INITIALIZING_MIXER",
    "MMERR_INVALID_DEVICE",
    "MMERR_ITPACK_INVALID_DATA",
    "MMERR_LOADING_HEADER",
    "MMERR_LOADING_PATTERN",
    "MMERR_LOADING_SAMPLEINFO",
    "MMERR_LOADING_TRACK",
    "MMERR_MAC_SPEED",
    "MMERR_MAC_START",
    "MMERR_MAX",
    "MMERR_MED_SYNTHSAMPLES",
    "MMERR_NON_BLOCK",
    "MMERR_NOT_A_MODULE",
    "MMERR_NOT_A_STREAM",
    "MMERR_NO_FLOAT32",
    "MMERR_OPENAL_BUFFERDATA",
    "MMERR_OPENAL_CREATECTX",
    "MMERR_OPENAL_CTXCURRENT",
    "MMERR_OPENAL_GENBUFFERS",
    "MMERR_OPENAL_GENSOURCES",
    "MMERR_OPENAL_GETSOURCE",
    "MMERR_OPENAL_QUEUEBUFFERS",
    "MMERR_OPENAL_SOURCE",
    "MMERR_OPENAL_SOURCEPLAY",
    "MMERR_OPENAL_SOURCESTOP",
    "MMERR_OPENAL_UNQUEUEBUFFERS",
    "MMERR_OPENING_AUDIO",
    "MMERR_OPENING_FILE",
    "MMERR_OS2_MIXSETUP",
    "MMERR_OS2_SEMAPHORE",
    "MMERR_OS2_THREAD",
    "MMERR_OS2_TIMER",
    "MMERR_OSS_SETFRAGMENT",
    "MMERR_OSS_SETSAMPLESIZE",
    "MMERR_OSS_SETSPEED",
    "MMERR_OSS_SETSTEREO",
    "MMERR_OSX_ADD_IO_PROC",
    "MMERR_OSX_BAD_PROPERTY",
    "MMERR_OSX_BUFFER_ALLOC",
    "MMERR_OSX_DEVICE_START",
    "MMERR_OSX_PTHREAD",
    "MMERR_OSX_SET_STEREO",
    "MMERR_OSX_UNKNOWN_DEVICE",
    "MMERR_OSX_UNSUPPORTED_FORMAT",
    "MMERR_OUT_OF_HANDLES",
    "MMERR_OUT_OF_MEMORY",
    "MMERR_SAMPLE_TOO_BIG",
    "MMERR_SGI_16BIT",
    "MMERR_SGI_8BIT",
    "MMERR_SGI_MONO",
    "MMERR_SGI_SPEED",
    "MMERR_SGI_STEREO",
    "MMERR_SNDIO_BADPARAMS",
    "MMERR_SNDIO_SETPARAMS",
    "MMERR_STEREO_ONLY",
    "MMERR_SUN_INIT",
    "MMERR_ULAW",
    "MMERR_UNKNOWN_WAVE_TYPE",
    "MMERR_WINMM_ALLOCATED",
    "MMERR_WINMM_DEVICEID",
    "MMERR_WINMM_FORMAT",
    "MMERR_WINMM_HANDLE",
    "MMERR_WINMM_UNKNOWN",
    "MODULE",
    "MREADER",
    "MUTE_EXCLUSIVE",
    "MUTE_INCLUSIVE",
    "MWRITER",
    "MikMod_Active",
    "MikMod_DisableOutput",
    "MikMod_DriverByOrdinal",
    "MikMod_DriverFromAlias",
    "MikMod_EnableOutput",
    "MikMod_Exit",
    "MikMod_GetVersion",
    "MikMod_InfoDriver",
    "MikMod_InfoLoader",
    "MikMod_Init",
    "MikMod_InitThreads",
    "MikMod_Lock",
    "MikMod_RegisterAllDrivers",
    "MikMod_RegisterAllLoaders",
    "MikMod_RegisterDriver",
    "MikMod_RegisterErrorHandler",
    "MikMod_RegisterLoader",
    "MikMod_RegisterPlayer",
    "MikMod_Reset",
    "MikMod_SetNumVoices",
    "MikMod_Unlock",
    "MikMod_Update",
    "MikMod_callback_t",
    "MikMod_calloc",
    "MikMod_critical",
    "MikMod_errno",
    "MikMod_free",
    "MikMod_handler",
    "MikMod_handler_t",
    "MikMod_malloc",
    "MikMod_player_t",
    "MikMod_realloc",
    "MikMod_strdup",
    "MikMod_strerror",
    "PAN_CENTER",
    "PAN_HALFLEFT",
    "PAN_HALFRIGHT",
    "PAN_LEFT",
    "PAN_RIGHT",
    "PAN_SURROUND",
    "Player_Active",
    "Player_Free",
    "Player_GetChannelPeriod",
    "Player_GetChannelVoice",
    "Player_GetModule",
    "Player_GetOrder",
    "Player_GetRow",
    "Player_Load",
    "Player_LoadFP",
    "Player_LoadGeneric",
    "Player_LoadMem",
    "Player_LoadTitle",
    "Player_LoadTitleFP",
    "Player_LoadTitleGeneric",
    "Player_LoadTitleMem",
    "Player_Mute",
    "Player_Muted",
    "Player_NextPosition",
    "Player_Paused",
    "Player_PrevPosition",
    "Player_QueryVoices",
    "Player_SetPosition",
    "Player_SetSpeed",
    "Player_SetTempo",
    "Player_SetVolume",
    "Player_Start",
    "Player_Stop",
    "Player_ToggleMute",
    "Player_TogglePause",
    "Player_Unmute",
    "SAMPLE",
    "SBYTE",
    "SFX_CRITICAL",
    "SF_16BITS",
    "SF_BIDI",
    "SF_BIG_ENDIAN",
    "SF_DELTA",
    "SF_EXTRAPLAYBACKMASK",
    "SF_FORMATMASK",
    "SF_ITPACKED",
    "SF_LOOP",
    "SF_OWNPAN",
    "SF_PLAYBACKMASK",
    "SF_REVERSE",
    "SF_SIGNED",
    "SF_STEREO",
    "SF_SUSTAIN",
    "SF_UST_LOOP",
    "SLONG",
    "SWORD",
    "Sample_Free",
    "Sample_Load",
    "Sample_LoadFP",
    "Sample_LoadGeneric",
    "Sample_LoadMem",
    "Sample_LoadRaw",
    "Sample_LoadRawFP",
    "Sample_LoadRawGeneric",
    "Sample_LoadRawMem",
    "Sample_Play",
    "UBYTE",
    "UF_ARPMEM",
    "UF_BGSLIDES",
    "UF_FT2QUIRKS",
    "UF_HIGHBPM",
    "UF_INST",
    "UF_LINEAR",
    "UF_MAXCHAN",
    "UF_NNA",
    "UF_NOWRAP",
    "UF_PANNING",
    "UF_S3MSLIDES",
    "UF_XMPERIODS",
    "ULONG",
    "UWORD",
    "VC_Exit",
    "VC_Init",
    "VC_PlayStart",
    "VC_PlayStop",
    "VC_SampleLength",
    "VC_SampleLoad",
    "VC_SampleSpace",
    "VC_SampleUnload",
    "VC_SetCallback",
    "VC_SetNumVoices",
    "VC_SilenceBytes",
    "VC_VoiceGetFrequency",
    "VC_VoiceGetPanning",
    "VC_VoiceGetPosition",
    "VC_VoiceGetVolume",
    "VC_VoicePlay",
    "VC_VoiceRealVolume",
    "VC_VoiceSetFrequency",
    "VC_VoiceSetPanning",
    "VC_VoiceSetVolume",
    "VC_VoiceStop",
    "VC_VoiceStopped",
    "VC_WriteBytes",
    "VOICEINFO",
    "Voice_GetFrequency",
    "Voice_GetPanning",
    "Voice_GetPosition",
    "Voice_GetVolume",
    "Voice_Play",
    "Voice_RealVolume",
    "Voice_SetFrequency",
    "Voice_SetPanning",
    "Voice_SetVolume",
    "Voice_Stop",
    "Voice_Stopped",
    "_MIKMOD_H_",
    "__mikmod_typetest",
    "c__Ea_MD_HARDWARE",
    "c__Ea_MD_MUSIC",
    "c__Ea_MMERR_OPENING_FILE",
    "drv_AF",
    "drv_ahi",
    "drv_aiff",
    "drv_aix",
    "drv_alsa",
    "drv_dart",
    "drv_dc",
    "drv_ds",
    "drv_esd",
    "drv_gp32",
    "drv_hp",
    "drv_mac",
    "drv_nas",
    "drv_nos",
    "drv_openal",
    "drv_os2",
    "drv_osles",
    "drv_oss",
    "drv_osx",
    "drv_pipe",
    "drv_psp",
    "drv_pulseaudio",
    "drv_raw",
    "drv_sam9407",
    "drv_sb",
    "drv_sdl",
    "drv_sgi",
    "drv_sndio",
    "drv_stdout",
    "drv_sun",
    "drv_ultra",
    "drv_wav",
    "drv_win",
    "drv_wss",
    "drv_xaudio2",
    "load_669",
    "load_amf",
    "load_asy",
    "load_dsm",
    "load_far",
    "load_gdm",
    "load_gt2",
    "load_imf",
    "load_it",
    "load_m15",
    "load_med",
    "load_mod",
    "load_mtm",
    "load_okt",
    "load_s3m",
    "load_stm",
    "load_stx",
    "load_ult",
    "load_umx",
    "load_uni",
    "load_xm",
    "md_device",
    "md_driver",
    "md_mixfreq",
    "md_mode",
    "md_musicvolume",
    "md_pansep",
    "md_reverb",
    "md_sndfxvolume",
    "md_volume",
    "size_t",
    "struct_ENVPT",
    "struct_INSTRUMENT",
    "struct_MDRIVER",
    "struct_MLOADER",
    "struct_MODULE",
    "struct_MP_CONTROL",
    "struct_MP_VOICE",
    "struct_MREADER",
    "struct_MWRITER",
    "struct_SAMPLE",
    "struct_SAMPLOAD",
    "struct_VOICEINFO",
    "struct__IO_FILE",
    "struct__IO_codecvt",
    "struct__IO_marker",
    "struct__IO_wide_data",
]
