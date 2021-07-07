r"""Wrapper for opus.h

Generated with:
./ctypesgen -I/usr/include/opus -lopus -lopusfile /usr/include/opus/opus.h /usr/include/opus/opusfile.h /usr/include/opus/opus_defines.h -o opus.py

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
_libdirs = []

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

add_library_search_dirs([])

# Begin libraries
_libs["opus"] = load_library("opus")
_libs["opusfile"] = load_library("opusfile")

# 2 libraries
# End libraries

# No modules

opus_int16 = c_int16# /usr/include/opus/opus_types.h: 53

opus_int32 = c_int32# /usr/include/opus/opus_types.h: 55

opus_uint32 = c_uint32# /usr/include/opus/opus_types.h: 56

opus_int64 = c_int64# /usr/include/opus/opus_types.h: 57

# /usr/include/opus/opus_defines.h: 782
if _libs["opus"].has("opus_strerror", "cdecl"):
    opus_strerror = _libs["opus"].get("opus_strerror", "cdecl")
    opus_strerror.argtypes = [c_int]
    opus_strerror.restype = c_char_p

# /usr/include/opus/opus_defines.h: 792
if _libs["opus"].has("opus_get_version_string", "cdecl"):
    opus_get_version_string = _libs["opus"].get("opus_get_version_string", "cdecl")
    opus_get_version_string.argtypes = []
    opus_get_version_string.restype = c_char_p

# /usr/include/opus/opus.h: 164
class struct_OpusEncoder(Structure):
    pass

OpusEncoder = struct_OpusEncoder# /usr/include/opus/opus.h: 164

# /usr/include/opus/opus.h: 171
if _libs["opus"].has("opus_encoder_get_size", "cdecl"):
    opus_encoder_get_size = _libs["opus"].get("opus_encoder_get_size", "cdecl")
    opus_encoder_get_size.argtypes = [c_int]
    opus_encoder_get_size.restype = c_int

# /usr/include/opus/opus.h: 208
if _libs["opus"].has("opus_encoder_create", "cdecl"):
    opus_encoder_create = _libs["opus"].get("opus_encoder_create", "cdecl")
    opus_encoder_create.argtypes = [opus_int32, c_int, c_int, POINTER(c_int)]
    opus_encoder_create.restype = POINTER(OpusEncoder)

# /usr/include/opus/opus.h: 228
if _libs["opus"].has("opus_encoder_init", "cdecl"):
    opus_encoder_init = _libs["opus"].get("opus_encoder_init", "cdecl")
    opus_encoder_init.argtypes = [POINTER(OpusEncoder), opus_int32, c_int, c_int]
    opus_encoder_init.restype = c_int

# /usr/include/opus/opus.h: 263
if _libs["opus"].has("opus_encode", "cdecl"):
    opus_encode = _libs["opus"].get("opus_encode", "cdecl")
    opus_encode.argtypes = [POINTER(OpusEncoder), POINTER(opus_int16), c_int, POINTER(c_ubyte), opus_int32]
    opus_encode.restype = opus_int32

# /usr/include/opus/opus.h: 304
if _libs["opus"].has("opus_encode_float", "cdecl"):
    opus_encode_float = _libs["opus"].get("opus_encode_float", "cdecl")
    opus_encode_float.argtypes = [POINTER(OpusEncoder), POINTER(c_float), c_int, POINTER(c_ubyte), opus_int32]
    opus_encode_float.restype = opus_int32

# /usr/include/opus/opus.h: 315
if _libs["opus"].has("opus_encoder_destroy", "cdecl"):
    opus_encoder_destroy = _libs["opus"].get("opus_encoder_destroy", "cdecl")
    opus_encoder_destroy.argtypes = [POINTER(OpusEncoder)]
    opus_encoder_destroy.restype = None

# /usr/include/opus/opus.h: 328
if _libs["opus"].has("opus_encoder_ctl", "cdecl"):
    _func = _libs["opus"].get("opus_encoder_ctl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(OpusEncoder), c_int]
    opus_encoder_ctl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/opus/opus.h: 399
class struct_OpusDecoder(Structure):
    pass

OpusDecoder = struct_OpusDecoder# /usr/include/opus/opus.h: 399

# /usr/include/opus/opus.h: 406
if _libs["opus"].has("opus_decoder_get_size", "cdecl"):
    opus_decoder_get_size = _libs["opus"].get("opus_decoder_get_size", "cdecl")
    opus_decoder_get_size.argtypes = [c_int]
    opus_decoder_get_size.restype = c_int

# /usr/include/opus/opus.h: 423
if _libs["opus"].has("opus_decoder_create", "cdecl"):
    opus_decoder_create = _libs["opus"].get("opus_decoder_create", "cdecl")
    opus_decoder_create.argtypes = [opus_int32, c_int, POINTER(c_int)]
    opus_decoder_create.restype = POINTER(OpusDecoder)

# /usr/include/opus/opus.h: 440
if _libs["opus"].has("opus_decoder_init", "cdecl"):
    opus_decoder_init = _libs["opus"].get("opus_decoder_init", "cdecl")
    opus_decoder_init.argtypes = [POINTER(OpusDecoder), opus_int32, c_int]
    opus_decoder_init.restype = c_int

# /usr/include/opus/opus.h: 462
if _libs["opus"].has("opus_decode", "cdecl"):
    opus_decode = _libs["opus"].get("opus_decode", "cdecl")
    opus_decode.argtypes = [POINTER(OpusDecoder), POINTER(c_ubyte), opus_int32, POINTER(opus_int16), c_int, c_int]
    opus_decode.restype = c_int

# /usr/include/opus/opus.h: 487
if _libs["opus"].has("opus_decode_float", "cdecl"):
    opus_decode_float = _libs["opus"].get("opus_decode_float", "cdecl")
    opus_decode_float.argtypes = [POINTER(OpusDecoder), POINTER(c_ubyte), opus_int32, POINTER(c_float), c_int, c_int]
    opus_decode_float.restype = c_int

# /usr/include/opus/opus.h: 507
if _libs["opus"].has("opus_decoder_ctl", "cdecl"):
    _func = _libs["opus"].get("opus_decoder_ctl", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(OpusDecoder), c_int]
    opus_decoder_ctl = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/opus/opus.h: 512
if _libs["opus"].has("opus_decoder_destroy", "cdecl"):
    opus_decoder_destroy = _libs["opus"].get("opus_decoder_destroy", "cdecl")
    opus_decoder_destroy.argtypes = [POINTER(OpusDecoder)]
    opus_decoder_destroy.restype = None

# /usr/include/opus/opus.h: 527
if _libs["opus"].has("opus_packet_parse", "cdecl"):
    opus_packet_parse = _libs["opus"].get("opus_packet_parse", "cdecl")
    opus_packet_parse.argtypes = [POINTER(c_ubyte), opus_int32, POINTER(c_ubyte), POINTER(c_ubyte) * int(48), opus_int16 * int(48), POINTER(c_int)]
    opus_packet_parse.restype = c_int

# /usr/include/opus/opus.h: 545
if _libs["opus"].has("opus_packet_get_bandwidth", "cdecl"):
    opus_packet_get_bandwidth = _libs["opus"].get("opus_packet_get_bandwidth", "cdecl")
    opus_packet_get_bandwidth.argtypes = [POINTER(c_ubyte)]
    opus_packet_get_bandwidth.restype = c_int

# /usr/include/opus/opus.h: 556
if _libs["opus"].has("opus_packet_get_samples_per_frame", "cdecl"):
    opus_packet_get_samples_per_frame = _libs["opus"].get("opus_packet_get_samples_per_frame", "cdecl")
    opus_packet_get_samples_per_frame.argtypes = [POINTER(c_ubyte), opus_int32]
    opus_packet_get_samples_per_frame.restype = c_int

# /usr/include/opus/opus.h: 563
if _libs["opus"].has("opus_packet_get_nb_channels", "cdecl"):
    opus_packet_get_nb_channels = _libs["opus"].get("opus_packet_get_nb_channels", "cdecl")
    opus_packet_get_nb_channels.argtypes = [POINTER(c_ubyte)]
    opus_packet_get_nb_channels.restype = c_int

# /usr/include/opus/opus.h: 572
if _libs["opus"].has("opus_packet_get_nb_frames", "cdecl"):
    opus_packet_get_nb_frames = _libs["opus"].get("opus_packet_get_nb_frames", "cdecl")
    opus_packet_get_nb_frames.argtypes = [POINTER(c_ubyte), opus_int32]
    opus_packet_get_nb_frames.restype = c_int

# /usr/include/opus/opus.h: 584
if _libs["opus"].has("opus_packet_get_nb_samples", "cdecl"):
    opus_packet_get_nb_samples = _libs["opus"].get("opus_packet_get_nb_samples", "cdecl")
    opus_packet_get_nb_samples.argtypes = [POINTER(c_ubyte), opus_int32, opus_int32]
    opus_packet_get_nb_samples.restype = c_int

# /usr/include/opus/opus.h: 594
if _libs["opus"].has("opus_decoder_get_nb_samples", "cdecl"):
    opus_decoder_get_nb_samples = _libs["opus"].get("opus_decoder_get_nb_samples", "cdecl")
    opus_decoder_get_nb_samples.argtypes = [POINTER(OpusDecoder), POINTER(c_ubyte), opus_int32]
    opus_decoder_get_nb_samples.restype = c_int

# /usr/include/opus/opus.h: 606
if _libs["opus"].has("opus_pcm_soft_clip", "cdecl"):
    opus_pcm_soft_clip = _libs["opus"].get("opus_pcm_soft_clip", "cdecl")
    opus_pcm_soft_clip.argtypes = [POINTER(c_float), c_int, c_int, POINTER(c_float)]
    opus_pcm_soft_clip.restype = None

# /usr/include/opus/opus.h: 754
class struct_OpusRepacketizer(Structure):
    pass

OpusRepacketizer = struct_OpusRepacketizer# /usr/include/opus/opus.h: 754

# /usr/include/opus/opus.h: 759
if _libs["opus"].has("opus_repacketizer_get_size", "cdecl"):
    opus_repacketizer_get_size = _libs["opus"].get("opus_repacketizer_get_size", "cdecl")
    opus_repacketizer_get_size.argtypes = []
    opus_repacketizer_get_size.restype = c_int

# /usr/include/opus/opus.h: 778
if _libs["opus"].has("opus_repacketizer_init", "cdecl"):
    opus_repacketizer_init = _libs["opus"].get("opus_repacketizer_init", "cdecl")
    opus_repacketizer_init.argtypes = [POINTER(OpusRepacketizer)]
    opus_repacketizer_init.restype = POINTER(OpusRepacketizer)

# /usr/include/opus/opus.h: 783
if _libs["opus"].has("opus_repacketizer_create", "cdecl"):
    opus_repacketizer_create = _libs["opus"].get("opus_repacketizer_create", "cdecl")
    opus_repacketizer_create.argtypes = []
    opus_repacketizer_create.restype = POINTER(OpusRepacketizer)

# /usr/include/opus/opus.h: 789
if _libs["opus"].has("opus_repacketizer_destroy", "cdecl"):
    opus_repacketizer_destroy = _libs["opus"].get("opus_repacketizer_destroy", "cdecl")
    opus_repacketizer_destroy.argtypes = [POINTER(OpusRepacketizer)]
    opus_repacketizer_destroy.restype = None

# /usr/include/opus/opus.h: 838
if _libs["opus"].has("opus_repacketizer_cat", "cdecl"):
    opus_repacketizer_cat = _libs["opus"].get("opus_repacketizer_cat", "cdecl")
    opus_repacketizer_cat.argtypes = [POINTER(OpusRepacketizer), POINTER(c_ubyte), opus_int32]
    opus_repacketizer_cat.restype = c_int

# /usr/include/opus/opus.h: 872
if _libs["opus"].has("opus_repacketizer_out_range", "cdecl"):
    opus_repacketizer_out_range = _libs["opus"].get("opus_repacketizer_out_range", "cdecl")
    opus_repacketizer_out_range.argtypes = [POINTER(OpusRepacketizer), c_int, c_int, POINTER(c_ubyte), opus_int32]
    opus_repacketizer_out_range.restype = opus_int32

# /usr/include/opus/opus.h: 884
if _libs["opus"].has("opus_repacketizer_get_nb_frames", "cdecl"):
    opus_repacketizer_get_nb_frames = _libs["opus"].get("opus_repacketizer_get_nb_frames", "cdecl")
    opus_repacketizer_get_nb_frames.argtypes = [POINTER(OpusRepacketizer)]
    opus_repacketizer_get_nb_frames.restype = c_int

# /usr/include/opus/opus.h: 915
if _libs["opus"].has("opus_repacketizer_out", "cdecl"):
    opus_repacketizer_out = _libs["opus"].get("opus_repacketizer_out", "cdecl")
    opus_repacketizer_out.argtypes = [POINTER(OpusRepacketizer), POINTER(c_ubyte), opus_int32]
    opus_repacketizer_out.restype = opus_int32

# /usr/include/opus/opus.h: 929
if _libs["opus"].has("opus_packet_pad", "cdecl"):
    opus_packet_pad = _libs["opus"].get("opus_packet_pad", "cdecl")
    opus_packet_pad.argtypes = [POINTER(c_ubyte), opus_int32, opus_int32]
    opus_packet_pad.restype = c_int

# /usr/include/opus/opus.h: 942
if _libs["opus"].has("opus_packet_unpad", "cdecl"):
    opus_packet_unpad = _libs["opus"].get("opus_packet_unpad", "cdecl")
    opus_packet_unpad.argtypes = [POINTER(c_ubyte), opus_int32]
    opus_packet_unpad.restype = opus_int32

# /usr/include/opus/opus.h: 958
if _libs["opus"].has("opus_multistream_packet_pad", "cdecl"):
    opus_multistream_packet_pad = _libs["opus"].get("opus_multistream_packet_pad", "cdecl")
    opus_multistream_packet_pad.argtypes = [POINTER(c_ubyte), opus_int32, opus_int32, c_int]
    opus_multistream_packet_pad.restype = c_int

# /usr/include/opus/opus.h: 973
if _libs["opus"].has("opus_multistream_packet_unpad", "cdecl"):
    opus_multistream_packet_unpad = _libs["opus"].get("opus_multistream_packet_unpad", "cdecl")
    opus_multistream_packet_unpad.argtypes = [POINTER(c_ubyte), opus_int32, c_int]
    opus_multistream_packet_unpad.restype = opus_int32

ogg_int64_t = c_int64# /usr/include/ogg/config_types.h: 23

# /usr/include/ogg/ogg.h: 102
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'packet',
    'bytes',
    'b_o_s',
    'e_o_s',
    'granulepos',
    'packetno',
]
struct_anon_25._fields_ = [
    ('packet', POINTER(c_ubyte)),
    ('bytes', c_long),
    ('b_o_s', c_long),
    ('e_o_s', c_long),
    ('granulepos', ogg_int64_t),
    ('packetno', ogg_int64_t),
]

ogg_packet = struct_anon_25# /usr/include/ogg/ogg.h: 102

# /usr/include/opus/opus_multistream.h: 183
class struct_OpusMSDecoder(Structure):
    pass

OpusMSDecoder = struct_OpusMSDecoder# /usr/include/opus/opus_multistream.h: 183

# /usr/include/opus/opusfile.h: 215
class struct_OpusHead(Structure):
    pass

OpusHead = struct_OpusHead# /usr/include/opus/opusfile.h: 128

# /usr/include/opus/opusfile.h: 301
class struct_OpusTags(Structure):
    pass

OpusTags = struct_OpusTags# /usr/include/opus/opusfile.h: 129

# /usr/include/opus/opusfile.h: 331
class struct_OpusPictureTag(Structure):
    pass

OpusPictureTag = struct_OpusPictureTag# /usr/include/opus/opusfile.h: 130

# /usr/include/opus/opusfile.h: 712
class struct_OpusServerInfo(Structure):
    pass

OpusServerInfo = struct_OpusServerInfo# /usr/include/opus/opusfile.h: 131

# /usr/include/opus/opusfile.h: 901
class struct_OpusFileCallbacks(Structure):
    pass

OpusFileCallbacks = struct_OpusFileCallbacks# /usr/include/opus/opusfile.h: 132

# /usr/include/opus/opusfile.h: 133
class struct_OggOpusFile(Structure):
    pass

OggOpusFile = struct_OggOpusFile# /usr/include/opus/opusfile.h: 133

struct_OpusHead.__slots__ = [
    'version',
    'channel_count',
    'pre_skip',
    'input_sample_rate',
    'output_gain',
    'mapping_family',
    'stream_count',
    'coupled_count',
    'mapping',
]
struct_OpusHead._fields_ = [
    ('version', c_int),
    ('channel_count', c_int),
    ('pre_skip', c_uint),
    ('input_sample_rate', opus_uint32),
    ('output_gain', c_int),
    ('mapping_family', c_int),
    ('stream_count', c_int),
    ('coupled_count', c_int),
    ('mapping', c_ubyte * int(255)),
]

struct_OpusTags.__slots__ = [
    'user_comments',
    'comment_lengths',
    'comments',
    'vendor',
]
struct_OpusTags._fields_ = [
    ('user_comments', POINTER(POINTER(c_char))),
    ('comment_lengths', POINTER(c_int)),
    ('comments', c_int),
    ('vendor', String),
]

struct_OpusPictureTag.__slots__ = [
    'type',
    'mime_type',
    'description',
    'width',
    'height',
    'depth',
    'colors',
    'data_length',
    'data',
    'format',
]
struct_OpusPictureTag._fields_ = [
    ('type', opus_int32),
    ('mime_type', String),
    ('description', String),
    ('width', opus_uint32),
    ('height', opus_uint32),
    ('depth', opus_uint32),
    ('colors', opus_uint32),
    ('data_length', opus_uint32),
    ('data', POINTER(c_ubyte)),
    ('format', c_int),
]

# /usr/include/opus/opusfile.h: 428
if _libs["opusfile"].has("opus_head_parse", "cdecl"):
    opus_head_parse = _libs["opusfile"].get("opus_head_parse", "cdecl")
    opus_head_parse.argtypes = [POINTER(OpusHead), POINTER(c_ubyte), c_size_t]
    opus_head_parse.restype = c_int

# /usr/include/opus/opusfile.h: 445
if _libs["opusfile"].has("opus_granule_sample", "cdecl"):
    opus_granule_sample = _libs["opusfile"].get("opus_granule_sample", "cdecl")
    opus_granule_sample.argtypes = [POINTER(OpusHead), ogg_int64_t]
    opus_granule_sample.restype = ogg_int64_t

# /usr/include/opus/opusfile.h: 462
if _libs["opusfile"].has("opus_tags_parse", "cdecl"):
    opus_tags_parse = _libs["opusfile"].get("opus_tags_parse", "cdecl")
    opus_tags_parse.argtypes = [POINTER(OpusTags), POINTER(c_ubyte), c_size_t]
    opus_tags_parse.restype = c_int

# /usr/include/opus/opusfile.h: 472
if _libs["opusfile"].has("opus_tags_copy", "cdecl"):
    opus_tags_copy = _libs["opusfile"].get("opus_tags_copy", "cdecl")
    opus_tags_copy.argtypes = [POINTER(OpusTags), POINTER(OpusTags)]
    opus_tags_copy.restype = c_int

# /usr/include/opus/opusfile.h: 478
if _libs["opusfile"].has("opus_tags_init", "cdecl"):
    opus_tags_init = _libs["opusfile"].get("opus_tags_init", "cdecl")
    opus_tags_init.argtypes = [POINTER(OpusTags)]
    opus_tags_init.restype = None

# /usr/include/opus/opusfile.h: 491
if _libs["opusfile"].has("opus_tags_add", "cdecl"):
    opus_tags_add = _libs["opusfile"].get("opus_tags_add", "cdecl")
    opus_tags_add.argtypes = [POINTER(OpusTags), String, String]
    opus_tags_add.restype = c_int

# /usr/include/opus/opusfile.h: 504
if _libs["opusfile"].has("opus_tags_add_comment", "cdecl"):
    opus_tags_add_comment = _libs["opusfile"].get("opus_tags_add_comment", "cdecl")
    opus_tags_add_comment.argtypes = [POINTER(OpusTags), String]
    opus_tags_add_comment.restype = c_int

# /usr/include/opus/opusfile.h: 520
if _libs["opusfile"].has("opus_tags_set_binary_suffix", "cdecl"):
    opus_tags_set_binary_suffix = _libs["opusfile"].get("opus_tags_set_binary_suffix", "cdecl")
    opus_tags_set_binary_suffix.argtypes = [POINTER(OpusTags), POINTER(c_ubyte), c_int]
    opus_tags_set_binary_suffix.restype = c_int

# /usr/include/opus/opusfile.h: 538
if _libs["opusfile"].has("opus_tags_query", "cdecl"):
    opus_tags_query = _libs["opusfile"].get("opus_tags_query", "cdecl")
    opus_tags_query.argtypes = [POINTER(OpusTags), String, c_int]
    opus_tags_query.restype = c_char_p

# /usr/include/opus/opusfile.h: 548
if _libs["opusfile"].has("opus_tags_query_count", "cdecl"):
    opus_tags_query_count = _libs["opusfile"].get("opus_tags_query_count", "cdecl")
    opus_tags_query_count.argtypes = [POINTER(OpusTags), String]
    opus_tags_query_count.restype = c_int

# /usr/include/opus/opusfile.h: 556
if _libs["opusfile"].has("opus_tags_get_binary_suffix", "cdecl"):
    opus_tags_get_binary_suffix = _libs["opusfile"].get("opus_tags_get_binary_suffix", "cdecl")
    opus_tags_get_binary_suffix.argtypes = [POINTER(OpusTags), POINTER(c_int)]
    opus_tags_get_binary_suffix.restype = POINTER(c_ubyte)

# /usr/include/opus/opusfile.h: 574
if _libs["opusfile"].has("opus_tags_get_album_gain", "cdecl"):
    opus_tags_get_album_gain = _libs["opusfile"].get("opus_tags_get_album_gain", "cdecl")
    opus_tags_get_album_gain.argtypes = [POINTER(OpusTags), POINTER(c_int)]
    opus_tags_get_album_gain.restype = c_int

# /usr/include/opus/opusfile.h: 592
if _libs["opusfile"].has("opus_tags_get_track_gain", "cdecl"):
    opus_tags_get_track_gain = _libs["opusfile"].get("opus_tags_get_track_gain", "cdecl")
    opus_tags_get_track_gain.argtypes = [POINTER(OpusTags), POINTER(c_int)]
    opus_tags_get_track_gain.restype = c_int

# /usr/include/opus/opusfile.h: 600
if _libs["opusfile"].has("opus_tags_clear", "cdecl"):
    opus_tags_clear = _libs["opusfile"].get("opus_tags_clear", "cdecl")
    opus_tags_clear.argtypes = [POINTER(OpusTags)]
    opus_tags_clear.restype = None

# /usr/include/opus/opusfile.h: 611
if _libs["opusfile"].has("opus_tagcompare", "cdecl"):
    opus_tagcompare = _libs["opusfile"].get("opus_tagcompare", "cdecl")
    opus_tagcompare.argtypes = [String, String]
    opus_tagcompare.restype = c_int

# /usr/include/opus/opusfile.h: 626
if _libs["opusfile"].has("opus_tagncompare", "cdecl"):
    opus_tagncompare = _libs["opusfile"].get("opus_tagncompare", "cdecl")
    opus_tagncompare.argtypes = [String, c_int, String]
    opus_tagncompare.restype = c_int

# /usr/include/opus/opusfile.h: 658
if _libs["opusfile"].has("opus_picture_tag_parse", "cdecl"):
    opus_picture_tag_parse = _libs["opusfile"].get("opus_picture_tag_parse", "cdecl")
    opus_picture_tag_parse.argtypes = [POINTER(OpusPictureTag), String]
    opus_picture_tag_parse.restype = c_int

# /usr/include/opus/opusfile.h: 665
if _libs["opusfile"].has("opus_picture_tag_init", "cdecl"):
    opus_picture_tag_init = _libs["opusfile"].get("opus_picture_tag_init", "cdecl")
    opus_picture_tag_init.argtypes = [POINTER(OpusPictureTag)]
    opus_picture_tag_init.restype = None

# /usr/include/opus/opusfile.h: 672
if _libs["opusfile"].has("opus_picture_tag_clear", "cdecl"):
    opus_picture_tag_clear = _libs["opusfile"].get("opus_picture_tag_clear", "cdecl")
    opus_picture_tag_clear.argtypes = [POINTER(OpusPictureTag)]
    opus_picture_tag_clear.restype = None

struct_OpusServerInfo.__slots__ = [
    'name',
    'description',
    'genre',
    'url',
    'server',
    'content_type',
    'bitrate_kbps',
    'is_public',
    'is_ssl',
]
struct_OpusServerInfo._fields_ = [
    ('name', String),
    ('description', String),
    ('genre', String),
    ('url', String),
    ('server', String),
    ('content_type', String),
    ('bitrate_kbps', opus_int32),
    ('is_public', c_int),
    ('is_ssl', c_int),
]

# /usr/include/opus/opusfile.h: 756
for _lib in _libs.values():
    if not _lib.has("opus_server_info_init", "cdecl"):
        continue
    opus_server_info_init = _lib.get("opus_server_info_init", "cdecl")
    opus_server_info_init.argtypes = [POINTER(OpusServerInfo)]
    opus_server_info_init.restype = None
    break

# /usr/include/opus/opusfile.h: 764
for _lib in _libs.values():
    if not _lib.has("opus_server_info_clear", "cdecl"):
        continue
    opus_server_info_clear = _lib.get("opus_server_info_clear", "cdecl")
    opus_server_info_clear.argtypes = [POINTER(OpusServerInfo)]
    opus_server_info_clear.restype = None
    break

op_read_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_ubyte), c_int)# /usr/include/opus/opusfile.h: 869

op_seek_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), opus_int64, c_int)# /usr/include/opus/opusfile.h: 880

op_tell_func = CFUNCTYPE(UNCHECKED(opus_int64), POINTER(None))# /usr/include/opus/opusfile.h: 884

op_close_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(None))# /usr/include/opus/opusfile.h: 890

struct_OpusFileCallbacks.__slots__ = [
    'read',
    'seek',
    'tell',
    'close',
]
struct_OpusFileCallbacks._fields_ = [
    ('read', op_read_func),
    ('seek', op_seek_func),
    ('tell', op_tell_func),
    ('close', op_close_func),
]

# /usr/include/opus/opusfile.h: 933
if _libs["opusfile"].has("op_fopen", "cdecl"):
    op_fopen = _libs["opusfile"].get("op_fopen", "cdecl")
    op_fopen.argtypes = [POINTER(OpusFileCallbacks), String, String]
    op_fopen.restype = POINTER(c_ubyte)
    op_fopen.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/opus/opusfile.h: 950
if _libs["opusfile"].has("op_fdopen", "cdecl"):
    op_fdopen = _libs["opusfile"].get("op_fdopen", "cdecl")
    op_fdopen.argtypes = [POINTER(OpusFileCallbacks), c_int, String]
    op_fdopen.restype = POINTER(c_ubyte)
    op_fdopen.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/opus/opusfile.h: 972
if _libs["opusfile"].has("op_freopen", "cdecl"):
    op_freopen = _libs["opusfile"].get("op_freopen", "cdecl")
    op_freopen.argtypes = [POINTER(OpusFileCallbacks), String, String, POINTER(None)]
    op_freopen.restype = POINTER(c_ubyte)
    op_freopen.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/opus/opusfile.h: 986
if _libs["opusfile"].has("op_mem_stream_create", "cdecl"):
    op_mem_stream_create = _libs["opusfile"].get("op_mem_stream_create", "cdecl")
    op_mem_stream_create.argtypes = [POINTER(OpusFileCallbacks), POINTER(c_ubyte), c_size_t]
    op_mem_stream_create.restype = POINTER(c_ubyte)
    op_mem_stream_create.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/opus/opusfile.h: 1012
for _lib in _libs.values():
    if not _lib.has("op_url_stream_vcreate", "cdecl"):
        continue
    op_url_stream_vcreate = _lib.get("op_url_stream_vcreate", "cdecl")
    op_url_stream_vcreate.argtypes = [POINTER(OpusFileCallbacks), String, c_void_p]
    op_url_stream_vcreate.restype = POINTER(c_ubyte)
    op_url_stream_vcreate.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/opus/opusfile.h: 1034
for _lib in _libs.values():
    if _lib.has("op_url_stream_create", "cdecl"):
        _func = _lib.get("op_url_stream_create", "cdecl")
        _restype = POINTER(c_ubyte)
        _errcheck = lambda v,*a : cast(v, c_void_p)
        _argtypes = [POINTER(OpusFileCallbacks), String]
        op_url_stream_create = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/opus/opusfile.h: 1080
if _libs["opusfile"].has("op_test", "cdecl"):
    op_test = _libs["opusfile"].get("op_test", "cdecl")
    op_test.argtypes = [POINTER(OpusHead), POINTER(c_ubyte), c_size_t]
    op_test.restype = c_int

# /usr/include/opus/opusfile.h: 1092
if _libs["opusfile"].has("op_open_file", "cdecl"):
    op_open_file = _libs["opusfile"].get("op_open_file", "cdecl")
    op_open_file.argtypes = [String, POINTER(c_int)]
    op_open_file.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1103
if _libs["opusfile"].has("op_open_memory", "cdecl"):
    op_open_memory = _libs["opusfile"].get("op_open_memory", "cdecl")
    op_open_memory.argtypes = [POINTER(c_ubyte), c_size_t, POINTER(c_int)]
    op_open_memory.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1132
for _lib in _libs.values():
    if not _lib.has("op_vopen_url", "cdecl"):
        continue
    op_vopen_url = _lib.get("op_vopen_url", "cdecl")
    op_vopen_url.argtypes = [String, POINTER(c_int), c_void_p]
    op_vopen_url.restype = POINTER(OggOpusFile)
    break

# /usr/include/opus/opusfile.h: 1154
for _lib in _libs.values():
    if _lib.has("op_open_url", "cdecl"):
        _func = _lib.get("op_open_url", "cdecl")
        _restype = POINTER(OggOpusFile)
        _errcheck = None
        _argtypes = [String, POINTER(c_int)]
        op_open_url = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/opus/opusfile.h: 1236
if _libs["opusfile"].has("op_open_callbacks", "cdecl"):
    op_open_callbacks = _libs["opusfile"].get("op_open_callbacks", "cdecl")
    op_open_callbacks.argtypes = [POINTER(None), POINTER(OpusFileCallbacks), POINTER(c_ubyte), c_size_t, POINTER(c_int)]
    op_open_callbacks.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1250
if _libs["opusfile"].has("op_test_file", "cdecl"):
    op_test_file = _libs["opusfile"].get("op_test_file", "cdecl")
    op_test_file.argtypes = [String, POINTER(c_int)]
    op_test_file.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1262
if _libs["opusfile"].has("op_test_memory", "cdecl"):
    op_test_memory = _libs["opusfile"].get("op_test_memory", "cdecl")
    op_test_memory.argtypes = [POINTER(c_ubyte), c_size_t, POINTER(c_int)]
    op_test_memory.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1293
for _lib in _libs.values():
    if not _lib.has("op_vtest_url", "cdecl"):
        continue
    op_vtest_url = _lib.get("op_vtest_url", "cdecl")
    op_vtest_url.argtypes = [String, POINTER(c_int), c_void_p]
    op_vtest_url.restype = POINTER(OggOpusFile)
    break

# /usr/include/opus/opusfile.h: 1317
for _lib in _libs.values():
    if _lib.has("op_test_url", "cdecl"):
        _func = _lib.get("op_test_url", "cdecl")
        _restype = POINTER(OggOpusFile)
        _errcheck = None
        _argtypes = [String, POINTER(c_int)]
        op_test_url = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/opus/opusfile.h: 1385
if _libs["opusfile"].has("op_test_callbacks", "cdecl"):
    op_test_callbacks = _libs["opusfile"].get("op_test_callbacks", "cdecl")
    op_test_callbacks.argtypes = [POINTER(None), POINTER(OpusFileCallbacks), POINTER(c_ubyte), c_size_t, POINTER(c_int)]
    op_test_callbacks.restype = POINTER(OggOpusFile)

# /usr/include/opus/opusfile.h: 1415
if _libs["opusfile"].has("op_test_open", "cdecl"):
    op_test_open = _libs["opusfile"].get("op_test_open", "cdecl")
    op_test_open.argtypes = [POINTER(OggOpusFile)]
    op_test_open.restype = c_int

# /usr/include/opus/opusfile.h: 1419
if _libs["opusfile"].has("op_free", "cdecl"):
    op_free = _libs["opusfile"].get("op_free", "cdecl")
    op_free.argtypes = [POINTER(OggOpusFile)]
    op_free.restype = None

# /usr/include/opus/opusfile.h: 1456
if _libs["opusfile"].has("op_seekable", "cdecl"):
    op_seekable = _libs["opusfile"].get("op_seekable", "cdecl")
    op_seekable.argtypes = [POINTER(OggOpusFile)]
    op_seekable.restype = c_int

# /usr/include/opus/opusfile.h: 1466
if _libs["opusfile"].has("op_link_count", "cdecl"):
    op_link_count = _libs["opusfile"].get("op_link_count", "cdecl")
    op_link_count.argtypes = [POINTER(OggOpusFile)]
    op_link_count.restype = c_int

# /usr/include/opus/opusfile.h: 1481
if _libs["opusfile"].has("op_serialno", "cdecl"):
    op_serialno = _libs["opusfile"].get("op_serialno", "cdecl")
    op_serialno.argtypes = [POINTER(OggOpusFile), c_int]
    op_serialno.restype = opus_uint32

# /usr/include/opus/opusfile.h: 1498
if _libs["opusfile"].has("op_channel_count", "cdecl"):
    op_channel_count = _libs["opusfile"].get("op_channel_count", "cdecl")
    op_channel_count.argtypes = [POINTER(OggOpusFile), c_int]
    op_channel_count.restype = c_int

# /usr/include/opus/opusfile.h: 1520
if _libs["opusfile"].has("op_raw_total", "cdecl"):
    op_raw_total = _libs["opusfile"].get("op_raw_total", "cdecl")
    op_raw_total.argtypes = [POINTER(OggOpusFile), c_int]
    op_raw_total.restype = opus_int64

# /usr/include/opus/opusfile.h: 1538
if _libs["opusfile"].has("op_pcm_total", "cdecl"):
    op_pcm_total = _libs["opusfile"].get("op_pcm_total", "cdecl")
    op_pcm_total.argtypes = [POINTER(OggOpusFile), c_int]
    op_pcm_total.restype = ogg_int64_t

# /usr/include/opus/opusfile.h: 1554
if _libs["opusfile"].has("op_head", "cdecl"):
    op_head = _libs["opusfile"].get("op_head", "cdecl")
    op_head.argtypes = [POINTER(OggOpusFile), c_int]
    op_head.restype = POINTER(OpusHead)

# /usr/include/opus/opusfile.h: 1572
if _libs["opusfile"].has("op_tags", "cdecl"):
    op_tags = _libs["opusfile"].get("op_tags", "cdecl")
    op_tags.argtypes = [POINTER(OggOpusFile), c_int]
    op_tags.restype = POINTER(OpusTags)

# /usr/include/opus/opusfile.h: 1589
if _libs["opusfile"].has("op_current_link", "cdecl"):
    op_current_link = _libs["opusfile"].get("op_current_link", "cdecl")
    op_current_link.argtypes = [POINTER(OggOpusFile)]
    op_current_link.restype = c_int

# /usr/include/opus/opusfile.h: 1611
if _libs["opusfile"].has("op_bitrate", "cdecl"):
    op_bitrate = _libs["opusfile"].get("op_bitrate", "cdecl")
    op_bitrate.argtypes = [POINTER(OggOpusFile), c_int]
    op_bitrate.restype = opus_int32

# /usr/include/opus/opusfile.h: 1624
if _libs["opusfile"].has("op_bitrate_instant", "cdecl"):
    op_bitrate_instant = _libs["opusfile"].get("op_bitrate_instant", "cdecl")
    op_bitrate_instant.argtypes = [POINTER(OggOpusFile)]
    op_bitrate_instant.restype = opus_int32

# /usr/include/opus/opusfile.h: 1630
if _libs["opusfile"].has("op_raw_tell", "cdecl"):
    op_raw_tell = _libs["opusfile"].get("op_raw_tell", "cdecl")
    op_raw_tell.argtypes = [POINTER(OggOpusFile)]
    op_raw_tell.restype = opus_int64

# /usr/include/opus/opusfile.h: 1639
if _libs["opusfile"].has("op_pcm_tell", "cdecl"):
    op_pcm_tell = _libs["opusfile"].get("op_pcm_tell", "cdecl")
    op_pcm_tell.argtypes = [POINTER(OggOpusFile)]
    op_pcm_tell.restype = ogg_int64_t

# /usr/include/opus/opusfile.h: 1687
if _libs["opusfile"].has("op_raw_seek", "cdecl"):
    op_raw_seek = _libs["opusfile"].get("op_raw_seek", "cdecl")
    op_raw_seek.argtypes = [POINTER(OggOpusFile), opus_int64]
    op_raw_seek.restype = c_int

# /usr/include/opus/opusfile.h: 1703
if _libs["opusfile"].has("op_pcm_seek", "cdecl"):
    op_pcm_seek = _libs["opusfile"].get("op_pcm_seek", "cdecl")
    op_pcm_seek.argtypes = [POINTER(OggOpusFile), ogg_int64_t]
    op_pcm_seek.restype = c_int

op_decode_cb_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(OpusMSDecoder), POINTER(None), POINTER(ogg_packet), c_int, c_int, c_int, c_int)# /usr/include/opus/opusfile.h: 1791

# /usr/include/opus/opusfile.h: 1815
if _libs["opusfile"].has("op_set_decode_callback", "cdecl"):
    op_set_decode_callback = _libs["opusfile"].get("op_set_decode_callback", "cdecl")
    op_set_decode_callback.argtypes = [POINTER(OggOpusFile), op_decode_cb_func, POINTER(None)]
    op_set_decode_callback.restype = None

# /usr/include/opus/opusfile.h: 1852
if _libs["opusfile"].has("op_set_gain_offset", "cdecl"):
    op_set_gain_offset = _libs["opusfile"].get("op_set_gain_offset", "cdecl")
    op_set_gain_offset.argtypes = [POINTER(OggOpusFile), c_int, opus_int32]
    op_set_gain_offset.restype = c_int

# /usr/include/opus/opusfile.h: 1865
if _libs["opusfile"].has("op_set_dither_enabled", "cdecl"):
    op_set_dither_enabled = _libs["opusfile"].get("op_set_dither_enabled", "cdecl")
    op_set_dither_enabled.argtypes = [POINTER(OggOpusFile), c_int]
    op_set_dither_enabled.restype = None

# /usr/include/opus/opusfile.h: 1947
if _libs["opusfile"].has("op_read", "cdecl"):
    op_read = _libs["opusfile"].get("op_read", "cdecl")
    op_read.argtypes = [POINTER(OggOpusFile), POINTER(opus_int16), c_int, POINTER(c_int)]
    op_read.restype = c_int

# /usr/include/opus/opusfile.h: 2028
if _libs["opusfile"].has("op_read_float", "cdecl"):
    op_read_float = _libs["opusfile"].get("op_read_float", "cdecl")
    op_read_float.argtypes = [POINTER(OggOpusFile), POINTER(c_float), c_int, POINTER(c_int)]
    op_read_float.restype = c_int

# /usr/include/opus/opusfile.h: 2089
if _libs["opusfile"].has("op_read_stereo", "cdecl"):
    op_read_stereo = _libs["opusfile"].get("op_read_stereo", "cdecl")
    op_read_stereo.argtypes = [POINTER(OggOpusFile), POINTER(opus_int16), c_int]
    op_read_stereo.restype = c_int

# /usr/include/opus/opusfile.h: 2150
if _libs["opusfile"].has("op_read_float_stereo", "cdecl"):
    op_read_float_stereo = _libs["opusfile"].get("op_read_float_stereo", "cdecl")
    op_read_float_stereo.argtypes = [POINTER(OggOpusFile), POINTER(c_float), c_int]
    op_read_float_stereo.restype = c_int

# /usr/include/opus/opus_defines.h: 46
try:
    OPUS_OK = 0
except:
    pass

# /usr/include/opus/opus_defines.h: 48
try:
    OPUS_BAD_ARG = (-1)
except:
    pass

# /usr/include/opus/opus_defines.h: 50
try:
    OPUS_BUFFER_TOO_SMALL = (-2)
except:
    pass

# /usr/include/opus/opus_defines.h: 52
try:
    OPUS_INTERNAL_ERROR = (-3)
except:
    pass

# /usr/include/opus/opus_defines.h: 54
try:
    OPUS_INVALID_PACKET = (-4)
except:
    pass

# /usr/include/opus/opus_defines.h: 56
try:
    OPUS_UNIMPLEMENTED = (-5)
except:
    pass

# /usr/include/opus/opus_defines.h: 58
try:
    OPUS_INVALID_STATE = (-6)
except:
    pass

# /usr/include/opus/opus_defines.h: 60
try:
    OPUS_ALLOC_FAIL = (-7)
except:
    pass

# /usr/include/opus/opus_defines.h: 85
def OPUS_GNUC_PREREQ(_maj, _min):
    return 0

# /usr/include/opus/opus_defines.h: 130
try:
    OPUS_SET_APPLICATION_REQUEST = 4000
except:
    pass

# /usr/include/opus/opus_defines.h: 131
try:
    OPUS_GET_APPLICATION_REQUEST = 4001
except:
    pass

# /usr/include/opus/opus_defines.h: 132
try:
    OPUS_SET_BITRATE_REQUEST = 4002
except:
    pass

# /usr/include/opus/opus_defines.h: 133
try:
    OPUS_GET_BITRATE_REQUEST = 4003
except:
    pass

# /usr/include/opus/opus_defines.h: 134
try:
    OPUS_SET_MAX_BANDWIDTH_REQUEST = 4004
except:
    pass

# /usr/include/opus/opus_defines.h: 135
try:
    OPUS_GET_MAX_BANDWIDTH_REQUEST = 4005
except:
    pass

# /usr/include/opus/opus_defines.h: 136
try:
    OPUS_SET_VBR_REQUEST = 4006
except:
    pass

# /usr/include/opus/opus_defines.h: 137
try:
    OPUS_GET_VBR_REQUEST = 4007
except:
    pass

# /usr/include/opus/opus_defines.h: 138
try:
    OPUS_SET_BANDWIDTH_REQUEST = 4008
except:
    pass

# /usr/include/opus/opus_defines.h: 139
try:
    OPUS_GET_BANDWIDTH_REQUEST = 4009
except:
    pass

# /usr/include/opus/opus_defines.h: 140
try:
    OPUS_SET_COMPLEXITY_REQUEST = 4010
except:
    pass

# /usr/include/opus/opus_defines.h: 141
try:
    OPUS_GET_COMPLEXITY_REQUEST = 4011
except:
    pass

# /usr/include/opus/opus_defines.h: 142
try:
    OPUS_SET_INBAND_FEC_REQUEST = 4012
except:
    pass

# /usr/include/opus/opus_defines.h: 143
try:
    OPUS_GET_INBAND_FEC_REQUEST = 4013
except:
    pass

# /usr/include/opus/opus_defines.h: 144
try:
    OPUS_SET_PACKET_LOSS_PERC_REQUEST = 4014
except:
    pass

# /usr/include/opus/opus_defines.h: 145
try:
    OPUS_GET_PACKET_LOSS_PERC_REQUEST = 4015
except:
    pass

# /usr/include/opus/opus_defines.h: 146
try:
    OPUS_SET_DTX_REQUEST = 4016
except:
    pass

# /usr/include/opus/opus_defines.h: 147
try:
    OPUS_GET_DTX_REQUEST = 4017
except:
    pass

# /usr/include/opus/opus_defines.h: 148
try:
    OPUS_SET_VBR_CONSTRAINT_REQUEST = 4020
except:
    pass

# /usr/include/opus/opus_defines.h: 149
try:
    OPUS_GET_VBR_CONSTRAINT_REQUEST = 4021
except:
    pass

# /usr/include/opus/opus_defines.h: 150
try:
    OPUS_SET_FORCE_CHANNELS_REQUEST = 4022
except:
    pass

# /usr/include/opus/opus_defines.h: 151
try:
    OPUS_GET_FORCE_CHANNELS_REQUEST = 4023
except:
    pass

# /usr/include/opus/opus_defines.h: 152
try:
    OPUS_SET_SIGNAL_REQUEST = 4024
except:
    pass

# /usr/include/opus/opus_defines.h: 153
try:
    OPUS_GET_SIGNAL_REQUEST = 4025
except:
    pass

# /usr/include/opus/opus_defines.h: 154
try:
    OPUS_GET_LOOKAHEAD_REQUEST = 4027
except:
    pass

# /usr/include/opus/opus_defines.h: 156
try:
    OPUS_GET_SAMPLE_RATE_REQUEST = 4029
except:
    pass

# /usr/include/opus/opus_defines.h: 157
try:
    OPUS_GET_FINAL_RANGE_REQUEST = 4031
except:
    pass

# /usr/include/opus/opus_defines.h: 158
try:
    OPUS_GET_PITCH_REQUEST = 4033
except:
    pass

# /usr/include/opus/opus_defines.h: 159
try:
    OPUS_SET_GAIN_REQUEST = 4034
except:
    pass

# /usr/include/opus/opus_defines.h: 160
try:
    OPUS_GET_GAIN_REQUEST = 4045
except:
    pass

# /usr/include/opus/opus_defines.h: 161
try:
    OPUS_SET_LSB_DEPTH_REQUEST = 4036
except:
    pass

# /usr/include/opus/opus_defines.h: 162
try:
    OPUS_GET_LSB_DEPTH_REQUEST = 4037
except:
    pass

# /usr/include/opus/opus_defines.h: 163
try:
    OPUS_GET_LAST_PACKET_DURATION_REQUEST = 4039
except:
    pass

# /usr/include/opus/opus_defines.h: 164
try:
    OPUS_SET_EXPERT_FRAME_DURATION_REQUEST = 4040
except:
    pass

# /usr/include/opus/opus_defines.h: 165
try:
    OPUS_GET_EXPERT_FRAME_DURATION_REQUEST = 4041
except:
    pass

# /usr/include/opus/opus_defines.h: 166
try:
    OPUS_SET_PREDICTION_DISABLED_REQUEST = 4042
except:
    pass

# /usr/include/opus/opus_defines.h: 167
try:
    OPUS_GET_PREDICTION_DISABLED_REQUEST = 4043
except:
    pass

# /usr/include/opus/opus_defines.h: 169
try:
    OPUS_SET_PHASE_INVERSION_DISABLED_REQUEST = 4046
except:
    pass

# /usr/include/opus/opus_defines.h: 170
try:
    OPUS_GET_PHASE_INVERSION_DISABLED_REQUEST = 4047
except:
    pass

# /usr/include/opus/opus_defines.h: 171
try:
    OPUS_GET_IN_DTX_REQUEST = 4049
except:
    pass

# /usr/include/opus/opus_defines.h: 177
def __opus_check_int(x):
    return (ord_if_char((x == (opus_int32 (ord_if_char(0))).value))).value

# /usr/include/opus/opus_defines.h: 178
def __opus_check_int_ptr(ptr):
    return (ptr + (ptr - cast(ptr, POINTER(opus_int32))))

# /usr/include/opus/opus_defines.h: 179
def __opus_check_uint_ptr(ptr):
    return (ptr + (ptr - cast(ptr, POINTER(opus_uint32))))

# /usr/include/opus/opus_defines.h: 188
try:
    OPUS_AUTO = (-1000)
except:
    pass

# /usr/include/opus/opus_defines.h: 189
try:
    OPUS_BITRATE_MAX = (-1)
except:
    pass

# /usr/include/opus/opus_defines.h: 193
try:
    OPUS_APPLICATION_VOIP = 2048
except:
    pass

# /usr/include/opus/opus_defines.h: 196
try:
    OPUS_APPLICATION_AUDIO = 2049
except:
    pass

# /usr/include/opus/opus_defines.h: 199
try:
    OPUS_APPLICATION_RESTRICTED_LOWDELAY = 2051
except:
    pass

# /usr/include/opus/opus_defines.h: 201
try:
    OPUS_SIGNAL_VOICE = 3001
except:
    pass

# /usr/include/opus/opus_defines.h: 202
try:
    OPUS_SIGNAL_MUSIC = 3002
except:
    pass

# /usr/include/opus/opus_defines.h: 203
try:
    OPUS_BANDWIDTH_NARROWBAND = 1101
except:
    pass

# /usr/include/opus/opus_defines.h: 204
try:
    OPUS_BANDWIDTH_MEDIUMBAND = 1102
except:
    pass

# /usr/include/opus/opus_defines.h: 205
try:
    OPUS_BANDWIDTH_WIDEBAND = 1103
except:
    pass

# /usr/include/opus/opus_defines.h: 206
try:
    OPUS_BANDWIDTH_SUPERWIDEBAND = 1104
except:
    pass

# /usr/include/opus/opus_defines.h: 207
try:
    OPUS_BANDWIDTH_FULLBAND = 1105
except:
    pass

# /usr/include/opus/opus_defines.h: 209
try:
    OPUS_FRAMESIZE_ARG = 5000
except:
    pass

# /usr/include/opus/opus_defines.h: 210
try:
    OPUS_FRAMESIZE_2_5_MS = 5001
except:
    pass

# /usr/include/opus/opus_defines.h: 211
try:
    OPUS_FRAMESIZE_5_MS = 5002
except:
    pass

# /usr/include/opus/opus_defines.h: 212
try:
    OPUS_FRAMESIZE_10_MS = 5003
except:
    pass

# /usr/include/opus/opus_defines.h: 213
try:
    OPUS_FRAMESIZE_20_MS = 5004
except:
    pass

# /usr/include/opus/opus_defines.h: 214
try:
    OPUS_FRAMESIZE_40_MS = 5005
except:
    pass

# /usr/include/opus/opus_defines.h: 215
try:
    OPUS_FRAMESIZE_60_MS = 5006
except:
    pass

# /usr/include/opus/opus_defines.h: 216
try:
    OPUS_FRAMESIZE_80_MS = 5007
except:
    pass

# /usr/include/opus/opus_defines.h: 217
try:
    OPUS_FRAMESIZE_100_MS = 5008
except:
    pass

# /usr/include/opus/opus_defines.h: 218
try:
    OPUS_FRAMESIZE_120_MS = 5009
except:
    pass

# /usr/include/opus/opus_defines.h: 662
try:
    OPUS_RESET_STATE = 4028
except:
    pass

# /usr/include/opus/opusfile.h: 18
try:
    _opusfile_h = 1
except:
    pass

# /usr/include/opus/opusfile.h: 120
def OP_GNUC_PREREQ(_maj, _min):
    return 0

# /usr/include/opus/opusfile.h: 160
try:
    OP_FALSE = (-1)
except:
    pass

# /usr/include/opus/opusfile.h: 162
try:
    OP_EOF = (-2)
except:
    pass

# /usr/include/opus/opusfile.h: 165
try:
    OP_HOLE = (-3)
except:
    pass

# /usr/include/opus/opusfile.h: 168
try:
    OP_EREAD = (-128)
except:
    pass

# /usr/include/opus/opusfile.h: 172
try:
    OP_EFAULT = (-129)
except:
    pass

# /usr/include/opus/opusfile.h: 175
try:
    OP_EIMPL = (-130)
except:
    pass

# /usr/include/opus/opusfile.h: 177
try:
    OP_EINVAL = (-131)
except:
    pass

# /usr/include/opus/opusfile.h: 182
try:
    OP_ENOTFORMAT = (-132)
except:
    pass

# /usr/include/opus/opusfile.h: 185
try:
    OP_EBADHEADER = (-133)
except:
    pass

# /usr/include/opus/opusfile.h: 187
try:
    OP_EVERSION = (-134)
except:
    pass

# /usr/include/opus/opusfile.h: 189
try:
    OP_ENOTAUDIO = (-135)
except:
    pass

# /usr/include/opus/opusfile.h: 193
try:
    OP_EBADPACKET = (-136)
except:
    pass

# /usr/include/opus/opusfile.h: 197
try:
    OP_EBADLINK = (-137)
except:
    pass

# /usr/include/opus/opusfile.h: 199
try:
    OP_ENOSEEK = (-138)
except:
    pass

# /usr/include/opus/opusfile.h: 201
try:
    OP_EBADTIMESTAMP = (-139)
except:
    pass

# /usr/include/opus/opusfile.h: 210
try:
    OPUS_CHANNEL_COUNT_MAX = 255
except:
    pass

# /usr/include/opus/opusfile.h: 318
try:
    OP_PIC_FORMAT_UNKNOWN = (-1)
except:
    pass

# /usr/include/opus/opusfile.h: 320
try:
    OP_PIC_FORMAT_URL = 0
except:
    pass

# /usr/include/opus/opusfile.h: 322
try:
    OP_PIC_FORMAT_JPEG = 1
except:
    pass

# /usr/include/opus/opusfile.h: 324
try:
    OP_PIC_FORMAT_PNG = 2
except:
    pass

# /usr/include/opus/opusfile.h: 326
try:
    OP_PIC_FORMAT_GIF = 3
except:
    pass

# /usr/include/opus/opusfile.h: 694
try:
    OP_SSL_SKIP_CERTIFICATE_CHECK_REQUEST = 6464
except:
    pass

# /usr/include/opus/opusfile.h: 695
try:
    OP_HTTP_PROXY_HOST_REQUEST = 6528
except:
    pass

# /usr/include/opus/opusfile.h: 696
try:
    OP_HTTP_PROXY_PORT_REQUEST = 6592
except:
    pass

# /usr/include/opus/opusfile.h: 697
try:
    OP_HTTP_PROXY_USER_REQUEST = 6656
except:
    pass

# /usr/include/opus/opusfile.h: 698
try:
    OP_HTTP_PROXY_PASS_REQUEST = 6720
except:
    pass

# /usr/include/opus/opusfile.h: 699
try:
    OP_GET_SERVER_INFO_REQUEST = 6784
except:
    pass

# /usr/include/opus/opusfile.h: 701
def OP_URL_OPT(_request):
    return (String (ord_if_char(_request))).value

# /usr/include/opus/opusfile.h: 705
def OP_CHECK_INT(_x):
    return (ord_if_char((_x == (opus_int32 (ord_if_char(0))).value))).value

# /usr/include/opus/opusfile.h: 706
def OP_CHECK_CONST_CHAR_PTR(_x):
    return (_x + (_x - (String (ord_if_char(_x))).value))

# /usr/include/opus/opusfile.h: 707
def OP_CHECK_SERVER_INFO_PTR(_x):
    return (_x + (_x - cast(_x, POINTER(OpusServerInfo))))

# /usr/include/opus/opusfile.h: 1751
try:
    OP_DEC_FORMAT_SHORT = 7008
except:
    pass

# /usr/include/opus/opusfile.h: 1754
try:
    OP_DEC_FORMAT_FLOAT = 7040
except:
    pass

# /usr/include/opus/opusfile.h: 1758
try:
    OP_DEC_USE_DEFAULT = 6720
except:
    pass

# /usr/include/opus/opusfile.h: 1821
try:
    OP_HEADER_GAIN = 0
except:
    pass

# /usr/include/opus/opusfile.h: 1825
try:
    OP_ALBUM_GAIN = 3007
except:
    pass

# /usr/include/opus/opusfile.h: 1829
try:
    OP_TRACK_GAIN = 3008
except:
    pass

# /usr/include/opus/opusfile.h: 1833
try:
    OP_ABSOLUTE_GAIN = 3009
except:
    pass

OpusEncoder = struct_OpusEncoder# /usr/include/opus/opus.h: 164

OpusDecoder = struct_OpusDecoder# /usr/include/opus/opus.h: 399

OpusRepacketizer = struct_OpusRepacketizer# /usr/include/opus/opus.h: 754

OpusHead = struct_OpusHead# /usr/include/opus/opusfile.h: 215

OpusTags = struct_OpusTags# /usr/include/opus/opusfile.h: 301

OpusPictureTag = struct_OpusPictureTag# /usr/include/opus/opusfile.h: 331

OpusServerInfo = struct_OpusServerInfo# /usr/include/opus/opusfile.h: 712

OpusFileCallbacks = struct_OpusFileCallbacks# /usr/include/opus/opusfile.h: 901

OggOpusFile = struct_OggOpusFile# /usr/include/opus/opusfile.h: 133

# No inserted files

# No prefix-stripping

