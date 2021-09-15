r"""Wrapper for ac3_parser.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lavcodec /usr/include/libavcodec/ac3_parser.h /usr/include/libavcodec/adts_parser.h /usr/include/libavcodec/avcodec.h /usr/include/libavcodec/avdct.h /usr/include/libavcodec/avfft.h /usr/include/libavcodec/bsf.h /usr/include/libavcodec/codec_desc.h /usr/include/libavcodec/codec.h /usr/include/libavcodec/codec_id.h /usr/include/libavcodec/codec_par.h /usr/include/libavcodec/d3d11va.h /usr/include/libavcodec/dirac.h /usr/include/libavcodec/dv_profile.h /usr/include/libavcodec/dxva2.h /usr/include/libavcodec/jni.h /usr/include/libavcodec/mediacodec.h /usr/include/libavcodec/packet.h /usr/include/libavcodec/qsv.h /usr/include/libavcodec/vaapi.h /usr/include/libavcodec/vdpau.h /usr/include/libavcodec/version.h /usr/include/libavcodec/videotoolbox.h /usr/include/libavcodec/vorbis_parser.h /usr/include/libavcodec/xvmc.h -L/usr/include/libavutil -o avcodec.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['/usr/include/libavutil']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs(['/usr/include/libavutil'])

# Begin libraries
_libs["avcodec"] = load_library("avcodec")

# 1 libraries
# End libraries

# No modules

# /usr/include/libavcodec/ac3_parser.h: 32
if _libs["avcodec"].has("av_ac3_parse_header", "cdecl"):
    av_ac3_parse_header = _libs["avcodec"].get("av_ac3_parse_header", "cdecl")
    av_ac3_parse_header.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint16)]
    av_ac3_parse_header.restype = c_int

# /usr/include/libavcodec/adts_parser.h: 34
if _libs["avcodec"].has("av_adts_header_parse", "cdecl"):
    av_adts_header_parse = _libs["avcodec"].get("av_adts_header_parse", "cdecl")
    av_adts_header_parse.argtypes = [POINTER(c_uint8), POINTER(c_uint32), POINTER(c_uint8)]
    av_adts_header_parse.restype = c_int

enum_AVMediaType = c_int# /usr/include/libavutil/avutil.h: 199

enum_AVPictureType = c_int# /usr/include/libavutil/avutil.h: 272

# /usr/include/libavutil/rational.h: 61
class struct_AVRational(Structure):
    pass

struct_AVRational.__slots__ = [
    'num',
    'den',
]
struct_AVRational._fields_ = [
    ('num', c_int),
    ('den', c_int),
]

AVRational = struct_AVRational# /usr/include/libavutil/rational.h: 61

enum_anon_25 = c_int# /usr/include/libavutil/log.h: 48

AVClassCategory = enum_anon_25# /usr/include/libavutil/log.h: 48

# /usr/include/libavutil/opt.h: 333
class struct_AVOptionRanges(Structure):
    pass

# /usr/include/libavutil/opt.h: 248
class struct_AVOption(Structure):
    pass

# /usr/include/libavutil/log.h: 67
class struct_AVClass(Structure):
    pass

struct_AVClass.__slots__ = [
    'class_name',
    'item_name',
    'option',
    'version',
    'log_level_offset_offset',
    'parent_log_context_offset',
    'child_next',
    'child_class_next',
    'category',
    'get_category',
    'query_ranges',
    'child_class_iterate',
]
struct_AVClass._fields_ = [
    ('class_name', String),
    ('item_name', CFUNCTYPE(UNCHECKED(c_char_p), POINTER(None))),
    ('option', POINTER(struct_AVOption)),
    ('version', c_int),
    ('log_level_offset_offset', c_int),
    ('parent_log_context_offset', c_int),
    ('child_next', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), POINTER(None))),
    ('child_class_next', CFUNCTYPE(UNCHECKED(POINTER(struct_AVClass)), POINTER(struct_AVClass))),
    ('category', AVClassCategory),
    ('get_category', CFUNCTYPE(UNCHECKED(AVClassCategory), POINTER(None))),
    ('query_ranges', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_AVOptionRanges)), POINTER(None), String, c_int)),
    ('child_class_iterate', CFUNCTYPE(UNCHECKED(POINTER(struct_AVClass)), POINTER(POINTER(None)))),
]

AVClass = struct_AVClass# /usr/include/libavutil/log.h: 161

enum_AVPixelFormat = c_int# /usr/include/libavutil/pixfmt.h: 64

enum_AVColorPrimaries = c_int# /usr/include/libavutil/pixfmt.h: 458

enum_AVColorTransferCharacteristic = c_int# /usr/include/libavutil/pixfmt.h: 483

enum_AVColorSpace = c_int# /usr/include/libavutil/pixfmt.h: 512

enum_AVColorRange = c_int# /usr/include/libavutil/pixfmt.h: 551

enum_AVChromaLocation = c_int# /usr/include/libavutil/pixfmt.h: 605

enum_AVSampleFormat = c_int# /usr/include/libavutil/samplefmt.h: 58

# /usr/include/libavutil/buffer.h: 76
class struct_AVBuffer(Structure):
    pass

AVBuffer = struct_AVBuffer# /usr/include/libavutil/buffer.h: 76

# /usr/include/libavutil/buffer.h: 101
class struct_AVBufferRef(Structure):
    pass

struct_AVBufferRef.__slots__ = [
    'buffer',
    'data',
    'size',
]
struct_AVBufferRef._fields_ = [
    ('buffer', POINTER(AVBuffer)),
    ('data', POINTER(c_uint8)),
    ('size', c_int),
]

AVBufferRef = struct_AVBufferRef# /usr/include/libavutil/buffer.h: 101

# /usr/include/libavutil/dict.h: 86
class struct_AVDictionary(Structure):
    pass

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 86

enum_AVFrameSideDataType = c_int# /usr/include/libavutil/frame.h: 48

# /usr/include/libavutil/frame.h: 230
class struct_AVFrameSideData(Structure):
    pass

struct_AVFrameSideData.__slots__ = [
    'type',
    'data',
    'size',
    'metadata',
    'buf',
]
struct_AVFrameSideData._fields_ = [
    ('type', enum_AVFrameSideDataType),
    ('data', POINTER(c_uint8)),
    ('size', c_int),
    ('metadata', POINTER(AVDictionary)),
    ('buf', POINTER(AVBufferRef)),
]

AVFrameSideData = struct_AVFrameSideData# /usr/include/libavutil/frame.h: 230

# /usr/include/libavutil/frame.h: 698
class struct_AVFrame(Structure):
    pass

struct_AVFrame.__slots__ = [
    'data',
    'linesize',
    'extended_data',
    'width',
    'height',
    'nb_samples',
    'format',
    'key_frame',
    'pict_type',
    'sample_aspect_ratio',
    'pts',
    'pkt_pts',
    'pkt_dts',
    'coded_picture_number',
    'display_picture_number',
    'quality',
    'opaque',
    'error',
    'repeat_pict',
    'interlaced_frame',
    'top_field_first',
    'palette_has_changed',
    'reordered_opaque',
    'sample_rate',
    'channel_layout',
    'buf',
    'extended_buf',
    'nb_extended_buf',
    'side_data',
    'nb_side_data',
    'flags',
    'color_range',
    'color_primaries',
    'color_trc',
    'colorspace',
    'chroma_location',
    'best_effort_timestamp',
    'pkt_pos',
    'pkt_duration',
    'metadata',
    'decode_error_flags',
    'channels',
    'pkt_size',
    'qscale_table',
    'qstride',
    'qscale_type',
    'qp_table_buf',
    'hw_frames_ctx',
    'opaque_ref',
    'crop_top',
    'crop_bottom',
    'crop_left',
    'crop_right',
    'private_ref',
]
struct_AVFrame._fields_ = [
    ('data', POINTER(c_uint8) * int(8)),
    ('linesize', c_int * int(8)),
    ('extended_data', POINTER(POINTER(c_uint8))),
    ('width', c_int),
    ('height', c_int),
    ('nb_samples', c_int),
    ('format', c_int),
    ('key_frame', c_int),
    ('pict_type', enum_AVPictureType),
    ('sample_aspect_ratio', AVRational),
    ('pts', c_int64),
    ('pkt_pts', c_int64),
    ('pkt_dts', c_int64),
    ('coded_picture_number', c_int),
    ('display_picture_number', c_int),
    ('quality', c_int),
    ('opaque', POINTER(None)),
    ('error', c_uint64 * int(8)),
    ('repeat_pict', c_int),
    ('interlaced_frame', c_int),
    ('top_field_first', c_int),
    ('palette_has_changed', c_int),
    ('reordered_opaque', c_int64),
    ('sample_rate', c_int),
    ('channel_layout', c_uint64),
    ('buf', POINTER(AVBufferRef) * int(8)),
    ('extended_buf', POINTER(POINTER(AVBufferRef))),
    ('nb_extended_buf', c_int),
    ('side_data', POINTER(POINTER(AVFrameSideData))),
    ('nb_side_data', c_int),
    ('flags', c_int),
    ('color_range', enum_AVColorRange),
    ('color_primaries', enum_AVColorPrimaries),
    ('color_trc', enum_AVColorTransferCharacteristic),
    ('colorspace', enum_AVColorSpace),
    ('chroma_location', enum_AVChromaLocation),
    ('best_effort_timestamp', c_int64),
    ('pkt_pos', c_int64),
    ('pkt_duration', c_int64),
    ('metadata', POINTER(AVDictionary)),
    ('decode_error_flags', c_int),
    ('channels', c_int),
    ('pkt_size', c_int),
    ('qscale_table', POINTER(c_int8)),
    ('qstride', c_int),
    ('qscale_type', c_int),
    ('qp_table_buf', POINTER(AVBufferRef)),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('opaque_ref', POINTER(AVBufferRef)),
    ('crop_top', c_size_t),
    ('crop_bottom', c_size_t),
    ('crop_left', c_size_t),
    ('crop_right', c_size_t),
    ('private_ref', POINTER(AVBufferRef)),
]

AVFrame = struct_AVFrame# /usr/include/libavutil/frame.h: 698

enum_AVHWDeviceType = c_int# /usr/include/libavutil/hwcontext.h: 27

enum_AVCodecID = c_int# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_NONE = 0# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEG1VIDEO = (AV_CODEC_ID_NONE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEG2VIDEO = (AV_CODEC_ID_MPEG1VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_H261 = (AV_CODEC_ID_MPEG2VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_H263 = (AV_CODEC_ID_H261 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RV10 = (AV_CODEC_ID_H263 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RV20 = (AV_CODEC_ID_RV10 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MJPEG = (AV_CODEC_ID_RV20 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MJPEGB = (AV_CODEC_ID_MJPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_LJPEG = (AV_CODEC_ID_MJPEGB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SP5X = (AV_CODEC_ID_LJPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_JPEGLS = (AV_CODEC_ID_SP5X + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEG4 = (AV_CODEC_ID_JPEGLS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RAWVIDEO = (AV_CODEC_ID_MPEG4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V1 = (AV_CODEC_ID_RAWVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V2 = (AV_CODEC_ID_MSMPEG4V1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V3 = (AV_CODEC_ID_MSMPEG4V2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMV1 = (AV_CODEC_ID_MSMPEG4V3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMV2 = (AV_CODEC_ID_WMV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_H263P = (AV_CODEC_ID_WMV2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_H263I = (AV_CODEC_ID_H263P + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FLV1 = (AV_CODEC_ID_H263I + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SVQ1 = (AV_CODEC_ID_FLV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SVQ3 = (AV_CODEC_ID_SVQ1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVVIDEO = (AV_CODEC_ID_SVQ3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HUFFYUV = (AV_CODEC_ID_DVVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CYUV = (AV_CODEC_ID_HUFFYUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_H264 = (AV_CODEC_ID_CYUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INDEO3 = (AV_CODEC_ID_H264 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP3 = (AV_CODEC_ID_INDEO3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_THEORA = (AV_CODEC_ID_VP3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ASV1 = (AV_CODEC_ID_THEORA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ASV2 = (AV_CODEC_ID_ASV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FFV1 = (AV_CODEC_ID_ASV2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_4XM = (AV_CODEC_ID_FFV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VCR1 = (AV_CODEC_ID_4XM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CLJR = (AV_CODEC_ID_VCR1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MDEC = (AV_CODEC_ID_CLJR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ROQ = (AV_CODEC_ID_MDEC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_VIDEO = (AV_CODEC_ID_ROQ + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XAN_WC3 = (AV_CODEC_ID_INTERPLAY_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XAN_WC4 = (AV_CODEC_ID_XAN_WC3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RPZA = (AV_CODEC_ID_XAN_WC4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CINEPAK = (AV_CODEC_ID_RPZA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WS_VQA = (AV_CODEC_ID_CINEPAK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSRLE = (AV_CODEC_ID_WS_VQA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSVIDEO1 = (AV_CODEC_ID_MSRLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IDCIN = (AV_CODEC_ID_MSVIDEO1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_8BPS = (AV_CODEC_ID_IDCIN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMC = (AV_CODEC_ID_8BPS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FLIC = (AV_CODEC_ID_SMC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION1 = (AV_CODEC_ID_FLIC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VMDVIDEO = (AV_CODEC_ID_TRUEMOTION1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSZH = (AV_CODEC_ID_VMDVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ZLIB = (AV_CODEC_ID_MSZH + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QTRLE = (AV_CODEC_ID_ZLIB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TSCC = (AV_CODEC_ID_QTRLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ULTI = (AV_CODEC_ID_TSCC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QDRAW = (AV_CODEC_ID_ULTI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VIXL = (AV_CODEC_ID_QDRAW + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QPEG = (AV_CODEC_ID_VIXL + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PNG = (AV_CODEC_ID_QPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PPM = (AV_CODEC_ID_PNG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PBM = (AV_CODEC_ID_PPM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PGM = (AV_CODEC_ID_PBM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PGMYUV = (AV_CODEC_ID_PGM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PAM = (AV_CODEC_ID_PGMYUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FFVHUFF = (AV_CODEC_ID_PAM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RV30 = (AV_CODEC_ID_FFVHUFF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RV40 = (AV_CODEC_ID_RV30 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VC1 = (AV_CODEC_ID_RV40 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMV3 = (AV_CODEC_ID_VC1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_LOCO = (AV_CODEC_ID_WMV3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WNV1 = (AV_CODEC_ID_LOCO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AASC = (AV_CODEC_ID_WNV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INDEO2 = (AV_CODEC_ID_AASC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FRAPS = (AV_CODEC_ID_INDEO2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION2 = (AV_CODEC_ID_FRAPS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BMP = (AV_CODEC_ID_TRUEMOTION2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CSCD = (AV_CODEC_ID_BMP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MMVIDEO = (AV_CODEC_ID_CSCD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ZMBV = (AV_CODEC_ID_MMVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVS = (AV_CODEC_ID_ZMBV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMACKVIDEO = (AV_CODEC_ID_AVS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_NUV = (AV_CODEC_ID_SMACKVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_KMVC = (AV_CODEC_ID_NUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FLASHSV = (AV_CODEC_ID_KMVC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CAVS = (AV_CODEC_ID_FLASHSV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_JPEG2000 = (AV_CODEC_ID_CAVS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VMNC = (AV_CODEC_ID_JPEG2000 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP5 = (AV_CODEC_ID_VMNC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP6 = (AV_CODEC_ID_VP5 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP6F = (AV_CODEC_ID_VP6 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TARGA = (AV_CODEC_ID_VP6F + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSICINVIDEO = (AV_CODEC_ID_TARGA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TIERTEXSEQVIDEO = (AV_CODEC_ID_DSICINVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TIFF = (AV_CODEC_ID_TIERTEXSEQVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_GIF = (AV_CODEC_ID_TIFF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DXA = (AV_CODEC_ID_GIF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DNXHD = (AV_CODEC_ID_DXA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_THP = (AV_CODEC_ID_DNXHD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SGI = (AV_CODEC_ID_THP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_C93 = (AV_CODEC_ID_SGI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BETHSOFTVID = (AV_CODEC_ID_C93 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PTX = (AV_CODEC_ID_BETHSOFTVID + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TXD = (AV_CODEC_ID_PTX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP6A = (AV_CODEC_ID_TXD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AMV = (AV_CODEC_ID_VP6A + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VB = (AV_CODEC_ID_AMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCX = (AV_CODEC_ID_VB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SUNRAST = (AV_CODEC_ID_PCX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INDEO4 = (AV_CODEC_ID_SUNRAST + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INDEO5 = (AV_CODEC_ID_INDEO4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MIMIC = (AV_CODEC_ID_INDEO5 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RL2 = (AV_CODEC_ID_MIMIC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ESCAPE124 = (AV_CODEC_ID_RL2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DIRAC = (AV_CODEC_ID_ESCAPE124 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BFI = (AV_CODEC_ID_DIRAC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CMV = (AV_CODEC_ID_BFI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MOTIONPIXELS = (AV_CODEC_ID_CMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TGV = (AV_CODEC_ID_MOTIONPIXELS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TGQ = (AV_CODEC_ID_TGV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TQI = (AV_CODEC_ID_TGQ + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AURA = (AV_CODEC_ID_TQI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AURA2 = (AV_CODEC_ID_AURA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_V210X = (AV_CODEC_ID_AURA2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TMV = (AV_CODEC_ID_V210X + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_V210 = (AV_CODEC_ID_TMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DPX = (AV_CODEC_ID_V210 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MAD = (AV_CODEC_ID_DPX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FRWU = (AV_CODEC_ID_MAD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FLASHSV2 = (AV_CODEC_ID_FRWU + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CDGRAPHICS = (AV_CODEC_ID_FLASHSV2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_R210 = (AV_CODEC_ID_CDGRAPHICS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ANM = (AV_CODEC_ID_R210 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BINKVIDEO = (AV_CODEC_ID_ANM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IFF_ILBM = (AV_CODEC_ID_BINKVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_KGV1 = (AV_CODEC_ID_IFF_ILBM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_YOP = (AV_CODEC_ID_KGV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP8 = (AV_CODEC_ID_YOP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PICTOR = (AV_CODEC_ID_VP8 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ANSI = (AV_CODEC_ID_PICTOR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_A64_MULTI = (AV_CODEC_ID_ANSI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_A64_MULTI5 = (AV_CODEC_ID_A64_MULTI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_R10K = (AV_CODEC_ID_A64_MULTI5 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MXPEG = (AV_CODEC_ID_R10K + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_LAGARITH = (AV_CODEC_ID_MXPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PRORES = (AV_CODEC_ID_LAGARITH + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_JV = (AV_CODEC_ID_PRORES + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DFA = (AV_CODEC_ID_JV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMV3IMAGE = (AV_CODEC_ID_DFA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VC1IMAGE = (AV_CODEC_ID_WMV3IMAGE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_UTVIDEO = (AV_CODEC_ID_VC1IMAGE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BMV_VIDEO = (AV_CODEC_ID_UTVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VBLE = (AV_CODEC_ID_BMV_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DXTORY = (AV_CODEC_ID_VBLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_V410 = (AV_CODEC_ID_DXTORY + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XWD = (AV_CODEC_ID_V410 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CDXL = (AV_CODEC_ID_XWD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XBM = (AV_CODEC_ID_CDXL + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ZEROCODEC = (AV_CODEC_ID_XBM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSS1 = (AV_CODEC_ID_ZEROCODEC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSA1 = (AV_CODEC_ID_MSS1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TSCC2 = (AV_CODEC_ID_MSA1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MTS2 = (AV_CODEC_ID_TSCC2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CLLC = (AV_CODEC_ID_MTS2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSS2 = (AV_CODEC_ID_CLLC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP9 = (AV_CODEC_ID_MSS2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AIC = (AV_CODEC_ID_VP9 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ESCAPE130 = (AV_CODEC_ID_AIC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_G2M = (AV_CODEC_ID_ESCAPE130 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WEBP = (AV_CODEC_ID_G2M + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HNM4_VIDEO = (AV_CODEC_ID_WEBP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HEVC = (AV_CODEC_ID_HNM4_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FIC = (AV_CODEC_ID_HEVC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ALIAS_PIX = (AV_CODEC_ID_FIC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BRENDER_PIX = (AV_CODEC_ID_ALIAS_PIX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PAF_VIDEO = (AV_CODEC_ID_BRENDER_PIX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_EXR = (AV_CODEC_ID_PAF_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP7 = (AV_CODEC_ID_EXR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SANM = (AV_CODEC_ID_VP7 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SGIRLE = (AV_CODEC_ID_SANM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MVC1 = (AV_CODEC_ID_SGIRLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MVC2 = (AV_CODEC_ID_MVC1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HQX = (AV_CODEC_ID_MVC2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TDSC = (AV_CODEC_ID_HQX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HQ_HQA = (AV_CODEC_ID_TDSC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HAP = (AV_CODEC_ID_HQ_HQA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DDS = (AV_CODEC_ID_HAP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DXV = (AV_CODEC_ID_DDS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SCREENPRESSO = (AV_CODEC_ID_DXV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RSCC = (AV_CODEC_ID_SCREENPRESSO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVS2 = (AV_CODEC_ID_RSCC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PGX = (AV_CODEC_ID_AVS2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVS3 = (AV_CODEC_ID_PGX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSP2 = (AV_CODEC_ID_AVS3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VVC = (AV_CODEC_ID_MSP2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_Y41P = 32768# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVRP = (AV_CODEC_ID_Y41P + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_012V = (AV_CODEC_ID_AVRP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVUI = (AV_CODEC_ID_012V + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AYUV = (AV_CODEC_ID_AVUI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TARGA_Y216 = (AV_CODEC_ID_AYUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_V308 = (AV_CODEC_ID_TARGA_Y216 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_V408 = (AV_CODEC_ID_V308 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_YUV4 = (AV_CODEC_ID_V408 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AVRN = (AV_CODEC_ID_YUV4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CPIA = (AV_CODEC_ID_AVRN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XFACE = (AV_CODEC_ID_CPIA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SNOW = (AV_CODEC_ID_XFACE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMVJPEG = (AV_CODEC_ID_SNOW + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_APNG = (AV_CODEC_ID_SMVJPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DAALA = (AV_CODEC_ID_APNG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CFHD = (AV_CODEC_ID_DAALA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION2RT = (AV_CODEC_ID_CFHD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_M101 = (AV_CODEC_ID_TRUEMOTION2RT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MAGICYUV = (AV_CODEC_ID_M101 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SHEERVIDEO = (AV_CODEC_ID_MAGICYUV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_YLC = (AV_CODEC_ID_SHEERVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PSD = (AV_CODEC_ID_YLC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PIXLET = (AV_CODEC_ID_PSD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SPEEDHQ = (AV_CODEC_ID_PIXLET + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FMVC = (AV_CODEC_ID_SPEEDHQ + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SCPR = (AV_CODEC_ID_FMVC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CLEARVIDEO = (AV_CODEC_ID_SCPR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XPM = (AV_CODEC_ID_CLEARVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AV1 = (AV_CODEC_ID_XPM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BITPACKED = (AV_CODEC_ID_AV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MSCC = (AV_CODEC_ID_BITPACKED + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SRGC = (AV_CODEC_ID_MSCC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SVG = (AV_CODEC_ID_SRGC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_GDV = (AV_CODEC_ID_SVG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FITS = (AV_CODEC_ID_GDV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IMM4 = (AV_CODEC_ID_FITS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PROSUMER = (AV_CODEC_ID_IMM4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MWSC = (AV_CODEC_ID_PROSUMER + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WCMV = (AV_CODEC_ID_MWSC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RASC = (AV_CODEC_ID_WCMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HYMT = (AV_CODEC_ID_RASC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ARBC = (AV_CODEC_ID_HYMT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AGM = (AV_CODEC_ID_ARBC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_LSCR = (AV_CODEC_ID_AGM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VP4 = (AV_CODEC_ID_LSCR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IMM5 = (AV_CODEC_ID_VP4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MVDV = (AV_CODEC_ID_IMM5 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MVHA = (AV_CODEC_ID_MVDV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CDTOONS = (AV_CODEC_ID_MVHA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MV30 = (AV_CODEC_ID_CDTOONS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_NOTCHLC = (AV_CODEC_ID_MV30 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PFM = (AV_CODEC_ID_NOTCHLC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MOBICLIP = (AV_CODEC_ID_PFM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PHOTOCD = (AV_CODEC_ID_MOBICLIP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IPU = (AV_CODEC_ID_PHOTOCD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ARGO = (AV_CODEC_ID_IPU + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CRI = (AV_CODEC_ID_ARGO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SIMBIOSIS_IMX = (AV_CODEC_ID_CRI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SGA_VIDEO = (AV_CODEC_ID_SIMBIOSIS_IMX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FIRST_AUDIO = 65536# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S16LE = 65536# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S16BE = (AV_CODEC_ID_PCM_S16LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U16LE = (AV_CODEC_ID_PCM_S16BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U16BE = (AV_CODEC_ID_PCM_U16LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S8 = (AV_CODEC_ID_PCM_U16BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U8 = (AV_CODEC_ID_PCM_S8 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_MULAW = (AV_CODEC_ID_PCM_U8 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_ALAW = (AV_CODEC_ID_PCM_MULAW + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S32LE = (AV_CODEC_ID_PCM_ALAW + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S32BE = (AV_CODEC_ID_PCM_S32LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U32LE = (AV_CODEC_ID_PCM_S32BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U32BE = (AV_CODEC_ID_PCM_U32LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S24LE = (AV_CODEC_ID_PCM_U32BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S24BE = (AV_CODEC_ID_PCM_S24LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U24LE = (AV_CODEC_ID_PCM_S24BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_U24BE = (AV_CODEC_ID_PCM_U24LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S24DAUD = (AV_CODEC_ID_PCM_U24BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_ZORK = (AV_CODEC_ID_PCM_S24DAUD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S16LE_PLANAR = (AV_CODEC_ID_PCM_ZORK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_DVD = (AV_CODEC_ID_PCM_S16LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F32BE = (AV_CODEC_ID_PCM_DVD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F32LE = (AV_CODEC_ID_PCM_F32BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F64BE = (AV_CODEC_ID_PCM_F32LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F64LE = (AV_CODEC_ID_PCM_F64BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_BLURAY = (AV_CODEC_ID_PCM_F64LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_LXF = (AV_CODEC_ID_PCM_BLURAY + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_S302M = (AV_CODEC_ID_PCM_LXF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S8_PLANAR = (AV_CODEC_ID_S302M + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S24LE_PLANAR = (AV_CODEC_ID_PCM_S8_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S32LE_PLANAR = (AV_CODEC_ID_PCM_S24LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S16BE_PLANAR = (AV_CODEC_ID_PCM_S32LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S64LE = 67584# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_S64BE = (AV_CODEC_ID_PCM_S64LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F16LE = (AV_CODEC_ID_PCM_S64BE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_F24LE = (AV_CODEC_ID_PCM_F16LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_VIDC = (AV_CODEC_ID_PCM_F24LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PCM_SGA = (AV_CODEC_ID_PCM_VIDC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_QT = 69632# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_WAV = (AV_CODEC_ID_ADPCM_IMA_QT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DK3 = (AV_CODEC_ID_ADPCM_IMA_WAV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DK4 = (AV_CODEC_ID_ADPCM_IMA_DK3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_WS = (AV_CODEC_ID_ADPCM_IMA_DK4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_SMJPEG = (AV_CODEC_ID_ADPCM_IMA_WS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_MS = (AV_CODEC_ID_ADPCM_IMA_SMJPEG + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_4XM = (AV_CODEC_ID_ADPCM_MS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_XA = (AV_CODEC_ID_ADPCM_4XM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_ADX = (AV_CODEC_ID_ADPCM_XA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA = (AV_CODEC_ID_ADPCM_ADX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_G726 = (AV_CODEC_ID_ADPCM_EA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_CT = (AV_CODEC_ID_ADPCM_G726 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_SWF = (AV_CODEC_ID_ADPCM_CT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_YAMAHA = (AV_CODEC_ID_ADPCM_SWF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_4 = (AV_CODEC_ID_ADPCM_YAMAHA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_3 = (AV_CODEC_ID_ADPCM_SBPRO_4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_2 = (AV_CODEC_ID_ADPCM_SBPRO_3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_THP = (AV_CODEC_ID_ADPCM_SBPRO_2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_AMV = (AV_CODEC_ID_ADPCM_THP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R1 = (AV_CODEC_ID_ADPCM_IMA_AMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R3 = (AV_CODEC_ID_ADPCM_EA_R1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R2 = (AV_CODEC_ID_ADPCM_EA_R3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_EA_SEAD = (AV_CODEC_ID_ADPCM_EA_R2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_EA_EACS = (AV_CODEC_ID_ADPCM_IMA_EA_SEAD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_XAS = (AV_CODEC_ID_ADPCM_IMA_EA_EACS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_MAXIS_XA = (AV_CODEC_ID_ADPCM_EA_XAS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_ISS = (AV_CODEC_ID_ADPCM_EA_MAXIS_XA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_G722 = (AV_CODEC_ID_ADPCM_IMA_ISS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_APC = (AV_CODEC_ID_ADPCM_G722 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_VIMA = (AV_CODEC_ID_ADPCM_IMA_APC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_AFC = 71680# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_OKI = (AV_CODEC_ID_ADPCM_AFC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_DTK = (AV_CODEC_ID_ADPCM_IMA_OKI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_RAD = (AV_CODEC_ID_ADPCM_DTK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_G726LE = (AV_CODEC_ID_ADPCM_IMA_RAD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_THP_LE = (AV_CODEC_ID_ADPCM_G726LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_PSX = (AV_CODEC_ID_ADPCM_THP_LE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_AICA = (AV_CODEC_ID_ADPCM_PSX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DAT4 = (AV_CODEC_ID_ADPCM_AICA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_MTAF = (AV_CODEC_ID_ADPCM_IMA_DAT4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_AGM = (AV_CODEC_ID_ADPCM_MTAF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_ARGO = (AV_CODEC_ID_ADPCM_AGM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_SSI = (AV_CODEC_ID_ADPCM_ARGO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_ZORK = (AV_CODEC_ID_ADPCM_IMA_SSI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_APM = (AV_CODEC_ID_ADPCM_ZORK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_ALP = (AV_CODEC_ID_ADPCM_IMA_APM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_MTF = (AV_CODEC_ID_ADPCM_IMA_ALP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_CUNNING = (AV_CODEC_ID_ADPCM_IMA_MTF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_MOFLEX = (AV_CODEC_ID_ADPCM_IMA_CUNNING + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AMR_NB = 73728# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AMR_WB = (AV_CODEC_ID_AMR_NB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RA_144 = 77824# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RA_288 = (AV_CODEC_ID_RA_144 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ROQ_DPCM = 81920# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_DPCM = (AV_CODEC_ID_ROQ_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XAN_DPCM = (AV_CODEC_ID_INTERPLAY_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SOL_DPCM = (AV_CODEC_ID_XAN_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SDX2_DPCM = 83968# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_GREMLIN_DPCM = (AV_CODEC_ID_SDX2_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DERF_DPCM = (AV_CODEC_ID_GREMLIN_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP2 = 86016# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP3 = (AV_CODEC_ID_MP2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AAC = (AV_CODEC_ID_MP3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AC3 = (AV_CODEC_ID_AAC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DTS = (AV_CODEC_ID_AC3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VORBIS = (AV_CODEC_ID_DTS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVAUDIO = (AV_CODEC_ID_VORBIS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMAV1 = (AV_CODEC_ID_DVAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMAV2 = (AV_CODEC_ID_WMAV1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MACE3 = (AV_CODEC_ID_WMAV2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MACE6 = (AV_CODEC_ID_MACE3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VMDAUDIO = (AV_CODEC_ID_MACE6 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FLAC = (AV_CODEC_ID_VMDAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP3ADU = (AV_CODEC_ID_FLAC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP3ON4 = (AV_CODEC_ID_MP3ADU + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SHORTEN = (AV_CODEC_ID_MP3ON4 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ALAC = (AV_CODEC_ID_SHORTEN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WESTWOOD_SND1 = (AV_CODEC_ID_ALAC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_GSM = (AV_CODEC_ID_WESTWOOD_SND1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QDM2 = (AV_CODEC_ID_GSM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_COOK = (AV_CODEC_ID_QDM2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TRUESPEECH = (AV_CODEC_ID_COOK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TTA = (AV_CODEC_ID_TRUESPEECH + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMACKAUDIO = (AV_CODEC_ID_TTA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QCELP = (AV_CODEC_ID_SMACKAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WAVPACK = (AV_CODEC_ID_QCELP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSICINAUDIO = (AV_CODEC_ID_WAVPACK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IMC = (AV_CODEC_ID_DSICINAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MUSEPACK7 = (AV_CODEC_ID_IMC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MLP = (AV_CODEC_ID_MUSEPACK7 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_GSM_MS = (AV_CODEC_ID_MLP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC3 = (AV_CODEC_ID_GSM_MS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_APE = (AV_CODEC_ID_ATRAC3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_NELLYMOSER = (AV_CODEC_ID_APE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MUSEPACK8 = (AV_CODEC_ID_NELLYMOSER + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SPEEX = (AV_CODEC_ID_MUSEPACK8 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMAVOICE = (AV_CODEC_ID_SPEEX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMAPRO = (AV_CODEC_ID_WMAVOICE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WMALOSSLESS = (AV_CODEC_ID_WMAPRO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC3P = (AV_CODEC_ID_WMALOSSLESS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_EAC3 = (AV_CODEC_ID_ATRAC3P + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SIPR = (AV_CODEC_ID_EAC3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP1 = (AV_CODEC_ID_SIPR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TWINVQ = (AV_CODEC_ID_MP1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TRUEHD = (AV_CODEC_ID_TWINVQ + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MP4ALS = (AV_CODEC_ID_TRUEHD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC1 = (AV_CODEC_ID_MP4ALS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BINKAUDIO_RDFT = (AV_CODEC_ID_ATRAC1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BINKAUDIO_DCT = (AV_CODEC_ID_BINKAUDIO_RDFT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_AAC_LATM = (AV_CODEC_ID_BINKAUDIO_DCT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_QDMC = (AV_CODEC_ID_AAC_LATM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CELT = (AV_CODEC_ID_QDMC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_G723_1 = (AV_CODEC_ID_CELT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_G729 = (AV_CODEC_ID_G723_1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_8SVX_EXP = (AV_CODEC_ID_G729 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_8SVX_FIB = (AV_CODEC_ID_8SVX_EXP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BMV_AUDIO = (AV_CODEC_ID_8SVX_FIB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_RALF = (AV_CODEC_ID_BMV_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IAC = (AV_CODEC_ID_RALF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ILBC = (AV_CODEC_ID_IAC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_OPUS = (AV_CODEC_ID_ILBC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_COMFORT_NOISE = (AV_CODEC_ID_OPUS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TAK = (AV_CODEC_ID_COMFORT_NOISE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_METASOUND = (AV_CODEC_ID_TAK + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PAF_AUDIO = (AV_CODEC_ID_METASOUND + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ON2AVC = (AV_CODEC_ID_PAF_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSS_SP = (AV_CODEC_ID_ON2AVC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_CODEC2 = (AV_CODEC_ID_DSS_SP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FFWAVESYNTH = 88064# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SONIC = (AV_CODEC_ID_FFWAVESYNTH + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SONIC_LS = (AV_CODEC_ID_SONIC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_EVRC = (AV_CODEC_ID_SONIC_LS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMV = (AV_CODEC_ID_EVRC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSD_LSBF = (AV_CODEC_ID_SMV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSD_MSBF = (AV_CODEC_ID_DSD_LSBF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSD_LSBF_PLANAR = (AV_CODEC_ID_DSD_MSBF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DSD_MSBF_PLANAR = (AV_CODEC_ID_DSD_LSBF_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_4GV = (AV_CODEC_ID_DSD_MSBF_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_ACM = (AV_CODEC_ID_4GV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XMA1 = (AV_CODEC_ID_INTERPLAY_ACM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XMA2 = (AV_CODEC_ID_XMA1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DST = (AV_CODEC_ID_XMA2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC3AL = (AV_CODEC_ID_DST + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC3PAL = (AV_CODEC_ID_ATRAC3AL + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DOLBY_E = (AV_CODEC_ID_ATRAC3PAL + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_APTX = (AV_CODEC_ID_DOLBY_E + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_APTX_HD = (AV_CODEC_ID_APTX + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SBC = (AV_CODEC_ID_APTX_HD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ATRAC9 = (AV_CODEC_ID_SBC + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HCOM = (AV_CODEC_ID_ATRAC9 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ACELP_KELVIN = (AV_CODEC_ID_HCOM + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEGH_3D_AUDIO = (AV_CODEC_ID_ACELP_KELVIN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SIREN = (AV_CODEC_ID_MPEGH_3D_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HCA = (AV_CODEC_ID_SIREN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FASTAUDIO = (AV_CODEC_ID_HCA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FIRST_SUBTITLE = 94208# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVD_SUBTITLE = 94208# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVB_SUBTITLE = (AV_CODEC_ID_DVD_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TEXT = (AV_CODEC_ID_DVB_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XSUB = (AV_CODEC_ID_TEXT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SSA = (AV_CODEC_ID_XSUB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MOV_TEXT = (AV_CODEC_ID_SSA + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HDMV_PGS_SUBTITLE = (AV_CODEC_ID_MOV_TEXT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVB_TELETEXT = (AV_CODEC_ID_HDMV_PGS_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SRT = (AV_CODEC_ID_DVB_TELETEXT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MICRODVD = 96256# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_EIA_608 = (AV_CODEC_ID_MICRODVD + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_JACOSUB = (AV_CODEC_ID_EIA_608 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SAMI = (AV_CODEC_ID_JACOSUB + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_REALTEXT = (AV_CODEC_ID_SAMI + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_STL = (AV_CODEC_ID_REALTEXT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SUBVIEWER1 = (AV_CODEC_ID_STL + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SUBVIEWER = (AV_CODEC_ID_SUBVIEWER1 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SUBRIP = (AV_CODEC_ID_SUBVIEWER + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WEBVTT = (AV_CODEC_ID_SUBRIP + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPL2 = (AV_CODEC_ID_WEBVTT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_VPLAYER = (AV_CODEC_ID_MPL2 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PJS = (AV_CODEC_ID_VPLAYER + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ASS = (AV_CODEC_ID_PJS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_HDMV_TEXT_SUBTITLE = (AV_CODEC_ID_ASS + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TTML = (AV_CODEC_ID_HDMV_TEXT_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_ARIB_CAPTION = (AV_CODEC_ID_TTML + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FIRST_UNKNOWN = 98304# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TTF = 98304# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SCTE_35 = (AV_CODEC_ID_TTF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_EPG = (AV_CODEC_ID_SCTE_35 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BINTEXT = 100352# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_XBIN = (AV_CODEC_ID_BINTEXT + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_IDF = (AV_CODEC_ID_XBIN + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_OTF = (AV_CODEC_ID_IDF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_SMPTE_KLV = (AV_CODEC_ID_OTF + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_DVD_NAV = (AV_CODEC_ID_SMPTE_KLV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_TIMED_ID3 = (AV_CODEC_ID_DVD_NAV + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_BIN_DATA = (AV_CODEC_ID_TIMED_ID3 + 1)# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_PROBE = 102400# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEG2TS = 131072# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_MPEG4SYSTEMS = 131073# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_FFMETADATA = 135168# /usr/include/libavcodec/codec_id.h: 46

AV_CODEC_ID_WRAPPED_AVFRAME = 135169# /usr/include/libavcodec/codec_id.h: 46

# /usr/include/libavcodec/codec_id.h: 580
if _libs["avcodec"].has("avcodec_get_type", "cdecl"):
    avcodec_get_type = _libs["avcodec"].get("avcodec_get_type", "cdecl")
    avcodec_get_type.argtypes = [enum_AVCodecID]
    avcodec_get_type.restype = enum_AVMediaType

# /usr/include/libavcodec/codec_id.h: 586
if _libs["avcodec"].has("avcodec_get_name", "cdecl"):
    avcodec_get_name = _libs["avcodec"].get("avcodec_get_name", "cdecl")
    avcodec_get_name.argtypes = [enum_AVCodecID]
    avcodec_get_name.restype = c_char_p

enum_AVFieldOrder = c_int# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_UNKNOWN = 0# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_PROGRESSIVE = (AV_FIELD_UNKNOWN + 1)# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_TT = (AV_FIELD_PROGRESSIVE + 1)# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_BB = (AV_FIELD_TT + 1)# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_TB = (AV_FIELD_BB + 1)# /usr/include/libavcodec/codec_par.h: 36

AV_FIELD_BT = (AV_FIELD_TB + 1)# /usr/include/libavcodec/codec_par.h: 36

# /usr/include/libavcodec/codec_par.h: 201
class struct_AVCodecParameters(Structure):
    pass

struct_AVCodecParameters.__slots__ = [
    'codec_type',
    'codec_id',
    'codec_tag',
    'extradata',
    'extradata_size',
    'format',
    'bit_rate',
    'bits_per_coded_sample',
    'bits_per_raw_sample',
    'profile',
    'level',
    'width',
    'height',
    'sample_aspect_ratio',
    'field_order',
    'color_range',
    'color_primaries',
    'color_trc',
    'color_space',
    'chroma_location',
    'video_delay',
    'channel_layout',
    'channels',
    'sample_rate',
    'block_align',
    'frame_size',
    'initial_padding',
    'trailing_padding',
    'seek_preroll',
]
struct_AVCodecParameters._fields_ = [
    ('codec_type', enum_AVMediaType),
    ('codec_id', enum_AVCodecID),
    ('codec_tag', c_uint32),
    ('extradata', POINTER(c_uint8)),
    ('extradata_size', c_int),
    ('format', c_int),
    ('bit_rate', c_int64),
    ('bits_per_coded_sample', c_int),
    ('bits_per_raw_sample', c_int),
    ('profile', c_int),
    ('level', c_int),
    ('width', c_int),
    ('height', c_int),
    ('sample_aspect_ratio', AVRational),
    ('field_order', enum_AVFieldOrder),
    ('color_range', enum_AVColorRange),
    ('color_primaries', enum_AVColorPrimaries),
    ('color_trc', enum_AVColorTransferCharacteristic),
    ('color_space', enum_AVColorSpace),
    ('chroma_location', enum_AVChromaLocation),
    ('video_delay', c_int),
    ('channel_layout', c_uint64),
    ('channels', c_int),
    ('sample_rate', c_int),
    ('block_align', c_int),
    ('frame_size', c_int),
    ('initial_padding', c_int),
    ('trailing_padding', c_int),
    ('seek_preroll', c_int),
]

AVCodecParameters = struct_AVCodecParameters# /usr/include/libavcodec/codec_par.h: 201

# /usr/include/libavcodec/codec_par.h: 208
if _libs["avcodec"].has("avcodec_parameters_alloc", "cdecl"):
    avcodec_parameters_alloc = _libs["avcodec"].get("avcodec_parameters_alloc", "cdecl")
    avcodec_parameters_alloc.argtypes = []
    avcodec_parameters_alloc.restype = POINTER(AVCodecParameters)

# /usr/include/libavcodec/codec_par.h: 214
if _libs["avcodec"].has("avcodec_parameters_free", "cdecl"):
    avcodec_parameters_free = _libs["avcodec"].get("avcodec_parameters_free", "cdecl")
    avcodec_parameters_free.argtypes = [POINTER(POINTER(AVCodecParameters))]
    avcodec_parameters_free.restype = None

# /usr/include/libavcodec/codec_par.h: 222
if _libs["avcodec"].has("avcodec_parameters_copy", "cdecl"):
    avcodec_parameters_copy = _libs["avcodec"].get("avcodec_parameters_copy", "cdecl")
    avcodec_parameters_copy.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecParameters)]
    avcodec_parameters_copy.restype = c_int

enum_AVPacketSideDataType = c_int# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_PALETTE = 0# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_NEW_EXTRADATA = (AV_PKT_DATA_PALETTE + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_PARAM_CHANGE = (AV_PKT_DATA_NEW_EXTRADATA + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_H263_MB_INFO = (AV_PKT_DATA_PARAM_CHANGE + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_REPLAYGAIN = (AV_PKT_DATA_H263_MB_INFO + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_DISPLAYMATRIX = (AV_PKT_DATA_REPLAYGAIN + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_STEREO3D = (AV_PKT_DATA_DISPLAYMATRIX + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_AUDIO_SERVICE_TYPE = (AV_PKT_DATA_STEREO3D + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_QUALITY_STATS = (AV_PKT_DATA_AUDIO_SERVICE_TYPE + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_FALLBACK_TRACK = (AV_PKT_DATA_QUALITY_STATS + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_CPB_PROPERTIES = (AV_PKT_DATA_FALLBACK_TRACK + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_SKIP_SAMPLES = (AV_PKT_DATA_CPB_PROPERTIES + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_JP_DUALMONO = (AV_PKT_DATA_SKIP_SAMPLES + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_STRINGS_METADATA = (AV_PKT_DATA_JP_DUALMONO + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_SUBTITLE_POSITION = (AV_PKT_DATA_STRINGS_METADATA + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL = (AV_PKT_DATA_SUBTITLE_POSITION + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_WEBVTT_IDENTIFIER = (AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_WEBVTT_SETTINGS = (AV_PKT_DATA_WEBVTT_IDENTIFIER + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_METADATA_UPDATE = (AV_PKT_DATA_WEBVTT_SETTINGS + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_MPEGTS_STREAM_ID = (AV_PKT_DATA_METADATA_UPDATE + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_MASTERING_DISPLAY_METADATA = (AV_PKT_DATA_MPEGTS_STREAM_ID + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_SPHERICAL = (AV_PKT_DATA_MASTERING_DISPLAY_METADATA + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_CONTENT_LIGHT_LEVEL = (AV_PKT_DATA_SPHERICAL + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_A53_CC = (AV_PKT_DATA_CONTENT_LIGHT_LEVEL + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_ENCRYPTION_INIT_INFO = (AV_PKT_DATA_A53_CC + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_ENCRYPTION_INFO = (AV_PKT_DATA_ENCRYPTION_INIT_INFO + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_AFD = (AV_PKT_DATA_ENCRYPTION_INFO + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_PRFT = (AV_PKT_DATA_AFD + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_ICC_PROFILE = (AV_PKT_DATA_PRFT + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_DOVI_CONF = (AV_PKT_DATA_ICC_PROFILE + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_S12M_TIMECODE = (AV_PKT_DATA_DOVI_CONF + 1)# /usr/include/libavcodec/packet.h: 40

AV_PKT_DATA_NB = (AV_PKT_DATA_S12M_TIMECODE + 1)# /usr/include/libavcodec/packet.h: 40

# /usr/include/libavcodec/packet.h: 314
class struct_AVPacketSideData(Structure):
    pass

struct_AVPacketSideData.__slots__ = [
    'data',
    'size',
    'type',
]
struct_AVPacketSideData._fields_ = [
    ('data', POINTER(c_uint8)),
    ('size', c_int),
    ('type', enum_AVPacketSideDataType),
]

AVPacketSideData = struct_AVPacketSideData# /usr/include/libavcodec/packet.h: 314

# /usr/include/libavcodec/packet.h: 400
class struct_AVPacket(Structure):
    pass

struct_AVPacket.__slots__ = [
    'buf',
    'pts',
    'dts',
    'data',
    'size',
    'stream_index',
    'flags',
    'side_data',
    'side_data_elems',
    'duration',
    'pos',
    'convergence_duration',
]
struct_AVPacket._fields_ = [
    ('buf', POINTER(AVBufferRef)),
    ('pts', c_int64),
    ('dts', c_int64),
    ('data', POINTER(c_uint8)),
    ('size', c_int),
    ('stream_index', c_int),
    ('flags', c_int),
    ('side_data', POINTER(AVPacketSideData)),
    ('side_data_elems', c_int),
    ('duration', c_int64),
    ('pos', c_int64),
    ('convergence_duration', c_int64),
]

AVPacket = struct_AVPacket# /usr/include/libavcodec/packet.h: 400

# /usr/include/libavcodec/packet.h: 404
class struct_AVPacketList(Structure):
    pass

struct_AVPacketList.__slots__ = [
    'pkt',
    'next',
]
struct_AVPacketList._fields_ = [
    ('pkt', AVPacket),
    ('next', POINTER(struct_AVPacketList)),
]

AVPacketList = struct_AVPacketList# /usr/include/libavcodec/packet.h: 407

enum_AVSideDataParamChangeFlags = c_int# /usr/include/libavcodec/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_COUNT = 1# /usr/include/libavcodec/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_LAYOUT = 2# /usr/include/libavcodec/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_SAMPLE_RATE = 4# /usr/include/libavcodec/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_DIMENSIONS = 8# /usr/include/libavcodec/packet.h: 431

# /usr/include/libavcodec/packet.h: 449
if _libs["avcodec"].has("av_packet_alloc", "cdecl"):
    av_packet_alloc = _libs["avcodec"].get("av_packet_alloc", "cdecl")
    av_packet_alloc.argtypes = []
    av_packet_alloc.restype = POINTER(AVPacket)

# /usr/include/libavcodec/packet.h: 461
if _libs["avcodec"].has("av_packet_clone", "cdecl"):
    av_packet_clone = _libs["avcodec"].get("av_packet_clone", "cdecl")
    av_packet_clone.argtypes = [POINTER(AVPacket)]
    av_packet_clone.restype = POINTER(AVPacket)

# /usr/include/libavcodec/packet.h: 470
if _libs["avcodec"].has("av_packet_free", "cdecl"):
    av_packet_free = _libs["avcodec"].get("av_packet_free", "cdecl")
    av_packet_free.argtypes = [POINTER(POINTER(AVPacket))]
    av_packet_free.restype = None

# /usr/include/libavcodec/packet.h: 488
if _libs["avcodec"].has("av_init_packet", "cdecl"):
    av_init_packet = _libs["avcodec"].get("av_init_packet", "cdecl")
    av_init_packet.argtypes = [POINTER(AVPacket)]
    av_init_packet.restype = None

# /usr/include/libavcodec/packet.h: 499
if _libs["avcodec"].has("av_new_packet", "cdecl"):
    av_new_packet = _libs["avcodec"].get("av_new_packet", "cdecl")
    av_new_packet.argtypes = [POINTER(AVPacket), c_int]
    av_new_packet.restype = c_int

# /usr/include/libavcodec/packet.h: 507
if _libs["avcodec"].has("av_shrink_packet", "cdecl"):
    av_shrink_packet = _libs["avcodec"].get("av_shrink_packet", "cdecl")
    av_shrink_packet.argtypes = [POINTER(AVPacket), c_int]
    av_shrink_packet.restype = None

# /usr/include/libavcodec/packet.h: 515
if _libs["avcodec"].has("av_grow_packet", "cdecl"):
    av_grow_packet = _libs["avcodec"].get("av_grow_packet", "cdecl")
    av_grow_packet.argtypes = [POINTER(AVPacket), c_int]
    av_grow_packet.restype = c_int

# /usr/include/libavcodec/packet.h: 530
if _libs["avcodec"].has("av_packet_from_data", "cdecl"):
    av_packet_from_data = _libs["avcodec"].get("av_packet_from_data", "cdecl")
    av_packet_from_data.argtypes = [POINTER(AVPacket), POINTER(c_uint8), c_int]
    av_packet_from_data.restype = c_int

# /usr/include/libavcodec/packet.h: 540
if _libs["avcodec"].has("av_dup_packet", "cdecl"):
    av_dup_packet = _libs["avcodec"].get("av_dup_packet", "cdecl")
    av_dup_packet.argtypes = [POINTER(AVPacket)]
    av_dup_packet.restype = c_int

# /usr/include/libavcodec/packet.h: 549
if _libs["avcodec"].has("av_copy_packet", "cdecl"):
    av_copy_packet = _libs["avcodec"].get("av_copy_packet", "cdecl")
    av_copy_packet.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_copy_packet.restype = c_int

# /usr/include/libavcodec/packet.h: 559
if _libs["avcodec"].has("av_copy_packet_side_data", "cdecl"):
    av_copy_packet_side_data = _libs["avcodec"].get("av_copy_packet_side_data", "cdecl")
    av_copy_packet_side_data.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_copy_packet_side_data.restype = c_int

# /usr/include/libavcodec/packet.h: 569
if _libs["avcodec"].has("av_free_packet", "cdecl"):
    av_free_packet = _libs["avcodec"].get("av_free_packet", "cdecl")
    av_free_packet.argtypes = [POINTER(AVPacket)]
    av_free_packet.restype = None

# /usr/include/libavcodec/packet.h: 579
if _libs["avcodec"].has("av_packet_new_side_data", "cdecl"):
    av_packet_new_side_data = _libs["avcodec"].get("av_packet_new_side_data", "cdecl")
    av_packet_new_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_int]
    av_packet_new_side_data.restype = POINTER(c_uint8)

# /usr/include/libavcodec/packet.h: 599
if _libs["avcodec"].has("av_packet_add_side_data", "cdecl"):
    av_packet_add_side_data = _libs["avcodec"].get("av_packet_add_side_data", "cdecl")
    av_packet_add_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(c_uint8), c_size_t]
    av_packet_add_side_data.restype = c_int

# /usr/include/libavcodec/packet.h: 610
if _libs["avcodec"].has("av_packet_shrink_side_data", "cdecl"):
    av_packet_shrink_side_data = _libs["avcodec"].get("av_packet_shrink_side_data", "cdecl")
    av_packet_shrink_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_int]
    av_packet_shrink_side_data.restype = c_int

# /usr/include/libavcodec/packet.h: 626
if _libs["avcodec"].has("av_packet_get_side_data", "cdecl"):
    av_packet_get_side_data = _libs["avcodec"].get("av_packet_get_side_data", "cdecl")
    av_packet_get_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(c_int)]
    av_packet_get_side_data.restype = POINTER(c_uint8)

# /usr/include/libavcodec/packet.h: 635
if _libs["avcodec"].has("av_packet_merge_side_data", "cdecl"):
    av_packet_merge_side_data = _libs["avcodec"].get("av_packet_merge_side_data", "cdecl")
    av_packet_merge_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_merge_side_data.restype = c_int

# /usr/include/libavcodec/packet.h: 638
if _libs["avcodec"].has("av_packet_split_side_data", "cdecl"):
    av_packet_split_side_data = _libs["avcodec"].get("av_packet_split_side_data", "cdecl")
    av_packet_split_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_split_side_data.restype = c_int

# /usr/include/libavcodec/packet.h: 641
if _libs["avcodec"].has("av_packet_side_data_name", "cdecl"):
    av_packet_side_data_name = _libs["avcodec"].get("av_packet_side_data_name", "cdecl")
    av_packet_side_data_name.argtypes = [enum_AVPacketSideDataType]
    av_packet_side_data_name.restype = c_char_p

# /usr/include/libavcodec/packet.h: 651
if _libs["avcodec"].has("av_packet_pack_dictionary", "cdecl"):
    av_packet_pack_dictionary = _libs["avcodec"].get("av_packet_pack_dictionary", "cdecl")
    av_packet_pack_dictionary.argtypes = [POINTER(AVDictionary), POINTER(c_int)]
    av_packet_pack_dictionary.restype = POINTER(c_uint8)

# /usr/include/libavcodec/packet.h: 664
if _libs["avcodec"].has("av_packet_unpack_dictionary", "cdecl"):
    av_packet_unpack_dictionary = _libs["avcodec"].get("av_packet_unpack_dictionary", "cdecl")
    av_packet_unpack_dictionary.argtypes = [POINTER(c_uint8), c_int, POINTER(POINTER(AVDictionary))]
    av_packet_unpack_dictionary.restype = c_int

# /usr/include/libavcodec/packet.h: 676
if _libs["avcodec"].has("av_packet_free_side_data", "cdecl"):
    av_packet_free_side_data = _libs["avcodec"].get("av_packet_free_side_data", "cdecl")
    av_packet_free_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_free_side_data.restype = None

# /usr/include/libavcodec/packet.h: 695
if _libs["avcodec"].has("av_packet_ref", "cdecl"):
    av_packet_ref = _libs["avcodec"].get("av_packet_ref", "cdecl")
    av_packet_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_ref.restype = c_int

# /usr/include/libavcodec/packet.h: 705
if _libs["avcodec"].has("av_packet_unref", "cdecl"):
    av_packet_unref = _libs["avcodec"].get("av_packet_unref", "cdecl")
    av_packet_unref.argtypes = [POINTER(AVPacket)]
    av_packet_unref.restype = None

# /usr/include/libavcodec/packet.h: 715
if _libs["avcodec"].has("av_packet_move_ref", "cdecl"):
    av_packet_move_ref = _libs["avcodec"].get("av_packet_move_ref", "cdecl")
    av_packet_move_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_move_ref.restype = None

# /usr/include/libavcodec/packet.h: 728
if _libs["avcodec"].has("av_packet_copy_props", "cdecl"):
    av_packet_copy_props = _libs["avcodec"].get("av_packet_copy_props", "cdecl")
    av_packet_copy_props.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_copy_props.restype = c_int

# /usr/include/libavcodec/packet.h: 744
if _libs["avcodec"].has("av_packet_make_refcounted", "cdecl"):
    av_packet_make_refcounted = _libs["avcodec"].get("av_packet_make_refcounted", "cdecl")
    av_packet_make_refcounted.argtypes = [POINTER(AVPacket)]
    av_packet_make_refcounted.restype = c_int

# /usr/include/libavcodec/packet.h: 755
if _libs["avcodec"].has("av_packet_make_writable", "cdecl"):
    av_packet_make_writable = _libs["avcodec"].get("av_packet_make_writable", "cdecl")
    av_packet_make_writable.argtypes = [POINTER(AVPacket)]
    av_packet_make_writable.restype = c_int

# /usr/include/libavcodec/packet.h: 768
if _libs["avcodec"].has("av_packet_rescale_ts", "cdecl"):
    av_packet_rescale_ts = _libs["avcodec"].get("av_packet_rescale_ts", "cdecl")
    av_packet_rescale_ts.argtypes = [POINTER(AVPacket), AVRational, AVRational]
    av_packet_rescale_ts.restype = None

# /usr/include/libavcodec/bsf.h: 37
class struct_AVBSFInternal(Structure):
    pass

AVBSFInternal = struct_AVBSFInternal# /usr/include/libavcodec/bsf.h: 37

# /usr/include/libavcodec/bsf.h: 98
class struct_AVBitStreamFilter(Structure):
    pass

# /usr/include/libavcodec/bsf.h: 96
class struct_AVBSFContext(Structure):
    pass

struct_AVBSFContext.__slots__ = [
    'av_class',
    'filter',
    'internal',
    'priv_data',
    'par_in',
    'par_out',
    'time_base_in',
    'time_base_out',
]
struct_AVBSFContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('filter', POINTER(struct_AVBitStreamFilter)),
    ('internal', POINTER(AVBSFInternal)),
    ('priv_data', POINTER(None)),
    ('par_in', POINTER(AVCodecParameters)),
    ('par_out', POINTER(AVCodecParameters)),
    ('time_base_in', AVRational),
    ('time_base_out', AVRational),
]

AVBSFContext = struct_AVBSFContext# /usr/include/libavcodec/bsf.h: 96

struct_AVBitStreamFilter.__slots__ = [
    'name',
    'codec_ids',
    'priv_class',
    'priv_data_size',
    'init',
    'filter',
    'close',
    'flush',
]
struct_AVBitStreamFilter._fields_ = [
    ('name', String),
    ('codec_ids', POINTER(enum_AVCodecID)),
    ('priv_class', POINTER(AVClass)),
    ('priv_data_size', c_int),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVBSFContext))),
    ('filter', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVBSFContext), POINTER(AVPacket))),
    ('close', CFUNCTYPE(UNCHECKED(None), POINTER(AVBSFContext))),
    ('flush', CFUNCTYPE(UNCHECKED(None), POINTER(AVBSFContext))),
]

AVBitStreamFilter = struct_AVBitStreamFilter# /usr/include/libavcodec/bsf.h: 132

# /usr/include/libavcodec/bsf.h: 138
if _libs["avcodec"].has("av_bsf_get_by_name", "cdecl"):
    av_bsf_get_by_name = _libs["avcodec"].get("av_bsf_get_by_name", "cdecl")
    av_bsf_get_by_name.argtypes = [String]
    av_bsf_get_by_name.restype = POINTER(AVBitStreamFilter)

# /usr/include/libavcodec/bsf.h: 149
if _libs["avcodec"].has("av_bsf_iterate", "cdecl"):
    av_bsf_iterate = _libs["avcodec"].get("av_bsf_iterate", "cdecl")
    av_bsf_iterate.argtypes = [POINTER(POINTER(None))]
    av_bsf_iterate.restype = POINTER(AVBitStreamFilter)

# /usr/include/libavcodec/bsf.h: 163
if _libs["avcodec"].has("av_bsf_alloc", "cdecl"):
    av_bsf_alloc = _libs["avcodec"].get("av_bsf_alloc", "cdecl")
    av_bsf_alloc.argtypes = [POINTER(AVBitStreamFilter), POINTER(POINTER(AVBSFContext))]
    av_bsf_alloc.restype = c_int

# /usr/include/libavcodec/bsf.h: 169
if _libs["avcodec"].has("av_bsf_init", "cdecl"):
    av_bsf_init = _libs["avcodec"].get("av_bsf_init", "cdecl")
    av_bsf_init.argtypes = [POINTER(AVBSFContext)]
    av_bsf_init.restype = c_int

# /usr/include/libavcodec/bsf.h: 189
if _libs["avcodec"].has("av_bsf_send_packet", "cdecl"):
    av_bsf_send_packet = _libs["avcodec"].get("av_bsf_send_packet", "cdecl")
    av_bsf_send_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_send_packet.restype = c_int

# /usr/include/libavcodec/bsf.h: 215
if _libs["avcodec"].has("av_bsf_receive_packet", "cdecl"):
    av_bsf_receive_packet = _libs["avcodec"].get("av_bsf_receive_packet", "cdecl")
    av_bsf_receive_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_receive_packet.restype = c_int

# /usr/include/libavcodec/bsf.h: 220
if _libs["avcodec"].has("av_bsf_flush", "cdecl"):
    av_bsf_flush = _libs["avcodec"].get("av_bsf_flush", "cdecl")
    av_bsf_flush.argtypes = [POINTER(AVBSFContext)]
    av_bsf_flush.restype = None

# /usr/include/libavcodec/bsf.h: 226
if _libs["avcodec"].has("av_bsf_free", "cdecl"):
    av_bsf_free = _libs["avcodec"].get("av_bsf_free", "cdecl")
    av_bsf_free.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_free.restype = None

# /usr/include/libavcodec/bsf.h: 234
if _libs["avcodec"].has("av_bsf_get_class", "cdecl"):
    av_bsf_get_class = _libs["avcodec"].get("av_bsf_get_class", "cdecl")
    av_bsf_get_class.argtypes = []
    av_bsf_get_class.restype = POINTER(AVClass)

# /usr/include/libavcodec/bsf.h: 240
class struct_AVBSFList(Structure):
    pass

AVBSFList = struct_AVBSFList# /usr/include/libavcodec/bsf.h: 240

# /usr/include/libavcodec/bsf.h: 249
if _libs["avcodec"].has("av_bsf_list_alloc", "cdecl"):
    av_bsf_list_alloc = _libs["avcodec"].get("av_bsf_list_alloc", "cdecl")
    av_bsf_list_alloc.argtypes = []
    av_bsf_list_alloc.restype = POINTER(AVBSFList)

# /usr/include/libavcodec/bsf.h: 256
if _libs["avcodec"].has("av_bsf_list_free", "cdecl"):
    av_bsf_list_free = _libs["avcodec"].get("av_bsf_list_free", "cdecl")
    av_bsf_list_free.argtypes = [POINTER(POINTER(AVBSFList))]
    av_bsf_list_free.restype = None

# /usr/include/libavcodec/bsf.h: 266
if _libs["avcodec"].has("av_bsf_list_append", "cdecl"):
    av_bsf_list_append = _libs["avcodec"].get("av_bsf_list_append", "cdecl")
    av_bsf_list_append.argtypes = [POINTER(AVBSFList), POINTER(AVBSFContext)]
    av_bsf_list_append.restype = c_int

# /usr/include/libavcodec/bsf.h: 278
if _libs["avcodec"].has("av_bsf_list_append2", "cdecl"):
    av_bsf_list_append2 = _libs["avcodec"].get("av_bsf_list_append2", "cdecl")
    av_bsf_list_append2.argtypes = [POINTER(AVBSFList), String, POINTER(POINTER(AVDictionary))]
    av_bsf_list_append2.restype = c_int

# /usr/include/libavcodec/bsf.h: 295
if _libs["avcodec"].has("av_bsf_list_finalize", "cdecl"):
    av_bsf_list_finalize = _libs["avcodec"].get("av_bsf_list_finalize", "cdecl")
    av_bsf_list_finalize.argtypes = [POINTER(POINTER(AVBSFList)), POINTER(POINTER(AVBSFContext))]
    av_bsf_list_finalize.restype = c_int

# /usr/include/libavcodec/bsf.h: 310
if _libs["avcodec"].has("av_bsf_list_parse_str", "cdecl"):
    av_bsf_list_parse_str = _libs["avcodec"].get("av_bsf_list_parse_str", "cdecl")
    av_bsf_list_parse_str.argtypes = [String, POINTER(POINTER(AVBSFContext))]
    av_bsf_list_parse_str.restype = c_int

# /usr/include/libavcodec/bsf.h: 319
if _libs["avcodec"].has("av_bsf_get_null_filter", "cdecl"):
    av_bsf_get_null_filter = _libs["avcodec"].get("av_bsf_get_null_filter", "cdecl")
    av_bsf_get_null_filter.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_get_null_filter.restype = c_int

# /usr/include/libavcodec/codec.h: 186
class struct_AVProfile(Structure):
    pass

struct_AVProfile.__slots__ = [
    'profile',
    'name',
]
struct_AVProfile._fields_ = [
    ('profile', c_int),
    ('name', String),
]

AVProfile = struct_AVProfile# /usr/include/libavcodec/codec.h: 186

# /usr/include/libavcodec/codec.h: 188
class struct_AVCodecDefault(Structure):
    pass

AVCodecDefault = struct_AVCodecDefault# /usr/include/libavcodec/codec.h: 188

# /usr/include/libavcodec/avcodec.h: 536
class struct_AVCodecContext(Structure):
    pass

# /usr/include/libavcodec/avcodec.h: 2722
class struct_AVSubtitle(Structure):
    pass

# /usr/include/libavcodec/codec.h: 197
class struct_AVCodec(Structure):
    pass

# /usr/include/libavcodec/codec.h: 343
class struct_AVCodecHWConfigInternal(Structure):
    pass

struct_AVCodec.__slots__ = [
    'name',
    'long_name',
    'type',
    'id',
    'capabilities',
    'supported_framerates',
    'pix_fmts',
    'supported_samplerates',
    'sample_fmts',
    'channel_layouts',
    'max_lowres',
    'priv_class',
    'profiles',
    'wrapper_name',
    'priv_data_size',
    'next',
    'update_thread_context',
    'defaults',
    'init_static_data',
    'init',
    'encode_sub',
    'encode2',
    'decode',
    'close',
    'receive_packet',
    'receive_frame',
    'flush',
    'caps_internal',
    'bsfs',
    'hw_configs',
    'codec_tags',
]
struct_AVCodec._fields_ = [
    ('name', String),
    ('long_name', String),
    ('type', enum_AVMediaType),
    ('id', enum_AVCodecID),
    ('capabilities', c_int),
    ('supported_framerates', POINTER(AVRational)),
    ('pix_fmts', POINTER(enum_AVPixelFormat)),
    ('supported_samplerates', POINTER(c_int)),
    ('sample_fmts', POINTER(enum_AVSampleFormat)),
    ('channel_layouts', POINTER(c_uint64)),
    ('max_lowres', c_uint8),
    ('priv_class', POINTER(AVClass)),
    ('profiles', POINTER(AVProfile)),
    ('wrapper_name', String),
    ('priv_data_size', c_int),
    ('next', POINTER(struct_AVCodec)),
    ('update_thread_context', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(struct_AVCodecContext))),
    ('defaults', POINTER(AVCodecDefault)),
    ('init_static_data', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVCodec))),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext))),
    ('encode_sub', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(c_uint8), c_int, POINTER(struct_AVSubtitle))),
    ('encode2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(struct_AVPacket), POINTER(struct_AVFrame), POINTER(c_int))),
    ('decode', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(None), POINTER(c_int), POINTER(struct_AVPacket))),
    ('close', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext))),
    ('receive_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(struct_AVPacket))),
    ('receive_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(struct_AVFrame))),
    ('flush', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVCodecContext))),
    ('caps_internal', c_int),
    ('bsfs', String),
    ('hw_configs', POINTER(POINTER(struct_AVCodecHWConfigInternal))),
    ('codec_tags', POINTER(c_uint32)),
]

AVCodec = struct_AVCodec# /usr/include/libavcodec/codec.h: 349

# /usr/include/libavcodec/codec.h: 360
if _libs["avcodec"].has("av_codec_iterate", "cdecl"):
    av_codec_iterate = _libs["avcodec"].get("av_codec_iterate", "cdecl")
    av_codec_iterate.argtypes = [POINTER(POINTER(None))]
    av_codec_iterate.restype = POINTER(AVCodec)

# /usr/include/libavcodec/codec.h: 368
if _libs["avcodec"].has("avcodec_find_decoder", "cdecl"):
    avcodec_find_decoder = _libs["avcodec"].get("avcodec_find_decoder", "cdecl")
    avcodec_find_decoder.argtypes = [enum_AVCodecID]
    avcodec_find_decoder.restype = POINTER(AVCodec)

# /usr/include/libavcodec/codec.h: 376
if _libs["avcodec"].has("avcodec_find_decoder_by_name", "cdecl"):
    avcodec_find_decoder_by_name = _libs["avcodec"].get("avcodec_find_decoder_by_name", "cdecl")
    avcodec_find_decoder_by_name.argtypes = [String]
    avcodec_find_decoder_by_name.restype = POINTER(AVCodec)

# /usr/include/libavcodec/codec.h: 384
if _libs["avcodec"].has("avcodec_find_encoder", "cdecl"):
    avcodec_find_encoder = _libs["avcodec"].get("avcodec_find_encoder", "cdecl")
    avcodec_find_encoder.argtypes = [enum_AVCodecID]
    avcodec_find_encoder.restype = POINTER(AVCodec)

# /usr/include/libavcodec/codec.h: 392
if _libs["avcodec"].has("avcodec_find_encoder_by_name", "cdecl"):
    avcodec_find_encoder_by_name = _libs["avcodec"].get("avcodec_find_encoder_by_name", "cdecl")
    avcodec_find_encoder_by_name.argtypes = [String]
    avcodec_find_encoder_by_name.restype = POINTER(AVCodec)

# /usr/include/libavcodec/codec.h: 396
if _libs["avcodec"].has("av_codec_is_encoder", "cdecl"):
    av_codec_is_encoder = _libs["avcodec"].get("av_codec_is_encoder", "cdecl")
    av_codec_is_encoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_encoder.restype = c_int

# /usr/include/libavcodec/codec.h: 401
if _libs["avcodec"].has("av_codec_is_decoder", "cdecl"):
    av_codec_is_decoder = _libs["avcodec"].get("av_codec_is_decoder", "cdecl")
    av_codec_is_decoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_decoder.restype = c_int

enum_anon_28 = c_int# /usr/include/libavcodec/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_HW_DEVICE_CTX = 1# /usr/include/libavcodec/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_HW_FRAMES_CTX = 2# /usr/include/libavcodec/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_INTERNAL = 4# /usr/include/libavcodec/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_AD_HOC = 8# /usr/include/libavcodec/codec.h: 403

# /usr/include/libavcodec/codec.h: 465
class struct_AVCodecHWConfig(Structure):
    pass

struct_AVCodecHWConfig.__slots__ = [
    'pix_fmt',
    'methods',
    'device_type',
]
struct_AVCodecHWConfig._fields_ = [
    ('pix_fmt', enum_AVPixelFormat),
    ('methods', c_int),
    ('device_type', enum_AVHWDeviceType),
]

AVCodecHWConfig = struct_AVCodecHWConfig# /usr/include/libavcodec/codec.h: 465

# /usr/include/libavcodec/codec.h: 474
if _libs["avcodec"].has("avcodec_get_hw_config", "cdecl"):
    avcodec_get_hw_config = _libs["avcodec"].get("avcodec_get_hw_config", "cdecl")
    avcodec_get_hw_config.argtypes = [POINTER(AVCodec), c_int]
    avcodec_get_hw_config.restype = POINTER(AVCodecHWConfig)

# /usr/include/libavcodec/codec_desc.h: 66
class struct_AVCodecDescriptor(Structure):
    pass

struct_AVCodecDescriptor.__slots__ = [
    'id',
    'type',
    'name',
    'long_name',
    'props',
    'mime_types',
    'profiles',
]
struct_AVCodecDescriptor._fields_ = [
    ('id', enum_AVCodecID),
    ('type', enum_AVMediaType),
    ('name', String),
    ('long_name', String),
    ('props', c_int),
    ('mime_types', POINTER(POINTER(c_char))),
    ('profiles', POINTER(struct_AVProfile)),
]

AVCodecDescriptor = struct_AVCodecDescriptor# /usr/include/libavcodec/codec_desc.h: 66

# /usr/include/libavcodec/codec_desc.h: 107
if _libs["avcodec"].has("avcodec_descriptor_get", "cdecl"):
    avcodec_descriptor_get = _libs["avcodec"].get("avcodec_descriptor_get", "cdecl")
    avcodec_descriptor_get.argtypes = [enum_AVCodecID]
    avcodec_descriptor_get.restype = POINTER(AVCodecDescriptor)

# /usr/include/libavcodec/codec_desc.h: 116
if _libs["avcodec"].has("avcodec_descriptor_next", "cdecl"):
    avcodec_descriptor_next = _libs["avcodec"].get("avcodec_descriptor_next", "cdecl")
    avcodec_descriptor_next.argtypes = [POINTER(AVCodecDescriptor)]
    avcodec_descriptor_next.restype = POINTER(AVCodecDescriptor)

# /usr/include/libavcodec/codec_desc.h: 122
if _libs["avcodec"].has("avcodec_descriptor_get_by_name", "cdecl"):
    avcodec_descriptor_get_by_name = _libs["avcodec"].get("avcodec_descriptor_get_by_name", "cdecl")
    avcodec_descriptor_get_by_name.argtypes = [String]
    avcodec_descriptor_get_by_name.restype = POINTER(AVCodecDescriptor)

enum_AVDiscard = c_int# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_NONE = (-16)# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_DEFAULT = 0# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_NONREF = 8# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_BIDIR = 16# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_NONINTRA = 24# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_NONKEY = 32# /usr/include/libavcodec/avcodec.h: 227

AVDISCARD_ALL = 48# /usr/include/libavcodec/avcodec.h: 227

enum_AVAudioServiceType = c_int# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_MAIN = 0# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_EFFECTS = 1# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_VISUALLY_IMPAIRED = 2# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_HEARING_IMPAIRED = 3# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_DIALOGUE = 4# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_COMMENTARY = 5# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_EMERGENCY = 6# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_VOICE_OVER = 7# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_KARAOKE = 8# /usr/include/libavcodec/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_NB = (AV_AUDIO_SERVICE_TYPE_KARAOKE + 1)# /usr/include/libavcodec/avcodec.h: 239

# /usr/include/libavcodec/avcodec.h: 260
class struct_RcOverride(Structure):
    pass

struct_RcOverride.__slots__ = [
    'start_frame',
    'end_frame',
    'qscale',
    'quality_factor',
]
struct_RcOverride._fields_ = [
    ('start_frame', c_int),
    ('end_frame', c_int),
    ('qscale', c_int),
    ('quality_factor', c_float),
]

RcOverride = struct_RcOverride# /usr/include/libavcodec/avcodec.h: 260

# /usr/include/libavcodec/avcodec.h: 446
class struct_AVPanScan(Structure):
    pass

struct_AVPanScan.__slots__ = [
    'id',
    'width',
    'height',
    'position',
]
struct_AVPanScan._fields_ = [
    ('id', c_int),
    ('width', c_int),
    ('height', c_int),
    ('position', (c_int16 * int(2)) * int(3)),
]

AVPanScan = struct_AVPanScan# /usr/include/libavcodec/avcodec.h: 446

# /usr/include/libavcodec/avcodec.h: 496
class struct_AVCPBProperties(Structure):
    pass

struct_AVCPBProperties.__slots__ = [
    'max_bitrate',
    'min_bitrate',
    'avg_bitrate',
    'buffer_size',
    'vbv_delay',
]
struct_AVCPBProperties._fields_ = [
    ('max_bitrate', c_int),
    ('min_bitrate', c_int),
    ('avg_bitrate', c_int),
    ('buffer_size', c_int),
    ('vbv_delay', c_uint64),
]

AVCPBProperties = struct_AVCPBProperties# /usr/include/libavcodec/avcodec.h: 496

# /usr/include/libavcodec/avcodec.h: 509
class struct_AVProducerReferenceTime(Structure):
    pass

struct_AVProducerReferenceTime.__slots__ = [
    'wallclock',
    'flags',
]
struct_AVProducerReferenceTime._fields_ = [
    ('wallclock', c_int64),
    ('flags', c_int),
]

AVProducerReferenceTime = struct_AVProducerReferenceTime# /usr/include/libavcodec/avcodec.h: 509

# /usr/include/libavcodec/avcodec.h: 521
class struct_AVCodecInternal(Structure):
    pass

# /usr/include/libavcodec/avcodec.h: 2438
class struct_AVHWAccel(Structure):
    pass

struct_AVCodecContext.__slots__ = [
    'av_class',
    'log_level_offset',
    'codec_type',
    'codec',
    'codec_id',
    'codec_tag',
    'priv_data',
    'internal',
    'opaque',
    'bit_rate',
    'bit_rate_tolerance',
    'global_quality',
    'compression_level',
    'flags',
    'flags2',
    'extradata',
    'extradata_size',
    'time_base',
    'ticks_per_frame',
    'delay',
    'width',
    'height',
    'coded_width',
    'coded_height',
    'gop_size',
    'pix_fmt',
    'draw_horiz_band',
    'get_format',
    'max_b_frames',
    'b_quant_factor',
    'b_frame_strategy',
    'b_quant_offset',
    'has_b_frames',
    'mpeg_quant',
    'i_quant_factor',
    'i_quant_offset',
    'lumi_masking',
    'temporal_cplx_masking',
    'spatial_cplx_masking',
    'p_masking',
    'dark_masking',
    'slice_count',
    'prediction_method',
    'slice_offset',
    'sample_aspect_ratio',
    'me_cmp',
    'me_sub_cmp',
    'mb_cmp',
    'ildct_cmp',
    'dia_size',
    'last_predictor_count',
    'pre_me',
    'me_pre_cmp',
    'pre_dia_size',
    'me_subpel_quality',
    'me_range',
    'slice_flags',
    'mb_decision',
    'intra_matrix',
    'inter_matrix',
    'scenechange_threshold',
    'noise_reduction',
    'intra_dc_precision',
    'skip_top',
    'skip_bottom',
    'mb_lmin',
    'mb_lmax',
    'me_penalty_compensation',
    'bidir_refine',
    'brd_scale',
    'keyint_min',
    'refs',
    'chromaoffset',
    'mv0_threshold',
    'b_sensitivity',
    'color_primaries',
    'color_trc',
    'colorspace',
    'color_range',
    'chroma_sample_location',
    'slices',
    'field_order',
    'sample_rate',
    'channels',
    'sample_fmt',
    'frame_size',
    'frame_number',
    'block_align',
    'cutoff',
    'channel_layout',
    'request_channel_layout',
    'audio_service_type',
    'request_sample_fmt',
    'get_buffer2',
    'refcounted_frames',
    'qcompress',
    'qblur',
    'qmin',
    'qmax',
    'max_qdiff',
    'rc_buffer_size',
    'rc_override_count',
    'rc_override',
    'rc_max_rate',
    'rc_min_rate',
    'rc_max_available_vbv_use',
    'rc_min_vbv_overflow_use',
    'rc_initial_buffer_occupancy',
    'coder_type',
    'context_model',
    'frame_skip_threshold',
    'frame_skip_factor',
    'frame_skip_exp',
    'frame_skip_cmp',
    'trellis',
    'min_prediction_order',
    'max_prediction_order',
    'timecode_frame_start',
    'rtp_callback',
    'rtp_payload_size',
    'mv_bits',
    'header_bits',
    'i_tex_bits',
    'p_tex_bits',
    'i_count',
    'p_count',
    'skip_count',
    'misc_bits',
    'frame_bits',
    'stats_out',
    'stats_in',
    'workaround_bugs',
    'strict_std_compliance',
    'error_concealment',
    'debug',
    'err_recognition',
    'reordered_opaque',
    'hwaccel',
    'hwaccel_context',
    'error',
    'dct_algo',
    'idct_algo',
    'bits_per_coded_sample',
    'bits_per_raw_sample',
    'lowres',
    'coded_frame',
    'thread_count',
    'thread_type',
    'active_thread_type',
    'thread_safe_callbacks',
    'execute',
    'execute2',
    'nsse_weight',
    'profile',
    'level',
    'skip_loop_filter',
    'skip_idct',
    'skip_frame',
    'subtitle_header',
    'subtitle_header_size',
    'vbv_delay',
    'side_data_only_packets',
    'initial_padding',
    'framerate',
    'sw_pix_fmt',
    'pkt_timebase',
    'codec_descriptor',
    'pts_correction_num_faulty_pts',
    'pts_correction_num_faulty_dts',
    'pts_correction_last_pts',
    'pts_correction_last_dts',
    'sub_charenc',
    'sub_charenc_mode',
    'skip_alpha',
    'seek_preroll',
    'debug_mv',
    'chroma_intra_matrix',
    'dump_separator',
    'codec_whitelist',
    'properties',
    'coded_side_data',
    'nb_coded_side_data',
    'hw_frames_ctx',
    'sub_text_format',
    'trailing_padding',
    'max_pixels',
    'hw_device_ctx',
    'hwaccel_flags',
    'apply_cropping',
    'extra_hw_frames',
    'discard_damaged_percentage',
    'max_samples',
    'export_side_data',
    'get_encode_buffer',
]
struct_AVCodecContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('log_level_offset', c_int),
    ('codec_type', enum_AVMediaType),
    ('codec', POINTER(struct_AVCodec)),
    ('codec_id', enum_AVCodecID),
    ('codec_tag', c_uint),
    ('priv_data', POINTER(None)),
    ('internal', POINTER(struct_AVCodecInternal)),
    ('opaque', POINTER(None)),
    ('bit_rate', c_int64),
    ('bit_rate_tolerance', c_int),
    ('global_quality', c_int),
    ('compression_level', c_int),
    ('flags', c_int),
    ('flags2', c_int),
    ('extradata', POINTER(c_uint8)),
    ('extradata_size', c_int),
    ('time_base', AVRational),
    ('ticks_per_frame', c_int),
    ('delay', c_int),
    ('width', c_int),
    ('height', c_int),
    ('coded_width', c_int),
    ('coded_height', c_int),
    ('gop_size', c_int),
    ('pix_fmt', enum_AVPixelFormat),
    ('draw_horiz_band', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVCodecContext), POINTER(AVFrame), c_int * int(8), c_int, c_int, c_int)),
    ('get_format', CFUNCTYPE(UNCHECKED(enum_AVPixelFormat), POINTER(struct_AVCodecContext), POINTER(enum_AVPixelFormat))),
    ('max_b_frames', c_int),
    ('b_quant_factor', c_float),
    ('b_frame_strategy', c_int),
    ('b_quant_offset', c_float),
    ('has_b_frames', c_int),
    ('mpeg_quant', c_int),
    ('i_quant_factor', c_float),
    ('i_quant_offset', c_float),
    ('lumi_masking', c_float),
    ('temporal_cplx_masking', c_float),
    ('spatial_cplx_masking', c_float),
    ('p_masking', c_float),
    ('dark_masking', c_float),
    ('slice_count', c_int),
    ('prediction_method', c_int),
    ('slice_offset', POINTER(c_int)),
    ('sample_aspect_ratio', AVRational),
    ('me_cmp', c_int),
    ('me_sub_cmp', c_int),
    ('mb_cmp', c_int),
    ('ildct_cmp', c_int),
    ('dia_size', c_int),
    ('last_predictor_count', c_int),
    ('pre_me', c_int),
    ('me_pre_cmp', c_int),
    ('pre_dia_size', c_int),
    ('me_subpel_quality', c_int),
    ('me_range', c_int),
    ('slice_flags', c_int),
    ('mb_decision', c_int),
    ('intra_matrix', POINTER(c_uint16)),
    ('inter_matrix', POINTER(c_uint16)),
    ('scenechange_threshold', c_int),
    ('noise_reduction', c_int),
    ('intra_dc_precision', c_int),
    ('skip_top', c_int),
    ('skip_bottom', c_int),
    ('mb_lmin', c_int),
    ('mb_lmax', c_int),
    ('me_penalty_compensation', c_int),
    ('bidir_refine', c_int),
    ('brd_scale', c_int),
    ('keyint_min', c_int),
    ('refs', c_int),
    ('chromaoffset', c_int),
    ('mv0_threshold', c_int),
    ('b_sensitivity', c_int),
    ('color_primaries', enum_AVColorPrimaries),
    ('color_trc', enum_AVColorTransferCharacteristic),
    ('colorspace', enum_AVColorSpace),
    ('color_range', enum_AVColorRange),
    ('chroma_sample_location', enum_AVChromaLocation),
    ('slices', c_int),
    ('field_order', enum_AVFieldOrder),
    ('sample_rate', c_int),
    ('channels', c_int),
    ('sample_fmt', enum_AVSampleFormat),
    ('frame_size', c_int),
    ('frame_number', c_int),
    ('block_align', c_int),
    ('cutoff', c_int),
    ('channel_layout', c_uint64),
    ('request_channel_layout', c_uint64),
    ('audio_service_type', enum_AVAudioServiceType),
    ('request_sample_fmt', enum_AVSampleFormat),
    ('get_buffer2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(AVFrame), c_int)),
    ('refcounted_frames', c_int),
    ('qcompress', c_float),
    ('qblur', c_float),
    ('qmin', c_int),
    ('qmax', c_int),
    ('max_qdiff', c_int),
    ('rc_buffer_size', c_int),
    ('rc_override_count', c_int),
    ('rc_override', POINTER(RcOverride)),
    ('rc_max_rate', c_int64),
    ('rc_min_rate', c_int64),
    ('rc_max_available_vbv_use', c_float),
    ('rc_min_vbv_overflow_use', c_float),
    ('rc_initial_buffer_occupancy', c_int),
    ('coder_type', c_int),
    ('context_model', c_int),
    ('frame_skip_threshold', c_int),
    ('frame_skip_factor', c_int),
    ('frame_skip_exp', c_int),
    ('frame_skip_cmp', c_int),
    ('trellis', c_int),
    ('min_prediction_order', c_int),
    ('max_prediction_order', c_int),
    ('timecode_frame_start', c_int64),
    ('rtp_callback', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVCodecContext), POINTER(None), c_int, c_int)),
    ('rtp_payload_size', c_int),
    ('mv_bits', c_int),
    ('header_bits', c_int),
    ('i_tex_bits', c_int),
    ('p_tex_bits', c_int),
    ('i_count', c_int),
    ('p_count', c_int),
    ('skip_count', c_int),
    ('misc_bits', c_int),
    ('frame_bits', c_int),
    ('stats_out', String),
    ('stats_in', String),
    ('workaround_bugs', c_int),
    ('strict_std_compliance', c_int),
    ('error_concealment', c_int),
    ('debug', c_int),
    ('err_recognition', c_int),
    ('reordered_opaque', c_int64),
    ('hwaccel', POINTER(struct_AVHWAccel)),
    ('hwaccel_context', POINTER(None)),
    ('error', c_uint64 * int(8)),
    ('dct_algo', c_int),
    ('idct_algo', c_int),
    ('bits_per_coded_sample', c_int),
    ('bits_per_raw_sample', c_int),
    ('lowres', c_int),
    ('coded_frame', POINTER(AVFrame)),
    ('thread_count', c_int),
    ('thread_type', c_int),
    ('active_thread_type', c_int),
    ('thread_safe_callbacks', c_int),
    ('execute', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(None)), POINTER(None), POINTER(c_int), c_int, c_int)),
    ('execute2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(None), c_int, c_int), POINTER(None), POINTER(c_int), c_int)),
    ('nsse_weight', c_int),
    ('profile', c_int),
    ('level', c_int),
    ('skip_loop_filter', enum_AVDiscard),
    ('skip_idct', enum_AVDiscard),
    ('skip_frame', enum_AVDiscard),
    ('subtitle_header', POINTER(c_uint8)),
    ('subtitle_header_size', c_int),
    ('vbv_delay', c_uint64),
    ('side_data_only_packets', c_int),
    ('initial_padding', c_int),
    ('framerate', AVRational),
    ('sw_pix_fmt', enum_AVPixelFormat),
    ('pkt_timebase', AVRational),
    ('codec_descriptor', POINTER(AVCodecDescriptor)),
    ('pts_correction_num_faulty_pts', c_int64),
    ('pts_correction_num_faulty_dts', c_int64),
    ('pts_correction_last_pts', c_int64),
    ('pts_correction_last_dts', c_int64),
    ('sub_charenc', String),
    ('sub_charenc_mode', c_int),
    ('skip_alpha', c_int),
    ('seek_preroll', c_int),
    ('debug_mv', c_int),
    ('chroma_intra_matrix', POINTER(c_uint16)),
    ('dump_separator', POINTER(c_uint8)),
    ('codec_whitelist', String),
    ('properties', c_uint),
    ('coded_side_data', POINTER(AVPacketSideData)),
    ('nb_coded_side_data', c_int),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('sub_text_format', c_int),
    ('trailing_padding', c_int),
    ('max_pixels', c_int64),
    ('hw_device_ctx', POINTER(AVBufferRef)),
    ('hwaccel_flags', c_int),
    ('apply_cropping', c_int),
    ('extra_hw_frames', c_int),
    ('discard_damaged_percentage', c_int),
    ('max_samples', c_int64),
    ('export_side_data', c_int),
    ('get_encode_buffer', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(AVPacket), c_int)),
]

AVCodecContext = struct_AVCodecContext# /usr/include/libavcodec/avcodec.h: 2385

# /usr/include/libavcodec/avcodec.h: 2393
if _libs["avcodec"].has("av_codec_get_pkt_timebase", "cdecl"):
    av_codec_get_pkt_timebase = _libs["avcodec"].get("av_codec_get_pkt_timebase", "cdecl")
    av_codec_get_pkt_timebase.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_pkt_timebase.restype = AVRational

# /usr/include/libavcodec/avcodec.h: 2395
if _libs["avcodec"].has("av_codec_set_pkt_timebase", "cdecl"):
    av_codec_set_pkt_timebase = _libs["avcodec"].get("av_codec_set_pkt_timebase", "cdecl")
    av_codec_set_pkt_timebase.argtypes = [POINTER(AVCodecContext), AVRational]
    av_codec_set_pkt_timebase.restype = None

# /usr/include/libavcodec/avcodec.h: 2398
if _libs["avcodec"].has("av_codec_get_codec_descriptor", "cdecl"):
    av_codec_get_codec_descriptor = _libs["avcodec"].get("av_codec_get_codec_descriptor", "cdecl")
    av_codec_get_codec_descriptor.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_codec_descriptor.restype = POINTER(AVCodecDescriptor)

# /usr/include/libavcodec/avcodec.h: 2400
if _libs["avcodec"].has("av_codec_set_codec_descriptor", "cdecl"):
    av_codec_set_codec_descriptor = _libs["avcodec"].get("av_codec_set_codec_descriptor", "cdecl")
    av_codec_set_codec_descriptor.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecDescriptor)]
    av_codec_set_codec_descriptor.restype = None

# /usr/include/libavcodec/avcodec.h: 2403
if _libs["avcodec"].has("av_codec_get_codec_properties", "cdecl"):
    av_codec_get_codec_properties = _libs["avcodec"].get("av_codec_get_codec_properties", "cdecl")
    av_codec_get_codec_properties.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_codec_properties.restype = c_uint

# /usr/include/libavcodec/avcodec.h: 2406
if _libs["avcodec"].has("av_codec_get_lowres", "cdecl"):
    av_codec_get_lowres = _libs["avcodec"].get("av_codec_get_lowres", "cdecl")
    av_codec_get_lowres.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_lowres.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2408
if _libs["avcodec"].has("av_codec_set_lowres", "cdecl"):
    av_codec_set_lowres = _libs["avcodec"].get("av_codec_set_lowres", "cdecl")
    av_codec_set_lowres.argtypes = [POINTER(AVCodecContext), c_int]
    av_codec_set_lowres.restype = None

# /usr/include/libavcodec/avcodec.h: 2411
if _libs["avcodec"].has("av_codec_get_seek_preroll", "cdecl"):
    av_codec_get_seek_preroll = _libs["avcodec"].get("av_codec_get_seek_preroll", "cdecl")
    av_codec_get_seek_preroll.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_seek_preroll.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2413
if _libs["avcodec"].has("av_codec_set_seek_preroll", "cdecl"):
    av_codec_set_seek_preroll = _libs["avcodec"].get("av_codec_set_seek_preroll", "cdecl")
    av_codec_set_seek_preroll.argtypes = [POINTER(AVCodecContext), c_int]
    av_codec_set_seek_preroll.restype = None

# /usr/include/libavcodec/avcodec.h: 2416
if _libs["avcodec"].has("av_codec_get_chroma_intra_matrix", "cdecl"):
    av_codec_get_chroma_intra_matrix = _libs["avcodec"].get("av_codec_get_chroma_intra_matrix", "cdecl")
    av_codec_get_chroma_intra_matrix.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_chroma_intra_matrix.restype = POINTER(c_uint16)

# /usr/include/libavcodec/avcodec.h: 2418
if _libs["avcodec"].has("av_codec_set_chroma_intra_matrix", "cdecl"):
    av_codec_set_chroma_intra_matrix = _libs["avcodec"].get("av_codec_set_chroma_intra_matrix", "cdecl")
    av_codec_set_chroma_intra_matrix.argtypes = [POINTER(AVCodecContext), POINTER(c_uint16)]
    av_codec_set_chroma_intra_matrix.restype = None

# /usr/include/libavcodec/avcodec.h: 2425
if _libs["avcodec"].has("av_codec_get_max_lowres", "cdecl"):
    av_codec_get_max_lowres = _libs["avcodec"].get("av_codec_get_max_lowres", "cdecl")
    av_codec_get_max_lowres.argtypes = [POINTER(AVCodec)]
    av_codec_get_max_lowres.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2428
class struct_MpegEncContext(Structure):
    pass

struct_AVHWAccel.__slots__ = [
    'name',
    'type',
    'id',
    'pix_fmt',
    'capabilities',
    'alloc_frame',
    'start_frame',
    'decode_params',
    'decode_slice',
    'end_frame',
    'frame_priv_data_size',
    'decode_mb',
    'init',
    'uninit',
    'priv_data_size',
    'caps_internal',
    'frame_params',
]
struct_AVHWAccel._fields_ = [
    ('name', String),
    ('type', enum_AVMediaType),
    ('id', enum_AVCodecID),
    ('pix_fmt', enum_AVPixelFormat),
    ('capabilities', c_int),
    ('alloc_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(AVFrame))),
    ('start_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(c_uint8), c_uint32)),
    ('decode_params', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), c_int, POINTER(c_uint8), c_uint32)),
    ('decode_slice', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(c_uint8), c_uint32)),
    ('end_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('frame_priv_data_size', c_int),
    ('decode_mb', CFUNCTYPE(UNCHECKED(None), POINTER(struct_MpegEncContext))),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('uninit', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('priv_data_size', c_int),
    ('caps_internal', c_int),
    ('frame_params', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(AVBufferRef))),
]

AVHWAccel = struct_AVHWAccel# /usr/include/libavcodec/avcodec.h: 2598

# /usr/include/libavcodec/avcodec.h: 2660
class struct_AVPicture(Structure):
    pass

struct_AVPicture.__slots__ = [
    'data',
    'linesize',
]
struct_AVPicture._fields_ = [
    ('data', POINTER(c_uint8) * int(8)),
    ('linesize', c_int * int(8)),
]

AVPicture = struct_AVPicture# /usr/include/libavcodec/avcodec.h: 2660

enum_AVSubtitleType = c_int# /usr/include/libavcodec/avcodec.h: 2667

SUBTITLE_NONE = 0# /usr/include/libavcodec/avcodec.h: 2667

SUBTITLE_BITMAP = (SUBTITLE_NONE + 1)# /usr/include/libavcodec/avcodec.h: 2667

SUBTITLE_TEXT = (SUBTITLE_BITMAP + 1)# /usr/include/libavcodec/avcodec.h: 2667

SUBTITLE_ASS = (SUBTITLE_TEXT + 1)# /usr/include/libavcodec/avcodec.h: 2667

# /usr/include/libavcodec/avcodec.h: 2720
class struct_AVSubtitleRect(Structure):
    pass

struct_AVSubtitleRect.__slots__ = [
    'x',
    'y',
    'w',
    'h',
    'nb_colors',
    'pict',
    'data',
    'linesize',
    'type',
    'text',
    'ass',
    'flags',
]
struct_AVSubtitleRect._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('w', c_int),
    ('h', c_int),
    ('nb_colors', c_int),
    ('pict', AVPicture),
    ('data', POINTER(c_uint8) * int(4)),
    ('linesize', c_int * int(4)),
    ('type', enum_AVSubtitleType),
    ('text', String),
    ('ass', String),
    ('flags', c_int),
]

AVSubtitleRect = struct_AVSubtitleRect# /usr/include/libavcodec/avcodec.h: 2720

struct_AVSubtitle.__slots__ = [
    'format',
    'start_display_time',
    'end_display_time',
    'num_rects',
    'rects',
    'pts',
]
struct_AVSubtitle._fields_ = [
    ('format', c_uint16),
    ('start_display_time', c_uint32),
    ('end_display_time', c_uint32),
    ('num_rects', c_uint),
    ('rects', POINTER(POINTER(AVSubtitleRect))),
    ('pts', c_int64),
]

AVSubtitle = struct_AVSubtitle# /usr/include/libavcodec/avcodec.h: 2729

# /usr/include/libavcodec/avcodec.h: 2738
if _libs["avcodec"].has("av_codec_next", "cdecl"):
    av_codec_next = _libs["avcodec"].get("av_codec_next", "cdecl")
    av_codec_next.argtypes = [POINTER(AVCodec)]
    av_codec_next.restype = POINTER(AVCodec)

# /usr/include/libavcodec/avcodec.h: 2744
if _libs["avcodec"].has("avcodec_version", "cdecl"):
    avcodec_version = _libs["avcodec"].get("avcodec_version", "cdecl")
    avcodec_version.argtypes = []
    avcodec_version.restype = c_uint

# /usr/include/libavcodec/avcodec.h: 2749
if _libs["avcodec"].has("avcodec_configuration", "cdecl"):
    avcodec_configuration = _libs["avcodec"].get("avcodec_configuration", "cdecl")
    avcodec_configuration.argtypes = []
    avcodec_configuration.restype = c_char_p

# /usr/include/libavcodec/avcodec.h: 2754
if _libs["avcodec"].has("avcodec_license", "cdecl"):
    avcodec_license = _libs["avcodec"].get("avcodec_license", "cdecl")
    avcodec_license.argtypes = []
    avcodec_license.restype = c_char_p

# /usr/include/libavcodec/avcodec.h: 2761
if _libs["avcodec"].has("avcodec_register", "cdecl"):
    avcodec_register = _libs["avcodec"].get("avcodec_register", "cdecl")
    avcodec_register.argtypes = [POINTER(AVCodec)]
    avcodec_register.restype = None

# /usr/include/libavcodec/avcodec.h: 2767
if _libs["avcodec"].has("avcodec_register_all", "cdecl"):
    avcodec_register_all = _libs["avcodec"].get("avcodec_register_all", "cdecl")
    avcodec_register_all.argtypes = []
    avcodec_register_all.restype = None

# /usr/include/libavcodec/avcodec.h: 2783
if _libs["avcodec"].has("avcodec_alloc_context3", "cdecl"):
    avcodec_alloc_context3 = _libs["avcodec"].get("avcodec_alloc_context3", "cdecl")
    avcodec_alloc_context3.argtypes = [POINTER(AVCodec)]
    avcodec_alloc_context3.restype = POINTER(AVCodecContext)

# /usr/include/libavcodec/avcodec.h: 2789
if _libs["avcodec"].has("avcodec_free_context", "cdecl"):
    avcodec_free_context = _libs["avcodec"].get("avcodec_free_context", "cdecl")
    avcodec_free_context.argtypes = [POINTER(POINTER(AVCodecContext))]
    avcodec_free_context.restype = None

# /usr/include/libavcodec/avcodec.h: 2797
if _libs["avcodec"].has("avcodec_get_context_defaults3", "cdecl"):
    avcodec_get_context_defaults3 = _libs["avcodec"].get("avcodec_get_context_defaults3", "cdecl")
    avcodec_get_context_defaults3.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec)]
    avcodec_get_context_defaults3.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2806
if _libs["avcodec"].has("avcodec_get_class", "cdecl"):
    avcodec_get_class = _libs["avcodec"].get("avcodec_get_class", "cdecl")
    avcodec_get_class.argtypes = []
    avcodec_get_class.restype = POINTER(AVClass)

# /usr/include/libavcodec/avcodec.h: 2813
if _libs["avcodec"].has("avcodec_get_frame_class", "cdecl"):
    avcodec_get_frame_class = _libs["avcodec"].get("avcodec_get_frame_class", "cdecl")
    avcodec_get_frame_class.argtypes = []
    avcodec_get_frame_class.restype = POINTER(AVClass)

# /usr/include/libavcodec/avcodec.h: 2822
if _libs["avcodec"].has("avcodec_get_subtitle_rect_class", "cdecl"):
    avcodec_get_subtitle_rect_class = _libs["avcodec"].get("avcodec_get_subtitle_rect_class", "cdecl")
    avcodec_get_subtitle_rect_class.argtypes = []
    avcodec_get_subtitle_rect_class.restype = POINTER(AVClass)

# /usr/include/libavcodec/avcodec.h: 2843
if _libs["avcodec"].has("avcodec_copy_context", "cdecl"):
    avcodec_copy_context = _libs["avcodec"].get("avcodec_copy_context", "cdecl")
    avcodec_copy_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecContext)]
    avcodec_copy_context.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2853
if _libs["avcodec"].has("avcodec_parameters_from_context", "cdecl"):
    avcodec_parameters_from_context = _libs["avcodec"].get("avcodec_parameters_from_context", "cdecl")
    avcodec_parameters_from_context.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecContext)]
    avcodec_parameters_from_context.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2864
if _libs["avcodec"].has("avcodec_parameters_to_context", "cdecl"):
    avcodec_parameters_to_context = _libs["avcodec"].get("avcodec_parameters_to_context", "cdecl")
    # avcodec_parameters_to_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecParameters)]
    avcodec_parameters_to_context.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2904
if _libs["avcodec"].has("avcodec_open2", "cdecl"):
    avcodec_open2 = _libs["avcodec"].get("avcodec_open2", "cdecl")
    # avcodec_open2.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec), POINTER(POINTER(AVDictionary))]
    avcodec_open2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2919
if _libs["avcodec"].has("avcodec_close", "cdecl"):
    avcodec_close = _libs["avcodec"].get("avcodec_close", "cdecl")
    avcodec_close.argtypes = [POINTER(AVCodecContext)]
    avcodec_close.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2926
if _libs["avcodec"].has("avsubtitle_free", "cdecl"):
    avsubtitle_free = _libs["avcodec"].get("avsubtitle_free", "cdecl")
    avsubtitle_free.argtypes = [POINTER(AVSubtitle)]
    avsubtitle_free.restype = None

# /usr/include/libavcodec/avcodec.h: 2942
if _libs["avcodec"].has("avcodec_default_get_buffer2", "cdecl"):
    avcodec_default_get_buffer2 = _libs["avcodec"].get("avcodec_default_get_buffer2", "cdecl")
    avcodec_default_get_buffer2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), c_int]
    avcodec_default_get_buffer2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2949
if _libs["avcodec"].has("avcodec_default_get_encode_buffer", "cdecl"):
    avcodec_default_get_encode_buffer = _libs["avcodec"].get("avcodec_default_get_encode_buffer", "cdecl")
    avcodec_default_get_encode_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), c_int]
    avcodec_default_get_encode_buffer.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2958
if _libs["avcodec"].has("avcodec_align_dimensions", "cdecl"):
    avcodec_align_dimensions = _libs["avcodec"].get("avcodec_align_dimensions", "cdecl")
    avcodec_align_dimensions.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int)]
    avcodec_align_dimensions.restype = None

# /usr/include/libavcodec/avcodec.h: 2967
if _libs["avcodec"].has("avcodec_align_dimensions2", "cdecl"):
    avcodec_align_dimensions2 = _libs["avcodec"].get("avcodec_align_dimensions2", "cdecl")
    avcodec_align_dimensions2.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int), c_int * int(8)]
    avcodec_align_dimensions2.restype = None

# /usr/include/libavcodec/avcodec.h: 2979
if _libs["avcodec"].has("avcodec_enum_to_chroma_pos", "cdecl"):
    avcodec_enum_to_chroma_pos = _libs["avcodec"].get("avcodec_enum_to_chroma_pos", "cdecl")
    avcodec_enum_to_chroma_pos.argtypes = [POINTER(c_int), POINTER(c_int), enum_AVChromaLocation]
    avcodec_enum_to_chroma_pos.restype = c_int

# /usr/include/libavcodec/avcodec.h: 2990
if _libs["avcodec"].has("avcodec_chroma_pos_to_enum", "cdecl"):
    avcodec_chroma_pos_to_enum = _libs["avcodec"].get("avcodec_chroma_pos_to_enum", "cdecl")
    avcodec_chroma_pos_to_enum.argtypes = [c_int, c_int]
    avcodec_chroma_pos_to_enum.restype = enum_AVChromaLocation

# /usr/include/libavcodec/avcodec.h: 3047
if _libs["avcodec"].has("avcodec_decode_audio4", "cdecl"):
    avcodec_decode_audio4 = _libs["avcodec"].get("avcodec_decode_audio4", "cdecl")
    avcodec_decode_audio4.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_audio4.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3096
if _libs["avcodec"].has("avcodec_decode_video2", "cdecl"):
    avcodec_decode_video2 = _libs["avcodec"].get("avcodec_decode_video2", "cdecl")
    avcodec_decode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_video2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3128
if _libs["avcodec"].has("avcodec_decode_subtitle2", "cdecl"):
    avcodec_decode_subtitle2 = _libs["avcodec"].get("avcodec_decode_subtitle2", "cdecl")
    avcodec_decode_subtitle2.argtypes = [POINTER(AVCodecContext), POINTER(AVSubtitle), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_subtitle2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3182
if _libs["avcodec"].has("avcodec_send_packet", "cdecl"):
    avcodec_send_packet = _libs["avcodec"].get("avcodec_send_packet", "cdecl")
    avcodec_send_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_send_packet.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3205
if _libs["avcodec"].has("avcodec_receive_frame", "cdecl"):
    avcodec_receive_frame = _libs["avcodec"].get("avcodec_receive_frame", "cdecl")
    # avcodec_receive_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_receive_frame.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3242
if _libs["avcodec"].has("avcodec_send_frame", "cdecl"):
    avcodec_send_frame = _libs["avcodec"].get("avcodec_send_frame", "cdecl")
    avcodec_send_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_send_frame.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3259
if _libs["avcodec"].has("avcodec_receive_packet", "cdecl"):
    avcodec_receive_packet = _libs["avcodec"].get("avcodec_receive_packet", "cdecl")
    avcodec_receive_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_receive_packet.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3358
if _libs["avcodec"].has("avcodec_get_hw_frames_parameters", "cdecl"):
    avcodec_get_hw_frames_parameters = _libs["avcodec"].get("avcodec_get_hw_frames_parameters", "cdecl")
    avcodec_get_hw_frames_parameters.argtypes = [POINTER(AVCodecContext), POINTER(AVBufferRef), enum_AVPixelFormat, POINTER(POINTER(AVBufferRef))]
    avcodec_get_hw_frames_parameters.restype = c_int

enum_AVPictureStructure = c_int# /usr/include/libavcodec/avcodec.h: 3370

AV_PICTURE_STRUCTURE_UNKNOWN = 0# /usr/include/libavcodec/avcodec.h: 3370

AV_PICTURE_STRUCTURE_TOP_FIELD = (AV_PICTURE_STRUCTURE_UNKNOWN + 1)# /usr/include/libavcodec/avcodec.h: 3370

AV_PICTURE_STRUCTURE_BOTTOM_FIELD = (AV_PICTURE_STRUCTURE_TOP_FIELD + 1)# /usr/include/libavcodec/avcodec.h: 3370

AV_PICTURE_STRUCTURE_FRAME = (AV_PICTURE_STRUCTURE_BOTTOM_FIELD + 1)# /usr/include/libavcodec/avcodec.h: 3370

# /usr/include/libavcodec/avcodec.h: 3544
class struct_AVCodecParser(Structure):
    pass

# /usr/include/libavcodec/avcodec.h: 3542
class struct_AVCodecParserContext(Structure):
    pass

struct_AVCodecParserContext.__slots__ = [
    'priv_data',
    'parser',
    'frame_offset',
    'cur_offset',
    'next_frame_offset',
    'pict_type',
    'repeat_pict',
    'pts',
    'dts',
    'last_pts',
    'last_dts',
    'fetch_timestamp',
    'cur_frame_start_index',
    'cur_frame_offset',
    'cur_frame_pts',
    'cur_frame_dts',
    'flags',
    'offset',
    'cur_frame_end',
    'key_frame',
    'convergence_duration',
    'dts_sync_point',
    'dts_ref_dts_delta',
    'pts_dts_delta',
    'cur_frame_pos',
    'pos',
    'last_pos',
    'duration',
    'field_order',
    'picture_structure',
    'output_picture_number',
    'width',
    'height',
    'coded_width',
    'coded_height',
    'format',
]
struct_AVCodecParserContext._fields_ = [
    ('priv_data', POINTER(None)),
    ('parser', POINTER(struct_AVCodecParser)),
    ('frame_offset', c_int64),
    ('cur_offset', c_int64),
    ('next_frame_offset', c_int64),
    ('pict_type', c_int),
    ('repeat_pict', c_int),
    ('pts', c_int64),
    ('dts', c_int64),
    ('last_pts', c_int64),
    ('last_dts', c_int64),
    ('fetch_timestamp', c_int),
    ('cur_frame_start_index', c_int),
    ('cur_frame_offset', c_int64 * int(4)),
    ('cur_frame_pts', c_int64 * int(4)),
    ('cur_frame_dts', c_int64 * int(4)),
    ('flags', c_int),
    ('offset', c_int64),
    ('cur_frame_end', c_int64 * int(4)),
    ('key_frame', c_int),
    ('convergence_duration', c_int64),
    ('dts_sync_point', c_int),
    ('dts_ref_dts_delta', c_int),
    ('pts_dts_delta', c_int),
    ('cur_frame_pos', c_int64 * int(4)),
    ('pos', c_int64),
    ('last_pos', c_int64),
    ('duration', c_int),
    ('field_order', enum_AVFieldOrder),
    ('picture_structure', enum_AVPictureStructure),
    ('output_picture_number', c_int),
    ('width', c_int),
    ('height', c_int),
    ('coded_width', c_int),
    ('coded_height', c_int),
    ('format', c_int),
]

AVCodecParserContext = struct_AVCodecParserContext# /usr/include/libavcodec/avcodec.h: 3542

struct_AVCodecParser.__slots__ = [
    'codec_ids',
    'priv_data_size',
    'parser_init',
    'parser_parse',
    'parser_close',
    'split',
    'next',
]
struct_AVCodecParser._fields_ = [
    ('codec_ids', c_int * int(5)),
    ('priv_data_size', c_int),
    ('parser_init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecParserContext))),
    ('parser_parse', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int)),
    ('parser_close', CFUNCTYPE(UNCHECKED(None), POINTER(AVCodecParserContext))),
    ('split', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(c_uint8), c_int)),
    ('next', POINTER(struct_AVCodecParser)),
]

AVCodecParser = struct_AVCodecParser# /usr/include/libavcodec/avcodec.h: 3560

# /usr/include/libavcodec/avcodec.h: 3571
if _libs["avcodec"].has("av_parser_iterate", "cdecl"):
    av_parser_iterate = _libs["avcodec"].get("av_parser_iterate", "cdecl")
    av_parser_iterate.argtypes = [POINTER(POINTER(None))]
    av_parser_iterate.restype = POINTER(AVCodecParser)

# /usr/include/libavcodec/avcodec.h: 3575
if _libs["avcodec"].has("av_parser_next", "cdecl"):
    av_parser_next = _libs["avcodec"].get("av_parser_next", "cdecl")
    av_parser_next.argtypes = [POINTER(AVCodecParser)]
    av_parser_next.restype = POINTER(AVCodecParser)

# /usr/include/libavcodec/avcodec.h: 3578
if _libs["avcodec"].has("av_register_codec_parser", "cdecl"):
    av_register_codec_parser = _libs["avcodec"].get("av_register_codec_parser", "cdecl")
    av_register_codec_parser.argtypes = [POINTER(AVCodecParser)]
    av_register_codec_parser.restype = None

# /usr/include/libavcodec/avcodec.h: 3580
if _libs["avcodec"].has("av_parser_init", "cdecl"):
    av_parser_init = _libs["avcodec"].get("av_parser_init", "cdecl")
    av_parser_init.argtypes = [c_int]
    av_parser_init.restype = POINTER(AVCodecParserContext)

# /usr/include/libavcodec/avcodec.h: 3613
if _libs["avcodec"].has("av_parser_parse2", "cdecl"):
    av_parser_parse2 = _libs["avcodec"].get("av_parser_parse2", "cdecl")
    av_parser_parse2.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int64, c_int64, c_int64]
    av_parser_parse2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3627
if _libs["avcodec"].has("av_parser_change", "cdecl"):
    av_parser_change = _libs["avcodec"].get("av_parser_change", "cdecl")
    av_parser_change.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int]
    av_parser_change.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3632
if _libs["avcodec"].has("av_parser_close", "cdecl"):
    av_parser_close = _libs["avcodec"].get("av_parser_close", "cdecl")
    av_parser_close.argtypes = [POINTER(AVCodecParserContext)]
    av_parser_close.restype = None

# /usr/include/libavcodec/avcodec.h: 3688
if _libs["avcodec"].has("avcodec_encode_audio2", "cdecl"):
    avcodec_encode_audio2 = _libs["avcodec"].get("avcodec_encode_audio2", "cdecl")
    avcodec_encode_audio2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
    avcodec_encode_audio2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3729
if _libs["avcodec"].has("avcodec_encode_video2", "cdecl"):
    avcodec_encode_video2 = _libs["avcodec"].get("avcodec_encode_video2", "cdecl")
    avcodec_encode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
    avcodec_encode_video2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3733
if _libs["avcodec"].has("avcodec_encode_subtitle", "cdecl"):
    avcodec_encode_subtitle = _libs["avcodec"].get("avcodec_encode_subtitle", "cdecl")
    avcodec_encode_subtitle.argtypes = [POINTER(AVCodecContext), POINTER(c_uint8), c_int, POINTER(AVSubtitle)]
    avcodec_encode_subtitle.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3751
if _libs["avcodec"].has("avpicture_alloc", "cdecl"):
    avpicture_alloc = _libs["avcodec"].get("avpicture_alloc", "cdecl")
    avpicture_alloc.argtypes = [POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    avpicture_alloc.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3757
if _libs["avcodec"].has("avpicture_free", "cdecl"):
    avpicture_free = _libs["avcodec"].get("avpicture_free", "cdecl")
    avpicture_free.argtypes = [POINTER(AVPicture)]
    avpicture_free.restype = None

# /usr/include/libavcodec/avcodec.h: 3763
if _libs["avcodec"].has("avpicture_fill", "cdecl"):
    avpicture_fill = _libs["avcodec"].get("avpicture_fill", "cdecl")
    avpicture_fill.argtypes = [POINTER(AVPicture), POINTER(c_uint8), enum_AVPixelFormat, c_int, c_int]
    avpicture_fill.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3770
if _libs["avcodec"].has("avpicture_layout", "cdecl"):
    avpicture_layout = _libs["avcodec"].get("avpicture_layout", "cdecl")
    avpicture_layout.argtypes = [POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int, POINTER(c_ubyte), c_int]
    avpicture_layout.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3778
if _libs["avcodec"].has("avpicture_get_size", "cdecl"):
    avpicture_get_size = _libs["avcodec"].get("avpicture_get_size", "cdecl")
    avpicture_get_size.argtypes = [enum_AVPixelFormat, c_int, c_int]
    avpicture_get_size.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3784
if _libs["avcodec"].has("av_picture_copy", "cdecl"):
    av_picture_copy = _libs["avcodec"].get("av_picture_copy", "cdecl")
    av_picture_copy.argtypes = [POINTER(AVPicture), POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    av_picture_copy.restype = None

# /usr/include/libavcodec/avcodec.h: 3791
if _libs["avcodec"].has("av_picture_crop", "cdecl"):
    av_picture_crop = _libs["avcodec"].get("av_picture_crop", "cdecl")
    av_picture_crop.argtypes = [POINTER(AVPicture), POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    av_picture_crop.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3798
if _libs["avcodec"].has("av_picture_pad", "cdecl"):
    av_picture_pad = _libs["avcodec"].get("av_picture_pad", "cdecl")
    av_picture_pad.argtypes = [POINTER(AVPicture), POINTER(AVPicture), c_int, c_int, enum_AVPixelFormat, c_int, c_int, c_int, c_int, POINTER(c_int)]
    av_picture_pad.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3828
if _libs["avcodec"].has("avcodec_get_chroma_sub_sample", "cdecl"):
    avcodec_get_chroma_sub_sample = _libs["avcodec"].get("avcodec_get_chroma_sub_sample", "cdecl")
    avcodec_get_chroma_sub_sample.argtypes = [enum_AVPixelFormat, POINTER(c_int), POINTER(c_int)]
    avcodec_get_chroma_sub_sample.restype = None

# /usr/include/libavcodec/avcodec.h: 3836
if _libs["avcodec"].has("avcodec_pix_fmt_to_codec_tag", "cdecl"):
    avcodec_pix_fmt_to_codec_tag = _libs["avcodec"].get("avcodec_pix_fmt_to_codec_tag", "cdecl")
    avcodec_pix_fmt_to_codec_tag.argtypes = [enum_AVPixelFormat]
    avcodec_pix_fmt_to_codec_tag.restype = c_uint

# /usr/include/libavcodec/avcodec.h: 3855
if _libs["avcodec"].has("avcodec_find_best_pix_fmt_of_list", "cdecl"):
    avcodec_find_best_pix_fmt_of_list = _libs["avcodec"].get("avcodec_find_best_pix_fmt_of_list", "cdecl")
    avcodec_find_best_pix_fmt_of_list.argtypes = [POINTER(enum_AVPixelFormat), enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt_of_list.restype = enum_AVPixelFormat

# /usr/include/libavcodec/avcodec.h: 3864
if _libs["avcodec"].has("avcodec_get_pix_fmt_loss", "cdecl"):
    avcodec_get_pix_fmt_loss = _libs["avcodec"].get("avcodec_get_pix_fmt_loss", "cdecl")
    avcodec_get_pix_fmt_loss.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, c_int]
    avcodec_get_pix_fmt_loss.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3870
if _libs["avcodec"].has("avcodec_find_best_pix_fmt_of_2", "cdecl"):
    avcodec_find_best_pix_fmt_of_2 = _libs["avcodec"].get("avcodec_find_best_pix_fmt_of_2", "cdecl")
    avcodec_find_best_pix_fmt_of_2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt_of_2.restype = enum_AVPixelFormat

# /usr/include/libavcodec/avcodec.h: 3874
if _libs["avcodec"].has("avcodec_find_best_pix_fmt2", "cdecl"):
    avcodec_find_best_pix_fmt2 = _libs["avcodec"].get("avcodec_find_best_pix_fmt2", "cdecl")
    avcodec_find_best_pix_fmt2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt2.restype = enum_AVPixelFormat

# /usr/include/libavcodec/avcodec.h: 3878
if _libs["avcodec"].has("avcodec_default_get_format", "cdecl"):
    avcodec_default_get_format = _libs["avcodec"].get("avcodec_default_get_format", "cdecl")
    avcodec_default_get_format.argtypes = [POINTER(struct_AVCodecContext), POINTER(enum_AVPixelFormat)]
    avcodec_default_get_format.restype = enum_AVPixelFormat

# /usr/include/libavcodec/avcodec.h: 3897
if _libs["avcodec"].has("av_get_codec_tag_string", "cdecl"):
    av_get_codec_tag_string = _libs["avcodec"].get("av_get_codec_tag_string", "cdecl")
    av_get_codec_tag_string.argtypes = [String, c_size_t, c_uint]
    av_get_codec_tag_string.restype = c_size_t

# /usr/include/libavcodec/avcodec.h: 3900
if _libs["avcodec"].has("avcodec_string", "cdecl"):
    avcodec_string = _libs["avcodec"].get("avcodec_string", "cdecl")
    avcodec_string.argtypes = [String, c_int, POINTER(AVCodecContext), c_int]
    avcodec_string.restype = None

# /usr/include/libavcodec/avcodec.h: 3909
if _libs["avcodec"].has("av_get_profile_name", "cdecl"):
    av_get_profile_name = _libs["avcodec"].get("av_get_profile_name", "cdecl")
    av_get_profile_name.argtypes = [POINTER(AVCodec), c_int]
    av_get_profile_name.restype = c_char_p

# /usr/include/libavcodec/avcodec.h: 3922
if _libs["avcodec"].has("avcodec_profile_name", "cdecl"):
    avcodec_profile_name = _libs["avcodec"].get("avcodec_profile_name", "cdecl")
    avcodec_profile_name.argtypes = [enum_AVCodecID, c_int]
    avcodec_profile_name.restype = c_char_p

# /usr/include/libavcodec/avcodec.h: 3924
if _libs["avcodec"].has("avcodec_default_execute", "cdecl"):
    avcodec_default_execute = _libs["avcodec"].get("avcodec_default_execute", "cdecl")
    avcodec_default_execute.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None)), POINTER(None), POINTER(c_int), c_int, c_int]
    avcodec_default_execute.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3925
if _libs["avcodec"].has("avcodec_default_execute2", "cdecl"):
    avcodec_default_execute2 = _libs["avcodec"].get("avcodec_default_execute2", "cdecl")
    avcodec_default_execute2.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None), c_int, c_int), POINTER(None), POINTER(c_int), c_int]
    avcodec_default_execute2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3951
if _libs["avcodec"].has("avcodec_fill_audio_frame", "cdecl"):
    avcodec_fill_audio_frame = _libs["avcodec"].get("avcodec_fill_audio_frame", "cdecl")
    avcodec_fill_audio_frame.argtypes = [POINTER(AVFrame), c_int, enum_AVSampleFormat, POINTER(c_uint8), c_int, c_int]
    avcodec_fill_audio_frame.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3972
if _libs["avcodec"].has("avcodec_flush_buffers", "cdecl"):
    avcodec_flush_buffers = _libs["avcodec"].get("avcodec_flush_buffers", "cdecl")
    avcodec_flush_buffers.argtypes = [POINTER(AVCodecContext)]
    avcodec_flush_buffers.restype = None

# /usr/include/libavcodec/avcodec.h: 3980
if _libs["avcodec"].has("av_get_bits_per_sample", "cdecl"):
    av_get_bits_per_sample = _libs["avcodec"].get("av_get_bits_per_sample", "cdecl")
    av_get_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_bits_per_sample.restype = c_int

# /usr/include/libavcodec/avcodec.h: 3988
if _libs["avcodec"].has("av_get_pcm_codec", "cdecl"):
    av_get_pcm_codec = _libs["avcodec"].get("av_get_pcm_codec", "cdecl")
    av_get_pcm_codec.argtypes = [enum_AVSampleFormat, c_int]
    av_get_pcm_codec.restype = enum_AVCodecID

# /usr/include/libavcodec/avcodec.h: 3998
if _libs["avcodec"].has("av_get_exact_bits_per_sample", "cdecl"):
    av_get_exact_bits_per_sample = _libs["avcodec"].get("av_get_exact_bits_per_sample", "cdecl")
    av_get_exact_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_exact_bits_per_sample.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4008
if _libs["avcodec"].has("av_get_audio_frame_duration", "cdecl"):
    av_get_audio_frame_duration = _libs["avcodec"].get("av_get_audio_frame_duration", "cdecl")
    av_get_audio_frame_duration.argtypes = [POINTER(AVCodecContext), c_int]
    av_get_audio_frame_duration.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4014
if _libs["avcodec"].has("av_get_audio_frame_duration2", "cdecl"):
    av_get_audio_frame_duration2 = _libs["avcodec"].get("av_get_audio_frame_duration2", "cdecl")
    av_get_audio_frame_duration2.argtypes = [POINTER(AVCodecParameters), c_int]
    av_get_audio_frame_duration2.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4017
class struct_AVBitStreamFilterContext(Structure):
    pass

struct_AVBitStreamFilterContext.__slots__ = [
    'priv_data',
    'filter',
    'parser',
    'next',
    'args',
]
struct_AVBitStreamFilterContext._fields_ = [
    ('priv_data', POINTER(None)),
    ('filter', POINTER(struct_AVBitStreamFilter)),
    ('parser', POINTER(AVCodecParserContext)),
    ('next', POINTER(struct_AVBitStreamFilterContext)),
    ('args', String),
]

AVBitStreamFilterContext = struct_AVBitStreamFilterContext# /usr/include/libavcodec/avcodec.h: 4027

# /usr/include/libavcodec/avcodec.h: 4034
if _libs["avcodec"].has("av_register_bitstream_filter", "cdecl"):
    av_register_bitstream_filter = _libs["avcodec"].get("av_register_bitstream_filter", "cdecl")
    av_register_bitstream_filter.argtypes = [POINTER(AVBitStreamFilter)]
    av_register_bitstream_filter.restype = None

# /usr/include/libavcodec/avcodec.h: 4041
if _libs["avcodec"].has("av_bitstream_filter_init", "cdecl"):
    av_bitstream_filter_init = _libs["avcodec"].get("av_bitstream_filter_init", "cdecl")
    av_bitstream_filter_init.argtypes = [String]
    av_bitstream_filter_init.restype = POINTER(AVBitStreamFilterContext)

# /usr/include/libavcodec/avcodec.h: 4048
if _libs["avcodec"].has("av_bitstream_filter_filter", "cdecl"):
    av_bitstream_filter_filter = _libs["avcodec"].get("av_bitstream_filter_filter", "cdecl")
    av_bitstream_filter_filter.argtypes = [POINTER(AVBitStreamFilterContext), POINTER(AVCodecContext), String, POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int]
    av_bitstream_filter_filter.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4058
if _libs["avcodec"].has("av_bitstream_filter_close", "cdecl"):
    av_bitstream_filter_close = _libs["avcodec"].get("av_bitstream_filter_close", "cdecl")
    av_bitstream_filter_close.argtypes = [POINTER(AVBitStreamFilterContext)]
    av_bitstream_filter_close.restype = None

# /usr/include/libavcodec/avcodec.h: 4065
if _libs["avcodec"].has("av_bitstream_filter_next", "cdecl"):
    av_bitstream_filter_next = _libs["avcodec"].get("av_bitstream_filter_next", "cdecl")
    av_bitstream_filter_next.argtypes = [POINTER(AVBitStreamFilter)]
    av_bitstream_filter_next.restype = POINTER(AVBitStreamFilter)

# /usr/include/libavcodec/avcodec.h: 4070
if _libs["avcodec"].has("av_bsf_next", "cdecl"):
    av_bsf_next = _libs["avcodec"].get("av_bsf_next", "cdecl")
    av_bsf_next.argtypes = [POINTER(POINTER(None))]
    av_bsf_next.restype = POINTER(AVBitStreamFilter)

# /usr/include/libavcodec/avcodec.h: 4082
if _libs["avcodec"].has("av_fast_padded_malloc", "cdecl"):
    av_fast_padded_malloc = _libs["avcodec"].get("av_fast_padded_malloc", "cdecl")
    av_fast_padded_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_malloc.restype = None

# /usr/include/libavcodec/avcodec.h: 4088
if _libs["avcodec"].has("av_fast_padded_mallocz", "cdecl"):
    av_fast_padded_mallocz = _libs["avcodec"].get("av_fast_padded_mallocz", "cdecl")
    av_fast_padded_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_mallocz.restype = None

# /usr/include/libavcodec/avcodec.h: 4097
if _libs["avcodec"].has("av_xiphlacing", "cdecl"):
    av_xiphlacing = _libs["avcodec"].get("av_xiphlacing", "cdecl")
    av_xiphlacing.argtypes = [POINTER(c_ubyte), c_uint]
    av_xiphlacing.restype = c_uint

# /usr/include/libavcodec/avcodec.h: 4106
if _libs["avcodec"].has("av_register_hwaccel", "cdecl"):
    av_register_hwaccel = _libs["avcodec"].get("av_register_hwaccel", "cdecl")
    av_register_hwaccel.argtypes = [POINTER(AVHWAccel)]
    av_register_hwaccel.restype = None

# /usr/include/libavcodec/avcodec.h: 4117
if _libs["avcodec"].has("av_hwaccel_next", "cdecl"):
    av_hwaccel_next = _libs["avcodec"].get("av_hwaccel_next", "cdecl")
    av_hwaccel_next.argtypes = [POINTER(AVHWAccel)]
    av_hwaccel_next.restype = POINTER(AVHWAccel)

enum_AVLockOp = c_int# /usr/include/libavcodec/avcodec.h: 4126

AV_LOCK_CREATE = 0# /usr/include/libavcodec/avcodec.h: 4126

AV_LOCK_OBTAIN = (AV_LOCK_CREATE + 1)# /usr/include/libavcodec/avcodec.h: 4126

AV_LOCK_RELEASE = (AV_LOCK_OBTAIN + 1)# /usr/include/libavcodec/avcodec.h: 4126

AV_LOCK_DESTROY = (AV_LOCK_RELEASE + 1)# /usr/include/libavcodec/avcodec.h: 4126

# /usr/include/libavcodec/avcodec.h: 4160
if _libs["avcodec"].has("av_lockmgr_register", "cdecl"):
    av_lockmgr_register = _libs["avcodec"].get("av_lockmgr_register", "cdecl")
    av_lockmgr_register.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(None)), enum_AVLockOp)]
    av_lockmgr_register.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4167
if _libs["avcodec"].has("avcodec_is_open", "cdecl"):
    avcodec_is_open = _libs["avcodec"].get("avcodec_is_open", "cdecl")
    avcodec_is_open.argtypes = [POINTER(AVCodecContext)]
    avcodec_is_open.restype = c_int

# /usr/include/libavcodec/avcodec.h: 4178
if _libs["avcodec"].has("av_cpb_properties_alloc", "cdecl"):
    av_cpb_properties_alloc = _libs["avcodec"].get("av_cpb_properties_alloc", "cdecl")
    av_cpb_properties_alloc.argtypes = [POINTER(c_size_t)]
    av_cpb_properties_alloc.restype = POINTER(AVCPBProperties)

enum_AVOptionType = c_int# /usr/include/libavutil/opt.h: 223

# /usr/include/libavutil/opt.h: 267
class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'i64',
    'dbl',
    'str',
    'q',
]
union_anon_29._fields_ = [
    ('i64', c_int64),
    ('dbl', c_double),
    ('str', String),
    ('q', AVRational),
]

struct_AVOption.__slots__ = [
    'name',
    'help',
    'offset',
    'type',
    'default_val',
    'min',
    'max',
    'flags',
    'unit',
]
struct_AVOption._fields_ = [
    ('name', String),
    ('help', String),
    ('offset', c_int),
    ('type', enum_AVOptionType),
    ('default_val', union_anon_29),
    ('min', c_double),
    ('max', c_double),
    ('flags', c_int),
    ('unit', String),
]

# /usr/include/libavutil/opt.h: 328
class struct_AVOptionRange(Structure):
    pass

struct_AVOptionRange.__slots__ = [
    'str',
    'value_min',
    'value_max',
    'component_min',
    'component_max',
    'is_range',
]
struct_AVOptionRange._fields_ = [
    ('str', String),
    ('value_min', c_double),
    ('value_max', c_double),
    ('component_min', c_double),
    ('component_max', c_double),
    ('is_range', c_int),
]

AVOptionRange = struct_AVOptionRange# /usr/include/libavutil/opt.h: 328

struct_AVOptionRanges.__slots__ = [
    'range',
    'nb_ranges',
    'nb_components',
]
struct_AVOptionRanges._fields_ = [
    ('range', POINTER(POINTER(AVOptionRange))),
    ('nb_ranges', c_int),
    ('nb_components', c_int),
]

# /usr/include/libavcodec/avdct.h: 74
class struct_AVDCT(Structure):
    pass

struct_AVDCT.__slots__ = [
    'av_class',
    'idct',
    'idct_permutation',
    'fdct',
    'dct_algo',
    'idct_algo',
    'get_pixels',
    'bits_per_sample',
    'get_pixels_unaligned',
]
struct_AVDCT._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('idct', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16))),
    ('idct_permutation', c_uint8 * int(64)),
    ('fdct', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16))),
    ('dct_algo', c_int),
    ('idct_algo', c_int),
    ('get_pixels', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16), POINTER(c_uint8), c_ptrdiff_t)),
    ('bits_per_sample', c_int),
    ('get_pixels_unaligned', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16), POINTER(c_uint8), c_ptrdiff_t)),
]

AVDCT = struct_AVDCT# /usr/include/libavcodec/avdct.h: 74

# /usr/include/libavcodec/avdct.h: 83
if _libs["avcodec"].has("avcodec_dct_alloc", "cdecl"):
    avcodec_dct_alloc = _libs["avcodec"].get("avcodec_dct_alloc", "cdecl")
    avcodec_dct_alloc.argtypes = []
    avcodec_dct_alloc.restype = POINTER(AVDCT)

# /usr/include/libavcodec/avdct.h: 84
if _libs["avcodec"].has("avcodec_dct_init", "cdecl"):
    avcodec_dct_init = _libs["avcodec"].get("avcodec_dct_init", "cdecl")
    avcodec_dct_init.argtypes = [POINTER(AVDCT)]
    avcodec_dct_init.restype = c_int

# /usr/include/libavcodec/avdct.h: 86
if _libs["avcodec"].has("avcodec_dct_get_class", "cdecl"):
    avcodec_dct_get_class = _libs["avcodec"].get("avcodec_dct_get_class", "cdecl")
    avcodec_dct_get_class.argtypes = []
    avcodec_dct_get_class.restype = POINTER(AVClass)

FFTSample = c_float# /usr/include/libavcodec/avfft.h: 35

# /usr/include/libavcodec/avfft.h: 39
class struct_FFTComplex(Structure):
    pass

struct_FFTComplex.__slots__ = [
    're',
    'im',
]
struct_FFTComplex._fields_ = [
    ('re', FFTSample),
    ('im', FFTSample),
]

FFTComplex = struct_FFTComplex# /usr/include/libavcodec/avfft.h: 39

# /usr/include/libavcodec/avfft.h: 41
class struct_FFTContext(Structure):
    pass

FFTContext = struct_FFTContext# /usr/include/libavcodec/avfft.h: 41

# /usr/include/libavcodec/avfft.h: 48
if _libs["avcodec"].has("av_fft_init", "cdecl"):
    av_fft_init = _libs["avcodec"].get("av_fft_init", "cdecl")
    av_fft_init.argtypes = [c_int, c_int]
    av_fft_init.restype = POINTER(FFTContext)

# /usr/include/libavcodec/avfft.h: 53
if _libs["avcodec"].has("av_fft_permute", "cdecl"):
    av_fft_permute = _libs["avcodec"].get("av_fft_permute", "cdecl")
    av_fft_permute.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_permute.restype = None

# /usr/include/libavcodec/avfft.h: 59
if _libs["avcodec"].has("av_fft_calc", "cdecl"):
    av_fft_calc = _libs["avcodec"].get("av_fft_calc", "cdecl")
    av_fft_calc.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_calc.restype = None

# /usr/include/libavcodec/avfft.h: 61
if _libs["avcodec"].has("av_fft_end", "cdecl"):
    av_fft_end = _libs["avcodec"].get("av_fft_end", "cdecl")
    av_fft_end.argtypes = [POINTER(FFTContext)]
    av_fft_end.restype = None

# /usr/include/libavcodec/avfft.h: 63
if _libs["avcodec"].has("av_mdct_init", "cdecl"):
    av_mdct_init = _libs["avcodec"].get("av_mdct_init", "cdecl")
    av_mdct_init.argtypes = [c_int, c_int, c_double]
    av_mdct_init.restype = POINTER(FFTContext)

# /usr/include/libavcodec/avfft.h: 64
if _libs["avcodec"].has("av_imdct_calc", "cdecl"):
    av_imdct_calc = _libs["avcodec"].get("av_imdct_calc", "cdecl")
    av_imdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_calc.restype = None

# /usr/include/libavcodec/avfft.h: 65
if _libs["avcodec"].has("av_imdct_half", "cdecl"):
    av_imdct_half = _libs["avcodec"].get("av_imdct_half", "cdecl")
    av_imdct_half.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_half.restype = None

# /usr/include/libavcodec/avfft.h: 66
if _libs["avcodec"].has("av_mdct_calc", "cdecl"):
    av_mdct_calc = _libs["avcodec"].get("av_mdct_calc", "cdecl")
    av_mdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_mdct_calc.restype = None

# /usr/include/libavcodec/avfft.h: 67
if _libs["avcodec"].has("av_mdct_end", "cdecl"):
    av_mdct_end = _libs["avcodec"].get("av_mdct_end", "cdecl")
    av_mdct_end.argtypes = [POINTER(FFTContext)]
    av_mdct_end.restype = None

enum_RDFTransformType = c_int# /usr/include/libavcodec/avfft.h: 71

DFT_R2C = 0# /usr/include/libavcodec/avfft.h: 71

IDFT_C2R = (DFT_R2C + 1)# /usr/include/libavcodec/avfft.h: 71

IDFT_R2C = (IDFT_C2R + 1)# /usr/include/libavcodec/avfft.h: 71

DFT_C2R = (IDFT_R2C + 1)# /usr/include/libavcodec/avfft.h: 71

# /usr/include/libavcodec/avfft.h: 78
class struct_RDFTContext(Structure):
    pass

RDFTContext = struct_RDFTContext# /usr/include/libavcodec/avfft.h: 78

# /usr/include/libavcodec/avfft.h: 85
if _libs["avcodec"].has("av_rdft_init", "cdecl"):
    av_rdft_init = _libs["avcodec"].get("av_rdft_init", "cdecl")
    av_rdft_init.argtypes = [c_int, enum_RDFTransformType]
    av_rdft_init.restype = POINTER(RDFTContext)

# /usr/include/libavcodec/avfft.h: 86
if _libs["avcodec"].has("av_rdft_calc", "cdecl"):
    av_rdft_calc = _libs["avcodec"].get("av_rdft_calc", "cdecl")
    av_rdft_calc.argtypes = [POINTER(RDFTContext), POINTER(FFTSample)]
    av_rdft_calc.restype = None

# /usr/include/libavcodec/avfft.h: 87
if _libs["avcodec"].has("av_rdft_end", "cdecl"):
    av_rdft_end = _libs["avcodec"].get("av_rdft_end", "cdecl")
    av_rdft_end.argtypes = [POINTER(RDFTContext)]
    av_rdft_end.restype = None

# /usr/include/libavcodec/avfft.h: 91
class struct_DCTContext(Structure):
    pass

DCTContext = struct_DCTContext# /usr/include/libavcodec/avfft.h: 91

enum_DCTTransformType = c_int# /usr/include/libavcodec/avfft.h: 93

DCT_II = 0# /usr/include/libavcodec/avfft.h: 93

DCT_III = (DCT_II + 1)# /usr/include/libavcodec/avfft.h: 93

DCT_I = (DCT_III + 1)# /usr/include/libavcodec/avfft.h: 93

DST_I = (DCT_I + 1)# /usr/include/libavcodec/avfft.h: 93

# /usr/include/libavcodec/avfft.h: 110
if _libs["avcodec"].has("av_dct_init", "cdecl"):
    av_dct_init = _libs["avcodec"].get("av_dct_init", "cdecl")
    av_dct_init.argtypes = [c_int, enum_DCTTransformType]
    av_dct_init.restype = POINTER(DCTContext)

# /usr/include/libavcodec/avfft.h: 111
if _libs["avcodec"].has("av_dct_calc", "cdecl"):
    av_dct_calc = _libs["avcodec"].get("av_dct_calc", "cdecl")
    av_dct_calc.argtypes = [POINTER(DCTContext), POINTER(FFTSample)]
    av_dct_calc.restype = None

# /usr/include/libavcodec/avfft.h: 112
if _libs["avcodec"].has("av_dct_end", "cdecl"):
    av_dct_end = _libs["avcodec"].get("av_dct_end", "cdecl")
    av_dct_end.argtypes = [POINTER(DCTContext)]
    av_dct_end.restype = None

# /usr/include/libavcodec/adts_parser.h: 25
try:
    AV_AAC_ADTS_HEADER_SIZE = 7
except:
    pass

# /usr/include/libavutil/version.h: 56
def AV_VERSION_INT(a, b, c):
    return (((a << 16) | (b << 8)) | c)

# /usr/include/libavutil/version.h: 64
def AV_VERSION_MAJOR(a):
    return (a >> 16)

# /usr/include/libavutil/version.h: 65
def AV_VERSION_MINOR(a):
    return ((a & 65280) >> 8)

# /usr/include/libavutil/version.h: 66
def AV_VERSION_MICRO(a):
    return (a & 255)

# /usr/include/libavutil/version.h: 81
try:
    LIBAVUTIL_VERSION_MAJOR = 56
except:
    pass

# /usr/include/libavutil/version.h: 82
try:
    LIBAVUTIL_VERSION_MINOR = 70
except:
    pass

# /usr/include/libavutil/version.h: 83
try:
    LIBAVUTIL_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavutil/version.h: 85
try:
    LIBAVUTIL_VERSION_INT = (AV_VERSION_INT (LIBAVUTIL_VERSION_MAJOR, LIBAVUTIL_VERSION_MINOR, LIBAVUTIL_VERSION_MICRO))
except:
    pass

# /usr/include/libavutil/version.h: 91
try:
    LIBAVUTIL_BUILD = LIBAVUTIL_VERSION_INT
except:
    pass

# /usr/include/libavutil/version.h: 109
try:
    FF_API_VAAPI = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 112
try:
    FF_API_FRAME_QP = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 115
try:
    FF_API_PLUS1_MINUS1 = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 118
try:
    FF_API_ERROR_FRAME = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 121
try:
    FF_API_PKT_PTS = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 124
try:
    FF_API_CRYPTO_SIZE_T = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 127
try:
    FF_API_FRAME_GET_SET = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 130
try:
    FF_API_PSEUDOPAL = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 133
try:
    FF_API_CHILD_CLASS_NEXT = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 136
try:
    FF_API_BUFFER_SIZE_T = (LIBAVUTIL_VERSION_MAJOR < 57)
except:
    pass

# /usr/include/libavutil/version.h: 139
try:
    FF_API_D2STR = (LIBAVUTIL_VERSION_MAJOR < 58)
except:
    pass

# /usr/include/libavutil/version.h: 142
try:
    FF_API_DECLARE_ALIGNED = (LIBAVUTIL_VERSION_MAJOR < 58)
except:
    pass

# /usr/include/libavcodec/codec_id.h: 186
try:
    AV_CODEC_ID_IFF_BYTERUN1 = AV_CODEC_ID_IFF_ILBM
except:
    pass

# /usr/include/libavcodec/codec_id.h: 224
try:
    AV_CODEC_ID_H265 = AV_CODEC_ID_HEVC
except:
    pass

# /usr/include/libavcodec/codec_id.h: 248
try:
    AV_CODEC_ID_H266 = AV_CODEC_ID_VVC
except:
    pass

# /usr/include/libavcodec/version.h: 30
try:
    LIBAVCODEC_VERSION_MAJOR = 58
except:
    pass

# /usr/include/libavcodec/version.h: 31
try:
    LIBAVCODEC_VERSION_MINOR = 134
except:
    pass

# /usr/include/libavcodec/version.h: 32
try:
    LIBAVCODEC_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavcodec/version.h: 34
try:
    LIBAVCODEC_VERSION_INT = (AV_VERSION_INT (LIBAVCODEC_VERSION_MAJOR, LIBAVCODEC_VERSION_MINOR, LIBAVCODEC_VERSION_MICRO))
except:
    pass

# /usr/include/libavcodec/version.h: 40
try:
    LIBAVCODEC_BUILD = LIBAVCODEC_VERSION_INT
except:
    pass

# /usr/include/libavcodec/version.h: 55
try:
    FF_API_AVCTX_TIMEBASE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 58
try:
    FF_API_CODED_FRAME = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 61
try:
    FF_API_SIDEDATA_ONLY_PKT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 64
try:
    FF_API_VDPAU_PROFILE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 67
try:
    FF_API_CONVERGENCE_DURATION = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 70
try:
    FF_API_AVPICTURE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 73
try:
    FF_API_AVPACKET_OLD_API = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 76
try:
    FF_API_RTP_CALLBACK = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 79
try:
    FF_API_VBV_DELAY = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 82
try:
    FF_API_CODER_TYPE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 85
try:
    FF_API_STAT_BITS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 88
try:
    FF_API_PRIVATE_OPT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 91
try:
    FF_API_ASS_TIMING = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 94
try:
    FF_API_OLD_BSF = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 97
try:
    FF_API_COPY_CONTEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 100
try:
    FF_API_GET_CONTEXT_DEFAULTS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 103
try:
    FF_API_NVENC_OLD_NAME = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 106
try:
    FF_API_STRUCT_VAAPI_CONTEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 109
try:
    FF_API_MERGE_SD_API = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 112
try:
    FF_API_TAG_STRING = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 115
try:
    FF_API_GETCHROMA = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 118
try:
    FF_API_CODEC_GET_SET = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 121
try:
    FF_API_USER_VISIBLE_AVHWACCEL = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 124
try:
    FF_API_LOCKMGR = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 127
try:
    FF_API_NEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 130
try:
    FF_API_UNSANITIZED_BITRATES = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 133
try:
    FF_API_OPENH264_SLICE_MODE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 136
try:
    FF_API_OPENH264_CABAC = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 139
try:
    FF_API_UNUSED_CODEC_CAPS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 142
try:
    FF_API_AVPRIV_PUT_BITS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 145
try:
    FF_API_OLD_ENCDEC = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 148
try:
    FF_API_AVCODEC_PIX_FMT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 151
try:
    FF_API_MPV_RC_STRATEGY = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 154
try:
    FF_API_PARSER_CHANGE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavcodec/version.h: 157
try:
    FF_API_THREAD_SAFE_CALLBACKS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavcodec/version.h: 160
try:
    FF_API_DEBUG_MV = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavcodec/version.h: 163
try:
    FF_API_GET_FRAME_CLASS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavcodec/version.h: 166
try:
    FF_API_AUTO_THREADS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavcodec/version.h: 169
try:
    FF_API_INIT_PACKET = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavcodec/packet.h: 304
try:
    AV_PKT_DATA_QUALITY_FACTOR = AV_PKT_DATA_QUALITY_STATS
except:
    pass

# /usr/include/libavcodec/packet.h: 410
try:
    AV_PKT_FLAG_KEY = 1
except:
    pass

# /usr/include/libavcodec/packet.h: 411
try:
    AV_PKT_FLAG_CORRUPT = 2
except:
    pass

# /usr/include/libavcodec/packet.h: 417
try:
    AV_PKT_FLAG_DISCARD = 4
except:
    pass

# /usr/include/libavcodec/packet.h: 424
try:
    AV_PKT_FLAG_TRUSTED = 8
except:
    pass

# /usr/include/libavcodec/packet.h: 429
try:
    AV_PKT_FLAG_DISPOSABLE = 16
except:
    pass

# /usr/include/libavcodec/codec.h: 44
try:
    AV_CODEC_CAP_DRAW_HORIZ_BAND = (1 << 0)
except:
    pass

# /usr/include/libavcodec/codec.h: 52
try:
    AV_CODEC_CAP_DR1 = (1 << 1)
except:
    pass

# /usr/include/libavcodec/codec.h: 53
try:
    AV_CODEC_CAP_TRUNCATED = (1 << 3)
except:
    pass

# /usr/include/libavcodec/codec.h: 77
try:
    AV_CODEC_CAP_DELAY = (1 << 5)
except:
    pass

# /usr/include/libavcodec/codec.h: 82
try:
    AV_CODEC_CAP_SMALL_LAST_FRAME = (1 << 6)
except:
    pass

# /usr/include/libavcodec/codec.h: 95
try:
    AV_CODEC_CAP_SUBFRAMES = (1 << 8)
except:
    pass

# /usr/include/libavcodec/codec.h: 100
try:
    AV_CODEC_CAP_EXPERIMENTAL = (1 << 9)
except:
    pass

# /usr/include/libavcodec/codec.h: 104
try:
    AV_CODEC_CAP_CHANNEL_CONF = (1 << 10)
except:
    pass

# /usr/include/libavcodec/codec.h: 108
try:
    AV_CODEC_CAP_FRAME_THREADS = (1 << 12)
except:
    pass

# /usr/include/libavcodec/codec.h: 112
try:
    AV_CODEC_CAP_SLICE_THREADS = (1 << 13)
except:
    pass

# /usr/include/libavcodec/codec.h: 116
try:
    AV_CODEC_CAP_PARAM_CHANGE = (1 << 14)
except:
    pass

# /usr/include/libavcodec/codec.h: 122
try:
    AV_CODEC_CAP_OTHER_THREADS = (1 << 15)
except:
    pass

# /usr/include/libavcodec/codec.h: 124
try:
    AV_CODEC_CAP_AUTO_THREADS = AV_CODEC_CAP_OTHER_THREADS
except:
    pass

# /usr/include/libavcodec/codec.h: 129
try:
    AV_CODEC_CAP_VARIABLE_FRAME_SIZE = (1 << 16)
except:
    pass

# /usr/include/libavcodec/codec.h: 139
try:
    AV_CODEC_CAP_AVOID_PROBING = (1 << 17)
except:
    pass

# /usr/include/libavcodec/codec.h: 145
try:
    AV_CODEC_CAP_INTRA_ONLY = 1073741824
except:
    pass

# /usr/include/libavcodec/codec.h: 149
try:
    AV_CODEC_CAP_LOSSLESS = 2147483648
except:
    pass

# /usr/include/libavcodec/codec.h: 157
try:
    AV_CODEC_CAP_HARDWARE = (1 << 18)
except:
    pass

# /usr/include/libavcodec/codec.h: 164
try:
    AV_CODEC_CAP_HYBRID = (1 << 19)
except:
    pass

# /usr/include/libavcodec/codec.h: 171
try:
    AV_CODEC_CAP_ENCODER_REORDERED_OPAQUE = (1 << 20)
except:
    pass

# /usr/include/libavcodec/codec.h: 178
try:
    AV_CODEC_CAP_ENCODER_FLUSH = (1 << 21)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 72
try:
    AV_CODEC_PROP_INTRA_ONLY = (1 << 0)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 78
try:
    AV_CODEC_PROP_LOSSY = (1 << 1)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 82
try:
    AV_CODEC_PROP_LOSSLESS = (1 << 2)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 92
try:
    AV_CODEC_PROP_REORDER = (1 << 3)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 97
try:
    AV_CODEC_PROP_BITMAP_SUB = (1 << 16)
except:
    pass

# /usr/include/libavcodec/codec_desc.h: 102
try:
    AV_CODEC_PROP_TEXT_SUB = (1 << 17)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 215
try:
    AV_INPUT_BUFFER_PADDING_SIZE = 64
except:
    pass

# /usr/include/libavcodec/avcodec.h: 222
try:
    AV_INPUT_BUFFER_MIN_SIZE = 16384
except:
    pass

# /usr/include/libavcodec/avcodec.h: 271
try:
    AV_CODEC_FLAG_UNALIGNED = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 275
try:
    AV_CODEC_FLAG_QSCALE = (1 << 1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 279
try:
    AV_CODEC_FLAG_4MV = (1 << 2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 283
try:
    AV_CODEC_FLAG_OUTPUT_CORRUPT = (1 << 3)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 287
try:
    AV_CODEC_FLAG_QPEL = (1 << 4)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 292
try:
    AV_CODEC_FLAG_DROPCHANGED = (1 << 5)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 296
try:
    AV_CODEC_FLAG_PASS1 = (1 << 9)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 300
try:
    AV_CODEC_FLAG_PASS2 = (1 << 10)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 304
try:
    AV_CODEC_FLAG_LOOP_FILTER = (1 << 11)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 308
try:
    AV_CODEC_FLAG_GRAY = (1 << 13)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 312
try:
    AV_CODEC_FLAG_PSNR = (1 << 15)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 317
try:
    AV_CODEC_FLAG_TRUNCATED = (1 << 16)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 321
try:
    AV_CODEC_FLAG_INTERLACED_DCT = (1 << 18)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 325
try:
    AV_CODEC_FLAG_LOW_DELAY = (1 << 19)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 329
try:
    AV_CODEC_FLAG_GLOBAL_HEADER = (1 << 22)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 333
try:
    AV_CODEC_FLAG_BITEXACT = (1 << 23)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 338
try:
    AV_CODEC_FLAG_AC_PRED = (1 << 24)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 342
try:
    AV_CODEC_FLAG_INTERLACED_ME = (1 << 29)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 343
try:
    AV_CODEC_FLAG_CLOSED_GOP = (1 << 31)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 348
try:
    AV_CODEC_FLAG2_FAST = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 352
try:
    AV_CODEC_FLAG2_NO_OUTPUT = (1 << 2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 356
try:
    AV_CODEC_FLAG2_LOCAL_HEADER = (1 << 3)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 361
try:
    AV_CODEC_FLAG2_DROP_FRAME_TIMECODE = (1 << 13)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 367
try:
    AV_CODEC_FLAG2_CHUNKS = (1 << 15)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 371
try:
    AV_CODEC_FLAG2_IGNORE_CROP = (1 << 16)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 376
try:
    AV_CODEC_FLAG2_SHOW_ALL = (1 << 22)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 380
try:
    AV_CODEC_FLAG2_EXPORT_MVS = (1 << 28)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 384
try:
    AV_CODEC_FLAG2_SKIP_MANUAL = (1 << 29)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 388
try:
    AV_CODEC_FLAG2_RO_FLUSH_NOOP = (1 << 30)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 403
try:
    AV_CODEC_EXPORT_DATA_MVS = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 407
try:
    AV_CODEC_EXPORT_DATA_PRFT = (1 << 1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 412
try:
    AV_CODEC_EXPORT_DATA_VIDEO_ENC_PARAMS = (1 << 2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 417
try:
    AV_CODEC_EXPORT_DATA_FILM_GRAIN = (1 << 3)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 514
try:
    AV_GET_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 519
try:
    AV_GET_ENCODE_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 609
try:
    FF_COMPRESSION_DEFAULT = (-1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 896
try:
    FF_PRED_LEFT = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 897
try:
    FF_PRED_PLANE = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 898
try:
    FF_PRED_MEDIAN = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 941
try:
    FF_CMP_SAD = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 942
try:
    FF_CMP_SSE = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 943
try:
    FF_CMP_SATD = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 944
try:
    FF_CMP_DCT = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 945
try:
    FF_CMP_PSNR = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 946
try:
    FF_CMP_BIT = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 947
try:
    FF_CMP_RD = 6
except:
    pass

# /usr/include/libavcodec/avcodec.h: 948
try:
    FF_CMP_ZERO = 7
except:
    pass

# /usr/include/libavcodec/avcodec.h: 949
try:
    FF_CMP_VSAD = 8
except:
    pass

# /usr/include/libavcodec/avcodec.h: 950
try:
    FF_CMP_VSSE = 9
except:
    pass

# /usr/include/libavcodec/avcodec.h: 951
try:
    FF_CMP_NSSE = 10
except:
    pass

# /usr/include/libavcodec/avcodec.h: 952
try:
    FF_CMP_W53 = 11
except:
    pass

# /usr/include/libavcodec/avcodec.h: 953
try:
    FF_CMP_W97 = 12
except:
    pass

# /usr/include/libavcodec/avcodec.h: 954
try:
    FF_CMP_DCTMAX = 13
except:
    pass

# /usr/include/libavcodec/avcodec.h: 955
try:
    FF_CMP_DCT264 = 14
except:
    pass

# /usr/include/libavcodec/avcodec.h: 956
try:
    FF_CMP_MEDIAN_SAD = 15
except:
    pass

# /usr/include/libavcodec/avcodec.h: 957
try:
    FF_CMP_CHROMA = 256
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1015
try:
    SLICE_FLAG_CODED_ORDER = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1016
try:
    SLICE_FLAG_ALLOW_FIELD = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1017
try:
    SLICE_FLAG_ALLOW_PLANE = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1025
try:
    FF_MB_DECISION_SIMPLE = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1026
try:
    FF_MB_DECISION_BITS = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1027
try:
    FF_MB_DECISION_RD = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1447
try:
    FF_CODER_TYPE_VLC = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1448
try:
    FF_CODER_TYPE_AC = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1449
try:
    FF_CODER_TYPE_RAW = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1450
try:
    FF_CODER_TYPE_RLE = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1573
try:
    FF_BUG_AUTODETECT = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1574
try:
    FF_BUG_XVID_ILACE = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1575
try:
    FF_BUG_UMP4 = 8
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1576
try:
    FF_BUG_NO_PADDING = 16
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1577
try:
    FF_BUG_AMV = 32
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1578
try:
    FF_BUG_QPEL_CHROMA = 64
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1579
try:
    FF_BUG_STD_QPEL = 128
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1580
try:
    FF_BUG_QPEL_CHROMA2 = 256
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1581
try:
    FF_BUG_DIRECT_BLOCKSIZE = 512
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1582
try:
    FF_BUG_EDGE = 1024
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1583
try:
    FF_BUG_HPEL_CHROMA = 2048
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1584
try:
    FF_BUG_DC_CLIP = 4096
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1585
try:
    FF_BUG_MS = 8192
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1586
try:
    FF_BUG_TRUNCATED = 16384
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1587
try:
    FF_BUG_IEDGE = 32768
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1602
try:
    FF_COMPLIANCE_VERY_STRICT = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1603
try:
    FF_COMPLIANCE_STRICT = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1604
try:
    FF_COMPLIANCE_NORMAL = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1605
try:
    FF_COMPLIANCE_UNOFFICIAL = (-1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1606
try:
    FF_COMPLIANCE_EXPERIMENTAL = (-2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1614
try:
    FF_EC_GUESS_MVS = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1615
try:
    FF_EC_DEBLOCK = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1616
try:
    FF_EC_FAVOR_INTER = 256
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1624
try:
    FF_DEBUG_PICT_INFO = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1625
try:
    FF_DEBUG_RC = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1626
try:
    FF_DEBUG_BITSTREAM = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1627
try:
    FF_DEBUG_MB_TYPE = 8
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1628
try:
    FF_DEBUG_QP = 16
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1629
try:
    FF_DEBUG_DCT_COEFF = 64
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1630
try:
    FF_DEBUG_SKIP = 128
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1631
try:
    FF_DEBUG_STARTCODE = 256
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1632
try:
    FF_DEBUG_ER = 1024
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1633
try:
    FF_DEBUG_MMCO = 2048
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1634
try:
    FF_DEBUG_BUGS = 4096
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1635
try:
    FF_DEBUG_BUFFERS = 32768
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1636
try:
    FF_DEBUG_THREADS = 65536
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1637
try:
    FF_DEBUG_GREEN_MD = 8388608
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1638
try:
    FF_DEBUG_NOMC = 16777216
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1653
try:
    AV_EF_CRCCHECK = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1654
try:
    AV_EF_BITSTREAM = (1 << 1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1655
try:
    AV_EF_BUFFER = (1 << 2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1656
try:
    AV_EF_EXPLODE = (1 << 3)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1658
try:
    AV_EF_IGNORE_ERR = (1 << 15)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1659
try:
    AV_EF_CAREFUL = (1 << 16)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1660
try:
    AV_EF_COMPLIANT = (1 << 17)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1661
try:
    AV_EF_AGGRESSIVE = (1 << 18)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1707
try:
    FF_DCT_AUTO = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1708
try:
    FF_DCT_FASTINT = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1709
try:
    FF_DCT_INT = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1710
try:
    FF_DCT_MMX = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1711
try:
    FF_DCT_ALTIVEC = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1712
try:
    FF_DCT_FAAN = 6
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1720
try:
    FF_IDCT_AUTO = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1721
try:
    FF_IDCT_INT = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1722
try:
    FF_IDCT_SIMPLE = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1723
try:
    FF_IDCT_SIMPLEMMX = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1724
try:
    FF_IDCT_ARM = 7
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1725
try:
    FF_IDCT_ALTIVEC = 8
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1726
try:
    FF_IDCT_SIMPLEARM = 10
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1727
try:
    FF_IDCT_XVID = 14
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1728
try:
    FF_IDCT_SIMPLEARMV5TE = 16
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1729
try:
    FF_IDCT_SIMPLEARMV6 = 17
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1730
try:
    FF_IDCT_FAAN = 20
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1731
try:
    FF_IDCT_SIMPLENEON = 22
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1732
try:
    FF_IDCT_NONE = 24
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1733
try:
    FF_IDCT_SIMPLEAUTO = 128
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1784
try:
    FF_THREAD_FRAME = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1785
try:
    FF_THREAD_SLICE = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1859
try:
    FF_PROFILE_UNKNOWN = (-99)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1860
try:
    FF_PROFILE_RESERVED = (-100)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1862
try:
    FF_PROFILE_AAC_MAIN = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1863
try:
    FF_PROFILE_AAC_LOW = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1864
try:
    FF_PROFILE_AAC_SSR = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1865
try:
    FF_PROFILE_AAC_LTP = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1866
try:
    FF_PROFILE_AAC_HE = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1867
try:
    FF_PROFILE_AAC_HE_V2 = 28
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1868
try:
    FF_PROFILE_AAC_LD = 22
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1869
try:
    FF_PROFILE_AAC_ELD = 38
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1870
try:
    FF_PROFILE_MPEG2_AAC_LOW = 128
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1871
try:
    FF_PROFILE_MPEG2_AAC_HE = 131
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1873
try:
    FF_PROFILE_DNXHD = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1874
try:
    FF_PROFILE_DNXHR_LB = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1875
try:
    FF_PROFILE_DNXHR_SQ = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1876
try:
    FF_PROFILE_DNXHR_HQ = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1877
try:
    FF_PROFILE_DNXHR_HQX = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1878
try:
    FF_PROFILE_DNXHR_444 = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1880
try:
    FF_PROFILE_DTS = 20
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1881
try:
    FF_PROFILE_DTS_ES = 30
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1882
try:
    FF_PROFILE_DTS_96_24 = 40
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1883
try:
    FF_PROFILE_DTS_HD_HRA = 50
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1884
try:
    FF_PROFILE_DTS_HD_MA = 60
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1885
try:
    FF_PROFILE_DTS_EXPRESS = 70
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1887
try:
    FF_PROFILE_MPEG2_422 = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1888
try:
    FF_PROFILE_MPEG2_HIGH = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1889
try:
    FF_PROFILE_MPEG2_SS = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1890
try:
    FF_PROFILE_MPEG2_SNR_SCALABLE = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1891
try:
    FF_PROFILE_MPEG2_MAIN = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1892
try:
    FF_PROFILE_MPEG2_SIMPLE = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1894
try:
    FF_PROFILE_H264_CONSTRAINED = (1 << 9)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1895
try:
    FF_PROFILE_H264_INTRA = (1 << 11)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1897
try:
    FF_PROFILE_H264_BASELINE = 66
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1898
try:
    FF_PROFILE_H264_CONSTRAINED_BASELINE = (66 | FF_PROFILE_H264_CONSTRAINED)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1899
try:
    FF_PROFILE_H264_MAIN = 77
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1900
try:
    FF_PROFILE_H264_EXTENDED = 88
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1901
try:
    FF_PROFILE_H264_HIGH = 100
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1902
try:
    FF_PROFILE_H264_HIGH_10 = 110
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1903
try:
    FF_PROFILE_H264_HIGH_10_INTRA = (110 | FF_PROFILE_H264_INTRA)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1904
try:
    FF_PROFILE_H264_MULTIVIEW_HIGH = 118
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1905
try:
    FF_PROFILE_H264_HIGH_422 = 122
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1906
try:
    FF_PROFILE_H264_HIGH_422_INTRA = (122 | FF_PROFILE_H264_INTRA)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1907
try:
    FF_PROFILE_H264_STEREO_HIGH = 128
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1908
try:
    FF_PROFILE_H264_HIGH_444 = 144
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1909
try:
    FF_PROFILE_H264_HIGH_444_PREDICTIVE = 244
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1910
try:
    FF_PROFILE_H264_HIGH_444_INTRA = (244 | FF_PROFILE_H264_INTRA)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1911
try:
    FF_PROFILE_H264_CAVLC_444 = 44
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1913
try:
    FF_PROFILE_VC1_SIMPLE = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1914
try:
    FF_PROFILE_VC1_MAIN = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1915
try:
    FF_PROFILE_VC1_COMPLEX = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1916
try:
    FF_PROFILE_VC1_ADVANCED = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1918
try:
    FF_PROFILE_MPEG4_SIMPLE = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1919
try:
    FF_PROFILE_MPEG4_SIMPLE_SCALABLE = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1920
try:
    FF_PROFILE_MPEG4_CORE = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1921
try:
    FF_PROFILE_MPEG4_MAIN = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1922
try:
    FF_PROFILE_MPEG4_N_BIT = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1923
try:
    FF_PROFILE_MPEG4_SCALABLE_TEXTURE = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1924
try:
    FF_PROFILE_MPEG4_SIMPLE_FACE_ANIMATION = 6
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1925
try:
    FF_PROFILE_MPEG4_BASIC_ANIMATED_TEXTURE = 7
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1926
try:
    FF_PROFILE_MPEG4_HYBRID = 8
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1927
try:
    FF_PROFILE_MPEG4_ADVANCED_REAL_TIME = 9
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1928
try:
    FF_PROFILE_MPEG4_CORE_SCALABLE = 10
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1929
try:
    FF_PROFILE_MPEG4_ADVANCED_CODING = 11
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1930
try:
    FF_PROFILE_MPEG4_ADVANCED_CORE = 12
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1931
try:
    FF_PROFILE_MPEG4_ADVANCED_SCALABLE_TEXTURE = 13
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1932
try:
    FF_PROFILE_MPEG4_SIMPLE_STUDIO = 14
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1933
try:
    FF_PROFILE_MPEG4_ADVANCED_SIMPLE = 15
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1935
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_0 = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1936
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_1 = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1937
try:
    FF_PROFILE_JPEG2000_CSTREAM_NO_RESTRICTION = 32768
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1938
try:
    FF_PROFILE_JPEG2000_DCINEMA_2K = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1939
try:
    FF_PROFILE_JPEG2000_DCINEMA_4K = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1941
try:
    FF_PROFILE_VP9_0 = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1942
try:
    FF_PROFILE_VP9_1 = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1943
try:
    FF_PROFILE_VP9_2 = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1944
try:
    FF_PROFILE_VP9_3 = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1946
try:
    FF_PROFILE_HEVC_MAIN = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1947
try:
    FF_PROFILE_HEVC_MAIN_10 = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1948
try:
    FF_PROFILE_HEVC_MAIN_STILL_PICTURE = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1949
try:
    FF_PROFILE_HEVC_REXT = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1951
try:
    FF_PROFILE_VVC_MAIN_10 = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1952
try:
    FF_PROFILE_VVC_MAIN_10_444 = 33
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1954
try:
    FF_PROFILE_AV1_MAIN = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1955
try:
    FF_PROFILE_AV1_HIGH = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1956
try:
    FF_PROFILE_AV1_PROFESSIONAL = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1958
try:
    FF_PROFILE_MJPEG_HUFFMAN_BASELINE_DCT = 192
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1959
try:
    FF_PROFILE_MJPEG_HUFFMAN_EXTENDED_SEQUENTIAL_DCT = 193
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1960
try:
    FF_PROFILE_MJPEG_HUFFMAN_PROGRESSIVE_DCT = 194
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1961
try:
    FF_PROFILE_MJPEG_HUFFMAN_LOSSLESS = 195
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1962
try:
    FF_PROFILE_MJPEG_JPEG_LS = 247
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1964
try:
    FF_PROFILE_SBC_MSBC = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1966
try:
    FF_PROFILE_PRORES_PROXY = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1967
try:
    FF_PROFILE_PRORES_LT = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1968
try:
    FF_PROFILE_PRORES_STANDARD = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1969
try:
    FF_PROFILE_PRORES_HQ = 3
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1970
try:
    FF_PROFILE_PRORES_4444 = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1971
try:
    FF_PROFILE_PRORES_XQ = 5
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1973
try:
    FF_PROFILE_ARIB_PROFILE_A = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1974
try:
    FF_PROFILE_ARIB_PROFILE_C = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1976
try:
    FF_PROFILE_KLVA_SYNC = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1977
try:
    FF_PROFILE_KLVA_ASYNC = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 1985
try:
    FF_LEVEL_UNKNOWN = (-99)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2118
try:
    FF_SUB_CHARENC_MODE_DO_NOTHING = (-1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2119
try:
    FF_SUB_CHARENC_MODE_AUTOMATIC = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2120
try:
    FF_SUB_CHARENC_MODE_PRE_DECODER = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2121
try:
    FF_SUB_CHARENC_MODE_IGNORE = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2150
try:
    FF_DEBUG_VIS_MV_P_FOR = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2151
try:
    FF_DEBUG_VIS_MV_B_FOR = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2152
try:
    FF_DEBUG_VIS_MV_B_BACK = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2184
try:
    FF_CODEC_PROPERTY_LOSSLESS = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2185
try:
    FF_CODEC_PROPERTY_CLOSED_CAPTIONS = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2226
try:
    FF_SUB_TEXT_FMT_ASS = 0
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2228
try:
    FF_SUB_TEXT_FMT_ASS_WITH_TIMINGS = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2604
try:
    AV_HWACCEL_CODEC_CAP_EXPERIMENTAL = 512
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2614
try:
    AV_HWACCEL_FLAG_IGNORE_LEVEL = (1 << 0)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2620
try:
    AV_HWACCEL_FLAG_ALLOW_HIGH_DEPTH = (1 << 1)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2634
try:
    AV_HWACCEL_FLAG_ALLOW_PROFILE_MISMATCH = (1 << 2)
except:
    pass

# /usr/include/libavcodec/avcodec.h: 2685
try:
    AV_SUBTITLE_FLAG_FORCED = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 3404
try:
    AV_PARSER_PTS_NB = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 3411
try:
    PARSER_FLAG_COMPLETE_FRAMES = 1
except:
    pass

# /usr/include/libavcodec/avcodec.h: 3412
try:
    PARSER_FLAG_ONCE = 2
except:
    pass

# /usr/include/libavcodec/avcodec.h: 3414
try:
    PARSER_FLAG_FETCHED_OFFSET = 4
except:
    pass

# /usr/include/libavcodec/avcodec.h: 3415
try:
    PARSER_FLAG_USE_CODEC_TS = 4096
except:
    pass

# /usr/include/libavcodec/d3d11va.h: 35
try:
    _WIN32_WINNT = 1538
except:
    pass

AVCodecParameters = struct_AVCodecParameters# /usr/include/libavcodec/codec_par.h: 201

AVPacketSideData = struct_AVPacketSideData# /usr/include/libavcodec/packet.h: 314

AVPacket = struct_AVPacket# /usr/include/libavcodec/packet.h: 400

AVPacketList = struct_AVPacketList# /usr/include/libavcodec/packet.h: 404

AVBSFInternal = struct_AVBSFInternal# /usr/include/libavcodec/bsf.h: 37

AVBitStreamFilter = struct_AVBitStreamFilter# /usr/include/libavcodec/bsf.h: 98

AVBSFContext = struct_AVBSFContext# /usr/include/libavcodec/bsf.h: 96

AVBSFList = struct_AVBSFList# /usr/include/libavcodec/bsf.h: 240

AVProfile = struct_AVProfile# /usr/include/libavcodec/codec.h: 186

AVCodecDefault = struct_AVCodecDefault# /usr/include/libavcodec/codec.h: 188

AVCodecContext = struct_AVCodecContext# /usr/include/libavcodec/avcodec.h: 536

AVSubtitle = struct_AVSubtitle# /usr/include/libavcodec/avcodec.h: 2722

AVCodec = struct_AVCodec# /usr/include/libavcodec/codec.h: 197

AVCodecHWConfigInternal = struct_AVCodecHWConfigInternal# /usr/include/libavcodec/codec.h: 343

AVCodecHWConfig = struct_AVCodecHWConfig# /usr/include/libavcodec/codec.h: 465

AVCodecDescriptor = struct_AVCodecDescriptor# /usr/include/libavcodec/codec_desc.h: 66

RcOverride = struct_RcOverride# /usr/include/libavcodec/avcodec.h: 260

AVPanScan = struct_AVPanScan# /usr/include/libavcodec/avcodec.h: 446

AVCPBProperties = struct_AVCPBProperties# /usr/include/libavcodec/avcodec.h: 496

AVProducerReferenceTime = struct_AVProducerReferenceTime# /usr/include/libavcodec/avcodec.h: 509

AVCodecInternal = struct_AVCodecInternal# /usr/include/libavcodec/avcodec.h: 521

AVHWAccel = struct_AVHWAccel# /usr/include/libavcodec/avcodec.h: 2438

MpegEncContext = struct_MpegEncContext# /usr/include/libavcodec/avcodec.h: 2428

AVPicture = struct_AVPicture# /usr/include/libavcodec/avcodec.h: 2660

AVSubtitleRect = struct_AVSubtitleRect# /usr/include/libavcodec/avcodec.h: 2720

AVCodecParser = struct_AVCodecParser# /usr/include/libavcodec/avcodec.h: 3544

AVCodecParserContext = struct_AVCodecParserContext# /usr/include/libavcodec/avcodec.h: 3542

AVBitStreamFilterContext = struct_AVBitStreamFilterContext# /usr/include/libavcodec/avcodec.h: 4017

AVDCT = struct_AVDCT# /usr/include/libavcodec/avdct.h: 74

FFTComplex = struct_FFTComplex# /usr/include/libavcodec/avfft.h: 39

FFTContext = struct_FFTContext# /usr/include/libavcodec/avfft.h: 41

RDFTContext = struct_RDFTContext# /usr/include/libavcodec/avfft.h: 78

DCTContext = struct_DCTContext# /usr/include/libavcodec/avfft.h: 91

# No inserted files

# No prefix-stripping

