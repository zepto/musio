from ctypes import *

_libraries = {}
_libraries['/usr/lib/libFLAC.so'] = CDLL('/usr/lib/libFLAC.so')
STRING = c_char_p
WSTRING = c_wchar_p


# __S32_TYPE = int # alias
# __DADDR_T_TYPE = __S32_TYPE # alias
FLAC__STREAM_DECODER_READ_STATUS_CONTINUE = 0
# __UID_T_TYPE = __U32_TYPE # alias
# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
FLAC__STREAM_ENCODER_MEMORY_ALLOCATION_ERROR = 8
FLAC__STREAM_ENCODER_FRAMING_ERROR = 7
FLAC__STREAM_ENCODER_IO_ERROR = 6
FLAC__STREAM_ENCODER_CLIENT_ERROR = 5
FLAC__STREAM_ENCODER_VERIFY_MISMATCH_IN_AUDIO_DATA = 4
FLAC__STREAM_ENCODER_VERIFY_DECODER_ERROR = 3
FLAC__STREAM_ENCODER_OGG_ERROR = 2
FLAC__STREAM_ENCODER_OK = 0
FLAC__SUBFRAME_TYPE_LPC = 3
FLAC__SUBFRAME_TYPE_FIXED = 2
FLAC__SUBFRAME_TYPE_VERBATIM = 1
FLAC__SUBFRAME_TYPE_CONSTANT = 0
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2 = 1
FLAC__STREAM_DECODER_LENGTH_STATUS_UNSUPPORTED = 2
FLAC__STREAM_DECODER_LENGTH_STATUS_ERROR = 1
FLAC__STREAM_DECODER_LENGTH_STATUS_OK = 0
# __GID_T_TYPE = __U32_TYPE # alias
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_INTERNAL_ERROR = 12
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_MEMORY_ALLOCATION_ERROR = 11
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_BAD_METADATA = 5
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_NOT_WRITABLE = 4
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
__BYTE_ORDER = __LITTLE_ENDIAN # alias
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
class __va_list_tag(Structure):
    pass
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
_IO_va_list = __gnuc_va_list # alias
__ssize_t = c_long
_IO_ssize_t = __ssize_t # alias
size_t = c_ulong
_IO_size_t = size_t # alias
class _G_fpos_t(Structure):
    pass
__off_t = c_long
class __mbstate_t(Structure):
    pass
class N11__mbstate_t4DOT_56E(Union):
    pass
N11__mbstate_t4DOT_56E._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * 4),
]
__mbstate_t._fields_ = [
    ('__count', c_int),
    ('__value', N11__mbstate_t4DOT_56E),
]
_G_fpos_t._fields_ = [
    ('__pos', __off_t),
    ('__state', __mbstate_t),
]
_IO_fpos_t = _G_fpos_t # alias
class _IO_FILE(Structure):
    pass
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libFLAC.so'], 'stdout')
stdout = stdout # alias
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libFLAC.so'], 'stdin')
stdin = stdin # alias
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libFLAC.so'], 'stderr')
stderr = stderr # alias
# __wur = __attribute_warn_unused_result__ # alias
# __WCHAR_MIN = __WCHAR_MIN__ # alias
# __WCHAR_MAX = __WCHAR_MAX__ # alias
FLAC__MAX_METADATA_TYPE = 126
FLAC__METADATA_TYPE_UNDEFINED = 7
FLAC__METADATA_TYPE_CUESHEET = 5
FLAC__METADATA_TYPE_VORBIS_COMMENT = 4
FLAC__METADATA_TYPE_PADDING = 1
FLAC__METADATA_TYPE_STREAMINFO = 0
FLAC__STREAM_DECODER_SEEK_STATUS_OK = 0
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_ERROR_OPENING_FILE = 2
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_ILLEGAL_INPUT = 1
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_OK = 0
FLAC__STREAM_DECODER_TELL_STATUS_UNSUPPORTED = 2
FLAC__STREAM_DECODER_TELL_STATUS_OK = 0
FLAC__STREAM_DECODER_WRITE_STATUS_ABORT = 1
FLAC__STREAM_DECODER_WRITE_STATUS_CONTINUE = 0
# __USECONDS_T_TYPE = __U32_TYPE # alias
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
# __SLONG32_TYPE = int # alias
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
# __PID_T_TYPE = __S32_TYPE # alias
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __MODE_T_TYPE = __U32_TYPE # alias
# __KEY_T_TYPE = __S32_TYPE # alias
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __INO64_T_TYPE = __UQUAD_TYPE # alias
# __ID_T_TYPE = __U32_TYPE # alias
FLAC__STREAM_DECODER_READ_STATUS_ABORT = 2
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
FLAC__STREAM_DECODER_READ_STATUS_END_OF_STREAM = 1
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
__FLOAT_WORD_ORDER = __BYTE_ORDER # alias
# __DEV_T_TYPE = __UQUAD_TYPE # alias
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __CLOCKID_T_TYPE = __S32_TYPE # alias
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
__uid_t = c_uint
_IO_uid_t = __uid_t # alias
__pid_t = c_int
_IO_pid_t = __pid_t # alias
_IO_off_t = __off_t # alias
__off64_t = c_long
_IO_off64_t = __off64_t # alias
# _IO_iconv_t = _G_iconv_t # alias
class _G_fpos64_t(Structure):
    pass
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
# _IO_file_flags = _flags # alias
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_SAMPLE_RATE = 6
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_NUMBER_OF_CHANNELS = 4
FLAC__STREAM_ENCODER_SEEK_STATUS_OK = 0
FLAC__STREAM_DECODER_ABORTED = 7
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE = 0
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
# def __bswap_constant_64(x): return (__extension__ ((((x) & 0xff00000000000000ull) >> 56) | (((x) & 0x00ff000000000000ull) >> 40) | (((x) & 0x0000ff0000000000ull) >> 24) | (((x) & 0x000000ff00000000ull) >> 8) | (((x) & 0x00000000ff000000ull) << 8) | (((x) & 0x0000000000ff0000ull) << 24) | (((x) & 0x000000000000ff00ull) << 40) | (((x) & 0x00000000000000ffull) << 56))) # macro
def __bswap_constant_32(x): return ((((x) & 0xff000000) >> 24) | (((x) & 0x00ff0000) >> 8) | (((x) & 0x0000ff00) << 8) | (((x) & 0x000000ff) << 24)) # macro
# def __bswap_constant_16(x): return ((unsigned short int) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8))) # macro
FLAC__STREAM_METADATA_PICTURE_TYPE_VIDEO_SCREEN_CAPTURE = 16
FLAC__STREAM_METADATA_PICTURE_TYPE_DURING_PERFORMANCE = 15
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
FLAC__STREAM_METADATA_PICTURE_TYPE_COMPOSER = 11
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
def __W_STOPCODE(sig): return ((sig) << 8 | 0x7f) # macro
def __W_EXITCODE(ret,sig): return ((ret) << 8 | (sig)) # macro
def __WTERMSIG(status): return ((status) & 0x7f) # macro
def __WSTOPSIG(status): return __WEXITSTATUS(status) # macro
# def __WIFSIGNALED(status): return (((signed char) (((status) & 0x7f) + 1) >> 1) > 0) # macro
def __WIFCONTINUED(status): return ((status) == __W_CONTINUED) # macro
# def __WAIT_INT(status): return (*(int *) &(status)) # macro
def __STRING(x): return #x # macro
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
FLAC__METADATA_CHAIN_STATUS_NOT_A_FLAC_FILE = 3
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
def __PMT(args): return args # macro
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_BITS_PER_SAMPLE = 5
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_CALLBACKS = 3
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
FLAC__STREAM_ENCODER_INIT_STATUS_UNSUPPORTED_CONTAINER = 2
FLAC__STREAM_ENCODER_INIT_STATUS_ENCODER_ERROR = 1
FLAC__STREAM_ENCODER_INIT_STATUS_OK = 0
FLAC__METADATA_CHAIN_STATUS_INVALID_CALLBACKS = 13
FLAC__STREAM_DECODER_MEMORY_ALLOCATION_ERROR = 8
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
FLAC__CHANNEL_ASSIGNMENT_RIGHT_SIDE = 2
FLAC__CHANNEL_ASSIGNMENT_LEFT_SIDE = 1
FLAC__METADATA_TYPE_PICTURE = 6
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_UNLINK_ERROR = 10
FLAC__STREAM_ENCODER_INIT_STATUS_ALREADY_INITIALIZED = 13
FLAC__METADATA_TYPE_SEEKTABLE = 3
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_QLP_COEFF_PRECISION = 9
FLAC__STREAM_ENCODER_SEEK_STATUS_UNSUPPORTED = 2
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_BLOCK_SIZE = 7
FLAC__METADATA_TYPE_APPLICATION = 2
FLAC__STREAM_DECODER_SEEK_ERROR = 6
FLAC__METADATA_CHAIN_STATUS_OK = 0
FLAC__STREAM_ENCODER_SEEK_STATUS_ERROR = 1
FLAC__STREAM_DECODER_OGG_ERROR = 5
FLAC__FRAME_NUMBER_TYPE_SAMPLE_NUMBER = 1
FLAC__FRAME_NUMBER_TYPE_FRAME_NUMBER = 0
FLAC__STREAM_ENCODER_TELL_STATUS_UNSUPPORTED = 2
FLAC__STREAM_ENCODER_TELL_STATUS_ERROR = 1
FLAC__STREAM_ENCODER_TELL_STATUS_OK = 0
FLAC__STREAM_ENCODER_UNINITIALIZED = 1
# _IO_wint_t = wint_t # alias
FLAC__STREAM_DECODER_INIT_STATUS_ALREADY_INITIALIZED = 5
FLAC__STREAM_DECODER_INIT_STATUS_ERROR_OPENING_FILE = 4
FLAC__STREAM_DECODER_INIT_STATUS_MEMORY_ALLOCATION_ERROR = 3
FLAC__STREAM_DECODER_INIT_STATUS_INVALID_CALLBACKS = 2
FLAC__STREAM_DECODER_INIT_STATUS_UNSUPPORTED_CONTAINER = 1
FLAC__STREAM_DECODER_INIT_STATUS_OK = 0
FLAC__STREAM_METADATA_PICTURE_TYPE_UNDEFINED = 21
FLAC__STREAM_DECODER_READ_METADATA = 1
def WIFEXITED(status): return __WIFEXITED (__WAIT_INT (status)) # macro
def WIFCONTINUED(status): return __WIFCONTINUED (__WAIT_INT (status)) # macro
def WEXITSTATUS(status): return __WEXITSTATUS (__WAIT_INT (status)) # macro
def UINTMAX_C(c): return c ## UL # macro
def UINT8_C(c): return c # macro
def UINT64_C(c): return c ## UL # macro
def UINT32_C(c): return c ## U # macro
def UINT16_C(c): return c # macro
def INTMAX_C(c): return c ## L # macro
def INT8_C(c): return c # macro
def INT64_C(c): return c ## L # macro
def INT32_C(c): return c # macro
def INT16_C(c): return c # macro
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp) # macro
def FD_SET(fd,fdsetp): return __FD_SET (fd, fdsetp) # macro
def FD_ISSET(fd,fdsetp): return __FD_ISSET (fd, fdsetp) # macro
def FD_CLR(fd,fdsetp): return __FD_CLR (fd, fdsetp) # macro
FLAC__CHANNEL_ASSIGNMENT_MID_SIDE = 3
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_METADATA = 12
FLAC__STREAM_ENCODER_INIT_STATUS_NOT_STREAMABLE = 11
FLAC__STREAM_ENCODER_INIT_STATUS_BLOCK_SIZE_TOO_SMALL_FOR_LPC_ORDER = 10
FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_MAX_LPC_ORDER = 8
FLAC__STREAM_ENCODER_WRITE_STATUS_FATAL_ERROR = 1
FLAC__STREAM_ENCODER_WRITE_STATUS_OK = 0
FLAC__CHANNEL_ASSIGNMENT_INDEPENDENT = 0
FLAC__METADATA_CHAIN_STATUS_WRONG_WRITE_CALL = 15
FLAC__METADATA_CHAIN_STATUS_READ_WRITE_MISMATCH = 14
FLAC__METADATA_CHAIN_STATUS_INTERNAL_ERROR = 12
FLAC__METADATA_CHAIN_STATUS_MEMORY_ALLOCATION_ERROR = 11
FLAC__METADATA_CHAIN_STATUS_UNLINK_ERROR = 10
FLAC__METADATA_CHAIN_STATUS_RENAME_ERROR = 9
FLAC__METADATA_CHAIN_STATUS_WRITE_ERROR = 8
FLAC__METADATA_CHAIN_STATUS_SEEK_ERROR = 7
FLAC__METADATA_CHAIN_STATUS_READ_ERROR = 6
FLAC__METADATA_CHAIN_STATUS_BAD_METADATA = 5
FLAC__METADATA_CHAIN_STATUS_NOT_WRITABLE = 4
FLAC__METADATA_CHAIN_STATUS_ERROR_OPENING_FILE = 2
FLAC__METADATA_CHAIN_STATUS_ILLEGAL_INPUT = 1
__codecvt_noconv = 3
__codecvt_error = 2
__codecvt_partial = 1
__codecvt_ok = 0
FLAC__STREAM_ENCODER_READ_STATUS_UNSUPPORTED = 3
FLAC__STREAM_ENCODER_READ_STATUS_ABORT = 2
FLAC__STREAM_ENCODER_READ_STATUS_END_OF_STREAM = 1
FLAC__STREAM_ENCODER_READ_STATUS_CONTINUE = 0
_G_va_list = __gnuc_va_list # alias
# WCHAR_MIN = __WCHAR_MIN # alias
# WCHAR_MAX = __WCHAR_MAX # alias
__PDP_ENDIAN = 3412 # Variable c_int '3412'
PDP_ENDIAN = __PDP_ENDIAN # alias
# NULL = __null # alias
__NFDBITS = 64 # Variable c_int '64'
NFDBITS = __NFDBITS # alias
LITTLE_ENDIAN = __LITTLE_ENDIAN # alias
__FD_SETSIZE = 1024 # Variable c_int '1024'
FD_SETSIZE = __FD_SETSIZE # alias
BYTE_ORDER = __BYTE_ORDER # alias
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
BUFSIZ = _IO_BUFSIZ # alias
__BIG_ENDIAN = 4321 # Variable c_int '4321'
BIG_ENDIAN = __BIG_ENDIAN # alias
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
def minor(dev): return gnu_dev_minor (dev) # macro
def makedev(maj,min): return gnu_dev_makedev (maj, min) # macro
def major(dev): return gnu_dev_major (dev) # macro
def le64toh(x): return (x) # macro
def le32toh(x): return (x) # macro
def le16toh(x): return (x) # macro
def htole64(x): return (x) # macro
def htole32(x): return (x) # macro
def htole16(x): return (x) # macro
def htobe64(x): return __bswap_64 (x) # macro
def htobe32(x): return __bswap_32 (x) # macro
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
def htobe16(x): return __bswap_16 (x) # macro
def getc(_fp): return _IO_getc (_fp) # macro
def be64toh(x): return __bswap_64 (x) # macro
def be32toh(x): return __bswap_32 (x) # macro
def be16toh(x): return __bswap_16 (x) # macro
def alloca(size): return __builtin_alloca (size) # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
# def __u_intN_t(N,MODE): return typedef unsigned int u_int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
# def __intN_t(N,MODE): return typedef int int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
def WSTOPSIG(status): return __WSTOPSIG (__WAIT_INT (status)) # macro
def WIFSTOPPED(status): return __WIFSTOPPED (__WAIT_INT (status)) # macro
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_NOT_A_FLAC_FILE = 3
FLAC__STREAM_DECODER_ERROR_STATUS_FRAME_CRC_MISMATCH = 2
FLAC__STREAM_DECODER_UNINITIALIZED = 9
FLAC__STREAM_DECODER_END_OF_STREAM = 4
FLAC__STREAM_DECODER_READ_FRAME = 3
FLAC__STREAM_DECODER_SEARCH_FOR_FRAME_SYNC = 2
FLAC__STREAM_DECODER_SEARCH_FOR_METADATA = 0
FLAC__STREAM_DECODER_SEEK_STATUS_ERROR = 1
FLAC__STREAM_METADATA_PICTURE_TYPE_PUBLISHER_LOGOTYPE = 20
FLAC__STREAM_METADATA_PICTURE_TYPE_BAND_LOGOTYPE = 19
FLAC__STREAM_METADATA_PICTURE_TYPE_ILLUSTRATION = 18
FLAC__STREAM_METADATA_PICTURE_TYPE_FISH = 17
# def __bswap_16(x): return (__extension__ ({ unsigned short int __v, __x = (unsigned short int) (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_16 (__x); else __asm__ ("rorw $8, %w0" : "=r" (__v) : "0" (__x) : "cc"); __v; })) # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
FLAC__STREAM_METADATA_PICTURE_TYPE_DURING_RECORDING = 14
FLAC__STREAM_METADATA_PICTURE_TYPE_RECORDING_LOCATION = 13
FLAC__STREAM_METADATA_PICTURE_TYPE_LYRICIST = 12
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
FLAC__STREAM_METADATA_PICTURE_TYPE_BAND = 10
FLAC__STREAM_METADATA_PICTURE_TYPE_CONDUCTOR = 9
FLAC__STREAM_METADATA_PICTURE_TYPE_ARTIST = 8
FLAC__STREAM_METADATA_PICTURE_TYPE_LEAD_ARTIST = 7
FLAC__STREAM_METADATA_PICTURE_TYPE_MEDIA = 6
FLAC__STREAM_METADATA_PICTURE_TYPE_LEAFLET_PAGE = 5
FLAC__STREAM_METADATA_PICTURE_TYPE_BACK_COVER = 4
FLAC__STREAM_METADATA_PICTURE_TYPE_FRONT_COVER = 3
FLAC__STREAM_METADATA_PICTURE_TYPE_FILE_ICON = 2
FLAC__STREAM_METADATA_PICTURE_TYPE_FILE_ICON_STANDARD = 1
FLAC__STREAM_METADATA_PICTURE_TYPE_OTHER = 0
def __WIFEXITED(status): return (__WTERMSIG(status) == 0) # macro
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_RENAME_ERROR = 9
def __WEXITSTATUS(status): return (((status) & 0xff00) >> 8) # macro
FLAC__STREAM_DECODER_ERROR_STATUS_UNPARSEABLE_STREAM = 3
def __WCOREDUMP(status): return ((status) & __WCOREFLAG) # macro
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_WRITE_ERROR = 8
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_SEEK_ERROR = 7
def __P(args): return args # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
def __LONG_LONG_PAIR(HI,LO): return LO, HI # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
FLAC__METADATA_SIMPLE_ITERATOR_STATUS_READ_ERROR = 6
# def __LDBL_REDIR(name,proto): return name proto # macro
# def __FD_ZERO(fdsp): return do { int __d0, __d1; __asm__ __volatile__ ("cld; rep; " __FD_ZERO_STOS : "=c" (__d0), "=D" (__d1) : "a" (0), "0" (sizeof (fd_set) / sizeof (__fd_mask)), "1" (&__FDS_BITS (fdsp)[0]) : "memory"); } while (0) # macro
# def __FD_SET(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] |= __FD_MASK (d))) # macro
FLAC__STREAM_DECODER_SEEK_STATUS_UNSUPPORTED = 2
# def __FD_MASK(d): return ((__fd_mask) (1UL << ((d) % __NFDBITS))) # macro
def __FD_ISSET(d,set): return ((__FDS_BITS (set)[__FD_ELT (d)] & __FD_MASK (d)) != 0) # macro
# def __FD_ELT(d): return __extension__ ({ long int __d = (d); (__builtin_constant_p (__d) ? (0 <= __d && __d < __FD_SETSIZE ? (__d / __NFDBITS) : __fdelt_warn (__d)) : __fdelt_chk (__d)); }) # macro
# def __FD_CLR(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] &= ~__FD_MASK (d))) # macro
# def __FDS_BITS(set): return ((set)->fds_bits) # macro
def __CONCAT(x,y): return x ## y # macro
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
def __WIFSTOPPED(status): return (((status) & 0xff) == 0x7f) # macro
FLAC__STREAM_DECODER_ERROR_STATUS_BAD_HEADER = 1
FLAC__STREAM_DECODER_ERROR_STATUS_LOST_SYNC = 0
FLAC__STREAM_DECODER_TELL_STATUS_ERROR = 1
def WIFSIGNALED(status): return __WIFSIGNALED (__WAIT_INT (status)) # macro
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
def WTERMSIG(status): return __WTERMSIG (__WAIT_INT (status)) # macro
INT_LEAST8_MAX = 127 # Variable c_int '127'
_ATFILE_SOURCE = 1 # Variable c_int '1'
EOF = -1 # Variable c_int '-0x00000000000000001'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
UINT8_MAX = 255 # Variable c_int '255'
__have_pthread_attr_t = 1 # Variable c_int '1'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
FLAC__SUBSET_MAX_RICE_PARTITION_ORDER = 8 # Variable c_uint '8u'
INT32_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
FLAC__MAX_QLP_COEFF_PRECISION = 15 # Variable c_uint '15u'
_IONBF = 2 # Variable c_int '2'
__STDLIB_MB_LEN_MAX = 16 # Variable c_int '16'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
FLAC_API_VERSION_CURRENT = 11 # Variable c_int '11'
INT64_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
UINT_FAST16_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__WCOREFLAG = 128 # Variable c_int '128'
_STRUCT_TIMEVAL = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
RAND_MAX = 2147483647 # Variable c_int '2147483647'
__SIZEOF_PTHREAD_RWLOCKATTR_T = 8 # Variable c_int '8'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
__SIZEOF_PTHREAD_CONDATTR_T = 4 # Variable c_int '4'
FLAC_API_VERSION_REVISION = 0 # Variable c_int '0'
_IO_LEFT = 2 # Variable c_int '2'
FLAC__MIN_QLP_COEFF_PRECISION = 5 # Variable c_uint '5u'
UINTMAX_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
_SYS_SELECT_H = 1 # Variable c_int '1'
_IO_SHOWPOINT = 256 # Variable c_int '256'
_G_config_h = 1 # Variable c_int '1'
____mbstate_t_defined = 1 # Variable c_int '1'
FLAC__MIN_BLOCK_SIZE = 16 # Variable c_uint '16u'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
__USE_ATFILE = 1 # Variable c_int '1'
INTMAX_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
__time_t_defined = 1 # Variable c_int '1'
TMP_MAX = 238328 # Variable c_int '238328'
INT_LEAST16_MAX = 32767 # Variable c_int '32767'
FLAC__STREAM_SYNC_LENGTH = 4 # Variable c_uint '4u'
_G_HAVE_MMAP = 1 # Variable c_int '1'
FOPEN_MAX = 16 # Variable c_int '16'
INT_LEAST32_MAX = 2147483647 # Variable c_int '2147483647'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
INTMAX_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
__SIZEOF_PTHREAD_MUTEXATTR_T = 4 # Variable c_int '4'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
INT64_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
_ISOC99_SOURCE = 1 # Variable c_int '1'
UINT_FAST8_MAX = 255 # Variable c_int '255'
__USE_POSIX = 1 # Variable c_int '1'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_SIGSET_H_types = 1 # Variable c_int '1'
_IO_NO_WRITES = 8 # Variable c_int '8'
INT_LEAST8_MIN = -128 # Variable c_int '-0x00000000000000080'
FLAC__STREAM_METADATA_STREAMINFO_LENGTH = 34 # Variable c_uint '34u'
FLAC__MAX_LPC_ORDER = 32 # Variable c_uint '32u'
_OLD_STDIO_MAGIC = 4206624768 # Variable c_uint '4206624768u'
_STDLIB_H = 1 # Variable c_int '1'
INT_FAST64_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
_ALLOCA_H = 1 # Variable c_int '1'
INT_FAST64_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
__FILE_defined = 1 # Variable c_int '1'
__clock_t_defined = 1 # Variable c_int '1'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
FLAC__STREAM_METADATA_SEEKPOINT_LENGTH = 18 # Variable c_uint '18u'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
_STDIO_H = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944 # Variable c_uint '4222418944u'
__USE_POSIX199309 = 1 # Variable c_int '1'
FLAC__MIN_BITS_PER_SAMPLE = 4 # Variable c_uint '4u'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 20 # Variable c_int '20'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
FLAC__MAX_FIXED_ORDER = 4 # Variable c_uint '4u'
_IO_UPPERCASE = 512 # Variable c_int '512'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
UINT32_MAX = 4294967295 # Variable c_uint '4294967295u'
__clockid_t_defined = 1 # Variable c_int '1'
_IO_SHOWBASE = 128 # Variable c_int '128'
__timer_t_defined = 1 # Variable c_int '1'
SEEK_SET = 0 # Variable c_int '0'
FLAC__MAX_SAMPLE_RATE = 655350 # Variable c_uint '655350u'
FLAC__MAX_CHANNELS = 8 # Variable c_uint '8u'
_IO_FIXED = 4096 # Variable c_int '4096'
__BIT_TYPES_DEFINED__ = 1 # Variable c_int '1'
__lldiv_t_defined = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIER_T = 32 # Variable c_int '32'
INT_LEAST16_MIN = -32768 # Variable c_int '-0x00000000000008000'
_SYS_TYPES_H = 1 # Variable c_int '1'
FLAC__MAX_BITS_PER_SAMPLE = 32 # Variable c_uint '32u'
_IO_USER_BUF = 1 # Variable c_int '1'
FLAC__SUBSET_MAX_BLOCK_SIZE_48000HZ = 4608 # Variable c_uint '4608u'
_IO_EOF_SEEN = 16 # Variable c_int '16'
_IOS_BIN = 128 # Variable c_int '128'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_IO_ERR_SEEN = 32 # Variable c_int '32'
_IOFBF = 0 # Variable c_int '0'
FLAC__MAX_RICE_PARTITION_ORDER = 15 # Variable c_uint '15u'
_IO_SKIPWS = 1 # Variable c_int '1'
__timespec_defined = 1 # Variable c_int '1'
SEEK_END = 2 # Variable c_int '2'
__USE_GNU = 1 # Variable c_int '1'
WUNTRACED = 2 # Variable c_int '2'
__USE_ISOC95 = 1 # Variable c_int '1'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
UINTPTR_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
_IO_IN_BACKUP = 256 # Variable c_int '256'
_IOS_NOREPLACE = 64 # Variable c_int '64'
__SIZEOF_PTHREAD_BARRIERATTR_T = 4 # Variable c_int '4'
INT16_MIN = -32768 # Variable c_int '-0x00000000000008000'
_ISOC11_SOURCE = 1 # Variable c_int '1'
INT8_MAX = 127 # Variable c_int '127'
____FILE_defined = 1 # Variable c_int '1'
L_tmpnam = 20 # Variable c_int '20'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
__PTHREAD_RWLOCK_INT_FLAGS_SHARED = 1 # Variable c_int '1'
SEEK_CUR = 1 # Variable c_int '1'
_IO_DEC = 16 # Variable c_int '16'
INT_LEAST64_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
__SIZEOF_PTHREAD_MUTEX_T = 40 # Variable c_int '40'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
__USE_POSIX199506 = 1 # Variable c_int '1'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
__USE_MISC = 1 # Variable c_int '1'
__GLIBC__ = 2 # Variable c_int '2'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
__ldiv_t_defined = 1 # Variable c_int '1'
__WNOTHREAD = 536870912 # Variable c_int '536870912'
_IO_RIGHT = 4 # Variable c_int '4'
INT8_MIN = -128 # Variable c_int '-0x00000000000000080'
__W_CONTINUED = 65535 # Variable c_int '65535'
_IO_LINE_BUF = 512 # Variable c_int '512'
_IO_OCT = 32 # Variable c_int '32'
WSTOPPED = 2 # Variable c_int '2'
_IOS_TRUNC = 16 # Variable c_int '16'
INTPTR_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
FLAC__STREAM_METADATA_HEADER_LENGTH = 4 # Variable c_uint '4u'
UINT_LEAST64_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
L_ctermid = 9 # Variable c_int '9'
_ENDIAN_H = 1 # Variable c_int '1'
UINT_FAST64_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
_IOS_APPEND = 8 # Variable c_int '8'
_STDINT_H = 1 # Variable c_int '1'
__PTHREAD_MUTEX_HAVE_PREV = 1 # Variable c_int '1'
_IO_INTERNAL = 8 # Variable c_int '8'
__SIZEOF_PTHREAD_RWLOCK_T = 56 # Variable c_int '56'
__OFF_T_MATCHES_OFF64_T = 1 # Variable c_int '1'
PTRDIFF_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
WNOHANG = 1 # Variable c_int '1'
_IO_LINKED = 128 # Variable c_int '128'
INT_LEAST32_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
_IOS_NOCREATE = 32 # Variable c_int '32'
FILENAME_MAX = 4096 # Variable c_int '4096'
L_cuserid = 9 # Variable c_int '9'
_SYS_SYSMACROS_H = 1 # Variable c_int '1'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
UINT16_MAX = 65535 # Variable c_int '65535'
SEEK_HOLE = 4 # Variable c_int '4'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
EXIT_SUCCESS = 0 # Variable c_int '0'
INT32_MAX = 2147483647 # Variable c_int '2147483647'
UINT_LEAST8_MAX = 255 # Variable c_int '255'
INT_LEAST64_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_COND_T = 48 # Variable c_int '48'
PTRDIFF_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
UINT_FAST32_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
_FEATURES_H = 1 # Variable c_int '1'
_IO_HEX = 64 # Variable c_int '64'
__WCLONE = 2147483648 # Variable c_uint '2147483648u'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
FLAC__MAX_BLOCK_SIZE = 65535 # Variable c_uint '65535u'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
INT_FAST32_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
SEEK_DATA = 3 # Variable c_int '3'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
_IOS_INPUT = 1 # Variable c_int '1'
SIG_ATOMIC_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
__WALL = 1073741824 # Variable c_int '1073741824'
_IO_UNITBUF = 8192 # Variable c_int '8192'
_BITS_TYPES_H = 1 # Variable c_int '1'
SIG_ATOMIC_MAX = 2147483647 # Variable c_int '2147483647'
__INO_T_MATCHES_INO64_T = 1 # Variable c_int '1'
INT_FAST32_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
UINT_LEAST32_MAX = 4294967295 # Variable c_uint '4294967295u'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
INT_FAST16_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
_IO_NO_READS = 4 # Variable c_int '4'
_IO_MAGIC_MASK = 4294901760 # Variable c_uint '4294901760u'
WNOWAIT = 16777216 # Variable c_int '16777216'
__WORDSIZE = 64 # Variable c_int '64'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
_IO_UNBUFFERED = 2 # Variable c_int '2'
INT_FAST16_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
INT_FAST8_MIN = -128 # Variable c_int '-0x00000000000000080'
FLAC_API_VERSION_AGE = 3 # Variable c_int '3'
WEXITED = 4 # Variable c_int '4'
__USE_XOPEN = 1 # Variable c_int '1'
FLAC__REFERENCE_CODEC_MAX_BITS_PER_SAMPLE = 24 # Variable c_uint '24u'
_XOPEN_SOURCE = 700 # Variable c_int '700'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
__SIZEOF_PTHREAD_ATTR_T = 56 # Variable c_int '56'
_IOS_ATEND = 4 # Variable c_int '4'
SIZE_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
INT_FAST8_MAX = 127 # Variable c_int '127'
WINT_MIN = 0 # Variable c_uint '0u'
_IOS_OUTPUT = 2 # Variable c_int '2'
_SIGSET_NWORDS = 16 # Variable c_ulong '16ul'
FLAC__SUBSET_MAX_LPC_ORDER_48000HZ = 12 # Variable c_uint '12u'
UINT_LEAST16_MAX = 65535 # Variable c_int '65535'
_BITS_BYTESWAP_H = 1 # Variable c_int '1'
INTPTR_MAX = 9223372036854775807 # Variable c_long '9223372036854775807l'
UINT64_MAX = 18446744073709551615 # Variable c_ulong '-1ul'
__USE_ISOC99 = 1 # Variable c_int '1'
_BITS_WCHAR_H = 1 # Variable c_int '1'
_BITS_PTHREADTYPES_H = 1 # Variable c_int '1'
INT16_MAX = 32767 # Variable c_int '32767'
WCONTINUED = 8 # Variable c_int '8'
__USE_ISOC11 = 1 # Variable c_int '1'
EXIT_FAILURE = 1 # Variable c_int '1'
WINT_MAX = 4294967295 # Variable c_uint '4294967295u'
_IOLBF = 1 # Variable c_int '1'
_XLOCALE_H = 1 # Variable c_int '1'
FLAC__MAX_METADATA_TYPE_CODE = 126 # Variable c_uint '126u'
__FD_ZERO_STOS = 'stosq' # Variable STRING '(const char*)"stosq"'
FLAC__IOHandle = c_void_p
FLAC__IOCallback_Read = CFUNCTYPE(size_t, c_void_p, size_t, size_t, FLAC__IOHandle)
FLAC__IOCallback_Write = CFUNCTYPE(size_t, c_void_p, size_t, size_t, FLAC__IOHandle)
int64_t = c_int64
FLAC__int64 = int64_t
FLAC__IOCallback_Seek = CFUNCTYPE(c_int, FLAC__IOHandle, FLAC__int64, c_int)
FLAC__IOCallback_Tell = CFUNCTYPE(FLAC__int64, FLAC__IOHandle)
FLAC__IOCallback_Eof = CFUNCTYPE(c_int, FLAC__IOHandle)
FLAC__IOCallback_Close = CFUNCTYPE(c_int, FLAC__IOHandle)
class FLAC__IOCallbacks(Structure):
    pass
