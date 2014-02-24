from ctypes import *

_libraries = {}
_libraries['/usr/lib/libmikmod.so'] = CDLL('/usr/lib/libmikmod.so')
STRING = c_char_p
WSTRING = c_wchar_p


def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
MD_SOFTWARE = 1
MMERR_MAX = 96
MMERR_ALSA_SETCHANNELS = 91
MMERR_DS_EVENT = 55
MMERR_ALSA_PCM_WRITE = 94
# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MMERR_HP_AUDIO_OUTPUT = 34
def __WIFCONTINUED(status): return ((status) == __W_CONTINUED) # macro
# __UID_T_TYPE = __U32_TYPE # alias
MMERR_OPENAL_GETSOURCE = 84
MMERR_OS2_TIMER = 49
MMERR_OPENAL_QUEUEBUFFERS = 81
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
class _G_fpos_t(Structure):
    pass
__off_t = c_long
class __mbstate_t(Structure):
    pass
class N11__mbstate_t3DOT_2E(Union):
    pass
N11__mbstate_t3DOT_2E._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * 4),
]
__mbstate_t._fields_ = [
    ('__count', c_int),
    ('__value', N11__mbstate_t3DOT_2E),
]
_G_fpos_t._fields_ = [
    ('__pos', __off_t),
    ('__state', __mbstate_t),
]
_IO_fpos_t = _G_fpos_t # alias
MMERR_NO_FLOAT32 = 75
MMERR_DOSSB_STARTDMA = 74
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MMERR_DOSWSS_STARTDMA = 73
MMERR_INITIALIZING_MIXER = 17
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
MMERR_OSX_DEVICE_START = 71
MMERR_OSX_ADD_IO_PROC = 70
MMERR_OSX_BUFFER_ALLOC = 69
MMERR_OS2_THREAD = 50
MMERR_OSX_SET_STEREO = 68
MMERR_OSX_UNSUPPORTED_FORMAT = 67
MMERR_OSX_BAD_PROPERTY = 66
MMERR_OSX_UNKNOWN_DEVICE = 65
MMERR_SUN_INIT = 46
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
MMERR_MAC_SPEED = 63
MMERR_WINMM_UNKNOWN = 62
MMERR_WINMM_FORMAT = 61
MMERR_ALSA_BUFFERSIZE = 92
MMERR_WINMM_DEVICEID = 60
MMERR_WINMM_ALLOCATED = 59
MMERR_SGI_MONO = 45
MMERR_WINMM_HANDLE = 58
MMERR_DS_UPDATE = 57
MD_HARDWARE = 0
MMERR_DS_THREAD = 56
MMERR_DS_BUFFER = 52
MMERR_DS_PRIORITY = 51
class _G_fpos64_t(Structure):
    pass
