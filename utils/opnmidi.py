r"""Wrapper for opnmidi.h

Generated with:
ctypesgen -lOPNMIDI /usr/include/opnmidi.h -o opnmidi.py

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
_libs["OPNMIDI"] = load_library("OPNMIDI")

# 1 libraries
# End libraries

# No modules

OPN2_UInt8 = c_uint8# /usr/include/opnmidi.h: 49

OPN2_UInt16 = c_uint16# /usr/include/opnmidi.h: 50

OPN2_SInt8 = c_int8# /usr/include/opnmidi.h: 51

OPN2_SInt16 = c_int16# /usr/include/opnmidi.h: 52

enum_OPNMIDI_ChipType = c_int# /usr/include/opnmidi.h: 102

OPNMIDI_ChipType_OPN2 = 0# /usr/include/opnmidi.h: 102

OPNMIDI_ChipType_OPNA = (OPNMIDI_ChipType_OPN2 + 1)# /usr/include/opnmidi.h: 102

enum_OPNMIDI_VolumeModels = c_int# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_AUTO = 0# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_Generic = (OPNMIDI_VolumeModel_AUTO + 1)# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_NativeOPN2 = (OPNMIDI_VolumeModel_Generic + 1)# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_DMX = (OPNMIDI_VolumeModel_NativeOPN2 + 1)# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_APOGEE = (OPNMIDI_VolumeModel_DMX + 1)# /usr/include/opnmidi.h: 113

OPNMIDI_VolumeModel_9X = (OPNMIDI_VolumeModel_APOGEE + 1)# /usr/include/opnmidi.h: 113

enum_OPNMIDI_SampleType = c_int# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_S16 = 0# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_S8 = (OPNMIDI_SampleType_S16 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_F32 = (OPNMIDI_SampleType_S8 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_F64 = (OPNMIDI_SampleType_F32 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_S24 = (OPNMIDI_SampleType_F64 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_S32 = (OPNMIDI_SampleType_S24 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_U8 = (OPNMIDI_SampleType_S32 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_U16 = (OPNMIDI_SampleType_U8 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_U24 = (OPNMIDI_SampleType_U16 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_U32 = (OPNMIDI_SampleType_U24 + 1)# /usr/include/opnmidi.h: 132

OPNMIDI_SampleType_Count = (OPNMIDI_SampleType_U32 + 1)# /usr/include/opnmidi.h: 132

# /usr/include/opnmidi.h: 161
class struct_OPNMIDI_AudioFormat(Structure):
    pass

struct_OPNMIDI_AudioFormat.__slots__ = [
    'type',
    'containerSize',
    'sampleOffset',
]
struct_OPNMIDI_AudioFormat._fields_ = [
    ('type', enum_OPNMIDI_SampleType),
    ('containerSize', c_uint),
    ('sampleOffset', c_uint),
]

# /usr/include/opnmidi.h: 174
class struct_OPN2_MIDIPlayer(Structure):
    pass

struct_OPN2_MIDIPlayer.__slots__ = [
    'opn2_midiPlayer',
]
struct_OPN2_MIDIPlayer._fields_ = [
    ('opn2_midiPlayer', POINTER(None)),
]

# /usr/include/opnmidi.h: 189
if _libs["OPNMIDI"].has("opn2_setNumChips", "cdecl"):
    opn2_setNumChips = _libs["OPNMIDI"].get("opn2_setNumChips", "cdecl")
    opn2_setNumChips.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setNumChips.restype = c_int

# /usr/include/opnmidi.h: 196
if _libs["OPNMIDI"].has("opn2_getNumChips", "cdecl"):
    opn2_getNumChips = _libs["OPNMIDI"].get("opn2_getNumChips", "cdecl")
    opn2_getNumChips.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getNumChips.restype = c_int

# /usr/include/opnmidi.h: 203
if _libs["OPNMIDI"].has("opn2_getNumChipsObtained", "cdecl"):
    opn2_getNumChipsObtained = _libs["OPNMIDI"].get("opn2_getNumChipsObtained", "cdecl")
    opn2_getNumChipsObtained.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getNumChipsObtained.restype = c_int

# /usr/include/opnmidi.h: 211
class struct_OPN2_Bank(Structure):
    pass

struct_OPN2_Bank.__slots__ = [
    'pointer',
]
struct_OPN2_Bank._fields_ = [
    ('pointer', POINTER(None) * int(3)),
]

OPN2_Bank = struct_OPN2_Bank# /usr/include/opnmidi.h: 211

# /usr/include/opnmidi.h: 224
class struct_OPN2_BankId(Structure):
    pass

struct_OPN2_BankId.__slots__ = [
    'percussive',
    'msb',
    'lsb',
]
struct_OPN2_BankId._fields_ = [
    ('percussive', OPN2_UInt8),
    ('msb', OPN2_UInt8),
    ('lsb', OPN2_UInt8),
]

OPN2_BankId = struct_OPN2_BankId# /usr/include/opnmidi.h: 224

enum_OPN2_BankAccessFlags = c_int# /usr/include/opnmidi.h: 229

OPNMIDI_Bank_Create = 1# /usr/include/opnmidi.h: 229

OPNMIDI_Bank_CreateRt = (1 | 2)# /usr/include/opnmidi.h: 229

enum_anon_3 = c_int# /usr/include/opnmidi.h: 244

OPNMIDI_InstrumentVersion = 0# /usr/include/opnmidi.h: 244

enum_OPN2_InstrumentFlags = c_int# /usr/include/opnmidi.h: 256

OPNMIDI_Ins_Pseudo8op = 1# /usr/include/opnmidi.h: 256

OPNMIDI_Ins_IsBlank = 2# /usr/include/opnmidi.h: 256

OPN2_InstrumentFlags = enum_OPN2_InstrumentFlags# /usr/include/opnmidi.h: 256

# /usr/include/opnmidi.h: 277
class struct_OPN2_Operator(Structure):
    pass

struct_OPN2_Operator.__slots__ = [
    'dtfm_30',
    'level_40',
    'rsatk_50',
    'amdecay1_60',
    'decay2_70',
    'susrel_80',
    'ssgeg_90',
]
struct_OPN2_Operator._fields_ = [
    ('dtfm_30', OPN2_UInt8),
    ('level_40', OPN2_UInt8),
    ('rsatk_50', OPN2_UInt8),
    ('amdecay1_60', OPN2_UInt8),
    ('decay2_70', OPN2_UInt8),
    ('susrel_80', OPN2_UInt8),
    ('ssgeg_90', OPN2_UInt8),
]

OPN2_Operator = struct_OPN2_Operator# /usr/include/opnmidi.h: 277

# /usr/include/opnmidi.h: 304
class struct_OPN2_Instrument(Structure):
    pass

struct_OPN2_Instrument.__slots__ = [
    'version',
    'note_offset',
    'midi_velocity_offset',
    'percussion_key_number',
    'inst_flags',
    'fbalg',
    'lfosens',
    'operators',
    'delay_on_ms',
    'delay_off_ms',
]
struct_OPN2_Instrument._fields_ = [
    ('version', c_int),
    ('note_offset', OPN2_SInt16),
    ('midi_velocity_offset', OPN2_SInt8),
    ('percussion_key_number', OPN2_UInt8),
    ('inst_flags', OPN2_UInt8),
    ('fbalg', OPN2_UInt8),
    ('lfosens', OPN2_UInt8),
    ('operators', OPN2_Operator * int(4)),
    ('delay_on_ms', OPN2_UInt16),
    ('delay_off_ms', OPN2_UInt16),
]

OPN2_Instrument = struct_OPN2_Instrument# /usr/include/opnmidi.h: 304

# /usr/include/opnmidi.h: 384
if _libs["OPNMIDI"].has("opn2_setLfoEnabled", "cdecl"):
    opn2_setLfoEnabled = _libs["OPNMIDI"].get("opn2_setLfoEnabled", "cdecl")
    opn2_setLfoEnabled.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setLfoEnabled.restype = None

# /usr/include/opnmidi.h: 387
if _libs["OPNMIDI"].has("opn2_getLfoEnabled", "cdecl"):
    opn2_getLfoEnabled = _libs["OPNMIDI"].get("opn2_getLfoEnabled", "cdecl")
    opn2_getLfoEnabled.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getLfoEnabled.restype = c_int

# /usr/include/opnmidi.h: 390
if _libs["OPNMIDI"].has("opn2_setLfoFrequency", "cdecl"):
    opn2_setLfoFrequency = _libs["OPNMIDI"].get("opn2_setLfoFrequency", "cdecl")
    opn2_setLfoFrequency.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setLfoFrequency.restype = None

# /usr/include/opnmidi.h: 393
if _libs["OPNMIDI"].has("opn2_getLfoFrequency", "cdecl"):
    opn2_getLfoFrequency = _libs["OPNMIDI"].get("opn2_getLfoFrequency", "cdecl")
    opn2_getLfoFrequency.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getLfoFrequency.restype = c_int

# /usr/include/opnmidi.h: 396
if _libs["OPNMIDI"].has("opn2_setChipType", "cdecl"):
    opn2_setChipType = _libs["OPNMIDI"].get("opn2_setChipType", "cdecl")
    opn2_setChipType.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setChipType.restype = None

# /usr/include/opnmidi.h: 399
if _libs["OPNMIDI"].has("opn2_getChipType", "cdecl"):
    opn2_getChipType = _libs["OPNMIDI"].get("opn2_getChipType", "cdecl")
    opn2_getChipType.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getChipType.restype = c_int

# /usr/include/opnmidi.h: 406
if _libs["OPNMIDI"].has("opn2_setScaleModulators", "cdecl"):
    opn2_setScaleModulators = _libs["OPNMIDI"].get("opn2_setScaleModulators", "cdecl")
    opn2_setScaleModulators.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setScaleModulators.restype = None

# /usr/include/opnmidi.h: 417
if _libs["OPNMIDI"].has("opn2_setFullRangeBrightness", "cdecl"):
    opn2_setFullRangeBrightness = _libs["OPNMIDI"].get("opn2_setFullRangeBrightness", "cdecl")
    opn2_setFullRangeBrightness.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setFullRangeBrightness.restype = None

# /usr/include/opnmidi.h: 425
if _libs["OPNMIDI"].has("opn2_setAutoArpeggio", "cdecl"):
    opn2_setAutoArpeggio = _libs["OPNMIDI"].get("opn2_setAutoArpeggio", "cdecl")
    opn2_setAutoArpeggio.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setAutoArpeggio.restype = None

# /usr/include/opnmidi.h: 432
if _libs["OPNMIDI"].has("opn2_setLoopEnabled", "cdecl"):
    opn2_setLoopEnabled = _libs["OPNMIDI"].get("opn2_setLoopEnabled", "cdecl")
    opn2_setLoopEnabled.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setLoopEnabled.restype = None

# /usr/include/opnmidi.h: 439
if _libs["OPNMIDI"].has("opn2_setSoftPanEnabled", "cdecl"):
    opn2_setSoftPanEnabled = _libs["OPNMIDI"].get("opn2_setSoftPanEnabled", "cdecl")
    opn2_setSoftPanEnabled.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setSoftPanEnabled.restype = None

# /usr/include/opnmidi.h: 447
if _libs["OPNMIDI"].has("opn2_setLogarithmicVolumes", "cdecl"):
    opn2_setLogarithmicVolumes = _libs["OPNMIDI"].get("opn2_setLogarithmicVolumes", "cdecl")
    opn2_setLogarithmicVolumes.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setLogarithmicVolumes.restype = None

# /usr/include/opnmidi.h: 454
if _libs["OPNMIDI"].has("opn2_setVolumeRangeModel", "cdecl"):
    opn2_setVolumeRangeModel = _libs["OPNMIDI"].get("opn2_setVolumeRangeModel", "cdecl")
    opn2_setVolumeRangeModel.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setVolumeRangeModel.restype = None

# /usr/include/opnmidi.h: 461
if _libs["OPNMIDI"].has("opn2_getVolumeRangeModel", "cdecl"):
    opn2_getVolumeRangeModel = _libs["OPNMIDI"].get("opn2_getVolumeRangeModel", "cdecl")
    opn2_getVolumeRangeModel.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_getVolumeRangeModel.restype = c_int

# /usr/include/opnmidi.h: 472
if _libs["OPNMIDI"].has("opn2_openBankFile", "cdecl"):
    opn2_openBankFile = _libs["OPNMIDI"].get("opn2_openBankFile", "cdecl")
    opn2_openBankFile.argtypes = [POINTER(struct_OPN2_MIDIPlayer), String]
    opn2_openBankFile.restype = c_int

# /usr/include/opnmidi.h: 484
if _libs["OPNMIDI"].has("opn2_openBankData", "cdecl"):
    opn2_openBankData = _libs["OPNMIDI"].get("opn2_openBankData", "cdecl")
    opn2_openBankData.argtypes = [POINTER(struct_OPN2_MIDIPlayer), POINTER(None), c_long]
    opn2_openBankData.restype = c_int

# /usr/include/opnmidi.h: 495
if _libs["OPNMIDI"].has("opn2_emulatorName", "cdecl"):
    opn2_emulatorName = _libs["OPNMIDI"].get("opn2_emulatorName", "cdecl")
    opn2_emulatorName.argtypes = []
    opn2_emulatorName.restype = c_char_p

# /usr/include/opnmidi.h: 502
if _libs["OPNMIDI"].has("opn2_chipEmulatorName", "cdecl"):
    opn2_chipEmulatorName = _libs["OPNMIDI"].get("opn2_chipEmulatorName", "cdecl")
    opn2_chipEmulatorName.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_chipEmulatorName.restype = c_char_p

enum_Opn2_Emulator = c_int# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_MAME = 0# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_NUKED = (OPNMIDI_EMU_MAME + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_GENS = (OPNMIDI_EMU_NUKED + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_GX = (OPNMIDI_EMU_GENS + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_NP2 = (OPNMIDI_EMU_GX + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_MAME_2608 = (OPNMIDI_EMU_NP2 + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_PMDWIN = (OPNMIDI_EMU_MAME_2608 + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_VGM_DUMPER = (OPNMIDI_EMU_PMDWIN + 1)# /usr/include/opnmidi.h: 507

OPNMIDI_EMU_end = (OPNMIDI_VGM_DUMPER + 1)# /usr/include/opnmidi.h: 507

# /usr/include/opnmidi.h: 535
if _libs["OPNMIDI"].has("opn2_switchEmulator", "cdecl"):
    opn2_switchEmulator = _libs["OPNMIDI"].get("opn2_switchEmulator", "cdecl")
    opn2_switchEmulator.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_switchEmulator.restype = c_int

# /usr/include/opnmidi.h: 544
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_anon_4._fields_ = [
    ('major', OPN2_UInt16),
    ('minor', OPN2_UInt16),
    ('patch', OPN2_UInt16),
]

OPN2_Version = struct_anon_4# /usr/include/opnmidi.h: 544

# /usr/include/opnmidi.h: 555
if _libs["OPNMIDI"].has("opn2_setRunAtPcmRate", "cdecl"):
    opn2_setRunAtPcmRate = _libs["OPNMIDI"].get("opn2_setRunAtPcmRate", "cdecl")
    opn2_setRunAtPcmRate.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int]
    opn2_setRunAtPcmRate.restype = c_int

# /usr/include/opnmidi.h: 563
if _libs["OPNMIDI"].has("opn2_setDeviceIdentifier", "cdecl"):
    opn2_setDeviceIdentifier = _libs["OPNMIDI"].get("opn2_setDeviceIdentifier", "cdecl")
    opn2_setDeviceIdentifier.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_uint]
    opn2_setDeviceIdentifier.restype = c_int

# /usr/include/opnmidi.h: 574
if _libs["OPNMIDI"].has("opn2_linkedLibraryVersion", "cdecl"):
    opn2_linkedLibraryVersion = _libs["OPNMIDI"].get("opn2_linkedLibraryVersion", "cdecl")
    opn2_linkedLibraryVersion.argtypes = []
    opn2_linkedLibraryVersion.restype = c_char_p

# /usr/include/opnmidi.h: 580
if _libs["OPNMIDI"].has("opn2_linkedVersion", "cdecl"):
    opn2_linkedVersion = _libs["OPNMIDI"].get("opn2_linkedVersion", "cdecl")
    opn2_linkedVersion.argtypes = []
    opn2_linkedVersion.restype = POINTER(OPN2_Version)

# /usr/include/opnmidi.h: 590
if _libs["OPNMIDI"].has("opn2_errorString", "cdecl"):
    opn2_errorString = _libs["OPNMIDI"].get("opn2_errorString", "cdecl")
    opn2_errorString.argtypes = []
    opn2_errorString.restype = c_char_p

# /usr/include/opnmidi.h: 597
if _libs["OPNMIDI"].has("opn2_errorInfo", "cdecl"):
    opn2_errorInfo = _libs["OPNMIDI"].get("opn2_errorInfo", "cdecl")
    opn2_errorInfo.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_errorInfo.restype = c_char_p

# /usr/include/opnmidi.h: 614
if _libs["OPNMIDI"].has("opn2_init", "cdecl"):
    opn2_init = _libs["OPNMIDI"].get("opn2_init", "cdecl")
    opn2_init.argtypes = [c_long]
    opn2_init.restype = POINTER(struct_OPN2_MIDIPlayer)

# /usr/include/opnmidi.h: 620
if _libs["OPNMIDI"].has("opn2_close", "cdecl"):
    opn2_close = _libs["OPNMIDI"].get("opn2_close", "cdecl")
    opn2_close.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_close.restype = None

# /usr/include/opnmidi.h: 634
if _libs["OPNMIDI"].has("opn2_openFile", "cdecl"):
    opn2_openFile = _libs["OPNMIDI"].get("opn2_openFile", "cdecl")
    opn2_openFile.argtypes = [POINTER(struct_OPN2_MIDIPlayer), String]
    opn2_openFile.restype = c_int

# /usr/include/opnmidi.h: 646
if _libs["OPNMIDI"].has("opn2_openData", "cdecl"):
    opn2_openData = _libs["OPNMIDI"].get("opn2_openData", "cdecl")
    opn2_openData.argtypes = [POINTER(struct_OPN2_MIDIPlayer), POINTER(None), c_ulong]
    opn2_openData.restype = c_int

# /usr/include/opnmidi.h: 652
if _libs["OPNMIDI"].has("opn2_reset", "cdecl"):
    opn2_reset = _libs["OPNMIDI"].get("opn2_reset", "cdecl")
    opn2_reset.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_reset.restype = None

# /usr/include/opnmidi.h: 662
if _libs["OPNMIDI"].has("opn2_totalTimeLength", "cdecl"):
    opn2_totalTimeLength = _libs["OPNMIDI"].get("opn2_totalTimeLength", "cdecl")
    opn2_totalTimeLength.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_totalTimeLength.restype = c_double

# /usr/include/opnmidi.h: 672
if _libs["OPNMIDI"].has("opn2_loopStartTime", "cdecl"):
    opn2_loopStartTime = _libs["OPNMIDI"].get("opn2_loopStartTime", "cdecl")
    opn2_loopStartTime.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_loopStartTime.restype = c_double

# /usr/include/opnmidi.h: 682
if _libs["OPNMIDI"].has("opn2_loopEndTime", "cdecl"):
    opn2_loopEndTime = _libs["OPNMIDI"].get("opn2_loopEndTime", "cdecl")
    opn2_loopEndTime.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_loopEndTime.restype = c_double

# /usr/include/opnmidi.h: 692
if _libs["OPNMIDI"].has("opn2_positionTell", "cdecl"):
    opn2_positionTell = _libs["OPNMIDI"].get("opn2_positionTell", "cdecl")
    opn2_positionTell.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_positionTell.restype = c_double

# /usr/include/opnmidi.h: 702
if _libs["OPNMIDI"].has("opn2_positionSeek", "cdecl"):
    opn2_positionSeek = _libs["OPNMIDI"].get("opn2_positionSeek", "cdecl")
    opn2_positionSeek.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_double]
    opn2_positionSeek.restype = None

# /usr/include/opnmidi.h: 711
if _libs["OPNMIDI"].has("opn2_positionRewind", "cdecl"):
    opn2_positionRewind = _libs["OPNMIDI"].get("opn2_positionRewind", "cdecl")
    opn2_positionRewind.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_positionRewind.restype = None

# /usr/include/opnmidi.h: 721
if _libs["OPNMIDI"].has("opn2_setTempo", "cdecl"):
    opn2_setTempo = _libs["OPNMIDI"].get("opn2_setTempo", "cdecl")
    opn2_setTempo.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_double]
    opn2_setTempo.restype = None

# /usr/include/opnmidi.h: 728
if _libs["OPNMIDI"].has("opn2_atEnd", "cdecl"):
    opn2_atEnd = _libs["OPNMIDI"].get("opn2_atEnd", "cdecl")
    opn2_atEnd.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_atEnd.restype = c_int

# /usr/include/opnmidi.h: 735
if _libs["OPNMIDI"].has("opn2_trackCount", "cdecl"):
    opn2_trackCount = _libs["OPNMIDI"].get("opn2_trackCount", "cdecl")
    opn2_trackCount.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_trackCount.restype = c_size_t

# /usr/include/opnmidi.h: 746
if _libs["OPNMIDI"].has("opn2_metaMusicTitle", "cdecl"):
    opn2_metaMusicTitle = _libs["OPNMIDI"].get("opn2_metaMusicTitle", "cdecl")
    opn2_metaMusicTitle.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_metaMusicTitle.restype = c_char_p

# /usr/include/opnmidi.h: 753
if _libs["OPNMIDI"].has("opn2_metaMusicCopyright", "cdecl"):
    opn2_metaMusicCopyright = _libs["OPNMIDI"].get("opn2_metaMusicCopyright", "cdecl")
    opn2_metaMusicCopyright.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_metaMusicCopyright.restype = c_char_p

# /usr/include/opnmidi.h: 763
if _libs["OPNMIDI"].has("opn2_metaTrackTitleCount", "cdecl"):
    opn2_metaTrackTitleCount = _libs["OPNMIDI"].get("opn2_metaTrackTitleCount", "cdecl")
    opn2_metaTrackTitleCount.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_metaTrackTitleCount.restype = c_size_t

# /usr/include/opnmidi.h: 771
if _libs["OPNMIDI"].has("opn2_metaTrackTitle", "cdecl"):
    opn2_metaTrackTitle = _libs["OPNMIDI"].get("opn2_metaTrackTitle", "cdecl")
    opn2_metaTrackTitle.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_size_t]
    opn2_metaTrackTitle.restype = c_char_p

# /usr/include/opnmidi.h: 776
class struct_Opn2_MarkerEntry(Structure):
    pass

struct_Opn2_MarkerEntry.__slots__ = [
    'label',
    'pos_time',
    'pos_ticks',
]
struct_Opn2_MarkerEntry._fields_ = [
    ('label', String),
    ('pos_time', c_double),
    ('pos_ticks', c_ulong),
]

# /usr/include/opnmidi.h: 791
if _libs["OPNMIDI"].has("opn2_metaMarkerCount", "cdecl"):
    opn2_metaMarkerCount = _libs["OPNMIDI"].get("opn2_metaMarkerCount", "cdecl")
    opn2_metaMarkerCount.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_metaMarkerCount.restype = c_size_t

# /usr/include/opnmidi.h: 799
if _libs["OPNMIDI"].has("opn2_metaMarker", "cdecl"):
    opn2_metaMarker = _libs["OPNMIDI"].get("opn2_metaMarker", "cdecl")
    opn2_metaMarker.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_size_t]
    opn2_metaMarker.restype = struct_Opn2_MarkerEntry

# /usr/include/opnmidi.h: 822
if _libs["OPNMIDI"].has("opn2_play", "cdecl"):
    opn2_play = _libs["OPNMIDI"].get("opn2_play", "cdecl")
    opn2_play.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int, POINTER(c_short)]
    opn2_play.restype = c_int

# /usr/include/opnmidi.h: 842
if _libs["OPNMIDI"].has("opn2_playFormat", "cdecl"):
    opn2_playFormat = _libs["OPNMIDI"].get("opn2_playFormat", "cdecl")
    opn2_playFormat.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int, POINTER(OPN2_UInt8), POINTER(OPN2_UInt8), POINTER(struct_OPNMIDI_AudioFormat)]
    opn2_playFormat.restype = c_int

# /usr/include/opnmidi.h: 861
if _libs["OPNMIDI"].has("opn2_generate", "cdecl"):
    opn2_generate = _libs["OPNMIDI"].get("opn2_generate", "cdecl")
    opn2_generate.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int, POINTER(c_short)]
    opn2_generate.restype = c_int

# /usr/include/opnmidi.h: 882
if _libs["OPNMIDI"].has("opn2_generateFormat", "cdecl"):
    opn2_generateFormat = _libs["OPNMIDI"].get("opn2_generateFormat", "cdecl")
    opn2_generateFormat.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_int, POINTER(OPN2_UInt8), POINTER(OPN2_UInt8), POINTER(struct_OPNMIDI_AudioFormat)]
    opn2_generateFormat.restype = c_int

# /usr/include/opnmidi.h: 894
if _libs["OPNMIDI"].has("opn2_tickEvents", "cdecl"):
    opn2_tickEvents = _libs["OPNMIDI"].get("opn2_tickEvents", "cdecl")
    opn2_tickEvents.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_double, c_double]
    opn2_tickEvents.restype = c_double

enum_OPNMIDI_TrackOptions = c_int# /usr/include/opnmidi.h: 899

OPNMIDI_TrackOption_On = 1# /usr/include/opnmidi.h: 899

OPNMIDI_TrackOption_Off = 2# /usr/include/opnmidi.h: 899

OPNMIDI_TrackOption_Solo = 3# /usr/include/opnmidi.h: 899

# /usr/include/opnmidi.h: 915
if _libs["OPNMIDI"].has("opn2_setTrackOptions", "cdecl"):
    opn2_setTrackOptions = _libs["OPNMIDI"].get("opn2_setTrackOptions", "cdecl")
    opn2_setTrackOptions.argtypes = [POINTER(struct_OPN2_MIDIPlayer), c_size_t, c_uint]
    opn2_setTrackOptions.restype = c_int

# /usr/include/opnmidi.h: 926
if _libs["OPNMIDI"].has("opn2_panic", "cdecl"):
    opn2_panic = _libs["OPNMIDI"].get("opn2_panic", "cdecl")
    opn2_panic.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_panic.restype = None

# /usr/include/opnmidi.h: 932
if _libs["OPNMIDI"].has("opn2_rt_resetState", "cdecl"):
    opn2_rt_resetState = _libs["OPNMIDI"].get("opn2_rt_resetState", "cdecl")
    opn2_rt_resetState.argtypes = [POINTER(struct_OPN2_MIDIPlayer)]
    opn2_rt_resetState.restype = None

# /usr/include/opnmidi.h: 942
if _libs["OPNMIDI"].has("opn2_rt_noteOn", "cdecl"):
    opn2_rt_noteOn = _libs["OPNMIDI"].get("opn2_rt_noteOn", "cdecl")
    opn2_rt_noteOn.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8, OPN2_UInt8]
    opn2_rt_noteOn.restype = c_int

# /usr/include/opnmidi.h: 950
if _libs["OPNMIDI"].has("opn2_rt_noteOff", "cdecl"):
    opn2_rt_noteOff = _libs["OPNMIDI"].get("opn2_rt_noteOff", "cdecl")
    opn2_rt_noteOff.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8]
    opn2_rt_noteOff.restype = None

# /usr/include/opnmidi.h: 959
if _libs["OPNMIDI"].has("opn2_rt_noteAfterTouch", "cdecl"):
    opn2_rt_noteAfterTouch = _libs["OPNMIDI"].get("opn2_rt_noteAfterTouch", "cdecl")
    opn2_rt_noteAfterTouch.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8, OPN2_UInt8]
    opn2_rt_noteAfterTouch.restype = None

# /usr/include/opnmidi.h: 967
if _libs["OPNMIDI"].has("opn2_rt_channelAfterTouch", "cdecl"):
    opn2_rt_channelAfterTouch = _libs["OPNMIDI"].get("opn2_rt_channelAfterTouch", "cdecl")
    opn2_rt_channelAfterTouch.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8]
    opn2_rt_channelAfterTouch.restype = None

# /usr/include/opnmidi.h: 976
if _libs["OPNMIDI"].has("opn2_rt_controllerChange", "cdecl"):
    opn2_rt_controllerChange = _libs["OPNMIDI"].get("opn2_rt_controllerChange", "cdecl")
    opn2_rt_controllerChange.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8, OPN2_UInt8]
    opn2_rt_controllerChange.restype = None

# /usr/include/opnmidi.h: 984
if _libs["OPNMIDI"].has("opn2_rt_patchChange", "cdecl"):
    opn2_rt_patchChange = _libs["OPNMIDI"].get("opn2_rt_patchChange", "cdecl")
    opn2_rt_patchChange.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8]
    opn2_rt_patchChange.restype = None

# /usr/include/opnmidi.h: 992
if _libs["OPNMIDI"].has("opn2_rt_pitchBend", "cdecl"):
    opn2_rt_pitchBend = _libs["OPNMIDI"].get("opn2_rt_pitchBend", "cdecl")
    opn2_rt_pitchBend.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt16]
    opn2_rt_pitchBend.restype = None

# /usr/include/opnmidi.h: 1001
if _libs["OPNMIDI"].has("opn2_rt_pitchBendML", "cdecl"):
    opn2_rt_pitchBendML = _libs["OPNMIDI"].get("opn2_rt_pitchBendML", "cdecl")
    opn2_rt_pitchBendML.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8, OPN2_UInt8]
    opn2_rt_pitchBendML.restype = None

# /usr/include/opnmidi.h: 1009
if _libs["OPNMIDI"].has("opn2_rt_bankChangeLSB", "cdecl"):
    opn2_rt_bankChangeLSB = _libs["OPNMIDI"].get("opn2_rt_bankChangeLSB", "cdecl")
    opn2_rt_bankChangeLSB.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8]
    opn2_rt_bankChangeLSB.restype = None

# /usr/include/opnmidi.h: 1017
if _libs["OPNMIDI"].has("opn2_rt_bankChangeMSB", "cdecl"):
    opn2_rt_bankChangeMSB = _libs["OPNMIDI"].get("opn2_rt_bankChangeMSB", "cdecl")
    opn2_rt_bankChangeMSB.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_UInt8]
    opn2_rt_bankChangeMSB.restype = None

# /usr/include/opnmidi.h: 1025
if _libs["OPNMIDI"].has("opn2_rt_bankChange", "cdecl"):
    opn2_rt_bankChange = _libs["OPNMIDI"].get("opn2_rt_bankChange", "cdecl")
    opn2_rt_bankChange.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_UInt8, OPN2_SInt16]
    opn2_rt_bankChange.restype = None

# /usr/include/opnmidi.h: 1034
if _libs["OPNMIDI"].has("opn2_rt_systemExclusive", "cdecl"):
    opn2_rt_systemExclusive = _libs["OPNMIDI"].get("opn2_rt_systemExclusive", "cdecl")
    opn2_rt_systemExclusive.argtypes = [POINTER(struct_OPN2_MIDIPlayer), POINTER(OPN2_UInt8), c_size_t]
    opn2_rt_systemExclusive.restype = c_int

OPN2_RawEventHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), OPN2_UInt8, OPN2_UInt8, OPN2_UInt8, POINTER(OPN2_UInt8), c_size_t)# /usr/include/opnmidi.h: 1047

OPN2_NoteHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, c_int, c_int, c_double)# /usr/include/opnmidi.h: 1056

OPN2_DebugMessageHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /usr/include/opnmidi.h: 1063

# /usr/include/opnmidi.h: 1071
if _libs["OPNMIDI"].has("opn2_setRawEventHook", "cdecl"):
    opn2_setRawEventHook = _libs["OPNMIDI"].get("opn2_setRawEventHook", "cdecl")
    opn2_setRawEventHook.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_RawEventHook, POINTER(None)]
    opn2_setRawEventHook.restype = None

# /usr/include/opnmidi.h: 1079
if _libs["OPNMIDI"].has("opn2_setNoteHook", "cdecl"):
    opn2_setNoteHook = _libs["OPNMIDI"].get("opn2_setNoteHook", "cdecl")
    opn2_setNoteHook.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_NoteHook, POINTER(None)]
    opn2_setNoteHook.restype = None

# /usr/include/opnmidi.h: 1087
if _libs["OPNMIDI"].has("opn2_setDebugMessageHook", "cdecl"):
    opn2_setDebugMessageHook = _libs["OPNMIDI"].get("opn2_setDebugMessageHook", "cdecl")
    opn2_setDebugMessageHook.argtypes = [POINTER(struct_OPN2_MIDIPlayer), OPN2_DebugMessageHook, POINTER(None)]
    opn2_setDebugMessageHook.restype = None

# /usr/include/opnmidi.h: 1108
if _libs["OPNMIDI"].has("opn2_describeChannels", "cdecl"):
    opn2_describeChannels = _libs["OPNMIDI"].get("opn2_describeChannels", "cdecl")
    opn2_describeChannels.argtypes = [POINTER(struct_OPN2_MIDIPlayer), String, String, c_size_t]
    opn2_describeChannels.restype = c_int

# /usr/include/opnmidi.h: 31
try:
    OPNMIDI_VERSION_MAJOR = 1
except:
    pass

# /usr/include/opnmidi.h: 32
try:
    OPNMIDI_VERSION_MINOR = 5
except:
    pass

# /usr/include/opnmidi.h: 33
try:
    OPNMIDI_VERSION_PATCHLEVEL = 1
except:
    pass

# /usr/include/opnmidi.h: 35
def OPNMIDI_TOSTR_I(s):
    return s

# /usr/include/opnmidi.h: 36
def OPNMIDI_TOSTR(s):
    return (OPNMIDI_TOSTR_I (s))

# /usr/include/opnmidi.h: 42
try:
    OPN_OPN2_SAMPLE_RATE = 53267
except:
    pass

# /usr/include/opnmidi.h: 43
try:
    OPN_OPNA_SAMPLE_RATE = 55466
except:
    pass

# /usr/include/opnmidi.h: 181
try:
    opn2_setNumCards = opn2_setNumChips
except:
    pass

OPNMIDI_AudioFormat = struct_OPNMIDI_AudioFormat# /usr/include/opnmidi.h: 161

OPN2_MIDIPlayer = struct_OPN2_MIDIPlayer# /usr/include/opnmidi.h: 174

OPN2_Bank = struct_OPN2_Bank# /usr/include/opnmidi.h: 211

OPN2_BankId = struct_OPN2_BankId# /usr/include/opnmidi.h: 224

OPN2_Operator = struct_OPN2_Operator# /usr/include/opnmidi.h: 277

OPN2_Instrument = struct_OPN2_Instrument# /usr/include/opnmidi.h: 304

Opn2_MarkerEntry = struct_Opn2_MarkerEntry# /usr/include/opnmidi.h: 776

# No inserted files

# No prefix-stripping

