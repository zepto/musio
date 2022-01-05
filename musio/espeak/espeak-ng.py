# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I/usr/lib/clang/13.0.0/include']
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
_libraries['libespeak-ng.so'] = ctypes.CDLL('/usr/lib/libespeak-ng.so')


ESPEAK_NG_H = True # macro
SPEAK_LIB_H = True # macro
ESPEAK_API = True # macro
ESPEAK_API_REVISION = 12 # macro
espeakRATE_MINIMUM = 80 # macro
espeakRATE_MAXIMUM = 450 # macro
espeakRATE_NORMAL = 175 # macro
espeakINITIALIZE_PHONEME_EVENTS = 0x0001 # macro
espeakINITIALIZE_PHONEME_IPA = 0x0002 # macro
espeakINITIALIZE_DONT_EXIT = 0x8000 # macro
espeakCHARS_AUTO = 0 # macro
espeakCHARS_UTF8 = 1 # macro
espeakCHARS_8BIT = 2 # macro
espeakCHARS_WCHAR = 3 # macro
espeakCHARS_16BIT = 4 # macro
espeakSSML = 0x10 # macro
espeakPHONEMES = 0x100 # macro
espeakENDPAUSE = 0x1000 # macro
espeakKEEP_NAMEDATA = 0x2000 # macro
espeakPHONEMES_SHOW = 0x01 # macro
espeakPHONEMES_IPA = 0x02 # macro
espeakPHONEMES_TRACE = 0x08 # macro
espeakPHONEMES_MBROLA = 0x10 # macro
espeakPHONEMES_TIE = 0x80 # macro
ESPEAK_NG_API = True # macro
ESPEAKNG_DEFAULT_VOICE = "en" # macro

# values for enumeration 'c__EA_espeak_EVENT_TYPE'
c__EA_espeak_EVENT_TYPE__enumvalues = {
    0: 'espeakEVENT_LIST_TERMINATED',
    1: 'espeakEVENT_WORD',
    2: 'espeakEVENT_SENTENCE',
    3: 'espeakEVENT_MARK',
    4: 'espeakEVENT_PLAY',
    5: 'espeakEVENT_END',
    6: 'espeakEVENT_MSG_TERMINATED',
    7: 'espeakEVENT_PHONEME',
    8: 'espeakEVENT_SAMPLERATE',
}
espeakEVENT_LIST_TERMINATED = 0
espeakEVENT_WORD = 1
espeakEVENT_SENTENCE = 2
espeakEVENT_MARK = 3
espeakEVENT_PLAY = 4
espeakEVENT_END = 5
espeakEVENT_MSG_TERMINATED = 6
espeakEVENT_PHONEME = 7
espeakEVENT_SAMPLERATE = 8
c__EA_espeak_EVENT_TYPE = ctypes.c_uint32 # enum
espeak_EVENT_TYPE = c__EA_espeak_EVENT_TYPE
espeak_EVENT_TYPE__enumvalues = c__EA_espeak_EVENT_TYPE__enumvalues
class struct_c__SA_espeak_EVENT(Structure):
    pass

class union_c__SA_espeak_EVENT_0(Union):
    pass

union_c__SA_espeak_EVENT_0._pack_ = 1 # source:False
union_c__SA_espeak_EVENT_0._fields_ = [
    ('number', ctypes.c_int32),
    ('name', ctypes.POINTER(ctypes.c_char)),
    ('string', ctypes.c_char * 8),
]

struct_c__SA_espeak_EVENT._pack_ = 1 # source:False
struct_c__SA_espeak_EVENT._fields_ = [
    ('type', espeak_EVENT_TYPE),
    ('unique_identifier', ctypes.c_uint32),
    ('text_position', ctypes.c_int32),
    ('length', ctypes.c_int32),
    ('audio_position', ctypes.c_int32),
    ('sample', ctypes.c_int32),
    ('user_data', ctypes.POINTER(None)),
    ('id', union_c__SA_espeak_EVENT_0),
]

espeak_EVENT = struct_c__SA_espeak_EVENT

# values for enumeration 'c__EA_espeak_POSITION_TYPE'
c__EA_espeak_POSITION_TYPE__enumvalues = {
    1: 'POS_CHARACTER',
    2: 'POS_WORD',
    3: 'POS_SENTENCE',
}
POS_CHARACTER = 1
POS_WORD = 2
POS_SENTENCE = 3
c__EA_espeak_POSITION_TYPE = ctypes.c_uint32 # enum
espeak_POSITION_TYPE = c__EA_espeak_POSITION_TYPE
espeak_POSITION_TYPE__enumvalues = c__EA_espeak_POSITION_TYPE__enumvalues