FLAC__IOCallbacks._fields_ = [
    ('read', FLAC__IOCallback_Read),
    ('write', FLAC__IOCallback_Write),
    ('seek', FLAC__IOCallback_Seek),
    ('tell', FLAC__IOCallback_Tell),
    ('eof', FLAC__IOCallback_Eof),
    ('close', FLAC__IOCallback_Close),
]
FLAC_API_SUPPORTS_OGG_FLAC = (c_int).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC_API_SUPPORTS_OGG_FLAC')
FLAC__VERSION_STRING = (STRING).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__VERSION_STRING')
FLAC__VENDOR_STRING = (STRING).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__VENDOR_STRING')
uint8_t = c_uint8
FLAC__uint8 = uint8_t
FLAC__byte = FLAC__uint8
FLAC__STREAM_SYNC_STRING = (FLAC__byte * 4).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_SYNC_STRING')
FLAC__STREAM_SYNC = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_SYNC')
FLAC__STREAM_SYNC_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_SYNC_LEN')

# values for enumeration 'FLAC__EntropyCodingMethodType'
FLAC__EntropyCodingMethodType = c_int # enum
FLAC__EntropyCodingMethodTypeString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__EntropyCodingMethodTypeString')
class FLAC__EntropyCodingMethod_PartitionedRiceContents(Structure):
    pass
FLAC__EntropyCodingMethod_PartitionedRiceContents._fields_ = [
    ('parameters', POINTER(c_uint)),
    ('raw_bits', POINTER(c_uint)),
    ('capacity_by_order', c_uint),
]
class FLAC__EntropyCodingMethod_PartitionedRice(Structure):
    pass
FLAC__EntropyCodingMethod_PartitionedRice._fields_ = [
    ('order', c_uint),
    ('contents', POINTER(FLAC__EntropyCodingMethod_PartitionedRiceContents)),
]
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ORDER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ORDER_LEN')
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_PARAMETER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_PARAMETER_LEN')
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_PARAMETER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_PARAMETER_LEN')
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_RAW_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_RAW_LEN')
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ESCAPE_PARAMETER = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ESCAPE_PARAMETER')
FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_ESCAPE_PARAMETER = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_ESCAPE_PARAMETER')
class N25FLAC__EntropyCodingMethod4DOT_23E(Union):
    pass
N25FLAC__EntropyCodingMethod4DOT_23E._fields_ = [
    ('partitioned_rice', FLAC__EntropyCodingMethod_PartitionedRice),
]
class FLAC__EntropyCodingMethod(Structure):
    pass
FLAC__EntropyCodingMethod._fields_ = [
    ('type', FLAC__EntropyCodingMethodType),
    ('data', N25FLAC__EntropyCodingMethod4DOT_23E),
]
FLAC__ENTROPY_CODING_METHOD_TYPE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ENTROPY_CODING_METHOD_TYPE_LEN')

# values for enumeration 'FLAC__SubframeType'
FLAC__SubframeType = c_int # enum
FLAC__SubframeTypeString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SubframeTypeString')
class FLAC__Subframe_Constant(Structure):
    pass
int32_t = c_int32
FLAC__int32 = int32_t
FLAC__Subframe_Constant._fields_ = [
    ('value', FLAC__int32),
]
class FLAC__Subframe_Verbatim(Structure):
    pass
FLAC__Subframe_Verbatim._fields_ = [
    ('data', POINTER(FLAC__int32)),
]
class FLAC__Subframe_Fixed(Structure):
    pass
FLAC__Subframe_Fixed._fields_ = [
    ('entropy_coding_method', FLAC__EntropyCodingMethod),
    ('order', c_uint),
    ('warmup', FLAC__int32 * 4),
    ('residual', POINTER(FLAC__int32)),
]
class FLAC__Subframe_LPC(Structure):
    pass
FLAC__Subframe_LPC._fields_ = [
    ('entropy_coding_method', FLAC__EntropyCodingMethod),
    ('order', c_uint),
    ('qlp_coeff_precision', c_uint),
    ('quantization_level', c_int),
    ('qlp_coeff', FLAC__int32 * 32),
    ('warmup', FLAC__int32 * 32),
    ('residual', POINTER(FLAC__int32)),
]
FLAC__SUBFRAME_LPC_QLP_COEFF_PRECISION_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_LPC_QLP_COEFF_PRECISION_LEN')
FLAC__SUBFRAME_LPC_QLP_SHIFT_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_LPC_QLP_SHIFT_LEN')
class N14FLAC__Subframe4DOT_30E(Union):
    pass
N14FLAC__Subframe4DOT_30E._fields_ = [
    ('constant', FLAC__Subframe_Constant),
    ('fixed', FLAC__Subframe_Fixed),
    ('lpc', FLAC__Subframe_LPC),
    ('verbatim', FLAC__Subframe_Verbatim),
]
class FLAC__Subframe(Structure):
    pass
FLAC__Subframe._fields_ = [
    ('type', FLAC__SubframeType),
    ('data', N14FLAC__Subframe4DOT_30E),
    ('wasted_bits', c_uint),
]
FLAC__SUBFRAME_ZERO_PAD_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_ZERO_PAD_LEN')
FLAC__SUBFRAME_TYPE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_TYPE_LEN')
FLAC__SUBFRAME_WASTED_BITS_FLAG_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_WASTED_BITS_FLAG_LEN')
FLAC__SUBFRAME_TYPE_CONSTANT_BYTE_ALIGNED_MASK = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_TYPE_CONSTANT_BYTE_ALIGNED_MASK')
FLAC__SUBFRAME_TYPE_VERBATIM_BYTE_ALIGNED_MASK = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_TYPE_VERBATIM_BYTE_ALIGNED_MASK')
FLAC__SUBFRAME_TYPE_FIXED_BYTE_ALIGNED_MASK = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_TYPE_FIXED_BYTE_ALIGNED_MASK')
FLAC__SUBFRAME_TYPE_LPC_BYTE_ALIGNED_MASK = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__SUBFRAME_TYPE_LPC_BYTE_ALIGNED_MASK')

# values for enumeration 'FLAC__ChannelAssignment'
FLAC__ChannelAssignment = c_int # enum
FLAC__ChannelAssignmentString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__ChannelAssignmentString')

# values for enumeration 'FLAC__FrameNumberType'
FLAC__FrameNumberType = c_int # enum
FLAC__FrameNumberTypeString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FrameNumberTypeString')
class N17FLAC__FrameHeader4DOT_34E(Union):
    pass
uint32_t = c_uint32
FLAC__uint32 = uint32_t
uint64_t = c_uint64
FLAC__uint64 = uint64_t
N17FLAC__FrameHeader4DOT_34E._fields_ = [
    ('frame_number', FLAC__uint32),
    ('sample_number', FLAC__uint64),
]
class FLAC__FrameHeader(Structure):
    pass
FLAC__FrameHeader._fields_ = [
    ('blocksize', c_uint),
    ('sample_rate', c_uint),
    ('channels', c_uint),
    ('channel_assignment', FLAC__ChannelAssignment),
    ('bits_per_sample', c_uint),
    ('number_type', FLAC__FrameNumberType),
    ('number', N17FLAC__FrameHeader4DOT_34E),
    ('crc', FLAC__uint8),
]
FLAC__FRAME_HEADER_SYNC = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_SYNC')
FLAC__FRAME_HEADER_SYNC_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_SYNC_LEN')
FLAC__FRAME_HEADER_RESERVED_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_RESERVED_LEN')
FLAC__FRAME_HEADER_BLOCKING_STRATEGY_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_BLOCKING_STRATEGY_LEN')
FLAC__FRAME_HEADER_BLOCK_SIZE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_BLOCK_SIZE_LEN')
FLAC__FRAME_HEADER_SAMPLE_RATE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_SAMPLE_RATE_LEN')
FLAC__FRAME_HEADER_CHANNEL_ASSIGNMENT_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_CHANNEL_ASSIGNMENT_LEN')
FLAC__FRAME_HEADER_BITS_PER_SAMPLE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_BITS_PER_SAMPLE_LEN')
FLAC__FRAME_HEADER_ZERO_PAD_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_ZERO_PAD_LEN')
FLAC__FRAME_HEADER_CRC_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_HEADER_CRC_LEN')
class FLAC__FrameFooter(Structure):
    pass
uint16_t = c_uint16
FLAC__uint16 = uint16_t
FLAC__FrameFooter._fields_ = [
    ('crc', FLAC__uint16),
]
FLAC__FRAME_FOOTER_CRC_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__FRAME_FOOTER_CRC_LEN')
class FLAC__Frame(Structure):
    pass
FLAC__Frame._fields_ = [
    ('header', FLAC__FrameHeader),
    ('subframes', FLAC__Subframe * 8),
    ('footer', FLAC__FrameFooter),
]

# values for enumeration 'FLAC__MetadataType'
FLAC__MetadataType = c_int # enum
FLAC__MetadataTypeString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__MetadataTypeString')
class FLAC__StreamMetadata_StreamInfo(Structure):
    pass
FLAC__StreamMetadata_StreamInfo._fields_ = [
    ('min_blocksize', c_uint),
    ('max_blocksize', c_uint),
    ('min_framesize', c_uint),
    ('max_framesize', c_uint),
    ('sample_rate', c_uint),
    ('channels', c_uint),
    ('bits_per_sample', c_uint),
    ('total_samples', FLAC__uint64),
    ('md5sum', FLAC__byte * 16),
]
FLAC__STREAM_METADATA_STREAMINFO_MIN_BLOCK_SIZE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_MIN_BLOCK_SIZE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_MAX_BLOCK_SIZE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_MAX_BLOCK_SIZE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_MIN_FRAME_SIZE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_MIN_FRAME_SIZE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_MAX_FRAME_SIZE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_MAX_FRAME_SIZE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_SAMPLE_RATE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_SAMPLE_RATE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_CHANNELS_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_CHANNELS_LEN')
FLAC__STREAM_METADATA_STREAMINFO_BITS_PER_SAMPLE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_BITS_PER_SAMPLE_LEN')
FLAC__STREAM_METADATA_STREAMINFO_TOTAL_SAMPLES_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_TOTAL_SAMPLES_LEN')
FLAC__STREAM_METADATA_STREAMINFO_MD5SUM_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_STREAMINFO_MD5SUM_LEN')
class FLAC__StreamMetadata_Padding(Structure):
    pass
