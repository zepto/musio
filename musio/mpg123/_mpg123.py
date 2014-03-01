from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/usr/lib/libmpg123.so'] = CDLL('/usr/lib/libmpg123.so')
WSTRING = c_wchar_p


MPG123_FORCE_MONO = 7
MPG123_PICTURE = 65536
MPG123_INT_OVERFLOW = 43
MPG123_LFS_OVERFLOW = 42
# def __WIFSIGNALED(status): return (((signed char) (((status) & 0x7f) + 1) >> 1) > 0) # macro
MPG123_BAD_CUSTOM_IO = 41
MPG123_LSEEK_FAILED = 40
MPG123_BAD_VALUE = 39
MPG123_NULL_BUFFER = 31
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
MPG123_MISSING_FEATURE = 38
MPG123_BAD_DECODER_SETUP = 37
MPG123_FEATURE_OUTPUT_32BIT = 3
MPG123_INDEX_FAIL = 36
MPG123_BAD_KEY = 34
MPG123_CBR = 0
MPG123_ENC_UNSIGNED_8 = 1
MPG123_NO_8BIT = 29
MPG123_RESYNC_FAIL = 28
MPG123_BAD_INDEX_PAR = 26
MPG123_BAD_PARS = 25
MPG123_M_STEREO = 0
MPG123_NO_READER = 24
def minor(dev): return gnu_dev_minor (dev) # macro
def WIFCONTINUED(status): return __WIFCONTINUED (__WAIT_INT (status)) # macro
def WEXITSTATUS(status): return __WEXITSTATUS (__WAIT_INT (status)) # macro
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp) # macro
def FD_SET(fd,fdsetp): return __FD_SET (fd, fdsetp) # macro
def __bswap_constant_32(x): return ((((x) & 0xff000000) >> 24) | (((x) & 0x00ff0000) >> 8) | (((x) & 0x0000ff00) << 8) | (((x) & 0x000000ff) << 24)) # macro
MPG123_NO_SEEK_FROM_END = 19
# __MODE_T_TYPE = __U32_TYPE # alias
def FD_ISSET(fd,fdsetp): return __FD_ISSET (fd, fdsetp) # macro
MPG123_ERR_NULL = 17
MPG123_NO_SPACE = 14
MPG123_BAD_RVA = 12
MPG123_NO_BUFFERS = 11
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
__BYTE_ORDER = __LITTLE_ENDIAN # alias
# def __FD_CLR(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] &= ~__FD_MASK (d))) # macro
# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MPG123_RVA_MIX = 1
# __ID_T_TYPE = __U32_TYPE # alias
MPG123_RVA_OFF = 0
MPG123_ERR_READER = 18
MPG123_BAD_RATE = 3
MPG123_NULL_POINTER = 33
def WTERMSIG(status): return __WTERMSIG (__WAIT_INT (status)) # macro
def __WCOREDUMP(status): return ((status) & __WCOREFLAG) # macro
MPG123_ERR = -1
def WIFSIGNALED(status): return __WIFSIGNALED (__WAIT_INT (status)) # macro
MPG123_NEW_FORMAT = -11
MPG123_FEATURE_DECODE_NTOM = 11
# def __WAIT_INT(status): return (*(int *) &(status)) # macro
MPG123_M_DUAL = 2
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def __LONG_LONG_PAIR(HI,LO): return LO, HI # macro
# __SLONG32_TYPE = int # alias
MPG123_NO_INDEX = 35
MPG123_FEATURE_DECODE_DOWNSAMPLE = 10
def be16toh(x): return __bswap_16 (x) # macro
mpg123_id3_enc_max = 3
mpg123_id3_utf8 = 3
mpg123_id3_latin1 = 0
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __S32_TYPE = int # alias
mpg123_id3_utf16be = 2
def __PMT(args): return args # macro
MPG123_ORIGINAL = 8
mpg123_id3_utf16bom = 1
def __P(args): return args # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
def major(dev): return gnu_dev_major (dev) # macro
mpg123_id3_pic_composer = 11
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
LITTLE_ENDIAN = __LITTLE_ENDIAN # alias
MPG123_COPYRIGHT = 2
MPG123_PRIVATE = 4
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
MPG123_BAD_HANDLE = 10
MPG123_FEATURE_DECODE_LAYER3 = 8
MPG123_ABR = 2
MPG123_FEATURE_TIMEOUT_READ = 13
MPG123_FEATURE_OUTPUT_8BIT = 1
MPG123_FEATURE_ABI_UTF8OPEN = 0
MPG123_FEATURE_OUTPUT_16BIT = 2
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
MPG123_BAD_DECODER = 9
MPG123_FEATURE_DECODE_LAYER2 = 7
mpg123_id3_pic_publisher_logo = 20
# __KEY_T_TYPE = __S32_TYPE # alias
MPG123_M_JOINT = 1
MPG123_NO_TIMEOUT = 21
mpg123_id3_pic_illustration = 18
mpg123_id3_pic_fish = 17
mpg123_id3_pic_video = 16
mpg123_id3_pic_performance = 15
mpg123_id3_pic_recording = 14
mpg123_id3_pic_location = 13
# def __FD_MASK(d): return ((__fd_mask) 1 << ((d) % __NFDBITS)) # macro
mpg123_id3_pic_lyricist = 12
__NFDBITS = 64 # Variable c_int '64'
NFDBITS = __NFDBITS # alias
mpg123_id3_pic_orchestra = 10
mpg123_id3_pic_conductor = 9
BYTE_ORDER = __BYTE_ORDER # alias
mpg123_text_icy = 3
mpg123_id3_pic_lead = 7
mpg123_id3_pic_media = 6
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
mpg123_id3_pic_other = 0
mpg123_id3_pic_leaflet = 5
mpg123_id3_pic_back_cover = 4
MPG123_FEATURE_PARSE_ICY = 12
mpg123_id3_pic_front_cover = 3
mpg123_id3_pic_other_icon = 2
mpg123_id3_pic_icon = 1
MPG123_CRC = 1
# __wur = __attribute_warn_unused_result__ # alias
# __USECONDS_T_TYPE = __U32_TYPE # alias
# __UID_T_TYPE = __U32_TYPE # alias
MPG123_NOT_INITIALIZED = 8
def makedev(maj,min): return gnu_dev_makedev (maj, min) # macro
MPG123_NO_GAPLESS = 13
def le32toh(x): return (x) # macro
def FD_CLR(fd,fdsetp): return __FD_CLR (fd, fdsetp) # macro
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
def htole64(x): return (x) # macro
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def htobe64(x): return __bswap_64 (x) # macro
def htobe32(x): return __bswap_32 (x) # macro
def htobe16(x): return __bswap_16 (x) # macro
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MPG123_AUTO_RESAMPLE = 32768
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
MPG123_SKIP_ID3V2 = 8192
MPG123_IGNORE_STREAMLENGTH = 4096
MPG123_PLAIN_ID3TEXT = 2048
MPG123_FORCE_FLOAT = 1024
MPG123_FUZZY = 512
MPG123_SEEKBUFFER = 256
# __INO64_T_TYPE = __UQUAD_TYPE # alias
# def __u_intN_t(N,MODE): return typedef unsigned int u_int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
MPG123_ENC_ANY = 30719
MPG123_QUIET = 32
MPG123_FORCE_8BIT = 16
MPG123_FORCE_STEREO = 8
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
MPG123_MONO_RIGHT = 2
MPG123_MONO_LEFT = 1
MPG123_OUT_OF_MEM = 7
# def __bswap_constant_16(x): return ((unsigned short int) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8))) # macro
MPG123_FEATURE_PARSE_ID3V2 = 5
mpg123_text_utf16be = 7
# def __bswap_16(x): return (__extension__ ({ unsigned short int __v, __x = (unsigned short int) (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_16 (__x); else __asm__ ("rorw $8, %w0" : "=r" (__v) : "0" (__x) : "cc"); __v; })) # macro
__FLOAT_WORD_ORDER = __BYTE_ORDER # alias
# __DEV_T_TYPE = __UQUAD_TYPE # alias
MPG123_FRANKENSTEIN = 3
# __DADDR_T_TYPE = __S32_TYPE # alias
MPG123_2_5 = 2
mpg123_id3_pic_artist = 8
MPG123_2_0 = 1
MPG123_FEEDPOOL = 17
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
MPG123_M_MONO = 3
def __W_STOPCODE(sig): return ((sig) << 8 | 0x7f) # macro
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MPG123_BAD_ALIGN = 30
MPG123_PREFRAMES = 16
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
__PDP_ENDIAN = 3412 # Variable c_int '3412'
PDP_ENDIAN = __PDP_ENDIAN # alias
MPG123_RVA_MAX = 2
def __WIFSTOPPED(status): return (((status) & 0xff) == 0x7f) # macro
def __WIFEXITED(status): return (__WTERMSIG(status) == 0) # macro
MPG123_ENC_8 = 15
def __WIFCONTINUED(status): return ((status) == __W_CONTINUED) # macro
# def __FD_ELT(d): return __extension__ ({ long int __d = (d); (__builtin_constant_p (__d) ? (0 <= __d && __d < __FD_SETSIZE ? (__d / __NFDBITS) : __fdelt_warn (__d)) : __fdelt_chk (__d)); }) # macro
MPG123_ENC_FLOAT_64 = 1024
def le16toh(x): return (x) # macro
__FD_SETSIZE = 1024 # Variable c_int '1024'
FD_SETSIZE = __FD_SETSIZE # alias
MPG123_RVA_ALBUM = 2
def __STRING(x): return #x # macro
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
MPG123_NO_SEEK = 23
MPG123_RIGHT = 2
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
def __WEXITSTATUS(status): return (((status) & 0xff00) >> 8) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
# def __FDS_BITS(set): return ((set)->fds_bits) # macro
MPG123_TIMEOUT = 12
MPG123_LEFT = 1
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
MPG123_BAD_PARAM = 5
mpg123_text_unknown = 0
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
MPG123_ENC_SIGNED_24 = 20608
MPG123_NO_RELSEEK = 32
def __FD_ISSET(d,set): return ((__FDS_BITS (set)[__FD_ELT (d)] & __FD_MASK (d)) != 0) # macro
mpg123_text_utf8 = 1
MPG123_ENC_UNSIGNED_32 = 8448
def le64toh(x): return (x) # macro
MPG123_ENC_SIGNED_32 = 4480
def alloca(size): return __builtin_alloca (size) # macro
MPG123_OUT_OF_SYNC = 27
MPG123_BAD_FILE = 22
# __PID_T_TYPE = __S32_TYPE # alias
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
MPG123_ENC_FLOAT_32 = 512
MPG123_GAPLESS = 64
MPG123_ENC_UNSIGNED_24 = 24576
MPG123_ENC_ALAW_8 = 8
def be64toh(x): return __bswap_64 (x) # macro
__BIG_ENDIAN = 4321 # Variable c_int '4321'
BIG_ENDIAN = __BIG_ENDIAN # alias
MPG123_ENC_SIGNED_8 = 130
MPG123_OK = 0
MPG123_ENC_SIGNED_16 = 208
def be32toh(x): return __bswap_32 (x) # macro
MPG123_ENC_FLOAT = 3584
MPG123_ENC_32 = 256
MPG123_ENC_24 = 16384
def WIFSTOPPED(status): return __WIFSTOPPED (__WAIT_INT (status)) # macro
MPG123_ENC_16 = 64
MPG123_IGNORE_INFOFRAME = 16384
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MPG123_ENC_UNSIGNED_16 = 96
MPG123_ERR_16TO8TABLE = 4
MPG123_LR = 3
# def __LDBL_REDIR(name,proto): return name proto # macro
MPG123_DONE = -12
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
MPG123_ENC_SIGNED = 128
mpg123_text_latin1 = 2
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MPG123_BAD_BUFFER = 6
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
MPG123_BAD_WHENCE = 20
MPG123_NO_RESYNC = 128
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
def WIFEXITED(status): return __WIFEXITED (__WAIT_INT (status)) # macro
# __GID_T_TYPE = __U32_TYPE # alias
def WSTOPSIG(status): return __WSTOPSIG (__WAIT_INT (status)) # macro
# def __intN_t(N,MODE): return typedef int int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
MPG123_BAD_CHANNEL = 2
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def __W_EXITCODE(ret,sig): return ((ret) << 8 | (sig)) # macro
MPG123_BUFFERFILL = 2
def htole32(x): return (x) # macro
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
# def __bswap_constant_64(x): return (__extension__ ((((x) & 0xff00000000000000ull) >> 56) | (((x) & 0x00ff000000000000ull) >> 40) | (((x) & 0x0000ff0000000000ull) >> 24) | (((x) & 0x000000ff00000000ull) >> 8) | (((x) & 0x00000000ff000000ull) << 8) | (((x) & 0x0000000000ff0000ull) << 24) | (((x) & 0x000000000000ff00ull) << 40) | (((x) & 0x00000000000000ffull) << 56))) # macro
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MPG123_FEATURE_DECODE_ACCURATE = 9
MPG123_MONO = 1
MPG123_VBR = 1
MPG123_BAD_OUTFORMAT = 1
# def __FD_ZERO(fdsp): return do { int __d0, __d1; __asm__ __volatile__ ("cld; rep; " __FD_ZERO_STOS : "=c" (__d0), "=D" (__d1) : "a" (0), "0" (sizeof (fd_set) / sizeof (__fd_mask)), "1" (&__FDS_BITS (fdsp)[0]) : "memory"); } while (0) # macro
MPG123_MONO_MIX = 4
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
MPG123_STEREO = 2
def htole16(x): return (x) # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
def __CONCAT(x,y): return x ## y # macro
MPG123_FEATURE_DECODE_LAYER1 = 6
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
MPG123_FEATURE_INDEX = 4
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def __FD_SET(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] |= __FD_MASK (d))) # macro
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
MPG123_1_0 = 0
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
mpg123_text_max = 7
MPG123_FEEDBUFFER = 18
mpg123_text_utf16bom = 6
mpg123_text_utf16 = 5
mpg123_text_cp1252 = 4
MPG123_RESYNC_LIMIT = 14
MPG123_REMOVE_FLAGS = 13
MPG123_ENC_ULAW_8 = 4
MPG123_OUTSCALE = 11
MPG123_ICY_INTERVAL = 10
MPG123_DECODE_FRAMES = 9
MPG123_START_FRAME = 8
MPG123_UPSPEED = 7
MPG123_INDEX_SIZE = 15
MPG123_DOWNSPEED = 6
MPG123_BAD_BAND = 16
MPG123_DOWN_SAMPLE = 4
MPG123_FORCE_RATE = 3
MPG123_ADD_FLAGS = 2
MPG123_FLAGS = 1
MPG123_VERBOSE = 0
MPG123_RVA = 5
def __WTERMSIG(status): return ((status) & 0x7f) # macro
def __WSTOPSIG(status): return __WEXITSTATUS(status) # macro
# __CLOCKID_T_TYPE = __S32_TYPE # alias
MPG123_FRESH_DECODER = 4
MPG123_ACCURATE = 1
# NULL = __null # alias
MPG123_NEED_MORE = -10
MPG123_BAD_TYPES = 15
mpg123_id3_pic_artist_logo = 19
WSTOPPED = 2 # Variable c_int '2'
__STDLIB_MB_LEN_MAX = 16 # Variable c_int '16'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIERATTR_T = 4 # Variable c_int '4'
__have_pthread_attr_t = 1 # Variable c_int '1'
__WCLONE = 2147483648 # Variable c_uint '2147483648u'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__WCOREFLAG = 128 # Variable c_int '128'
_STRUCT_TIMEVAL = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
WNOWAIT = 16777216 # Variable c_int '16777216'
RAND_MAX = 2147483647 # Variable c_int '2147483647'
__WORDSIZE = 64 # Variable c_int '64'
MPG123_NEW_ID3 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_CONDATTR_T = 4 # Variable c_int '4'
_BITS_PTHREADTYPES_H = 1 # Variable c_int '1'
__USE_ATFILE = 1 # Variable c_int '1'
__time_t_defined = 1 # Variable c_int '1'
_SYS_SELECT_H = 1 # Variable c_int '1'
MPG123_NEW_ICY = 4 # Variable c_int '4'
__SIZEOF_PTHREAD_MUTEXATTR_T = 4 # Variable c_int '4'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
__USE_POSIX = 1 # Variable c_int '1'
_STDLIB_H = 1 # Variable c_int '1'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
_ALLOCA_H = 1 # Variable c_int '1'
__clock_t_defined = 1 # Variable c_int '1'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN = 1 # Variable c_int '1'
__USE_POSIX199309 = 1 # Variable c_int '1'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 19 # Variable c_int '19'
__clockid_t_defined = 1 # Variable c_int '1'
__timer_t_defined = 1 # Variable c_int '1'
__lldiv_t_defined = 1 # Variable c_int '1'
__ldiv_t_defined = 1 # Variable c_int '1'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIER_T = 32 # Variable c_int '32'
_SYS_TYPES_H = 1 # Variable c_int '1'
MPG123_ID3 = 3 # Variable c_int '3'
__timespec_defined = 1 # Variable c_int '1'
__USE_GNU = 1 # Variable c_int '1'
WUNTRACED = 2 # Variable c_int '2'
__USE_BSD = 1 # Variable c_int '1'
__USE_ISOC95 = 1 # Variable c_int '1'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_SIGSET_H_types = 1 # Variable c_int '1'
_ISOC11_SOURCE = 1 # Variable c_int '1'
__PTHREAD_RWLOCK_INT_FLAGS_SHARED = 1 # Variable c_int '1'
__USE_SVID = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_MUTEX_T = 40 # Variable c_int '40'
__USE_UNIX98 = 1 # Variable c_int '1'
__USE_POSIX199506 = 1 # Variable c_int '1'
__USE_MISC = 1 # Variable c_int '1'
__BIT_TYPES_DEFINED__ = 1 # Variable c_int '1'
__WNOTHREAD = 536870912 # Variable c_int '536870912'
__W_CONTINUED = 65535 # Variable c_int '65535'
__PTHREAD_MUTEX_HAVE_ELISION = 1 # Variable c_int '1'
_ENDIAN_H = 1 # Variable c_int '1'
__PTHREAD_MUTEX_HAVE_PREV = 1 # Variable c_int '1'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_RWLOCK_T = 56 # Variable c_int '56'
_BITS_BYTESWAP_H = 1 # Variable c_int '1'
WNOHANG = 1 # Variable c_int '1'
__OFF_T_MATCHES_OFF64_T = 1 # Variable c_int '1'
_SYS_SYSMACROS_H = 1 # Variable c_int '1'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
EXIT_SUCCESS = 0 # Variable c_int '0'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_COND_T = 48 # Variable c_int '48'
_FEATURES_H = 1 # Variable c_int '1'
__WALL = 1073741824 # Variable c_int '1073741824'
_BITS_TYPES_H = 1 # Variable c_int '1'
__INO_T_MATCHES_INO64_T = 1 # Variable c_int '1'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
MPG123_API_VERSION = 39 # Variable c_int '39'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_RWLOCKATTR_T = 8 # Variable c_int '8'
_SYS_CDEFS_H = 1 # Variable c_int '1'
WEXITED = 4 # Variable c_int '4'
_XOPEN_SOURCE = 700 # Variable c_int '700'
__SIZEOF_PTHREAD_ATTR_T = 56 # Variable c_int '56'
_SIGSET_NWORDS = 16 # Variable c_ulong '16ul'
MPG123_ICY = 12 # Variable c_int '12'
__GLIBC__ = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
WCONTINUED = 8 # Variable c_int '8'
__USE_ISOC11 = 1 # Variable c_int '1'
EXIT_FAILURE = 1 # Variable c_int '1'
_BSD_SOURCE = 1 # Variable c_int '1'
_XLOCALE_H = 1 # Variable c_int '1'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
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
class N14pthread_cond_t4DOT_11E(Structure):
    pass
