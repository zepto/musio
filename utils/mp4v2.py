from ctypes import *

_libraries = {}
_libraries['/usr/lib/libmp4v2.so'] = CDLL('/usr/lib/libmp4v2.so')
STRING = c_char_p


def MP4_IS_VALID_SAMPLE_ID(x): return ((x) != MP4_INVALID_SAMPLE_ID) # macro
# def MP4_IS_OD_TRACK_TYPE(type): return (!strcasecmp(type, MP4_OD_TRACK_TYPE)) # macro
def INTMAX_C(c): return c ## L # macro
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# def MP4_IS_MPEG2_VIDEO_TYPE(type): return (((type) >= MP4_MPEG2_SIMPLE_VIDEO_TYPE && (type) <= MP4_MPEG2_442_VIDEO_TYPE) || MP4_IS_MPEG1_VIDEO_TYPE(type)) # macro
# def MP4_IS_MPEG2_AAC_AUDIO_TYPE(type): return (((type) >= MP4_MPEG2_AAC_MAIN_AUDIO_TYPE && (type) <= MP4_MPEG2_AAC_SSR_AUDIO_TYPE)) # macro
def MP4_IS_VALID_FILE_HANDLE(x): return ((x) != MP4_INVALID_FILE_HANDLE) # macro
def MP4_IS_MPEG1_VIDEO_TYPE(type): return ((type) == MP4_MPEG1_VIDEO_TYPE) # macro
MP4_ITMF_BT_DATETIME = 17
# def MP4_IS_MP3_AUDIO_TYPE(type): return ((type) == MP4_MPEG1_AUDIO_TYPE || (type) == MP4_MPEG2_AUDIO_TYPE) # macro
# def MP4_IS_HINT_TRACK_TYPE(type): return (!strcasecmp(type, MP4_HINT_TRACK_TYPE)) # macro
MP4ChapterTypeNone = 0
# def MP4_IS_AUDIO_TRACK_TYPE(type): return (!strcasecmp(type, MP4_AUDIO_TRACK_TYPE)) # macro
def MP4_IS_VALID_EDIT_ID(x): return ((x) != MP4_INVALID_EDIT_ID) # macro
FILEMODE_MODIFY = 2
def MP4_IS_VALID_DURATION(x): return ((x) != MP4_INVALID_DURATION) # macro
# def MP4_IS_SYSTEMS_TRACK_TYPE(type): return (!strcasecmp(type, MP4_CLOCK_TRACK_TYPE) || !strcasecmp(type, MP4_MPEG7_TRACK_TYPE) || !strcasecmp(type, MP4_OCI_TRACK_TYPE) || !strcasecmp(type, MP4_IPMP_TRACK_TYPE) || !strcasecmp(type, MP4_MPEGJ_TRACK_TYPE)) # macro
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
# def MP4_IS_SCENE_TRACK_TYPE(type): return (!strcasecmp(type, MP4_SCENE_TRACK_TYPE)) # macro
def INT16_C(c): return c # macro
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
# __S32_TYPE = int # alias
# __PID_T_TYPE = __S32_TYPE # alias
# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def MP4_IS_VIDEO_TRACK_TYPE(type): return (!strcasecmp(type, MP4_VIDEO_TRACK_TYPE)) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
class _IO_FILE(Structure):
    pass
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp4v2.so'], 'stdin')
stdin = stdin # alias
MP4_ITMF_BT_DURATION = 16
# _G_stat64 = stat64 # alias
def va_start(v,l): return __builtin_va_start(v,l) # macro
# __USECONDS_T_TYPE = __U32_TYPE # alias
# def MP4_IS_MPEG4_AAC_AUDIO_TYPE(mpeg4Type): return (((mpeg4Type) >= MP4_MPEG4_AAC_MAIN_AUDIO_TYPE && (mpeg4Type) <= MP4_MPEG4_AAC_HE_AUDIO_TYPE) || (mpeg4Type) == MP4_MPEG4_AAC_SCALABLE_AUDIO_TYPE || (mpeg4Type) == 17) # macro
def __va_copy(d,s): return __builtin_va_copy(d,s) # macro
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
MP4_ITMF_BT_ISRC = 9
__codecvt_noconv = 3
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
# __MODE_T_TYPE = __U32_TYPE # alias
MP4_ITMF_BT_SJIS = 3
def getc(_fp): return _IO_getc (_fp) # macro
__codecvt_error = 2
# _G_MMAP64 = __mmap64 # alias
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
__codecvt_ok = 0
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
# def MP4_IS_CNTL_TRACK_TYPE(type): return (!strcasecmp(type, MP4_CNTL_TRACK_TYPE)) # macro
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp4v2.so'], 'stdout')
stdout = stdout # alias
# __SLONG32_TYPE = int # alias
# __UID_T_TYPE = __U32_TYPE # alias
__codecvt_partial = 1
FILEMODE_READ = 1
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
def MP4_IS_MPEG4_VIDEO_TYPE(type): return ((type) == MP4_MPEG4_VIDEO_TYPE) # macro
def UINT8_C(c): return c # macro
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
# def MP4_IS_AAC_AUDIO_TYPE(type): return (MP4_IS_MPEG2_AAC_AUDIO_TYPE(type) || (type) == MP4_MPEG4_AUDIO_TYPE) # macro
__off_t = c_long
_G_off_t = __off_t # alias
MP4_LOG_VERBOSE1 = 4
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __DEV_T_TYPE = __UQUAD_TYPE # alias
# __DADDR_T_TYPE = __S32_TYPE # alias
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
__ssize_t = c_long
_G_ssize_t = __ssize_t # alias
_IO_ssize_t = _G_ssize_t # alias
class __va_list_tag(Structure):
    pass
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
_IO_va_list = __gnuc_va_list # alias
class _G_fpos_t(Structure):
    pass
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
_IO_pos_t = _G_fpos_t # alias
__off64_t = c_long
_G_off64_t = __off64_t # alias
_IO_off64_t = _G_off64_t # alias
MP4_ART_PNG = 4
class _G_fpos64_t(Structure):
    pass
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
# _IO_iconv_t = _G_iconv_t # alias
MP4_SDT_HAS_REDUNDANT_CODING = 1
def __STRING(x): return #x # macro
_G_va_list = __gnuc_va_list # alias
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MP4_LOG_ERROR = 1
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
_MP4_SDT_RESERVED = 128
MP4_MPEG2_MAIN_VIDEO_TYPE = 97 # Variable c_int '97'
MP4_MPEG2_VIDEO_TYPE = MP4_MPEG2_MAIN_VIDEO_TYPE # alias
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
# __INO64_T_TYPE = __UQUAD_TYPE # alias
def UINTMAX_C(c): return c ## UL # macro
MP4_LOG_VERBOSE4 = 7
# __ID_T_TYPE = __U32_TYPE # alias
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
# __GID_T_TYPE = __U32_TYPE # alias
# __KEY_T_TYPE = __S32_TYPE # alias
__pid_t = c_int
_G_pid_t = __pid_t # alias
# __SWBLK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
# _G_VTABLE_LABEL_PREFIX_ID = __vt_ # alias
FILEMODE_CREATE = 3
MP4_LOG_VERBOSE3 = 6
# __CLOCKID_T_TYPE = __S32_TYPE # alias
# _G_OPEN64 = __open64 # alias
def __glibc_unlikely(cond): return __builtin_expect((cond), 0) # macro
def va_copy(d,s): return __builtin_va_copy(d,s) # macro
MP4_SDT_EARLIER_DISPLAY_TIMES_ALLOWED = 64
MP4_SDT_IS_INDEPENDENT = 32
FILEMODE_UNDEFINED = 0
MP4_SDT_HAS_DEPENDENTS = 4
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
# NULL = __null # alias
MP4_NANOSECONDS_TIME_SCALE = 1000000000 # Variable c_int '1000000000'
MP4_NSECS_TIME_SCALE = MP4_NANOSECONDS_TIME_SCALE # alias
MP4_LOG_VERBOSE2 = 5
_IO_off_t = _G_off_t # alias
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
MP4_ITMF_BT_UNDEFINED = 255
MP4_ITMF_BT_BMP = 27
def va_end(v): return __builtin_va_end(v) # macro
MP4_ITMF_BT_UPC = 25
MP4_ITMF_BT_RIAA_PA = 24
MP4_ITMF_BT_INTEGER = 21
def UINT64_C(c): return c ## UL # macro
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
MP4_ITMF_BT_URL = 15
MP4_ITMF_BT_PNG = 14
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MP4_ITMF_BT_JPEG = 13
MP4_ITMF_BT_GIF = 12
MP4_ITMF_BT_MI3P = 10
MP4_SECONDS_TIME_SCALE = 1 # Variable c_int '1'
MP4_SECS_TIME_SCALE = MP4_SECONDS_TIME_SCALE # alias
def __CONCAT(x,y): return x ## y # macro
MP4_ITMF_BT_UUID = 8
MP4_ITMF_BT_XML = 7
MP4_ITMF_BT_HTML = 6
_IO_fpos_t = _G_fpos_t # alias
MP4_ITMF_BT_UTF8 = 1
MP4_ITMF_BT_IMPLICIT = 0
_G_HAVE_SYS_WAIT = 1 # Variable c_int '1'
_IO_HAVE_SYS_WAIT = _G_HAVE_SYS_WAIT # alias
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
__uid_t = c_uint
_G_uid_t = __uid_t # alias
MP4_ITMF_BT_UTF16 = 2
size_t = c_ulong
_G_size_t = size_t # alias
MP4_MILLISECONDS_TIME_SCALE = 1000 # Variable c_int '1000'
MP4_MSECS_TIME_SCALE = MP4_MILLISECONDS_TIME_SCALE # alias
# _G_LSEEK64 = __lseek64 # alias
MP4_LOG_INFO = 3
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
MP4_SDT_UNKNOWN = 0
MP4_MPEG2_AAC_MAIN_AUDIO_TYPE = 102 # Variable c_int '102'
MP4_MPEG2_AAC_AUDIO_TYPE = MP4_MPEG2_AAC_MAIN_AUDIO_TYPE # alias
_IO_uid_t = _G_uid_t # alias
MP4_MPEG2_AUDIO_TYPE = 105 # Variable c_int '105'
MP4_MP3_AUDIO_TYPE = MP4_MPEG2_AUDIO_TYPE # alias
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
BUFSIZ = _IO_BUFSIZ # alias
# def __LDBL_REDIR(name,proto): return name proto # macro
MP4_LOG_WARNING = 2
MP4_ART_GIF = 2
def __PMT(args): return args # macro
_IO_pid_t = _G_pid_t # alias
MP4ChapterTypeNero = 4
MP4_ART_BMP = 1
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
def va_arg(v,l): return __builtin_va_arg(v,l) # macro
def offsetof(TYPE,MEMBER): return __builtin_offsetof (TYPE, MEMBER) # macro
def INT64_C(c): return c ## L # macro
MP4_SDT_IS_DEPENDENT = 16
def INT8_C(c): return c # macro
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
MP4_SDT_HAS_NO_DEPENDENTS = 8
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
# _G_wint_t = wint_t # alias
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
# _IO_file_flags = _flags # alias
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
_IO_size_t = _G_size_t # alias
def __P(args): return args # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
MP4_SDT_HAS_NO_REDUNDANT_CODING = 2
MP4_MICROSECONDS_TIME_SCALE = 1000000 # Variable c_int '1000000'
MP4_USECS_TIME_SCALE = MP4_MICROSECONDS_TIME_SCALE # alias
def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
MP4ChapterTypeQt = 2
def INT32_C(c): return c # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
MP4_LOG_NONE = 0
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
# _G_wchar_t = wchar_t # alias
# _IO_wint_t = _G_wint_t # alias
MP4_ART_JPEG = 3
def _G_FSTAT64(fd,buf): return __fxstat64 (_STAT_VER, fd, buf) # macro
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
MP4_ART_UNDEFINED = 0
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/lib/libmp4v2.so'], 'stderr')
stderr = stderr # alias
def UINT32_C(c): return c ## U # macro
def UINT16_C(c): return c # macro
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
MP4_ITMF_BT_GENRES = 18
def MP4_IS_VALID_TRACK_ID(x): return ((x) != MP4_INVALID_TRACK_ID) # macro
MP4ChapterTypeAny = 1
def MP4_IS_VALID_TIMESTAMP(x): return ((x) != MP4_INVALID_TIMESTAMP) # macro
MP4_AUDIO_TRACK_TYPE = 'soun' # Variable STRING '(const char*)"soun"'
_IO_IN_BACKUP = 256 # Variable c_int '256'
_G_HAVE_IO_GETLINE_INFO = 1 # Variable c_int '1'
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
MP4V2_PROJECT_repo_root = 'https://mp4v2.googlecode.com/svn' # Variable STRING '(const char*)"https://mp4v2.googlecode.com/svn"'
MP4_MPEG2_HIGH_VIDEO_TYPE = 100 # Variable c_int '100'
_IO_LEFT = 2 # Variable c_int '2'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
MP4V2_PROJECT_version_major = 2 # Variable c_int '2'
MPEG4_ASP_L3 = 243 # Variable c_int '243'
MPEG4_ASP_L2 = 242 # Variable c_int '242'
MPEG4_ASP_L1 = 241 # Variable c_int '241'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
_IONBF = 2 # Variable c_int '2'
MPEG4_ASP_L5 = 245 # Variable c_int '245'
MPEG4_ASP_L4 = 244 # Variable c_int '244'
__USE_XOPEN2K = 1 # Variable c_int '1'
__USE_XOPEN = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
MP4_MPEG4_TTSI_AUDIO_TYPE = 12 # Variable c_int '12'
TRUE = 1 # Variable c_int '1'
MP4V2_PROJECT_irc = 'irc://irc.freenode.net/handbrake' # Variable STRING '(const char*)"irc://irc.freenode.net/handbrake"'
MP4_G723_AUDIO_TYPE = 229 # Variable c_int '229'
_IO_UPPERCASE = 512 # Variable c_int '512'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
MP4_SET_DYNAMIC_PAYLOAD = 255 # Variable c_int '255'
MP4_INVALID_TRACK_ID = 0 # Variable c_uint '0u'
_IO_EOF_SEEN = 16 # Variable c_int '16'
MP4V2_PROJECT_url_discussion = 'http://groups.google.com/group/mp4v2' # Variable STRING '(const char*)"http://groups.google.com/group/mp4v2"'
_IO_LINE_BUF = 512 # Variable c_int '512'
MP4_VORBIS_AUDIO_TYPE = 225 # Variable c_int '225'
MP4V2_PROJECT_repo_rev = 493 # Variable c_int '493'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
MPEG4_FGSP_L5 = 253 # Variable c_int '253'
_G_HAVE_LONG_DOUBLE_IO = 1 # Variable c_int '1'
MP4_MPEG4_WAVETABLE_AUDIO_TYPE = 14 # Variable c_int '14'
MPEG4_ACP_L2 = 194 # Variable c_int '194'
MPEG4_ACP_L1 = 193 # Variable c_int '193'
_IO_RIGHT = 4 # Variable c_int '4'
MPEG4_STP_L1 = 81 # Variable c_int '81'
MP4_OCI_TRACK_TYPE = 'ocsm' # Variable STRING '(const char*)"ocsm"'
_G_config_h = 1 # Variable c_int '1'
_IOS_APPEND = 8 # Variable c_int '8'
MP4V2_CHAPTER_TITLE_MAX = 1023 # Variable c_int '1023'
MP4_JPEG_VIDEO_TYPE = 108 # Variable c_int '108'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
_G_USING_THUNKS = 1 # Variable c_int '1'
MPEG4_ARTSP_L4 = 148 # Variable c_int '148'
__USE_ATFILE = 1 # Variable c_int '1'
MPEG4_FGSP_L2 = 250 # Variable c_int '250'
__GLIBC_HAVE_LONG_LONG = 1 # Variable c_int '1'
TMP_MAX = 238328 # Variable c_int '238328'
MPEG4_CSP_L1 = 161 # Variable c_int '161'
MP4_INVALID_TIMESTAMP = 18446744073709551615 # Variable c_ulong '-1u'
_IO_FIXED = 4096 # Variable c_int '4096'
FOPEN_MAX = 16 # Variable c_int '16'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
MP4_INVALID_EDIT_ID = 0 # Variable c_uint '0u'
_POSIX_SOURCE = 1 # Variable c_int '1'
MP4_MPEG4_AAC_HE_AUDIO_TYPE = 5 # Variable c_int '5'
_ISOC95_SOURCE = 1 # Variable c_int '1'
MPEG4_ASP_L0 = 240 # Variable c_int '240'
MP4_MPEG4_ALS_AUDIO_TYPE = 31 # Variable c_int '31'
__STDC_ISO_10646__ = 201103 # Variable c_long '201103l'
__USE_POSIX = 1 # Variable c_int '1'
MPEG4_ACEP_L3 = 179 # Variable c_int '179'
_IO_NO_WRITES = 8 # Variable c_int '8'
MP4_MPEG2_SNR_VIDEO_TYPE = 98 # Variable c_int '98'
MP4V2_PROJECT_repo_url = 'https://mp4v2.googlecode.com/svn/releases/2.0.0' # Variable STRING '(const char*)"https://mp4v2.googlecode.com/svn/releases/2.0.0"'
MP4_OD_TRACK_TYPE = 'odsm' # Variable STRING '(const char*)"odsm"'
MP4_CLOCK_TRACK_TYPE = 'crsm' # Variable STRING '(const char*)"crsm"'
_G_HAVE_IO_FILE_OPEN = 1 # Variable c_int '1'
MP4V2_PROJECT_version_hex = 131072 # Variable c_int '131072'
MP4V2_PROJECT_repo_uuid = '6e6572fa-98a6-11dd-ad9f-f77439c74b79' # Variable STRING '(const char*)"6e6572fa-98a6-11dd-ad9f-f77439c74b79"'
MP4_PRIVATE_VIDEO_TYPE = 208 # Variable c_int '208'
__FILE_defined = 1 # Variable c_int '1'
MPEG4_AST_L1 = 209 # Variable c_int '209'
MP4_ALAW_AUDIO_TYPE = 227 # Variable c_int '227'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
_IO_USER_BUF = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944 # Variable c_uint '4222418944u'
_G_NAMES_HAVE_UNDERSCORE = 0 # Variable c_int '0'
MP4_CNTL_TRACK_TYPE = 'cntl' # Variable STRING '(const char*)"cntl"'
MP4V2_PROJECT_url_downloads = 'http://code.google.com/p/mp4v2/downloads/list' # Variable STRING '(const char*)"http://code.google.com/p/mp4v2/downloads/list"'
MPEG4_BATP_L1 = 113 # Variable c_int '113'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
MP4_VIDEO_TRACK_TYPE = 'vide' # Variable STRING '(const char*)"vide"'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 16 # Variable c_int '16'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
MP4_MPEG1_AUDIO_TYPE = 107 # Variable c_int '107'
MP4_MPEG1_VIDEO_TYPE = 106 # Variable c_int '106'
__WCHAR_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
MP4_MPEG4_VIDEO_TYPE = 32 # Variable c_int '32'
_IO_SHOWBASE = 128 # Variable c_int '128'
_ISOC99_SOURCE = 1 # Variable c_int '1'
_G_HAVE_MMAP = 1 # Variable c_int '1'
MPEG4_MP_L3 = 51 # Variable c_int '51'
__STDC_NO_THREADS__ = 1 # Variable c_int '1'
MPEG4_MP_L2 = 50 # Variable c_int '50'
MP4_MPEG4_AAC_LC_AUDIO_TYPE = 2 # Variable c_int '2'
MP4_CREATE_64BIT_DATA = 1 # Variable c_int '1'
_SVID_SOURCE = 1 # Variable c_int '1'
MP4_MPEG4_AAC_MAIN_AUDIO_TYPE = 1 # Variable c_int '1'
MP4V2_PROJECT_version_minor = 0 # Variable c_int '0'
MPEG4_SFBAP_L1 = 99 # Variable c_int '99'
MPEG4_MP_L4 = 52 # Variable c_int '52'
__FD_SETSIZE = 1024 # Variable c_int '1024'
MPEG4_SFBAP_L2 = 100 # Variable c_int '100'
MP4_MPEG2_SIMPLE_VIDEO_TYPE = 96 # Variable c_int '96'
MP4_PCM16_LITTLE_ENDIAN_AUDIO_TYPE = 224 # Variable c_int '224'
MP4_MPEG4_LAYER2_AUDIO_TYPE = 33 # Variable c_int '33'
L_cuserid = 9 # Variable c_int '9'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_G_VTABLE_LABEL_HAS_LENGTH = 1 # Variable c_int '1'
_IO_ERR_SEEN = 32 # Variable c_int '32'
MP4_INVALID_DURATION = 18446744073709551615 # Variable c_ulong '-1u'
_IOFBF = 0 # Variable c_int '0'
MP4_CREATE_64BIT_TIME = 2 # Variable c_int '2'
MPEG4_C_STUDIO_P_L3 = 231 # Variable c_int '231'
MP4_PCM16_BIG_ENDIAN_AUDIO_TYPE = 230 # Variable c_int '230'
MPEG4_C_STUDIO_P_L1 = 229 # Variable c_int '229'
_IO_LINKED = 128 # Variable c_int '128'
SEEK_END = 2 # Variable c_int '2'
_G_HAVE_PRINTF_FP = 1 # Variable c_int '1'
MPEG4_SSP_L1 = 17 # Variable c_int '17'
MP4V2_PROJECT_repo_branch = '2.0.0' # Variable STRING '(const char*)"2.0.0"'
MPEG4_SSP_L2 = 18 # Variable c_int '18'
__USE_BSD = 1 # Variable c_int '1'
_IOS_ATEND = 4 # Variable c_int '4'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
MP4_MPEG4_MIDI_AUDIO_TYPE = 15 # Variable c_int '15'
MP4_INVALID_AUDIO_TYPE = 0 # Variable c_int '0'
MPEG4_FGSP_L0 = 248 # Variable c_int '248'
MPEG4_BATP_L2 = 114 # Variable c_int '114'
MPEG4_FGSP_L1 = 249 # Variable c_int '249'
MP4_MPEG4_AAC_SCALABLE_AUDIO_TYPE = 6 # Variable c_int '6'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
_IOS_NOREPLACE = 64 # Variable c_int '64'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
MP4_MPEG4_CELP_AUDIO_TYPE = 8 # Variable c_int '8'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_ISOC11_SOURCE = 1 # Variable c_int '1'
MP4V2_PROJECT_version_point = 0 # Variable c_int '0'
____FILE_defined = 1 # Variable c_int '1'
MP4_MPEG4_AUDIO_TYPE = 64 # Variable c_int '64'
L_tmpnam = 20 # Variable c_int '20'
MP4V2_PROJECT_name_formal = 'MP4v2 2.0.0' # Variable STRING '(const char*)"MP4v2 2.0.0"'
MP4_MPEG4_LAYER3_AUDIO_TYPE = 34 # Variable c_int '34'
_IO_DEC = 16 # Variable c_int '16'
SEEK_CUR = 1 # Variable c_int '1'
MPEG4_ACEP_L4 = 180 # Variable c_int '180'
__USE_SVID = 1 # Variable c_int '1'
MPEG4_ACEP_L2 = 178 # Variable c_int '178'
MPEG4_ACEP_L1 = 177 # Variable c_int '177'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
__USE_ANSI = 1 # Variable c_int '1'
MPEG4_ASP_L3B = 247 # Variable c_int '247'
__USE_MISC = 1 # Variable c_int '1'
__GLIBC__ = 2 # Variable c_int '2'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
__STDC_IEC_559__ = 1 # Variable c_int '1'
MP4_MPEG4_AAC_LTP_AUDIO_TYPE = 4 # Variable c_int '4'
MP4_MPEG4_HVXC_AUDIO_TYPE = 9 # Variable c_int '9'
MP4_TEXT_TRACK_TYPE = 'text' # Variable STRING '(const char*)"text"'
MP4_AC3_AUDIO_TYPE = 226 # Variable c_int '226'
_IO_OCT = 32 # Variable c_int '32'
MPEG4_NBP_L2 = 66 # Variable c_int '66'
_IOS_TRUNC = 16 # Variable c_int '16'
MP4_SUBTITLE_TRACK_TYPE = 'sbtl' # Variable STRING '(const char*)"sbtl"'
__USE_ISOC99 = 1 # Variable c_int '1'
MP4_H263_VIDEO_TYPE = 242 # Variable c_int '242'
_IOS_BIN = 128 # Variable c_int '128'
MPEG4_AST_L3 = 211 # Variable c_int '211'
MPEG4_AST_L2 = 210 # Variable c_int '210'
MPEG4_CP_L1 = 33 # Variable c_int '33'
_STDC_PREDEF_H = 1 # Variable c_int '1'
_STDINT_H = 1 # Variable c_int '1'
MPEG4_C_STUDIO_P_L2 = 230 # Variable c_int '230'
__USE_FORTIFY_LEVEL = 0 # Variable c_int '0'
MPEG4_C_STUDIO_P_L4 = 232 # Variable c_int '232'
MP4V2_PROJECT_repo_type = 'stable' # Variable STRING '(const char*)"stable"'
_IO_SKIPWS = 1 # Variable c_int '1'
MP4V2_PROJECT_url_website = 'http://code.google.com/p/mp4v2' # Variable STRING '(const char*)"http://code.google.com/p/mp4v2"'
MP4V2_PROJECT_name_lower = 'mp4v2' # Variable STRING '(const char*)"mp4v2"'
_IOS_NOCREATE = 32 # Variable c_int '32'
MP4_H261_VIDEO_TYPE = 243 # Variable c_int '243'
FILENAME_MAX = 4096 # Variable c_int '4096'
__STDC_IEC_559_COMPLEX__ = 1 # Variable c_int '1'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
__USE_POSIX199309 = 1 # Variable c_int '1'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
MP4_INVALID_SAMPLE_ID = 0 # Variable c_uint '0u'
MPEG4_ARTSP_L3 = 147 # Variable c_int '147'
MPEG4_ARTSP_L2 = 146 # Variable c_int '146'
MPEG4_ARTSP_L1 = 145 # Variable c_int '145'
__WCHAR_MAX = 2147483647 # Variable c_int '2147483647'
MP4_MPEG4_LAYER1_AUDIO_TYPE = 32 # Variable c_int '32'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
__USE_GNU = 1 # Variable c_int '1'
MP4_MPEG2_SPATIAL_VIDEO_TYPE = 99 # Variable c_int '99'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
_FEATURES_H = 1 # Variable c_int '1'
_IO_HEX = 64 # Variable c_int '64'
MP4_SUBPIC_TRACK_TYPE = 'subp' # Variable STRING '(const char*)"subp"'
MP4V2_PROJECT_build = 'Sun Jul 22 13:03:18 UTC 2012' # Variable STRING '(const char*)"Sun Jul 22 13:03:18 UTC 2012"'
MPEG4_FGSP_L4 = 252 # Variable c_int '252'
MP4V2_PROJECT_version = '2.0.0' # Variable STRING '(const char*)"2.0.0"'
MPEG4_FGSP_L3 = 251 # Variable c_int '251'
SEEK_DATA = 3 # Variable c_int '3'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
MP4V2_PROJECT_bugreport = '<kidjan@gmail.com>' # Variable STRING '(const char*)"<kidjan@gmail.com>"'
_IOS_INPUT = 1 # Variable c_int '1'
__USE_POSIX199506 = 1 # Variable c_int '1'
_IO_UNITBUF = 8192 # Variable c_int '8192'
_BITS_TYPES_H = 1 # Variable c_int '1'
_STDIO_H = 1 # Variable c_int '1'
MPEG4_SP_L3 = 3 # Variable c_int '3'
MPEG4_SP_L2 = 2 # Variable c_int '2'
MPEG4_SP_L1 = 1 # Variable c_int '1'
MPEG4_SP_L0 = 8 # Variable c_int '8'
SEEK_HOLE = 4 # Variable c_int '4'
MP4_MPEGJ_TRACK_TYPE = 'mjsm' # Variable STRING '(const char*)"mjsm"'
MP4_SCENE_TRACK_TYPE = 'sdsm' # Variable STRING '(const char*)"sdsm"'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
MP4V2_PROJECT_name = 'MP4v2' # Variable STRING '(const char*)"MP4v2"'
MP4_MPEG4_MAIN_SYNTHETIC_AUDIO_TYPE = 13 # Variable c_int '13'
MP4_INVALID_VIDEO_TYPE = 0 # Variable c_int '0'
MP4_PRIVATE_AUDIO_TYPE = 192 # Variable c_int '192'
MP4_YUV12_VIDEO_TYPE = 240 # Variable c_int '240'
MP4_CLOSE_DO_NOT_COMPUTE_BITRATE = 1 # Variable c_int '1'
_G_VTABLE_LABEL_PREFIX = '__vt_' # Variable STRING '(const char*)"__vt_"'
MP4_ULAW_AUDIO_TYPE = 228 # Variable c_int '228'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
L_ctermid = 9 # Variable c_int '9'
MP4_HINT_TRACK_TYPE = 'hint' # Variable STRING '(const char*)"hint"'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
_IO_NO_READS = 4 # Variable c_int '4'
_IO_MAGIC_MASK = 4294901760 # Variable c_uint '4294901760u'
_IO_SHOWPOINT = 256 # Variable c_int '256'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
MP4_MPEG7_TRACK_TYPE = 'm7sm' # Variable STRING '(const char*)"m7sm"'
_IO_INTERNAL = 8 # Variable c_int '8'
_IO_UNBUFFERED = 2 # Variable c_int '2'
____mbstate_t_defined = 1 # Variable c_int '1'
_OLD_STDIO_MAGIC = 4206624768 # Variable c_uint '4206624768u'
MP4_MPEG2_AAC_LC_AUDIO_TYPE = 103 # Variable c_int '103'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
MPEG4_SFAP_L2 = 98 # Variable c_int '98'
MPEG4_CP_L2 = 34 # Variable c_int '34'
_XOPEN_SOURCE = 700 # Variable c_int '700'
MPEG4_SFAP_L1 = 97 # Variable c_int '97'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
SEEK_SET = 0 # Variable c_int '0'
MPEG4_S_STUDIO_P_L4 = 228 # Variable c_int '228'
_G_NEED_STDARG_H = 1 # Variable c_int '1'
MP4V2_PROJECT_name_upper = 'MP4V2' # Variable STRING '(const char*)"MP4V2"'
MP4_MPEG4_SLS_AUDIO_TYPE = 35 # Variable c_int '35'
_IOS_OUTPUT = 2 # Variable c_int '2'
__USE_ISOC95 = 1 # Variable c_int '1'
MP4_MPEG4_ALGORITHMIC_FX_AUDIO_TYPE = 16 # Variable c_int '16'
MP4_IPMP_TRACK_TYPE = 'ipsm' # Variable STRING '(const char*)"ipsm"'
FALSE = 0 # Variable c_int '0'
MPEG4_CSP_L3 = 163 # Variable c_int '163'
MPEG4_CSP_L2 = 162 # Variable c_int '162'
EOF = -1 # Variable c_int '-0x00000000000000001'
MP4V2_PROJECT_repo_date = '2012-05-20 15:16:54 -0700 (Sun, 20 May 2012)' # Variable STRING '(const char*)"2012-05-20 15:16:54 -0700 (Sun, 20 May 2012)"'
_BITS_WCHAR_H = 1 # Variable c_int '1'
MP4_MPEG2_442_VIDEO_TYPE = 101 # Variable c_int '101'
MP4_MPEG2_AAC_SSR_AUDIO_TYPE = 104 # Variable c_int '104'
MPEG4_HP_L1 = 129 # Variable c_int '129'
MPEG4_HP_L2 = 130 # Variable c_int '130'
_G_HAVE_ATEXIT = 1 # Variable c_int '1'
_G_HAVE_BOOL = 1 # Variable c_int '1'
__USE_ISOC11 = 1 # Variable c_int '1'
MP4_MPEG4_INVALID_AUDIO_TYPE = 0 # Variable c_int '0'
MPEG4_S_STUDIO_P_L3 = 227 # Variable c_int '227'
MPEG4_S_STUDIO_P_L2 = 226 # Variable c_int '226'
MPEG4_S_STUDIO_P_L1 = 225 # Variable c_int '225'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
_BSD_SOURCE = 1 # Variable c_int '1'
MP4_MPEG4_AAC_SSR_AUDIO_TYPE = 3 # Variable c_int '3'
_IOLBF = 1 # Variable c_int '1'
_G_int16_t = c_short
_G_int32_t = c_int
_G_uint16_t = c_ushort
_G_uint32_t = c_uint
vprintf = _libraries['/usr/lib/libmp4v2.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
getchar = _libraries['/usr/lib/libmp4v2.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
FILE = _IO_FILE
fgetc_unlocked = _libraries['/usr/lib/libmp4v2.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/lib/libmp4v2.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/lib/libmp4v2.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/lib/libmp4v2.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/lib/libmp4v2.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/lib/libmp4v2.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/lib/libmp4v2.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/lib/libmp4v2.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/lib/libmp4v2.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/lib/libmp4v2.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmp4v2.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmp4v2.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/lib/libmp4v2.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/lib/libmp4v2.so'], '_sys_errlist')
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
__swblk_t = c_long
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
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp4v2.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp4v2.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/lib/libmp4v2.so'], '_IO_2_1_stderr_')
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
__underflow = _libraries['/usr/lib/libmp4v2.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/lib/libmp4v2.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/lib/libmp4v2.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/lib/libmp4v2.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/lib/libmp4v2.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/lib/libmp4v2.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/lib/libmp4v2.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/lib/libmp4v2.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/lib/libmp4v2.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/lib/libmp4v2.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/lib/libmp4v2.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/lib/libmp4v2.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag), POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/lib/libmp4v2.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag)]
_IO_padn = _libraries['/usr/lib/libmp4v2.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/lib/libmp4v2.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/lib/libmp4v2.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/lib/libmp4v2.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/lib/libmp4v2.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
class MP4Chapter_s(Structure):
    pass
uint64_t = c_uint64
MP4Duration = uint64_t
MP4Chapter_s._fields_ = [
    ('duration', MP4Duration),
    ('title', c_char * 1024),
]
MP4Chapter_t = MP4Chapter_s

# values for enumeration 'MP4ChapterType'
MP4ChapterType = c_int # enum
MP4FileHandle = c_void_p
uint32_t = c_uint32
MP4TrackId = uint32_t
MP4AddChapter = _libraries['/usr/lib/libmp4v2.so'].MP4AddChapter
MP4AddChapter.restype = None
MP4AddChapter.argtypes = [MP4FileHandle, MP4TrackId, MP4Duration, STRING]
MP4AddChapterTextTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddChapterTextTrack
MP4AddChapterTextTrack.restype = MP4TrackId
MP4AddChapterTextTrack.argtypes = [MP4FileHandle, MP4TrackId, uint32_t]
MP4Timestamp = uint64_t
MP4AddNeroChapter = _libraries['/usr/lib/libmp4v2.so'].MP4AddNeroChapter
MP4AddNeroChapter.restype = None
MP4AddNeroChapter.argtypes = [MP4FileHandle, MP4Timestamp, STRING]
MP4ConvertChapters = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertChapters
MP4ConvertChapters.restype = MP4ChapterType
MP4ConvertChapters.argtypes = [MP4FileHandle, MP4ChapterType]
MP4DeleteChapters = _libraries['/usr/lib/libmp4v2.so'].MP4DeleteChapters
MP4DeleteChapters.restype = MP4ChapterType
MP4DeleteChapters.argtypes = [MP4FileHandle, MP4ChapterType, MP4TrackId]
MP4GetChapters = _libraries['/usr/lib/libmp4v2.so'].MP4GetChapters
MP4GetChapters.restype = MP4ChapterType
MP4GetChapters.argtypes = [MP4FileHandle, POINTER(POINTER(MP4Chapter_t)), POINTER(uint32_t), MP4ChapterType]
MP4SetChapters = _libraries['/usr/lib/libmp4v2.so'].MP4SetChapters
MP4SetChapters.restype = MP4ChapterType
MP4SetChapters.argtypes = [MP4FileHandle, POINTER(MP4Chapter_t), uint32_t, MP4ChapterType]

# values for enumeration 'MP4FileMode_e'
MP4FileMode_e = c_int # enum
MP4FileMode = MP4FileMode_e
class MP4FileProvider_s(Structure):
    pass
int64_t = c_int64
MP4FileProvider_s._fields_ = [
    ('open', CFUNCTYPE(c_void_p, STRING, MP4FileMode)),
    ('seek', CFUNCTYPE(c_int, c_void_p, int64_t)),
    ('read', CFUNCTYPE(c_int, c_void_p, c_void_p, int64_t, POINTER(int64_t), int64_t)),
    ('write', CFUNCTYPE(c_int, c_void_p, c_void_p, int64_t, POINTER(int64_t), int64_t)),
    ('close', CFUNCTYPE(c_int, c_void_p)),
]
MP4FileProvider = MP4FileProvider_s
MP4Close = _libraries['/usr/lib/libmp4v2.so'].MP4Close
MP4Close.restype = None
MP4Close.argtypes = [MP4FileHandle, uint32_t]
MP4Create = _libraries['/usr/lib/libmp4v2.so'].MP4Create
MP4Create.restype = MP4FileHandle
MP4Create.argtypes = [STRING, uint32_t]
MP4CreateEx = _libraries['/usr/lib/libmp4v2.so'].MP4CreateEx
MP4CreateEx.restype = MP4FileHandle
MP4CreateEx.argtypes = [STRING, uint32_t, c_int, c_int, STRING, uint32_t, POINTER(STRING), uint32_t]
MP4Dump = _libraries['/usr/lib/libmp4v2.so'].MP4Dump
MP4Dump.restype = c_bool
MP4Dump.argtypes = [MP4FileHandle, c_bool]
MP4FileInfo = _libraries['/usr/lib/libmp4v2.so'].MP4FileInfo
MP4FileInfo.restype = STRING
MP4FileInfo.argtypes = [STRING, MP4TrackId]
MP4GetFilename = _libraries['/usr/lib/libmp4v2.so'].MP4GetFilename
MP4GetFilename.restype = STRING
MP4GetFilename.argtypes = [MP4FileHandle]
MP4Info = _libraries['/usr/lib/libmp4v2.so'].MP4Info
MP4Info.restype = STRING
MP4Info.argtypes = [MP4FileHandle, MP4TrackId]
MP4Modify = _libraries['/usr/lib/libmp4v2.so'].MP4Modify
MP4Modify.restype = MP4FileHandle
MP4Modify.argtypes = [STRING, uint32_t]
MP4Optimize = _libraries['/usr/lib/libmp4v2.so'].MP4Optimize
MP4Optimize.restype = c_bool
MP4Optimize.argtypes = [STRING, STRING]
MP4Read = _libraries['/usr/lib/libmp4v2.so'].MP4Read
MP4Read.restype = MP4FileHandle
MP4Read.argtypes = [STRING]
MP4ReadProvider = _libraries['/usr/lib/libmp4v2.so'].MP4ReadProvider
MP4ReadProvider.restype = MP4FileHandle
MP4ReadProvider.argtypes = [STRING, POINTER(MP4FileProvider)]
MP4HaveAtom = _libraries['/usr/lib/libmp4v2.so'].MP4HaveAtom
MP4HaveAtom.restype = c_bool
MP4HaveAtom.argtypes = [MP4FileHandle, STRING]
MP4GetIntegerProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetIntegerProperty
MP4GetIntegerProperty.restype = c_bool
MP4GetIntegerProperty.argtypes = [MP4FileHandle, STRING, POINTER(uint64_t)]
MP4GetFloatProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetFloatProperty
MP4GetFloatProperty.restype = c_bool
MP4GetFloatProperty.argtypes = [MP4FileHandle, STRING, POINTER(c_float)]
MP4GetStringProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetStringProperty
MP4GetStringProperty.restype = c_bool
MP4GetStringProperty.argtypes = [MP4FileHandle, STRING, POINTER(STRING)]
uint8_t = c_uint8
MP4GetBytesProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetBytesProperty
MP4GetBytesProperty.restype = c_bool
MP4GetBytesProperty.argtypes = [MP4FileHandle, STRING, POINTER(POINTER(uint8_t)), POINTER(uint32_t)]
MP4SetIntegerProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetIntegerProperty
MP4SetIntegerProperty.restype = c_bool
MP4SetIntegerProperty.argtypes = [MP4FileHandle, STRING, int64_t]
MP4SetFloatProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetFloatProperty
MP4SetFloatProperty.restype = c_bool
MP4SetFloatProperty.argtypes = [MP4FileHandle, STRING, c_float]
MP4SetStringProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetStringProperty
MP4SetStringProperty.restype = c_bool
MP4SetStringProperty.argtypes = [MP4FileHandle, STRING, STRING]
MP4SetBytesProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetBytesProperty
MP4SetBytesProperty.restype = c_bool
MP4SetBytesProperty.argtypes = [MP4FileHandle, STRING, POINTER(uint8_t), uint32_t]
MP4GetDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetDuration
MP4GetDuration.restype = MP4Duration
MP4GetDuration.argtypes = [MP4FileHandle]
MP4GetTimeScale = _libraries['/usr/lib/libmp4v2.so'].MP4GetTimeScale
MP4GetTimeScale.restype = uint32_t
MP4GetTimeScale.argtypes = [MP4FileHandle]
MP4SetTimeScale = _libraries['/usr/lib/libmp4v2.so'].MP4SetTimeScale
MP4SetTimeScale.restype = c_bool
MP4SetTimeScale.argtypes = [MP4FileHandle, uint32_t]
MP4ChangeMovieTimeScale = _libraries['/usr/lib/libmp4v2.so'].MP4ChangeMovieTimeScale
MP4ChangeMovieTimeScale.restype = None
MP4ChangeMovieTimeScale.argtypes = [MP4FileHandle, uint32_t]
MP4GetODProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetODProfileLevel
MP4GetODProfileLevel.restype = uint8_t
MP4GetODProfileLevel.argtypes = [MP4FileHandle]
MP4SetODProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4SetODProfileLevel
MP4SetODProfileLevel.restype = c_bool
MP4SetODProfileLevel.argtypes = [MP4FileHandle, uint8_t]
MP4GetSceneProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetSceneProfileLevel
MP4GetSceneProfileLevel.restype = uint8_t
MP4GetSceneProfileLevel.argtypes = [MP4FileHandle]
MP4SetSceneProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4SetSceneProfileLevel
MP4SetSceneProfileLevel.restype = c_bool
MP4SetSceneProfileLevel.argtypes = [MP4FileHandle, uint8_t]
MP4GetVideoProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetVideoProfileLevel
MP4GetVideoProfileLevel.restype = uint8_t
MP4GetVideoProfileLevel.argtypes = [MP4FileHandle, MP4TrackId]
MP4SetVideoProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4SetVideoProfileLevel
MP4SetVideoProfileLevel.restype = None
MP4SetVideoProfileLevel.argtypes = [MP4FileHandle, uint8_t]
MP4GetAudioProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetAudioProfileLevel
MP4GetAudioProfileLevel.restype = uint8_t
MP4GetAudioProfileLevel.argtypes = [MP4FileHandle]
MP4SetAudioProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4SetAudioProfileLevel
MP4SetAudioProfileLevel.restype = None
MP4SetAudioProfileLevel.argtypes = [MP4FileHandle, uint8_t]
MP4GetGraphicsProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetGraphicsProfileLevel
MP4GetGraphicsProfileLevel.restype = uint8_t
MP4GetGraphicsProfileLevel.argtypes = [MP4FileHandle]
MP4SetGraphicsProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4SetGraphicsProfileLevel
MP4SetGraphicsProfileLevel.restype = c_bool
MP4SetGraphicsProfileLevel.argtypes = [MP4FileHandle, uint8_t]
MP4SampleId = uint32_t
MP4EditId = uint32_t

# values for enumeration 'MP4LogLevel'
MP4LogLevel = c_int # enum
MP4LogCallback = CFUNCTYPE(None, MP4LogLevel, STRING, POINTER(__va_list_tag))
encryptFunc_t = CFUNCTYPE(uint32_t, uint32_t, uint32_t, POINTER(uint8_t), POINTER(uint32_t), POINTER(POINTER(uint8_t)))
MP4Make3GPCompliant = _libraries['/usr/lib/libmp4v2.so'].MP4Make3GPCompliant
MP4Make3GPCompliant.restype = c_bool
MP4Make3GPCompliant.argtypes = [STRING, STRING, uint32_t, POINTER(STRING), uint32_t, c_bool]
MP4AddTrackEdit = _libraries['/usr/lib/libmp4v2.so'].MP4AddTrackEdit
MP4AddTrackEdit.restype = MP4EditId
MP4AddTrackEdit.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId, MP4Timestamp, MP4Duration, c_bool]
MP4DeleteTrackEdit = _libraries['/usr/lib/libmp4v2.so'].MP4DeleteTrackEdit
MP4DeleteTrackEdit.restype = c_bool
MP4DeleteTrackEdit.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId]
MP4GetTrackNumberOfEdits = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackNumberOfEdits
MP4GetTrackNumberOfEdits.restype = uint32_t
MP4GetTrackNumberOfEdits.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackEditTotalDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackEditTotalDuration
MP4GetTrackEditTotalDuration.restype = MP4Duration
MP4GetTrackEditTotalDuration.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId]
MP4GetTrackEditMediaStart = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackEditMediaStart
MP4GetTrackEditMediaStart.restype = MP4Timestamp
MP4GetTrackEditMediaStart.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId]
MP4SetTrackEditMediaStart = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackEditMediaStart
MP4SetTrackEditMediaStart.restype = c_bool
MP4SetTrackEditMediaStart.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId, MP4Timestamp]
MP4GetTrackEditDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackEditDuration
MP4GetTrackEditDuration.restype = MP4Duration
MP4GetTrackEditDuration.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId]
MP4SetTrackEditDuration = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackEditDuration
MP4SetTrackEditDuration.restype = c_bool
MP4SetTrackEditDuration.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId, MP4Duration]
int8_t = c_int8
MP4GetTrackEditDwell = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackEditDwell
MP4GetTrackEditDwell.restype = int8_t
MP4GetTrackEditDwell.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId]
MP4SetTrackEditDwell = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackEditDwell
MP4SetTrackEditDwell.restype = c_bool
MP4SetTrackEditDwell.argtypes = [MP4FileHandle, MP4TrackId, MP4EditId, c_bool]
MP4ReadSampleFromEditTime = _libraries['/usr/lib/libmp4v2.so'].MP4ReadSampleFromEditTime
MP4ReadSampleFromEditTime.restype = c_bool
MP4ReadSampleFromEditTime.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp, POINTER(POINTER(uint8_t)), POINTER(uint32_t), POINTER(MP4Timestamp), POINTER(MP4Duration), POINTER(MP4Duration), POINTER(c_bool)]
MP4GetSampleIdFromEditTime = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleIdFromEditTime
MP4GetSampleIdFromEditTime.restype = MP4SampleId
MP4GetSampleIdFromEditTime.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp, POINTER(MP4Timestamp), POINTER(MP4Duration)]
MP4ConvertFromMovieDuration = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertFromMovieDuration
MP4ConvertFromMovieDuration.restype = uint64_t
MP4ConvertFromMovieDuration.argtypes = [MP4FileHandle, MP4Duration, uint32_t]
MP4ConvertFromTrackTimestamp = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertFromTrackTimestamp
MP4ConvertFromTrackTimestamp.restype = uint64_t
MP4ConvertFromTrackTimestamp.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp, uint32_t]
MP4ConvertToTrackTimestamp = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertToTrackTimestamp
MP4ConvertToTrackTimestamp.restype = MP4Timestamp
MP4ConvertToTrackTimestamp.argtypes = [MP4FileHandle, MP4TrackId, uint64_t, uint32_t]
MP4ConvertFromTrackDuration = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertFromTrackDuration
MP4ConvertFromTrackDuration.restype = uint64_t
MP4ConvertFromTrackDuration.argtypes = [MP4FileHandle, MP4TrackId, MP4Duration, uint32_t]
MP4ConvertToTrackDuration = _libraries['/usr/lib/libmp4v2.so'].MP4ConvertToTrackDuration
MP4ConvertToTrackDuration.restype = MP4Duration
MP4ConvertToTrackDuration.argtypes = [MP4FileHandle, MP4TrackId, uint64_t, uint32_t]
MP4BinaryToBase16 = _libraries['/usr/lib/libmp4v2.so'].MP4BinaryToBase16
MP4BinaryToBase16.restype = STRING
MP4BinaryToBase16.argtypes = [POINTER(uint8_t), uint32_t]
MP4BinaryToBase64 = _libraries['/usr/lib/libmp4v2.so'].MP4BinaryToBase64
MP4BinaryToBase64.restype = STRING
MP4BinaryToBase64.argtypes = [POINTER(uint8_t), uint32_t]
MP4Free = _libraries['/usr/lib/libmp4v2.so'].MP4Free
MP4Free.restype = None
MP4Free.argtypes = [c_void_p]
MP4SetLogCallback = _libraries['/usr/lib/libmp4v2.so'].MP4SetLogCallback
MP4SetLogCallback.restype = None
MP4SetLogCallback.argtypes = [MP4LogCallback]
MP4LogGetLevel = _libraries['/usr/lib/libmp4v2.so'].MP4LogGetLevel
MP4LogGetLevel.restype = MP4LogLevel
MP4LogGetLevel.argtypes = []
MP4LogSetLevel = _libraries['/usr/lib/libmp4v2.so'].MP4LogSetLevel
MP4LogSetLevel.restype = None
MP4LogSetLevel.argtypes = [MP4LogLevel]
class mp4v2_ismacryp_session_params(Structure):
    pass