FLAC__StreamMetadata_Padding._fields_ = [
    ('dummy', c_int),
]
class FLAC__StreamMetadata_Application(Structure):
    pass
FLAC__StreamMetadata_Application._fields_ = [
    ('id', FLAC__byte * 4),
    ('data', POINTER(FLAC__byte)),
]
FLAC__STREAM_METADATA_APPLICATION_ID_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_APPLICATION_ID_LEN')
class FLAC__StreamMetadata_SeekPoint(Structure):
    pass
FLAC__StreamMetadata_SeekPoint._fields_ = [
    ('sample_number', FLAC__uint64),
    ('stream_offset', FLAC__uint64),
    ('frame_samples', c_uint),
]
FLAC__STREAM_METADATA_SEEKPOINT_SAMPLE_NUMBER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_SEEKPOINT_SAMPLE_NUMBER_LEN')
FLAC__STREAM_METADATA_SEEKPOINT_STREAM_OFFSET_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_SEEKPOINT_STREAM_OFFSET_LEN')
FLAC__STREAM_METADATA_SEEKPOINT_FRAME_SAMPLES_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_SEEKPOINT_FRAME_SAMPLES_LEN')
FLAC__STREAM_METADATA_SEEKPOINT_PLACEHOLDER = (FLAC__uint64).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_SEEKPOINT_PLACEHOLDER')
class FLAC__StreamMetadata_SeekTable(Structure):
    pass
FLAC__StreamMetadata_SeekTable._fields_ = [
    ('num_points', c_uint),
    ('points', POINTER(FLAC__StreamMetadata_SeekPoint)),
]
class FLAC__StreamMetadata_VorbisComment_Entry(Structure):
    pass
FLAC__StreamMetadata_VorbisComment_Entry._fields_ = [
    ('length', FLAC__uint32),
    ('entry', POINTER(FLAC__byte)),
]
FLAC__STREAM_METADATA_VORBIS_COMMENT_ENTRY_LENGTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_VORBIS_COMMENT_ENTRY_LENGTH_LEN')
class FLAC__StreamMetadata_VorbisComment(Structure):
    pass
FLAC__StreamMetadata_VorbisComment._fields_ = [
    ('vendor_string', FLAC__StreamMetadata_VorbisComment_Entry),
    ('num_comments', FLAC__uint32),
    ('comments', POINTER(FLAC__StreamMetadata_VorbisComment_Entry)),
]
FLAC__STREAM_METADATA_VORBIS_COMMENT_NUM_COMMENTS_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_VORBIS_COMMENT_NUM_COMMENTS_LEN')
class FLAC__StreamMetadata_CueSheet_Index(Structure):
    pass
FLAC__StreamMetadata_CueSheet_Index._fields_ = [
    ('offset', FLAC__uint64),
    ('number', FLAC__byte),
]
FLAC__STREAM_METADATA_CUESHEET_INDEX_OFFSET_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_INDEX_OFFSET_LEN')
FLAC__STREAM_METADATA_CUESHEET_INDEX_NUMBER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_INDEX_NUMBER_LEN')
FLAC__STREAM_METADATA_CUESHEET_INDEX_RESERVED_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_INDEX_RESERVED_LEN')
class FLAC__StreamMetadata_CueSheet_Track(Structure):
    pass
FLAC__StreamMetadata_CueSheet_Track._fields_ = [
    ('offset', FLAC__uint64),
    ('number', FLAC__byte),
    ('isrc', c_char * 13),
    ('type', c_uint, 1),
    ('pre_emphasis', c_uint, 1),
    ('num_indices', FLAC__byte),
    ('indices', POINTER(FLAC__StreamMetadata_CueSheet_Index)),
]
FLAC__STREAM_METADATA_CUESHEET_TRACK_OFFSET_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_OFFSET_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_NUMBER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_NUMBER_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_ISRC_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_ISRC_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_TYPE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_TYPE_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_PRE_EMPHASIS_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_PRE_EMPHASIS_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_RESERVED_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_RESERVED_LEN')
FLAC__STREAM_METADATA_CUESHEET_TRACK_NUM_INDICES_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_TRACK_NUM_INDICES_LEN')
class FLAC__StreamMetadata_CueSheet(Structure):
    pass
FLAC__bool = c_int
FLAC__StreamMetadata_CueSheet._fields_ = [
    ('media_catalog_number', c_char * 129),
    ('lead_in', FLAC__uint64),
    ('is_cd', FLAC__bool),
    ('num_tracks', c_uint),
    ('tracks', POINTER(FLAC__StreamMetadata_CueSheet_Track)),
]
FLAC__STREAM_METADATA_CUESHEET_MEDIA_CATALOG_NUMBER_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_MEDIA_CATALOG_NUMBER_LEN')
FLAC__STREAM_METADATA_CUESHEET_LEAD_IN_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_LEAD_IN_LEN')
FLAC__STREAM_METADATA_CUESHEET_IS_CD_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_IS_CD_LEN')
FLAC__STREAM_METADATA_CUESHEET_RESERVED_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_RESERVED_LEN')
FLAC__STREAM_METADATA_CUESHEET_NUM_TRACKS_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_CUESHEET_NUM_TRACKS_LEN')

# values for enumeration 'FLAC__StreamMetadata_Picture_Type'
FLAC__StreamMetadata_Picture_Type = c_int # enum
FLAC__StreamMetadata_Picture_TypeString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamMetadata_Picture_TypeString')
class FLAC__StreamMetadata_Picture(Structure):
    pass
FLAC__StreamMetadata_Picture._fields_ = [
    ('type', FLAC__StreamMetadata_Picture_Type),
    ('mime_type', STRING),
    ('description', POINTER(FLAC__byte)),
    ('width', FLAC__uint32),
    ('height', FLAC__uint32),
    ('depth', FLAC__uint32),
    ('colors', FLAC__uint32),
    ('data_length', FLAC__uint32),
    ('data', POINTER(FLAC__byte)),
]
FLAC__STREAM_METADATA_PICTURE_TYPE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_TYPE_LEN')
FLAC__STREAM_METADATA_PICTURE_MIME_TYPE_LENGTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_MIME_TYPE_LENGTH_LEN')
FLAC__STREAM_METADATA_PICTURE_DESCRIPTION_LENGTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_DESCRIPTION_LENGTH_LEN')
FLAC__STREAM_METADATA_PICTURE_WIDTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_WIDTH_LEN')
FLAC__STREAM_METADATA_PICTURE_HEIGHT_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_HEIGHT_LEN')
FLAC__STREAM_METADATA_PICTURE_DEPTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_DEPTH_LEN')
FLAC__STREAM_METADATA_PICTURE_COLORS_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_COLORS_LEN')
FLAC__STREAM_METADATA_PICTURE_DATA_LENGTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_PICTURE_DATA_LENGTH_LEN')
class FLAC__StreamMetadata_Unknown(Structure):
    pass
FLAC__StreamMetadata_Unknown._fields_ = [
    ('data', POINTER(FLAC__byte)),
]
class N20FLAC__StreamMetadata4DOT_52E(Union):
    pass
N20FLAC__StreamMetadata4DOT_52E._fields_ = [
    ('stream_info', FLAC__StreamMetadata_StreamInfo),
    ('padding', FLAC__StreamMetadata_Padding),
    ('application', FLAC__StreamMetadata_Application),
    ('seek_table', FLAC__StreamMetadata_SeekTable),
    ('vorbis_comment', FLAC__StreamMetadata_VorbisComment),
    ('cue_sheet', FLAC__StreamMetadata_CueSheet),
    ('picture', FLAC__StreamMetadata_Picture),
    ('unknown', FLAC__StreamMetadata_Unknown),
]
class FLAC__StreamMetadata(Structure):
    pass
FLAC__StreamMetadata._fields_ = [
    ('type', FLAC__MetadataType),
    ('is_last', FLAC__bool),
    ('length', c_uint),
    ('data', N20FLAC__StreamMetadata4DOT_52E),
]
FLAC__STREAM_METADATA_IS_LAST_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_IS_LAST_LEN')
FLAC__STREAM_METADATA_TYPE_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_TYPE_LEN')
FLAC__STREAM_METADATA_LENGTH_LEN = (c_uint).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__STREAM_METADATA_LENGTH_LEN')
FLAC__format_sample_rate_is_valid = _libraries['/usr/lib/libFLAC.so'].FLAC__format_sample_rate_is_valid
FLAC__format_sample_rate_is_valid.restype = FLAC__bool
FLAC__format_sample_rate_is_valid.argtypes = [c_uint]
FLAC__format_blocksize_is_subset = _libraries['/usr/lib/libFLAC.so'].FLAC__format_blocksize_is_subset
FLAC__format_blocksize_is_subset.restype = FLAC__bool
FLAC__format_blocksize_is_subset.argtypes = [c_uint, c_uint]
FLAC__format_sample_rate_is_subset = _libraries['/usr/lib/libFLAC.so'].FLAC__format_sample_rate_is_subset
FLAC__format_sample_rate_is_subset.restype = FLAC__bool
FLAC__format_sample_rate_is_subset.argtypes = [c_uint]
FLAC__format_vorbiscomment_entry_name_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_vorbiscomment_entry_name_is_legal
FLAC__format_vorbiscomment_entry_name_is_legal.restype = FLAC__bool
FLAC__format_vorbiscomment_entry_name_is_legal.argtypes = [STRING]
FLAC__format_vorbiscomment_entry_value_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_vorbiscomment_entry_value_is_legal
FLAC__format_vorbiscomment_entry_value_is_legal.restype = FLAC__bool
FLAC__format_vorbiscomment_entry_value_is_legal.argtypes = [POINTER(FLAC__byte), c_uint]
FLAC__format_vorbiscomment_entry_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_vorbiscomment_entry_is_legal
FLAC__format_vorbiscomment_entry_is_legal.restype = FLAC__bool
FLAC__format_vorbiscomment_entry_is_legal.argtypes = [POINTER(FLAC__byte), c_uint]
FLAC__format_seektable_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_seektable_is_legal
FLAC__format_seektable_is_legal.restype = FLAC__bool
FLAC__format_seektable_is_legal.argtypes = [POINTER(FLAC__StreamMetadata_SeekTable)]
FLAC__format_seektable_sort = _libraries['/usr/lib/libFLAC.so'].FLAC__format_seektable_sort
FLAC__format_seektable_sort.restype = c_uint
FLAC__format_seektable_sort.argtypes = [POINTER(FLAC__StreamMetadata_SeekTable)]
FLAC__format_cuesheet_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_cuesheet_is_legal
FLAC__format_cuesheet_is_legal.restype = FLAC__bool
FLAC__format_cuesheet_is_legal.argtypes = [POINTER(FLAC__StreamMetadata_CueSheet), FLAC__bool, POINTER(STRING)]
FLAC__format_picture_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__format_picture_is_legal
FLAC__format_picture_is_legal.restype = FLAC__bool
FLAC__format_picture_is_legal.argtypes = [POINTER(FLAC__StreamMetadata_Picture), POINTER(STRING)]
FLAC__metadata_get_streaminfo = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_get_streaminfo
FLAC__metadata_get_streaminfo.restype = FLAC__bool
FLAC__metadata_get_streaminfo.argtypes = [STRING, POINTER(FLAC__StreamMetadata)]
FLAC__metadata_get_tags = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_get_tags
FLAC__metadata_get_tags.restype = FLAC__bool
FLAC__metadata_get_tags.argtypes = [STRING, POINTER(POINTER(FLAC__StreamMetadata))]
FLAC__metadata_get_cuesheet = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_get_cuesheet
FLAC__metadata_get_cuesheet.restype = FLAC__bool
FLAC__metadata_get_cuesheet.argtypes = [STRING, POINTER(POINTER(FLAC__StreamMetadata))]
FLAC__metadata_get_picture = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_get_picture
FLAC__metadata_get_picture.restype = FLAC__bool
FLAC__metadata_get_picture.argtypes = [STRING, POINTER(POINTER(FLAC__StreamMetadata)), FLAC__StreamMetadata_Picture_Type, STRING, POINTER(FLAC__byte), c_uint, c_uint, c_uint, c_uint]
class FLAC__Metadata_SimpleIterator(Structure):
    pass
FLAC__Metadata_SimpleIterator._fields_ = [
]

# values for enumeration 'FLAC__Metadata_SimpleIteratorStatus'
FLAC__Metadata_SimpleIteratorStatus = c_int # enum
FLAC__Metadata_SimpleIteratorStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__Metadata_SimpleIteratorStatusString')
FLAC__metadata_simple_iterator_new = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_new
FLAC__metadata_simple_iterator_new.restype = POINTER(FLAC__Metadata_SimpleIterator)
FLAC__metadata_simple_iterator_new.argtypes = []
FLAC__metadata_simple_iterator_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_delete
FLAC__metadata_simple_iterator_delete.restype = None
FLAC__metadata_simple_iterator_delete.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_status = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_status
FLAC__metadata_simple_iterator_status.restype = FLAC__Metadata_SimpleIteratorStatus
FLAC__metadata_simple_iterator_status.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_init = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_init
FLAC__metadata_simple_iterator_init.restype = FLAC__bool
FLAC__metadata_simple_iterator_init.argtypes = [POINTER(FLAC__Metadata_SimpleIterator), STRING, FLAC__bool, FLAC__bool]
FLAC__metadata_simple_iterator_is_writable = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_is_writable
FLAC__metadata_simple_iterator_is_writable.restype = FLAC__bool
FLAC__metadata_simple_iterator_is_writable.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_next = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_next
FLAC__metadata_simple_iterator_next.restype = FLAC__bool
FLAC__metadata_simple_iterator_next.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_prev = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_prev
FLAC__metadata_simple_iterator_prev.restype = FLAC__bool
FLAC__metadata_simple_iterator_prev.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_is_last = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_is_last
FLAC__metadata_simple_iterator_is_last.restype = FLAC__bool
FLAC__metadata_simple_iterator_is_last.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
off_t = __off_t
FLAC__metadata_simple_iterator_get_block_offset = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_get_block_offset
FLAC__metadata_simple_iterator_get_block_offset.restype = off_t
FLAC__metadata_simple_iterator_get_block_offset.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_get_block_type = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_get_block_type
FLAC__metadata_simple_iterator_get_block_type.restype = FLAC__MetadataType
FLAC__metadata_simple_iterator_get_block_type.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_get_block_length = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_get_block_length
FLAC__metadata_simple_iterator_get_block_length.restype = c_uint
FLAC__metadata_simple_iterator_get_block_length.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_get_application_id = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_get_application_id
FLAC__metadata_simple_iterator_get_application_id.restype = FLAC__bool
FLAC__metadata_simple_iterator_get_application_id.argtypes = [POINTER(FLAC__Metadata_SimpleIterator), POINTER(FLAC__byte)]
FLAC__metadata_simple_iterator_get_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_get_block
FLAC__metadata_simple_iterator_get_block.restype = POINTER(FLAC__StreamMetadata)
FLAC__metadata_simple_iterator_get_block.argtypes = [POINTER(FLAC__Metadata_SimpleIterator)]
FLAC__metadata_simple_iterator_set_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_set_block
FLAC__metadata_simple_iterator_set_block.restype = FLAC__bool
FLAC__metadata_simple_iterator_set_block.argtypes = [POINTER(FLAC__Metadata_SimpleIterator), POINTER(FLAC__StreamMetadata), FLAC__bool]
FLAC__metadata_simple_iterator_insert_block_after = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_insert_block_after
FLAC__metadata_simple_iterator_insert_block_after.restype = FLAC__bool
FLAC__metadata_simple_iterator_insert_block_after.argtypes = [POINTER(FLAC__Metadata_SimpleIterator), POINTER(FLAC__StreamMetadata), FLAC__bool]
FLAC__metadata_simple_iterator_delete_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_simple_iterator_delete_block
FLAC__metadata_simple_iterator_delete_block.restype = FLAC__bool
FLAC__metadata_simple_iterator_delete_block.argtypes = [POINTER(FLAC__Metadata_SimpleIterator), FLAC__bool]
class FLAC__Metadata_Chain(Structure):
    pass
FLAC__Metadata_Chain._fields_ = [
]
class FLAC__Metadata_Iterator(Structure):
    pass
FLAC__Metadata_Iterator._fields_ = [
]

