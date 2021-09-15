r"""Wrapper for avformat.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lavformat /usr/include/libavformat/avformat.h /usr/include/libavformat/avio.h /usr/include/libavformat/version.h -L/usr/include/libavutil -o avformat.py

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
_libs["avformat"] = load_library("avformat")

# 1 libraries
# End libraries

# No modules

__off_t = c_long# /usr/include/bits/types.h: 152

__off64_t = c_long# /usr/include/bits/types.h: 153

# /usr/include/bits/types/struct_FILE.h: 49
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE# /usr/include/bits/types/FILE.h: 7

# /usr/include/bits/types/struct_FILE.h: 36
class struct__IO_marker(Structure):
    pass

# /usr/include/bits/types/struct_FILE.h: 37
class struct__IO_codecvt(Structure):
    pass

# /usr/include/bits/types/struct_FILE.h: 38
class struct__IO_wide_data(Structure):
    pass

_IO_lock_t = None# /usr/include/bits/types/struct_FILE.h: 43

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '_codecvt',
    '_wide_data',
    '_freeres_list',
    '_freeres_buf',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * int(1)),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('_codecvt', POINTER(struct__IO_codecvt)),
    ('_wide_data', POINTER(struct__IO_wide_data)),
    ('_freeres_list', POINTER(struct__IO_FILE)),
    ('_freeres_buf', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * int((((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t)))),
]

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

# /usr/include/libavutil/channel_layout.h: 173
class struct_AVBPrint(Structure):
    pass

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

enum_AVIODirEntryType = c_int# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_UNKNOWN = 0# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_BLOCK_DEVICE = (AVIO_ENTRY_UNKNOWN + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_CHARACTER_DEVICE = (AVIO_ENTRY_BLOCK_DEVICE + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_DIRECTORY = (AVIO_ENTRY_CHARACTER_DEVICE + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_NAMED_PIPE = (AVIO_ENTRY_DIRECTORY + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_SYMBOLIC_LINK = (AVIO_ENTRY_NAMED_PIPE + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_SOCKET = (AVIO_ENTRY_SYMBOLIC_LINK + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_FILE = (AVIO_ENTRY_SOCKET + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_SERVER = (AVIO_ENTRY_FILE + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_SHARE = (AVIO_ENTRY_SERVER + 1)# /usr/include/libavformat/avio.h: 66

AVIO_ENTRY_WORKGROUP = (AVIO_ENTRY_SHARE + 1)# /usr/include/libavformat/avio.h: 66

# /usr/include/libavformat/avio.h: 101
class struct_AVIODirEntry(Structure):
    pass

struct_AVIODirEntry.__slots__ = [
    'name',
    'type',
    'utf8',
    'size',
    'modification_timestamp',
    'access_timestamp',
    'status_change_timestamp',
    'user_id',
    'group_id',
    'filemode',
]
struct_AVIODirEntry._fields_ = [
    ('name', String),
    ('type', c_int),
    ('utf8', c_int),
    ('size', c_int64),
    ('modification_timestamp', c_int64),
    ('access_timestamp', c_int64),
    ('status_change_timestamp', c_int64),
    ('user_id', c_int64),
    ('group_id', c_int64),
    ('filemode', c_int64),
]

AVIODirEntry = struct_AVIODirEntry# /usr/include/libavformat/avio.h: 101

# /usr/include/libavformat/avio.h: 104
class struct_URLContext(Structure):
    pass

# /usr/include/libavformat/avio.h: 105
class struct_AVIODirContext(Structure):
    pass

struct_AVIODirContext.__slots__ = [
    'url_context',
]
struct_AVIODirContext._fields_ = [
    ('url_context', POINTER(struct_URLContext)),
]

AVIODirContext = struct_AVIODirContext# /usr/include/libavformat/avio.h: 105

enum_AVIODataMarkerType = c_int# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_HEADER = 0# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_SYNC_POINT = (AVIO_DATA_MARKER_HEADER + 1)# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_BOUNDARY_POINT = (AVIO_DATA_MARKER_SYNC_POINT + 1)# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_UNKNOWN = (AVIO_DATA_MARKER_BOUNDARY_POINT + 1)# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_TRAILER = (AVIO_DATA_MARKER_UNKNOWN + 1)# /usr/include/libavformat/avio.h: 111

AVIO_DATA_MARKER_FLUSH_POINT = (AVIO_DATA_MARKER_TRAILER + 1)# /usr/include/libavformat/avio.h: 111

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

# /usr/include/libavformat/avio.h: 361
if _libs["avformat"].has("avio_find_protocol_name", "cdecl"):
    avio_find_protocol_name = _libs["avformat"].get("avio_find_protocol_name", "cdecl")
    avio_find_protocol_name.argtypes = [String]
    avio_find_protocol_name.restype = c_char_p

# /usr/include/libavformat/avio.h: 375
if _libs["avformat"].has("avio_check", "cdecl"):
    avio_check = _libs["avformat"].get("avio_check", "cdecl")
    avio_check.argtypes = [String, c_int]
    avio_check.restype = c_int

# /usr/include/libavformat/avio.h: 386
if _libs["avformat"].has("avpriv_io_move", "cdecl"):
    avpriv_io_move = _libs["avformat"].get("avpriv_io_move", "cdecl")
    avpriv_io_move.argtypes = [String, String]
    avpriv_io_move.restype = c_int

# /usr/include/libavformat/avio.h: 394
if _libs["avformat"].has("avpriv_io_delete", "cdecl"):
    avpriv_io_delete = _libs["avformat"].get("avpriv_io_delete", "cdecl")
    avpriv_io_delete.argtypes = [String]
    avpriv_io_delete.restype = c_int

# /usr/include/libavformat/avio.h: 406
if _libs["avformat"].has("avio_open_dir", "cdecl"):
    avio_open_dir = _libs["avformat"].get("avio_open_dir", "cdecl")
    avio_open_dir.argtypes = [POINTER(POINTER(AVIODirContext)), String, POINTER(POINTER(AVDictionary))]
    avio_open_dir.restype = c_int

# /usr/include/libavformat/avio.h: 419
if _libs["avformat"].has("avio_read_dir", "cdecl"):
    avio_read_dir = _libs["avformat"].get("avio_read_dir", "cdecl")
    avio_read_dir.argtypes = [POINTER(AVIODirContext), POINTER(POINTER(AVIODirEntry))]
    avio_read_dir.restype = c_int

# /usr/include/libavformat/avio.h: 430
if _libs["avformat"].has("avio_close_dir", "cdecl"):
    avio_close_dir = _libs["avformat"].get("avio_close_dir", "cdecl")
    avio_close_dir.argtypes = [POINTER(POINTER(AVIODirContext))]
    avio_close_dir.restype = c_int

# /usr/include/libavformat/avio.h: 437
if _libs["avformat"].has("avio_free_directory_entry", "cdecl"):
    avio_free_directory_entry = _libs["avformat"].get("avio_free_directory_entry", "cdecl")
    avio_free_directory_entry.argtypes = [POINTER(POINTER(AVIODirEntry))]
    avio_free_directory_entry.restype = None

# /usr/include/libavformat/avio.h: 462
if _libs["avformat"].has("avio_alloc_context", "cdecl"):
    avio_alloc_context = _libs["avformat"].get("avio_alloc_context", "cdecl")
    avio_alloc_context.argtypes = [POINTER(c_ubyte), c_int, c_int, POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_uint8), c_int), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_uint8), c_int), CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int64, c_int)]
    avio_alloc_context.restype = POINTER(AVIOContext)

# /usr/include/libavformat/avio.h: 477
if _libs["avformat"].has("avio_context_free", "cdecl"):
    avio_context_free = _libs["avformat"].get("avio_context_free", "cdecl")
    avio_context_free.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_context_free.restype = None

# /usr/include/libavformat/avio.h: 479
if _libs["avformat"].has("avio_w8", "cdecl"):
    avio_w8 = _libs["avformat"].get("avio_w8", "cdecl")
    avio_w8.argtypes = [POINTER(AVIOContext), c_int]
    avio_w8.restype = None

# /usr/include/libavformat/avio.h: 480
if _libs["avformat"].has("avio_write", "cdecl"):
    avio_write = _libs["avformat"].get("avio_write", "cdecl")
    avio_write.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_write.restype = None

# /usr/include/libavformat/avio.h: 481
if _libs["avformat"].has("avio_wl64", "cdecl"):
    avio_wl64 = _libs["avformat"].get("avio_wl64", "cdecl")
    avio_wl64.argtypes = [POINTER(AVIOContext), c_uint64]
    avio_wl64.restype = None

# /usr/include/libavformat/avio.h: 482
if _libs["avformat"].has("avio_wb64", "cdecl"):
    avio_wb64 = _libs["avformat"].get("avio_wb64", "cdecl")
    avio_wb64.argtypes = [POINTER(AVIOContext), c_uint64]
    avio_wb64.restype = None

# /usr/include/libavformat/avio.h: 483
if _libs["avformat"].has("avio_wl32", "cdecl"):
    avio_wl32 = _libs["avformat"].get("avio_wl32", "cdecl")
    avio_wl32.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl32.restype = None

# /usr/include/libavformat/avio.h: 484
if _libs["avformat"].has("avio_wb32", "cdecl"):
    avio_wb32 = _libs["avformat"].get("avio_wb32", "cdecl")
    avio_wb32.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb32.restype = None

# /usr/include/libavformat/avio.h: 485
if _libs["avformat"].has("avio_wl24", "cdecl"):
    avio_wl24 = _libs["avformat"].get("avio_wl24", "cdecl")
    avio_wl24.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl24.restype = None

# /usr/include/libavformat/avio.h: 486
if _libs["avformat"].has("avio_wb24", "cdecl"):
    avio_wb24 = _libs["avformat"].get("avio_wb24", "cdecl")
    avio_wb24.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb24.restype = None

# /usr/include/libavformat/avio.h: 487
if _libs["avformat"].has("avio_wl16", "cdecl"):
    avio_wl16 = _libs["avformat"].get("avio_wl16", "cdecl")
    avio_wl16.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl16.restype = None

# /usr/include/libavformat/avio.h: 488
if _libs["avformat"].has("avio_wb16", "cdecl"):
    avio_wb16 = _libs["avformat"].get("avio_wb16", "cdecl")
    avio_wb16.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb16.restype = None

# /usr/include/libavformat/avio.h: 494
if _libs["avformat"].has("avio_put_str", "cdecl"):
    avio_put_str = _libs["avformat"].get("avio_put_str", "cdecl")
    avio_put_str.argtypes = [POINTER(AVIOContext), String]
    avio_put_str.restype = c_int

# /usr/include/libavformat/avio.h: 503
if _libs["avformat"].has("avio_put_str16le", "cdecl"):
    avio_put_str16le = _libs["avformat"].get("avio_put_str16le", "cdecl")
    avio_put_str16le.argtypes = [POINTER(AVIOContext), String]
    avio_put_str16le.restype = c_int

# /usr/include/libavformat/avio.h: 512
if _libs["avformat"].has("avio_put_str16be", "cdecl"):
    avio_put_str16be = _libs["avformat"].get("avio_put_str16be", "cdecl")
    avio_put_str16be.argtypes = [POINTER(AVIOContext), String]
    avio_put_str16be.restype = c_int

# /usr/include/libavformat/avio.h: 524
if _libs["avformat"].has("avio_write_marker", "cdecl"):
    avio_write_marker = _libs["avformat"].get("avio_write_marker", "cdecl")
    avio_write_marker.argtypes = [POINTER(AVIOContext), c_int64, enum_AVIODataMarkerType]
    avio_write_marker.restype = None

# /usr/include/libavformat/avio.h: 545
if _libs["avformat"].has("avio_seek", "cdecl"):
    avio_seek = _libs["avformat"].get("avio_seek", "cdecl")
    avio_seek.argtypes = [POINTER(AVIOContext), c_int64, c_int]
    avio_seek.restype = c_int64

# /usr/include/libavformat/avio.h: 551
if _libs["avformat"].has("avio_skip", "cdecl"):
    avio_skip = _libs["avformat"].get("avio_skip", "cdecl")
    avio_skip.argtypes = [POINTER(AVIOContext), c_int64]
    avio_skip.restype = c_int64

# /usr/include/libavformat/avio.h: 566
if _libs["avformat"].has("avio_size", "cdecl"):
    avio_size = _libs["avformat"].get("avio_size", "cdecl")
    avio_size.argtypes = [POINTER(AVIOContext)]
    avio_size.restype = c_int64

# /usr/include/libavformat/avio.h: 572
if _libs["avformat"].has("avio_feof", "cdecl"):
    avio_feof = _libs["avformat"].get("avio_feof", "cdecl")
    avio_feof.argtypes = [POINTER(AVIOContext)]
    avio_feof.restype = c_int

# /usr/include/libavformat/avio.h: 578
if _libs["avformat"].has("avio_printf", "cdecl"):
    _func = _libs["avformat"].get("avio_printf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(AVIOContext), String]
    avio_printf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavformat/avio.h: 585
if _libs["avformat"].has("avio_print_string_array", "cdecl"):
    avio_print_string_array = _libs["avformat"].get("avio_print_string_array", "cdecl")
    avio_print_string_array.argtypes = [POINTER(AVIOContext), POINTER(POINTER(c_char))]
    avio_print_string_array.restype = None

# /usr/include/libavformat/avio.h: 607
if _libs["avformat"].has("avio_flush", "cdecl"):
    avio_flush = _libs["avformat"].get("avio_flush", "cdecl")
    avio_flush.argtypes = [POINTER(AVIOContext)]
    avio_flush.restype = None

# /usr/include/libavformat/avio.h: 613
if _libs["avformat"].has("avio_read", "cdecl"):
    avio_read = _libs["avformat"].get("avio_read", "cdecl")
    avio_read.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_read.restype = c_int

# /usr/include/libavformat/avio.h: 622
if _libs["avformat"].has("avio_read_partial", "cdecl"):
    avio_read_partial = _libs["avformat"].get("avio_read_partial", "cdecl")
    avio_read_partial.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_read_partial.restype = c_int

# /usr/include/libavformat/avio.h: 631
if _libs["avformat"].has("avio_r8", "cdecl"):
    avio_r8 = _libs["avformat"].get("avio_r8", "cdecl")
    avio_r8.argtypes = [POINTER(AVIOContext)]
    avio_r8.restype = c_int

# /usr/include/libavformat/avio.h: 632
if _libs["avformat"].has("avio_rl16", "cdecl"):
    avio_rl16 = _libs["avformat"].get("avio_rl16", "cdecl")
    avio_rl16.argtypes = [POINTER(AVIOContext)]
    avio_rl16.restype = c_uint

# /usr/include/libavformat/avio.h: 633
if _libs["avformat"].has("avio_rl24", "cdecl"):
    avio_rl24 = _libs["avformat"].get("avio_rl24", "cdecl")
    avio_rl24.argtypes = [POINTER(AVIOContext)]
    avio_rl24.restype = c_uint

# /usr/include/libavformat/avio.h: 634
if _libs["avformat"].has("avio_rl32", "cdecl"):
    avio_rl32 = _libs["avformat"].get("avio_rl32", "cdecl")
    avio_rl32.argtypes = [POINTER(AVIOContext)]
    avio_rl32.restype = c_uint

# /usr/include/libavformat/avio.h: 635
if _libs["avformat"].has("avio_rl64", "cdecl"):
    avio_rl64 = _libs["avformat"].get("avio_rl64", "cdecl")
    avio_rl64.argtypes = [POINTER(AVIOContext)]
    avio_rl64.restype = c_uint64

# /usr/include/libavformat/avio.h: 636
if _libs["avformat"].has("avio_rb16", "cdecl"):
    avio_rb16 = _libs["avformat"].get("avio_rb16", "cdecl")
    avio_rb16.argtypes = [POINTER(AVIOContext)]
    avio_rb16.restype = c_uint

# /usr/include/libavformat/avio.h: 637
if _libs["avformat"].has("avio_rb24", "cdecl"):
    avio_rb24 = _libs["avformat"].get("avio_rb24", "cdecl")
    avio_rb24.argtypes = [POINTER(AVIOContext)]
    avio_rb24.restype = c_uint

# /usr/include/libavformat/avio.h: 638
if _libs["avformat"].has("avio_rb32", "cdecl"):
    avio_rb32 = _libs["avformat"].get("avio_rb32", "cdecl")
    avio_rb32.argtypes = [POINTER(AVIOContext)]
    avio_rb32.restype = c_uint

# /usr/include/libavformat/avio.h: 639
if _libs["avformat"].has("avio_rb64", "cdecl"):
    avio_rb64 = _libs["avformat"].get("avio_rb64", "cdecl")
    avio_rb64.argtypes = [POINTER(AVIOContext)]
    avio_rb64.restype = c_uint64

# /usr/include/libavformat/avio.h: 656
if _libs["avformat"].has("avio_get_str", "cdecl"):
    avio_get_str = _libs["avformat"].get("avio_get_str", "cdecl")
    avio_get_str.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str.restype = c_int

# /usr/include/libavformat/avio.h: 664
if _libs["avformat"].has("avio_get_str16le", "cdecl"):
    avio_get_str16le = _libs["avformat"].get("avio_get_str16le", "cdecl")
    avio_get_str16le.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str16le.restype = c_int

# /usr/include/libavformat/avio.h: 665
if _libs["avformat"].has("avio_get_str16be", "cdecl"):
    avio_get_str16be = _libs["avformat"].get("avio_get_str16be", "cdecl")
    avio_get_str16be.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str16be.restype = c_int

# /usr/include/libavformat/avio.h: 717
if _libs["avformat"].has("avio_open", "cdecl"):
    avio_open = _libs["avformat"].get("avio_open", "cdecl")
    avio_open.argtypes = [POINTER(POINTER(AVIOContext)), String, c_int]
    avio_open.restype = c_int

# /usr/include/libavformat/avio.h: 737
if _libs["avformat"].has("avio_open2", "cdecl"):
    avio_open2 = _libs["avformat"].get("avio_open2", "cdecl")
    avio_open2.argtypes = [POINTER(POINTER(AVIOContext)), String, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary))]
    avio_open2.restype = c_int

# /usr/include/libavformat/avio.h: 750
if _libs["avformat"].has("avio_close", "cdecl"):
    avio_close = _libs["avformat"].get("avio_close", "cdecl")
    avio_close.argtypes = [POINTER(AVIOContext)]
    avio_close.restype = c_int

# /usr/include/libavformat/avio.h: 763
if _libs["avformat"].has("avio_closep", "cdecl"):
    avio_closep = _libs["avformat"].get("avio_closep", "cdecl")
    avio_closep.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_closep.restype = c_int

# /usr/include/libavformat/avio.h: 772
if _libs["avformat"].has("avio_open_dyn_buf", "cdecl"):
    avio_open_dyn_buf = _libs["avformat"].get("avio_open_dyn_buf", "cdecl")
    avio_open_dyn_buf.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_open_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 784
if _libs["avformat"].has("avio_get_dyn_buf", "cdecl"):
    avio_get_dyn_buf = _libs["avformat"].get("avio_get_dyn_buf", "cdecl")
    avio_get_dyn_buf.argtypes = [POINTER(AVIOContext), POINTER(POINTER(c_uint8))]
    avio_get_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 795
if _libs["avformat"].has("avio_close_dyn_buf", "cdecl"):
    avio_close_dyn_buf = _libs["avformat"].get("avio_close_dyn_buf", "cdecl")
    avio_close_dyn_buf.argtypes = [POINTER(AVIOContext), POINTER(POINTER(c_uint8))]
    avio_close_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 808
if _libs["avformat"].has("avio_enum_protocols", "cdecl"):
    avio_enum_protocols = _libs["avformat"].get("avio_enum_protocols", "cdecl")
    avio_enum_protocols.argtypes = [POINTER(POINTER(None)), c_int]
    avio_enum_protocols.restype = c_char_p

# /usr/include/libavformat/avio.h: 815
if _libs["avformat"].has("avio_protocol_get_class", "cdecl"):
    avio_protocol_get_class = _libs["avformat"].get("avio_protocol_get_class", "cdecl")
    avio_protocol_get_class.argtypes = [String]
    avio_protocol_get_class.restype = POINTER(AVClass)

# /usr/include/libavformat/avio.h: 824
if _libs["avformat"].has("avio_pause", "cdecl"):
    avio_pause = _libs["avformat"].get("avio_pause", "cdecl")
    avio_pause.argtypes = [POINTER(AVIOContext), c_int]
    avio_pause.restype = c_int

# /usr/include/libavformat/avio.h: 845
if _libs["avformat"].has("avio_seek_time", "cdecl"):
    avio_seek_time = _libs["avformat"].get("avio_seek_time", "cdecl")
    avio_seek_time.argtypes = [POINTER(AVIOContext), c_int, c_int64, c_int]
    avio_seek_time.restype = c_int64

# /usr/include/libavformat/avio.h: 857
if _libs["avformat"].has("avio_read_to_bprint", "cdecl"):
    avio_read_to_bprint = _libs["avformat"].get("avio_read_to_bprint", "cdecl")
    avio_read_to_bprint.argtypes = [POINTER(AVIOContext), POINTER(struct_AVBPrint), c_size_t]
    avio_read_to_bprint.restype = c_int

# /usr/include/libavformat/avio.h: 866
if _libs["avformat"].has("avio_accept", "cdecl"):
    avio_accept = _libs["avformat"].get("avio_accept", "cdecl")
    avio_accept.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVIOContext))]
    avio_accept.restype = c_int

# /usr/include/libavformat/avio.h: 887
if _libs["avformat"].has("avio_handshake", "cdecl"):
    avio_handshake = _libs["avformat"].get("avio_handshake", "cdecl")
    avio_handshake.argtypes = [POINTER(AVIOContext)]
    avio_handshake.restype = c_int

# /usr/include/libavformat/avformat.h: 1234
class struct_AVFormatContext(Structure):
    pass

# /usr/include/libavformat/avformat.h: 321
class struct_AVDeviceInfoList(Structure):
    pass

# /usr/include/libavformat/avformat.h: 322
class struct_AVDeviceCapabilitiesQuery(Structure):
    pass

# /usr/include/libavformat/avformat.h: 414
if _libs["avformat"].has("av_get_packet", "cdecl"):
    av_get_packet = _libs["avformat"].get("av_get_packet", "cdecl")
    av_get_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
    av_get_packet.restype = c_int

# /usr/include/libavformat/avformat.h: 431
if _libs["avformat"].has("av_append_packet", "cdecl"):
    av_append_packet = _libs["avformat"].get("av_append_packet", "cdecl")
    av_append_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
    av_append_packet.restype = c_int

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

AVSTREAM_PARSE_NONE = 0# /usr/include/libavformat/avformat.h: 792

AVSTREAM_PARSE_FULL = (AVSTREAM_PARSE_NONE + 1)# /usr/include/libavformat/avformat.h: 792

AVSTREAM_PARSE_HEADERS = (AVSTREAM_PARSE_FULL + 1)# /usr/include/libavformat/avformat.h: 792

AVSTREAM_PARSE_TIMESTAMPS = (AVSTREAM_PARSE_HEADERS + 1)# /usr/include/libavformat/avformat.h: 792

AVSTREAM_PARSE_FULL_ONCE = (AVSTREAM_PARSE_TIMESTAMPS + 1)# /usr/include/libavformat/avformat.h: 792

AVSTREAM_PARSE_FULL_RAW = (AVSTREAM_PARSE_FULL_ONCE + 1)# /usr/include/libavformat/avformat.h: 792

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

# /usr/include/libavformat/avformat.h: 1124
if _libs["avformat"].has("av_stream_get_r_frame_rate", "cdecl"):
    av_stream_get_r_frame_rate = _libs["avformat"].get("av_stream_get_r_frame_rate", "cdecl")
    av_stream_get_r_frame_rate.argtypes = [POINTER(AVStream)]
    av_stream_get_r_frame_rate.restype = AVRational

# /usr/include/libavformat/avformat.h: 1126
if _libs["avformat"].has("av_stream_set_r_frame_rate", "cdecl"):
    av_stream_set_r_frame_rate = _libs["avformat"].get("av_stream_set_r_frame_rate", "cdecl")
    av_stream_set_r_frame_rate.argtypes = [POINTER(AVStream), AVRational]
    av_stream_set_r_frame_rate.restype = None

# /usr/include/libavformat/avformat.h: 1129
if _libs["avformat"].has("av_stream_get_recommended_encoder_configuration", "cdecl"):
    av_stream_get_recommended_encoder_configuration = _libs["avformat"].get("av_stream_get_recommended_encoder_configuration", "cdecl")
    av_stream_get_recommended_encoder_configuration.argtypes = [POINTER(AVStream)]
    if sizeof(c_int) == sizeof(c_void_p):
        av_stream_get_recommended_encoder_configuration.restype = ReturnString
    else:
        av_stream_get_recommended_encoder_configuration.restype = String
        av_stream_get_recommended_encoder_configuration.errcheck = ReturnString

# /usr/include/libavformat/avformat.h: 1131
if _libs["avformat"].has("av_stream_set_recommended_encoder_configuration", "cdecl"):
    av_stream_set_recommended_encoder_configuration = _libs["avformat"].get("av_stream_set_recommended_encoder_configuration", "cdecl")
    av_stream_set_recommended_encoder_configuration.argtypes = [POINTER(AVStream), String]
    av_stream_set_recommended_encoder_configuration.restype = None

# /usr/include/libavformat/avformat.h: 1135
if _libs["avformat"].has("av_stream_get_parser", "cdecl"):
    av_stream_get_parser = _libs["avformat"].get("av_stream_get_parser", "cdecl")
    av_stream_get_parser.argtypes = [POINTER(AVStream)]
    av_stream_get_parser.restype = POINTER(struct_AVCodecParserContext)

# /usr/include/libavformat/avformat.h: 1142
if _libs["avformat"].has("av_stream_get_end_pts", "cdecl"):
    av_stream_get_end_pts = _libs["avformat"].get("av_stream_get_end_pts", "cdecl")
    av_stream_get_end_pts.argtypes = [POINTER(AVStream)]
    av_stream_get_end_pts.restype = c_int64

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

AVOpenCallback = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(POINTER(AVIOContext)), String, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary)))# /usr/include/libavformat/avformat.h: 1205

enum_AVDurationEstimationMethod = c_int# /usr/include/libavformat/avformat.h: 1212

AVFMT_DURATION_FROM_PTS = 0# /usr/include/libavformat/avformat.h: 1212

AVFMT_DURATION_FROM_STREAM = (AVFMT_DURATION_FROM_PTS + 1)# /usr/include/libavformat/avformat.h: 1212

AVFMT_DURATION_FROM_BITRATE = (AVFMT_DURATION_FROM_STREAM + 1)# /usr/include/libavformat/avformat.h: 1212

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

# /usr/include/libavformat/avformat.h: 1873
if _libs["avformat"].has("av_format_get_probe_score", "cdecl"):
    av_format_get_probe_score = _libs["avformat"].get("av_format_get_probe_score", "cdecl")
    av_format_get_probe_score.argtypes = [POINTER(AVFormatContext)]
    av_format_get_probe_score.restype = c_int

# /usr/include/libavformat/avformat.h: 1875
if _libs["avformat"].has("av_format_get_video_codec", "cdecl"):
    av_format_get_video_codec = _libs["avformat"].get("av_format_get_video_codec", "cdecl")
    av_format_get_video_codec.argtypes = [POINTER(AVFormatContext)]
    av_format_get_video_codec.restype = POINTER(AVCodec)

# /usr/include/libavformat/avformat.h: 1877
if _libs["avformat"].has("av_format_set_video_codec", "cdecl"):
    av_format_set_video_codec = _libs["avformat"].get("av_format_set_video_codec", "cdecl")
    av_format_set_video_codec.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    av_format_set_video_codec.restype = None

# /usr/include/libavformat/avformat.h: 1879
if _libs["avformat"].has("av_format_get_audio_codec", "cdecl"):
    av_format_get_audio_codec = _libs["avformat"].get("av_format_get_audio_codec", "cdecl")
    av_format_get_audio_codec.argtypes = [POINTER(AVFormatContext)]
    av_format_get_audio_codec.restype = POINTER(AVCodec)

# /usr/include/libavformat/avformat.h: 1881
if _libs["avformat"].has("av_format_set_audio_codec", "cdecl"):
    av_format_set_audio_codec = _libs["avformat"].get("av_format_set_audio_codec", "cdecl")
    av_format_set_audio_codec.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    av_format_set_audio_codec.restype = None

# /usr/include/libavformat/avformat.h: 1883
if _libs["avformat"].has("av_format_get_subtitle_codec", "cdecl"):
    av_format_get_subtitle_codec = _libs["avformat"].get("av_format_get_subtitle_codec", "cdecl")
    av_format_get_subtitle_codec.argtypes = [POINTER(AVFormatContext)]
    av_format_get_subtitle_codec.restype = POINTER(AVCodec)

# /usr/include/libavformat/avformat.h: 1885
if _libs["avformat"].has("av_format_set_subtitle_codec", "cdecl"):
    av_format_set_subtitle_codec = _libs["avformat"].get("av_format_set_subtitle_codec", "cdecl")
    av_format_set_subtitle_codec.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    av_format_set_subtitle_codec.restype = None

# /usr/include/libavformat/avformat.h: 1887
if _libs["avformat"].has("av_format_get_data_codec", "cdecl"):
    av_format_get_data_codec = _libs["avformat"].get("av_format_get_data_codec", "cdecl")
    av_format_get_data_codec.argtypes = [POINTER(AVFormatContext)]
    av_format_get_data_codec.restype = POINTER(AVCodec)

# /usr/include/libavformat/avformat.h: 1889
if _libs["avformat"].has("av_format_set_data_codec", "cdecl"):
    av_format_set_data_codec = _libs["avformat"].get("av_format_set_data_codec", "cdecl")
    av_format_set_data_codec.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    av_format_set_data_codec.restype = None

# /usr/include/libavformat/avformat.h: 1891
if _libs["avformat"].has("av_format_get_metadata_header_padding", "cdecl"):
    av_format_get_metadata_header_padding = _libs["avformat"].get("av_format_get_metadata_header_padding", "cdecl")
    av_format_get_metadata_header_padding.argtypes = [POINTER(AVFormatContext)]
    av_format_get_metadata_header_padding.restype = c_int

# /usr/include/libavformat/avformat.h: 1893
if _libs["avformat"].has("av_format_set_metadata_header_padding", "cdecl"):
    av_format_set_metadata_header_padding = _libs["avformat"].get("av_format_set_metadata_header_padding", "cdecl")
    av_format_set_metadata_header_padding.argtypes = [POINTER(AVFormatContext), c_int]
    av_format_set_metadata_header_padding.restype = None

# /usr/include/libavformat/avformat.h: 1895
if _libs["avformat"].has("av_format_get_opaque", "cdecl"):
    av_format_get_opaque = _libs["avformat"].get("av_format_get_opaque", "cdecl")
    av_format_get_opaque.argtypes = [POINTER(AVFormatContext)]
    av_format_get_opaque.restype = POINTER(c_ubyte)
    av_format_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavformat/avformat.h: 1897
if _libs["avformat"].has("av_format_set_opaque", "cdecl"):
    av_format_set_opaque = _libs["avformat"].get("av_format_set_opaque", "cdecl")
    av_format_set_opaque.argtypes = [POINTER(AVFormatContext), POINTER(None)]
    av_format_set_opaque.restype = None

# /usr/include/libavformat/avformat.h: 1899
if _libs["avformat"].has("av_format_get_control_message_cb", "cdecl"):
    av_format_get_control_message_cb = _libs["avformat"].get("av_format_get_control_message_cb", "cdecl")
    av_format_get_control_message_cb.argtypes = [POINTER(AVFormatContext)]
    av_format_get_control_message_cb.restype = av_format_control_message

# /usr/include/libavformat/avformat.h: 1901
if _libs["avformat"].has("av_format_set_control_message_cb", "cdecl"):
    av_format_set_control_message_cb = _libs["avformat"].get("av_format_set_control_message_cb", "cdecl")
    av_format_set_control_message_cb.argtypes = [POINTER(AVFormatContext), av_format_control_message]
    av_format_set_control_message_cb.restype = None

# /usr/include/libavformat/avformat.h: 1903
if _libs["avformat"].has("av_format_get_open_cb", "cdecl"):
    av_format_get_open_cb = _libs["avformat"].get("av_format_get_open_cb", "cdecl")
    av_format_get_open_cb.argtypes = [POINTER(AVFormatContext)]
    av_format_get_open_cb.restype = AVOpenCallback

# /usr/include/libavformat/avformat.h: 1904
if _libs["avformat"].has("av_format_set_open_cb", "cdecl"):
    av_format_set_open_cb = _libs["avformat"].get("av_format_set_open_cb", "cdecl")
    av_format_set_open_cb.argtypes = [POINTER(AVFormatContext), AVOpenCallback]
    av_format_set_open_cb.restype = None

# /usr/include/libavformat/avformat.h: 1912
if _libs["avformat"].has("av_format_inject_global_side_data", "cdecl"):
    av_format_inject_global_side_data = _libs["avformat"].get("av_format_inject_global_side_data", "cdecl")
    av_format_inject_global_side_data.argtypes = [POINTER(AVFormatContext)]
    av_format_inject_global_side_data.restype = None

# /usr/include/libavformat/avformat.h: 1919
if _libs["avformat"].has("av_fmt_ctx_get_duration_estimation_method", "cdecl"):
    av_fmt_ctx_get_duration_estimation_method = _libs["avformat"].get("av_fmt_ctx_get_duration_estimation_method", "cdecl")
    av_fmt_ctx_get_duration_estimation_method.argtypes = [POINTER(AVFormatContext)]
    av_fmt_ctx_get_duration_estimation_method.restype = enum_AVDurationEstimationMethod

# /usr/include/libavformat/avformat.h: 1933
if _libs["avformat"].has("avformat_version", "cdecl"):
    avformat_version = _libs["avformat"].get("avformat_version", "cdecl")
    avformat_version.argtypes = []
    avformat_version.restype = c_uint

# /usr/include/libavformat/avformat.h: 1938
if _libs["avformat"].has("avformat_configuration", "cdecl"):
    avformat_configuration = _libs["avformat"].get("avformat_configuration", "cdecl")
    avformat_configuration.argtypes = []
    avformat_configuration.restype = c_char_p

# /usr/include/libavformat/avformat.h: 1943
if _libs["avformat"].has("avformat_license", "cdecl"):
    avformat_license = _libs["avformat"].get("avformat_license", "cdecl")
    avformat_license.argtypes = []
    avformat_license.restype = c_char_p

# /usr/include/libavformat/avformat.h: 1955
if _libs["avformat"].has("av_register_all", "cdecl"):
    av_register_all = _libs["avformat"].get("av_register_all", "cdecl")
    av_register_all.argtypes = []
    av_register_all.restype = None

# /usr/include/libavformat/avformat.h: 1958
if _libs["avformat"].has("av_register_input_format", "cdecl"):
    av_register_input_format = _libs["avformat"].get("av_register_input_format", "cdecl")
    av_register_input_format.argtypes = [POINTER(AVInputFormat)]
    av_register_input_format.restype = None

# /usr/include/libavformat/avformat.h: 1960
if _libs["avformat"].has("av_register_output_format", "cdecl"):
    av_register_output_format = _libs["avformat"].get("av_register_output_format", "cdecl")
    av_register_output_format.argtypes = [POINTER(AVOutputFormat)]
    av_register_output_format.restype = None

# /usr/include/libavformat/avformat.h: 1977
if _libs["avformat"].has("avformat_network_init", "cdecl"):
    avformat_network_init = _libs["avformat"].get("avformat_network_init", "cdecl")
    avformat_network_init.argtypes = []
    avformat_network_init.restype = c_int

# /usr/include/libavformat/avformat.h: 1983
if _libs["avformat"].has("avformat_network_deinit", "cdecl"):
    avformat_network_deinit = _libs["avformat"].get("avformat_network_deinit", "cdecl")
    avformat_network_deinit.argtypes = []
    avformat_network_deinit.restype = c_int

# /usr/include/libavformat/avformat.h: 1992
if _libs["avformat"].has("av_iformat_next", "cdecl"):
    av_iformat_next = _libs["avformat"].get("av_iformat_next", "cdecl")
    av_iformat_next.argtypes = [POINTER(AVInputFormat)]
    av_iformat_next.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2000
if _libs["avformat"].has("av_oformat_next", "cdecl"):
    av_oformat_next = _libs["avformat"].get("av_oformat_next", "cdecl")
    av_oformat_next.argtypes = [POINTER(AVOutputFormat)]
    av_oformat_next.restype = POINTER(AVOutputFormat)

# /usr/include/libavformat/avformat.h: 2012
if _libs["avformat"].has("av_muxer_iterate", "cdecl"):
    av_muxer_iterate = _libs["avformat"].get("av_muxer_iterate", "cdecl")
    av_muxer_iterate.argtypes = [POINTER(POINTER(None))]
    av_muxer_iterate.restype = POINTER(AVOutputFormat)

# /usr/include/libavformat/avformat.h: 2023
if _libs["avformat"].has("av_demuxer_iterate", "cdecl"):
    av_demuxer_iterate = _libs["avformat"].get("av_demuxer_iterate", "cdecl")
    av_demuxer_iterate.argtypes = [POINTER(POINTER(None))]
    av_demuxer_iterate.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2030
if _libs["avformat"].has("avformat_alloc_context", "cdecl"):
    avformat_alloc_context = _libs["avformat"].get("avformat_alloc_context", "cdecl")
    avformat_alloc_context.argtypes = []
    avformat_alloc_context.restype = POINTER(AVFormatContext)

# /usr/include/libavformat/avformat.h: 2036
if _libs["avformat"].has("avformat_free_context", "cdecl"):
    avformat_free_context = _libs["avformat"].get("avformat_free_context", "cdecl")
    avformat_free_context.argtypes = [POINTER(AVFormatContext)]
    avformat_free_context.restype = None

# /usr/include/libavformat/avformat.h: 2044
if _libs["avformat"].has("avformat_get_class", "cdecl"):
    avformat_get_class = _libs["avformat"].get("avformat_get_class", "cdecl")
    avformat_get_class.argtypes = []
    avformat_get_class.restype = POINTER(AVClass)

# /usr/include/libavformat/avformat.h: 2065
if _libs["avformat"].has("avformat_new_stream", "cdecl"):
    avformat_new_stream = _libs["avformat"].get("avformat_new_stream", "cdecl")
    avformat_new_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    avformat_new_stream.restype = POINTER(AVStream)

# /usr/include/libavformat/avformat.h: 2079
if _libs["avformat"].has("av_stream_add_side_data", "cdecl"):
    av_stream_add_side_data = _libs["avformat"].get("av_stream_add_side_data", "cdecl")
    av_stream_add_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, POINTER(c_uint8), c_size_t]
    av_stream_add_side_data.restype = c_int

# /usr/include/libavformat/avformat.h: 2090
if _libs["avformat"].has("av_stream_new_side_data", "cdecl"):
    av_stream_new_side_data = _libs["avformat"].get("av_stream_new_side_data", "cdecl")
    av_stream_new_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, c_int]
    av_stream_new_side_data.restype = POINTER(c_uint8)

# /usr/include/libavformat/avformat.h: 2105
if _libs["avformat"].has("av_stream_get_side_data", "cdecl"):
    av_stream_get_side_data = _libs["avformat"].get("av_stream_get_side_data", "cdecl")
    av_stream_get_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, POINTER(c_int)]
    av_stream_get_side_data.restype = POINTER(c_uint8)

# /usr/include/libavformat/avformat.h: 2112
if _libs["avformat"].has("av_new_program", "cdecl"):
    av_new_program = _libs["avformat"].get("av_new_program", "cdecl")
    av_new_program.argtypes = [POINTER(AVFormatContext), c_int]
    av_new_program.restype = POINTER(AVProgram)

# /usr/include/libavformat/avformat.h: 2135
if _libs["avformat"].has("avformat_alloc_output_context2", "cdecl"):
    avformat_alloc_output_context2 = _libs["avformat"].get("avformat_alloc_output_context2", "cdecl")
    avformat_alloc_output_context2.argtypes = [POINTER(POINTER(AVFormatContext)), POINTER(AVOutputFormat), String, String]
    avformat_alloc_output_context2.restype = c_int

# /usr/include/libavformat/avformat.h: 2146
if _libs["avformat"].has("av_find_input_format", "cdecl"):
    av_find_input_format = _libs["avformat"].get("av_find_input_format", "cdecl")
    av_find_input_format.argtypes = [String]
    av_find_input_format.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2155
if _libs["avformat"].has("av_probe_input_format", "cdecl"):
    av_probe_input_format = _libs["avformat"].get("av_probe_input_format", "cdecl")
    av_probe_input_format.argtypes = [POINTER(AVProbeData), c_int]
    av_probe_input_format.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2169
if _libs["avformat"].has("av_probe_input_format2", "cdecl"):
    av_probe_input_format2 = _libs["avformat"].get("av_probe_input_format2", "cdecl")
    av_probe_input_format2.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
    av_probe_input_format2.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2178
if _libs["avformat"].has("av_probe_input_format3", "cdecl"):
    av_probe_input_format3 = _libs["avformat"].get("av_probe_input_format3", "cdecl")
    av_probe_input_format3.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
    av_probe_input_format3.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 2196
if _libs["avformat"].has("av_probe_input_buffer2", "cdecl"):
    av_probe_input_buffer2 = _libs["avformat"].get("av_probe_input_buffer2", "cdecl")
    av_probe_input_buffer2.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVInputFormat)), String, POINTER(None), c_uint, c_uint]
    av_probe_input_buffer2.restype = c_int

# /usr/include/libavformat/avformat.h: 2203
if _libs["avformat"].has("av_probe_input_buffer", "cdecl"):
    av_probe_input_buffer = _libs["avformat"].get("av_probe_input_buffer", "cdecl")
    av_probe_input_buffer.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVInputFormat)), String, POINTER(None), c_uint, c_uint]
    av_probe_input_buffer.restype = c_int

# /usr/include/libavformat/avformat.h: 2226
if _libs["avformat"].has("avformat_open_input", "cdecl"):
    avformat_open_input = _libs["avformat"].get("avformat_open_input", "cdecl")
    avformat_open_input.argtypes = [POINTER(POINTER(AVFormatContext)), String, POINTER(AVInputFormat), POINTER(POINTER(AVDictionary))]
    avformat_open_input.restype = c_int

# /usr/include/libavformat/avformat.h: 2233
if _libs["avformat"].has("av_demuxer_open", "cdecl"):
    av_demuxer_open = _libs["avformat"].get("av_demuxer_open", "cdecl")
    av_demuxer_open.argtypes = [POINTER(AVFormatContext)]
    av_demuxer_open.restype = c_int

# /usr/include/libavformat/avformat.h: 2257
if _libs["avformat"].has("avformat_find_stream_info", "cdecl"):
    avformat_find_stream_info = _libs["avformat"].get("avformat_find_stream_info", "cdecl")
    avformat_find_stream_info.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_find_stream_info.restype = c_int

# /usr/include/libavformat/avformat.h: 2269
if _libs["avformat"].has("av_find_program_from_stream", "cdecl"):
    av_find_program_from_stream = _libs["avformat"].get("av_find_program_from_stream", "cdecl")
    av_find_program_from_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVProgram), c_int]
    av_find_program_from_stream.restype = POINTER(AVProgram)

# /usr/include/libavformat/avformat.h: 2271
if _libs["avformat"].has("av_program_add_stream_index", "cdecl"):
    av_program_add_stream_index = _libs["avformat"].get("av_program_add_stream_index", "cdecl")
    av_program_add_stream_index.argtypes = [POINTER(AVFormatContext), c_int, c_uint]
    av_program_add_stream_index.restype = None

# /usr/include/libavformat/avformat.h: 2297
if _libs["avformat"].has("av_find_best_stream", "cdecl"):
    av_find_best_stream = _libs["avformat"].get("av_find_best_stream", "cdecl")
    av_find_best_stream.argtypes = [POINTER(AVFormatContext), enum_AVMediaType, c_int, c_int, POINTER(POINTER(AVCodec)), c_int]
    av_find_best_stream.restype = c_int

# /usr/include/libavformat/avformat.h: 2331
if _libs["avformat"].has("av_read_frame", "cdecl"):
    av_read_frame = _libs["avformat"].get("av_read_frame", "cdecl")
    # av_read_frame.argtypes = [POINTER(AVFormatContext, POINTER(AVPacket)]
    av_read_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2346
if _libs["avformat"].has("av_seek_frame", "cdecl"):
    av_seek_frame = _libs["avformat"].get("av_seek_frame", "cdecl")
    av_seek_frame.argtypes = [POINTER(AVFormatContext), c_int, c_int64, c_int]
    av_seek_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2375
if _libs["avformat"].has("avformat_seek_file", "cdecl"):
    avformat_seek_file = _libs["avformat"].get("avformat_seek_file", "cdecl")
    avformat_seek_file.argtypes = [POINTER(AVFormatContext), c_int, c_int64, c_int64, c_int64, c_int]
    avformat_seek_file.restype = c_int

# /usr/include/libavformat/avformat.h: 2393
if _libs["avformat"].has("avformat_flush", "cdecl"):
    avformat_flush = _libs["avformat"].get("avformat_flush", "cdecl")
    avformat_flush.argtypes = [POINTER(AVFormatContext)]
    avformat_flush.restype = c_int

# /usr/include/libavformat/avformat.h: 2399
if _libs["avformat"].has("av_read_play", "cdecl"):
    av_read_play = _libs["avformat"].get("av_read_play", "cdecl")
    av_read_play.argtypes = [POINTER(AVFormatContext)]
    av_read_play.restype = c_int

# /usr/include/libavformat/avformat.h: 2406
if _libs["avformat"].has("av_read_pause", "cdecl"):
    av_read_pause = _libs["avformat"].get("av_read_pause", "cdecl")
    av_read_pause.argtypes = [POINTER(AVFormatContext)]
    av_read_pause.restype = c_int

# /usr/include/libavformat/avformat.h: 2412
if _libs["avformat"].has("avformat_close_input", "cdecl"):
    avformat_close_input = _libs["avformat"].get("avformat_close_input", "cdecl")
    avformat_close_input.argtypes = [POINTER(POINTER(AVFormatContext))]
    avformat_close_input.restype = None

# /usr/include/libavformat/avformat.h: 2448
if _libs["avformat"].has("avformat_write_header", "cdecl"):
    avformat_write_header = _libs["avformat"].get("avformat_write_header", "cdecl")
    avformat_write_header.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_write_header.restype = c_int

# /usr/include/libavformat/avformat.h: 2470
if _libs["avformat"].has("avformat_init_output", "cdecl"):
    avformat_init_output = _libs["avformat"].get("avformat_init_output", "cdecl")
    avformat_init_output.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_init_output.restype = c_int

# /usr/include/libavformat/avformat.h: 2509
if _libs["avformat"].has("av_write_frame", "cdecl"):
    av_write_frame = _libs["avformat"].get("av_write_frame", "cdecl")
    av_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
    av_write_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2554
if _libs["avformat"].has("av_interleaved_write_frame", "cdecl"):
    av_interleaved_write_frame = _libs["avformat"].get("av_interleaved_write_frame", "cdecl")
    av_interleaved_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
    av_interleaved_write_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2564
if _libs["avformat"].has("av_write_uncoded_frame", "cdecl"):
    av_write_uncoded_frame = _libs["avformat"].get("av_write_uncoded_frame", "cdecl")
    av_write_uncoded_frame.argtypes = [POINTER(AVFormatContext), c_int, POINTER(AVFrame)]
    av_write_uncoded_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2583
if _libs["avformat"].has("av_interleaved_write_uncoded_frame", "cdecl"):
    av_interleaved_write_uncoded_frame = _libs["avformat"].get("av_interleaved_write_uncoded_frame", "cdecl")
    av_interleaved_write_uncoded_frame.argtypes = [POINTER(AVFormatContext), c_int, POINTER(AVFrame)]
    av_interleaved_write_uncoded_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2592
if _libs["avformat"].has("av_write_uncoded_frame_query", "cdecl"):
    av_write_uncoded_frame_query = _libs["avformat"].get("av_write_uncoded_frame_query", "cdecl")
    av_write_uncoded_frame_query.argtypes = [POINTER(AVFormatContext), c_int]
    av_write_uncoded_frame_query.restype = c_int

# /usr/include/libavformat/avformat.h: 2603
if _libs["avformat"].has("av_write_trailer", "cdecl"):
    av_write_trailer = _libs["avformat"].get("av_write_trailer", "cdecl")
    av_write_trailer.argtypes = [POINTER(AVFormatContext)]
    av_write_trailer.restype = c_int

# /usr/include/libavformat/avformat.h: 2617
if _libs["avformat"].has("av_guess_format", "cdecl"):
    av_guess_format = _libs["avformat"].get("av_guess_format", "cdecl")
    av_guess_format.argtypes = [String, String, String]
    av_guess_format.restype = POINTER(AVOutputFormat)

# /usr/include/libavformat/avformat.h: 2624
if _libs["avformat"].has("av_guess_codec", "cdecl"):
    av_guess_codec = _libs["avformat"].get("av_guess_codec", "cdecl")
    av_guess_codec.argtypes = [POINTER(AVOutputFormat), String, String, String, enum_AVMediaType]
    av_guess_codec.restype = enum_AVCodecID

# /usr/include/libavformat/avformat.h: 2643
if _libs["avformat"].has("av_get_output_timestamp", "cdecl"):
    av_get_output_timestamp = _libs["avformat"].get("av_get_output_timestamp", "cdecl")
    av_get_output_timestamp.argtypes = [POINTER(struct_AVFormatContext), c_int, POINTER(c_int64), POINTER(c_int64)]
    av_get_output_timestamp.restype = c_int

# /usr/include/libavformat/avformat.h: 2670
if _libs["avformat"].has("av_hex_dump", "cdecl"):
    av_hex_dump = _libs["avformat"].get("av_hex_dump", "cdecl")
    av_hex_dump.argtypes = [POINTER(FILE), POINTER(c_uint8), c_int]
    av_hex_dump.restype = None

# /usr/include/libavformat/avformat.h: 2684
if _libs["avformat"].has("av_hex_dump_log", "cdecl"):
    av_hex_dump_log = _libs["avformat"].get("av_hex_dump_log", "cdecl")
    av_hex_dump_log.argtypes = [POINTER(None), c_int, POINTER(c_uint8), c_int]
    av_hex_dump_log.restype = None

# /usr/include/libavformat/avformat.h: 2694
if _libs["avformat"].has("av_pkt_dump2", "cdecl"):
    av_pkt_dump2 = _libs["avformat"].get("av_pkt_dump2", "cdecl")
    av_pkt_dump2.argtypes = [POINTER(FILE), POINTER(AVPacket), c_int, POINTER(AVStream)]
    av_pkt_dump2.restype = None

# /usr/include/libavformat/avformat.h: 2708
if _libs["avformat"].has("av_pkt_dump_log2", "cdecl"):
    av_pkt_dump_log2 = _libs["avformat"].get("av_pkt_dump_log2", "cdecl")
    av_pkt_dump_log2.argtypes = [POINTER(None), c_int, POINTER(AVPacket), c_int, POINTER(AVStream)]
    av_pkt_dump_log2.restype = None

# /usr/include/libavformat/avformat.h: 2719
if _libs["avformat"].has("av_codec_get_id", "cdecl"):
    av_codec_get_id = _libs["avformat"].get("av_codec_get_id", "cdecl")
    av_codec_get_id.argtypes = [POINTER(POINTER(struct_AVCodecTag)), c_uint]
    av_codec_get_id.restype = enum_AVCodecID

# /usr/include/libavformat/avformat.h: 2729
if _libs["avformat"].has("av_codec_get_tag", "cdecl"):
    av_codec_get_tag = _libs["avformat"].get("av_codec_get_tag", "cdecl")
    av_codec_get_tag.argtypes = [POINTER(POINTER(struct_AVCodecTag)), enum_AVCodecID]
    av_codec_get_tag.restype = c_uint

# /usr/include/libavformat/avformat.h: 2740
if _libs["avformat"].has("av_codec_get_tag2", "cdecl"):
    av_codec_get_tag2 = _libs["avformat"].get("av_codec_get_tag2", "cdecl")
    av_codec_get_tag2.argtypes = [POINTER(POINTER(struct_AVCodecTag)), enum_AVCodecID, POINTER(c_uint)]
    av_codec_get_tag2.restype = c_int

# /usr/include/libavformat/avformat.h: 2743
if _libs["avformat"].has("av_find_default_stream_index", "cdecl"):
    av_find_default_stream_index = _libs["avformat"].get("av_find_default_stream_index", "cdecl")
    av_find_default_stream_index.argtypes = [POINTER(AVFormatContext)]
    av_find_default_stream_index.restype = c_int

# /usr/include/libavformat/avformat.h: 2756
if _libs["avformat"].has("av_index_search_timestamp", "cdecl"):
    av_index_search_timestamp = _libs["avformat"].get("av_index_search_timestamp", "cdecl")
    av_index_search_timestamp.argtypes = [POINTER(AVStream), c_int64, c_int]
    av_index_search_timestamp.restype = c_int

# /usr/include/libavformat/avformat.h: 2764
if _libs["avformat"].has("av_add_index_entry", "cdecl"):
    av_add_index_entry = _libs["avformat"].get("av_add_index_entry", "cdecl")
    av_add_index_entry.argtypes = [POINTER(AVStream), c_int64, c_int64, c_int, c_int, c_int]
    av_add_index_entry.restype = c_int

# /usr/include/libavformat/avformat.h: 2787
if _libs["avformat"].has("av_url_split", "cdecl"):
    av_url_split = _libs["avformat"].get("av_url_split", "cdecl")
    av_url_split.argtypes = [String, c_int, String, c_int, String, c_int, POINTER(c_int), String, c_int, String]
    av_url_split.restype = None

# /usr/include/libavformat/avformat.h: 2805
if _libs["avformat"].has("av_dump_format", "cdecl"):
    av_dump_format = _libs["avformat"].get("av_dump_format", "cdecl")
    av_dump_format.argtypes = [POINTER(AVFormatContext), c_int, String, c_int]
    av_dump_format.restype = None

# /usr/include/libavformat/avformat.h: 2826
if _libs["avformat"].has("av_get_frame_filename2", "cdecl"):
    av_get_frame_filename2 = _libs["avformat"].get("av_get_frame_filename2", "cdecl")
    av_get_frame_filename2.argtypes = [String, c_int, String, c_int, c_int]
    av_get_frame_filename2.restype = c_int

# /usr/include/libavformat/avformat.h: 2829
if _libs["avformat"].has("av_get_frame_filename", "cdecl"):
    av_get_frame_filename = _libs["avformat"].get("av_get_frame_filename", "cdecl")
    av_get_frame_filename.argtypes = [String, c_int, String, c_int]
    av_get_frame_filename.restype = c_int

# /usr/include/libavformat/avformat.h: 2838
if _libs["avformat"].has("av_filename_number_test", "cdecl"):
    av_filename_number_test = _libs["avformat"].get("av_filename_number_test", "cdecl")
    av_filename_number_test.argtypes = [String]
    av_filename_number_test.restype = c_int

# /usr/include/libavformat/avformat.h: 2857
if _libs["avformat"].has("av_sdp_create", "cdecl"):
    av_sdp_create = _libs["avformat"].get("av_sdp_create", "cdecl")
    av_sdp_create.argtypes = [POINTER(POINTER(AVFormatContext)), c_int, String, c_int]
    av_sdp_create.restype = c_int

# /usr/include/libavformat/avformat.h: 2866
if _libs["avformat"].has("av_match_ext", "cdecl"):
    av_match_ext = _libs["avformat"].get("av_match_ext", "cdecl")
    av_match_ext.argtypes = [String, String]
    av_match_ext.restype = c_int

# /usr/include/libavformat/avformat.h: 2878
if _libs["avformat"].has("avformat_query_codec", "cdecl"):
    avformat_query_codec = _libs["avformat"].get("avformat_query_codec", "cdecl")
    avformat_query_codec.argtypes = [POINTER(AVOutputFormat), enum_AVCodecID, c_int]
    avformat_query_codec.restype = c_int

# /usr/include/libavformat/avformat.h: 2896
if _libs["avformat"].has("avformat_get_riff_video_tags", "cdecl"):
    avformat_get_riff_video_tags = _libs["avformat"].get("avformat_get_riff_video_tags", "cdecl")
    avformat_get_riff_video_tags.argtypes = []
    avformat_get_riff_video_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2900
if _libs["avformat"].has("avformat_get_riff_audio_tags", "cdecl"):
    avformat_get_riff_audio_tags = _libs["avformat"].get("avformat_get_riff_audio_tags", "cdecl")
    avformat_get_riff_audio_tags.argtypes = []
    avformat_get_riff_audio_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2904
if _libs["avformat"].has("avformat_get_mov_video_tags", "cdecl"):
    avformat_get_mov_video_tags = _libs["avformat"].get("avformat_get_mov_video_tags", "cdecl")
    avformat_get_mov_video_tags.argtypes = []
    avformat_get_mov_video_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2908
if _libs["avformat"].has("avformat_get_mov_audio_tags", "cdecl"):
    avformat_get_mov_audio_tags = _libs["avformat"].get("avformat_get_mov_audio_tags", "cdecl")
    avformat_get_mov_audio_tags.argtypes = []
    avformat_get_mov_audio_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2931
if _libs["avformat"].has("av_guess_sample_aspect_ratio", "cdecl"):
    av_guess_sample_aspect_ratio = _libs["avformat"].get("av_guess_sample_aspect_ratio", "cdecl")
    av_guess_sample_aspect_ratio.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), POINTER(AVFrame)]
    av_guess_sample_aspect_ratio.restype = AVRational

# /usr/include/libavformat/avformat.h: 2941
if _libs["avformat"].has("av_guess_frame_rate", "cdecl"):
    av_guess_frame_rate = _libs["avformat"].get("av_guess_frame_rate", "cdecl")
    av_guess_frame_rate.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), POINTER(AVFrame)]
    av_guess_frame_rate.restype = AVRational

# /usr/include/libavformat/avformat.h: 2956
if _libs["avformat"].has("avformat_match_stream_specifier", "cdecl"):
    avformat_match_stream_specifier = _libs["avformat"].get("avformat_match_stream_specifier", "cdecl")
    avformat_match_stream_specifier.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), String]
    avformat_match_stream_specifier.restype = c_int

# /usr/include/libavformat/avformat.h: 2959
if _libs["avformat"].has("avformat_queue_attached_pictures", "cdecl"):
    avformat_queue_attached_pictures = _libs["avformat"].get("avformat_queue_attached_pictures", "cdecl")
    avformat_queue_attached_pictures.argtypes = [POINTER(AVFormatContext)]
    avformat_queue_attached_pictures.restype = c_int

# /usr/include/libavformat/avformat.h: 2974
if _libs["avformat"].has("av_apply_bitstream_filters", "cdecl"):
    av_apply_bitstream_filters = _libs["avformat"].get("av_apply_bitstream_filters", "cdecl")
    av_apply_bitstream_filters.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVBitStreamFilterContext)]
    av_apply_bitstream_filters.restype = c_int

enum_AVTimebaseSource = c_int# /usr/include/libavformat/avformat.h: 2978

AVFMT_TBCF_AUTO = (-1)# /usr/include/libavformat/avformat.h: 2978

AVFMT_TBCF_DECODER = (AVFMT_TBCF_AUTO + 1)# /usr/include/libavformat/avformat.h: 2978

AVFMT_TBCF_DEMUXER = (AVFMT_TBCF_DECODER + 1)# /usr/include/libavformat/avformat.h: 2978

AVFMT_TBCF_R_FRAMERATE = (AVFMT_TBCF_DEMUXER + 1)# /usr/include/libavformat/avformat.h: 2978

# /usr/include/libavformat/avformat.h: 2997
if _libs["avformat"].has("avformat_transfer_internal_stream_timing_info", "cdecl"):
    avformat_transfer_internal_stream_timing_info = _libs["avformat"].get("avformat_transfer_internal_stream_timing_info", "cdecl")
    avformat_transfer_internal_stream_timing_info.argtypes = [POINTER(AVOutputFormat), POINTER(AVStream), POINTER(AVStream), enum_AVTimebaseSource]
    avformat_transfer_internal_stream_timing_info.restype = c_int

# /usr/include/libavformat/avformat.h: 3006
if _libs["avformat"].has("av_stream_get_codec_timebase", "cdecl"):
    av_stream_get_codec_timebase = _libs["avformat"].get("av_stream_get_codec_timebase", "cdecl")
    av_stream_get_codec_timebase.argtypes = [POINTER(AVStream)]
    av_stream_get_codec_timebase.restype = AVRational

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

# /usr/include/libavformat/avio.h: 40
try:
    AVIO_SEEKABLE_NORMAL = (1 << 0)
except:
    pass

# /usr/include/libavformat/avio.h: 45
try:
    AVIO_SEEKABLE_TIME = (1 << 1)
except:
    pass

# /usr/include/libavformat/avio.h: 531
try:
    AVSEEK_SIZE = 65536
except:
    pass

# /usr/include/libavformat/avio.h: 539
try:
    AVSEEK_FORCE = 131072
except:
    pass

# /usr/include/libavformat/avio.h: 674
try:
    AVIO_FLAG_READ = 1
except:
    pass

# /usr/include/libavformat/avio.h: 675
try:
    AVIO_FLAG_WRITE = 2
except:
    pass

# /usr/include/libavformat/avio.h: 676
try:
    AVIO_FLAG_READ_WRITE = (AVIO_FLAG_READ | AVIO_FLAG_WRITE)
except:
    pass

# /usr/include/libavformat/avio.h: 693
try:
    AVIO_FLAG_NONBLOCK = 8
except:
    pass

# /usr/include/libavformat/avio.h: 701
try:
    AVIO_FLAG_DIRECT = 32768
except:
    pass

# /usr/include/libavformat/avformat.h: 448
try:
    AVPROBE_SCORE_RETRY = (AVPROBE_SCORE_MAX / 4)
except:
    pass

# /usr/include/libavformat/avformat.h: 449
try:
    AVPROBE_SCORE_STREAM_RETRY = ((AVPROBE_SCORE_MAX / 4) - 1)
except:
    pass

# /usr/include/libavformat/avformat.h: 451
try:
    AVPROBE_SCORE_EXTENSION = 50
except:
    pass

# /usr/include/libavformat/avformat.h: 452
try:
    AVPROBE_SCORE_MIME = 75
except:
    pass

# /usr/include/libavformat/avformat.h: 453
try:
    AVPROBE_SCORE_MAX = 100
except:
    pass

# /usr/include/libavformat/avformat.h: 455
try:
    AVPROBE_PADDING_SIZE = 32
except:
    pass

# /usr/include/libavformat/avformat.h: 458
try:
    AVFMT_NOFILE = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 459
try:
    AVFMT_NEEDNUMBER = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 460
try:
    AVFMT_SHOW_IDS = 8
except:
    pass

# /usr/include/libavformat/avformat.h: 461
try:
    AVFMT_GLOBALHEADER = 64
except:
    pass

# /usr/include/libavformat/avformat.h: 462
try:
    AVFMT_NOTIMESTAMPS = 128
except:
    pass

# /usr/include/libavformat/avformat.h: 463
try:
    AVFMT_GENERIC_INDEX = 256
except:
    pass

# /usr/include/libavformat/avformat.h: 464
try:
    AVFMT_TS_DISCONT = 512
except:
    pass

# /usr/include/libavformat/avformat.h: 465
try:
    AVFMT_VARIABLE_FPS = 1024
except:
    pass

# /usr/include/libavformat/avformat.h: 466
try:
    AVFMT_NODIMENSIONS = 2048
except:
    pass

# /usr/include/libavformat/avformat.h: 467
try:
    AVFMT_NOSTREAMS = 4096
except:
    pass

# /usr/include/libavformat/avformat.h: 468
try:
    AVFMT_NOBINSEARCH = 8192
except:
    pass

# /usr/include/libavformat/avformat.h: 469
try:
    AVFMT_NOGENSEARCH = 16384
except:
    pass

# /usr/include/libavformat/avformat.h: 470
try:
    AVFMT_NO_BYTE_SEEK = 32768
except:
    pass

# /usr/include/libavformat/avformat.h: 471
try:
    AVFMT_ALLOW_FLUSH = 65536
except:
    pass

# /usr/include/libavformat/avformat.h: 472
try:
    AVFMT_TS_NONSTRICT = 131072
except:
    pass

# /usr/include/libavformat/avformat.h: 475
try:
    AVFMT_TS_NEGATIVE = 262144
except:
    pass

# /usr/include/libavformat/avformat.h: 484
try:
    AVFMT_SEEK_TO_PTS = 67108864
except:
    pass

# /usr/include/libavformat/avformat.h: 811
try:
    AVINDEX_KEYFRAME = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 812
try:
    AVINDEX_DISCARD_FRAME = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 820
try:
    AV_DISPOSITION_DEFAULT = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 821
try:
    AV_DISPOSITION_DUB = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 822
try:
    AV_DISPOSITION_ORIGINAL = 4
except:
    pass

# /usr/include/libavformat/avformat.h: 823
try:
    AV_DISPOSITION_COMMENT = 8
except:
    pass

# /usr/include/libavformat/avformat.h: 824
try:
    AV_DISPOSITION_LYRICS = 16
except:
    pass

# /usr/include/libavformat/avformat.h: 825
try:
    AV_DISPOSITION_KARAOKE = 32
except:
    pass

# /usr/include/libavformat/avformat.h: 832
try:
    AV_DISPOSITION_FORCED = 64
except:
    pass

# /usr/include/libavformat/avformat.h: 833
try:
    AV_DISPOSITION_HEARING_IMPAIRED = 128
except:
    pass

# /usr/include/libavformat/avformat.h: 834
try:
    AV_DISPOSITION_VISUAL_IMPAIRED = 256
except:
    pass

# /usr/include/libavformat/avformat.h: 835
try:
    AV_DISPOSITION_CLEAN_EFFECTS = 512
except:
    pass

# /usr/include/libavformat/avformat.h: 843
try:
    AV_DISPOSITION_ATTACHED_PIC = 1024
except:
    pass

# /usr/include/libavformat/avformat.h: 848
try:
    AV_DISPOSITION_TIMED_THUMBNAILS = 2048
except:
    pass

# /usr/include/libavformat/avformat.h: 855
try:
    AV_DISPOSITION_CAPTIONS = 65536
except:
    pass

# /usr/include/libavformat/avformat.h: 856
try:
    AV_DISPOSITION_DESCRIPTIONS = 131072
except:
    pass

# /usr/include/libavformat/avformat.h: 857
try:
    AV_DISPOSITION_METADATA = 262144
except:
    pass

# /usr/include/libavformat/avformat.h: 858
try:
    AV_DISPOSITION_DEPENDENT = 524288
except:
    pass

# /usr/include/libavformat/avformat.h: 859
try:
    AV_DISPOSITION_STILL_IMAGE = 1048576
except:
    pass

# /usr/include/libavformat/avformat.h: 864
try:
    AV_PTS_WRAP_IGNORE = 0
except:
    pass

# /usr/include/libavformat/avformat.h: 865
try:
    AV_PTS_WRAP_ADD_OFFSET = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 866
try:
    AV_PTS_WRAP_SUB_OFFSET = (-1)
except:
    pass

# /usr/include/libavformat/avformat.h: 1001
try:
    AVSTREAM_EVENT_FLAG_METADATA_UPDATED = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1007
try:
    AVSTREAM_EVENT_FLAG_NEW_PACKETS = (1 << 1)
except:
    pass

# /usr/include/libavformat/avformat.h: 1144
try:
    AV_PROGRAM_RUNNING = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1179
try:
    AVFMTCTX_NOHEADER = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1181
try:
    AVFMTCTX_UNSEEKABLE = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 1366
try:
    AVFMT_FLAG_GENPTS = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1367
try:
    AVFMT_FLAG_IGNIDX = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 1368
try:
    AVFMT_FLAG_NONBLOCK = 4
except:
    pass

# /usr/include/libavformat/avformat.h: 1369
try:
    AVFMT_FLAG_IGNDTS = 8
except:
    pass

# /usr/include/libavformat/avformat.h: 1370
try:
    AVFMT_FLAG_NOFILLIN = 16
except:
    pass

# /usr/include/libavformat/avformat.h: 1371
try:
    AVFMT_FLAG_NOPARSE = 32
except:
    pass

# /usr/include/libavformat/avformat.h: 1372
try:
    AVFMT_FLAG_NOBUFFER = 64
except:
    pass

# /usr/include/libavformat/avformat.h: 1373
try:
    AVFMT_FLAG_CUSTOM_IO = 128
except:
    pass

# /usr/include/libavformat/avformat.h: 1374
try:
    AVFMT_FLAG_DISCARD_CORRUPT = 256
except:
    pass

# /usr/include/libavformat/avformat.h: 1375
try:
    AVFMT_FLAG_FLUSH_PACKETS = 512
except:
    pass

# /usr/include/libavformat/avformat.h: 1382
try:
    AVFMT_FLAG_BITEXACT = 1024
except:
    pass

# /usr/include/libavformat/avformat.h: 1384
try:
    AVFMT_FLAG_MP4A_LATM = 32768
except:
    pass

# /usr/include/libavformat/avformat.h: 1386
try:
    AVFMT_FLAG_SORT_DTS = 65536
except:
    pass

# /usr/include/libavformat/avformat.h: 1388
try:
    AVFMT_FLAG_PRIV_OPT = 131072
except:
    pass

# /usr/include/libavformat/avformat.h: 1391
try:
    AVFMT_FLAG_KEEP_SIDE_DATA = 262144
except:
    pass

# /usr/include/libavformat/avformat.h: 1393
try:
    AVFMT_FLAG_FAST_SEEK = 524288
except:
    pass

# /usr/include/libavformat/avformat.h: 1394
try:
    AVFMT_FLAG_SHORTEST = 1048576
except:
    pass

# /usr/include/libavformat/avformat.h: 1395
try:
    AVFMT_FLAG_AUTO_BSF = 2097152
except:
    pass

# /usr/include/libavformat/avformat.h: 1520
try:
    FF_FDEBUG_TS = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1564
try:
    AVFMT_EVENT_FLAG_METADATA_UPDATED = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1580
try:
    AVFMT_AVOID_NEG_TS_AUTO = (-1)
except:
    pass

# /usr/include/libavformat/avformat.h: 1581
try:
    AVFMT_AVOID_NEG_TS_MAKE_NON_NEGATIVE = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1582
try:
    AVFMT_AVOID_NEG_TS_MAKE_ZERO = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 2417
try:
    AVSEEK_FLAG_BACKWARD = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 2418
try:
    AVSEEK_FLAG_BYTE = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 2419
try:
    AVSEEK_FLAG_ANY = 4
except:
    pass

# /usr/include/libavformat/avformat.h: 2420
try:
    AVSEEK_FLAG_FRAME = 8
except:
    pass

# /usr/include/libavformat/avformat.h: 2427
try:
    AVSTREAM_INIT_IN_WRITE_HEADER = 0
except:
    pass

# /usr/include/libavformat/avformat.h: 2428
try:
    AVSTREAM_INIT_IN_INIT_OUTPUT = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 2811
try:
    AV_FRAME_FILENAME_FLAGS_MULTIPLE = 1
except:
    pass

AVIOInterruptCB = struct_AVIOInterruptCB# /usr/include/libavformat/avio.h: 61

AVIODirEntry = struct_AVIODirEntry# /usr/include/libavformat/avio.h: 101

URLContext = struct_URLContext# /usr/include/libavformat/avio.h: 104

AVIODirContext = struct_AVIODirContext# /usr/include/libavformat/avio.h: 105

AVIOContext = struct_AVIOContext# /usr/include/libavformat/avio.h: 352

AVFormatContext = struct_AVFormatContext# /usr/include/libavformat/avformat.h: 1234

AVDeviceInfoList = struct_AVDeviceInfoList# /usr/include/libavformat/avformat.h: 321

AVDeviceCapabilitiesQuery = struct_AVDeviceCapabilitiesQuery# /usr/include/libavformat/avformat.h: 322

AVCodecTag = struct_AVCodecTag# /usr/include/libavformat/avformat.h: 436

AVProbeData = struct_AVProbeData# /usr/include/libavformat/avformat.h: 446

AVOutputFormat = struct_AVOutputFormat# /usr/include/libavformat/avformat.h: 490

AVInputFormat = struct_AVInputFormat# /usr/include/libavformat/avformat.h: 640

AVIndexEntry = struct_AVIndexEntry# /usr/include/libavformat/avformat.h: 818

AVStreamInternal = struct_AVStreamInternal# /usr/include/libavformat/avformat.h: 850

AVStream = struct_AVStream# /usr/include/libavformat/avformat.h: 1116

AVProgram = struct_AVProgram# /usr/include/libavformat/avformat.h: 1177

AVChapter = struct_AVChapter# /usr/include/libavformat/avformat.h: 1196

AVFormatInternal = struct_AVFormatInternal# /usr/include/libavformat/avformat.h: 1218

# No inserted files

# No prefix-stripping