__off64_t = c_long
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
MMERR_OS2_SEMAPHORE = 48
MMERR_OS2_MIXSETUP = 47
# __S32_TYPE = int # alias
# __CLOCKID_T_TYPE = __S32_TYPE # alias
MMERR_SGI_STEREO = 44
MMERR_SGI_8BIT = 43
MMERR_SGI_16BIT = 42
MMERR_OSS_SETSPEED = 40
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MD_MUSIC = 0
MMERR_OSS_SETSAMPLESIZE = 38
MMERR_OSS_SETFRAGMENT = 37
MMERR_HP_BUFFERSIZE = 36
MMERR_OPENAL_UNQUEUEBUFFERS = 82
MMERR_ALSA_SETRATE = 90
MMERR_HP_AUDIO_DESC = 35
MMERR_SGI_SPEED = 41
MMERR_ALSA_SETPARAMS = 88
MMERR_HP_SETSPEED = 32
MMERR_HP_SETSAMPLESIZE = 31
MMERR_GUS_SETTINGS = 28
MMERR_AIX_CONFIG_CONTROL = 26
MMERR_AIX_CONFIG_INIT = 25
MMERR_AF_AUDIO_PORT = 24
MMERR_NON_BLOCK = 23
MMERR_OSS_SETSTEREO = 39
MMERR_ULAW = 22
MMERR_STEREO_ONLY = 21
MMERR_16BIT_ONLY = 20
MMERR_8BIT_ONLY = 19
# _IO_file_flags = _flags # alias
MMERR_OPENING_AUDIO = 18
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
__BYTE_ORDER = __LITTLE_ENDIAN # alias
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
MMERR_INVALID_DEVICE = 16
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
class __va_list_tag(Structure):
    pass
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
_G_va_list = __gnuc_va_list # alias
# def __FDS_BITS(set): return ((set)->fds_bits) # macro
MMERR_ALSA_NOCONFIG = 87
MMERR_OUT_OF_MEMORY = 2
MMERR_OPENING_FILE = 1
# __PID_T_TYPE = __S32_TYPE # alias
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
def __WIFEXITED(status): return (__WTERMSIG(status) == 0) # macro
MMERR_HP_CHANNELS = 33
def WTERMSIG(status): return __WTERMSIG (__WAIT_INT (status)) # macro
# __SLONG32_TYPE = int # alias
MMERR_MAC_START = 64
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
def FD_CLR(fd,fdsetp): return __FD_CLR (fd, fdsetp) # macro
MMERR_OPENAL_SOURCESTOP = 86
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
class _IO_FILE(Structure):
    pass
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmikmod.so'], 'stdout')
stdout = stdout # alias
MMERR_GUS_TIMER = 30
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmikmod.so'], 'stderr')
stderr = stderr # alias
# __wur = __attribute_warn_unused_result__ # alias
# __USECONDS_T_TYPE = __U32_TYPE # alias
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def le64toh(x): return (x) # macro
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
MMERR_MED_SYNTHSAMPLES = 13
MMERR_GUS_RESET = 29
MMERR_OPENAL_SOURCE = 80
# __MODE_T_TYPE = __U32_TYPE # alias
MMERR_OPENAL_SOURCEPLAY = 85
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp) # macro
# __KEY_T_TYPE = __S32_TYPE # alias
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __INO64_T_TYPE = __UQUAD_TYPE # alias
# __ID_T_TYPE = __U32_TYPE # alias
# __GID_T_TYPE = __U32_TYPE # alias
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
def __STRING(x): return #x # macro
def htole64(x): return (x) # macro
__FLOAT_WORD_ORDER = __BYTE_ORDER # alias
# __DEV_T_TYPE = __UQUAD_TYPE # alias
# __DADDR_T_TYPE = __S32_TYPE # alias
def htobe16(x): return __bswap_16 (x) # macro
def alloca(size): return __builtin_alloca (size) # macro
def be64toh(x): return __bswap_64 (x) # macro
MMERR_NOT_A_STREAM = 12
def be32toh(x): return __bswap_32 (x) # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
MMERR_OPENAL_GENSOURCES = 79
_IO_va_list = __gnuc_va_list # alias
__uid_t = c_uint
_IO_uid_t = __uid_t # alias
# def __u_intN_t(N,MODE): return typedef unsigned int u_int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
_IO_off_t = __off_t # alias
# _IO_wint_t = wint_t # alias
_IO_off64_t = __off64_t # alias
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
def WSTOPSIG(status): return __WSTOPSIG (__WAIT_INT (status)) # macro
__codecvt_noconv = 3
BYTE_ORDER = __BYTE_ORDER # alias
BUFSIZ = _IO_BUFSIZ # alias
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmikmod.so'], 'stdin')
stdin = stdin # alias
def __WTERMSIG(status): return ((status) & 0x7f) # macro
MMERR_NOT_A_MODULE = 11
MMERR_AIX_CONFIG_START = 27
__codecvt_ok = 0
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MMERR_ALSA_SETFORMAT = 89
def le16toh(x): return (x) # macro
__PDP_ENDIAN = 3412 # Variable c_int '3412'
PDP_ENDIAN = __PDP_ENDIAN # alias
MMERR_DETECTING_DEVICE = 15
def minor(dev): return gnu_dev_minor (dev) # macro
def htole32(x): return (x) # macro
def WIFSTOPPED(status): return __WIFSTOPPED (__WAIT_INT (status)) # macro
MMERR_ITPACK_INVALID_DATA = 14
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
MMERR_LOADING_SAMPLEINFO = 10
def __CONCAT(x,y): return x ## y # macro
def WIFSIGNALED(status): return __WIFSIGNALED (__WAIT_INT (status)) # macro
# def __FD_CLR(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] &= ~__FD_MASK (d))) # macro
def WEXITSTATUS(status): return __WEXITSTATUS (__WAIT_INT (status)) # macro
MMERR_OPENAL_CTXCURRENT = 77
def FD_ISSET(fd,fdsetp): return __FD_ISSET (fd, fdsetp) # macro
def htobe32(x): return __bswap_32 (x) # macro
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
def __W_EXITCODE(ret,sig): return ((ret) << 8 | (sig)) # macro
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
# def __FD_ZERO(fdsp): return do { int __d0, __d1; __asm__ __volatile__ ("cld; rep; " __FD_ZERO_STOS : "=c" (__d0), "=D" (__d1) : "a" (0), "0" (sizeof (fd_set) / sizeof (__fd_mask)), "1" (&__FDS_BITS (fdsp)[0]) : "memory"); } while (0) # macro
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
MMERR_LOADING_HEADER = 9
def htole16(x): return (x) # macro
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
MMERR_ALSA_PCM_START = 93
MMERR_OPENAL_CREATECTX = 76
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def __WIFSTOPPED(status): return (((status) & 0xff) == 0x7f) # macro
__codecvt_error = 2
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
MMERR_LOADING_TRACK = 8
def htobe64(x): return __bswap_64 (x) # macro
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
__codecvt_partial = 1
MMERR_OPENAL_BUFFERDATA = 83
# def __LDBL_REDIR(name,proto): return name proto # macro
__ssize_t = c_long
_IO_ssize_t = __ssize_t # alias
def WIFCONTINUED(status): return __WIFCONTINUED (__WAIT_INT (status)) # macro
def __WSTOPSIG(status): return __WEXITSTATUS(status) # macro
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MMERR_LOADING_PATTERN = 7
__pid_t = c_int
_IO_pid_t = __pid_t # alias
MMERR_ALSA_PCM_RECOVER = 95
# def __intN_t(N,MODE): return typedef int int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
# _IO_iconv_t = _G_iconv_t # alias
# def __WAIT_INT(status): return (*(int *) &(status)) # macro
MMERR_OPENAL_GENBUFFERS = 78
# def __bswap_16(x): return (__extension__ ({ unsigned short int __v, __x = (unsigned short int) (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_16 (__x); else __asm__ ("rorw $8, %w0" : "=r" (__v) : "0" (__x) : "cc"); __v; })) # macro
# def __bswap_constant_64(x): return (__extension__ ((((x) & 0xff00000000000000ull) >> 56) | (((x) & 0x00ff000000000000ull) >> 40) | (((x) & 0x0000ff0000000000ull) >> 24) | (((x) & 0x000000ff00000000ull) >> 8) | (((x) & 0x00000000ff000000ull) << 8) | (((x) & 0x0000000000ff0000ull) << 24) | (((x) & 0x000000000000ff00ull) << 40) | (((x) & 0x00000000000000ffull) << 56))) # macro
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def __bswap_constant_16(x): return ((unsigned short int) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8))) # macro
def le32toh(x): return (x) # macro
MD_SNDFX = 1
size_t = c_ulong
_IO_size_t = size_t # alias
def __LONG_LONG_PAIR(HI,LO): return LO, HI # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
def getc(_fp): return _IO_getc (_fp) # macro
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
MMERR_OSX_PTHREAD = 72
def makedev(maj,min): return gnu_dev_makedev (maj, min) # macro
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
def WIFEXITED(status): return __WIFEXITED (__WAIT_INT (status)) # macro
__NFDBITS = 64 # Variable c_int '64'
NFDBITS = __NFDBITS # alias
__FD_SETSIZE = 1024 # Variable c_int '1024'
FD_SETSIZE = __FD_SETSIZE # alias
# def __WIFSIGNALED(status): return (((signed char) (((status) & 0x7f) + 1) >> 1) > 0) # macro
LITTLE_ENDIAN = __LITTLE_ENDIAN # alias
def __WEXITSTATUS(status): return (((status) & 0xff00) >> 8) # macro
__BIG_ENDIAN = 4321 # Variable c_int '4321'
BIG_ENDIAN = __BIG_ENDIAN # alias
def __WCOREDUMP(status): return ((status) & __WCOREFLAG) # macro
def FD_SET(fd,fdsetp): return __FD_SET (fd, fdsetp) # macro
def major(dev): return gnu_dev_major (dev) # macro
def __bswap_constant_32(x): return ((((x) & 0xff000000) >> 24) | (((x) & 0x00ff0000) >> 8) | (((x) & 0x0000ff00) << 8) | (((x) & 0x000000ff) << 24)) # macro
MMERR_SAMPLE_TOO_BIG = 4
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# NULL = __null # alias
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
def __PMT(args): return args # macro
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
MMERR_DS_NOTIFY = 54
def __P(args): return args # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
def __W_STOPCODE(sig): return ((sig) << 8 | 0x7f) # macro
# def __FD_MASK(d): return ((__fd_mask) 1 << ((d) % __NFDBITS)) # macro
MMERR_OUT_OF_HANDLES = 5
def __FD_ISSET(d,set): return ((__FDS_BITS (set)[__FD_ELT (d)] & __FD_MASK (d)) != 0) # macro
# def __FD_ELT(d): return __extension__ ({ long int __d = (d); (__builtin_constant_p (__d) ? (0 <= __d && __d < __FD_SETSIZE ? (__d / __NFDBITS) : __fdelt_warn (__d)) : __fdelt_chk (__d)); }) # macro
# def __FD_SET(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] |= __FD_MASK (d))) # macro
MMERR_UNKNOWN_WAVE_TYPE = 6
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
MMERR_DYNAMIC_LINKING = 3
def be16toh(x): return __bswap_16 (x) # macro
MMERR_DS_FORMAT = 53
WSTOPPED = 2 # Variable c_int '2'
__STDLIB_MB_LEN_MAX = 16 # Variable c_int '16'
EOF = -1 # Variable c_int '-0x00000000000000001'
SF_SUSTAIN = 2048 # Variable c_int '2048'
__have_pthread_attr_t = 1 # Variable c_int '1'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
__WCLONE = 2147483648 # Variable c_uint '2147483648u'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_IONBF = 2 # Variable c_int '2'
_IO_USER_BUF = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
__time_t_defined = 1 # Variable c_int '1'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__WCOREFLAG = 128 # Variable c_int '128'
_STRUCT_TIMEVAL = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
__USE_ISOC11 = 1 # Variable c_int '1'
SEEK_SET = 0 # Variable c_int '0'
WNOWAIT = 16777216 # Variable c_int '16777216'
__USE_POSIX199309 = 1 # Variable c_int '1'
_IO_LINE_BUF = 512 # Variable c_int '512'
__SIZEOF_PTHREAD_RWLOCKATTR_T = 8 # Variable c_int '8'
INSTNOTES = 120 # Variable c_int '120'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
DMODE_STEREO = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_CONDATTR_T = 4 # Variable c_int '4'
_IO_LEFT = 2 # Variable c_int '2'
DMODE_SIMDMIXER = 2048 # Variable c_int '2048'
SF_PLAYBACKMASK = 3072 # Variable c_int '3072'
UF_HIGHBPM = 64 # Variable c_int '64'
_IO_SHOWPOINT = 256 # Variable c_int '256'
_IO_RIGHT = 4 # Variable c_int '4'
_IOS_APPEND = 8 # Variable c_int '8'
PAN_HALFRIGHT = 192 # Variable c_int '192'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
__USE_ATFILE = 1 # Variable c_int '1'
UF_S3MSLIDES = 16 # Variable c_int '16'
__lldiv_t_defined = 1 # Variable c_int '1'
TMP_MAX = 238328 # Variable c_int '238328'
_SYS_SELECT_H = 1 # Variable c_int '1'
FOPEN_MAX = 16 # Variable c_int '16'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
__SIZEOF_PTHREAD_MUTEXATTR_T = 4 # Variable c_int '4'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
_IO_DEC = 16 # Variable c_int '16'
MUTE_INCLUSIVE = 32001 # Variable c_int '32001'
SF_EXTRAPLAYBACKMASK = 12288 # Variable c_int '12288'
__USE_POSIX = 1 # Variable c_int '1'
_IO_NO_WRITES = 8 # Variable c_int '8'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
_STDLIB_H = 1 # Variable c_int '1'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
_ALLOCA_H = 1 # Variable c_int '1'
__FILE_defined = 1 # Variable c_int '1'
__clock_t_defined = 1 # Variable c_int '1'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
DMODE_16BITS = 1 # Variable c_int '1'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
__USE_XOPEN = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944 # Variable c_uint '4222418944u'
_IO_NO_READS = 4 # Variable c_int '4'
SF_FORMATMASK = 63 # Variable c_int '63'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 19 # Variable c_int '19'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
SF_OWNPAN = 4096 # Variable c_int '4096'
_IO_UPPERCASE = 512 # Variable c_int '512'
__clockid_t_defined = 1 # Variable c_int '1'
_IO_SHOWBASE = 128 # Variable c_int '128'
__timer_t_defined = 1 # Variable c_int '1'
PAN_RIGHT = 255 # Variable c_int '255'
MUTE_EXCLUSIVE = 32000 # Variable c_int '32000'
SF_DELTA = 16 # Variable c_int '16'
_G_HAVE_MMAP = 1 # Variable c_int '1'
_IO_FIXED = 4096 # Variable c_int '4096'
LIBMIKMOD_VERSION_MAJOR = 3 # Variable c_long '3l'
__ldiv_t_defined = 1 # Variable c_int '1'
SF_LOOP = 256 # Variable c_int '256'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIER_T = 32 # Variable c_int '32'
_SYS_TYPES_H = 1 # Variable c_int '1'
____mbstate_t_defined = 1 # Variable c_int '1'
LIBMIKMOD_VERSION = 197381 # Variable c_long '197381l'
_IO_EOF_SEEN = 16 # Variable c_int '16'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
_IO_ERR_SEEN = 32 # Variable c_int '32'
_IOFBF = 0 # Variable c_int '0'
_IO_SKIPWS = 1 # Variable c_int '1'
__timespec_defined = 1 # Variable c_int '1'
UF_FT2QUIRKS = 512 # Variable c_int '512'
SEEK_END = 2 # Variable c_int '2'
__USE_GNU = 1 # Variable c_int '1'
WUNTRACED = 2 # Variable c_int '2'
__USE_BSD = 1 # Variable c_int '1'
__USE_ISOC95 = 1 # Variable c_int '1'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
LIBMIKMOD_VERSION_MINOR = 3 # Variable c_long '3l'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_IO_IN_BACKUP = 256 # Variable c_int '256'
_IOS_NOREPLACE = 64 # Variable c_int '64'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIERATTR_T = 4 # Variable c_int '4'
_SIGSET_H_types = 1 # Variable c_int '1'
_ISOC11_SOURCE = 1 # Variable c_int '1'
DMODE_INTERP = 512 # Variable c_int '512'
____FILE_defined = 1 # Variable c_int '1'
L_tmpnam = 20 # Variable c_int '20'
__PTHREAD_RWLOCK_INT_FLAGS_SHARED = 1 # Variable c_int '1'
SEEK_CUR = 1 # Variable c_int '1'
UF_BGSLIDES = 32 # Variable c_int '32'
PAN_CENTER = 128 # Variable c_int '128'
__USE_SVID = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_MUTEX_T = 40 # Variable c_int '40'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
__USE_POSIX199506 = 1 # Variable c_int '1'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
__USE_MISC = 1 # Variable c_int '1'
DMODE_HQMIXER = 16 # Variable c_int '16'
SF_UST_LOOP = 8192 # Variable c_int '8192'
UF_PANNING = 1024 # Variable c_int '1024'
__WNOTHREAD = 536870912 # Variable c_int '536870912'
UF_LINEAR = 2 # Variable c_int '2'
__W_CONTINUED = 65535 # Variable c_int '65535'
RAND_MAX = 2147483647 # Variable c_int '2147483647'
_IO_OCT = 32 # Variable c_int '32'
PAN_HALFLEFT = 64 # Variable c_int '64'
_IOS_TRUNC = 16 # Variable c_int '16'
__PTHREAD_MUTEX_HAVE_ELISION = 1 # Variable c_int '1'
L_ctermid = 9 # Variable c_int '9'
_IOS_BIN = 128 # Variable c_int '128'
__OFF_T_MATCHES_OFF64_T = 1 # Variable c_int '1'
_ATFILE_SOURCE = 1 # Variable c_int '1'
_ENDIAN_H = 1 # Variable c_int '1'
__PTHREAD_MUTEX_HAVE_PREV = 1 # Variable c_int '1'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_RWLOCK_T = 56 # Variable c_int '56'
_BITS_BYTESWAP_H = 1 # Variable c_int '1'
WNOHANG = 1 # Variable c_int '1'
_IO_LINKED = 128 # Variable c_int '128'
LIBMIKMOD_REVISION = 5 # Variable c_long '5l'
_IOS_NOCREATE = 32 # Variable c_int '32'
PAN_LEFT = 0 # Variable c_int '0'
FILENAME_MAX = 4096 # Variable c_int '4096'
L_cuserid = 9 # Variable c_int '9'
_SYS_SYSMACROS_H = 1 # Variable c_int '1'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
SEEK_HOLE = 4 # Variable c_int '4'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
SF_STEREO = 2 # Variable c_int '2'
EXIT_SUCCESS = 0 # Variable c_int '0'
DMODE_SOFT_MUSIC = 8 # Variable c_int '8'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_COND_T = 48 # Variable c_int '48'
_FEATURES_H = 1 # Variable c_int '1'
_IO_HEX = 64 # Variable c_int '64'
__BIT_TYPES_DEFINED__ = 1 # Variable c_int '1'
SEEK_DATA = 3 # Variable c_int '3'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
UF_NOWRAP = 128 # Variable c_int '128'
_IOS_INPUT = 1 # Variable c_int '1'
SF_BIG_ENDIAN = 8 # Variable c_int '8'
__WALL = 1073741824 # Variable c_int '1073741824'
_IO_UNITBUF = 8192 # Variable c_int '8192'
_BITS_TYPES_H = 1 # Variable c_int '1'
DMODE_SOFT_SNDFX = 4 # Variable c_int '4'
_STDIO_H = 1 # Variable c_int '1'
PAN_SURROUND = 512 # Variable c_int '512'
SF_BIDI = 512 # Variable c_int '512'
__INO_T_MATCHES_INO64_T = 1 # Variable c_int '1'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
DMODE_FLOAT = 32 # Variable c_int '32'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
SF_SIGNED = 4 # Variable c_int '4'
DMODE_NOISEREDUCTION = 4096 # Variable c_int '4096'
UF_XMPERIODS = 1 # Variable c_int '1'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
UF_NNA = 8 # Variable c_int '8'
_IO_MAGIC_MASK = 4294901760 # Variable c_uint '4294901760u'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
_G_config_h = 1 # Variable c_int '1'
DMODE_SURROUND = 256 # Variable c_int '256'
_IO_UNBUFFERED = 2 # Variable c_int '2'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_OLD_STDIO_MAGIC = 4206624768 # Variable c_uint '4206624768u'
WEXITED = 4 # Variable c_int '4'
_XOPEN_SOURCE = 700 # Variable c_int '700'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
__SIZEOF_PTHREAD_ATTR_T = 56 # Variable c_int '56'
_IOS_ATEND = 4 # Variable c_int '4'
UF_MAXCHAN = 64 # Variable c_int '64'
SF_16BITS = 1 # Variable c_int '1'
_IOS_OUTPUT = 2 # Variable c_int '2'
_SIGSET_NWORDS = 16 # Variable c_ulong '16ul'
UF_INST = 4 # Variable c_int '4'
SF_ITPACKED = 32 # Variable c_int '32'
__GLIBC__ = 2 # Variable c_int '2'
UF_ARPMEM = 256 # Variable c_int '256'
__USE_ISOC99 = 1 # Variable c_int '1'
_BITS_PTHREADTYPES_H = 1 # Variable c_int '1'
DMODE_REVERSE = 1024 # Variable c_int '1024'
WCONTINUED = 8 # Variable c_int '8'
SFX_CRITICAL = 1 # Variable c_int '1'
ENVPOINTS = 32 # Variable c_int '32'
_IO_INTERNAL = 8 # Variable c_int '8'
EXIT_FAILURE = 1 # Variable c_int '1'
SF_REVERSE = 1024 # Variable c_int '1024'
_BSD_SOURCE = 1 # Variable c_int '1'
_IOLBF = 1 # Variable c_int '1'
_XLOCALE_H = 1 # Variable c_int '1'
__FD_ZERO_STOS = 'stosq' # Variable STRING '(const char*)"stosq"'
pthread_t = c_ulong
class pthread_attr_t(Union):
    pass
pthread_attr_t._fields_ = [
    ('__size', c_char * 56),
    ('__align', c_long),
]
class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._fields_ = [
    ('__prev', POINTER(__pthread_internal_list)),
    ('__next', POINTER(__pthread_internal_list)),
]
__pthread_list_t = __pthread_internal_list
class __pthread_mutex_s(Structure):
    pass
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]
class pthread_mutex_t(Union):
    pass
pthread_mutex_t._fields_ = [
    ('__data', __pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]
class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
class N14pthread_cond_t4DOT_16E(Structure):
    pass
N14pthread_cond_t4DOT_16E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class pthread_cond_t(Union):
    pass
pthread_cond_t._fields_ = [
    ('__data', N14pthread_cond_t4DOT_16E),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]
class pthread_condattr_t(Union):
    pass
pthread_condattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_19E(Structure):
    pass
N16pthread_rwlock_t4DOT_19E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class pthread_rwlock_t(Union):
    pass
pthread_rwlock_t._fields_ = [
    ('__data', N16pthread_rwlock_t4DOT_19E),
    ('__size', c_char * 56),
    ('__align', c_long),
]
class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]
pthread_spinlock_t = c_int
class pthread_barrier_t(Union):
    pass