# values for enumeration 'FLAC__Metadata_ChainStatus'
FLAC__Metadata_ChainStatus = c_int # enum
FLAC__Metadata_ChainStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__Metadata_ChainStatusString')
FLAC__metadata_chain_new = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_new
FLAC__metadata_chain_new.restype = POINTER(FLAC__Metadata_Chain)
FLAC__metadata_chain_new.argtypes = []
FLAC__metadata_chain_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_delete
FLAC__metadata_chain_delete.restype = None
FLAC__metadata_chain_delete.argtypes = [POINTER(FLAC__Metadata_Chain)]
FLAC__metadata_chain_status = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_status
FLAC__metadata_chain_status.restype = FLAC__Metadata_ChainStatus
FLAC__metadata_chain_status.argtypes = [POINTER(FLAC__Metadata_Chain)]
FLAC__metadata_chain_read = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_read
FLAC__metadata_chain_read.restype = FLAC__bool
FLAC__metadata_chain_read.argtypes = [POINTER(FLAC__Metadata_Chain), STRING]
FLAC__metadata_chain_read_ogg = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_read_ogg
FLAC__metadata_chain_read_ogg.restype = FLAC__bool
FLAC__metadata_chain_read_ogg.argtypes = [POINTER(FLAC__Metadata_Chain), STRING]
FLAC__metadata_chain_read_with_callbacks = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_read_with_callbacks
FLAC__metadata_chain_read_with_callbacks.restype = FLAC__bool
FLAC__metadata_chain_read_with_callbacks.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__IOHandle, FLAC__IOCallbacks]
FLAC__metadata_chain_read_ogg_with_callbacks = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_read_ogg_with_callbacks
FLAC__metadata_chain_read_ogg_with_callbacks.restype = FLAC__bool
FLAC__metadata_chain_read_ogg_with_callbacks.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__IOHandle, FLAC__IOCallbacks]
FLAC__metadata_chain_check_if_tempfile_needed = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_check_if_tempfile_needed
FLAC__metadata_chain_check_if_tempfile_needed.restype = FLAC__bool
FLAC__metadata_chain_check_if_tempfile_needed.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__bool]
FLAC__metadata_chain_write = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_write
FLAC__metadata_chain_write.restype = FLAC__bool
FLAC__metadata_chain_write.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__bool, FLAC__bool]
FLAC__metadata_chain_write_with_callbacks = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_write_with_callbacks
FLAC__metadata_chain_write_with_callbacks.restype = FLAC__bool
FLAC__metadata_chain_write_with_callbacks.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__bool, FLAC__IOHandle, FLAC__IOCallbacks]
FLAC__metadata_chain_write_with_callbacks_and_tempfile = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_write_with_callbacks_and_tempfile
FLAC__metadata_chain_write_with_callbacks_and_tempfile.restype = FLAC__bool
FLAC__metadata_chain_write_with_callbacks_and_tempfile.argtypes = [POINTER(FLAC__Metadata_Chain), FLAC__bool, FLAC__IOHandle, FLAC__IOCallbacks, FLAC__IOHandle, FLAC__IOCallbacks]
FLAC__metadata_chain_merge_padding = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_merge_padding
FLAC__metadata_chain_merge_padding.restype = None
FLAC__metadata_chain_merge_padding.argtypes = [POINTER(FLAC__Metadata_Chain)]
FLAC__metadata_chain_sort_padding = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_chain_sort_padding
FLAC__metadata_chain_sort_padding.restype = None
FLAC__metadata_chain_sort_padding.argtypes = [POINTER(FLAC__Metadata_Chain)]
FLAC__metadata_iterator_new = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_new
FLAC__metadata_iterator_new.restype = POINTER(FLAC__Metadata_Iterator)
FLAC__metadata_iterator_new.argtypes = []
FLAC__metadata_iterator_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_delete
FLAC__metadata_iterator_delete.restype = None
FLAC__metadata_iterator_delete.argtypes = [POINTER(FLAC__Metadata_Iterator)]
FLAC__metadata_iterator_init = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_init
FLAC__metadata_iterator_init.restype = None
FLAC__metadata_iterator_init.argtypes = [POINTER(FLAC__Metadata_Iterator), POINTER(FLAC__Metadata_Chain)]
FLAC__metadata_iterator_next = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_next
FLAC__metadata_iterator_next.restype = FLAC__bool
FLAC__metadata_iterator_next.argtypes = [POINTER(FLAC__Metadata_Iterator)]
FLAC__metadata_iterator_prev = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_prev
FLAC__metadata_iterator_prev.restype = FLAC__bool
FLAC__metadata_iterator_prev.argtypes = [POINTER(FLAC__Metadata_Iterator)]
FLAC__metadata_iterator_get_block_type = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_get_block_type
FLAC__metadata_iterator_get_block_type.restype = FLAC__MetadataType
FLAC__metadata_iterator_get_block_type.argtypes = [POINTER(FLAC__Metadata_Iterator)]
FLAC__metadata_iterator_get_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_get_block
FLAC__metadata_iterator_get_block.restype = POINTER(FLAC__StreamMetadata)
FLAC__metadata_iterator_get_block.argtypes = [POINTER(FLAC__Metadata_Iterator)]
FLAC__metadata_iterator_set_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_set_block
FLAC__metadata_iterator_set_block.restype = FLAC__bool
FLAC__metadata_iterator_set_block.argtypes = [POINTER(FLAC__Metadata_Iterator), POINTER(FLAC__StreamMetadata)]
FLAC__metadata_iterator_delete_block = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_delete_block
FLAC__metadata_iterator_delete_block.restype = FLAC__bool
FLAC__metadata_iterator_delete_block.argtypes = [POINTER(FLAC__Metadata_Iterator), FLAC__bool]
FLAC__metadata_iterator_insert_block_before = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_insert_block_before
FLAC__metadata_iterator_insert_block_before.restype = FLAC__bool
FLAC__metadata_iterator_insert_block_before.argtypes = [POINTER(FLAC__Metadata_Iterator), POINTER(FLAC__StreamMetadata)]
FLAC__metadata_iterator_insert_block_after = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_iterator_insert_block_after
FLAC__metadata_iterator_insert_block_after.restype = FLAC__bool
FLAC__metadata_iterator_insert_block_after.argtypes = [POINTER(FLAC__Metadata_Iterator), POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_new = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_new
FLAC__metadata_object_new.restype = POINTER(FLAC__StreamMetadata)
FLAC__metadata_object_new.argtypes = [FLAC__MetadataType]
FLAC__metadata_object_clone = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_clone
FLAC__metadata_object_clone.restype = POINTER(FLAC__StreamMetadata)
FLAC__metadata_object_clone.argtypes = [POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_delete
FLAC__metadata_object_delete.restype = None
FLAC__metadata_object_delete.argtypes = [POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_is_equal = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_is_equal
FLAC__metadata_object_is_equal.restype = FLAC__bool
FLAC__metadata_object_is_equal.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_application_set_data = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_application_set_data
FLAC__metadata_object_application_set_data.restype = FLAC__bool
FLAC__metadata_object_application_set_data.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(FLAC__byte), c_uint, FLAC__bool]
FLAC__metadata_object_seektable_resize_points = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_resize_points
FLAC__metadata_object_seektable_resize_points.restype = FLAC__bool
FLAC__metadata_object_seektable_resize_points.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_seektable_set_point = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_set_point
FLAC__metadata_object_seektable_set_point.restype = None
FLAC__metadata_object_seektable_set_point.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__StreamMetadata_SeekPoint]
FLAC__metadata_object_seektable_insert_point = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_insert_point
FLAC__metadata_object_seektable_insert_point.restype = FLAC__bool
FLAC__metadata_object_seektable_insert_point.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__StreamMetadata_SeekPoint]
FLAC__metadata_object_seektable_delete_point = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_delete_point
FLAC__metadata_object_seektable_delete_point.restype = FLAC__bool
FLAC__metadata_object_seektable_delete_point.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_seektable_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_is_legal
FLAC__metadata_object_seektable_is_legal.restype = FLAC__bool
FLAC__metadata_object_seektable_is_legal.argtypes = [POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_seektable_template_append_placeholders = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_append_placeholders
FLAC__metadata_object_seektable_template_append_placeholders.restype = FLAC__bool
FLAC__metadata_object_seektable_template_append_placeholders.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_seektable_template_append_point = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_append_point
FLAC__metadata_object_seektable_template_append_point.restype = FLAC__bool
FLAC__metadata_object_seektable_template_append_point.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__uint64]
FLAC__metadata_object_seektable_template_append_points = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_append_points
FLAC__metadata_object_seektable_template_append_points.restype = FLAC__bool
FLAC__metadata_object_seektable_template_append_points.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(FLAC__uint64), c_uint]
FLAC__metadata_object_seektable_template_append_spaced_points = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_append_spaced_points
FLAC__metadata_object_seektable_template_append_spaced_points.restype = FLAC__bool
FLAC__metadata_object_seektable_template_append_spaced_points.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__uint64]
FLAC__metadata_object_seektable_template_append_spaced_points_by_samples = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_append_spaced_points_by_samples
FLAC__metadata_object_seektable_template_append_spaced_points_by_samples.restype = FLAC__bool
FLAC__metadata_object_seektable_template_append_spaced_points_by_samples.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__uint64]
FLAC__metadata_object_seektable_template_sort = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_seektable_template_sort
FLAC__metadata_object_seektable_template_sort.restype = FLAC__bool
FLAC__metadata_object_seektable_template_sort.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__bool]
FLAC__metadata_object_vorbiscomment_set_vendor_string = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_set_vendor_string
FLAC__metadata_object_vorbiscomment_set_vendor_string.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_set_vendor_string.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__StreamMetadata_VorbisComment_Entry, FLAC__bool]
FLAC__metadata_object_vorbiscomment_resize_comments = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_resize_comments
FLAC__metadata_object_vorbiscomment_resize_comments.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_resize_comments.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_vorbiscomment_set_comment = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_set_comment
FLAC__metadata_object_vorbiscomment_set_comment.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_set_comment.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__StreamMetadata_VorbisComment_Entry, FLAC__bool]
FLAC__metadata_object_vorbiscomment_insert_comment = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_insert_comment
FLAC__metadata_object_vorbiscomment_insert_comment.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_insert_comment.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, FLAC__StreamMetadata_VorbisComment_Entry, FLAC__bool]
FLAC__metadata_object_vorbiscomment_append_comment = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_append_comment
FLAC__metadata_object_vorbiscomment_append_comment.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_append_comment.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__StreamMetadata_VorbisComment_Entry, FLAC__bool]
FLAC__metadata_object_vorbiscomment_replace_comment = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_replace_comment
FLAC__metadata_object_vorbiscomment_replace_comment.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_replace_comment.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__StreamMetadata_VorbisComment_Entry, FLAC__bool, FLAC__bool]
FLAC__metadata_object_vorbiscomment_delete_comment = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_delete_comment
FLAC__metadata_object_vorbiscomment_delete_comment.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_delete_comment.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_vorbiscomment_entry_from_name_value_pair = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_entry_from_name_value_pair
FLAC__metadata_object_vorbiscomment_entry_from_name_value_pair.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_entry_from_name_value_pair.argtypes = [POINTER(FLAC__StreamMetadata_VorbisComment_Entry), STRING, STRING]
FLAC__metadata_object_vorbiscomment_entry_to_name_value_pair = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_entry_to_name_value_pair
FLAC__metadata_object_vorbiscomment_entry_to_name_value_pair.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_entry_to_name_value_pair.argtypes = [FLAC__StreamMetadata_VorbisComment_Entry, POINTER(STRING), POINTER(STRING)]
FLAC__metadata_object_vorbiscomment_entry_matches = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_entry_matches
FLAC__metadata_object_vorbiscomment_entry_matches.restype = FLAC__bool
FLAC__metadata_object_vorbiscomment_entry_matches.argtypes = [FLAC__StreamMetadata_VorbisComment_Entry, STRING, c_uint]
FLAC__metadata_object_vorbiscomment_find_entry_from = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_find_entry_from
FLAC__metadata_object_vorbiscomment_find_entry_from.restype = c_int
FLAC__metadata_object_vorbiscomment_find_entry_from.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, STRING]
FLAC__metadata_object_vorbiscomment_remove_entry_matching = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_remove_entry_matching
FLAC__metadata_object_vorbiscomment_remove_entry_matching.restype = c_int
FLAC__metadata_object_vorbiscomment_remove_entry_matching.argtypes = [POINTER(FLAC__StreamMetadata), STRING]
FLAC__metadata_object_vorbiscomment_remove_entries_matching = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_vorbiscomment_remove_entries_matching
FLAC__metadata_object_vorbiscomment_remove_entries_matching.restype = c_int
FLAC__metadata_object_vorbiscomment_remove_entries_matching.argtypes = [POINTER(FLAC__StreamMetadata), STRING]
FLAC__metadata_object_cuesheet_track_new = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_new
FLAC__metadata_object_cuesheet_track_new.restype = POINTER(FLAC__StreamMetadata_CueSheet_Track)
FLAC__metadata_object_cuesheet_track_new.argtypes = []
FLAC__metadata_object_cuesheet_track_clone = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_clone
FLAC__metadata_object_cuesheet_track_clone.restype = POINTER(FLAC__StreamMetadata_CueSheet_Track)
FLAC__metadata_object_cuesheet_track_clone.argtypes = [POINTER(FLAC__StreamMetadata_CueSheet_Track)]
FLAC__metadata_object_cuesheet_track_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_delete
FLAC__metadata_object_cuesheet_track_delete.restype = None
FLAC__metadata_object_cuesheet_track_delete.argtypes = [POINTER(FLAC__StreamMetadata_CueSheet_Track)]
FLAC__metadata_object_cuesheet_track_resize_indices = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_resize_indices
FLAC__metadata_object_cuesheet_track_resize_indices.restype = FLAC__bool
FLAC__metadata_object_cuesheet_track_resize_indices.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, c_uint]
FLAC__metadata_object_cuesheet_track_insert_index = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_insert_index
FLAC__metadata_object_cuesheet_track_insert_index.restype = FLAC__bool
FLAC__metadata_object_cuesheet_track_insert_index.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, c_uint, FLAC__StreamMetadata_CueSheet_Index]
FLAC__metadata_object_cuesheet_track_insert_blank_index = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_insert_blank_index
FLAC__metadata_object_cuesheet_track_insert_blank_index.restype = FLAC__bool
FLAC__metadata_object_cuesheet_track_insert_blank_index.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, c_uint]
FLAC__metadata_object_cuesheet_track_delete_index = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_track_delete_index
FLAC__metadata_object_cuesheet_track_delete_index.restype = FLAC__bool
FLAC__metadata_object_cuesheet_track_delete_index.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, c_uint]
FLAC__metadata_object_cuesheet_resize_tracks = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_resize_tracks
FLAC__metadata_object_cuesheet_resize_tracks.restype = FLAC__bool
FLAC__metadata_object_cuesheet_resize_tracks.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_cuesheet_set_track = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_set_track
FLAC__metadata_object_cuesheet_set_track.restype = FLAC__bool
FLAC__metadata_object_cuesheet_set_track.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, POINTER(FLAC__StreamMetadata_CueSheet_Track), FLAC__bool]
FLAC__metadata_object_cuesheet_insert_track = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_insert_track
FLAC__metadata_object_cuesheet_insert_track.restype = FLAC__bool
FLAC__metadata_object_cuesheet_insert_track.argtypes = [POINTER(FLAC__StreamMetadata), c_uint, POINTER(FLAC__StreamMetadata_CueSheet_Track), FLAC__bool]
FLAC__metadata_object_cuesheet_insert_blank_track = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_insert_blank_track
FLAC__metadata_object_cuesheet_insert_blank_track.restype = FLAC__bool
FLAC__metadata_object_cuesheet_insert_blank_track.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_cuesheet_delete_track = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_delete_track
FLAC__metadata_object_cuesheet_delete_track.restype = FLAC__bool
FLAC__metadata_object_cuesheet_delete_track.argtypes = [POINTER(FLAC__StreamMetadata), c_uint]
FLAC__metadata_object_cuesheet_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_is_legal
FLAC__metadata_object_cuesheet_is_legal.restype = FLAC__bool
FLAC__metadata_object_cuesheet_is_legal.argtypes = [POINTER(FLAC__StreamMetadata), FLAC__bool, POINTER(STRING)]
FLAC__metadata_object_cuesheet_calculate_cddb_id = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_cuesheet_calculate_cddb_id
FLAC__metadata_object_cuesheet_calculate_cddb_id.restype = FLAC__uint32
FLAC__metadata_object_cuesheet_calculate_cddb_id.argtypes = [POINTER(FLAC__StreamMetadata)]
FLAC__metadata_object_picture_set_mime_type = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_picture_set_mime_type
FLAC__metadata_object_picture_set_mime_type.restype = FLAC__bool
FLAC__metadata_object_picture_set_mime_type.argtypes = [POINTER(FLAC__StreamMetadata), STRING, FLAC__bool]
FLAC__metadata_object_picture_set_description = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_picture_set_description
FLAC__metadata_object_picture_set_description.restype = FLAC__bool
FLAC__metadata_object_picture_set_description.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(FLAC__byte), FLAC__bool]
FLAC__metadata_object_picture_set_data = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_picture_set_data
FLAC__metadata_object_picture_set_data.restype = FLAC__bool
FLAC__metadata_object_picture_set_data.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(FLAC__byte), FLAC__uint32, FLAC__bool]
FLAC__metadata_object_picture_is_legal = _libraries['/usr/lib/libFLAC.so'].FLAC__metadata_object_picture_is_legal
FLAC__metadata_object_picture_is_legal.restype = FLAC__bool
FLAC__metadata_object_picture_is_legal.argtypes = [POINTER(FLAC__StreamMetadata), POINTER(STRING)]
int8_t = c_int8
FLAC__int8 = int8_t
int16_t = c_int16
FLAC__int16 = int16_t

# values for enumeration 'FLAC__StreamDecoderState'
FLAC__StreamDecoderState = c_int # enum
FLAC__StreamDecoderStateString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderStateString')

# values for enumeration 'FLAC__StreamDecoderInitStatus'
FLAC__StreamDecoderInitStatus = c_int # enum
FLAC__StreamDecoderInitStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderInitStatusString')

# values for enumeration 'FLAC__StreamDecoderReadStatus'
FLAC__StreamDecoderReadStatus = c_int # enum
FLAC__StreamDecoderReadStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderReadStatusString')

# values for enumeration 'FLAC__StreamDecoderSeekStatus'
FLAC__StreamDecoderSeekStatus = c_int # enum
FLAC__StreamDecoderSeekStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderSeekStatusString')

# values for enumeration 'FLAC__StreamDecoderTellStatus'
FLAC__StreamDecoderTellStatus = c_int # enum
FLAC__StreamDecoderTellStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderTellStatusString')

# values for enumeration 'FLAC__StreamDecoderLengthStatus'
FLAC__StreamDecoderLengthStatus = c_int # enum
FLAC__StreamDecoderLengthStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderLengthStatusString')

# values for enumeration 'FLAC__StreamDecoderWriteStatus'
FLAC__StreamDecoderWriteStatus = c_int # enum
FLAC__StreamDecoderWriteStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderWriteStatusString')

# values for enumeration 'FLAC__StreamDecoderErrorStatus'
FLAC__StreamDecoderErrorStatus = c_int # enum
FLAC__StreamDecoderErrorStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamDecoderErrorStatusString')
class FLAC__StreamDecoderProtected(Structure):
    pass
FLAC__StreamDecoderProtected._fields_ = [
]
class FLAC__StreamDecoderPrivate(Structure):
    pass
FLAC__StreamDecoderPrivate._fields_ = [
]
class FLAC__StreamDecoder(Structure):
    pass