# values for enumeration 'c__EA_espeak_AUDIO_OUTPUT'
c__EA_espeak_AUDIO_OUTPUT__enumvalues = {
    0: 'AUDIO_OUTPUT_PLAYBACK',
    1: 'AUDIO_OUTPUT_RETRIEVAL',
    2: 'AUDIO_OUTPUT_SYNCHRONOUS',
    3: 'AUDIO_OUTPUT_SYNCH_PLAYBACK',
}
AUDIO_OUTPUT_PLAYBACK = 0
AUDIO_OUTPUT_RETRIEVAL = 1
AUDIO_OUTPUT_SYNCHRONOUS = 2
AUDIO_OUTPUT_SYNCH_PLAYBACK = 3
c__EA_espeak_AUDIO_OUTPUT = ctypes.c_uint32 # enum
espeak_AUDIO_OUTPUT = c__EA_espeak_AUDIO_OUTPUT
espeak_AUDIO_OUTPUT__enumvalues = c__EA_espeak_AUDIO_OUTPUT__enumvalues

# values for enumeration 'c__EA_espeak_ERROR'
c__EA_espeak_ERROR__enumvalues = {
    0: 'EE_OK',
    -1: 'EE_INTERNAL_ERROR',
    1: 'EE_BUFFER_FULL',
    2: 'EE_NOT_FOUND',
}
EE_OK = 0
EE_INTERNAL_ERROR = -1
EE_BUFFER_FULL = 1
EE_NOT_FOUND = 2
c__EA_espeak_ERROR = ctypes.c_int32 # enum
espeak_ERROR = c__EA_espeak_ERROR
espeak_ERROR__enumvalues = c__EA_espeak_ERROR__enumvalues
espeak_Initialize = _libraries['libespeak-ng.so'].espeak_Initialize
espeak_Initialize.restype = ctypes.c_int32
espeak_Initialize.argtypes = [espeak_AUDIO_OUTPUT, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_int32]
t_espeak_callback = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(ctypes.c_int16), ctypes.c_int32, ctypes.POINTER(struct_c__SA_espeak_EVENT))
espeak_SetSynthCallback = _libraries['libespeak-ng.so'].espeak_SetSynthCallback
espeak_SetSynthCallback.restype = None
espeak_SetSynthCallback.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(ctypes.c_int16), ctypes.c_int32, ctypes.POINTER(struct_c__SA_espeak_EVENT))]
espeak_SetUriCallback = _libraries['libespeak-ng.so'].espeak_SetUriCallback
espeak_SetUriCallback.restype = None
espeak_SetUriCallback.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char))]
espeak_SetPhonemeCallback = _libraries['libespeak-ng.so'].espeak_SetPhonemeCallback
espeak_SetPhonemeCallback.restype = None
espeak_SetPhonemeCallback.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(ctypes.c_char))]
size_t = ctypes.c_uint64
espeak_Synth = _libraries['libespeak-ng.so'].espeak_Synth
espeak_Synth.restype = espeak_ERROR
espeak_Synth.argtypes = [ctypes.POINTER(None), size_t, ctypes.c_uint32, espeak_POSITION_TYPE, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(None)]
espeak_Synth_Mark = _libraries['libespeak-ng.so'].espeak_Synth_Mark
espeak_Synth_Mark.restype = espeak_ERROR
espeak_Synth_Mark.argtypes = [ctypes.POINTER(None), size_t, ctypes.POINTER(ctypes.c_char), ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(None)]
espeak_Key = _libraries['libespeak-ng.so'].espeak_Key
espeak_Key.restype = espeak_ERROR
espeak_Key.argtypes = [ctypes.POINTER(ctypes.c_char)]
wchar_t = ctypes.c_int32
espeak_Char = _libraries['libespeak-ng.so'].espeak_Char
espeak_Char.restype = espeak_ERROR
espeak_Char.argtypes = [wchar_t]

