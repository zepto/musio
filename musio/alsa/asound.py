from ctypes.util import find_library
from ctypes import *
_alsa_lib = cdll.LoadLibrary(find_library('asound'))
import mod_play
import mod_dumb
import sys
from threading import Thread

if hex(sys.hexversion) >= '0x30102f0':
    raw_input = input


class _snd_pcm(Structure):
    _fields_ = [
            ]
snd_pcm_t = _snd_pcm
snd_pcm_stream_t = c_int
# * Playback stream 
SND_PCM_STREAM_PLAYBACK = 0
# * Capture stream 
SND_PCM_STREAM_CAPTURE = 1
SND_PCM_STREAM_LAST = SND_PCM_STREAM_CAPTURE
class _snd_pcm_hw_params(Structure):
    _fields_ = [
            ]
snd_pcm_hw_params_t = _snd_pcm_hw_params 

class _snd_pcm_info(Structure):
    _fields_ = [
            ]
snd_pcm_info_t = _snd_pcm_info

# PCM access type 
# mmap access with simple interleaved channels 
SND_PCM_ACCESS_MMAP_INTERLEAVED = 0,
# mmap access with simple non interleaved channels 
SND_PCM_ACCESS_MMAP_NONINTERLEAVED = 1
# mmap access with complex placement 
SND_PCM_ACCESS_MMAP_COMPLEX = 2
# snd_pcm_readi/snd_pcm_writei access 
SND_PCM_ACCESS_RW_INTERLEAVED = 3
# snd_pcm_readn/snd_pcm_writen access 
SND_PCM_ACCESS_RW_NONINTERLEAVED = 4
SND_PCM_ACCESS_LAST = SND_PCM_ACCESS_RW_NONINTERLEAVED
snd_pcm_access_t = c_int

# PCM sample format 
# Unknown 
SND_PCM_FORMAT_UNKNOWN = -1
# Signed 8 bit 
SND_PCM_FORMAT_S8 = 0
# Unsigned 8 bit 
SND_PCM_FORMAT_U8 = 1
# Signed 16 bit Little Endian 
SND_PCM_FORMAT_S16_LE = 2
# Signed 16 bit Big Endian 
SND_PCM_FORMAT_S16_BE = 3
# Unsigned 16 bit Little Endian 
SND_PCM_FORMAT_U16_LE = 4
# Unsigned 16 bit Big Endian 
SND_PCM_FORMAT_U16_BE = 5
# Signed 24 bit Little Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_S24_LE = 6
# Signed 24 bit Big Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_S24_BE = 7
# Unsigned 24 bit Little Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_U24_LE = 8
# Unsigned 24 bit Big Endian using low three bytes in 32-bit word 
SND_PCM_FORMAT_U24_BE = 9
# Signed 32 bit Little Endian 
SND_PCM_FORMAT_S32_LE = 10
# Signed 32 bit Big Endian 
SND_PCM_FORMAT_S32_BE = 11
# Unsigned 32 bit Little Endian 
SND_PCM_FORMAT_U32_LE = 12
# Unsigned 32 bit Big Endian 
SND_PCM_FORMAT_U32_BE = 13
# Float 32 bit Little Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT_LE = 14
# Float 32 bit Big Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT_BE = 15
# Float 64 bit Little Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT64_LE = 16
# Float 64 bit Big Endian, Range -1.0 to 1.0 
SND_PCM_FORMAT_FLOAT64_BE = 17
# IEC-958 Little Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME_LE = 18
# IEC-958 Big Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME_BE = 19
# Mu-Law 
SND_PCM_FORMAT_MU_LAW = 20
# A-Law 
SND_PCM_FORMAT_A_LAW = 21
# Ima-ADPCM 
SND_PCM_FORMAT_IMA_ADPCM = 22
# MPEG 
SND_PCM_FORMAT_MPEG = 23
# GSM 
SND_PCM_FORMAT_GSM = 24
# Special 
SND_PCM_FORMAT_SPECIAL = 31
# Signed 24bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S24_3LE = 32
# Signed 24bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S24_3BE = 33
# Unsigned 24bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U24_3LE = 34
# Unsigned 24bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U24_3BE = 35
# Signed 20bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S20_3LE = 36
# Signed 20bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S20_3BE = 37
# Unsigned 20bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U20_3LE = 38
# Unsigned 20bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U20_3BE = 39
# Signed 18bit Little Endian in 3bytes format 
SND_PCM_FORMAT_S18_3LE = 40
# Signed 18bit Big Endian in 3bytes format 
SND_PCM_FORMAT_S18_3BE = 41
# Unsigned 18bit Little Endian in 3bytes format 
SND_PCM_FORMAT_U18_3LE = 42
# Unsigned 18bit Big Endian in 3bytes format 
SND_PCM_FORMAT_U18_3BE = 43
SND_PCM_FORMAT_LAST = SND_PCM_FORMAT_U18_3BE