pthread_barrier_t._fields_ = [
    ('__size', c_char * 32),
    ('__align', c_long),
]
class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
__fdelt_chk = _libraries['/usr/lib/libmikmod.so'].__fdelt_chk
__fdelt_chk.restype = c_long
__fdelt_chk.argtypes = [c_long]
__fdelt_warn = _libraries['/usr/lib/libmikmod.so'].__fdelt_warn
__fdelt_warn.restype = c_long
__fdelt_warn.argtypes = [c_long]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
getchar = _libraries['/usr/lib/libmikmod.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
FILE = _IO_FILE
fgetc_unlocked = _libraries['/usr/lib/libmikmod.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/lib/libmikmod.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/lib/libmikmod.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/lib/libmikmod.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/lib/libmikmod.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/lib/libmikmod.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/lib/libmikmod.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/lib/libmikmod.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/lib/libmikmod.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/lib/libmikmod.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
__sprintf_chk = _libraries['/usr/lib/libmikmod.so'].__sprintf_chk
__sprintf_chk.restype = c_int
__sprintf_chk.argtypes = [STRING, c_int, size_t, STRING]
__vsprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vsprintf_chk
__vsprintf_chk.restype = c_int
__vsprintf_chk.argtypes = [STRING, c_int, size_t, STRING, POINTER(__va_list_tag)]
sprintf = _libraries['/usr/lib/libmikmod.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vsprintf = _libraries['/usr/lib/libmikmod.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
__snprintf_chk = _libraries['/usr/lib/libmikmod.so'].__snprintf_chk
__snprintf_chk.restype = c_int
__snprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING]
__vsnprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vsnprintf_chk
__vsnprintf_chk.restype = c_int
__vsnprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['/usr/lib/libmikmod.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/lib/libmikmod.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
__fprintf_chk = _libraries['/usr/lib/libmikmod.so'].__fprintf_chk
__fprintf_chk.restype = c_int
__fprintf_chk.argtypes = [POINTER(FILE), c_int, STRING]
__printf_chk = _libraries['/usr/lib/libmikmod.so'].__printf_chk
__printf_chk.restype = c_int
__printf_chk.argtypes = [c_int, STRING]
__vfprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vfprintf_chk
__vfprintf_chk.restype = c_int
__vfprintf_chk.argtypes = [POINTER(FILE), c_int, STRING, POINTER(__va_list_tag)]
__vprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vprintf_chk
__vprintf_chk.restype = c_int
__vprintf_chk.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
fprintf = _libraries['/usr/lib/libmikmod.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/lib/libmikmod.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
vprintf = _libraries['/usr/lib/libmikmod.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
vfprintf = _libraries['/usr/lib/libmikmod.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
__dprintf_chk = _libraries['/usr/lib/libmikmod.so'].__dprintf_chk
__dprintf_chk.restype = c_int
__dprintf_chk.argtypes = [c_int, c_int, STRING]
__vdprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vdprintf_chk
__vdprintf_chk.restype = c_int
__vdprintf_chk.argtypes = [c_int, c_int, STRING, POINTER(__va_list_tag)]
dprintf = _libraries['/usr/lib/libmikmod.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
vdprintf = _libraries['/usr/lib/libmikmod.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
__asprintf_chk = _libraries['/usr/lib/libmikmod.so'].__asprintf_chk
__asprintf_chk.restype = c_int
__asprintf_chk.argtypes = [POINTER(STRING), c_int, STRING]
__vasprintf_chk = _libraries['/usr/lib/libmikmod.so'].__vasprintf_chk
__vasprintf_chk.restype = c_int
__vasprintf_chk.argtypes = [POINTER(STRING), c_int, STRING, POINTER(__va_list_tag)]
class obstack(Structure):
    pass
__obstack_printf_chk = _libraries['/usr/lib/libmikmod.so'].__obstack_printf_chk
__obstack_printf_chk.restype = c_int
__obstack_printf_chk.argtypes = [POINTER(obstack), c_int, STRING]
__obstack_vprintf_chk = _libraries['/usr/lib/libmikmod.so'].__obstack_vprintf_chk
__obstack_vprintf_chk.restype = c_int
__obstack_vprintf_chk.argtypes = [POINTER(obstack), c_int, STRING, POINTER(__va_list_tag)]
asprintf = _libraries['/usr/lib/libmikmod.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
__asprintf = _libraries['/usr/lib/libmikmod.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
obstack_printf = _libraries['/usr/lib/libmikmod.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
vasprintf = _libraries['/usr/lib/libmikmod.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
obstack_vprintf = _libraries['/usr/lib/libmikmod.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, POINTER(__va_list_tag)]
__fgets_chk = _libraries['/usr/lib/libmikmod.so'].__fgets_chk
__fgets_chk.restype = STRING
__fgets_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets = _libraries['/usr/lib/libmikmod.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_chk = _libraries['/usr/lib/libmikmod.so'].__fread_chk
__fread_chk.restype = size_t
__fread_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread = _libraries['/usr/lib/libmikmod.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__fgets_unlocked_chk = _libraries['/usr/lib/libmikmod.so'].__fgets_unlocked_chk
__fgets_unlocked_chk.restype = STRING
__fgets_unlocked_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets_unlocked = _libraries['/usr/lib/libmikmod.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_unlocked_chk = _libraries['/usr/lib/libmikmod.so'].__fread_unlocked_chk
__fread_unlocked_chk.restype = size_t
__fread_unlocked_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread_unlocked = _libraries['/usr/lib/libmikmod.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
bsearch = _libraries['/usr/lib/libmikmod.so'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
atof = _libraries['/usr/lib/libmikmod.so'].atof
atof.restype = c_double
atof.argtypes = [STRING]
__realpath_chk = _libraries['/usr/lib/libmikmod.so'].__realpath_chk
__realpath_chk.restype = STRING
__realpath_chk.argtypes = [STRING, STRING, size_t]
realpath = _libraries['/usr/lib/libmikmod.so'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__ptsname_r_chk = _libraries['/usr/lib/libmikmod.so'].__ptsname_r_chk
__ptsname_r_chk.restype = c_int
__ptsname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ptsname_r = _libraries['/usr/lib/libmikmod.so'].ptsname_r
ptsname_r.restype = c_int
ptsname_r.argtypes = [c_int, STRING, size_t]
__wctomb_chk = _libraries['/usr/lib/libmikmod.so'].__wctomb_chk
__wctomb_chk.restype = c_int
__wctomb_chk.argtypes = [STRING, c_wchar, size_t]
wctomb = _libraries['/usr/lib/libmikmod.so'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
__mbstowcs_chk = _libraries['/usr/lib/libmikmod.so'].__mbstowcs_chk
__mbstowcs_chk.restype = size_t
__mbstowcs_chk.argtypes = [WSTRING, STRING, size_t, size_t]
mbstowcs = _libraries['/usr/lib/libmikmod.so'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
__wcstombs_chk = _libraries['/usr/lib/libmikmod.so'].__wcstombs_chk
__wcstombs_chk.restype = size_t
__wcstombs_chk.argtypes = [STRING, WSTRING, size_t, size_t]
wcstombs = _libraries['/usr/lib/libmikmod.so'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmikmod.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmikmod.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmikmod.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmikmod.so'], '_sys_errlist')
class timeval(Structure):
    pass
__time_t = c_long
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__clock_t = c_long
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__key_t = c_int
__clockid_t = c_int
__timer_t = c_void_p
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__fsword_t = c_long
__syscall_slong_t = c_long
__syscall_ulong_t = c_ulong
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
class wait(Union):
    pass
class N4wait3DOT_6E(Structure):
    pass
N4wait3DOT_6E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait3DOT_7E(Structure):
    pass
N4wait3DOT_7E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait3DOT_6E),
    ('__wait_stopped', N4wait3DOT_7E),
]
class _IO_jump_t(Structure):
    pass
_IO_jump_t._fields_ = [
]
_IO_lock_t = None
class _IO_marker(Structure):
    pass
_IO_marker._fields_ = [
    ('_next', POINTER(_IO_marker)),
    ('_sbuf', POINTER(_IO_FILE)),
    ('_pos', c_int),
]

# values for enumeration '__codecvt_result'
__codecvt_result = c_int # enum
_IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', STRING),
    ('_IO_read_end', STRING),
    ('_IO_read_base', STRING),
    ('_IO_write_base', STRING),
    ('_IO_write_ptr', STRING),
    ('_IO_write_end', STRING),
    ('_IO_buf_base', STRING),
    ('_IO_buf_end', STRING),
    ('_IO_save_base', STRING),
    ('_IO_backup_base', STRING),
    ('_IO_save_end', STRING),
    ('_markers', POINTER(_IO_marker)),
    ('_chain', POINTER(_IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_byte),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', c_void_p),
    ('__pad2', c_void_p),
    ('__pad3', c_void_p),
    ('__pad4', c_void_p),
    ('__pad5', size_t),
    ('_mode', c_int),
    ('_unused2', c_char * 20),
]
class _IO_FILE_plus(Structure):
    pass
_IO_FILE_plus._fields_ = [
]
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmikmod.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmikmod.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmikmod.so'], '_IO_2_1_stderr_')
__io_read_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_write_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_seek_fn = CFUNCTYPE(c_int, c_void_p, POINTER(__off64_t), c_int)
__io_close_fn = CFUNCTYPE(c_int, c_void_p)
cookie_read_function_t = __io_read_fn
cookie_write_function_t = __io_write_fn
cookie_seek_function_t = __io_seek_fn
cookie_close_function_t = __io_close_fn
class _IO_cookie_io_functions_t(Structure):
    pass
_IO_cookie_io_functions_t._fields_ = [
    ('read', POINTER(__io_read_fn)),
    ('write', POINTER(__io_write_fn)),
    ('seek', POINTER(__io_seek_fn)),
    ('close', POINTER(__io_close_fn)),
]
cookie_io_functions_t = _IO_cookie_io_functions_t
class _IO_cookie_file(Structure):
    pass
_IO_cookie_file._fields_ = [
]
__underflow = _libraries['/usr/lib/libmikmod.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/lib/libmikmod.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/lib/libmikmod.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/lib/libmikmod.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/lib/libmikmod.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/lib/libmikmod.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/lib/libmikmod.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/lib/libmikmod.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/lib/libmikmod.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/lib/libmikmod.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/lib/libmikmod.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/lib/libmikmod.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag), POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/lib/libmikmod.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag)]
_IO_padn = _libraries['/usr/lib/libmikmod.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/lib/libmikmod.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/lib/libmikmod.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/lib/libmikmod.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/lib/libmikmod.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
MikMod_GetVersion = _libraries['/usr/lib/libmikmod.so'].MikMod_GetVersion
MikMod_GetVersion.restype = c_long
MikMod_GetVersion.argtypes = []
CHAR = c_char
SBYTE = c_byte
UBYTE = c_ubyte
SWORD = c_short
UWORD = c_ushort
SLONG = c_int
ULONG = c_uint
BOOL = c_int

# values for unnamed enumeration
MikMod_handler = CFUNCTYPE(None)
MikMod_handler_t = POINTER(MikMod_handler)
MikMod_errno = (c_int).in_dll(_libraries['/usr/lib/libmikmod.so'], 'MikMod_errno')
MikMod_critical = (BOOL).in_dll(_libraries['/usr/lib/libmikmod.so'], 'MikMod_critical')
MikMod_strerror = _libraries['/usr/lib/libmikmod.so'].MikMod_strerror
MikMod_strerror.restype = STRING
MikMod_strerror.argtypes = [c_int]
MikMod_RegisterErrorHandler = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterErrorHandler
MikMod_RegisterErrorHandler.restype = MikMod_handler_t
MikMod_RegisterErrorHandler.argtypes = [MikMod_handler_t]
MikMod_RegisterAllDrivers = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterAllDrivers
MikMod_RegisterAllDrivers.restype = None
MikMod_RegisterAllDrivers.argtypes = []
MikMod_InfoDriver = _libraries['/usr/lib/libmikmod.so'].MikMod_InfoDriver
MikMod_InfoDriver.restype = STRING
MikMod_InfoDriver.argtypes = []
class MDRIVER(Structure):
    pass
MikMod_RegisterDriver = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterDriver
MikMod_RegisterDriver.restype = None
MikMod_RegisterDriver.argtypes = [POINTER(MDRIVER)]
MikMod_DriverFromAlias = _libraries['/usr/lib/libmikmod.so'].MikMod_DriverFromAlias
MikMod_DriverFromAlias.restype = c_int
MikMod_DriverFromAlias.argtypes = [STRING]
MikMod_DriverByOrdinal = _libraries['/usr/lib/libmikmod.so'].MikMod_DriverByOrdinal
MikMod_DriverByOrdinal.restype = POINTER(MDRIVER)
MikMod_DriverByOrdinal.argtypes = [c_int]
MikMod_Init = _libraries['/usr/lib/libmikmod.so'].MikMod_Init
MikMod_Init.restype = c_int
MikMod_Init.argtypes = [STRING]
MikMod_Exit = _libraries['/usr/lib/libmikmod.so'].MikMod_Exit
MikMod_Exit.restype = None
MikMod_Exit.argtypes = []
MikMod_Reset = _libraries['/usr/lib/libmikmod.so'].MikMod_Reset
MikMod_Reset.restype = c_int
MikMod_Reset.argtypes = [STRING]
MikMod_SetNumVoices = _libraries['/usr/lib/libmikmod.so'].MikMod_SetNumVoices
MikMod_SetNumVoices.restype = c_int
MikMod_SetNumVoices.argtypes = [c_int, c_int]
MikMod_Active = _libraries['/usr/lib/libmikmod.so'].MikMod_Active
MikMod_Active.restype = BOOL
MikMod_Active.argtypes = []
MikMod_EnableOutput = _libraries['/usr/lib/libmikmod.so'].MikMod_EnableOutput
MikMod_EnableOutput.restype = c_int
MikMod_EnableOutput.argtypes = []
MikMod_DisableOutput = _libraries['/usr/lib/libmikmod.so'].MikMod_DisableOutput
MikMod_DisableOutput.restype = None
MikMod_DisableOutput.argtypes = []
MikMod_Update = _libraries['/usr/lib/libmikmod.so'].MikMod_Update
MikMod_Update.restype = None
MikMod_Update.argtypes = []
MikMod_InitThreads = _libraries['/usr/lib/libmikmod.so'].MikMod_InitThreads
MikMod_InitThreads.restype = BOOL
MikMod_InitThreads.argtypes = []
MikMod_Lock = _libraries['/usr/lib/libmikmod.so'].MikMod_Lock
MikMod_Lock.restype = None
MikMod_Lock.argtypes = []
MikMod_Unlock = _libraries['/usr/lib/libmikmod.so'].MikMod_Unlock
MikMod_Unlock.restype = None
MikMod_Unlock.argtypes = []
MikMod_malloc = _libraries['/usr/lib/libmikmod.so'].MikMod_malloc
MikMod_malloc.restype = c_void_p
MikMod_malloc.argtypes = [size_t]
MikMod_calloc = _libraries['/usr/lib/libmikmod.so'].MikMod_calloc
MikMod_calloc.restype = c_void_p
MikMod_calloc.argtypes = [size_t, size_t]
MikMod_realloc = _libraries['/usr/lib/libmikmod.so'].MikMod_realloc
MikMod_realloc.restype = c_void_p
MikMod_realloc.argtypes = [c_void_p, size_t]
MikMod_strdup = _libraries['/usr/lib/libmikmod.so'].MikMod_strdup
MikMod_strdup.restype = STRING
MikMod_strdup.argtypes = [STRING]
MikMod_free = _libraries['/usr/lib/libmikmod.so'].MikMod_free
MikMod_free.restype = None
MikMod_free.argtypes = [c_void_p]
class MREADER(Structure):
    pass
MREADER._fields_ = [
    ('Seek', CFUNCTYPE(c_int, POINTER(MREADER), c_long, c_int)),
    ('Tell', CFUNCTYPE(c_long, POINTER(MREADER))),
    ('Read', CFUNCTYPE(BOOL, POINTER(MREADER), c_void_p, size_t)),
    ('Get', CFUNCTYPE(c_int, POINTER(MREADER))),
    ('Eof', CFUNCTYPE(BOOL, POINTER(MREADER))),
    ('iobase', c_long),
    ('prev_iobase', c_long),
]
class MWRITER(Structure):
    pass
MWRITER._fields_ = [
    ('Seek', CFUNCTYPE(c_int, POINTER(MWRITER), c_long, c_int)),
    ('Tell', CFUNCTYPE(c_long, POINTER(MWRITER))),
    ('Write', CFUNCTYPE(BOOL, POINTER(MWRITER), c_void_p, size_t)),
    ('Put', CFUNCTYPE(c_int, POINTER(MWRITER), c_int)),
]
class SAMPLE(Structure):
    pass
SAMPLE._fields_ = [
    ('panning', SWORD),
    ('speed', ULONG),
    ('volume', UBYTE),
    ('inflags', UWORD),
    ('flags', UWORD),
    ('length', ULONG),
    ('loopstart', ULONG),
    ('loopend', ULONG),
    ('susbegin', ULONG),
    ('susend', ULONG),
    ('globvol', UBYTE),
    ('vibflags', UBYTE),
    ('vibtype', UBYTE),
    ('vibsweep', UBYTE),
    ('vibdepth', UBYTE),
    ('vibrate', UBYTE),
    ('samplename', STRING),
    ('avibpos', UWORD),
    ('divfactor', UBYTE),
    ('seekpos', ULONG),
    ('handle', SWORD),
    ('onfree', CFUNCTYPE(None, c_void_p)),
    ('ctx', c_void_p),
]
Sample_LoadRaw = _libraries['/usr/lib/libmikmod.so'].Sample_LoadRaw
Sample_LoadRaw.restype = POINTER(SAMPLE)
Sample_LoadRaw.argtypes = [STRING, ULONG, ULONG, ULONG]
Sample_LoadRawFP = _libraries['/usr/lib/libmikmod.so'].Sample_LoadRawFP
Sample_LoadRawFP.restype = POINTER(SAMPLE)
Sample_LoadRawFP.argtypes = [POINTER(FILE), ULONG, ULONG, ULONG]
Sample_LoadRawMem = _libraries['/usr/lib/libmikmod.so'].Sample_LoadRawMem
Sample_LoadRawMem.restype = POINTER(SAMPLE)
Sample_LoadRawMem.argtypes = [STRING, c_int, ULONG, ULONG, ULONG]
Sample_LoadRawGeneric = _libraries['/usr/lib/libmikmod.so'].Sample_LoadRawGeneric
Sample_LoadRawGeneric.restype = POINTER(SAMPLE)
Sample_LoadRawGeneric.argtypes = [POINTER(MREADER), ULONG, ULONG, ULONG]
Sample_Load = _libraries['/usr/lib/libmikmod.so'].Sample_Load
Sample_Load.restype = POINTER(SAMPLE)
Sample_Load.argtypes = [STRING]
Sample_LoadFP = _libraries['/usr/lib/libmikmod.so'].Sample_LoadFP
Sample_LoadFP.restype = POINTER(SAMPLE)
Sample_LoadFP.argtypes = [POINTER(FILE)]
Sample_LoadMem = _libraries['/usr/lib/libmikmod.so'].Sample_LoadMem
Sample_LoadMem.restype = POINTER(SAMPLE)
Sample_LoadMem.argtypes = [STRING, c_int]
Sample_LoadGeneric = _libraries['/usr/lib/libmikmod.so'].Sample_LoadGeneric
Sample_LoadGeneric.restype = POINTER(SAMPLE)
Sample_LoadGeneric.argtypes = [POINTER(MREADER)]
Sample_Free = _libraries['/usr/lib/libmikmod.so'].Sample_Free
Sample_Free.restype = None
Sample_Free.argtypes = [POINTER(SAMPLE)]
Sample_Play = _libraries['/usr/lib/libmikmod.so'].Sample_Play
Sample_Play.restype = SBYTE
Sample_Play.argtypes = [POINTER(SAMPLE), ULONG, UBYTE]
Voice_SetVolume = _libraries['/usr/lib/libmikmod.so'].Voice_SetVolume
Voice_SetVolume.restype = None
Voice_SetVolume.argtypes = [SBYTE, UWORD]
Voice_GetVolume = _libraries['/usr/lib/libmikmod.so'].Voice_GetVolume
Voice_GetVolume.restype = UWORD
Voice_GetVolume.argtypes = [SBYTE]
Voice_SetFrequency = _libraries['/usr/lib/libmikmod.so'].Voice_SetFrequency
Voice_SetFrequency.restype = None
Voice_SetFrequency.argtypes = [SBYTE, ULONG]
Voice_GetFrequency = _libraries['/usr/lib/libmikmod.so'].Voice_GetFrequency
Voice_GetFrequency.restype = ULONG
Voice_GetFrequency.argtypes = [SBYTE]
Voice_SetPanning = _libraries['/usr/lib/libmikmod.so'].Voice_SetPanning
Voice_SetPanning.restype = None
Voice_SetPanning.argtypes = [SBYTE, ULONG]
Voice_GetPanning = _libraries['/usr/lib/libmikmod.so'].Voice_GetPanning
Voice_GetPanning.restype = ULONG
Voice_GetPanning.argtypes = [SBYTE]
Voice_Play = _libraries['/usr/lib/libmikmod.so'].Voice_Play
Voice_Play.restype = None
Voice_Play.argtypes = [SBYTE, POINTER(SAMPLE), ULONG]
Voice_Stop = _libraries['/usr/lib/libmikmod.so'].Voice_Stop
Voice_Stop.restype = None
Voice_Stop.argtypes = [SBYTE]
Voice_Stopped = _libraries['/usr/lib/libmikmod.so'].Voice_Stopped
Voice_Stopped.restype = BOOL
Voice_Stopped.argtypes = [SBYTE]
Voice_GetPosition = _libraries['/usr/lib/libmikmod.so'].Voice_GetPosition
Voice_GetPosition.restype = SLONG
Voice_GetPosition.argtypes = [SBYTE]
Voice_RealVolume = _libraries['/usr/lib/libmikmod.so'].Voice_RealVolume
Voice_RealVolume.restype = ULONG
Voice_RealVolume.argtypes = [SBYTE]
class ENVPT(Structure):
    pass
ENVPT._fields_ = [
    ('pos', SWORD),
    ('val', SWORD),
]
class INSTRUMENT(Structure):
    pass
INSTRUMENT._fields_ = [
    ('insname', STRING),
    ('flags', UBYTE),
    ('samplenumber', UWORD * 120),
    ('samplenote', UBYTE * 120),
    ('nnatype', UBYTE),
    ('dca', UBYTE),
    ('dct', UBYTE),
    ('globvol', UBYTE),
    ('volfade', UWORD),
    ('panning', SWORD),
    ('pitpansep', UBYTE),
    ('pitpancenter', UBYTE),
    ('rvolvar', UBYTE),
    ('rpanvar', UBYTE),
    ('volflg', UBYTE),
    ('volpts', UBYTE),
    ('volsusbeg', UBYTE),
    ('volsusend', UBYTE),
    ('volbeg', UBYTE),
    ('volend', UBYTE),
    ('volenv', ENVPT * 32),
    ('panflg', UBYTE),
    ('panpts', UBYTE),
    ('pansusbeg', UBYTE),
    ('pansusend', UBYTE),
    ('panbeg', UBYTE),
    ('panend', UBYTE),
    ('panenv', ENVPT * 32),
    ('pitflg', UBYTE),
    ('pitpts', UBYTE),
    ('pitsusbeg', UBYTE),
    ('pitsusend', UBYTE),
    ('pitbeg', UBYTE),
    ('pitend', UBYTE),
    ('pitenv', ENVPT * 32),
]
class MP_CONTROL(Structure):
    pass
MP_CONTROL._fields_ = [
]
class MP_VOICE(Structure):
    pass
MP_VOICE._fields_ = [
]
class MODULE(Structure):
    pass
MODULE._fields_ = [
    ('songname', STRING),
    ('modtype', STRING),
    ('comment', STRING),
    ('flags', UWORD),
    ('numchn', UBYTE),
    ('numvoices', UBYTE),
    ('numpos', UWORD),
    ('numpat', UWORD),
    ('numins', UWORD),
    ('numsmp', UWORD),
    ('instruments', POINTER(INSTRUMENT)),
    ('samples', POINTER(SAMPLE)),
    ('realchn', UBYTE),
    ('totalchn', UBYTE),
    ('reppos', UWORD),
    ('initspeed', UBYTE),
    ('inittempo', UWORD),
    ('initvolume', UBYTE),
    ('panning', UWORD * 64),
    ('chanvol', UBYTE * 64),
    ('bpm', UWORD),
    ('sngspd', UWORD),
    ('volume', SWORD),
    ('extspd', BOOL),
    ('panflag', BOOL),
    ('wrap', BOOL),
    ('loop', BOOL),
    ('fadeout', BOOL),
    ('patpos', UWORD),
    ('sngpos', SWORD),
    ('sngtime', ULONG),
    ('relspd', SWORD),
    ('numtrk', UWORD),
    ('tracks', POINTER(POINTER(UBYTE))),
    ('patterns', POINTER(UWORD)),
    ('pattrows', POINTER(UWORD)),
    ('positions', POINTER(UWORD)),
    ('forbid', BOOL),
    ('numrow', UWORD),
    ('vbtick', UWORD),
    ('sngremainder', UWORD),
    ('control', POINTER(MP_CONTROL)),
    ('voice', POINTER(MP_VOICE)),
    ('globalslide', UBYTE),
    ('pat_repcrazy', UBYTE),
    ('patbrk', UWORD),
    ('patdly', UBYTE),
    ('patdly2', UBYTE),
    ('posjmp', SWORD),
    ('bpmlimit', UWORD),
]
class VOICEINFO(Structure):
    pass
VOICEINFO._fields_ = [
    ('i', POINTER(INSTRUMENT)),
    ('s', POINTER(SAMPLE)),
    ('panning', SWORD),
    ('volume', SBYTE),
    ('period', UWORD),
    ('kick', UBYTE),
]
class MLOADER(Structure):
    pass
MLOADER._fields_ = [
]
MikMod_InfoLoader = _libraries['/usr/lib/libmikmod.so'].MikMod_InfoLoader
MikMod_InfoLoader.restype = STRING
MikMod_InfoLoader.argtypes = []
MikMod_RegisterAllLoaders = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterAllLoaders
MikMod_RegisterAllLoaders.restype = None
MikMod_RegisterAllLoaders.argtypes = []
MikMod_RegisterLoader = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterLoader
MikMod_RegisterLoader.restype = None
MikMod_RegisterLoader.argtypes = [POINTER(MLOADER)]
load_669 = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_669')
load_amf = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_amf')
load_asy = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_asy')
load_dsm = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_dsm')
load_far = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_far')
load_gdm = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_gdm')
load_gt2 = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_gt2')
load_it = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_it')
load_imf = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_imf')
load_med = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_med')
load_m15 = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_m15')
load_mod = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_mod')
load_mtm = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_mtm')
load_okt = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_okt')
load_stm = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_stm')
load_stx = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_stx')
load_s3m = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_s3m')
load_ult = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_ult')
load_umx = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_umx')
load_uni = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_uni')
load_xm = (MLOADER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'load_xm')
Player_Load = _libraries['/usr/lib/libmikmod.so'].Player_Load
Player_Load.restype = POINTER(MODULE)
Player_Load.argtypes = [STRING, c_int, BOOL]
Player_LoadFP = _libraries['/usr/lib/libmikmod.so'].Player_LoadFP
Player_LoadFP.restype = POINTER(MODULE)
Player_LoadFP.argtypes = [POINTER(FILE), c_int, BOOL]
Player_LoadMem = _libraries['/usr/lib/libmikmod.so'].Player_LoadMem
Player_LoadMem.restype = POINTER(MODULE)
Player_LoadMem.argtypes = [STRING, c_int, c_int, BOOL]
Player_LoadGeneric = _libraries['/usr/lib/libmikmod.so'].Player_LoadGeneric
Player_LoadGeneric.restype = POINTER(MODULE)
Player_LoadGeneric.argtypes = [POINTER(MREADER), c_int, BOOL]
Player_LoadTitle = _libraries['/usr/lib/libmikmod.so'].Player_LoadTitle
Player_LoadTitle.restype = STRING
Player_LoadTitle.argtypes = [STRING]
Player_LoadTitleFP = _libraries['/usr/lib/libmikmod.so'].Player_LoadTitleFP
Player_LoadTitleFP.restype = STRING
Player_LoadTitleFP.argtypes = [POINTER(FILE)]
Player_LoadTitleMem = _libraries['/usr/lib/libmikmod.so'].Player_LoadTitleMem
Player_LoadTitleMem.restype = STRING
Player_LoadTitleMem.argtypes = [STRING, c_int]
Player_LoadTitleGeneric = _libraries['/usr/lib/libmikmod.so'].Player_LoadTitleGeneric
Player_LoadTitleGeneric.restype = STRING
Player_LoadTitleGeneric.argtypes = [POINTER(MREADER)]
Player_Free = _libraries['/usr/lib/libmikmod.so'].Player_Free
Player_Free.restype = None
Player_Free.argtypes = [POINTER(MODULE)]
Player_Start = _libraries['/usr/lib/libmikmod.so'].Player_Start
Player_Start.restype = None
Player_Start.argtypes = [POINTER(MODULE)]
Player_Active = _libraries['/usr/lib/libmikmod.so'].Player_Active
Player_Active.restype = BOOL
Player_Active.argtypes = []
Player_Stop = _libraries['/usr/lib/libmikmod.so'].Player_Stop
Player_Stop.restype = None
Player_Stop.argtypes = []
Player_TogglePause = _libraries['/usr/lib/libmikmod.so'].Player_TogglePause
Player_TogglePause.restype = None
Player_TogglePause.argtypes = []
Player_Paused = _libraries['/usr/lib/libmikmod.so'].Player_Paused
Player_Paused.restype = BOOL
Player_Paused.argtypes = []
Player_NextPosition = _libraries['/usr/lib/libmikmod.so'].Player_NextPosition
Player_NextPosition.restype = None
Player_NextPosition.argtypes = []
Player_PrevPosition = _libraries['/usr/lib/libmikmod.so'].Player_PrevPosition
Player_PrevPosition.restype = None
Player_PrevPosition.argtypes = []
Player_SetPosition = _libraries['/usr/lib/libmikmod.so'].Player_SetPosition
Player_SetPosition.restype = None
Player_SetPosition.argtypes = [UWORD]
Player_Muted = _libraries['/usr/lib/libmikmod.so'].Player_Muted
Player_Muted.restype = BOOL
Player_Muted.argtypes = [UBYTE]
Player_SetVolume = _libraries['/usr/lib/libmikmod.so'].Player_SetVolume
Player_SetVolume.restype = None
Player_SetVolume.argtypes = [SWORD]
Player_GetModule = _libraries['/usr/lib/libmikmod.so'].Player_GetModule
Player_GetModule.restype = POINTER(MODULE)
Player_GetModule.argtypes = []
Player_SetSpeed = _libraries['/usr/lib/libmikmod.so'].Player_SetSpeed
Player_SetSpeed.restype = None
Player_SetSpeed.argtypes = [UWORD]
Player_SetTempo = _libraries['/usr/lib/libmikmod.so'].Player_SetTempo
Player_SetTempo.restype = None
Player_SetTempo.argtypes = [UWORD]
Player_Unmute = _libraries['/usr/lib/libmikmod.so'].Player_Unmute
Player_Unmute.restype = None
Player_Unmute.argtypes = [SLONG]
Player_Mute = _libraries['/usr/lib/libmikmod.so'].Player_Mute
Player_Mute.restype = None
Player_Mute.argtypes = [SLONG]
Player_ToggleMute = _libraries['/usr/lib/libmikmod.so'].Player_ToggleMute
Player_ToggleMute.restype = None
Player_ToggleMute.argtypes = [SLONG]
Player_GetChannelVoice = _libraries['/usr/lib/libmikmod.so'].Player_GetChannelVoice
Player_GetChannelVoice.restype = c_int
Player_GetChannelVoice.argtypes = [UBYTE]
Player_GetChannelPeriod = _libraries['/usr/lib/libmikmod.so'].Player_GetChannelPeriod
Player_GetChannelPeriod.restype = UWORD
Player_GetChannelPeriod.argtypes = [UBYTE]
Player_QueryVoices = _libraries['/usr/lib/libmikmod.so'].Player_QueryVoices
Player_QueryVoices.restype = c_int
Player_QueryVoices.argtypes = [UWORD, POINTER(VOICEINFO)]
Player_GetRow = _libraries['/usr/lib/libmikmod.so'].Player_GetRow
Player_GetRow.restype = c_int
Player_GetRow.argtypes = []
Player_GetOrder = _libraries['/usr/lib/libmikmod.so'].Player_GetOrder
Player_GetOrder.restype = c_int
Player_GetOrder.argtypes = []
MikMod_player_t = CFUNCTYPE(None)
MikMod_callback_t = CFUNCTYPE(None, POINTER(c_ubyte), size_t)
MikMod_RegisterPlayer = _libraries['/usr/lib/libmikmod.so'].MikMod_RegisterPlayer
MikMod_RegisterPlayer.restype = MikMod_player_t
MikMod_RegisterPlayer.argtypes = [MikMod_player_t]

# values for unnamed enumeration

# values for unnamed enumeration
class SAMPLOAD(Structure):
    pass
SAMPLOAD._fields_ = [
]
MDRIVER._fields_ = [
    ('next', POINTER(MDRIVER)),
    ('Name', STRING),
    ('Version', STRING),
    ('HardVoiceLimit', UBYTE),
    ('SoftVoiceLimit', UBYTE),
    ('Alias', STRING),
    ('CmdLineHelp', STRING),
    ('CommandLine', CFUNCTYPE(None, STRING)),
    ('IsPresent', CFUNCTYPE(BOOL)),
    ('SampleLoad', CFUNCTYPE(SWORD, POINTER(SAMPLOAD), c_int)),
    ('SampleUnload', CFUNCTYPE(None, SWORD)),
    ('FreeSampleSpace', CFUNCTYPE(ULONG, c_int)),
    ('RealSampleLength', CFUNCTYPE(ULONG, c_int, POINTER(SAMPLE))),
    ('Init', CFUNCTYPE(c_int)),
    ('Exit', CFUNCTYPE(None)),
    ('Reset', CFUNCTYPE(c_int)),
    ('SetNumVoices', CFUNCTYPE(c_int)),
    ('PlayStart', CFUNCTYPE(c_int)),
    ('PlayStop', CFUNCTYPE(None)),
    ('Update', CFUNCTYPE(None)),
    ('Pause', CFUNCTYPE(None)),
    ('VoiceSetVolume', CFUNCTYPE(None, UBYTE, UWORD)),
    ('VoiceGetVolume', CFUNCTYPE(UWORD, UBYTE)),
    ('VoiceSetFrequency', CFUNCTYPE(None, UBYTE, ULONG)),
    ('VoiceGetFrequency', CFUNCTYPE(ULONG, UBYTE)),
    ('VoiceSetPanning', CFUNCTYPE(None, UBYTE, ULONG)),
    ('VoiceGetPanning', CFUNCTYPE(ULONG, UBYTE)),
    ('VoicePlay', CFUNCTYPE(None, UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD)),
    ('VoiceStop', CFUNCTYPE(None, UBYTE)),
    ('VoiceStopped', CFUNCTYPE(BOOL, UBYTE)),
    ('VoiceGetPosition', CFUNCTYPE(SLONG, UBYTE)),
    ('VoiceRealVolume', CFUNCTYPE(ULONG, UBYTE)),
]
md_volume = (UBYTE).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_volume')
md_musicvolume = (UBYTE).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_musicvolume')
md_sndfxvolume = (UBYTE).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_sndfxvolume')
md_reverb = (UBYTE).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_reverb')
md_pansep = (UBYTE).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_pansep')
md_device = (UWORD).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_device')
md_mixfreq = (UWORD).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_mixfreq')
md_mode = (UWORD).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_mode')
md_driver = (POINTER(MDRIVER)).in_dll(_libraries['/usr/lib/libmikmod.so'], 'md_driver')
drv_nos = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_nos')
drv_pipe = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_pipe')
drv_raw = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_raw')
drv_stdout = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_stdout')
drv_wav = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_wav')
drv_aiff = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_aiff')
drv_ultra = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_ultra')
drv_sam9407 = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_sam9407')
drv_AF = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_AF')
drv_aix = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_aix')
drv_alsa = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_alsa')
drv_esd = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_esd')
drv_pulseaudio = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_pulseaudio')
drv_hp = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_hp')
drv_nas = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_nas')
drv_oss = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_oss')
drv_openal = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_openal')
drv_sdl = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_sdl')
drv_sgi = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_sgi')
drv_sun = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_sun')
drv_dart = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_dart')
drv_os2 = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_os2')
drv_ds = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_ds')
drv_xaudio2 = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_xaudio2')
drv_win = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_win')
drv_mac = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_mac')
drv_osx = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_osx')
drv_gp32 = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_gp32')
drv_wss = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_wss')
drv_sb = (MDRIVER).in_dll(_libraries['/usr/lib/libmikmod.so'], 'drv_sb')
VC_Init = _libraries['/usr/lib/libmikmod.so'].VC_Init
VC_Init.restype = c_int
VC_Init.argtypes = []
VC_Exit = _libraries['/usr/lib/libmikmod.so'].VC_Exit
VC_Exit.restype = None
VC_Exit.argtypes = []
VC_SetCallback = _libraries['/usr/lib/libmikmod.so'].VC_SetCallback
VC_SetCallback.restype = None
VC_SetCallback.argtypes = [MikMod_callback_t]
VC_SetNumVoices = _libraries['/usr/lib/libmikmod.so'].VC_SetNumVoices
VC_SetNumVoices.restype = c_int
VC_SetNumVoices.argtypes = []
VC_SampleSpace = _libraries['/usr/lib/libmikmod.so'].VC_SampleSpace
VC_SampleSpace.restype = ULONG
VC_SampleSpace.argtypes = [c_int]
VC_SampleLength = _libraries['/usr/lib/libmikmod.so'].VC_SampleLength
VC_SampleLength.restype = ULONG
VC_SampleLength.argtypes = [c_int, POINTER(SAMPLE)]
VC_PlayStart = _libraries['/usr/lib/libmikmod.so'].VC_PlayStart
VC_PlayStart.restype = c_int
VC_PlayStart.argtypes = []
VC_PlayStop = _libraries['/usr/lib/libmikmod.so'].VC_PlayStop
VC_PlayStop.restype = None
VC_PlayStop.argtypes = []
VC_SampleLoad = _libraries['/usr/lib/libmikmod.so'].VC_SampleLoad
VC_SampleLoad.restype = SWORD
VC_SampleLoad.argtypes = [POINTER(SAMPLOAD), c_int]
VC_SampleUnload = _libraries['/usr/lib/libmikmod.so'].VC_SampleUnload
VC_SampleUnload.restype = None
VC_SampleUnload.argtypes = [SWORD]
VC_WriteBytes = _libraries['/usr/lib/libmikmod.so'].VC_WriteBytes
VC_WriteBytes.restype = ULONG
VC_WriteBytes.argtypes = [POINTER(SBYTE), ULONG]
VC_SilenceBytes = _libraries['/usr/lib/libmikmod.so'].VC_SilenceBytes
VC_SilenceBytes.restype = ULONG
VC_SilenceBytes.argtypes = [POINTER(SBYTE), ULONG]
VC_VoiceSetVolume = _libraries['/usr/lib/libmikmod.so'].VC_VoiceSetVolume
VC_VoiceSetVolume.restype = None
VC_VoiceSetVolume.argtypes = [UBYTE, UWORD]
VC_VoiceGetVolume = _libraries['/usr/lib/libmikmod.so'].VC_VoiceGetVolume
VC_VoiceGetVolume.restype = UWORD
VC_VoiceGetVolume.argtypes = [UBYTE]
VC_VoiceSetFrequency = _libraries['/usr/lib/libmikmod.so'].VC_VoiceSetFrequency
VC_VoiceSetFrequency.restype = None
VC_VoiceSetFrequency.argtypes = [UBYTE, ULONG]
VC_VoiceGetFrequency = _libraries['/usr/lib/libmikmod.so'].VC_VoiceGetFrequency
VC_VoiceGetFrequency.restype = ULONG
VC_VoiceGetFrequency.argtypes = [UBYTE]
VC_VoiceSetPanning = _libraries['/usr/lib/libmikmod.so'].VC_VoiceSetPanning
VC_VoiceSetPanning.restype = None
VC_VoiceSetPanning.argtypes = [UBYTE, ULONG]
VC_VoiceGetPanning = _libraries['/usr/lib/libmikmod.so'].VC_VoiceGetPanning
VC_VoiceGetPanning.restype = ULONG
VC_VoiceGetPanning.argtypes = [UBYTE]
VC_VoicePlay = _libraries['/usr/lib/libmikmod.so'].VC_VoicePlay
VC_VoicePlay.restype = None
VC_VoicePlay.argtypes = [UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD]
VC_VoiceStop = _libraries['/usr/lib/libmikmod.so'].VC_VoiceStop
VC_VoiceStop.restype = None
VC_VoiceStop.argtypes = [UBYTE]
VC_VoiceStopped = _libraries['/usr/lib/libmikmod.so'].VC_VoiceStopped
VC_VoiceStopped.restype = BOOL
VC_VoiceStopped.argtypes = [UBYTE]
VC_VoiceGetPosition = _libraries['/usr/lib/libmikmod.so'].VC_VoiceGetPosition
VC_VoiceGetPosition.restype = SLONG
VC_VoiceGetPosition.argtypes = [UBYTE]
VC_VoiceRealVolume = _libraries['/usr/lib/libmikmod.so'].VC_VoiceRealVolume
VC_VoiceRealVolume.restype = ULONG
VC_VoiceRealVolume.argtypes = [UBYTE]
__FILE = _IO_FILE
va_list = __gnuc_va_list
off_t = __off_t
off64_t = __off64_t
ssize_t = __ssize_t
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/lib/libmikmod.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/lib/libmikmod.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/lib/libmikmod.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/lib/libmikmod.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/lib/libmikmod.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/lib/libmikmod.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/lib/libmikmod.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/lib/libmikmod.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/lib/libmikmod.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/lib/libmikmod.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/lib/libmikmod.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/lib/libmikmod.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/lib/libmikmod.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/lib/libmikmod.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/lib/libmikmod.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/lib/libmikmod.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/lib/libmikmod.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/lib/libmikmod.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/lib/libmikmod.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/lib/libmikmod.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/lib/libmikmod.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/lib/libmikmod.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/lib/libmikmod.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/lib/libmikmod.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fscanf = _libraries['/usr/lib/libmikmod.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/lib/libmikmod.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/lib/libmikmod.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/lib/libmikmod.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['/usr/lib/libmikmod.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['/usr/lib/libmikmod.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['/usr/lib/libmikmod.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/lib/libmikmod.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/lib/libmikmod.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/lib/libmikmod.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/lib/libmikmod.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/lib/libmikmod.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
gets = _libraries['/usr/lib/libmikmod.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
__getdelim = _libraries['/usr/lib/libmikmod.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/lib/libmikmod.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/lib/libmikmod.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/lib/libmikmod.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/lib/libmikmod.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fwrite = _libraries['/usr/lib/libmikmod.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/lib/libmikmod.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/lib/libmikmod.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/lib/libmikmod.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/lib/libmikmod.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/lib/libmikmod.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/lib/libmikmod.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/lib/libmikmod.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/lib/libmikmod.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/lib/libmikmod.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/lib/libmikmod.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/lib/libmikmod.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/lib/libmikmod.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/lib/libmikmod.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/lib/libmikmod.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/lib/libmikmod.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/lib/libmikmod.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/lib/libmikmod.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/lib/libmikmod.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/lib/libmikmod.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/lib/libmikmod.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/lib/libmikmod.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/lib/libmikmod.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/lib/libmikmod.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/lib/libmikmod.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
obstack._fields_ = [
]
flockfile = _libraries['/usr/lib/libmikmod.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/lib/libmikmod.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/lib/libmikmod.so'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
__ctype_get_mb_cur_max = _libraries['/usr/lib/libmikmod.so'].__ctype_get_mb_cur_max
__ctype_get_mb_cur_max.restype = size_t
__ctype_get_mb_cur_max.argtypes = []
strtod = _libraries['/usr/lib/libmikmod.so'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['/usr/lib/libmikmod.so'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['/usr/lib/libmikmod.so'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['/usr/lib/libmikmod.so'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['/usr/lib/libmikmod.so'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['/usr/lib/libmikmod.so'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['/usr/lib/libmikmod.so'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['/usr/lib/libmikmod.so'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['/usr/lib/libmikmod.so'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
strtol_l = _libraries['/usr/lib/libmikmod.so'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['/usr/lib/libmikmod.so'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['/usr/lib/libmikmod.so'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['/usr/lib/libmikmod.so'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['/usr/lib/libmikmod.so'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['/usr/lib/libmikmod.so'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['/usr/lib/libmikmod.so'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
atoi = _libraries['/usr/lib/libmikmod.so'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['/usr/lib/libmikmod.so'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['/usr/lib/libmikmod.so'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
l64a = _libraries['/usr/lib/libmikmod.so'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['/usr/lib/libmikmod.so'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['/usr/lib/libmikmod.so'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['/usr/lib/libmikmod.so'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['/usr/lib/libmikmod.so'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['/usr/lib/libmikmod.so'].setstate
setstate.restype = STRING
setstate.argtypes = [STRING]
class random_data(Structure):
    pass
int32_t = c_int32
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
random_r = _libraries['/usr/lib/libmikmod.so'].random_r
random_r.restype = c_int
random_r.argtypes = [POINTER(random_data), POINTER(int32_t)]
srandom_r = _libraries['/usr/lib/libmikmod.so'].srandom_r
srandom_r.restype = c_int
srandom_r.argtypes = [c_uint, POINTER(random_data)]
initstate_r = _libraries['/usr/lib/libmikmod.so'].initstate_r
initstate_r.restype = c_int
initstate_r.argtypes = [c_uint, STRING, size_t, POINTER(random_data)]
setstate_r = _libraries['/usr/lib/libmikmod.so'].setstate_r
setstate_r.restype = c_int
setstate_r.argtypes = [STRING, POINTER(random_data)]
rand = _libraries['/usr/lib/libmikmod.so'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['/usr/lib/libmikmod.so'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['/usr/lib/libmikmod.so'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['/usr/lib/libmikmod.so'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['/usr/lib/libmikmod.so'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['/usr/lib/libmikmod.so'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['/usr/lib/libmikmod.so'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['/usr/lib/libmikmod.so'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['/usr/lib/libmikmod.so'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['/usr/lib/libmikmod.so'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['/usr/lib/libmikmod.so'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['/usr/lib/libmikmod.so'].lcong48
lcong48.restype = None
lcong48.argtypes = [POINTER(c_ushort)]
class drand48_data(Structure):
    pass
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
drand48_r = _libraries['/usr/lib/libmikmod.so'].drand48_r
drand48_r.restype = c_int
drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
erand48_r = _libraries['/usr/lib/libmikmod.so'].erand48_r
erand48_r.restype = c_int
erand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_double)]
lrand48_r = _libraries['/usr/lib/libmikmod.so'].lrand48_r
lrand48_r.restype = c_int
lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
nrand48_r = _libraries['/usr/lib/libmikmod.so'].nrand48_r
nrand48_r.restype = c_int
nrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
mrand48_r = _libraries['/usr/lib/libmikmod.so'].mrand48_r
mrand48_r.restype = c_int
mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
jrand48_r = _libraries['/usr/lib/libmikmod.so'].jrand48_r
jrand48_r.restype = c_int
jrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
srand48_r = _libraries['/usr/lib/libmikmod.so'].srand48_r
srand48_r.restype = c_int
srand48_r.argtypes = [c_long, POINTER(drand48_data)]
seed48_r = _libraries['/usr/lib/libmikmod.so'].seed48_r
seed48_r.restype = c_int
seed48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
lcong48_r = _libraries['/usr/lib/libmikmod.so'].lcong48_r
lcong48_r.restype = c_int
lcong48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
malloc = _libraries['/usr/lib/libmikmod.so'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['/usr/lib/libmikmod.so'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['/usr/lib/libmikmod.so'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['/usr/lib/libmikmod.so'].free
free.restype = None
free.argtypes = [c_void_p]
cfree = _libraries['/usr/lib/libmikmod.so'].cfree
cfree.restype = None
cfree.argtypes = [c_void_p]
valloc = _libraries['/usr/lib/libmikmod.so'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
posix_memalign = _libraries['/usr/lib/libmikmod.so'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]
aligned_alloc = _libraries['/usr/lib/libmikmod.so'].aligned_alloc
aligned_alloc.restype = c_void_p
aligned_alloc.argtypes = [size_t, size_t]
abort = _libraries['/usr/lib/libmikmod.so'].abort
abort.restype = None
abort.argtypes = []
on_exit = _libraries['/usr/lib/libmikmod.so'].on_exit
on_exit.restype = c_int
on_exit.argtypes = [CFUNCTYPE(None, c_int, c_void_p), c_void_p]
exit = _libraries['/usr/lib/libmikmod.so'].exit
exit.restype = None
exit.argtypes = [c_int]
quick_exit = _libraries['/usr/lib/libmikmod.so'].quick_exit
quick_exit.restype = None
quick_exit.argtypes = [c_int]
_Exit = _libraries['/usr/lib/libmikmod.so']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['/usr/lib/libmikmod.so'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
secure_getenv = _libraries['/usr/lib/libmikmod.so'].secure_getenv
secure_getenv.restype = STRING
secure_getenv.argtypes = [STRING]
putenv = _libraries['/usr/lib/libmikmod.so'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['/usr/lib/libmikmod.so'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['/usr/lib/libmikmod.so'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
clearenv = _libraries['/usr/lib/libmikmod.so'].clearenv
clearenv.restype = c_int
clearenv.argtypes = []
mktemp = _libraries['/usr/lib/libmikmod.so'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['/usr/lib/libmikmod.so'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemp64 = _libraries['/usr/lib/libmikmod.so'].mkstemp64
mkstemp64.restype = c_int
mkstemp64.argtypes = [STRING]
mkstemps = _libraries['/usr/lib/libmikmod.so'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkstemps64 = _libraries['/usr/lib/libmikmod.so'].mkstemps64
mkstemps64.restype = c_int
mkstemps64.argtypes = [STRING, c_int]
mkdtemp = _libraries['/usr/lib/libmikmod.so'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
mkostemp = _libraries['/usr/lib/libmikmod.so'].mkostemp
mkostemp.restype = c_int
mkostemp.argtypes = [STRING, c_int]
mkostemp64 = _libraries['/usr/lib/libmikmod.so'].mkostemp64
mkostemp64.restype = c_int
mkostemp64.argtypes = [STRING, c_int]
mkostemps = _libraries['/usr/lib/libmikmod.so'].mkostemps
mkostemps.restype = c_int
mkostemps.argtypes = [STRING, c_int, c_int]
mkostemps64 = _libraries['/usr/lib/libmikmod.so'].mkostemps64
mkostemps64.restype = c_int
mkostemps64.argtypes = [STRING, c_int, c_int]
system = _libraries['/usr/lib/libmikmod.so'].system
system.restype = c_int
system.argtypes = [STRING]
canonicalize_file_name = _libraries['/usr/lib/libmikmod.so'].canonicalize_file_name
canonicalize_file_name.restype = STRING
canonicalize_file_name.argtypes = [STRING]
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
qsort = _libraries['/usr/lib/libmikmod.so'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['/usr/lib/libmikmod.so'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['/usr/lib/libmikmod.so'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['/usr/lib/libmikmod.so'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['/usr/lib/libmikmod.so'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['/usr/lib/libmikmod.so'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['/usr/lib/libmikmod.so'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['/usr/lib/libmikmod.so'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['/usr/lib/libmikmod.so'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['/usr/lib/libmikmod.so'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['/usr/lib/libmikmod.so'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
qecvt = _libraries['/usr/lib/libmikmod.so'].qecvt
qecvt.restype = STRING
qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qfcvt = _libraries['/usr/lib/libmikmod.so'].qfcvt
qfcvt.restype = STRING
qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qgcvt = _libraries['/usr/lib/libmikmod.so'].qgcvt
qgcvt.restype = STRING
qgcvt.argtypes = [c_longdouble, c_int, STRING]
ecvt_r = _libraries['/usr/lib/libmikmod.so'].ecvt_r
ecvt_r.restype = c_int
ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
fcvt_r = _libraries['/usr/lib/libmikmod.so'].fcvt_r
fcvt_r.restype = c_int
fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qecvt_r = _libraries['/usr/lib/libmikmod.so'].qecvt_r
qecvt_r.restype = c_int
qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qfcvt_r = _libraries['/usr/lib/libmikmod.so'].qfcvt_r
qfcvt_r.restype = c_int
qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
mblen = _libraries['/usr/lib/libmikmod.so'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['/usr/lib/libmikmod.so'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
rpmatch = _libraries['/usr/lib/libmikmod.so'].rpmatch
rpmatch.restype = c_int
rpmatch.argtypes = [STRING]
getsubopt = _libraries['/usr/lib/libmikmod.so'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
posix_openpt = _libraries['/usr/lib/libmikmod.so'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['/usr/lib/libmikmod.so'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['/usr/lib/libmikmod.so'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['/usr/lib/libmikmod.so'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
getpt = _libraries['/usr/lib/libmikmod.so'].getpt
getpt.restype = c_int
getpt.argtypes = []
getloadavg = _libraries['/usr/lib/libmikmod.so'].getloadavg
getloadavg.restype = c_int
getloadavg.argtypes = [POINTER(c_double), c_int]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
select = _libraries['/usr/lib/libmikmod.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
pselect = _libraries['/usr/lib/libmikmod.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/lib/libmikmod.so'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/lib/libmikmod.so'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/lib/libmikmod.so'].gnu_dev_makedev
gnu_dev_makedev.restype = c_ulonglong
gnu_dev_makedev.argtypes = [c_uint, c_uint]
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
gid_t = __gid_t
mode_t = __mode_t
nlink_t = __nlink_t
uid_t = __uid_t
pid_t = __pid_t
id_t = __id_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
int8_t = c_int8
int16_t = c_int16
int64_t = c_int64
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulong
register_t = c_long
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
clock_t = __clock_t
time_t = __time_t
clockid_t = __clockid_t
timer_t = __timer_t
class __locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(__locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
__locale_data._fields_ = [
]
locale_t = __locale_t
__all__ = ['__uint16_t', '_ATFILE_SOURCE', 'EOF', '__glibc_unlikely',
           'wctomb', 'getc_unlocked', 'MMERR_OPENAL_CREATECTX',
           '_IO_USER_LOCK', 'MikMod_calloc', 'u_short',
           '__INO_T_MATCHES_INO64_T', '__off64_t', '__int16_t',
           'Sample_LoadRawFP', 'md_volume', 'MMERR_MED_SYNTHSAMPLES',
           '__WCOREFLAG', 'MMERR_OPENAL_SOURCEPLAY', 'fpos_t',
           '_G_HAVE_MREMAP', 'Voice_SetFrequency', 'fprintf',
           'N14pthread_cond_t4DOT_16E', 'ftell', 'qecvt',
           'MikMod_GetVersion', 'MMERR_AIX_CONFIG_INIT', '_G_va_list',
           '__SIZEOF_PTHREAD_CONDATTR_T', 'makedev', 'getline',
           '__FD_ISSET', '__realpath_chk', '_IO_BUFSIZ', 'rand_r',
           'MikMod_RegisterLoader', '__FILE', '_IO_off64_t',
           'MikMod_free', 'uid_t', 'erand48_r', 'Player_Mute',
           '_IO_fpos64_t', 'SEEK_HOLE', 'UF_S3MSLIDES',
           '__time_t_defined', '__time_t', '__WSTOPSIG', '__NFDBITS',
           '__ASMNAME', 'htole32', '__SIZEOF_PTHREAD_MUTEXATTR_T',
           '_POSIX_SOURCE', '_IO_FIXED', '_IO_jump_t',
           'VC_SetNumVoices', 'stderr', 'drv_wss', '__ptsname_r_chk',
           'atoi', 'MMERR_SGI_STEREO', 'ftrylockfile',
           'fputc_unlocked', 'nrand48_r', 'load_amf', '__uint64_t',
           'drv_pipe', '_DEFAULT_SOURCE', 'snprintf', '_ALLOCA_H',
           '__va_list_tag', 'MikMod_DriverByOrdinal', 'mkostemps',
           '_IO_USER_BUF', 'MMERR_SAMPLE_TOO_BIG', '__vfprintf_chk',
           'drv_mac', '__USE_POSIX199309', 'SF_FORMATMASK',
           'VC_VoiceSetPanning', 'mktemp', '__clockid_t',
           'getchar_unlocked', 'MikMod_DisableOutput', 'SFX_CRITICAL',
           'MMERR_DS_FORMAT', 'MMERR_ALSA_PCM_WRITE', 'MMERR_MAX',
           'fsid_t', '__mbstowcs_chk', '_IO_SHOWBASE', 'md_reverb',
           'id_t', 'PAN_RIGHT', 'MUTE_EXCLUSIVE', '__WEXITSTATUS',
           '_G_HAVE_MMAP', '__codecvt_partial', 'MUTE_INCLUSIVE',
           'SF_LOOP', 'MMERR_NON_BLOCK', 'drv_wav', 'be64toh',
           '__SIZEOF_PTHREAD_BARRIER_T', 'blkcnt_t',
           'MMERR_DS_UPDATE', 'SLONG', 'MikMod_RegisterErrorHandler',
           'free', 'setstate_r', 'fsetpos64', '_IO_DONT_CLOSE',
           '__locale_data', '__u_long', 'MMERR_NOT_A_STREAM', 'wait',
           '_IO_SKIPWS', 'drv_dart', 'load_med', '__WIFEXITED',
           'vsprintf', 'Voice_GetPosition', 'popen', '_IO_SCIENTIFIC',
           'pthread_t', 'strtod', 'MMERR_GUS_TIMER', 'qecvt_r',
           '__locale_struct', '__PMT', 'Voice_SetPanning',
           '_LARGEFILE_SOURCE', 'u_int8_t', 'qfcvt_r',
           'Player_LoadGeneric', 'realloc', '__mode_t', 'PAN_CENTER',
           'drv_aix', 'Sample_LoadRawMem', '__off_t', 'unlockpt',
           'fmemopen', 'MikMod_player_t', 'select', 'getchar',
           'UF_PANNING', 'drv_ultra', '__WNOTHREAD', 'u_quad_t',
           'UF_LINEAR', 'canonicalize_file_name', 'fsfilcnt64_t',
           'fputs_unlocked', '_IO_UNITBUF', 'MikMod_critical',
           '_IOS_TRUNC', 'MMERR_ALSA_PCM_START',
           'MMERR_OSX_ADD_IO_PROC', 'SF_STEREO', 'DMODE_SOFT_SNDFX',
           'minor', 'strtof_l', 'MMERR_ITPACK_INVALID_DATA',
           'ftello64', '__USE_FORTIFY_LEVEL', '__int8_t',
           'Voice_RealVolume', '__fsblkcnt64_t', 'strtold',
           'drv_sam9407', '__uflow', 'BIG_ENDIAN', 'PAN_LEFT',
           'pthread_barrierattr_t', 'Voice_Play', '__WTERMSIG',
           '__USE_XOPEN_EXTENDED', 'fopencookie', 'fopen64',
           'timer_t', 'drv_ds', 'VC_VoiceStop', '__fsfilcnt64_t',
           '_IO_pid_t', '_IO_FILE', 'pthread_key_t',
           'MMERR_WINMM_HANDLE', 'mkdtemp', '_IO_BOOLALPHA',
           '__io_read_fn', '__WALL', 'PAN_HALFLEFT',
           'MMERR_SGI_SPEED', 'off_t', '__fsblkcnt_t', 'abort',
           'FD_ZERO', 'MMERR_OSX_PTHREAD', 'strtoll',
           '__STDC_CONSTANT_MACROS', 'feof', 'SF_SIGNED',
           'sys_errlist', '__WIFCONTINUED', 'clearerr',
           '__wcstombs_chk', 'lcong48', 'lrand48', 'VC_Exit',
           'MikMod_strerror', '__WORDSIZE', 'u_char', 'rewind',
           'on_exit', 'MikMod_errno', 'putc_unlocked', 'CHAR',
           'flockfile', 'WEXITED', '_XOPEN_SOURCE',
           '_IO_free_backup_area', 'unsetenv', 'MMERR_STEREO_ONLY',
           'SF_16BITS', 'VC_WriteBytes', 'srand48_r', 'key_t',
           '__USE_ISOC95', 'UF_INST', 'uint', 'MMERR_OPENING_AUDIO',
           'valloc', '__GLIBC__', 'pthread_rwlockattr_t', 'ENVPT',
           '__USE_ISOC99', 'load_669', 'funlockfile', '_IO_fpos_t',
           'md_mixfreq', 'stdin', 'getloadavg', '__u_int',
           '__sprintf_chk', 'SF_REVERSE', 'load_gdm',
           'N16pthread_rwlock_t4DOT_19E', 'ssize_t', '_XLOCALE_H',
           '__fsfilcnt_t', 'le32toh', 'vscanf', 'rand',
           'MMERR_OPENAL_BUFFERDATA', 'strtouq', 'drv_pulseaudio',
           '__glibc_likely', 'MikMod_Exit', '__LONG_LONG_PAIR',
           '__WCOREDUMP', 'MMERR_LOADING_SAMPLEINFO',
           'MMERR_HP_SETSAMPLESIZE', '_IONBF', 'FILE',
           'pthread_mutexattr_t', 'size_t', '__USE_XOPEN',
           'md_sndfxvolume', 'Sample_Load', 'DMODE_REVERSE',
           'drv_oss', 'strtol_l', 'open_memstream', '__USE_POSIX2',
           'fwrite', '_IO_ftrylockfile', '_IO_marker',
           'MMERR_HP_BUFFERSIZE', 'MMERR_OPENAL_CTXCURRENT', 'gid_t',
           '__wctomb_chk', 'mkostemps64', 'DMODE_STEREO',
           'feof_unlocked', '__qaddr_t', '__GLIBC_PREREQ',
           'DMODE_SIMDMIXER', 'PAN_SURROUND', '__W_EXITCODE',
           '_IO_RIGHT', '_IOS_APPEND', 'MMERR_ULAW', 'PAN_HALFRIGHT',
           'LITTLE_ENDIAN', 'SAMPLE', 'sprintf',
           'MMERR_OSX_DEVICE_START', 'MikMod_callback_t',
           '__asprintf_chk', 'Player_QueryVoices', 'SWORD',
           '__USE_ATFILE', 'load_ult', 'u_int16_t', 'TMP_MAX',
           'drv_hp', '_G_BUFSIZ', '__vprintf_chk', 'MikMod_Lock',
           'MMERR_OSS_SETSAMPLESIZE', 'MMERR_OS2_TIMER', 'gcvt',
           'getdelim', 'MREADER', 'useconds_t', '__int32_t',
           'SAMPLOAD', '__USE_POSIX', '_IO_NO_WRITES', '__locale_t',
           'load_mtm', 'MMERR_NOT_A_MODULE', 'VC_VoiceGetFrequency',
           'Player_Paused', 'vsscanf', 'md_mode', 'DMODE_HQMIXER',
           'VC_VoiceSetVolume', '__fsword_t', '__fd_mask',
           '__FILE_defined', 'load_mod', 'fileno_unlocked',
           'N4wait3DOT_7E', 'clock_t', 'VOICEINFO', '_IO_NO_READS',
           'WIFSIGNALED', 'initstate_r', '__useconds_t',
           'MMERR_WINMM_DEVICEID', 'vasprintf', '__GLIBC_MINOR__',
           '_IO_CURRENTLY_PUTTING', 'MMERR_OUT_OF_HANDLES',
           'MMERR_DS_BUFFER', '__clockid_t_defined', '__BYTE_ORDER',
           '_IO_funlockfile', '__SIZEOF_PTHREAD_ATTR_T', 'drv_win',
           'MMERR_MAC_SPEED', '_IO_vfprintf', '__fgets_chk',
           'pthread_barrier_t', '__ldiv_t_defined', 'u_int32_t',
           'pthread_rwlock_t', 'fileno', 'asprintf',
           '__pthread_internal_list', '__WORDSIZE_TIME64_COMPAT32',
           '_IO_cookie_io_functions_t', 'load_far', 'labs',
           '_SYS_TYPES_H', '__gnuc_va_list', '__P', 'qsort_r',
           '_IO_ERR_SEEN', 'div', 'fseeko', 'putchar', 'VC_PlayStart',
           'MMERR_HP_AUDIO_OUTPUT', '__USE_GNU', 'WUNTRACED',
           'VC_VoiceRealVolume', 'htobe16',
           'MMERR_OPENAL_QUEUEBUFFERS', '__pthread_list_t',
           'pthread_attr_t', 'tmpfile', '__attribute_format_arg__',
           'LIBMIKMOD_VERSION_MINOR', '__rlim64_t', 'ino_t',
           '_G_IO_IO_FILE_VERSION', '_POSIX_C_SOURCE', 'major',
           '_IO_ssize_t', 'qsort', 'Sample_LoadRaw', 'mbtowc',
           'load_stx', '__W_STOPCODE', 'UF_BGSLIDES', 'calloc',
           '__blksize_t', 'MikMod_Reset', '__USE_SVID',
           'pthread_spinlock_t', '_IO_seekoff', 'UBYTE', 'load_stm',
           'getpt', '_IO_IS_APPENDING', 'SF_UST_LOOP', 'drv_osx',
           'ecvt', 'VC_SampleSpace', '_sys_nerr', 'scanf',
           '__W_CONTINUED', 'system', 'fclose', '__bswap_constant_32',
           'MMERR_DS_THREAD', 'ino64_t', 'le16toh', 'Voice_SetVolume',
           '__asprintf', 'L_ctermid', 'mkstemp64', 'ecvt_r',
           '__mbstate_t', 'Player_LoadTitleMem', '__uint8_t',
           'setbuffer', '_IO_INTERNAL', '__SIZEOF_PTHREAD_RWLOCK_T',
           'MMERR_ALSA_BUFFERSIZE', 'MMERR_MAC_START', '__caddr_t',
           '__obstack_printf_chk', '__blkcnt64_t', 'mkostemp',
           'drv_alsa', 'MMERR_DS_NOTIFY', '_IOS_NOCREATE', '_Exit',
           'dprintf', '__vdprintf_chk', '_IO_TIED_PUT_GET', 'div_t',
           'MD_SOFTWARE', 'MMERR_OPENAL_SOURCE', 'MikMod_strdup',
           'quad_t', '__USE_LARGEFILE', '__USE_EXTERN_INLINES',
           '__SIZEOF_PTHREAD_COND_T', 'va_list', '_IO_BE',
           '_FEATURES_H', 'MikMod_Init', 'wcstombs', 'SEEK_DATA',
           'drand48_r', 'UF_NOWRAP', '__REDIRECT_NTH_LDBL',
           'MD_MUSIC', 'pthread_cond_t', 'Player_Active',
           '_BITS_TYPES_H', 'MMERR_AIX_CONFIG_CONTROL', 'PDP_ENDIAN',
           '__ctype_get_mb_cur_max', 'Player_PrevPosition', 'vprintf',
           '__fread_chk', '__rlim_t', '__FLOAT_WORD_ORDER',
           'md_driver', 'MWRITER', 'setstate', 'nlink_t',
           'secure_getenv', 'MMERR_SGI_8BIT', 'Player_GetOrder',
           '_XOPEN_SOURCE_EXTENDED', 'pthread_mutex_t', '__warnattr',
           'WNOWAIT', '__int64_t', '_IO_UNBUFFERED', '__u_char',
           'realpath', 'Player_LoadMem', 'ulong',
           'MMERR_OSX_SET_STEREO', '_IOS_ATEND', 'UF_MAXCHAN',
           'Player_GetChannelVoice', '__clock_t', 'int8_t',
           'SF_ITPACKED', '__WIFSTOPPED', 'UF_ARPMEM',
           'MMERR_OUT_OF_MEMORY', 'perror', 'Sample_LoadGeneric',
           'Player_GetChannelPeriod', 'MikMod_SetNumVoices',
           'srand48', 'fsblkcnt_t', 'MMERR_OS2_MIXSETUP',
           'SF_BIG_ENDIAN', '__quad_t', 'VC_SetCallback',
           '_BSD_SOURCE', 'fseeko64', '__obstack_vprintf_chk',
           '__uid_t', 'setlinebuf', '__FD_ZERO_STOS', 'setvbuf',
           'vfprintf', 'WTERMSIG', '__pthread_mutex_s',
           'obstack_vprintf', 'Voice_GetFrequency', 'load_okt',
           '__printf_chk', 'a64l', 'random', '_IO_putc',
           'MMERR_ALSA_SETFORMAT', '__GNU_LIBRARY__',
           '_BITS_TYPESIZES_H', 'putchar_unlocked', 'mode_t',
           'strtoull', '__STDLIB_MB_LEN_MAX', '__USE_LARGEFILE64',
           'MMERR_OSX_UNSUPPORTED_FORMAT', 'md_pansep', 'strtol',
           'fputc', '__underflow', 'VC_VoiceGetPosition', 'htobe64',
           'MikMod_InitThreads', '_IO_2_1_stdin_', 'Player_SetSpeed',
           'strtof', 'fgetpos64', 'mkstemps', 'fputs', '_IO_LINE_BUF',
           'lrand48_r', 'MikMod_InfoLoader', 'INSTNOTES',
           'cookie_seek_function_t', 'Player_Unmute',
           'Voice_GetPanning', 'strtoq', 'MikMod_DriverFromAlias',
           '__loff_t', 'Player_Free', 'SF_PLAYBACKMASK', 'l64a',
           'FD_CLR', '_G_config_h', '____mbstate_t_defined',
           'MLOADER', 'load_s3m', 'MODULE', '_IO_LEFT',
           '_IO_FLAGS2_MMAP', 'ptsname_r', 'VC_SampleUnload',
           '__lldiv_t_defined', 'strtod_l',
           'MMERR_INITIALIZING_MIXER', '__WCLONE',
           'MMERR_OSX_BAD_PROPERTY', 'load_asy', 'FOPEN_MAX',
           'srandom', '_IO_DELETE_DONT_CLOSE', 'fscanf', 'remove',
           '_G_fpos_t', '__attribute_format_strfmon__', 'fd_mask',
           'SF_EXTRAPLAYBACKMASK', 'SF_DELTA', 'Sample_LoadMem',
           '__bos', 'cookie_close_function_t', 'be32toh', '_STDLIB_H',
           'strtoul', '__ssize_t', 'comparison_fn_t',
           'cookie_write_function_t', 'ferror_unlocked', 'qgcvt',
           '__fprintf_chk', 'quick_exit', 'int16_t', 'drv_os2',
           'drv_stdout', 'jrand48', 'MMERR_WINMM_ALLOCATED',
           'VC_VoiceStopped', 'MikMod_InfoDriver', '__sigset_t',
           'random_data', '_sys_errlist', 'fgetpos', 'strtoll_l',
           'MMERR_DOSWSS_STARTDMA', 'posix_memalign', '_IO_padn',
           'WIFCONTINUED', 'Player_SetPosition', 'ldiv_t', 'vdprintf',
           'LIBMIKMOD_VERSION_MAJOR', '__getdelim', 'fflush',
           'Player_SetTempo', '__overflow', '__USE_XOPEN2K',
           '__FD_SETSIZE', 'Player_GetRow', 'htole16', 'md_device',
           'DMODE_INTERP', 'load_it', '__intptr_t', 'Voice_GetVolume',
           'seed48_r', '_IO_LINKED', '__timespec_defined',
           'vsnprintf', 'MMERR_ALSA_SETCHANNELS', 'lcong48_r',
           '_IO_va_list', '__blkcnt_t', 'MDRIVER', '_IO_size_t',
           'drv_xaudio2', 'fd_set', 'caddr_t', 'MMERR_SGI_16BIT',
           'blkcnt64_t', 'VC_VoicePlay', 'timespec',
           '__vsnprintf_chk', '__SIZEOF_PTHREAD_BARRIERATTR_T',
           '_IO_flockfile', 'MMERR_UNKNOWN_WAVE_TYPE',
           'LIBMIKMOD_VERSION', '_IOS_INPUT', 'MMERR_HP_SETSPEED',
           'L_tmpnam', 'off64_t', '__PTHREAD_RWLOCK_INT_FLAGS_SHARED',
           'ptsname', '_IOS_BIN', 'alloca', '_IO_peekc_locked',
           'tmpfile64', 'MikMod_handler', 'sys_nerr', '_IO_BAD_SEEN',
           '__USE_MISC', '__BIT_TYPES_DEFINED__', 'putw', 'htole64',
           'getsubopt', 'puts', '__syscall_slong_t',
           '__compar_d_fn_t', 'VC_VoiceSetFrequency', 'obstack',
           'aligned_alloc', 'N11__mbstate_t3DOT_2E',
           'MMERR_GUS_SETTINGS', 'drv_AF', 'MMERR_OSS_SETSTEREO',
           'gnu_dev_major', 'tmpnam_r', 'putc', '_IO_2_1_stderr_',
           '__PTHREAD_MUTEX_HAVE_ELISION', 'DMODE_SOFT_MUSIC',
           '_IO_HEX', 'MMERR_OPENAL_SOURCESTOP', 'fread',
           'N4wait3DOT_6E', '__PTHREAD_MUTEX_HAVE_PREV', 'tmpnam',
           '__OFF_T_MATCHES_OFF64_T', 'WSTOPSIG',
           'MMERR_OSX_UNKNOWN_DEVICE', 'WNOHANG', 'fpos64_t',
           '__dev_t', 'Voice_Stop', 'MMERR_GUS_RESET', 'pselect',
           'FILENAME_MAX', 'L_cuserid', '_SYS_SYSMACROS_H',
           'MMERR_AF_AUDIO_PORT', 'drand48', 'EXIT_SUCCESS',
           '__suseconds_t', '__dprintf_chk', 'u_long', 'drv_sgi',
           'random_r', 'Player_SetVolume', 'qfcvt', 'initstate',
           'MMERR_LOADING_PATTERN', 'rename', 'malloc', 'ushort',
           '__USE_POSIX199506', 'stdout', 'Player_LoadTitleFP',
           '__BIG_ENDIAN', 'srand', 'fwrite_unlocked', 'SF_BIDI',
           '_IO_uid_t', 'MikMod_EnableOutput',
           'MMERR_DYNAMIC_LINKING', 'atoll', 'Voice_Stopped',
           'time_t', 'DMODE_NOISEREDUCTION', 'drand48_data',
           'blksize_t', 'clockid_t', 'Player_LoadTitle', 'getc',
           'Player_ToggleMute', 'MMERR_DS_PRIORITY', 'drv_esd',
           'UF_NNA', 'VC_SampleLength', '__USE_XOPEN2K8XSI',
           'MMERR_ALSA_PCM_RECOVER', 'fsblkcnt64_t', '_IO_ferror',
           'MMERR_WINMM_FORMAT', 'gets', 'Sample_Free',
           '_SYS_CDEFS_H', 'fsfilcnt_t', 'getw', '_OLD_STDIO_MAGIC',
           'Player_NextPosition', 'grantpt', 'SF_OWNPAN',
           '__snprintf_chk', '_IO_IS_FILEBUF', 'SEEK_SET',
           '__io_write_fn', 'drv_sun', '_IOS_OUTPUT', 'drv_openal',
           '__ino_t', '__vsprintf_chk', 'MMERR_OSS_SETFRAGMENT',
           '_IO_lock_t', 'setbuf', '_IO_2_1_stdout_',
           '__REDIRECT_LDBL', 'srandom_r', 'md_musicvolume',
           'load_xm', 'WCONTINUED', 'MMERR_8BIT_ONLY', 'ENVPOINTS',
           'load_gt2', 'INSTRUMENT', 'MMERR_DS_EVENT',
           '_IO_FLAGS2_NOTCANCEL', 'MMERR_HP_CHANNELS',
           'VC_SampleLoad', 'load_uni', 'MikMod_Update',
           'suseconds_t', 'be16toh', 'WSTOPPED', 'fseek', 'SBYTE',
           '__USE_XOPEN2KXSI', 'SF_SUSTAIN', '__LITTLE_ENDIAN',
           '__have_pthread_attr_t', 'MikMod_RegisterDriver',
           'mkstemps64', 'pthread_condattr_t',
           'MMERR_AIX_CONFIG_START', 'pthread_once_t', 'drv_aiff',
           '__fsid_t', 'u_int64_t', 'VC_SilenceBytes', 'load_m15',
           'timeval', 'MMERR_LOADING_TRACK', '__uint32_t',
           '__USE_XOPEN2K8', '_STRUCT_TIMEVAL', '__compar_fn_t',
           'DMODE_FLOAT', 'ldiv', 'load_umx', 'Player_GetModule',
           'RAND_MAX', 'setenv', 'P_tmpdir', '__ino64_t',
           '__u_quad_t', 'Player_Muted', 'int32_t', 'loff_t',
           'drv_sb', 'UF_HIGHBPM', 'MMERR_OS2_SEMAPHORE',
           '_IO_SHOWPOINT', '_IO_sgetn', '_BITS_PTHREADTYPES_H',
           '__fread_unlocked_chk', 'WIFSTOPPED', 'MMERR_16BIT_ONLY',
           'nrand48', 'VC_VoiceGetPanning', 'register_t',
           'gnu_dev_minor', '_SYS_SELECT_H', 'renameat', '_IO_DEC',
           '__fgets_unlocked_chk', '_G_fpos64_t',
           'MMERR_WINMM_UNKNOWN', '_ISOC95_SOURCE', 'drv_raw',
           '_ISOC99_SOURCE', 'freopen', '__nlink_t', 'MD_HARDWARE',
           'fread_unlocked', 'drv_sdl', 'tempnam',
           'MikMod_RegisterAllDrivers', '__syscall_ulong_t', 'lldiv',
           'rpmatch', '__io_close_fn', 'fgetc', 'load_dsm', 'pclose',
           'printf', '__fdelt_warn', 'llabs', 'abs', 'seed48',
           '__clock_t_defined', '__pid_t', 'DMODE_16BITS',
           '_IO_SHOWPOS', '__codecvt_ok', 'fgets', '_IO_MAGIC',
           'mblen', 'ctermid', '__id_t', 'cookie_io_functions_t',
           '_IO_feof', 'MMERR_OPENAL_GENSOURCES',
           'MMERR_OPENAL_GETSOURCE', 'ULONG', 'fgetc_unlocked',
           '_IO_UPPERCASE', '__timer_t', 'fsetpos', '_IO_EOF_SEEN',
           '__timer_t_defined', 'exit', 'Sample_LoadRawGeneric',
           'VC_PlayStop', 'VC_VoiceGetVolume', 'mbstowcs',
           'MMERR_OPENING_FILE', 'MikMod_Unlock',
           'MMERR_ALSA_NOCONFIG', '_SVID_SOURCE', 'FD_ISSET',
           'LIBMIKMOD_REVISION', 'MikMod_malloc',
           'MMERR_INVALID_DEVICE', '__codecvt_result',
           '__vasprintf_chk', 'fcloseall', 'MMERR_OSX_BUFFER_ALLOC',
           'MikMod_handler_t', '_IOFBF', 'drv_nas', 'MikMod_Active',
           'cfree', 'UWORD', 'UF_FT2QUIRKS', 'SEEK_END', '_IO_peekc',
           'MP_VOICE', '__USE_BSD', 'MMERR_OS2_THREAD',
           'fflush_unlocked', 'MMERR_OPENAL_GENBUFFERS', '__CONCAT',
           'bsearch', 'clearerr_unlocked', 'load_imf',
           '_IO_IN_BACKUP', '_IOS_NOREPLACE', 'fcvt',
           '_SIGSET_H_types', '_ISOC11_SOURCE', 'obstack_printf',
           '____FILE_defined', 'WIFEXITED', '__fdelt_chk',
           'Sample_Play', 'Player_TogglePause', 'SEEK_CUR',
           'mkostemp64', '_IO_off_t', '__SIZEOF_PTHREAD_MUTEX_T',
           '__USE_UNIX98', '_IO_STDIO', 'fgets_unlocked',
           'MikMod_RegisterAllLoaders', '__gid_t', '_IO_FILE_plus',
           'MMERR_OPENAL_UNQUEUEBUFFERS', 'putenv', 'fdopen',
           'MD_SNDFX', '_IO_OCT', 'MMERR_OSS_SETSPEED', '__daddr_t',
           '_IO_cookie_file', 'Player_Stop', '__sig_atomic_t',
           'MP_CONTROL', 'sigset_t', 'mrand48_r', 'mrand48',
           'MMERR_HP_AUDIO_DESC', '__io_seek_fn', 'u_int', 'getenv',
           'htobe32', 'MMERR_SUN_INIT', 'BUFSIZ', 'atol', 'VC_Init',
           'atof', 'strtoull_l', 'freopen64', 'erand48', '_IO_getc',
           '_IO_UNIFIED_JUMPTABLES', 'MMERR_SGI_MONO', 'fopen',
           'cuserid', 'MMERR_LOADING_HEADER', 'BOOL', '_ENDIAN_H',
           '_IO_vfscanf', 'cookie_read_function_t', 'ungetc',
           'MMERR_ALSA_SETRATE', 'Player_LoadFP',
           'Player_LoadTitleGeneric', 'drv_nos', 'daddr_t', 'sscanf',
           'FD_SET', '_STDIO_H', 'ftello', 'jrand48_r',
           '_IO_FLAGS2_USER_WBUF', '__STRING', 'int64_t',
           '_IO_seekpos', 'WEXITSTATUS', 'le64toh', '__GNUC_PREREQ',
           'BYTE_ORDER', 'MikMod_RegisterPlayer', 'posix_openpt',
           'UF_XMPERIODS', 'lldiv_t', 'MMERR_NO_FLOAT32',
           'gnu_dev_makedev', 'strtold_l', '_IO_MAGIC_MASK',
           '__SIZEOF_PTHREAD_RWLOCKATTR_T', '__PDP_ENDIAN',
           '__u_short', 'Sample_LoadFP', 'DMODE_SURROUND', 'clearenv',
           'mkstemp', 'vfscanf', '__key_t', 'Player_Load',
           '_LARGEFILE64_SOURCE', '__va_arg_pack', 'FD_SETSIZE',
           'ferror', '_BITS_BYTESWAP_H', '__codecvt_error',
           'MMERR_DETECTING_DEVICE', 'MMERR_ALSA_SETPARAMS',
           '_SIGSET_NWORDS', '__va_arg_pack_len', 'dev_t', '__bos0',
           'MikMod_realloc', '__SYSCALL_WORDSIZE', 'strtoul_l',
           'locale_t', 'Player_Start', '__socklen_t', '__USE_ISOC11',
           'EXIT_FAILURE', 'fcvt_r', 'pid_t', 'drv_gp32',
           '__codecvt_noconv', '_IOLBF', 'MMERR_DOSSB_STARTDMA',
           'NFDBITS']