# values for enumeration 'c__EA_espeak_PARAMETER'
c__EA_espeak_PARAMETER__enumvalues = {
    0: 'espeakSILENCE',
    1: 'espeakRATE',
    2: 'espeakVOLUME',
    3: 'espeakPITCH',
    4: 'espeakRANGE',
    5: 'espeakPUNCTUATION',
    6: 'espeakCAPITALS',
    7: 'espeakWORDGAP',
    8: 'espeakOPTIONS',
    9: 'espeakINTONATION',
    10: 'espeakRESERVED1',
    11: 'espeakRESERVED2',
    12: 'espeakEMPHASIS',
    13: 'espeakLINELENGTH',
    14: 'espeakVOICETYPE',
    15: 'N_SPEECH_PARAM',
}
espeakSILENCE = 0
espeakRATE = 1
espeakVOLUME = 2
espeakPITCH = 3
espeakRANGE = 4
espeakPUNCTUATION = 5
espeakCAPITALS = 6
espeakWORDGAP = 7
espeakOPTIONS = 8
espeakINTONATION = 9
espeakRESERVED1 = 10
espeakRESERVED2 = 11
espeakEMPHASIS = 12
espeakLINELENGTH = 13
espeakVOICETYPE = 14
N_SPEECH_PARAM = 15
c__EA_espeak_PARAMETER = ctypes.c_uint32 # enum
espeak_PARAMETER = c__EA_espeak_PARAMETER
espeak_PARAMETER__enumvalues = c__EA_espeak_PARAMETER__enumvalues

# values for enumeration 'c__EA_espeak_PUNCT_TYPE'
c__EA_espeak_PUNCT_TYPE__enumvalues = {
    0: 'espeakPUNCT_NONE',
    1: 'espeakPUNCT_ALL',
    2: 'espeakPUNCT_SOME',
}
espeakPUNCT_NONE = 0
espeakPUNCT_ALL = 1
espeakPUNCT_SOME = 2
c__EA_espeak_PUNCT_TYPE = ctypes.c_uint32 # enum
espeak_PUNCT_TYPE = c__EA_espeak_PUNCT_TYPE
espeak_PUNCT_TYPE__enumvalues = c__EA_espeak_PUNCT_TYPE__enumvalues
espeak_SetParameter = _libraries['libespeak-ng.so'].espeak_SetParameter
espeak_SetParameter.restype = espeak_ERROR
espeak_SetParameter.argtypes = [espeak_PARAMETER, ctypes.c_int32, ctypes.c_int32]
espeak_GetParameter = _libraries['libespeak-ng.so'].espeak_GetParameter
espeak_GetParameter.restype = ctypes.c_int32
espeak_GetParameter.argtypes = [espeak_PARAMETER, ctypes.c_int32]
espeak_SetPunctuationList = _libraries['libespeak-ng.so'].espeak_SetPunctuationList
espeak_SetPunctuationList.restype = espeak_ERROR
espeak_SetPunctuationList.argtypes = [ctypes.POINTER(ctypes.c_int32)]
class struct__IO_FILE(Structure):
    pass

class struct__IO_wide_data(Structure):
    pass

class struct__IO_codecvt(Structure):
    pass

class struct__IO_marker(Structure):
    pass

struct__IO_FILE._pack_ = 1 # source:False
struct__IO_FILE._fields_ = [
    ('_flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('_IO_read_ptr', ctypes.POINTER(ctypes.c_char)),
    ('_IO_read_end', ctypes.POINTER(ctypes.c_char)),
    ('_IO_read_base', ctypes.POINTER(ctypes.c_char)),
    ('_IO_write_base', ctypes.POINTER(ctypes.c_char)),
    ('_IO_write_ptr', ctypes.POINTER(ctypes.c_char)),
    ('_IO_write_end', ctypes.POINTER(ctypes.c_char)),
    ('_IO_buf_base', ctypes.POINTER(ctypes.c_char)),
    ('_IO_buf_end', ctypes.POINTER(ctypes.c_char)),
    ('_IO_save_base', ctypes.POINTER(ctypes.c_char)),
    ('_IO_backup_base', ctypes.POINTER(ctypes.c_char)),
    ('_IO_save_end', ctypes.POINTER(ctypes.c_char)),
    ('_markers', ctypes.POINTER(struct__IO_marker)),
    ('_chain', ctypes.POINTER(struct__IO_FILE)),
    ('_fileno', ctypes.c_int32),
    ('_flags2', ctypes.c_int32),
    ('_old_offset', ctypes.c_int64),
    ('_cur_column', ctypes.c_uint16),
    ('_vtable_offset', ctypes.c_byte),
    ('_shortbuf', ctypes.c_char * 1),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('_lock', ctypes.POINTER(None)),
    ('_offset', ctypes.c_int64),
    ('_codecvt', ctypes.POINTER(struct__IO_codecvt)),
    ('_wide_data', ctypes.POINTER(struct__IO_wide_data)),
    ('_freeres_list', ctypes.POINTER(struct__IO_FILE)),
    ('_freeres_buf', ctypes.POINTER(None)),
    ('__pad5', ctypes.c_uint64),
    ('_mode', ctypes.c_int32),
    ('_unused2', ctypes.c_char * 20),
]

espeak_SetPhonemeTrace = _libraries['libespeak-ng.so'].espeak_SetPhonemeTrace
espeak_SetPhonemeTrace.restype = None
espeak_SetPhonemeTrace.argtypes = [ctypes.c_int32, ctypes.POINTER(struct__IO_FILE)]
espeak_TextToPhonemes = _libraries['libespeak-ng.so'].espeak_TextToPhonemes
espeak_TextToPhonemes.restype = ctypes.POINTER(ctypes.c_char)
espeak_TextToPhonemes.argtypes = [ctypes.POINTER(ctypes.POINTER(None)), ctypes.c_int32, ctypes.c_int32]
espeak_CompileDictionary = _libraries['libespeak-ng.so'].espeak_CompileDictionary
espeak_CompileDictionary.restype = None
espeak_CompileDictionary.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(struct__IO_FILE), ctypes.c_int32]
class struct_c__SA_espeak_VOICE(Structure):
    pass

