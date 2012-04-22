from ctypes import *

_libraries = {}
_libraries['/usr/lib/libespeak.so'] = CDLL('/usr/lib/libespeak.so')
STRING = c_char_p
WSTRING = c_wchar_p


__u_quad_t = c_ulonglong
__UQUAD_TYPE = __u_quad_t # alias
# __USECONDS_T_TYPE = __U32_TYPE # alias
class _IO_FILE(Structure):
    pass
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libespeak.so'], 'stderr')
stderr = stderr # alias
N_SPEECH_PARAM = 15
espeakLINELENGTH = 13
espeakEMPHASIS = 12
espeakRESERVED2 = 11
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
BUFSIZ = _IO_BUFSIZ # alias
__RLIM64_T_TYPE = __UQUAD_TYPE # alias
espeakWORDGAP = 7
espeakCAPITALS = 6
espeakPUNCTUATION = 5
espeakINTONATION = 9
espeakPITCH = 3
espeakVOLUME = 2
# __RLIM_T_TYPE = __ULONGWORD_TYPE # alias
espeakRATE = 1
# __SUSECONDS_T_TYPE = __SLONGWORD_TYPE # alias
# __SWORD_TYPE = int # alias
EE_BUFFER_FULL = 1
# __UID_T_TYPE = __U32_TYPE # alias
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libespeak.so'], 'stdin')
stdin = stdin # alias
espeakPUNCT_SOME = 2
espeakPUNCT_ALL = 1
# __TIME_T_TYPE = __SLONGWORD_TYPE # alias
__quad_t = c_longlong
__S64_TYPE = __quad_t # alias
espeakPUNCT_NONE = 0
__SQUAD_TYPE = __quad_t # alias
__OFF64_T_TYPE = __SQUAD_TYPE # alias
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
espeakEVENT_SAMPLERATE = 8
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
espeakRANGE = 4
__FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
# __FSFILCNT_T_TYPE = __ULONGWORD_TYPE # alias
# __S32_TYPE = int # alias
# __PID_T_TYPE = __S32_TYPE # alias
__FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
# __DADDR_T_TYPE = __S32_TYPE # alias
__DEV_T_TYPE = __UQUAD_TYPE # alias
# __CLOCK_T_TYPE = __SLONGWORD_TYPE # alias
__gnuc_va_list = STRING
_IO_va_list = __gnuc_va_list # alias
# __CLOCKID_T_TYPE = __S32_TYPE # alias
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
# __BLKCNT_T_TYPE = __SLONGWORD_TYPE # alias
EE_OK = 0
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
def offsetof(TYPE,MEMBER): return __builtin_offsetof (TYPE, MEMBER) # macro
def getc(_fp): return _IO_getc (_fp) # macro
# __MODE_T_TYPE = __U32_TYPE # alias
AUDIO_OUTPUT_SYNCHRONOUS = 2
espeakEVENT_MARK = 3
def __STRING(x): return #x # macro
EE_NOT_FOUND = 2
# __NLINK_T_TYPE = __UWORD_TYPE # alias
# _G_wint_t = wint_t # alias
# _IO_wint_t = _G_wint_t # alias
EE_INTERNAL_ERROR = -1
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
espeakVOICETYPE = 14
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
# __KEY_T_TYPE = __S32_TYPE # alias
# __INO_T_TYPE = __ULONGWORD_TYPE # alias
espeakRESERVED1 = 10
__INO64_T_TYPE = __UQUAD_TYPE # alias
# __ID_T_TYPE = __U32_TYPE # alias
espeakOPTIONS = 8
# _G_wchar_t = wchar_t # alias
espeakEVENT_PHONEME = 7
POS_CHARACTER = 1
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
# _IO_iconv_t = _G_iconv_t # alias
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
_G_HAVE_SYS_WAIT = 1 # Variable c_int '1'
_IO_HAVE_SYS_WAIT = _G_HAVE_SYS_WAIT # alias
size_t = c_uint
_G_size_t = size_t # alias
# _IO_file_flags = _flags # alias
def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
class _G_fpos64_t(Structure):
    pass