FLAC__StreamDecoder._fields_ = [
    ('protected_', POINTER(FLAC__StreamDecoderProtected)),
    ('private_', POINTER(FLAC__StreamDecoderPrivate)),
]
FLAC__StreamDecoderReadCallback = CFUNCTYPE(FLAC__StreamDecoderReadStatus, POINTER(FLAC__StreamDecoder), POINTER(FLAC__byte), POINTER(size_t), c_void_p)
FLAC__StreamDecoderSeekCallback = CFUNCTYPE(FLAC__StreamDecoderSeekStatus, POINTER(FLAC__StreamDecoder), FLAC__uint64, c_void_p)
FLAC__StreamDecoderTellCallback = CFUNCTYPE(FLAC__StreamDecoderTellStatus, POINTER(FLAC__StreamDecoder), POINTER(FLAC__uint64), c_void_p)
FLAC__StreamDecoderLengthCallback = CFUNCTYPE(FLAC__StreamDecoderLengthStatus, POINTER(FLAC__StreamDecoder), POINTER(FLAC__uint64), c_void_p)
FLAC__StreamDecoderEofCallback = CFUNCTYPE(FLAC__bool, POINTER(FLAC__StreamDecoder), c_void_p)
FLAC__StreamDecoderWriteCallback = CFUNCTYPE(FLAC__StreamDecoderWriteStatus, POINTER(FLAC__StreamDecoder), POINTER(FLAC__Frame), POINTER(POINTER(FLAC__int32)), c_void_p)
FLAC__StreamDecoderMetadataCallback = CFUNCTYPE(None, POINTER(FLAC__StreamDecoder), POINTER(FLAC__StreamMetadata), c_void_p)
FLAC__StreamDecoderErrorCallback = CFUNCTYPE(None, POINTER(FLAC__StreamDecoder), FLAC__StreamDecoderErrorStatus, c_void_p)
FLAC__stream_decoder_new = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_new
FLAC__stream_decoder_new.restype = POINTER(FLAC__StreamDecoder)
FLAC__stream_decoder_new.argtypes = []
FLAC__stream_decoder_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_delete
FLAC__stream_decoder_delete.restype = None
FLAC__stream_decoder_delete.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_set_ogg_serial_number = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_ogg_serial_number
FLAC__stream_decoder_set_ogg_serial_number.restype = FLAC__bool
FLAC__stream_decoder_set_ogg_serial_number.argtypes = [POINTER(FLAC__StreamDecoder), c_long]
FLAC__stream_decoder_set_md5_checking = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_md5_checking
FLAC__stream_decoder_set_md5_checking.restype = FLAC__bool
FLAC__stream_decoder_set_md5_checking.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__bool]
FLAC__stream_decoder_set_metadata_respond = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_respond
FLAC__stream_decoder_set_metadata_respond.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_respond.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__MetadataType]
FLAC__stream_decoder_set_metadata_respond_application = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_respond_application
FLAC__stream_decoder_set_metadata_respond_application.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_respond_application.argtypes = [POINTER(FLAC__StreamDecoder), POINTER(FLAC__byte)]
FLAC__stream_decoder_set_metadata_respond_all = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_respond_all
FLAC__stream_decoder_set_metadata_respond_all.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_respond_all.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_set_metadata_ignore = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_ignore
FLAC__stream_decoder_set_metadata_ignore.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_ignore.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__MetadataType]
FLAC__stream_decoder_set_metadata_ignore_application = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_ignore_application
FLAC__stream_decoder_set_metadata_ignore_application.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_ignore_application.argtypes = [POINTER(FLAC__StreamDecoder), POINTER(FLAC__byte)]
FLAC__stream_decoder_set_metadata_ignore_all = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_set_metadata_ignore_all
FLAC__stream_decoder_set_metadata_ignore_all.restype = FLAC__bool
FLAC__stream_decoder_set_metadata_ignore_all.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_state = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_state
FLAC__stream_decoder_get_state.restype = FLAC__StreamDecoderState
FLAC__stream_decoder_get_state.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_resolved_state_string = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_resolved_state_string
FLAC__stream_decoder_get_resolved_state_string.restype = STRING
FLAC__stream_decoder_get_resolved_state_string.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_md5_checking = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_md5_checking
FLAC__stream_decoder_get_md5_checking.restype = FLAC__bool
FLAC__stream_decoder_get_md5_checking.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_total_samples = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_total_samples
FLAC__stream_decoder_get_total_samples.restype = FLAC__uint64
FLAC__stream_decoder_get_total_samples.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_channels = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_channels
FLAC__stream_decoder_get_channels.restype = c_uint
FLAC__stream_decoder_get_channels.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_channel_assignment = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_channel_assignment
FLAC__stream_decoder_get_channel_assignment.restype = FLAC__ChannelAssignment
FLAC__stream_decoder_get_channel_assignment.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_bits_per_sample = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_bits_per_sample
FLAC__stream_decoder_get_bits_per_sample.restype = c_uint
FLAC__stream_decoder_get_bits_per_sample.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_sample_rate = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_sample_rate
FLAC__stream_decoder_get_sample_rate.restype = c_uint
FLAC__stream_decoder_get_sample_rate.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_blocksize = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_blocksize
FLAC__stream_decoder_get_blocksize.restype = c_uint
FLAC__stream_decoder_get_blocksize.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_get_decode_position = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_get_decode_position
FLAC__stream_decoder_get_decode_position.restype = FLAC__bool
FLAC__stream_decoder_get_decode_position.argtypes = [POINTER(FLAC__StreamDecoder), POINTER(FLAC__uint64)]
FLAC__stream_decoder_init_stream = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_stream
FLAC__stream_decoder_init_stream.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_stream.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__StreamDecoderReadCallback, FLAC__StreamDecoderSeekCallback, FLAC__StreamDecoderTellCallback, FLAC__StreamDecoderLengthCallback, FLAC__StreamDecoderEofCallback, FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FLAC__stream_decoder_init_ogg_stream = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_ogg_stream
FLAC__stream_decoder_init_ogg_stream.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_ogg_stream.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__StreamDecoderReadCallback, FLAC__StreamDecoderSeekCallback, FLAC__StreamDecoderTellCallback, FLAC__StreamDecoderLengthCallback, FLAC__StreamDecoderEofCallback, FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FILE = _IO_FILE
FLAC__stream_decoder_init_FILE = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_FILE
FLAC__stream_decoder_init_FILE.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_FILE.argtypes = [POINTER(FLAC__StreamDecoder), POINTER(FILE), FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FLAC__stream_decoder_init_ogg_FILE = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_ogg_FILE
FLAC__stream_decoder_init_ogg_FILE.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_ogg_FILE.argtypes = [POINTER(FLAC__StreamDecoder), POINTER(FILE), FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FLAC__stream_decoder_init_file = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_file
FLAC__stream_decoder_init_file.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_file.argtypes = [POINTER(FLAC__StreamDecoder), STRING, FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FLAC__stream_decoder_init_ogg_file = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_init_ogg_file
FLAC__stream_decoder_init_ogg_file.restype = FLAC__StreamDecoderInitStatus
FLAC__stream_decoder_init_ogg_file.argtypes = [POINTER(FLAC__StreamDecoder), STRING, FLAC__StreamDecoderWriteCallback, FLAC__StreamDecoderMetadataCallback, FLAC__StreamDecoderErrorCallback, c_void_p]
FLAC__stream_decoder_finish = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_finish
FLAC__stream_decoder_finish.restype = FLAC__bool
FLAC__stream_decoder_finish.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_flush = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_flush
FLAC__stream_decoder_flush.restype = FLAC__bool
FLAC__stream_decoder_flush.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_reset = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_reset
FLAC__stream_decoder_reset.restype = FLAC__bool
FLAC__stream_decoder_reset.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_process_single = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_process_single
FLAC__stream_decoder_process_single.restype = FLAC__bool
FLAC__stream_decoder_process_single.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_process_until_end_of_metadata = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_process_until_end_of_metadata
FLAC__stream_decoder_process_until_end_of_metadata.restype = FLAC__bool
FLAC__stream_decoder_process_until_end_of_metadata.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_process_until_end_of_stream = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_process_until_end_of_stream
FLAC__stream_decoder_process_until_end_of_stream.restype = FLAC__bool
FLAC__stream_decoder_process_until_end_of_stream.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_skip_single_frame = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_skip_single_frame
FLAC__stream_decoder_skip_single_frame.restype = FLAC__bool
FLAC__stream_decoder_skip_single_frame.argtypes = [POINTER(FLAC__StreamDecoder)]
FLAC__stream_decoder_seek_absolute = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_decoder_seek_absolute
FLAC__stream_decoder_seek_absolute.restype = FLAC__bool
FLAC__stream_decoder_seek_absolute.argtypes = [POINTER(FLAC__StreamDecoder), FLAC__uint64]

# values for enumeration 'FLAC__StreamEncoderState'
FLAC__StreamEncoderState = c_int # enum
FLAC__StreamEncoderStateString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderStateString')

# values for enumeration 'FLAC__StreamEncoderInitStatus'
FLAC__StreamEncoderInitStatus = c_int # enum
FLAC__StreamEncoderInitStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderInitStatusString')

# values for enumeration 'FLAC__StreamEncoderReadStatus'
FLAC__StreamEncoderReadStatus = c_int # enum
FLAC__StreamEncoderReadStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderReadStatusString')

# values for enumeration 'FLAC__StreamEncoderWriteStatus'
FLAC__StreamEncoderWriteStatus = c_int # enum
FLAC__StreamEncoderWriteStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderWriteStatusString')

# values for enumeration 'FLAC__StreamEncoderSeekStatus'
FLAC__StreamEncoderSeekStatus = c_int # enum
FLAC__StreamEncoderSeekStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderSeekStatusString')

# values for enumeration 'FLAC__StreamEncoderTellStatus'
FLAC__StreamEncoderTellStatus = c_int # enum
FLAC__StreamEncoderTellStatusString = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'FLAC__StreamEncoderTellStatusString')
class FLAC__StreamEncoderProtected(Structure):
    pass
FLAC__StreamEncoderProtected._fields_ = [
]
class FLAC__StreamEncoderPrivate(Structure):
    pass
FLAC__StreamEncoderPrivate._fields_ = [
]
class FLAC__StreamEncoder(Structure):
    pass
FLAC__StreamEncoder._fields_ = [
    ('protected_', POINTER(FLAC__StreamEncoderProtected)),
    ('private_', POINTER(FLAC__StreamEncoderPrivate)),
]
FLAC__StreamEncoderReadCallback = CFUNCTYPE(FLAC__StreamEncoderReadStatus, POINTER(FLAC__StreamEncoder), POINTER(FLAC__byte), POINTER(size_t), c_void_p)
FLAC__StreamEncoderWriteCallback = CFUNCTYPE(FLAC__StreamEncoderWriteStatus, POINTER(FLAC__StreamEncoder), POINTER(FLAC__byte), size_t, c_uint, c_uint, c_void_p)
FLAC__StreamEncoderSeekCallback = CFUNCTYPE(FLAC__StreamEncoderSeekStatus, POINTER(FLAC__StreamEncoder), FLAC__uint64, c_void_p)
FLAC__StreamEncoderTellCallback = CFUNCTYPE(FLAC__StreamEncoderTellStatus, POINTER(FLAC__StreamEncoder), POINTER(FLAC__uint64), c_void_p)
FLAC__StreamEncoderMetadataCallback = CFUNCTYPE(None, POINTER(FLAC__StreamEncoder), POINTER(FLAC__StreamMetadata), c_void_p)
FLAC__StreamEncoderProgressCallback = CFUNCTYPE(None, POINTER(FLAC__StreamEncoder), FLAC__uint64, FLAC__uint64, c_uint, c_uint, c_void_p)
FLAC__stream_encoder_new = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_new
FLAC__stream_encoder_new.restype = POINTER(FLAC__StreamEncoder)
FLAC__stream_encoder_new.argtypes = []
FLAC__stream_encoder_delete = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_delete
FLAC__stream_encoder_delete.restype = None
FLAC__stream_encoder_delete.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_set_ogg_serial_number = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_ogg_serial_number
FLAC__stream_encoder_set_ogg_serial_number.restype = FLAC__bool
FLAC__stream_encoder_set_ogg_serial_number.argtypes = [POINTER(FLAC__StreamEncoder), c_long]
FLAC__stream_encoder_set_verify = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_verify
FLAC__stream_encoder_set_verify.restype = FLAC__bool
FLAC__stream_encoder_set_verify.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_streamable_subset = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_streamable_subset
FLAC__stream_encoder_set_streamable_subset.restype = FLAC__bool
FLAC__stream_encoder_set_streamable_subset.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_channels = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_channels
FLAC__stream_encoder_set_channels.restype = FLAC__bool
FLAC__stream_encoder_set_channels.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_bits_per_sample = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_bits_per_sample
FLAC__stream_encoder_set_bits_per_sample.restype = FLAC__bool
FLAC__stream_encoder_set_bits_per_sample.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_sample_rate = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_sample_rate
FLAC__stream_encoder_set_sample_rate.restype = FLAC__bool
FLAC__stream_encoder_set_sample_rate.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_compression_level = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_compression_level
FLAC__stream_encoder_set_compression_level.restype = FLAC__bool
FLAC__stream_encoder_set_compression_level.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_blocksize = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_blocksize
FLAC__stream_encoder_set_blocksize.restype = FLAC__bool
FLAC__stream_encoder_set_blocksize.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_do_mid_side_stereo = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_do_mid_side_stereo
FLAC__stream_encoder_set_do_mid_side_stereo.restype = FLAC__bool
FLAC__stream_encoder_set_do_mid_side_stereo.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_loose_mid_side_stereo = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_loose_mid_side_stereo
FLAC__stream_encoder_set_loose_mid_side_stereo.restype = FLAC__bool
FLAC__stream_encoder_set_loose_mid_side_stereo.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_apodization = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_apodization
FLAC__stream_encoder_set_apodization.restype = FLAC__bool
FLAC__stream_encoder_set_apodization.argtypes = [POINTER(FLAC__StreamEncoder), STRING]
FLAC__stream_encoder_set_max_lpc_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_max_lpc_order
FLAC__stream_encoder_set_max_lpc_order.restype = FLAC__bool
FLAC__stream_encoder_set_max_lpc_order.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_qlp_coeff_precision = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_qlp_coeff_precision
FLAC__stream_encoder_set_qlp_coeff_precision.restype = FLAC__bool
FLAC__stream_encoder_set_qlp_coeff_precision.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_do_qlp_coeff_prec_search = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_do_qlp_coeff_prec_search
FLAC__stream_encoder_set_do_qlp_coeff_prec_search.restype = FLAC__bool
FLAC__stream_encoder_set_do_qlp_coeff_prec_search.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_do_escape_coding = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_do_escape_coding
FLAC__stream_encoder_set_do_escape_coding.restype = FLAC__bool
FLAC__stream_encoder_set_do_escape_coding.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_do_exhaustive_model_search = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_do_exhaustive_model_search
FLAC__stream_encoder_set_do_exhaustive_model_search.restype = FLAC__bool
FLAC__stream_encoder_set_do_exhaustive_model_search.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__bool]
FLAC__stream_encoder_set_min_residual_partition_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_min_residual_partition_order
FLAC__stream_encoder_set_min_residual_partition_order.restype = FLAC__bool
FLAC__stream_encoder_set_min_residual_partition_order.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_max_residual_partition_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_max_residual_partition_order
FLAC__stream_encoder_set_max_residual_partition_order.restype = FLAC__bool
FLAC__stream_encoder_set_max_residual_partition_order.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_rice_parameter_search_dist = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_rice_parameter_search_dist
FLAC__stream_encoder_set_rice_parameter_search_dist.restype = FLAC__bool
FLAC__stream_encoder_set_rice_parameter_search_dist.argtypes = [POINTER(FLAC__StreamEncoder), c_uint]
FLAC__stream_encoder_set_total_samples_estimate = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_total_samples_estimate
FLAC__stream_encoder_set_total_samples_estimate.restype = FLAC__bool
FLAC__stream_encoder_set_total_samples_estimate.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__uint64]
FLAC__stream_encoder_set_metadata = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_set_metadata
FLAC__stream_encoder_set_metadata.restype = FLAC__bool
FLAC__stream_encoder_set_metadata.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(POINTER(FLAC__StreamMetadata)), c_uint]
FLAC__stream_encoder_get_state = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_state
FLAC__stream_encoder_get_state.restype = FLAC__StreamEncoderState
FLAC__stream_encoder_get_state.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_verify_decoder_state = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_verify_decoder_state
FLAC__stream_encoder_get_verify_decoder_state.restype = FLAC__StreamDecoderState
FLAC__stream_encoder_get_verify_decoder_state.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_resolved_state_string = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_resolved_state_string
FLAC__stream_encoder_get_resolved_state_string.restype = STRING
FLAC__stream_encoder_get_resolved_state_string.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_verify_decoder_error_stats = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_verify_decoder_error_stats
FLAC__stream_encoder_get_verify_decoder_error_stats.restype = None
FLAC__stream_encoder_get_verify_decoder_error_stats.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(FLAC__uint64), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(FLAC__int32), POINTER(FLAC__int32)]
FLAC__stream_encoder_get_verify = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_verify
FLAC__stream_encoder_get_verify.restype = FLAC__bool
FLAC__stream_encoder_get_verify.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_streamable_subset = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_streamable_subset
FLAC__stream_encoder_get_streamable_subset.restype = FLAC__bool
FLAC__stream_encoder_get_streamable_subset.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_channels = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_channels
FLAC__stream_encoder_get_channels.restype = c_uint
FLAC__stream_encoder_get_channels.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_bits_per_sample = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_bits_per_sample
FLAC__stream_encoder_get_bits_per_sample.restype = c_uint
FLAC__stream_encoder_get_bits_per_sample.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_sample_rate = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_sample_rate
FLAC__stream_encoder_get_sample_rate.restype = c_uint
FLAC__stream_encoder_get_sample_rate.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_blocksize = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_blocksize
FLAC__stream_encoder_get_blocksize.restype = c_uint
FLAC__stream_encoder_get_blocksize.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_do_mid_side_stereo = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_do_mid_side_stereo
FLAC__stream_encoder_get_do_mid_side_stereo.restype = FLAC__bool
FLAC__stream_encoder_get_do_mid_side_stereo.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_loose_mid_side_stereo = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_loose_mid_side_stereo
FLAC__stream_encoder_get_loose_mid_side_stereo.restype = FLAC__bool
FLAC__stream_encoder_get_loose_mid_side_stereo.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_max_lpc_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_max_lpc_order
FLAC__stream_encoder_get_max_lpc_order.restype = c_uint
FLAC__stream_encoder_get_max_lpc_order.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_qlp_coeff_precision = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_qlp_coeff_precision
FLAC__stream_encoder_get_qlp_coeff_precision.restype = c_uint
FLAC__stream_encoder_get_qlp_coeff_precision.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_do_qlp_coeff_prec_search = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_do_qlp_coeff_prec_search
FLAC__stream_encoder_get_do_qlp_coeff_prec_search.restype = FLAC__bool
FLAC__stream_encoder_get_do_qlp_coeff_prec_search.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_do_escape_coding = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_do_escape_coding
FLAC__stream_encoder_get_do_escape_coding.restype = FLAC__bool
FLAC__stream_encoder_get_do_escape_coding.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_do_exhaustive_model_search = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_do_exhaustive_model_search
FLAC__stream_encoder_get_do_exhaustive_model_search.restype = FLAC__bool
FLAC__stream_encoder_get_do_exhaustive_model_search.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_min_residual_partition_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_min_residual_partition_order
FLAC__stream_encoder_get_min_residual_partition_order.restype = c_uint
FLAC__stream_encoder_get_min_residual_partition_order.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_max_residual_partition_order = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_max_residual_partition_order
FLAC__stream_encoder_get_max_residual_partition_order.restype = c_uint
FLAC__stream_encoder_get_max_residual_partition_order.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_rice_parameter_search_dist = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_rice_parameter_search_dist
FLAC__stream_encoder_get_rice_parameter_search_dist.restype = c_uint
FLAC__stream_encoder_get_rice_parameter_search_dist.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_get_total_samples_estimate = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_get_total_samples_estimate
FLAC__stream_encoder_get_total_samples_estimate.restype = FLAC__uint64
FLAC__stream_encoder_get_total_samples_estimate.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_init_stream = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_stream
FLAC__stream_encoder_init_stream.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_stream.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__StreamEncoderWriteCallback, FLAC__StreamEncoderSeekCallback, FLAC__StreamEncoderTellCallback, FLAC__StreamEncoderMetadataCallback, c_void_p]
FLAC__stream_encoder_init_ogg_stream = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_ogg_stream
FLAC__stream_encoder_init_ogg_stream.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_ogg_stream.argtypes = [POINTER(FLAC__StreamEncoder), FLAC__StreamEncoderReadCallback, FLAC__StreamEncoderWriteCallback, FLAC__StreamEncoderSeekCallback, FLAC__StreamEncoderTellCallback, FLAC__StreamEncoderMetadataCallback, c_void_p]
FLAC__stream_encoder_init_FILE = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_FILE
FLAC__stream_encoder_init_FILE.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_FILE.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(FILE), FLAC__StreamEncoderProgressCallback, c_void_p]
FLAC__stream_encoder_init_ogg_FILE = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_ogg_FILE
FLAC__stream_encoder_init_ogg_FILE.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_ogg_FILE.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(FILE), FLAC__StreamEncoderProgressCallback, c_void_p]
FLAC__stream_encoder_init_file = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_file
FLAC__stream_encoder_init_file.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_file.argtypes = [POINTER(FLAC__StreamEncoder), STRING, FLAC__StreamEncoderProgressCallback, c_void_p]
FLAC__stream_encoder_init_ogg_file = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_init_ogg_file
FLAC__stream_encoder_init_ogg_file.restype = FLAC__StreamEncoderInitStatus
FLAC__stream_encoder_init_ogg_file.argtypes = [POINTER(FLAC__StreamEncoder), STRING, FLAC__StreamEncoderProgressCallback, c_void_p]
FLAC__stream_encoder_finish = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_finish
FLAC__stream_encoder_finish.restype = FLAC__bool
FLAC__stream_encoder_finish.argtypes = [POINTER(FLAC__StreamEncoder)]
FLAC__stream_encoder_process = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_process
FLAC__stream_encoder_process.restype = FLAC__bool
FLAC__stream_encoder_process.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(POINTER(FLAC__int32)), c_uint]
FLAC__stream_encoder_process_interleaved = _libraries['/usr/lib/libFLAC.so'].FLAC__stream_encoder_process_interleaved
FLAC__stream_encoder_process_interleaved.restype = FLAC__bool
FLAC__stream_encoder_process_interleaved.argtypes = [POINTER(FLAC__StreamEncoder), POINTER(FLAC__int32), c_uint]
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
    ('__rwelision', c_byte),
    ('__pad1', c_ubyte * 7),
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
__fdelt_chk = _libraries['/usr/lib/libFLAC.so'].__fdelt_chk
__fdelt_chk.restype = c_long
__fdelt_chk.argtypes = [c_long]
__fdelt_warn = _libraries['/usr/lib/libFLAC.so'].__fdelt_warn
__fdelt_warn.restype = c_long
__fdelt_warn.argtypes = [c_long]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
getchar = _libraries['/usr/lib/libFLAC.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
fgetc_unlocked = _libraries['/usr/lib/libFLAC.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/lib/libFLAC.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/lib/libFLAC.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/lib/libFLAC.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/lib/libFLAC.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/lib/libFLAC.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/lib/libFLAC.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/lib/libFLAC.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/lib/libFLAC.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/lib/libFLAC.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
__sprintf_chk = _libraries['/usr/lib/libFLAC.so'].__sprintf_chk
__sprintf_chk.restype = c_int
__sprintf_chk.argtypes = [STRING, c_int, size_t, STRING]
__vsprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vsprintf_chk
__vsprintf_chk.restype = c_int
__vsprintf_chk.argtypes = [STRING, c_int, size_t, STRING, POINTER(__va_list_tag)]
sprintf = _libraries['/usr/lib/libFLAC.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vsprintf = _libraries['/usr/lib/libFLAC.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
__snprintf_chk = _libraries['/usr/lib/libFLAC.so'].__snprintf_chk
__snprintf_chk.restype = c_int
__snprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING]
__vsnprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vsnprintf_chk
__vsnprintf_chk.restype = c_int
__vsnprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['/usr/lib/libFLAC.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/lib/libFLAC.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
__fprintf_chk = _libraries['/usr/lib/libFLAC.so'].__fprintf_chk
__fprintf_chk.restype = c_int
__fprintf_chk.argtypes = [POINTER(FILE), c_int, STRING]
__printf_chk = _libraries['/usr/lib/libFLAC.so'].__printf_chk
__printf_chk.restype = c_int
__printf_chk.argtypes = [c_int, STRING]
__vfprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vfprintf_chk
__vfprintf_chk.restype = c_int
__vfprintf_chk.argtypes = [POINTER(FILE), c_int, STRING, POINTER(__va_list_tag)]
__vprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vprintf_chk
__vprintf_chk.restype = c_int
__vprintf_chk.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
fprintf = _libraries['/usr/lib/libFLAC.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/lib/libFLAC.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
vprintf = _libraries['/usr/lib/libFLAC.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
vfprintf = _libraries['/usr/lib/libFLAC.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
__dprintf_chk = _libraries['/usr/lib/libFLAC.so'].__dprintf_chk
__dprintf_chk.restype = c_int
__dprintf_chk.argtypes = [c_int, c_int, STRING]
__vdprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vdprintf_chk
__vdprintf_chk.restype = c_int
__vdprintf_chk.argtypes = [c_int, c_int, STRING, POINTER(__va_list_tag)]
dprintf = _libraries['/usr/lib/libFLAC.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
vdprintf = _libraries['/usr/lib/libFLAC.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
__asprintf_chk = _libraries['/usr/lib/libFLAC.so'].__asprintf_chk
__asprintf_chk.restype = c_int
__asprintf_chk.argtypes = [POINTER(STRING), c_int, STRING]
__vasprintf_chk = _libraries['/usr/lib/libFLAC.so'].__vasprintf_chk
__vasprintf_chk.restype = c_int
__vasprintf_chk.argtypes = [POINTER(STRING), c_int, STRING, POINTER(__va_list_tag)]
class obstack(Structure):
    pass
__obstack_printf_chk = _libraries['/usr/lib/libFLAC.so'].__obstack_printf_chk
__obstack_printf_chk.restype = c_int
__obstack_printf_chk.argtypes = [POINTER(obstack), c_int, STRING]
__obstack_vprintf_chk = _libraries['/usr/lib/libFLAC.so'].__obstack_vprintf_chk
__obstack_vprintf_chk.restype = c_int
__obstack_vprintf_chk.argtypes = [POINTER(obstack), c_int, STRING, POINTER(__va_list_tag)]
asprintf = _libraries['/usr/lib/libFLAC.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
__asprintf = _libraries['/usr/lib/libFLAC.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
obstack_printf = _libraries['/usr/lib/libFLAC.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
vasprintf = _libraries['/usr/lib/libFLAC.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
obstack_vprintf = _libraries['/usr/lib/libFLAC.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, POINTER(__va_list_tag)]
__fgets_chk = _libraries['/usr/lib/libFLAC.so'].__fgets_chk
__fgets_chk.restype = STRING
__fgets_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets = _libraries['/usr/lib/libFLAC.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_chk = _libraries['/usr/lib/libFLAC.so'].__fread_chk
__fread_chk.restype = size_t
__fread_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread = _libraries['/usr/lib/libFLAC.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__fgets_unlocked_chk = _libraries['/usr/lib/libFLAC.so'].__fgets_unlocked_chk
__fgets_unlocked_chk.restype = STRING
__fgets_unlocked_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets_unlocked = _libraries['/usr/lib/libFLAC.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_unlocked_chk = _libraries['/usr/lib/libFLAC.so'].__fread_unlocked_chk
__fread_unlocked_chk.restype = size_t
__fread_unlocked_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread_unlocked = _libraries['/usr/lib/libFLAC.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
bsearch = _libraries['/usr/lib/libFLAC.so'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
atof = _libraries['/usr/lib/libFLAC.so'].atof
atof.restype = c_double
atof.argtypes = [STRING]
__realpath_chk = _libraries['/usr/lib/libFLAC.so'].__realpath_chk
__realpath_chk.restype = STRING
__realpath_chk.argtypes = [STRING, STRING, size_t]
realpath = _libraries['/usr/lib/libFLAC.so'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__ptsname_r_chk = _libraries['/usr/lib/libFLAC.so'].__ptsname_r_chk
__ptsname_r_chk.restype = c_int
__ptsname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ptsname_r = _libraries['/usr/lib/libFLAC.so'].ptsname_r
ptsname_r.restype = c_int
ptsname_r.argtypes = [c_int, STRING, size_t]
__wctomb_chk = _libraries['/usr/lib/libFLAC.so'].__wctomb_chk
__wctomb_chk.restype = c_int
__wctomb_chk.argtypes = [STRING, c_wchar, size_t]
wctomb = _libraries['/usr/lib/libFLAC.so'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
__mbstowcs_chk = _libraries['/usr/lib/libFLAC.so'].__mbstowcs_chk
__mbstowcs_chk.restype = size_t
__mbstowcs_chk.argtypes = [WSTRING, STRING, size_t, size_t]
mbstowcs = _libraries['/usr/lib/libFLAC.so'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
__wcstombs_chk = _libraries['/usr/lib/libFLAC.so'].__wcstombs_chk
__wcstombs_chk.restype = size_t
__wcstombs_chk.argtypes = [STRING, WSTRING, size_t, size_t]
wcstombs = _libraries['/usr/lib/libFLAC.so'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libFLAC.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libFLAC.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libFLAC.so'], '_sys_errlist')
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
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libFLAC.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libFLAC.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libFLAC.so'], '_IO_2_1_stderr_')
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
__underflow = _libraries['/usr/lib/libFLAC.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/lib/libFLAC.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/lib/libFLAC.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/lib/libFLAC.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/lib/libFLAC.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/lib/libFLAC.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/lib/libFLAC.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/lib/libFLAC.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/lib/libFLAC.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/lib/libFLAC.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/lib/libFLAC.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/lib/libFLAC.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag), POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/lib/libFLAC.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag)]
_IO_padn = _libraries['/usr/lib/libFLAC.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/lib/libFLAC.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/lib/libFLAC.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/lib/libFLAC.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/lib/libFLAC.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong
__FILE = _IO_FILE
va_list = __gnuc_va_list
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/lib/libFLAC.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/lib/libFLAC.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/lib/libFLAC.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/lib/libFLAC.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/lib/libFLAC.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/lib/libFLAC.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/lib/libFLAC.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/lib/libFLAC.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/lib/libFLAC.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/lib/libFLAC.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/lib/libFLAC.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/lib/libFLAC.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/lib/libFLAC.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/lib/libFLAC.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/lib/libFLAC.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/lib/libFLAC.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/lib/libFLAC.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/lib/libFLAC.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/lib/libFLAC.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/lib/libFLAC.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/lib/libFLAC.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/lib/libFLAC.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/lib/libFLAC.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/lib/libFLAC.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fscanf = _libraries['/usr/lib/libFLAC.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/lib/libFLAC.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/lib/libFLAC.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/lib/libFLAC.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['/usr/lib/libFLAC.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['/usr/lib/libFLAC.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['/usr/lib/libFLAC.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/lib/libFLAC.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/lib/libFLAC.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/lib/libFLAC.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/lib/libFLAC.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/lib/libFLAC.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
gets = _libraries['/usr/lib/libFLAC.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
__getdelim = _libraries['/usr/lib/libFLAC.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/lib/libFLAC.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/lib/libFLAC.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/lib/libFLAC.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/lib/libFLAC.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fwrite = _libraries['/usr/lib/libFLAC.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/lib/libFLAC.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/lib/libFLAC.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/lib/libFLAC.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/lib/libFLAC.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/lib/libFLAC.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/lib/libFLAC.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/lib/libFLAC.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/lib/libFLAC.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/lib/libFLAC.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/lib/libFLAC.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/lib/libFLAC.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/lib/libFLAC.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/lib/libFLAC.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/lib/libFLAC.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/lib/libFLAC.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/lib/libFLAC.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/lib/libFLAC.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/lib/libFLAC.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/lib/libFLAC.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/lib/libFLAC.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/lib/libFLAC.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/lib/libFLAC.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/lib/libFLAC.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/lib/libFLAC.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
obstack._fields_ = [
]
flockfile = _libraries['/usr/lib/libFLAC.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/lib/libFLAC.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/lib/libFLAC.so'].funlockfile
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
__ctype_get_mb_cur_max = _libraries['/usr/lib/libFLAC.so'].__ctype_get_mb_cur_max
__ctype_get_mb_cur_max.restype = size_t
__ctype_get_mb_cur_max.argtypes = []
strtod = _libraries['/usr/lib/libFLAC.so'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['/usr/lib/libFLAC.so'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['/usr/lib/libFLAC.so'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['/usr/lib/libFLAC.so'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['/usr/lib/libFLAC.so'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['/usr/lib/libFLAC.so'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['/usr/lib/libFLAC.so'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['/usr/lib/libFLAC.so'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['/usr/lib/libFLAC.so'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
strtol_l = _libraries['/usr/lib/libFLAC.so'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['/usr/lib/libFLAC.so'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['/usr/lib/libFLAC.so'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['/usr/lib/libFLAC.so'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['/usr/lib/libFLAC.so'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['/usr/lib/libFLAC.so'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['/usr/lib/libFLAC.so'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
atoi = _libraries['/usr/lib/libFLAC.so'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['/usr/lib/libFLAC.so'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['/usr/lib/libFLAC.so'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
l64a = _libraries['/usr/lib/libFLAC.so'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['/usr/lib/libFLAC.so'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['/usr/lib/libFLAC.so'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['/usr/lib/libFLAC.so'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['/usr/lib/libFLAC.so'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['/usr/lib/libFLAC.so'].setstate
setstate.restype = STRING
setstate.argtypes = [STRING]
class random_data(Structure):
    pass
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
random_r = _libraries['/usr/lib/libFLAC.so'].random_r
random_r.restype = c_int
random_r.argtypes = [POINTER(random_data), POINTER(int32_t)]
srandom_r = _libraries['/usr/lib/libFLAC.so'].srandom_r
srandom_r.restype = c_int
srandom_r.argtypes = [c_uint, POINTER(random_data)]
initstate_r = _libraries['/usr/lib/libFLAC.so'].initstate_r
initstate_r.restype = c_int
initstate_r.argtypes = [c_uint, STRING, size_t, POINTER(random_data)]
setstate_r = _libraries['/usr/lib/libFLAC.so'].setstate_r
setstate_r.restype = c_int
setstate_r.argtypes = [STRING, POINTER(random_data)]
rand = _libraries['/usr/lib/libFLAC.so'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['/usr/lib/libFLAC.so'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['/usr/lib/libFLAC.so'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['/usr/lib/libFLAC.so'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['/usr/lib/libFLAC.so'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['/usr/lib/libFLAC.so'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['/usr/lib/libFLAC.so'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['/usr/lib/libFLAC.so'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['/usr/lib/libFLAC.so'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['/usr/lib/libFLAC.so'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['/usr/lib/libFLAC.so'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['/usr/lib/libFLAC.so'].lcong48
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
drand48_r = _libraries['/usr/lib/libFLAC.so'].drand48_r
drand48_r.restype = c_int
drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
erand48_r = _libraries['/usr/lib/libFLAC.so'].erand48_r
erand48_r.restype = c_int
erand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_double)]
lrand48_r = _libraries['/usr/lib/libFLAC.so'].lrand48_r
lrand48_r.restype = c_int
lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
nrand48_r = _libraries['/usr/lib/libFLAC.so'].nrand48_r
nrand48_r.restype = c_int
nrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
mrand48_r = _libraries['/usr/lib/libFLAC.so'].mrand48_r
mrand48_r.restype = c_int
mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
jrand48_r = _libraries['/usr/lib/libFLAC.so'].jrand48_r
jrand48_r.restype = c_int
jrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
srand48_r = _libraries['/usr/lib/libFLAC.so'].srand48_r
srand48_r.restype = c_int
srand48_r.argtypes = [c_long, POINTER(drand48_data)]
seed48_r = _libraries['/usr/lib/libFLAC.so'].seed48_r
seed48_r.restype = c_int
seed48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
lcong48_r = _libraries['/usr/lib/libFLAC.so'].lcong48_r
lcong48_r.restype = c_int
lcong48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
malloc = _libraries['/usr/lib/libFLAC.so'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['/usr/lib/libFLAC.so'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['/usr/lib/libFLAC.so'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['/usr/lib/libFLAC.so'].free
free.restype = None
free.argtypes = [c_void_p]
cfree = _libraries['/usr/lib/libFLAC.so'].cfree
cfree.restype = None
cfree.argtypes = [c_void_p]
valloc = _libraries['/usr/lib/libFLAC.so'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
posix_memalign = _libraries['/usr/lib/libFLAC.so'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]
aligned_alloc = _libraries['/usr/lib/libFLAC.so'].aligned_alloc
aligned_alloc.restype = c_void_p
aligned_alloc.argtypes = [size_t, size_t]
abort = _libraries['/usr/lib/libFLAC.so'].abort
abort.restype = None
abort.argtypes = []
on_exit = _libraries['/usr/lib/libFLAC.so'].on_exit
on_exit.restype = c_int
on_exit.argtypes = [CFUNCTYPE(None, c_int, c_void_p), c_void_p]
exit = _libraries['/usr/lib/libFLAC.so'].exit
exit.restype = None
exit.argtypes = [c_int]
quick_exit = _libraries['/usr/lib/libFLAC.so'].quick_exit
quick_exit.restype = None
quick_exit.argtypes = [c_int]
_Exit = _libraries['/usr/lib/libFLAC.so']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['/usr/lib/libFLAC.so'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
secure_getenv = _libraries['/usr/lib/libFLAC.so'].secure_getenv
secure_getenv.restype = STRING
secure_getenv.argtypes = [STRING]
putenv = _libraries['/usr/lib/libFLAC.so'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['/usr/lib/libFLAC.so'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['/usr/lib/libFLAC.so'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
clearenv = _libraries['/usr/lib/libFLAC.so'].clearenv
clearenv.restype = c_int
clearenv.argtypes = []
mktemp = _libraries['/usr/lib/libFLAC.so'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['/usr/lib/libFLAC.so'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemp64 = _libraries['/usr/lib/libFLAC.so'].mkstemp64
mkstemp64.restype = c_int
mkstemp64.argtypes = [STRING]
mkstemps = _libraries['/usr/lib/libFLAC.so'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkstemps64 = _libraries['/usr/lib/libFLAC.so'].mkstemps64
mkstemps64.restype = c_int
mkstemps64.argtypes = [STRING, c_int]
mkdtemp = _libraries['/usr/lib/libFLAC.so'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
mkostemp = _libraries['/usr/lib/libFLAC.so'].mkostemp
mkostemp.restype = c_int
mkostemp.argtypes = [STRING, c_int]
mkostemp64 = _libraries['/usr/lib/libFLAC.so'].mkostemp64
mkostemp64.restype = c_int
mkostemp64.argtypes = [STRING, c_int]
mkostemps = _libraries['/usr/lib/libFLAC.so'].mkostemps
mkostemps.restype = c_int
mkostemps.argtypes = [STRING, c_int, c_int]
mkostemps64 = _libraries['/usr/lib/libFLAC.so'].mkostemps64
mkostemps64.restype = c_int
mkostemps64.argtypes = [STRING, c_int, c_int]
system = _libraries['/usr/lib/libFLAC.so'].system
system.restype = c_int
system.argtypes = [STRING]
canonicalize_file_name = _libraries['/usr/lib/libFLAC.so'].canonicalize_file_name
canonicalize_file_name.restype = STRING
canonicalize_file_name.argtypes = [STRING]
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
qsort = _libraries['/usr/lib/libFLAC.so'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['/usr/lib/libFLAC.so'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['/usr/lib/libFLAC.so'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['/usr/lib/libFLAC.so'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['/usr/lib/libFLAC.so'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['/usr/lib/libFLAC.so'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['/usr/lib/libFLAC.so'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['/usr/lib/libFLAC.so'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['/usr/lib/libFLAC.so'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['/usr/lib/libFLAC.so'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['/usr/lib/libFLAC.so'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
qecvt = _libraries['/usr/lib/libFLAC.so'].qecvt
qecvt.restype = STRING
qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qfcvt = _libraries['/usr/lib/libFLAC.so'].qfcvt
qfcvt.restype = STRING
qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qgcvt = _libraries['/usr/lib/libFLAC.so'].qgcvt
qgcvt.restype = STRING
qgcvt.argtypes = [c_longdouble, c_int, STRING]
ecvt_r = _libraries['/usr/lib/libFLAC.so'].ecvt_r
ecvt_r.restype = c_int
ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
fcvt_r = _libraries['/usr/lib/libFLAC.so'].fcvt_r
fcvt_r.restype = c_int
fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qecvt_r = _libraries['/usr/lib/libFLAC.so'].qecvt_r
qecvt_r.restype = c_int
qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qfcvt_r = _libraries['/usr/lib/libFLAC.so'].qfcvt_r
qfcvt_r.restype = c_int
qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
mblen = _libraries['/usr/lib/libFLAC.so'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['/usr/lib/libFLAC.so'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
rpmatch = _libraries['/usr/lib/libFLAC.so'].rpmatch
rpmatch.restype = c_int
rpmatch.argtypes = [STRING]
getsubopt = _libraries['/usr/lib/libFLAC.so'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
posix_openpt = _libraries['/usr/lib/libFLAC.so'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['/usr/lib/libFLAC.so'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['/usr/lib/libFLAC.so'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['/usr/lib/libFLAC.so'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
getpt = _libraries['/usr/lib/libFLAC.so'].getpt
getpt.restype = c_int
getpt.argtypes = []
getloadavg = _libraries['/usr/lib/libFLAC.so'].getloadavg
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
select = _libraries['/usr/lib/libFLAC.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
pselect = _libraries['/usr/lib/libFLAC.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/lib/libFLAC.so'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/lib/libFLAC.so'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/lib/libFLAC.so'].gnu_dev_makedev
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
ssize_t = __ssize_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
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
__all__ = ['FLAC__Metadata_Chain',
           'FLAC__METADATA_CHAIN_STATUS_INVALID_CALLBACKS',
           'FLAC__Metadata_SimpleIterator', '_ATFILE_SOURCE', 'EOF',
           'FLAC__metadata_chain_sort_padding', '__glibc_unlikely',
           'wctomb', 'FLAC__stream_encoder_get_blocksize',
           'FLAC__IOHandle', '_IO_USER_LOCK', 'div_t',
           'FLAC__SUBSET_MAX_RICE_PARTITION_ORDER', 'u_short',
           '__INO_T_MATCHES_INO64_T', 'mkostemp64', '__off64_t',
           'N14pthread_cond_t4DOT_11E', 'fsetpos',
           'FLAC_API_VERSION_CURRENT',
           'FLAC__StreamDecoderErrorStatus',
           'FLAC__METADATA_CHAIN_STATUS_BAD_METADATA', 'timer_t',
           '__WCOREFLAG', 'uint8_t', 'fpos_t', '_G_HAVE_MREMAP',
           'FLAC__StreamMetadata_SeekTable',
           'FLAC__STREAM_METADATA_CUESHEET_RESERVED_LEN', 'uid_t',
           'FLAC__STREAM_ENCODER_SEEK_STATUS_UNSUPPORTED', 'qecvt',
           'FLAC__STREAM_ENCODER_CLIENT_ERROR',
           'FLAC__stream_decoder_init_ogg_FILE',
           'FLAC__metadata_object_cuesheet_track_delete_index',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2',
           'FLAC__FrameHeader',
           'FLAC__STREAM_ENCODER_READ_STATUS_END_OF_STREAM',
           'FLAC__METADATA_TYPE_PADDING',
           '__SIZEOF_PTHREAD_CONDATTR_T', 'srandom', 'makedev',
           'FLAC__stream_decoder_set_md5_checking', '__FD_ISSET',
           '__realpath_chk', 'FLAC__STREAM_DECODER_SEEK_ERROR',
           '_IO_BUFSIZ', 'rand_r', 'getpt', '__FILE',
           'FLAC__stream_decoder_get_resolved_state_string',
           '_IO_off64_t', 'INT_FAST16_MIN',
           'FLAC__STREAM_DECODER_LENGTH_STATUS_UNSUPPORTED',
           'FLAC__metadata_simple_iterator_init',
           'FLAC__stream_decoder_init_file', '_IO_fpos64_t',
           'SEEK_HOLE',
           'FLAC__metadata_object_vorbiscomment_entry_from_name_value_pair',
           'ftell', 'FLAC__stream_decoder_flush', '__time_t_defined',
           'FLAC__StreamDecoderSeekStatus', 'INT_LEAST16_MAX',
           '__WSTOPSIG', '__NFDBITS',
           'FLAC__stream_encoder_init_FILE', '__ASMNAME',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_ESCAPE_PARAMETER',
           'funlockfile', 'UINT8_C',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_MAX_LPC_ORDER',
           'htole32', 'FLAC__METADATA_TYPE_CUESHEET',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_BAD_METADATA',
           '_POSIX_SOURCE', 'wait', 'FLAC__StreamEncoderTellCallback',
           'uint_fast16_t', '_IO_jump_t',
           'FLAC__STREAM_DECODER_WRITE_STATUS_ABORT',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_OK', 'va_list',
           'stderr',
           'FLAC__metadata_object_seektable_template_append_spaced_points_by_samples',
           'pthread_key_t', 'div', 'INT_LEAST8_MIN', 'realpath',
           'fputc_unlocked',
           'FLAC__metadata_iterator_insert_block_after',
           'FLAC__stream_decoder_get_decode_position',
           'FLAC__metadata_object_vorbiscomment_set_vendor_string',
           'FLAC__stream_decoder_reset', 'INT_FAST64_MIN', 'snprintf',
           '_ALLOCA_H', '__va_list_tag',
           'FLAC__metadata_iterator_insert_block_before',
           'FLAC__StreamEncoderProgressCallback',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_DURING_PERFORMANCE',
           'mkostemps', '_IO_USER_BUF',
           'FLAC__StreamDecoderInitStatusString', 'UINTMAX_C',
           'nlink_t', 'FLAC__metadata_simple_iterator_get_block_type',
           '__USE_POSIX199309', 'mktemp', 'FLAC__MIN_BITS_PER_SAMPLE',
           'getchar_unlocked', 'FLAC__MAX_FIXED_ORDER',
           'FLAC__StreamDecoderErrorStatusString', '__timer_t',
           'mblen', 'FLAC__metadata_simple_iterator_set_block',
           'FLAC__STREAM_METADATA_PICTURE_WIDTH_LEN',
           '__mbstowcs_chk', '_IO_SHOWBASE', 'abs',
           'FLAC__metadata_iterator_next', 'id_t', '_IO_FILE',
           '__WEXITSTATUS', '_G_HAVE_MMAP', '__codecvt_partial',
           '__attribute_format_strfmon__',
           'N14FLAC__Subframe4DOT_30E', '__WORDSIZE_TIME64_COMPAT32',
           'FLAC__SubframeType',
           'FLAC__metadata_chain_write_with_callbacks', 'be64toh',
           'FLAC__StreamEncoderStateString', 'UINT16_C',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_BLOCK_SIZE',
           'blkcnt_t',
           'FLAC__metadata_object_vorbiscomment_remove_entries_matching',
           'FLAC__metadata_object_vorbiscomment_find_entry_from',
           'open_memstream',
           'FLAC__STREAM_DECODER_ERROR_STATUS_LOST_SYNC',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_PUBLISHER_LOGOTYPE',
           'fsetpos64', '_IOS_BIN', 'FLAC__MAX_SAMPLE_RATE',
           '__locale_data',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_ILLUSTRATION',
           'FLAC__metadata_iterator_prev', 'INTMAX_C', '_IO_SKIPWS',
           '__qaddr_t',
           'FLAC__stream_decoder_set_metadata_ignore_application',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_PRE_EMPHASIS_LEN',
           '__WIFEXITED', 'clearenv',
           'FLAC__CHANNEL_ASSIGNMENT_LEFT_SIDE', '__codecvt_result',
           '_IO_SCIENTIFIC', 'FLAC__ChannelAssignmentString',
           'strtod', 'FLAC__MAX_BITS_PER_SAMPLE',
           'FLAC__VERSION_STRING', 'FLAC__format_cuesheet_is_legal',
           'qecvt_r', 'FLAC__StreamEncoderTellStatusString', '__PMT',
           'uint_fast8_t', '_LARGEFILE_SOURCE', 'u_int8_t', 'srand',
           'INT8_MAX', 'realloc', '__mode_t',
           'FLAC__STREAM_METADATA_VORBIS_COMMENT_ENTRY_LENGTH_LEN',
           'FLAC__metadata_object_cuesheet_calculate_cddb_id',
           'u_int64_t', '_IO_DEC', 'FLAC__StreamDecoderWriteCallback',
           '__off_t',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_CALLBACKS',
           'fmemopen', 'select',
           'FLAC__format_vorbiscomment_entry_value_is_legal',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_NUMBER_OF_CHANNELS',
           '__fgets_unlocked_chk',
           'FLAC__METADATA_CHAIN_STATUS_INTERNAL_ERROR', 'u_quad_t',
           'FLAC__StreamDecoderInitStatus',
           'FLAC__metadata_object_seektable_resize_points', 'perror',
           'fsfilcnt64_t', 'FLAC__STREAM_DECODER_READ_FRAME',
           'fputs_unlocked', '_IOFBF', 'cfree', '_IOS_TRUNC',
           'INTPTR_MIN',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_TYPE_LEN',
           'initstate_r', 'uint_least32_t', 'int_least64_t', 'ftello',
           'FLAC__metadata_chain_read_with_callbacks', 'minor',
           'FLAC__stream_encoder_get_do_mid_side_stereo',
           'FLAC__STREAM_METADATA_CUESHEET_INDEX_NUMBER_LEN',
           'FLAC__METADATA_CHAIN_STATUS_WRITE_ERROR',
           'FLAC__stream_encoder_set_qlp_coeff_precision', 'ftello64',
           'FLAC__metadata_get_tags', 'qsort', 'ferror_unlocked',
           '__USE_FORTIFY_LEVEL',
           'FLAC__stream_encoder_set_streamable_subset', '_G_va_list',
           '__fsblkcnt64_t', 'PTRDIFF_MAX',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_LEN',
           'FLAC__metadata_simple_iterator_delete_block',
           'FLAC__metadata_iterator_set_block', 'INT32_MIN',
           'putchar', 'BIG_ENDIAN',
           'FLAC__SUBFRAME_WASTED_BITS_FLAG_LEN',
           'FLAC__SubframeTypeString',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_MEDIA',
           'FLAC__STREAM_DECODER_INIT_STATUS_INVALID_CALLBACKS',
           '_IO_uid_t', '__USE_XOPEN_EXTENDED',
           'FLAC__STREAM_SYNC_LEN', 'INT_LEAST32_MAX', 'fopen64',
           'FLAC__metadata_object_vorbiscomment_delete_comment',
           'ftrylockfile', 'FLAC__STREAM_METADATA_IS_LAST_LEN',
           'FLAC__METADATA_TYPE_PICTURE',
           'FLAC__stream_encoder_set_do_qlp_coeff_prec_search',
           '__fsfilcnt64_t', '_IO_pid_t',
           'FLAC__StreamMetadata_SeekPoint', 'ulong',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_CONDUCTOR',
           '__uint16_t', 'FLAC__stream_decoder_get_total_samples',
           'FLAC__MAX_BLOCK_SIZE', 'fprintf', 'ldiv_t',
           '_IO_BOOLALPHA', '__io_read_fn',
           'FLAC__metadata_object_cuesheet_track_insert_blank_index',
           'strtoul', '__WALL', '_IO_UNITBUF',
           'FLAC__IOCallback_Seek',
           'FLAC__metadata_object_vorbiscomment_remove_entry_matching',
           'FLAC__metadata_simple_iterator_status', 'intptr_t',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_SEEK_ERROR',
           'off_t', 'strtold', 'abort', 'FD_ZERO', '__fsblkcnt_t',
           'strtoll', '__STDC_CONSTANT_MACROS', 'feof',
           'FLAC__metadata_object_seektable_set_point', 'locale_t',
           '__WIFCONTINUED', 'clearerr',
           'FLAC__SUBFRAME_TYPE_VERBATIM', 'mkstemps',
           'FLAC__STREAM_ENCODER_FRAMING_ERROR', 'lcong48', 'lrand48',
           'FLAC__Metadata_SimpleIteratorStatusString',
           'UINT_FAST16_MAX', '__WORDSIZE',
           'FLAC__metadata_object_new', 'vfprintf', 'rewind',
           'on_exit', 'putc_unlocked', 'int_fast8_t', 'INT_FAST8_MIN',
           'UINT32_C', 'fsblkcnt_t', 'WEXITED',
           'FLAC__REFERENCE_CODEC_MAX_BITS_PER_SAMPLE',
           '_XOPEN_SOURCE', '_IO_free_backup_area', 'getline',
           'mrand48_r', 'FLAC__CHANNEL_ASSIGNMENT_MID_SIDE',
           'FLAC__metadata_simple_iterator_delete', 'WINT_MIN',
           'srand48_r', 'FLAC__int8', '__USE_ISOC95',
           'FLAC__STREAM_METADATA_SEEKPOINT_FRAME_SAMPLES_LEN',
           'FLAC__IOCallback_Read',
           'FLAC__stream_decoder_get_md5_checking',
           'FLAC__metadata_simple_iterator_prev', '__GLIBC__',
           'pthread_rwlockattr_t', 'FLAC__StreamEncoderSeekStatus',
           'FLAC__StreamMetadata_Padding', '__USE_ISOC99', 'fcvt',
           'FLAC__StreamDecoderPrivate',
           'FLAC__metadata_object_picture_is_legal',
           'FLAC__STREAM_METADATA_STREAMINFO_MD5SUM_LEN',
           '_IO_fpos_t',
           'FLAC__STREAM_METADATA_SEEKPOINT_SAMPLE_NUMBER_LEN',
           'FLAC__STREAM_ENCODER_INIT_STATUS_OK', 'getloadavg',
           '__u_int', 'FLAC__stream_encoder_set_metadata',
           'N17FLAC__FrameHeader4DOT_34E',
           'FLAC__metadata_object_vorbiscomment_append_comment',
           'FLAC__SUBFRAME_TYPE_FIXED_BYTE_ALIGNED_MASK',
           'FLAC__STREAM_ENCODER_INIT_STATUS_BLOCK_SIZE_TOO_SMALL_FOR_LPC_ORDER',
           'ssize_t', '_XLOCALE_H',
           'FLAC__STREAM_METADATA_CUESHEET_INDEX_RESERVED_LEN',
           'FLAC__MAX_METADATA_TYPE_CODE', '__fsfilcnt_t',
           'INT_LEAST8_MAX', 'le32toh', 'vscanf',
           'FLAC__CHANNEL_ASSIGNMENT_RIGHT_SIDE',
           'FLAC__stream_encoder_get_resolved_state_string',
           'UINT8_MAX', 'strtouq',
           'FLAC__STREAM_METADATA_STREAMINFO_MAX_FRAME_SIZE_LEN',
           '__glibc_likely', '__LONG_LONG_PAIR', '__WCOREDUMP',
           '_IONBF', 'FLAC__metadata_object_application_set_data',
           'FLAC__stream_encoder_init_ogg_FILE', 'size_t',
           '__USE_XOPEN', 'remove', 'FLAC__IOCallback_Eof',
           'FLAC__STREAM_METADATA_STREAMINFO_BITS_PER_SAMPLE_LEN',
           'FLAC__STREAM_DECODER_INIT_STATUS_OK', 'FLAC__bool',
           '__USE_POSIX2', '__time_t', '_IO_ftrylockfile',
           'INT_LEAST16_MIN', 'fdopen', 'uint_least16_t',
           'FLAC__metadata_get_streaminfo',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_BAND_LOGOTYPE',
           'FLAC__METADATA_CHAIN_STATUS_WRONG_WRITE_CALL', 'vfscanf',
           'mkostemps64', 'FLAC__STREAM_DECODER_SEEK_STATUS_ERROR',
           'feof_unlocked', 'FLAC__stream_decoder_get_channels',
           '__GLIBC_PREREQ', 'FLAC__MIN_QLP_COEFF_PRECISION',
           'FLAC__stream_decoder_get_blocksize', 'N4wait3DOT_1E',
           '__W_EXITCODE', 'FLAC__STREAM_ENCODER_TELL_STATUS_OK',
           'FLAC__STREAM_DECODER_ABORTED',
           'FLAC__METADATA_TYPE_SEEKTABLE',
           'FLAC__metadata_object_vorbiscomment_resize_comments',
           'FLAC__EntropyCodingMethod_PartitionedRiceContents',
           'LITTLE_ENDIAN',
           'FLAC__metadata_object_cuesheet_set_track', 'u_char',
           'fpos64_t', '__asprintf_chk',
           'FLAC__STREAM_METADATA_SEEKPOINT_PLACEHOLDER',
           '__USE_ATFILE',
           'FLAC__STREAM_METADATA_PICTURE_DATA_LENGTH_LEN',
           'u_int16_t', 'TMP_MAX', 'daddr_t', '_G_BUFSIZ',
           'FLAC__STREAM_SYNC_LENGTH', 'gets', 'INTMAX_MIN',
           'FLAC__STREAM_DECODER_END_OF_STREAM', 'gnu_dev_major',
           'FLAC__IOCallback_Tell', 'FLAC__StreamEncoderProtected',
           'scanf',
           'FLAC__metadata_object_seektable_template_append_point',
           'FLAC__StreamMetadata_CueSheet',
           'FLAC__STREAM_DECODER_INIT_STATUS_UNSUPPORTED_CONTAINER',
           'FLAC__STREAM_DECODER_TELL_STATUS_OK',
           'FLAC__STREAM_METADATA_CUESHEET_IS_CD_LEN',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_COMPOSER',
           'UINT_FAST8_MAX', '__USE_POSIX', '_IO_NO_WRITES',
           '__locale_t',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_LEAFLET_PAGE',
           'FLAC__MAX_LPC_ORDER', 'pthread_spinlock_t',
           'FLAC__metadata_object_picture_set_mime_type',
           'UINT64_MAX', 'FLAC__FRAME_HEADER_SYNC',
           '__SIZEOF_PTHREAD_MUTEXATTR_T',
           'FLAC__metadata_chain_merge_padding', '_IO_seekoff',
           'FLAC__StreamEncoderReadStatusString', 'INT_FAST64_MAX',
           '__fsword_t', 'FLAC_API_VERSION_AGE', '__fd_mask',
           '__FILE_defined', 'FLAC__stream_encoder_init_ogg_stream',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_SAMPLE_RATE',
           'fwrite_unlocked', 'fgets_unlocked', 'clock_t',
           '_IO_NO_READS', 'WIFSIGNALED',
           'FLAC__METADATA_TYPE_STREAMINFO',
           'FLAC__STREAM_DECODER_INIT_STATUS_ERROR_OPENING_FILE',
           '__useconds_t', '_BITS_WCHAR_H', '__GLIBC_MINOR__',
           '_IO_CURRENTLY_PUTTING', 'FLAC__Metadata_ChainStatus',
           'FLAC__Subframe_Constant', 'FLAC__MetadataTypeString',
           'FLAC__METADATA_CHAIN_STATUS_OK', '__fread_chk',
           '__clockid_t_defined',
           'FLAC__stream_decoder_set_metadata_respond_application',
           'unsetenv', 'FLAC__stream_encoder_set_max_lpc_order',
           '__vfprintf_chk', '__BYTE_ORDER', '_IO_funlockfile',
           '__SIZEOF_PTHREAD_ATTR_T',
           'FLAC__stream_decoder_set_ogg_serial_number',
           'FLAC__MAX_CHANNELS', '_IO_vfprintf', 'uint_least8_t',
           'pthread_barrier_t', '__gid_t', 'u_int32_t',
           'pthread_rwlock_t', 'FLAC__StreamDecoderTellCallback',
           'asprintf', '__pthread_internal_list',
           'N11__mbstate_t4DOT_56E',
           'FLAC__FRAME_HEADER_BLOCK_SIZE_LEN',
           '_IO_cookie_io_functions_t', 'free', 'labs',
           '_SYS_TYPES_H',
           'FLAC__metadata_object_cuesheet_track_resize_indices',
           '__gnuc_va_list', '__P',
           'FLAC__STREAM_DECODER_TELL_STATUS_UNSUPPORTED',
           '__ptsname_r_chk', 'FLAC__StreamMetadata_Application',
           'qsort_r', '_IO_ERR_SEEN', 'sprintf', 'fseeko',
           'FLAC__StreamDecoderLengthStatusString', 'putenv',
           '__USE_GNU', 'atoll',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_RECORDING_LOCATION',
           'WUNTRACED', 'mbtowc', 'random_r', 'htobe16',
           'FLAC_API_SUPPORTS_OGG_FLAC', '__pthread_list_t',
           'FLAC__StreamMetadata_StreamInfo',
           'FLAC__STREAM_ENCODER_OGG_ERROR', 'pthread_attr_t',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_FILE_ICON_STANDARD',
           '__attribute_format_arg__',
           'FLAC__format_blocksize_is_subset', 'ferror',
           '__vprintf_chk', 'ino_t', '_G_IO_IO_FILE_VERSION',
           '_POSIX_C_SOURCE', 'major', 'fopencookie',
           'FLAC__STREAM_METADATA_APPLICATION_ID_LEN',
           'FLAC__SUBFRAME_LPC_QLP_COEFF_PRECISION_LEN',
           '__suseconds_t', '_IO_ssize_t',
           'FLAC__StreamMetadata_Picture',
           'FLAC__METADATA_TYPE_UNDEFINED', 'valloc',
           'FLAC__metadata_chain_delete', '__W_STOPCODE',
           'FLAC__metadata_simple_iterator_next', 'calloc',
           'FLAC__stream_encoder_set_rice_parameter_search_dist',
           'FLAC__STREAM_ENCODER_TELL_STATUS_ERROR', 'strtol_l',
           'FLAC__STREAM_ENCODER_OK',
           'FLAC__stream_encoder_set_do_escape_coding',
           'cookie_write_function_t', 'FLAC__int32',
           'FLAC__Metadata_ChainStatusString', '_IO_2_1_stdout_',
           '_IO_IS_APPENDING', '__ldiv_t_defined',
           'FLAC__stream_encoder_get_loose_mid_side_stereo',
           'FLAC__stream_decoder_skip_single_frame', 'FLAC__uint16',
           '_IO_ferror', '_sys_nerr', 'INT8_MIN',
           'FLAC__metadata_object_cuesheet_is_legal', '__W_CONTINUED',
           'system', 'fclose', '__bswap_constant_32', 'time_t',
           'FLAC__stream_encoder_set_max_residual_partition_order',
           'le16toh', 'UINT_LEAST64_MAX', '__asprintf',
           'FLAC__STREAM_ENCODER_READ_STATUS_CONTINUE',
           'FLAC__stream_encoder_get_streamable_subset', 'mkstemp64',
           'UINT_FAST64_MAX', '__mbstate_t', '__quad_t',
           'FLAC__stream_encoder_get_do_qlp_coeff_prec_search',
           '__uint8_t', 'FLAC__stream_decoder_init_stream',
           'FLAC__metadata_object_cuesheet_insert_track',
           '_IO_INTERNAL', '__SIZEOF_PTHREAD_RWLOCK_T',
           'FLAC__STREAM_METADATA_PICTURE_DESCRIPTION_LENGTH_LEN',
           'FLAC__Subframe_LPC', 'getsubopt', '__caddr_t',
           'FLAC__STREAM_METADATA_CUESHEET_INDEX_OFFSET_LEN',
           '__blkcnt64_t', 'mkostemp', 'setstate',
           'FLAC__STREAM_METADATA_STREAMINFO_TOTAL_SAMPLES_LEN',
           '_IOS_NOCREATE', '_Exit',
           'FLAC__stream_encoder_set_apodization', 'L_ctermid',
           '__vdprintf_chk', '_IO_TIED_PUT_GET', 'fseeko64',
           'FLAC__STREAM_DECODER_READ_METADATA', 'INT32_MAX',
           '__fprintf_chk', 'FLAC__stream_decoder_seek_absolute',
           'uint_fast64_t',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_LEAD_ARTIST',
           '__USE_LARGEFILE', '__USE_EXTERN_INLINES',
           'FLAC__STREAM_DECODER_READ_STATUS_ABORT', 'PTRDIFF_MIN',
           'setbuffer', '_IO_BE', '_FEATURES_H', '__WCLONE',
           'FLAC__STREAM_METADATA_SEEKPOINT_LENGTH',
           'FLAC__STREAM_DECODER_LENGTH_STATUS_ERROR',
           'FLAC__STREAM_ENCODER_INIT_STATUS_ENCODER_ERROR',
           'WCONTINUED', 'SEEK_DATA', 'drand48_r', 'INT64_C',
           '__REDIRECT_NTH_LDBL', 'stdin', 'pthread_cond_t',
           '__rlim64_t', '_BITS_TYPES_H', 'uintptr_t',
           'FLAC__ENTROPY_CODING_METHOD_TYPE_LEN', 'PDP_ENDIAN',
           '__ctype_get_mb_cur_max',
           'FLAC__STREAM_METADATA_CUESHEET_NUM_TRACKS_LEN',
           'FLAC__STREAM_ENCODER_UNINITIALIZED',
           'FLAC__format_vorbiscomment_entry_name_is_legal',
           'strtoll_l', 'FLAC__stream_decoder_init_ogg_stream',
           'vprintf', 'FLAC__STREAM_SYNC_STRING', '__rlim_t',
           '__FLOAT_WORD_ORDER',
           'FLAC__stream_encoder_get_bits_per_sample',
           'FLAC__StreamDecoderTellStatus',
           'FLAC__metadata_object_seektable_delete_point',
           '_DEFAULT_SOURCE', '__sprintf_chk', 'int_fast32_t',
           'lcong48_r', 'secure_getenv',
           'FLAC__metadata_object_clone', 'jrand48',
           '_XOPEN_SOURCE_EXTENDED',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_FISH',
           'fileno_unlocked', '_IO_off_t',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_UNLINK_ERROR',
           'WNOWAIT', 'FLAC__STREAM_METADATA_LENGTH_LEN',
           'FLAC__FRAME_HEADER_ZERO_PAD_LEN',
           'FLAC__stream_decoder_init_FILE', '_IO_UNBUFFERED',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_DURING_RECORDING',
           'FLAC__metadata_object_cuesheet_track_new', 'printf',
           'FLAC__STREAM_DECODER_ERROR_STATUS_BAD_HEADER',
           'FLAC__METADATA_CHAIN_STATUS_UNLINK_ERROR',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_OFFSET_LEN',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_ERROR_OPENING_FILE',
           'FLAC__stream_decoder_finish', '_IOS_ATEND',
           'INT_FAST8_MAX', '__clock_t', 'fsfilcnt_t', 'ino64_t',
           'int8_t', '__obstack_printf_chk', '__WIFSTOPPED',
           'INTPTR_MAX',
           'FLAC__STREAM_DECODER_ERROR_STATUS_UNPARSEABLE_STREAM',
           'FLAC__metadata_iterator_new',
           'FLAC__stream_encoder_init_file',
           'FLAC__metadata_object_picture_set_data', 'srand48',
           'FLAC__FRAME_NUMBER_TYPE_SAMPLE_NUMBER',
           'FLAC__stream_encoder_set_ogg_serial_number',
           'FLAC__metadata_object_cuesheet_track_insert_index',
           '_IO_flockfile', 'drand48_data',
           'FLAC__STREAM_DECODER_OGG_ERROR',
           'FLAC__STREAM_DECODER_INIT_STATUS_ALREADY_INITIALIZED',
           'FLAC__stream_encoder_get_verify_decoder_state',
           'WINT_MAX', 'FLAC__stream_encoder_get_do_escape_coding',
           'fscanf', '__key_t',
           'FLAC__STREAM_METADATA_PICTURE_MIME_TYPE_LENGTH_LEN',
           'FLAC__uint8', 'FLAC__SUBFRAME_TYPE_LPC_BYTE_ALIGNED_MASK',
           '__obstack_vprintf_chk', '__uid_t', 'FLAC__FrameFooter',
           '__int8_t', '__FD_ZERO_STOS',
           'FLAC__format_seektable_is_legal',
           'FLAC__STREAM_METADATA_PICTURE_HEIGHT_LEN', 'WTERMSIG',
           '__pthread_mutex_s', 'obstack_vprintf', 'atol',
           '__printf_chk', 'a64l', 'random', '_IO_putc',
           'N16pthread_rwlock_t4DOT_14E',
           'FLAC__metadata_object_seektable_template_append_placeholders',
           'FLAC__metadata_object_vorbiscomment_entry_matches',
           'FLAC__STREAM_DECODER_SEEK_STATUS_OK',
           'FLAC__SUBFRAME_LPC_QLP_SHIFT_LEN', '__GNU_LIBRARY__',
           '_BITS_TYPESIZES_H', 'UINT32_MAX', 'mode_t', 'strtoull',
           '__STDLIB_MB_LEN_MAX', '__USE_LARGEFILE64',
           'FLAC__STREAM_SYNC',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE2_PARAMETER_LEN',
           '__USE_XOPEN2KXSI', 'strtol',
           'FLAC__METADATA_CHAIN_STATUS_MEMORY_ALLOCATION_ERROR',
           '__underflow', 'htobe64',
           'FLAC__metadata_object_cuesheet_insert_blank_track',
           'grantpt', '_IO_2_1_stdin_', 'pthread_mutexattr_t',
           'strtof', 'fgetpos64', 'uint',
           'FLAC__stream_encoder_set_do_mid_side_stereo',
           'FLAC__STREAM_METADATA_STREAMINFO_SAMPLE_RATE_LEN',
           'FLAC__StreamEncoderInitStatusString', 'fputs',
           '_IO_LINE_BUF', 'FLAC__FRAME_HEADER_BITS_PER_SAMPLE_LEN',
           'fd_mask', 'strtof_l',
           'FLAC__metadata_object_vorbiscomment_entry_to_name_value_pair',
           'cookie_seek_function_t',
           'FLAC__STREAM_ENCODER_VERIFY_DECODER_ERROR', 'strtoq',
           '_IO_padn', '__loff_t', 'UINTMAX_MAX', 'l64a', 'FD_CLR',
           '_G_config_h', '____mbstate_t_defined',
           'FLAC__stream_encoder_get_state', 'erand48_r',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_UNDEFINED',
           '_IO_FLAGS2_MMAP', 'setstate_r', 'key_t', 'erand48',
           'uint_least64_t', 'ptsname_r', '__lldiv_t_defined',
           'strtod_l',
           'FLAC__SUBFRAME_TYPE_CONSTANT_BYTE_ALIGNED_MASK',
           'FLAC__EntropyCodingMethodTypeString', '_IO_getc',
           'FLAC__EntropyCodingMethod_PartitionedRice',
           'FLAC__STREAM_METADATA_HEADER_LENGTH', 'FLAC__Subframe',
           'FOPEN_MAX',
           'FLAC__stream_decoder_process_until_end_of_metadata',
           'FLAC__int64', '_IO_DELETE_DONT_CLOSE', 'INTMAX_MAX',
           'FLAC__FRAME_HEADER_RESERVED_LEN', 'FLAC__uint64',
           '_G_fpos_t', 'FLAC__STREAM_DECODER_SEARCH_FOR_METADATA',
           'INT64_MIN', 'FLAC__STREAM_ENCODER_WRITE_STATUS_OK',
           '__fgets_chk',
           'FLAC__STREAM_METADATA_CUESHEET_LEAD_IN_LEN', 'fcvt_r',
           'FLAC__STREAM_METADATA_STREAMINFO_CHANNELS_LEN',
           'FLAC__format_vorbiscomment_entry_is_legal',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_WRITE_ERROR',
           'UINT_LEAST8_MAX', '__int16_t', '__bos',
           'FLAC__metadata_simple_iterator_new', 'be32toh',
           '_STDLIB_H', 'FLAC__StreamEncoderWriteStatusString',
           'FILE', '__ssize_t', 'flockfile', 'comparison_fn_t',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_PARAMETER_LEN',
           'FLAC__STREAM_DECODER_INIT_STATUS_MEMORY_ALLOCATION_ERROR',
           'FLAC__StreamDecoderStateString', '_IO_peekc_locked',
           'FLAC__StreamDecoderSeekStatusString', 'INT_LEAST64_MIN',
           'qgcvt', 'FLAC__format_sample_rate_is_valid',
           'FLAC__metadata_chain_read_ogg_with_callbacks', 'int16_t',
           'cuserid', 'FLAC__metadata_simple_iterator_is_writable',
           'FLAC__StreamDecoderWriteStatus', 'UINT_LEAST32_MAX',
           '__io_write_fn', '__warnattr',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_METADATA',
           '__SIZEOF_PTHREAD_COND_T', 'random_data',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_BITS_PER_SAMPLE',
           'fgetpos', 'FLAC__stream_decoder_process_single',
           'FLAC__STREAM_ENCODER_TELL_STATUS_UNSUPPORTED',
           'FLAC__STREAM_ENCODER_WRITE_STATUS_FATAL_ERROR',
           'FLAC__StreamEncoderWriteStatus',
           'FLAC__metadata_object_seektable_template_append_spaced_points',
           'FLAC__FRAME_HEADER_BLOCKING_STRATEGY_LEN',
           'posix_memalign',
           'FLAC__FRAME_HEADER_CHANNEL_ASSIGNMENT_LEN',
           'WIFCONTINUED', 'FLAC__Subframe_Verbatim', 'fputc',
           'vdprintf', 'FLAC__StreamEncoderSeekCallback',
           'FLAC__StreamDecoderLengthCallback', '__getdelim',
           '__overflow', '__SIZEOF_PTHREAD_BARRIER_T',
           '__USE_XOPEN2K', 'fd_set', 'quad_t', '__FD_SETSIZE',
           'FLAC__stream_decoder_get_bits_per_sample', 'ungetc',
           'FLAC__METADATA_CHAIN_STATUS_NOT_WRITABLE', 'htole16',
           'FLAC__StreamDecoderReadCallback',
           'FLAC__StreamMetadata_Picture_TypeString',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_OTHER',
           'FLAC__STREAM_ENCODER_IO_ERROR',
           'FLAC__stream_decoder_set_metadata_ignore_all', 'seed48_r',
           'FLAC__MAX_RICE_PARTITION_ORDER', '_IO_LINKED',
           '__timespec_defined', 'vsnprintf', '_IO_FILE_plus',
           'FLAC__METADATA_CHAIN_STATUS_READ_ERROR',
           'FLAC__stream_encoder_new', '_IO_va_list',
           'FLAC__metadata_simple_iterator_get_block_length',
           'FLAC__METADATA_CHAIN_STATUS_ERROR_OPENING_FILE',
           'clockid_t', '_IO_size_t',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_RAW_LEN',
           'UINTPTR_MAX', 'fwrite', 'caddr_t',
           'FLAC__stream_decoder_process_until_end_of_stream',
           'uint16_t', 'timespec', 'FLAC__IOCallback_Write',
           '__vsnprintf_chk', '__SIZEOF_PTHREAD_BARRIERATTR_T',
           'INT16_MIN', 'INT16_C', 'FLAC__StreamEncoderTellStatus',
           '_IOS_INPUT', 'vasprintf', 'L_tmpnam',
           'FLAC__stream_encoder_finish',
           '__PTHREAD_RWLOCK_INT_FLAGS_SHARED', 'getdelim',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_NOT_A_FLAC_FILE',
           '_IO_DONT_CLOSE', 'alloca', 'INT_LEAST64_MAX',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_FRONT_COVER',
           '__uflow', 'FLAC__MIN_BLOCK_SIZE', 'sys_nerr', 'fileno',
           '_IO_BAD_SEEN', '__USE_MISC', '__intptr_t',
           'FLAC__StreamMetadata_CueSheet_Track',
           '__BIT_TYPES_DEFINED__', 'putw', 'htole64',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_NUMBER_LEN', 'puts',
           '__syscall_slong_t', '__compar_d_fn_t', '__u_long',
           'obstack', 'aligned_alloc', 'WIFEXITED', 'RAND_MAX',
           'FLAC__stream_decoder_set_metadata_respond', 'nrand48_r',
           'FLAC__stream_encoder_process_interleaved', 'tmpnam_r',
           'putc', 'FLAC__METADATA_CHAIN_STATUS_NOT_A_FLAC_FILE',
           'FLAC__metadata_simple_iterator_insert_block_after',
           'rand', '_IO_HEX',
           'FLAC__stream_encoder_set_compression_level', 'fread',
           '_STDINT_H', '__PTHREAD_MUTEX_HAVE_PREV', 'SIG_ATOMIC_MAX',
           'tmpnam', '__OFF_T_MATCHES_OFF64_T', 'WSTOPSIG',
           'FLAC__StreamEncoderInitStatus', 'WNOHANG',
           'FLAC__STREAM_METADATA_STREAMINFO_MIN_FRAME_SIZE_LEN',
           'N4wait3DOT_2E', '__dev_t', 'FLAC__FRAME_HEADER_SYNC_LEN',
           '_sys_errlist', 'FLAC__StreamMetadata_Unknown', 'pselect',
           'FILENAME_MAX', 'L_cuserid', '_SYS_SYSMACROS_H',
           'FLAC_API_VERSION_REVISION', 'UINT16_MAX', 'drand48',
           'EXIT_SUCCESS', 'FLAC__StreamDecoderMetadataCallback',
           'jrand48_r',
           'FLAC__metadata_object_seektable_insert_point', 'fgetc',
           '__dprintf_chk', 'u_long',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_BACK_COVER',
           'UINT_FAST32_MAX', 'vsscanf', 'qfcvt', 'strtold_l',
           'INT_FAST32_MIN', 'vsprintf',
           'FLAC__StreamEncoderReadStatus', 'rename', 'loff_t',
           'SIG_ATOMIC_MIN', 'ushort', '__USE_POSIX199506',
           'FLAC__metadata_object_is_equal',
           'FLAC__STREAM_DECODER_SEARCH_FOR_FRAME_SYNC', 'stdout',
           'FLAC__Frame', 'FLAC__IOCallbacks', '__BIG_ENDIAN',
           'uint64_t', '__u_char', 'uintmax_t',
           'FLAC__stream_encoder_get_total_samples_estimate',
           '__WTERMSIG', 'u_int',
           'FLAC__metadata_object_seektable_template_sort',
           'FLAC__FrameNumberTypeString', 'int_fast16_t', 'initstate',
           '__blkcnt_t', 'INT32_C',
           'FLAC__STREAM_METADATA_VORBIS_COMMENT_NUM_COMMENTS_LEN',
           'FLAC__FRAME_HEADER_CRC_LEN', 'pthread_t', '_IO_seekpos',
           'INT_FAST16_MAX',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_RENAME_ERROR',
           'getc', 'qfcvt_r',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE',
           '__USE_XOPEN2K8XSI',
           'FLAC__StreamMetadata_VorbisComment_Entry', 'fsblkcnt64_t',
           'FLAC__stream_encoder_set_sample_rate', '_IO_RIGHT',
           'FLAC__stream_encoder_init_stream',
           'FLAC__METADATA_TYPE_APPLICATION', 'FLAC__StreamMetadata',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_ARTIST',
           'FLAC__stream_decoder_new', 'getw', '_OLD_STDIO_MAGIC',
           'fread_unlocked', 'FLAC__MAX_METADATA_TYPE',
           'FLAC__Subframe_Fixed', 'FLAC__stream_encoder_delete',
           '__snprintf_chk', '_IO_IS_FILEBUF', 'SEEK_SET', 'SIZE_MAX',
           'FLAC__STREAM_DECODER_READ_STATUS_END_OF_STREAM',
           'FLAC__stream_encoder_set_do_exhaustive_model_search',
           'FLAC__metadata_object_cuesheet_track_clone',
           '_IOS_OUTPUT',
           'FLAC__stream_encoder_get_qlp_coeff_precision',
           'FLAC__SUBSET_MAX_LPC_ORDER_48000HZ', 'UINT_LEAST16_MAX',
           '__vsprintf_chk',
           'FLAC__STREAM_METADATA_PICTURE_COLORS_LEN', '_IO_lock_t',
           'setbuf', 'FLAC__STREAM_DECODER_UNINITIALIZED',
           'FLAC__SUBFRAME_TYPE_CONSTANT', '__REDIRECT_LDBL',
           'FLAC__EntropyCodingMethodType', 'srandom_r',
           'FLAC__metadata_object_vorbiscomment_insert_comment',
           '__fread_unlocked_chk', 'FLAC__metadata_get_cuesheet',
           'FLAC__FRAME_HEADER_SAMPLE_RATE_LEN', 'INT_FAST32_MAX',
           'FLAC__STREAM_ENCODER_INIT_STATUS_NOT_STREAMABLE',
           'FLAC__STREAM_ENCODER_INIT_STATUS_INVALID_QLP_COEFF_PRECISION',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_FILE_ICON',
           '__int64_t', 'nrand48', 'pthread_mutex_t',
           '_IO_FLAGS2_NOTCANCEL', 'uint32_t',
           'FLAC__stream_decoder_get_channel_assignment',
           'FLAC__SUBFRAME_TYPE_FIXED',
           'FLAC__stream_decoder_set_metadata_respond_all',
           '__have_pthread_attr_t', 'suseconds_t', 'be16toh',
           'FLAC__STREAM_METADATA_STREAMINFO_MAX_BLOCK_SIZE_LEN',
           'WSTOPPED', 'fseek',
           'FLAC__STREAM_DECODER_SEEK_STATUS_UNSUPPORTED',
           'FLAC__metadata_chain_check_if_tempfile_needed',
           'FLAC__metadata_chain_write_with_callbacks_and_tempfile',
           'dprintf', '__LITTLE_ENDIAN', '_IO_LEFT',
           'FLAC__STREAM_METADATA_TYPE_LEN',
           'FLAC__SUBFRAME_ZERO_PAD_LEN', 'mkstemps64',
           'pthread_condattr_t', 'pthread_once_t',
           'FLAC__MAX_QLP_COEFF_PRECISION', '__fsid_t',
           'FLAC__StreamDecoderProtected', '__wcstombs_chk', 'fflush',
           'timeval',
           'FLAC__metadata_object_vorbiscomment_set_comment',
           'INT64_MAX', '__uint32_t', '__USE_XOPEN2K8',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_INTERNAL_ERROR',
           '_STRUCT_TIMEVAL',
           'FLAC__metadata_simple_iterator_get_application_id',
           'ldiv', 'fflush_unlocked', 'ptsname',
           'FLAC__stream_encoder_set_min_residual_partition_order',
           'FLAC__stream_encoder_get_max_residual_partition_order',
           'FLAC__STREAM_DECODER_READ_STATUS_CONTINUE', 'setenv',
           'P_tmpdir', '__ino64_t', '__u_quad_t', 'int32_t',
           '__u_short', 'FLAC__StreamDecoderTellStatusString',
           'FLAC__stream_encoder_get_rice_parameter_search_dist',
           'off64_t', 'dev_t', 'blksize_t',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ORDER_LEN',
           '_IO_SHOWPOINT', 'FLAC__StreamEncoderWriteCallback',
           '_IO_sgetn', 'FLAC__StreamDecoderEofCallback',
           '_BITS_PTHREADTYPES_H', 'FLAC__FrameNumberType',
           'FLAC__StreamMetadata_CueSheet_Index', 'WIFSTOPPED',
           'FLAC__metadata_iterator_delete_block',
           'FLAC__StreamEncoder', 'register_t', 'lrand48_r',
           'gnu_dev_minor', '_SYS_SELECT_H',
           'FLAC__stream_encoder_get_min_residual_partition_order',
           '__vasprintf_chk', 'renameat',
           'FLAC__STREAM_ENCODER_READ_STATUS_ABORT', '_G_fpos64_t',
           'FLAC__STREAM_METADATA_CUESHEET_MEDIA_CATALOG_NUMBER_LEN',
           'popen', 'FLAC__metadata_chain_read_ogg', '_ISOC95_SOURCE',
           'FLAC__stream_encoder_get_verify',
           'FLAC__StreamDecoderLengthStatus', '_ISOC99_SOURCE',
           'FLAC__metadata_chain_read', 'freopen', '__nlink_t',
           '__compar_fn_t', 'FLAC__StreamDecoderWriteStatusString',
           'FLAC__STREAM_METADATA_STREAMINFO_LENGTH', 'tempnam',
           'FLAC__STREAM_METADATA_PICTURE_DEPTH_LEN',
           '__syscall_ulong_t', 'lldiv', 'tmpfile64', 'rpmatch',
           'FLAC__metadata_get_picture', 'FLAC__byte', 'gcvt',
           'pclose', 'FLAC__StreamDecoderState', '__fdelt_warn',
           'llabs', 'FLAC__stream_decoder_delete',
           'FLAC__stream_encoder_get_verify_decoder_error_stats',
           '_IO_2_1_stderr_', 'unlockpt', '__clock_t_defined',
           '__pid_t', '_IO_SHOWPOS', '__codecvt_ok', 'fgets',
           '_IO_MAGIC', 'FLAC__StreamDecoder', 'ctermid', '__id_t',
           'cookie_io_functions_t', 'FLAC__int16', '_IO_feof',
           'FLAC__STREAM_ENCODER_MEMORY_ALLOCATION_ERROR', 'gid_t',
           'fgetc_unlocked', 'cookie_close_function_t',
           '_IO_UPPERCASE', '__int32_t',
           'FLAC__StreamDecoderReadStatusString',
           'FLAC__stream_encoder_set_loose_mid_side_stereo',
           '_IO_EOF_SEEN', '__timer_t_defined', 'exit',
           'FLAC__STREAM_METADATA_SEEKPOINT_STREAM_OFFSET_LEN',
           '__clockid_t', 'getchar', 'mbstowcs', '_IO_FIXED',
           'mkdtemp', 'FLAC__STREAM_DECODER_LENGTH_STATUS_OK',
           'FLAC__STREAM_ENCODER_VERIFY_MISMATCH_IN_AUDIO_DATA',
           'FLAC__format_picture_is_legal',
           'FLAC__StreamEncoderSeekStatusString',
           'FLAC__StreamEncoderReadCallback',
           'FLAC__format_sample_rate_is_subset', 'FD_ISSET',
           '__io_close_fn', 'FLAC__stream_encoder_set_blocksize',
           'FLAC__METADATA_CHAIN_STATUS_ILLEGAL_INPUT',
           'FLAC__FRAME_FOOTER_CRC_LEN',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_ILLEGAL_INPUT',
           'FLAC__SUBSET_MAX_BLOCK_SIZE_48000HZ', 'fcloseall',
           'FLAC__stream_encoder_set_verify',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_ISRC_LEN', 'INT8_C',
           'seed48', 'putchar_unlocked',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_LYRICIST',
           '_SYS_CDEFS_H',
           'FLAC__STREAM_DECODER_WRITE_STATUS_CONTINUE', 'SEEK_END',
           '_IO_peekc', '__WNOTHREAD',
           'FLAC__FRAME_NUMBER_TYPE_FRAME_NUMBER',
           'canonicalize_file_name', 'malloc',
           'FLAC__STREAM_DECODER_MEMORY_ALLOCATION_ERROR',
           'sys_errlist', '__CONCAT', 'bsearch', 'clearerr_unlocked',
           'FLAC__STREAM_ENCODER_SEEK_STATUS_OK',
           'FLAC__metadata_object_seektable_is_legal',
           '_IO_IN_BACKUP', '_IOS_NOREPLACE',
           'FLAC__Metadata_SimpleIteratorStatus', '_SIGSET_H_types',
           '_ISOC11_SOURCE',
           'FLAC__metadata_simple_iterator_get_block',
           'FLAC__ChannelAssignment', 'obstack_printf',
           '____FILE_defined', '__fdelt_chk', 'INT16_MAX',
           'FLAC__metadata_iterator_init',
           'FLAC__metadata_object_seektable_template_append_points',
           'SEEK_CUR',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_VIDEO_SCREEN_CAPTURE',
           '__locale_struct', 'FLAC__SUBFRAME_TYPE_LEN',
           '__SIZEOF_PTHREAD_MUTEX_T', '__USE_UNIX98', '_IO_STDIO',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_RESERVED_LEN',
           'fopen', 'FLAC__metadata_simple_iterator_is_last',
           'FLAC__stream_decoder_get_state',
           'FLAC__METADATA_CHAIN_STATUS_READ_WRITE_MISMATCH',
           'FLAC__metadata_iterator_delete',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_NOT_WRITABLE',
           'useconds_t', 'FLAC__StreamMetadata_VorbisComment',
           '_IO_marker',
           'FLAC__metadata_object_cuesheet_resize_tracks',
           'FLAC__StreamEncoderPrivate',
           'FLAC__METADATA_TYPE_VORBIS_COMMENT',
           'FLAC__stream_encoder_get_channels', '_IO_OCT',
           'FLAC__metadata_object_cuesheet_track_delete', '__daddr_t',
           'quick_exit', '_IO_cookie_file', '__sig_atomic_t',
           '__blksize_t',
           'FLAC__stream_encoder_get_do_exhaustive_model_search',
           'sigset_t', 'FLAC__metadata_object_cuesheet_delete_track',
           'pthread_barrierattr_t',
           'FLAC__STREAM_ENCODER_READ_STATUS_UNSUPPORTED',
           'FLAC__stream_decoder_get_sample_rate',
           'N25FLAC__EntropyCodingMethod4DOT_23E', '_IOS_APPEND',
           'N20FLAC__StreamMetadata4DOT_52E', 'FLAC__VENDOR_STRING',
           '__io_seek_fn', 'FLAC__stream_encoder_set_channels',
           'FLAC__STREAM_METADATA_STREAMINFO_MIN_BLOCK_SIZE_LEN',
           'UINT64_C',
           'FLAC__STREAM_METADATA_CUESHEET_TRACK_NUM_INDICES_LEN',
           'getenv', 'htobe32', 'atoi', 'BUFSIZ',
           'FLAC__StreamMetadata_Picture_Type', 'wcstombs',
           'INT_LEAST32_MIN', 'atof', 'strtoull_l', 'freopen64',
           'FLAC__StreamEncoderState', 'FLAC__stream_encoder_process',
           'FLAC__IOCallback_Close',
           'FLAC__metadata_simple_iterator_get_block_offset',
           '_IO_UNIFIED_JUMPTABLES',
           'FLAC__StreamDecoderSeekCallback', 'getc_unlocked',
           'FLAC__Metadata_Iterator', 'tmpfile',
           'FLAC__metadata_object_vorbiscomment_replace_comment',
           '_ENDIAN_H', '_IO_vfscanf', 'cookie_read_function_t',
           'FLAC__METADATA_CHAIN_STATUS_RENAME_ERROR',
           'FLAC__MetadataType',
           'FLAC__STREAM_DECODER_TELL_STATUS_ERROR',
           'FLAC__stream_encoder_set_bits_per_sample',
           'FLAC__metadata_chain_status', 'blkcnt64_t',
           'FLAC__METADATA_CHAIN_STATUS_SEEK_ERROR', 'ecvt_r',
           'int_least16_t', 'sscanf',
           'FLAC__STREAM_ENCODER_INIT_STATUS_UNSUPPORTED_CONTAINER',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_MEMORY_ALLOCATION_ERROR',
           'FD_SET', 'mrand48', '_STDIO_H',
           'FLAC__CHANNEL_ASSIGNMENT_INDEPENDENT',
           'FLAC__metadata_chain_new', 'FLAC__EntropyCodingMethod',
           'FLAC__metadata_object_delete', '_IO_FLAGS2_USER_WBUF',
           '__STRING', 'int64_t', 'FLAC__uint32', 'WEXITSTATUS',
           'le64toh', '__GNUC_PREREQ', 'BYTE_ORDER', 'posix_openpt',
           'FLAC__STREAM_ENCODER_INIT_STATUS_ALREADY_INITIALIZED',
           'FLAC__METADATA_SIMPLE_ITERATOR_STATUS_READ_ERROR',
           'lldiv_t', '__uint64_t', '__sigset_t', 'gnu_dev_makedev',
           'FLAC__StreamEncoderMetadataCallback', '_IO_MAGIC_MASK',
           '__SIZEOF_PTHREAD_RWLOCKATTR_T', '__PDP_ENDIAN',
           'FLAC__SUBFRAME_TYPE_LPC', 'mkstemp', 'int_fast64_t',
           'FLAC__format_seektable_sort',
           'FLAC__stream_encoder_get_sample_rate',
           'FLAC__metadata_iterator_get_block_type', 'fsid_t',
           'FLAC__metadata_iterator_get_block', '_LARGEFILE64_SOURCE',
           '__va_arg_pack', 'FD_SETSIZE',
           'FLAC__StreamDecoderErrorCallback',
           'FLAC__SUBFRAME_TYPE_VERBATIM_BYTE_ALIGNED_MASK',
           '_BITS_BYTESWAP_H', '__codecvt_error',
           'FLAC__metadata_object_picture_set_description', '__ino_t',
           '__wctomb_chk', 'FLAC__metadata_chain_write',
           '_SIGSET_NWORDS', '__va_arg_pack_len', 'intmax_t',
           'FLAC__ENTROPY_CODING_METHOD_PARTITIONED_RICE_ESCAPE_PARAMETER',
           '__bos0', 'FLAC__stream_encoder_init_ogg_file',
           '__SYSCALL_WORDSIZE',
           'FLAC__STREAM_ENCODER_SEEK_STATUS_ERROR', 'strtoul_l',
           'setlinebuf', 'int_least32_t', 'uint_fast32_t',
           'FLAC__stream_decoder_set_metadata_ignore', '__socklen_t',
           'FLAC__stream_encoder_set_total_samples_estimate',
           '__USE_ISOC11', 'EXIT_FAILURE',
           'FLAC__STREAM_DECODER_ERROR_STATUS_FRAME_CRC_MISMATCH',
           'FLAC__stream_decoder_init_ogg_file',
           'FLAC__stream_encoder_get_max_lpc_order',
           'FLAC__StreamDecoderReadStatus', 'pid_t', 'setvbuf',
           '__codecvt_noconv', '_IOLBF',
           'FLAC__STREAM_METADATA_PICTURE_TYPE_BAND', 'int_least8_t',
           'ecvt', 'NFDBITS']