struct_c__SA_espeak_VOICE._pack_ = 1 # source:False
struct_c__SA_espeak_VOICE._fields_ = [
    ('name', ctypes.POINTER(ctypes.c_char)),
    ('languages', ctypes.POINTER(ctypes.c_char)),
    ('identifier', ctypes.POINTER(ctypes.c_char)),
    ('gender', ctypes.c_ubyte),
    ('age', ctypes.c_ubyte),
    ('variant', ctypes.c_ubyte),
    ('xx1', ctypes.c_ubyte),
    ('score', ctypes.c_int32),
    ('spare', ctypes.POINTER(None)),
]

espeak_VOICE = struct_c__SA_espeak_VOICE
espeak_ListVoices = _libraries['libespeak-ng.so'].espeak_ListVoices
espeak_ListVoices.restype = ctypes.POINTER(ctypes.POINTER(struct_c__SA_espeak_VOICE))
espeak_ListVoices.argtypes = [ctypes.POINTER(struct_c__SA_espeak_VOICE)]
espeak_SetVoiceByFile = _libraries['libespeak-ng.so'].espeak_SetVoiceByFile
espeak_SetVoiceByFile.restype = espeak_ERROR
espeak_SetVoiceByFile.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_SetVoiceByName = _libraries['libespeak-ng.so'].espeak_SetVoiceByName
espeak_SetVoiceByName.restype = espeak_ERROR
espeak_SetVoiceByName.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_SetVoiceByProperties = _libraries['libespeak-ng.so'].espeak_SetVoiceByProperties
espeak_SetVoiceByProperties.restype = espeak_ERROR
espeak_SetVoiceByProperties.argtypes = [ctypes.POINTER(struct_c__SA_espeak_VOICE)]
espeak_GetCurrentVoice = _libraries['libespeak-ng.so'].espeak_GetCurrentVoice
espeak_GetCurrentVoice.restype = ctypes.POINTER(struct_c__SA_espeak_VOICE)
espeak_GetCurrentVoice.argtypes = []
espeak_Cancel = _libraries['libespeak-ng.so'].espeak_Cancel
espeak_Cancel.restype = espeak_ERROR
espeak_Cancel.argtypes = []
espeak_IsPlaying = _libraries['libespeak-ng.so'].espeak_IsPlaying
espeak_IsPlaying.restype = ctypes.c_int32
espeak_IsPlaying.argtypes = []
espeak_Synchronize = _libraries['libespeak-ng.so'].espeak_Synchronize
espeak_Synchronize.restype = espeak_ERROR
espeak_Synchronize.argtypes = []
espeak_Terminate = _libraries['libespeak-ng.so'].espeak_Terminate
espeak_Terminate.restype = espeak_ERROR
espeak_Terminate.argtypes = []
espeak_Info = _libraries['libespeak-ng.so'].espeak_Info
espeak_Info.restype = ctypes.POINTER(ctypes.c_char)
espeak_Info.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_char))]

