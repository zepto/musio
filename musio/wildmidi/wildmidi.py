# -*- coding: utf-8 -*-
#
# TARGET arch is: []
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


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
            if field.startswith('PADDING_'):
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
        if hasattr(cls, '_fields_'):
            return (f[0] for f in cls._fields_ if not f[0].startswith('PADDING'))
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
                        fields[name] = (
                            type_((lambda callback: lambda *args: callback(*args))(
                                bound_fields[name]))
                        )
                    del bound_fields[name]
                else:
                    # default callback implementation (does nothing)
                    try:
                        default_ = type_(0).restype().value
                    except TypeError:
                        default_ = None
                    fields[name] = type_((
                        lambda default_: lambda *args: default_)(default_))
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
            ))
        return cls(**fields)


class Union(ctypes.Union, AsDictMixin):
    pass



def string_cast(char_pointer, encoding='utf-8', errors='strict'):
    value = ctypes.cast(char_pointer, ctypes.c_char_p).value
    if value is not None and encoding is not None:
        value = value.decode(encoding, errors=errors)
    return value


def char_pointer_cast(string, encoding='utf-8'):
    if encoding is not None:
        try:
            string = string.encode(encoding)
        except AttributeError:
            # In Python3, bytes has no encode attribute
            pass
    string = ctypes.c_char_p(string)
    return ctypes.cast(string, ctypes.POINTER(ctypes.c_char))



c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16

_libraries = {}
_libraries['libWildMidi.so'] = ctypes.CDLL('/usr/lib/libWildMidi.so')


WILDMIDI_LIB_H = True # macro
LIBWILDMIDI_VER_MAJOR = 0 # macro
LIBWILDMIDI_VER_MINOR = 4 # macro
LIBWILDMIDI_VER_MICRO = 4 # macro
# def LIBWILDMIDI_VERSION((0<<16):  # macro
#    return |(4<<8)|(4))  
WM_MO_LOG_VOLUME = 0x0001 # macro
WM_MO_ENHANCED_RESAMPLING = 0x0002 # macro
WM_MO_REVERB = 0x0004 # macro
WM_MO_LOOP = 0x0008 # macro
WM_MO_SAVEASTYPE0 = 0x1000 # macro
WM_MO_ROUNDTEMPO = 0x2000 # macro
WM_MO_STRIPSILENCE = 0x4000 # macro
WM_MO_TEXTASLYRIC = 0x8000 # macro
WM_CO_XMI_TYPE = 0x0010 # macro
WM_CO_FREQUENCY = 0x0020 # macro
WM_GS_VERSION = 0x0001 # macro
WM_SYMBOL = True # macro
class struct__WM_Info(Structure):
    pass

struct__WM_Info._pack_ = 1 # source:False
struct__WM_Info._fields_ = [
    ('copyright', ctypes.POINTER(ctypes.c_char)),
    ('current_sample', ctypes.c_uint32),
    ('approx_total_samples', ctypes.c_uint32),
    ('mixer_options', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('total_midi_time', ctypes.c_uint32),
]

midi = None
_WM_VIO_Allocate = ctypes.CFUNCTYPE(ctypes.POINTER(None), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_uint32))
_WM_VIO_Free = ctypes.CFUNCTYPE(None, ctypes.POINTER(None))
class struct__WM_VIO(Structure):
    pass

struct__WM_VIO._pack_ = 1 # source:False
struct__WM_VIO._fields_ = [
    ('allocate_file', ctypes.CFUNCTYPE(ctypes.POINTER(None), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_uint32))),
    ('free_file', ctypes.CFUNCTYPE(None, ctypes.POINTER(None))),
]