#if __BYTE_ORDER == __LITTLE_ENDIAN
# Signed 16 bit CPU endian 
SND_PCM_FORMAT_S16 = SND_PCM_FORMAT_S16_LE
# Unsigned 16 bit CPU endian 
SND_PCM_FORMAT_U16 = SND_PCM_FORMAT_U16_LE
# Signed 24 bit CPU endian 
SND_PCM_FORMAT_S24 = SND_PCM_FORMAT_S24_LE
# Unsigned 24 bit CPU endian 
SND_PCM_FORMAT_U24 = SND_PCM_FORMAT_U24_LE
# Signed 32 bit CPU endian 
SND_PCM_FORMAT_S32 = SND_PCM_FORMAT_S32_LE
# Unsigned 32 bit CPU endian 
SND_PCM_FORMAT_U32 = SND_PCM_FORMAT_U32_LE
# Float 32 bit CPU endian 
SND_PCM_FORMAT_FLOAT = SND_PCM_FORMAT_FLOAT_LE
# Float 64 bit CPU endian 
SND_PCM_FORMAT_FLOAT64 = SND_PCM_FORMAT_FLOAT64_LE
# IEC-958 CPU Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME = SND_PCM_FORMAT_IEC958_SUBFRAME_LE
#elif __BYTE_ORDER == __BIG_ENDIAN
# Signed 16 bit CPU endian 
SND_PCM_FORMAT_S16 = SND_PCM_FORMAT_S16_BE
# Unsigned 16 bit CPU endian 
SND_PCM_FORMAT_U16 = SND_PCM_FORMAT_U16_BE
# Signed 24 bit CPU endian 
SND_PCM_FORMAT_S24 = SND_PCM_FORMAT_S24_BE
# Unsigned 24 bit CPU endian 
SND_PCM_FORMAT_U24 = SND_PCM_FORMAT_U24_BE
# Signed 32 bit CPU endian 
SND_PCM_FORMAT_S32 = SND_PCM_FORMAT_S32_BE
# Unsigned 32 bit CPU endian 
SND_PCM_FORMAT_U32 = SND_PCM_FORMAT_U32_BE
# Float 32 bit CPU endian 
SND_PCM_FORMAT_FLOAT = SND_PCM_FORMAT_FLOAT_BE
# Float 64 bit CPU endian 
SND_PCM_FORMAT_FLOAT64 = SND_PCM_FORMAT_FLOAT64_BE
# IEC-958 CPU Endian 
SND_PCM_FORMAT_IEC958_SUBFRAME = SND_PCM_FORMAT_IEC958_SUBFRAME_BE
snd_pcm_format_t = c_int

# Open 
SND_PCM_STATE_OPEN = 0
# Setup installed  
SND_PCM_STATE_SETUP = 1
# Ready to start 
SND_PCM_STATE_PREPARED = 2
# Running 
SND_PCM_STATE_RUNNING = 3
# Stopped: underrun (playback) or overrun (capture) detected 
SND_PCM_STATE_XRUN = 4
# Draining: running (playback) or stopped (capture) 
SND_PCM_STATE_DRAINING = 5
# Paused 
SND_PCM_STATE_PAUSED = 6
# Hardware is suspended 
SND_PCM_STATE_SUSPENDED = 7
# Hardware is disconnected 
SND_PCM_STATE_DISCONNECTED = 8
SND_PCM_STATE_LAST = SND_PCM_STATE_DISCONNECTED

snd_pcm_state_t = c_int

# Unsigned frames quantity 
snd_pcm_uframes_t = c_ulong
# Signed frames quantity 
snd_pcm_sframes_t = c_long

EINTR = 4
EPIPE = 32
EBADFD = 77
ESTRPIPE = 86

#snd_pcm_state_t snd_pcm_state(snd_pcm_t *pcm);
snd_pcm_state = _alsa_lib.snd_pcm_state
snd_pcm_state.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_state.restype = snd_pcm_state_t

