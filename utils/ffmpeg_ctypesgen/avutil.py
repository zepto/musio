r"""Wrapper for adler32.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lavutil /usr/include/libavutil/adler32.h /usr/include/libavutil/aes_ctr.h /usr/include/libavutil/aes.h /usr/include/libavutil/attributes.h /usr/include/libavutil/audio_fifo.h /usr/include/libavutil/avassert.h /usr/include/libavutil/avconfig.h /usr/include/libavutil/avstring.h /usr/include/libavutil/avutil.h /usr/include/libavutil/base64.h /usr/include/libavutil/blowfish.h /usr/include/libavutil/bprint.h /usr/include/libavutil/bswap.h /usr/include/libavutil/buffer.h /usr/include/libavutil/camellia.h /usr/include/libavutil/cast5.h /usr/include/libavutil/channel_layout.h /usr/include/libavutil/common.h /usr/include/libavutil/cpu.h /usr/include/libavutil/crc.h /usr/include/libavutil/des.h /usr/include/libavutil/dict.h /usr/include/libavutil/display.h /usr/include/libavutil/dovi_meta.h /usr/include/libavutil/downmix_info.h /usr/include/libavutil/encryption_info.h /usr/include/libavutil/error.h /usr/include/libavutil/eval.h /usr/include/libavutil/ffversion.h /usr/include/libavutil/fifo.h /usr/include/libavutil/file.h /usr/include/libavutil/film_grain_params.h /usr/include/libavutil/frame.h /usr/include/libavutil/hash.h /usr/include/libavutil/hdr_dynamic_metadata.h /usr/include/libavutil/hmac.h /usr/include/libavutil/hwcontext_cuda.h /usr/include/libavutil/hwcontext_d3d11va.h /usr/include/libavutil/hwcontext_drm.h /usr/include/libavutil/hwcontext_dxva2.h /usr/include/libavutil/hwcontext.h /usr/include/libavutil/hwcontext_mediacodec.h /usr/include/libavutil/hwcontext_opencl.h /usr/include/libavutil/hwcontext_qsv.h /usr/include/libavutil/hwcontext_vaapi.h /usr/include/libavutil/hwcontext_vdpau.h /usr/include/libavutil/hwcontext_videotoolbox.h /usr/include/libavutil/hwcontext_vulkan.h /usr/include/libavutil/imgutils.h /usr/include/libavutil/intfloat.h /usr/include/libavutil/intreadwrite.h /usr/include/libavutil/lfg.h /usr/include/libavutil/log.h /usr/include/libavutil/lzo.h /usr/include/libavutil/macros.h /usr/include/libavutil/mastering_display_metadata.h /usr/include/libavutil/mathematics.h /usr/include/libavutil/md5.h /usr/include/libavutil/mem.h /usr/include/libavutil/motion_vector.h /usr/include/libavutil/murmur3.h /usr/include/libavutil/opt.h /usr/include/libavutil/parseutils.h /usr/include/libavutil/pixdesc.h /usr/include/libavutil/pixelutils.h /usr/include/libavutil/pixfmt.h /usr/include/libavutil/random_seed.h /usr/include/libavutil/rational.h /usr/include/libavutil/rc4.h /usr/include/libavutil/replaygain.h /usr/include/libavutil/ripemd.h /usr/include/libavutil/samplefmt.h /usr/include/libavutil/sha512.h /usr/include/libavutil/sha.h /usr/include/libavutil/spherical.h /usr/include/libavutil/stereo3d.h /usr/include/libavutil/tea.h /usr/include/libavutil/threadmessage.h /usr/include/libavutil/timecode.h /usr/include/libavutil/time.h /usr/include/libavutil/timestamp.h /usr/include/libavutil/tree.h /usr/include/libavutil/twofish.h /usr/include/libavutil/tx.h /usr/include/libavutil/version.h /usr/include/libavutil/video_enc_params.h /usr/include/libavutil/xtea.h -L/usr/include/libavutil -o avutil.py

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
_libs["avutil"] = load_library("avutil")

# 1 libraries
# End libraries

# No modules

__off_t = c_long# /usr/include/bits/types.h: 152

__off64_t = c_long# /usr/include/bits/types.h: 153

AVAdler = c_ulong# /usr/include/libavutil/adler32.h: 44

# /usr/include/libavutil/adler32.h: 61
if _libs["avutil"].has("av_adler32_update", "cdecl"):
    av_adler32_update = _libs["avutil"].get("av_adler32_update", "cdecl")
    av_adler32_update.argtypes = [AVAdler, POINTER(c_uint8), c_uint]
    av_adler32_update.restype = AVAdler

# /usr/include/libavutil/aes_ctr.h: 33
class struct_AVAESCTR(Structure):
    pass

# /usr/include/libavutil/aes_ctr.h: 38
if _libs["avutil"].has("av_aes_ctr_alloc", "cdecl"):
    av_aes_ctr_alloc = _libs["avutil"].get("av_aes_ctr_alloc", "cdecl")
    av_aes_ctr_alloc.argtypes = []
    av_aes_ctr_alloc.restype = POINTER(struct_AVAESCTR)

# /usr/include/libavutil/aes_ctr.h: 44
if _libs["avutil"].has("av_aes_ctr_init", "cdecl"):
    av_aes_ctr_init = _libs["avutil"].get("av_aes_ctr_init", "cdecl")
    av_aes_ctr_init.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_init.restype = c_int

# /usr/include/libavutil/aes_ctr.h: 49
if _libs["avutil"].has("av_aes_ctr_free", "cdecl"):
    av_aes_ctr_free = _libs["avutil"].get("av_aes_ctr_free", "cdecl")
    av_aes_ctr_free.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_free.restype = None

# /usr/include/libavutil/aes_ctr.h: 57
if _libs["avutil"].has("av_aes_ctr_crypt", "cdecl"):
    av_aes_ctr_crypt = _libs["avutil"].get("av_aes_ctr_crypt", "cdecl")
    av_aes_ctr_crypt.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8), POINTER(c_uint8), c_int]
    av_aes_ctr_crypt.restype = None

# /usr/include/libavutil/aes_ctr.h: 62
if _libs["avutil"].has("av_aes_ctr_get_iv", "cdecl"):
    av_aes_ctr_get_iv = _libs["avutil"].get("av_aes_ctr_get_iv", "cdecl")
    av_aes_ctr_get_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_get_iv.restype = POINTER(c_uint8)

# /usr/include/libavutil/aes_ctr.h: 67
if _libs["avutil"].has("av_aes_ctr_set_random_iv", "cdecl"):
    av_aes_ctr_set_random_iv = _libs["avutil"].get("av_aes_ctr_set_random_iv", "cdecl")
    av_aes_ctr_set_random_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_set_random_iv.restype = None

# /usr/include/libavutil/aes_ctr.h: 72
if _libs["avutil"].has("av_aes_ctr_set_iv", "cdecl"):
    av_aes_ctr_set_iv = _libs["avutil"].get("av_aes_ctr_set_iv", "cdecl")
    av_aes_ctr_set_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_set_iv.restype = None

# /usr/include/libavutil/aes_ctr.h: 77
if _libs["avutil"].has("av_aes_ctr_set_full_iv", "cdecl"):
    av_aes_ctr_set_full_iv = _libs["avutil"].get("av_aes_ctr_set_full_iv", "cdecl")
    av_aes_ctr_set_full_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_set_full_iv.restype = None

# /usr/include/libavutil/aes_ctr.h: 82
if _libs["avutil"].has("av_aes_ctr_increment_iv", "cdecl"):
    av_aes_ctr_increment_iv = _libs["avutil"].get("av_aes_ctr_increment_iv", "cdecl")
    av_aes_ctr_increment_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_increment_iv.restype = None

# /usr/include/libavutil/aes.h: 35
try:
    av_aes_size = (c_int).in_dll(_libs["avutil"], "av_aes_size")
except:
    pass

# /usr/include/libavutil/aes.h: 37
class struct_AVAES(Structure):
    pass

# /usr/include/libavutil/aes.h: 42
if _libs["avutil"].has("av_aes_alloc", "cdecl"):
    av_aes_alloc = _libs["avutil"].get("av_aes_alloc", "cdecl")
    av_aes_alloc.argtypes = []
    av_aes_alloc.restype = POINTER(struct_AVAES)

# /usr/include/libavutil/aes.h: 49
if _libs["avutil"].has("av_aes_init", "cdecl"):
    av_aes_init = _libs["avutil"].get("av_aes_init", "cdecl")
    av_aes_init.argtypes = [POINTER(struct_AVAES), POINTER(c_uint8), c_int, c_int]
    av_aes_init.restype = c_int

# /usr/include/libavutil/aes.h: 59
if _libs["avutil"].has("av_aes_crypt", "cdecl"):
    av_aes_crypt = _libs["avutil"].get("av_aes_crypt", "cdecl")
    av_aes_crypt.argtypes = [POINTER(struct_AVAES), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_aes_crypt.restype = None

# /usr/include/libavutil/avutil.h: 171
if _libs["avutil"].has("avutil_version", "cdecl"):
    avutil_version = _libs["avutil"].get("avutil_version", "cdecl")
    avutil_version.argtypes = []
    avutil_version.restype = c_uint

# /usr/include/libavutil/avutil.h: 178
if _libs["avutil"].has("av_version_info", "cdecl"):
    av_version_info = _libs["avutil"].get("av_version_info", "cdecl")
    av_version_info.argtypes = []
    av_version_info.restype = c_char_p

# /usr/include/libavutil/avutil.h: 183
if _libs["avutil"].has("avutil_configuration", "cdecl"):
    avutil_configuration = _libs["avutil"].get("avutil_configuration", "cdecl")
    avutil_configuration.argtypes = []
    avutil_configuration.restype = c_char_p

# /usr/include/libavutil/avutil.h: 188
if _libs["avutil"].has("avutil_license", "cdecl"):
    avutil_license = _libs["avutil"].get("avutil_license", "cdecl")
    avutil_license.argtypes = []
    avutil_license.restype = c_char_p

enum_AVMediaType = c_int# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_UNKNOWN = (-1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_VIDEO = (AVMEDIA_TYPE_UNKNOWN + 1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_AUDIO = (AVMEDIA_TYPE_VIDEO + 1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_DATA = (AVMEDIA_TYPE_AUDIO + 1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_SUBTITLE = (AVMEDIA_TYPE_DATA + 1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_ATTACHMENT = (AVMEDIA_TYPE_SUBTITLE + 1)# /usr/include/libavutil/avutil.h: 199

AVMEDIA_TYPE_NB = (AVMEDIA_TYPE_ATTACHMENT + 1)# /usr/include/libavutil/avutil.h: 199

# /usr/include/libavutil/avutil.h: 213
if _libs["avutil"].has("av_get_media_type_string", "cdecl"):
    av_get_media_type_string = _libs["avutil"].get("av_get_media_type_string", "cdecl")
    av_get_media_type_string.argtypes = [enum_AVMediaType]
    av_get_media_type_string.restype = c_char_p

enum_AVPictureType = c_int# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_NONE = 0# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_I = (AV_PICTURE_TYPE_NONE + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_P = (AV_PICTURE_TYPE_I + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_B = (AV_PICTURE_TYPE_P + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_S = (AV_PICTURE_TYPE_B + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_SI = (AV_PICTURE_TYPE_S + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_SP = (AV_PICTURE_TYPE_SI + 1)# /usr/include/libavutil/avutil.h: 272

AV_PICTURE_TYPE_BI = (AV_PICTURE_TYPE_SP + 1)# /usr/include/libavutil/avutil.h: 272

# /usr/include/libavutil/avutil.h: 290
if _libs["avutil"].has("av_get_picture_type_char", "cdecl"):
    av_get_picture_type_char = _libs["avutil"].get("av_get_picture_type_char", "cdecl")
    av_get_picture_type_char.argtypes = [enum_AVPictureType]
    av_get_picture_type_char.restype = c_char

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

# /usr/include/libavutil/common.h: 186
if _libs["avutil"].has("av_log2", "cdecl"):
    av_log2 = _libs["avutil"].get("av_log2", "cdecl")
    av_log2.argtypes = [c_uint]
    av_log2.restype = c_int

# /usr/include/libavutil/common.h: 190
if _libs["avutil"].has("av_log2_16bit", "cdecl"):
    av_log2_16bit = _libs["avutil"].get("av_log2_16bit", "cdecl")
    av_log2_16bit.argtypes = [c_uint]
    av_log2_16bit.restype = c_int

# /usr/include/libavutil/common.h: 376
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /usr/include/libavutil/common.h: 395
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /usr/include/libavutil/error.h: 97
if _libs["avutil"].has("av_strerror", "cdecl"):
    av_strerror = _libs["avutil"].get("av_strerror", "cdecl")
    av_strerror.argtypes = [c_int, String, c_size_t]
    av_strerror.restype = c_int

# /usr/include/libavutil/mem.h: 202
if _libs["avutil"].has("av_malloc", "cdecl"):
    av_malloc = _libs["avutil"].get("av_malloc", "cdecl")
    av_malloc.argtypes = [c_size_t]
    av_malloc.restype = POINTER(c_ubyte)
    av_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 213
if _libs["avutil"].has("av_mallocz", "cdecl"):
    av_mallocz = _libs["avutil"].get("av_mallocz", "cdecl")
    av_mallocz.argtypes = [c_size_t]
    av_mallocz.restype = POINTER(c_ubyte)
    av_mallocz.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 226
if _libs["avutil"].has("av_malloc_array", "cdecl"):
    av_malloc_array = _libs["avutil"].get("av_malloc_array", "cdecl")
    av_malloc_array.argtypes = [c_size_t, c_size_t]
    av_malloc_array.restype = POINTER(c_ubyte)
    av_malloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 241
if _libs["avutil"].has("av_mallocz_array", "cdecl"):
    av_mallocz_array = _libs["avutil"].get("av_mallocz_array", "cdecl")
    av_mallocz_array.argtypes = [c_size_t, c_size_t]
    av_mallocz_array.restype = POINTER(c_ubyte)
    av_mallocz_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 248
if _libs["avutil"].has("av_calloc", "cdecl"):
    av_calloc = _libs["avutil"].get("av_calloc", "cdecl")
    av_calloc.argtypes = [c_size_t, c_size_t]
    av_calloc.restype = POINTER(c_ubyte)
    av_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 270
if _libs["avutil"].has("av_realloc", "cdecl"):
    av_realloc = _libs["avutil"].get("av_realloc", "cdecl")
    av_realloc.argtypes = [POINTER(None), c_size_t]
    av_realloc.restype = POINTER(c_ubyte)
    av_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 292
if _libs["avutil"].has("av_reallocp", "cdecl"):
    av_reallocp = _libs["avutil"].get("av_reallocp", "cdecl")
    av_reallocp.argtypes = [POINTER(None), c_size_t]
    av_reallocp.restype = c_int

# /usr/include/libavutil/mem.h: 309
if _libs["avutil"].has("av_realloc_f", "cdecl"):
    av_realloc_f = _libs["avutil"].get("av_realloc_f", "cdecl")
    av_realloc_f.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_f.restype = POINTER(c_ubyte)
    av_realloc_f.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 329
if _libs["avutil"].has("av_realloc_array", "cdecl"):
    av_realloc_array = _libs["avutil"].get("av_realloc_array", "cdecl")
    av_realloc_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_array.restype = POINTER(c_ubyte)
    av_realloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 348
if _libs["avutil"].has("av_reallocp_array", "cdecl"):
    av_reallocp_array = _libs["avutil"].get("av_reallocp_array", "cdecl")
    av_reallocp_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_reallocp_array.restype = c_int

# /usr/include/libavutil/mem.h: 382
if _libs["avutil"].has("av_fast_realloc", "cdecl"):
    av_fast_realloc = _libs["avutil"].get("av_fast_realloc", "cdecl")
    av_fast_realloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_realloc.restype = POINTER(c_ubyte)
    av_fast_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 413
if _libs["avutil"].has("av_fast_malloc", "cdecl"):
    av_fast_malloc = _libs["avutil"].get("av_fast_malloc", "cdecl")
    av_fast_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_malloc.restype = None

# /usr/include/libavutil/mem.h: 433
if _libs["avutil"].has("av_fast_mallocz", "cdecl"):
    av_fast_mallocz = _libs["avutil"].get("av_fast_mallocz", "cdecl")
    av_fast_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_mallocz.restype = None

# /usr/include/libavutil/mem.h: 446
if _libs["avutil"].has("av_free", "cdecl"):
    av_free = _libs["avutil"].get("av_free", "cdecl")
    av_free.argtypes = [POINTER(None)]
    av_free.restype = None

# /usr/include/libavutil/mem.h: 469
if _libs["avutil"].has("av_freep", "cdecl"):
    av_freep = _libs["avutil"].get("av_freep", "cdecl")
    av_freep.argtypes = [POINTER(None)]
    av_freep.restype = None

# /usr/include/libavutil/mem.h: 479
if _libs["avutil"].has("av_strdup", "cdecl"):
    av_strdup = _libs["avutil"].get("av_strdup", "cdecl")
    av_strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strdup.restype = ReturnString
    else:
        av_strdup.restype = String
        av_strdup.errcheck = ReturnString

# /usr/include/libavutil/mem.h: 490
if _libs["avutil"].has("av_strndup", "cdecl"):
    av_strndup = _libs["avutil"].get("av_strndup", "cdecl")
    av_strndup.argtypes = [String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strndup.restype = ReturnString
    else:
        av_strndup.restype = String
        av_strndup.errcheck = ReturnString

# /usr/include/libavutil/mem.h: 500
if _libs["avutil"].has("av_memdup", "cdecl"):
    av_memdup = _libs["avutil"].get("av_memdup", "cdecl")
    av_memdup.argtypes = [POINTER(None), c_size_t]
    av_memdup.restype = POINTER(c_ubyte)
    av_memdup.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 513
if _libs["avutil"].has("av_memcpy_backptr", "cdecl"):
    av_memcpy_backptr = _libs["avutil"].get("av_memcpy_backptr", "cdecl")
    av_memcpy_backptr.argtypes = [POINTER(c_uint8), c_int, c_int]
    av_memcpy_backptr.restype = None

# /usr/include/libavutil/mem.h: 615
if _libs["avutil"].has("av_dynarray_add", "cdecl"):
    av_dynarray_add = _libs["avutil"].get("av_dynarray_add", "cdecl")
    av_dynarray_add.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add.restype = None

# /usr/include/libavutil/mem.h: 628
if _libs["avutil"].has("av_dynarray_add_nofree", "cdecl"):
    av_dynarray_add_nofree = _libs["avutil"].get("av_dynarray_add_nofree", "cdecl")
    av_dynarray_add_nofree.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add_nofree.restype = c_int

# /usr/include/libavutil/mem.h: 653
if _libs["avutil"].has("av_dynarray2_add", "cdecl"):
    av_dynarray2_add = _libs["avutil"].get("av_dynarray2_add", "cdecl")
    av_dynarray2_add.argtypes = [POINTER(POINTER(None)), POINTER(c_int), c_size_t, POINTER(c_uint8)]
    av_dynarray2_add.restype = POINTER(c_ubyte)
    av_dynarray2_add.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 677
for _lib in _libs.values():
    try:
        t = (c_size_t).in_dll(_lib, "t")
        break
    except:
        pass

# /usr/include/libavutil/mem.h: 699
if _libs["avutil"].has("av_max_alloc", "cdecl"):
    av_max_alloc = _libs["avutil"].get("av_max_alloc", "cdecl")
    av_max_alloc.argtypes = [c_size_t]
    av_max_alloc.restype = None

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

# /usr/include/libavutil/rational.h: 73
for _lib in _libs.values():
    try:
        r = (AVRational).in_dll(_lib, "r")
        break
    except:
        pass

# /usr/include/libavutil/rational.h: 90
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /usr/include/libavutil/rational.h: 120
if _libs["avutil"].has("av_reduce", "cdecl"):
    av_reduce = _libs["avutil"].get("av_reduce", "cdecl")
    av_reduce.argtypes = [POINTER(c_int), POINTER(c_int), c_int64, c_int64, c_int64]
    av_reduce.restype = c_int

# /usr/include/libavutil/rational.h: 128
if _libs["avutil"].has("av_mul_q", "cdecl"):
    av_mul_q = _libs["avutil"].get("av_mul_q", "cdecl")
    av_mul_q.argtypes = [AVRational, AVRational]
    av_mul_q.restype = AVRational

# /usr/include/libavutil/rational.h: 136
if _libs["avutil"].has("av_div_q", "cdecl"):
    av_div_q = _libs["avutil"].get("av_div_q", "cdecl")
    av_div_q.argtypes = [AVRational, AVRational]
    av_div_q.restype = AVRational

# /usr/include/libavutil/rational.h: 144
if _libs["avutil"].has("av_add_q", "cdecl"):
    av_add_q = _libs["avutil"].get("av_add_q", "cdecl")
    av_add_q.argtypes = [AVRational, AVRational]
    av_add_q.restype = AVRational

# /usr/include/libavutil/rational.h: 152
if _libs["avutil"].has("av_sub_q", "cdecl"):
    av_sub_q = _libs["avutil"].get("av_sub_q", "cdecl")
    av_sub_q.argtypes = [AVRational, AVRational]
    av_sub_q.restype = AVRational

# /usr/include/libavutil/rational.h: 161
for _lib in _libs.values():
    try:
        r = (AVRational).in_dll(_lib, "r")
        break
    except:
        pass

# /usr/include/libavutil/rational.h: 176
if _libs["avutil"].has("av_d2q", "cdecl"):
    av_d2q = _libs["avutil"].get("av_d2q", "cdecl")
    av_d2q.argtypes = [c_double, c_int]
    av_d2q.restype = AVRational

# /usr/include/libavutil/rational.h: 188
if _libs["avutil"].has("av_nearer_q", "cdecl"):
    av_nearer_q = _libs["avutil"].get("av_nearer_q", "cdecl")
    av_nearer_q.argtypes = [AVRational, AVRational, AVRational]
    av_nearer_q.restype = c_int

# /usr/include/libavutil/rational.h: 197
if _libs["avutil"].has("av_find_nearest_q_idx", "cdecl"):
    av_find_nearest_q_idx = _libs["avutil"].get("av_find_nearest_q_idx", "cdecl")
    av_find_nearest_q_idx.argtypes = [AVRational, POINTER(AVRational)]
    av_find_nearest_q_idx.restype = c_int

# /usr/include/libavutil/rational.h: 208
if _libs["avutil"].has("av_q2intfloat", "cdecl"):
    av_q2intfloat = _libs["avutil"].get("av_q2intfloat", "cdecl")
    av_q2intfloat.argtypes = [AVRational]
    av_q2intfloat.restype = c_uint32

# /usr/include/libavutil/rational.h: 214
if _libs["avutil"].has("av_gcd_q", "cdecl"):
    av_gcd_q = _libs["avutil"].get("av_gcd_q", "cdecl")
    av_gcd_q.argtypes = [AVRational, AVRational, c_int, AVRational]
    av_gcd_q.restype = AVRational

# /usr/include/libavutil/intfloat.h: 27
class union_av_intfloat32(Union):
    pass

union_av_intfloat32.__slots__ = [
    'i',
    'f',
]
union_av_intfloat32._fields_ = [
    ('i', c_uint32),
    ('f', c_float),
]

# /usr/include/libavutil/intfloat.h: 32
class union_av_intfloat64(Union):
    pass

union_av_intfloat64.__slots__ = [
    'i',
    'f',
]
union_av_intfloat64._fields_ = [
    ('i', c_uint64),
    ('f', c_double),
]

# /usr/include/libavutil/intfloat.h: 42
for _lib in _libs.values():
    try:
        v = (union_av_intfloat32).in_dll(_lib, "v")
        break
    except:
        pass

# /usr/include/libavutil/intfloat.h: 52
for _lib in _libs.values():
    try:
        v = (union_av_intfloat32).in_dll(_lib, "v")
        break
    except:
        pass

# /usr/include/libavutil/intfloat.h: 62
for _lib in _libs.values():
    try:
        v = (union_av_intfloat64).in_dll(_lib, "v")
        break
    except:
        pass

# /usr/include/libavutil/intfloat.h: 72
for _lib in _libs.values():
    try:
        v = (union_av_intfloat64).in_dll(_lib, "v")
        break
    except:
        pass

enum_AVRounding = c_int# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_ZERO = 0# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_INF = 1# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_DOWN = 2# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_UP = 3# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_NEAR_INF = 5# /usr/include/libavutil/mathematics.h: 79

AV_ROUND_PASS_MINMAX = 8192# /usr/include/libavutil/mathematics.h: 79

# /usr/include/libavutil/mathematics.h: 118
if _libs["avutil"].has("av_gcd", "cdecl"):
    av_gcd = _libs["avutil"].get("av_gcd", "cdecl")
    av_gcd.argtypes = [c_int64, c_int64]
    av_gcd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 130
if _libs["avutil"].has("av_rescale", "cdecl"):
    av_rescale = _libs["avutil"].get("av_rescale", "cdecl")
    av_rescale.argtypes = [c_int64, c_int64, c_int64]
    av_rescale.restype = c_int64

# /usr/include/libavutil/mathematics.h: 140
if _libs["avutil"].has("av_rescale_rnd", "cdecl"):
    av_rescale_rnd = _libs["avutil"].get("av_rescale_rnd", "cdecl")
    av_rescale_rnd.argtypes = [c_int64, c_int64, c_int64, enum_AVRounding]
    av_rescale_rnd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 151
if _libs["avutil"].has("av_rescale_q", "cdecl"):
    av_rescale_q = _libs["avutil"].get("av_rescale_q", "cdecl")
    av_rescale_q.argtypes = [c_int64, AVRational, AVRational]
    av_rescale_q.restype = c_int64

# /usr/include/libavutil/mathematics.h: 160
if _libs["avutil"].has("av_rescale_q_rnd", "cdecl"):
    av_rescale_q_rnd = _libs["avutil"].get("av_rescale_q_rnd", "cdecl")
    av_rescale_q_rnd.argtypes = [c_int64, AVRational, AVRational, enum_AVRounding]
    av_rescale_q_rnd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 175
if _libs["avutil"].has("av_compare_ts", "cdecl"):
    av_compare_ts = _libs["avutil"].get("av_compare_ts", "cdecl")
    av_compare_ts.argtypes = [c_int64, AVRational, c_int64, AVRational]
    av_compare_ts.restype = c_int

# /usr/include/libavutil/mathematics.h: 195
if _libs["avutil"].has("av_compare_mod", "cdecl"):
    av_compare_mod = _libs["avutil"].get("av_compare_mod", "cdecl")
    av_compare_mod.argtypes = [c_uint64, c_uint64, c_uint64]
    av_compare_mod.restype = c_int64

# /usr/include/libavutil/mathematics.h: 222
if _libs["avutil"].has("av_rescale_delta", "cdecl"):
    av_rescale_delta = _libs["avutil"].get("av_rescale_delta", "cdecl")
    av_rescale_delta.argtypes = [AVRational, c_int64, AVRational, c_int, POINTER(c_int64), AVRational]
    av_rescale_delta.restype = c_int64

# /usr/include/libavutil/mathematics.h: 235
if _libs["avutil"].has("av_add_stable", "cdecl"):
    av_add_stable = _libs["avutil"].get("av_add_stable", "cdecl")
    av_add_stable.argtypes = [AVRational, c_int64, AVRational, c_int64]
    av_add_stable.restype = c_int64

enum_anon_25 = c_int# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_NA = 0# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_INPUT = (AV_CLASS_CATEGORY_NA + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_OUTPUT = (AV_CLASS_CATEGORY_INPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_MUXER = (AV_CLASS_CATEGORY_OUTPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEMUXER = (AV_CLASS_CATEGORY_MUXER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_ENCODER = (AV_CLASS_CATEGORY_DEMUXER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DECODER = (AV_CLASS_CATEGORY_ENCODER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_FILTER = (AV_CLASS_CATEGORY_DECODER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_BITSTREAM_FILTER = (AV_CLASS_CATEGORY_FILTER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_SWSCALER = (AV_CLASS_CATEGORY_BITSTREAM_FILTER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_SWRESAMPLER = (AV_CLASS_CATEGORY_SWSCALER + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT = 40# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_DEVICE_INPUT = (AV_CLASS_CATEGORY_DEVICE_OUTPUT + 1)# /usr/include/libavutil/log.h: 48

AV_CLASS_CATEGORY_NB = (AV_CLASS_CATEGORY_DEVICE_INPUT + 1)# /usr/include/libavutil/log.h: 48

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

# /usr/include/libavutil/log.h: 252
if _libs["avutil"].has("av_log", "cdecl"):
    _func = _libs["avutil"].get("av_log", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, String]
    av_log = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/log.h: 273
if _libs["avutil"].has("av_log_once", "cdecl"):
    _func = _libs["avutil"].get("av_log_once", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, c_int, POINTER(c_int), String]
    av_log_once = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/log.h: 291
if _libs["avutil"].has("av_vlog", "cdecl"):
    av_vlog = _libs["avutil"].get("av_vlog", "cdecl")
    av_vlog.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_vlog.restype = None

# /usr/include/libavutil/log.h: 300
if _libs["avutil"].has("av_log_get_level", "cdecl"):
    av_log_get_level = _libs["avutil"].get("av_log_get_level", "cdecl")
    av_log_get_level.argtypes = []
    av_log_get_level.restype = c_int

# /usr/include/libavutil/log.h: 309
if _libs["avutil"].has("av_log_set_level", "cdecl"):
    av_log_set_level = _libs["avutil"].get("av_log_set_level", "cdecl")
    av_log_set_level.argtypes = [c_int]
    av_log_set_level.restype = None

# /usr/include/libavutil/log.h: 321
if _libs["avutil"].has("av_log_set_callback", "cdecl"):
    av_log_set_callback = _libs["avutil"].get("av_log_set_callback", "cdecl")
    av_log_set_callback.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, String, c_void_p)]
    av_log_set_callback.restype = None

# /usr/include/libavutil/log.h: 336
if _libs["avutil"].has("av_log_default_callback", "cdecl"):
    av_log_default_callback = _libs["avutil"].get("av_log_default_callback", "cdecl")
    av_log_default_callback.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_log_default_callback.restype = None

# /usr/include/libavutil/log.h: 346
if _libs["avutil"].has("av_default_item_name", "cdecl"):
    av_default_item_name = _libs["avutil"].get("av_default_item_name", "cdecl")
    av_default_item_name.argtypes = [POINTER(None)]
    av_default_item_name.restype = c_char_p

# /usr/include/libavutil/log.h: 347
if _libs["avutil"].has("av_default_get_category", "cdecl"):
    av_default_get_category = _libs["avutil"].get("av_default_get_category", "cdecl")
    av_default_get_category.argtypes = [POINTER(None)]
    av_default_get_category.restype = AVClassCategory

# /usr/include/libavutil/log.h: 356
if _libs["avutil"].has("av_log_format_line", "cdecl"):
    av_log_format_line = _libs["avutil"].get("av_log_format_line", "cdecl")
    av_log_format_line.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line.restype = None

# /usr/include/libavutil/log.h: 373
if _libs["avutil"].has("av_log_format_line2", "cdecl"):
    av_log_format_line2 = _libs["avutil"].get("av_log_format_line2", "cdecl")
    av_log_format_line2.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line2.restype = c_int

# /usr/include/libavutil/log.h: 394
if _libs["avutil"].has("av_log_set_flags", "cdecl"):
    av_log_set_flags = _libs["avutil"].get("av_log_set_flags", "cdecl")
    av_log_set_flags.argtypes = [c_int]
    av_log_set_flags.restype = None

# /usr/include/libavutil/log.h: 395
if _libs["avutil"].has("av_log_get_flags", "cdecl"):
    av_log_get_flags = _libs["avutil"].get("av_log_get_flags", "cdecl")
    av_log_get_flags.argtypes = []
    av_log_get_flags.restype = c_int

enum_AVPixelFormat = c_int# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NONE = (-1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P = (AV_PIX_FMT_NONE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUYV422 = (AV_PIX_FMT_YUV420P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB24 = (AV_PIX_FMT_YUYV422 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR24 = (AV_PIX_FMT_RGB24 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P = (AV_PIX_FMT_BGR24 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P = (AV_PIX_FMT_YUV422P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV410P = (AV_PIX_FMT_YUV444P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV411P = (AV_PIX_FMT_YUV410P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY8 = (AV_PIX_FMT_YUV411P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_MONOWHITE = (AV_PIX_FMT_GRAY8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_MONOBLACK = (AV_PIX_FMT_MONOWHITE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_PAL8 = (AV_PIX_FMT_MONOBLACK + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVJ420P = (AV_PIX_FMT_PAL8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVJ422P = (AV_PIX_FMT_YUVJ420P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVJ444P = (AV_PIX_FMT_YUVJ422P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_UYVY422 = (AV_PIX_FMT_YUVJ444P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_UYYVYY411 = (AV_PIX_FMT_UYVY422 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR8 = (AV_PIX_FMT_UYYVYY411 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR4 = (AV_PIX_FMT_BGR8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR4_BYTE = (AV_PIX_FMT_BGR4 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB8 = (AV_PIX_FMT_BGR4_BYTE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB4 = (AV_PIX_FMT_RGB8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB4_BYTE = (AV_PIX_FMT_RGB4 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV12 = (AV_PIX_FMT_RGB4_BYTE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV21 = (AV_PIX_FMT_NV12 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_ARGB = (AV_PIX_FMT_NV21 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBA = (AV_PIX_FMT_ARGB + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_ABGR = (AV_PIX_FMT_RGBA + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGRA = (AV_PIX_FMT_ABGR + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY16BE = (AV_PIX_FMT_BGRA + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY16LE = (AV_PIX_FMT_GRAY16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV440P = (AV_PIX_FMT_GRAY16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVJ440P = (AV_PIX_FMT_YUV440P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P = (AV_PIX_FMT_YUVJ440P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB48BE = (AV_PIX_FMT_YUVA420P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB48LE = (AV_PIX_FMT_RGB48BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB565BE = (AV_PIX_FMT_RGB48LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB565LE = (AV_PIX_FMT_RGB565BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB555BE = (AV_PIX_FMT_RGB565LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB555LE = (AV_PIX_FMT_RGB555BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR565BE = (AV_PIX_FMT_RGB555LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR565LE = (AV_PIX_FMT_BGR565BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR555BE = (AV_PIX_FMT_BGR565LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR555LE = (AV_PIX_FMT_BGR555BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VAAPI_MOCO = (AV_PIX_FMT_BGR555LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VAAPI_IDCT = (AV_PIX_FMT_VAAPI_MOCO + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VAAPI_VLD = (AV_PIX_FMT_VAAPI_IDCT + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VAAPI = AV_PIX_FMT_VAAPI_VLD# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P16LE = (AV_PIX_FMT_VAAPI + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P16BE = (AV_PIX_FMT_YUV420P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P16LE = (AV_PIX_FMT_YUV420P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P16BE = (AV_PIX_FMT_YUV422P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P16LE = (AV_PIX_FMT_YUV422P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P16BE = (AV_PIX_FMT_YUV444P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_DXVA2_VLD = (AV_PIX_FMT_YUV444P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB444LE = (AV_PIX_FMT_DXVA2_VLD + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB444BE = (AV_PIX_FMT_RGB444LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR444LE = (AV_PIX_FMT_RGB444BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR444BE = (AV_PIX_FMT_BGR444LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YA8 = (AV_PIX_FMT_BGR444BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_Y400A = AV_PIX_FMT_YA8# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY8A = AV_PIX_FMT_YA8# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR48BE = (AV_PIX_FMT_GRAY8A + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR48LE = (AV_PIX_FMT_BGR48BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P9BE = (AV_PIX_FMT_BGR48LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P9LE = (AV_PIX_FMT_YUV420P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P10BE = (AV_PIX_FMT_YUV420P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P10LE = (AV_PIX_FMT_YUV420P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P10BE = (AV_PIX_FMT_YUV420P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P10LE = (AV_PIX_FMT_YUV422P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P9BE = (AV_PIX_FMT_YUV422P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P9LE = (AV_PIX_FMT_YUV444P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P10BE = (AV_PIX_FMT_YUV444P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P10LE = (AV_PIX_FMT_YUV444P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P9BE = (AV_PIX_FMT_YUV444P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P9LE = (AV_PIX_FMT_YUV422P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP = (AV_PIX_FMT_YUV422P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBR24P = AV_PIX_FMT_GBRP# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP9BE = (AV_PIX_FMT_GBR24P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP9LE = (AV_PIX_FMT_GBRP9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP10BE = (AV_PIX_FMT_GBRP9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP10LE = (AV_PIX_FMT_GBRP10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP16BE = (AV_PIX_FMT_GBRP10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP16LE = (AV_PIX_FMT_GBRP16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P = (AV_PIX_FMT_GBRP16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P = (AV_PIX_FMT_YUVA422P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P9BE = (AV_PIX_FMT_YUVA444P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P9LE = (AV_PIX_FMT_YUVA420P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P9BE = (AV_PIX_FMT_YUVA420P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P9LE = (AV_PIX_FMT_YUVA422P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P9BE = (AV_PIX_FMT_YUVA422P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P9LE = (AV_PIX_FMT_YUVA444P9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P10BE = (AV_PIX_FMT_YUVA444P9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P10LE = (AV_PIX_FMT_YUVA420P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P10BE = (AV_PIX_FMT_YUVA420P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P10LE = (AV_PIX_FMT_YUVA422P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P10BE = (AV_PIX_FMT_YUVA422P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P10LE = (AV_PIX_FMT_YUVA444P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P16BE = (AV_PIX_FMT_YUVA444P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA420P16LE = (AV_PIX_FMT_YUVA420P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P16BE = (AV_PIX_FMT_YUVA420P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P16LE = (AV_PIX_FMT_YUVA422P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P16BE = (AV_PIX_FMT_YUVA422P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P16LE = (AV_PIX_FMT_YUVA444P16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VDPAU = (AV_PIX_FMT_YUVA444P16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XYZ12LE = (AV_PIX_FMT_VDPAU + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XYZ12BE = (AV_PIX_FMT_XYZ12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV16 = (AV_PIX_FMT_XYZ12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV20LE = (AV_PIX_FMT_NV16 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV20BE = (AV_PIX_FMT_NV20LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBA64BE = (AV_PIX_FMT_NV20BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBA64LE = (AV_PIX_FMT_RGBA64BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGRA64BE = (AV_PIX_FMT_RGBA64LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGRA64LE = (AV_PIX_FMT_BGRA64BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YVYU422 = (AV_PIX_FMT_BGRA64LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YA16BE = (AV_PIX_FMT_YVYU422 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YA16LE = (AV_PIX_FMT_YA16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP = (AV_PIX_FMT_YA16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP16BE = (AV_PIX_FMT_GBRAP + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP16LE = (AV_PIX_FMT_GBRAP16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_QSV = (AV_PIX_FMT_GBRAP16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_MMAL = (AV_PIX_FMT_QSV + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_D3D11VA_VLD = (AV_PIX_FMT_MMAL + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_CUDA = (AV_PIX_FMT_D3D11VA_VLD + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_0RGB = (AV_PIX_FMT_CUDA + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGB0 = (AV_PIX_FMT_0RGB + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_0BGR = (AV_PIX_FMT_RGB0 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BGR0 = (AV_PIX_FMT_0BGR + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P12BE = (AV_PIX_FMT_BGR0 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P12LE = (AV_PIX_FMT_YUV420P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P14BE = (AV_PIX_FMT_YUV420P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV420P14LE = (AV_PIX_FMT_YUV420P14BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P12BE = (AV_PIX_FMT_YUV420P14LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P12LE = (AV_PIX_FMT_YUV422P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P14BE = (AV_PIX_FMT_YUV422P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV422P14LE = (AV_PIX_FMT_YUV422P14BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P12BE = (AV_PIX_FMT_YUV422P14LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P12LE = (AV_PIX_FMT_YUV444P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P14BE = (AV_PIX_FMT_YUV444P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV444P14LE = (AV_PIX_FMT_YUV444P14BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP12BE = (AV_PIX_FMT_YUV444P14LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP12LE = (AV_PIX_FMT_GBRP12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP14BE = (AV_PIX_FMT_GBRP12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRP14LE = (AV_PIX_FMT_GBRP14BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVJ411P = (AV_PIX_FMT_GBRP14LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR8 = (AV_PIX_FMT_YUVJ411P + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB8 = (AV_PIX_FMT_BAYER_BGGR8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG8 = (AV_PIX_FMT_BAYER_RGGB8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG8 = (AV_PIX_FMT_BAYER_GBRG8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR16LE = (AV_PIX_FMT_BAYER_GRBG8 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR16BE = (AV_PIX_FMT_BAYER_BGGR16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB16LE = (AV_PIX_FMT_BAYER_BGGR16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB16BE = (AV_PIX_FMT_BAYER_RGGB16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG16LE = (AV_PIX_FMT_BAYER_RGGB16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG16BE = (AV_PIX_FMT_BAYER_GBRG16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG16LE = (AV_PIX_FMT_BAYER_GBRG16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG16BE = (AV_PIX_FMT_BAYER_GRBG16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XVMC = (AV_PIX_FMT_BAYER_GRBG16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV440P10LE = (AV_PIX_FMT_XVMC + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV440P10BE = (AV_PIX_FMT_YUV440P10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV440P12LE = (AV_PIX_FMT_YUV440P10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUV440P12BE = (AV_PIX_FMT_YUV440P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_AYUV64LE = (AV_PIX_FMT_YUV440P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_AYUV64BE = (AV_PIX_FMT_AYUV64LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VIDEOTOOLBOX = (AV_PIX_FMT_AYUV64BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P010LE = (AV_PIX_FMT_VIDEOTOOLBOX + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P010BE = (AV_PIX_FMT_P010LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP12BE = (AV_PIX_FMT_P010BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP12LE = (AV_PIX_FMT_GBRAP12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP10BE = (AV_PIX_FMT_GBRAP12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAP10LE = (AV_PIX_FMT_GBRAP10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_MEDIACODEC = (AV_PIX_FMT_GBRAP10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY12BE = (AV_PIX_FMT_MEDIACODEC + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY12LE = (AV_PIX_FMT_GRAY12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY10BE = (AV_PIX_FMT_GRAY12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY10LE = (AV_PIX_FMT_GRAY10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P016LE = (AV_PIX_FMT_GRAY10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P016BE = (AV_PIX_FMT_P016LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_D3D11 = (AV_PIX_FMT_P016BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY9BE = (AV_PIX_FMT_D3D11 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY9LE = (AV_PIX_FMT_GRAY9BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRPF32BE = (AV_PIX_FMT_GRAY9LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRPF32LE = (AV_PIX_FMT_GBRPF32BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAPF32BE = (AV_PIX_FMT_GBRPF32LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GBRAPF32LE = (AV_PIX_FMT_GBRAPF32BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_DRM_PRIME = (AV_PIX_FMT_GBRAPF32LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_OPENCL = (AV_PIX_FMT_DRM_PRIME + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY14BE = (AV_PIX_FMT_OPENCL + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAY14LE = (AV_PIX_FMT_GRAY14BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAYF32BE = (AV_PIX_FMT_GRAY14LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_GRAYF32LE = (AV_PIX_FMT_GRAYF32BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P12BE = (AV_PIX_FMT_GRAYF32LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA422P12LE = (AV_PIX_FMT_YUVA422P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P12BE = (AV_PIX_FMT_YUVA422P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_YUVA444P12LE = (AV_PIX_FMT_YUVA444P12BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV24 = (AV_PIX_FMT_YUVA444P12LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NV42 = (AV_PIX_FMT_NV24 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VULKAN = (AV_PIX_FMT_NV42 + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_Y210BE = (AV_PIX_FMT_VULKAN + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_Y210LE = (AV_PIX_FMT_Y210BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_X2RGB10LE = (AV_PIX_FMT_Y210LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_X2RGB10BE = (AV_PIX_FMT_X2RGB10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NB = (AV_PIX_FMT_X2RGB10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

enum_AVColorPrimaries = c_int# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_RESERVED0 = 0# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_BT709 = 1# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_BT470M = 4# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_BT470BG = 5# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_FILM = 8# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_BT2020 = 9# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTE428 = 10# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTEST428_1 = AVCOL_PRI_SMPTE428# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTE431 = 11# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_SMPTE432 = 12# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_EBU3213 = 22# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_JEDEC_P22 = AVCOL_PRI_EBU3213# /usr/include/libavutil/pixfmt.h: 458

AVCOL_PRI_NB = (AVCOL_PRI_JEDEC_P22 + 1)# /usr/include/libavutil/pixfmt.h: 458

enum_AVColorTransferCharacteristic = c_int# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_RESERVED0 = 0# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_BT709 = 1# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_GAMMA22 = 4# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_GAMMA28 = 5# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_LINEAR = 8# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_LOG = 9# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_LOG_SQRT = 10# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_IEC61966_2_4 = 11# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_BT1361_ECG = 12# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_IEC61966_2_1 = 13# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_BT2020_10 = 14# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_BT2020_12 = 15# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTE2084 = 16# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTEST2084 = AVCOL_TRC_SMPTE2084# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTE428 = 17# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_SMPTEST428_1 = AVCOL_TRC_SMPTE428# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_ARIB_STD_B67 = 18# /usr/include/libavutil/pixfmt.h: 483

AVCOL_TRC_NB = (AVCOL_TRC_ARIB_STD_B67 + 1)# /usr/include/libavutil/pixfmt.h: 483

enum_AVColorSpace = c_int# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_RGB = 0# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_BT709 = 1# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_FCC = 4# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_BT470BG = 5# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_YCGCO = 8# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_YCOCG = AVCOL_SPC_YCGCO# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_BT2020_NCL = 9# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_BT2020_CL = 10# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_SMPTE2085 = 11# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_CHROMA_DERIVED_NCL = 12# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_CHROMA_DERIVED_CL = 13# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_ICTCP = 14# /usr/include/libavutil/pixfmt.h: 512

AVCOL_SPC_NB = (AVCOL_SPC_ICTCP + 1)# /usr/include/libavutil/pixfmt.h: 512

enum_AVColorRange = c_int# /usr/include/libavutil/pixfmt.h: 551

AVCOL_RANGE_UNSPECIFIED = 0# /usr/include/libavutil/pixfmt.h: 551

AVCOL_RANGE_MPEG = 1# /usr/include/libavutil/pixfmt.h: 551

AVCOL_RANGE_JPEG = 2# /usr/include/libavutil/pixfmt.h: 551

AVCOL_RANGE_NB = (AVCOL_RANGE_JPEG + 1)# /usr/include/libavutil/pixfmt.h: 551

enum_AVChromaLocation = c_int# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_UNSPECIFIED = 0# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_LEFT = 1# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_CENTER = 2# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_TOPLEFT = 3# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_TOP = 4# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_BOTTOMLEFT = 5# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_BOTTOM = 6# /usr/include/libavutil/pixfmt.h: 605

AVCHROMA_LOC_NB = (AVCHROMA_LOC_BOTTOM + 1)# /usr/include/libavutil/pixfmt.h: 605

# /usr/include/libavutil/avutil.h: 321
if _libs["avutil"].has("av_int_list_length_for_size", "cdecl"):
    av_int_list_length_for_size = _libs["avutil"].get("av_int_list_length_for_size", "cdecl")
    av_int_list_length_for_size.argtypes = [c_uint, POINTER(None), c_uint64]
    av_int_list_length_for_size.restype = c_uint

# /usr/include/libavutil/avutil.h: 339
if _libs["avutil"].has("av_fopen_utf8", "cdecl"):
    av_fopen_utf8 = _libs["avutil"].get("av_fopen_utf8", "cdecl")
    av_fopen_utf8.argtypes = [String, String]
    av_fopen_utf8.restype = POINTER(FILE)

# /usr/include/libavutil/avutil.h: 344
if _libs["avutil"].has("av_get_time_base_q", "cdecl"):
    av_get_time_base_q = _libs["avutil"].get("av_get_time_base_q", "cdecl")
    av_get_time_base_q.argtypes = []
    av_get_time_base_q.restype = AVRational

# /usr/include/libavutil/avutil.h: 358
if _libs["avutil"].has("av_fourcc_make_string", "cdecl"):
    av_fourcc_make_string = _libs["avutil"].get("av_fourcc_make_string", "cdecl")
    av_fourcc_make_string.argtypes = [String, c_uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        av_fourcc_make_string.restype = ReturnString
    else:
        av_fourcc_make_string.restype = String
        av_fourcc_make_string.errcheck = ReturnString

# /usr/include/libavutil/fifo.h: 35
class struct_AVFifoBuffer(Structure):
    pass

struct_AVFifoBuffer.__slots__ = [
    'buffer',
    'rptr',
    'wptr',
    'end',
    'rndx',
    'wndx',
]
struct_AVFifoBuffer._fields_ = [
    ('buffer', POINTER(c_uint8)),
    ('rptr', POINTER(c_uint8)),
    ('wptr', POINTER(c_uint8)),
    ('end', POINTER(c_uint8)),
    ('rndx', c_uint32),
    ('wndx', c_uint32),
]

AVFifoBuffer = struct_AVFifoBuffer# /usr/include/libavutil/fifo.h: 35

# /usr/include/libavutil/fifo.h: 42
if _libs["avutil"].has("av_fifo_alloc", "cdecl"):
    av_fifo_alloc = _libs["avutil"].get("av_fifo_alloc", "cdecl")
    av_fifo_alloc.argtypes = [c_uint]
    av_fifo_alloc.restype = POINTER(AVFifoBuffer)

# /usr/include/libavutil/fifo.h: 50
if _libs["avutil"].has("av_fifo_alloc_array", "cdecl"):
    av_fifo_alloc_array = _libs["avutil"].get("av_fifo_alloc_array", "cdecl")
    av_fifo_alloc_array.argtypes = [c_size_t, c_size_t]
    av_fifo_alloc_array.restype = POINTER(AVFifoBuffer)

# /usr/include/libavutil/fifo.h: 56
if _libs["avutil"].has("av_fifo_free", "cdecl"):
    av_fifo_free = _libs["avutil"].get("av_fifo_free", "cdecl")
    av_fifo_free.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_free.restype = None

# /usr/include/libavutil/fifo.h: 62
if _libs["avutil"].has("av_fifo_freep", "cdecl"):
    av_fifo_freep = _libs["avutil"].get("av_fifo_freep", "cdecl")
    av_fifo_freep.argtypes = [POINTER(POINTER(AVFifoBuffer))]
    av_fifo_freep.restype = None

# /usr/include/libavutil/fifo.h: 68
if _libs["avutil"].has("av_fifo_reset", "cdecl"):
    av_fifo_reset = _libs["avutil"].get("av_fifo_reset", "cdecl")
    av_fifo_reset.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_reset.restype = None

# /usr/include/libavutil/fifo.h: 76
if _libs["avutil"].has("av_fifo_size", "cdecl"):
    av_fifo_size = _libs["avutil"].get("av_fifo_size", "cdecl")
    av_fifo_size.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_size.restype = c_int

# /usr/include/libavutil/fifo.h: 84
if _libs["avutil"].has("av_fifo_space", "cdecl"):
    av_fifo_space = _libs["avutil"].get("av_fifo_space", "cdecl")
    av_fifo_space.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_space.restype = c_int

# /usr/include/libavutil/fifo.h: 95
if _libs["avutil"].has("av_fifo_generic_peek_at", "cdecl"):
    av_fifo_generic_peek_at = _libs["avutil"].get("av_fifo_generic_peek_at", "cdecl")
    av_fifo_generic_peek_at.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek_at.restype = c_int

# /usr/include/libavutil/fifo.h: 105
if _libs["avutil"].has("av_fifo_generic_peek", "cdecl"):
    av_fifo_generic_peek = _libs["avutil"].get("av_fifo_generic_peek", "cdecl")
    av_fifo_generic_peek.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek.restype = c_int

# /usr/include/libavutil/fifo.h: 114
if _libs["avutil"].has("av_fifo_generic_read", "cdecl"):
    av_fifo_generic_read = _libs["avutil"].get("av_fifo_generic_read", "cdecl")
    av_fifo_generic_read.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_read.restype = c_int

# /usr/include/libavutil/fifo.h: 129
if _libs["avutil"].has("av_fifo_generic_write", "cdecl"):
    av_fifo_generic_write = _libs["avutil"].get("av_fifo_generic_write", "cdecl")
    av_fifo_generic_write.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_write.restype = c_int

# /usr/include/libavutil/fifo.h: 139
if _libs["avutil"].has("av_fifo_realloc2", "cdecl"):
    av_fifo_realloc2 = _libs["avutil"].get("av_fifo_realloc2", "cdecl")
    av_fifo_realloc2.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_realloc2.restype = c_int

# /usr/include/libavutil/fifo.h: 150
if _libs["avutil"].has("av_fifo_grow", "cdecl"):
    av_fifo_grow = _libs["avutil"].get("av_fifo_grow", "cdecl")
    av_fifo_grow.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_grow.restype = c_int

# /usr/include/libavutil/fifo.h: 157
if _libs["avutil"].has("av_fifo_drain", "cdecl"):
    av_fifo_drain = _libs["avutil"].get("av_fifo_drain", "cdecl")
    av_fifo_drain.argtypes = [POINTER(AVFifoBuffer), c_int]
    av_fifo_drain.restype = None

# /usr/include/libavutil/fifo.h: 171
for _lib in _libs.values():
    try:
        ptr = (POINTER(c_uint8)).in_dll(_lib, "ptr")
        break
    except:
        pass

enum_AVSampleFormat = c_int# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_NONE = (-1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_U8 = (AV_SAMPLE_FMT_NONE + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S16 = (AV_SAMPLE_FMT_U8 + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S32 = (AV_SAMPLE_FMT_S16 + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_FLT = (AV_SAMPLE_FMT_S32 + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_DBL = (AV_SAMPLE_FMT_FLT + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_U8P = (AV_SAMPLE_FMT_DBL + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S16P = (AV_SAMPLE_FMT_U8P + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S32P = (AV_SAMPLE_FMT_S16P + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_FLTP = (AV_SAMPLE_FMT_S32P + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_DBLP = (AV_SAMPLE_FMT_FLTP + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S64 = (AV_SAMPLE_FMT_DBLP + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_S64P = (AV_SAMPLE_FMT_S64 + 1)# /usr/include/libavutil/samplefmt.h: 58

AV_SAMPLE_FMT_NB = (AV_SAMPLE_FMT_S64P + 1)# /usr/include/libavutil/samplefmt.h: 58

# /usr/include/libavutil/samplefmt.h: 81
if _libs["avutil"].has("av_get_sample_fmt_name", "cdecl"):
    av_get_sample_fmt_name = _libs["avutil"].get("av_get_sample_fmt_name", "cdecl")
    av_get_sample_fmt_name.argtypes = [enum_AVSampleFormat]
    av_get_sample_fmt_name.restype = c_char_p

# /usr/include/libavutil/samplefmt.h: 87
if _libs["avutil"].has("av_get_sample_fmt", "cdecl"):
    av_get_sample_fmt = _libs["avutil"].get("av_get_sample_fmt", "cdecl")
    av_get_sample_fmt.argtypes = [String]
    av_get_sample_fmt.restype = enum_AVSampleFormat

# /usr/include/libavutil/samplefmt.h: 95
if _libs["avutil"].has("av_get_alt_sample_fmt", "cdecl"):
    av_get_alt_sample_fmt = _libs["avutil"].get("av_get_alt_sample_fmt", "cdecl")
    av_get_alt_sample_fmt.argtypes = [enum_AVSampleFormat, c_int]
    av_get_alt_sample_fmt.restype = enum_AVSampleFormat

# /usr/include/libavutil/samplefmt.h: 106
if _libs["avutil"].has("av_get_packed_sample_fmt", "cdecl"):
    av_get_packed_sample_fmt = _libs["avutil"].get("av_get_packed_sample_fmt", "cdecl")
    av_get_packed_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_packed_sample_fmt.restype = enum_AVSampleFormat

# /usr/include/libavutil/samplefmt.h: 117
if _libs["avutil"].has("av_get_planar_sample_fmt", "cdecl"):
    av_get_planar_sample_fmt = _libs["avutil"].get("av_get_planar_sample_fmt", "cdecl")
    av_get_planar_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_planar_sample_fmt.restype = enum_AVSampleFormat

# /usr/include/libavutil/samplefmt.h: 131
if _libs["avutil"].has("av_get_sample_fmt_string", "cdecl"):
    av_get_sample_fmt_string = _libs["avutil"].get("av_get_sample_fmt_string", "cdecl")
    av_get_sample_fmt_string.argtypes = [String, c_int, enum_AVSampleFormat]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_sample_fmt_string.restype = ReturnString
    else:
        av_get_sample_fmt_string.restype = String
        av_get_sample_fmt_string.errcheck = ReturnString

# /usr/include/libavutil/samplefmt.h: 140
if _libs["avutil"].has("av_get_bytes_per_sample", "cdecl"):
    av_get_bytes_per_sample = _libs["avutil"].get("av_get_bytes_per_sample", "cdecl")
    av_get_bytes_per_sample.argtypes = [enum_AVSampleFormat]
    av_get_bytes_per_sample.restype = c_int

# /usr/include/libavutil/samplefmt.h: 148
if _libs["avutil"].has("av_sample_fmt_is_planar", "cdecl"):
    av_sample_fmt_is_planar = _libs["avutil"].get("av_sample_fmt_is_planar", "cdecl")
    av_sample_fmt_is_planar.argtypes = [enum_AVSampleFormat]
    av_sample_fmt_is_planar.restype = c_int

# /usr/include/libavutil/samplefmt.h: 160
if _libs["avutil"].has("av_samples_get_buffer_size", "cdecl"):
    av_samples_get_buffer_size = _libs["avutil"].get("av_samples_get_buffer_size", "cdecl")
    av_samples_get_buffer_size.argtypes = [POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_get_buffer_size.restype = c_int

# /usr/include/libavutil/samplefmt.h: 202
if _libs["avutil"].has("av_samples_fill_arrays", "cdecl"):
    av_samples_fill_arrays = _libs["avutil"].get("av_samples_fill_arrays", "cdecl")
    av_samples_fill_arrays.argtypes = [POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_fill_arrays.restype = c_int

# /usr/include/libavutil/samplefmt.h: 226
if _libs["avutil"].has("av_samples_alloc", "cdecl"):
    av_samples_alloc = _libs["avutil"].get("av_samples_alloc", "cdecl")
    av_samples_alloc.argtypes = [POINTER(POINTER(c_uint8)), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc.restype = c_int

# /usr/include/libavutil/samplefmt.h: 238
if _libs["avutil"].has("av_samples_alloc_array_and_samples", "cdecl"):
    av_samples_alloc_array_and_samples = _libs["avutil"].get("av_samples_alloc_array_and_samples", "cdecl")
    av_samples_alloc_array_and_samples.argtypes = [POINTER(POINTER(POINTER(c_uint8))), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc_array_and_samples.restype = c_int

# /usr/include/libavutil/samplefmt.h: 252
if _libs["avutil"].has("av_samples_copy", "cdecl"):
    av_samples_copy = _libs["avutil"].get("av_samples_copy", "cdecl")
    av_samples_copy.argtypes = [POINTER(POINTER(c_uint8)), POINTER(POINTER(c_uint8)), c_int, c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_copy.restype = c_int

# /usr/include/libavutil/samplefmt.h: 265
if _libs["avutil"].has("av_samples_set_silence", "cdecl"):
    av_samples_set_silence = _libs["avutil"].get("av_samples_set_silence", "cdecl")
    av_samples_set_silence.argtypes = [POINTER(POINTER(c_uint8)), c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_set_silence.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 49
class struct_AVAudioFifo(Structure):
    pass

AVAudioFifo = struct_AVAudioFifo# /usr/include/libavutil/audio_fifo.h: 49

# /usr/include/libavutil/audio_fifo.h: 56
if _libs["avutil"].has("av_audio_fifo_free", "cdecl"):
    av_audio_fifo_free = _libs["avutil"].get("av_audio_fifo_free", "cdecl")
    av_audio_fifo_free.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_free.restype = None

# /usr/include/libavutil/audio_fifo.h: 66
if _libs["avutil"].has("av_audio_fifo_alloc", "cdecl"):
    av_audio_fifo_alloc = _libs["avutil"].get("av_audio_fifo_alloc", "cdecl")
    av_audio_fifo_alloc.argtypes = [enum_AVSampleFormat, c_int, c_int]
    av_audio_fifo_alloc.restype = POINTER(AVAudioFifo)

# /usr/include/libavutil/audio_fifo.h: 77
if _libs["avutil"].has("av_audio_fifo_realloc", "cdecl"):
    av_audio_fifo_realloc = _libs["avutil"].get("av_audio_fifo_realloc", "cdecl")
    av_audio_fifo_realloc.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_realloc.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 95
if _libs["avutil"].has("av_audio_fifo_write", "cdecl"):
    av_audio_fifo_write = _libs["avutil"].get("av_audio_fifo_write", "cdecl")
    av_audio_fifo_write.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_write.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 111
if _libs["avutil"].has("av_audio_fifo_peek", "cdecl"):
    av_audio_fifo_peek = _libs["avutil"].get("av_audio_fifo_peek", "cdecl")
    av_audio_fifo_peek.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_peek.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 128
if _libs["avutil"].has("av_audio_fifo_peek_at", "cdecl"):
    av_audio_fifo_peek_at = _libs["avutil"].get("av_audio_fifo_peek_at", "cdecl")
    av_audio_fifo_peek_at.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int, c_int]
    av_audio_fifo_peek_at.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 144
if _libs["avutil"].has("av_audio_fifo_read", "cdecl"):
    av_audio_fifo_read = _libs["avutil"].get("av_audio_fifo_read", "cdecl")
    av_audio_fifo_read.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_read.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 155
if _libs["avutil"].has("av_audio_fifo_drain", "cdecl"):
    av_audio_fifo_drain = _libs["avutil"].get("av_audio_fifo_drain", "cdecl")
    av_audio_fifo_drain.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_drain.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 164
if _libs["avutil"].has("av_audio_fifo_reset", "cdecl"):
    av_audio_fifo_reset = _libs["avutil"].get("av_audio_fifo_reset", "cdecl")
    av_audio_fifo_reset.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_reset.restype = None

# /usr/include/libavutil/audio_fifo.h: 172
if _libs["avutil"].has("av_audio_fifo_size", "cdecl"):
    av_audio_fifo_size = _libs["avutil"].get("av_audio_fifo_size", "cdecl")
    av_audio_fifo_size.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_size.restype = c_int

# /usr/include/libavutil/audio_fifo.h: 180
if _libs["avutil"].has("av_audio_fifo_space", "cdecl"):
    av_audio_fifo_space = _libs["avutil"].get("av_audio_fifo_space", "cdecl")
    av_audio_fifo_space.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_space.restype = c_int

# /usr/include/libavutil/avassert.h: 73
if _libs["avutil"].has("av_assert0_fpu", "cdecl"):
    av_assert0_fpu = _libs["avutil"].get("av_assert0_fpu", "cdecl")
    av_assert0_fpu.argtypes = []
    av_assert0_fpu.restype = None

# /usr/include/libavutil/avstring.h: 43
if _libs["avutil"].has("av_strstart", "cdecl"):
    av_strstart = _libs["avutil"].get("av_strstart", "cdecl")
    av_strstart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_strstart.restype = c_int

# /usr/include/libavutil/avstring.h: 55
if _libs["avutil"].has("av_stristart", "cdecl"):
    av_stristart = _libs["avutil"].get("av_stristart", "cdecl")
    av_stristart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_stristart.restype = c_int

# /usr/include/libavutil/avstring.h: 69
if _libs["avutil"].has("av_stristr", "cdecl"):
    av_stristr = _libs["avutil"].get("av_stristr", "cdecl")
    av_stristr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_stristr.restype = ReturnString
    else:
        av_stristr.restype = String
        av_stristr.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 84
if _libs["avutil"].has("av_strnstr", "cdecl"):
    av_strnstr = _libs["avutil"].get("av_strnstr", "cdecl")
    av_strnstr.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strnstr.restype = ReturnString
    else:
        av_strnstr.restype = String
        av_strnstr.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 101
if _libs["avutil"].has("av_strlcpy", "cdecl"):
    av_strlcpy = _libs["avutil"].get("av_strlcpy", "cdecl")
    av_strlcpy.argtypes = [String, String, c_size_t]
    av_strlcpy.restype = c_size_t

# /usr/include/libavutil/avstring.h: 119
if _libs["avutil"].has("av_strlcat", "cdecl"):
    av_strlcat = _libs["avutil"].get("av_strlcat", "cdecl")
    av_strlcat.argtypes = [String, String, c_size_t]
    av_strlcat.restype = c_size_t

# /usr/include/libavutil/avstring.h: 133
if _libs["avutil"].has("av_strlcatf", "cdecl"):
    _func = _libs["avutil"].get("av_strlcatf", "cdecl")
    _restype = c_size_t
    _errcheck = None
    _argtypes = [String, c_size_t, String]
    av_strlcatf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/avstring.h: 143
for _lib in _libs.values():
    try:
        i = (c_size_t).in_dll(_lib, "i")
        break
    except:
        pass

# /usr/include/libavutil/avstring.h: 157
if _libs["avutil"].has("av_asprintf", "cdecl"):
    _func = _libs["avutil"].get("av_asprintf", "cdecl")
    _restype = String
    _errcheck = None
    _argtypes = [String]
    av_asprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/avstring.h: 165
if _libs["avutil"].has("av_d2str", "cdecl"):
    av_d2str = _libs["avutil"].get("av_d2str", "cdecl")
    av_d2str.argtypes = [c_double]
    if sizeof(c_int) == sizeof(c_void_p):
        av_d2str.restype = ReturnString
    else:
        av_d2str.restype = String
        av_d2str.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 182
if _libs["avutil"].has("av_get_token", "cdecl"):
    av_get_token = _libs["avutil"].get("av_get_token", "cdecl")
    av_get_token.argtypes = [POINTER(POINTER(c_char)), String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_token.restype = ReturnString
    else:
        av_get_token.restype = String
        av_get_token.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 206
if _libs["avutil"].has("av_strtok", "cdecl"):
    av_strtok = _libs["avutil"].get("av_strtok", "cdecl")
    av_strtok.argtypes = [String, String, POINTER(POINTER(c_char))]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strtok.restype = ReturnString
    else:
        av_strtok.restype = String
        av_strtok.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 266
if _libs["avutil"].has("av_strcasecmp", "cdecl"):
    av_strcasecmp = _libs["avutil"].get("av_strcasecmp", "cdecl")
    av_strcasecmp.argtypes = [String, String]
    av_strcasecmp.restype = c_int

# /usr/include/libavutil/avstring.h: 272
if _libs["avutil"].has("av_strncasecmp", "cdecl"):
    av_strncasecmp = _libs["avutil"].get("av_strncasecmp", "cdecl")
    av_strncasecmp.argtypes = [String, String, c_size_t]
    av_strncasecmp.restype = c_int

# /usr/include/libavutil/avstring.h: 278
if _libs["avutil"].has("av_strireplace", "cdecl"):
    av_strireplace = _libs["avutil"].get("av_strireplace", "cdecl")
    av_strireplace.argtypes = [String, String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strireplace.restype = ReturnString
    else:
        av_strireplace.restype = String
        av_strireplace.errcheck = ReturnString

# /usr/include/libavutil/avstring.h: 288
if _libs["avutil"].has("av_basename", "cdecl"):
    av_basename = _libs["avutil"].get("av_basename", "cdecl")
    av_basename.argtypes = [String]
    av_basename.restype = c_char_p

# /usr/include/libavutil/avstring.h: 298
if _libs["avutil"].has("av_dirname", "cdecl"):
    av_dirname = _libs["avutil"].get("av_dirname", "cdecl")
    av_dirname.argtypes = [String]
    av_dirname.restype = c_char_p

# /usr/include/libavutil/avstring.h: 311
if _libs["avutil"].has("av_match_name", "cdecl"):
    av_match_name = _libs["avutil"].get("av_match_name", "cdecl")
    av_match_name.argtypes = [String, String]
    av_match_name.restype = c_int

# /usr/include/libavutil/avstring.h: 321
if _libs["avutil"].has("av_append_path_component", "cdecl"):
    av_append_path_component = _libs["avutil"].get("av_append_path_component", "cdecl")
    av_append_path_component.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_append_path_component.restype = ReturnString
    else:
        av_append_path_component.restype = String
        av_append_path_component.errcheck = ReturnString

enum_AVEscapeMode = c_int# /usr/include/libavutil/avstring.h: 323

AV_ESCAPE_MODE_AUTO = 0# /usr/include/libavutil/avstring.h: 323

AV_ESCAPE_MODE_BACKSLASH = (AV_ESCAPE_MODE_AUTO + 1)# /usr/include/libavutil/avstring.h: 323

AV_ESCAPE_MODE_QUOTE = (AV_ESCAPE_MODE_BACKSLASH + 1)# /usr/include/libavutil/avstring.h: 323

AV_ESCAPE_MODE_XML = (AV_ESCAPE_MODE_QUOTE + 1)# /usr/include/libavutil/avstring.h: 323

# /usr/include/libavutil/avstring.h: 377
if _libs["avutil"].has("av_escape", "cdecl"):
    av_escape = _libs["avutil"].get("av_escape", "cdecl")
    av_escape.argtypes = [POINTER(POINTER(c_char)), String, String, enum_AVEscapeMode, c_int]
    av_escape.restype = c_int

# /usr/include/libavutil/avstring.h: 417
if _libs["avutil"].has("av_utf8_decode", "cdecl"):
    av_utf8_decode = _libs["avutil"].get("av_utf8_decode", "cdecl")
    av_utf8_decode.argtypes = [POINTER(c_int32), POINTER(POINTER(c_uint8)), POINTER(c_uint8), c_uint]
    av_utf8_decode.restype = c_int

# /usr/include/libavutil/avstring.h: 425
if _libs["avutil"].has("av_match_list", "cdecl"):
    av_match_list = _libs["avutil"].get("av_match_list", "cdecl")
    av_match_list.argtypes = [String, String, c_char]
    av_match_list.restype = c_int

# /usr/include/libavutil/avstring.h: 431
if _libs["avutil"].has("av_sscanf", "cdecl"):
    _func = _libs["avutil"].get("av_sscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    av_sscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/base64.h: 42
if _libs["avutil"].has("av_base64_decode", "cdecl"):
    av_base64_decode = _libs["avutil"].get("av_base64_decode", "cdecl")
    av_base64_decode.argtypes = [POINTER(c_uint8), String, c_int]
    av_base64_decode.restype = c_int

# /usr/include/libavutil/base64.h: 60
if _libs["avutil"].has("av_base64_encode", "cdecl"):
    av_base64_encode = _libs["avutil"].get("av_base64_encode", "cdecl")
    av_base64_encode.argtypes = [String, c_int, POINTER(c_uint8), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_base64_encode.restype = ReturnString
    else:
        av_base64_encode.restype = String
        av_base64_encode.errcheck = ReturnString

# /usr/include/libavutil/blowfish.h: 38
class struct_AVBlowfish(Structure):
    pass

struct_AVBlowfish.__slots__ = [
    'p',
    's',
]
struct_AVBlowfish._fields_ = [
    ('p', c_uint32 * int((16 + 2))),
    ('s', (c_uint32 * int(256)) * int(4)),
]

AVBlowfish = struct_AVBlowfish# /usr/include/libavutil/blowfish.h: 38

# /usr/include/libavutil/blowfish.h: 43
if _libs["avutil"].has("av_blowfish_alloc", "cdecl"):
    av_blowfish_alloc = _libs["avutil"].get("av_blowfish_alloc", "cdecl")
    av_blowfish_alloc.argtypes = []
    av_blowfish_alloc.restype = POINTER(AVBlowfish)

# /usr/include/libavutil/blowfish.h: 52
if _libs["avutil"].has("av_blowfish_init", "cdecl"):
    av_blowfish_init = _libs["avutil"].get("av_blowfish_init", "cdecl")
    av_blowfish_init.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint8), c_int]
    av_blowfish_init.restype = None

# /usr/include/libavutil/blowfish.h: 62
if _libs["avutil"].has("av_blowfish_crypt_ecb", "cdecl"):
    av_blowfish_crypt_ecb = _libs["avutil"].get("av_blowfish_crypt_ecb", "cdecl")
    av_blowfish_crypt_ecb.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint32), POINTER(c_uint32), c_int]
    av_blowfish_crypt_ecb.restype = None

# /usr/include/libavutil/blowfish.h: 75
if _libs["avutil"].has("av_blowfish_crypt", "cdecl"):
    av_blowfish_crypt = _libs["avutil"].get("av_blowfish_crypt", "cdecl")
    av_blowfish_crypt.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_blowfish_crypt.restype = None

# /usr/include/libavutil/bprint.h: 82
class struct_ff_pad_helper_AVBPrint(Structure):
    pass

struct_ff_pad_helper_AVBPrint.__slots__ = [
    'str',
    'len',
    'size',
    'size_max',
    'reserved_internal_buffer',
]
struct_ff_pad_helper_AVBPrint._fields_ = [
    ('str', String),
    ('len', c_uint),
    ('size', c_uint),
    ('size_max', c_uint),
    ('reserved_internal_buffer', c_char * int(1)),
]

# /usr/include/libavutil/bprint.h: 82
class struct_AVBPrint(Structure):
    pass

struct_AVBPrint.__slots__ = [
    'str',
    'len',
    'size',
    'size_max',
    'reserved_internal_buffer',
    'reserved_padding',
]
struct_AVBPrint._fields_ = [
    ('str', String),
    ('len', c_uint),
    ('size', c_uint),
    ('size_max', c_uint),
    ('reserved_internal_buffer', c_char * int(1)),
    ('reserved_padding', c_char * int((1024 - sizeof(struct_ff_pad_helper_AVBPrint)))),
]

AVBPrint = struct_AVBPrint# /usr/include/libavutil/bprint.h: 82

# /usr/include/libavutil/bprint.h: 111
if _libs["avutil"].has("av_bprint_init", "cdecl"):
    av_bprint_init = _libs["avutil"].get("av_bprint_init", "cdecl")
    av_bprint_init.argtypes = [POINTER(AVBPrint), c_uint, c_uint]
    av_bprint_init.restype = None

# /usr/include/libavutil/bprint.h: 122
if _libs["avutil"].has("av_bprint_init_for_buffer", "cdecl"):
    av_bprint_init_for_buffer = _libs["avutil"].get("av_bprint_init_for_buffer", "cdecl")
    av_bprint_init_for_buffer.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_init_for_buffer.restype = None

# /usr/include/libavutil/bprint.h: 127
if _libs["avutil"].has("av_bprintf", "cdecl"):
    _func = _libs["avutil"].get("av_bprintf", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(AVBPrint), String]
    av_bprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavutil/bprint.h: 132
if _libs["avutil"].has("av_vbprintf", "cdecl"):
    av_vbprintf = _libs["avutil"].get("av_vbprintf", "cdecl")
    av_vbprintf.argtypes = [POINTER(AVBPrint), String, c_void_p]
    av_vbprintf.restype = None

# /usr/include/libavutil/bprint.h: 137
if _libs["avutil"].has("av_bprint_chars", "cdecl"):
    av_bprint_chars = _libs["avutil"].get("av_bprint_chars", "cdecl")
    av_bprint_chars.argtypes = [POINTER(AVBPrint), c_char, c_uint]
    av_bprint_chars.restype = None

# /usr/include/libavutil/bprint.h: 146
if _libs["avutil"].has("av_bprint_append_data", "cdecl"):
    av_bprint_append_data = _libs["avutil"].get("av_bprint_append_data", "cdecl")
    av_bprint_append_data.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_append_data.restype = None

# /usr/include/libavutil/bprint.h: 148
class struct_tm(Structure):
    pass

# /usr/include/libavutil/bprint.h: 160
if _libs["avutil"].has("av_bprint_strftime", "cdecl"):
    av_bprint_strftime = _libs["avutil"].get("av_bprint_strftime", "cdecl")
    av_bprint_strftime.argtypes = [POINTER(AVBPrint), String, POINTER(struct_tm)]
    av_bprint_strftime.restype = None

# /usr/include/libavutil/bprint.h: 171
if _libs["avutil"].has("av_bprint_get_buffer", "cdecl"):
    av_bprint_get_buffer = _libs["avutil"].get("av_bprint_get_buffer", "cdecl")
    av_bprint_get_buffer.argtypes = [POINTER(AVBPrint), c_uint, POINTER(POINTER(c_ubyte)), POINTER(c_uint)]
    av_bprint_get_buffer.restype = None

# /usr/include/libavutil/bprint.h: 177
if _libs["avutil"].has("av_bprint_clear", "cdecl"):
    av_bprint_clear = _libs["avutil"].get("av_bprint_clear", "cdecl")
    av_bprint_clear.argtypes = [POINTER(AVBPrint)]
    av_bprint_clear.restype = None

# /usr/include/libavutil/bprint.h: 201
if _libs["avutil"].has("av_bprint_finalize", "cdecl"):
    av_bprint_finalize = _libs["avutil"].get("av_bprint_finalize", "cdecl")
    av_bprint_finalize.argtypes = [POINTER(AVBPrint), POINTER(POINTER(c_char))]
    av_bprint_finalize.restype = c_int

# /usr/include/libavutil/bprint.h: 216
if _libs["avutil"].has("av_bprint_escape", "cdecl"):
    av_bprint_escape = _libs["avutil"].get("av_bprint_escape", "cdecl")
    av_bprint_escape.argtypes = [POINTER(AVBPrint), String, String, enum_AVEscapeMode, c_int]
    av_bprint_escape.restype = None

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

# /usr/include/libavutil/buffer.h: 109
if _libs["avutil"].has("av_buffer_alloc", "cdecl"):
    av_buffer_alloc = _libs["avutil"].get("av_buffer_alloc", "cdecl")
    av_buffer_alloc.argtypes = [c_int]
    av_buffer_alloc.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 119
if _libs["avutil"].has("av_buffer_allocz", "cdecl"):
    av_buffer_allocz = _libs["avutil"].get("av_buffer_allocz", "cdecl")
    av_buffer_allocz.argtypes = [c_int]
    av_buffer_allocz.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 146
if _libs["avutil"].has("av_buffer_create", "cdecl"):
    av_buffer_create = _libs["avutil"].get("av_buffer_create", "cdecl")
    av_buffer_create.argtypes = [POINTER(c_uint8), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(c_uint8)), POINTER(None), c_int]
    av_buffer_create.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 158
if _libs["avutil"].has("av_buffer_default_free", "cdecl"):
    av_buffer_default_free = _libs["avutil"].get("av_buffer_default_free", "cdecl")
    av_buffer_default_free.argtypes = [POINTER(None), POINTER(c_uint8)]
    av_buffer_default_free.restype = None

# /usr/include/libavutil/buffer.h: 166
if _libs["avutil"].has("av_buffer_ref", "cdecl"):
    av_buffer_ref = _libs["avutil"].get("av_buffer_ref", "cdecl")
    av_buffer_ref.argtypes = [POINTER(AVBufferRef)]
    av_buffer_ref.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 174
if _libs["avutil"].has("av_buffer_unref", "cdecl"):
    av_buffer_unref = _libs["avutil"].get("av_buffer_unref", "cdecl")
    av_buffer_unref.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_unref.restype = None

# /usr/include/libavutil/buffer.h: 182
if _libs["avutil"].has("av_buffer_is_writable", "cdecl"):
    av_buffer_is_writable = _libs["avutil"].get("av_buffer_is_writable", "cdecl")
    av_buffer_is_writable.argtypes = [POINTER(AVBufferRef)]
    av_buffer_is_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 187
if _libs["avutil"].has("av_buffer_get_opaque", "cdecl"):
    av_buffer_get_opaque = _libs["avutil"].get("av_buffer_get_opaque", "cdecl")
    av_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/buffer.h: 189
if _libs["avutil"].has("av_buffer_get_ref_count", "cdecl"):
    av_buffer_get_ref_count = _libs["avutil"].get("av_buffer_get_ref_count", "cdecl")
    av_buffer_get_ref_count.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_ref_count.restype = c_int

# /usr/include/libavutil/buffer.h: 200
if _libs["avutil"].has("av_buffer_make_writable", "cdecl"):
    av_buffer_make_writable = _libs["avutil"].get("av_buffer_make_writable", "cdecl")
    av_buffer_make_writable.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_make_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 218
if _libs["avutil"].has("av_buffer_realloc", "cdecl"):
    av_buffer_realloc = _libs["avutil"].get("av_buffer_realloc", "cdecl")
    av_buffer_realloc.argtypes = [POINTER(POINTER(AVBufferRef)), c_int]
    av_buffer_realloc.restype = c_int

# /usr/include/libavutil/buffer.h: 237
if _libs["avutil"].has("av_buffer_replace", "cdecl"):
    av_buffer_replace = _libs["avutil"].get("av_buffer_replace", "cdecl")
    av_buffer_replace.argtypes = [POINTER(POINTER(AVBufferRef)), POINTER(AVBufferRef)]
    av_buffer_replace.restype = c_int

# /usr/include/libavutil/buffer.h: 277
class struct_AVBufferPool(Structure):
    pass

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 277

# /usr/include/libavutil/buffer.h: 289
if _libs["avutil"].has("av_buffer_pool_init", "cdecl"):
    av_buffer_pool_init = _libs["avutil"].get("av_buffer_pool_init", "cdecl")
    av_buffer_pool_init.argtypes = [c_int, CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), c_int)]
    av_buffer_pool_init.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 310
if _libs["avutil"].has("av_buffer_pool_init2", "cdecl"):
    av_buffer_pool_init2 = _libs["avutil"].get("av_buffer_pool_init2", "cdecl")
    av_buffer_pool_init2.argtypes = [c_int, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), POINTER(None), c_int), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    av_buffer_pool_init2.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 326
if _libs["avutil"].has("av_buffer_pool_uninit", "cdecl"):
    av_buffer_pool_uninit = _libs["avutil"].get("av_buffer_pool_uninit", "cdecl")
    av_buffer_pool_uninit.argtypes = [POINTER(POINTER(AVBufferPool))]
    av_buffer_pool_uninit.restype = None

# /usr/include/libavutil/buffer.h: 334
if _libs["avutil"].has("av_buffer_pool_get", "cdecl"):
    av_buffer_pool_get = _libs["avutil"].get("av_buffer_pool_get", "cdecl")
    av_buffer_pool_get.argtypes = [POINTER(AVBufferPool)]
    av_buffer_pool_get.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 347
if _libs["avutil"].has("av_buffer_pool_buffer_get_opaque", "cdecl"):
    av_buffer_pool_buffer_get_opaque = _libs["avutil"].get("av_buffer_pool_buffer_get_opaque", "cdecl")
    av_buffer_pool_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_pool_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_pool_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/camellia.h: 36
try:
    av_camellia_size = (c_int).in_dll(_libs["avutil"], "av_camellia_size")
except:
    pass

# /usr/include/libavutil/camellia.h: 38
class struct_AVCAMELLIA(Structure):
    pass

# /usr/include/libavutil/camellia.h: 44
if _libs["avutil"].has("av_camellia_alloc", "cdecl"):
    av_camellia_alloc = _libs["avutil"].get("av_camellia_alloc", "cdecl")
    av_camellia_alloc.argtypes = []
    av_camellia_alloc.restype = POINTER(struct_AVCAMELLIA)

# /usr/include/libavutil/camellia.h: 53
if _libs["avutil"].has("av_camellia_init", "cdecl"):
    av_camellia_init = _libs["avutil"].get("av_camellia_init", "cdecl")
    av_camellia_init.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(c_uint8), c_int]
    av_camellia_init.restype = c_int

# /usr/include/libavutil/camellia.h: 65
if _libs["avutil"].has("av_camellia_crypt", "cdecl"):
    av_camellia_crypt = _libs["avutil"].get("av_camellia_crypt", "cdecl")
    av_camellia_crypt.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_camellia_crypt.restype = None

# /usr/include/libavutil/cast5.h: 36
try:
    av_cast5_size = (c_int).in_dll(_libs["avutil"], "av_cast5_size")
except:
    pass

# /usr/include/libavutil/cast5.h: 38
class struct_AVCAST5(Structure):
    pass

# /usr/include/libavutil/cast5.h: 44
if _libs["avutil"].has("av_cast5_alloc", "cdecl"):
    av_cast5_alloc = _libs["avutil"].get("av_cast5_alloc", "cdecl")
    av_cast5_alloc.argtypes = []
    av_cast5_alloc.restype = POINTER(struct_AVCAST5)

# /usr/include/libavutil/cast5.h: 53
if _libs["avutil"].has("av_cast5_init", "cdecl"):
    av_cast5_init = _libs["avutil"].get("av_cast5_init", "cdecl")
    av_cast5_init.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), c_int]
    av_cast5_init.restype = c_int

# /usr/include/libavutil/cast5.h: 64
if _libs["avutil"].has("av_cast5_crypt", "cdecl"):
    av_cast5_crypt = _libs["avutil"].get("av_cast5_crypt", "cdecl")
    av_cast5_crypt.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), POINTER(c_uint8), c_int, c_int]
    av_cast5_crypt.restype = None

# /usr/include/libavutil/cast5.h: 76
if _libs["avutil"].has("av_cast5_crypt2", "cdecl"):
    av_cast5_crypt2 = _libs["avutil"].get("av_cast5_crypt2", "cdecl")
    av_cast5_crypt2.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_cast5_crypt2.restype = None

enum_AVMatrixEncoding = c_int# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_NONE = 0# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DOLBY = (AV_MATRIX_ENCODING_NONE + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DPLII = (AV_MATRIX_ENCODING_DOLBY + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DPLIIX = (AV_MATRIX_ENCODING_DPLII + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DPLIIZ = (AV_MATRIX_ENCODING_DPLIIX + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DOLBYEX = (AV_MATRIX_ENCODING_DPLIIZ + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_DOLBYHEADPHONE = (AV_MATRIX_ENCODING_DOLBYEX + 1)# /usr/include/libavutil/channel_layout.h: 120

AV_MATRIX_ENCODING_NB = (AV_MATRIX_ENCODING_DOLBYHEADPHONE + 1)# /usr/include/libavutil/channel_layout.h: 120

# /usr/include/libavutil/channel_layout.h: 148
if _libs["avutil"].has("av_get_channel_layout", "cdecl"):
    av_get_channel_layout = _libs["avutil"].get("av_get_channel_layout", "cdecl")
    av_get_channel_layout.argtypes = [String]
    av_get_channel_layout.restype = c_uint64

# /usr/include/libavutil/channel_layout.h: 162
if _libs["avutil"].has("av_get_extended_channel_layout", "cdecl"):
    av_get_extended_channel_layout = _libs["avutil"].get("av_get_extended_channel_layout", "cdecl")
    av_get_extended_channel_layout.argtypes = [String, POINTER(c_uint64), POINTER(c_int)]
    av_get_extended_channel_layout.restype = c_int

# /usr/include/libavutil/channel_layout.h: 171
if _libs["avutil"].has("av_get_channel_layout_string", "cdecl"):
    av_get_channel_layout_string = _libs["avutil"].get("av_get_channel_layout_string", "cdecl")
    av_get_channel_layout_string.argtypes = [String, c_int, c_int, c_uint64]
    av_get_channel_layout_string.restype = None

# /usr/include/libavutil/channel_layout.h: 177
if _libs["avutil"].has("av_bprint_channel_layout", "cdecl"):
    av_bprint_channel_layout = _libs["avutil"].get("av_bprint_channel_layout", "cdecl")
    av_bprint_channel_layout.argtypes = [POINTER(struct_AVBPrint), c_int, c_uint64]
    av_bprint_channel_layout.restype = None

# /usr/include/libavutil/channel_layout.h: 182
if _libs["avutil"].has("av_get_channel_layout_nb_channels", "cdecl"):
    av_get_channel_layout_nb_channels = _libs["avutil"].get("av_get_channel_layout_nb_channels", "cdecl")
    av_get_channel_layout_nb_channels.argtypes = [c_uint64]
    av_get_channel_layout_nb_channels.restype = c_int

# /usr/include/libavutil/channel_layout.h: 187
if _libs["avutil"].has("av_get_default_channel_layout", "cdecl"):
    av_get_default_channel_layout = _libs["avutil"].get("av_get_default_channel_layout", "cdecl")
    av_get_default_channel_layout.argtypes = [c_int]
    av_get_default_channel_layout.restype = c_int64

# /usr/include/libavutil/channel_layout.h: 198
if _libs["avutil"].has("av_get_channel_layout_channel_index", "cdecl"):
    av_get_channel_layout_channel_index = _libs["avutil"].get("av_get_channel_layout_channel_index", "cdecl")
    av_get_channel_layout_channel_index.argtypes = [c_uint64, c_uint64]
    av_get_channel_layout_channel_index.restype = c_int

# /usr/include/libavutil/channel_layout.h: 204
if _libs["avutil"].has("av_channel_layout_extract_channel", "cdecl"):
    av_channel_layout_extract_channel = _libs["avutil"].get("av_channel_layout_extract_channel", "cdecl")
    av_channel_layout_extract_channel.argtypes = [c_uint64, c_int]
    av_channel_layout_extract_channel.restype = c_uint64

# /usr/include/libavutil/channel_layout.h: 211
if _libs["avutil"].has("av_get_channel_name", "cdecl"):
    av_get_channel_name = _libs["avutil"].get("av_get_channel_name", "cdecl")
    av_get_channel_name.argtypes = [c_uint64]
    av_get_channel_name.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 219
if _libs["avutil"].has("av_get_channel_description", "cdecl"):
    av_get_channel_description = _libs["avutil"].get("av_get_channel_description", "cdecl")
    av_get_channel_description.argtypes = [c_uint64]
    av_get_channel_description.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 230
if _libs["avutil"].has("av_get_standard_channel_layout", "cdecl"):
    av_get_standard_channel_layout = _libs["avutil"].get("av_get_standard_channel_layout", "cdecl")
    av_get_standard_channel_layout.argtypes = [c_uint, POINTER(c_uint64), POINTER(POINTER(c_char))]
    av_get_standard_channel_layout.restype = c_int

# /usr/include/libavutil/cpu.h: 83
if _libs["avutil"].has("av_get_cpu_flags", "cdecl"):
    av_get_cpu_flags = _libs["avutil"].get("av_get_cpu_flags", "cdecl")
    av_get_cpu_flags.argtypes = []
    av_get_cpu_flags.restype = c_int

# /usr/include/libavutil/cpu.h: 89
if _libs["avutil"].has("av_force_cpu_flags", "cdecl"):
    av_force_cpu_flags = _libs["avutil"].get("av_force_cpu_flags", "cdecl")
    av_force_cpu_flags.argtypes = [c_int]
    av_force_cpu_flags.restype = None

# /usr/include/libavutil/cpu.h: 96
if _libs["avutil"].has("av_set_cpu_flags_mask", "cdecl"):
    av_set_cpu_flags_mask = _libs["avutil"].get("av_set_cpu_flags_mask", "cdecl")
    av_set_cpu_flags_mask.argtypes = [c_int]
    av_set_cpu_flags_mask.restype = None

# /usr/include/libavutil/cpu.h: 108
if _libs["avutil"].has("av_parse_cpu_flags", "cdecl"):
    av_parse_cpu_flags = _libs["avutil"].get("av_parse_cpu_flags", "cdecl")
    av_parse_cpu_flags.argtypes = [String]
    av_parse_cpu_flags.restype = c_int

# /usr/include/libavutil/cpu.h: 115
if _libs["avutil"].has("av_parse_cpu_caps", "cdecl"):
    av_parse_cpu_caps = _libs["avutil"].get("av_parse_cpu_caps", "cdecl")
    av_parse_cpu_caps.argtypes = [POINTER(c_uint), String]
    av_parse_cpu_caps.restype = c_int

# /usr/include/libavutil/cpu.h: 120
if _libs["avutil"].has("av_cpu_count", "cdecl"):
    av_cpu_count = _libs["avutil"].get("av_cpu_count", "cdecl")
    av_cpu_count.argtypes = []
    av_cpu_count.restype = c_int

# /usr/include/libavutil/cpu.h: 131
if _libs["avutil"].has("av_cpu_max_align", "cdecl"):
    av_cpu_max_align = _libs["avutil"].get("av_cpu_max_align", "cdecl")
    av_cpu_max_align.argtypes = []
    av_cpu_max_align.restype = c_size_t

AVCRC = c_uint32# /usr/include/libavutil/crc.h: 47

enum_anon_26 = c_int# /usr/include/libavutil/crc.h: 59

AV_CRC_8_ATM = 0# /usr/include/libavutil/crc.h: 59

AV_CRC_16_ANSI = (AV_CRC_8_ATM + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_16_CCITT = (AV_CRC_16_ANSI + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_32_IEEE = (AV_CRC_16_CCITT + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_32_IEEE_LE = (AV_CRC_32_IEEE + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_16_ANSI_LE = (AV_CRC_32_IEEE_LE + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_24_IEEE = (AV_CRC_16_ANSI_LE + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_8_EBU = (AV_CRC_24_IEEE + 1)# /usr/include/libavutil/crc.h: 59

AV_CRC_MAX = (AV_CRC_8_EBU + 1)# /usr/include/libavutil/crc.h: 59

AVCRCId = enum_anon_26# /usr/include/libavutil/crc.h: 59

# /usr/include/libavutil/crc.h: 77
if _libs["avutil"].has("av_crc_init", "cdecl"):
    av_crc_init = _libs["avutil"].get("av_crc_init", "cdecl")
    av_crc_init.argtypes = [POINTER(AVCRC), c_int, c_int, c_uint32, c_int]
    av_crc_init.restype = c_int

# /usr/include/libavutil/crc.h: 84
if _libs["avutil"].has("av_crc_get_table", "cdecl"):
    av_crc_get_table = _libs["avutil"].get("av_crc_get_table", "cdecl")
    av_crc_get_table.argtypes = [AVCRCId]
    av_crc_get_table.restype = POINTER(AVCRC)

# /usr/include/libavutil/crc.h: 93
if _libs["avutil"].has("av_crc", "cdecl"):
    av_crc = _libs["avutil"].get("av_crc", "cdecl")
    av_crc.argtypes = [POINTER(AVCRC), c_uint32, POINTER(c_uint8), c_size_t]
    av_crc.restype = c_uint32

# /usr/include/libavutil/des.h: 36
class struct_AVDES(Structure):
    pass

struct_AVDES.__slots__ = [
    'round_keys',
    'triple_des',
]
struct_AVDES._fields_ = [
    ('round_keys', (c_uint64 * int(16)) * int(3)),
    ('triple_des', c_int),
]

AVDES = struct_AVDES# /usr/include/libavutil/des.h: 36

# /usr/include/libavutil/des.h: 41
if _libs["avutil"].has("av_des_alloc", "cdecl"):
    av_des_alloc = _libs["avutil"].get("av_des_alloc", "cdecl")
    av_des_alloc.argtypes = []
    av_des_alloc.restype = POINTER(AVDES)

# /usr/include/libavutil/des.h: 50
if _libs["avutil"].has("av_des_init", "cdecl"):
    av_des_init = _libs["avutil"].get("av_des_init", "cdecl")
    av_des_init.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), c_int, c_int]
    av_des_init.restype = c_int

# /usr/include/libavutil/des.h: 62
if _libs["avutil"].has("av_des_crypt", "cdecl"):
    av_des_crypt = _libs["avutil"].get("av_des_crypt", "cdecl")
    av_des_crypt.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_des_crypt.restype = None

# /usr/include/libavutil/des.h: 71
if _libs["avutil"].has("av_des_mac", "cdecl"):
    av_des_mac = _libs["avutil"].get("av_des_mac", "cdecl")
    av_des_mac.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), POINTER(c_uint8), c_int]
    av_des_mac.restype = None

# /usr/include/libavutil/dict.h: 84
class struct_AVDictionaryEntry(Structure):
    pass

struct_AVDictionaryEntry.__slots__ = [
    'key',
    'value',
]
struct_AVDictionaryEntry._fields_ = [
    ('key', String),
    ('value', String),
]

AVDictionaryEntry = struct_AVDictionaryEntry# /usr/include/libavutil/dict.h: 84

# /usr/include/libavutil/dict.h: 86
class struct_AVDictionary(Structure):
    pass

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 86

# /usr/include/libavutil/dict.h: 103
if _libs["avutil"].has("av_dict_get", "cdecl"):
    av_dict_get = _libs["avutil"].get("av_dict_get", "cdecl")
    av_dict_get.argtypes = [POINTER(AVDictionary), String, POINTER(AVDictionaryEntry), c_int]
    av_dict_get.restype = POINTER(AVDictionaryEntry)

# /usr/include/libavutil/dict.h: 112
if _libs["avutil"].has("av_dict_count", "cdecl"):
    av_dict_count = _libs["avutil"].get("av_dict_count", "cdecl")
    av_dict_count.argtypes = [POINTER(AVDictionary)]
    av_dict_count.restype = c_int

# /usr/include/libavutil/dict.h: 130
if _libs["avutil"].has("av_dict_set", "cdecl"):
    av_dict_set = _libs["avutil"].get("av_dict_set", "cdecl")
    av_dict_set.argtypes = [POINTER(POINTER(AVDictionary)), String, String, c_int]
    av_dict_set.restype = c_int

# /usr/include/libavutil/dict.h: 138
if _libs["avutil"].has("av_dict_set_int", "cdecl"):
    av_dict_set_int = _libs["avutil"].get("av_dict_set_int", "cdecl")
    av_dict_set_int.argtypes = [POINTER(POINTER(AVDictionary)), String, c_int64, c_int]
    av_dict_set_int.restype = c_int

# /usr/include/libavutil/dict.h: 156
if _libs["avutil"].has("av_dict_parse_string", "cdecl"):
    av_dict_parse_string = _libs["avutil"].get("av_dict_parse_string", "cdecl")
    av_dict_parse_string.argtypes = [POINTER(POINTER(AVDictionary)), String, String, String, c_int]
    av_dict_parse_string.restype = c_int

# /usr/include/libavutil/dict.h: 170
if _libs["avutil"].has("av_dict_copy", "cdecl"):
    av_dict_copy = _libs["avutil"].get("av_dict_copy", "cdecl")
    av_dict_copy.argtypes = [POINTER(POINTER(AVDictionary)), POINTER(AVDictionary), c_int]
    av_dict_copy.restype = c_int

# /usr/include/libavutil/dict.h: 176
if _libs["avutil"].has("av_dict_free", "cdecl"):
    av_dict_free = _libs["avutil"].get("av_dict_free", "cdecl")
    # av_dict_free.argtypes = [POINTER(POINTER(AVDictionary))]
    av_dict_free.restype = None

# /usr/include/libavutil/dict.h: 193
if _libs["avutil"].has("av_dict_get_string", "cdecl"):
    av_dict_get_string = _libs["avutil"].get("av_dict_get_string", "cdecl")
    av_dict_get_string.argtypes = [POINTER(AVDictionary), POINTER(POINTER(c_char)), c_char, c_char]
    av_dict_get_string.restype = c_int

# /usr/include/libavutil/display.h: 88
if _libs["avutil"].has("av_display_rotation_get", "cdecl"):
    av_display_rotation_get = _libs["avutil"].get("av_display_rotation_get", "cdecl")
    av_display_rotation_get.argtypes = [c_int32 * int(9)]
    av_display_rotation_get.restype = c_double

# /usr/include/libavutil/display.h: 98
if _libs["avutil"].has("av_display_rotation_set", "cdecl"):
    av_display_rotation_set = _libs["avutil"].get("av_display_rotation_set", "cdecl")
    av_display_rotation_set.argtypes = [c_int32 * int(9), c_double]
    av_display_rotation_set.restype = None

# /usr/include/libavutil/display.h: 107
if _libs["avutil"].has("av_display_matrix_flip", "cdecl"):
    av_display_matrix_flip = _libs["avutil"].get("av_display_matrix_flip", "cdecl")
    av_display_matrix_flip.argtypes = [c_int32 * int(9), c_int, c_int]
    av_display_matrix_flip.restype = None

# /usr/include/libavutil/dovi_meta.h: 60
class struct_AVDOVIDecoderConfigurationRecord(Structure):
    pass

struct_AVDOVIDecoderConfigurationRecord.__slots__ = [
    'dv_version_major',
    'dv_version_minor',
    'dv_profile',
    'dv_level',
    'rpu_present_flag',
    'el_present_flag',
    'bl_present_flag',
    'dv_bl_signal_compatibility_id',
]
struct_AVDOVIDecoderConfigurationRecord._fields_ = [
    ('dv_version_major', c_uint8),
    ('dv_version_minor', c_uint8),
    ('dv_profile', c_uint8),
    ('dv_level', c_uint8),
    ('rpu_present_flag', c_uint8),
    ('el_present_flag', c_uint8),
    ('bl_present_flag', c_uint8),
    ('dv_bl_signal_compatibility_id', c_uint8),
]

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /usr/include/libavutil/dovi_meta.h: 60

# /usr/include/libavutil/dovi_meta.h: 68
if _libs["avutil"].has("av_dovi_alloc", "cdecl"):
    av_dovi_alloc = _libs["avutil"].get("av_dovi_alloc", "cdecl")
    av_dovi_alloc.argtypes = [POINTER(c_size_t)]
    av_dovi_alloc.restype = POINTER(AVDOVIDecoderConfigurationRecord)

enum_AVFrameSideDataType = c_int# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_PANSCAN = 0# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_A53_CC = (AV_FRAME_DATA_PANSCAN + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_STEREO3D = (AV_FRAME_DATA_A53_CC + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_MATRIXENCODING = (AV_FRAME_DATA_STEREO3D + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_DOWNMIX_INFO = (AV_FRAME_DATA_MATRIXENCODING + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_REPLAYGAIN = (AV_FRAME_DATA_DOWNMIX_INFO + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_DISPLAYMATRIX = (AV_FRAME_DATA_REPLAYGAIN + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_AFD = (AV_FRAME_DATA_DISPLAYMATRIX + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_MOTION_VECTORS = (AV_FRAME_DATA_AFD + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_SKIP_SAMPLES = (AV_FRAME_DATA_MOTION_VECTORS + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_AUDIO_SERVICE_TYPE = (AV_FRAME_DATA_SKIP_SAMPLES + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_MASTERING_DISPLAY_METADATA = (AV_FRAME_DATA_AUDIO_SERVICE_TYPE + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_GOP_TIMECODE = (AV_FRAME_DATA_MASTERING_DISPLAY_METADATA + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_SPHERICAL = (AV_FRAME_DATA_GOP_TIMECODE + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_CONTENT_LIGHT_LEVEL = (AV_FRAME_DATA_SPHERICAL + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_ICC_PROFILE = (AV_FRAME_DATA_CONTENT_LIGHT_LEVEL + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_QP_TABLE_PROPERTIES = (AV_FRAME_DATA_ICC_PROFILE + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_QP_TABLE_DATA = (AV_FRAME_DATA_QP_TABLE_PROPERTIES + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_S12M_TIMECODE = (AV_FRAME_DATA_QP_TABLE_DATA + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_DYNAMIC_HDR_PLUS = (AV_FRAME_DATA_S12M_TIMECODE + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_REGIONS_OF_INTEREST = (AV_FRAME_DATA_DYNAMIC_HDR_PLUS + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_VIDEO_ENC_PARAMS = (AV_FRAME_DATA_REGIONS_OF_INTEREST + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_SEI_UNREGISTERED = (AV_FRAME_DATA_VIDEO_ENC_PARAMS + 1)# /usr/include/libavutil/frame.h: 48

AV_FRAME_DATA_FILM_GRAIN_PARAMS = (AV_FRAME_DATA_SEI_UNREGISTERED + 1)# /usr/include/libavutil/frame.h: 48

enum_AVActiveFormatDescription = c_int# /usr/include/libavutil/frame.h: 203

AV_AFD_SAME = 8# /usr/include/libavutil/frame.h: 203

AV_AFD_4_3 = 9# /usr/include/libavutil/frame.h: 203

AV_AFD_16_9 = 10# /usr/include/libavutil/frame.h: 203

AV_AFD_14_9 = 11# /usr/include/libavutil/frame.h: 203

AV_AFD_4_3_SP_14_9 = 13# /usr/include/libavutil/frame.h: 203

AV_AFD_16_9_SP_14_9 = 14# /usr/include/libavutil/frame.h: 203

AV_AFD_SP_4_3 = 15# /usr/include/libavutil/frame.h: 203

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

# /usr/include/libavutil/frame.h: 286
class struct_AVRegionOfInterest(Structure):
    pass

struct_AVRegionOfInterest.__slots__ = [
    'self_size',
    'top',
    'bottom',
    'left',
    'right',
    'qoffset',
]
struct_AVRegionOfInterest._fields_ = [
    ('self_size', c_uint32),
    ('top', c_int),
    ('bottom', c_int),
    ('left', c_int),
    ('right', c_int),
    ('qoffset', AVRational),
]

AVRegionOfInterest = struct_AVRegionOfInterest# /usr/include/libavutil/frame.h: 286

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

# /usr/include/libavutil/frame.h: 706
if _libs["avutil"].has("av_frame_get_best_effort_timestamp", "cdecl"):
    av_frame_get_best_effort_timestamp = _libs["avutil"].get("av_frame_get_best_effort_timestamp", "cdecl")
    av_frame_get_best_effort_timestamp.argtypes = [POINTER(AVFrame)]
    av_frame_get_best_effort_timestamp.restype = c_int64

# /usr/include/libavutil/frame.h: 708
if _libs["avutil"].has("av_frame_set_best_effort_timestamp", "cdecl"):
    av_frame_set_best_effort_timestamp = _libs["avutil"].get("av_frame_set_best_effort_timestamp", "cdecl")
    av_frame_set_best_effort_timestamp.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_best_effort_timestamp.restype = None

# /usr/include/libavutil/frame.h: 710
if _libs["avutil"].has("av_frame_get_pkt_duration", "cdecl"):
    av_frame_get_pkt_duration = _libs["avutil"].get("av_frame_get_pkt_duration", "cdecl")
    av_frame_get_pkt_duration.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_duration.restype = c_int64

# /usr/include/libavutil/frame.h: 712
if _libs["avutil"].has("av_frame_set_pkt_duration", "cdecl"):
    av_frame_set_pkt_duration = _libs["avutil"].get("av_frame_set_pkt_duration", "cdecl")
    av_frame_set_pkt_duration.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_pkt_duration.restype = None

# /usr/include/libavutil/frame.h: 714
if _libs["avutil"].has("av_frame_get_pkt_pos", "cdecl"):
    av_frame_get_pkt_pos = _libs["avutil"].get("av_frame_get_pkt_pos", "cdecl")
    av_frame_get_pkt_pos.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_pos.restype = c_int64

# /usr/include/libavutil/frame.h: 716
if _libs["avutil"].has("av_frame_set_pkt_pos", "cdecl"):
    av_frame_set_pkt_pos = _libs["avutil"].get("av_frame_set_pkt_pos", "cdecl")
    av_frame_set_pkt_pos.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_pkt_pos.restype = None

# /usr/include/libavutil/frame.h: 718
if _libs["avutil"].has("av_frame_get_channel_layout", "cdecl"):
    av_frame_get_channel_layout = _libs["avutil"].get("av_frame_get_channel_layout", "cdecl")
    av_frame_get_channel_layout.argtypes = [POINTER(AVFrame)]
    av_frame_get_channel_layout.restype = c_int64

# /usr/include/libavutil/frame.h: 720
if _libs["avutil"].has("av_frame_set_channel_layout", "cdecl"):
    av_frame_set_channel_layout = _libs["avutil"].get("av_frame_set_channel_layout", "cdecl")
    av_frame_set_channel_layout.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_channel_layout.restype = None

# /usr/include/libavutil/frame.h: 722
if _libs["avutil"].has("av_frame_get_channels", "cdecl"):
    av_frame_get_channels = _libs["avutil"].get("av_frame_get_channels", "cdecl")
    av_frame_get_channels.argtypes = [POINTER(AVFrame)]
    av_frame_get_channels.restype = c_int

# /usr/include/libavutil/frame.h: 724
if _libs["avutil"].has("av_frame_set_channels", "cdecl"):
    av_frame_set_channels = _libs["avutil"].get("av_frame_set_channels", "cdecl")
    av_frame_set_channels.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_channels.restype = None

# /usr/include/libavutil/frame.h: 726
if _libs["avutil"].has("av_frame_get_sample_rate", "cdecl"):
    av_frame_get_sample_rate = _libs["avutil"].get("av_frame_get_sample_rate", "cdecl")
    av_frame_get_sample_rate.argtypes = [POINTER(AVFrame)]
    av_frame_get_sample_rate.restype = c_int

# /usr/include/libavutil/frame.h: 728
if _libs["avutil"].has("av_frame_set_sample_rate", "cdecl"):
    av_frame_set_sample_rate = _libs["avutil"].get("av_frame_set_sample_rate", "cdecl")
    av_frame_set_sample_rate.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_sample_rate.restype = None

# /usr/include/libavutil/frame.h: 730
if _libs["avutil"].has("av_frame_get_metadata", "cdecl"):
    av_frame_get_metadata = _libs["avutil"].get("av_frame_get_metadata", "cdecl")
    av_frame_get_metadata.argtypes = [POINTER(AVFrame)]
    av_frame_get_metadata.restype = POINTER(AVDictionary)

# /usr/include/libavutil/frame.h: 732
if _libs["avutil"].has("av_frame_set_metadata", "cdecl"):
    av_frame_set_metadata = _libs["avutil"].get("av_frame_set_metadata", "cdecl")
    av_frame_set_metadata.argtypes = [POINTER(AVFrame), POINTER(AVDictionary)]
    av_frame_set_metadata.restype = None

# /usr/include/libavutil/frame.h: 734
if _libs["avutil"].has("av_frame_get_decode_error_flags", "cdecl"):
    av_frame_get_decode_error_flags = _libs["avutil"].get("av_frame_get_decode_error_flags", "cdecl")
    av_frame_get_decode_error_flags.argtypes = [POINTER(AVFrame)]
    av_frame_get_decode_error_flags.restype = c_int

# /usr/include/libavutil/frame.h: 736
if _libs["avutil"].has("av_frame_set_decode_error_flags", "cdecl"):
    av_frame_set_decode_error_flags = _libs["avutil"].get("av_frame_set_decode_error_flags", "cdecl")
    av_frame_set_decode_error_flags.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_decode_error_flags.restype = None

# /usr/include/libavutil/frame.h: 738
if _libs["avutil"].has("av_frame_get_pkt_size", "cdecl"):
    av_frame_get_pkt_size = _libs["avutil"].get("av_frame_get_pkt_size", "cdecl")
    av_frame_get_pkt_size.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_size.restype = c_int

# /usr/include/libavutil/frame.h: 740
if _libs["avutil"].has("av_frame_set_pkt_size", "cdecl"):
    av_frame_set_pkt_size = _libs["avutil"].get("av_frame_set_pkt_size", "cdecl")
    av_frame_set_pkt_size.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_pkt_size.restype = None

# /usr/include/libavutil/frame.h: 743
if _libs["avutil"].has("av_frame_get_qp_table", "cdecl"):
    av_frame_get_qp_table = _libs["avutil"].get("av_frame_get_qp_table", "cdecl")
    av_frame_get_qp_table.argtypes = [POINTER(AVFrame), POINTER(c_int), POINTER(c_int)]
    av_frame_get_qp_table.restype = POINTER(c_int8)

# /usr/include/libavutil/frame.h: 745
if _libs["avutil"].has("av_frame_set_qp_table", "cdecl"):
    av_frame_set_qp_table = _libs["avutil"].get("av_frame_set_qp_table", "cdecl")
    av_frame_set_qp_table.argtypes = [POINTER(AVFrame), POINTER(AVBufferRef), c_int, c_int]
    av_frame_set_qp_table.restype = c_int

# /usr/include/libavutil/frame.h: 748
if _libs["avutil"].has("av_frame_get_colorspace", "cdecl"):
    av_frame_get_colorspace = _libs["avutil"].get("av_frame_get_colorspace", "cdecl")
    av_frame_get_colorspace.argtypes = [POINTER(AVFrame)]
    av_frame_get_colorspace.restype = enum_AVColorSpace

# /usr/include/libavutil/frame.h: 750
if _libs["avutil"].has("av_frame_set_colorspace", "cdecl"):
    av_frame_set_colorspace = _libs["avutil"].get("av_frame_set_colorspace", "cdecl")
    av_frame_set_colorspace.argtypes = [POINTER(AVFrame), enum_AVColorSpace]
    av_frame_set_colorspace.restype = None

# /usr/include/libavutil/frame.h: 752
if _libs["avutil"].has("av_frame_get_color_range", "cdecl"):
    av_frame_get_color_range = _libs["avutil"].get("av_frame_get_color_range", "cdecl")
    av_frame_get_color_range.argtypes = [POINTER(AVFrame)]
    av_frame_get_color_range.restype = enum_AVColorRange

# /usr/include/libavutil/frame.h: 754
if _libs["avutil"].has("av_frame_set_color_range", "cdecl"):
    av_frame_set_color_range = _libs["avutil"].get("av_frame_set_color_range", "cdecl")
    av_frame_set_color_range.argtypes = [POINTER(AVFrame), enum_AVColorRange]
    av_frame_set_color_range.restype = None

# /usr/include/libavutil/frame.h: 761
if _libs["avutil"].has("av_get_colorspace_name", "cdecl"):
    av_get_colorspace_name = _libs["avutil"].get("av_get_colorspace_name", "cdecl")
    av_get_colorspace_name.argtypes = [enum_AVColorSpace]
    av_get_colorspace_name.restype = c_char_p

# /usr/include/libavutil/frame.h: 773
if _libs["avutil"].has("av_frame_alloc", "cdecl"):
    av_frame_alloc = _libs["avutil"].get("av_frame_alloc", "cdecl")
    av_frame_alloc.argtypes = []
    av_frame_alloc.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 782
if _libs["avutil"].has("av_frame_free", "cdecl"):
    av_frame_free = _libs["avutil"].get("av_frame_free", "cdecl")
    av_frame_free.argtypes = [POINTER(POINTER(AVFrame))]
    av_frame_free.restype = None

# /usr/include/libavutil/frame.h: 799
if _libs["avutil"].has("av_frame_ref", "cdecl"):
    av_frame_ref = _libs["avutil"].get("av_frame_ref", "cdecl")
    av_frame_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_ref.restype = c_int

# /usr/include/libavutil/frame.h: 808
if _libs["avutil"].has("av_frame_clone", "cdecl"):
    av_frame_clone = _libs["avutil"].get("av_frame_clone", "cdecl")
    av_frame_clone.argtypes = [POINTER(AVFrame)]
    av_frame_clone.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 813
if _libs["avutil"].has("av_frame_unref", "cdecl"):
    av_frame_unref = _libs["avutil"].get("av_frame_unref", "cdecl")
    av_frame_unref.argtypes = [POINTER(AVFrame)]
    av_frame_unref.restype = None

# /usr/include/libavutil/frame.h: 822
if _libs["avutil"].has("av_frame_move_ref", "cdecl"):
    av_frame_move_ref = _libs["avutil"].get("av_frame_move_ref", "cdecl")
    av_frame_move_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_move_ref.restype = None

# /usr/include/libavutil/frame.h: 847
if _libs["avutil"].has("av_frame_get_buffer", "cdecl"):
    av_frame_get_buffer = _libs["avutil"].get("av_frame_get_buffer", "cdecl")
    av_frame_get_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_buffer.restype = c_int

# /usr/include/libavutil/frame.h: 861
if _libs["avutil"].has("av_frame_is_writable", "cdecl"):
    av_frame_is_writable = _libs["avutil"].get("av_frame_is_writable", "cdecl")
    av_frame_is_writable.argtypes = [POINTER(AVFrame)]
    av_frame_is_writable.restype = c_int

# /usr/include/libavutil/frame.h: 874
if _libs["avutil"].has("av_frame_make_writable", "cdecl"):
    av_frame_make_writable = _libs["avutil"].get("av_frame_make_writable", "cdecl")
    av_frame_make_writable.argtypes = [POINTER(AVFrame)]
    av_frame_make_writable.restype = c_int

# /usr/include/libavutil/frame.h: 887
if _libs["avutil"].has("av_frame_copy", "cdecl"):
    av_frame_copy = _libs["avutil"].get("av_frame_copy", "cdecl")
    av_frame_copy.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy.restype = c_int

# /usr/include/libavutil/frame.h: 897
if _libs["avutil"].has("av_frame_copy_props", "cdecl"):
    av_frame_copy_props = _libs["avutil"].get("av_frame_copy_props", "cdecl")
    av_frame_copy_props.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy_props.restype = c_int

# /usr/include/libavutil/frame.h: 907
if _libs["avutil"].has("av_frame_get_plane_buffer", "cdecl"):
    av_frame_get_plane_buffer = _libs["avutil"].get("av_frame_get_plane_buffer", "cdecl")
    av_frame_get_plane_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_plane_buffer.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/frame.h: 918
if _libs["avutil"].has("av_frame_new_side_data", "cdecl"):
    av_frame_new_side_data = _libs["avutil"].get("av_frame_new_side_data", "cdecl")
    av_frame_new_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, c_int]
    av_frame_new_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 938
if _libs["avutil"].has("av_frame_new_side_data_from_buf", "cdecl"):
    av_frame_new_side_data_from_buf = _libs["avutil"].get("av_frame_new_side_data_from_buf", "cdecl")
    av_frame_new_side_data_from_buf.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, POINTER(AVBufferRef)]
    av_frame_new_side_data_from_buf.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 946
if _libs["avutil"].has("av_frame_get_side_data", "cdecl"):
    av_frame_get_side_data = _libs["avutil"].get("av_frame_get_side_data", "cdecl")
    av_frame_get_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_get_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 952
if _libs["avutil"].has("av_frame_remove_side_data", "cdecl"):
    av_frame_remove_side_data = _libs["avutil"].get("av_frame_remove_side_data", "cdecl")
    av_frame_remove_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_remove_side_data.restype = None

enum_anon_27 = c_int# /usr/include/libavutil/frame.h: 958

AV_FRAME_CROP_UNALIGNED = (1 << 0)# /usr/include/libavutil/frame.h: 958

# /usr/include/libavutil/frame.h: 986
if _libs["avutil"].has("av_frame_apply_cropping", "cdecl"):
    av_frame_apply_cropping = _libs["avutil"].get("av_frame_apply_cropping", "cdecl")
    av_frame_apply_cropping.argtypes = [POINTER(AVFrame), c_int]
    av_frame_apply_cropping.restype = c_int

# /usr/include/libavutil/frame.h: 991
if _libs["avutil"].has("av_frame_side_data_name", "cdecl"):
    av_frame_side_data_name = _libs["avutil"].get("av_frame_side_data_name", "cdecl")
    av_frame_side_data_name.argtypes = [enum_AVFrameSideDataType]
    av_frame_side_data_name.restype = c_char_p

enum_AVDownmixType = c_int# /usr/include/libavutil/downmix_info.h: 44

AV_DOWNMIX_TYPE_UNKNOWN = 0# /usr/include/libavutil/downmix_info.h: 44

AV_DOWNMIX_TYPE_LORO = (AV_DOWNMIX_TYPE_UNKNOWN + 1)# /usr/include/libavutil/downmix_info.h: 44

AV_DOWNMIX_TYPE_LTRT = (AV_DOWNMIX_TYPE_LORO + 1)# /usr/include/libavutil/downmix_info.h: 44

AV_DOWNMIX_TYPE_DPLII = (AV_DOWNMIX_TYPE_LTRT + 1)# /usr/include/libavutil/downmix_info.h: 44

AV_DOWNMIX_TYPE_NB = (AV_DOWNMIX_TYPE_DPLII + 1)# /usr/include/libavutil/downmix_info.h: 44

# /usr/include/libavutil/downmix_info.h: 93
class struct_AVDownmixInfo(Structure):
    pass

struct_AVDownmixInfo.__slots__ = [
    'preferred_downmix_type',
    'center_mix_level',
    'center_mix_level_ltrt',
    'surround_mix_level',
    'surround_mix_level_ltrt',
    'lfe_mix_level',
]
struct_AVDownmixInfo._fields_ = [
    ('preferred_downmix_type', enum_AVDownmixType),
    ('center_mix_level', c_double),
    ('center_mix_level_ltrt', c_double),
    ('surround_mix_level', c_double),
    ('surround_mix_level_ltrt', c_double),
    ('lfe_mix_level', c_double),
]

AVDownmixInfo = struct_AVDownmixInfo# /usr/include/libavutil/downmix_info.h: 93

# /usr/include/libavutil/downmix_info.h: 105
if _libs["avutil"].has("av_downmix_info_update_side_data", "cdecl"):
    av_downmix_info_update_side_data = _libs["avutil"].get("av_downmix_info_update_side_data", "cdecl")
    av_downmix_info_update_side_data.argtypes = [POINTER(AVFrame)]
    av_downmix_info_update_side_data.restype = POINTER(AVDownmixInfo)

# /usr/include/libavutil/encryption_info.h: 35
class struct_AVSubsampleEncryptionInfo(Structure):
    pass

struct_AVSubsampleEncryptionInfo.__slots__ = [
    'bytes_of_clear_data',
    'bytes_of_protected_data',
]
struct_AVSubsampleEncryptionInfo._fields_ = [
    ('bytes_of_clear_data', c_uint),
    ('bytes_of_protected_data', c_uint),
]

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /usr/include/libavutil/encryption_info.h: 35

# /usr/include/libavutil/encryption_info.h: 81
class struct_AVEncryptionInfo(Structure):
    pass

struct_AVEncryptionInfo.__slots__ = [
    'scheme',
    'crypt_byte_block',
    'skip_byte_block',
    'key_id',
    'key_id_size',
    'iv',
    'iv_size',
    'subsamples',
    'subsample_count',
]
struct_AVEncryptionInfo._fields_ = [
    ('scheme', c_uint32),
    ('crypt_byte_block', c_uint32),
    ('skip_byte_block', c_uint32),
    ('key_id', POINTER(c_uint8)),
    ('key_id_size', c_uint32),
    ('iv', POINTER(c_uint8)),
    ('iv_size', c_uint32),
    ('subsamples', POINTER(AVSubsampleEncryptionInfo)),
    ('subsample_count', c_uint32),
]

AVEncryptionInfo = struct_AVEncryptionInfo# /usr/include/libavutil/encryption_info.h: 81

# /usr/include/libavutil/encryption_info.h: 88
class struct_AVEncryptionInitInfo(Structure):
    pass

struct_AVEncryptionInitInfo.__slots__ = [
    'system_id',
    'system_id_size',
    'key_ids',
    'num_key_ids',
    'key_id_size',
    'data',
    'data_size',
    'next',
]
struct_AVEncryptionInitInfo._fields_ = [
    ('system_id', POINTER(c_uint8)),
    ('system_id_size', c_uint32),
    ('key_ids', POINTER(POINTER(c_uint8))),
    ('num_key_ids', c_uint32),
    ('key_id_size', c_uint32),
    ('data', POINTER(c_uint8)),
    ('data_size', c_uint32),
    ('next', POINTER(struct_AVEncryptionInitInfo)),
]

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /usr/include/libavutil/encryption_info.h: 123

# /usr/include/libavutil/encryption_info.h: 136
if _libs["avutil"].has("av_encryption_info_alloc", "cdecl"):
    av_encryption_info_alloc = _libs["avutil"].get("av_encryption_info_alloc", "cdecl")
    av_encryption_info_alloc.argtypes = [c_uint32, c_uint32, c_uint32]
    av_encryption_info_alloc.restype = POINTER(AVEncryptionInfo)

# /usr/include/libavutil/encryption_info.h: 142
if _libs["avutil"].has("av_encryption_info_clone", "cdecl"):
    av_encryption_info_clone = _libs["avutil"].get("av_encryption_info_clone", "cdecl")
    av_encryption_info_clone.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_clone.restype = POINTER(AVEncryptionInfo)

# /usr/include/libavutil/encryption_info.h: 148
if _libs["avutil"].has("av_encryption_info_free", "cdecl"):
    av_encryption_info_free = _libs["avutil"].get("av_encryption_info_free", "cdecl")
    av_encryption_info_free.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_free.restype = None

# /usr/include/libavutil/encryption_info.h: 157
if _libs["avutil"].has("av_encryption_info_get_side_data", "cdecl"):
    av_encryption_info_get_side_data = _libs["avutil"].get("av_encryption_info_get_side_data", "cdecl")
    av_encryption_info_get_side_data.argtypes = [POINTER(c_uint8), c_size_t]
    av_encryption_info_get_side_data.restype = POINTER(AVEncryptionInfo)

# /usr/include/libavutil/encryption_info.h: 166
if _libs["avutil"].has("av_encryption_info_add_side_data", "cdecl"):
    av_encryption_info_add_side_data = _libs["avutil"].get("av_encryption_info_add_side_data", "cdecl")
    av_encryption_info_add_side_data.argtypes = [POINTER(AVEncryptionInfo), POINTER(c_size_t)]
    av_encryption_info_add_side_data.restype = POINTER(c_uint8)

# /usr/include/libavutil/encryption_info.h: 176
if _libs["avutil"].has("av_encryption_init_info_alloc", "cdecl"):
    av_encryption_init_info_alloc = _libs["avutil"].get("av_encryption_init_info_alloc", "cdecl")
    av_encryption_init_info_alloc.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
    av_encryption_init_info_alloc.restype = POINTER(AVEncryptionInitInfo)

# /usr/include/libavutil/encryption_info.h: 183
if _libs["avutil"].has("av_encryption_init_info_free", "cdecl"):
    av_encryption_init_info_free = _libs["avutil"].get("av_encryption_init_info_free", "cdecl")
    av_encryption_init_info_free.argtypes = [POINTER(AVEncryptionInitInfo)]
    av_encryption_init_info_free.restype = None

# /usr/include/libavutil/encryption_info.h: 192
if _libs["avutil"].has("av_encryption_init_info_get_side_data", "cdecl"):
    av_encryption_init_info_get_side_data = _libs["avutil"].get("av_encryption_init_info_get_side_data", "cdecl")
    av_encryption_init_info_get_side_data.argtypes = [POINTER(c_uint8), c_size_t]
    av_encryption_init_info_get_side_data.restype = POINTER(AVEncryptionInitInfo)

# /usr/include/libavutil/encryption_info.h: 202
if _libs["avutil"].has("av_encryption_init_info_add_side_data", "cdecl"):
    av_encryption_init_info_add_side_data = _libs["avutil"].get("av_encryption_init_info_add_side_data", "cdecl")
    av_encryption_init_info_add_side_data.argtypes = [POINTER(AVEncryptionInitInfo), POINTER(c_size_t)]
    av_encryption_init_info_add_side_data.restype = POINTER(c_uint8)

# /usr/include/libavutil/eval.h: 31
class struct_AVExpr(Structure):
    pass

AVExpr = struct_AVExpr# /usr/include/libavutil/eval.h: 31

# /usr/include/libavutil/eval.h: 51
if _libs["avutil"].has("av_expr_parse_and_eval", "cdecl"):
    av_expr_parse_and_eval = _libs["avutil"].get("av_expr_parse_and_eval", "cdecl")
    av_expr_parse_and_eval.argtypes = [POINTER(c_double), String, POINTER(POINTER(c_char)), POINTER(c_double), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), POINTER(None), c_int, POINTER(None)]
    av_expr_parse_and_eval.restype = c_int

# /usr/include/libavutil/eval.h: 74
if _libs["avutil"].has("av_expr_parse", "cdecl"):
    av_expr_parse = _libs["avutil"].get("av_expr_parse", "cdecl")
    av_expr_parse.argtypes = [POINTER(POINTER(AVExpr)), String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), c_int, POINTER(None)]
    av_expr_parse.restype = c_int

# /usr/include/libavutil/eval.h: 87
if _libs["avutil"].has("av_expr_eval", "cdecl"):
    av_expr_eval = _libs["avutil"].get("av_expr_eval", "cdecl")
    av_expr_eval.argtypes = [POINTER(AVExpr), POINTER(c_double), POINTER(None)]
    av_expr_eval.restype = c_double

# /usr/include/libavutil/eval.h: 97
if _libs["avutil"].has("av_expr_count_vars", "cdecl"):
    av_expr_count_vars = _libs["avutil"].get("av_expr_count_vars", "cdecl")
    av_expr_count_vars.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int]
    av_expr_count_vars.restype = c_int

# /usr/include/libavutil/eval.h: 111
if _libs["avutil"].has("av_expr_count_func", "cdecl"):
    av_expr_count_func = _libs["avutil"].get("av_expr_count_func", "cdecl")
    av_expr_count_func.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int, c_int]
    av_expr_count_func.restype = c_int

# /usr/include/libavutil/eval.h: 116
if _libs["avutil"].has("av_expr_free", "cdecl"):
    av_expr_free = _libs["avutil"].get("av_expr_free", "cdecl")
    av_expr_free.argtypes = [POINTER(AVExpr)]
    av_expr_free.restype = None

# /usr/include/libavutil/eval.h: 135
if _libs["avutil"].has("av_strtod", "cdecl"):
    av_strtod = _libs["avutil"].get("av_strtod", "cdecl")
    av_strtod.argtypes = [String, POINTER(POINTER(c_char))]
    av_strtod.restype = c_double

# /usr/include/libavutil/file.h: 46
if _libs["avutil"].has("av_file_map", "cdecl"):
    av_file_map = _libs["avutil"].get("av_file_map", "cdecl")
    av_file_map.argtypes = [String, POINTER(POINTER(c_uint8)), POINTER(c_size_t), c_int, POINTER(None)]
    av_file_map.restype = c_int

# /usr/include/libavutil/file.h: 55
if _libs["avutil"].has("av_file_unmap", "cdecl"):
    av_file_unmap = _libs["avutil"].get("av_file_unmap", "cdecl")
    av_file_unmap.argtypes = [POINTER(c_uint8), c_size_t]
    av_file_unmap.restype = None

# /usr/include/libavutil/file.h: 69
if _libs["avutil"].has("av_tempfile", "cdecl"):
    av_tempfile = _libs["avutil"].get("av_tempfile", "cdecl")
    av_tempfile.argtypes = [String, POINTER(POINTER(c_char)), c_int, POINTER(None)]
    av_tempfile.restype = c_int

enum_AVFilmGrainParamsType = c_int# /usr/include/libavutil/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_NONE = 0# /usr/include/libavutil/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_AV1 = (AV_FILM_GRAIN_PARAMS_NONE + 1)# /usr/include/libavutil/film_grain_params.h: 24

# /usr/include/libavutil/film_grain_params.h: 118
class struct_AVFilmGrainAOMParams(Structure):
    pass

struct_AVFilmGrainAOMParams.__slots__ = [
    'num_y_points',
    'y_points',
    'chroma_scaling_from_luma',
    'num_uv_points',
    'uv_points',
    'scaling_shift',
    'ar_coeff_lag',
    'ar_coeffs_y',
    'ar_coeffs_uv',
    'ar_coeff_shift',
    'grain_scale_shift',
    'uv_mult',
    'uv_mult_luma',
    'uv_offset',
    'overlap_flag',
    'limit_output_range',
]
struct_AVFilmGrainAOMParams._fields_ = [
    ('num_y_points', c_int),
    ('y_points', (c_uint8 * int(2)) * int(14)),
    ('chroma_scaling_from_luma', c_int),
    ('num_uv_points', c_int * int(2)),
    ('uv_points', ((c_uint8 * int(2)) * int(10)) * int(2)),
    ('scaling_shift', c_int),
    ('ar_coeff_lag', c_int),
    ('ar_coeffs_y', c_int8 * int(24)),
    ('ar_coeffs_uv', (c_int8 * int(25)) * int(2)),
    ('ar_coeff_shift', c_int),
    ('grain_scale_shift', c_int),
    ('uv_mult', c_int * int(2)),
    ('uv_mult_luma', c_int * int(2)),
    ('uv_offset', c_int * int(2)),
    ('overlap_flag', c_int),
    ('limit_output_range', c_int),
]

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /usr/include/libavutil/film_grain_params.h: 118

# /usr/include/libavutil/film_grain_params.h: 144
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'aom',
]
union_anon_28._fields_ = [
    ('aom', AVFilmGrainAOMParams),
]

# /usr/include/libavutil/film_grain_params.h: 147
class struct_AVFilmGrainParams(Structure):
    pass

struct_AVFilmGrainParams.__slots__ = [
    'type',
    'seed',
    'codec',
]
struct_AVFilmGrainParams._fields_ = [
    ('type', enum_AVFilmGrainParamsType),
    ('seed', c_uint64),
    ('codec', union_anon_28),
]

AVFilmGrainParams = struct_AVFilmGrainParams# /usr/include/libavutil/film_grain_params.h: 147

# /usr/include/libavutil/film_grain_params.h: 157
if _libs["avutil"].has("av_film_grain_params_alloc", "cdecl"):
    av_film_grain_params_alloc = _libs["avutil"].get("av_film_grain_params_alloc", "cdecl")
    av_film_grain_params_alloc.argtypes = [POINTER(c_size_t)]
    av_film_grain_params_alloc.restype = POINTER(AVFilmGrainParams)

# /usr/include/libavutil/film_grain_params.h: 166
if _libs["avutil"].has("av_film_grain_params_create_side_data", "cdecl"):
    av_film_grain_params_create_side_data = _libs["avutil"].get("av_film_grain_params_create_side_data", "cdecl")
    av_film_grain_params_create_side_data.argtypes = [POINTER(AVFrame)]
    av_film_grain_params_create_side_data.restype = POINTER(AVFilmGrainParams)

# /usr/include/libavutil/hash.h: 117
class struct_AVHashContext(Structure):
    pass

# /usr/include/libavutil/hash.h: 127
if _libs["avutil"].has("av_hash_alloc", "cdecl"):
    av_hash_alloc = _libs["avutil"].get("av_hash_alloc", "cdecl")
    av_hash_alloc.argtypes = [POINTER(POINTER(struct_AVHashContext)), String]
    av_hash_alloc.restype = c_int

# /usr/include/libavutil/hash.h: 137
if _libs["avutil"].has("av_hash_names", "cdecl"):
    av_hash_names = _libs["avutil"].get("av_hash_names", "cdecl")
    av_hash_names.argtypes = [c_int]
    av_hash_names.restype = c_char_p

# /usr/include/libavutil/hash.h: 142
if _libs["avutil"].has("av_hash_get_name", "cdecl"):
    av_hash_get_name = _libs["avutil"].get("av_hash_get_name", "cdecl")
    av_hash_get_name.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_name.restype = c_char_p

# /usr/include/libavutil/hash.h: 169
if _libs["avutil"].has("av_hash_get_size", "cdecl"):
    av_hash_get_size = _libs["avutil"].get("av_hash_get_size", "cdecl")
    av_hash_get_size.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_size.restype = c_int

# /usr/include/libavutil/hash.h: 176
if _libs["avutil"].has("av_hash_init", "cdecl"):
    av_hash_init = _libs["avutil"].get("av_hash_init", "cdecl")
    av_hash_init.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_init.restype = None

# /usr/include/libavutil/hash.h: 186
if _libs["avutil"].has("av_hash_update", "cdecl"):
    av_hash_update = _libs["avutil"].get("av_hash_update", "cdecl")
    av_hash_update.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_update.restype = None

# /usr/include/libavutil/hash.h: 205
if _libs["avutil"].has("av_hash_final", "cdecl"):
    av_hash_final = _libs["avutil"].get("av_hash_final", "cdecl")
    av_hash_final.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8)]
    av_hash_final.restype = None

# /usr/include/libavutil/hash.h: 220
if _libs["avutil"].has("av_hash_final_bin", "cdecl"):
    av_hash_final_bin = _libs["avutil"].get("av_hash_final_bin", "cdecl")
    av_hash_final_bin.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_bin.restype = None

# /usr/include/libavutil/hash.h: 238
if _libs["avutil"].has("av_hash_final_hex", "cdecl"):
    av_hash_final_hex = _libs["avutil"].get("av_hash_final_hex", "cdecl")
    av_hash_final_hex.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_hex.restype = None

# /usr/include/libavutil/hash.h: 256
if _libs["avutil"].has("av_hash_final_b64", "cdecl"):
    av_hash_final_b64 = _libs["avutil"].get("av_hash_final_b64", "cdecl")
    av_hash_final_b64.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_b64.restype = None

# /usr/include/libavutil/hash.h: 263
if _libs["avutil"].has("av_hash_freep", "cdecl"):
    av_hash_freep = _libs["avutil"].get("av_hash_freep", "cdecl")
    av_hash_freep.argtypes = [POINTER(POINTER(struct_AVHashContext))]
    av_hash_freep.restype = None

enum_AVHDRPlusOverlapProcessOption = c_int# /usr/include/libavutil/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_WEIGHTED_AVERAGING = 0# /usr/include/libavutil/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_LAYERING = 1# /usr/include/libavutil/hdr_dynamic_metadata.h: 30

# /usr/include/libavutil/hdr_dynamic_metadata.h: 53
class struct_AVHDRPlusPercentile(Structure):
    pass

struct_AVHDRPlusPercentile.__slots__ = [
    'percentage',
    'percentile',
]
struct_AVHDRPlusPercentile._fields_ = [
    ('percentage', c_uint8),
    ('percentile', AVRational),
]

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /usr/include/libavutil/hdr_dynamic_metadata.h: 53

# /usr/include/libavutil/hdr_dynamic_metadata.h: 230
class struct_AVHDRPlusColorTransformParams(Structure):
    pass

struct_AVHDRPlusColorTransformParams.__slots__ = [
    'window_upper_left_corner_x',
    'window_upper_left_corner_y',
    'window_lower_right_corner_x',
    'window_lower_right_corner_y',
    'center_of_ellipse_x',
    'center_of_ellipse_y',
    'rotation_angle',
    'semimajor_axis_internal_ellipse',
    'semimajor_axis_external_ellipse',
    'semiminor_axis_external_ellipse',
    'overlap_process_option',
    'maxscl',
    'average_maxrgb',
    'num_distribution_maxrgb_percentiles',
    'distribution_maxrgb',
    'fraction_bright_pixels',
    'tone_mapping_flag',
    'knee_point_x',
    'knee_point_y',
    'num_bezier_curve_anchors',
    'bezier_curve_anchors',
    'color_saturation_mapping_flag',
    'color_saturation_weight',
]
struct_AVHDRPlusColorTransformParams._fields_ = [
    ('window_upper_left_corner_x', AVRational),
    ('window_upper_left_corner_y', AVRational),
    ('window_lower_right_corner_x', AVRational),
    ('window_lower_right_corner_y', AVRational),
    ('center_of_ellipse_x', c_uint16),
    ('center_of_ellipse_y', c_uint16),
    ('rotation_angle', c_uint8),
    ('semimajor_axis_internal_ellipse', c_uint16),
    ('semimajor_axis_external_ellipse', c_uint16),
    ('semiminor_axis_external_ellipse', c_uint16),
    ('overlap_process_option', enum_AVHDRPlusOverlapProcessOption),
    ('maxscl', AVRational * int(3)),
    ('average_maxrgb', AVRational),
    ('num_distribution_maxrgb_percentiles', c_uint8),
    ('distribution_maxrgb', AVHDRPlusPercentile * int(15)),
    ('fraction_bright_pixels', AVRational),
    ('tone_mapping_flag', c_uint8),
    ('knee_point_x', AVRational),
    ('knee_point_y', AVRational),
    ('num_bezier_curve_anchors', c_uint8),
    ('bezier_curve_anchors', AVRational * int(15)),
    ('color_saturation_mapping_flag', c_uint8),
    ('color_saturation_weight', AVRational),
]

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /usr/include/libavutil/hdr_dynamic_metadata.h: 230

# /usr/include/libavutil/hdr_dynamic_metadata.h: 323
class struct_AVDynamicHDRPlus(Structure):
    pass

struct_AVDynamicHDRPlus.__slots__ = [
    'itu_t_t35_country_code',
    'application_version',
    'num_windows',
    'params',
    'targeted_system_display_maximum_luminance',
    'targeted_system_display_actual_peak_luminance_flag',
    'num_rows_targeted_system_display_actual_peak_luminance',
    'num_cols_targeted_system_display_actual_peak_luminance',
    'targeted_system_display_actual_peak_luminance',
    'mastering_display_actual_peak_luminance_flag',
    'num_rows_mastering_display_actual_peak_luminance',
    'num_cols_mastering_display_actual_peak_luminance',
    'mastering_display_actual_peak_luminance',
]
struct_AVDynamicHDRPlus._fields_ = [
    ('itu_t_t35_country_code', c_uint8),
    ('application_version', c_uint8),
    ('num_windows', c_uint8),
    ('params', AVHDRPlusColorTransformParams * int(3)),
    ('targeted_system_display_maximum_luminance', AVRational),
    ('targeted_system_display_actual_peak_luminance_flag', c_uint8),
    ('num_rows_targeted_system_display_actual_peak_luminance', c_uint8),
    ('num_cols_targeted_system_display_actual_peak_luminance', c_uint8),
    ('targeted_system_display_actual_peak_luminance', (AVRational * int(25)) * int(25)),
    ('mastering_display_actual_peak_luminance_flag', c_uint8),
    ('num_rows_mastering_display_actual_peak_luminance', c_uint8),
    ('num_cols_mastering_display_actual_peak_luminance', c_uint8),
    ('mastering_display_actual_peak_luminance', (AVRational * int(25)) * int(25)),
]

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /usr/include/libavutil/hdr_dynamic_metadata.h: 323

# /usr/include/libavutil/hdr_dynamic_metadata.h: 332
if _libs["avutil"].has("av_dynamic_hdr_plus_alloc", "cdecl"):
    av_dynamic_hdr_plus_alloc = _libs["avutil"].get("av_dynamic_hdr_plus_alloc", "cdecl")
    av_dynamic_hdr_plus_alloc.argtypes = [POINTER(c_size_t)]
    av_dynamic_hdr_plus_alloc.restype = POINTER(AVDynamicHDRPlus)

# /usr/include/libavutil/hdr_dynamic_metadata.h: 341
if _libs["avutil"].has("av_dynamic_hdr_plus_create_side_data", "cdecl"):
    av_dynamic_hdr_plus_create_side_data = _libs["avutil"].get("av_dynamic_hdr_plus_create_side_data", "cdecl")
    av_dynamic_hdr_plus_create_side_data.argtypes = [POINTER(AVFrame)]
    av_dynamic_hdr_plus_create_side_data.restype = POINTER(AVDynamicHDRPlus)

enum_AVHMACType = c_int# /usr/include/libavutil/hmac.h: 33

AV_HMAC_MD5 = 0# /usr/include/libavutil/hmac.h: 33

AV_HMAC_SHA1 = (AV_HMAC_MD5 + 1)# /usr/include/libavutil/hmac.h: 33

AV_HMAC_SHA224 = (AV_HMAC_SHA1 + 1)# /usr/include/libavutil/hmac.h: 33

AV_HMAC_SHA256 = (AV_HMAC_SHA224 + 1)# /usr/include/libavutil/hmac.h: 33

AV_HMAC_SHA384 = (AV_HMAC_SHA256 + 1)# /usr/include/libavutil/hmac.h: 33

AV_HMAC_SHA512 = (AV_HMAC_SHA384 + 1)# /usr/include/libavutil/hmac.h: 33

# /usr/include/libavutil/hmac.h: 42
class struct_AVHMAC(Structure):
    pass

AVHMAC = struct_AVHMAC# /usr/include/libavutil/hmac.h: 42

# /usr/include/libavutil/hmac.h: 48
if _libs["avutil"].has("av_hmac_alloc", "cdecl"):
    av_hmac_alloc = _libs["avutil"].get("av_hmac_alloc", "cdecl")
    av_hmac_alloc.argtypes = [enum_AVHMACType]
    av_hmac_alloc.restype = POINTER(AVHMAC)

# /usr/include/libavutil/hmac.h: 54
if _libs["avutil"].has("av_hmac_free", "cdecl"):
    av_hmac_free = _libs["avutil"].get("av_hmac_free", "cdecl")
    av_hmac_free.argtypes = [POINTER(AVHMAC)]
    av_hmac_free.restype = None

# /usr/include/libavutil/hmac.h: 62
if _libs["avutil"].has("av_hmac_init", "cdecl"):
    av_hmac_init = _libs["avutil"].get("av_hmac_init", "cdecl")
    av_hmac_init.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_init.restype = None

# /usr/include/libavutil/hmac.h: 70
if _libs["avutil"].has("av_hmac_update", "cdecl"):
    av_hmac_update = _libs["avutil"].get("av_hmac_update", "cdecl")
    av_hmac_update.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_update.restype = None

# /usr/include/libavutil/hmac.h: 79
if _libs["avutil"].has("av_hmac_final", "cdecl"):
    av_hmac_final = _libs["avutil"].get("av_hmac_final", "cdecl")
    av_hmac_final.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_final.restype = c_int

# /usr/include/libavutil/hmac.h: 92
if _libs["avutil"].has("av_hmac_calc", "cdecl"):
    av_hmac_calc = _libs["avutil"].get("av_hmac_calc", "cdecl")
    av_hmac_calc.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint, POINTER(c_uint8), c_uint, POINTER(c_uint8), c_uint]
    av_hmac_calc.restype = c_int

# /usr/include/libavutil/attributes.h: 33
def AV_GCC_VERSION_AT_LEAST(x, y):
    return 0

# /usr/include/libavutil/attributes.h: 34
def AV_GCC_VERSION_AT_MOST(x, y):
    return 0

# /usr/include/libavutil/attributes.h: 126
def AV_NOWARN_DEPRECATED(code):
    return code

# /usr/include/libavutil/attributes.h: 156
def av_uninit(x):
    return x

# /usr/include/libavutil/attributes.h: 163
def av_builtin_constant_p(x):
    return 0

# /usr/include/libavutil/macros.h: 36
def AV_STRINGIFY(s):
    return (AV_TOSTRING (s))

# /usr/include/libavutil/macros.h: 37
def AV_TOSTRING(s):
    return s

# /usr/include/libavutil/macros.h: 48
def FFALIGN(x, a):
    return (((x + a) - 1) & (~(a - 1)))

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

# /usr/include/libavutil/aes_ctr.h: 30
try:
    AES_CTR_KEY_SIZE = 16
except:
    pass

# /usr/include/libavutil/aes_ctr.h: 31
try:
    AES_CTR_IV_SIZE = 8
except:
    pass

# /usr/include/libavutil/avutil.h: 225
try:
    FF_LAMBDA_SHIFT = 7
except:
    pass

# /usr/include/libavutil/avutil.h: 226
try:
    FF_LAMBDA_SCALE = (1 << FF_LAMBDA_SHIFT)
except:
    pass

# /usr/include/libavutil/avutil.h: 227
try:
    FF_QP2LAMBDA = 118
except:
    pass

# /usr/include/libavutil/avutil.h: 228
try:
    FF_LAMBDA_MAX = ((256 * 128) - 1)
except:
    pass

# /usr/include/libavutil/avutil.h: 230
try:
    FF_QUALITY_SCALE = FF_LAMBDA_SCALE
except:
    pass

# /usr/include/libavutil/avutil.h: 254
try:
    AV_TIME_BASE = 1000000
except:
    pass

# /usr/include/libavutil/avconfig.h: 4
try:
    AV_HAVE_BIGENDIAN = 0
except:
    pass

# /usr/include/libavutil/avconfig.h: 5
try:
    AV_HAVE_FAST_UNALIGNED = 1
except:
    pass

# /usr/include/libavutil/common.h: 50
def AV_NE(be, le):
    return le

# /usr/include/libavutil/common.h: 54
def RSHIFT(a, b):
    return (a > 0) and ((a + ((1 << b) >> 1)) >> b) or (((a + ((1 << b) >> 1)) - 1) >> b)

# /usr/include/libavutil/common.h: 56
def ROUNDED_DIV(a, b):
    return ((a >= 0) and (a + (b >> 1)) or (a - (b >> 1)) / b)

# /usr/include/libavutil/common.h: 58
def AV_CEIL_RSHIFT(a, b):
    return (not (av_builtin_constant_p (b))) and (-((-a) >> b)) or (((a + (1 << b)) - 1) >> b)

# /usr/include/libavutil/common.h: 61
try:
    FF_CEIL_RSHIFT = AV_CEIL_RSHIFT
except:
    pass

# /usr/include/libavutil/common.h: 63
def FFUDIV(a, b):
    return ((a > 0) and a or ((a - b) + 1) / b)

# /usr/include/libavutil/common.h: 64
def FFUMOD(a, b):
    return (a - (b * (FFUDIV (a, b))))

# /usr/include/libavutil/common.h: 72
def FFABS(a):
    return (a >= 0) and a or (-a)

# /usr/include/libavutil/common.h: 73
def FFSIGN(a):
    return (a > 0) and 1 or (-1)

# /usr/include/libavutil/common.h: 81
def FFNABS(a):
    return (a <= 0) and a or (-a)

# /usr/include/libavutil/common.h: 89
def FFABSU(a):
    return (a <= 0) and (-(c_uint (ord_if_char(a))).value) or (c_uint (ord_if_char(a))).value

# /usr/include/libavutil/common.h: 90
def FFABS64U(a):
    return (a <= 0) and (-(c_uint64 (ord_if_char(a))).value) or (c_uint64 (ord_if_char(a))).value

# /usr/include/libavutil/common.h: 101
def FFDIFFSIGN(x, y):
    return ((x > y) - (x < y))

# /usr/include/libavutil/common.h: 103
def FFMAX(a, b):
    return (a > b) and a or b

# /usr/include/libavutil/common.h: 104
def FFMAX3(a, b, c):
    return (FFMAX ((FFMAX (a, b)), c))

# /usr/include/libavutil/common.h: 105
def FFMIN(a, b):
    return (a > b) and b or a

# /usr/include/libavutil/common.h: 106
def FFMIN3(a, b, c):
    return (FFMIN ((FFMIN (a, b)), c))

# /usr/include/libavutil/common.h: 109
def FF_ARRAY_ELEMS(a):
    return (sizeof(a) / sizeof((a [0])))

# /usr/include/libavutil/common.h: 478
def MKTAG(a, b, c, d):
    return (((a | (b << 8)) | (c << 16)) | ((c_uint (ord_if_char(d))).value << 24))

# /usr/include/libavutil/common.h: 479
def MKBETAG(a, b, c, d):
    return (((d | (c << 8)) | (b << 16)) | ((c_uint (ord_if_char(a))).value << 24))

# /usr/include/libavutil/error.h: 39
def AVERROR(e):
    return (-e)

# /usr/include/libavutil/error.h: 40
def AVUNERROR(e):
    return (-e)

# /usr/include/libavutil/error.h: 47
def FFERRTAG(a, b, c, d):
    return (-(c_int (ord_if_char((MKTAG (a, b, c, d))))).value)

# /usr/include/libavutil/error.h: 49
try:
    AVERROR_BSF_NOT_FOUND = (FFERRTAG (248, b'B', b'S', b'F'))
except:
    pass

# /usr/include/libavutil/error.h: 50
try:
    AVERROR_BUG = (FFERRTAG (b'B', b'U', b'G', b'!'))
except:
    pass

# /usr/include/libavutil/error.h: 51
try:
    AVERROR_BUFFER_TOO_SMALL = (FFERRTAG (b'B', b'U', b'F', b'S'))
except:
    pass

# /usr/include/libavutil/error.h: 52
try:
    AVERROR_DECODER_NOT_FOUND = (FFERRTAG (248, b'D', b'E', b'C'))
except:
    pass

# /usr/include/libavutil/error.h: 53
try:
    AVERROR_DEMUXER_NOT_FOUND = (FFERRTAG (248, b'D', b'E', b'M'))
except:
    pass

# /usr/include/libavutil/error.h: 54
try:
    AVERROR_ENCODER_NOT_FOUND = (FFERRTAG (248, b'E', b'N', b'C'))
except:
    pass

# /usr/include/libavutil/error.h: 55
try:
    AVERROR_EOF = (FFERRTAG (b'E', b'O', b'F', b' '))
except:
    pass

# /usr/include/libavutil/error.h: 56
try:
    AVERROR_EXIT = (FFERRTAG (b'E', b'X', b'I', b'T'))
except:
    pass

# /usr/include/libavutil/error.h: 57
try:
    AVERROR_EXTERNAL = (FFERRTAG (b'E', b'X', b'T', b' '))
except:
    pass

# /usr/include/libavutil/error.h: 58
try:
    AVERROR_FILTER_NOT_FOUND = (FFERRTAG (248, b'F', b'I', b'L'))
except:
    pass

# /usr/include/libavutil/error.h: 59
try:
    AVERROR_INVALIDDATA = (FFERRTAG (b'I', b'N', b'D', b'A'))
except:
    pass

# /usr/include/libavutil/error.h: 60
try:
    AVERROR_MUXER_NOT_FOUND = (FFERRTAG (248, b'M', b'U', b'X'))
except:
    pass

# /usr/include/libavutil/error.h: 61
try:
    AVERROR_OPTION_NOT_FOUND = (FFERRTAG (248, b'O', b'P', b'T'))
except:
    pass

# /usr/include/libavutil/error.h: 62
try:
    AVERROR_PATCHWELCOME = (FFERRTAG (b'P', b'A', b'W', b'E'))
except:
    pass

# /usr/include/libavutil/error.h: 63
try:
    AVERROR_PROTOCOL_NOT_FOUND = (FFERRTAG (248, b'P', b'R', b'O'))
except:
    pass

# /usr/include/libavutil/error.h: 65
try:
    AVERROR_STREAM_NOT_FOUND = (FFERRTAG (248, b'S', b'T', b'R'))
except:
    pass

# /usr/include/libavutil/error.h: 70
try:
    AVERROR_BUG2 = (FFERRTAG (b'B', b'U', b'G', b' '))
except:
    pass

# /usr/include/libavutil/error.h: 71
try:
    AVERROR_UNKNOWN = (FFERRTAG (b'U', b'N', b'K', b'N'))
except:
    pass

# /usr/include/libavutil/error.h: 72
try:
    AVERROR_EXPERIMENTAL = (-733130664)
except:
    pass

# /usr/include/libavutil/error.h: 73
try:
    AVERROR_INPUT_CHANGED = (-1668179713)
except:
    pass

# /usr/include/libavutil/error.h: 74
try:
    AVERROR_OUTPUT_CHANGED = (-1668179714)
except:
    pass

# /usr/include/libavutil/error.h: 76
try:
    AVERROR_HTTP_BAD_REQUEST = (FFERRTAG (248, b'4', b'0', b'0'))
except:
    pass

# /usr/include/libavutil/error.h: 77
try:
    AVERROR_HTTP_UNAUTHORIZED = (FFERRTAG (248, b'4', b'0', b'1'))
except:
    pass

# /usr/include/libavutil/error.h: 78
try:
    AVERROR_HTTP_FORBIDDEN = (FFERRTAG (248, b'4', b'0', b'3'))
except:
    pass

# /usr/include/libavutil/error.h: 79
try:
    AVERROR_HTTP_NOT_FOUND = (FFERRTAG (248, b'4', b'0', b'4'))
except:
    pass

# /usr/include/libavutil/error.h: 80
try:
    AVERROR_HTTP_OTHER_4XX = (FFERRTAG (248, b'4', b'X', b'X'))
except:
    pass

# /usr/include/libavutil/error.h: 81
try:
    AVERROR_HTTP_SERVER_ERROR = (FFERRTAG (248, b'5', b'X', b'X'))
except:
    pass

# /usr/include/libavutil/error.h: 83
try:
    AV_ERROR_MAX_STRING_SIZE = 64
except:
    pass

# /usr/include/libavutil/mem.h: 125
def DECLARE_ALIGNED(n, t, v):
    return (t + v)

# /usr/include/libavutil/mem.h: 126
def DECLARE_ASM_ALIGNED(n, t, v):
    return (t + v)

# /usr/include/libavutil/mathematics.h: 46
try:
    M_LOG2_10 = 3.321928094887362
except:
    pass

# /usr/include/libavutil/mathematics.h: 49
try:
    M_PHI = 1.618033988749895
except:
    pass

# /usr/include/libavutil/log.h: 50
def AV_IS_INPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_INPUT))

# /usr/include/libavutil/log.h: 55
def AV_IS_OUTPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_OUTPUT))

# /usr/include/libavutil/log.h: 176
try:
    AV_LOG_QUIET = (-8)
except:
    pass

# /usr/include/libavutil/log.h: 181
try:
    AV_LOG_PANIC = 0
except:
    pass

# /usr/include/libavutil/log.h: 188
try:
    AV_LOG_FATAL = 8
except:
    pass

# /usr/include/libavutil/log.h: 194
try:
    AV_LOG_ERROR = 16
except:
    pass

# /usr/include/libavutil/log.h: 200
try:
    AV_LOG_WARNING = 24
except:
    pass

# /usr/include/libavutil/log.h: 205
try:
    AV_LOG_INFO = 32
except:
    pass

# /usr/include/libavutil/log.h: 210
try:
    AV_LOG_VERBOSE = 40
except:
    pass

# /usr/include/libavutil/log.h: 215
try:
    AV_LOG_DEBUG = 48
except:
    pass

# /usr/include/libavutil/log.h: 220
try:
    AV_LOG_TRACE = 56
except:
    pass

# /usr/include/libavutil/log.h: 222
try:
    AV_LOG_MAX_OFFSET = (AV_LOG_TRACE - AV_LOG_QUIET)
except:
    pass

# /usr/include/libavutil/log.h: 236
def AV_LOG_C(x):
    return (x << 8)

# /usr/include/libavutil/log.h: 384
try:
    AV_LOG_SKIP_REPEATED = 1
except:
    pass

# /usr/include/libavutil/log.h: 392
try:
    AV_LOG_PRINT_LEVEL = 2
except:
    pass

# /usr/include/libavutil/pixfmt.h: 32
try:
    AVPALETTE_SIZE = 1024
except:
    pass

# /usr/include/libavutil/pixfmt.h: 33
try:
    AVPALETTE_COUNT = 256
except:
    pass

# /usr/include/libavutil/avutil.h: 331
def av_int_list_length(list, term):
    return (av_int_list_length_for_size (sizeof((list[0])), list, term))

# /usr/include/libavutil/avutil.h: 346
try:
    AV_FOURCC_MAX_STRING_SIZE = 32
except:
    pass

# /usr/include/libavutil/avstring.h: 338
try:
    AV_ESCAPE_FLAG_WHITESPACE = (1 << 0)
except:
    pass

# /usr/include/libavutil/avstring.h: 345
try:
    AV_ESCAPE_FLAG_STRICT = (1 << 1)
except:
    pass

# /usr/include/libavutil/avstring.h: 351
try:
    AV_ESCAPE_FLAG_XML_SINGLE_QUOTES = (1 << 2)
except:
    pass

# /usr/include/libavutil/avstring.h: 357
try:
    AV_ESCAPE_FLAG_XML_DOUBLE_QUOTES = (1 << 3)
except:
    pass

# /usr/include/libavutil/avstring.h: 380
try:
    AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES = 1
except:
    pass

# /usr/include/libavutil/avstring.h: 381
try:
    AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS = 2
except:
    pass

# /usr/include/libavutil/avstring.h: 382
try:
    AV_UTF8_FLAG_ACCEPT_SURROGATES = 4
except:
    pass

# /usr/include/libavutil/avstring.h: 383
try:
    AV_UTF8_FLAG_EXCLUDE_XML_INVALID_CONTROL_CODES = 8
except:
    pass

# /usr/include/libavutil/avstring.h: 385
try:
    AV_UTF8_FLAG_ACCEPT_ALL = ((AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES | AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS) | AV_UTF8_FLAG_ACCEPT_SURROGATES)
except:
    pass

# /usr/include/libavutil/base64.h: 48
def AV_BASE64_DECODE_SIZE(x):
    return ((x * 3) / 4)

# /usr/include/libavutil/base64.h: 66
def AV_BASE64_SIZE(x):
    return ((((x + 2) / 3) * 4) + 1)

# /usr/include/libavutil/blowfish.h: 33
try:
    AV_BF_ROUNDS = 16
except:
    pass

# /usr/include/libavutil/bprint.h: 94
try:
    AV_BPRINT_SIZE_UNLIMITED = (c_uint (ord_if_char((-1)))).value
except:
    pass

# /usr/include/libavutil/bprint.h: 95
try:
    AV_BPRINT_SIZE_AUTOMATIC = 1
except:
    pass

# /usr/include/libavutil/bprint.h: 96
try:
    AV_BPRINT_SIZE_COUNT_ONLY = 0
except:
    pass

# /usr/include/libavutil/bswap.h: 51
def AV_BSWAP16C(x):
    return (((x << 8) & 65280) | ((x >> 8) & 255))

# /usr/include/libavutil/bswap.h: 52
def AV_BSWAP32C(x):
    return (((AV_BSWAP16C (x)) << 16) | (AV_BSWAP16C ((x >> 16))))

# /usr/include/libavutil/bswap.h: 53
def AV_BSWAP64C(x):
    return (((AV_BSWAP32C (x)) << 32) | (AV_BSWAP32C ((x >> 32))))

# /usr/include/libavutil/bswap.h: 95
def av_le2ne16(x):
    return x

# /usr/include/libavutil/bswap.h: 96
def av_le2ne32(x):
    return x

# /usr/include/libavutil/bswap.h: 97
def av_le2ne64(x):
    return x

# /usr/include/libavutil/bswap.h: 99
def AV_LE2NEC(s, x):
    return x

# /usr/include/libavutil/bswap.h: 105
def AV_LE2NE16C(x):
    return (AV_LE2NEC (16, x))

# /usr/include/libavutil/bswap.h: 106
def AV_LE2NE32C(x):
    return (AV_LE2NEC (32, x))

# /usr/include/libavutil/bswap.h: 107
def AV_LE2NE64C(x):
    return (AV_LE2NEC (64, x))

# /usr/include/libavutil/buffer.h: 128
try:
    AV_BUFFER_FLAG_READONLY = (1 << 0)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 49
try:
    AV_CH_FRONT_LEFT = 1
except:
    pass

# /usr/include/libavutil/channel_layout.h: 50
try:
    AV_CH_FRONT_RIGHT = 2
except:
    pass

# /usr/include/libavutil/channel_layout.h: 51
try:
    AV_CH_FRONT_CENTER = 4
except:
    pass

# /usr/include/libavutil/channel_layout.h: 52
try:
    AV_CH_LOW_FREQUENCY = 8
except:
    pass

# /usr/include/libavutil/channel_layout.h: 53
try:
    AV_CH_BACK_LEFT = 16
except:
    pass

# /usr/include/libavutil/channel_layout.h: 54
try:
    AV_CH_BACK_RIGHT = 32
except:
    pass

# /usr/include/libavutil/channel_layout.h: 55
try:
    AV_CH_FRONT_LEFT_OF_CENTER = 64
except:
    pass

# /usr/include/libavutil/channel_layout.h: 56
try:
    AV_CH_FRONT_RIGHT_OF_CENTER = 128
except:
    pass

# /usr/include/libavutil/channel_layout.h: 57
try:
    AV_CH_BACK_CENTER = 256
except:
    pass

# /usr/include/libavutil/channel_layout.h: 58
try:
    AV_CH_SIDE_LEFT = 512
except:
    pass

# /usr/include/libavutil/channel_layout.h: 59
try:
    AV_CH_SIDE_RIGHT = 1024
except:
    pass

# /usr/include/libavutil/channel_layout.h: 60
try:
    AV_CH_TOP_CENTER = 2048
except:
    pass

# /usr/include/libavutil/channel_layout.h: 61
try:
    AV_CH_TOP_FRONT_LEFT = 4096
except:
    pass

# /usr/include/libavutil/channel_layout.h: 62
try:
    AV_CH_TOP_FRONT_CENTER = 8192
except:
    pass

# /usr/include/libavutil/channel_layout.h: 63
try:
    AV_CH_TOP_FRONT_RIGHT = 16384
except:
    pass

# /usr/include/libavutil/channel_layout.h: 64
try:
    AV_CH_TOP_BACK_LEFT = 32768
except:
    pass

# /usr/include/libavutil/channel_layout.h: 65
try:
    AV_CH_TOP_BACK_CENTER = 65536
except:
    pass

# /usr/include/libavutil/channel_layout.h: 66
try:
    AV_CH_TOP_BACK_RIGHT = 131072
except:
    pass

# /usr/include/libavutil/channel_layout.h: 67
try:
    AV_CH_STEREO_LEFT = 536870912
except:
    pass

# /usr/include/libavutil/channel_layout.h: 68
try:
    AV_CH_STEREO_RIGHT = 1073741824
except:
    pass

# /usr/include/libavutil/channel_layout.h: 69
try:
    AV_CH_WIDE_LEFT = 2147483648
except:
    pass

# /usr/include/libavutil/channel_layout.h: 70
try:
    AV_CH_WIDE_RIGHT = 4294967296
except:
    pass

# /usr/include/libavutil/channel_layout.h: 71
try:
    AV_CH_SURROUND_DIRECT_LEFT = 8589934592
except:
    pass

# /usr/include/libavutil/channel_layout.h: 72
try:
    AV_CH_SURROUND_DIRECT_RIGHT = 17179869184
except:
    pass

# /usr/include/libavutil/channel_layout.h: 73
try:
    AV_CH_LOW_FREQUENCY_2 = 34359738368
except:
    pass

# /usr/include/libavutil/channel_layout.h: 74
try:
    AV_CH_TOP_SIDE_LEFT = 68719476736
except:
    pass

# /usr/include/libavutil/channel_layout.h: 75
try:
    AV_CH_TOP_SIDE_RIGHT = 137438953472
except:
    pass

# /usr/include/libavutil/channel_layout.h: 76
try:
    AV_CH_BOTTOM_FRONT_CENTER = 274877906944
except:
    pass

# /usr/include/libavutil/channel_layout.h: 77
try:
    AV_CH_BOTTOM_FRONT_LEFT = 549755813888
except:
    pass

# /usr/include/libavutil/channel_layout.h: 78
try:
    AV_CH_BOTTOM_FRONT_RIGHT = 1099511627776
except:
    pass

# /usr/include/libavutil/channel_layout.h: 83
try:
    AV_CH_LAYOUT_NATIVE = 9223372036854775808
except:
    pass

# /usr/include/libavutil/channel_layout.h: 90
try:
    AV_CH_LAYOUT_MONO = AV_CH_FRONT_CENTER
except:
    pass

# /usr/include/libavutil/channel_layout.h: 91
try:
    AV_CH_LAYOUT_STEREO = (AV_CH_FRONT_LEFT | AV_CH_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 92
try:
    AV_CH_LAYOUT_2POINT1 = (AV_CH_LAYOUT_STEREO | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 93
try:
    AV_CH_LAYOUT_2_1 = (AV_CH_LAYOUT_STEREO | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 94
try:
    AV_CH_LAYOUT_SURROUND = (AV_CH_LAYOUT_STEREO | AV_CH_FRONT_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 95
try:
    AV_CH_LAYOUT_3POINT1 = (AV_CH_LAYOUT_SURROUND | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 96
try:
    AV_CH_LAYOUT_4POINT0 = (AV_CH_LAYOUT_SURROUND | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 97
try:
    AV_CH_LAYOUT_4POINT1 = (AV_CH_LAYOUT_4POINT0 | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 98
try:
    AV_CH_LAYOUT_2_2 = ((AV_CH_LAYOUT_STEREO | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 99
try:
    AV_CH_LAYOUT_QUAD = ((AV_CH_LAYOUT_STEREO | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 100
try:
    AV_CH_LAYOUT_5POINT0 = ((AV_CH_LAYOUT_SURROUND | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 101
try:
    AV_CH_LAYOUT_5POINT1 = (AV_CH_LAYOUT_5POINT0 | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 102
try:
    AV_CH_LAYOUT_5POINT0_BACK = ((AV_CH_LAYOUT_SURROUND | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 103
try:
    AV_CH_LAYOUT_5POINT1_BACK = (AV_CH_LAYOUT_5POINT0_BACK | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 104
try:
    AV_CH_LAYOUT_6POINT0 = (AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 105
try:
    AV_CH_LAYOUT_6POINT0_FRONT = ((AV_CH_LAYOUT_2_2 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 106
try:
    AV_CH_LAYOUT_HEXAGONAL = (AV_CH_LAYOUT_5POINT0_BACK | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 107
try:
    AV_CH_LAYOUT_6POINT1 = (AV_CH_LAYOUT_5POINT1 | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 108
try:
    AV_CH_LAYOUT_6POINT1_BACK = (AV_CH_LAYOUT_5POINT1_BACK | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 109
try:
    AV_CH_LAYOUT_6POINT1_FRONT = (AV_CH_LAYOUT_6POINT0_FRONT | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 110
try:
    AV_CH_LAYOUT_7POINT0 = ((AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 111
try:
    AV_CH_LAYOUT_7POINT0_FRONT = ((AV_CH_LAYOUT_5POINT0 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 112
try:
    AV_CH_LAYOUT_7POINT1 = ((AV_CH_LAYOUT_5POINT1 | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 113
try:
    AV_CH_LAYOUT_7POINT1_WIDE = ((AV_CH_LAYOUT_5POINT1 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 114
try:
    AV_CH_LAYOUT_7POINT1_WIDE_BACK = ((AV_CH_LAYOUT_5POINT1_BACK | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 115
try:
    AV_CH_LAYOUT_OCTAGONAL = (((AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_LEFT) | AV_CH_BACK_CENTER) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 116
try:
    AV_CH_LAYOUT_HEXADECAGONAL = ((((((((AV_CH_LAYOUT_OCTAGONAL | AV_CH_WIDE_LEFT) | AV_CH_WIDE_RIGHT) | AV_CH_TOP_BACK_LEFT) | AV_CH_TOP_BACK_RIGHT) | AV_CH_TOP_BACK_CENTER) | AV_CH_TOP_FRONT_CENTER) | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 117
try:
    AV_CH_LAYOUT_STEREO_DOWNMIX = (AV_CH_STEREO_LEFT | AV_CH_STEREO_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 118
try:
    AV_CH_LAYOUT_22POINT2 = ((((((((((((((((((AV_CH_LAYOUT_5POINT1_BACK | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER) | AV_CH_BACK_CENTER) | AV_CH_LOW_FREQUENCY_2) | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT) | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT) | AV_CH_TOP_FRONT_CENTER) | AV_CH_TOP_CENTER) | AV_CH_TOP_BACK_LEFT) | AV_CH_TOP_BACK_RIGHT) | AV_CH_TOP_SIDE_LEFT) | AV_CH_TOP_SIDE_RIGHT) | AV_CH_TOP_BACK_CENTER) | AV_CH_BOTTOM_FRONT_CENTER) | AV_CH_BOTTOM_FRONT_LEFT) | AV_CH_BOTTOM_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/cpu.h: 28
try:
    AV_CPU_FLAG_FORCE = 2147483648
except:
    pass

# /usr/include/libavutil/cpu.h: 31
try:
    AV_CPU_FLAG_MMX = 1
except:
    pass

# /usr/include/libavutil/cpu.h: 32
try:
    AV_CPU_FLAG_MMXEXT = 2
except:
    pass

# /usr/include/libavutil/cpu.h: 33
try:
    AV_CPU_FLAG_MMX2 = 2
except:
    pass

# /usr/include/libavutil/cpu.h: 34
try:
    AV_CPU_FLAG_3DNOW = 4
except:
    pass

# /usr/include/libavutil/cpu.h: 35
try:
    AV_CPU_FLAG_SSE = 8
except:
    pass

# /usr/include/libavutil/cpu.h: 36
try:
    AV_CPU_FLAG_SSE2 = 16
except:
    pass

# /usr/include/libavutil/cpu.h: 37
try:
    AV_CPU_FLAG_SSE2SLOW = 1073741824
except:
    pass

# /usr/include/libavutil/cpu.h: 39
try:
    AV_CPU_FLAG_3DNOWEXT = 32
except:
    pass

# /usr/include/libavutil/cpu.h: 40
try:
    AV_CPU_FLAG_SSE3 = 64
except:
    pass

# /usr/include/libavutil/cpu.h: 41
try:
    AV_CPU_FLAG_SSE3SLOW = 536870912
except:
    pass

# /usr/include/libavutil/cpu.h: 43
try:
    AV_CPU_FLAG_SSSE3 = 128
except:
    pass

# /usr/include/libavutil/cpu.h: 44
try:
    AV_CPU_FLAG_SSSE3SLOW = 67108864
except:
    pass

# /usr/include/libavutil/cpu.h: 45
try:
    AV_CPU_FLAG_ATOM = 268435456
except:
    pass

# /usr/include/libavutil/cpu.h: 46
try:
    AV_CPU_FLAG_SSE4 = 256
except:
    pass

# /usr/include/libavutil/cpu.h: 47
try:
    AV_CPU_FLAG_SSE42 = 512
except:
    pass

# /usr/include/libavutil/cpu.h: 48
try:
    AV_CPU_FLAG_AESNI = 524288
except:
    pass

# /usr/include/libavutil/cpu.h: 49
try:
    AV_CPU_FLAG_AVX = 16384
except:
    pass

# /usr/include/libavutil/cpu.h: 50
try:
    AV_CPU_FLAG_AVXSLOW = 134217728
except:
    pass

# /usr/include/libavutil/cpu.h: 51
try:
    AV_CPU_FLAG_XOP = 1024
except:
    pass

# /usr/include/libavutil/cpu.h: 52
try:
    AV_CPU_FLAG_FMA4 = 2048
except:
    pass

# /usr/include/libavutil/cpu.h: 53
try:
    AV_CPU_FLAG_CMOV = 4096
except:
    pass

# /usr/include/libavutil/cpu.h: 54
try:
    AV_CPU_FLAG_AVX2 = 32768
except:
    pass

# /usr/include/libavutil/cpu.h: 55
try:
    AV_CPU_FLAG_FMA3 = 65536
except:
    pass

# /usr/include/libavutil/cpu.h: 56
try:
    AV_CPU_FLAG_BMI1 = 131072
except:
    pass

# /usr/include/libavutil/cpu.h: 57
try:
    AV_CPU_FLAG_BMI2 = 262144
except:
    pass

# /usr/include/libavutil/cpu.h: 58
try:
    AV_CPU_FLAG_AVX512 = 1048576
except:
    pass

# /usr/include/libavutil/cpu.h: 60
try:
    AV_CPU_FLAG_ALTIVEC = 1
except:
    pass

# /usr/include/libavutil/cpu.h: 61
try:
    AV_CPU_FLAG_VSX = 2
except:
    pass

# /usr/include/libavutil/cpu.h: 62
try:
    AV_CPU_FLAG_POWER8 = 4
except:
    pass

# /usr/include/libavutil/cpu.h: 64
try:
    AV_CPU_FLAG_ARMV5TE = (1 << 0)
except:
    pass

# /usr/include/libavutil/cpu.h: 65
try:
    AV_CPU_FLAG_ARMV6 = (1 << 1)
except:
    pass

# /usr/include/libavutil/cpu.h: 66
try:
    AV_CPU_FLAG_ARMV6T2 = (1 << 2)
except:
    pass

# /usr/include/libavutil/cpu.h: 67
try:
    AV_CPU_FLAG_VFP = (1 << 3)
except:
    pass

# /usr/include/libavutil/cpu.h: 68
try:
    AV_CPU_FLAG_VFPV3 = (1 << 4)
except:
    pass

# /usr/include/libavutil/cpu.h: 69
try:
    AV_CPU_FLAG_NEON = (1 << 5)
except:
    pass

# /usr/include/libavutil/cpu.h: 70
try:
    AV_CPU_FLAG_ARMV8 = (1 << 6)
except:
    pass

# /usr/include/libavutil/cpu.h: 71
try:
    AV_CPU_FLAG_VFP_VM = (1 << 7)
except:
    pass

# /usr/include/libavutil/cpu.h: 72
try:
    AV_CPU_FLAG_SETEND = (1 << 16)
except:
    pass

# /usr/include/libavutil/cpu.h: 74
try:
    AV_CPU_FLAG_MMI = (1 << 0)
except:
    pass

# /usr/include/libavutil/cpu.h: 75
try:
    AV_CPU_FLAG_MSA = (1 << 1)
except:
    pass

# /usr/include/libavutil/dict.h: 69
try:
    AV_DICT_MATCH_CASE = 1
except:
    pass

# /usr/include/libavutil/dict.h: 70
try:
    AV_DICT_IGNORE_SUFFIX = 2
except:
    pass

# /usr/include/libavutil/dict.h: 72
try:
    AV_DICT_DONT_STRDUP_KEY = 4
except:
    pass

# /usr/include/libavutil/dict.h: 74
try:
    AV_DICT_DONT_STRDUP_VAL = 8
except:
    pass

# /usr/include/libavutil/dict.h: 76
try:
    AV_DICT_DONT_OVERWRITE = 16
except:
    pass

# /usr/include/libavutil/dict.h: 77
try:
    AV_DICT_APPEND = 32
except:
    pass

# /usr/include/libavutil/dict.h: 79
try:
    AV_DICT_MULTIKEY = 64
except:
    pass

# /usr/include/libavutil/frame.h: 319
try:
    AV_NUM_DATA_POINTERS = 8
except:
    pass

# /usr/include/libavutil/frame.h: 543
try:
    AV_FRAME_FLAG_CORRUPT = (1 << 0)
except:
    pass

# /usr/include/libavutil/frame.h: 547
try:
    AV_FRAME_FLAG_DISCARD = (1 << 2)
except:
    pass

# /usr/include/libavutil/frame.h: 614
try:
    FF_DECODE_ERROR_INVALID_BITSTREAM = 1
except:
    pass

# /usr/include/libavutil/frame.h: 615
try:
    FF_DECODE_ERROR_MISSING_REFERENCE = 2
except:
    pass

# /usr/include/libavutil/frame.h: 616
try:
    FF_DECODE_ERROR_CONCEALMENT_ACTIVE = 4
except:
    pass

# /usr/include/libavutil/frame.h: 617
try:
    FF_DECODE_ERROR_DECODE_SLICES = 8
except:
    pass

# /usr/include/libavutil/ffversion.h: 4
try:
    FFMPEG_VERSION = 'n4.4'
except:
    pass

# /usr/include/libavutil/hash.h: 158
try:
    AV_HASH_MAX_SIZE = 64
except:
    pass

AVAESCTR = struct_AVAESCTR# /usr/include/libavutil/aes_ctr.h: 33

AVAES = struct_AVAES# /usr/include/libavutil/aes.h: 37

AVRational = struct_AVRational# /usr/include/libavutil/rational.h: 61

av_intfloat32 = union_av_intfloat32# /usr/include/libavutil/intfloat.h: 27

av_intfloat64 = union_av_intfloat64# /usr/include/libavutil/intfloat.h: 32

AVOptionRanges = struct_AVOptionRanges# /usr/include/libavutil/log.h: 60

AVOption = struct_AVOption# /usr/include/libavutil/log.h: 85

AVClass = struct_AVClass# /usr/include/libavutil/log.h: 67

AVFifoBuffer = struct_AVFifoBuffer# /usr/include/libavutil/fifo.h: 35

AVAudioFifo = struct_AVAudioFifo# /usr/include/libavutil/audio_fifo.h: 49

AVBlowfish = struct_AVBlowfish# /usr/include/libavutil/blowfish.h: 38

ff_pad_helper_AVBPrint = struct_ff_pad_helper_AVBPrint# /usr/include/libavutil/bprint.h: 82

AVBPrint = struct_AVBPrint# /usr/include/libavutil/bprint.h: 82

tm = struct_tm# /usr/include/libavutil/bprint.h: 148

AVBuffer = struct_AVBuffer# /usr/include/libavutil/buffer.h: 76

AVBufferRef = struct_AVBufferRef# /usr/include/libavutil/buffer.h: 101

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 277

AVCAMELLIA = struct_AVCAMELLIA# /usr/include/libavutil/camellia.h: 38

AVCAST5 = struct_AVCAST5# /usr/include/libavutil/cast5.h: 38

AVDES = struct_AVDES# /usr/include/libavutil/des.h: 36

AVDictionaryEntry = struct_AVDictionaryEntry# /usr/include/libavutil/dict.h: 84

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 86

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /usr/include/libavutil/dovi_meta.h: 60

AVFrameSideData = struct_AVFrameSideData# /usr/include/libavutil/frame.h: 230

AVRegionOfInterest = struct_AVRegionOfInterest# /usr/include/libavutil/frame.h: 286

AVFrame = struct_AVFrame# /usr/include/libavutil/frame.h: 698

AVDownmixInfo = struct_AVDownmixInfo# /usr/include/libavutil/downmix_info.h: 93

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /usr/include/libavutil/encryption_info.h: 35

AVEncryptionInfo = struct_AVEncryptionInfo# /usr/include/libavutil/encryption_info.h: 81

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /usr/include/libavutil/encryption_info.h: 88

AVExpr = struct_AVExpr# /usr/include/libavutil/eval.h: 31

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /usr/include/libavutil/film_grain_params.h: 118

AVFilmGrainParams = struct_AVFilmGrainParams# /usr/include/libavutil/film_grain_params.h: 147

AVHashContext = struct_AVHashContext# /usr/include/libavutil/hash.h: 117

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /usr/include/libavutil/hdr_dynamic_metadata.h: 53

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /usr/include/libavutil/hdr_dynamic_metadata.h: 230

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /usr/include/libavutil/hdr_dynamic_metadata.h: 323

AVHMAC = struct_AVHMAC# /usr/include/libavutil/hmac.h: 42

# No inserted files

# No prefix-stripping