# values for enumeration 'c__EA_espeak_ng_STATUS'
c__EA_espeak_ng_STATUS__enumvalues = {
    1879048192: 'ENS_GROUP_MASK',
    0: 'ENS_GROUP_ERRNO',
    268435456: 'ENS_GROUP_ESPEAK_NG',
    0: 'ENS_OK',
    268435967: 'ENS_COMPILE_ERROR',
    268436223: 'ENS_VERSION_MISMATCH',
    268436479: 'ENS_FIFO_BUFFER_FULL',
    268436735: 'ENS_NOT_INITIALIZED',
    268436991: 'ENS_AUDIO_ERROR',
    268437247: 'ENS_VOICE_NOT_FOUND',
    268437503: 'ENS_MBROLA_NOT_FOUND',
    268437759: 'ENS_MBROLA_VOICE_NOT_FOUND',
    268438015: 'ENS_EVENT_BUFFER_FULL',
    268438271: 'ENS_NOT_SUPPORTED',
    268438527: 'ENS_UNSUPPORTED_PHON_FORMAT',
    268438783: 'ENS_NO_SPECT_FRAMES',
    268439039: 'ENS_EMPTY_PHONEME_MANIFEST',
    268439295: 'ENS_SPEECH_STOPPED',
    268439551: 'ENS_UNKNOWN_PHONEME_FEATURE',
    268439807: 'ENS_UNKNOWN_TEXT_ENCODING',
}
ENS_GROUP_MASK = 1879048192
ENS_GROUP_ERRNO = 0
ENS_GROUP_ESPEAK_NG = 268435456
ENS_OK = 0
ENS_COMPILE_ERROR = 268435967
ENS_VERSION_MISMATCH = 268436223
ENS_FIFO_BUFFER_FULL = 268436479
ENS_NOT_INITIALIZED = 268436735
ENS_AUDIO_ERROR = 268436991
ENS_VOICE_NOT_FOUND = 268437247
ENS_MBROLA_NOT_FOUND = 268437503
ENS_MBROLA_VOICE_NOT_FOUND = 268437759
ENS_EVENT_BUFFER_FULL = 268438015
ENS_NOT_SUPPORTED = 268438271
ENS_UNSUPPORTED_PHON_FORMAT = 268438527
ENS_NO_SPECT_FRAMES = 268438783
ENS_EMPTY_PHONEME_MANIFEST = 268439039
ENS_SPEECH_STOPPED = 268439295
ENS_UNKNOWN_PHONEME_FEATURE = 268439551
ENS_UNKNOWN_TEXT_ENCODING = 268439807
c__EA_espeak_ng_STATUS = ctypes.c_uint32 # enum
espeak_ng_STATUS = c__EA_espeak_ng_STATUS
espeak_ng_STATUS__enumvalues = c__EA_espeak_ng_STATUS__enumvalues

# values for enumeration 'c__EA_espeak_ng_OUTPUT_MODE'
c__EA_espeak_ng_OUTPUT_MODE__enumvalues = {
    1: 'ENOUTPUT_MODE_SYNCHRONOUS',
    2: 'ENOUTPUT_MODE_SPEAK_AUDIO',
}
ENOUTPUT_MODE_SYNCHRONOUS = 1
ENOUTPUT_MODE_SPEAK_AUDIO = 2
c__EA_espeak_ng_OUTPUT_MODE = ctypes.c_uint32 # enum
espeak_ng_OUTPUT_MODE = c__EA_espeak_ng_OUTPUT_MODE
espeak_ng_OUTPUT_MODE__enumvalues = c__EA_espeak_ng_OUTPUT_MODE__enumvalues

# values for enumeration 'c__EA_espeak_ng_VOICE_GENDER'
c__EA_espeak_ng_VOICE_GENDER__enumvalues = {
    0: 'ENGENDER_UNKNOWN',
    1: 'ENGENDER_MALE',
    2: 'ENGENDER_FEMALE',
    3: 'ENGENDER_NEUTRAL',
}
ENGENDER_UNKNOWN = 0
ENGENDER_MALE = 1
ENGENDER_FEMALE = 2
ENGENDER_NEUTRAL = 3
c__EA_espeak_ng_VOICE_GENDER = ctypes.c_uint32 # enum
espeak_ng_VOICE_GENDER = c__EA_espeak_ng_VOICE_GENDER
espeak_ng_VOICE_GENDER__enumvalues = c__EA_espeak_ng_VOICE_GENDER__enumvalues
class struct_espeak_ng_ERROR_CONTEXT_(Structure):
    pass

