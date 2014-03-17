from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/usr/lib/libmagic.so'] = CDLL('/usr/lib/libmagic.so')


# __SYSCALL_SLONG_TYPE = __SLONGWORD_TYPE # alias
# __FSWORD_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def __LONG_LONG_PAIR(HI,LO): return LO, HI # macro
def __P(args): return args # macro
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
# def __LDBL_REDIR(name,proto): return name proto # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
# def __FD_ZERO(fdsp): return do { int __d0, __d1; __asm__ __volatile__ ("cld; rep; " __FD_ZERO_STOS : "=c" (__d0), "=D" (__d1) : "a" (0), "0" (sizeof (fd_set) / sizeof (__fd_mask)), "1" (&__FDS_BITS (fdsp)[0]) : "memory"); } while (0) # macro
# def __FD_MASK(d): return ((__fd_mask) 1 << ((d) % __NFDBITS)) # macro
def __FD_ISSET(d,set): return ((__FDS_BITS (set)[__FD_ELT (d)] & __FD_MASK (d)) != 0) # macro
# def __FD_ELT(d): return __extension__ ({ long int __d = (d); (__builtin_constant_p (__d) ? (0 <= __d && __d < __FD_SETSIZE ? (__d / __NFDBITS) : __fdelt_warn (__d)) : __fdelt_chk (__d)); }) # macro
# def __FD_CLR(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] &= ~__FD_MASK (d))) # macro
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def FD_ISSET(fd,fdsetp): return __FD_ISSET (fd, fdsetp) # macro
def FD_CLR(fd,fdsetp): return __FD_CLR (fd, fdsetp) # macro
# __SYSCALL_ULONG_TYPE = __ULONGWORD_TYPE # alias
# __FSBLKCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
__BYTE_ORDER = __LITTLE_ENDIAN # alias
__FLOAT_WORD_ORDER = __BYTE_ORDER # alias
# def __intN_t(N,MODE): return typedef int int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
# __CLOCK_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def __FD_SET(d,set): return ((void) (__FDS_BITS (set)[__FD_ELT (d)] |= __FD_MASK (d))) # macro
# __S32_TYPE = int # alias
# __CLOCKID_T_TYPE = __S32_TYPE # alias
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
# __BLKCNT_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __BLKSIZE_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
# __ID_T_TYPE = __U32_TYPE # alias
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp) # macro
def FD_SET(fd,fdsetp): return __FD_SET (fd, fdsetp) # macro
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
LITTLE_ENDIAN = __LITTLE_ENDIAN # alias
def __CONCAT(x,y): return x ## y # macro
# def __FDS_BITS(set): return ((set)->fds_bits) # macro
def __bswap_constant_32(x): return ((((x) & 0xff000000) >> 24) | (((x) & 0x00ff0000) >> 8) | (((x) & 0x0000ff00) << 8) | (((x) & 0x000000ff) << 24)) # macro
# __RLIM_T_TYPE = __SYSCALL_ULONG_TYPE # alias
def minor(dev): return gnu_dev_minor (dev) # macro
def major(dev): return gnu_dev_major (dev) # macro
# def __bswap_16(x): return (__extension__ ({ unsigned short int __v, __x = (unsigned short int) (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_16 (__x); else __asm__ ("rorw $8, %w0" : "=r" (__v) : "0" (__x) : "cc"); __v; })) # macro
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
def le32toh(x): return (x) # macro
def htole64(x): return (x) # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
# __PID_T_TYPE = __S32_TYPE # alias
# __wur = __attribute_warn_unused_result__ # alias
def htobe32(x): return __bswap_32 (x) # macro
def be32toh(x): return __bswap_32 (x) # macro
def be16toh(x): return __bswap_16 (x) # macro
# __USECONDS_T_TYPE = __U32_TYPE # alias
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
def le64toh(x): return (x) # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
__NFDBITS = 64 # Variable c_int '64'
NFDBITS = __NFDBITS # alias
# def __u_intN_t(N,MODE): return typedef unsigned int u_int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
# __TIME_T_TYPE = __SYSCALL_SLONG_TYPE # alias
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
# __UID_T_TYPE = __U32_TYPE # alias
# def __bswap_constant_64(x): return (__extension__ ((((x) & 0xff00000000000000ull) >> 56) | (((x) & 0x00ff000000000000ull) >> 40) | (((x) & 0x0000ff0000000000ull) >> 24) | (((x) & 0x000000ff00000000ull) >> 8) | (((x) & 0x00000000ff000000ull) << 8) | (((x) & 0x0000000000ff0000ull) << 24) | (((x) & 0x000000000000ff00ull) << 40) | (((x) & 0x00000000000000ffull) << 56))) # macro
# __SLONG32_TYPE = int # alias
# __SUSECONDS_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# def __bswap_constant_16(x): return ((unsigned short int) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8))) # macro
# __OFF_T_TYPE = __SYSCALL_SLONG_TYPE # alias
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
# __MODE_T_TYPE = __U32_TYPE # alias
# __KEY_T_TYPE = __S32_TYPE # alias
# __INO_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __NLINK_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __INO64_T_TYPE = __UQUAD_TYPE # alias
# __GID_T_TYPE = __U32_TYPE # alias
# __FSFILCNT_T_TYPE = __SYSCALL_ULONG_TYPE # alias
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
# __DEV_T_TYPE = __UQUAD_TYPE # alias
# __DADDR_T_TYPE = __S32_TYPE # alias
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
__PDP_ENDIAN = 3412 # Variable c_int '3412'
PDP_ENDIAN = __PDP_ENDIAN # alias
MAGIC_NO_CHECK_TEXT = 131072 # Variable c_int '131072'
MAGIC_NO_CHECK_ASCII = MAGIC_NO_CHECK_TEXT # alias
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
BYTE_ORDER = __BYTE_ORDER # alias
__BIG_ENDIAN = 4321 # Variable c_int '4321'
BIG_ENDIAN = __BIG_ENDIAN # alias
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
def makedev(maj,min): return gnu_dev_makedev (maj, min) # macro
def le16toh(x): return (x) # macro
def htole32(x): return (x) # macro
__FD_SETSIZE = 1024 # Variable c_int '1024'
FD_SETSIZE = __FD_SETSIZE # alias
def htole16(x): return (x) # macro
def htobe64(x): return __bswap_64 (x) # macro
def htobe16(x): return __bswap_16 (x) # macro
def be64toh(x): return __bswap_64 (x) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
def __STRING(x): return #x # macro
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
def __PMT(args): return args # macro
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIERATTR_T = 4 # Variable c_int '4'
__have_pthread_attr_t = 1 # Variable c_int '1'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
__USE_XOPEN = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
MAGIC_PRESERVE_ATIME = 128 # Variable c_int '128'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
_STRUCT_TIMEVAL = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_RWLOCKATTR_T = 8 # Variable c_int '8'
__SIZEOF_PTHREAD_CONDATTR_T = 4 # Variable c_int '4'
MAGIC_NO_CHECK_COMPRESS = 4096 # Variable c_int '4096'
_BITS_PTHREADTYPES_H = 1 # Variable c_int '1'
MAGIC_NO_CHECK_FORTRAN = 0 # Variable c_int '0'
__USE_ATFILE = 1 # Variable c_int '1'
__time_t_defined = 1 # Variable c_int '1'
MAGIC_NO_CHECK_ELF = 65536 # Variable c_int '65536'
_SYS_SELECT_H = 1 # Variable c_int '1'
MAGIC_COMPRESS = 4 # Variable c_int '4'
__SIZEOF_PTHREAD_MUTEXATTR_T = 4 # Variable c_int '4'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
__USE_POSIX = 1 # Variable c_int '1'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
MAGIC_NO_CHECK_CDF = 262144 # Variable c_int '262144'
__clock_t_defined = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_POSIX199309 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_COND_T = 48 # Variable c_int '48'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 19 # Variable c_int '19'
__clockid_t_defined = 1 # Variable c_int '1'
__timer_t_defined = 1 # Variable c_int '1'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_BARRIER_T = 32 # Variable c_int '32'
_SYS_TYPES_H = 1 # Variable c_int '1'
__timespec_defined = 1 # Variable c_int '1'
__USE_GNU = 1 # Variable c_int '1'
__USE_BSD = 1 # Variable c_int '1'
__USE_ISOC95 = 1 # Variable c_int '1'
MAGIC_CHECK = 64 # Variable c_int '64'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_SIGSET_H_types = 1 # Variable c_int '1'
_ISOC11_SOURCE = 1 # Variable c_int '1'
__PTHREAD_RWLOCK_INT_FLAGS_SHARED = 1 # Variable c_int '1'
__USE_SVID = 1 # Variable c_int '1'
__SIZEOF_PTHREAD_MUTEX_T = 40 # Variable c_int '40'
__USE_UNIX98 = 1 # Variable c_int '1'
__USE_MISC = 1 # Variable c_int '1'
__BIT_TYPES_DEFINED__ = 1 # Variable c_int '1'
MAGIC_MIME_TYPE = 16 # Variable c_int '16'
__PTHREAD_MUTEX_HAVE_ELISION = 1 # Variable c_int '1'
__OFF_T_MATCHES_OFF64_T = 1 # Variable c_int '1'
_ENDIAN_H = 1 # Variable c_int '1'
__PTHREAD_MUTEX_HAVE_PREV = 1 # Variable c_int '1'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_RWLOCK_T = 56 # Variable c_int '56'
_BITS_BYTESWAP_H = 1 # Variable c_int '1'
MAGIC_SYMLINK = 2 # Variable c_int '2'
_SYS_SYSMACROS_H = 1 # Variable c_int '1'
MAGIC_APPLE = 2048 # Variable c_int '2048'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
MAGIC_CONTINUE = 32 # Variable c_int '32'
MAGIC_MIME = 1040 # Variable c_int '1040'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
MAGIC_NO_CHECK_TROFF = 0 # Variable c_int '0'
_FEATURES_H = 1 # Variable c_int '1'
MAGIC_NO_CHECK_APPTYPE = 32768 # Variable c_int '32768'
MAGIC_NO_CHECK_BUILTIN = 3649536 # Variable c_int '3649536'
__USE_POSIX199506 = 1 # Variable c_int '1'
_BITS_TYPES_H = 1 # Variable c_int '1'
MAGIC_DEBUG = 1 # Variable c_int '1'
MAGIC_ERROR = 512 # Variable c_int '512'
__INO_T_MATCHES_INO64_T = 1 # Variable c_int '1'
MAGIC_NO_CHECK_SOFT = 16384 # Variable c_int '16384'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
MAGIC_VERSION = 516 # Variable c_int '516'
MAGIC_RAW = 256 # Variable c_int '256'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
MAGIC_NO_CHECK_ENCODING = 2097152 # Variable c_int '2097152'
_SYS_CDEFS_H = 1 # Variable c_int '1'
MAGIC_MIME_ENCODING = 1024 # Variable c_int '1024'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
_XOPEN_SOURCE = 700 # Variable c_int '700'
MAGIC_NO_CHECK_TOKENS = 1048576 # Variable c_int '1048576'
__SIZEOF_PTHREAD_ATTR_T = 56 # Variable c_int '56'
MAGIC_DEVICES = 8 # Variable c_int '8'
_SIGSET_NWORDS = 16 # Variable c_ulong '16ul'
__GLIBC__ = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
MAGIC_NONE = 0 # Variable c_int '0'
__USE_ISOC11 = 1 # Variable c_int '1'
MAGIC_NO_CHECK_TAR = 8192 # Variable c_int '8192'
_BSD_SOURCE = 1 # Variable c_int '1'
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
class N14pthread_cond_t3DOT_6E(Structure):
    pass
