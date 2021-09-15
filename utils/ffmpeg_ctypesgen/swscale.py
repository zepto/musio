r"""Wrapper for swscale.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lswscale /usr/include/libswscale/swscale.h /usr/include/libswscale/version.h -L/usr/include/libavutil -o swscale.py

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
_libs["swscale"] = load_library("swscale")

# 1 libraries
# End libraries

# No modules

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

enum_AVPixelFormat = c_int# /usr/include/libavutil/pixfmt.h: 64

# /usr/include/libswscale/swscale.h: 45
if _libs["swscale"].has("swscale_version", "cdecl"):
    swscale_version = _libs["swscale"].get("swscale_version", "cdecl")
    swscale_version.argtypes = []
    swscale_version.restype = c_uint

# /usr/include/libswscale/swscale.h: 50
if _libs["swscale"].has("swscale_configuration", "cdecl"):
    swscale_configuration = _libs["swscale"].get("swscale_configuration", "cdecl")
    swscale_configuration.argtypes = []
    swscale_configuration.restype = c_char_p

# /usr/include/libswscale/swscale.h: 55
if _libs["swscale"].has("swscale_license", "cdecl"):
    swscale_license = _libs["swscale"].get("swscale_license", "cdecl")
    swscale_license.argtypes = []
    swscale_license.restype = c_char_p

# /usr/include/libswscale/swscale.h: 105
if _libs["swscale"].has("sws_getCoefficients", "cdecl"):
    sws_getCoefficients = _libs["swscale"].get("sws_getCoefficients", "cdecl")
    sws_getCoefficients.argtypes = [c_int]
    sws_getCoefficients.restype = POINTER(c_int)

# /usr/include/libswscale/swscale.h: 112
class struct_SwsVector(Structure):
    pass

struct_SwsVector.__slots__ = [
    'coeff',
    'length',
]
struct_SwsVector._fields_ = [
    ('coeff', POINTER(c_double)),
    ('length', c_int),
]

SwsVector = struct_SwsVector# /usr/include/libswscale/swscale.h: 112

# /usr/include/libswscale/swscale.h: 120
class struct_SwsFilter(Structure):
    pass

struct_SwsFilter.__slots__ = [
    'lumH',
    'lumV',
    'chrH',
    'chrV',
]
struct_SwsFilter._fields_ = [
    ('lumH', POINTER(SwsVector)),
    ('lumV', POINTER(SwsVector)),
    ('chrH', POINTER(SwsVector)),
    ('chrV', POINTER(SwsVector)),
]

SwsFilter = struct_SwsFilter# /usr/include/libswscale/swscale.h: 120

# /usr/include/libswscale/swscale.h: 122
class struct_SwsContext(Structure):
    pass

# /usr/include/libswscale/swscale.h: 128
if _libs["swscale"].has("sws_isSupportedInput", "cdecl"):
    sws_isSupportedInput = _libs["swscale"].get("sws_isSupportedInput", "cdecl")
    sws_isSupportedInput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedInput.restype = c_int

# /usr/include/libswscale/swscale.h: 134
if _libs["swscale"].has("sws_isSupportedOutput", "cdecl"):
    sws_isSupportedOutput = _libs["swscale"].get("sws_isSupportedOutput", "cdecl")
    sws_isSupportedOutput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedOutput.restype = c_int

# /usr/include/libswscale/swscale.h: 141
if _libs["swscale"].has("sws_isSupportedEndiannessConversion", "cdecl"):
    sws_isSupportedEndiannessConversion = _libs["swscale"].get("sws_isSupportedEndiannessConversion", "cdecl")
    sws_isSupportedEndiannessConversion.argtypes = [enum_AVPixelFormat]
    sws_isSupportedEndiannessConversion.restype = c_int

# /usr/include/libswscale/swscale.h: 148
if _libs["swscale"].has("sws_alloc_context", "cdecl"):
    sws_alloc_context = _libs["swscale"].get("sws_alloc_context", "cdecl")
    sws_alloc_context.argtypes = []
    sws_alloc_context.restype = POINTER(struct_SwsContext)

# /usr/include/libswscale/swscale.h: 157
if _libs["swscale"].has("sws_init_context", "cdecl"):
    sws_init_context = _libs["swscale"].get("sws_init_context", "cdecl")
    sws_init_context.argtypes = [POINTER(struct_SwsContext), POINTER(SwsFilter), POINTER(SwsFilter)]
    sws_init_context.restype = c_int

# /usr/include/libswscale/swscale.h: 163
if _libs["swscale"].has("sws_freeContext", "cdecl"):
    sws_freeContext = _libs["swscale"].get("sws_freeContext", "cdecl")
    sws_freeContext.argtypes = [POINTER(struct_SwsContext)]
    sws_freeContext.restype = None

# /usr/include/libswscale/swscale.h: 186
if _libs["swscale"].has("sws_getContext", "cdecl"):
    sws_getContext = _libs["swscale"].get("sws_getContext", "cdecl")
    sws_getContext.argtypes = [c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getContext.restype = POINTER(struct_SwsContext)

# /usr/include/libswscale/swscale.h: 217
if _libs["swscale"].has("sws_scale", "cdecl"):
    sws_scale = _libs["swscale"].get("sws_scale", "cdecl")
    sws_scale.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(c_uint8)), POINTER(c_int), c_int, c_int, POINTER(POINTER(c_uint8)), POINTER(c_int)]
    sws_scale.restype = c_int

# /usr/include/libswscale/swscale.h: 231
if _libs["swscale"].has("sws_setColorspaceDetails", "cdecl"):
    sws_setColorspaceDetails = _libs["swscale"].get("sws_setColorspaceDetails", "cdecl")
    sws_setColorspaceDetails.argtypes = [POINTER(struct_SwsContext), c_int * int(4), c_int, c_int * int(4), c_int, c_int, c_int, c_int]
    sws_setColorspaceDetails.restype = c_int

# /usr/include/libswscale/swscale.h: 238
if _libs["swscale"].has("sws_getColorspaceDetails", "cdecl"):
    sws_getColorspaceDetails = _libs["swscale"].get("sws_getColorspaceDetails", "cdecl")
    sws_getColorspaceDetails.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    sws_getColorspaceDetails.restype = c_int

# /usr/include/libswscale/swscale.h: 245
if _libs["swscale"].has("sws_allocVec", "cdecl"):
    sws_allocVec = _libs["swscale"].get("sws_allocVec", "cdecl")
    sws_allocVec.argtypes = [c_int]
    sws_allocVec.restype = POINTER(SwsVector)

# /usr/include/libswscale/swscale.h: 251
if _libs["swscale"].has("sws_getGaussianVec", "cdecl"):
    sws_getGaussianVec = _libs["swscale"].get("sws_getGaussianVec", "cdecl")
    sws_getGaussianVec.argtypes = [c_double, c_double]
    sws_getGaussianVec.restype = POINTER(SwsVector)

# /usr/include/libswscale/swscale.h: 256
if _libs["swscale"].has("sws_scaleVec", "cdecl"):
    sws_scaleVec = _libs["swscale"].get("sws_scaleVec", "cdecl")
    sws_scaleVec.argtypes = [POINTER(SwsVector), c_double]
    sws_scaleVec.restype = None

# /usr/include/libswscale/swscale.h: 261
if _libs["swscale"].has("sws_normalizeVec", "cdecl"):
    sws_normalizeVec = _libs["swscale"].get("sws_normalizeVec", "cdecl")
    sws_normalizeVec.argtypes = [POINTER(SwsVector), c_double]
    sws_normalizeVec.restype = None

# /usr/include/libswscale/swscale.h: 264
if _libs["swscale"].has("sws_getConstVec", "cdecl"):
    sws_getConstVec = _libs["swscale"].get("sws_getConstVec", "cdecl")
    sws_getConstVec.argtypes = [c_double, c_int]
    sws_getConstVec.restype = POINTER(SwsVector)

# /usr/include/libswscale/swscale.h: 265
if _libs["swscale"].has("sws_getIdentityVec", "cdecl"):
    sws_getIdentityVec = _libs["swscale"].get("sws_getIdentityVec", "cdecl")
    sws_getIdentityVec.argtypes = []
    sws_getIdentityVec.restype = POINTER(SwsVector)

# /usr/include/libswscale/swscale.h: 266
if _libs["swscale"].has("sws_convVec", "cdecl"):
    sws_convVec = _libs["swscale"].get("sws_convVec", "cdecl")
    sws_convVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
    sws_convVec.restype = None

# /usr/include/libswscale/swscale.h: 267
if _libs["swscale"].has("sws_addVec", "cdecl"):
    sws_addVec = _libs["swscale"].get("sws_addVec", "cdecl")
    sws_addVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
    sws_addVec.restype = None

# /usr/include/libswscale/swscale.h: 268
if _libs["swscale"].has("sws_subVec", "cdecl"):
    sws_subVec = _libs["swscale"].get("sws_subVec", "cdecl")
    sws_subVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
    sws_subVec.restype = None

# /usr/include/libswscale/swscale.h: 269
if _libs["swscale"].has("sws_shiftVec", "cdecl"):
    sws_shiftVec = _libs["swscale"].get("sws_shiftVec", "cdecl")
    sws_shiftVec.argtypes = [POINTER(SwsVector), c_int]
    sws_shiftVec.restype = None

# /usr/include/libswscale/swscale.h: 270
if _libs["swscale"].has("sws_cloneVec", "cdecl"):
    sws_cloneVec = _libs["swscale"].get("sws_cloneVec", "cdecl")
    sws_cloneVec.argtypes = [POINTER(SwsVector)]
    sws_cloneVec.restype = POINTER(SwsVector)

# /usr/include/libswscale/swscale.h: 271
if _libs["swscale"].has("sws_printVec2", "cdecl"):
    sws_printVec2 = _libs["swscale"].get("sws_printVec2", "cdecl")
    sws_printVec2.argtypes = [POINTER(SwsVector), POINTER(AVClass), c_int]
    sws_printVec2.restype = None

# /usr/include/libswscale/swscale.h: 274
if _libs["swscale"].has("sws_freeVec", "cdecl"):
    sws_freeVec = _libs["swscale"].get("sws_freeVec", "cdecl")
    sws_freeVec.argtypes = [POINTER(SwsVector)]
    sws_freeVec.restype = None

# /usr/include/libswscale/swscale.h: 276
if _libs["swscale"].has("sws_getDefaultFilter", "cdecl"):
    sws_getDefaultFilter = _libs["swscale"].get("sws_getDefaultFilter", "cdecl")
    sws_getDefaultFilter.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_int]
    sws_getDefaultFilter.restype = POINTER(SwsFilter)

# /usr/include/libswscale/swscale.h: 280
if _libs["swscale"].has("sws_freeFilter", "cdecl"):
    sws_freeFilter = _libs["swscale"].get("sws_freeFilter", "cdecl")
    sws_freeFilter.argtypes = [POINTER(SwsFilter)]
    sws_freeFilter.restype = None

# /usr/include/libswscale/swscale.h: 294
if _libs["swscale"].has("sws_getCachedContext", "cdecl"):
    sws_getCachedContext = _libs["swscale"].get("sws_getCachedContext", "cdecl")
    sws_getCachedContext.argtypes = [POINTER(struct_SwsContext), c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getCachedContext.restype = POINTER(struct_SwsContext)

# /usr/include/libswscale/swscale.h: 310
if _libs["swscale"].has("sws_convertPalette8ToPacked32", "cdecl"):
    sws_convertPalette8ToPacked32 = _libs["swscale"].get("sws_convertPalette8ToPacked32", "cdecl")
    sws_convertPalette8ToPacked32.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8)]
    sws_convertPalette8ToPacked32.restype = None

# /usr/include/libswscale/swscale.h: 322
if _libs["swscale"].has("sws_convertPalette8ToPacked24", "cdecl"):
    sws_convertPalette8ToPacked24 = _libs["swscale"].get("sws_convertPalette8ToPacked24", "cdecl")
    sws_convertPalette8ToPacked24.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8)]
    sws_convertPalette8ToPacked24.restype = None

# /usr/include/libswscale/swscale.h: 330
if _libs["swscale"].has("sws_get_class", "cdecl"):
    sws_get_class = _libs["swscale"].get("sws_get_class", "cdecl")
    sws_get_class.argtypes = []
    sws_get_class.restype = POINTER(AVClass)

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

# /usr/include/libswscale/version.h: 29
try:
    LIBSWSCALE_VERSION_MAJOR = 5
except:
    pass

# /usr/include/libswscale/version.h: 30
try:
    LIBSWSCALE_VERSION_MINOR = 9
except:
    pass

# /usr/include/libswscale/version.h: 31
try:
    LIBSWSCALE_VERSION_MICRO = 100
except:
    pass

# /usr/include/libswscale/version.h: 33
try:
    LIBSWSCALE_VERSION_INT = (AV_VERSION_INT (LIBSWSCALE_VERSION_MAJOR, LIBSWSCALE_VERSION_MINOR, LIBSWSCALE_VERSION_MICRO))
except:
    pass

# /usr/include/libswscale/version.h: 39
try:
    LIBSWSCALE_BUILD = LIBSWSCALE_VERSION_INT
except:
    pass

# /usr/include/libswscale/version.h: 50
try:
    FF_API_SWS_VECTOR = (LIBSWSCALE_VERSION_MAJOR < 6)
except:
    pass

# /usr/include/libswscale/swscale.h: 58
try:
    SWS_FAST_BILINEAR = 1
except:
    pass

# /usr/include/libswscale/swscale.h: 59
try:
    SWS_BILINEAR = 2
except:
    pass

# /usr/include/libswscale/swscale.h: 60
try:
    SWS_BICUBIC = 4
except:
    pass

# /usr/include/libswscale/swscale.h: 61
try:
    SWS_X = 8
except:
    pass

# /usr/include/libswscale/swscale.h: 62
try:
    SWS_POINT = 16
except:
    pass

# /usr/include/libswscale/swscale.h: 63
try:
    SWS_AREA = 32
except:
    pass

# /usr/include/libswscale/swscale.h: 64
try:
    SWS_BICUBLIN = 64
except:
    pass

# /usr/include/libswscale/swscale.h: 65
try:
    SWS_GAUSS = 128
except:
    pass

# /usr/include/libswscale/swscale.h: 66
try:
    SWS_SINC = 256
except:
    pass

# /usr/include/libswscale/swscale.h: 67
try:
    SWS_LANCZOS = 512
except:
    pass

# /usr/include/libswscale/swscale.h: 68
try:
    SWS_SPLINE = 1024
except:
    pass

# /usr/include/libswscale/swscale.h: 70
try:
    SWS_SRC_V_CHR_DROP_MASK = 196608
except:
    pass

# /usr/include/libswscale/swscale.h: 71
try:
    SWS_SRC_V_CHR_DROP_SHIFT = 16
except:
    pass

# /usr/include/libswscale/swscale.h: 73
try:
    SWS_PARAM_DEFAULT = 123456
except:
    pass

# /usr/include/libswscale/swscale.h: 75
try:
    SWS_PRINT_INFO = 4096
except:
    pass

# /usr/include/libswscale/swscale.h: 79
try:
    SWS_FULL_CHR_H_INT = 8192
except:
    pass

# /usr/include/libswscale/swscale.h: 81
try:
    SWS_FULL_CHR_H_INP = 16384
except:
    pass

# /usr/include/libswscale/swscale.h: 82
try:
    SWS_DIRECT_BGR = 32768
except:
    pass

# /usr/include/libswscale/swscale.h: 83
try:
    SWS_ACCURATE_RND = 262144
except:
    pass

# /usr/include/libswscale/swscale.h: 84
try:
    SWS_BITEXACT = 524288
except:
    pass

# /usr/include/libswscale/swscale.h: 85
try:
    SWS_ERROR_DIFFUSION = 8388608
except:
    pass

# /usr/include/libswscale/swscale.h: 87
try:
    SWS_MAX_REDUCE_CUTOFF = 0.002
except:
    pass

# /usr/include/libswscale/swscale.h: 89
try:
    SWS_CS_ITU709 = 1
except:
    pass

# /usr/include/libswscale/swscale.h: 90
try:
    SWS_CS_FCC = 4
except:
    pass

# /usr/include/libswscale/swscale.h: 91
try:
    SWS_CS_ITU601 = 5
except:
    pass

# /usr/include/libswscale/swscale.h: 92
try:
    SWS_CS_ITU624 = 5
except:
    pass

# /usr/include/libswscale/swscale.h: 93
try:
    SWS_CS_SMPTE170M = 5
except:
    pass

# /usr/include/libswscale/swscale.h: 94
try:
    SWS_CS_SMPTE240M = 7
except:
    pass

# /usr/include/libswscale/swscale.h: 95
try:
    SWS_CS_DEFAULT = 5
except:
    pass

# /usr/include/libswscale/swscale.h: 96
try:
    SWS_CS_BT2020 = 9
except:
    pass

SwsVector = struct_SwsVector# /usr/include/libswscale/swscale.h: 112

SwsFilter = struct_SwsFilter# /usr/include/libswscale/swscale.h: 120

SwsContext = struct_SwsContext# /usr/include/libswscale/swscale.h: 122

# No inserted files

# No prefix-stripping