__off64_t = __quad_t
_G_fpos64_t._pack_ = 4
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
__uid_t = c_uint
_G_uid_t = __uid_t # alias
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
_G_va_list = __gnuc_va_list # alias
# __SWBLK_T_TYPE = __SLONGWORD_TYPE # alias
def _G_ARGS(ARGLIST): return ARGLIST # macro
# __GID_T_TYPE = __U32_TYPE # alias
__ssize_t = c_int
_G_ssize_t = __ssize_t # alias
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
POS_SENTENCE = 3
POS_WORD = 2
def _G_FSTAT64(fd,buf): return __fxstat64 (_STAT_VER, fd, buf) # macro
# _G_VTABLE_LABEL_PREFIX_ID = __vt_ # alias
# __FSBLKCNT_T_TYPE = __ULONGWORD_TYPE # alias
_G_off64_t = __off64_t # alias
espeakEVENT_MSG_TERMINATED = 6
espeakEVENT_END = 5
espeakEVENT_PLAY = 4
# _G_LSEEK64 = __lseek64 # alias
__pid_t = c_int
_G_pid_t = __pid_t # alias
espeakEVENT_SENTENCE = 2
espeakEVENT_WORD = 1
# NULL = __null # alias
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
espeakEVENT_LIST_TERMINATED = 0
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libespeak.so'], 'stdout')
stdout = stdout # alias
espeakSILENCE = 0
# _G_MMAP64 = __mmap64 # alias
__codecvt_noconv = 3
__codecvt_error = 2
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
__codecvt_partial = 1
__codecvt_ok = 0
__U64_TYPE = __u_quad_t # alias
def _PARAMS(protos): return __P(protos) # macro
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
AUDIO_OUTPUT_PLAYBACK = 0
_IO_pos_t = _G_fpos_t # alias
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
# _G_OPEN64 = __open64 # alias
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
_G_off_t = __off_t # alias
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
# def __LDBL_REDIR(name,proto): return name proto # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
_IO_pid_t = _G_pid_t # alias
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
__BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
# __BLKSIZE_T_TYPE = __SLONGWORD_TYPE # alias
def __P(args): return args # macro
def __PMT(args): return args # macro
_IO_ssize_t = _G_ssize_t # alias
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
_IO_size_t = _G_size_t # alias
_IO_off_t = _G_off_t # alias
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
_IO_off64_t = _G_off64_t # alias
_IO_uid_t = _G_uid_t # alias
def __CONCAT(x,y): return x ## y # macro
AUDIO_OUTPUT_SYNCH_PLAYBACK = 3
AUDIO_OUTPUT_RETRIEVAL = 1
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
# _G_stat64 = stat64 # alias
# __OFF_T_TYPE = __SLONGWORD_TYPE # alias
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
_G_HAVE_IO_GETLINE_INFO = 1 # Variable c_int '1'
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
_G_HAVE_SYS_CDEFS = 1 # Variable c_int '1'
_IO_LEFT = 2 # Variable c_int '2'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_IONBF = 2 # Variable c_int '2'
_IO_USER_BUF = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
EOF = -1 # Variable c_int '-0x000000001'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
_IO_SHOWBASE = 128 # Variable c_int '128'
L_cuserid = 9 # Variable c_int '9'
_IO_LINE_BUF = 512 # Variable c_int '512'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
_G_HAVE_LONG_DOUBLE_IO = 1 # Variable c_int '1'
espeakPHONEMES = 256 # Variable c_int '256'
_IO_SHOWPOINT = 256 # Variable c_int '256'
_G_config_h = 1 # Variable c_int '1'
_IOS_APPEND = 8 # Variable c_int '8'
__STDC_IEC_559__ = 1 # Variable c_int '1'
espeakSSML = 16 # Variable c_int '16'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
_G_USING_THUNKS = 1 # Variable c_int '1'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
__USE_ATFILE = 1 # Variable c_int '1'
__GLIBC_HAVE_LONG_LONG = 1 # Variable c_int '1'
TMP_MAX = 238328 # Variable c_int '238328'
_G_VTABLE_LABEL_PREFIX = '__vt_' # Variable STRING '(const char*)"__vt_"'
_IO_FIXED = 4096 # Variable c_int '4096'
FOPEN_MAX = 16 # Variable c_int '16'
_IO_DEC = 16 # Variable c_int '16'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
__USE_POSIX = 1 # Variable c_int '1'
_IO_NO_WRITES = 8 # Variable c_int '8'
_G_HAVE_IO_FILE_OPEN = 1 # Variable c_int '1'
__FILE_defined = 1 # Variable c_int '1'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
_STDIO_H = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944 # Variable c_uint '-72548352u'
_G_NAMES_HAVE_UNDERSCORE = 0 # Variable c_int '0'
ESPEAK_API_REVISION = 6 # Variable c_int '6'
_IO_NO_READS = 4 # Variable c_int '4'
__GLIBC_MINOR__ = 15 # Variable c_int '15'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
_IO_UPPERCASE = 512 # Variable c_int '512'
_IO_EOF_SEEN = 16 # Variable c_int '16'
espeakCHARS_16BIT = 4 # Variable c_int '4'
_G_HAVE_MMAP = 1 # Variable c_int '1'
espeakRATE_MAXIMUM = 450 # Variable c_int '450'
espeakRATE_MINIMUM = 80 # Variable c_int '80'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__FD_SETSIZE = 1024 # Variable c_int '1024'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
_G_VTABLE_LABEL_HAS_LENGTH = 1 # Variable c_int '1'
_IO_ERR_SEEN = 32 # Variable c_int '32'
_IOFBF = 0 # Variable c_int '0'
_IO_SKIPWS = 1 # Variable c_int '1'
SEEK_END = 2 # Variable c_int '2'
__USE_GNU = 1 # Variable c_int '1'
espeakCHARS_WCHAR = 3 # Variable c_int '3'
__USE_BSD = 1 # Variable c_int '1'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
_IO_IN_BACKUP = 256 # Variable c_int '256'
_IOS_NOREPLACE = 64 # Variable c_int '64'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
____FILE_defined = 1 # Variable c_int '1'
L_tmpnam = 20 # Variable c_int '20'
SEEK_CUR = 1 # Variable c_int '1'
_IOS_BIN = 128 # Variable c_int '128'
__USE_SVID = 1 # Variable c_int '1'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
__USE_ANSI = 1 # Variable c_int '1'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
__USE_MISC = 1 # Variable c_int '1'
__GLIBC__ = 2 # Variable c_int '2'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
_IO_RIGHT = 4 # Variable c_int '4'
_IO_OCT = 32 # Variable c_int '32'
_IOS_OUTPUT = 2 # Variable c_int '2'
_IOS_TRUNC = 16 # Variable c_int '16'
L_ctermid = 9 # Variable c_int '9'
_IO_HEX = 64 # Variable c_int '64'
__USE_FORTIFY_LEVEL = 0 # Variable c_int '0'
_IO_LINKED = 128 # Variable c_int '128'
__STDC_ISO_10646__ = 200009 # Variable c_long '200009l'
_IOS_NOCREATE = 32 # Variable c_int '32'
FILENAME_MAX = 4096 # Variable c_int '4096'
__STDC_IEC_559_COMPLEX__ = 1 # Variable c_int '1'
espeakRATE_NORMAL = 175 # Variable c_int '175'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
_FEATURES_H = 1 # Variable c_int '1'
espeakENDPAUSE = 4096 # Variable c_int '4096'
SEEK_DATA = 3 # Variable c_int '3'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
_IOS_INPUT = 1 # Variable c_int '1'
espeakKEEP_NAMEDATA = 8192 # Variable c_int '8192'
__USE_POSIX199506 = 1 # Variable c_int '1'
_IO_UNITBUF = 8192 # Variable c_int '8192'
_BITS_TYPES_H = 1 # Variable c_int '1'
SEEK_HOLE = 4 # Variable c_int '4'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
__USE_POSIX199309 = 1 # Variable c_int '1'
_IO_MAGIC_MASK = 4294901760 # Variable c_uint '-65536u'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 32 # Variable c_int '32'
espeakINITIALIZE_PHONEME_EVENTS = 1 # Variable c_int '1'
_IO_UNBUFFERED = 2 # Variable c_int '2'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_OLD_STDIO_MAGIC = 4206624768 # Variable c_uint '-88342528u'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN = 1 # Variable c_int '1'
_XOPEN_SOURCE = 700 # Variable c_int '700'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
SEEK_SET = 0 # Variable c_int '0'
espeakCHARS_UTF8 = 1 # Variable c_int '1'
_IOS_ATEND = 4 # Variable c_int '4'
_G_NEED_STDARG_H = 1 # Variable c_int '1'
_G_HAVE_PRINTF_FP = 1 # Variable c_int '1'
__USE_ISOC95 = 1 # Variable c_int '1'
espeakCHARS_8BIT = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
_G_HAVE_ATEXIT = 1 # Variable c_int '1'
_G_HAVE_BOOL = 1 # Variable c_int '1'
__mbstate_t_defined = 1 # Variable c_int '1'
_IO_INTERNAL = 8 # Variable c_int '8'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
espeakINITIALIZE_DONT_EXIT = 32768 # Variable c_int '32768'
_BSD_SOURCE = 1 # Variable c_int '1'
espeakCHARS_AUTO = 0 # Variable c_int '0'
_IOLBF = 1 # Variable c_int '1'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_G_int16_t = c_short
_G_int32_t = c_int
_G_uint16_t = c_ushort
_G_uint32_t = c_uint
vprintf = _libraries['/usr/lib/libespeak.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, __gnuc_va_list]
getchar = _libraries['/usr/lib/libespeak.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
FILE = _IO_FILE
fgetc_unlocked = _libraries['/usr/lib/libespeak.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/lib/libespeak.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/lib/libespeak.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/lib/libespeak.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/lib/libespeak.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/lib/libespeak.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/lib/libespeak.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/lib/libespeak.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/lib/libespeak.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/lib/libespeak.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libespeak.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libespeak.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libespeak.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libespeak.so'], '_sys_errlist')
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
__int64_t = c_longlong
__uint64_t = c_ulonglong
__dev_t = __u_quad_t
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = __u_quad_t
__mode_t = c_uint
__nlink_t = c_uint
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__clock_t = c_long
__rlim_t = c_ulong
__rlim64_t = __u_quad_t
__id_t = c_uint
__time_t = c_long
__useconds_t = c_uint
__suseconds_t = c_long
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__clockid_t = c_int
__timer_t = c_void_p
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = __quad_t
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = __u_quad_t
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = __u_quad_t
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_int
__socklen_t = c_uint

# values for enumeration 'espeak_EVENT_TYPE'
espeak_EVENT_TYPE = c_int # enum
class N12espeak_EVENT3DOT_8E(Union):
    pass
N12espeak_EVENT3DOT_8E._fields_ = [
    ('number', c_int),
    ('name', STRING),
]
class espeak_EVENT(Structure):
    pass
espeak_EVENT._fields_ = [
    ('type', espeak_EVENT_TYPE),
    ('unique_identifier', c_uint),
    ('text_position', c_int),
    ('length', c_int),
    ('audio_position', c_int),
    ('sample', c_int),
    ('user_data', c_void_p),
    ('id', N12espeak_EVENT3DOT_8E),
]

# values for enumeration 'espeak_POSITION_TYPE'
espeak_POSITION_TYPE = c_int # enum

# values for enumeration 'espeak_AUDIO_OUTPUT'
espeak_AUDIO_OUTPUT = c_int # enum

# values for enumeration 'espeak_ERROR'
espeak_ERROR = c_int # enum
espeak_Initialize = _libraries['/usr/lib/libespeak.so'].espeak_Initialize
espeak_Initialize.restype = c_int
espeak_Initialize.argtypes = [espeak_AUDIO_OUTPUT, c_int, STRING, c_int]
t_espeak_callback = CFUNCTYPE(c_int, POINTER(c_short), c_int, POINTER(espeak_EVENT))
espeak_SetSynthCallback = _libraries['/usr/lib/libespeak.so'].espeak_SetSynthCallback
espeak_SetSynthCallback.restype = None
espeak_SetSynthCallback.argtypes = [t_espeak_callback]
espeak_SetUriCallback = _libraries['/usr/lib/libespeak.so'].espeak_SetUriCallback
espeak_SetUriCallback.restype = None
espeak_SetUriCallback.argtypes = [CFUNCTYPE(c_int, c_int, STRING, STRING)]
espeak_Synth = _libraries['/usr/lib/libespeak.so'].espeak_Synth
espeak_Synth.restype = espeak_ERROR
espeak_Synth.argtypes = [c_void_p, size_t, c_uint, espeak_POSITION_TYPE, c_uint, c_uint, POINTER(c_uint), c_void_p]
espeak_Synth_Mark = _libraries['/usr/lib/libespeak.so'].espeak_Synth_Mark
espeak_Synth_Mark.restype = espeak_ERROR
espeak_Synth_Mark.argtypes = [c_void_p, size_t, STRING, c_uint, c_uint, POINTER(c_uint), c_void_p]
espeak_Key = _libraries['/usr/lib/libespeak.so'].espeak_Key
espeak_Key.restype = espeak_ERROR
espeak_Key.argtypes = [STRING]
espeak_Char = _libraries['/usr/lib/libespeak.so'].espeak_Char
espeak_Char.restype = espeak_ERROR
espeak_Char.argtypes = [c_wchar]

# values for enumeration 'espeak_PARAMETER'
espeak_PARAMETER = c_int # enum

# values for enumeration 'espeak_PUNCT_TYPE'
espeak_PUNCT_TYPE = c_int # enum
espeak_SetParameter = _libraries['/usr/lib/libespeak.so'].espeak_SetParameter
espeak_SetParameter.restype = espeak_ERROR
espeak_SetParameter.argtypes = [espeak_PARAMETER, c_int, c_int]
espeak_GetParameter = _libraries['/usr/lib/libespeak.so'].espeak_GetParameter
espeak_GetParameter.restype = c_int
espeak_GetParameter.argtypes = [espeak_PARAMETER, c_int]
espeak_SetPunctuationList = _libraries['/usr/lib/libespeak.so'].espeak_SetPunctuationList
espeak_SetPunctuationList.restype = espeak_ERROR
espeak_SetPunctuationList.argtypes = [WSTRING]
espeak_SetPhonemeTrace = _libraries['/usr/lib/libespeak.so'].espeak_SetPhonemeTrace
espeak_SetPhonemeTrace.restype = None
espeak_SetPhonemeTrace.argtypes = [c_int, POINTER(FILE)]
espeak_CompileDictionary = _libraries['/usr/lib/libespeak.so'].espeak_CompileDictionary
espeak_CompileDictionary.restype = None
espeak_CompileDictionary.argtypes = [STRING, POINTER(FILE), c_int]
class espeak_VOICE(Structure):
    pass
espeak_VOICE._fields_ = [
    ('name', STRING),
    ('languages', STRING),
    ('identifier', STRING),
    ('gender', c_ubyte),
    ('age', c_ubyte),
    ('variant', c_ubyte),
    ('xx1', c_ubyte),
    ('score', c_int),
    ('spare', c_void_p),
]
espeak_ListVoices = _libraries['/usr/lib/libespeak.so'].espeak_ListVoices
espeak_ListVoices.restype = POINTER(POINTER(espeak_VOICE))
espeak_ListVoices.argtypes = [POINTER(espeak_VOICE)]
espeak_SetVoiceByName = _libraries['/usr/lib/libespeak.so'].espeak_SetVoiceByName
espeak_SetVoiceByName.restype = espeak_ERROR
espeak_SetVoiceByName.argtypes = [STRING]
espeak_SetVoiceByProperties = _libraries['/usr/lib/libespeak.so'].espeak_SetVoiceByProperties
espeak_SetVoiceByProperties.restype = espeak_ERROR
espeak_SetVoiceByProperties.argtypes = [POINTER(espeak_VOICE)]
espeak_GetCurrentVoice = _libraries['/usr/lib/libespeak.so'].espeak_GetCurrentVoice
espeak_GetCurrentVoice.restype = POINTER(espeak_VOICE)
espeak_GetCurrentVoice.argtypes = []
espeak_Cancel = _libraries['/usr/lib/libespeak.so'].espeak_Cancel
espeak_Cancel.restype = espeak_ERROR
espeak_Cancel.argtypes = []
espeak_IsPlaying = _libraries['/usr/lib/libespeak.so'].espeak_IsPlaying
espeak_IsPlaying.restype = c_int
espeak_IsPlaying.argtypes = []
espeak_Synchronize = _libraries['/usr/lib/libespeak.so'].espeak_Synchronize
espeak_Synchronize.restype = espeak_ERROR
espeak_Synchronize.argtypes = []
espeak_Terminate = _libraries['/usr/lib/libespeak.so'].espeak_Terminate
espeak_Terminate.restype = espeak_ERROR
espeak_Terminate.argtypes = []
espeak_Info = _libraries['/usr/lib/libespeak.so'].espeak_Info
espeak_Info.restype = STRING
espeak_Info.argtypes = [POINTER(STRING)]
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
_IO_FILE._pack_ = 4
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
    ('_unused2', c_char * 40),
]
class _IO_FILE_plus(Structure):
    pass
