from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/usr/lib/libxmp.so'] = CDLL('/usr/lib/libxmp.so')


def xmp_set_position(p,x): return xmp_control((p), XMP_CTL_POS_SET, (x)) # macro
def xmp_restart_module(p): return xmp_control((p), XMP_CTL_MOD_RESTART) # macro
def xmp_seek_time(p,x): return xmp_control((p), XMP_CTL_SEEK_TIME, (x)) # macro
def xmp_prev_position(p): return xmp_control((p), XMP_CTL_POS_PREV) # macro
XMP_INST_NNA_OFF = 2 # Variable c_int '2'
XMP_INST_DCA_OFF = XMP_INST_NNA_OFF # alias
XMP_INST_NNA_CUT = 0 # Variable c_int '0'
XMP_INST_DCA_CUT = XMP_INST_NNA_CUT # alias
def xmp_channel_mute(p,x,y): return xmp_control((p), XMP_CTL_CH_MUTE, (x), (y)) # macro
def xmp_mixer_amp(p,x): return xmp_control((p), XMP_CTL_MIXER_AMP, (x)) # macro
def xmp_mixer_mix(p,x): return xmp_control((p), XMP_CTL_MIXER_MIX, (x)) # macro
def xmp_next_position(p): return xmp_control((p), XMP_CTL_POS_NEXT) # macro
def xmp_stop_module(p): return xmp_control((p), XMP_CTL_MOD_STOP) # macro
XMP_INST_NNA_FADE = 3 # Variable c_int '3'
XMP_INST_DCA_FADE = XMP_INST_NNA_FADE # alias
XMP_CTL_POS_SET = 2 # Variable c_int '2'
XMP_MAX_KEYS = 121 # Variable c_int '121'
XMP_ENVELOPE_SLOOP = 16 # Variable c_int '16'
XMP_ENVELOPE_LOOP = 4 # Variable c_int '4'
XMP_INST_DCT_NOTE = 1 # Variable c_int '1'
XMP_SAMPLE_16BIT = 1 # Variable c_int '1'
XMP_VERSION = '3.9.4' # Variable STRING '(const char*)"3.9.4"'
XMP_INST_DCT_INST = 3 # Variable c_int '3'
XMP_CTL_POS_NEXT = 0 # Variable c_int '0'
XMP_SAMPLE_LOOP_FULL = 16 # Variable c_int '16'
XMP_ERROR_LOAD = 4 # Variable c_int '4'
XMP_ENVELOPE_CARRY = 32 # Variable c_int '32'
XMP_MAX_MOD_LENGTH = 256 # Variable c_int '256'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
XMP_ENVELOPE_SUS = 2 # Variable c_int '2'
XMP_CTL_MOD_STOP = 3 # Variable c_int '3'
XMP_MIX_NEAREST = 8 # Variable c_int '8'
XMP_KEY_CUT = 130 # Variable c_int '130'
XMP_MAX_ENV_POINTS = 32 # Variable c_int '32'
XMP_INST_DCT_OFF = 0 # Variable c_int '0'
XMP_KEY_OFF = 129 # Variable c_int '129'
XMP_VER_MAJOR = 3 # Variable c_int '3'
XMP_INST_DCT_SMP = 2 # Variable c_int '2'
XMP_MIX_NOFILTER = 16 # Variable c_int '16'
XMP_CTL_POS_PREV = 1 # Variable c_int '1'
XMP_ERROR_INTERNAL = 2 # Variable c_int '2'
XMP_CHANNEL_SYNTH = 1 # Variable c_int '1'
XMP_ERROR_FORMAT = 3 # Variable c_int '3'
XMP_CTL_MOD_RESTART = 4 # Variable c_int '4'
XMP_CTL_SEEK_TIME = 7 # Variable c_int '7'
XMP_NAME_SIZE = 64 # Variable c_int '64'
XMP_VERCODE = 198916 # Variable c_int '198916'
XMP_ERROR_SYSTEM = 6 # Variable c_int '6'
XMP_SAMPLE_SYNTH = 32768 # Variable c_int '32768'
XMP_PERIOD_BASE = 6847 # Variable c_int '6847'
XMP_MIX_8BIT = 1 # Variable c_int '1'
XMP_CTL_MIXER_MIX = 16 # Variable c_int '16'
XMP_END = 1 # Variable c_int '1'
XMP_CTL_CH_MUTE = 8 # Variable c_int '8'
XMP_MIX_MONO = 4 # Variable c_int '4'
XMP_SAMPLE_LOOP = 2 # Variable c_int '2'
XMP_SAMPLE_LOOP_BIDIR = 4 # Variable c_int '4'
XMP_INST_NNA_CONT = 1 # Variable c_int '1'
XMP_VER_MINOR = 9 # Variable c_int '9'
XMP_ENVELOPE_FLT = 8 # Variable c_int '8'
XMP_ERROR_DEPACK = 5 # Variable c_int '5'
XMP_ENVELOPE_ON = 1 # Variable c_int '1'
XMP_MAX_CHANNELS = 64 # Variable c_int '64'
XMP_VER_RELEASE = 4 # Variable c_int '4'
XMP_CHANNEL_MUTE = 2 # Variable c_int '2'
XMP_MIX_UNSIGNED = 2 # Variable c_int '2'
XMP_KEY_FADE = 131 # Variable c_int '131'
XMP_CTL_MIXER_AMP = 9 # Variable c_int '9'
XMP_SAMPLE_LOOP_REVERSE = 8 # Variable c_int '8'
class xmp_channel(Structure):
    pass
