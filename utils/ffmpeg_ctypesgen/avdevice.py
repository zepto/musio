r"""Wrapper for avdevice.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lavdevice /usr/include/libavdevice/avdevice.h /usr/include/libavdevice/version.h -L/usr/include/libavutil -o avdevice.py

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
_libs["avdevice"] = load_library("avdevice")

# 1 libraries
# End libraries

# No modules

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

enum_AVPixelFormat = c_int# /usr/include/libavutil/pixfmt.h: 64

enum_AVColorPrimaries = c_int# /usr/include/libavutil/pixfmt.h: 458

enum_AVColorTransferCharacteristic = c_int# /usr/include/libavutil/pixfmt.h: 483

enum_AVColorSpace = c_int# /usr/include/libavutil/pixfmt.h: 512

enum_AVColorRange = c_int# /usr/include/libavutil/pixfmt.h: 551

enum_AVChromaLocation = c_int# /usr/include/libavutil/pixfmt.h: 605

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

# /usr/include/libavutil/dict.h: 86
class struct_AVDictionary(Structure):
    pass

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 86

enum_AVSampleFormat = c_int# /usr/include/libavutil/samplefmt.h: 58

enum_AVOptionType = c_int# /usr/include/libavutil/opt.h: 223

# /usr/include/libavutil/opt.h: 267
class union_anon_26(Union):
    pass

union_anon_26.__slots__ = [
    'i64',
    'dbl',
    'str',
    'q',
]
union_anon_26._fields_ = [
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
    ('default_val', union_anon_26),
    ('min', c_double),
    ('max', c_double),
    ('flags', c_int),
    ('unit', String),
]

AVOption = struct_AVOption# /usr/include/libavutil/opt.h: 305

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

enum_AVCodecID = c_int# /usr/include/libavcodec/codec_id.h: 46

enum_AVFieldOrder = c_int# /usr/include/libavcodec/codec_par.h: 36

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

enum_AVPacketSideDataType = c_int# /usr/include/libavcodec/packet.h: 40

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

enum_AVDiscard = c_int# /usr/include/libavcodec/avcodec.h: 227

enum_AVAudioServiceType = c_int# /usr/include/libavcodec/avcodec.h: 239

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

enum_AVPictureStructure = c_int# /usr/include/libavcodec/avcodec.h: 3370

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

# /usr/include/libavformat/avio.h: 61
class struct_AVIOInterruptCB(Structure):
    pass

struct_AVIOInterruptCB.__slots__ = [
    'callback',
    'opaque',
]
struct_AVIOInterruptCB._fields_ = [
    ('callback', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('opaque', POINTER(None)),
]

AVIOInterruptCB = struct_AVIOInterruptCB# /usr/include/libavformat/avio.h: 61

enum_AVIODataMarkerType = c_int# /usr/include/libavformat/avio.h: 111

# /usr/include/libavformat/avio.h: 352
class struct_AVIOContext(Structure):
    pass

struct_AVIOContext.__slots__ = [
    'av_class',
    'buffer',
    'buffer_size',
    'buf_ptr',
    'buf_end',
    'opaque',
    'read_packet',
    'write_packet',
    'seek',
    'pos',
    'eof_reached',
    'write_flag',
    'max_packet_size',
    'checksum',
    'checksum_ptr',
    'update_checksum',
    'error',
    'read_pause',
    'read_seek',
    'seekable',
    'maxsize',
    'direct',
    'bytes_read',
    'seek_count',
    'writeout_count',
    'orig_buffer_size',
    'short_seek_threshold',
    'protocol_whitelist',
    'protocol_blacklist',
    'write_data_type',
    'ignore_boundary_point',
    'current_type',
    'last_time',
    'short_seek_get',
    'written',
    'buf_ptr_max',
    'min_packet_size',
]
struct_AVIOContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('buffer', POINTER(c_ubyte)),
    ('buffer_size', c_int),
    ('buf_ptr', POINTER(c_ubyte)),
    ('buf_end', POINTER(c_ubyte)),
    ('opaque', POINTER(None)),
    ('read_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_uint8), c_int)),
    ('write_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_uint8), c_int)),
    ('seek', CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int64, c_int)),
    ('pos', c_int64),
    ('eof_reached', c_int),
    ('write_flag', c_int),
    ('max_packet_size', c_int),
    ('checksum', c_ulong),
    ('checksum_ptr', POINTER(c_ubyte)),
    ('update_checksum', CFUNCTYPE(UNCHECKED(c_ulong), c_ulong, POINTER(c_uint8), c_uint)),
    ('error', c_int),
    ('read_pause', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int)),
    ('read_seek', CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int, c_int64, c_int)),
    ('seekable', c_int),
    ('maxsize', c_int64),
    ('direct', c_int),
    ('bytes_read', c_int64),
    ('seek_count', c_int),
    ('writeout_count', c_int),
    ('orig_buffer_size', c_int),
    ('short_seek_threshold', c_int),
    ('protocol_whitelist', String),
    ('protocol_blacklist', String),
    ('write_data_type', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_uint8), c_int, enum_AVIODataMarkerType, c_int64)),
    ('ignore_boundary_point', c_int),
    ('current_type', enum_AVIODataMarkerType),
    ('last_time', c_int64),
    ('short_seek_get', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('written', c_int64),
    ('buf_ptr_max', POINTER(c_ubyte)),
    ('min_packet_size', c_int),
]

AVIOContext = struct_AVIOContext# /usr/include/libavformat/avio.h: 352

# /usr/include/libavformat/avformat.h: 1234
class struct_AVFormatContext(Structure):
    pass

# /usr/include/libavdevice/avdevice.h: 465
class struct_AVDeviceInfoList(Structure):
    pass

# /usr/include/libavdevice/avdevice.h: 401
class struct_AVDeviceCapabilitiesQuery(Structure):
    pass

# /usr/include/libavformat/avformat.h: 436
class struct_AVCodecTag(Structure):
    pass

# /usr/include/libavformat/avformat.h: 446
class struct_AVProbeData(Structure):
    pass

struct_AVProbeData.__slots__ = [
    'filename',
    'buf',
    'buf_size',
    'mime_type',
]
struct_AVProbeData._fields_ = [
    ('filename', String),
    ('buf', POINTER(c_ubyte)),
    ('buf_size', c_int),
    ('mime_type', String),
]

AVProbeData = struct_AVProbeData# /usr/include/libavformat/avformat.h: 446

# /usr/include/libavformat/avformat.h: 490
class struct_AVOutputFormat(Structure):
    pass

struct_AVOutputFormat.__slots__ = [
    'name',
    'long_name',
    'mime_type',
    'extensions',
    'audio_codec',
    'video_codec',
    'subtitle_codec',
    'flags',
    'codec_tag',
    'priv_class',
    'next',
    'priv_data_size',
    'write_header',
    'write_packet',
    'write_trailer',
    'interleave_packet',
    'query_codec',
    'get_output_timestamp',
    'control_message',
    'write_uncoded_frame',
    'get_device_list',
    'create_device_capabilities',
    'free_device_capabilities',
    'data_codec',
    'init',
    'deinit',
    'check_bitstream',
]
struct_AVOutputFormat._fields_ = [
    ('name', String),
    ('long_name', String),
    ('mime_type', String),
    ('extensions', String),
    ('audio_codec', enum_AVCodecID),
    ('video_codec', enum_AVCodecID),
    ('subtitle_codec', enum_AVCodecID),
    ('flags', c_int),
    ('codec_tag', POINTER(POINTER(struct_AVCodecTag))),
    ('priv_class', POINTER(AVClass)),
    ('next', POINTER(struct_AVOutputFormat)),
    ('priv_data_size', c_int),
    ('write_header', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('write_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(AVPacket))),
    ('write_trailer', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('interleave_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(AVPacket), POINTER(AVPacket), c_int)),
    ('query_codec', CFUNCTYPE(UNCHECKED(c_int), enum_AVCodecID, c_int)),
    ('get_output_timestamp', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVFormatContext), c_int, POINTER(c_int64), POINTER(c_int64))),
    ('control_message', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, POINTER(None), c_size_t)),
    ('write_uncoded_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, POINTER(POINTER(AVFrame)), c_uint)),
    ('get_device_list', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceInfoList))),
    ('create_device_capabilities', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceCapabilitiesQuery))),
    ('free_device_capabilities', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceCapabilitiesQuery))),
    ('data_codec', enum_AVCodecID),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('deinit', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVFormatContext))),
    ('check_bitstream', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(AVPacket))),
]

AVOutputFormat = struct_AVOutputFormat# /usr/include/libavformat/avformat.h: 631

# /usr/include/libavformat/avformat.h: 640
class struct_AVInputFormat(Structure):
    pass

struct_AVInputFormat.__slots__ = [
    'name',
    'long_name',
    'flags',
    'extensions',
    'codec_tag',
    'priv_class',
    'mime_type',
    'next',
    'raw_codec_id',
    'priv_data_size',
    'read_probe',
    'read_header',
    'read_packet',
    'read_close',
    'read_seek',
    'read_timestamp',
    'read_play',
    'read_pause',
    'read_seek2',
    'get_device_list',
    'create_device_capabilities',
    'free_device_capabilities',
]
struct_AVInputFormat._fields_ = [
    ('name', String),
    ('long_name', String),
    ('flags', c_int),
    ('extensions', String),
    ('codec_tag', POINTER(POINTER(struct_AVCodecTag))),
    ('priv_class', POINTER(AVClass)),
    ('mime_type', String),
    ('next', POINTER(struct_AVInputFormat)),
    ('raw_codec_id', c_int),
    ('priv_data_size', c_int),
    ('read_probe', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVProbeData))),
    ('read_header', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('read_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(AVPacket))),
    ('read_close', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('read_seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, c_int64, c_int)),
    ('read_timestamp', CFUNCTYPE(UNCHECKED(c_int64), POINTER(struct_AVFormatContext), c_int, POINTER(c_int64), c_int64)),
    ('read_play', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('read_pause', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext))),
    ('read_seek2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, c_int64, c_int64, c_int64, c_int)),
    ('get_device_list', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceInfoList))),
    ('create_device_capabilities', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceCapabilitiesQuery))),
    ('free_device_capabilities', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(struct_AVDeviceCapabilitiesQuery))),
]

AVInputFormat = struct_AVInputFormat# /usr/include/libavformat/avformat.h: 787

enum_AVStreamParseType = c_int# /usr/include/libavformat/avformat.h: 792

# /usr/include/libavformat/avformat.h: 818
class struct_AVIndexEntry(Structure):
    pass

struct_AVIndexEntry.__slots__ = [
    'pos',
    'timestamp',
    'flags',
    'size',
    'min_distance',
]
struct_AVIndexEntry._fields_ = [
    ('pos', c_int64),
    ('timestamp', c_int64),
    ('flags', c_int, 2),
    ('size', c_int, 30),
    ('min_distance', c_int),
]

AVIndexEntry = struct_AVIndexEntry# /usr/include/libavformat/avformat.h: 818

# /usr/include/libavformat/avformat.h: 850
class struct_AVStreamInternal(Structure):
    pass

AVStreamInternal = struct_AVStreamInternal# /usr/include/libavformat/avformat.h: 850

# /usr/include/libavformat/avformat.h: 1116
class struct_AVStream(Structure):
    pass

struct_AVStream.__slots__ = [
    'index',
    'id',
    'codec',
    'priv_data',
    'time_base',
    'start_time',
    'duration',
    'nb_frames',
    'disposition',
    'discard',
    'sample_aspect_ratio',
    'metadata',
    'avg_frame_rate',
    'attached_pic',
    'side_data',
    'nb_side_data',
    'event_flags',
    'r_frame_rate',
    'recommended_encoder_configuration',
    'codecpar',
    'unused',
    'pts_wrap_bits',
    'first_dts',
    'cur_dts',
    'last_IP_pts',
    'last_IP_duration',
    'probe_packets',
    'codec_info_nb_frames',
    'need_parsing',
    'parser',
    'unused7',
    'unused6',
    'unused5',
    'index_entries',
    'nb_index_entries',
    'index_entries_allocated_size',
    'stream_identifier',
    'unused8',
    'unused9',
    'unused10',
    'internal',
]
struct_AVStream._fields_ = [
    ('index', c_int),
    ('id', c_int),
    ('codec', POINTER(AVCodecContext)),
    ('priv_data', POINTER(None)),
    ('time_base', AVRational),
    ('start_time', c_int64),
    ('duration', c_int64),
    ('nb_frames', c_int64),
    ('disposition', c_int),
    ('discard', enum_AVDiscard),
    ('sample_aspect_ratio', AVRational),
    ('metadata', POINTER(AVDictionary)),
    ('avg_frame_rate', AVRational),
    ('attached_pic', AVPacket),
    ('side_data', POINTER(AVPacketSideData)),
    ('nb_side_data', c_int),
    ('event_flags', c_int),
    ('r_frame_rate', AVRational),
    ('recommended_encoder_configuration', String),
    ('codecpar', POINTER(AVCodecParameters)),
    ('unused', POINTER(None)),
    ('pts_wrap_bits', c_int),
    ('first_dts', c_int64),
    ('cur_dts', c_int64),
    ('last_IP_pts', c_int64),
    ('last_IP_duration', c_int),
    ('probe_packets', c_int),
    ('codec_info_nb_frames', c_int),
    ('need_parsing', enum_AVStreamParseType),
    ('parser', POINTER(struct_AVCodecParserContext)),
    ('unused7', POINTER(None)),
    ('unused6', AVProbeData),
    ('unused5', c_int64 * int((16 + 1))),
    ('index_entries', POINTER(AVIndexEntry)),
    ('nb_index_entries', c_int),
    ('index_entries_allocated_size', c_uint),
    ('stream_identifier', c_int),
    ('unused8', c_int),
    ('unused9', c_int),
    ('unused10', c_int),
    ('internal', POINTER(AVStreamInternal)),
]

AVStream = struct_AVStream# /usr/include/libavformat/avformat.h: 1116

# /usr/include/libavformat/avformat.h: 1177
class struct_AVProgram(Structure):
    pass

struct_AVProgram.__slots__ = [
    'id',
    'flags',
    'discard',
    'stream_index',
    'nb_stream_indexes',
    'metadata',
    'program_num',
    'pmt_pid',
    'pcr_pid',
    'pmt_version',
    'start_time',
    'end_time',
    'pts_wrap_reference',
    'pts_wrap_behavior',
]
struct_AVProgram._fields_ = [
    ('id', c_int),
    ('flags', c_int),
    ('discard', enum_AVDiscard),
    ('stream_index', POINTER(c_uint)),
    ('nb_stream_indexes', c_uint),
    ('metadata', POINTER(AVDictionary)),
    ('program_num', c_int),
    ('pmt_pid', c_int),
    ('pcr_pid', c_int),
    ('pmt_version', c_int),
    ('start_time', c_int64),
    ('end_time', c_int64),
    ('pts_wrap_reference', c_int64),
    ('pts_wrap_behavior', c_int),
]

AVProgram = struct_AVProgram# /usr/include/libavformat/avformat.h: 1177

# /usr/include/libavformat/avformat.h: 1196
class struct_AVChapter(Structure):
    pass

struct_AVChapter.__slots__ = [
    'id',
    'time_base',
    'start',
    'end',
    'metadata',
]
struct_AVChapter._fields_ = [
    ('id', c_int),
    ('time_base', AVRational),
    ('start', c_int64),
    ('end', c_int64),
    ('metadata', POINTER(AVDictionary)),
]

AVChapter = struct_AVChapter# /usr/include/libavformat/avformat.h: 1196

av_format_control_message = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, POINTER(None), c_size_t)# /usr/include/libavformat/avformat.h: 1202

enum_AVDurationEstimationMethod = c_int# /usr/include/libavformat/avformat.h: 1212

# /usr/include/libavformat/avformat.h: 1218
class struct_AVFormatInternal(Structure):
    pass

AVFormatInternal = struct_AVFormatInternal# /usr/include/libavformat/avformat.h: 1218

struct_AVFormatContext.__slots__ = [
    'av_class',
    'iformat',
    'oformat',
    'priv_data',
    'pb',
    'ctx_flags',
    'nb_streams',
    'streams',
    'filename',
    'url',
    'start_time',
    'duration',
    'bit_rate',
    'packet_size',
    'max_delay',
    'flags',
    'probesize',
    'max_analyze_duration',
    'key',
    'keylen',
    'nb_programs',
    'programs',
    'video_codec_id',
    'audio_codec_id',
    'subtitle_codec_id',
    'max_index_size',
    'max_picture_buffer',
    'nb_chapters',
    'chapters',
    'metadata',
    'start_time_realtime',
    'fps_probe_size',
    'error_recognition',
    'interrupt_callback',
    'debug',
    'max_interleave_delta',
    'strict_std_compliance',
    'event_flags',
    'max_ts_probe',
    'avoid_negative_ts',
    'ts_id',
    'audio_preload',
    'max_chunk_duration',
    'max_chunk_size',
    'use_wallclock_as_timestamps',
    'avio_flags',
    'duration_estimation_method',
    'skip_initial_bytes',
    'correct_ts_overflow',
    'seek2any',
    'flush_packets',
    'probe_score',
    'format_probesize',
    'codec_whitelist',
    'format_whitelist',
    'internal',
    'io_repositioned',
    'video_codec',
    'audio_codec',
    'subtitle_codec',
    'data_codec',
    'metadata_header_padding',
    'opaque',
    'control_message_cb',
    'output_ts_offset',
    'dump_separator',
    'data_codec_id',
    'open_cb',
    'protocol_whitelist',
    'io_open',
    'io_close',
    'protocol_blacklist',
    'max_streams',
    'skip_estimate_duration_from_pts',
    'max_probe_packets',
]
struct_AVFormatContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('iformat', POINTER(struct_AVInputFormat)),
    ('oformat', POINTER(struct_AVOutputFormat)),
    ('priv_data', POINTER(None)),
    ('pb', POINTER(AVIOContext)),
    ('ctx_flags', c_int),
    ('nb_streams', c_uint),
    ('streams', POINTER(POINTER(AVStream))),
    ('filename', c_char * int(1024)),
    ('url', String),
    ('start_time', c_int64),
    ('duration', c_int64),
    ('bit_rate', c_int64),
    ('packet_size', c_uint),
    ('max_delay', c_int),
    ('flags', c_int),
    ('probesize', c_int64),
    ('max_analyze_duration', c_int64),
    ('key', POINTER(c_uint8)),
    ('keylen', c_int),
    ('nb_programs', c_uint),
    ('programs', POINTER(POINTER(AVProgram))),
    ('video_codec_id', enum_AVCodecID),
    ('audio_codec_id', enum_AVCodecID),
    ('subtitle_codec_id', enum_AVCodecID),
    ('max_index_size', c_uint),
    ('max_picture_buffer', c_uint),
    ('nb_chapters', c_uint),
    ('chapters', POINTER(POINTER(AVChapter))),
    ('metadata', POINTER(AVDictionary)),
    ('start_time_realtime', c_int64),
    ('fps_probe_size', c_int),
    ('error_recognition', c_int),
    ('interrupt_callback', AVIOInterruptCB),
    ('debug', c_int),
    ('max_interleave_delta', c_int64),
    ('strict_std_compliance', c_int),
    ('event_flags', c_int),
    ('max_ts_probe', c_int),
    ('avoid_negative_ts', c_int),
    ('ts_id', c_int),
    ('audio_preload', c_int),
    ('max_chunk_duration', c_int),
    ('max_chunk_size', c_int),
    ('use_wallclock_as_timestamps', c_int),
    ('avio_flags', c_int),
    ('duration_estimation_method', enum_AVDurationEstimationMethod),
    ('skip_initial_bytes', c_int64),
    ('correct_ts_overflow', c_uint),
    ('seek2any', c_int),
    ('flush_packets', c_int),
    ('probe_score', c_int),
    ('format_probesize', c_int),
    ('codec_whitelist', String),
    ('format_whitelist', String),
    ('internal', POINTER(AVFormatInternal)),
    ('io_repositioned', c_int),
    ('video_codec', POINTER(AVCodec)),
    ('audio_codec', POINTER(AVCodec)),
    ('subtitle_codec', POINTER(AVCodec)),
    ('data_codec', POINTER(AVCodec)),
    ('metadata_header_padding', c_int),
    ('opaque', POINTER(None)),
    ('control_message_cb', av_format_control_message),
    ('output_ts_offset', c_int64),
    ('dump_separator', POINTER(c_uint8)),
    ('data_codec_id', enum_AVCodecID),
    ('open_cb', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(POINTER(AVIOContext)), String, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary)))),
    ('protocol_whitelist', String),
    ('io_open', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(POINTER(AVIOContext)), String, c_int, POINTER(POINTER(AVDictionary)))),
    ('io_close', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVFormatContext), POINTER(AVIOContext))),
    ('protocol_blacklist', String),
    ('max_streams', c_int),
    ('skip_estimate_duration_from_pts', c_int),
    ('max_probe_packets', c_int),
]

AVFormatContext = struct_AVFormatContext# /usr/include/libavformat/avformat.h: 1865

# /usr/include/libavdevice/avdevice.h: 56
if _libs["avdevice"].has("avdevice_version", "cdecl"):
    avdevice_version = _libs["avdevice"].get("avdevice_version", "cdecl")
    avdevice_version.argtypes = []
    avdevice_version.restype = c_uint

# /usr/include/libavdevice/avdevice.h: 61
if _libs["avdevice"].has("avdevice_configuration", "cdecl"):
    avdevice_configuration = _libs["avdevice"].get("avdevice_configuration", "cdecl")
    avdevice_configuration.argtypes = []
    avdevice_configuration.restype = c_char_p

# /usr/include/libavdevice/avdevice.h: 66
if _libs["avdevice"].has("avdevice_license", "cdecl"):
    avdevice_license = _libs["avdevice"].get("avdevice_license", "cdecl")
    avdevice_license.argtypes = []
    avdevice_license.restype = c_char_p

# /usr/include/libavdevice/avdevice.h: 71
if _libs["avdevice"].has("avdevice_register_all", "cdecl"):
    avdevice_register_all = _libs["avdevice"].get("avdevice_register_all", "cdecl")
    avdevice_register_all.argtypes = []
    avdevice_register_all.restype = None

# /usr/include/libavdevice/avdevice.h: 80
if _libs["avdevice"].has("av_input_audio_device_next", "cdecl"):
    av_input_audio_device_next = _libs["avdevice"].get("av_input_audio_device_next", "cdecl")
    av_input_audio_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_audio_device_next.restype = POINTER(AVInputFormat)

# /usr/include/libavdevice/avdevice.h: 89
if _libs["avdevice"].has("av_input_video_device_next", "cdecl"):
    av_input_video_device_next = _libs["avdevice"].get("av_input_video_device_next", "cdecl")
    av_input_video_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_video_device_next.restype = POINTER(AVInputFormat)

# /usr/include/libavdevice/avdevice.h: 98
if _libs["avdevice"].has("av_output_audio_device_next", "cdecl"):
    av_output_audio_device_next = _libs["avdevice"].get("av_output_audio_device_next", "cdecl")
    av_output_audio_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_audio_device_next.restype = POINTER(AVOutputFormat)

# /usr/include/libavdevice/avdevice.h: 107
if _libs["avdevice"].has("av_output_video_device_next", "cdecl"):
    av_output_video_device_next = _libs["avdevice"].get("av_output_video_device_next", "cdecl")
    av_output_video_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_video_device_next.restype = POINTER(AVOutputFormat)

# /usr/include/libavdevice/avdevice.h: 114
class struct_AVDeviceRect(Structure):
    pass

struct_AVDeviceRect.__slots__ = [
    'x',
    'y',
    'width',
    'height',
]
struct_AVDeviceRect._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
]

AVDeviceRect = struct_AVDeviceRect# /usr/include/libavdevice/avdevice.h: 114

enum_AVAppToDevMessageType = c_int# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_NONE = (((ord('E') | (ord('N') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(b'N'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_WINDOW_SIZE = (((ord('M') | (ord('O') << 8)) | (ord('E') << 16)) | ((c_uint (ord_if_char(b'G'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_WINDOW_REPAINT = (((ord('A') | (ord('P') << 8)) | (ord('E') << 16)) | ((c_uint (ord_if_char(b'R'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_PAUSE = (((ord(' ') | (ord('U') << 8)) | (ord('A') << 16)) | ((c_uint (ord_if_char(b'P'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_PLAY = (((ord('Y') | (ord('A') << 8)) | (ord('L') << 16)) | ((c_uint (ord_if_char(b'P'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_TOGGLE_PAUSE = (((ord('T') | (ord('U') << 8)) | (ord('A') << 16)) | ((c_uint (ord_if_char(b'P'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_SET_VOLUME = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(b'S'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(b' '))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_UNMUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(b'U'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_TOGGLE_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(b'T'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_GET_VOLUME = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(b'G'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

AV_APP_TO_DEV_GET_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(b'G'))).value << 24))# /usr/include/libavdevice/avdevice.h: 119

enum_AVDevToAppMessageType = c_int# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_NONE = (((ord('E') | (ord('N') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(b'N'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_CREATE_WINDOW_BUFFER = (((ord('E') | (ord('R') << 8)) | (ord('C') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_PREPARE_WINDOW_BUFFER = (((ord('E') | (ord('R') << 8)) | (ord('P') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_DISPLAY_WINDOW_BUFFER = (((ord('S') | (ord('I') << 8)) | (ord('D') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_DESTROY_WINDOW_BUFFER = (((ord('S') | (ord('E') << 8)) | (ord('D') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_BUFFER_OVERFLOW = (((ord('L') | (ord('F') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_BUFFER_UNDERFLOW = (((ord('L') | (ord('F') << 8)) | (ord('U') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_BUFFER_READABLE = (((ord(' ') | (ord('D') << 8)) | (ord('R') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_BUFFER_WRITABLE = (((ord(' ') | (ord('R') << 8)) | (ord('W') << 16)) | ((c_uint (ord_if_char(b'B'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_MUTE_STATE_CHANGED = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(b'C'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

AV_DEV_TO_APP_VOLUME_LEVEL_CHANGED = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(b'C'))).value << 24))# /usr/include/libavdevice/avdevice.h: 198

# /usr/include/libavdevice/avdevice.h: 306
if _libs["avdevice"].has("avdevice_app_to_dev_control_message", "cdecl"):
    avdevice_app_to_dev_control_message = _libs["avdevice"].get("avdevice_app_to_dev_control_message", "cdecl")
    avdevice_app_to_dev_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVAppToDevMessageType, POINTER(None), c_size_t]
    avdevice_app_to_dev_control_message.restype = c_int

# /usr/include/libavdevice/avdevice.h: 320
if _libs["avdevice"].has("avdevice_dev_to_app_control_message", "cdecl"):
    avdevice_dev_to_app_control_message = _libs["avdevice"].get("avdevice_dev_to_app_control_message", "cdecl")
    avdevice_dev_to_app_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVDevToAppMessageType, POINTER(None), c_size_t]
    avdevice_dev_to_app_control_message.restype = c_int

struct_AVDeviceCapabilitiesQuery.__slots__ = [
    'av_class',
    'device_context',
    'codec',
    'sample_format',
    'pixel_format',
    'sample_rate',
    'channels',
    'channel_layout',
    'window_width',
    'window_height',
    'frame_width',
    'frame_height',
    'fps',
]
struct_AVDeviceCapabilitiesQuery._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('device_context', POINTER(AVFormatContext)),
    ('codec', enum_AVCodecID),
    ('sample_format', enum_AVSampleFormat),
    ('pixel_format', enum_AVPixelFormat),
    ('sample_rate', c_int),
    ('channels', c_int),
    ('channel_layout', c_int64),
    ('window_width', c_int),
    ('window_height', c_int),
    ('frame_width', c_int),
    ('frame_height', c_int),
    ('fps', AVRational),
]

AVDeviceCapabilitiesQuery = struct_AVDeviceCapabilitiesQuery# /usr/include/libavdevice/avdevice.h: 415

# /usr/include/libavdevice/avdevice.h: 421
try:
    av_device_capabilities = (POINTER(AVOption)).in_dll(_libs["avdevice"], "av_device_capabilities")
except:
    pass

# /usr/include/libavdevice/avdevice.h: 441
if _libs["avdevice"].has("avdevice_capabilities_create", "cdecl"):
    avdevice_capabilities_create = _libs["avdevice"].get("avdevice_capabilities_create", "cdecl")
    avdevice_capabilities_create.argtypes = [POINTER(POINTER(AVDeviceCapabilitiesQuery)), POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avdevice_capabilities_create.restype = c_int

# /usr/include/libavdevice/avdevice.h: 451
if _libs["avdevice"].has("avdevice_capabilities_free", "cdecl"):
    avdevice_capabilities_free = _libs["avdevice"].get("avdevice_capabilities_free", "cdecl")
    avdevice_capabilities_free.argtypes = [POINTER(POINTER(AVDeviceCapabilitiesQuery)), POINTER(AVFormatContext)]
    avdevice_capabilities_free.restype = None

# /usr/include/libavdevice/avdevice.h: 460
class struct_AVDeviceInfo(Structure):
    pass

struct_AVDeviceInfo.__slots__ = [
    'device_name',
    'device_description',
]
struct_AVDeviceInfo._fields_ = [
    ('device_name', String),
    ('device_description', String),
]

AVDeviceInfo = struct_AVDeviceInfo# /usr/include/libavdevice/avdevice.h: 460

struct_AVDeviceInfoList.__slots__ = [
    'devices',
    'nb_devices',
    'default_device',
]
struct_AVDeviceInfoList._fields_ = [
    ('devices', POINTER(POINTER(AVDeviceInfo))),
    ('nb_devices', c_int),
    ('default_device', c_int),
]

AVDeviceInfoList = struct_AVDeviceInfoList# /usr/include/libavdevice/avdevice.h: 469

# /usr/include/libavdevice/avdevice.h: 484
if _libs["avdevice"].has("avdevice_list_devices", "cdecl"):
    avdevice_list_devices = _libs["avdevice"].get("avdevice_list_devices", "cdecl")
    avdevice_list_devices.argtypes = [POINTER(struct_AVFormatContext), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_devices.restype = c_int

# /usr/include/libavdevice/avdevice.h: 491
if _libs["avdevice"].has("avdevice_free_list_devices", "cdecl"):
    avdevice_free_list_devices = _libs["avdevice"].get("avdevice_free_list_devices", "cdecl")
    avdevice_free_list_devices.argtypes = [POINTER(POINTER(AVDeviceInfoList))]
    avdevice_free_list_devices.restype = None

# /usr/include/libavdevice/avdevice.h: 510
if _libs["avdevice"].has("avdevice_list_input_sources", "cdecl"):
    avdevice_list_input_sources = _libs["avdevice"].get("avdevice_list_input_sources", "cdecl")
    avdevice_list_input_sources.argtypes = [POINTER(struct_AVInputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_input_sources.restype = c_int

# /usr/include/libavdevice/avdevice.h: 512
if _libs["avdevice"].has("avdevice_list_output_sinks", "cdecl"):
    avdevice_list_output_sinks = _libs["avdevice"].get("avdevice_list_output_sinks", "cdecl")
    avdevice_list_output_sinks.argtypes = [POINTER(struct_AVOutputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_output_sinks.restype = c_int

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

# /usr/include/libavdevice/version.h: 30
try:
    LIBAVDEVICE_VERSION_MAJOR = 58
except:
    pass

# /usr/include/libavdevice/version.h: 31
try:
    LIBAVDEVICE_VERSION_MINOR = 13
except:
    pass

# /usr/include/libavdevice/version.h: 32
try:
    LIBAVDEVICE_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavdevice/version.h: 34
try:
    LIBAVDEVICE_VERSION_INT = (AV_VERSION_INT (LIBAVDEVICE_VERSION_MAJOR, LIBAVDEVICE_VERSION_MINOR, LIBAVDEVICE_VERSION_MICRO))
except:
    pass

# /usr/include/libavdevice/version.h: 40
try:
    LIBAVDEVICE_BUILD = LIBAVDEVICE_VERSION_INT
except:
    pass

# /usr/include/libavdevice/version.h: 50
try:
    FF_API_DEVICE_CAPABILITIES = (LIBAVDEVICE_VERSION_MAJOR < 60)
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

# /usr/include/libavformat/version.h: 34
try:
    LIBAVFORMAT_VERSION_MAJOR = 58
except:
    pass

# /usr/include/libavformat/version.h: 35
try:
    LIBAVFORMAT_VERSION_MINOR = 76
except:
    pass

# /usr/include/libavformat/version.h: 36
try:
    LIBAVFORMAT_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavformat/version.h: 38
try:
    LIBAVFORMAT_VERSION_INT = (AV_VERSION_INT (LIBAVFORMAT_VERSION_MAJOR, LIBAVFORMAT_VERSION_MINOR, LIBAVFORMAT_VERSION_MICRO))
except:
    pass

# /usr/include/libavformat/version.h: 44
try:
    LIBAVFORMAT_BUILD = LIBAVFORMAT_VERSION_INT
except:
    pass

# /usr/include/libavformat/version.h: 59
try:
    FF_API_COMPUTE_PKT_FIELDS2 = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 62
try:
    FF_API_OLD_OPEN_CALLBACKS = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 65
try:
    FF_API_LAVF_AVCTX = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 68
try:
    FF_API_HTTP_USER_AGENT = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 71
try:
    FF_API_HLS_WRAP = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 74
try:
    FF_API_HLS_USE_LOCALTIME = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 77
try:
    FF_API_LAVF_KEEPSIDE_FLAG = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 80
try:
    FF_API_OLD_ROTATE_API = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 83
try:
    FF_API_FORMAT_GET_SET = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 86
try:
    FF_API_OLD_AVIO_EOF_0 = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 89
try:
    FF_API_LAVF_FFSERVER = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 92
try:
    FF_API_FORMAT_FILENAME = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 95
try:
    FF_API_OLD_RTSP_OPTIONS = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 101
try:
    FF_API_DASH_MIN_SEG_DURATION = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 104
try:
    FF_API_LAVF_MP4A_LATM = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 107
try:
    FF_API_AVIOFORMAT = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 110
try:
    FF_API_DEMUXER_OPEN = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 113
try:
    FF_API_CHAPTER_ID_INT = (LIBAVFORMAT_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavformat/version.h: 116
try:
    FF_API_LAVF_PRIV_OPT = (LIBAVFORMAT_VERSION_MAJOR < 60)
except:
    pass

# /usr/include/libavformat/version.h: 121
try:
    FF_API_R_FRAME_RATE = 1
except:
    pass

AVDeviceInfoList = struct_AVDeviceInfoList# /usr/include/libavdevice/avdevice.h: 465

AVDeviceCapabilitiesQuery = struct_AVDeviceCapabilitiesQuery# /usr/include/libavdevice/avdevice.h: 401

AVDeviceRect = struct_AVDeviceRect# /usr/include/libavdevice/avdevice.h: 114

AVDeviceInfo = struct_AVDeviceInfo# /usr/include/libavdevice/avdevice.h: 460

# No inserted files

# No prefix-stripping