N14pthread_cond_t4DOT_11E._fields_ = [
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
    ('__data', N14pthread_cond_t4DOT_11E),
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
class N16pthread_rwlock_t4DOT_14E(Structure):
    pass
N16pthread_rwlock_t4DOT_14E._fields_ = [
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
    ('__data', N16pthread_rwlock_t4DOT_14E),
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
__fdelt_chk = _libraries['/usr/lib/libmpg123.so'].__fdelt_chk
__fdelt_chk.restype = c_long
__fdelt_chk.argtypes = [c_long]
__fdelt_warn = _libraries['/usr/lib/libmpg123.so'].__fdelt_warn
__fdelt_warn.restype = c_long
__fdelt_warn.argtypes = [c_long]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
size_t = c_ulong
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
bsearch = _libraries['/usr/lib/libmpg123.so'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
atof = _libraries['/usr/lib/libmpg123.so'].atof
atof.restype = c_double
atof.argtypes = [STRING]
__realpath_chk = _libraries['/usr/lib/libmpg123.so'].__realpath_chk
__realpath_chk.restype = STRING
__realpath_chk.argtypes = [STRING, STRING, size_t]
realpath = _libraries['/usr/lib/libmpg123.so'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__ptsname_r_chk = _libraries['/usr/lib/libmpg123.so'].__ptsname_r_chk
__ptsname_r_chk.restype = c_int
__ptsname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ptsname_r = _libraries['/usr/lib/libmpg123.so'].ptsname_r
ptsname_r.restype = c_int
ptsname_r.argtypes = [c_int, STRING, size_t]
__wctomb_chk = _libraries['/usr/lib/libmpg123.so'].__wctomb_chk
__wctomb_chk.restype = c_int
__wctomb_chk.argtypes = [STRING, c_wchar, size_t]
wctomb = _libraries['/usr/lib/libmpg123.so'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
__mbstowcs_chk = _libraries['/usr/lib/libmpg123.so'].__mbstowcs_chk
__mbstowcs_chk.restype = size_t
__mbstowcs_chk.argtypes = [WSTRING, STRING, size_t, size_t]
mbstowcs = _libraries['/usr/lib/libmpg123.so'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
__wcstombs_chk = _libraries['/usr/lib/libmpg123.so'].__wcstombs_chk
__wcstombs_chk.restype = size_t
__wcstombs_chk.argtypes = [STRING, WSTRING, size_t, size_t]
wcstombs = _libraries['/usr/lib/libmpg123.so'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
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
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
__off_t = c_long
__off64_t = c_long
__pid_t = c_int
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
__ssize_t = c_long
__syscall_slong_t = c_long
__syscall_ulong_t = c_ulong
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
class wait(Union):
    pass
class N4wait3DOT_1E(Structure):
    pass
N4wait3DOT_1E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait3DOT_2E(Structure):
    pass
N4wait3DOT_2E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait3DOT_1E),
    ('__wait_stopped', N4wait3DOT_2E),
]
class mpg123_handle_struct(Structure):
    pass
mpg123_handle_struct._fields_ = [
]
mpg123_handle = mpg123_handle_struct
mpg123_init = _libraries['/usr/lib/libmpg123.so'].mpg123_init
mpg123_init.restype = c_int
mpg123_init.argtypes = []
mpg123_exit = _libraries['/usr/lib/libmpg123.so'].mpg123_exit
mpg123_exit.restype = None
mpg123_exit.argtypes = []
mpg123_new = _libraries['/usr/lib/libmpg123.so'].mpg123_new
mpg123_new.restype = POINTER(mpg123_handle)
mpg123_new.argtypes = [STRING, POINTER(c_int)]
mpg123_delete = _libraries['/usr/lib/libmpg123.so'].mpg123_delete
mpg123_delete.restype = None
mpg123_delete.argtypes = [POINTER(mpg123_handle)]

# values for enumeration 'mpg123_parms'
mpg123_parms = c_int # enum

# values for enumeration 'mpg123_param_flags'
mpg123_param_flags = c_int # enum

# values for enumeration 'mpg123_param_rva'
mpg123_param_rva = c_int # enum
mpg123_param = _libraries['/usr/lib/libmpg123.so'].mpg123_param
mpg123_param.restype = c_int
mpg123_param.argtypes = [POINTER(mpg123_handle), mpg123_parms, c_long, c_double]
mpg123_getparam = _libraries['/usr/lib/libmpg123.so'].mpg123_getparam
mpg123_getparam.restype = c_int
mpg123_getparam.argtypes = [POINTER(mpg123_handle), mpg123_parms, POINTER(c_long), POINTER(c_double)]

# values for enumeration 'mpg123_feature_set'
mpg123_feature_set = c_int # enum
mpg123_feature = _libraries['/usr/lib/libmpg123.so'].mpg123_feature
mpg123_feature.restype = c_int
mpg123_feature.argtypes = [mpg123_feature_set]

# values for enumeration 'mpg123_errors'
mpg123_errors = c_int # enum
mpg123_plain_strerror = _libraries['/usr/lib/libmpg123.so'].mpg123_plain_strerror
mpg123_plain_strerror.restype = STRING
mpg123_plain_strerror.argtypes = [c_int]
mpg123_strerror = _libraries['/usr/lib/libmpg123.so'].mpg123_strerror
mpg123_strerror.restype = STRING
mpg123_strerror.argtypes = [POINTER(mpg123_handle)]
mpg123_errcode = _libraries['/usr/lib/libmpg123.so'].mpg123_errcode
mpg123_errcode.restype = c_int
mpg123_errcode.argtypes = [POINTER(mpg123_handle)]
mpg123_decoders = _libraries['/usr/lib/libmpg123.so'].mpg123_decoders
mpg123_decoders.restype = POINTER(STRING)
mpg123_decoders.argtypes = []
mpg123_supported_decoders = _libraries['/usr/lib/libmpg123.so'].mpg123_supported_decoders
mpg123_supported_decoders.restype = POINTER(STRING)
mpg123_supported_decoders.argtypes = []
mpg123_decoder = _libraries['/usr/lib/libmpg123.so'].mpg123_decoder
mpg123_decoder.restype = c_int
mpg123_decoder.argtypes = [POINTER(mpg123_handle), STRING]
mpg123_current_decoder = _libraries['/usr/lib/libmpg123.so'].mpg123_current_decoder
mpg123_current_decoder.restype = STRING
mpg123_current_decoder.argtypes = [POINTER(mpg123_handle)]

# values for enumeration 'mpg123_enc_enum'
mpg123_enc_enum = c_int # enum

# values for enumeration 'mpg123_channelcount'
mpg123_channelcount = c_int # enum
mpg123_rates = _libraries['/usr/lib/libmpg123.so'].mpg123_rates
mpg123_rates.restype = None
mpg123_rates.argtypes = [POINTER(POINTER(c_long)), POINTER(size_t)]
mpg123_encodings = _libraries['/usr/lib/libmpg123.so'].mpg123_encodings
mpg123_encodings.restype = None
mpg123_encodings.argtypes = [POINTER(POINTER(c_int)), POINTER(size_t)]
mpg123_encsize = _libraries['/usr/lib/libmpg123.so'].mpg123_encsize
mpg123_encsize.restype = c_int
mpg123_encsize.argtypes = [c_int]
mpg123_format_none = _libraries['/usr/lib/libmpg123.so'].mpg123_format_none
mpg123_format_none.restype = c_int
mpg123_format_none.argtypes = [POINTER(mpg123_handle)]
mpg123_format_all = _libraries['/usr/lib/libmpg123.so'].mpg123_format_all
mpg123_format_all.restype = c_int
mpg123_format_all.argtypes = [POINTER(mpg123_handle)]
mpg123_format = _libraries['/usr/lib/libmpg123.so'].mpg123_format
mpg123_format.restype = c_int
mpg123_format.argtypes = [POINTER(mpg123_handle), c_long, c_int, c_int]
mpg123_format_support = _libraries['/usr/lib/libmpg123.so'].mpg123_format_support
mpg123_format_support.restype = c_int
mpg123_format_support.argtypes = [POINTER(mpg123_handle), c_long, c_int]
mpg123_getformat = _libraries['/usr/lib/libmpg123.so'].mpg123_getformat
mpg123_getformat.restype = c_int
mpg123_getformat.argtypes = [POINTER(mpg123_handle), POINTER(c_long), POINTER(c_int), POINTER(c_int)]
mpg123_open = _libraries['/usr/lib/libmpg123.so'].mpg123_open
mpg123_open.restype = c_int
mpg123_open.argtypes = [POINTER(mpg123_handle), STRING]
mpg123_open_fd = _libraries['/usr/lib/libmpg123.so'].mpg123_open_fd
mpg123_open_fd.restype = c_int
mpg123_open_fd.argtypes = [POINTER(mpg123_handle), c_int]
mpg123_open_handle = _libraries['/usr/lib/libmpg123.so'].mpg123_open_handle
mpg123_open_handle.restype = c_int
mpg123_open_handle.argtypes = [POINTER(mpg123_handle), c_void_p]
mpg123_open_feed = _libraries['/usr/lib/libmpg123.so'].mpg123_open_feed
mpg123_open_feed.restype = c_int
mpg123_open_feed.argtypes = [POINTER(mpg123_handle)]
mpg123_close = _libraries['/usr/lib/libmpg123.so'].mpg123_close
mpg123_close.restype = c_int
mpg123_close.argtypes = [POINTER(mpg123_handle)]
mpg123_read = _libraries['/usr/lib/libmpg123.so'].mpg123_read
mpg123_read.restype = c_int
mpg123_read.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), size_t, POINTER(size_t)]
mpg123_feed = _libraries['/usr/lib/libmpg123.so'].mpg123_feed
mpg123_feed.restype = c_int
mpg123_feed.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), size_t]
mpg123_decode = _libraries['/usr/lib/libmpg123.so'].mpg123_decode
mpg123_decode.restype = c_int
mpg123_decode.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), size_t, POINTER(c_ubyte), size_t, POINTER(size_t)]
off_t = __off_t
mpg123_decode_frame = _libraries['/usr/lib/libmpg123.so'].mpg123_decode_frame
mpg123_decode_frame.restype = c_int
mpg123_decode_frame.argtypes = [POINTER(mpg123_handle), POINTER(off_t), POINTER(POINTER(c_ubyte)), POINTER(size_t)]
mpg123_framebyframe_decode = _libraries['/usr/lib/libmpg123.so'].mpg123_framebyframe_decode
mpg123_framebyframe_decode.restype = c_int
mpg123_framebyframe_decode.argtypes = [POINTER(mpg123_handle), POINTER(off_t), POINTER(POINTER(c_ubyte)), POINTER(size_t)]
mpg123_framebyframe_next = _libraries['/usr/lib/libmpg123.so'].mpg123_framebyframe_next
mpg123_framebyframe_next.restype = c_int
mpg123_framebyframe_next.argtypes = [POINTER(mpg123_handle)]
mpg123_framedata = _libraries['/usr/lib/libmpg123.so'].mpg123_framedata
mpg123_framedata.restype = c_int
mpg123_framedata.argtypes = [POINTER(mpg123_handle), POINTER(c_ulong), POINTER(POINTER(c_ubyte)), POINTER(size_t)]
mpg123_framepos = _libraries['/usr/lib/libmpg123.so'].mpg123_framepos
mpg123_framepos.restype = off_t
mpg123_framepos.argtypes = [POINTER(mpg123_handle)]
mpg123_tell = _libraries['/usr/lib/libmpg123.so'].mpg123_tell
mpg123_tell.restype = off_t
mpg123_tell.argtypes = [POINTER(mpg123_handle)]
mpg123_tellframe = _libraries['/usr/lib/libmpg123.so'].mpg123_tellframe
mpg123_tellframe.restype = off_t
mpg123_tellframe.argtypes = [POINTER(mpg123_handle)]
mpg123_tell_stream = _libraries['/usr/lib/libmpg123.so'].mpg123_tell_stream
mpg123_tell_stream.restype = off_t
mpg123_tell_stream.argtypes = [POINTER(mpg123_handle)]
mpg123_seek = _libraries['/usr/lib/libmpg123.so'].mpg123_seek
mpg123_seek.restype = off_t
mpg123_seek.argtypes = [POINTER(mpg123_handle), off_t, c_int]
mpg123_feedseek = _libraries['/usr/lib/libmpg123.so'].mpg123_feedseek
mpg123_feedseek.restype = off_t
mpg123_feedseek.argtypes = [POINTER(mpg123_handle), off_t, c_int, POINTER(off_t)]
mpg123_seek_frame = _libraries['/usr/lib/libmpg123.so'].mpg123_seek_frame
mpg123_seek_frame.restype = off_t
mpg123_seek_frame.argtypes = [POINTER(mpg123_handle), off_t, c_int]
mpg123_timeframe = _libraries['/usr/lib/libmpg123.so'].mpg123_timeframe
mpg123_timeframe.restype = off_t
mpg123_timeframe.argtypes = [POINTER(mpg123_handle), c_double]
mpg123_index = _libraries['/usr/lib/libmpg123.so'].mpg123_index
mpg123_index.restype = c_int
mpg123_index.argtypes = [POINTER(mpg123_handle), POINTER(POINTER(off_t)), POINTER(off_t), POINTER(size_t)]
mpg123_set_index = _libraries['/usr/lib/libmpg123.so'].mpg123_set_index
mpg123_set_index.restype = c_int
mpg123_set_index.argtypes = [POINTER(mpg123_handle), POINTER(off_t), off_t, size_t]
mpg123_position = _libraries['/usr/lib/libmpg123.so'].mpg123_position
mpg123_position.restype = c_int
mpg123_position.argtypes = [POINTER(mpg123_handle), off_t, off_t, POINTER(off_t), POINTER(off_t), POINTER(c_double), POINTER(c_double)]