uint16_t = c_uint16
mp4v2_ismacryp_session_params._fields_ = [
    ('scheme_type', uint32_t),
    ('scheme_version', uint16_t),
    ('key_ind_len', uint8_t),
    ('iv_len', uint8_t),
    ('selective_enc', uint8_t),
    ('kms_uri', STRING),
]
mp4v2_ismacrypParams = mp4v2_ismacryp_session_params
MP4DefaultISMACrypParams = _libraries['/usr/lib/libmp4v2.so'].MP4DefaultISMACrypParams
MP4DefaultISMACrypParams.restype = POINTER(mp4v2_ismacrypParams)
MP4DefaultISMACrypParams.argtypes = [POINTER(mp4v2_ismacrypParams)]
MP4AddEncAudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddEncAudioTrack
MP4AddEncAudioTrack.restype = MP4TrackId
MP4AddEncAudioTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, POINTER(mp4v2_ismacrypParams), uint8_t]
MP4AddEncVideoTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddEncVideoTrack
MP4AddEncVideoTrack.restype = MP4TrackId
MP4AddEncVideoTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint16_t, uint16_t, POINTER(mp4v2_ismacrypParams), uint8_t, STRING]
MP4AddEncH264VideoTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddEncH264VideoTrack
MP4AddEncH264VideoTrack.restype = MP4TrackId
MP4AddEncH264VideoTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint16_t, uint16_t, MP4FileHandle, MP4TrackId, POINTER(mp4v2_ismacrypParams)]
MP4EncAndCloneTrack = _libraries['/usr/lib/libmp4v2.so'].MP4EncAndCloneTrack
MP4EncAndCloneTrack.restype = MP4TrackId
MP4EncAndCloneTrack.argtypes = [MP4FileHandle, MP4TrackId, POINTER(mp4v2_ismacrypParams), MP4FileHandle, MP4TrackId]
MP4EncAndCopyTrack = _libraries['/usr/lib/libmp4v2.so'].MP4EncAndCopyTrack
MP4EncAndCopyTrack.restype = MP4TrackId
MP4EncAndCopyTrack.argtypes = [MP4FileHandle, MP4TrackId, POINTER(mp4v2_ismacrypParams), encryptFunc_t, uint32_t, MP4FileHandle, c_bool, MP4TrackId]
MP4MakeIsmaCompliant = _libraries['/usr/lib/libmp4v2.so'].MP4MakeIsmaCompliant
MP4MakeIsmaCompliant.restype = c_bool
MP4MakeIsmaCompliant.argtypes = [STRING, c_bool]
MP4MakeIsmaSdpIod = _libraries['/usr/lib/libmp4v2.so'].MP4MakeIsmaSdpIod
MP4MakeIsmaSdpIod.restype = STRING
MP4MakeIsmaSdpIod.argtypes = [uint8_t, uint32_t, POINTER(uint8_t), uint32_t, uint8_t, uint32_t, POINTER(uint8_t), uint32_t]