uint16_t = ctypes.c_uint16
WildMidi_GetString = _libraries['libWildMidi.so'].WildMidi_GetString
WildMidi_GetString.restype = ctypes.POINTER(ctypes.c_char)
WildMidi_GetString.argtypes = [uint16_t]
WildMidi_GetVersion = _libraries['libWildMidi.so'].WildMidi_GetVersion
WildMidi_GetVersion.restype = ctypes.c_int64
WildMidi_GetVersion.argtypes = []
WildMidi_Init = _libraries['libWildMidi.so'].WildMidi_Init
WildMidi_Init.restype = ctypes.c_int32
WildMidi_Init.argtypes = [ctypes.POINTER(ctypes.c_char), uint16_t, uint16_t]
WildMidi_InitVIO = _libraries['libWildMidi.so'].WildMidi_InitVIO
WildMidi_InitVIO.restype = ctypes.c_int32
WildMidi_InitVIO.argtypes = [ctypes.POINTER(struct__WM_VIO), ctypes.POINTER(ctypes.c_char), uint16_t, uint16_t]
uint8_t = ctypes.c_uint8
WildMidi_MasterVolume = _libraries['libWildMidi.so'].WildMidi_MasterVolume
WildMidi_MasterVolume.restype = ctypes.c_int32
WildMidi_MasterVolume.argtypes = [uint8_t]
WildMidi_Open = _libraries['libWildMidi.so'].WildMidi_Open
WildMidi_Open.restype = ctypes.POINTER(None)
WildMidi_Open.argtypes = [ctypes.POINTER(ctypes.c_char)]
uint32_t = ctypes.c_uint32
WildMidi_OpenBuffer = _libraries['libWildMidi.so'].WildMidi_OpenBuffer
WildMidi_OpenBuffer.restype = ctypes.POINTER(None)
WildMidi_OpenBuffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte), uint32_t]
WildMidi_GetMidiOutput = _libraries['libWildMidi.so'].WildMidi_GetMidiOutput
WildMidi_GetMidiOutput.restype = ctypes.c_int32
WildMidi_GetMidiOutput.argtypes = [ctypes.POINTER(None), ctypes.POINTER(ctypes.POINTER(ctypes.c_byte)), ctypes.POINTER(ctypes.c_uint32)]
WildMidi_GetOutput = _libraries['libWildMidi.so'].WildMidi_GetOutput
WildMidi_GetOutput.restype = ctypes.c_int32
WildMidi_GetOutput.argtypes = [ctypes.POINTER(None), ctypes.POINTER(ctypes.c_byte), uint32_t]
WildMidi_SetOption = _libraries['libWildMidi.so'].WildMidi_SetOption
WildMidi_SetOption.restype = ctypes.c_int32
WildMidi_SetOption.argtypes = [ctypes.POINTER(None), uint16_t, uint16_t]
WildMidi_SetCvtOption = _libraries['libWildMidi.so'].WildMidi_SetCvtOption
WildMidi_SetCvtOption.restype = ctypes.c_int32
WildMidi_SetCvtOption.argtypes = [uint16_t, uint16_t]
WildMidi_ConvertToMidi = _libraries['libWildMidi.so'].WildMidi_ConvertToMidi
WildMidi_ConvertToMidi.restype = ctypes.c_int32
WildMidi_ConvertToMidi.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)), ctypes.POINTER(ctypes.c_uint32)]
WildMidi_ConvertBufferToMidi = _libraries['libWildMidi.so'].WildMidi_ConvertBufferToMidi
WildMidi_ConvertBufferToMidi.restype = ctypes.c_int32
WildMidi_ConvertBufferToMidi.argtypes = [ctypes.POINTER(ctypes.c_ubyte), uint32_t, ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)), ctypes.POINTER(ctypes.c_uint32)]
WildMidi_GetInfo = _libraries['libWildMidi.so'].WildMidi_GetInfo
WildMidi_GetInfo.restype = ctypes.POINTER(struct__WM_Info)
WildMidi_GetInfo.argtypes = [ctypes.POINTER(None)]
WildMidi_FastSeek = _libraries['libWildMidi.so'].WildMidi_FastSeek
WildMidi_FastSeek.restype = ctypes.c_int32
WildMidi_FastSeek.argtypes = [ctypes.POINTER(None), ctypes.POINTER(ctypes.c_uint64)]
int8_t = ctypes.c_int8
WildMidi_SongSeek = _libraries['libWildMidi.so'].WildMidi_SongSeek
WildMidi_SongSeek.restype = ctypes.c_int32
WildMidi_SongSeek.argtypes = [ctypes.POINTER(None), int8_t]
WildMidi_Close = _libraries['libWildMidi.so'].WildMidi_Close
WildMidi_Close.restype = ctypes.c_int32
WildMidi_Close.argtypes = [ctypes.POINTER(None)]
WildMidi_Shutdown = _libraries['libWildMidi.so'].WildMidi_Shutdown
WildMidi_Shutdown.restype = ctypes.c_int32
WildMidi_Shutdown.argtypes = []
WildMidi_GetLyric = _libraries['libWildMidi.so'].WildMidi_GetLyric
WildMidi_GetLyric.restype = ctypes.POINTER(ctypes.c_char)
WildMidi_GetLyric.argtypes = [ctypes.POINTER(None)]
WildMidi_GetError = _libraries['libWildMidi.so'].WildMidi_GetError
WildMidi_GetError.restype = ctypes.POINTER(ctypes.c_char)
WildMidi_GetError.argtypes = []
WildMidi_ClearError = _libraries['libWildMidi.so'].WildMidi_ClearError
WildMidi_ClearError.restype = None
WildMidi_ClearError.argtypes = []
__all__ = \
    ['LIBWILDMIDI_VER_MAJOR', 'LIBWILDMIDI_VER_MICRO',
    'LIBWILDMIDI_VER_MINOR', 'WILDMIDI_LIB_H', 'WM_CO_FREQUENCY',
    'WM_CO_XMI_TYPE', 'WM_GS_VERSION', 'WM_MO_ENHANCED_RESAMPLING',
    'WM_MO_LOG_VOLUME', 'WM_MO_LOOP', 'WM_MO_REVERB',
    'WM_MO_ROUNDTEMPO', 'WM_MO_SAVEASTYPE0', 'WM_MO_STRIPSILENCE',
    'WM_MO_TEXTASLYRIC', 'WM_SYMBOL', 'WildMidi_ClearError',
    'WildMidi_Close', 'WildMidi_ConvertBufferToMidi',
    'WildMidi_ConvertToMidi', 'WildMidi_FastSeek',
    'WildMidi_GetError', 'WildMidi_GetInfo', 'WildMidi_GetLyric',
    'WildMidi_GetMidiOutput', 'WildMidi_GetOutput',
    'WildMidi_GetString', 'WildMidi_GetVersion', 'WildMidi_Init',
    'WildMidi_InitVIO', 'WildMidi_MasterVolume', 'WildMidi_Open',
    'WildMidi_OpenBuffer', 'WildMidi_SetCvtOption',
    'WildMidi_SetOption', 'WildMidi_Shutdown', 'WildMidi_SongSeek',
    '_WM_VIO_Allocate', '_WM_VIO_Free', 'int8_t', 'midi',
    'struct__WM_Info', 'struct__WM_VIO', 'uint16_t', 'uint32_t',
    'uint8_t']