snd_pcm_open = _alsa_lib.snd_pcm_open
snd_pcm_open.argtypes = [POINTER(POINTER(snd_pcm_t)), c_char_p, snd_pcm_stream_t, c_int]
snd_pcm_open.restype = c_int


handle = POINTER(snd_pcm_t)()
# Open PCM device for playback. 
rc = snd_pcm_open(byref(handle), 'default',
                SND_PCM_STREAM_PLAYBACK, 0)
print(rc)
print("state = %d" % snd_pcm_state(handle))

#int snd_pcm_set_params(snd_pcm_t *pcm,
#snd_pcm_format_t format,
#snd_pcm_access_t access,
#unsigned int channels,
#unsigned int rate,
#int soft_resample,
#unsigned int latency);
snd_pcm_set_params = _alsa_lib.snd_pcm_set_params
snd_pcm_set_params.argtypes = [POINTER(snd_pcm_t), snd_pcm_format_t, snd_pcm_access_t, c_uint, c_uint, c_int, c_uint]
snd_pcm_set_params.restype = c_int
print(snd_pcm_set_params(handle, SND_PCM_FORMAT_S16_LE, SND_PCM_ACCESS_RW_INTERLEAVED, 2, 44100, 1, 500000))

params = POINTER(snd_pcm_hw_params_t)()
#int snd_pcm_hw_params_current(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params_current = _alsa_lib.snd_pcm_hw_params_current
snd_pcm_hw_params_current.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_current.restype = c_int

snd_pcm_hw_params_malloc = _alsa_lib.snd_pcm_hw_params_malloc
snd_pcm_hw_params_malloc.argtypes = [POINTER(POINTER(snd_pcm_hw_params_t))]
snd_pcm_hw_params_malloc.restype = c_int
print(snd_pcm_hw_params_malloc(byref(params)))
print(snd_pcm_hw_params_current(handle, params))
snd_pcm_hw_params_free = _alsa_lib.snd_pcm_hw_params_free
snd_pcm_hw_params_free.argtypes = [POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_free.restype = None
#snd_pcm_hw_params_free(params)
snd_pcm_hw_params_any = _alsa_lib.snd_pcm_hw_params_any
snd_pcm_hw_params_any.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params_any.restype = c_int
#print(snd_pcm_hw_params_any(handle, params))
#int snd_pcm_hw_params_set_access(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_access_t _access);
snd_pcm_hw_params_set_access = _alsa_lib.snd_pcm_hw_params_set_access
snd_pcm_hw_params_set_access.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_access_t]
snd_pcm_hw_params_set_access.restype = c_int
#print(snd_pcm_hw_params_set_access(handle, params,
#SND_PCM_ACCESS_RW_INTERLEAVED))
#int snd_pcm_hw_params_set_format(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_format_t val);
snd_pcm_hw_params_set_format = _alsa_lib.snd_pcm_hw_params_set_format
snd_pcm_hw_params_set_format.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_format_t]
snd_pcm_hw_params_set_format.restype = c_int
#print(snd_pcm_hw_params_set_format(handle, params, SND_PCM_FORMAT_S16_LE))

snd_strerror = _alsa_lib.snd_strerror
snd_strerror.argtypes = [c_int]
snd_strerror.restype = c_char_p
#print snd_strerror(32)