# values for enumeration 'MP4ItmfBasicType_e'
MP4ItmfBasicType_e = c_int # enum
MP4ItmfBasicType = MP4ItmfBasicType_e
class MP4ItmfData_s(Structure):
    pass
MP4ItmfData_s._fields_ = [
    ('typeSetIdentifier', uint8_t),
    ('typeCode', MP4ItmfBasicType),
    ('locale', uint32_t),
    ('value', POINTER(uint8_t)),
    ('valueSize', uint32_t),
]
MP4ItmfData = MP4ItmfData_s
class MP4ItmfDataList_s(Structure):
    pass
MP4ItmfDataList_s._fields_ = [
    ('elements', POINTER(MP4ItmfData)),
    ('size', uint32_t),
]
MP4ItmfDataList = MP4ItmfDataList_s
class MP4ItmfItem_s(Structure):
    pass
MP4ItmfItem_s._fields_ = [
    ('__handle', c_void_p),
    ('code', STRING),
    ('mean', STRING),
    ('name', STRING),
    ('dataList', MP4ItmfDataList),
]
MP4ItmfItem = MP4ItmfItem_s
class MP4ItmfItemList_s(Structure):
    pass
MP4ItmfItemList_s._fields_ = [
    ('elements', POINTER(MP4ItmfItem)),
    ('size', uint32_t),
]
MP4ItmfItemList = MP4ItmfItemList_s
MP4ItmfItemAlloc = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfItemAlloc
MP4ItmfItemAlloc.restype = POINTER(MP4ItmfItem)
MP4ItmfItemAlloc.argtypes = [STRING, uint32_t]
MP4ItmfItemFree = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfItemFree
MP4ItmfItemFree.restype = None
MP4ItmfItemFree.argtypes = [POINTER(MP4ItmfItem)]
MP4ItmfItemListFree = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfItemListFree
MP4ItmfItemListFree.restype = None
MP4ItmfItemListFree.argtypes = [POINTER(MP4ItmfItemList)]
MP4ItmfGetItems = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfGetItems
MP4ItmfGetItems.restype = POINTER(MP4ItmfItemList)
MP4ItmfGetItems.argtypes = [MP4FileHandle]
MP4ItmfGetItemsByCode = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfGetItemsByCode
MP4ItmfGetItemsByCode.restype = POINTER(MP4ItmfItemList)
MP4ItmfGetItemsByCode.argtypes = [MP4FileHandle, STRING]
MP4ItmfGetItemsByMeaning = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfGetItemsByMeaning
MP4ItmfGetItemsByMeaning.restype = POINTER(MP4ItmfItemList)
MP4ItmfGetItemsByMeaning.argtypes = [MP4FileHandle, STRING, STRING]
MP4ItmfAddItem = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfAddItem
MP4ItmfAddItem.restype = c_bool
MP4ItmfAddItem.argtypes = [MP4FileHandle, POINTER(MP4ItmfItem)]
MP4ItmfSetItem = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfSetItem
MP4ItmfSetItem.restype = c_bool
MP4ItmfSetItem.argtypes = [MP4FileHandle, POINTER(MP4ItmfItem)]
MP4ItmfRemoveItem = _libraries['/usr/lib/libmp4v2.so'].MP4ItmfRemoveItem
MP4ItmfRemoveItem.restype = c_bool
MP4ItmfRemoveItem.argtypes = [MP4FileHandle, POINTER(MP4ItmfItem)]