N14pthread_cond_t3DOT_6E._fields_ = [
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
    ('__data', N14pthread_cond_t3DOT_6E),
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
class N16pthread_rwlock_t3DOT_9E(Structure):
    pass
N16pthread_rwlock_t3DOT_9E._fields_ = [
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
    ('__data', N16pthread_rwlock_t3DOT_9E),
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
__fdelt_chk = _libraries['/usr/lib/libmagic.so'].__fdelt_chk
__fdelt_chk.restype = c_long
__fdelt_chk.argtypes = [c_long]
__fdelt_warn = _libraries['/usr/lib/libmagic.so'].__fdelt_warn
__fdelt_warn.restype = c_long
__fdelt_warn.argtypes = [c_long]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
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
class magic_set(Structure):
    pass
magic_set._fields_ = [
]
magic_t = POINTER(magic_set)
magic_open = _libraries['/usr/lib/libmagic.so'].magic_open
magic_open.restype = magic_t
magic_open.argtypes = [c_int]
magic_close = _libraries['/usr/lib/libmagic.so'].magic_close
magic_close.restype = None
magic_close.argtypes = [magic_t]
magic_getpath = _libraries['/usr/lib/libmagic.so'].magic_getpath
magic_getpath.restype = STRING
magic_getpath.argtypes = [STRING, c_int]
magic_file = _libraries['/usr/lib/libmagic.so'].magic_file
magic_file.restype = STRING
magic_file.argtypes = [magic_t, STRING]
magic_descriptor = _libraries['/usr/lib/libmagic.so'].magic_descriptor
magic_descriptor.restype = STRING
magic_descriptor.argtypes = [magic_t, c_int]
size_t = c_ulong
magic_buffer = _libraries['/usr/lib/libmagic.so'].magic_buffer
magic_buffer.restype = STRING
magic_buffer.argtypes = [magic_t, c_void_p, size_t]
magic_error = _libraries['/usr/lib/libmagic.so'].magic_error
magic_error.restype = STRING
magic_error.argtypes = [magic_t]
magic_setflags = _libraries['/usr/lib/libmagic.so'].magic_setflags
magic_setflags.restype = c_int
magic_setflags.argtypes = [magic_t, c_int]
magic_version = _libraries['/usr/lib/libmagic.so'].magic_version
magic_version.restype = c_int
magic_version.argtypes = []
magic_load = _libraries['/usr/lib/libmagic.so'].magic_load
magic_load.restype = c_int
magic_load.argtypes = [magic_t, STRING]
magic_compile = _libraries['/usr/lib/libmagic.so'].magic_compile
magic_compile.restype = c_int
magic_compile.argtypes = [magic_t, STRING]
magic_check = _libraries['/usr/lib/libmagic.so'].magic_check
magic_check.restype = c_int
magic_check.argtypes = [magic_t, STRING]
magic_list = _libraries['/usr/lib/libmagic.so'].magic_list
magic_list.restype = c_int
magic_list.argtypes = [magic_t, STRING]
magic_errno = _libraries['/usr/lib/libmagic.so'].magic_errno
magic_errno.restype = c_int
magic_errno.argtypes = [magic_t]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
select = _libraries['/usr/lib/libmagic.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
pselect = _libraries['/usr/lib/libmagic.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/lib/libmagic.so'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/lib/libmagic.so'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/lib/libmagic.so'].gnu_dev_makedev
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
off_t = __off_t
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
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
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
__all__ = ['be16toh', '__pthread_mutex_s', 'le32toh',
           '__USE_XOPEN2KXSI', '_POSIX_C_SOURCE', '__glibc_unlikely',
           '__LITTLE_ENDIAN', '__have_pthread_attr_t',
           '__glibc_likely', '__LONG_LONG_PAIR',
           'N14pthread_cond_t3DOT_6E', '__GNU_LIBRARY__',
           '_BITS_TYPESIZES_H', '__fsid_t', 'mode_t',
           'pthread_mutexattr_t', 'size_t', '__USE_XOPEN',
           '__USE_LARGEFILE64', 'timeval', 'u_int16_t',
           'MAGIC_PRESERVE_ATIME', '__key_t', '__uint32_t',
           '__USE_XOPEN2K8', 'htobe64', '_STRUCT_TIMEVAL',
           '__USE_POSIX2', '__time_t', 'ino_t', 'magic_check',
           'magic_getpath', '__syscall_slong_t', '__WORDSIZE',
           'ino64_t', '__ino64_t', '__SIZEOF_PTHREAD_CONDATTR_T',
           '__pthread_list_t', '__GLIBC_PREREQ', 'makedev',
           'MAGIC_NO_CHECK_TEXT', '__FD_ISSET', '__loff_t',
           'MAGIC_NO_CHECK_COMPRESS', 'id_t', 'blksize_t', 'daddr_t',
           'loff_t', 'LITTLE_ENDIAN', '_BITS_PTHREADTYPES_H',
           'u_char', 'int32_t', 'MAGIC_NO_CHECK_FORTRAN', 'uid_t',
           '__USE_ATFILE', 'u_int64_t', '__time_t_defined',
           '__u_quad_t', 'MAGIC_NO_CHECK_ELF', '__NFDBITS',
           'MAGIC_NO_CHECK_ASCII', '_SYS_SELECT_H', '__ASMNAME',
           'MAGIC_COMPRESS', 'pthread_condattr_t', 'sigset_t',
           'htole32', '__SIZEOF_PTHREAD_MUTEXATTR_T', '_POSIX_SOURCE',
           '_ISOC95_SOURCE', 'useconds_t', '__int32_t',
           '_ISOC99_SOURCE', 'pthread_rwlock_t', 'timer_t',
           '__USE_POSIX', 'fsfilcnt_t', '_SIGSET_H_types',
           'magic_file', 'gnu_dev_makedev', '__int16_t', '__bos',
           'time_t', 'be32toh', '__uint64_t', '_DEFAULT_SOURCE',
           '__ssize_t', 'fd_set', '__nlink_t', 'MAGIC_NO_CHECK_CDF',
           '__off_t', '__fdelt_warn', '__fd_mask', 'u_short',
           '__clock_t_defined', '__pid_t', 'int16_t', 'MAGIC_MIME',
           'ulong', 'u_int32_t', '__warnattr', '__id_t',
           'gnu_dev_major', '__sigset_t', 'MAGIC_NO_CHECK_TROFF',
           '__useconds_t', '__SYSCALL_WORDSIZE', '__GLIBC_MINOR__',
           'clock_t', '__timer_t', '__clockid_t_defined',
           '__fsfilcnt64_t', '__timer_t_defined', '__BYTE_ORDER',
           'magic_open', '_SVID_SOURCE', '__off64_t',
           'magic_descriptor', '__pthread_internal_list',
           '__attribute_format_strfmon__', 'u_int8_t',
           'pthread_barrier_t', '__gid_t', '__SIZEOF_PTHREAD_ATTR_T',
           '__WORDSIZE_TIME64_COMPAT32', 'magic_close', 'fd_mask',
           'magic_buffer', 'magic_t', 'be64toh', '__USE_XOPEN2K',
           'FD_ISSET', '__SIZEOF_PTHREAD_BARRIER_T', '__FD_SETSIZE',
           '_SYS_TYPES_H', '_ENDIAN_H', 'htole16', '__P',
           '__intptr_t', '__u_long', '__qaddr_t',
           '__timespec_defined', 'magic_version', '__USE_GNU',
           'ushort', '__USE_BSD', '_SIGSET_NWORDS', 'htobe16',
           'MAGIC_CHECK', 'pthread_t', 'clockid_t', '__CONCAT',
           'pthread_attr_t', '__attribute_format_arg__', 'caddr_t',
           '__u_int', '__rlim64_t', '__PMT', 'timespec',
           '_LARGEFILE_SOURCE', '__SIZEOF_PTHREAD_BARRIERATTR_T',
           'major', '_ISOC11_SOURCE', 'uint',
           'N16pthread_rwlock_t3DOT_9E', '__mode_t', 'off64_t',
           '__PTHREAD_RWLOCK_INT_FLAGS_SHARED', 'magic_error',
           '__blksize_t', '__syscall_ulong_t', '__USE_SVID',
           'pthread_spinlock_t', '__SIZEOF_PTHREAD_MUTEX_T',
           '__USE_UNIX98', 'pthread_cond_t', 'blkcnt_t', '__USE_MISC',
           'fsblkcnt_t', 'select', '__BIT_TYPES_DEFINED__', 'htole64',
           'u_quad_t', 'magic_compile', 'register_t', '__fsword_t',
           'fsfilcnt64_t', 'magic_set', '__bswap_constant_32',
           '__daddr_t', 'MAGIC_MIME_TYPE', 'le16toh', '_BITS_TYPES_H',
           '__sig_atomic_t', '__PTHREAD_MUTEX_HAVE_ELISION',
           'MAGIC_DEBUG', '_ATFILE_SOURCE', 'fsblkcnt64_t',
           '__quad_t', '__uint8_t', '__PTHREAD_MUTEX_HAVE_PREV',
           '__USE_FORTIFY_LEVEL', '__SIZEOF_PTHREAD_RWLOCK_T',
           '__OFF_T_MATCHES_OFF64_T', 'u_int', 'htobe32', '__caddr_t',
           'magic_load', '__blkcnt64_t', '__dev_t', 'MAGIC_SYMLINK',
           '_XOPEN_SOURCE', 'BIG_ENDIAN', 'off_t', 'gid_t',
           'pthread_barrierattr_t', '_SYS_SYSMACROS_H', 'MAGIC_APPLE',
           '__INO_T_MATCHES_INO64_T', '__USE_XOPEN_EXTENDED',
           '__suseconds_t', '__uint16_t', 'pid_t', 'MAGIC_CONTINUE',
           'quad_t', 'u_long', '__USE_LARGEFILE',
           '__USE_EXTERN_INLINES', '__SIZEOF_PTHREAD_COND_T',
           '_FEATURES_H', 'minor', 'MAGIC_NO_CHECK_APPTYPE',
           '__socklen_t', 'pthread_key_t', 'pthread_once_t',
           'blkcnt64_t', 'gnu_dev_minor', '__REDIRECT_NTH_LDBL',
           'MAGIC_NO_CHECK_BUILTIN', '__USE_POSIX199506', 'FD_SET',
           '__BIG_ENDIAN', '__u_char', 'MAGIC_ERROR', 'pselect',
           'PDP_ENDIAN', '__fsblkcnt_t', 'FD_ZERO', '__STRING',
           'int64_t', 'MAGIC_NO_CHECK_SOFT', 'FD_CLR',
           '__STDC_CONSTANT_MACROS', '__FLOAT_WORD_ORDER', 'le64toh',
           '__GNUC_PREREQ', 'BYTE_ORDER', '__rlim_t', 'nlink_t',
           'MAGIC_VERSION', 'MAGIC_RAW', '_XOPEN_SOURCE_EXTENDED',
           'pthread_mutex_t', '__USE_POSIX199309',
           '__USE_XOPEN2K8XSI', '__SIZEOF_PTHREAD_RWLOCKATTR_T',
           '__PDP_ENDIAN', '__u_short', '__fsblkcnt64_t',
           'MAGIC_NO_CHECK_ENCODING', '_SYS_CDEFS_H',
           'MAGIC_MIME_ENCODING', 'fsid_t', '_LARGEFILE64_SOURCE',
           '__va_arg_pack', 'FD_SETSIZE', '__clockid_t',
           'MAGIC_NO_CHECK_TOKENS', '_BITS_BYTESWAP_H', 'magic_list',
           'MAGIC_DEVICES', 'key_t', '__USE_ISOC95', 'magic_errno',
           '__ino_t', '__va_arg_pack_len', '__fdelt_chk', '__bos0',
           '__GLIBC__', 'pthread_rwlockattr_t', '__REDIRECT_LDBL',
           '__USE_ISOC99', '__blkcnt_t', 'int8_t', 'MAGIC_NONE',
           '__fsfilcnt_t', '__USE_ISOC11', 'suseconds_t',
           'MAGIC_NO_CHECK_TAR', '__int64_t', '_BSD_SOURCE',
           'ssize_t', '__clock_t', 'dev_t', '__uid_t',
           'magic_setflags', '__int8_t', '__FD_ZERO_STOS', 'NFDBITS']