#int snd_pcm_hw_params_set_channels(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val);
snd_pcm_hw_params_set_channels = _alsa_lib.snd_pcm_hw_params_set_channels
snd_pcm_hw_params_set_channels.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint]
snd_pcm_hw_params_set_channels.restype = c_int
#print(snd_pcm_hw_params_set_channels(handle, params, 2))
#int snd_pcm_hw_params_set_rate(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int val, int dir);
snd_pcm_hw_params_set_rate = _alsa_lib.snd_pcm_hw_params_set_rate
snd_pcm_hw_params_set_rate.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), c_uint, c_int]
snd_pcm_hw_params_set_rate.restype = c_int
#int snd_pcm_hw_params_set_rate_near(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, unsigned int *val, int *dir);
snd_pcm_hw_params_set_rate_near = _alsa_lib.snd_pcm_hw_params_set_rate_near
snd_pcm_hw_params_set_rate_near.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), POINTER(c_uint), POINTER(c_int)]
snd_pcm_hw_params_set_rate_near.restype = c_int
#dir = c_int() #POINTER(c_int)()
freq = c_uint(44100)
#print snd_pcm_hw_params_set_rate_near(handle, params, byref(freq), byref(dir))
#print(snd_pcm_hw_params_set_rate(handle, params, 44100, 0)) #byref(freq), byref(dir))
#int snd_pcm_hw_params_set_period_size(snd_pcm_t *pcm, snd_pcm_hw_params_t *params, snd_pcm_uframes_t val, int dir);
snd_pcm_hw_params_set_period_size = _alsa_lib.snd_pcm_hw_params_set_period_size
snd_pcm_hw_params_set_period_size.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t), snd_pcm_uframes_t, c_int]
snd_pcm_hw_params_set_period_size.restype = c_int
#rc = snd_pcm_hw_params_set_period_size(handle, params, 512, 0)
#print(snd_strerror(rc))
#int snd_pcm_hw_params(snd_pcm_t *pcm, snd_pcm_hw_params_t *params);
snd_pcm_hw_params = _alsa_lib.snd_pcm_hw_params
snd_pcm_hw_params.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_hw_params_t)]
snd_pcm_hw_params.restype = c_int
#rc = snd_pcm_hw_params(handle, params)
#print(rc)
#int snd_pcm_hw_params_get_period_size(const snd_pcm_hw_params_t *params, snd_pcm_uframes_t *frames, int *dir);
snd_pcm_hw_params_get_period_size = _alsa_lib.snd_pcm_hw_params_get_period_size
snd_pcm_hw_params_get_period_size.argtypes = [POINTER(snd_pcm_hw_params_t), POINTER(snd_pcm_uframes_t), POINTER(c_int)]
snd_pcm_hw_params_get_period_size.restype = c_int
frames = snd_pcm_uframes_t()
dirf = c_int()
print(snd_pcm_hw_params_get_period_size(params, byref(frames), byref(dirf)))
print(frames)
#int snd_pcm_get_params(snd_pcm_t *pcm,
#snd_pcm_uframes_t *buffer_size,
#snd_pcm_uframes_t *period_size);
snd_pcm_get_params = _alsa_lib.snd_pcm_get_params
snd_pcm_get_params.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_uframes_t), POINTER(snd_pcm_uframes_t)]
snd_pcm_get_params.restype = c_int
buf_size = snd_pcm_uframes_t()
period_size = snd_pcm_uframes_t()
print(snd_pcm_get_params(handle, byref(buf_size), byref(period_size)))
print("buffer = %s, period = %s" % (buf_size, period_size))
#ssize_t snd_pcm_frames_to_bytes(snd_pcm_t *pcm, snd_pcm_sframes_t frames);
snd_pcm_frames_to_bytes = _alsa_lib.snd_pcm_frames_to_bytes
snd_pcm_frames_to_bytes.argtypes = [POINTER(snd_pcm_t), snd_pcm_sframes_t]
snd_pcm_frames_to_bytes.restype = c_size_t
print(snd_pcm_frames_to_bytes(handle, snd_pcm_sframes_t(period_size.value)))
#snd_pcm_sframes_t snd_pcm_bytes_to_frames(snd_pcm_t *pcm, ssize_t bytes);
snd_pcm_bytes_to_frames = _alsa_lib.snd_pcm_bytes_to_frames
snd_pcm_bytes_to_frames.argtypes = [POINTER(snd_pcm_t), c_size_t]
snd_pcm_bytes_to_frames.restype = snd_pcm_sframes_t
print(snd_pcm_bytes_to_frames(handle, 4096))
#long snd_pcm_bytes_to_samples(snd_pcm_t *pcm, ssize_t bytes);
snd_pcm_bytes_to_samples = _alsa_lib.snd_pcm_bytes_to_samples
snd_pcm_bytes_to_samples.argtypes = [POINTER(snd_pcm_t), c_size_t]
snd_pcm_bytes_to_samples.restype = c_long
print(snd_pcm_bytes_to_samples(handle, 4096))
#ssize_t snd_pcm_samples_to_bytes(snd_pcm_t *pcm, long samples);
snd_pcm_samples_to_bytes = _alsa_lib.snd_pcm_samples_to_bytes
snd_pcm_samples_to_bytes.argtypes = [POINTER(snd_pcm_t), c_long]
snd_pcm_samples_to_bytes.restype = c_size_t
print(snd_pcm_samples_to_bytes(handle, 4096))
#int snd_pcm_info_malloc(snd_pcm_info_t **ptr);
info = POINTER(snd_pcm_info_t)()
snd_pcm_info_malloc = _alsa_lib.snd_pcm_info_malloc
snd_pcm_info_malloc.argtypes = [POINTER(POINTER(snd_pcm_info_t))]
snd_pcm_info_malloc.restype = c_int
print(snd_pcm_info_malloc(byref(info)))
#void snd_pcm_info_free(snd_pcm_info_t *obj);
snd_pcm_info_free = _alsa_lib.snd_pcm_info_free
snd_pcm_info_free.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_free.restype = None
#int snd_pcm_info(snd_pcm_t *pcm, snd_pcm_info_t *info);
snd_pcm_info = _alsa_lib.snd_pcm_info
snd_pcm_info.argtypes = [POINTER(snd_pcm_t), POINTER(snd_pcm_info_t)]
snd_pcm_info.restype = c_int
print(snd_pcm_info(handle, info))
#const char *snd_pcm_info_get_name(const snd_pcm_info_t *obj);
snd_pcm_info_get_name = _alsa_lib.snd_pcm_info_get_name
snd_pcm_info_get_name.argtypes = [POINTER(snd_pcm_info_t)]
snd_pcm_info_get_name.restype = c_char_p
print(snd_pcm_info_get_name(info))
snd_pcm_info_free(info)
#int snd_pcm_drain(snd_pcm_t *pcm);
snd_pcm_drain = _alsa_lib.snd_pcm_drain
snd_pcm_drain.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_drain.restype = c_int
#int snd_pcm_close(snd_pcm_t *pcm);
snd_pcm_close = _alsa_lib.snd_pcm_close
snd_pcm_close.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_close.restype = c_int
#int snd_pcm_hw_free(snd_pcm_t *pcm);
snd_pcm_hw_free = _alsa_lib.snd_pcm_hw_free
snd_pcm_hw_free.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_hw_free.restype = c_int
#snd_pcm_sframes_t snd_pcm_writei(snd_pcm_t *pcm, const void *buffer, snd_pcm_uframes_t size);
snd_pcm_writei = _alsa_lib.snd_pcm_writei
snd_pcm_writei.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_writei.restype = snd_pcm_sframes_t
#snd_pcm_sframes_t snd_pcm_readi(snd_pcm_t *pcm, void *buffer, snd_pcm_uframes_t size);
snd_pcm_readi = _alsa_lib.snd_pcm_readi
snd_pcm_readi.argtypes = [POINTER(snd_pcm_t), c_void_p, snd_pcm_uframes_t]
snd_pcm_readi.restype = snd_pcm_sframes_t
#int snd_pcm_recover(snd_pcm_t *pcm, int err, int silent);
snd_pcm_recover = _alsa_lib.snd_pcm_recover
snd_pcm_recover.argtypes = [POINTER(snd_pcm_t), c_int, c_int]
snd_pcm_recover.restype = c_int
#int snd_pcm_prepare(snd_pcm_t *pcm);
snd_pcm_prepare = _alsa_lib.snd_pcm_prepare
snd_pcm_prepare.argtypes = [POINTER(snd_pcm_t)]
snd_pcm_prepare.restype = c_int
#snd_pcm_prepare(handle);

print("state = %d" % snd_pcm_state(handle))

print ("Playing: %s" % sys.argv[1])
depth=16
bigendian=False
channels = 2
buffer_size = None
unsigned = False
with mod_dumb.DumbFile(sys.argv[1]) as dumb:
    playing = {}
    def play(playing):
        while playing['playing']:
            data = dumb.read()
            if not data:
                dumb.seek(0)
                continue
            rc = snd_pcm_writei(handle, data, (len(data) / 4));
            if rc == -EPIPE:
# EPIPE means underrun 
                snd_pcm_recover(handle, rc, 0)
            elif rc < 0:
                print(snd_strerror(rc))
            elif rc != len(data)/4:
                print("Write %d frames" % rc)
        print("Done.")
    playing['playing'] = True
    play_t = Thread(target=play, args=(playing,))
    play_t.start()
    raw_input()
    playing['playing'] = False
    play_t.join()
print("Exiting...")

print("state = %d" % snd_pcm_state(handle))
print(snd_pcm_drain(handle))
print("state = %d" % snd_pcm_state(handle))
print(snd_pcm_hw_free(handle))
print(snd_pcm_close(handle))
#size = frames * 4;  2 bytes/sample, 2 channels 