# values for enumeration 'MP4TagArtworkType_e'
MP4TagArtworkType_e = c_int # enum
MP4TagArtworkType = MP4TagArtworkType_e
class MP4TagArtwork_s(Structure):
    pass
MP4TagArtwork_s._fields_ = [
    ('data', c_void_p),
    ('size', uint32_t),
    ('type', MP4TagArtworkType),
]
MP4TagArtwork = MP4TagArtwork_s
class MP4TagTrack_s(Structure):
    pass
MP4TagTrack_s._fields_ = [
    ('index', uint16_t),
    ('total', uint16_t),
]
MP4TagTrack = MP4TagTrack_s
class MP4TagDisk_s(Structure):
    pass
MP4TagDisk_s._fields_ = [
    ('index', uint16_t),
    ('total', uint16_t),
]
MP4TagDisk = MP4TagDisk_s
class MP4Tags_s(Structure):
    pass
MP4Tags_s._fields_ = [
    ('__handle', c_void_p),
    ('name', STRING),
    ('artist', STRING),
    ('albumArtist', STRING),
    ('album', STRING),
    ('grouping', STRING),
    ('composer', STRING),
    ('comments', STRING),
    ('genre', STRING),
    ('genreType', POINTER(uint16_t)),
    ('releaseDate', STRING),
    ('track', POINTER(MP4TagTrack)),
    ('disk', POINTER(MP4TagDisk)),
    ('tempo', POINTER(uint16_t)),
    ('compilation', POINTER(uint8_t)),
    ('tvShow', STRING),
    ('tvNetwork', STRING),
    ('tvEpisodeID', STRING),
    ('tvSeason', POINTER(uint32_t)),
    ('tvEpisode', POINTER(uint32_t)),
    ('description', STRING),
    ('longDescription', STRING),
    ('lyrics', STRING),
    ('sortName', STRING),
    ('sortArtist', STRING),
    ('sortAlbumArtist', STRING),
    ('sortAlbum', STRING),
    ('sortComposer', STRING),
    ('sortTVShow', STRING),
    ('artwork', POINTER(MP4TagArtwork)),
    ('artworkCount', uint32_t),
    ('copyright', STRING),
    ('encodingTool', STRING),
    ('encodedBy', STRING),
    ('purchaseDate', STRING),
    ('podcast', POINTER(uint8_t)),
    ('keywords', STRING),
    ('category', STRING),
    ('hdVideo', POINTER(uint8_t)),
    ('mediaType', POINTER(uint8_t)),
    ('contentRating', POINTER(uint8_t)),
    ('gapless', POINTER(uint8_t)),
    ('iTunesAccount', STRING),
    ('iTunesAccountType', POINTER(uint8_t)),
    ('iTunesCountry', POINTER(uint32_t)),
    ('contentID', POINTER(uint32_t)),
    ('artistID', POINTER(uint32_t)),
    ('playlistID', POINTER(uint64_t)),
    ('genreID', POINTER(uint32_t)),
    ('composerID', POINTER(uint32_t)),
    ('xid', STRING),
]
MP4Tags = MP4Tags_s
MP4TagsAlloc = _libraries['/usr/lib/libmp4v2.so'].MP4TagsAlloc
MP4TagsAlloc.restype = POINTER(MP4Tags)
MP4TagsAlloc.argtypes = []
MP4TagsFetch = _libraries['/usr/lib/libmp4v2.so'].MP4TagsFetch
MP4TagsFetch.restype = c_bool
MP4TagsFetch.argtypes = [POINTER(MP4Tags), MP4FileHandle]
MP4TagsStore = _libraries['/usr/lib/libmp4v2.so'].MP4TagsStore
MP4TagsStore.restype = c_bool
MP4TagsStore.argtypes = [POINTER(MP4Tags), MP4FileHandle]
MP4TagsFree = _libraries['/usr/lib/libmp4v2.so'].MP4TagsFree
MP4TagsFree.restype = None
MP4TagsFree.argtypes = [POINTER(MP4Tags)]
MP4TagsHasMetadata = _libraries['/usr/lib/libmp4v2.so'].MP4TagsHasMetadata
MP4TagsHasMetadata.restype = c_bool
MP4TagsHasMetadata.argtypes = [POINTER(MP4Tags), POINTER(c_bool)]
MP4TagsSetName = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetName
MP4TagsSetName.restype = c_bool
MP4TagsSetName.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetArtist = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetArtist
MP4TagsSetArtist.restype = c_bool
MP4TagsSetArtist.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetAlbumArtist = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetAlbumArtist
MP4TagsSetAlbumArtist.restype = c_bool
MP4TagsSetAlbumArtist.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetAlbum = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetAlbum
MP4TagsSetAlbum.restype = c_bool
MP4TagsSetAlbum.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetGrouping = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetGrouping
MP4TagsSetGrouping.restype = c_bool
MP4TagsSetGrouping.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetComposer = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetComposer
MP4TagsSetComposer.restype = c_bool
MP4TagsSetComposer.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetComments = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetComments
MP4TagsSetComments.restype = c_bool
MP4TagsSetComments.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetGenre = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetGenre
MP4TagsSetGenre.restype = c_bool
MP4TagsSetGenre.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetGenreType = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetGenreType
MP4TagsSetGenreType.restype = c_bool
MP4TagsSetGenreType.argtypes = [POINTER(MP4Tags), POINTER(uint16_t)]
MP4TagsSetReleaseDate = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetReleaseDate
MP4TagsSetReleaseDate.restype = c_bool
MP4TagsSetReleaseDate.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetTrack = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTrack
MP4TagsSetTrack.restype = c_bool
MP4TagsSetTrack.argtypes = [POINTER(MP4Tags), POINTER(MP4TagTrack)]
MP4TagsSetDisk = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetDisk
MP4TagsSetDisk.restype = c_bool
MP4TagsSetDisk.argtypes = [POINTER(MP4Tags), POINTER(MP4TagDisk)]
MP4TagsSetTempo = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTempo
MP4TagsSetTempo.restype = c_bool
MP4TagsSetTempo.argtypes = [POINTER(MP4Tags), POINTER(uint16_t)]
MP4TagsSetCompilation = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetCompilation
MP4TagsSetCompilation.restype = c_bool
MP4TagsSetCompilation.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetTVShow = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTVShow
MP4TagsSetTVShow.restype = c_bool
MP4TagsSetTVShow.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetTVNetwork = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTVNetwork
MP4TagsSetTVNetwork.restype = c_bool
MP4TagsSetTVNetwork.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetTVEpisodeID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTVEpisodeID
MP4TagsSetTVEpisodeID.restype = c_bool
MP4TagsSetTVEpisodeID.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetTVSeason = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTVSeason
MP4TagsSetTVSeason.restype = c_bool
MP4TagsSetTVSeason.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetTVEpisode = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetTVEpisode
MP4TagsSetTVEpisode.restype = c_bool
MP4TagsSetTVEpisode.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetDescription = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetDescription
MP4TagsSetDescription.restype = c_bool
MP4TagsSetDescription.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetLongDescription = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetLongDescription
MP4TagsSetLongDescription.restype = c_bool
MP4TagsSetLongDescription.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetLyrics = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetLyrics
MP4TagsSetLyrics.restype = c_bool
MP4TagsSetLyrics.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortName = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortName
MP4TagsSetSortName.restype = c_bool
MP4TagsSetSortName.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortArtist = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortArtist
MP4TagsSetSortArtist.restype = c_bool
MP4TagsSetSortArtist.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortAlbumArtist = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortAlbumArtist
MP4TagsSetSortAlbumArtist.restype = c_bool
MP4TagsSetSortAlbumArtist.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortAlbum = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortAlbum
MP4TagsSetSortAlbum.restype = c_bool
MP4TagsSetSortAlbum.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortComposer = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortComposer
MP4TagsSetSortComposer.restype = c_bool
MP4TagsSetSortComposer.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetSortTVShow = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetSortTVShow
MP4TagsSetSortTVShow.restype = c_bool
MP4TagsSetSortTVShow.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsAddArtwork = _libraries['/usr/lib/libmp4v2.so'].MP4TagsAddArtwork
MP4TagsAddArtwork.restype = c_bool
MP4TagsAddArtwork.argtypes = [POINTER(MP4Tags), POINTER(MP4TagArtwork)]
MP4TagsSetArtwork = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetArtwork
MP4TagsSetArtwork.restype = c_bool
MP4TagsSetArtwork.argtypes = [POINTER(MP4Tags), uint32_t, POINTER(MP4TagArtwork)]
MP4TagsRemoveArtwork = _libraries['/usr/lib/libmp4v2.so'].MP4TagsRemoveArtwork
MP4TagsRemoveArtwork.restype = c_bool
MP4TagsRemoveArtwork.argtypes = [POINTER(MP4Tags), uint32_t]
MP4TagsSetCopyright = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetCopyright
MP4TagsSetCopyright.restype = c_bool
MP4TagsSetCopyright.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetEncodingTool = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetEncodingTool
MP4TagsSetEncodingTool.restype = c_bool
MP4TagsSetEncodingTool.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetEncodedBy = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetEncodedBy
MP4TagsSetEncodedBy.restype = c_bool
MP4TagsSetEncodedBy.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetPurchaseDate = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetPurchaseDate
MP4TagsSetPurchaseDate.restype = c_bool
MP4TagsSetPurchaseDate.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetPodcast = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetPodcast
MP4TagsSetPodcast.restype = c_bool
MP4TagsSetPodcast.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetKeywords = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetKeywords
MP4TagsSetKeywords.restype = c_bool
MP4TagsSetKeywords.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetCategory = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetCategory
MP4TagsSetCategory.restype = c_bool
MP4TagsSetCategory.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetHDVideo = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetHDVideo
MP4TagsSetHDVideo.restype = c_bool
MP4TagsSetHDVideo.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetMediaType = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetMediaType
MP4TagsSetMediaType.restype = c_bool
MP4TagsSetMediaType.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetContentRating = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetContentRating
MP4TagsSetContentRating.restype = c_bool
MP4TagsSetContentRating.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetGapless = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetGapless
MP4TagsSetGapless.restype = c_bool
MP4TagsSetGapless.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetITunesAccount = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetITunesAccount
MP4TagsSetITunesAccount.restype = c_bool
MP4TagsSetITunesAccount.argtypes = [POINTER(MP4Tags), STRING]
MP4TagsSetITunesAccountType = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetITunesAccountType
MP4TagsSetITunesAccountType.restype = c_bool
MP4TagsSetITunesAccountType.argtypes = [POINTER(MP4Tags), POINTER(uint8_t)]
MP4TagsSetITunesCountry = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetITunesCountry
MP4TagsSetITunesCountry.restype = c_bool
MP4TagsSetITunesCountry.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetContentID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetContentID
MP4TagsSetContentID.restype = c_bool
MP4TagsSetContentID.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetArtistID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetArtistID
MP4TagsSetArtistID.restype = c_bool
MP4TagsSetArtistID.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetPlaylistID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetPlaylistID
MP4TagsSetPlaylistID.restype = c_bool
MP4TagsSetPlaylistID.argtypes = [POINTER(MP4Tags), POINTER(uint64_t)]
MP4TagsSetGenreID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetGenreID
MP4TagsSetGenreID.restype = c_bool
MP4TagsSetGenreID.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetComposerID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetComposerID
MP4TagsSetComposerID.restype = c_bool
MP4TagsSetComposerID.argtypes = [POINTER(MP4Tags), POINTER(uint32_t)]
MP4TagsSetXID = _libraries['/usr/lib/libmp4v2.so'].MP4TagsSetXID
MP4TagsSetXID.restype = c_bool
MP4TagsSetXID.argtypes = [POINTER(MP4Tags), STRING]

