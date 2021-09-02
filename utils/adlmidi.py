r"""Wrapper for adlmidi.h

Generated with:
ctypesgen /usr/include/adlmidi.h -lADLMIDI -o adlmidi.py

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
_libs["ADLMIDI"] = load_library("ADLMIDI")

# 1 libraries
# End libraries

# No modules

ADL_UInt8 = c_uint8# /usr/include/adlmidi.h: 48

ADL_UInt16 = c_uint16# /usr/include/adlmidi.h: 49

ADL_SInt8 = c_int8# /usr/include/adlmidi.h: 50

ADL_SInt16 = c_int16# /usr/include/adlmidi.h: 51

enum_ADLMIDI_VolumeModels = c_int# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_AUTO = 0# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_Generic = 1# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_NativeOPL3 = 2# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_CMF = ADLMIDI_VolumeModel_NativeOPL3# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_DMX = 3# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_APOGEE = 4# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_9X = 5# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_DMX_Fixed = 6# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_APOGEE_Fixed = 7# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_AIL = 8# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_9X_GENERIC_FM = 9# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_HMI = 10# /usr/include/adlmidi.h: 101

ADLMIDI_VolumeModel_HMI_OLD = 11# /usr/include/adlmidi.h: 101

enum_ADLMIDI_SampleType = c_int# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_S16 = 0# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_S8 = (ADLMIDI_SampleType_S16 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_F32 = (ADLMIDI_SampleType_S8 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_F64 = (ADLMIDI_SampleType_F32 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_S24 = (ADLMIDI_SampleType_F64 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_S32 = (ADLMIDI_SampleType_S24 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_U8 = (ADLMIDI_SampleType_S32 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_U16 = (ADLMIDI_SampleType_U8 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_U24 = (ADLMIDI_SampleType_U16 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_U32 = (ADLMIDI_SampleType_U24 + 1)# /usr/include/adlmidi.h: 134

ADLMIDI_SampleType_Count = (ADLMIDI_SampleType_U32 + 1)# /usr/include/adlmidi.h: 134

# /usr/include/adlmidi.h: 163
class struct_ADLMIDI_AudioFormat(Structure):
    pass

struct_ADLMIDI_AudioFormat.__slots__ = [
    'type',
    'containerSize',
    'sampleOffset',
]
struct_ADLMIDI_AudioFormat._fields_ = [
    ('type', enum_ADLMIDI_SampleType),
    ('containerSize', c_uint),
    ('sampleOffset', c_uint),
]

# /usr/include/adlmidi.h: 176
class struct_ADL_MIDIPlayer(Structure):
    pass

struct_ADL_MIDIPlayer.__slots__ = [
    'adl_midiPlayer',
]
struct_ADL_MIDIPlayer._fields_ = [
    ('adl_midiPlayer', POINTER(None)),
]

# /usr/include/adlmidi.h: 191
if _libs["ADLMIDI"].has("adl_setNumChips", "cdecl"):
    adl_setNumChips = _libs["ADLMIDI"].get("adl_setNumChips", "cdecl")
    adl_setNumChips.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setNumChips.restype = c_int

# /usr/include/adlmidi.h: 198
if _libs["ADLMIDI"].has("adl_getNumChips", "cdecl"):
    adl_getNumChips = _libs["ADLMIDI"].get("adl_getNumChips", "cdecl")
    adl_getNumChips.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getNumChips.restype = c_int

# /usr/include/adlmidi.h: 205
if _libs["ADLMIDI"].has("adl_getNumChipsObtained", "cdecl"):
    adl_getNumChipsObtained = _libs["ADLMIDI"].get("adl_getNumChipsObtained", "cdecl")
    adl_getNumChipsObtained.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getNumChipsObtained.restype = c_int

# /usr/include/adlmidi.h: 216
if _libs["ADLMIDI"].has("adl_setBank", "cdecl"):
    adl_setBank = _libs["ADLMIDI"].get("adl_setBank", "cdecl")
    adl_setBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setBank.restype = c_int

# /usr/include/adlmidi.h: 222
if _libs["ADLMIDI"].has("adl_getBanksCount", "cdecl"):
    adl_getBanksCount = _libs["ADLMIDI"].get("adl_getBanksCount", "cdecl")
    adl_getBanksCount.argtypes = []
    adl_getBanksCount.restype = c_int

# /usr/include/adlmidi.h: 228
if _libs["ADLMIDI"].has("adl_getBankNames", "cdecl"):
    adl_getBankNames = _libs["ADLMIDI"].get("adl_getBankNames", "cdecl")
    adl_getBankNames.argtypes = []
    adl_getBankNames.restype = POINTER(POINTER(c_char))

# /usr/include/adlmidi.h: 236
class struct_ADL_Bank(Structure):
    pass

struct_ADL_Bank.__slots__ = [
    'pointer',
]
struct_ADL_Bank._fields_ = [
    ('pointer', POINTER(None) * int(3)),
]

ADL_Bank = struct_ADL_Bank# /usr/include/adlmidi.h: 236

# /usr/include/adlmidi.h: 249
class struct_ADL_BankId(Structure):
    pass

struct_ADL_BankId.__slots__ = [
    'percussive',
    'msb',
    'lsb',
]
struct_ADL_BankId._fields_ = [
    ('percussive', ADL_UInt8),
    ('msb', ADL_UInt8),
    ('lsb', ADL_UInt8),
]

ADL_BankId = struct_ADL_BankId# /usr/include/adlmidi.h: 249

enum_ADL_BankAccessFlags = c_int# /usr/include/adlmidi.h: 254

ADLMIDI_Bank_Create = 1# /usr/include/adlmidi.h: 254

ADLMIDI_Bank_CreateRt = (1 | 2)# /usr/include/adlmidi.h: 254

enum_anon_3 = c_int# /usr/include/adlmidi.h: 268

ADLMIDI_InstrumentVersion = 0# /usr/include/adlmidi.h: 268

enum_ADL_InstrumentFlags = c_int# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_2op = 0# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_4op = 1# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_Pseudo4op = 2# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_IsBlank = 4# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_RhythmModeMask = 56# /usr/include/adlmidi.h: 292

ADLMIDI_Ins_ALL_MASK = 7# /usr/include/adlmidi.h: 292

ADL_InstrumentFlags = enum_ADL_InstrumentFlags# /usr/include/adlmidi.h: 292

enum_ADL_RhythmMode = c_int# /usr/include/adlmidi.h: 309

ADLMIDI_RM_BassDrum = 8# /usr/include/adlmidi.h: 309

ADLMIDI_RM_Snare = 16# /usr/include/adlmidi.h: 309

ADLMIDI_RM_TomTom = 24# /usr/include/adlmidi.h: 309

ADLMIDI_RM_Cymbal = 32# /usr/include/adlmidi.h: 309

ADLMIDI_RM_HiHat = 40# /usr/include/adlmidi.h: 309

ADL_RhythmMode = enum_ADL_RhythmMode# /usr/include/adlmidi.h: 309

# /usr/include/adlmidi.h: 327
class struct_ADL_Operator(Structure):
    pass

struct_ADL_Operator.__slots__ = [
    'avekf_20',
    'ksl_l_40',
    'atdec_60',
    'susrel_80',
    'waveform_E0',
]
struct_ADL_Operator._fields_ = [
    ('avekf_20', ADL_UInt8),
    ('ksl_l_40', ADL_UInt8),
    ('atdec_60', ADL_UInt8),
    ('susrel_80', ADL_UInt8),
    ('waveform_E0', ADL_UInt8),
]

ADL_Operator = struct_ADL_Operator# /usr/include/adlmidi.h: 327

# /usr/include/adlmidi.h: 380
class struct_ADL_Instrument(Structure):
    pass

struct_ADL_Instrument.__slots__ = [
    'version',
    'note_offset1',
    'note_offset2',
    'midi_velocity_offset',
    'second_voice_detune',
    'percussion_key_number',
    'inst_flags',
    'fb_conn1_C0',
    'fb_conn2_C0',
    'operators',
    'delay_on_ms',
    'delay_off_ms',
]
struct_ADL_Instrument._fields_ = [
    ('version', c_int),
    ('note_offset1', ADL_SInt16),
    ('note_offset2', ADL_SInt16),
    ('midi_velocity_offset', ADL_SInt8),
    ('second_voice_detune', ADL_SInt8),
    ('percussion_key_number', ADL_UInt8),
    ('inst_flags', ADL_UInt8),
    ('fb_conn1_C0', ADL_UInt8),
    ('fb_conn2_C0', ADL_UInt8),
    ('operators', ADL_Operator * int(4)),
    ('delay_on_ms', ADL_UInt16),
    ('delay_off_ms', ADL_UInt16),
]

ADL_Instrument = struct_ADL_Instrument# /usr/include/adlmidi.h: 380

# /usr/include/adlmidi.h: 393
if _libs["ADLMIDI"].has("adl_reserveBanks", "cdecl"):
    adl_reserveBanks = _libs["ADLMIDI"].get("adl_reserveBanks", "cdecl")
    adl_reserveBanks.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_uint]
    adl_reserveBanks.restype = c_int

# /usr/include/adlmidi.h: 402
if _libs["ADLMIDI"].has("adl_getBank", "cdecl"):
    adl_getBank = _libs["ADLMIDI"].get("adl_getBank", "cdecl")
    adl_getBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_BankId), c_int, POINTER(ADL_Bank)]
    adl_getBank.restype = c_int

# /usr/include/adlmidi.h: 410
if _libs["ADLMIDI"].has("adl_getBankId", "cdecl"):
    adl_getBankId = _libs["ADLMIDI"].get("adl_getBankId", "cdecl")
    adl_getBankId.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank), POINTER(ADL_BankId)]
    adl_getBankId.restype = c_int

# /usr/include/adlmidi.h: 417
if _libs["ADLMIDI"].has("adl_removeBank", "cdecl"):
    adl_removeBank = _libs["ADLMIDI"].get("adl_removeBank", "cdecl")
    adl_removeBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank)]
    adl_removeBank.restype = c_int

# /usr/include/adlmidi.h: 424
if _libs["ADLMIDI"].has("adl_getFirstBank", "cdecl"):
    adl_getFirstBank = _libs["ADLMIDI"].get("adl_getFirstBank", "cdecl")
    adl_getFirstBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank)]
    adl_getFirstBank.restype = c_int

# /usr/include/adlmidi.h: 431
if _libs["ADLMIDI"].has("adl_getNextBank", "cdecl"):
    adl_getNextBank = _libs["ADLMIDI"].get("adl_getNextBank", "cdecl")
    adl_getNextBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank)]
    adl_getNextBank.restype = c_int

# /usr/include/adlmidi.h: 440
if _libs["ADLMIDI"].has("adl_getInstrument", "cdecl"):
    adl_getInstrument = _libs["ADLMIDI"].get("adl_getInstrument", "cdecl")
    adl_getInstrument.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank), c_uint, POINTER(ADL_Instrument)]
    adl_getInstrument.restype = c_int

# /usr/include/adlmidi.h: 451
if _libs["ADLMIDI"].has("adl_setInstrument", "cdecl"):
    adl_setInstrument = _libs["ADLMIDI"].get("adl_setInstrument", "cdecl")
    adl_setInstrument.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank), c_uint, POINTER(ADL_Instrument)]
    adl_setInstrument.restype = c_int

# /usr/include/adlmidi.h: 459
if _libs["ADLMIDI"].has("adl_loadEmbeddedBank", "cdecl"):
    adl_loadEmbeddedBank = _libs["ADLMIDI"].get("adl_loadEmbeddedBank", "cdecl")
    adl_loadEmbeddedBank.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_Bank), c_int]
    adl_loadEmbeddedBank.restype = c_int

# /usr/include/adlmidi.h: 476
if _libs["ADLMIDI"].has("adl_setNumFourOpsChn", "cdecl"):
    adl_setNumFourOpsChn = _libs["ADLMIDI"].get("adl_setNumFourOpsChn", "cdecl")
    adl_setNumFourOpsChn.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setNumFourOpsChn.restype = c_int

# /usr/include/adlmidi.h: 483
if _libs["ADLMIDI"].has("adl_getNumFourOpsChn", "cdecl"):
    adl_getNumFourOpsChn = _libs["ADLMIDI"].get("adl_getNumFourOpsChn", "cdecl")
    adl_getNumFourOpsChn.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getNumFourOpsChn.restype = c_int

# /usr/include/adlmidi.h: 490
if _libs["ADLMIDI"].has("adl_getNumFourOpsChnObtained", "cdecl"):
    adl_getNumFourOpsChnObtained = _libs["ADLMIDI"].get("adl_getNumFourOpsChnObtained", "cdecl")
    adl_getNumFourOpsChnObtained.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getNumFourOpsChnObtained.restype = c_int

# /usr/include/adlmidi.h: 503
if _libs["ADLMIDI"].has("adl_setPercMode", "cdecl"):
    adl_setPercMode = _libs["ADLMIDI"].get("adl_setPercMode", "cdecl")
    adl_setPercMode.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setPercMode.restype = None

# /usr/include/adlmidi.h: 510
if _libs["ADLMIDI"].has("adl_setHVibrato", "cdecl"):
    adl_setHVibrato = _libs["ADLMIDI"].get("adl_setHVibrato", "cdecl")
    adl_setHVibrato.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setHVibrato.restype = None

# /usr/include/adlmidi.h: 517
if _libs["ADLMIDI"].has("adl_getHVibrato", "cdecl"):
    adl_getHVibrato = _libs["ADLMIDI"].get("adl_getHVibrato", "cdecl")
    adl_getHVibrato.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getHVibrato.restype = c_int

# /usr/include/adlmidi.h: 524
if _libs["ADLMIDI"].has("adl_setHTremolo", "cdecl"):
    adl_setHTremolo = _libs["ADLMIDI"].get("adl_setHTremolo", "cdecl")
    adl_setHTremolo.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setHTremolo.restype = None

# /usr/include/adlmidi.h: 531
if _libs["ADLMIDI"].has("adl_getHTremolo", "cdecl"):
    adl_getHTremolo = _libs["ADLMIDI"].get("adl_getHTremolo", "cdecl")
    adl_getHTremolo.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getHTremolo.restype = c_int

# /usr/include/adlmidi.h: 538
if _libs["ADLMIDI"].has("adl_setScaleModulators", "cdecl"):
    adl_setScaleModulators = _libs["ADLMIDI"].get("adl_setScaleModulators", "cdecl")
    adl_setScaleModulators.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setScaleModulators.restype = None

# /usr/include/adlmidi.h: 549
if _libs["ADLMIDI"].has("adl_setFullRangeBrightness", "cdecl"):
    adl_setFullRangeBrightness = _libs["ADLMIDI"].get("adl_setFullRangeBrightness", "cdecl")
    adl_setFullRangeBrightness.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setFullRangeBrightness.restype = None

# /usr/include/adlmidi.h: 557
if _libs["ADLMIDI"].has("adl_setAutoArpeggio", "cdecl"):
    adl_setAutoArpeggio = _libs["ADLMIDI"].get("adl_setAutoArpeggio", "cdecl")
    adl_setAutoArpeggio.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setAutoArpeggio.restype = None

# /usr/include/adlmidi.h: 564
if _libs["ADLMIDI"].has("adl_setLoopEnabled", "cdecl"):
    adl_setLoopEnabled = _libs["ADLMIDI"].get("adl_setLoopEnabled", "cdecl")
    adl_setLoopEnabled.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setLoopEnabled.restype = None

# /usr/include/adlmidi.h: 571
if _libs["ADLMIDI"].has("adl_setSoftPanEnabled", "cdecl"):
    adl_setSoftPanEnabled = _libs["ADLMIDI"].get("adl_setSoftPanEnabled", "cdecl")
    adl_setSoftPanEnabled.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setSoftPanEnabled.restype = None

# /usr/include/adlmidi.h: 579
if _libs["ADLMIDI"].has("adl_setLogarithmicVolumes", "cdecl"):
    adl_setLogarithmicVolumes = _libs["ADLMIDI"].get("adl_setLogarithmicVolumes", "cdecl")
    adl_setLogarithmicVolumes.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setLogarithmicVolumes.restype = None

# /usr/include/adlmidi.h: 586
if _libs["ADLMIDI"].has("adl_setVolumeRangeModel", "cdecl"):
    adl_setVolumeRangeModel = _libs["ADLMIDI"].get("adl_setVolumeRangeModel", "cdecl")
    adl_setVolumeRangeModel.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setVolumeRangeModel.restype = None

# /usr/include/adlmidi.h: 593
if _libs["ADLMIDI"].has("adl_getVolumeRangeModel", "cdecl"):
    adl_getVolumeRangeModel = _libs["ADLMIDI"].get("adl_getVolumeRangeModel", "cdecl")
    adl_getVolumeRangeModel.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_getVolumeRangeModel.restype = c_int

# /usr/include/adlmidi.h: 604
if _libs["ADLMIDI"].has("adl_openBankFile", "cdecl"):
    adl_openBankFile = _libs["ADLMIDI"].get("adl_openBankFile", "cdecl")
    adl_openBankFile.argtypes = [POINTER(struct_ADL_MIDIPlayer), String]
    adl_openBankFile.restype = c_int

# /usr/include/adlmidi.h: 616
if _libs["ADLMIDI"].has("adl_openBankData", "cdecl"):
    adl_openBankData = _libs["ADLMIDI"].get("adl_openBankData", "cdecl")
    adl_openBankData.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(None), c_ulong]
    adl_openBankData.restype = c_int

# /usr/include/adlmidi.h: 627
if _libs["ADLMIDI"].has("adl_emulatorName", "cdecl"):
    adl_emulatorName = _libs["ADLMIDI"].get("adl_emulatorName", "cdecl")
    adl_emulatorName.argtypes = []
    adl_emulatorName.restype = c_char_p

# /usr/include/adlmidi.h: 634
if _libs["ADLMIDI"].has("adl_chipEmulatorName", "cdecl"):
    adl_chipEmulatorName = _libs["ADLMIDI"].get("adl_chipEmulatorName", "cdecl")
    adl_chipEmulatorName.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_chipEmulatorName.restype = c_char_p

enum_ADL_Emulator = c_int# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_NUKED = 0# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_NUKED_174 = (ADLMIDI_EMU_NUKED + 1)# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_DOSBOX = (ADLMIDI_EMU_NUKED_174 + 1)# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_OPAL = (ADLMIDI_EMU_DOSBOX + 1)# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_JAVA = (ADLMIDI_EMU_OPAL + 1)# /usr/include/adlmidi.h: 639

ADLMIDI_EMU_end = (ADLMIDI_EMU_JAVA + 1)# /usr/include/adlmidi.h: 639

# /usr/include/adlmidi.h: 661
if _libs["ADLMIDI"].has("adl_switchEmulator", "cdecl"):
    adl_switchEmulator = _libs["ADLMIDI"].get("adl_switchEmulator", "cdecl")
    adl_switchEmulator.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_switchEmulator.restype = c_int

# /usr/include/adlmidi.h: 670
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_anon_4._fields_ = [
    ('major', ADL_UInt16),
    ('minor', ADL_UInt16),
    ('patch', ADL_UInt16),
]

ADL_Version = struct_anon_4# /usr/include/adlmidi.h: 670

# /usr/include/adlmidi.h: 681
if _libs["ADLMIDI"].has("adl_setRunAtPcmRate", "cdecl"):
    adl_setRunAtPcmRate = _libs["ADLMIDI"].get("adl_setRunAtPcmRate", "cdecl")
    adl_setRunAtPcmRate.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int]
    adl_setRunAtPcmRate.restype = c_int

# /usr/include/adlmidi.h: 689
if _libs["ADLMIDI"].has("adl_setDeviceIdentifier", "cdecl"):
    adl_setDeviceIdentifier = _libs["ADLMIDI"].get("adl_setDeviceIdentifier", "cdecl")
    adl_setDeviceIdentifier.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_uint]
    adl_setDeviceIdentifier.restype = c_int

# /usr/include/adlmidi.h: 699
if _libs["ADLMIDI"].has("adl_linkedLibraryVersion", "cdecl"):
    adl_linkedLibraryVersion = _libs["ADLMIDI"].get("adl_linkedLibraryVersion", "cdecl")
    adl_linkedLibraryVersion.argtypes = []
    adl_linkedLibraryVersion.restype = c_char_p

# /usr/include/adlmidi.h: 705
if _libs["ADLMIDI"].has("adl_linkedVersion", "cdecl"):
    adl_linkedVersion = _libs["ADLMIDI"].get("adl_linkedVersion", "cdecl")
    adl_linkedVersion.argtypes = []
    adl_linkedVersion.restype = POINTER(ADL_Version)

# /usr/include/adlmidi.h: 718
if _libs["ADLMIDI"].has("adl_errorString", "cdecl"):
    adl_errorString = _libs["ADLMIDI"].get("adl_errorString", "cdecl")
    adl_errorString.argtypes = []
    adl_errorString.restype = c_char_p

# /usr/include/adlmidi.h: 725
if _libs["ADLMIDI"].has("adl_errorInfo", "cdecl"):
    adl_errorInfo = _libs["ADLMIDI"].get("adl_errorInfo", "cdecl")
    adl_errorInfo.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_errorInfo.restype = c_char_p

# /usr/include/adlmidi.h: 742
if _libs["ADLMIDI"].has("adl_init", "cdecl"):
    adl_init = _libs["ADLMIDI"].get("adl_init", "cdecl")
    adl_init.argtypes = [c_long]
    adl_init.restype = POINTER(struct_ADL_MIDIPlayer)

# /usr/include/adlmidi.h: 748
if _libs["ADLMIDI"].has("adl_close", "cdecl"):
    adl_close = _libs["ADLMIDI"].get("adl_close", "cdecl")
    adl_close.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_close.restype = None

# /usr/include/adlmidi.h: 763
if _libs["ADLMIDI"].has("adl_openFile", "cdecl"):
    adl_openFile = _libs["ADLMIDI"].get("adl_openFile", "cdecl")
    adl_openFile.argtypes = [POINTER(struct_ADL_MIDIPlayer), String]
    adl_openFile.restype = c_int

# /usr/include/adlmidi.h: 775
if _libs["ADLMIDI"].has("adl_openData", "cdecl"):
    adl_openData = _libs["ADLMIDI"].get("adl_openData", "cdecl")
    adl_openData.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(None), c_ulong]
    adl_openData.restype = c_int

# /usr/include/adlmidi.h: 781
if _libs["ADLMIDI"].has("adl_reset", "cdecl"):
    adl_reset = _libs["ADLMIDI"].get("adl_reset", "cdecl")
    adl_reset.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_reset.restype = None

# /usr/include/adlmidi.h: 791
if _libs["ADLMIDI"].has("adl_totalTimeLength", "cdecl"):
    adl_totalTimeLength = _libs["ADLMIDI"].get("adl_totalTimeLength", "cdecl")
    adl_totalTimeLength.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_totalTimeLength.restype = c_double

# /usr/include/adlmidi.h: 801
if _libs["ADLMIDI"].has("adl_loopStartTime", "cdecl"):
    adl_loopStartTime = _libs["ADLMIDI"].get("adl_loopStartTime", "cdecl")
    adl_loopStartTime.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_loopStartTime.restype = c_double

# /usr/include/adlmidi.h: 811
if _libs["ADLMIDI"].has("adl_loopEndTime", "cdecl"):
    adl_loopEndTime = _libs["ADLMIDI"].get("adl_loopEndTime", "cdecl")
    adl_loopEndTime.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_loopEndTime.restype = c_double

# /usr/include/adlmidi.h: 821
if _libs["ADLMIDI"].has("adl_positionTell", "cdecl"):
    adl_positionTell = _libs["ADLMIDI"].get("adl_positionTell", "cdecl")
    adl_positionTell.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_positionTell.restype = c_double

# /usr/include/adlmidi.h: 831
if _libs["ADLMIDI"].has("adl_positionSeek", "cdecl"):
    adl_positionSeek = _libs["ADLMIDI"].get("adl_positionSeek", "cdecl")
    adl_positionSeek.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_double]
    adl_positionSeek.restype = None

# /usr/include/adlmidi.h: 840
if _libs["ADLMIDI"].has("adl_positionRewind", "cdecl"):
    adl_positionRewind = _libs["ADLMIDI"].get("adl_positionRewind", "cdecl")
    adl_positionRewind.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_positionRewind.restype = None

# /usr/include/adlmidi.h: 850
if _libs["ADLMIDI"].has("adl_setTempo", "cdecl"):
    adl_setTempo = _libs["ADLMIDI"].get("adl_setTempo", "cdecl")
    adl_setTempo.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_double]
    adl_setTempo.restype = None

# /usr/include/adlmidi.h: 857
if _libs["ADLMIDI"].has("adl_atEnd", "cdecl"):
    adl_atEnd = _libs["ADLMIDI"].get("adl_atEnd", "cdecl")
    adl_atEnd.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_atEnd.restype = c_int

# /usr/include/adlmidi.h: 864
if _libs["ADLMIDI"].has("adl_trackCount", "cdecl"):
    adl_trackCount = _libs["ADLMIDI"].get("adl_trackCount", "cdecl")
    adl_trackCount.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_trackCount.restype = c_size_t

enum_ADLMIDI_TrackOptions = c_int# /usr/include/adlmidi.h: 869

ADLMIDI_TrackOption_On = 1# /usr/include/adlmidi.h: 869

ADLMIDI_TrackOption_Off = 2# /usr/include/adlmidi.h: 869

ADLMIDI_TrackOption_Solo = 3# /usr/include/adlmidi.h: 869

# /usr/include/adlmidi.h: 885
if _libs["ADLMIDI"].has("adl_setTrackOptions", "cdecl"):
    adl_setTrackOptions = _libs["ADLMIDI"].get("adl_setTrackOptions", "cdecl")
    adl_setTrackOptions.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_size_t, c_uint]
    adl_setTrackOptions.restype = c_int

ADL_TriggerHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_uint, c_size_t)# /usr/include/adlmidi.h: 893

# /usr/include/adlmidi.h: 902
if _libs["ADLMIDI"].has("adl_setTriggerHandler", "cdecl"):
    adl_setTriggerHandler = _libs["ADLMIDI"].get("adl_setTriggerHandler", "cdecl")
    adl_setTriggerHandler.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_TriggerHandler, POINTER(None)]
    adl_setTriggerHandler.restype = c_int

# /usr/include/adlmidi.h: 914
if _libs["ADLMIDI"].has("adl_metaMusicTitle", "cdecl"):
    adl_metaMusicTitle = _libs["ADLMIDI"].get("adl_metaMusicTitle", "cdecl")
    adl_metaMusicTitle.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_metaMusicTitle.restype = c_char_p

# /usr/include/adlmidi.h: 921
if _libs["ADLMIDI"].has("adl_metaMusicCopyright", "cdecl"):
    adl_metaMusicCopyright = _libs["ADLMIDI"].get("adl_metaMusicCopyright", "cdecl")
    adl_metaMusicCopyright.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_metaMusicCopyright.restype = c_char_p

# /usr/include/adlmidi.h: 931
if _libs["ADLMIDI"].has("adl_metaTrackTitleCount", "cdecl"):
    adl_metaTrackTitleCount = _libs["ADLMIDI"].get("adl_metaTrackTitleCount", "cdecl")
    adl_metaTrackTitleCount.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_metaTrackTitleCount.restype = c_size_t

# /usr/include/adlmidi.h: 939
if _libs["ADLMIDI"].has("adl_metaTrackTitle", "cdecl"):
    adl_metaTrackTitle = _libs["ADLMIDI"].get("adl_metaTrackTitle", "cdecl")
    adl_metaTrackTitle.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_size_t]
    adl_metaTrackTitle.restype = c_char_p

# /usr/include/adlmidi.h: 944
class struct_Adl_MarkerEntry(Structure):
    pass

struct_Adl_MarkerEntry.__slots__ = [
    'label',
    'pos_time',
    'pos_ticks',
]
struct_Adl_MarkerEntry._fields_ = [
    ('label', String),
    ('pos_time', c_double),
    ('pos_ticks', c_ulong),
]

# /usr/include/adlmidi.h: 959
if _libs["ADLMIDI"].has("adl_metaMarkerCount", "cdecl"):
    adl_metaMarkerCount = _libs["ADLMIDI"].get("adl_metaMarkerCount", "cdecl")
    adl_metaMarkerCount.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_metaMarkerCount.restype = c_size_t

# /usr/include/adlmidi.h: 967
if _libs["ADLMIDI"].has("adl_metaMarker", "cdecl"):
    adl_metaMarker = _libs["ADLMIDI"].get("adl_metaMarker", "cdecl")
    adl_metaMarker.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_size_t]
    adl_metaMarker.restype = struct_Adl_MarkerEntry

# /usr/include/adlmidi.h: 990
if _libs["ADLMIDI"].has("adl_play", "cdecl"):
    adl_play = _libs["ADLMIDI"].get("adl_play", "cdecl")
    adl_play.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int, POINTER(c_short)]
    adl_play.restype = c_int

# /usr/include/adlmidi.h: 1010
if _libs["ADLMIDI"].has("adl_playFormat", "cdecl"):
    adl_playFormat = _libs["ADLMIDI"].get("adl_playFormat", "cdecl")
    adl_playFormat.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int, POINTER(ADL_UInt8), POINTER(ADL_UInt8), POINTER(struct_ADLMIDI_AudioFormat)]
    adl_playFormat.restype = c_int

# /usr/include/adlmidi.h: 1029
if _libs["ADLMIDI"].has("adl_generate", "cdecl"):
    adl_generate = _libs["ADLMIDI"].get("adl_generate", "cdecl")
    adl_generate.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int, POINTER(c_short)]
    adl_generate.restype = c_int

# /usr/include/adlmidi.h: 1050
if _libs["ADLMIDI"].has("adl_generateFormat", "cdecl"):
    adl_generateFormat = _libs["ADLMIDI"].get("adl_generateFormat", "cdecl")
    adl_generateFormat.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_int, POINTER(ADL_UInt8), POINTER(ADL_UInt8), POINTER(struct_ADLMIDI_AudioFormat)]
    adl_generateFormat.restype = c_int

# /usr/include/adlmidi.h: 1066
if _libs["ADLMIDI"].has("adl_tickEvents", "cdecl"):
    adl_tickEvents = _libs["ADLMIDI"].get("adl_tickEvents", "cdecl")
    adl_tickEvents.argtypes = [POINTER(struct_ADL_MIDIPlayer), c_double, c_double]
    adl_tickEvents.restype = c_double

# /usr/include/adlmidi.h: 1077
if _libs["ADLMIDI"].has("adl_panic", "cdecl"):
    adl_panic = _libs["ADLMIDI"].get("adl_panic", "cdecl")
    adl_panic.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_panic.restype = None

# /usr/include/adlmidi.h: 1083
if _libs["ADLMIDI"].has("adl_rt_resetState", "cdecl"):
    adl_rt_resetState = _libs["ADLMIDI"].get("adl_rt_resetState", "cdecl")
    adl_rt_resetState.argtypes = [POINTER(struct_ADL_MIDIPlayer)]
    adl_rt_resetState.restype = None

# /usr/include/adlmidi.h: 1093
if _libs["ADLMIDI"].has("adl_rt_noteOn", "cdecl"):
    adl_rt_noteOn = _libs["ADLMIDI"].get("adl_rt_noteOn", "cdecl")
    adl_rt_noteOn.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8, ADL_UInt8]
    adl_rt_noteOn.restype = c_int

# /usr/include/adlmidi.h: 1101
if _libs["ADLMIDI"].has("adl_rt_noteOff", "cdecl"):
    adl_rt_noteOff = _libs["ADLMIDI"].get("adl_rt_noteOff", "cdecl")
    adl_rt_noteOff.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8]
    adl_rt_noteOff.restype = None

# /usr/include/adlmidi.h: 1110
if _libs["ADLMIDI"].has("adl_rt_noteAfterTouch", "cdecl"):
    adl_rt_noteAfterTouch = _libs["ADLMIDI"].get("adl_rt_noteAfterTouch", "cdecl")
    adl_rt_noteAfterTouch.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8, ADL_UInt8]
    adl_rt_noteAfterTouch.restype = None

# /usr/include/adlmidi.h: 1118
if _libs["ADLMIDI"].has("adl_rt_channelAfterTouch", "cdecl"):
    adl_rt_channelAfterTouch = _libs["ADLMIDI"].get("adl_rt_channelAfterTouch", "cdecl")
    adl_rt_channelAfterTouch.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8]
    adl_rt_channelAfterTouch.restype = None

# /usr/include/adlmidi.h: 1127
if _libs["ADLMIDI"].has("adl_rt_controllerChange", "cdecl"):
    adl_rt_controllerChange = _libs["ADLMIDI"].get("adl_rt_controllerChange", "cdecl")
    adl_rt_controllerChange.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8, ADL_UInt8]
    adl_rt_controllerChange.restype = None

# /usr/include/adlmidi.h: 1135
if _libs["ADLMIDI"].has("adl_rt_patchChange", "cdecl"):
    adl_rt_patchChange = _libs["ADLMIDI"].get("adl_rt_patchChange", "cdecl")
    adl_rt_patchChange.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8]
    adl_rt_patchChange.restype = None

# /usr/include/adlmidi.h: 1143
if _libs["ADLMIDI"].has("adl_rt_pitchBend", "cdecl"):
    adl_rt_pitchBend = _libs["ADLMIDI"].get("adl_rt_pitchBend", "cdecl")
    adl_rt_pitchBend.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt16]
    adl_rt_pitchBend.restype = None

# /usr/include/adlmidi.h: 1152
if _libs["ADLMIDI"].has("adl_rt_pitchBendML", "cdecl"):
    adl_rt_pitchBendML = _libs["ADLMIDI"].get("adl_rt_pitchBendML", "cdecl")
    adl_rt_pitchBendML.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8, ADL_UInt8]
    adl_rt_pitchBendML.restype = None

# /usr/include/adlmidi.h: 1160
if _libs["ADLMIDI"].has("adl_rt_bankChangeLSB", "cdecl"):
    adl_rt_bankChangeLSB = _libs["ADLMIDI"].get("adl_rt_bankChangeLSB", "cdecl")
    adl_rt_bankChangeLSB.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8]
    adl_rt_bankChangeLSB.restype = None

# /usr/include/adlmidi.h: 1168
if _libs["ADLMIDI"].has("adl_rt_bankChangeMSB", "cdecl"):
    adl_rt_bankChangeMSB = _libs["ADLMIDI"].get("adl_rt_bankChangeMSB", "cdecl")
    adl_rt_bankChangeMSB.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_UInt8]
    adl_rt_bankChangeMSB.restype = None

# /usr/include/adlmidi.h: 1177
if _libs["ADLMIDI"].has("adl_rt_bankChange", "cdecl"):
    adl_rt_bankChange = _libs["ADLMIDI"].get("adl_rt_bankChange", "cdecl")
    adl_rt_bankChange.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_UInt8, ADL_SInt16]
    adl_rt_bankChange.restype = None

# /usr/include/adlmidi.h: 1186
if _libs["ADLMIDI"].has("adl_rt_systemExclusive", "cdecl"):
    adl_rt_systemExclusive = _libs["ADLMIDI"].get("adl_rt_systemExclusive", "cdecl")
    adl_rt_systemExclusive.argtypes = [POINTER(struct_ADL_MIDIPlayer), POINTER(ADL_UInt8), c_size_t]
    adl_rt_systemExclusive.restype = c_int

ADL_RawEventHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), ADL_UInt8, ADL_UInt8, ADL_UInt8, POINTER(ADL_UInt8), c_size_t)# /usr/include/adlmidi.h: 1202

ADL_NoteHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, c_int, c_int, c_double)# /usr/include/adlmidi.h: 1212

ADL_DebugMessageHook = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /usr/include/adlmidi.h: 1219

# /usr/include/adlmidi.h: 1227
if _libs["ADLMIDI"].has("adl_setRawEventHook", "cdecl"):
    adl_setRawEventHook = _libs["ADLMIDI"].get("adl_setRawEventHook", "cdecl")
    adl_setRawEventHook.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_RawEventHook, POINTER(None)]
    adl_setRawEventHook.restype = None

# /usr/include/adlmidi.h: 1235
if _libs["ADLMIDI"].has("adl_setNoteHook", "cdecl"):
    adl_setNoteHook = _libs["ADLMIDI"].get("adl_setNoteHook", "cdecl")
    adl_setNoteHook.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_NoteHook, POINTER(None)]
    adl_setNoteHook.restype = None

# /usr/include/adlmidi.h: 1243
if _libs["ADLMIDI"].has("adl_setDebugMessageHook", "cdecl"):
    adl_setDebugMessageHook = _libs["ADLMIDI"].get("adl_setDebugMessageHook", "cdecl")
    adl_setDebugMessageHook.argtypes = [POINTER(struct_ADL_MIDIPlayer), ADL_DebugMessageHook, POINTER(None)]
    adl_setDebugMessageHook.restype = None

# /usr/include/adlmidi.h: 1265
if _libs["ADLMIDI"].has("adl_describeChannels", "cdecl"):
    adl_describeChannels = _libs["ADLMIDI"].get("adl_describeChannels", "cdecl")
    adl_describeChannels.argtypes = [POINTER(struct_ADL_MIDIPlayer), String, String, c_size_t]
    adl_describeChannels.restype = c_int

# /usr/include/adlmidi.h: 31
try:
    ADLMIDI_VERSION_MAJOR = 1
except:
    pass

# /usr/include/adlmidi.h: 32
try:
    ADLMIDI_VERSION_MINOR = 5
except:
    pass

# /usr/include/adlmidi.h: 33
try:
    ADLMIDI_VERSION_PATCHLEVEL = 1
except:
    pass

# /usr/include/adlmidi.h: 35
def ADLMIDI_TOSTR_I(s):
    return s

# /usr/include/adlmidi.h: 36
def ADLMIDI_TOSTR(s):
    return (ADLMIDI_TOSTR_I (s))

# /usr/include/adlmidi.h: 42
try:
    ADL_CHIP_SAMPLE_RATE = 49716
except:
    pass

# /usr/include/adlmidi.h: 183
try:
    adl_setNumCards = adl_setNumChips
except:
    pass

ADLMIDI_AudioFormat = struct_ADLMIDI_AudioFormat# /usr/include/adlmidi.h: 163

ADL_MIDIPlayer = struct_ADL_MIDIPlayer# /usr/include/adlmidi.h: 176

ADL_Bank = struct_ADL_Bank# /usr/include/adlmidi.h: 236

ADL_BankId = struct_ADL_BankId# /usr/include/adlmidi.h: 249

ADL_Operator = struct_ADL_Operator# /usr/include/adlmidi.h: 327

ADL_Instrument = struct_ADL_Instrument# /usr/include/adlmidi.h: 380

Adl_MarkerEntry = struct_Adl_MarkerEntry# /usr/include/adlmidi.h: 944

# No inserted files

# No prefix-stripping

