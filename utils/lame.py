from ctypes import *

_libraries = {}
_libraries['/usr/lib/libmp3lame.so'] = CDLL('/usr/lib/libmp3lame.so')
STRING = c_char_p


LAME_NOMEM = -10
vbr_mt = 1
vbr_abr = 3
V1 = 490
# NULL = __null # alias
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
MDB_STRICT_ISO = 1
__codecvt_noconv = 3
MDB_DEFAULT = 0
V2 = 480
MDB_MAXIMUM = 2
PSY_NSPSYTUNE = 2
PSY_GPSYCHO = 1
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
__codecvt_ok = 0
MEDIUM = 1006
EXTREME_FAST = 1005
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
STANDARD_FAST = 1004
INSANE = 1003
EXTREME = 1002
vbr_off = 0
VBR_70 = 470
BUFSIZ = _IO_BUFSIZ # alias
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
def va_copy(d,s): return __builtin_va_copy(d,s) # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
def va_arg(v,l): return __builtin_va_arg(v,l) # macro
# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
LAME_INTERNALERROR = -13
class _IO_FILE(Structure):
    pass
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'stdout')
stdout = stdout # alias
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'stdin')
stdin = stdin # alias
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'stderr')
stderr = stderr # alias
# __wur = __attribute_warn_unused_result__ # alias
# __SLONG32_TYPE = int # alias
# __UID_T_TYPE = __U32_TYPE # alias
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
def __va_copy(d,s): return __builtin_va_copy(d,s) # macro
# __S32_TYPE = int # alias
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __PID_T_TYPE = __S32_TYPE # alias
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __KEY_T_TYPE = __S32_TYPE # alias
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
# __INO64_T_TYPE = __UQUAD_TYPE # alias
# __ID_T_TYPE = __U32_TYPE # alias
# __GID_T_TYPE = __U32_TYPE # alias
MAX_INDICATOR = 5
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __DEV_T_TYPE = __UQUAD_TYPE # alias
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
# __CLOCKID_T_TYPE = __S32_TYPE # alias
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
# __USECONDS_T_TYPE = __U32_TYPE # alias
MEDIUM_FAST = 1007
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
def getc(_fp): return _IO_getc (_fp) # macro
size_t = c_ulong
_IO_size_t = size_t # alias
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
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
FRONTEND_FILETOOLARGE = -82
def __STRING(x): return #x # macro
FRONTEND_WRITEERROR = -81
class __va_list_tag(Structure):
    pass
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
_G_va_list = __gnuc_va_list # alias
# _IO_iconv_t = _G_iconv_t # alias
# __MODE_T_TYPE = __U32_TYPE # alias
LAME_GENERICERROR = -1
LAME_OKAY = 0
LAME_BADBITRATE = -11
__codecvt_error = 2
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
def va_end(v): return __builtin_va_end(v) # macro
def offsetof(TYPE,MEMBER): return __builtin_offsetof (TYPE, MEMBER) # macro
VBR_100 = 500
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
V0 = 500
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
__codecvt_partial = 1
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
STEREO = 0
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
def __CONCAT(x,y): return x ## y # macro
def __PMT(args): return args # macro
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# def __LDBL_REDIR(name,proto): return name proto # macro
def __P(args): return args # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
_IO_off_t = __off_t # alias
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
VBR_60 = 460
# __DADDR_T_TYPE = __S32_TYPE # alias
LAME_NOERROR = 0
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
STANDARD = 1001
NOT_SET = 4
DUAL_CHANNEL = 2
JOINT_STEREO = 1
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
R3MIX = 1000
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
VBR_90 = 490
VBR_80 = 480
V3 = 470
V4 = 460
VBR_50 = 450
V5 = 450
VBR_40 = 440
V6 = 440
VBR_30 = 430
V7 = 430
VBR_20 = 420
V8 = 420
VBR_10 = 410
# _IO_wint_t = wint_t # alias
V9 = 410
ABR_320 = 320
ABR_8 = 8
_IO_va_list = __gnuc_va_list # alias
PAD_NO = 0
__uid_t = c_uint
_IO_uid_t = __uid_t # alias
vbr_max_indicator = 5
MONO = 3
__ssize_t = c_long
_IO_ssize_t = __ssize_t # alias
vbr_rh = 2
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
vbr_default = 4
__pid_t = c_int
_IO_pid_t = __pid_t # alias
__off64_t = c_long
_IO_off64_t = __off64_t # alias
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
PAD_MAX_INDICATOR = 3
PAD_ADJUST = 2
PAD_ALL = 1
SSE = 3
class _G_fpos64_t(Structure):
    pass
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
AMD_3DNOW = 2
MMX = 1
# _IO_file_flags = _flags # alias
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
FRONTEND_READERROR = -80
def va_start(v,l): return __builtin_va_start(v,l) # macro
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
LAME_BADSAMPFREQ = -12
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
vbr_mtrh = 4
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
_ATFILE_SOURCE = 1 # Variable c_int '1'
EOF = -1 # Variable c_int '-0x00000000000000001'
_IO_LEFT = 2 # Variable c_int '2'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_IONBF = 2 # Variable c_int '2'
__USE_XOPEN = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
_IO_SHOWBASE = 128 # Variable c_int '128'
_IO_LINE_BUF = 512 # Variable c_int '512'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
_IO_SHOWPOINT = 256 # Variable c_int '256'
_IO_RIGHT = 4 # Variable c_int '4'
_IOS_APPEND = 8 # Variable c_int '8'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
__USE_ATFILE = 1 # Variable c_int '1'
LAME_MAXALBUMART = 131072 # Variable c_int '131072'
TMP_MAX = 238328 # Variable c_int '238328'
FOPEN_MAX = 16 # Variable c_int '16'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
__USE_POSIX = 1 # Variable c_int '1'
_IO_NO_WRITES = 8 # Variable c_int '8'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
__FILE_defined = 1 # Variable c_int '1'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
_STDIO_H = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944 # Variable c_uint '4222418944u'
_IO_NO_READS = 4 # Variable c_int '4'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 19 # Variable c_int '19'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
__USE_MISC = 1 # Variable c_int '1'
_IO_UPPERCASE = 512 # Variable c_int '512'
LAME_MAXMP3BUFFER = 147456 # Variable c_int '147456'
_IO_EOF_SEEN = 16 # Variable c_int '16'
_G_HAVE_MMAP = 1 # Variable c_int '1'
_IO_FIXED = 4096 # Variable c_int '4096'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__FD_SETSIZE = 1024 # Variable c_int '1024'
____mbstate_t_defined = 1 # Variable c_int '1'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
_IO_ERR_SEEN = 32 # Variable c_int '32'
_IOFBF = 0 # Variable c_int '0'
_IO_LINKED = 128 # Variable c_int '128'
SEEK_END = 2 # Variable c_int '2'
__USE_GNU = 1 # Variable c_int '1'
__USE_BSD = 1 # Variable c_int '1'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
_G_config_h = 1 # Variable c_int '1'
_IO_IN_BACKUP = 256 # Variable c_int '256'
_IOS_NOREPLACE = 64 # Variable c_int '64'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_ISOC11_SOURCE = 1 # Variable c_int '1'
_IO_USER_BUF = 1 # Variable c_int '1'
____FILE_defined = 1 # Variable c_int '1'
L_tmpnam = 20 # Variable c_int '20'
SEEK_CUR = 1 # Variable c_int '1'
_IO_DEC = 16 # Variable c_int '16'
__USE_SVID = 1 # Variable c_int '1'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
_IOS_BIN = 128 # Variable c_int '128'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
_IO_OCT = 32 # Variable c_int '32'
_IOS_TRUNC = 16 # Variable c_int '16'
L_ctermid = 9 # Variable c_int '9'
_IO_HEX = 64 # Variable c_int '64'
_IO_INTERNAL = 8 # Variable c_int '8'
__OFF_T_MATCHES_OFF64_T = 1 # Variable c_int '1'
_IO_SKIPWS = 1 # Variable c_int '1'
_IOS_NOCREATE = 32 # Variable c_int '32'
FILENAME_MAX = 4096 # Variable c_int '4096'
L_cuserid = 9 # Variable c_int '9'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
__INO_T_MATCHES_INO64_T = 1 # Variable c_int '1'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
_FEATURES_H = 1 # Variable c_int '1'
SEEK_DATA = 3 # Variable c_int '3'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
_IOS_INPUT = 1 # Variable c_int '1'
__USE_POSIX199506 = 1 # Variable c_int '1'
_IO_UNITBUF = 8192 # Variable c_int '8192'
_BITS_TYPES_H = 1 # Variable c_int '1'
SEEK_HOLE = 4 # Variable c_int '4'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
__USE_POSIX199309 = 1 # Variable c_int '1'
_IO_MAGIC_MASK = 4294901760 # Variable c_uint '4294901760u'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
_IO_UNBUFFERED = 2 # Variable c_int '2'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_OLD_STDIO_MAGIC = 4206624768 # Variable c_uint '4206624768u'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
_XOPEN_SOURCE = 700 # Variable c_int '700'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
SEEK_SET = 0 # Variable c_int '0'
_IOS_ATEND = 4 # Variable c_int '4'
_IOS_OUTPUT = 2 # Variable c_int '2'
__USE_ISOC95 = 1 # Variable c_int '1'
__GLIBC__ = 2 # Variable c_int '2'
DEPRECATED_OR_OBSOLETE_CODE_REMOVED = 1 # Variable c_int '1'
__USE_ISOC99 = 1 # Variable c_int '1'
__USE_ISOC11 = 1 # Variable c_int '1'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
_BSD_SOURCE = 1 # Variable c_int '1'
_IOLBF = 1 # Variable c_int '1'
getchar = _libraries['/usr/lib/libmp3lame.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
FILE = _IO_FILE
fgetc_unlocked = _libraries['/usr/lib/libmp3lame.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/lib/libmp3lame.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/lib/libmp3lame.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/lib/libmp3lame.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/lib/libmp3lame.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/lib/libmp3lame.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/lib/libmp3lame.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/lib/libmp3lame.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/lib/libmp3lame.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/lib/libmp3lame.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
__sprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__sprintf_chk
__sprintf_chk.restype = c_int
__sprintf_chk.argtypes = [STRING, c_int, size_t, STRING]
__vsprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vsprintf_chk
__vsprintf_chk.restype = c_int
__vsprintf_chk.argtypes = [STRING, c_int, size_t, STRING, POINTER(__va_list_tag)]
sprintf = _libraries['/usr/lib/libmp3lame.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vsprintf = _libraries['/usr/lib/libmp3lame.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
__snprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__snprintf_chk
__snprintf_chk.restype = c_int
__snprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING]
__vsnprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vsnprintf_chk
__vsnprintf_chk.restype = c_int
__vsnprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['/usr/lib/libmp3lame.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/lib/libmp3lame.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
__fprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__fprintf_chk
__fprintf_chk.restype = c_int
__fprintf_chk.argtypes = [POINTER(FILE), c_int, STRING]
__printf_chk = _libraries['/usr/lib/libmp3lame.so'].__printf_chk
__printf_chk.restype = c_int
__printf_chk.argtypes = [c_int, STRING]
__vfprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vfprintf_chk
__vfprintf_chk.restype = c_int
__vfprintf_chk.argtypes = [POINTER(FILE), c_int, STRING, POINTER(__va_list_tag)]
__vprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vprintf_chk
__vprintf_chk.restype = c_int
__vprintf_chk.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
fprintf = _libraries['/usr/lib/libmp3lame.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/lib/libmp3lame.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
vprintf = _libraries['/usr/lib/libmp3lame.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
vfprintf = _libraries['/usr/lib/libmp3lame.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
__dprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__dprintf_chk
__dprintf_chk.restype = c_int
__dprintf_chk.argtypes = [c_int, c_int, STRING]
__vdprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vdprintf_chk
__vdprintf_chk.restype = c_int
__vdprintf_chk.argtypes = [c_int, c_int, STRING, POINTER(__va_list_tag)]
dprintf = _libraries['/usr/lib/libmp3lame.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
vdprintf = _libraries['/usr/lib/libmp3lame.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
__asprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__asprintf_chk
__asprintf_chk.restype = c_int
__asprintf_chk.argtypes = [POINTER(STRING), c_int, STRING]
__vasprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__vasprintf_chk
__vasprintf_chk.restype = c_int
__vasprintf_chk.argtypes = [POINTER(STRING), c_int, STRING, POINTER(__va_list_tag)]
class obstack(Structure):
    pass
__obstack_printf_chk = _libraries['/usr/lib/libmp3lame.so'].__obstack_printf_chk
__obstack_printf_chk.restype = c_int
__obstack_printf_chk.argtypes = [POINTER(obstack), c_int, STRING]
__obstack_vprintf_chk = _libraries['/usr/lib/libmp3lame.so'].__obstack_vprintf_chk
__obstack_vprintf_chk.restype = c_int
__obstack_vprintf_chk.argtypes = [POINTER(obstack), c_int, STRING, POINTER(__va_list_tag)]
asprintf = _libraries['/usr/lib/libmp3lame.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
__asprintf = _libraries['/usr/lib/libmp3lame.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
obstack_printf = _libraries['/usr/lib/libmp3lame.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
vasprintf = _libraries['/usr/lib/libmp3lame.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
obstack_vprintf = _libraries['/usr/lib/libmp3lame.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, POINTER(__va_list_tag)]
__fgets_chk = _libraries['/usr/lib/libmp3lame.so'].__fgets_chk
__fgets_chk.restype = STRING
__fgets_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets = _libraries['/usr/lib/libmp3lame.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_chk = _libraries['/usr/lib/libmp3lame.so'].__fread_chk
__fread_chk.restype = size_t
__fread_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread = _libraries['/usr/lib/libmp3lame.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__fgets_unlocked_chk = _libraries['/usr/lib/libmp3lame.so'].__fgets_unlocked_chk
__fgets_unlocked_chk.restype = STRING
__fgets_unlocked_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets_unlocked = _libraries['/usr/lib/libmp3lame.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_unlocked_chk = _libraries['/usr/lib/libmp3lame.so'].__fread_unlocked_chk
__fread_unlocked_chk.restype = size_t
__fread_unlocked_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread_unlocked = _libraries['/usr/lib/libmp3lame.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmp3lame.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmp3lame.so'], '_sys_errlist')
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
__time_t = c_long
__useconds_t = c_uint
__suseconds_t = c_long
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
lame_report_function = CFUNCTYPE(None, STRING, POINTER(__va_list_tag))

# values for enumeration 'vbr_mode_e'
vbr_mode_e = c_int # enum
vbr_mode = vbr_mode_e

# values for enumeration 'MPEG_mode_e'
MPEG_mode_e = c_int # enum
MPEG_mode = MPEG_mode_e

# values for enumeration 'Padding_type_e'
Padding_type_e = c_int # enum
Padding_type = Padding_type_e

# values for enumeration 'preset_mode_e'
preset_mode_e = c_int # enum
preset_mode = preset_mode_e

# values for enumeration 'asm_optimizations_e'
asm_optimizations_e = c_int # enum
asm_optimizations = asm_optimizations_e

# values for enumeration 'Psy_model_e'
Psy_model_e = c_int # enum
Psy_model = Psy_model_e

# values for enumeration 'buffer_constraint_e'
buffer_constraint_e = c_int # enum
buffer_constraint = buffer_constraint_e
class lame_global_struct(Structure):
    pass
lame_global_struct._fields_ = [
]
lame_global_flags = lame_global_struct
lame_t = POINTER(lame_global_flags)
lame_init = _libraries['/usr/lib/libmp3lame.so'].lame_init
lame_init.restype = POINTER(lame_global_flags)
lame_init.argtypes = []
lame_set_num_samples = _libraries['/usr/lib/libmp3lame.so'].lame_set_num_samples
lame_set_num_samples.restype = c_int
lame_set_num_samples.argtypes = [POINTER(lame_global_flags), c_ulong]
lame_get_num_samples = _libraries['/usr/lib/libmp3lame.so'].lame_get_num_samples
lame_get_num_samples.restype = c_ulong
lame_get_num_samples.argtypes = [POINTER(lame_global_flags)]
lame_set_in_samplerate = _libraries['/usr/lib/libmp3lame.so'].lame_set_in_samplerate
lame_set_in_samplerate.restype = c_int
lame_set_in_samplerate.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_in_samplerate = _libraries['/usr/lib/libmp3lame.so'].lame_get_in_samplerate
lame_get_in_samplerate.restype = c_int
lame_get_in_samplerate.argtypes = [POINTER(lame_global_flags)]
lame_set_num_channels = _libraries['/usr/lib/libmp3lame.so'].lame_set_num_channels
lame_set_num_channels.restype = c_int
lame_set_num_channels.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_num_channels = _libraries['/usr/lib/libmp3lame.so'].lame_get_num_channels
lame_get_num_channels.restype = c_int
lame_get_num_channels.argtypes = [POINTER(lame_global_flags)]
lame_set_scale = _libraries['/usr/lib/libmp3lame.so'].lame_set_scale
lame_set_scale.restype = c_int
lame_set_scale.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_scale = _libraries['/usr/lib/libmp3lame.so'].lame_get_scale
lame_get_scale.restype = c_float
lame_get_scale.argtypes = [POINTER(lame_global_flags)]
lame_set_scale_left = _libraries['/usr/lib/libmp3lame.so'].lame_set_scale_left
lame_set_scale_left.restype = c_int
lame_set_scale_left.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_scale_left = _libraries['/usr/lib/libmp3lame.so'].lame_get_scale_left
lame_get_scale_left.restype = c_float
lame_get_scale_left.argtypes = [POINTER(lame_global_flags)]
lame_set_scale_right = _libraries['/usr/lib/libmp3lame.so'].lame_set_scale_right
lame_set_scale_right.restype = c_int
lame_set_scale_right.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_scale_right = _libraries['/usr/lib/libmp3lame.so'].lame_get_scale_right
lame_get_scale_right.restype = c_float
lame_get_scale_right.argtypes = [POINTER(lame_global_flags)]
lame_set_out_samplerate = _libraries['/usr/lib/libmp3lame.so'].lame_set_out_samplerate
lame_set_out_samplerate.restype = c_int
lame_set_out_samplerate.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_out_samplerate = _libraries['/usr/lib/libmp3lame.so'].lame_get_out_samplerate
lame_get_out_samplerate.restype = c_int
lame_get_out_samplerate.argtypes = [POINTER(lame_global_flags)]
lame_set_analysis = _libraries['/usr/lib/libmp3lame.so'].lame_set_analysis
lame_set_analysis.restype = c_int
lame_set_analysis.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_analysis = _libraries['/usr/lib/libmp3lame.so'].lame_get_analysis
lame_get_analysis.restype = c_int
lame_get_analysis.argtypes = [POINTER(lame_global_flags)]
lame_set_bWriteVbrTag = _libraries['/usr/lib/libmp3lame.so'].lame_set_bWriteVbrTag
lame_set_bWriteVbrTag.restype = c_int
lame_set_bWriteVbrTag.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_bWriteVbrTag = _libraries['/usr/lib/libmp3lame.so'].lame_get_bWriteVbrTag
lame_get_bWriteVbrTag.restype = c_int
lame_get_bWriteVbrTag.argtypes = [POINTER(lame_global_flags)]
lame_set_decode_only = _libraries['/usr/lib/libmp3lame.so'].lame_set_decode_only
lame_set_decode_only.restype = c_int
lame_set_decode_only.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_decode_only = _libraries['/usr/lib/libmp3lame.so'].lame_get_decode_only
lame_get_decode_only.restype = c_int
lame_get_decode_only.argtypes = [POINTER(lame_global_flags)]
lame_set_quality = _libraries['/usr/lib/libmp3lame.so'].lame_set_quality
lame_set_quality.restype = c_int
lame_set_quality.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_quality = _libraries['/usr/lib/libmp3lame.so'].lame_get_quality
lame_get_quality.restype = c_int
lame_get_quality.argtypes = [POINTER(lame_global_flags)]
lame_set_mode = _libraries['/usr/lib/libmp3lame.so'].lame_set_mode
lame_set_mode.restype = c_int
lame_set_mode.argtypes = [POINTER(lame_global_flags), MPEG_mode]
lame_get_mode = _libraries['/usr/lib/libmp3lame.so'].lame_get_mode
lame_get_mode.restype = MPEG_mode
lame_get_mode.argtypes = [POINTER(lame_global_flags)]
lame_set_force_ms = _libraries['/usr/lib/libmp3lame.so'].lame_set_force_ms
lame_set_force_ms.restype = c_int
lame_set_force_ms.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_force_ms = _libraries['/usr/lib/libmp3lame.so'].lame_get_force_ms
lame_get_force_ms.restype = c_int
lame_get_force_ms.argtypes = [POINTER(lame_global_flags)]
lame_set_free_format = _libraries['/usr/lib/libmp3lame.so'].lame_set_free_format
lame_set_free_format.restype = c_int
lame_set_free_format.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_free_format = _libraries['/usr/lib/libmp3lame.so'].lame_get_free_format
lame_get_free_format.restype = c_int
lame_get_free_format.argtypes = [POINTER(lame_global_flags)]
lame_set_findReplayGain = _libraries['/usr/lib/libmp3lame.so'].lame_set_findReplayGain
lame_set_findReplayGain.restype = c_int
lame_set_findReplayGain.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_findReplayGain = _libraries['/usr/lib/libmp3lame.so'].lame_get_findReplayGain
lame_get_findReplayGain.restype = c_int
lame_get_findReplayGain.argtypes = [POINTER(lame_global_flags)]
lame_set_decode_on_the_fly = _libraries['/usr/lib/libmp3lame.so'].lame_set_decode_on_the_fly
lame_set_decode_on_the_fly.restype = c_int
lame_set_decode_on_the_fly.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_decode_on_the_fly = _libraries['/usr/lib/libmp3lame.so'].lame_get_decode_on_the_fly
lame_get_decode_on_the_fly.restype = c_int
lame_get_decode_on_the_fly.argtypes = [POINTER(lame_global_flags)]
lame_set_nogap_total = _libraries['/usr/lib/libmp3lame.so'].lame_set_nogap_total
lame_set_nogap_total.restype = c_int
lame_set_nogap_total.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_nogap_total = _libraries['/usr/lib/libmp3lame.so'].lame_get_nogap_total
lame_get_nogap_total.restype = c_int
lame_get_nogap_total.argtypes = [POINTER(lame_global_flags)]
lame_set_nogap_currentindex = _libraries['/usr/lib/libmp3lame.so'].lame_set_nogap_currentindex
lame_set_nogap_currentindex.restype = c_int
lame_set_nogap_currentindex.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_nogap_currentindex = _libraries['/usr/lib/libmp3lame.so'].lame_get_nogap_currentindex
lame_get_nogap_currentindex.restype = c_int
lame_get_nogap_currentindex.argtypes = [POINTER(lame_global_flags)]
lame_set_errorf = _libraries['/usr/lib/libmp3lame.so'].lame_set_errorf
lame_set_errorf.restype = c_int
lame_set_errorf.argtypes = [POINTER(lame_global_flags), lame_report_function]
lame_set_debugf = _libraries['/usr/lib/libmp3lame.so'].lame_set_debugf
lame_set_debugf.restype = c_int
lame_set_debugf.argtypes = [POINTER(lame_global_flags), lame_report_function]
lame_set_msgf = _libraries['/usr/lib/libmp3lame.so'].lame_set_msgf
lame_set_msgf.restype = c_int
lame_set_msgf.argtypes = [POINTER(lame_global_flags), lame_report_function]
lame_set_brate = _libraries['/usr/lib/libmp3lame.so'].lame_set_brate
lame_set_brate.restype = c_int
lame_set_brate.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_brate = _libraries['/usr/lib/libmp3lame.so'].lame_get_brate
lame_get_brate.restype = c_int
lame_get_brate.argtypes = [POINTER(lame_global_flags)]
lame_set_compression_ratio = _libraries['/usr/lib/libmp3lame.so'].lame_set_compression_ratio
lame_set_compression_ratio.restype = c_int
lame_set_compression_ratio.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_compression_ratio = _libraries['/usr/lib/libmp3lame.so'].lame_get_compression_ratio
lame_get_compression_ratio.restype = c_float
lame_get_compression_ratio.argtypes = [POINTER(lame_global_flags)]
lame_set_preset = _libraries['/usr/lib/libmp3lame.so'].lame_set_preset
lame_set_preset.restype = c_int
lame_set_preset.argtypes = [POINTER(lame_global_flags), c_int]
lame_set_asm_optimizations = _libraries['/usr/lib/libmp3lame.so'].lame_set_asm_optimizations
lame_set_asm_optimizations.restype = c_int
lame_set_asm_optimizations.argtypes = [POINTER(lame_global_flags), c_int, c_int]
lame_set_copyright = _libraries['/usr/lib/libmp3lame.so'].lame_set_copyright
lame_set_copyright.restype = c_int
lame_set_copyright.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_copyright = _libraries['/usr/lib/libmp3lame.so'].lame_get_copyright
lame_get_copyright.restype = c_int
lame_get_copyright.argtypes = [POINTER(lame_global_flags)]
lame_set_original = _libraries['/usr/lib/libmp3lame.so'].lame_set_original
lame_set_original.restype = c_int
lame_set_original.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_original = _libraries['/usr/lib/libmp3lame.so'].lame_get_original
lame_get_original.restype = c_int
lame_get_original.argtypes = [POINTER(lame_global_flags)]
lame_set_error_protection = _libraries['/usr/lib/libmp3lame.so'].lame_set_error_protection
lame_set_error_protection.restype = c_int
lame_set_error_protection.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_error_protection = _libraries['/usr/lib/libmp3lame.so'].lame_get_error_protection
lame_get_error_protection.restype = c_int
lame_get_error_protection.argtypes = [POINTER(lame_global_flags)]
lame_set_extension = _libraries['/usr/lib/libmp3lame.so'].lame_set_extension
lame_set_extension.restype = c_int
lame_set_extension.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_extension = _libraries['/usr/lib/libmp3lame.so'].lame_get_extension
lame_get_extension.restype = c_int
lame_get_extension.argtypes = [POINTER(lame_global_flags)]
lame_set_strict_ISO = _libraries['/usr/lib/libmp3lame.so'].lame_set_strict_ISO
lame_set_strict_ISO.restype = c_int
lame_set_strict_ISO.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_strict_ISO = _libraries['/usr/lib/libmp3lame.so'].lame_get_strict_ISO
lame_get_strict_ISO.restype = c_int
lame_get_strict_ISO.argtypes = [POINTER(lame_global_flags)]
lame_set_disable_reservoir = _libraries['/usr/lib/libmp3lame.so'].lame_set_disable_reservoir
lame_set_disable_reservoir.restype = c_int
lame_set_disable_reservoir.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_disable_reservoir = _libraries['/usr/lib/libmp3lame.so'].lame_get_disable_reservoir
lame_get_disable_reservoir.restype = c_int
lame_get_disable_reservoir.argtypes = [POINTER(lame_global_flags)]
lame_set_quant_comp = _libraries['/usr/lib/libmp3lame.so'].lame_set_quant_comp
lame_set_quant_comp.restype = c_int
lame_set_quant_comp.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_quant_comp = _libraries['/usr/lib/libmp3lame.so'].lame_get_quant_comp
lame_get_quant_comp.restype = c_int
lame_get_quant_comp.argtypes = [POINTER(lame_global_flags)]
lame_set_quant_comp_short = _libraries['/usr/lib/libmp3lame.so'].lame_set_quant_comp_short
lame_set_quant_comp_short.restype = c_int
lame_set_quant_comp_short.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_quant_comp_short = _libraries['/usr/lib/libmp3lame.so'].lame_get_quant_comp_short
lame_get_quant_comp_short.restype = c_int
lame_get_quant_comp_short.argtypes = [POINTER(lame_global_flags)]
lame_set_experimentalX = _libraries['/usr/lib/libmp3lame.so'].lame_set_experimentalX
lame_set_experimentalX.restype = c_int
lame_set_experimentalX.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_experimentalX = _libraries['/usr/lib/libmp3lame.so'].lame_get_experimentalX
lame_get_experimentalX.restype = c_int
lame_get_experimentalX.argtypes = [POINTER(lame_global_flags)]
lame_set_experimentalY = _libraries['/usr/lib/libmp3lame.so'].lame_set_experimentalY
lame_set_experimentalY.restype = c_int
lame_set_experimentalY.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_experimentalY = _libraries['/usr/lib/libmp3lame.so'].lame_get_experimentalY
lame_get_experimentalY.restype = c_int
lame_get_experimentalY.argtypes = [POINTER(lame_global_flags)]
lame_set_experimentalZ = _libraries['/usr/lib/libmp3lame.so'].lame_set_experimentalZ
lame_set_experimentalZ.restype = c_int
lame_set_experimentalZ.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_experimentalZ = _libraries['/usr/lib/libmp3lame.so'].lame_get_experimentalZ
lame_get_experimentalZ.restype = c_int
lame_get_experimentalZ.argtypes = [POINTER(lame_global_flags)]
lame_set_exp_nspsytune = _libraries['/usr/lib/libmp3lame.so'].lame_set_exp_nspsytune
lame_set_exp_nspsytune.restype = c_int
lame_set_exp_nspsytune.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_exp_nspsytune = _libraries['/usr/lib/libmp3lame.so'].lame_get_exp_nspsytune
lame_get_exp_nspsytune.restype = c_int
lame_get_exp_nspsytune.argtypes = [POINTER(lame_global_flags)]
lame_set_msfix = _libraries['/usr/lib/libmp3lame.so'].lame_set_msfix
lame_set_msfix.restype = None
lame_set_msfix.argtypes = [POINTER(lame_global_flags), c_double]
lame_get_msfix = _libraries['/usr/lib/libmp3lame.so'].lame_get_msfix
lame_get_msfix.restype = c_float
lame_get_msfix.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR
lame_set_VBR.restype = c_int
lame_set_VBR.argtypes = [POINTER(lame_global_flags), vbr_mode]
lame_get_VBR = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR
lame_get_VBR.restype = vbr_mode
lame_get_VBR.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_q = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_q
lame_set_VBR_q.restype = c_int
lame_set_VBR_q.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_VBR_q = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_q
lame_get_VBR_q.restype = c_int
lame_get_VBR_q.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_quality = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_quality
lame_set_VBR_quality.restype = c_int
lame_set_VBR_quality.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_VBR_quality = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_quality
lame_get_VBR_quality.restype = c_float
lame_get_VBR_quality.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_mean_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_mean_bitrate_kbps
lame_set_VBR_mean_bitrate_kbps.restype = c_int
lame_set_VBR_mean_bitrate_kbps.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_VBR_mean_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_mean_bitrate_kbps
lame_get_VBR_mean_bitrate_kbps.restype = c_int
lame_get_VBR_mean_bitrate_kbps.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_min_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_min_bitrate_kbps
lame_set_VBR_min_bitrate_kbps.restype = c_int
lame_set_VBR_min_bitrate_kbps.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_VBR_min_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_min_bitrate_kbps
lame_get_VBR_min_bitrate_kbps.restype = c_int
lame_get_VBR_min_bitrate_kbps.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_max_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_max_bitrate_kbps
lame_set_VBR_max_bitrate_kbps.restype = c_int
lame_set_VBR_max_bitrate_kbps.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_VBR_max_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_max_bitrate_kbps
lame_get_VBR_max_bitrate_kbps.restype = c_int
lame_get_VBR_max_bitrate_kbps.argtypes = [POINTER(lame_global_flags)]
lame_set_VBR_hard_min = _libraries['/usr/lib/libmp3lame.so'].lame_set_VBR_hard_min
lame_set_VBR_hard_min.restype = c_int
lame_set_VBR_hard_min.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_VBR_hard_min = _libraries['/usr/lib/libmp3lame.so'].lame_get_VBR_hard_min
lame_get_VBR_hard_min.restype = c_int
lame_get_VBR_hard_min.argtypes = [POINTER(lame_global_flags)]
lame_set_lowpassfreq = _libraries['/usr/lib/libmp3lame.so'].lame_set_lowpassfreq
lame_set_lowpassfreq.restype = c_int
lame_set_lowpassfreq.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_lowpassfreq = _libraries['/usr/lib/libmp3lame.so'].lame_get_lowpassfreq
lame_get_lowpassfreq.restype = c_int
lame_get_lowpassfreq.argtypes = [POINTER(lame_global_flags)]
lame_set_lowpasswidth = _libraries['/usr/lib/libmp3lame.so'].lame_set_lowpasswidth
lame_set_lowpasswidth.restype = c_int
lame_set_lowpasswidth.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_lowpasswidth = _libraries['/usr/lib/libmp3lame.so'].lame_get_lowpasswidth
lame_get_lowpasswidth.restype = c_int
lame_get_lowpasswidth.argtypes = [POINTER(lame_global_flags)]
lame_set_highpassfreq = _libraries['/usr/lib/libmp3lame.so'].lame_set_highpassfreq
lame_set_highpassfreq.restype = c_int
lame_set_highpassfreq.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_highpassfreq = _libraries['/usr/lib/libmp3lame.so'].lame_get_highpassfreq
lame_get_highpassfreq.restype = c_int
lame_get_highpassfreq.argtypes = [POINTER(lame_global_flags)]
lame_set_highpasswidth = _libraries['/usr/lib/libmp3lame.so'].lame_set_highpasswidth
lame_set_highpasswidth.restype = c_int
lame_set_highpasswidth.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_highpasswidth = _libraries['/usr/lib/libmp3lame.so'].lame_get_highpasswidth
lame_get_highpasswidth.restype = c_int
lame_get_highpasswidth.argtypes = [POINTER(lame_global_flags)]
lame_set_ATHonly = _libraries['/usr/lib/libmp3lame.so'].lame_set_ATHonly
lame_set_ATHonly.restype = c_int
lame_set_ATHonly.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_ATHonly = _libraries['/usr/lib/libmp3lame.so'].lame_get_ATHonly
lame_get_ATHonly.restype = c_int
lame_get_ATHonly.argtypes = [POINTER(lame_global_flags)]
lame_set_ATHshort = _libraries['/usr/lib/libmp3lame.so'].lame_set_ATHshort
lame_set_ATHshort.restype = c_int
lame_set_ATHshort.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_ATHshort = _libraries['/usr/lib/libmp3lame.so'].lame_get_ATHshort
lame_get_ATHshort.restype = c_int
lame_get_ATHshort.argtypes = [POINTER(lame_global_flags)]
lame_set_noATH = _libraries['/usr/lib/libmp3lame.so'].lame_set_noATH
lame_set_noATH.restype = c_int
lame_set_noATH.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_noATH = _libraries['/usr/lib/libmp3lame.so'].lame_get_noATH
lame_get_noATH.restype = c_int
lame_get_noATH.argtypes = [POINTER(lame_global_flags)]
lame_set_ATHtype = _libraries['/usr/lib/libmp3lame.so'].lame_set_ATHtype
lame_set_ATHtype.restype = c_int
lame_set_ATHtype.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_ATHtype = _libraries['/usr/lib/libmp3lame.so'].lame_get_ATHtype
lame_get_ATHtype.restype = c_int
lame_get_ATHtype.argtypes = [POINTER(lame_global_flags)]
lame_set_ATHlower = _libraries['/usr/lib/libmp3lame.so'].lame_set_ATHlower
lame_set_ATHlower.restype = c_int
lame_set_ATHlower.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_ATHlower = _libraries['/usr/lib/libmp3lame.so'].lame_get_ATHlower
lame_get_ATHlower.restype = c_float
lame_get_ATHlower.argtypes = [POINTER(lame_global_flags)]
lame_set_athaa_type = _libraries['/usr/lib/libmp3lame.so'].lame_set_athaa_type
lame_set_athaa_type.restype = c_int
lame_set_athaa_type.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_athaa_type = _libraries['/usr/lib/libmp3lame.so'].lame_get_athaa_type
lame_get_athaa_type.restype = c_int
lame_get_athaa_type.argtypes = [POINTER(lame_global_flags)]
lame_set_athaa_sensitivity = _libraries['/usr/lib/libmp3lame.so'].lame_set_athaa_sensitivity
lame_set_athaa_sensitivity.restype = c_int
lame_set_athaa_sensitivity.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_athaa_sensitivity = _libraries['/usr/lib/libmp3lame.so'].lame_get_athaa_sensitivity
lame_get_athaa_sensitivity.restype = c_float
lame_get_athaa_sensitivity.argtypes = [POINTER(lame_global_flags)]
lame_set_allow_diff_short = _libraries['/usr/lib/libmp3lame.so'].lame_set_allow_diff_short
lame_set_allow_diff_short.restype = c_int
lame_set_allow_diff_short.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_allow_diff_short = _libraries['/usr/lib/libmp3lame.so'].lame_get_allow_diff_short
lame_get_allow_diff_short.restype = c_int
lame_get_allow_diff_short.argtypes = [POINTER(lame_global_flags)]
lame_set_useTemporal = _libraries['/usr/lib/libmp3lame.so'].lame_set_useTemporal
lame_set_useTemporal.restype = c_int
lame_set_useTemporal.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_useTemporal = _libraries['/usr/lib/libmp3lame.so'].lame_get_useTemporal
lame_get_useTemporal.restype = c_int
lame_get_useTemporal.argtypes = [POINTER(lame_global_flags)]
lame_set_interChRatio = _libraries['/usr/lib/libmp3lame.so'].lame_set_interChRatio
lame_set_interChRatio.restype = c_int
lame_set_interChRatio.argtypes = [POINTER(lame_global_flags), c_float]
lame_get_interChRatio = _libraries['/usr/lib/libmp3lame.so'].lame_get_interChRatio
lame_get_interChRatio.restype = c_float
lame_get_interChRatio.argtypes = [POINTER(lame_global_flags)]
lame_set_no_short_blocks = _libraries['/usr/lib/libmp3lame.so'].lame_set_no_short_blocks
lame_set_no_short_blocks.restype = c_int
lame_set_no_short_blocks.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_no_short_blocks = _libraries['/usr/lib/libmp3lame.so'].lame_get_no_short_blocks
lame_get_no_short_blocks.restype = c_int
lame_get_no_short_blocks.argtypes = [POINTER(lame_global_flags)]
lame_set_force_short_blocks = _libraries['/usr/lib/libmp3lame.so'].lame_set_force_short_blocks
lame_set_force_short_blocks.restype = c_int
lame_set_force_short_blocks.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_force_short_blocks = _libraries['/usr/lib/libmp3lame.so'].lame_get_force_short_blocks
lame_get_force_short_blocks.restype = c_int
lame_get_force_short_blocks.argtypes = [POINTER(lame_global_flags)]
lame_set_emphasis = _libraries['/usr/lib/libmp3lame.so'].lame_set_emphasis
lame_set_emphasis.restype = c_int
lame_set_emphasis.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_emphasis = _libraries['/usr/lib/libmp3lame.so'].lame_get_emphasis
lame_get_emphasis.restype = c_int
lame_get_emphasis.argtypes = [POINTER(lame_global_flags)]
lame_get_version = _libraries['/usr/lib/libmp3lame.so'].lame_get_version
lame_get_version.restype = c_int
lame_get_version.argtypes = [POINTER(lame_global_flags)]
lame_get_encoder_delay = _libraries['/usr/lib/libmp3lame.so'].lame_get_encoder_delay
lame_get_encoder_delay.restype = c_int
lame_get_encoder_delay.argtypes = [POINTER(lame_global_flags)]
lame_get_encoder_padding = _libraries['/usr/lib/libmp3lame.so'].lame_get_encoder_padding
lame_get_encoder_padding.restype = c_int
lame_get_encoder_padding.argtypes = [POINTER(lame_global_flags)]
lame_get_framesize = _libraries['/usr/lib/libmp3lame.so'].lame_get_framesize
lame_get_framesize.restype = c_int
lame_get_framesize.argtypes = [POINTER(lame_global_flags)]
lame_get_mf_samples_to_encode = _libraries['/usr/lib/libmp3lame.so'].lame_get_mf_samples_to_encode
lame_get_mf_samples_to_encode.restype = c_int
lame_get_mf_samples_to_encode.argtypes = [POINTER(lame_global_flags)]
lame_get_size_mp3buffer = _libraries['/usr/lib/libmp3lame.so'].lame_get_size_mp3buffer
lame_get_size_mp3buffer.restype = c_int
lame_get_size_mp3buffer.argtypes = [POINTER(lame_global_flags)]
lame_get_frameNum = _libraries['/usr/lib/libmp3lame.so'].lame_get_frameNum
lame_get_frameNum.restype = c_int
lame_get_frameNum.argtypes = [POINTER(lame_global_flags)]
lame_get_totalframes = _libraries['/usr/lib/libmp3lame.so'].lame_get_totalframes
lame_get_totalframes.restype = c_int
lame_get_totalframes.argtypes = [POINTER(lame_global_flags)]
lame_get_RadioGain = _libraries['/usr/lib/libmp3lame.so'].lame_get_RadioGain
lame_get_RadioGain.restype = c_int
lame_get_RadioGain.argtypes = [POINTER(lame_global_flags)]
lame_get_AudiophileGain = _libraries['/usr/lib/libmp3lame.so'].lame_get_AudiophileGain
lame_get_AudiophileGain.restype = c_int
lame_get_AudiophileGain.argtypes = [POINTER(lame_global_flags)]
lame_get_PeakSample = _libraries['/usr/lib/libmp3lame.so'].lame_get_PeakSample
lame_get_PeakSample.restype = c_float
lame_get_PeakSample.argtypes = [POINTER(lame_global_flags)]
lame_get_noclipGainChange = _libraries['/usr/lib/libmp3lame.so'].lame_get_noclipGainChange
lame_get_noclipGainChange.restype = c_int
lame_get_noclipGainChange.argtypes = [POINTER(lame_global_flags)]
lame_get_noclipScale = _libraries['/usr/lib/libmp3lame.so'].lame_get_noclipScale
lame_get_noclipScale.restype = c_float
lame_get_noclipScale.argtypes = [POINTER(lame_global_flags)]
lame_init_params = _libraries['/usr/lib/libmp3lame.so'].lame_init_params
lame_init_params.restype = c_int
lame_init_params.argtypes = [POINTER(lame_global_flags)]
get_lame_version = _libraries['/usr/lib/libmp3lame.so'].get_lame_version
get_lame_version.restype = STRING
get_lame_version.argtypes = []
get_lame_short_version = _libraries['/usr/lib/libmp3lame.so'].get_lame_short_version
get_lame_short_version.restype = STRING
get_lame_short_version.argtypes = []
get_lame_very_short_version = _libraries['/usr/lib/libmp3lame.so'].get_lame_very_short_version
get_lame_very_short_version.restype = STRING
get_lame_very_short_version.argtypes = []
get_psy_version = _libraries['/usr/lib/libmp3lame.so'].get_psy_version
get_psy_version.restype = STRING
get_psy_version.argtypes = []
get_lame_url = _libraries['/usr/lib/libmp3lame.so'].get_lame_url
get_lame_url.restype = STRING
get_lame_url.argtypes = []
get_lame_os_bitness = _libraries['/usr/lib/libmp3lame.so'].get_lame_os_bitness
get_lame_os_bitness.restype = STRING
get_lame_os_bitness.argtypes = []
class lame_version_t(Structure):
    pass
lame_version_t._fields_ = [
    ('major', c_int),
    ('minor', c_int),
    ('alpha', c_int),
    ('beta', c_int),
    ('psy_major', c_int),
    ('psy_minor', c_int),
    ('psy_alpha', c_int),
    ('psy_beta', c_int),
    ('features', STRING),
]
get_lame_version_numerical = _libraries['/usr/lib/libmp3lame.so'].get_lame_version_numerical
get_lame_version_numerical.restype = None
get_lame_version_numerical.argtypes = [POINTER(lame_version_t)]
lame_print_config = _libraries['/usr/lib/libmp3lame.so'].lame_print_config
lame_print_config.restype = None
lame_print_config.argtypes = [POINTER(lame_global_flags)]
lame_print_internals = _libraries['/usr/lib/libmp3lame.so'].lame_print_internals
lame_print_internals.restype = None
lame_print_internals.argtypes = [POINTER(lame_global_flags)]
lame_encode_buffer = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer
lame_encode_buffer.restype = c_int
lame_encode_buffer.argtypes = [POINTER(lame_global_flags), POINTER(c_short), POINTER(c_short), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_interleaved = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_interleaved
lame_encode_buffer_interleaved.restype = c_int
lame_encode_buffer_interleaved.argtypes = [POINTER(lame_global_flags), POINTER(c_short), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_float = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_float
lame_encode_buffer_float.restype = c_int
lame_encode_buffer_float.argtypes = [POINTER(lame_global_flags), POINTER(c_float), POINTER(c_float), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_ieee_float = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_ieee_float
lame_encode_buffer_ieee_float.restype = c_int
lame_encode_buffer_ieee_float.argtypes = [lame_t, POINTER(c_float), POINTER(c_float), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_interleaved_ieee_float = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_interleaved_ieee_float
lame_encode_buffer_interleaved_ieee_float.restype = c_int
lame_encode_buffer_interleaved_ieee_float.argtypes = [lame_t, POINTER(c_float), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_ieee_double = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_ieee_double
lame_encode_buffer_ieee_double.restype = c_int
lame_encode_buffer_ieee_double.argtypes = [lame_t, POINTER(c_double), POINTER(c_double), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_interleaved_ieee_double = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_interleaved_ieee_double
lame_encode_buffer_interleaved_ieee_double.restype = c_int
lame_encode_buffer_interleaved_ieee_double.argtypes = [lame_t, POINTER(c_double), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_long = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_long
lame_encode_buffer_long.restype = c_int
lame_encode_buffer_long.argtypes = [POINTER(lame_global_flags), POINTER(c_long), POINTER(c_long), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_long2 = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_long2
lame_encode_buffer_long2.restype = c_int
lame_encode_buffer_long2.argtypes = [POINTER(lame_global_flags), POINTER(c_long), POINTER(c_long), c_int, POINTER(c_ubyte), c_int]
lame_encode_buffer_int = _libraries['/usr/lib/libmp3lame.so'].lame_encode_buffer_int
lame_encode_buffer_int.restype = c_int
lame_encode_buffer_int.argtypes = [POINTER(lame_global_flags), POINTER(c_int), POINTER(c_int), c_int, POINTER(c_ubyte), c_int]
lame_encode_flush = _libraries['/usr/lib/libmp3lame.so'].lame_encode_flush
lame_encode_flush.restype = c_int
lame_encode_flush.argtypes = [POINTER(lame_global_flags), POINTER(c_ubyte), c_int]
lame_encode_flush_nogap = _libraries['/usr/lib/libmp3lame.so'].lame_encode_flush_nogap
lame_encode_flush_nogap.restype = c_int
lame_encode_flush_nogap.argtypes = [POINTER(lame_global_flags), POINTER(c_ubyte), c_int]
lame_init_bitstream = _libraries['/usr/lib/libmp3lame.so'].lame_init_bitstream
lame_init_bitstream.restype = c_int
lame_init_bitstream.argtypes = [POINTER(lame_global_flags)]
lame_bitrate_hist = _libraries['/usr/lib/libmp3lame.so'].lame_bitrate_hist
lame_bitrate_hist.restype = None
lame_bitrate_hist.argtypes = [POINTER(lame_global_flags), POINTER(c_int)]
lame_bitrate_kbps = _libraries['/usr/lib/libmp3lame.so'].lame_bitrate_kbps
lame_bitrate_kbps.restype = None
lame_bitrate_kbps.argtypes = [POINTER(lame_global_flags), POINTER(c_int)]
lame_stereo_mode_hist = _libraries['/usr/lib/libmp3lame.so'].lame_stereo_mode_hist
lame_stereo_mode_hist.restype = None
lame_stereo_mode_hist.argtypes = [POINTER(lame_global_flags), POINTER(c_int)]
lame_bitrate_stereo_mode_hist = _libraries['/usr/lib/libmp3lame.so'].lame_bitrate_stereo_mode_hist
lame_bitrate_stereo_mode_hist.restype = None
lame_bitrate_stereo_mode_hist.argtypes = [POINTER(lame_global_flags), POINTER(c_int * 4)]
lame_block_type_hist = _libraries['/usr/lib/libmp3lame.so'].lame_block_type_hist
lame_block_type_hist.restype = None
lame_block_type_hist.argtypes = [POINTER(lame_global_flags), POINTER(c_int)]
lame_bitrate_block_type_hist = _libraries['/usr/lib/libmp3lame.so'].lame_bitrate_block_type_hist
lame_bitrate_block_type_hist.restype = None
lame_bitrate_block_type_hist.argtypes = [POINTER(lame_global_flags), POINTER(c_int * 6)]
lame_mp3_tags_fid = _libraries['/usr/lib/libmp3lame.so'].lame_mp3_tags_fid
lame_mp3_tags_fid.restype = None
lame_mp3_tags_fid.argtypes = [POINTER(lame_global_flags), POINTER(FILE)]
lame_get_lametag_frame = _libraries['/usr/lib/libmp3lame.so'].lame_get_lametag_frame
lame_get_lametag_frame.restype = size_t
lame_get_lametag_frame.argtypes = [POINTER(lame_global_flags), POINTER(c_ubyte), size_t]
lame_close = _libraries['/usr/lib/libmp3lame.so'].lame_close
lame_close.restype = c_int
lame_close.argtypes = [POINTER(lame_global_flags)]
class hip_global_struct(Structure):
    pass
hip_global_struct._fields_ = [
]
hip_global_flags = hip_global_struct
hip_t = POINTER(hip_global_flags)
class mp3data_struct(Structure):
    pass
mp3data_struct._fields_ = [
    ('header_parsed', c_int),
    ('stereo', c_int),
    ('samplerate', c_int),
    ('bitrate', c_int),
    ('mode', c_int),
    ('mode_ext', c_int),
    ('framesize', c_int),
    ('nsamp', c_ulong),
    ('totalframes', c_int),
    ('framenum', c_int),
]
hip_decode_init = _libraries['/usr/lib/libmp3lame.so'].hip_decode_init
hip_decode_init.restype = hip_t
hip_decode_init.argtypes = []
hip_decode_exit = _libraries['/usr/lib/libmp3lame.so'].hip_decode_exit
hip_decode_exit.restype = c_int
hip_decode_exit.argtypes = [hip_t]
hip_set_errorf = _libraries['/usr/lib/libmp3lame.so'].hip_set_errorf
hip_set_errorf.restype = None
hip_set_errorf.argtypes = [hip_t, lame_report_function]
hip_set_debugf = _libraries['/usr/lib/libmp3lame.so'].hip_set_debugf
hip_set_debugf.restype = None
hip_set_debugf.argtypes = [hip_t, lame_report_function]
hip_set_msgf = _libraries['/usr/lib/libmp3lame.so'].hip_set_msgf
hip_set_msgf.restype = None
hip_set_msgf.argtypes = [hip_t, lame_report_function]
hip_decode = _libraries['/usr/lib/libmp3lame.so'].hip_decode
hip_decode.restype = c_int
hip_decode.argtypes = [hip_t, POINTER(c_ubyte), size_t, POINTER(c_short), POINTER(c_short)]
hip_decode_headers = _libraries['/usr/lib/libmp3lame.so'].hip_decode_headers
hip_decode_headers.restype = c_int
hip_decode_headers.argtypes = [hip_t, POINTER(c_ubyte), size_t, POINTER(c_short), POINTER(c_short), POINTER(mp3data_struct)]
hip_decode1 = _libraries['/usr/lib/libmp3lame.so'].hip_decode1
hip_decode1.restype = c_int
hip_decode1.argtypes = [hip_t, POINTER(c_ubyte), size_t, POINTER(c_short), POINTER(c_short)]
hip_decode1_headers = _libraries['/usr/lib/libmp3lame.so'].hip_decode1_headers
hip_decode1_headers.restype = c_int
hip_decode1_headers.argtypes = [hip_t, POINTER(c_ubyte), size_t, POINTER(c_short), POINTER(c_short), POINTER(mp3data_struct)]
hip_decode1_headersB = _libraries['/usr/lib/libmp3lame.so'].hip_decode1_headersB
hip_decode1_headersB.restype = c_int
hip_decode1_headersB.argtypes = [hip_t, POINTER(c_ubyte), size_t, POINTER(c_short), POINTER(c_short), POINTER(mp3data_struct), POINTER(c_int), POINTER(c_int)]
id3tag_genre_list = _libraries['/usr/lib/libmp3lame.so'].id3tag_genre_list
id3tag_genre_list.restype = None
id3tag_genre_list.argtypes = [CFUNCTYPE(None, c_int, STRING, c_void_p), c_void_p]
id3tag_init = _libraries['/usr/lib/libmp3lame.so'].id3tag_init
id3tag_init.restype = None
id3tag_init.argtypes = [lame_t]
id3tag_add_v2 = _libraries['/usr/lib/libmp3lame.so'].id3tag_add_v2
id3tag_add_v2.restype = None
id3tag_add_v2.argtypes = [lame_t]
id3tag_v1_only = _libraries['/usr/lib/libmp3lame.so'].id3tag_v1_only
id3tag_v1_only.restype = None
id3tag_v1_only.argtypes = [lame_t]
id3tag_v2_only = _libraries['/usr/lib/libmp3lame.so'].id3tag_v2_only
id3tag_v2_only.restype = None
id3tag_v2_only.argtypes = [lame_t]
id3tag_space_v1 = _libraries['/usr/lib/libmp3lame.so'].id3tag_space_v1
id3tag_space_v1.restype = None
id3tag_space_v1.argtypes = [lame_t]
id3tag_pad_v2 = _libraries['/usr/lib/libmp3lame.so'].id3tag_pad_v2
id3tag_pad_v2.restype = None
id3tag_pad_v2.argtypes = [lame_t]
id3tag_set_pad = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_pad
id3tag_set_pad.restype = None
id3tag_set_pad.argtypes = [lame_t, size_t]
id3tag_set_title = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_title
id3tag_set_title.restype = None
id3tag_set_title.argtypes = [lame_t, STRING]
id3tag_set_artist = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_artist
id3tag_set_artist.restype = None
id3tag_set_artist.argtypes = [lame_t, STRING]
id3tag_set_album = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_album
id3tag_set_album.restype = None
id3tag_set_album.argtypes = [lame_t, STRING]
id3tag_set_year = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_year
id3tag_set_year.restype = None
id3tag_set_year.argtypes = [lame_t, STRING]
id3tag_set_comment = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_comment
id3tag_set_comment.restype = None
id3tag_set_comment.argtypes = [lame_t, STRING]
id3tag_set_track = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_track
id3tag_set_track.restype = c_int
id3tag_set_track.argtypes = [lame_t, STRING]
id3tag_set_genre = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_genre
id3tag_set_genre.restype = c_int
id3tag_set_genre.argtypes = [lame_t, STRING]
id3tag_set_fieldvalue = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_fieldvalue
id3tag_set_fieldvalue.restype = c_int
id3tag_set_fieldvalue.argtypes = [lame_t, STRING]
id3tag_set_albumart = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_albumart
id3tag_set_albumart.restype = c_int
id3tag_set_albumart.argtypes = [lame_t, STRING, size_t]
lame_get_id3v1_tag = _libraries['/usr/lib/libmp3lame.so'].lame_get_id3v1_tag
lame_get_id3v1_tag.restype = size_t
lame_get_id3v1_tag.argtypes = [lame_t, POINTER(c_ubyte), size_t]
lame_get_id3v2_tag = _libraries['/usr/lib/libmp3lame.so'].lame_get_id3v2_tag
lame_get_id3v2_tag.restype = size_t
lame_get_id3v2_tag.argtypes = [lame_t, POINTER(c_ubyte), size_t]
lame_set_write_id3tag_automatic = _libraries['/usr/lib/libmp3lame.so'].lame_set_write_id3tag_automatic
lame_set_write_id3tag_automatic.restype = None
lame_set_write_id3tag_automatic.argtypes = [POINTER(lame_global_flags), c_int]
lame_get_write_id3tag_automatic = _libraries['/usr/lib/libmp3lame.so'].lame_get_write_id3tag_automatic
lame_get_write_id3tag_automatic.restype = c_int
lame_get_write_id3tag_automatic.argtypes = [POINTER(lame_global_flags)]
id3tag_set_textinfo_latin1 = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_textinfo_latin1
id3tag_set_textinfo_latin1.restype = c_int
id3tag_set_textinfo_latin1.argtypes = [lame_t, STRING, STRING]
id3tag_set_comment_latin1 = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_comment_latin1
id3tag_set_comment_latin1.restype = c_int
id3tag_set_comment_latin1.argtypes = [lame_t, STRING, STRING, STRING]
id3tag_set_fieldvalue_utf16 = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_fieldvalue_utf16
id3tag_set_fieldvalue_utf16.restype = c_int
id3tag_set_fieldvalue_utf16.argtypes = [lame_t, POINTER(c_ushort)]
id3tag_set_textinfo_utf16 = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_textinfo_utf16
id3tag_set_textinfo_utf16.restype = c_int
id3tag_set_textinfo_utf16.argtypes = [lame_t, STRING, POINTER(c_ushort)]
id3tag_set_comment_utf16 = _libraries['/usr/lib/libmp3lame.so'].id3tag_set_comment_utf16
id3tag_set_comment_utf16.restype = c_int
id3tag_set_comment_utf16.argtypes = [lame_t, STRING, POINTER(c_ushort), POINTER(c_ushort)]
bitrate_table = (c_int * 16 * 3).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'bitrate_table')
samplerate_table = (c_int * 4 * 3).in_dll(_libraries['/usr/lib/libmp3lame.so'], 'samplerate_table')
lame_get_bitrate = _libraries['/usr/lib/libmp3lame.so'].lame_get_bitrate
lame_get_bitrate.restype = c_int
lame_get_bitrate.argtypes = [c_int, c_int]
lame_get_samplerate = _libraries['/usr/lib/libmp3lame.so'].lame_get_samplerate
lame_get_samplerate.restype = c_int
lame_get_samplerate.argtypes = [c_int, c_int]

# values for enumeration 'lame_errorcodes_t'
lame_errorcodes_t = c_int # enum
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
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp3lame.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp3lame.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp3lame.so'], '_IO_2_1_stderr_')
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
__underflow = _libraries['/usr/lib/libmp3lame.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/lib/libmp3lame.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/lib/libmp3lame.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/lib/libmp3lame.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/lib/libmp3lame.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/lib/libmp3lame.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/lib/libmp3lame.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/lib/libmp3lame.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/lib/libmp3lame.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/lib/libmp3lame.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/lib/libmp3lame.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/lib/libmp3lame.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag), POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/lib/libmp3lame.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag)]
_IO_padn = _libraries['/usr/lib/libmp3lame.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/lib/libmp3lame.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/lib/libmp3lame.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/lib/libmp3lame.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/lib/libmp3lame.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
__FILE = _IO_FILE
off_t = __off_t
off64_t = __off64_t
ssize_t = __ssize_t
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/lib/libmp3lame.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/lib/libmp3lame.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/lib/libmp3lame.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/lib/libmp3lame.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/lib/libmp3lame.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/lib/libmp3lame.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/lib/libmp3lame.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/lib/libmp3lame.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/lib/libmp3lame.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/lib/libmp3lame.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/lib/libmp3lame.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/lib/libmp3lame.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/lib/libmp3lame.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/lib/libmp3lame.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/lib/libmp3lame.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/lib/libmp3lame.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/lib/libmp3lame.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/lib/libmp3lame.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/lib/libmp3lame.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/lib/libmp3lame.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/lib/libmp3lame.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/lib/libmp3lame.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/lib/libmp3lame.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/lib/libmp3lame.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fscanf = _libraries['/usr/lib/libmp3lame.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/lib/libmp3lame.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/lib/libmp3lame.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/lib/libmp3lame.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['/usr/lib/libmp3lame.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['/usr/lib/libmp3lame.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['/usr/lib/libmp3lame.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/lib/libmp3lame.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/lib/libmp3lame.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/lib/libmp3lame.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/lib/libmp3lame.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/lib/libmp3lame.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
gets = _libraries['/usr/lib/libmp3lame.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
__getdelim = _libraries['/usr/lib/libmp3lame.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/lib/libmp3lame.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/lib/libmp3lame.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/lib/libmp3lame.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/lib/libmp3lame.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fwrite = _libraries['/usr/lib/libmp3lame.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/lib/libmp3lame.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/lib/libmp3lame.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/lib/libmp3lame.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/lib/libmp3lame.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/lib/libmp3lame.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/lib/libmp3lame.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/lib/libmp3lame.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/lib/libmp3lame.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/lib/libmp3lame.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/lib/libmp3lame.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/lib/libmp3lame.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/lib/libmp3lame.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/lib/libmp3lame.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/lib/libmp3lame.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/lib/libmp3lame.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/lib/libmp3lame.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/lib/libmp3lame.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/lib/libmp3lame.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/lib/libmp3lame.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/lib/libmp3lame.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/lib/libmp3lame.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/lib/libmp3lame.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/lib/libmp3lame.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/lib/libmp3lame.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
obstack._fields_ = [
]
flockfile = _libraries['/usr/lib/libmp3lame.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/lib/libmp3lame.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/lib/libmp3lame.so'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
va_list = __gnuc_va_list
ptrdiff_t = c_long
__all__ = ['lame_set_VBR_quality', '_ATFILE_SOURCE', 'EOF',
           '__glibc_unlikely', 'getc_unlocked', '_IO_USER_LOCK',
           'freopen64', 'lame_block_type_hist', 'JOINT_STEREO',
           '__int16_t', 'fsetpos', 'fpos_t', '_G_HAVE_MREMAP', 'MONO',
           'ftell', 'va_end', 'lame_set_highpassfreq', '_G_va_list',
           'getline', 'lame_set_experimentalZ',
           'lame_set_interChRatio', '_IO_BUFSIZ', 'LAME_NOMEM',
           'id3tag_set_year', '__FILE', 'get_psy_version',
           '_IO_off64_t', 'lame_set_experimentalX',
           'lame_get_lametag_frame', '_IO_fpos64_t',
           'lame_init_bitstream', 'lame_get_nogap_total', '__time_t',
           'PSY_NSPSYTUNE', '__GLIBC_PREREQ', 'lame_get_RadioGain',
           'lame_set_extension', '__ASMNAME', 'LAME_BADSAMPFREQ',
           '_POSIX_SOURCE', '_IO_jump_t',
           'lame_set_disable_reservoir', 'MAX_INDICATOR', 'stderr',
           'lame_set_asm_optimizations', 'lame_set_ATHshort',
           'lame_get_ATHlower', 'fputc_unlocked', '__uint64_t',
           '_DEFAULT_SOURCE', 'snprintf', '__va_list_tag',
           '__off64_t', 'lame_encode_buffer_interleaved_ieee_double',
           'lame_set_ATHlower', '_IO_uid_t', 'lame_set_quality',
           'hip_decode_headers', 'lame_get_num_channels',
           '__USE_POSIX199309', '__clockid_t', 'getchar_unlocked',
           'lame_init', '_IO_SHOWBASE', 'NOT_SET', '_G_HAVE_MMAP',
           '__codecvt_partial', '__attribute_format_strfmon__',
           'STANDARD_FAST', 'id3tag_set_fieldvalue_utf16',
           'open_memstream', 'fsetpos64', '_IO_DONT_CLOSE',
           '__u_long', 'id3tag_set_comment_utf16', '_IO_SKIPWS',
           'FRONTEND_READERROR', 'buffer_constraint_e', 'popen',
           '_IO_SCIENTIFIC', 'lame_set_decode_only',
           'lame_encode_buffer_ieee_double',
           'lame_get_error_protection', 'lame_bitrate_hist', '__PMT',
           'lame_set_VBR', '_LARGEFILE_SOURCE', '__mode_t',
           'lame_get_force_short_blocks', 'vbr_off', '_IO_DEC',
           '__off_t', 'fmemopen', 'DUAL_CHANNEL', 'VBR_40',
           'lame_get_VBR_min_bitrate_kbps', 'getchar',
           'id3tag_set_track', 'lame_get_num_samples',
           'vbr_max_indicator', 'lame_set_bWriteVbrTag',
           'lame_set_lowpassfreq', 'lame_set_decode_on_the_fly',
           '_IOS_TRUNC', 'fclose', 'id3tag_set_fieldvalue',
           'ftello64', 'get_lame_version_numerical',
           '__USE_FORTIFY_LEVEL', '__int8_t', '__fsblkcnt64_t',
           'vbr_mt', 'lame_encode_buffer_float', 'MDB_STRICT_ISO',
           'lame_get_scale_right', 'vbr_mode', 'SEEK_HOLE',
           '__USE_XOPEN_EXTENDED', 'fopencookie', 'MMX',
           'lame_set_strict_ISO', 'ftrylockfile',
           'lame_set_allow_diff_short', 'VBR_30', '__fsfilcnt64_t',
           '_IO_pid_t', '_IO_FILE', 'hip_decode', 'lame_set_noATH',
           'VBR_100', '_IO_BOOLALPHA', '__io_read_fn', '_IO_UNITBUF',
           'lame_get_original', 'off_t', 'lame_close', 'vbr_abr',
           'fprintf', 'lame_get_ATHshort', '__fsblkcnt_t',
           '__STDC_CONSTANT_MACROS', 'feof',
           'lame_set_quant_comp_short', 'lame_set_num_channels',
           'clearerr', '__fsid_t', '__WORDSIZE',
           'lame_set_force_short_blocks', 'putc_unlocked',
           'flockfile', 'vasprintf', '_IO_free_backup_area',
           'lame_set_nogap_currentindex', 'lame_set_msfix',
           '__USE_ISOC95', 'lame_get_highpasswidth', '__GLIBC__',
           '__USE_ISOC99', 'id3tag_init', 'funlockfile', '_IO_fpos_t',
           'lame_get_VBR', 'lame_get_copyright', 'stdin', '__u_int',
           '__sprintf_chk', 'hip_decode1_headers', 'ssize_t',
           '__clock_t', 'lame_encode_buffer_long', '__fsfilcnt_t',
           'samplerate_table', 'PSY_GPSYCHO', 'lame_get_samplerate',
           'vscanf', '__glibc_likely', '_IONBF', 'FILE',
           'ferror_unlocked', 'size_t', '__USE_XOPEN', 'V0',
           'lame_set_analysis', '_IO_ferror', '__USE_POSIX2',
           'PAD_ALL', 'fwrite', 'lame_get_strict_ISO',
           '_IO_ftrylockfile', '__USE_XOPEN2K8XSI',
           '__syscall_slong_t', 'id3tag_v2_only', 'feof_unlocked',
           '__qaddr_t', 'lame_get_exp_nspsytune',
           'lame_get_free_format', 'id3tag_set_comment_latin1',
           '_IO_RIGHT', '_IOS_APPEND', 'get_lame_os_bitness',
           'lame_get_noclipGainChange', 'VBR_70', 'fpos64_t',
           '__asprintf_chk', '__USE_ATFILE', 'LAME_MAXALBUMART',
           'EXTREME_FAST', 'TMP_MAX', 'PAD_ADJUST', '_G_BUFSIZ',
           '__vprintf_chk', 'PAD_MAX_INDICATOR',
           'lame_get_nogap_currentindex', 'getdelim', '__int32_t',
           '__USE_POSIX', 'lame_print_internals', '_IO_NO_WRITES',
           'lame_get_decode_on_the_fly', 'vsscanf', '_IO_funlockfile',
           '__fsword_t', '__FILE_defined', 'lame_set_ATHonly',
           'fwrite_unlocked', 'Psy_model_e', 'lame_set_msgf',
           '_IO_NO_READS', '__useconds_t', '_XOPEN_SOURCE',
           '__GLIBC_MINOR__', '_IO_CURRENTLY_PUTTING', '_STDIO_H',
           'R3MIX', 'LAME_MAXMP3BUFFER', 'sprintf',
           'lame_set_experimentalY', 'asm_optimizations',
           'lame_set_num_samples', 'lame_get_encoder_padding',
           'lame_get_VBR_hard_min', 'lame_set_in_samplerate',
           'id3tag_pad_v2', 'id3tag_space_v1', 'asprintf',
           '__printf_chk', '__WORDSIZE_TIME64_COMPAT32',
           '_IO_cookie_io_functions_t', 'lame_set_debugf',
           '__gnuc_va_list', '__P', 'preset_mode', '_IO_ERR_SEEN',
           'fseeko', 'putchar', '__USE_GNU',
           'get_lame_very_short_version', 'lame_get_no_short_blocks',
           '__attribute_format_arg__', 'SSE', 'ferror', '__rlim64_t',
           '_G_IO_IO_FILE_VERSION', '__REDIRECT_NTH_LDBL',
           '_POSIX_C_SOURCE', 'lame_get_analysis', '_IO_ssize_t',
           'PAD_NO', '__blksize_t', 'lame_set_nogap_total',
           '__USE_SVID', 'lame_get_AudiophileGain', '_IO_seekoff',
           'lame_get_force_ms', 'lame_get_out_samplerate',
           '_IO_IS_APPENDING', 'lame_get_emphasis', '_sys_nerr',
           'scanf', 'lame_set_findReplayGain',
           'lame_set_VBR_max_bitrate_kbps',
           'lame_get_allow_diff_short', 'get_lame_short_version',
           '__asprintf', 'L_ctermid', 'lame_get_VBR_quality',
           '__mbstate_t', '__uint8_t', 'setbuffer', '_IO_INTERNAL',
           '__u_char', 'hip_decode1', '__obstack_printf_chk',
           '__blkcnt64_t', '_IOS_NOCREATE', 'dprintf',
           '__vdprintf_chk', '_IO_TIED_PUT_GET',
           'hip_decode1_headersB', '__fprintf_chk',
           'lame_get_quality', '__USE_LARGEFILE',
           '__USE_EXTERN_INLINES', 'lame_get_PeakSample', '_IO_BE',
           '_FEATURES_H', 'lame_get_noclipScale',
           'lame_get_experimentalX', 'SEEK_DATA',
           'lame_set_scale_left', 'vsnprintf', '_IO_peekc_locked',
           '_BITS_TYPES_H', 'lame_set_athaa_type',
           'lame_set_lowpasswidth', '__fread_chk', '__rlim_t',
           'va_list', '_XOPEN_SOURCE_EXTENDED', 'VBR_20', '_IO_off_t',
           'lame_errorcodes_t', 'lame_get_VBR_q', '_IO_UNBUFFERED',
           'lame_set_preset', 'lame_get_mode', '_IOS_ATEND',
           'hip_global_struct', 'id3tag_set_pad', 'vbr_rh',
           'lame_get_mf_samples_to_encode',
           'DEPRECATED_OR_OBSOLETE_CODE_REMOVED', 'perror', 'VBR_90',
           '__quad_t', 'fscanf', '__key_t', 'fseeko64',
           '__obstack_vprintf_chk', '__uid_t', 'LAME_NOERROR',
           'buffer_constraint', 'setvbuf', 'vfprintf', '__uint16_t',
           'obstack_vprintf', '_IO_putc', 'lame_get_extension',
           '__GNU_LIBRARY__', '_BITS_TYPESIZES_H', 'putchar_unlocked',
           '_IO_USER_BUF', '__USE_LARGEFILE64', 'fputc',
           'lame_encode_flush_nogap', '__underflow', '_IO_2_1_stdin_',
           'fgetpos64', 'lame_set_emphasis', 'hip_set_errorf',
           'fputs', '_IO_LINE_BUF', 'lame_get_bWriteVbrTag',
           'lame_get_disable_reservoir', 'lame_get_quant_comp',
           '__loff_t', '_G_config_h', '____mbstate_t_defined',
           'cookie_seek_function_t', '_IO_FLAGS2_MMAP',
           'LAME_INTERNALERROR', 'lame_get_write_id3tag_automatic',
           'id3tag_add_v2', 'fileno', 'FOPEN_MAX',
           '_IO_DELETE_DONT_CLOSE', 'lame_set_out_samplerate',
           'lame_set_VBR_hard_min', 'remove', '_G_fpos_t',
           'lame_mp3_tags_fid', '__fgets_chk', 'lame_set_ATHtype',
           '__bos', 'INSANE', '__ssize_t', 'VBR_60',
           'lame_get_ATHtype', 'lame_print_config',
           'hip_global_flags', '__io_write_fn', '__warnattr',
           'lame_get_VBR_mean_bitrate_kbps',
           'lame_set_compression_ratio', 'lame_get_id3v2_tag',
           '_sys_errlist', 'fgetpos', 'lame_get_brate',
           'asm_optimizations_e', '_IO_padn', 'vdprintf',
           'lame_set_VBR_mean_bitrate_kbps', '__getdelim',
           'lame_encode_buffer_ieee_float', '__USE_XOPEN2K',
           '__FD_SETSIZE', 'lame_bitrate_stereo_mode_hist',
           'Padding_type', 'lame_get_highpassfreq', '__intptr_t',
           'tmpnam_r', '_IO_LINKED', '_IO_FILE_plus',
           'LAME_BADBITRATE', '_IO_va_list', '__blkcnt_t',
           'MEDIUM_FAST', '_IO_size_t', 'lame_get_interChRatio',
           'lame_encode_buffer_interleaved', 'lame_bitrate_kbps',
           '__vsnprintf_chk', '_IO_flockfile', '_IOS_INPUT',
           'lame_set_error_protection', 'FRONTEND_WRITEERROR',
           'L_tmpnam', 'off64_t', 'V2', 'lame_t', '_IOS_BIN',
           '__uflow', 'tmpfile64', 'sys_nerr', '_IO_BAD_SEEN',
           '__USE_MISC', 'putw', 'puts', 'clearerr_unlocked',
           'obstack', 'N11__mbstate_t3DOT_2E', 'va_arg',
           'lame_stereo_mode_hist', 'putc', 'hip_set_msgf', '_IO_HEX',
           'lame_set_free_format', 'lame_set_scale_right', 'tmpnam',
           '__OFF_T_MATCHES_OFF64_T', 'STANDARD',
           'lame_set_VBR_min_bitrate_kbps', 'lame_set_scale',
           '__dev_t', 'FILENAME_MAX', 'L_cuserid',
           'lame_encode_buffer_long2', 'lame_set_athaa_sensitivity',
           '__suseconds_t', 'lame_set_highpasswidth', '__dprintf_chk',
           'lame_encode_buffer_interleaved_ieee_float', 'hip_t',
           'id3tag_set_genre', 'lame_set_useTemporal',
           'lame_get_noATH', 'vsprintf', 'rename', 'rewind',
           '__USE_POSIX199506', 'stdout',
           'lame_get_VBR_max_bitrate_kbps', 'lame_set_errorf',
           '__INO_T_MATCHES_INO64_T', 'lame_report_function',
           'lame_encode_buffer', 'getc', 'vbr_mtrh', 'V1', 'ABR_320',
           'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
           'hip_decode_init', 'gets', '_SYS_CDEFS_H', 'getw',
           '_OLD_STDIO_MAGIC', 'va_copy', 'lame_set_copyright',
           '__snprintf_chk', '_IO_IS_FILEBUF', 'SEEK_SET',
           'lame_get_lowpassfreq', 'lame_get_totalframes',
           '_IOS_OUTPUT', 'lame_get_lowpasswidth', '__ino_t',
           '__vsprintf_chk', '_IO_lock_t', 'setbuf',
           '_IO_2_1_stdout_', '__REDIRECT_LDBL', 'MPEG_mode_e',
           'id3tag_set_album', 'VBR_10', 'lame_get_scale_left',
           'mp3data_struct', 'vbr_default', 'lame_get_id3v1_tag',
           'lame_get_in_samplerate', '__int64_t', 'fopen64',
           'get_lame_url', 'Psy_model', 'fseek', '__USE_XOPEN2KXSI',
           'cookie_write_function_t', '_IO_LEFT', '_IO_marker',
           'Padding_type_e', '__timer_t', 'fflush', 'MPEG_mode',
           '__uint32_t', '__USE_XOPEN2K8', 'lame_get_scale',
           'fflush_unlocked', 'id3tag_set_albumart',
           'lame_global_struct', 'P_tmpdir', '__ino64_t',
           'lame_encode_flush', 'VBR_80', 'hip_decode_exit',
           '_IO_SHOWPOINT', '_IO_sgetn', '__fread_unlocked_chk',
           '_IO_FLAGS2_NOTCANCEL', 'lame_get_size_mp3buffer',
           'va_start', 'STEREO', 'renameat', 'AMD_3DNOW',
           '__fgets_unlocked_chk', '_G_fpos64_t', 'hip_set_debugf',
           '_ISOC95_SOURCE', '_ISOC99_SOURCE', 'freopen', '__nlink_t',
           'lame_version_t', 'sscanf', 'fread_unlocked', 'tempnam',
           'tmpfile', '__syscall_ulong_t', 'lame_get_bitrate',
           '__io_close_fn', 'fgetc', 'pclose', 'printf',
           'LAME_GENERICERROR', '__pid_t', '_IO_SHOWPOS',
           '__codecvt_ok', 'fgets', '__codecvt_noconv', '_IO_MAGIC',
           'lame_set_VBR_q', 'ctermid', '__id_t',
           'cookie_io_functions_t', 'lame_encode_buffer_int',
           '_IO_feof', 'lame_set_quant_comp', '__SYSCALL_WORDSIZE',
           'fgetc_unlocked', 'cookie_close_function_t',
           '_IO_UPPERCASE', 'lame_get_compression_ratio',
           '_IO_EOF_SEEN', '_IO_vfprintf', '_IO_FIXED',
           'id3tag_set_title', 'lame_get_framesize', 'MEDIUM',
           '__vfprintf_chk', '_SVID_SOURCE', '__codecvt_result',
           '__vasprintf_chk', 'fcloseall', 'bitrate_table', 'VBR_50',
           '_IOFBF', 'SEEK_END', '_IO_peekc', '__USE_BSD',
           'MDB_MAXIMUM', 'sys_errlist', '__CONCAT', 'ptrdiff_t',
           'ABR_8', '_IO_IN_BACKUP', '_IOS_NOREPLACE', 'LAME_OKAY',
           '_ISOC11_SOURCE', 'obstack_printf', '____FILE_defined',
           'SEEK_CUR', 'fputs_unlocked', '__USE_UNIX98', '_IO_STDIO',
           'fgets_unlocked', 'fopen',
           'lame_set_write_id3tag_automatic', '__gid_t', 'fdopen',
           'id3tag_set_comment', '_IO_OCT', 'lame_init_params',
           '__daddr_t', 'lame_set_no_short_blocks', '_IO_cookie_file',
           '__caddr_t', 'lame_set_mode', 'vprintf', '__io_seek_fn',
           'lame_get_decode_only', 'lame_get_version', 'BUFSIZ',
           'lame_get_frameNum', 'id3tag_set_textinfo_latin1',
           '__overflow', 'lame_set_exp_nspsytune',
           'lame_get_athaa_type', '_IO_getc',
           'lame_get_athaa_sensitivity', '_IO_UNIFIED_JUMPTABLES',
           'cuserid', 'id3tag_set_textinfo_utf16', 'lame_get_ATHonly',
           '_IO_vfscanf', 'cookie_read_function_t', 'ungetc',
           'EXTREME', 'lame_get_useTemporal', 'fileno_unlocked',
           '_IO_2_1_stderr_', 'fread', 'ftello',
           '_IO_FLAGS2_USER_WBUF', '__STRING', 'lame_set_brate',
           '_IO_seekpos', 'lame_get_findReplayGain', '__GNUC_PREREQ',
           '__va_copy', 'preset_mode_e', 'lame_set_original',
           '_IO_MAGIC_MASK', 'lame_get_experimentalZ',
           'lame_get_experimentalY', 'FRONTEND_FILETOOLARGE',
           '__u_quad_t', '__u_short', 'vfscanf',
           'lame_bitrate_block_type_hist', '_BSD_SOURCE',
           '_LARGEFILE64_SOURCE', 'id3tag_genre_list',
           '__va_arg_pack', 'lame_set_force_ms', '__codecvt_error',
           '__va_arg_pack_len', '__bos0', 'id3tag_v1_only',
           'lame_get_quant_comp_short', 'lame_get_msfix',
           'lame_global_flags', 'id3tag_set_artist', 'setlinebuf',
           'lame_get_encoder_delay', '__socklen_t', '__USE_ISOC11',
           'get_lame_version', 'MDB_DEFAULT', '_IOLBF', 'offsetof',
           'vbr_mode_e']