xmp_channel._fields_ = [
    ('pan', c_int),
    ('vol', c_int),
    ('flg', c_int),
]
class xmp_pattern(Structure):
    pass
xmp_pattern._fields_ = [
    ('rows', c_int),
    ('index', c_int * 1),
]
class xmp_event(Structure):
    pass
xmp_event._fields_ = [
    ('note', c_ubyte),
    ('ins', c_ubyte),
    ('vol', c_ubyte),
    ('fxt', c_ubyte),
    ('fxp', c_ubyte),
    ('f2t', c_ubyte),
    ('f2p', c_ubyte),
    ('_flag', c_ubyte),
]
class xmp_track(Structure):
    pass
xmp_track._fields_ = [
    ('rows', c_int),
    ('event', xmp_event * 1),
]
class xmp_envelope(Structure):
    pass
xmp_envelope._fields_ = [
    ('flg', c_int),
    ('npt', c_int),
    ('scl', c_int),
    ('sus', c_int),
    ('sue', c_int),
    ('lps', c_int),
    ('lpe', c_int),
    ('data', c_short * 64),
]
class xmp_instrument(Structure):
    pass
class N14xmp_instrument3DOT_0E(Structure):
    pass
N14xmp_instrument3DOT_0E._fields_ = [
    ('ins', c_ubyte),
    ('xpo', c_byte),
]
class xmp_subinstrument(Structure):
    pass
xmp_instrument._fields_ = [
    ('name', c_char * 32),
    ('vol', c_int),
    ('nsm', c_int),
    ('rls', c_int),
    ('aei', xmp_envelope),
    ('pei', xmp_envelope),
    ('fei', xmp_envelope),
    ('vts', c_int),
    ('wts', c_int),
    ('map', N14xmp_instrument3DOT_0E * 121),
    ('sub', POINTER(xmp_subinstrument)),
]
xmp_subinstrument._fields_ = [
    ('vol', c_int),
    ('gvl', c_int),
    ('pan', c_int),
    ('xpo', c_int),
    ('fin', c_int),
    ('vwf', c_int),
    ('vde', c_int),
    ('vra', c_int),
    ('vsw', c_int),
    ('rvv', c_int),
    ('sid', c_int),
    ('nna', c_int),
    ('dct', c_int),
    ('dca', c_int),
    ('ifc', c_int),
    ('ifr', c_int),
    ('hld', c_int),
]
class xmp_sample(Structure):
    pass
xmp_sample._fields_ = [
    ('name', c_char * 32),
    ('len', c_int),
    ('lps', c_int),
    ('lpe', c_int),
    ('flg', c_int),
    ('data', POINTER(c_ubyte)),
]
class xmp_sequence(Structure):
    pass
xmp_sequence._fields_ = [
    ('entry_point', c_int),
    ('duration', c_int),
]
class xmp_module(Structure):
    pass