# values for enumeration 'mpg123_channels'
mpg123_channels = c_int # enum
mpg123_eq = _libraries['/usr/lib/libmpg123.so'].mpg123_eq
mpg123_eq.restype = c_int
mpg123_eq.argtypes = [POINTER(mpg123_handle), mpg123_channels, c_int, c_double]
mpg123_geteq = _libraries['/usr/lib/libmpg123.so'].mpg123_geteq
mpg123_geteq.restype = c_double
mpg123_geteq.argtypes = [POINTER(mpg123_handle), mpg123_channels, c_int]
mpg123_reset_eq = _libraries['/usr/lib/libmpg123.so'].mpg123_reset_eq
mpg123_reset_eq.restype = c_int
mpg123_reset_eq.argtypes = [POINTER(mpg123_handle)]
mpg123_volume = _libraries['/usr/lib/libmpg123.so'].mpg123_volume
mpg123_volume.restype = c_int
mpg123_volume.argtypes = [POINTER(mpg123_handle), c_double]
mpg123_volume_change = _libraries['/usr/lib/libmpg123.so'].mpg123_volume_change
mpg123_volume_change.restype = c_int
mpg123_volume_change.argtypes = [POINTER(mpg123_handle), c_double]
mpg123_getvolume = _libraries['/usr/lib/libmpg123.so'].mpg123_getvolume
mpg123_getvolume.restype = c_int
mpg123_getvolume.argtypes = [POINTER(mpg123_handle), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# values for enumeration 'mpg123_vbr'
mpg123_vbr = c_int # enum

# values for enumeration 'mpg123_version'
mpg123_version = c_int # enum

# values for enumeration 'mpg123_mode'
mpg123_mode = c_int # enum

# values for enumeration 'mpg123_flags'
mpg123_flags = c_int # enum
class mpg123_frameinfo(Structure):
    pass
mpg123_frameinfo._fields_ = [
    ('version', mpg123_version),
    ('layer', c_int),
    ('rate', c_long),
    ('mode', mpg123_mode),
    ('mode_ext', c_int),
    ('framesize', c_int),
    ('flags', mpg123_flags),
    ('emphasis', c_int),
    ('bitrate', c_int),
    ('abr_rate', c_int),
    ('vbr', mpg123_vbr),
]
mpg123_info = _libraries['/usr/lib/libmpg123.so'].mpg123_info
mpg123_info.restype = c_int
mpg123_info.argtypes = [POINTER(mpg123_handle), POINTER(mpg123_frameinfo)]
mpg123_safe_buffer = _libraries['/usr/lib/libmpg123.so'].mpg123_safe_buffer
mpg123_safe_buffer.restype = size_t
mpg123_safe_buffer.argtypes = []
mpg123_scan = _libraries['/usr/lib/libmpg123.so'].mpg123_scan
mpg123_scan.restype = c_int
mpg123_scan.argtypes = [POINTER(mpg123_handle)]
mpg123_length = _libraries['/usr/lib/libmpg123.so'].mpg123_length
mpg123_length.restype = off_t
mpg123_length.argtypes = [POINTER(mpg123_handle)]
mpg123_set_filesize = _libraries['/usr/lib/libmpg123.so'].mpg123_set_filesize
mpg123_set_filesize.restype = c_int
mpg123_set_filesize.argtypes = [POINTER(mpg123_handle), off_t]
mpg123_tpf = _libraries['/usr/lib/libmpg123.so'].mpg123_tpf
mpg123_tpf.restype = c_double
mpg123_tpf.argtypes = [POINTER(mpg123_handle)]
mpg123_spf = _libraries['/usr/lib/libmpg123.so'].mpg123_spf
mpg123_spf.restype = c_int
mpg123_spf.argtypes = [POINTER(mpg123_handle)]
mpg123_clip = _libraries['/usr/lib/libmpg123.so'].mpg123_clip
mpg123_clip.restype = c_long
mpg123_clip.argtypes = [POINTER(mpg123_handle)]

# values for enumeration 'mpg123_state'
mpg123_state = c_int # enum
mpg123_getstate = _libraries['/usr/lib/libmpg123.so'].mpg123_getstate
mpg123_getstate.restype = c_int
mpg123_getstate.argtypes = [POINTER(mpg123_handle), mpg123_state, POINTER(c_long), POINTER(c_double)]
class mpg123_string(Structure):
    pass
mpg123_string._fields_ = [
    ('p', STRING),
    ('size', size_t),
    ('fill', size_t),
]
mpg123_init_string = _libraries['/usr/lib/libmpg123.so'].mpg123_init_string
mpg123_init_string.restype = None
mpg123_init_string.argtypes = [POINTER(mpg123_string)]
mpg123_free_string = _libraries['/usr/lib/libmpg123.so'].mpg123_free_string
mpg123_free_string.restype = None
mpg123_free_string.argtypes = [POINTER(mpg123_string)]
mpg123_resize_string = _libraries['/usr/lib/libmpg123.so'].mpg123_resize_string
mpg123_resize_string.restype = c_int
mpg123_resize_string.argtypes = [POINTER(mpg123_string), size_t]
mpg123_grow_string = _libraries['/usr/lib/libmpg123.so'].mpg123_grow_string
mpg123_grow_string.restype = c_int
mpg123_grow_string.argtypes = [POINTER(mpg123_string), size_t]
mpg123_copy_string = _libraries['/usr/lib/libmpg123.so'].mpg123_copy_string
mpg123_copy_string.restype = c_int
mpg123_copy_string.argtypes = [POINTER(mpg123_string), POINTER(mpg123_string)]
mpg123_add_string = _libraries['/usr/lib/libmpg123.so'].mpg123_add_string
mpg123_add_string.restype = c_int
mpg123_add_string.argtypes = [POINTER(mpg123_string), STRING]
mpg123_add_substring = _libraries['/usr/lib/libmpg123.so'].mpg123_add_substring
mpg123_add_substring.restype = c_int
mpg123_add_substring.argtypes = [POINTER(mpg123_string), STRING, size_t, size_t]
mpg123_set_string = _libraries['/usr/lib/libmpg123.so'].mpg123_set_string
mpg123_set_string.restype = c_int
mpg123_set_string.argtypes = [POINTER(mpg123_string), STRING]
mpg123_set_substring = _libraries['/usr/lib/libmpg123.so'].mpg123_set_substring
mpg123_set_substring.restype = c_int
mpg123_set_substring.argtypes = [POINTER(mpg123_string), STRING, size_t, size_t]
mpg123_strlen = _libraries['/usr/lib/libmpg123.so'].mpg123_strlen
mpg123_strlen.restype = size_t
mpg123_strlen.argtypes = [POINTER(mpg123_string), c_int]
mpg123_chomp_string = _libraries['/usr/lib/libmpg123.so'].mpg123_chomp_string
mpg123_chomp_string.restype = c_int
mpg123_chomp_string.argtypes = [POINTER(mpg123_string)]

# values for enumeration 'mpg123_text_encoding'
mpg123_text_encoding = c_int # enum

# values for enumeration 'mpg123_id3_enc'
mpg123_id3_enc = c_int # enum
mpg123_enc_from_id3 = _libraries['/usr/lib/libmpg123.so'].mpg123_enc_from_id3
mpg123_enc_from_id3.restype = mpg123_text_encoding
mpg123_enc_from_id3.argtypes = [c_ubyte]
mpg123_store_utf8 = _libraries['/usr/lib/libmpg123.so'].mpg123_store_utf8
mpg123_store_utf8.restype = c_int
mpg123_store_utf8.argtypes = [POINTER(mpg123_string), mpg123_text_encoding, POINTER(c_ubyte), size_t]
class mpg123_text(Structure):
    pass
mpg123_text._fields_ = [
    ('lang', c_char * 3),
    ('id', c_char * 4),
    ('description', mpg123_string),
    ('text', mpg123_string),
]

# values for enumeration 'mpg123_id3_pic_type'
mpg123_id3_pic_type = c_int # enum
class mpg123_picture(Structure):
    pass
mpg123_picture._fields_ = [
    ('type', c_char),
    ('description', mpg123_string),
    ('mime_type', mpg123_string),
    ('size', size_t),
    ('data', POINTER(c_ubyte)),
]
class mpg123_id3v2(Structure):
    pass
mpg123_id3v2._fields_ = [
    ('version', c_ubyte),
    ('title', POINTER(mpg123_string)),
    ('artist', POINTER(mpg123_string)),
    ('album', POINTER(mpg123_string)),
    ('year', POINTER(mpg123_string)),
    ('genre', POINTER(mpg123_string)),
    ('comment', POINTER(mpg123_string)),
    ('comment_list', POINTER(mpg123_text)),
    ('comments', size_t),
    ('text', POINTER(mpg123_text)),
    ('texts', size_t),
    ('extra', POINTER(mpg123_text)),
    ('extras', size_t),
    ('picture', POINTER(mpg123_picture)),
    ('pictures', size_t),
]
class mpg123_id3v1(Structure):
    pass
mpg123_id3v1._fields_ = [
    ('tag', c_char * 3),
    ('title', c_char * 30),
    ('artist', c_char * 30),
    ('album', c_char * 30),
    ('year', c_char * 4),
    ('comment', c_char * 30),
    ('genre', c_ubyte),
]
mpg123_meta_check = _libraries['/usr/lib/libmpg123.so'].mpg123_meta_check
mpg123_meta_check.restype = c_int
mpg123_meta_check.argtypes = [POINTER(mpg123_handle)]
mpg123_meta_free = _libraries['/usr/lib/libmpg123.so'].mpg123_meta_free
mpg123_meta_free.restype = None
mpg123_meta_free.argtypes = [POINTER(mpg123_handle)]
mpg123_id3 = _libraries['/usr/lib/libmpg123.so'].mpg123_id3
mpg123_id3.restype = c_int
mpg123_id3.argtypes = [POINTER(mpg123_handle), POINTER(POINTER(mpg123_id3v1)), POINTER(POINTER(mpg123_id3v2))]
mpg123_icy = _libraries['/usr/lib/libmpg123.so'].mpg123_icy
mpg123_icy.restype = c_int
mpg123_icy.argtypes = [POINTER(mpg123_handle), POINTER(STRING)]
mpg123_icy2utf8 = _libraries['/usr/lib/libmpg123.so'].mpg123_icy2utf8
mpg123_icy2utf8.restype = STRING
mpg123_icy2utf8.argtypes = [STRING]
class mpg123_pars_struct(Structure):
    pass
mpg123_pars_struct._fields_ = [
]
mpg123_pars = mpg123_pars_struct
mpg123_parnew = _libraries['/usr/lib/libmpg123.so'].mpg123_parnew
mpg123_parnew.restype = POINTER(mpg123_handle)
mpg123_parnew.argtypes = [POINTER(mpg123_pars), STRING, POINTER(c_int)]
mpg123_new_pars = _libraries['/usr/lib/libmpg123.so'].mpg123_new_pars
mpg123_new_pars.restype = POINTER(mpg123_pars)
mpg123_new_pars.argtypes = [POINTER(c_int)]
mpg123_delete_pars = _libraries['/usr/lib/libmpg123.so'].mpg123_delete_pars
mpg123_delete_pars.restype = None
mpg123_delete_pars.argtypes = [POINTER(mpg123_pars)]
mpg123_fmt_none = _libraries['/usr/lib/libmpg123.so'].mpg123_fmt_none
mpg123_fmt_none.restype = c_int
mpg123_fmt_none.argtypes = [POINTER(mpg123_pars)]
mpg123_fmt_all = _libraries['/usr/lib/libmpg123.so'].mpg123_fmt_all
mpg123_fmt_all.restype = c_int
mpg123_fmt_all.argtypes = [POINTER(mpg123_pars)]
mpg123_fmt = _libraries['/usr/lib/libmpg123.so'].mpg123_fmt
mpg123_fmt.restype = c_int
mpg123_fmt.argtypes = [POINTER(mpg123_pars), c_long, c_int, c_int]
mpg123_fmt_support = _libraries['/usr/lib/libmpg123.so'].mpg123_fmt_support
mpg123_fmt_support.restype = c_int
mpg123_fmt_support.argtypes = [POINTER(mpg123_pars), c_long, c_int]
mpg123_par = _libraries['/usr/lib/libmpg123.so'].mpg123_par
mpg123_par.restype = c_int
mpg123_par.argtypes = [POINTER(mpg123_pars), mpg123_parms, c_long, c_double]
mpg123_getpar = _libraries['/usr/lib/libmpg123.so'].mpg123_getpar
mpg123_getpar.restype = c_int
mpg123_getpar.argtypes = [POINTER(mpg123_pars), mpg123_parms, POINTER(c_long), POINTER(c_double)]
mpg123_replace_buffer = _libraries['/usr/lib/libmpg123.so'].mpg123_replace_buffer
mpg123_replace_buffer.restype = c_int
mpg123_replace_buffer.argtypes = [POINTER(mpg123_handle), POINTER(c_ubyte), size_t]
mpg123_outblock = _libraries['/usr/lib/libmpg123.so'].mpg123_outblock
mpg123_outblock.restype = size_t
mpg123_outblock.argtypes = [POINTER(mpg123_handle)]
ssize_t = __ssize_t
mpg123_replace_reader = _libraries['/usr/lib/libmpg123.so'].mpg123_replace_reader
mpg123_replace_reader.restype = c_int
mpg123_replace_reader.argtypes = [POINTER(mpg123_handle), CFUNCTYPE(ssize_t, c_int, c_void_p, size_t), CFUNCTYPE(off_t, c_int, off_t, c_int)]
mpg123_replace_reader_handle = _libraries['/usr/lib/libmpg123.so'].mpg123_replace_reader_handle
mpg123_replace_reader_handle.restype = c_int
mpg123_replace_reader_handle.argtypes = [POINTER(mpg123_handle), CFUNCTYPE(ssize_t, c_void_p, c_void_p, size_t), CFUNCTYPE(off_t, c_void_p, off_t, c_int), CFUNCTYPE(None, c_void_p)]
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
__ctype_get_mb_cur_max = _libraries['/usr/lib/libmpg123.so'].__ctype_get_mb_cur_max
__ctype_get_mb_cur_max.restype = size_t
__ctype_get_mb_cur_max.argtypes = []
strtod = _libraries['/usr/lib/libmpg123.so'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['/usr/lib/libmpg123.so'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['/usr/lib/libmpg123.so'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['/usr/lib/libmpg123.so'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['/usr/lib/libmpg123.so'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['/usr/lib/libmpg123.so'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['/usr/lib/libmpg123.so'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['/usr/lib/libmpg123.so'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['/usr/lib/libmpg123.so'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
strtol_l = _libraries['/usr/lib/libmpg123.so'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['/usr/lib/libmpg123.so'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['/usr/lib/libmpg123.so'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['/usr/lib/libmpg123.so'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['/usr/lib/libmpg123.so'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['/usr/lib/libmpg123.so'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['/usr/lib/libmpg123.so'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
atoi = _libraries['/usr/lib/libmpg123.so'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['/usr/lib/libmpg123.so'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['/usr/lib/libmpg123.so'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
l64a = _libraries['/usr/lib/libmpg123.so'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['/usr/lib/libmpg123.so'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['/usr/lib/libmpg123.so'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['/usr/lib/libmpg123.so'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['/usr/lib/libmpg123.so'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['/usr/lib/libmpg123.so'].setstate
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
random_r = _libraries['/usr/lib/libmpg123.so'].random_r
random_r.restype = c_int
random_r.argtypes = [POINTER(random_data), POINTER(int32_t)]
srandom_r = _libraries['/usr/lib/libmpg123.so'].srandom_r
srandom_r.restype = c_int
srandom_r.argtypes = [c_uint, POINTER(random_data)]
initstate_r = _libraries['/usr/lib/libmpg123.so'].initstate_r
initstate_r.restype = c_int
initstate_r.argtypes = [c_uint, STRING, size_t, POINTER(random_data)]
setstate_r = _libraries['/usr/lib/libmpg123.so'].setstate_r
setstate_r.restype = c_int
setstate_r.argtypes = [STRING, POINTER(random_data)]
rand = _libraries['/usr/lib/libmpg123.so'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['/usr/lib/libmpg123.so'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['/usr/lib/libmpg123.so'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['/usr/lib/libmpg123.so'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['/usr/lib/libmpg123.so'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['/usr/lib/libmpg123.so'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['/usr/lib/libmpg123.so'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['/usr/lib/libmpg123.so'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['/usr/lib/libmpg123.so'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['/usr/lib/libmpg123.so'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['/usr/lib/libmpg123.so'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['/usr/lib/libmpg123.so'].lcong48
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
drand48_r = _libraries['/usr/lib/libmpg123.so'].drand48_r
drand48_r.restype = c_int
drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
erand48_r = _libraries['/usr/lib/libmpg123.so'].erand48_r
erand48_r.restype = c_int
erand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_double)]
lrand48_r = _libraries['/usr/lib/libmpg123.so'].lrand48_r
lrand48_r.restype = c_int
lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
nrand48_r = _libraries['/usr/lib/libmpg123.so'].nrand48_r
nrand48_r.restype = c_int
nrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
mrand48_r = _libraries['/usr/lib/libmpg123.so'].mrand48_r
mrand48_r.restype = c_int
mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
jrand48_r = _libraries['/usr/lib/libmpg123.so'].jrand48_r
jrand48_r.restype = c_int
jrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
srand48_r = _libraries['/usr/lib/libmpg123.so'].srand48_r
srand48_r.restype = c_int
srand48_r.argtypes = [c_long, POINTER(drand48_data)]
seed48_r = _libraries['/usr/lib/libmpg123.so'].seed48_r
seed48_r.restype = c_int
seed48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
lcong48_r = _libraries['/usr/lib/libmpg123.so'].lcong48_r
lcong48_r.restype = c_int
lcong48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
malloc = _libraries['/usr/lib/libmpg123.so'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['/usr/lib/libmpg123.so'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['/usr/lib/libmpg123.so'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['/usr/lib/libmpg123.so'].free
free.restype = None
free.argtypes = [c_void_p]
cfree = _libraries['/usr/lib/libmpg123.so'].cfree
cfree.restype = None
cfree.argtypes = [c_void_p]
valloc = _libraries['/usr/lib/libmpg123.so'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
posix_memalign = _libraries['/usr/lib/libmpg123.so'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]
aligned_alloc = _libraries['/usr/lib/libmpg123.so'].aligned_alloc
aligned_alloc.restype = c_void_p
aligned_alloc.argtypes = [size_t, size_t]
abort = _libraries['/usr/lib/libmpg123.so'].abort
abort.restype = None
abort.argtypes = []
on_exit = _libraries['/usr/lib/libmpg123.so'].on_exit
on_exit.restype = c_int
on_exit.argtypes = [CFUNCTYPE(None, c_int, c_void_p), c_void_p]
exit = _libraries['/usr/lib/libmpg123.so'].exit
exit.restype = None
exit.argtypes = [c_int]
quick_exit = _libraries['/usr/lib/libmpg123.so'].quick_exit
quick_exit.restype = None
quick_exit.argtypes = [c_int]
_Exit = _libraries['/usr/lib/libmpg123.so']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['/usr/lib/libmpg123.so'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
secure_getenv = _libraries['/usr/lib/libmpg123.so'].secure_getenv
secure_getenv.restype = STRING
secure_getenv.argtypes = [STRING]
putenv = _libraries['/usr/lib/libmpg123.so'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['/usr/lib/libmpg123.so'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['/usr/lib/libmpg123.so'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
clearenv = _libraries['/usr/lib/libmpg123.so'].clearenv
clearenv.restype = c_int
clearenv.argtypes = []
mktemp = _libraries['/usr/lib/libmpg123.so'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['/usr/lib/libmpg123.so'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemp64 = _libraries['/usr/lib/libmpg123.so'].mkstemp64
mkstemp64.restype = c_int
mkstemp64.argtypes = [STRING]
mkstemps = _libraries['/usr/lib/libmpg123.so'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkstemps64 = _libraries['/usr/lib/libmpg123.so'].mkstemps64
mkstemps64.restype = c_int
mkstemps64.argtypes = [STRING, c_int]
mkdtemp = _libraries['/usr/lib/libmpg123.so'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
mkostemp = _libraries['/usr/lib/libmpg123.so'].mkostemp
mkostemp.restype = c_int
mkostemp.argtypes = [STRING, c_int]
mkostemp64 = _libraries['/usr/lib/libmpg123.so'].mkostemp64
mkostemp64.restype = c_int
mkostemp64.argtypes = [STRING, c_int]
mkostemps = _libraries['/usr/lib/libmpg123.so'].mkostemps
mkostemps.restype = c_int
mkostemps.argtypes = [STRING, c_int, c_int]
mkostemps64 = _libraries['/usr/lib/libmpg123.so'].mkostemps64
mkostemps64.restype = c_int
mkostemps64.argtypes = [STRING, c_int, c_int]
system = _libraries['/usr/lib/libmpg123.so'].system
system.restype = c_int
system.argtypes = [STRING]
canonicalize_file_name = _libraries['/usr/lib/libmpg123.so'].canonicalize_file_name
canonicalize_file_name.restype = STRING
canonicalize_file_name.argtypes = [STRING]
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
qsort = _libraries['/usr/lib/libmpg123.so'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['/usr/lib/libmpg123.so'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['/usr/lib/libmpg123.so'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['/usr/lib/libmpg123.so'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['/usr/lib/libmpg123.so'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['/usr/lib/libmpg123.so'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['/usr/lib/libmpg123.so'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['/usr/lib/libmpg123.so'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['/usr/lib/libmpg123.so'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['/usr/lib/libmpg123.so'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['/usr/lib/libmpg123.so'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
qecvt = _libraries['/usr/lib/libmpg123.so'].qecvt
qecvt.restype = STRING
qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qfcvt = _libraries['/usr/lib/libmpg123.so'].qfcvt
qfcvt.restype = STRING
qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qgcvt = _libraries['/usr/lib/libmpg123.so'].qgcvt
qgcvt.restype = STRING
qgcvt.argtypes = [c_longdouble, c_int, STRING]
ecvt_r = _libraries['/usr/lib/libmpg123.so'].ecvt_r
ecvt_r.restype = c_int
ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
fcvt_r = _libraries['/usr/lib/libmpg123.so'].fcvt_r
fcvt_r.restype = c_int
fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qecvt_r = _libraries['/usr/lib/libmpg123.so'].qecvt_r
qecvt_r.restype = c_int
qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qfcvt_r = _libraries['/usr/lib/libmpg123.so'].qfcvt_r
qfcvt_r.restype = c_int
qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
mblen = _libraries['/usr/lib/libmpg123.so'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['/usr/lib/libmpg123.so'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
rpmatch = _libraries['/usr/lib/libmpg123.so'].rpmatch
rpmatch.restype = c_int
rpmatch.argtypes = [STRING]
getsubopt = _libraries['/usr/lib/libmpg123.so'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
posix_openpt = _libraries['/usr/lib/libmpg123.so'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['/usr/lib/libmpg123.so'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['/usr/lib/libmpg123.so'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['/usr/lib/libmpg123.so'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
getpt = _libraries['/usr/lib/libmpg123.so'].getpt
getpt.restype = c_int
getpt.argtypes = []
getloadavg = _libraries['/usr/lib/libmpg123.so'].getloadavg
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
select = _libraries['/usr/lib/libmpg123.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
pselect = _libraries['/usr/lib/libmpg123.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/lib/libmpg123.so'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/lib/libmpg123.so'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/lib/libmpg123.so'].gnu_dev_makedev
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
off64_t = __off64_t
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
__all__ = ['__uint16_t', 'MPG123_NO_8BIT', '__glibc_unlikely',
           'wctomb', 'mpg123_text_icy', 'mkstemps', 'mkostemp64',
           '__off64_t', '_ATFILE_SOURCE', '__WCOREFLAG',
           'MPG123_ENC_FLOAT_64', 'mpg123_version', 'secure_getenv',
           'MPG123_M_JOINT', 'mpg123_id3v1', 'makedev', '__FD_ISSET',
           'MPG123_RVA', 'rand_r', 'getpt', 'MPG123_ORIGINAL',
           'erand48_r', 'MPG123_ENC_UNSIGNED_24', 'mpg123_position',
           '__time_t_defined', '__time_t', 'MPG123_ENC_16',
           '__WSTOPSIG', '__GLIBC_PREREQ', '__ASMNAME', 'htole32',
           '__SIZEOF_PTHREAD_MUTEXATTR_T', '_POSIX_SOURCE',
           'MPG123_BUFFERFILL', 'pthread_rwlock_t', 'timer_t',
           '__ptsname_r_chk', 'div', 'mpg123_set_string',
           'gnu_dev_makedev', '__uint64_t', '_DEFAULT_SOURCE',
           'mpg123_icy2utf8', '_ALLOCA_H', 'strtoull',
           'MPG123_OUT_OF_SYNC', 'MPG123_OUT_OF_MEM',
           'N14pthread_cond_t4DOT_11E', '__ctype_get_mb_cur_max',
           'mpg123_vbr', '__USE_POSIX199309', 'MPG123_ENC_SIGNED_32',
           'mktemp', '__clockid_t', 'MPG123_IGNORE_STREAMLENGTH',
           '__mbstowcs_chk', 'MPG123_FUZZY', 'MPG123_MISSING_FEATURE',
           '__WEXITSTATUS', 'MPG123_FEATURE_OUTPUT_16BIT',
           'MPG123_1_0', '__attribute_format_strfmon__',
           'mpg123_channelcount', 'MPG123_BAD_DECODER_SETUP',
           'mpg123_enc_enum', 'be64toh', '__SIZEOF_PTHREAD_BARRIER_T',
           'mpg123_id3_pic_icon', 'mpg123_id3_enc', 'setstate_r',
           'mpg123_spf', 'MPG123_ADD_FLAGS',
           'MPG123_FEATURE_TIMEOUT_READ', '__u_long', 'wait',
           'mpg123_replace_reader', '__WIFEXITED',
           'mpg123_replace_buffer', 'MPG123_NO_SPACE', 'pthread_t',
           'MPG123_M_MONO', 'mpg123_decode_frame',
           'MPG123_NEW_FORMAT', 'MPG123_DOWNSPEED', 'mpg123_string',
           '__PMT', '_LARGEFILE_SOURCE', 'realloc', '__mode_t',
           'mpg123_length', 'qecvt', '__off_t', 'unlockpt',
           'mpg123_reset_eq', 'mpg123_id3_pic_illustration',
           '__WNOTHREAD', 'u_quad_t', 'canonicalize_file_name',
           'fsfilcnt64_t', 'daddr_t', 'mpg123_framebyframe_decode',
           'MPG123_OK', '_ENDIAN_H', 'strtof_l',
           'MPG123_NO_SEEK_FROM_END', 'MPG123_NO_READER', 'qsort',
           '__USE_FORTIFY_LEVEL', 'mpg123_id3_pic_lead',
           '__fsblkcnt64_t', 'MPG123_ENC_ULAW_8',
           '__SIZEOF_PTHREAD_CONDATTR_T', 'MPG123_ACCURATE',
           'BIG_ENDIAN', 'pthread_barrierattr_t', '__WTERMSIG',
           '__USE_XOPEN_EXTENDED', 'pid_t', 'mpg123_copy_string',
           'mpg123_getstate', 'mkostemps', 'strtoq', '__fsfilcnt64_t',
           'abort', 'mpg123_errors', 'pthread_key_t',
           'mpg123_feedseek', '__locale_struct', 'u_int8_t',
           '__realpath_chk', '__WALL', 'mpg123_free_string', 'off_t',
           'strtold', 'MPG123_VERBOSE', 'FD_ZERO',
           'MPG123_FEATURE_DECODE_ACCURATE', '__fsblkcnt_t',
           'strtoll', '__STDC_CONSTANT_MACROS', 'lcong48',
           'mpg123_handle', '__WIFCONTINUED', '__wcstombs_chk',
           'lrand48', 'mpg123_picture', '__WORDSIZE',
           'MPG123_RESYNC_LIMIT', 'mpg123_getparam', 'on_exit',
           'mpg123_param_flags', 'mblen', 'mpg123_id3_pic_orchestra',
           'WEXITED', '_XOPEN_SOURCE', 'unsetenv', 'mrand48_r',
           'mpg123_new_pars', 'srand48_r', 'key_t', '__USE_ISOC95',
           'mpg123_index', 'mpg123_id3_pic_leaflet', 'valloc',
           'MPG123_ICY', 'drand48_data', '__GLIBC__',
           'pthread_rwlockattr_t', 'mpg123_text_encoding',
           '__USE_ISOC99', 'MPG123_BAD_RATE',
           'MPG123_IGNORE_INFOFRAME', 'getloadavg', '__u_int',
           'ssize_t', '_XLOCALE_H', '__fsfilcnt_t',
           'mpg123_id3_pic_lyricist', 'le32toh', 'rand', 'strtouq',
           '_SIGSET_H_types', '__glibc_likely', '__LONG_LONG_PAIR',
           '__WCOREDUMP', 'strtoul', 'pthread_mutexattr_t', 'size_t',
           '__USE_XOPEN', 'mpg123_meta_check', 'MPG123_CBR',
           'strtol_l', 'mpg123_id3_pic_fish', 'mpg123_text_utf16be',
           'MPG123_NOT_INITIALIZED', 'mpg123_text_utf8', 'blkcnt_t',
           'MPG123_OUTSCALE', '__syscall_slong_t', '__wctomb_chk',
           'mkostemps64', 'mpg123_resize_string', 'MPG123_NEW_ID3',
           'ecvt', '__qaddr_t', '__NFDBITS', 'MPG123_BAD_OUTFORMAT',
           'MPG123_RESYNC_FAIL', 'mpg123_text_utf16',
           'mpg123_text_utf16bom', 'mpg123_decoders', 'mpg123_decode',
           '__W_EXITCODE', 'MPG123_FEATURE_OUTPUT_32BIT',
           'LITTLE_ENDIAN', 'u_char', 'mpg123_volume_change', 'uid_t',
           '__USE_ATFILE', 'u_int64_t', 'MPG123_BAD_HANDLE',
           'MPG123_NEW_ICY', 'sigset_t', 'MPG123_LFS_OVERFLOW',
           'mpg123_strlen', 'gcvt', 'seed48', 'useconds_t',
           '__int32_t', 'MPG123_ERR', '__USE_POSIX', '__locale_t',
           'MPG123_RIGHT', 'MPG123_AUTO_RESAMPLE',
           'mpg123_id3_pic_location', 'MPG123_COPYRIGHT',
           'MPG123_ERR_NULL', '__fsword_t', 'mpg123_eq',
           'MPG123_ENC_UNSIGNED_32', 'MPG123_BAD_CHANNEL',
           'mpg123_fmt_none', 'WIFSIGNALED', 'initstate_r',
           '__useconds_t', '__GLIBC_MINOR__', 'clock_t', 'div_t',
           '__clockid_t_defined', '__BYTE_ORDER',
           'MPG123_NULL_POINTER', 'MPG123_GAPLESS',
           'MPG123_INDEX_SIZE', 'mpg123_store_utf8',
           'pthread_barrier_t', 'strtoull_l', 'u_int32_t',
           'mpg123_volume', '__pthread_internal_list',
           '__WORDSIZE_TIME64_COMPAT32', 'free', 'labs',
           '_SYS_TYPES_H', '__P', 'qsort_r', 'MPG123_ENC_SIGNED_24',
           'MPG123_NO_TIMEOUT', 'MPG123_ERR_16TO8TABLE', '__USE_GNU',
           'WUNTRACED', 'MPG123_QUIET', 'random_r', 'htobe16',
           '__pthread_list_t', 'MPG123_MONO_MIX', 'pthread_attr_t',
           '__attribute_format_arg__', 'uint', '__rlim64_t', 'ino_t',
           'strtoll_l', 'MPG123_LSEEK_FAILED', '_POSIX_C_SOURCE',
           'major', '__W_CONTINUED', 'mbtowc', '__W_STOPCODE',
           '__blksize_t', '__USE_SVID', 'pthread_spinlock_t',
           'MPG123_REMOVE_FLAGS', '__ldiv_t_defined',
           'MPG123_FEATURE_OUTPUT_8BIT', 'MPG123_FEATURE_PARSE_ICY',
           'MPG123_M_STEREO', 'MPG123_BAD_RVA', 'system',
           '__bswap_constant_32', 'mpg123_id3_utf16bom', 'ino64_t',
           'le16toh', 'mpg123_id3_utf16be', 'MPG123_FORCE_MONO',
           'MPG123_PREFRAMES', 'ecvt_r', '__uint8_t',
           '__SIZEOF_PTHREAD_RWLOCK_T', 'mpg123_supported_decoders',
           '__caddr_t', 'strtod_l', '__blkcnt64_t', 'mkostemp',
           'MPG123_ABR', '_Exit', 'mpg123_fmt_support',
           'MPG123_MONO_LEFT', 'MPG123_BAD_INDEX_PAR', 'quad_t',
           '__USE_LARGEFILE', '__USE_EXTERN_INLINES',
           '__SIZEOF_PTHREAD_COND_T', '_FEATURES_H', 'mkstemp64',
           'int16_t', 'wcstombs', 'mpg123_id3_latin1',
           'MPG123_START_FRAME', 'MPG123_ENC_24', 'pthread_cond_t',
           'abs', 'MPG123_FEATURE_PARSE_ID3V2', '_BITS_TYPES_H',
           'MPG123_FEATURE_DECODE_LAYER2',
           'MPG123_FEATURE_DECODE_LAYER3', 'mpg123_pars_struct',
           'PDP_ENDIAN', 'MPG123_NO_RESYNC', 'mpg123_grow_string',
           '__rlim_t', 'MPG123_BAD_VALUE', 'N4wait3DOT_1E',
           'mpg123_rates', 'nlink_t', 'mpg123_id3_enc_max',
           '_XOPEN_SOURCE_EXTENDED', 'MPG123_BAD_KEY', 'timeval',
           'WNOWAIT', 'mpg123_id3_pic_type', 'mpg123_handle_struct',
           'MPG123_UPSPEED', '__u_char', '__id_t', 'realpath',
           'mpg123_open_handle', 'ulong', '__clock_t', 'int8_t',
           '__WIFSTOPPED', 'mpg123_set_filesize', 'MPG123_RVA_OFF',
           'MPG123_FEEDBUFFER', 'MPG123_NO_GAPLESS', 'srand48',
           'fsblkcnt_t', 'mpg123_text_latin1', 'MPG123_PICTURE',
           'mpg123_param_rva', 'mpg123_geteq', '__quad_t',
           'mpg123_format_none', '_BSD_SOURCE', 'dev_t', '__uid_t',
           '__FD_ZERO_STOS', 'WTERMSIG', '__pthread_mutex_s',
           'MPG123_FORCE_FLOAT', 'a64l', 'MPG123_DONE', 'random',
           'N16pthread_rwlock_t4DOT_14E', 'mpg123_outblock',
           '__GNU_LIBRARY__', '_BITS_TYPESIZES_H', 'nrand48_r',
           'mode_t', 'mpg123_chomp_string', '__STDLIB_MB_LEN_MAX',
           '__USE_LARGEFILE64', 'MPG123_FEATURE_ABI_UTF8OPEN',
           'mpg123_format_support', 'strtol', 'mpg123_par', 'htobe64',
           'grantpt', 'strtod', 'mpg123_tell_stream', 'strtof',
           'mpg123_clip', 'lrand48_r', 'mpg123_encodings',
           'mpg123_safe_buffer', '__loff_t', 'mpg123_set_index',
           'mpg123_set_substring', 'FD_CLR', 'MPG123_ICY_INTERVAL',
           'ptsname_r', 'MPG123_NO_SEEK', '__lldiv_t_defined',
           'MPG123_BAD_CUSTOM_IO', '__WCLONE', 'MPG123_ENC_SIGNED',
           'srandom', 'mpg123_open_feed', 'MPG123_LEFT',
           'mpg123_pars', 'mpg123_icy', 'fd_mask', 'MPG123_ENC_FLOAT',
           '__int16_t', '__bos', 'be32toh', '_STDLIB_H', 'mkdtemp',
           '__ssize_t', 'comparison_fn_t', 'mpg123_parms',
           'mpg123_feature', 'qgcvt', 'lcong48_r', 'quick_exit',
           'MPG123_FEEDPOOL', 'MPG123_FEATURE_DECODE_DOWNSAMPLE',
           'mpg123_feed', 'jrand48', '__warnattr', '__sigset_t',
           'posix_memalign', 'WIFCONTINUED', 'ldiv_t', 'MPG123_LR',
           'mpg123_tpf', 'mpg123_id3_pic_recording', 'MPG123_STEREO',
           '__USE_XOPEN2K', 'mpg123_text', '__FD_SETSIZE',
           'MPG123_TIMEOUT', 'id_t', 'htole16', '__intptr_t',
           'seed48_r', 'mpg123_scan', 'MPG123_ID3',
           '__timespec_defined', '__USE_POSIX2', '__blkcnt_t',
           'MPG123_ENC_SIGNED_8', 'clockid_t', 'MPG123_M_DUAL',
           'mpg123_id3v2', 'mpg123_exit', 'MPG123_NEED_MORE',
           'caddr_t', 'MPG123_NO_BUFFERS', 'timespec',
           '__SIZEOF_PTHREAD_BARRIERATTR_T', 'MPG123_BAD_PARAM',
           '__REDIRECT_NTH_LDBL', 'mpg123_id3_pic_media',
           'MPG123_NO_INDEX', 'off64_t',
           '__PTHREAD_RWLOCK_INT_FLAGS_SHARED', 'ptsname', 'alloca',
           '__USE_MISC', '__locale_data', 'MPG123_BAD_BAND',
           '__BIT_TYPES_DEFINED__', 'MPG123_MONO', 'getsubopt',
           '__compar_d_fn_t', 'MPG123_INT_OVERFLOW', 'aligned_alloc',
           'WIFEXITED', 'mpg123_framepos', 'mpg123_meta_free',
           'gnu_dev_major', 'MPG123_BAD_WHENCE',
           'MPG123_FEATURE_DECODE_LAYER1', 'mpg123_text_cp1252',
           '__PTHREAD_MUTEX_HAVE_ELISION', 'fcvt_r', 'MPG123_RVA_MIX',
           'MPG123_BAD_FILE', 'MPG123_NULL_BUFFER', 'MPG123_FLAGS',
           '__PTHREAD_MUTEX_HAVE_PREV', 'MPG123_NO_RELSEEK',
           '__OFF_T_MATCHES_OFF64_T', 'WSTOPSIG', 'WNOHANG',
           'mpg123_close', '__dev_t', 'mpg123_channels', 'pselect',
           '_SYS_SYSMACROS_H', 'drand48', 'EXIT_SUCCESS',
           '__suseconds_t', 'u_long', 'MPG123_BAD_TYPES', 'qfcvt',
           'mpg123_seek', 'clearenv', 'mpg123_id3_pic_performance',
           'malloc', 'ushort', '__USE_POSIX199506', 'mpg123_id3_utf8',
           'cfree', '__BIG_ENDIAN', 'srand',
           '__INO_T_MATCHES_INO64_T', 'mpg123_delete',
           'MPG123_SKIP_ID3V2', 'mpg123_plain_strerror',
           'MPG123_BAD_ALIGN', 'MPG123_PLAIN_ID3TEXT', 'time_t',
           'u_short', 'mpg123_text_max', 'mpg123_flags',
           '__FLOAT_WORD_ORDER', 'qfcvt_r', '__USE_XOPEN2K8XSI',
           'fsblkcnt64_t', 'mpg123_getpar', 'mpg123_seek_frame',
           'mpg123_mode', 'mpg123_id3_pic_video', '_SYS_CDEFS_H',
           'fsfilcnt_t', 'setstate', 'mpg123_init', 'MPG123_ENC_32',
           'mpg123_add_string', '__SIZEOF_PTHREAD_ATTR_T',
           'mpg123_framedata', '__ino_t', 'calloc', '__REDIRECT_LDBL',
           'mpg123_add_substring', 'srandom_r', 'mpg123_state',
           'MPG123_BAD_DECODER', 'WCONTINUED', 'drand48_r',
           'MPG123_FEATURE_DECODE_NTOM', 'MPG123_ENC_8', 'nrand48',
           'pthread_mutex_t', '__int64_t', 'suseconds_t', 'be16toh',
           'WSTOPPED', 'MPG123_CRC', '__USE_XOPEN2KXSI',
           'MPG123_DOWN_SAMPLE', '__LITTLE_ENDIAN',
           '__have_pthread_attr_t', 'mkstemps64',
           'pthread_condattr_t', 'pthread_once_t', '__fsid_t',
           'MPG123_FRESH_DECODER', 'random_data', 'u_int16_t',
           'atoll', '__uint32_t', '__USE_XOPEN2K8', '_STRUCT_TIMEVAL',
           'ldiv', 'mpg123_delete_pars', 'MPG123_BAD_PARS',
           'RAND_MAX', 'setenv', '__ino64_t', '__u_quad_t', 'int32_t',
           'mpg123_format_all', 'loff_t', 'mpg123_tellframe',
           'blksize_t', 'MPG123_ENC_ALAW_8',
           'mpg123_id3_pic_composer', 'mpg123_format',
           '_BITS_PTHREADTYPES_H', 'N4wait3DOT_2E', 'WIFSTOPPED',
           'mpg123_open_fd', 'register_t', 'gnu_dev_minor',
           'mpg123_param', '_SYS_SELECT_H', 'mpg123_fmt',
           'mpg123_text_unknown', 'MPG123_FORCE_8BIT',
           'MPG123_FEATURE_INDEX', '_ISOC95_SOURCE',
           'mpg123_framebyframe_next', '_ISOC99_SOURCE', '__nlink_t',
           '__compar_fn_t', 'mpg123_open', 'MPG123_INDEX_FAIL',
           'lldiv', 'fd_set', 'rpmatch', 'mrand48', '__fdelt_warn',
           'mpg123_strerror', '__clock_t_defined', '__pid_t',
           'mpg123_getvolume', 'MPG123_VBR', 'MPG123_RVA_ALBUM',
           '__SYSCALL_WORDSIZE', 'gid_t', 'MPG123_ENC_SIGNED_16',
           'mpg123_current_decoder', '__timer_t', 'qecvt_r',
           'mpg123_read', '__timer_t_defined', 'exit', 'select',
           'mpg123_getformat', 'mbstowcs',
           'mpg123_id3_pic_artist_logo', 'mpg123_id3',
           'MPG123_PRIVATE', '_SVID_SOURCE', 'FD_ISSET',
           'MPG123_ENC_UNSIGNED_8', 'MPG123_FORCE_STEREO', 'htole64',
           'mpg123_enc_from_id3', 'mpg123_id3_pic_publisher_logo',
           '__USE_BSD', 'mpg123_id3_pic_conductor', '__CONCAT',
           'MPG123_ENC_FLOAT_32', 'bsearch', 'fcvt',
           'MPG123_SEEKBUFFER', '_ISOC11_SOURCE', 'MPG123_ENC_ANY',
           '__fdelt_chk', 'mpg123_info', 'mpg123_timeframe',
           'MPG123_ERR_READER', '__syscall_ulong_t',
           '__SIZEOF_PTHREAD_MUTEX_T', '__USE_UNIX98',
           'MPG123_ENC_UNSIGNED_16', 'mpg123_tell', '__gid_t',
           'putenv', 'MPG123_2_0', 'MPG123_2_5', '__daddr_t',
           '__sig_atomic_t', 'mpg123_id3_pic_back_cover',
           'mpg123_fmt_all', 'l64a', 'u_int', 'getenv', 'htobe32',
           'atoi', '__fd_mask', 'atol', 'MPG123_FRANKENSTEIN', 'atof',
           'mpg123_parnew', 'erand48', 'minor', 'MPG123_MONO_RIGHT',
           'mpg123_encsize', 'blkcnt64_t', 'llabs',
           'mpg123_id3_pic_artist', 'FD_SET', 'mpg123_frameinfo',
           'jrand48_r', 'initstate', '__STRING', 'int64_t',
           'WEXITSTATUS', 'le64toh', '__GNUC_PREREQ', 'BYTE_ORDER',
           'posix_openpt', 'lldiv_t', 'MPG123_API_VERSION',
           'strtold_l', 'MPG123_FORCE_RATE',
           '__SIZEOF_PTHREAD_RWLOCKATTR_T', '__PDP_ENDIAN',
           '__u_short', 'mkstemp', 'mpg123_errcode', '__int8_t',
           '__key_t', 'fsid_t', '_LARGEFILE64_SOURCE',
           '__va_arg_pack', 'FD_SETSIZE', 'mpg123_id3_pic_other',
           '_BITS_BYTESWAP_H', 'MPG123_DECODE_FRAMES',
           'mpg123_id3_pic_front_cover', '_SIGSET_NWORDS',
           'mpg123_init_string', '__va_arg_pack_len',
           'MPG123_BAD_BUFFER', 'MPG123_RVA_MAX', '__bos0',
           'mpg123_id3_pic_other_icon', 'mpg123_decoder', 'strtoul_l',
           'locale_t', '__socklen_t', '__USE_ISOC11', 'EXIT_FAILURE',
           'mpg123_replace_reader_handle', 'mpg123_new',
           'mpg123_feature_set', 'NFDBITS']
