from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/usr/lib/libxmp.so'] = CDLL('/usr/lib/libxmp.so')


XMP_INST_NNA_FADE = 3 # Variable c_int '3'
XMP_INST_DCA_FADE = XMP_INST_NNA_FADE # alias
XMP_INST_NNA_OFF = 2 # Variable c_int '2'
XMP_INST_DCA_OFF = XMP_INST_NNA_OFF # alias
XMP_INST_NNA_CUT = 0 # Variable c_int '0'
XMP_INST_DCA_CUT = XMP_INST_NNA_CUT # alias
XMP_MAX_KEYS = 121 # Variable c_int '121'
XMP_PLAYER_VOLUME = 7 # Variable c_int '7'
XMP_ENVELOPE_SLOOP = 16 # Variable c_int '16'
XMP_ERROR_DEPACK = 5 # Variable c_int '5'
XMP_ERROR_INTERNAL = 2 # Variable c_int '2'
XMP_INST_DCT_NOTE = 1 # Variable c_int '1'
XMP_SAMPLE_16BIT = 1 # Variable c_int '1'
XMP_VERSION = '4.2.0' # Variable STRING '(const char*)"4.2.0"'
XMP_ENVELOPE_CARRY = 32 # Variable c_int '32'
XMP_SAMPLE_LOOP_FULL = 16 # Variable c_int '16'
XMP_SMPCTL_SKIP = 1 # Variable c_int '1'
XMP_VER_MAJOR = 4 # Variable c_int '4'
XMP_INST_DCT_INST = 3 # Variable c_int '3'
XMP_MAX_MOD_LENGTH = 256 # Variable c_int '256'
XMP_STATE_PLAYING = 2 # Variable c_int '2'
XMP_PLAYER_MIX = 1 # Variable c_int '1'
XMP_PLAYER_INTERP = 2 # Variable c_int '2'
XMP_PERIOD_BASE = 6847 # Variable c_int '6847'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
XMP_ERROR_STATE = 8 # Variable c_int '8'
XMP_FLAGS_VBLANK = 1 # Variable c_int '1'
XMP_MIN_SRATE = 4000 # Variable c_int '4000'
XMP_MAX_FRAMESIZE = 24585 # Variable c_int '24585'
XMP_ENVELOPE_SUS = 2 # Variable c_int '2'
XMP_MIN_BPM = 20 # Variable c_int '20'
XMP_INST_DCT_OFF = 0 # Variable c_int '0'
XMP_INTERP_NEAREST = 0 # Variable c_int '0'
XMP_INTERP_SPLINE = 2 # Variable c_int '2'
XMP_MAX_ENV_POINTS = 32 # Variable c_int '32'
XMP_INST_DCT_SMP = 2 # Variable c_int '2'
XMP_PLAYER_AMP = 0 # Variable c_int '0'
XMP_ERROR_INVALID = 7 # Variable c_int '7'
XMP_KEY_OFF = 129 # Variable c_int '129'
XMP_FORMAT_UNSIGNED = 2 # Variable c_int '2'
XMP_ENVELOPE_FLT = 8 # Variable c_int '8'
XMP_ERROR_FORMAT = 3 # Variable c_int '3'
XMP_PLAYER_FLAGS = 4 # Variable c_int '4'
XMP_ENVELOPE_LOOP = 4 # Variable c_int '4'
XMP_PLAYER_DSP = 3 # Variable c_int '3'
XMP_PLAYER_SMIX_VOLUME = 9 # Variable c_int '9'
XMP_PLAYER_STATE = 8 # Variable c_int '8'
XMP_NAME_SIZE = 64 # Variable c_int '64'
XMP_VERCODE = 262656 # Variable c_int '262656'
XMP_ERROR_SYSTEM = 6 # Variable c_int '6'
XMP_SAMPLE_SYNTH = 32768 # Variable c_int '32768'
XMP_SAMPLE_LOOP_BIDIR = 4 # Variable c_int '4'
XMP_SAMPLE_LOOP_REVERSE = 8 # Variable c_int '8'
XMP_END = 1 # Variable c_int '1'
XMP_STATE_UNLOADED = 0 # Variable c_int '0'
XMP_DSP_ALL = 1 # Variable c_int '1'
XMP_FLAGS_FIXLOOP = 4 # Variable c_int '4'
XMP_PLAYER_CFLAGS = 5 # Variable c_int '5'
XMP_FORMAT_MONO = 4 # Variable c_int '4'
XMP_DSP_LOWPASS = 1 # Variable c_int '1'
XMP_FLAGS_FX9BUG = 2 # Variable c_int '2'
XMP_STATE_LOADED = 1 # Variable c_int '1'
XMP_INST_NNA_CONT = 1 # Variable c_int '1'
XMP_INTERP_LINEAR = 1 # Variable c_int '1'
XMP_VER_MINOR = 2 # Variable c_int '2'
XMP_CHANNEL_SYNTH = 1 # Variable c_int '1'
XMP_FORMAT_8BIT = 1 # Variable c_int '1'
XMP_KEY_CUT = 130 # Variable c_int '130'
XMP_ENVELOPE_ON = 1 # Variable c_int '1'
XMP_MAX_CHANNELS = 64 # Variable c_int '64'
XMP_VER_RELEASE = 0 # Variable c_int '0'
XMP_CHANNEL_MUTE = 2 # Variable c_int '2'
XMP_SAMPLE_LOOP = 2 # Variable c_int '2'
XMP_KEY_FADE = 131 # Variable c_int '131'
XMP_MAX_SRATE = 49170 # Variable c_int '49170'
XMP_PLAYER_SMPCTL = 6 # Variable c_int '6'
XMP_ERROR_LOAD = 4 # Variable c_int '4'
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
    ('map', N14xmp_instrument3DOT_0E * 121),
    ('sub', POINTER(xmp_subinstrument)),
    ('extra', c_void_p),
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
xmp_module_info._fields_ = [
    ('md5', c_ubyte * 16),
    ('vol_base', c_int),
    ('mod', POINTER(xmp_module)),
    ('comment', STRING),
    ('num_sequences', c_int),
    ('seq_data', POINTER(xmp_sequence)),
]
class xmp_frame_info(Structure):
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
xmp_frame_info._fields_ = [
    ('pos', c_int),
    ('pattern', c_int),
    ('row', c_int),
    ('num_rows', c_int),
    ('frame', c_int),
    ('speed', c_int),
    ('bpm', c_int),
    ('time', c_int),
    ('total_time', c_int),
    ('frame_time', c_int),
    ('buffer', c_void_p),
    ('buffer_size', c_int),
    ('total_size', c_int),
    ('volume', c_int),
    ('loop_count', c_int),
    ('virt_channels', c_int),
    ('virt_used', c_int),
    ('sequence', c_int),
    ('channel_info', xmp_channel_info * 64),
]
xmp_context = c_void_p
xmp_version = (STRING).in_dll(_libraries['/usr/lib/libxmp.so'], 'xmp_version')
xmp_vercode = (c_uint).in_dll(_libraries['/usr/lib/libxmp.so'], 'xmp_vercode')
xmp_create_context = _libraries['/usr/lib/libxmp.so'].xmp_create_context
xmp_create_context.restype = xmp_context
xmp_create_context.argtypes = []
xmp_free_context = _libraries['/usr/lib/libxmp.so'].xmp_free_context
xmp_free_context.restype = None
xmp_free_context.argtypes = [xmp_context]
xmp_test_module = _libraries['/usr/lib/libxmp.so'].xmp_test_module
xmp_test_module.restype = c_int
xmp_test_module.argtypes = [STRING, POINTER(xmp_test_info)]
xmp_load_module = _libraries['/usr/lib/libxmp.so'].xmp_load_module
xmp_load_module.restype = c_int
xmp_load_module.argtypes = [xmp_context, STRING]
xmp_scan_module = _libraries['/usr/lib/libxmp.so'].xmp_scan_module
xmp_scan_module.restype = None
xmp_scan_module.argtypes = [xmp_context]
xmp_release_module = _libraries['/usr/lib/libxmp.so'].xmp_release_module
xmp_release_module.restype = None
xmp_release_module.argtypes = [xmp_context]
xmp_start_player = _libraries['/usr/lib/libxmp.so'].xmp_start_player
xmp_start_player.restype = c_int
xmp_start_player.argtypes = [xmp_context, c_int, c_int]
xmp_play_frame = _libraries['/usr/lib/libxmp.so'].xmp_play_frame
xmp_play_frame.restype = c_int
xmp_play_frame.argtypes = [xmp_context]
xmp_play_buffer = _libraries['/usr/lib/libxmp.so'].xmp_play_buffer
xmp_play_buffer.restype = c_int
xmp_play_buffer.argtypes = [xmp_context, c_void_p, c_int, c_int]
xmp_get_frame_info = _libraries['/usr/lib/libxmp.so'].xmp_get_frame_info
xmp_get_frame_info.restype = None
xmp_get_frame_info.argtypes = [xmp_context, POINTER(xmp_frame_info)]
xmp_end_player = _libraries['/usr/lib/libxmp.so'].xmp_end_player
xmp_end_player.restype = None
xmp_end_player.argtypes = [xmp_context]
xmp_inject_event = _libraries['/usr/lib/libxmp.so'].xmp_inject_event
xmp_inject_event.restype = None
xmp_inject_event.argtypes = [xmp_context, c_int, POINTER(xmp_event)]
xmp_get_module_info = _libraries['/usr/lib/libxmp.so'].xmp_get_module_info
xmp_get_module_info.restype = None
xmp_get_module_info.argtypes = [xmp_context, POINTER(xmp_module_info)]
xmp_get_format_list = _libraries['/usr/lib/libxmp.so'].xmp_get_format_list
xmp_get_format_list.restype = POINTER(STRING)
xmp_get_format_list.argtypes = []
xmp_next_position = _libraries['/usr/lib/libxmp.so'].xmp_next_position
xmp_next_position.restype = c_int
xmp_next_position.argtypes = [xmp_context]
xmp_prev_position = _libraries['/usr/lib/libxmp.so'].xmp_prev_position
xmp_prev_position.restype = c_int
xmp_prev_position.argtypes = [xmp_context]
xmp_set_position = _libraries['/usr/lib/libxmp.so'].xmp_set_position
xmp_set_position.restype = c_int
xmp_set_position.argtypes = [xmp_context, c_int]
xmp_stop_module = _libraries['/usr/lib/libxmp.so'].xmp_stop_module
xmp_stop_module.restype = None
xmp_stop_module.argtypes = [xmp_context]
xmp_restart_module = _libraries['/usr/lib/libxmp.so'].xmp_restart_module
xmp_restart_module.restype = None
xmp_restart_module.argtypes = [xmp_context]
xmp_seek_time = _libraries['/usr/lib/libxmp.so'].xmp_seek_time
xmp_seek_time.restype = c_int
xmp_seek_time.argtypes = [xmp_context, c_int]
xmp_channel_mute = _libraries['/usr/lib/libxmp.so'].xmp_channel_mute
xmp_channel_mute.restype = c_int
xmp_channel_mute.argtypes = [xmp_context, c_int, c_int]
xmp_channel_vol = _libraries['/usr/lib/libxmp.so'].xmp_channel_vol
xmp_channel_vol.restype = c_int
xmp_channel_vol.argtypes = [xmp_context, c_int, c_int]
xmp_set_player = _libraries['/usr/lib/libxmp.so'].xmp_set_player
xmp_set_player.restype = c_int
xmp_set_player.argtypes = [xmp_context, c_int, c_int]
xmp_get_player = _libraries['/usr/lib/libxmp.so'].xmp_get_player
xmp_get_player.restype = c_int
xmp_get_player.argtypes = [xmp_context, c_int]
xmp_set_instrument_path = _libraries['/usr/lib/libxmp.so'].xmp_set_instrument_path
xmp_set_instrument_path.restype = c_int
xmp_set_instrument_path.argtypes = [xmp_context, STRING]
xmp_load_module_from_memory = _libraries['/usr/lib/libxmp.so'].xmp_load_module_from_memory
xmp_load_module_from_memory.restype = c_int
xmp_load_module_from_memory.argtypes = [xmp_context, c_void_p, c_long]
xmp_start_smix = _libraries['/usr/lib/libxmp.so'].xmp_start_smix
xmp_start_smix.restype = c_int
xmp_start_smix.argtypes = [xmp_context, c_int, c_int]
xmp_end_smix = _libraries['/usr/lib/libxmp.so'].xmp_end_smix
xmp_end_smix.restype = None
xmp_end_smix.argtypes = [xmp_context]
xmp_smix_play_instrument = _libraries['/usr/lib/libxmp.so'].xmp_smix_play_instrument
xmp_smix_play_instrument.restype = c_int
xmp_smix_play_instrument.argtypes = [xmp_context, c_int, c_int, c_int, c_int]
xmp_smix_play_sample = _libraries['/usr/lib/libxmp.so'].xmp_smix_play_sample
xmp_smix_play_sample.restype = c_int
xmp_smix_play_sample.argtypes = [xmp_context, c_int, c_int, c_int, c_int]
xmp_smix_channel_pan = _libraries['/usr/lib/libxmp.so'].xmp_smix_channel_pan
xmp_smix_channel_pan.restype = c_int
xmp_smix_channel_pan.argtypes = [xmp_context, c_int, c_int]
xmp_smix_load_sample = _libraries['/usr/lib/libxmp.so'].xmp_smix_load_sample
xmp_smix_load_sample.restype = c_int
xmp_smix_load_sample.argtypes = [xmp_context, c_int, STRING]
xmp_smix_release_sample = _libraries['/usr/lib/libxmp.so'].xmp_smix_release_sample
xmp_smix_release_sample.restype = c_int
xmp_smix_release_sample.argtypes = [xmp_context, c_int]
__all__ = ['XMP_MAX_KEYS', 'XMP_INST_DCA_OFF', 'xmp_set_player',
           'XMP_SAMPLE_LOOP_FULL', 'xmp_free_context',
           'XMP_FLAGS_VBLANK', 'XMP_INST_DCT_OFF',
           'XMP_ERROR_INVALID', 'xmp_test_module', 'XMP_ENVELOPE_FLT',
           'xmp_smix_channel_pan', 'XMP_NAME_SIZE',
           'XMP_ERROR_SYSTEM', 'XMP_SAMPLE_SYNTH',
           'XMP_SAMPLE_LOOP_BIDIR', 'XMP_ENVELOPE_SUS', 'XMP_END',
           'XMP_INST_NNA_FADE', 'xmp_channel', 'XMP_PLAYER_CFLAGS',
           'XMP_FORMAT_MONO', 'xmp_play_frame', 'XMP_INST_NNA_CONT',
           'N14xmp_instrument3DOT_0E', 'XMP_KEY_CUT', 'xmp_envelope',
           'XMP_MAX_CHANNELS', 'XMP_CHANNEL_MUTE', 'XMP_SAMPLE_LOOP',
           'xmp_module', 'XMP_ENVELOPE_LOOP', 'xmp_get_player',
           'XMP_MAX_FRAMESIZE', 'xmp_get_module_info',
           'xmp_module_info', 'xmp_load_module_from_memory',
           'xmp_instrument', 'xmp_sample', 'XMP_MAX_MOD_LENGTH',
           'XMP_MAX_ENV_POINTS', 'xmp_scan_module', 'XMP_MIN_SRATE',
           'xmp_create_context', 'XMP_STATE_UNLOADED',
           'XMP_INTERP_SPLINE', 'XMP_VER_MAJOR', 'XMP_INST_DCT_SMP',
           'XMP_INST_NNA_CUT', 'XMP_FORMAT_UNSIGNED',
           'XMP_PLAYER_DSP', 'xmp_channel_info',
           'xmp_smix_play_instrument', 'XMP_PLAYER_STATE',
           'XMP_PERIOD_BASE', 'xmp_get_frame_info',
           'xmp_get_format_list', 'xmp_end_smix', 'XMP_STATE_LOADED',
           'XMP_INTERP_LINEAR', 'XMP_SMPCTL_SKIP', 'XMP_ENVELOPE_ON',
           'XMP_MAX_SRATE', 'XMP_PLAYER_SMPCTL', 'xmp_set_position',
           'XMP_ERROR_INTERNAL', 'xmp_track', 'xmp_seek_time',
           'XMP_ERROR_LOAD', 'XMP_ENVELOPE_CARRY',
           'XMP_PLAYER_INTERP', 'XMP_INST_DCA_CUT',
           'xmp_start_player', 'xmp_start_smix', 'xmp_pattern',
           'XMP_INST_DCA_FADE', 'XMP_INST_NNA_OFF', 'xmp_frame_info',
           'XMP_PLAYER_AMP', 'xmp_stop_module', 'XMP_ERROR_FORMAT',
           'XMP_PLAYER_FLAGS', 'xmp_vercode',
           'XMP_SAMPLE_LOOP_REVERSE', 'xmp_event',
           'xmp_subinstrument', 'XMP_FLAGS_FIXLOOP',
           'XMP_DSP_LOWPASS', 'XMP_FLAGS_FX9BUG', 'XMP_CHANNEL_SYNTH',
           'XMP_FORMAT_8BIT', 'XMP_ERROR_DEPACK', 'XMP_VER_RELEASE',
           'xmp_channel_mute', 'xmp_smix_release_sample',
           'XMP_KEY_FADE', 'xmp_test_info', 'xmp_smix_load_sample',
           'XMP_PLAYER_VOLUME', 'XMP_ENVELOPE_SLOOP',
           'xmp_release_module', 'XMP_INST_DCT_NOTE',
           'XMP_SAMPLE_16BIT', 'xmp_sequence', 'XMP_VERSION',
           'xmp_play_buffer', 'XMP_INST_DCT_INST',
           '__STDC_CONSTANT_MACROS', 'xmp_channel_vol',
           'XMP_ERROR_STATE', 'XMP_PLAYER_MIX', 'XMP_MIN_BPM',
           'XMP_INTERP_NEAREST', 'XMP_KEY_OFF', 'XMP_DSP_ALL',
           'xmp_prev_position', 'XMP_PLAYER_SMIX_VOLUME',
           'XMP_VERCODE', 'xmp_inject_event', 'xmp_restart_module',
           'xmp_set_instrument_path', 'xmp_load_module',
           'xmp_smix_play_sample', 'XMP_VER_MINOR',
           'XMP_STATE_PLAYING', 'xmp_context', 'xmp_end_player',
           'xmp_next_position', 'xmp_version']