_IO_FILE_plus._fields_ = [
]
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libespeak.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libespeak.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libespeak.so'], '_IO_2_1_stderr_')
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
__underflow = _libraries['/usr/lib/libespeak.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/lib/libespeak.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/lib/libespeak.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/lib/libespeak.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/lib/libespeak.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/lib/libespeak.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/lib/libespeak.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/lib/libespeak.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/lib/libespeak.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/lib/libespeak.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/lib/libespeak.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/lib/libespeak.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, __gnuc_va_list, POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/lib/libespeak.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, __gnuc_va_list]
_IO_padn = _libraries['/usr/lib/libespeak.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/lib/libespeak.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/lib/libespeak.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/lib/libespeak.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/lib/libespeak.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
__FILE = _IO_FILE
va_list = __gnuc_va_list
off_t = __off_t
off64_t = __off64_t
ssize_t = __ssize_t
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/lib/libespeak.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/lib/libespeak.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/lib/libespeak.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/lib/libespeak.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/lib/libespeak.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/lib/libespeak.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/lib/libespeak.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/lib/libespeak.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/lib/libespeak.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/lib/libespeak.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/lib/libespeak.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/lib/libespeak.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/lib/libespeak.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/lib/libespeak.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/lib/libespeak.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/lib/libespeak.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/lib/libespeak.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/lib/libespeak.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/lib/libespeak.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/lib/libespeak.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/lib/libespeak.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/lib/libespeak.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/lib/libespeak.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/lib/libespeak.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fprintf = _libraries['/usr/lib/libespeak.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/lib/libespeak.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
sprintf = _libraries['/usr/lib/libespeak.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vfprintf = _libraries['/usr/lib/libespeak.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, __gnuc_va_list]
vsprintf = _libraries['/usr/lib/libespeak.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, __gnuc_va_list]
snprintf = _libraries['/usr/lib/libespeak.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/lib/libespeak.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, __gnuc_va_list]
vasprintf = _libraries['/usr/lib/libespeak.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, __gnuc_va_list]
__asprintf = _libraries['/usr/lib/libespeak.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
asprintf = _libraries['/usr/lib/libespeak.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
vdprintf = _libraries['/usr/lib/libespeak.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, __gnuc_va_list]
dprintf = _libraries['/usr/lib/libespeak.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
fscanf = _libraries['/usr/lib/libespeak.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/lib/libespeak.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/lib/libespeak.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/lib/libespeak.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, __gnuc_va_list]
vscanf = _libraries['/usr/lib/libespeak.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, __gnuc_va_list]
vsscanf = _libraries['/usr/lib/libespeak.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, __gnuc_va_list]
fgetc = _libraries['/usr/lib/libespeak.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/lib/libespeak.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/lib/libespeak.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/lib/libespeak.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/lib/libespeak.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/lib/libespeak.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
fgets = _libraries['/usr/lib/libespeak.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
gets = _libraries['/usr/lib/libespeak.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
fgets_unlocked = _libraries['/usr/lib/libespeak.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__getdelim = _libraries['/usr/lib/libespeak.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/lib/libespeak.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/lib/libespeak.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/lib/libespeak.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/lib/libespeak.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fread = _libraries['/usr/lib/libespeak.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fwrite = _libraries['/usr/lib/libespeak.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/lib/libespeak.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fread_unlocked = _libraries['/usr/lib/libespeak.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/lib/libespeak.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/lib/libespeak.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/lib/libespeak.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/lib/libespeak.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/lib/libespeak.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/lib/libespeak.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/lib/libespeak.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/lib/libespeak.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/lib/libespeak.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/lib/libespeak.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/lib/libespeak.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/lib/libespeak.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/lib/libespeak.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/lib/libespeak.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/lib/libespeak.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/lib/libespeak.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/lib/libespeak.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/lib/libespeak.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/lib/libespeak.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/lib/libespeak.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/lib/libespeak.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/lib/libespeak.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/lib/libespeak.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
class obstack(Structure):
    pass
obstack._fields_ = [
]
obstack_printf = _libraries['/usr/lib/libespeak.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
obstack_vprintf = _libraries['/usr/lib/libespeak.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, __gnuc_va_list]
flockfile = _libraries['/usr/lib/libespeak.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/lib/libespeak.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/lib/libespeak.so'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
ptrdiff_t = c_int
__all__ = ['_ATFILE_SOURCE', 'EOF', 'getc_unlocked', '_IO_USER_LOCK',
           'freopen64', '__OFF64_T_TYPE', '_G_ssize_t',
           'espeakEMPHASIS', '__off64_t', '__int16_t', 'fsetpos',
           'espeak_POSITION_TYPE', 'fpos_t', '_G_HAVE_MREMAP',
           'ftell', '_G_va_list', '_G_int16_t', 'getline',
           'espeakPHONEMES', '_IO_BUFSIZ', '__FILE', '_IO_off64_t',
           '__USE_XOPEN_EXTENDED', 'espeak_Key', '_IO_fpos64_t',
           '__mbstate_t_defined', '__time_t', '__GLIBC_PREREQ',
           '__ASMNAME', '_POSIX_SOURCE', '_IO_jump_t', 'stderr',
           'fputc_unlocked', '__swblk_t', '__uint64_t', 'snprintf',
           'espeakPUNCTUATION', '__USE_POSIX199309', '__clockid_t',
           'getchar_unlocked', '_IO_SHOWBASE', '_G_ARGS',
           '_G_HAVE_MMAP', '__codecvt_partial',
           '__attribute_format_strfmon__', '_IO_pos_t',
           'open_memstream', 'fsetpos64', '_IO_DONT_CLOSE',
           'espeak_Synth_Mark', 'AUDIO_OUTPUT_SYNCHRONOUS',
           '_IO_SKIPWS', 'vsprintf', 'espeakCHARS_WCHAR', 'popen',
           '_IO_SCIENTIFIC', 'espeak_SetSynthCallback', '_G_FSTAT64',
           '__PMT', '_G_HAVE_SYS_WAIT', '__mode_t', '_IO_DEC',
           '__off_t', 'fmemopen', 'getchar', 'fputs_unlocked',
           '_IOS_TRUNC', 'ftello64', '__USE_FORTIFY_LEVEL',
           '__int8_t', '__fsblkcnt64_t', '__FSFILCNT64_T_TYPE',
           '__uflow', 'espeakRATE_NORMAL', '_IO_uid_t',
           '__FSBLKCNT64_T_TYPE', 'fopencookie', 'ftrylockfile',
           '__fsfilcnt64_t', '_IO_pid_t', '_IO_FILE', '_IO_BOOLALPHA',
           '__io_read_fn', 'espeak_SetPunctuationList', '_IO_UNITBUF',
           'off_t', 'fprintf', '__fsblkcnt_t',
           '__STDC_CONSTANT_MACROS', 'feof', 'clearerr',
           'espeakRESERVED1', 'espeakRESERVED2', '__fsid_t',
           '__WORDSIZE', 'vfprintf', 'rewind', 'putc_unlocked',
           'flockfile', '_XOPEN_SOURCE', '_IO_free_backup_area',
           'espeak_PUNCT_TYPE', 'ptrdiff_t', '__USE_ISOC95',
           '_G_off64_t', 'espeakCHARS_8BIT', '__USE_ISOC99',
           'espeak_ListVoices', '__rlim64_t', '_IO_fpos_t',
           'POS_WORD', 'stdin', '__u_int', 'ssize_t', '__clock_t',
           '__fsfilcnt_t', '_G_HAVE_IO_GETLINE_INFO',
           'espeakEVENT_MARK', 'espeak_SetPhonemeTrace', '_IONBF',
           'FILE', 'ferror_unlocked', 'size_t', '__USE_XOPEN',
           'espeakLINELENGTH', '__USE_POSIX2', 'fwrite',
           '_IO_ftrylockfile', '_IO_marker', 'espeakCAPITALS',
           'espeakEVENT_MSG_TERMINATED', 'feof_unlocked', '__qaddr_t',
           '_G_HAVE_LONG_DOUBLE_IO', 't_espeak_callback',
           'espeak_Cancel', '_IO_RIGHT', '_IOS_APPEND', 'fpos64_t',
           '__USE_ATFILE', 'perror', 'espeakPUNCT_SOME', 'TMP_MAX',
           '_G_BUFSIZ', 'espeak_EVENT', 'getdelim', '__int32_t',
           '__USE_POSIX', '_IO_NO_WRITES', 'vsscanf',
           '_G_HAVE_IO_FILE_OPEN', '__FILE_defined', 'remove',
           'fileno_unlocked', '_G_NAMES_HAVE_UNDERSCORE',
           '_IO_NO_READS', '__useconds_t', 'vasprintf',
           '__GLIBC_MINOR__', '_IO_CURRENTLY_PUTTING',
           '__INO64_T_TYPE', 'espeak_SetVoiceByName', 'sprintf',
           'vscanf', '__SQUAD_TYPE', 'espeakPUNCT_NONE',
           'espeakRATE_MAXIMUM', 'espeakRATE_MINIMUM', 'asprintf',
           'ferror', '_IO_cookie_io_functions_t', '__gnuc_va_list',
           '__P', 'AUDIO_OUTPUT_RETRIEVAL',
           '_G_VTABLE_LABEL_HAS_LENGTH', '_IO_ERR_SEEN', 'fseeko',
           'putchar', '__USE_GNU', '__attribute_format_arg__',
           'AUDIO_OUTPUT_SYNCH_PLAYBACK', '_G_IO_IO_FILE_VERSION',
           '_POSIX_C_SOURCE', '_IO_ssize_t', '__blksize_t',
           '__USE_SVID', '_IO_seekoff', 'setbuf', '__USE_ANSI',
           '__GLIBC__', '_IO_IS_APPENDING', '_sys_nerr', 'scanf',
           'fclose', '__asprintf', 'L_ctermid', '__mbstate_t',
           '__uint8_t', 'setbuffer', '_IO_INTERNAL', '__u_char',
           '__blkcnt64_t', '__STDC_ISO_10646__', '_IOS_NOCREATE',
           '_G_uid_t', 'dprintf', '_IO_TIED_PUT_GET',
           'AUDIO_OUTPUT_PLAYBACK', 'fscanf', '__USE_LARGEFILE',
           '__USE_EXTERN_INLINES', 'va_list', '_IO_BE', '_FEATURES_H',
           'espeak_SetUriCallback', 'SEEK_DATA', '_IOS_INPUT',
           '_IO_peekc_locked', '_BITS_TYPES_H', 'espeakRATE',
           '__rlim_t', '__UQUAD_TYPE', '_XOPEN_SOURCE_EXTENDED',
           '_IO_off_t', '_IO_UNBUFFERED', '_IOS_ATEND',
           'espeak_PARAMETER', 'espeak_VOICE', 'EE_OK',
           'espeak_EVENT_TYPE', 'espeak_Char', '__quad_t',
           'espeakINITIALIZE_DONT_EXIT', '__key_t', 'fseeko64',
           '__uid_t', 'setlinebuf', 'setvbuf', '_IO_funlockfile',
           '__uint16_t', 'espeak_SetVoiceByProperties',
           '_G_HAVE_SYS_CDEFS', '_IO_putc', '__GNU_LIBRARY__',
           '_BITS_TYPESIZES_H', 'putchar_unlocked', '_IO_USER_BUF',
           '__USE_LARGEFILE64', 'fputc', '__underflow',
           '_IO_2_1_stdin_', 'fgetpos64', 'fputs', '_IO_LINE_BUF',
           '__loff_t', '_G_config_h', 'espeakWORDGAP',
           '__RLIM64_T_TYPE', 'espeakEVENT_LIST_TERMINATED',
           'espeakSSML', 'cookie_seek_function_t', '_IO_FLAGS2_MMAP',
           '_G_USING_THUNKS', '__GLIBC_HAVE_LONG_LONG', 'fileno',
           'FOPEN_MAX', 'espeakINTONATION', '_IO_DELETE_DONT_CLOSE',
           'espeak_Synth', '_G_fpos_t', 'espeakEVENT_SENTENCE',
           'espeakSILENCE', '__bos', 'cookie_close_function_t',
           '__ssize_t', 'espeak_SetParameter', '__warnattr',
           'espeakEVENT_WORD', '_sys_errlist', 'fgetpos',
           'funlockfile', '_IO_padn', 'espeakCHARS_16BIT', 'vdprintf',
           '__getdelim', '__overflow', '__USE_XOPEN2K',
           '__FD_SETSIZE', 'EE_BUFFER_FULL', '__intptr_t',
           'EE_INTERNAL_ERROR', 'tmpnam_r', '_IO_LINKED',
           'espeak_Terminate', '_IO_FILE_plus', '_IO_va_list',
           '__blkcnt_t', '_IO_size_t', '_IO_flockfile',
           'espeak_AUDIO_OUTPUT', '__REDIRECT_NTH_LDBL', 'L_tmpnam',
           'off64_t', '_IOS_BIN', 'tmpfile64', 'sys_nerr',
           '_IO_BAD_SEEN', '__USE_MISC', 'putw', 'puts', '__u_long',
           'obstack', 'N11__mbstate_t3DOT_2E', 'putc', 'vsnprintf',
           '_IO_HEX', 'fread', 'tmpnam', '__dev_t',
           '_IO_HAVE_SYS_WAIT', 'FILENAME_MAX', 'L_cuserid',
           '__suseconds_t', 'espeakENDPAUSE', 'rename',
           '__USE_POSIX199506', 'stdout', '__S64_TYPE',
           '__DEV_T_TYPE', 'fwrite_unlocked', 'SEEK_HOLE',
           'espeak_GetParameter', 'getc', '__USE_XOPEN2K8XSI',
           '_IO_ferror', '_G_size_t', 'gets', '_SYS_CDEFS_H', 'getw',
           '_OLD_STDIO_MAGIC', '_G_pid_t', '_IO_IS_FILEBUF',
           'SEEK_SET', 'espeakCHARS_UTF8', '__io_write_fn',
           '_G_HAVE_PRINTF_FP', '__ino_t', '_IO_lock_t',
           'espeak_GetCurrentVoice', '_IO_2_1_stdout_',
           '__REDIRECT_LDBL', 'obstack_vprintf', 'espeakPUNCT_ALL',
           '_G_HAVE_BOOL', '__int64_t', 'espeakEVENT_SAMPLERATE',
           'espeakCHARS_AUTO', 'fopen64', '_LARGEFILE_SOURCE',
           'fseek', '__USE_XOPEN2KXSI', 'cookie_write_function_t',
           '_IO_LEFT', '_G_off_t', 'espeak_IsPlaying',
           'ESPEAK_API_REVISION', '__timer_t', 'fflush',
           'POS_CHARACTER', 'EE_NOT_FOUND', '__uint32_t',
           '__USE_XOPEN2K8', 'fflush_unlocked', 'POS_SENTENCE',
           'P_tmpdir', '__ino64_t', 'espeak_Info', '_IO_SHOWPOINT',
           '_IO_sgetn', '__STDC_IEC_559__', '_IO_FLAGS2_NOTCANCEL',
           'espeakOPTIONS', '_G_uint32_t', '_G_VTABLE_LABEL_PREFIX',
           'espeakVOLUME', 'renameat', '_G_fpos64_t', 'espeak_ERROR',
           '_ISOC95_SOURCE', 'espeakPITCH', '_ISOC99_SOURCE',
           'freopen', '__nlink_t', 'fread_unlocked', 'tempnam',
           'tmpfile', 'espeakEVENT_PHONEME', 'fgetc', 'pclose',
           'printf', '__pid_t', '__U64_TYPE', '__codecvt_ok',
           'espeak_Synchronize', '_IO_MAGIC', 'ctermid', '__id_t',
           'cookie_io_functions_t', '_IO_feof', 'espeakRANGE',
           'fgetc_unlocked', '_IO_UPPERCASE',
           'espeak_CompileDictionary', '_IO_EOF_SEEN', '_IO_vfprintf',
           '_IO_FIXED', 'N_SPEECH_PARAM', '_SVID_SOURCE',
           '_G_uint16_t', '__codecvt_result', 'fcloseall', '_IOFBF',
           'SEEK_END', '_IO_peekc', '__USE_BSD', 'sys_errlist',
           '__CONCAT', 'clearerr_unlocked', '_IO_IN_BACKUP',
           '_IOS_NOREPLACE', 'obstack_printf', '____FILE_defined',
           'SEEK_CUR', '__USE_UNIX98', '_IO_STDIO', 'fgets_unlocked',
           'fopen', '__gid_t', 'fdopen', '__io_close_fn', '_IO_OCT',
           '_IOS_OUTPUT', '__daddr_t', '_IO_cookie_file', '__caddr_t',
           'vprintf', '__io_seek_fn', 'N12espeak_EVENT3DOT_8E',
           'BUFSIZ', '__STDC_IEC_559_COMPLEX__', 'espeakEVENT_END',
           '_IO_getc', '_IO_UNIFIED_JUMPTABLES', 'cuserid',
           '_IO_vfscanf', 'cookie_read_function_t', 'ungetc',
           'espeakKEEP_NAMEDATA', 'sscanf', '_IO_SHOWPOS',
           'espeakEVENT_PLAY', '_IO_2_1_stderr_', '_STDIO_H',
           'ftello', 'fgets', 'espeak_Initialize',
           '_IO_FLAGS2_USER_WBUF', '__STRING', '_IO_seekpos',
           '_PARAMS', '__GNUC_PREREQ', '__BLKCNT64_T_TYPE',
           'espeakVOICETYPE', '_IO_MAGIC_MASK', '__u_quad_t',
           '__u_short', 'espeakINITIALIZE_PHONEME_EVENTS', 'vfscanf',
           '_BSD_SOURCE', '_LARGEFILE64_SOURCE', '__va_arg_pack',
           '__codecvt_error', '_G_NEED_STDARG_H', '__va_arg_pack_len',
           '__bos0', '_G_HAVE_ATEXIT', '__socklen_t',
           '__codecvt_noconv', '_IOLBF', '_G_int32_t', 'offsetof']
