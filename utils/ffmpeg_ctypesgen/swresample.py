r"""Wrapper for swresample.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lswresample /usr/include/libswresample/swresample.h /usr/include/libswresample/version.h -L/usr/include/libavutil -o swresample.py

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
_libs["swresample"] = load_library("swresample")

# 1 libraries
# End libraries

# No modules

enum_AVMatrixEncoding = c_int# /usr/include/libavutil/channel_layout.h: 120

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

# /usr/include/libavutil/log.h: 60
class struct_AVOptionRanges(Structure):
    pass

# /usr/include/libavutil/log.h: 85
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

enum_AVColorPrimaries = c_int# /usr/include/libavutil/pixfmt.h: 458

enum_AVColorTransferCharacteristic = c_int# /usr/include/libavutil/pixfmt.h: 483

enum_AVColorSpace = c_int# /usr/include/libavutil/pixfmt.h: 512

enum_AVColorRange = c_int# /usr/include/libavutil/pixfmt.h: 551

enum_AVChromaLocation = c_int# /usr/include/libavutil/pixfmt.h: 605

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

enum_AVSampleFormat = c_int# /usr/include/libavutil/samplefmt.h: 58

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

enum_SwrDitherType = c_int# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NONE = 0# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_RECTANGULAR = (SWR_DITHER_NONE + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_TRIANGULAR = (SWR_DITHER_RECTANGULAR + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_TRIANGULAR_HIGHPASS = (SWR_DITHER_TRIANGULAR + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS = 64# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_LIPSHITZ = (SWR_DITHER_NS + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_F_WEIGHTED = (SWR_DITHER_NS_LIPSHITZ + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_MODIFIED_E_WEIGHTED = (SWR_DITHER_NS_F_WEIGHTED + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_IMPROVED_E_WEIGHTED = (SWR_DITHER_NS_MODIFIED_E_WEIGHTED + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_SHIBATA = (SWR_DITHER_NS_IMPROVED_E_WEIGHTED + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_LOW_SHIBATA = (SWR_DITHER_NS_SHIBATA + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NS_HIGH_SHIBATA = (SWR_DITHER_NS_LOW_SHIBATA + 1)# /usr/include/libswresample/swresample.h: 141

SWR_DITHER_NB = (SWR_DITHER_NS_HIGH_SHIBATA + 1)# /usr/include/libswresample/swresample.h: 141

enum_SwrEngine = c_int# /usr/include/libswresample/swresample.h: 159

SWR_ENGINE_SWR = 0# /usr/include/libswresample/swresample.h: 159

SWR_ENGINE_SOXR = (SWR_ENGINE_SWR + 1)# /usr/include/libswresample/swresample.h: 159

SWR_ENGINE_NB = (SWR_ENGINE_SOXR + 1)# /usr/include/libswresample/swresample.h: 159

enum_SwrFilterType = c_int# /usr/include/libswresample/swresample.h: 166

SWR_FILTER_TYPE_CUBIC = 0# /usr/include/libswresample/swresample.h: 166

SWR_FILTER_TYPE_BLACKMAN_NUTTALL = (SWR_FILTER_TYPE_CUBIC + 1)# /usr/include/libswresample/swresample.h: 166

SWR_FILTER_TYPE_KAISER = (SWR_FILTER_TYPE_BLACKMAN_NUTTALL + 1)# /usr/include/libswresample/swresample.h: 166

# /usr/include/libswresample/swresample.h: 182
class struct_SwrContext(Structure):
    pass

SwrContext = struct_SwrContext# /usr/include/libswresample/swresample.h: 182

# /usr/include/libswresample/swresample.h: 191
if _libs["swresample"].has("swr_get_class", "cdecl"):
    swr_get_class = _libs["swresample"].get("swr_get_class", "cdecl")
    swr_get_class.argtypes = []
    swr_get_class.restype = POINTER(AVClass)

# /usr/include/libswresample/swresample.h: 207
if _libs["swresample"].has("swr_alloc", "cdecl"):
    swr_alloc = _libs["swresample"].get("swr_alloc", "cdecl")
    swr_alloc.argtypes = []
    swr_alloc.restype = POINTER(struct_SwrContext)

# /usr/include/libswresample/swresample.h: 219
if _libs["swresample"].has("swr_init", "cdecl"):
    swr_init = _libs["swresample"].get("swr_init", "cdecl")
    swr_init.argtypes = [POINTER(struct_SwrContext)]
    swr_init.restype = c_int

# /usr/include/libswresample/swresample.h: 228
if _libs["swresample"].has("swr_is_initialized", "cdecl"):
    swr_is_initialized = _libs["swresample"].get("swr_is_initialized", "cdecl")
    swr_is_initialized.argtypes = [POINTER(struct_SwrContext)]
    swr_is_initialized.restype = c_int

# /usr/include/libswresample/swresample.h: 250
if _libs["swresample"].has("swr_alloc_set_opts", "cdecl"):
    swr_alloc_set_opts = _libs["swresample"].get("swr_alloc_set_opts", "cdecl")
    swr_alloc_set_opts.argtypes = [POINTER(struct_SwrContext), c_int64, enum_AVSampleFormat, c_int, c_int64, enum_AVSampleFormat, c_int, c_int, POINTER(None)]
    swr_alloc_set_opts.restype = POINTER(struct_SwrContext)

# /usr/include/libswresample/swresample.h: 267
if _libs["swresample"].has("swr_free", "cdecl"):
    swr_free = _libs["swresample"].get("swr_free", "cdecl")
    swr_free.argtypes = [POINTER(POINTER(struct_SwrContext))]
    swr_free.restype = None

# /usr/include/libswresample/swresample.h: 279
if _libs["swresample"].has("swr_close", "cdecl"):
    swr_close = _libs["swresample"].get("swr_close", "cdecl")
    swr_close.argtypes = [POINTER(struct_SwrContext)]
    swr_close.restype = None

# /usr/include/libswresample/swresample.h: 306
if _libs["swresample"].has("swr_convert", "cdecl"):
    swr_convert = _libs["swresample"].get("swr_convert", "cdecl")
    swr_convert.argtypes = [POINTER(struct_SwrContext), POINTER(POINTER(c_uint8)), c_int, POINTER(POINTER(c_uint8)), c_int]
    swr_convert.restype = c_int

# /usr/include/libswresample/swresample.h: 326
if _libs["swresample"].has("swr_next_pts", "cdecl"):
    swr_next_pts = _libs["swresample"].get("swr_next_pts", "cdecl")
    swr_next_pts.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_next_pts.restype = c_int64

# /usr/include/libswresample/swresample.h: 353
if _libs["swresample"].has("swr_set_compensation", "cdecl"):
    swr_set_compensation = _libs["swresample"].get("swr_set_compensation", "cdecl")
    swr_set_compensation.argtypes = [POINTER(struct_SwrContext), c_int, c_int]
    swr_set_compensation.restype = c_int

# /usr/include/libswresample/swresample.h: 363
if _libs["swresample"].has("swr_set_channel_mapping", "cdecl"):
    swr_set_channel_mapping = _libs["swresample"].get("swr_set_channel_mapping", "cdecl")
    swr_set_channel_mapping.argtypes = [POINTER(struct_SwrContext), POINTER(c_int)]
    swr_set_channel_mapping.restype = c_int

# /usr/include/libswresample/swresample.h: 388
if _libs["swresample"].has("swr_build_matrix", "cdecl"):
    swr_build_matrix = _libs["swresample"].get("swr_build_matrix", "cdecl")
    swr_build_matrix.argtypes = [c_uint64, c_uint64, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), c_int, enum_AVMatrixEncoding, POINTER(None)]
    swr_build_matrix.restype = c_int

# /usr/include/libswresample/swresample.h: 404
if _libs["swresample"].has("swr_set_matrix", "cdecl"):
    swr_set_matrix = _libs["swresample"].get("swr_set_matrix", "cdecl")
    swr_set_matrix.argtypes = [POINTER(struct_SwrContext), POINTER(c_double), c_int]
    swr_set_matrix.restype = c_int

# /usr/include/libswresample/swresample.h: 424
if _libs["swresample"].has("swr_drop_output", "cdecl"):
    swr_drop_output = _libs["swresample"].get("swr_drop_output", "cdecl")
    swr_drop_output.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_drop_output.restype = c_int

# /usr/include/libswresample/swresample.h: 437
if _libs["swresample"].has("swr_inject_silence", "cdecl"):
    swr_inject_silence = _libs["swresample"].get("swr_inject_silence", "cdecl")
    swr_inject_silence.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_inject_silence.restype = c_int

# /usr/include/libswresample/swresample.h: 463
if _libs["swresample"].has("swr_get_delay", "cdecl"):
    swr_get_delay = _libs["swresample"].get("swr_get_delay", "cdecl")
    swr_get_delay.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_get_delay.restype = c_int64

# /usr/include/libswresample/swresample.h: 481
if _libs["swresample"].has("swr_get_out_samples", "cdecl"):
    swr_get_out_samples = _libs["swresample"].get("swr_get_out_samples", "cdecl")
    swr_get_out_samples.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_get_out_samples.restype = c_int

# /usr/include/libswresample/swresample.h: 498
if _libs["swresample"].has("swresample_version", "cdecl"):
    swresample_version = _libs["swresample"].get("swresample_version", "cdecl")
    swresample_version.argtypes = []
    swresample_version.restype = c_uint

# /usr/include/libswresample/swresample.h: 505
if _libs["swresample"].has("swresample_configuration", "cdecl"):
    swresample_configuration = _libs["swresample"].get("swresample_configuration", "cdecl")
    swresample_configuration.argtypes = []
    swresample_configuration.restype = c_char_p

# /usr/include/libswresample/swresample.h: 512
if _libs["swresample"].has("swresample_license", "cdecl"):
    swresample_license = _libs["swresample"].get("swresample_license", "cdecl")
    swresample_license.argtypes = []
    swresample_license.restype = c_char_p

# /usr/include/libswresample/swresample.h: 555
if _libs["swresample"].has("swr_convert_frame", "cdecl"):
    swr_convert_frame = _libs["swresample"].get("swr_convert_frame", "cdecl")
    swr_convert_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_convert_frame.restype = c_int

# /usr/include/libswresample/swresample.h: 572
if _libs["swresample"].has("swr_config_frame", "cdecl"):
    swr_config_frame = _libs["swresample"].get("swr_config_frame", "cdecl")
    swr_config_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_config_frame.restype = c_int

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

# /usr/include/libswresample/version.h: 31
try:
    LIBSWRESAMPLE_VERSION_MAJOR = 3
except:
    pass

# /usr/include/libswresample/version.h: 32
try:
    LIBSWRESAMPLE_VERSION_MINOR = 9
except:
    pass

# /usr/include/libswresample/version.h: 33
try:
    LIBSWRESAMPLE_VERSION_MICRO = 100
except:
    pass

# /usr/include/libswresample/version.h: 35
try:
    LIBSWRESAMPLE_VERSION_INT = (AV_VERSION_INT (LIBSWRESAMPLE_VERSION_MAJOR, LIBSWRESAMPLE_VERSION_MINOR, LIBSWRESAMPLE_VERSION_MICRO))
except:
    pass

# /usr/include/libswresample/version.h: 41
try:
    LIBSWRESAMPLE_BUILD = LIBSWRESAMPLE_VERSION_INT
except:
    pass

# /usr/include/libswresample/swresample.h: 136
try:
    SWR_FLAG_RESAMPLE = 1
except:
    pass

SwrContext = struct_SwrContext# /usr/include/libswresample/swresample.h: 182

# No inserted files

# No prefix-stripping