espeak_ng_ERROR_CONTEXT = ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_)
espeak_ng_ClearErrorContext = _libraries['libespeak-ng.so'].espeak_ng_ClearErrorContext
espeak_ng_ClearErrorContext.restype = None
espeak_ng_ClearErrorContext.argtypes = [ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_GetStatusCodeMessage = _libraries['libespeak-ng.so'].espeak_ng_GetStatusCodeMessage
espeak_ng_GetStatusCodeMessage.restype = None
espeak_ng_GetStatusCodeMessage.argtypes = [espeak_ng_STATUS, ctypes.POINTER(ctypes.c_char), size_t]
espeak_ng_PrintStatusCodeMessage = _libraries['libespeak-ng.so'].espeak_ng_PrintStatusCodeMessage
espeak_ng_PrintStatusCodeMessage.restype = None
espeak_ng_PrintStatusCodeMessage.argtypes = [espeak_ng_STATUS, ctypes.POINTER(struct__IO_FILE), espeak_ng_ERROR_CONTEXT]
espeak_ng_InitializePath = _libraries['libespeak-ng.so'].espeak_ng_InitializePath
espeak_ng_InitializePath.restype = None
espeak_ng_InitializePath.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_ng_Initialize = _libraries['libespeak-ng.so'].espeak_ng_Initialize
espeak_ng_Initialize.restype = espeak_ng_STATUS
espeak_ng_Initialize.argtypes = [ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_InitializeOutput = _libraries['libespeak-ng.so'].espeak_ng_InitializeOutput
espeak_ng_InitializeOutput.restype = espeak_ng_STATUS
espeak_ng_InitializeOutput.argtypes = [espeak_ng_OUTPUT_MODE, ctypes.c_int32, ctypes.POINTER(ctypes.c_char)]
espeak_ng_GetSampleRate = _libraries['libespeak-ng.so'].espeak_ng_GetSampleRate
espeak_ng_GetSampleRate.restype = ctypes.c_int32
espeak_ng_GetSampleRate.argtypes = []
espeak_ng_SetParameter = _libraries['libespeak-ng.so'].espeak_ng_SetParameter
espeak_ng_SetParameter.restype = espeak_ng_STATUS
espeak_ng_SetParameter.argtypes = [espeak_PARAMETER, ctypes.c_int32, ctypes.c_int32]
espeak_ng_SetPunctuationList = _libraries['libespeak-ng.so'].espeak_ng_SetPunctuationList
espeak_ng_SetPunctuationList.restype = espeak_ng_STATUS
espeak_ng_SetPunctuationList.argtypes = [ctypes.POINTER(ctypes.c_int32)]
espeak_ng_SetVoiceByName = _libraries['libespeak-ng.so'].espeak_ng_SetVoiceByName
espeak_ng_SetVoiceByName.restype = espeak_ng_STATUS
espeak_ng_SetVoiceByName.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_ng_SetVoiceByFile = _libraries['libespeak-ng.so'].espeak_ng_SetVoiceByFile
espeak_ng_SetVoiceByFile.restype = espeak_ng_STATUS
espeak_ng_SetVoiceByFile.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_ng_SetVoiceByProperties = _libraries['libespeak-ng.so'].espeak_ng_SetVoiceByProperties
espeak_ng_SetVoiceByProperties.restype = espeak_ng_STATUS
espeak_ng_SetVoiceByProperties.argtypes = [ctypes.POINTER(struct_c__SA_espeak_VOICE)]
espeak_ng_Synthesize = _libraries['libespeak-ng.so'].espeak_ng_Synthesize
espeak_ng_Synthesize.restype = espeak_ng_STATUS
espeak_ng_Synthesize.argtypes = [ctypes.POINTER(None), size_t, ctypes.c_uint32, espeak_POSITION_TYPE, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(None)]
espeak_ng_SynthesizeMark = _libraries['libespeak-ng.so'].espeak_ng_SynthesizeMark
espeak_ng_SynthesizeMark.restype = espeak_ng_STATUS
espeak_ng_SynthesizeMark.argtypes = [ctypes.POINTER(None), size_t, ctypes.POINTER(ctypes.c_char), ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(None)]
espeak_ng_SpeakKeyName = _libraries['libespeak-ng.so'].espeak_ng_SpeakKeyName
espeak_ng_SpeakKeyName.restype = espeak_ng_STATUS
espeak_ng_SpeakKeyName.argtypes = [ctypes.POINTER(ctypes.c_char)]
espeak_ng_SpeakCharacter = _libraries['libespeak-ng.so'].espeak_ng_SpeakCharacter
espeak_ng_SpeakCharacter.restype = espeak_ng_STATUS
espeak_ng_SpeakCharacter.argtypes = [wchar_t]
espeak_ng_Cancel = _libraries['libespeak-ng.so'].espeak_ng_Cancel
espeak_ng_Cancel.restype = espeak_ng_STATUS
espeak_ng_Cancel.argtypes = []
espeak_ng_Synchronize = _libraries['libespeak-ng.so'].espeak_ng_Synchronize
espeak_ng_Synchronize.restype = espeak_ng_STATUS
espeak_ng_Synchronize.argtypes = []
espeak_ng_Terminate = _libraries['libespeak-ng.so'].espeak_ng_Terminate
espeak_ng_Terminate.restype = espeak_ng_STATUS
espeak_ng_Terminate.argtypes = []
espeak_ng_CompileDictionary = _libraries['libespeak-ng.so'].espeak_ng_CompileDictionary
espeak_ng_CompileDictionary.restype = espeak_ng_STATUS
espeak_ng_CompileDictionary.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(struct__IO_FILE), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_CompileMbrolaVoice = _libraries['libespeak-ng.so'].espeak_ng_CompileMbrolaVoice
espeak_ng_CompileMbrolaVoice.restype = espeak_ng_STATUS
espeak_ng_CompileMbrolaVoice.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(struct__IO_FILE), ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_CompilePhonemeData = _libraries['libespeak-ng.so'].espeak_ng_CompilePhonemeData
espeak_ng_CompilePhonemeData.restype = espeak_ng_STATUS
espeak_ng_CompilePhonemeData.argtypes = [ctypes.c_int64, ctypes.POINTER(struct__IO_FILE), ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_CompileIntonation = _libraries['libespeak-ng.so'].espeak_ng_CompileIntonation
espeak_ng_CompileIntonation.restype = espeak_ng_STATUS
espeak_ng_CompileIntonation.argtypes = [ctypes.POINTER(struct__IO_FILE), ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
espeak_ng_CompilePhonemeDataPath = _libraries['libespeak-ng.so'].espeak_ng_CompilePhonemeDataPath
espeak_ng_CompilePhonemeDataPath.restype = espeak_ng_STATUS
espeak_ng_CompilePhonemeDataPath.argtypes = [ctypes.c_int64, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(struct__IO_FILE), ctypes.POINTER(ctypes.POINTER(struct_espeak_ng_ERROR_CONTEXT_))]
__all__ = \
    ['AUDIO_OUTPUT_PLAYBACK', 'AUDIO_OUTPUT_RETRIEVAL',
    'AUDIO_OUTPUT_SYNCHRONOUS', 'AUDIO_OUTPUT_SYNCH_PLAYBACK',
    'EE_BUFFER_FULL', 'EE_INTERNAL_ERROR', 'EE_NOT_FOUND', 'EE_OK',
    'ENGENDER_FEMALE', 'ENGENDER_MALE', 'ENGENDER_NEUTRAL',
    'ENGENDER_UNKNOWN', 'ENOUTPUT_MODE_SPEAK_AUDIO',
    'ENOUTPUT_MODE_SYNCHRONOUS', 'ENS_AUDIO_ERROR',
    'ENS_COMPILE_ERROR', 'ENS_EMPTY_PHONEME_MANIFEST',
    'ENS_EVENT_BUFFER_FULL', 'ENS_FIFO_BUFFER_FULL',
    'ENS_GROUP_ERRNO', 'ENS_GROUP_ESPEAK_NG', 'ENS_GROUP_MASK',
    'ENS_MBROLA_NOT_FOUND', 'ENS_MBROLA_VOICE_NOT_FOUND',
    'ENS_NOT_INITIALIZED', 'ENS_NOT_SUPPORTED', 'ENS_NO_SPECT_FRAMES',
    'ENS_OK', 'ENS_SPEECH_STOPPED', 'ENS_UNKNOWN_PHONEME_FEATURE',
    'ENS_UNKNOWN_TEXT_ENCODING', 'ENS_UNSUPPORTED_PHON_FORMAT',
    'ENS_VERSION_MISMATCH', 'ENS_VOICE_NOT_FOUND',
    'ESPEAKNG_DEFAULT_VOICE', 'ESPEAK_API', 'ESPEAK_API_REVISION',
    'ESPEAK_NG_API', 'ESPEAK_NG_H', 'N_SPEECH_PARAM', 'POS_CHARACTER',
    'POS_SENTENCE', 'POS_WORD', 'SPEAK_LIB_H',
    'c__EA_espeak_AUDIO_OUTPUT', 'c__EA_espeak_ERROR',
    'c__EA_espeak_EVENT_TYPE', 'c__EA_espeak_PARAMETER',
    'c__EA_espeak_POSITION_TYPE', 'c__EA_espeak_PUNCT_TYPE',
    'c__EA_espeak_ng_OUTPUT_MODE', 'c__EA_espeak_ng_STATUS',
    'c__EA_espeak_ng_VOICE_GENDER', 'espeakCAPITALS',
    'espeakCHARS_16BIT', 'espeakCHARS_8BIT', 'espeakCHARS_AUTO',
    'espeakCHARS_UTF8', 'espeakCHARS_WCHAR', 'espeakEMPHASIS',
    'espeakENDPAUSE', 'espeakEVENT_END',
    'espeakEVENT_LIST_TERMINATED', 'espeakEVENT_MARK',
    'espeakEVENT_MSG_TERMINATED', 'espeakEVENT_PHONEME',
    'espeakEVENT_PLAY', 'espeakEVENT_SAMPLERATE',
    'espeakEVENT_SENTENCE', 'espeakEVENT_WORD',
    'espeakINITIALIZE_DONT_EXIT', 'espeakINITIALIZE_PHONEME_EVENTS',
    'espeakINITIALIZE_PHONEME_IPA', 'espeakINTONATION',
    'espeakKEEP_NAMEDATA', 'espeakLINELENGTH', 'espeakOPTIONS',
    'espeakPHONEMES', 'espeakPHONEMES_IPA', 'espeakPHONEMES_MBROLA',
    'espeakPHONEMES_SHOW', 'espeakPHONEMES_TIE',
    'espeakPHONEMES_TRACE', 'espeakPITCH', 'espeakPUNCTUATION',
    'espeakPUNCT_ALL', 'espeakPUNCT_NONE', 'espeakPUNCT_SOME',
    'espeakRANGE', 'espeakRATE', 'espeakRATE_MAXIMUM',
    'espeakRATE_MINIMUM', 'espeakRATE_NORMAL', 'espeakRESERVED1',
    'espeakRESERVED2', 'espeakSILENCE', 'espeakSSML',
    'espeakVOICETYPE', 'espeakVOLUME', 'espeakWORDGAP',
    'espeak_AUDIO_OUTPUT', 'espeak_AUDIO_OUTPUT__enumvalues',
    'espeak_Cancel', 'espeak_Char', 'espeak_CompileDictionary',
    'espeak_ERROR', 'espeak_ERROR__enumvalues', 'espeak_EVENT',
    'espeak_EVENT_TYPE', 'espeak_EVENT_TYPE__enumvalues',
    'espeak_GetCurrentVoice', 'espeak_GetParameter', 'espeak_Info',
    'espeak_Initialize', 'espeak_IsPlaying', 'espeak_Key',
    'espeak_ListVoices', 'espeak_PARAMETER',
    'espeak_PARAMETER__enumvalues', 'espeak_POSITION_TYPE',
    'espeak_POSITION_TYPE__enumvalues', 'espeak_PUNCT_TYPE',
    'espeak_PUNCT_TYPE__enumvalues', 'espeak_SetParameter',
    'espeak_SetPhonemeCallback', 'espeak_SetPhonemeTrace',
    'espeak_SetPunctuationList', 'espeak_SetSynthCallback',
    'espeak_SetUriCallback', 'espeak_SetVoiceByFile',
    'espeak_SetVoiceByName', 'espeak_SetVoiceByProperties',
    'espeak_Synchronize', 'espeak_Synth', 'espeak_Synth_Mark',
    'espeak_Terminate', 'espeak_TextToPhonemes', 'espeak_VOICE',
    'espeak_ng_Cancel', 'espeak_ng_ClearErrorContext',
    'espeak_ng_CompileDictionary', 'espeak_ng_CompileIntonation',
    'espeak_ng_CompileMbrolaVoice', 'espeak_ng_CompilePhonemeData',
    'espeak_ng_CompilePhonemeDataPath', 'espeak_ng_ERROR_CONTEXT',
    'espeak_ng_GetSampleRate', 'espeak_ng_GetStatusCodeMessage',
    'espeak_ng_Initialize', 'espeak_ng_InitializeOutput',
    'espeak_ng_InitializePath', 'espeak_ng_OUTPUT_MODE',
    'espeak_ng_OUTPUT_MODE__enumvalues',
    'espeak_ng_PrintStatusCodeMessage', 'espeak_ng_STATUS',
    'espeak_ng_STATUS__enumvalues', 'espeak_ng_SetParameter',
    'espeak_ng_SetPunctuationList', 'espeak_ng_SetVoiceByFile',
    'espeak_ng_SetVoiceByName', 'espeak_ng_SetVoiceByProperties',
    'espeak_ng_SpeakCharacter', 'espeak_ng_SpeakKeyName',
    'espeak_ng_Synchronize', 'espeak_ng_Synthesize',
    'espeak_ng_SynthesizeMark', 'espeak_ng_Terminate',
    'espeak_ng_VOICE_GENDER', 'espeak_ng_VOICE_GENDER__enumvalues',
    'size_t', 'struct__IO_FILE', 'struct__IO_codecvt',
    'struct__IO_marker', 'struct__IO_wide_data',
    'struct_c__SA_espeak_EVENT', 'struct_c__SA_espeak_VOICE',
    'struct_espeak_ng_ERROR_CONTEXT_', 't_espeak_callback',
    'union_c__SA_espeak_EVENT_0', 'wchar_t']