xmp_module._fields_ = [
    ('name', c_char * 64),
    ('type', c_char * 64),
    ('pat', c_int),
    ('trk', c_int),
    ('chn', c_int),
    ('ins', c_int),
    ('smp', c_int),
    ('spd', c_int),
    ('bpm', c_int),
    ('len', c_int),
    ('rst', c_int),
    ('gvl', c_int),
    ('xxp', POINTER(POINTER(xmp_pattern))),
    ('xxt', POINTER(POINTER(xmp_track))),
    ('xxi', POINTER(xmp_instrument)),
    ('xxs', POINTER(xmp_sample)),
    ('xxc', xmp_channel * 64),
    ('xxo', c_ubyte * 256),
]
class xmp_test_info(Structure):
    pass
xmp_test_info._fields_ = [
    ('name', c_char * 64),
    ('type', c_char * 64),
]
class xmp_module_info(Structure):
    pass
class xmp_channel_info(Structure):
    pass
xmp_channel_info._fields_ = [
    ('period', c_uint),
    ('position', c_uint),
    ('pitchbend', c_short),
    ('note', c_ubyte),
    ('instrument', c_ubyte),
    ('sample', c_ubyte),
    ('volume', c_ubyte),
    ('pan', c_ubyte),
    ('reserved', c_ubyte),
    ('event', xmp_event),
]
xmp_module_info._fields_ = [
    ('order', c_int),
    ('pattern', c_int),
    ('row', c_int),
    ('num_rows', c_int),
    ('frame', c_int),
    ('speed', c_int),
    ('bpm', c_int),
    ('time', c_int),
    ('frame_time', c_int),
    ('total_time', c_int),
    ('buffer', c_void_p),
    ('buffer_size', c_int),
    ('total_size', c_int),
    ('volume', c_int),
    ('loop_count', c_int),
    ('virt_channels', c_int),
    ('virt_used', c_int),
    ('vol_base', c_int),
    ('channel_info', xmp_channel_info * 64),
    ('mod', POINTER(xmp_module)),
    ('comment', STRING),
    ('sequence', c_int),
    ('num_sequences', c_int),
    ('seq_data', POINTER(xmp_sequence)),
]
xmp_context = c_void_p
xmp_version = (STRING).in_dll(_libraries['/usr/lib/libxmp.so'], 'xmp_version')
xmp_vercode = (c_uint).in_dll(_libraries['/usr/lib/libxmp.so'], 'xmp_vercode')
xmp_create_context = _libraries['/usr/lib/libxmp.so'].xmp_create_context
xmp_create_context.restype = xmp_context
xmp_create_context.argtypes = []
xmp_test_module = _libraries['/usr/lib/libxmp.so'].xmp_test_module
xmp_test_module.restype = c_int
xmp_test_module.argtypes = [STRING, POINTER(xmp_test_info)]
xmp_free_context = _libraries['/usr/lib/libxmp.so'].xmp_free_context
xmp_free_context.restype = None
xmp_free_context.argtypes = [xmp_context]
xmp_load_module = _libraries['/usr/lib/libxmp.so'].xmp_load_module
xmp_load_module.restype = c_int
xmp_load_module.argtypes = [xmp_context, STRING]
xmp_release_module = _libraries['/usr/lib/libxmp.so'].xmp_release_module
xmp_release_module.restype = None
xmp_release_module.argtypes = [xmp_context]
xmp_player_start = _libraries['/usr/lib/libxmp.so'].xmp_player_start
xmp_player_start.restype = c_int
xmp_player_start.argtypes = [xmp_context, c_int, c_int]
xmp_player_frame = _libraries['/usr/lib/libxmp.so'].xmp_player_frame
xmp_player_frame.restype = c_int
xmp_player_frame.argtypes = [xmp_context]
xmp_player_get_info = _libraries['/usr/lib/libxmp.so'].xmp_player_get_info
xmp_player_get_info.restype = None
xmp_player_get_info.argtypes = [xmp_context, POINTER(xmp_module_info)]
xmp_player_end = _libraries['/usr/lib/libxmp.so'].xmp_player_end
xmp_player_end.restype = None
xmp_player_end.argtypes = [xmp_context]
xmp_inject_event = _libraries['/usr/lib/libxmp.so'].xmp_inject_event
xmp_inject_event.restype = None
xmp_inject_event.argtypes = [xmp_context, c_int, POINTER(xmp_event)]
xmp_get_format_list = _libraries['/usr/lib/libxmp.so'].xmp_get_format_list
xmp_get_format_list.restype = POINTER(STRING)
xmp_get_format_list.argtypes = []
xmp_control = _libraries['/usr/lib/libxmp.so'].xmp_control
xmp_control.restype = c_int
xmp_control.argtypes = [xmp_context, c_int]
__all__ = ['XMP_MAX_KEYS', 'XMP_INST_DCA_OFF', 'xmp_mixer_amp',
           'XMP_SAMPLE_LOOP_FULL', 'XMP_CTL_SEEK_TIME',
           'xmp_free_context', 'xmp_control', 'XMP_INST_DCT_OFF',
           'xmp_test_module', 'XMP_ENVELOPE_LOOP', 'xmp_player_start',
           'XMP_NAME_SIZE', 'XMP_ERROR_SYSTEM', 'XMP_SAMPLE_SYNTH',
           'XMP_SAMPLE_LOOP_BIDIR', 'XMP_END', 'XMP_INST_NNA_FADE',
           'xmp_channel', 'XMP_MIX_MONO', 'xmp_player_get_info',
           'XMP_INST_NNA_CONT', 'N14xmp_instrument3DOT_0E',
           'XMP_KEY_CUT', 'xmp_channel_info', 'XMP_MAX_CHANNELS',
           'XMP_CHANNEL_MUTE', 'XMP_MIX_UNSIGNED', 'xmp_module',
           'XMP_CTL_POS_SET', 'xmp_module_info', 'xmp_instrument',
           'xmp_sample', 'XMP_MAX_MOD_LENGTH', 'XMP_ENVELOPE_SUS',
           'xmp_create_context', 'XMP_VER_MAJOR', 'XMP_INST_DCT_SMP',
           'XMP_CTL_POS_PREV', 'xmp_player_end', 'XMP_INST_NNA_CUT',
           'XMP_CTL_MOD_RESTART', 'xmp_envelope', 'xmp_mixer_mix',
           'XMP_PERIOD_BASE', 'XMP_CTL_MIXER_MIX', 'XMP_SAMPLE_LOOP',
           'xmp_get_format_list', 'XMP_ENVELOPE_ON',
           'XMP_CHANNEL_SYNTH', 'xmp_test_info', 'XMP_ERROR_INTERNAL',
           'xmp_track', 'xmp_restart_module', 'XMP_CTL_POS_NEXT',
           'xmp_seek_time', 'XMP_ERROR_LOAD', 'XMP_ENVELOPE_CARRY',
           'XMP_INST_DCA_CUT', 'XMP_CTL_MOD_STOP', 'XMP_MIX_NEAREST',
           'xmp_pattern', 'XMP_INST_DCA_FADE', 'XMP_INST_NNA_OFF',
           'xmp_release_module', 'XMP_ERROR_FORMAT',
           'xmp_player_frame', 'xmp_vercode', 'xmp_version',
           'XMP_SAMPLE_16BIT', 'xmp_subinstrument',
           'XMP_ENVELOPE_FLT', 'XMP_ERROR_DEPACK', 'XMP_VER_RELEASE',
           'xmp_channel_mute', 'XMP_KEY_FADE', 'XMP_CTL_MIXER_AMP',
           'xmp_set_position', 'XMP_ENVELOPE_SLOOP',
           'xmp_stop_module', 'XMP_INST_DCT_NOTE', 'xmp_event',
           'xmp_sequence', 'XMP_VERSION', 'XMP_INST_DCT_INST',
           '__STDC_CONSTANT_MACROS', 'XMP_MAX_ENV_POINTS',
           'XMP_MIX_NOFILTER', 'XMP_KEY_OFF', 'xmp_prev_position',
           'XMP_VERCODE', 'XMP_MIX_8BIT', 'xmp_inject_event',
           'XMP_CTL_CH_MUTE', 'xmp_load_module', 'XMP_VER_MINOR',
           'xmp_context', 'xmp_next_position',
           'XMP_SAMPLE_LOOP_REVERSE']