# values for enumeration 'MP4SampleDependencyType_e'
MP4SampleDependencyType_e = c_int # enum
MP4SampleDependencyType = MP4SampleDependencyType_e
MP4ReadSample = _libraries['/usr/lib/libmp4v2.so'].MP4ReadSample
MP4ReadSample.restype = c_bool
MP4ReadSample.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, POINTER(POINTER(uint8_t)), POINTER(uint32_t), POINTER(MP4Timestamp), POINTER(MP4Duration), POINTER(MP4Duration), POINTER(c_bool)]
MP4ReadSampleFromTime = _libraries['/usr/lib/libmp4v2.so'].MP4ReadSampleFromTime
MP4ReadSampleFromTime.restype = c_bool
MP4ReadSampleFromTime.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp, POINTER(POINTER(uint8_t)), POINTER(uint32_t), POINTER(MP4Timestamp), POINTER(MP4Duration), POINTER(MP4Duration), POINTER(c_bool)]
MP4WriteSample = _libraries['/usr/lib/libmp4v2.so'].MP4WriteSample
MP4WriteSample.restype = c_bool
MP4WriteSample.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint32_t, MP4Duration, MP4Duration, c_bool]
MP4WriteSampleDependency = _libraries['/usr/lib/libmp4v2.so'].MP4WriteSampleDependency
MP4WriteSampleDependency.restype = c_bool
MP4WriteSampleDependency.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint32_t, MP4Duration, MP4Duration, c_bool, uint32_t]
MP4CopySample = _libraries['/usr/lib/libmp4v2.so'].MP4CopySample
MP4CopySample.restype = c_bool
MP4CopySample.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, MP4FileHandle, MP4TrackId, MP4Duration]
MP4EncAndCopySample = _libraries['/usr/lib/libmp4v2.so'].MP4EncAndCopySample
MP4EncAndCopySample.restype = c_bool
MP4EncAndCopySample.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, encryptFunc_t, uint32_t, MP4FileHandle, MP4TrackId, MP4Duration]
MP4ReferenceSample = _libraries['/usr/lib/libmp4v2.so'].MP4ReferenceSample
MP4ReferenceSample.restype = c_bool
MP4ReferenceSample.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, MP4FileHandle, MP4TrackId, MP4Duration]
MP4GetSampleSize = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleSize
MP4GetSampleSize.restype = uint32_t
MP4GetSampleSize.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId]
MP4GetTrackMaxSampleSize = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackMaxSampleSize
MP4GetTrackMaxSampleSize.restype = uint32_t
MP4GetTrackMaxSampleSize.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetSampleIdFromTime = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleIdFromTime
MP4GetSampleIdFromTime.restype = MP4SampleId
MP4GetSampleIdFromTime.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp, c_bool]
MP4GetSampleTime = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleTime
MP4GetSampleTime.restype = MP4Timestamp
MP4GetSampleTime.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId]
MP4GetSampleDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleDuration
MP4GetSampleDuration.restype = MP4Duration
MP4GetSampleDuration.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId]
MP4GetSampleRenderingOffset = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleRenderingOffset
MP4GetSampleRenderingOffset.restype = MP4Duration
MP4GetSampleRenderingOffset.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId]
MP4SetSampleRenderingOffset = _libraries['/usr/lib/libmp4v2.so'].MP4SetSampleRenderingOffset
MP4SetSampleRenderingOffset.restype = c_bool
MP4SetSampleRenderingOffset.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, MP4Duration]
MP4GetSampleSync = _libraries['/usr/lib/libmp4v2.so'].MP4GetSampleSync
MP4GetSampleSync.restype = int8_t
MP4GetSampleSync.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId]
MP4GetHintTrackRtpPayload = _libraries['/usr/lib/libmp4v2.so'].MP4GetHintTrackRtpPayload
MP4GetHintTrackRtpPayload.restype = c_bool
MP4GetHintTrackRtpPayload.argtypes = [MP4FileHandle, MP4TrackId, POINTER(STRING), POINTER(uint8_t), POINTER(uint16_t), POINTER(STRING)]
MP4SetHintTrackRtpPayload = _libraries['/usr/lib/libmp4v2.so'].MP4SetHintTrackRtpPayload
MP4SetHintTrackRtpPayload.restype = c_bool
MP4SetHintTrackRtpPayload.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(uint8_t), uint16_t, STRING, c_bool, c_bool]
MP4GetSessionSdp = _libraries['/usr/lib/libmp4v2.so'].MP4GetSessionSdp
MP4GetSessionSdp.restype = STRING
MP4GetSessionSdp.argtypes = [MP4FileHandle]
MP4SetSessionSdp = _libraries['/usr/lib/libmp4v2.so'].MP4SetSessionSdp
MP4SetSessionSdp.restype = c_bool
MP4SetSessionSdp.argtypes = [MP4FileHandle, STRING]
MP4AppendSessionSdp = _libraries['/usr/lib/libmp4v2.so'].MP4AppendSessionSdp
MP4AppendSessionSdp.restype = c_bool
MP4AppendSessionSdp.argtypes = [MP4FileHandle, STRING]
MP4GetHintTrackSdp = _libraries['/usr/lib/libmp4v2.so'].MP4GetHintTrackSdp
MP4GetHintTrackSdp.restype = STRING
MP4GetHintTrackSdp.argtypes = [MP4FileHandle, MP4TrackId]
MP4SetHintTrackSdp = _libraries['/usr/lib/libmp4v2.so'].MP4SetHintTrackSdp
MP4SetHintTrackSdp.restype = c_bool
MP4SetHintTrackSdp.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4AppendHintTrackSdp = _libraries['/usr/lib/libmp4v2.so'].MP4AppendHintTrackSdp
MP4AppendHintTrackSdp.restype = c_bool
MP4AppendHintTrackSdp.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4GetHintTrackReferenceTrackId = _libraries['/usr/lib/libmp4v2.so'].MP4GetHintTrackReferenceTrackId
MP4GetHintTrackReferenceTrackId.restype = MP4TrackId
MP4GetHintTrackReferenceTrackId.argtypes = [MP4FileHandle, MP4TrackId]
MP4ReadRtpHint = _libraries['/usr/lib/libmp4v2.so'].MP4ReadRtpHint
MP4ReadRtpHint.restype = c_bool
MP4ReadRtpHint.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, POINTER(uint16_t)]
MP4GetRtpHintNumberOfPackets = _libraries['/usr/lib/libmp4v2.so'].MP4GetRtpHintNumberOfPackets
MP4GetRtpHintNumberOfPackets.restype = uint16_t
MP4GetRtpHintNumberOfPackets.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetRtpPacketBFrame = _libraries['/usr/lib/libmp4v2.so'].MP4GetRtpPacketBFrame
MP4GetRtpPacketBFrame.restype = int8_t
MP4GetRtpPacketBFrame.argtypes = [MP4FileHandle, MP4TrackId, uint16_t]
int32_t = c_int32
MP4GetRtpPacketTransmitOffset = _libraries['/usr/lib/libmp4v2.so'].MP4GetRtpPacketTransmitOffset
MP4GetRtpPacketTransmitOffset.restype = int32_t
MP4GetRtpPacketTransmitOffset.argtypes = [MP4FileHandle, MP4TrackId, uint16_t]
MP4ReadRtpPacket = _libraries['/usr/lib/libmp4v2.so'].MP4ReadRtpPacket
MP4ReadRtpPacket.restype = c_bool
MP4ReadRtpPacket.argtypes = [MP4FileHandle, MP4TrackId, uint16_t, POINTER(POINTER(uint8_t)), POINTER(uint32_t), uint32_t, c_bool, c_bool]
MP4GetRtpTimestampStart = _libraries['/usr/lib/libmp4v2.so'].MP4GetRtpTimestampStart
MP4GetRtpTimestampStart.restype = MP4Timestamp
MP4GetRtpTimestampStart.argtypes = [MP4FileHandle, MP4TrackId]
MP4SetRtpTimestampStart = _libraries['/usr/lib/libmp4v2.so'].MP4SetRtpTimestampStart
MP4SetRtpTimestampStart.restype = c_bool
MP4SetRtpTimestampStart.argtypes = [MP4FileHandle, MP4TrackId, MP4Timestamp]
MP4AddRtpHint = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpHint
MP4AddRtpHint.restype = c_bool
MP4AddRtpHint.argtypes = [MP4FileHandle, MP4TrackId]
MP4AddRtpVideoHint = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpVideoHint
MP4AddRtpVideoHint.restype = c_bool
MP4AddRtpVideoHint.argtypes = [MP4FileHandle, MP4TrackId, c_bool, uint32_t]
MP4AddRtpPacket = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpPacket
MP4AddRtpPacket.restype = c_bool
MP4AddRtpPacket.argtypes = [MP4FileHandle, MP4TrackId, c_bool, int32_t]
MP4AddRtpImmediateData = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpImmediateData
MP4AddRtpImmediateData.restype = c_bool
MP4AddRtpImmediateData.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint32_t]
MP4AddRtpSampleData = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpSampleData
MP4AddRtpSampleData.restype = c_bool
MP4AddRtpSampleData.argtypes = [MP4FileHandle, MP4TrackId, MP4SampleId, uint32_t, uint32_t]
MP4AddRtpESConfigurationPacket = _libraries['/usr/lib/libmp4v2.so'].MP4AddRtpESConfigurationPacket
MP4AddRtpESConfigurationPacket.restype = c_bool
MP4AddRtpESConfigurationPacket.argtypes = [MP4FileHandle, MP4TrackId]
MP4WriteRtpHint = _libraries['/usr/lib/libmp4v2.so'].MP4WriteRtpHint
MP4WriteRtpHint.restype = c_bool
MP4WriteRtpHint.argtypes = [MP4FileHandle, MP4TrackId, MP4Duration, c_bool]
MP4AddTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddTrack
MP4AddTrack.restype = MP4TrackId
MP4AddTrack.argtypes = [MP4FileHandle, STRING, uint32_t]
MP4AddSystemsTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddSystemsTrack
MP4AddSystemsTrack.restype = MP4TrackId
MP4AddSystemsTrack.argtypes = [MP4FileHandle, STRING]
MP4AddODTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddODTrack
MP4AddODTrack.restype = MP4TrackId
MP4AddODTrack.argtypes = [MP4FileHandle]
MP4AddSceneTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddSceneTrack
MP4AddSceneTrack.restype = MP4TrackId
MP4AddSceneTrack.argtypes = [MP4FileHandle]
MP4AddAudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddAudioTrack
MP4AddAudioTrack.restype = MP4TrackId
MP4AddAudioTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint8_t]
MP4AddULawAudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddULawAudioTrack
MP4AddULawAudioTrack.restype = MP4TrackId
MP4AddULawAudioTrack.argtypes = [MP4FileHandle, uint32_t]
MP4AddALawAudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddALawAudioTrack
MP4AddALawAudioTrack.restype = MP4TrackId
MP4AddALawAudioTrack.argtypes = [MP4FileHandle, uint32_t]
MP4AddAC3AudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddAC3AudioTrack
MP4AddAC3AudioTrack.restype = MP4TrackId
MP4AddAC3AudioTrack.argtypes = [MP4FileHandle, uint32_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t]
MP4AddAmrAudioTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddAmrAudioTrack
MP4AddAmrAudioTrack.restype = MP4TrackId
MP4AddAmrAudioTrack.argtypes = [MP4FileHandle, uint32_t, uint16_t, uint8_t, uint8_t, c_bool]
MP4SetAmrVendor = _libraries['/usr/lib/libmp4v2.so'].MP4SetAmrVendor
MP4SetAmrVendor.restype = None
MP4SetAmrVendor.argtypes = [MP4FileHandle, MP4TrackId, uint32_t]
MP4SetAmrDecoderVersion = _libraries['/usr/lib/libmp4v2.so'].MP4SetAmrDecoderVersion
MP4SetAmrDecoderVersion.restype = None
MP4SetAmrDecoderVersion.argtypes = [MP4FileHandle, MP4TrackId, uint8_t]
MP4SetAmrModeSet = _libraries['/usr/lib/libmp4v2.so'].MP4SetAmrModeSet
MP4SetAmrModeSet.restype = None
MP4SetAmrModeSet.argtypes = [MP4FileHandle, MP4TrackId, uint16_t]
MP4GetAmrModeSet = _libraries['/usr/lib/libmp4v2.so'].MP4GetAmrModeSet
MP4GetAmrModeSet.restype = uint16_t
MP4GetAmrModeSet.argtypes = [MP4FileHandle, MP4TrackId]
MP4AddHrefTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddHrefTrack
MP4AddHrefTrack.restype = MP4TrackId
MP4AddHrefTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, STRING]
MP4GetHrefTrackBaseUrl = _libraries['/usr/lib/libmp4v2.so'].MP4GetHrefTrackBaseUrl
MP4GetHrefTrackBaseUrl.restype = STRING
MP4GetHrefTrackBaseUrl.argtypes = [MP4FileHandle, MP4TrackId]
MP4AddVideoTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddVideoTrack
MP4AddVideoTrack.restype = MP4TrackId
MP4AddVideoTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint16_t, uint16_t, uint8_t]
MP4AddH264VideoTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddH264VideoTrack
MP4AddH264VideoTrack.restype = MP4TrackId
MP4AddH264VideoTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint16_t, uint16_t, uint8_t, uint8_t, uint8_t, uint8_t]
MP4AddH264SequenceParameterSet = _libraries['/usr/lib/libmp4v2.so'].MP4AddH264SequenceParameterSet
MP4AddH264SequenceParameterSet.restype = None
MP4AddH264SequenceParameterSet.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint16_t]
MP4AddH264PictureParameterSet = _libraries['/usr/lib/libmp4v2.so'].MP4AddH264PictureParameterSet
MP4AddH264PictureParameterSet.restype = None
MP4AddH264PictureParameterSet.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint16_t]
MP4SetH263Vendor = _libraries['/usr/lib/libmp4v2.so'].MP4SetH263Vendor
MP4SetH263Vendor.restype = None
MP4SetH263Vendor.argtypes = [MP4FileHandle, MP4TrackId, uint32_t]
MP4SetH263DecoderVersion = _libraries['/usr/lib/libmp4v2.so'].MP4SetH263DecoderVersion
MP4SetH263DecoderVersion.restype = None
MP4SetH263DecoderVersion.argtypes = [MP4FileHandle, MP4TrackId, uint8_t]
MP4SetH263Bitrates = _libraries['/usr/lib/libmp4v2.so'].MP4SetH263Bitrates
MP4SetH263Bitrates.restype = None
MP4SetH263Bitrates.argtypes = [MP4FileHandle, MP4TrackId, uint32_t, uint32_t]
MP4AddH263VideoTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddH263VideoTrack
MP4AddH263VideoTrack.restype = MP4TrackId
MP4AddH263VideoTrack.argtypes = [MP4FileHandle, uint32_t, MP4Duration, uint16_t, uint16_t, uint8_t, uint8_t, uint32_t, uint32_t]
MP4AddHintTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddHintTrack
MP4AddHintTrack.restype = MP4TrackId
MP4AddHintTrack.argtypes = [MP4FileHandle, MP4TrackId]
MP4AddTextTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddTextTrack
MP4AddTextTrack.restype = MP4TrackId
MP4AddTextTrack.argtypes = [MP4FileHandle, MP4TrackId]
MP4AddSubtitleTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddSubtitleTrack
MP4AddSubtitleTrack.restype = MP4TrackId
MP4AddSubtitleTrack.argtypes = [MP4FileHandle, uint32_t, uint16_t, uint16_t]
MP4AddSubpicTrack = _libraries['/usr/lib/libmp4v2.so'].MP4AddSubpicTrack
MP4AddSubpicTrack.restype = MP4TrackId
MP4AddSubpicTrack.argtypes = [MP4FileHandle, uint32_t, uint16_t, uint16_t]
MP4AddPixelAspectRatio = _libraries['/usr/lib/libmp4v2.so'].MP4AddPixelAspectRatio
MP4AddPixelAspectRatio.restype = MP4TrackId
MP4AddPixelAspectRatio.argtypes = [MP4FileHandle, MP4TrackId, uint32_t, uint32_t]
MP4AddColr = _libraries['/usr/lib/libmp4v2.so'].MP4AddColr
MP4AddColr.restype = MP4TrackId
MP4AddColr.argtypes = [MP4FileHandle, MP4TrackId, uint16_t, uint16_t, uint16_t]
MP4CloneTrack = _libraries['/usr/lib/libmp4v2.so'].MP4CloneTrack
MP4CloneTrack.restype = MP4TrackId
MP4CloneTrack.argtypes = [MP4FileHandle, MP4TrackId, MP4FileHandle, MP4TrackId]
MP4CopyTrack = _libraries['/usr/lib/libmp4v2.so'].MP4CopyTrack
MP4CopyTrack.restype = MP4TrackId
MP4CopyTrack.argtypes = [MP4FileHandle, MP4TrackId, MP4FileHandle, c_bool, MP4TrackId]
MP4DeleteTrack = _libraries['/usr/lib/libmp4v2.so'].MP4DeleteTrack
MP4DeleteTrack.restype = c_bool
MP4DeleteTrack.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetNumberOfTracks = _libraries['/usr/lib/libmp4v2.so'].MP4GetNumberOfTracks
MP4GetNumberOfTracks.restype = uint32_t
MP4GetNumberOfTracks.argtypes = [MP4FileHandle, STRING, uint8_t]
MP4FindTrackId = _libraries['/usr/lib/libmp4v2.so'].MP4FindTrackId
MP4FindTrackId.restype = MP4TrackId
MP4FindTrackId.argtypes = [MP4FileHandle, uint16_t, STRING, uint8_t]
MP4FindTrackIndex = _libraries['/usr/lib/libmp4v2.so'].MP4FindTrackIndex
MP4FindTrackIndex.restype = uint16_t
MP4FindTrackIndex.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackDurationPerChunk = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackDurationPerChunk
MP4GetTrackDurationPerChunk.restype = c_bool
MP4GetTrackDurationPerChunk.argtypes = [MP4FileHandle, MP4TrackId, POINTER(MP4Duration)]
MP4SetTrackDurationPerChunk = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackDurationPerChunk
MP4SetTrackDurationPerChunk.restype = c_bool
MP4SetTrackDurationPerChunk.argtypes = [MP4FileHandle, MP4TrackId, MP4Duration]
MP4AddIPodUUID = _libraries['/usr/lib/libmp4v2.so'].MP4AddIPodUUID
MP4AddIPodUUID.restype = c_bool
MP4AddIPodUUID.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackType = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackType
MP4GetTrackType.restype = STRING
MP4GetTrackType.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackMediaDataName = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackMediaDataName
MP4GetTrackMediaDataName.restype = STRING
MP4GetTrackMediaDataName.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackMediaDataOriginalFormat = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackMediaDataOriginalFormat
MP4GetTrackMediaDataOriginalFormat.restype = c_bool
MP4GetTrackMediaDataOriginalFormat.argtypes = [MP4FileHandle, MP4TrackId, STRING, uint32_t]
MP4GetTrackDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackDuration
MP4GetTrackDuration.restype = MP4Duration
MP4GetTrackDuration.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackTimeScale = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackTimeScale
MP4GetTrackTimeScale.restype = uint32_t
MP4GetTrackTimeScale.argtypes = [MP4FileHandle, MP4TrackId]
MP4SetTrackTimeScale = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackTimeScale
MP4SetTrackTimeScale.restype = c_bool
MP4SetTrackTimeScale.argtypes = [MP4FileHandle, MP4TrackId, uint32_t]
MP4GetTrackLanguage = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackLanguage
MP4GetTrackLanguage.restype = c_bool
MP4GetTrackLanguage.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4SetTrackLanguage = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackLanguage
MP4SetTrackLanguage.restype = c_bool
MP4SetTrackLanguage.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4GetTrackName = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackName
MP4GetTrackName.restype = c_bool
MP4GetTrackName.argtypes = [MP4FileHandle, MP4TrackId, POINTER(STRING)]
MP4SetTrackName = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackName
MP4SetTrackName.restype = c_bool
MP4SetTrackName.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4GetTrackAudioMpeg4Type = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackAudioMpeg4Type
MP4GetTrackAudioMpeg4Type.restype = uint8_t
MP4GetTrackAudioMpeg4Type.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackEsdsObjectTypeId = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackEsdsObjectTypeId
MP4GetTrackEsdsObjectTypeId.restype = uint8_t
MP4GetTrackEsdsObjectTypeId.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackFixedSampleDuration = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackFixedSampleDuration
MP4GetTrackFixedSampleDuration.restype = MP4Duration
MP4GetTrackFixedSampleDuration.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackBitRate = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackBitRate
MP4GetTrackBitRate.restype = uint32_t
MP4GetTrackBitRate.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackVideoMetadata = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackVideoMetadata
MP4GetTrackVideoMetadata.restype = c_bool
MP4GetTrackVideoMetadata.argtypes = [MP4FileHandle, MP4TrackId, POINTER(POINTER(uint8_t)), POINTER(uint32_t)]
MP4GetTrackESConfiguration = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackESConfiguration
MP4GetTrackESConfiguration.restype = c_bool
MP4GetTrackESConfiguration.argtypes = [MP4FileHandle, MP4TrackId, POINTER(POINTER(uint8_t)), POINTER(uint32_t)]
MP4SetTrackESConfiguration = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackESConfiguration
MP4SetTrackESConfiguration.restype = c_bool
MP4SetTrackESConfiguration.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), uint32_t]
MP4GetTrackH264ProfileLevel = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackH264ProfileLevel
MP4GetTrackH264ProfileLevel.restype = c_bool
MP4GetTrackH264ProfileLevel.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint8_t), POINTER(uint8_t)]
MP4GetTrackH264SeqPictHeaders = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackH264SeqPictHeaders
MP4GetTrackH264SeqPictHeaders.restype = c_bool
MP4GetTrackH264SeqPictHeaders.argtypes = [MP4FileHandle, MP4TrackId, POINTER(POINTER(POINTER(uint8_t))), POINTER(POINTER(uint32_t)), POINTER(POINTER(POINTER(uint8_t))), POINTER(POINTER(uint32_t))]
MP4GetTrackH264LengthSize = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackH264LengthSize
MP4GetTrackH264LengthSize.restype = c_bool
MP4GetTrackH264LengthSize.argtypes = [MP4FileHandle, MP4TrackId, POINTER(uint32_t)]
MP4GetTrackNumberOfSamples = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackNumberOfSamples
MP4GetTrackNumberOfSamples.restype = MP4SampleId
MP4GetTrackNumberOfSamples.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackVideoWidth = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackVideoWidth
MP4GetTrackVideoWidth.restype = uint16_t
MP4GetTrackVideoWidth.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackVideoHeight = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackVideoHeight
MP4GetTrackVideoHeight.restype = uint16_t
MP4GetTrackVideoHeight.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackVideoFrameRate = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackVideoFrameRate
MP4GetTrackVideoFrameRate.restype = c_double
MP4GetTrackVideoFrameRate.argtypes = [MP4FileHandle, MP4TrackId]
MP4GetTrackAudioChannels = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackAudioChannels
MP4GetTrackAudioChannels.restype = c_int
MP4GetTrackAudioChannels.argtypes = [MP4FileHandle, MP4TrackId]
MP4IsIsmaCrypMediaTrack = _libraries['/usr/lib/libmp4v2.so'].MP4IsIsmaCrypMediaTrack
MP4IsIsmaCrypMediaTrack.restype = c_bool
MP4IsIsmaCrypMediaTrack.argtypes = [MP4FileHandle, MP4TrackId]
MP4HaveTrackAtom = _libraries['/usr/lib/libmp4v2.so'].MP4HaveTrackAtom
MP4HaveTrackAtom.restype = c_bool
MP4HaveTrackAtom.argtypes = [MP4FileHandle, MP4TrackId, STRING]
MP4GetTrackIntegerProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackIntegerProperty
MP4GetTrackIntegerProperty.restype = c_bool
MP4GetTrackIntegerProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(uint64_t)]
MP4GetTrackFloatProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackFloatProperty
MP4GetTrackFloatProperty.restype = c_bool
MP4GetTrackFloatProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(c_float)]
MP4GetTrackStringProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackStringProperty
MP4GetTrackStringProperty.restype = c_bool
MP4GetTrackStringProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(STRING)]
MP4GetTrackBytesProperty = _libraries['/usr/lib/libmp4v2.so'].MP4GetTrackBytesProperty
MP4GetTrackBytesProperty.restype = c_bool
MP4GetTrackBytesProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(POINTER(uint8_t)), POINTER(uint32_t)]
MP4SetTrackIntegerProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackIntegerProperty
MP4SetTrackIntegerProperty.restype = c_bool
MP4SetTrackIntegerProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, int64_t]
MP4SetTrackFloatProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackFloatProperty
MP4SetTrackFloatProperty.restype = c_bool
MP4SetTrackFloatProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, c_float]
MP4SetTrackStringProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackStringProperty
MP4SetTrackStringProperty.restype = c_bool
MP4SetTrackStringProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, STRING]
MP4SetTrackBytesProperty = _libraries['/usr/lib/libmp4v2.so'].MP4SetTrackBytesProperty
MP4SetTrackBytesProperty.restype = c_bool
MP4SetTrackBytesProperty.argtypes = [MP4FileHandle, MP4TrackId, STRING, POINTER(uint8_t), uint32_t]
int16_t = c_int16
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
off_t = __off_t
off64_t = __off64_t
ssize_t = __ssize_t
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/lib/libmp4v2.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/lib/libmp4v2.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/lib/libmp4v2.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/lib/libmp4v2.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/lib/libmp4v2.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/lib/libmp4v2.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/lib/libmp4v2.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/lib/libmp4v2.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/lib/libmp4v2.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/lib/libmp4v2.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/lib/libmp4v2.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/lib/libmp4v2.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/lib/libmp4v2.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/lib/libmp4v2.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/lib/libmp4v2.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/lib/libmp4v2.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/lib/libmp4v2.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/lib/libmp4v2.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/lib/libmp4v2.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/lib/libmp4v2.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/lib/libmp4v2.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/lib/libmp4v2.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/lib/libmp4v2.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/lib/libmp4v2.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fprintf = _libraries['/usr/lib/libmp4v2.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/lib/libmp4v2.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
sprintf = _libraries['/usr/lib/libmp4v2.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vfprintf = _libraries['/usr/lib/libmp4v2.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vsprintf = _libraries['/usr/lib/libmp4v2.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['/usr/lib/libmp4v2.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/lib/libmp4v2.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
vasprintf = _libraries['/usr/lib/libmp4v2.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
__asprintf = _libraries['/usr/lib/libmp4v2.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
asprintf = _libraries['/usr/lib/libmp4v2.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
vdprintf = _libraries['/usr/lib/libmp4v2.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
dprintf = _libraries['/usr/lib/libmp4v2.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
fscanf = _libraries['/usr/lib/libmp4v2.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/lib/libmp4v2.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/lib/libmp4v2.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/lib/libmp4v2.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['/usr/lib/libmp4v2.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['/usr/lib/libmp4v2.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['/usr/lib/libmp4v2.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/lib/libmp4v2.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/lib/libmp4v2.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/lib/libmp4v2.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/lib/libmp4v2.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/lib/libmp4v2.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
fgets = _libraries['/usr/lib/libmp4v2.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
gets = _libraries['/usr/lib/libmp4v2.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
fgets_unlocked = _libraries['/usr/lib/libmp4v2.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__getdelim = _libraries['/usr/lib/libmp4v2.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/lib/libmp4v2.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/lib/libmp4v2.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/lib/libmp4v2.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/lib/libmp4v2.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fread = _libraries['/usr/lib/libmp4v2.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fwrite = _libraries['/usr/lib/libmp4v2.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/lib/libmp4v2.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fread_unlocked = _libraries['/usr/lib/libmp4v2.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/lib/libmp4v2.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/lib/libmp4v2.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/lib/libmp4v2.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/lib/libmp4v2.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/lib/libmp4v2.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/lib/libmp4v2.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/lib/libmp4v2.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/lib/libmp4v2.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/lib/libmp4v2.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/lib/libmp4v2.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/lib/libmp4v2.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/lib/libmp4v2.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/lib/libmp4v2.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/lib/libmp4v2.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/lib/libmp4v2.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/lib/libmp4v2.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/lib/libmp4v2.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/lib/libmp4v2.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/lib/libmp4v2.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/lib/libmp4v2.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/lib/libmp4v2.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/lib/libmp4v2.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/lib/libmp4v2.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
class obstack(Structure):
    pass
obstack._fields_ = [
]
obstack_printf = _libraries['/usr/lib/libmp4v2.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
obstack_vprintf = _libraries['/usr/lib/libmp4v2.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, POINTER(__va_list_tag)]
flockfile = _libraries['/usr/lib/libmp4v2.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/lib/libmp4v2.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/lib/libmp4v2.so'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
ptrdiff_t = c_long
__all__ = ['MP4_ITMF_BT_ISRC', '_ATFILE_SOURCE', 'EOF',
           'MP4V2_PROJECT_repo_root', 'MP4GetTrackEditDuration',
           '__glibc_unlikely', 'MP4BinaryToBase16', 'getc_unlocked',
           '_IO_USER_LOCK', 'MPEG4_ASP_L3', 'MPEG4_ASP_L2',
           'MPEG4_ASP_L1', 'MPEG4_ASP_L0', '_G_ssize_t',
           'MPEG4_ASP_L5', '__off64_t', '__int16_t',
           'MP4V2_PROJECT_repo_type', 'MP4AddH263VideoTrack',
           'uint8_t', 'fpos_t', '_G_HAVE_MREMAP',
           'MP4TagsSetTVNetwork', 'fprintf', 'MP4SetSessionSdp',
           'MP4SetTrackEditMediaStart', 'va_end', '_G_va_list',
           'MP4SetBytesProperty', '_G_int16_t', 'getline',
           'MP4GetRtpHintNumberOfPackets', '_IO_BUFSIZ', '__FILE',
           '_IO_off64_t', 'MP4SetTrackIntegerProperty',
           '_IO_fpos64_t', 'MP4GetSampleIdFromEditTime',
           'MP4GetVideoProfileLevel', 'MP4_MICROSECONDS_TIME_SCALE',
           'MP4GetStringProperty', '__time_t', '__GLIBC_PREREQ',
           'MP4_ITMF_BT_DURATION', '__ASMNAME', 'MP4ItmfItemList',
           '_POSIX_SOURCE', 'uint_fast16_t', '_IO_jump_t', 'stderr',
           'MP4BinaryToBase64', 'MP4V2_PROJECT_repo_url', '__swblk_t',
           'MP4_IS_VALID_DURATION', 'snprintf', '__va_list_tag',
           'MP4_MPEG2_MAIN_VIDEO_TYPE', 'MPEG4_ASP_L4',
           'MP4LogSetLevel', 'MP4V2_PROJECT_repo_branch',
           'MP4_MP3_AUDIO_TYPE', 'UINTMAX_C',
           'MP4_CLOSE_DO_NOT_COMPUTE_BITRATE', '_IO_off_t',
           'MP4_MPEG2_AUDIO_TYPE', '__clockid_t', 'MP4CopyTrack',
           'getchar_unlocked', 'MP4AddALawAudioTrack',
           'MP4_MPEG1_AUDIO_TYPE', '__timer_t', 'MP4ReadProvider',
           'MP4_MPEG4_VIDEO_TYPE', 'MP4_MPEG2_VIDEO_TYPE',
           'MP4GetAmrModeSet', 'MP4_ITMF_BT_URL', '_G_HAVE_MMAP',
           '_G_fpos_t', '__attribute_format_strfmon__',
           '__STDC_NO_THREADS__', 'MP4TagsSetArtwork',
           'MP4_IS_VALID_TIMESTAMP', 'MP4SetGraphicsProfileLevel',
           '_IO_pos_t', 'UINT16_C', 'MP4GetTrackTimeScale',
           'MP4GetSessionSdp', 'MP4FileProvider', 'open_memstream',
           'fsetpos64', 'MP4ChapterTypeNone', '__u_long',
           'MP4ItmfItem_s', 'MP4_CREATE_64BIT_TIME',
           'MP4TagsSetAlbum', 'MP4TagsSetCategory',
           'MP4_IS_VALID_SAMPLE_ID', '_IO_SKIPWS',
           'MP4TagsSetContentID', 'fopen', 'MP4_ART_BMP', 'setbuf',
           'MP4Duration', '__codecvt_result', '_IO_SCIENTIFIC',
           'MP4TagArtworkType_e', '_IO_2_1_stdin_', 'MP4HaveAtom',
           '_IO_ferror', 'MP4EncAndCloneTrack', '_G_FSTAT64',
           'MP4_MPEG4_LAYER2_AUDIO_TYPE', '_IO_BOOLALPHA', '__PMT',
           'uint_fast8_t', '_LARGEFILE_SOURCE', '__io_read_fn',
           'MP4CopySample', 'MP4_SDT_UNKNOWN', 'MP4Free', '__mode_t',
           'MP4_MPEG4_LAYER3_AUDIO_TYPE', '_IO_DEC', 'MPEG4_SFAP_L1',
           '__off_t', 'MP4EncAndCopySample', 'fmemopen', 'getchar',
           'MP4_MPEG4_HVXC_AUDIO_TYPE', 'MP4TagsSetEncodingTool',
           'MP4GetTrackName', 'MP4TagsSetXID',
           'MP4_SDT_HAS_NO_DEPENDENTS', 'MP4_AC3_AUDIO_TYPE',
           'fputs_unlocked', 'MP4_ITMF_BT_GIF', '_IOS_TRUNC',
           'MP4ConvertToTrackTimestamp', 'uint_least32_t',
           'int_least64_t', 'MPEG4_AST_L3', 'MPEG4_AST_L2',
           'MPEG4_AST_L1', 'MP4V2_PROJECT_version',
           'MP4TagsSetDescription', 'MP4AddRtpHint',
           'MPEG4_C_STUDIO_P_L2', '__USE_FORTIFY_LEVEL', '__int8_t',
           '__fsblkcnt64_t', 'MP4GetTrackMediaDataName',
           'MP4SetSampleRenderingOffset', 'MP4TagsSetPurchaseDate',
           '__uflow', 'int32_t', 'MP4SetH263Vendor', 'SEEK_HOLE',
           '__USE_XOPEN_EXTENDED', 'MP4_INVALID_SAMPLE_ID',
           'MP4GetHintTrackRtpPayload', 'ftrylockfile',
           'MPEG4_C_STUDIO_P_L4', '__fsfilcnt64_t', '_IO_pid_t',
           'MP4TagDisk', '_IO_FILE', 'MP4AddPixelAspectRatio',
           'MP4AddHrefTrack', 'MPEG4_FGSP_L4', 'MPEG4_FGSP_L5',
           'MPEG4_FGSP_L2', 'MPEG4_FGSP_L3', 'MPEG4_FGSP_L0',
           'MPEG4_FGSP_L1', 'MP4V2_PROJECT_bugreport',
           'MP4TagsSetGenre', '_IO_UNITBUF', 'MP4EncAndCopyTrack',
           'intptr_t', 'off_t', '__fsblkcnt_t', 'MP4TagsFetch',
           'MP4DeleteTrack', 'MP4FileHandle',
           'MP4TagsSetITunesCountry',
           'MP4_MPEG4_MAIN_SYNTHETIC_AUDIO_TYPE',
           'MP4_PRIVATE_AUDIO_TYPE', 'feof',
           'MP4TagsSetContentRating', '__STDC_CONSTANT_MACROS',
           'clearerr', 'MP4TagsSetMediaType', 'MP4AddColr',
           'MP4ItmfItemList_s', 'MP4_MPEG4_TTSI_AUDIO_TYPE',
           'MP4WriteSample', '__WORDSIZE', 'vfprintf',
           'MPEG4_BATP_L2', 'putc_unlocked', '____mbstate_t_defined',
           'MP4_ITMF_BT_XML', 'MP4HaveTrackAtom',
           'MP4TagsSetAlbumArtist', 'UINT32_C',
           'MP4_MPEG4_SLS_AUDIO_TYPE', '_XOPEN_SOURCE',
           '_IO_free_backup_area', 'MP4_ITMF_BT_SJIS',
           'MP4_ITMF_BT_UUID', 'MP4GetSampleDuration',
           'MP4V2_PROJECT_name_upper', '__USE_ISOC95',
           'MP4GetDuration', 'MPEG4_CSP_L1', '_G_off64_t',
           '__GLIBC__', 'MPEG4_CSP_L2', '__USE_ISOC99', 'MP4_ART_GIF',
           'MP4SetTrackLanguage', 'MP4_MPEG2_AAC_SSR_AUDIO_TYPE',
           '_IO_fpos_t', 'MP4Tags_s', 'stdin', '__u_int',
           'MP4_MPEG4_INVALID_AUDIO_TYPE', 'ssize_t',
           'MP4GetTrackLanguage', '__clock_t', '__fsfilcnt_t',
           'MP4TagsSetLongDescription', 'MP4_AUDIO_TRACK_TYPE',
           '_G_HAVE_IO_GETLINE_INFO', 'MP4_MPEG2_HIGH_VIDEO_TYPE',
           'vscanf', 'MP4V2_PROJECT_version_major',
           'MP4_SDT_HAS_REDUNDANT_CODING', 'MP4GetSampleIdFromTime',
           '_IONBF', 'FILE', 'ferror_unlocked', 'size_t',
           '__USE_XOPEN', 'MP4TagDisk_s', 'TRUE',
           'MP4V2_PROJECT_version_point', '__USE_POSIX2',
           'MP4_ITMF_BT_UTF16', 'obstack_printf', '_IO_ftrylockfile',
           '_IO_marker', 'MP4_TEXT_TRACK_TYPE', 'uint_least16_t',
           '__syscall_slong_t', 'fseeko64',
           'MP4V2_PROJECT_url_discussion', 'MP4Make3GPCompliant',
           'feof_unlocked', '__qaddr_t', '_G_HAVE_LONG_DOUBLE_IO',
           'MP4TagsSetCopyright', 'MP4FindTrackId',
           'MP4GetTrackEditMediaStart', 'MP4FileInfo',
           'MP4SetSceneProfileLevel', '_IO_RIGHT', '_IOS_APPEND',
           'rewind', 'MP4AddULawAudioTrack', 'MP4_SDT_HAS_DEPENDENTS',
           'MP4ConvertFromMovieDuration', 'fpos64_t', '__USE_ATFILE',
           'perror', 'TMP_MAX', 'MP4TagsSetSortAlbum', '_G_BUFSIZ',
           'MP4_LOG_NONE', 'MP4DeleteTrackEdit',
           'MP4GetHintTrackReferenceTrackId',
           'MP4_MPEG4_AAC_HE_AUDIO_TYPE', 'MP4AddSceneTrack',
           '__int32_t', 'MP4AddSystemsTrack', '__USE_POSIX',
           '_IO_NO_WRITES', 'mp4v2_ismacryp_session_params',
           'flockfile', 'MP4AddEncH264VideoTrack',
           'MP4SetTrackBytesProperty', '_G_HAVE_IO_FILE_OPEN',
           'MP4SetIntegerProperty', 'MP4V2_PROJECT_repo_uuid',
           'MP4_IS_VALID_TRACK_ID', 'va_copy', '__FILE_defined',
           'MP4TagsSetPlaylistID', 'fwrite_unlocked',
           'MP4AddAC3AudioTrack', 'MP4ConvertFromTrackDuration',
           'MP4Info', '_G_NAMES_HAVE_UNDERSCORE',
           'MP4_CNTL_TRACK_TYPE', 'MP4SetTrackFloatProperty',
           'MP4Dump', 'MP4WriteSampleDependency', '__useconds_t',
           '_BITS_WCHAR_H', '__GLIBC_MINOR__',
           '_IO_CURRENTLY_PUTTING', 'MP4TagsSetLyrics', 'ftell',
           'MP4TagsAddArtwork', 'sprintf',
           'MP4GetRtpPacketTransmitOffset',
           'MP4GetTrackDurationPerChunk', 'uint_least8_t',
           'fgetpos64', 'MP4V2_PROJECT_version_hex',
           'MP4ChapterTypeAny', 'MP4_ALAW_AUDIO_TYPE',
           'MP4GetIntegerProperty', 'MP4TagsSetSortTVShow',
           'MP4SetAudioProfileLevel', 'asprintf',
           'MP4_MPEG4_AAC_MAIN_AUDIO_TYPE',
           '__WORDSIZE_TIME64_COMPAT32', 'MPEG4_SFBAP_L1',
           '_IO_cookie_io_functions_t', 'MPEG4_SFBAP_L2',
           'MP4TagArtwork_s', '__gnuc_va_list', '__P',
           'MP4TagArtwork', '_G_VTABLE_LABEL_HAS_LENGTH',
           '_IO_ERR_SEEN', 'MP4_INVALID_DURATION',
           'MP4GetTrackVideoWidth', 'MP4GetTrackAudioChannels',
           'fseeko', 'putchar', 'MP4AddNeroChapter', '__USE_GNU',
           'MPEG4_SSP_L1', 'MPEG4_SSP_L2',
           'MP4SetTrackStringProperty', 'fputc_unlocked',
           '__attribute_format_arg__', 'MP4ReadRtpHint', '__ino_t',
           'ferror', '__rlim64_t', '_G_IO_IO_FILE_VERSION',
           '_POSIX_C_SOURCE', 'MP4TagTrack', 'fopencookie',
           'MP4_SDT_IS_DEPENDENT', 'MP4FileMode_e', '_IO_ssize_t',
           'MP4_MPEG4_AUDIO_TYPE', 'MP4TrackId',
           'MP4_IPMP_TRACK_TYPE', '__blksize_t', '__uint64_t',
           '__USE_SVID', 'MP4TagsSetSortName', '_IO_seekoff',
           'MP4GetTrackNumberOfEdits', 'MP4SetVideoProfileLevel',
           '__USE_ANSI', 'MP4GetTrackMaxSampleSize', 'MPEG4_CSP_L3',
           '_IO_IS_APPENDING', 'MP4ItmfGetItems', '_sys_nerr',
           'scanf', 'MP4SetRtpTimestampStart', 'fclose',
           'MPEG4_NBP_L2', 'MP4AddTrackEdit', 'MP4FileMode',
           'MP4_ITMF_BT_IMPLICIT', '__asprintf',
           'MP4_MILLISECONDS_TIME_SCALE', 'MP4AddTextTrack',
           'MPEG4_CP_L2', 'MPEG4_CP_L1', '__mbstate_t', '__uint8_t',
           'setbuffer', 'MP4_MPEG4_WAVETABLE_AUDIO_TYPE', '__u_char',
           'MP4GetHrefTrackBaseUrl', 'MP4GetSampleSync',
           '__blkcnt64_t', 'int_fast8_t', '__STDC_ISO_10646__',
           'MP4_MPEG2_SPATIAL_VIDEO_TYPE', '_IOS_NOCREATE',
           'MP4_SDT_IS_INDEPENDENT', '_G_uid_t', 'L_ctermid',
           '_IO_TIED_PUT_GET', 'MPEG4_ARTSP_L4', 'MPEG4_ARTSP_L3',
           'MPEG4_ARTSP_L2', 'MPEG4_ARTSP_L1', 'fscanf',
           'uint_fast64_t', 'MP4ReferenceSample', '__USE_LARGEFILE',
           '__USE_EXTERN_INLINES', 'MP4TagsSetTrack', 'va_list',
           '_IO_BE', 'MP4_ITMF_BT_BMP', 'MP4TagsSetArtistID',
           'MP4V2_PROJECT_build', 'MP4_ITMF_BT_INTEGER', 'SEEK_DATA',
           'SEEK_CUR', '__REDIRECT_NTH_LDBL', 'MP4_MSECS_TIME_SCALE',
           '_IO_peekc_locked', 'MP4AddRtpESConfigurationPacket',
           'MP4SetHintTrackSdp', 'MP4_ULAW_AUDIO_TYPE',
           '_BITS_TYPES_H', 'uintptr_t', 'MP4_H261_VIDEO_TYPE',
           '_MP4_SDT_RESERVED', 'MP4TagsSetTVSeason',
           'MP4SetODProfileLevel', 'MP4_ITMF_BT_UNDEFINED',
           'MP4TagsRemoveArtwork', 'MP4AddRtpPacket', 'int_fast32_t',
           'MP4_ART_PNG', 'MP4AddRtpVideoHint', 'fputc',
           '_XOPEN_SOURCE_EXTENDED', 'MP4TagsSetArtist',
           '__USE_POSIX199309', '__USE_UNIX98', 'MP4ItmfRemoveItem',
           'MP4_MPEG7_TRACK_TYPE', '_IO_INTERNAL',
           'MP4ReadSampleFromTime', '_IO_UNBUFFERED', 'printf',
           'ptrdiff_t', 'MP4_PRIVATE_VIDEO_TYPE',
           'MP4GetAudioProfileLevel', '_IOS_ATEND',
           'MP4V2_CHAPTER_TITLE_MAX', 'MP4AppendHintTrackSdp',
           'MP4TagsSetGenreID', 'MP4_VORBIS_AUDIO_TYPE',
           'MP4_IS_MPEG1_VIDEO_TYPE', 'dprintf', 'MPEG4_HP_L1',
           'MPEG4_HP_L2', 'MP4SampleDependencyType_e',
           'MP4ItmfBasicType', 'fgets_unlocked',
           'MPEG4_S_STUDIO_P_L3', 'MPEG4_S_STUDIO_P_L2',
           'MPEG4_S_STUDIO_P_L1', '_BSD_SOURCE',
           'MPEG4_S_STUDIO_P_L4', '__uid_t', 'setlinebuf', 'setvbuf',
           '_IO_funlockfile', '__uint16_t', 'fgetpos',
           'obstack_vprintf', 'MP4SetTrackName', 'getw',
           'MP4SetChapters', '_IO_putc', 'MP4SampleId', 'UINT8_C',
           '__GNU_LIBRARY__', '_BITS_TYPESIZES_H', 'putchar_unlocked',
           'MP4AddHintTrack', '_IO_USER_BUF', '__USE_LARGEFILE64',
           'encryptFunc_t', 'MP4V2_PROJECT_irc', 'MP4AddChapter',
           '__underflow', 'INTMAX_C', 'MP4V2_PROJECT_name',
           'MP4_SDT_HAS_NO_REDUNDANT_CODING',
           'MP4_SET_DYNAMIC_PAYLOAD', 'MP4_INVALID_TRACK_ID',
           '_IO_SHOWBASE', 'MP4ItmfGetItemsByMeaning', 'fputs',
           '_IO_LINE_BUF', 'MP4FileProvider_s', 'MP4Read',
           'MP4_ITMF_BT_UPC', '__loff_t', 'MP4SetStringProperty',
           'MP4_OCI_TRACK_TYPE', '_G_config_h', 'MPEG4_BATP_L1',
           'cookie_seek_function_t', '_IO_FLAGS2_MMAP',
           '_G_USING_THUNKS', 'MP4AddEncVideoTrack',
           'MP4ReadRtpPacket', 'MP4Timestamp', 'FALSE',
           '__GLIBC_HAVE_LONG_LONG', 'MP4_ART_JPEG',
           'MP4_INVALID_TIMESTAMP', 'MP4GetSampleRenderingOffset',
           'fileno', 'vdprintf', 'FOPEN_MAX', '_IO_DELETE_DONT_CLOSE',
           'MP4AddSubpicTrack', 'MP4GetTimeScale', 'remove',
           '__codecvt_partial', 'MP4_MPEG4_ALS_AUDIO_TYPE',
           'MP4ConvertChapters', 'MP4_MPEG2_SNR_VIDEO_TYPE', '__bos',
           'cookie_close_function_t',
           'MP4GetTrackFixedSampleDuration', 'MP4_ITMF_BT_PNG',
           'MP4_CLOCK_TRACK_TYPE', '__ssize_t', '__getdelim',
           'MP4MakeIsmaCompliant', 'MP4_ITMF_BT_HTML', 'int16_t',
           'MP4SetAmrModeSet', 'MP4_MPEG4_AAC_LC_AUDIO_TYPE',
           'MP4TagTrack_s', 'MP4TagsSetEncodedBy', 'MP4AddTrack',
           '__warnattr', 'MP4V2_PROJECT_url_downloads',
           'MP4_VIDEO_TRACK_TYPE', '_sys_errlist',
           'MP4TagsSetKeywords', '_IO_seekpos', 'funlockfile',
           'MP4GetHintTrackSdp', 'cookie_read_function_t', '_IO_padn',
           'MP4AddAmrAudioTrack', '_FEATURES_H',
           'MP4AddH264PictureParameterSet',
           'MP4_MPEG2_AAC_AUDIO_TYPE', '__USE_XOPEN2K',
           'MP4TagsSetName', 'MP4GetSampleSize', 'MPEG4_MP_L2',
           '__overflow', 'MP4GetChapters', 'MP4_CREATE_64BIT_DATA',
           'MPEG4_MP_L3', 'MP4V2_PROJECT_version_minor',
           'MPEG4_MP_L4', '__FD_SETSIZE', 'ungetc', 'MP4_LOG_INFO',
           '__intptr_t', 'tmpnam_r', 'MP4ConvertFromTrackTimestamp',
           '_IO_LINKED', 'vsnprintf', '_IO_FILE_plus',
           'MP4AddSubtitleTrack', '_IO_va_list',
           'MP4ChangeMovieTimeScale', '__blkcnt_t',
           'MP4ItmfDataList_s', '_IO_size_t',
           'MP4_INVALID_AUDIO_TYPE', 'MP4FindTrackIndex', 'fwrite',
           'MP4TagsSetCompilation',
           'MP4_MPEG4_AAC_SCALABLE_AUDIO_TYPE', 'INT64_C',
           '_IO_flockfile', 'INT16_C', 'MP4GetTrackVideoHeight',
           '_IOS_INPUT', 'vasprintf', 'MP4GetTrackH264ProfileLevel',
           'L_tmpnam', 'MP4SetTrackEditDuration', '_IO_DONT_CLOSE',
           'MP4TagsSetComments', 'MPEG4_ACEP_L4', 'MPEG4_ACEP_L3',
           'MPEG4_ACEP_L2', 'MPEG4_ACEP_L1', 'MP4LogGetLevel',
           'sys_nerr', '_IO_BAD_SEEN', '__USE_MISC',
           'MP4SampleDependencyType', 'MP4_MPEG4_AAC_LTP_AUDIO_TYPE',
           'puts', 'MP4GetTrackESConfiguration', 'obstack',
           'N11__mbstate_t3DOT_2E', 'MP4AddVideoTrack', 'va_arg',
           'MP4_SUBTITLE_TRACK_TYPE', 'putc', 'MP4_H263_VIDEO_TYPE',
           'MP4GetRtpPacketBFrame', 'MP4_IS_MPEG4_VIDEO_TYPE',
           'MP4TagsSetSortAlbumArtist', '_IO_HEX', 'MP4TagsFree',
           'MP4AddIPodUUID', 'MP4SetTrackEditDwell', '_STDINT_H',
           'MP4_NANOSECONDS_TIME_SCALE', 'tmpnam',
           'MP4GetTrackStringProperty', 'MP4GetFloatProperty',
           '__dev_t', 'MP4V2_PROJECT_url_website', 'MP4Optimize',
           'MP4LogCallback', '_IO_HAVE_SYS_WAIT', 'FILENAME_MAX',
           'L_cuserid', 'MP4ItmfAddItem', 'MP4_LOG_WARNING',
           'MP4CreateEx', 'MP4SetTrackTimeScale', '__suseconds_t',
           'MP4_SDT_EARLIER_DISPLAY_TIMES_ALLOWED',
           'MP4_MPEG4_LAYER1_AUDIO_TYPE', 'MP4ItmfItemFree',
           'MP4TagArtworkType', 'MP4ItmfItemListFree', 'vsscanf',
           'MP4_MPEG2_SIMPLE_VIDEO_TYPE', 'vsprintf', 'rename',
           '__USE_POSIX199506', 'stdout', 'MP4Create', 'uint64_t',
           'MPEG4_SP_L3', 'MPEG4_SP_L2', 'MPEG4_SP_L1', 'MPEG4_SP_L0',
           '_IO_uid_t', 'MP4_SCENE_TRACK_TYPE', '__WCHAR_MAX',
           'int_fast16_t', 'MP4Modify', 'MP4_YUV12_VIDEO_TYPE',
           'INT32_C', 'MP4_NSECS_TIME_SCALE', 'MP4TagsAlloc',
           '__rlim_t', 'MP4ItmfItemAlloc', 'MP4AddRtpImmediateData',
           'MP4_IS_VALID_EDIT_ID', 'getc', '__USE_XOPEN2K8XSI',
           'MP4GetTrackIntegerProperty', 'MP4GetTrackBytesProperty',
           'MP4AppendSessionSdp', 'FILEMODE_CREATE', '_G_size_t',
           'gets', '_SYS_CDEFS_H', 'MP4GetTrackBitRate',
           '_OLD_STDIO_MAGIC', 'fread_unlocked',
           'MP4_MPEG4_MIDI_AUDIO_TYPE',
           'MP4_MPEG2_AAC_MAIN_AUDIO_TYPE', '_G_pid_t',
           'MP4_SECS_TIME_SCALE', '_IO_IS_FILEBUF', 'SEEK_SET',
           'MP4_USECS_TIME_SCALE', 'MP4GetTrackVideoFrameRate',
           '__io_write_fn', 'MP4TagsSetHDVideo', '_G_HAVE_PRINTF_FP',
           'MP4_ITMF_BT_RIAA_PA',
           'MP4_MPEG4_ALGORITHMIC_FX_AUDIO_TYPE', '_IO_lock_t',
           'MP4_SECONDS_TIME_SCALE', '_IO_2_1_stdout_',
           '__REDIRECT_LDBL', 'MP4ConvertToTrackDuration',
           'MP4TagsSetGenreType', 'MP4GetGraphicsProfileLevel',
           'MP4GetNumberOfTracks', 'uint16_t', '_G_HAVE_BOOL',
           'MP4TagsSetTVShow', 'MP4TagsSetComposer',
           'MP4SetTrackESConfiguration', '__int64_t',
           'FILEMODE_UNDEFINED', 'uint32_t', 'fopen64',
           'MP4_IS_VALID_FILE_HANDLE', '_G_HAVE_SYS_WAIT',
           'MP4ItmfSetItem', 'MP4SetLogCallback', '__USE_XOPEN2KXSI',
           'cookie_write_function_t', 'fread', '_IO_LEFT', '_G_off_t',
           '__fsid_t', 'fflush', 'MP4TagsSetITunesAccountType',
           '_LARGEFILE64_SOURCE', '_IO_MAGIC_MASK', '__uint32_t',
           '__USE_XOPEN2K8', 'MP4SetHintTrackRtpPayload',
           '_G_uint32_t', 'fflush_unlocked', 'MP4AddODTrack',
           'P_tmpdir', '__ino64_t', 'MP4ItmfDataList',
           'MP4GetSampleTime', 'MPEG4_ACP_L2', 'MPEG4_ACP_L1',
           'off64_t', 'MPEG4_STP_L1', '_IO_SHOWPOINT',
           'MP4MakeIsmaSdpIod', '_IO_sgetn', '__STDC_IEC_559__',
           'MP4_JPEG_VIDEO_TYPE', 'MP4_LOG_VERBOSE3',
           'MP4_LOG_VERBOSE2', 'MP4_LOG_VERBOSE1',
           '_IO_FLAGS2_NOTCANCEL', 'va_start', 'MP4_LOG_VERBOSE4',
           'MP4Chapter_t', 'MP4TagsSetDisk', 'MP4ChapterTypeNero',
           '_G_VTABLE_LABEL_PREFIX', 'MP4Chapter_s', 'renameat',
           'MP4ReadSampleFromEditTime', 'MP4Tags',
           'MP4GetTrackAudioMpeg4Type', 'MP4ItmfData_s',
           '_G_fpos64_t', 'popen', 'MP4AddRtpSampleData',
           'MP4GetTrackEditTotalDuration', '_ISOC95_SOURCE',
           'MP4TagsSetComposerID', '_ISOC99_SOURCE', 'freopen',
           '__nlink_t', 'mp4v2_ismacrypParams', 'MP4_OD_TRACK_TYPE',
           'tmpfile', 'MP4ChapterTypeQt', 'tmpfile64',
           '__io_close_fn', 'fgetc', 'MP4_ITMF_BT_MI3P',
           'MP4ReadSample', 'MP4EditId', 'MP4WriteRtpHint',
           'MP4ItmfGetItemsByCode', 'MP4GetFilename',
           'MP4AddAudioTrack', 'MP4SetAmrVendor', 'intmax_t',
           '__pid_t', 'MP4GetTrackNumberOfSamples', '_IO_SHOWPOS',
           '__codecvt_ok', 'fgets', '_IO_MAGIC', 'ctermid', '__id_t',
           'cookie_io_functions_t', 'MP4ItmfItem', '_IO_feof',
           'MP4AddChapterTextTrack', '__SYSCALL_WORDSIZE',
           'MP4V2_PROJECT_repo_rev', 'MP4GetTrackDuration',
           'fgetc_unlocked', 'int_least8_t', '_IO_UPPERCASE',
           'fsetpos', '_IO_EOF_SEEN', '_IO_vfprintf',
           'MP4GetSceneProfileLevel', 'int_least16_t', '_IO_FIXED',
           'MP4GetTrackH264LengthSize', '_SVID_SOURCE', '_G_uint16_t',
           'putw', 'MP4ItmfBasicType_e',
           'MP4_PCM16_LITTLE_ENDIAN_AUDIO_TYPE', 'MP4_ART_UNDEFINED',
           'fcloseall', 'MP4DeleteChapters', 'INT8_C', '_IOFBF',
           'MP4GetTrackEsdsObjectTypeId', 'MPEG4_C_STUDIO_P_L3',
           'MP4_PCM16_BIG_ENDIAN_AUDIO_TYPE', 'MPEG4_C_STUDIO_P_L1',
           'MP4TagsSetReleaseDate', 'SEEK_END', '_IO_peekc',
           'MP4SetH263Bitrates', '__USE_BSD', 'fseek', 'sys_errlist',
           'MP4SetH263DecoderVersion', '__CONCAT',
           'clearerr_unlocked', 'MP4LogLevel', 'MP4_LOG_ERROR',
           '_IO_IN_BACKUP', '_IOS_NOREPLACE', '_ISOC11_SOURCE',
           'tempnam', '____FILE_defined', 'MP4AddH264VideoTrack',
           'MP4GetTrackMediaDataOriginalFormat', 'uint_least64_t',
           'MP4GetBytesProperty', 'MP4GetRtpTimestampStart',
           'MP4V2_PROJECT_name_formal', 'MP4_MPEG4_CELP_AUDIO_TYPE',
           'MP4TagsSetGapless', '__syscall_ulong_t', 'FILEMODE_READ',
           '_IO_STDIO', 'MP4GetTrackFloatProperty', 'MPEG4_ASP_L3B',
           '_IOS_BIN', 'getdelim', '__gid_t', 'fdopen',
           'MP4TagsSetTVEpisodeID', 'MP4SetTrackDurationPerChunk',
           '_IO_OCT', 'MP4IsIsmaCrypMediaTrack', '_IOS_OUTPUT',
           '__daddr_t', '_IO_cookie_file', '__caddr_t',
           'MP4V2_PROJECT_name_lower', 'uintmax_t', 'pclose',
           'MP4GetTrackVideoMetadata', '_STDC_PREDEF_H',
           'MP4TagsStore', 'MP4AddEncAudioTrack', 'vprintf',
           '__io_seek_fn', '__fsword_t', 'UINT64_C', 'MP4CloneTrack',
           'int8_t', 'MP4TagsSetSortArtist', 'BUFSIZ',
           '__STDC_IEC_559_COMPLEX__', 'freopen64', '_IO_getc',
           'MP4TagsSetTempo', '_IO_UNIFIED_JUMPTABLES',
           '_G_HAVE_ATEXIT', 'MP4_ITMF_BT_DATETIME', 'cuserid',
           'MP4SetAmrDecoderVersion', '_IO_vfscanf', '__socklen_t',
           'MP4_SUBPIC_TRACK_TYPE', 'MP4TagsSetITunesAccount',
           'MP4GetTrackType', 'sscanf', 'fileno_unlocked',
           '_IO_2_1_stderr_', '_STDIO_H', 'ftello',
           'MP4SetFloatProperty', 'MP4_MPEGJ_TRACK_TYPE',
           '_IO_FLAGS2_USER_WBUF', '__STRING', 'int64_t',
           'MP4TagsSetTVEpisode', 'ftello64',
           'MP4_INVALID_VIDEO_TYPE', '__WCHAR_MIN',
           'MP4GetTrackH264SeqPictHeaders', 'MP4GetODProfileLevel',
           '__GNUC_PREREQ', 'MP4ItmfData', 'MP4GetTrackEditDwell',
           'MP4_HINT_TRACK_TYPE', '__va_copy', 'MP4TagsSetPodcast',
           '__quad_t', '_IO_NO_READS', 'MP4_G723_AUDIO_TYPE',
           'MP4SetTimeScale', '__u_quad_t', '__u_short',
           'MP4TagsSetGrouping', 'int_fast64_t', 'vfscanf', '__key_t',
           'MP4AddH264SequenceParameterSet',
           'MP4_MPEG2_AAC_LC_AUDIO_TYPE', 'MP4_ITMF_BT_UTF8',
           'MPEG4_SFAP_L2', '__va_arg_pack', 'MP4_MPEG1_VIDEO_TYPE',
           '__codecvt_error', 'MP4Close', '_G_NEED_STDARG_H',
           'MP4TagsHasMetadata', '__va_arg_pack_len', '__bos0',
           'MP4_ITMF_BT_GENRES', 'MP4ChapterType',
           'MP4V2_PROJECT_repo_date', 'MP4_MPEG2_442_VIDEO_TYPE',
           'int_least32_t', 'uint_fast32_t',
           'MP4DefaultISMACrypParams', 'MP4_INVALID_EDIT_ID',
           'MP4_MPEG4_AAC_SSR_AUDIO_TYPE', '__USE_ISOC11',
           'MP4TagsSetSortComposer', 'MP4_ITMF_BT_JPEG',
           '__codecvt_noconv', '_IOLBF', '_G_int32_t', 'offsetof',
           'FILEMODE_MODIFY']
