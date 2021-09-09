r"""Wrapper for sndfile.h


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
_libs["sndfile"] = load_library("sndfile")

# 1 libraries
# End libraries

# No modules

enum_anon_19 = c_int# /usr/include/sndfile.h: 47

SF_FORMAT_WAV = 65536# /usr/include/sndfile.h: 47

SF_FORMAT_AIFF = 131072# /usr/include/sndfile.h: 47

SF_FORMAT_AU = 196608# /usr/include/sndfile.h: 47

SF_FORMAT_RAW = 262144# /usr/include/sndfile.h: 47

SF_FORMAT_PAF = 327680# /usr/include/sndfile.h: 47

SF_FORMAT_SVX = 393216# /usr/include/sndfile.h: 47

SF_FORMAT_NIST = 458752# /usr/include/sndfile.h: 47

SF_FORMAT_VOC = 524288# /usr/include/sndfile.h: 47

SF_FORMAT_IRCAM = 655360# /usr/include/sndfile.h: 47

SF_FORMAT_W64 = 720896# /usr/include/sndfile.h: 47

SF_FORMAT_MAT4 = 786432# /usr/include/sndfile.h: 47

SF_FORMAT_MAT5 = 851968# /usr/include/sndfile.h: 47

SF_FORMAT_PVF = 917504# /usr/include/sndfile.h: 47

SF_FORMAT_XI = 983040# /usr/include/sndfile.h: 47

SF_FORMAT_HTK = 1048576# /usr/include/sndfile.h: 47

SF_FORMAT_SDS = 1114112# /usr/include/sndfile.h: 47

SF_FORMAT_AVR = 1179648# /usr/include/sndfile.h: 47

SF_FORMAT_WAVEX = 1245184# /usr/include/sndfile.h: 47

SF_FORMAT_SD2 = 1441792# /usr/include/sndfile.h: 47

SF_FORMAT_FLAC = 1507328# /usr/include/sndfile.h: 47

SF_FORMAT_CAF = 1572864# /usr/include/sndfile.h: 47

SF_FORMAT_WVE = 1638400# /usr/include/sndfile.h: 47

SF_FORMAT_OGG = 2097152# /usr/include/sndfile.h: 47

SF_FORMAT_MPC2K = 2162688# /usr/include/sndfile.h: 47

SF_FORMAT_RF64 = 2228224# /usr/include/sndfile.h: 47

SF_FORMAT_PCM_S8 = 1# /usr/include/sndfile.h: 47

SF_FORMAT_PCM_16 = 2# /usr/include/sndfile.h: 47

SF_FORMAT_PCM_24 = 3# /usr/include/sndfile.h: 47

SF_FORMAT_PCM_32 = 4# /usr/include/sndfile.h: 47

SF_FORMAT_PCM_U8 = 5# /usr/include/sndfile.h: 47

SF_FORMAT_FLOAT = 6# /usr/include/sndfile.h: 47

SF_FORMAT_DOUBLE = 7# /usr/include/sndfile.h: 47

SF_FORMAT_ULAW = 16# /usr/include/sndfile.h: 47

SF_FORMAT_ALAW = 17# /usr/include/sndfile.h: 47

SF_FORMAT_IMA_ADPCM = 18# /usr/include/sndfile.h: 47

SF_FORMAT_MS_ADPCM = 19# /usr/include/sndfile.h: 47

SF_FORMAT_GSM610 = 32# /usr/include/sndfile.h: 47

SF_FORMAT_VOX_ADPCM = 33# /usr/include/sndfile.h: 47

SF_FORMAT_NMS_ADPCM_16 = 34# /usr/include/sndfile.h: 47

SF_FORMAT_NMS_ADPCM_24 = 35# /usr/include/sndfile.h: 47

SF_FORMAT_NMS_ADPCM_32 = 36# /usr/include/sndfile.h: 47

SF_FORMAT_G721_32 = 48# /usr/include/sndfile.h: 47

SF_FORMAT_G723_24 = 49# /usr/include/sndfile.h: 47

SF_FORMAT_G723_40 = 50# /usr/include/sndfile.h: 47

SF_FORMAT_DWVW_12 = 64# /usr/include/sndfile.h: 47

SF_FORMAT_DWVW_16 = 65# /usr/include/sndfile.h: 47

SF_FORMAT_DWVW_24 = 66# /usr/include/sndfile.h: 47

SF_FORMAT_DWVW_N = 67# /usr/include/sndfile.h: 47

SF_FORMAT_DPCM_8 = 80# /usr/include/sndfile.h: 47

SF_FORMAT_DPCM_16 = 81# /usr/include/sndfile.h: 47

SF_FORMAT_VORBIS = 96# /usr/include/sndfile.h: 47

SF_FORMAT_OPUS = 100# /usr/include/sndfile.h: 47

SF_FORMAT_ALAC_16 = 112# /usr/include/sndfile.h: 47

SF_FORMAT_ALAC_20 = 113# /usr/include/sndfile.h: 47

SF_FORMAT_ALAC_24 = 114# /usr/include/sndfile.h: 47

SF_FORMAT_ALAC_32 = 115# /usr/include/sndfile.h: 47

SF_ENDIAN_FILE = 0# /usr/include/sndfile.h: 47

SF_ENDIAN_LITTLE = 268435456# /usr/include/sndfile.h: 47

SF_ENDIAN_BIG = 536870912# /usr/include/sndfile.h: 47

SF_ENDIAN_CPU = 805306368# /usr/include/sndfile.h: 47

SF_FORMAT_SUBMASK = 65535# /usr/include/sndfile.h: 47

SF_FORMAT_TYPEMASK = 268369920# /usr/include/sndfile.h: 47

SF_FORMAT_ENDMASK = 805306368# /usr/include/sndfile.h: 47

enum_anon_20 = c_int# /usr/include/sndfile.h: 137

SFC_GET_LIB_VERSION = 4096# /usr/include/sndfile.h: 137

SFC_GET_LOG_INFO = 4097# /usr/include/sndfile.h: 137

SFC_GET_CURRENT_SF_INFO = 4098# /usr/include/sndfile.h: 137

SFC_GET_NORM_DOUBLE = 4112# /usr/include/sndfile.h: 137

SFC_GET_NORM_FLOAT = 4113# /usr/include/sndfile.h: 137

SFC_SET_NORM_DOUBLE = 4114# /usr/include/sndfile.h: 137

SFC_SET_NORM_FLOAT = 4115# /usr/include/sndfile.h: 137

SFC_SET_SCALE_FLOAT_INT_READ = 4116# /usr/include/sndfile.h: 137

SFC_SET_SCALE_INT_FLOAT_WRITE = 4117# /usr/include/sndfile.h: 137

SFC_GET_SIMPLE_FORMAT_COUNT = 4128# /usr/include/sndfile.h: 137

SFC_GET_SIMPLE_FORMAT = 4129# /usr/include/sndfile.h: 137

SFC_GET_FORMAT_INFO = 4136# /usr/include/sndfile.h: 137

SFC_GET_FORMAT_MAJOR_COUNT = 4144# /usr/include/sndfile.h: 137

SFC_GET_FORMAT_MAJOR = 4145# /usr/include/sndfile.h: 137

SFC_GET_FORMAT_SUBTYPE_COUNT = 4146# /usr/include/sndfile.h: 137

SFC_GET_FORMAT_SUBTYPE = 4147# /usr/include/sndfile.h: 137

SFC_CALC_SIGNAL_MAX = 4160# /usr/include/sndfile.h: 137

SFC_CALC_NORM_SIGNAL_MAX = 4161# /usr/include/sndfile.h: 137

SFC_CALC_MAX_ALL_CHANNELS = 4162# /usr/include/sndfile.h: 137

SFC_CALC_NORM_MAX_ALL_CHANNELS = 4163# /usr/include/sndfile.h: 137

SFC_GET_SIGNAL_MAX = 4164# /usr/include/sndfile.h: 137

SFC_GET_MAX_ALL_CHANNELS = 4165# /usr/include/sndfile.h: 137

SFC_SET_ADD_PEAK_CHUNK = 4176# /usr/include/sndfile.h: 137

SFC_UPDATE_HEADER_NOW = 4192# /usr/include/sndfile.h: 137

SFC_SET_UPDATE_HEADER_AUTO = 4193# /usr/include/sndfile.h: 137

SFC_FILE_TRUNCATE = 4224# /usr/include/sndfile.h: 137

SFC_SET_RAW_START_OFFSET = 4240# /usr/include/sndfile.h: 137

SFC_SET_DITHER_ON_WRITE = 4256# /usr/include/sndfile.h: 137

SFC_SET_DITHER_ON_READ = 4257# /usr/include/sndfile.h: 137

SFC_GET_DITHER_INFO_COUNT = 4258# /usr/include/sndfile.h: 137

SFC_GET_DITHER_INFO = 4259# /usr/include/sndfile.h: 137

SFC_GET_EMBED_FILE_INFO = 4272# /usr/include/sndfile.h: 137

SFC_SET_CLIPPING = 4288# /usr/include/sndfile.h: 137

SFC_GET_CLIPPING = 4289# /usr/include/sndfile.h: 137

SFC_GET_CUE_COUNT = 4301# /usr/include/sndfile.h: 137

SFC_GET_CUE = 4302# /usr/include/sndfile.h: 137

SFC_SET_CUE = 4303# /usr/include/sndfile.h: 137

SFC_GET_INSTRUMENT = 4304# /usr/include/sndfile.h: 137

SFC_SET_INSTRUMENT = 4305# /usr/include/sndfile.h: 137

SFC_GET_LOOP_INFO = 4320# /usr/include/sndfile.h: 137

SFC_GET_BROADCAST_INFO = 4336# /usr/include/sndfile.h: 137

SFC_SET_BROADCAST_INFO = 4337# /usr/include/sndfile.h: 137

SFC_GET_CHANNEL_MAP_INFO = 4352# /usr/include/sndfile.h: 137

SFC_SET_CHANNEL_MAP_INFO = 4353# /usr/include/sndfile.h: 137

SFC_RAW_DATA_NEEDS_ENDSWAP = 4368# /usr/include/sndfile.h: 137

SFC_WAVEX_SET_AMBISONIC = 4608# /usr/include/sndfile.h: 137

SFC_WAVEX_GET_AMBISONIC = 4609# /usr/include/sndfile.h: 137

SFC_RF64_AUTO_DOWNGRADE = 4624# /usr/include/sndfile.h: 137

SFC_SET_VBR_ENCODING_QUALITY = 4864# /usr/include/sndfile.h: 137

SFC_SET_COMPRESSION_LEVEL = 4865# /usr/include/sndfile.h: 137

SFC_SET_OGG_PAGE_LATENCY_MS = 4866# /usr/include/sndfile.h: 137

SFC_SET_OGG_PAGE_LATENCY = 4867# /usr/include/sndfile.h: 137

SFC_SET_CART_INFO = 5120# /usr/include/sndfile.h: 137

SFC_GET_CART_INFO = 5121# /usr/include/sndfile.h: 137

SFC_SET_ORIGINAL_SAMPLERATE = 5376# /usr/include/sndfile.h: 137

SFC_GET_ORIGINAL_SAMPLERATE = 5377# /usr/include/sndfile.h: 137

SFC_TEST_IEEE_FLOAT_REPLACE = 24577# /usr/include/sndfile.h: 137

SFC_SET_ADD_HEADER_PAD_CHUNK = 4177# /usr/include/sndfile.h: 137

SFC_SET_ADD_DITHER_ON_WRITE = 4208# /usr/include/sndfile.h: 137

SFC_SET_ADD_DITHER_ON_READ = 4209# /usr/include/sndfile.h: 137

enum_anon_21 = c_int# /usr/include/sndfile.h: 250

SF_STR_TITLE = 1# /usr/include/sndfile.h: 250

SF_STR_COPYRIGHT = 2# /usr/include/sndfile.h: 250

SF_STR_SOFTWARE = 3# /usr/include/sndfile.h: 250

SF_STR_ARTIST = 4# /usr/include/sndfile.h: 250

SF_STR_COMMENT = 5# /usr/include/sndfile.h: 250

SF_STR_DATE = 6# /usr/include/sndfile.h: 250

SF_STR_ALBUM = 7# /usr/include/sndfile.h: 250

SF_STR_LICENSE = 8# /usr/include/sndfile.h: 250

SF_STR_TRACKNUMBER = 9# /usr/include/sndfile.h: 250

SF_STR_GENRE = 16# /usr/include/sndfile.h: 250

enum_anon_22 = c_int# /usr/include/sndfile.h: 271

SF_FALSE = 0# /usr/include/sndfile.h: 271

SF_TRUE = 1# /usr/include/sndfile.h: 271

SFM_READ = 16# /usr/include/sndfile.h: 271

SFM_WRITE = 32# /usr/include/sndfile.h: 271

SFM_RDWR = 48# /usr/include/sndfile.h: 271

SF_AMBISONIC_NONE = 64# /usr/include/sndfile.h: 271

SF_AMBISONIC_B_FORMAT = 65# /usr/include/sndfile.h: 271

enum_anon_23 = c_int# /usr/include/sndfile.h: 291

SF_ERR_NO_ERROR = 0# /usr/include/sndfile.h: 291

SF_ERR_UNRECOGNISED_FORMAT = 1# /usr/include/sndfile.h: 291

SF_ERR_SYSTEM = 2# /usr/include/sndfile.h: 291

SF_ERR_MALFORMED_FILE = 3# /usr/include/sndfile.h: 291

SF_ERR_UNSUPPORTED_ENCODING = 4# /usr/include/sndfile.h: 291

enum_anon_24 = c_int# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_INVALID = 0# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_MONO = 1# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_LEFT = (SF_CHANNEL_MAP_MONO + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_RIGHT = (SF_CHANNEL_MAP_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_CENTER = (SF_CHANNEL_MAP_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_FRONT_LEFT = (SF_CHANNEL_MAP_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_FRONT_RIGHT = (SF_CHANNEL_MAP_FRONT_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_FRONT_CENTER = (SF_CHANNEL_MAP_FRONT_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_REAR_CENTER = (SF_CHANNEL_MAP_FRONT_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_REAR_LEFT = (SF_CHANNEL_MAP_REAR_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_REAR_RIGHT = (SF_CHANNEL_MAP_REAR_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_LFE = (SF_CHANNEL_MAP_REAR_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_FRONT_LEFT_OF_CENTER = (SF_CHANNEL_MAP_LFE + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_FRONT_RIGHT_OF_CENTER = (SF_CHANNEL_MAP_FRONT_LEFT_OF_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_SIDE_LEFT = (SF_CHANNEL_MAP_FRONT_RIGHT_OF_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_SIDE_RIGHT = (SF_CHANNEL_MAP_SIDE_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_CENTER = (SF_CHANNEL_MAP_SIDE_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_FRONT_LEFT = (SF_CHANNEL_MAP_TOP_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_FRONT_RIGHT = (SF_CHANNEL_MAP_TOP_FRONT_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_FRONT_CENTER = (SF_CHANNEL_MAP_TOP_FRONT_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_REAR_LEFT = (SF_CHANNEL_MAP_TOP_FRONT_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_REAR_RIGHT = (SF_CHANNEL_MAP_TOP_REAR_LEFT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_TOP_REAR_CENTER = (SF_CHANNEL_MAP_TOP_REAR_RIGHT + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_AMBISONIC_B_W = (SF_CHANNEL_MAP_TOP_REAR_CENTER + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_AMBISONIC_B_X = (SF_CHANNEL_MAP_AMBISONIC_B_W + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_AMBISONIC_B_Y = (SF_CHANNEL_MAP_AMBISONIC_B_X + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_AMBISONIC_B_Z = (SF_CHANNEL_MAP_AMBISONIC_B_Y + 1)# /usr/include/sndfile.h: 303

SF_CHANNEL_MAP_MAX = (SF_CHANNEL_MAP_AMBISONIC_B_Z + 1)# /usr/include/sndfile.h: 303

# /usr/include/sndfile.h: 339
class struct_SNDFILE_tag(Structure):
    pass

SNDFILE = struct_SNDFILE_tag# /usr/include/sndfile.h: 339

sf_count_t = c_int64# /usr/include/sndfile.h: 348

# /usr/include/sndfile.h: 359
class struct_SF_INFO(Structure):
    pass

struct_SF_INFO.__slots__ = [
    'frames',
    'samplerate',
    'channels',
    'format',
    'sections',
    'seekable',
]
struct_SF_INFO._fields_ = [
    ('frames', sf_count_t),
    ('samplerate', c_int),
    ('channels', c_int),
    ('format', c_int),
    ('sections', c_int),
    ('seekable', c_int),
]

SF_INFO = struct_SF_INFO# /usr/include/sndfile.h: 368

# /usr/include/sndfile.h: 385
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'format',
    'name',
    'extension',
]
struct_anon_25._fields_ = [
    ('format', c_int),
    ('name', String),
    ('extension', String),
]

SF_FORMAT_INFO = struct_anon_25# /usr/include/sndfile.h: 385

enum_anon_26 = c_int# /usr/include/sndfile.h: 393

SFD_DEFAULT_LEVEL = 0# /usr/include/sndfile.h: 393

SFD_CUSTOM_LEVEL = 1073741824# /usr/include/sndfile.h: 393

SFD_NO_DITHER = 500# /usr/include/sndfile.h: 393

SFD_WHITE = 501# /usr/include/sndfile.h: 393

SFD_TRIANGULAR_PDF = 502# /usr/include/sndfile.h: 393

# /usr/include/sndfile.h: 406
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'type',
    'level',
    'name',
]
struct_anon_27._fields_ = [
    ('type', c_int),
    ('level', c_double),
    ('name', String),
]

SF_DITHER_INFO = struct_anon_27# /usr/include/sndfile.h: 406

# /usr/include/sndfile.h: 415
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'offset',
    'length',
]
struct_anon_28._fields_ = [
    ('offset', sf_count_t),
    ('length', sf_count_t),
]

SF_EMBED_FILE_INFO = struct_anon_28# /usr/include/sndfile.h: 415

# /usr/include/sndfile.h: 429
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'indx',
    'position',
    'fcc_chunk',
    'chunk_start',
    'block_start',
    'sample_offset',
    'name',
]
struct_anon_29._fields_ = [
    ('indx', c_int32),
    ('position', c_uint32),
    ('fcc_chunk', c_int32),
    ('chunk_start', c_int32),
    ('block_start', c_int32),
    ('sample_offset', c_uint32),
    ('name', c_char * int(256)),
]

SF_CUE_POINT = struct_anon_29# /usr/include/sndfile.h: 429

# /usr/include/sndfile.h: 437
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'cue_count',
    'cue_points',
]
struct_anon_30._fields_ = [
    ('cue_count', c_uint32),
    ('cue_points', SF_CUE_POINT * int(100)),
]

SF_CUES = struct_anon_30# /usr/include/sndfile.h: 437

enum_anon_31 = c_int# /usr/include/sndfile.h: 443

SF_LOOP_NONE = 800# /usr/include/sndfile.h: 443

SF_LOOP_FORWARD = (SF_LOOP_NONE + 1)# /usr/include/sndfile.h: 443

SF_LOOP_BACKWARD = (SF_LOOP_FORWARD + 1)# /usr/include/sndfile.h: 443

SF_LOOP_ALTERNATING = (SF_LOOP_BACKWARD + 1)# /usr/include/sndfile.h: 443

# /usr/include/sndfile.h: 460
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'mode',
    'start',
    'end',
    'count',
]
struct_anon_32._fields_ = [
    ('mode', c_int),
    ('start', c_uint32),
    ('end', c_uint32),
    ('count', c_uint32),
]

# /usr/include/sndfile.h: 466
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'gain',
    'basenote',
    'detune',
    'velocity_lo',
    'velocity_hi',
    'key_lo',
    'key_hi',
    'loop_count',
    'loops',
]
struct_anon_33._fields_ = [
    ('gain', c_int),
    ('basenote', c_char),
    ('detune', c_char),
    ('velocity_lo', c_char),
    ('velocity_hi', c_char),
    ('key_lo', c_char),
    ('key_hi', c_char),
    ('loop_count', c_int),
    ('loops', struct_anon_32 * int(16)),
]

SF_INSTRUMENT = struct_anon_33# /usr/include/sndfile.h: 466

# /usr/include/sndfile.h: 487
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'time_sig_num',
    'time_sig_den',
    'loop_mode',
    'num_beats',
    'bpm',
    'root_key',
    'future',
]
struct_anon_34._fields_ = [
    ('time_sig_num', c_short),
    ('time_sig_den', c_short),
    ('loop_mode', c_int),
    ('num_beats', c_int),
    ('bpm', c_float),
    ('root_key', c_int),
    ('future', c_int * int(6)),
]

SF_LOOP_INFO = struct_anon_34# /usr/include/sndfile.h: 487

# /usr/include/sndfile.h: 515
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'description',
    'originator',
    'originator_reference',
    'origination_date',
    'origination_time',
    'time_reference_low',
    'time_reference_high',
    'version',
    'umid',
    'loudness_value',
    'loudness_range',
    'max_true_peak_level',
    'max_momentary_loudness',
    'max_shortterm_loudness',
    'reserved',
    'coding_history_size',
    'coding_history',
]
struct_anon_35._fields_ = [
    ('description', c_char * int(256)),
    ('originator', c_char * int(32)),
    ('originator_reference', c_char * int(32)),
    ('origination_date', c_char * int(10)),
    ('origination_time', c_char * int(8)),
    ('time_reference_low', c_uint32),
    ('time_reference_high', c_uint32),
    ('version', c_short),
    ('umid', c_char * int(64)),
    ('loudness_value', c_int16),
    ('loudness_range', c_int16),
    ('max_true_peak_level', c_int16),
    ('max_momentary_loudness', c_int16),
    ('max_shortterm_loudness', c_int16),
    ('reserved', c_char * int(180)),
    ('coding_history_size', c_uint32),
    ('coding_history', c_char * int(256)),
]

SF_BROADCAST_INFO = struct_anon_35# /usr/include/sndfile.h: 515

# /usr/include/sndfile.h: 517
class struct_SF_CART_TIMER(Structure):
    pass

struct_SF_CART_TIMER.__slots__ = [
    'usage',
    'value',
]
struct_SF_CART_TIMER._fields_ = [
    ('usage', c_char * int(4)),
    ('value', c_int32),
]

SF_CART_TIMER = struct_SF_CART_TIMER# /usr/include/sndfile.h: 522

# /usr/include/sndfile.h: 549
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'version',
    'title',
    'artist',
    'cut_id',
    'client_id',
    'category',
    'classification',
    'out_cue',
    'start_date',
    'start_time',
    'end_date',
    'end_time',
    'producer_app_id',
    'producer_app_version',
    'user_def',
    'level_reference',
    'post_timers',
    'reserved',
    'url',
    'tag_text_size',
    'tag_text',
]
struct_anon_36._fields_ = [
    ('version', c_char * int(4)),
    ('title', c_char * int(64)),
    ('artist', c_char * int(64)),
    ('cut_id', c_char * int(64)),
    ('client_id', c_char * int(64)),
    ('category', c_char * int(64)),
    ('classification', c_char * int(64)),
    ('out_cue', c_char * int(64)),
    ('start_date', c_char * int(10)),
    ('start_time', c_char * int(8)),
    ('end_date', c_char * int(10)),
    ('end_time', c_char * int(8)),
    ('producer_app_id', c_char * int(64)),
    ('producer_app_version', c_char * int(64)),
    ('user_def', c_char * int(64)),
    ('level_reference', c_int32),
    ('post_timers', SF_CART_TIMER * int(8)),
    ('reserved', c_char * int(276)),
    ('url', c_char * int(1024)),
    ('tag_text_size', c_uint32),
    ('tag_text', c_char * int(256)),
]

SF_CART_INFO = struct_anon_36# /usr/include/sndfile.h: 549

sf_vio_get_filelen = CFUNCTYPE(UNCHECKED(sf_count_t), POINTER(None))# /usr/include/sndfile.h: 553

sf_vio_seek = CFUNCTYPE(UNCHECKED(sf_count_t), sf_count_t, c_int, POINTER(None))# /usr/include/sndfile.h: 554

sf_vio_read = CFUNCTYPE(UNCHECKED(sf_count_t), POINTER(None), sf_count_t, POINTER(None))# /usr/include/sndfile.h: 555

sf_vio_write = CFUNCTYPE(UNCHECKED(sf_count_t), POINTER(None), sf_count_t, POINTER(None))# /usr/include/sndfile.h: 556

sf_vio_tell = CFUNCTYPE(UNCHECKED(sf_count_t), POINTER(None))# /usr/include/sndfile.h: 557

# /usr/include/sndfile.h: 559
class struct_SF_VIRTUAL_IO(Structure):
    pass

struct_SF_VIRTUAL_IO.__slots__ = [
    'get_filelen',
    'seek',
    'read',
    'write',
    'tell',
]
struct_SF_VIRTUAL_IO._fields_ = [
    ('get_filelen', sf_vio_get_filelen),
    ('seek', sf_vio_seek),
    ('read', sf_vio_read),
    ('write', sf_vio_write),
    ('tell', sf_vio_tell),
]

SF_VIRTUAL_IO = struct_SF_VIRTUAL_IO# /usr/include/sndfile.h: 567

# /usr/include/sndfile.h: 576
if _libs["sndfile"].has("sf_open", "cdecl"):
    sf_open = _libs["sndfile"].get("sf_open", "cdecl")
    sf_open.argtypes = [String, c_int, POINTER(SF_INFO)]
    sf_open.restype = POINTER(SNDFILE)

# /usr/include/sndfile.h: 591
if _libs["sndfile"].has("sf_open_fd", "cdecl"):
    sf_open_fd = _libs["sndfile"].get("sf_open_fd", "cdecl")
    sf_open_fd.argtypes = [c_int, c_int, POINTER(SF_INFO), c_int]
    sf_open_fd.restype = POINTER(SNDFILE)

# /usr/include/sndfile.h: 593
if _libs["sndfile"].has("sf_open_virtual", "cdecl"):
    sf_open_virtual = _libs["sndfile"].get("sf_open_virtual", "cdecl")
    sf_open_virtual.argtypes = [POINTER(SF_VIRTUAL_IO), c_int, POINTER(SF_INFO), POINTER(None)]
    sf_open_virtual.restype = POINTER(SNDFILE)

# /usr/include/sndfile.h: 600
if _libs["sndfile"].has("sf_error", "cdecl"):
    sf_error = _libs["sndfile"].get("sf_error", "cdecl")
    sf_error.argtypes = [POINTER(SNDFILE)]
    sf_error.restype = c_int

# /usr/include/sndfile.h: 607
if _libs["sndfile"].has("sf_strerror", "cdecl"):
    sf_strerror = _libs["sndfile"].get("sf_strerror", "cdecl")
    sf_strerror.argtypes = [POINTER(SNDFILE)]
    sf_strerror.restype = c_char_p

# /usr/include/sndfile.h: 615
if _libs["sndfile"].has("sf_error_number", "cdecl"):
    sf_error_number = _libs["sndfile"].get("sf_error_number", "cdecl")
    sf_error_number.argtypes = [c_int]
    sf_error_number.restype = c_char_p

# /usr/include/sndfile.h: 623
if _libs["sndfile"].has("sf_perror", "cdecl"):
    sf_perror = _libs["sndfile"].get("sf_perror", "cdecl")
    sf_perror.argtypes = [POINTER(SNDFILE)]
    sf_perror.restype = c_int

# /usr/include/sndfile.h: 624
if _libs["sndfile"].has("sf_error_str", "cdecl"):
    sf_error_str = _libs["sndfile"].get("sf_error_str", "cdecl")
    sf_error_str.argtypes = [POINTER(SNDFILE), String, c_size_t]
    sf_error_str.restype = c_int

# /usr/include/sndfile.h: 631
if _libs["sndfile"].has("sf_command", "cdecl"):
    sf_command = _libs["sndfile"].get("sf_command", "cdecl")
    sf_command.argtypes = [POINTER(SNDFILE), c_int, POINTER(None), c_int]
    sf_command.restype = c_int

# /usr/include/sndfile.h: 636
if _libs["sndfile"].has("sf_format_check", "cdecl"):
    sf_format_check = _libs["sndfile"].get("sf_format_check", "cdecl")
    sf_format_check.argtypes = [POINTER(SF_INFO)]
    sf_format_check.restype = c_int

enum_anon_37 = c_int# /usr/include/sndfile.h: 651

SF_SEEK_SET = 0# /usr/include/sndfile.h: 651

SF_SEEK_CUR = 1# /usr/include/sndfile.h: 651

SF_SEEK_END = 2# /usr/include/sndfile.h: 651

# /usr/include/sndfile.h: 657
if _libs["sndfile"].has("sf_seek", "cdecl"):
    sf_seek = _libs["sndfile"].get("sf_seek", "cdecl")
    sf_seek.argtypes = [POINTER(SNDFILE), sf_count_t, c_int]
    sf_seek.restype = sf_count_t

# /usr/include/sndfile.h: 668
if _libs["sndfile"].has("sf_set_string", "cdecl"):
    sf_set_string = _libs["sndfile"].get("sf_set_string", "cdecl")
    sf_set_string.argtypes = [POINTER(SNDFILE), c_int, String]
    sf_set_string.restype = c_int

# /usr/include/sndfile.h: 670
if _libs["sndfile"].has("sf_get_string", "cdecl"):
    sf_get_string = _libs["sndfile"].get("sf_get_string", "cdecl")
    sf_get_string.argtypes = [POINTER(SNDFILE), c_int]
    sf_get_string.restype = c_char_p

# /usr/include/sndfile.h: 675
if _libs["sndfile"].has("sf_version_string", "cdecl"):
    sf_version_string = _libs["sndfile"].get("sf_version_string", "cdecl")
    sf_version_string.argtypes = []
    sf_version_string.restype = c_char_p

# /usr/include/sndfile.h: 688
if _libs["sndfile"].has("sf_current_byterate", "cdecl"):
    sf_current_byterate = _libs["sndfile"].get("sf_current_byterate", "cdecl")
    sf_current_byterate.argtypes = [POINTER(SNDFILE)]
    sf_current_byterate.restype = c_int

# /usr/include/sndfile.h: 693
if _libs["sndfile"].has("sf_read_raw", "cdecl"):
    sf_read_raw = _libs["sndfile"].get("sf_read_raw", "cdecl")
    sf_read_raw.argtypes = [POINTER(SNDFILE), POINTER(None), sf_count_t]
    sf_read_raw.restype = sf_count_t

# /usr/include/sndfile.h: 694
if _libs["sndfile"].has("sf_write_raw", "cdecl"):
    sf_write_raw = _libs["sndfile"].get("sf_write_raw", "cdecl")
    sf_write_raw.argtypes = [POINTER(SNDFILE), POINTER(None), sf_count_t]
    sf_write_raw.restype = sf_count_t

# /usr/include/sndfile.h: 707
if _libs["sndfile"].has("sf_readf_short", "cdecl"):
    sf_readf_short = _libs["sndfile"].get("sf_readf_short", "cdecl")
    sf_readf_short.argtypes = [POINTER(SNDFILE), POINTER(c_short), sf_count_t]
    sf_readf_short.restype = sf_count_t

# /usr/include/sndfile.h: 708
if _libs["sndfile"].has("sf_writef_short", "cdecl"):
    sf_writef_short = _libs["sndfile"].get("sf_writef_short", "cdecl")
    sf_writef_short.argtypes = [POINTER(SNDFILE), POINTER(c_short), sf_count_t]
    sf_writef_short.restype = sf_count_t

# /usr/include/sndfile.h: 710
if _libs["sndfile"].has("sf_readf_int", "cdecl"):
    sf_readf_int = _libs["sndfile"].get("sf_readf_int", "cdecl")
    sf_readf_int.argtypes = [POINTER(SNDFILE), POINTER(c_int), sf_count_t]
    sf_readf_int.restype = sf_count_t

# /usr/include/sndfile.h: 711
if _libs["sndfile"].has("sf_writef_int", "cdecl"):
    sf_writef_int = _libs["sndfile"].get("sf_writef_int", "cdecl")
    sf_writef_int.argtypes = [POINTER(SNDFILE), POINTER(c_int), sf_count_t]
    sf_writef_int.restype = sf_count_t

# /usr/include/sndfile.h: 713
if _libs["sndfile"].has("sf_readf_float", "cdecl"):
    sf_readf_float = _libs["sndfile"].get("sf_readf_float", "cdecl")
    sf_readf_float.argtypes = [POINTER(SNDFILE), POINTER(c_float), sf_count_t]
    sf_readf_float.restype = sf_count_t

# /usr/include/sndfile.h: 714
if _libs["sndfile"].has("sf_writef_float", "cdecl"):
    sf_writef_float = _libs["sndfile"].get("sf_writef_float", "cdecl")
    sf_writef_float.argtypes = [POINTER(SNDFILE), POINTER(c_float), sf_count_t]
    sf_writef_float.restype = sf_count_t

# /usr/include/sndfile.h: 716
if _libs["sndfile"].has("sf_readf_double", "cdecl"):
    sf_readf_double = _libs["sndfile"].get("sf_readf_double", "cdecl")
    sf_readf_double.argtypes = [POINTER(SNDFILE), POINTER(c_double), sf_count_t]
    sf_readf_double.restype = sf_count_t

# /usr/include/sndfile.h: 717
if _libs["sndfile"].has("sf_writef_double", "cdecl"):
    sf_writef_double = _libs["sndfile"].get("sf_writef_double", "cdecl")
    sf_writef_double.argtypes = [POINTER(SNDFILE), POINTER(c_double), sf_count_t]
    sf_writef_double.restype = sf_count_t

# /usr/include/sndfile.h: 725
if _libs["sndfile"].has("sf_read_short", "cdecl"):
    sf_read_short = _libs["sndfile"].get("sf_read_short", "cdecl")
    sf_read_short.argtypes = [POINTER(SNDFILE), POINTER(c_short), sf_count_t]
    sf_read_short.restype = sf_count_t

# /usr/include/sndfile.h: 726
if _libs["sndfile"].has("sf_write_short", "cdecl"):
    sf_write_short = _libs["sndfile"].get("sf_write_short", "cdecl")
    sf_write_short.argtypes = [POINTER(SNDFILE), POINTER(c_short), sf_count_t]
    sf_write_short.restype = sf_count_t

# /usr/include/sndfile.h: 728
if _libs["sndfile"].has("sf_read_int", "cdecl"):
    sf_read_int = _libs["sndfile"].get("sf_read_int", "cdecl")
    sf_read_int.argtypes = [POINTER(SNDFILE), POINTER(c_int), sf_count_t]
    sf_read_int.restype = sf_count_t

# /usr/include/sndfile.h: 729
if _libs["sndfile"].has("sf_write_int", "cdecl"):
    sf_write_int = _libs["sndfile"].get("sf_write_int", "cdecl")
    sf_write_int.argtypes = [POINTER(SNDFILE), POINTER(c_int), sf_count_t]
    sf_write_int.restype = sf_count_t

# /usr/include/sndfile.h: 731
if _libs["sndfile"].has("sf_read_float", "cdecl"):
    sf_read_float = _libs["sndfile"].get("sf_read_float", "cdecl")
    sf_read_float.argtypes = [POINTER(SNDFILE), POINTER(c_float), sf_count_t]
    sf_read_float.restype = sf_count_t

# /usr/include/sndfile.h: 732
if _libs["sndfile"].has("sf_write_float", "cdecl"):
    sf_write_float = _libs["sndfile"].get("sf_write_float", "cdecl")
    sf_write_float.argtypes = [POINTER(SNDFILE), POINTER(c_float), sf_count_t]
    sf_write_float.restype = sf_count_t

# /usr/include/sndfile.h: 734
if _libs["sndfile"].has("sf_read_double", "cdecl"):
    sf_read_double = _libs["sndfile"].get("sf_read_double", "cdecl")
    sf_read_double.argtypes = [POINTER(SNDFILE), POINTER(c_double), sf_count_t]
    sf_read_double.restype = sf_count_t

# /usr/include/sndfile.h: 735
if _libs["sndfile"].has("sf_write_double", "cdecl"):
    sf_write_double = _libs["sndfile"].get("sf_write_double", "cdecl")
    sf_write_double.argtypes = [POINTER(SNDFILE), POINTER(c_double), sf_count_t]
    sf_write_double.restype = sf_count_t

# /usr/include/sndfile.h: 743
if _libs["sndfile"].has("sf_close", "cdecl"):
    sf_close = _libs["sndfile"].get("sf_close", "cdecl")
    sf_close.argtypes = [POINTER(SNDFILE)]
    sf_close.restype = c_int

# /usr/include/sndfile.h: 751
if _libs["sndfile"].has("sf_write_sync", "cdecl"):
    sf_write_sync = _libs["sndfile"].get("sf_write_sync", "cdecl")
    sf_write_sync.argtypes = [POINTER(SNDFILE)]
    sf_write_sync.restype = None

# /usr/include/sndfile.h: 784
class struct_SF_CHUNK_INFO(Structure):
    pass

struct_SF_CHUNK_INFO.__slots__ = [
    'id',
    'id_size',
    'datalen',
    'data',
]
struct_SF_CHUNK_INFO._fields_ = [
    ('id', c_char * int(64)),
    ('id_size', c_uint),
    ('datalen', c_uint),
    ('data', POINTER(None)),
]

SF_CHUNK_INFO = struct_SF_CHUNK_INFO# /usr/include/sndfile.h: 791

# /usr/include/sndfile.h: 798
if _libs["sndfile"].has("sf_set_chunk", "cdecl"):
    sf_set_chunk = _libs["sndfile"].get("sf_set_chunk", "cdecl")
    sf_set_chunk.argtypes = [POINTER(SNDFILE), POINTER(SF_CHUNK_INFO)]
    sf_set_chunk.restype = c_int

# /usr/include/sndfile.h: 803
class struct_SF_CHUNK_ITERATOR(Structure):
    pass

SF_CHUNK_ITERATOR = struct_SF_CHUNK_ITERATOR# /usr/include/sndfile.h: 803

# /usr/include/sndfile.h: 821
if _libs["sndfile"].has("sf_get_chunk_iterator", "cdecl"):
    sf_get_chunk_iterator = _libs["sndfile"].get("sf_get_chunk_iterator", "cdecl")
    sf_get_chunk_iterator.argtypes = [POINTER(SNDFILE), POINTER(SF_CHUNK_INFO)]
    sf_get_chunk_iterator.restype = POINTER(SF_CHUNK_ITERATOR)

# /usr/include/sndfile.h: 835
if _libs["sndfile"].has("sf_next_chunk_iterator", "cdecl"):
    sf_next_chunk_iterator = _libs["sndfile"].get("sf_next_chunk_iterator", "cdecl")
    sf_next_chunk_iterator.argtypes = [POINTER(SF_CHUNK_ITERATOR)]
    sf_next_chunk_iterator.restype = POINTER(SF_CHUNK_ITERATOR)

# /usr/include/sndfile.h: 851
if _libs["sndfile"].has("sf_get_chunk_size", "cdecl"):
    sf_get_chunk_size = _libs["sndfile"].get("sf_get_chunk_size", "cdecl")
    sf_get_chunk_size.argtypes = [POINTER(SF_CHUNK_ITERATOR), POINTER(SF_CHUNK_INFO)]
    sf_get_chunk_size.restype = c_int

# /usr/include/sndfile.h: 865
if _libs["sndfile"].has("sf_get_chunk_data", "cdecl"):
    sf_get_chunk_data = _libs["sndfile"].get("sf_get_chunk_data", "cdecl")
    sf_get_chunk_data.argtypes = [POINTER(SF_CHUNK_ITERATOR), POINTER(SF_CHUNK_INFO)]
    sf_get_chunk_data.restype = c_int

# /usr/include/sndfile.h: 268
try:
    SF_STR_FIRST = SF_STR_TITLE
except:
    pass

# /usr/include/sndfile.h: 269
try:
    SF_STR_LAST = SF_STR_GENRE
except:
    pass

# /usr/include/sndfile.h: 350
try:
    SF_COUNT_MAX = 9223372036854775807
except:
    pass

SNDFILE_tag = struct_SNDFILE_tag# /usr/include/sndfile.h: 339

SF_INFO = struct_SF_INFO# /usr/include/sndfile.h: 359

SF_CART_TIMER = struct_SF_CART_TIMER# /usr/include/sndfile.h: 517

SF_VIRTUAL_IO = struct_SF_VIRTUAL_IO# /usr/include/sndfile.h: 559

SF_CHUNK_INFO = struct_SF_CHUNK_INFO# /usr/include/sndfile.h: 784

SF_CHUNK_ITERATOR = struct_SF_CHUNK_ITERATOR# /usr/include/sndfile.h: 803

# No inserted files

# No prefix-stripping

