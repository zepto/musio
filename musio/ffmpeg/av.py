r"""Wrapper for ac3_parser.h

Generated with:
ctypesgen -lavcodec -lavformat -lavutil -lavdevice -lswresample -lswscale av/ac3_parser.h av/adler32.h av/adts_parser.h av/aes_ctr.h av/aes.h av/attributes.h av/audio_fifo.h av/avassert.h av/avc1394.h av/avc1394_vcr.h av/avcodec.h av/avconfig.h av/avdct.h av/avdevice.h av/avfft.h av/avfilter.h av/avformat.h av/avio.h av/avstring.h av/avutil.h av/base64.h av/blowfish.h av/bprint.h av/bsf.h av/bswap.h av/buffer.h av/buffersink.h av/buffersrc.h av/camellia.h av/cast5.h av/channel_layout.h av/codec_desc.h av/codec.h av/codec_id.h av/codec_par.h av/common.h av/cpu.h av/crc.h av/des.h av/dict.h av/dirac.h av/display.h av/dovi_meta.h av/downmix_info.h av/dv_profile.h av/encryption_info.h av/error.h av/eval.h av/ffversion.h av/fifo.h av/file.h av/film_grain_params.h av/frame.h av/hash.h av/hdr_dynamic_metadata.h av/hmac.h av/hwcontext_drm.h av/hwcontext.h av/hwcontext_mediacodec.h av/hwcontext_opencl.h av/hwcontext_qsv.h av/hwcontext_vaapi.h av/hwcontext_vdpau.h av/hwcontext_vulkan.h av/imgutils.h av/intfloat.h av/intreadwrite.h av/jni.h av/lfg.h av/log.h av/lzo.h av/macros.h av/mastering_display_metadata.h av/mathematics.h av/md5.h av/mediacodec.h av/mem.h av/motion_vector.h av/murmur3.h av/opt.h av/packet.h av/parseutils.h av/pixdesc.h av/pixelutils.h av/pixfmt.h av/qsv.h av/random_seed.h av/rational.h av/rc4.h av/replaygain.h av/ripemd.h av/rom1394.h av/samplefmt.h av/sha512.h av/sha.h av/spherical.h av/stereo3d.h av/swresample.h av/swscale.h av/tea.h av/threadmessage.h av/timecode.h av/time.h av/timestamp.h av/tree.h av/twofish.h av/tx.h av/vaapi.h av/vdpau.h av/version.h av/video_enc_params.h av/vorbis_parser.h av/xtea.h av/xvmc.h -o av_test.py

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
_libs["avcodec"] = load_library("avcodec")
_libs["avformat"] = load_library("avformat")
_libs["avutil"] = load_library("avutil")
_libs["avdevice"] = load_library("avdevice")
_libs["swresample"] = load_library("swresample")
_libs["swscale"] = load_library("swscale")

# 6 libraries
# End libraries

# No modules

__uint8_t = c_ubyte# /usr/include/bits/types.h: 38

__uint16_t = c_uint# /usr/include/bits/types.h: 40

__uint32_t = c_uint# /usr/include/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/bits/types.h: 45

__off_t = c_long# /usr/include/bits/types.h: 152

__off64_t = c_long# /usr/include/bits/types.h: 153

__pid_t = c_int# /usr/include/bits/types.h: 154

__clock_t = c_long# /usr/include/bits/types.h: 156

__time_t = c_long# /usr/include/bits/types.h: 160

__clockid_t = c_int# /usr/include/bits/types.h: 169

__timer_t = POINTER(None)# /usr/include/bits/types.h: 172

__syscall_slong_t = c_long# /usr/include/bits/types.h: 197

# /home/josiah/ctypesgen_test/av/ac3_parser.h: 32
if _libs["avcodec"].has("av_ac3_parse_header", "cdecl"):
    av_ac3_parse_header = _libs["avcodec"].get("av_ac3_parse_header", "cdecl")
    av_ac3_parse_header.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint16)]
    av_ac3_parse_header.restype = c_int

AVAdler = c_ulong# /home/josiah/ctypesgen_test/av/adler32.h: 44

# /home/josiah/ctypesgen_test/av/adler32.h: 61
if _libs["avcodec"].has("av_adler32_update", "cdecl"):
    av_adler32_update = _libs["avcodec"].get("av_adler32_update", "cdecl")
    av_adler32_update.argtypes = [AVAdler, POINTER(c_uint8), c_uint]
    av_adler32_update.restype = AVAdler

# /home/josiah/ctypesgen_test/av/adts_parser.h: 34
if _libs["avcodec"].has("av_adts_header_parse", "cdecl"):
    av_adts_header_parse = _libs["avcodec"].get("av_adts_header_parse", "cdecl")
    av_adts_header_parse.argtypes = [POINTER(c_uint8), POINTER(c_uint32), POINTER(c_uint8)]
    av_adts_header_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 33
class struct_AVAESCTR(Structure):
    pass

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 38
if _libs["avcodec"].has("av_aes_ctr_alloc", "cdecl"):
    av_aes_ctr_alloc = _libs["avcodec"].get("av_aes_ctr_alloc", "cdecl")
    av_aes_ctr_alloc.argtypes = []
    av_aes_ctr_alloc.restype = POINTER(struct_AVAESCTR)

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 44
if _libs["avcodec"].has("av_aes_ctr_init", "cdecl"):
    av_aes_ctr_init = _libs["avcodec"].get("av_aes_ctr_init", "cdecl")
    av_aes_ctr_init.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_init.restype = c_int

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 49
if _libs["avcodec"].has("av_aes_ctr_free", "cdecl"):
    av_aes_ctr_free = _libs["avcodec"].get("av_aes_ctr_free", "cdecl")
    av_aes_ctr_free.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_free.restype = None

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 57
if _libs["avcodec"].has("av_aes_ctr_crypt", "cdecl"):
    av_aes_ctr_crypt = _libs["avcodec"].get("av_aes_ctr_crypt", "cdecl")
    av_aes_ctr_crypt.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8), POINTER(c_uint8), c_int]
    av_aes_ctr_crypt.restype = None

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 62
if _libs["avcodec"].has("av_aes_ctr_get_iv", "cdecl"):
    av_aes_ctr_get_iv = _libs["avcodec"].get("av_aes_ctr_get_iv", "cdecl")
    av_aes_ctr_get_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_get_iv.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 67
if _libs["avcodec"].has("av_aes_ctr_set_random_iv", "cdecl"):
    av_aes_ctr_set_random_iv = _libs["avcodec"].get("av_aes_ctr_set_random_iv", "cdecl")
    av_aes_ctr_set_random_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_set_random_iv.restype = None

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 72
if _libs["avcodec"].has("av_aes_ctr_set_iv", "cdecl"):
    av_aes_ctr_set_iv = _libs["avcodec"].get("av_aes_ctr_set_iv", "cdecl")
    av_aes_ctr_set_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_set_iv.restype = None

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 77
if _libs["avcodec"].has("av_aes_ctr_set_full_iv", "cdecl"):
    av_aes_ctr_set_full_iv = _libs["avcodec"].get("av_aes_ctr_set_full_iv", "cdecl")
    av_aes_ctr_set_full_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(c_uint8)]
    av_aes_ctr_set_full_iv.restype = None

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 82
if _libs["avcodec"].has("av_aes_ctr_increment_iv", "cdecl"):
    av_aes_ctr_increment_iv = _libs["avcodec"].get("av_aes_ctr_increment_iv", "cdecl")
    av_aes_ctr_increment_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_increment_iv.restype = None

# /home/josiah/ctypesgen_test/av/aes.h: 35
try:
    av_aes_size = (c_int).in_dll(_libs["avcodec"], "av_aes_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/aes.h: 37
class struct_AVAES(Structure):
    pass

# /home/josiah/ctypesgen_test/av/aes.h: 42
if _libs["avcodec"].has("av_aes_alloc", "cdecl"):
    av_aes_alloc = _libs["avcodec"].get("av_aes_alloc", "cdecl")
    av_aes_alloc.argtypes = []
    av_aes_alloc.restype = POINTER(struct_AVAES)

# /home/josiah/ctypesgen_test/av/aes.h: 49
if _libs["avcodec"].has("av_aes_init", "cdecl"):
    av_aes_init = _libs["avcodec"].get("av_aes_init", "cdecl")
    av_aes_init.argtypes = [POINTER(struct_AVAES), POINTER(c_uint8), c_int, c_int]
    av_aes_init.restype = c_int

# /home/josiah/ctypesgen_test/av/aes.h: 59
if _libs["avcodec"].has("av_aes_crypt", "cdecl"):
    av_aes_crypt = _libs["avcodec"].get("av_aes_crypt", "cdecl")
    av_aes_crypt.argtypes = [POINTER(struct_AVAES), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_aes_crypt.restype = None

# /home/josiah/ctypesgen_test/av/avutil.h: 171
if _libs["avcodec"].has("avutil_version", "cdecl"):
    avutil_version = _libs["avcodec"].get("avutil_version", "cdecl")
    avutil_version.argtypes = []
    avutil_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/avutil.h: 178
if _libs["avcodec"].has("av_version_info", "cdecl"):
    av_version_info = _libs["avcodec"].get("av_version_info", "cdecl")
    av_version_info.argtypes = []
    av_version_info.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avutil.h: 183
if _libs["avcodec"].has("avutil_configuration", "cdecl"):
    avutil_configuration = _libs["avcodec"].get("avutil_configuration", "cdecl")
    avutil_configuration.argtypes = []
    avutil_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avutil.h: 188
if _libs["avcodec"].has("avutil_license", "cdecl"):
    avutil_license = _libs["avcodec"].get("avutil_license", "cdecl")
    avutil_license.argtypes = []
    avutil_license.restype = c_char_p

enum_AVMediaType = c_int# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_UNKNOWN = (-1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_VIDEO = (AVMEDIA_TYPE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_AUDIO = (AVMEDIA_TYPE_VIDEO + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_DATA = (AVMEDIA_TYPE_AUDIO + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_SUBTITLE = (AVMEDIA_TYPE_DATA + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_ATTACHMENT = (AVMEDIA_TYPE_SUBTITLE + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

AVMEDIA_TYPE_NB = (AVMEDIA_TYPE_ATTACHMENT + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 199

# /home/josiah/ctypesgen_test/av/avutil.h: 213
if _libs["avcodec"].has("av_get_media_type_string", "cdecl"):
    av_get_media_type_string = _libs["avcodec"].get("av_get_media_type_string", "cdecl")
    av_get_media_type_string.argtypes = [enum_AVMediaType]
    av_get_media_type_string.restype = c_char_p

enum_AVPictureType = c_int# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_NONE = 0# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_I = (AV_PICTURE_TYPE_NONE + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_P = (AV_PICTURE_TYPE_I + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_B = (AV_PICTURE_TYPE_P + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_S = (AV_PICTURE_TYPE_B + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_SI = (AV_PICTURE_TYPE_S + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_SP = (AV_PICTURE_TYPE_SI + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

AV_PICTURE_TYPE_BI = (AV_PICTURE_TYPE_SP + 1)# /home/josiah/ctypesgen_test/av/avutil.h: 272

# /home/josiah/ctypesgen_test/av/avutil.h: 290
if _libs["avcodec"].has("av_get_picture_type_char", "cdecl"):
    av_get_picture_type_char = _libs["avcodec"].get("av_get_picture_type_char", "cdecl")
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

pid_t = __pid_t# /usr/include/sys/types.h: 97

clock_t = __clock_t# /usr/include/bits/types/clock_t.h: 7

clockid_t = __clockid_t# /usr/include/bits/types/clockid_t.h: 7

time_t = __time_t# /usr/include/bits/types/time_t.h: 7

timer_t = __timer_t# /usr/include/bits/types/timer_t.h: 7

u_int8_t = __uint8_t# /usr/include/sys/types.h: 158

u_int16_t = __uint16_t# /usr/include/sys/types.h: 159

u_int32_t = __uint32_t# /usr/include/sys/types.h: 160

u_int64_t = __uint64_t# /usr/include/sys/types.h: 161

# /usr/include/bits/types/struct_timespec.h: 10
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

# /home/josiah/ctypesgen_test/av/common.h: 186
if _libs["avcodec"].has("av_log2", "cdecl"):
    av_log2 = _libs["avcodec"].get("av_log2", "cdecl")
    av_log2.argtypes = [c_uint]
    av_log2.restype = c_int

# /home/josiah/ctypesgen_test/av/common.h: 190
if _libs["avcodec"].has("av_log2_16bit", "cdecl"):
    av_log2_16bit = _libs["avcodec"].get("av_log2_16bit", "cdecl")
    av_log2_16bit.argtypes = [c_uint]
    av_log2_16bit.restype = c_int

# /home/josiah/ctypesgen_test/av/common.h: 376
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/common.h: 395
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/error.h: 97
if _libs["avcodec"].has("av_strerror", "cdecl"):
    av_strerror = _libs["avcodec"].get("av_strerror", "cdecl")
    av_strerror.argtypes = [c_int, String, c_size_t]
    av_strerror.restype = c_int

# /home/josiah/ctypesgen_test/av/mem.h: 202
if _libs["avcodec"].has("av_malloc", "cdecl"):
    av_malloc = _libs["avcodec"].get("av_malloc", "cdecl")
    av_malloc.argtypes = [c_size_t]
    av_malloc.restype = POINTER(c_ubyte)
    av_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 213
if _libs["avcodec"].has("av_mallocz", "cdecl"):
    av_mallocz = _libs["avcodec"].get("av_mallocz", "cdecl")
    av_mallocz.argtypes = [c_size_t]
    av_mallocz.restype = POINTER(c_ubyte)
    av_mallocz.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 226
if _libs["avcodec"].has("av_malloc_array", "cdecl"):
    av_malloc_array = _libs["avcodec"].get("av_malloc_array", "cdecl")
    av_malloc_array.argtypes = [c_size_t, c_size_t]
    av_malloc_array.restype = POINTER(c_ubyte)
    av_malloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 241
if _libs["avcodec"].has("av_mallocz_array", "cdecl"):
    av_mallocz_array = _libs["avcodec"].get("av_mallocz_array", "cdecl")
    av_mallocz_array.argtypes = [c_size_t, c_size_t]
    av_mallocz_array.restype = POINTER(c_ubyte)
    av_mallocz_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 248
if _libs["avcodec"].has("av_calloc", "cdecl"):
    av_calloc = _libs["avcodec"].get("av_calloc", "cdecl")
    av_calloc.argtypes = [c_size_t, c_size_t]
    av_calloc.restype = POINTER(c_ubyte)
    av_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 270
if _libs["avcodec"].has("av_realloc", "cdecl"):
    av_realloc = _libs["avcodec"].get("av_realloc", "cdecl")
    av_realloc.argtypes = [POINTER(None), c_size_t]
    av_realloc.restype = POINTER(c_ubyte)
    av_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 292
if _libs["avcodec"].has("av_reallocp", "cdecl"):
    av_reallocp = _libs["avcodec"].get("av_reallocp", "cdecl")
    av_reallocp.argtypes = [POINTER(None), c_size_t]
    av_reallocp.restype = c_int

# /home/josiah/ctypesgen_test/av/mem.h: 309
if _libs["avcodec"].has("av_realloc_f", "cdecl"):
    av_realloc_f = _libs["avcodec"].get("av_realloc_f", "cdecl")
    av_realloc_f.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_f.restype = POINTER(c_ubyte)
    av_realloc_f.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 329
if _libs["avcodec"].has("av_realloc_array", "cdecl"):
    av_realloc_array = _libs["avcodec"].get("av_realloc_array", "cdecl")
    av_realloc_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_array.restype = POINTER(c_ubyte)
    av_realloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 348
if _libs["avcodec"].has("av_reallocp_array", "cdecl"):
    av_reallocp_array = _libs["avcodec"].get("av_reallocp_array", "cdecl")
    av_reallocp_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_reallocp_array.restype = c_int

# /home/josiah/ctypesgen_test/av/mem.h: 382
if _libs["avcodec"].has("av_fast_realloc", "cdecl"):
    av_fast_realloc = _libs["avcodec"].get("av_fast_realloc", "cdecl")
    av_fast_realloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_realloc.restype = POINTER(c_ubyte)
    av_fast_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 413
if _libs["avcodec"].has("av_fast_malloc", "cdecl"):
    av_fast_malloc = _libs["avcodec"].get("av_fast_malloc", "cdecl")
    av_fast_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_malloc.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 433
if _libs["avcodec"].has("av_fast_mallocz", "cdecl"):
    av_fast_mallocz = _libs["avcodec"].get("av_fast_mallocz", "cdecl")
    av_fast_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_mallocz.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 446
if _libs["avcodec"].has("av_free", "cdecl"):
    av_free = _libs["avcodec"].get("av_free", "cdecl")
    av_free.argtypes = [POINTER(None)]
    av_free.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 469
if _libs["avcodec"].has("av_freep", "cdecl"):
    av_freep = _libs["avcodec"].get("av_freep", "cdecl")
    av_freep.argtypes = [POINTER(None)]
    av_freep.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 479
if _libs["avcodec"].has("av_strdup", "cdecl"):
    av_strdup = _libs["avcodec"].get("av_strdup", "cdecl")
    av_strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strdup.restype = ReturnString
    else:
        av_strdup.restype = String
        av_strdup.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/mem.h: 490
if _libs["avcodec"].has("av_strndup", "cdecl"):
    av_strndup = _libs["avcodec"].get("av_strndup", "cdecl")
    av_strndup.argtypes = [String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strndup.restype = ReturnString
    else:
        av_strndup.restype = String
        av_strndup.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/mem.h: 500
if _libs["avcodec"].has("av_memdup", "cdecl"):
    av_memdup = _libs["avcodec"].get("av_memdup", "cdecl")
    av_memdup.argtypes = [POINTER(None), c_size_t]
    av_memdup.restype = POINTER(c_ubyte)
    av_memdup.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 513
if _libs["avcodec"].has("av_memcpy_backptr", "cdecl"):
    av_memcpy_backptr = _libs["avcodec"].get("av_memcpy_backptr", "cdecl")
    av_memcpy_backptr.argtypes = [POINTER(c_uint8), c_int, c_int]
    av_memcpy_backptr.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 615
if _libs["avcodec"].has("av_dynarray_add", "cdecl"):
    av_dynarray_add = _libs["avcodec"].get("av_dynarray_add", "cdecl")
    av_dynarray_add.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add.restype = None

# /home/josiah/ctypesgen_test/av/mem.h: 628
if _libs["avcodec"].has("av_dynarray_add_nofree", "cdecl"):
    av_dynarray_add_nofree = _libs["avcodec"].get("av_dynarray_add_nofree", "cdecl")
    av_dynarray_add_nofree.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add_nofree.restype = c_int

# /home/josiah/ctypesgen_test/av/mem.h: 653
if _libs["avcodec"].has("av_dynarray2_add", "cdecl"):
    av_dynarray2_add = _libs["avcodec"].get("av_dynarray2_add", "cdecl")
    av_dynarray2_add.argtypes = [POINTER(POINTER(None)), POINTER(c_int), c_size_t, POINTER(c_uint8)]
    av_dynarray2_add.restype = POINTER(c_ubyte)
    av_dynarray2_add.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/mem.h: 677
for _lib in _libs.values():
    try:
        t = (c_size_t).in_dll(_lib, "t")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/mem.h: 699
if _libs["avcodec"].has("av_max_alloc", "cdecl"):
    av_max_alloc = _libs["avcodec"].get("av_max_alloc", "cdecl")
    av_max_alloc.argtypes = [c_size_t]
    av_max_alloc.restype = None

# /home/josiah/ctypesgen_test/av/rational.h: 61
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

AVRational = struct_AVRational# /home/josiah/ctypesgen_test/av/rational.h: 61

# /home/josiah/ctypesgen_test/av/rational.h: 73
for _lib in _libs.values():
    try:
        r = (AVRational).in_dll(_lib, "r")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/rational.h: 90
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/rational.h: 120
if _libs["avcodec"].has("av_reduce", "cdecl"):
    av_reduce = _libs["avcodec"].get("av_reduce", "cdecl")
    av_reduce.argtypes = [POINTER(c_int), POINTER(c_int), c_int64, c_int64, c_int64]
    av_reduce.restype = c_int

# /home/josiah/ctypesgen_test/av/rational.h: 128
if _libs["avcodec"].has("av_mul_q", "cdecl"):
    av_mul_q = _libs["avcodec"].get("av_mul_q", "cdecl")
    av_mul_q.argtypes = [AVRational, AVRational]
    av_mul_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/rational.h: 136
if _libs["avcodec"].has("av_div_q", "cdecl"):
    av_div_q = _libs["avcodec"].get("av_div_q", "cdecl")
    av_div_q.argtypes = [AVRational, AVRational]
    av_div_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/rational.h: 144
if _libs["avcodec"].has("av_add_q", "cdecl"):
    av_add_q = _libs["avcodec"].get("av_add_q", "cdecl")
    av_add_q.argtypes = [AVRational, AVRational]
    av_add_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/rational.h: 152
if _libs["avcodec"].has("av_sub_q", "cdecl"):
    av_sub_q = _libs["avcodec"].get("av_sub_q", "cdecl")
    av_sub_q.argtypes = [AVRational, AVRational]
    av_sub_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/rational.h: 161
for _lib in _libs.values():
    try:
        r = (AVRational).in_dll(_lib, "r")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/rational.h: 176
if _libs["avcodec"].has("av_d2q", "cdecl"):
    av_d2q = _libs["avcodec"].get("av_d2q", "cdecl")
    av_d2q.argtypes = [c_double, c_int]
    av_d2q.restype = AVRational

# /home/josiah/ctypesgen_test/av/rational.h: 188
if _libs["avcodec"].has("av_nearer_q", "cdecl"):
    av_nearer_q = _libs["avcodec"].get("av_nearer_q", "cdecl")
    av_nearer_q.argtypes = [AVRational, AVRational, AVRational]
    av_nearer_q.restype = c_int

# /home/josiah/ctypesgen_test/av/rational.h: 197
if _libs["avcodec"].has("av_find_nearest_q_idx", "cdecl"):
    av_find_nearest_q_idx = _libs["avcodec"].get("av_find_nearest_q_idx", "cdecl")
    av_find_nearest_q_idx.argtypes = [AVRational, POINTER(AVRational)]
    av_find_nearest_q_idx.restype = c_int

# /home/josiah/ctypesgen_test/av/rational.h: 208
if _libs["avcodec"].has("av_q2intfloat", "cdecl"):
    av_q2intfloat = _libs["avcodec"].get("av_q2intfloat", "cdecl")
    av_q2intfloat.argtypes = [AVRational]
    av_q2intfloat.restype = c_uint32

# /home/josiah/ctypesgen_test/av/rational.h: 214
if _libs["avcodec"].has("av_gcd_q", "cdecl"):
    av_gcd_q = _libs["avcodec"].get("av_gcd_q", "cdecl")
    av_gcd_q.argtypes = [AVRational, AVRational, c_int, AVRational]
    av_gcd_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/intfloat.h: 27
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

# /home/josiah/ctypesgen_test/av/intfloat.h: 32
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

# /home/josiah/ctypesgen_test/av/intfloat.h: 42
for _lib in _libs.values():
    try:
        v = (union_av_intfloat32).in_dll(_lib, "v")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/intfloat.h: 52
for _lib in _libs.values():
    try:
        v = (union_av_intfloat32).in_dll(_lib, "v")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/intfloat.h: 62
for _lib in _libs.values():
    try:
        v = (union_av_intfloat64).in_dll(_lib, "v")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/intfloat.h: 72
for _lib in _libs.values():
    try:
        v = (union_av_intfloat64).in_dll(_lib, "v")
        break
    except:
        pass

enum_AVRounding = c_int# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_ZERO = 0# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_INF = 1# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_DOWN = 2# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_UP = 3# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_NEAR_INF = 5# /home/josiah/ctypesgen_test/av/mathematics.h: 79

AV_ROUND_PASS_MINMAX = 8192# /home/josiah/ctypesgen_test/av/mathematics.h: 79

# /home/josiah/ctypesgen_test/av/mathematics.h: 118
if _libs["avcodec"].has("av_gcd", "cdecl"):
    av_gcd = _libs["avcodec"].get("av_gcd", "cdecl")
    av_gcd.argtypes = [c_int64, c_int64]
    av_gcd.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 130
if _libs["avcodec"].has("av_rescale", "cdecl"):
    av_rescale = _libs["avcodec"].get("av_rescale", "cdecl")
    av_rescale.argtypes = [c_int64, c_int64, c_int64]
    av_rescale.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 140
if _libs["avcodec"].has("av_rescale_rnd", "cdecl"):
    av_rescale_rnd = _libs["avcodec"].get("av_rescale_rnd", "cdecl")
    av_rescale_rnd.argtypes = [c_int64, c_int64, c_int64, enum_AVRounding]
    av_rescale_rnd.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 151
if _libs["avcodec"].has("av_rescale_q", "cdecl"):
    av_rescale_q = _libs["avcodec"].get("av_rescale_q", "cdecl")
    av_rescale_q.argtypes = [c_int64, AVRational, AVRational]
    av_rescale_q.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 160
if _libs["avcodec"].has("av_rescale_q_rnd", "cdecl"):
    av_rescale_q_rnd = _libs["avcodec"].get("av_rescale_q_rnd", "cdecl")
    av_rescale_q_rnd.argtypes = [c_int64, AVRational, AVRational, enum_AVRounding]
    av_rescale_q_rnd.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 175
if _libs["avcodec"].has("av_compare_ts", "cdecl"):
    av_compare_ts = _libs["avcodec"].get("av_compare_ts", "cdecl")
    av_compare_ts.argtypes = [c_int64, AVRational, c_int64, AVRational]
    av_compare_ts.restype = c_int

# /home/josiah/ctypesgen_test/av/mathematics.h: 195
if _libs["avcodec"].has("av_compare_mod", "cdecl"):
    av_compare_mod = _libs["avcodec"].get("av_compare_mod", "cdecl")
    av_compare_mod.argtypes = [c_uint64, c_uint64, c_uint64]
    av_compare_mod.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 222
if _libs["avcodec"].has("av_rescale_delta", "cdecl"):
    av_rescale_delta = _libs["avcodec"].get("av_rescale_delta", "cdecl")
    av_rescale_delta.argtypes = [AVRational, c_int64, AVRational, c_int, POINTER(c_int64), AVRational]
    av_rescale_delta.restype = c_int64

# /home/josiah/ctypesgen_test/av/mathematics.h: 235
if _libs["avcodec"].has("av_add_stable", "cdecl"):
    av_add_stable = _libs["avcodec"].get("av_add_stable", "cdecl")
    av_add_stable.argtypes = [AVRational, c_int64, AVRational, c_int64]
    av_add_stable.restype = c_int64

enum_anon_25 = c_int# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_NA = 0# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_INPUT = (AV_CLASS_CATEGORY_NA + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_OUTPUT = (AV_CLASS_CATEGORY_INPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_MUXER = (AV_CLASS_CATEGORY_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEMUXER = (AV_CLASS_CATEGORY_MUXER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_ENCODER = (AV_CLASS_CATEGORY_DEMUXER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DECODER = (AV_CLASS_CATEGORY_ENCODER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_FILTER = (AV_CLASS_CATEGORY_DECODER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_BITSTREAM_FILTER = (AV_CLASS_CATEGORY_FILTER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_SWSCALER = (AV_CLASS_CATEGORY_BITSTREAM_FILTER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_SWRESAMPLER = (AV_CLASS_CATEGORY_SWSCALER + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT = 40# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_DEVICE_INPUT = (AV_CLASS_CATEGORY_DEVICE_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AV_CLASS_CATEGORY_NB = (AV_CLASS_CATEGORY_DEVICE_INPUT + 1)# /home/josiah/ctypesgen_test/av/log.h: 48

AVClassCategory = enum_anon_25# /home/josiah/ctypesgen_test/av/log.h: 48

# /usr/include/libavutil/opt.h: 333
class struct_AVOptionRanges(Structure):
    pass

# /usr/include/libavutil/opt.h: 248
class struct_AVOption(Structure):
    pass

# /home/josiah/ctypesgen_test/av/log.h: 67
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

AVClass = struct_AVClass# /home/josiah/ctypesgen_test/av/log.h: 161

# /home/josiah/ctypesgen_test/av/log.h: 252
if _libs["avcodec"].has("av_log", "cdecl"):
    _func = _libs["avcodec"].get("av_log", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, String]
    av_log = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/log.h: 273
if _libs["avcodec"].has("av_log_once", "cdecl"):
    _func = _libs["avcodec"].get("av_log_once", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, c_int, POINTER(c_int), String]
    av_log_once = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/log.h: 291
if _libs["avcodec"].has("av_vlog", "cdecl"):
    av_vlog = _libs["avcodec"].get("av_vlog", "cdecl")
    av_vlog.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_vlog.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 300
if _libs["avcodec"].has("av_log_get_level", "cdecl"):
    av_log_get_level = _libs["avcodec"].get("av_log_get_level", "cdecl")
    av_log_get_level.argtypes = []
    av_log_get_level.restype = c_int

# /home/josiah/ctypesgen_test/av/log.h: 309
if _libs["avcodec"].has("av_log_set_level", "cdecl"):
    av_log_set_level = _libs["avcodec"].get("av_log_set_level", "cdecl")
    av_log_set_level.argtypes = [c_int]
    av_log_set_level.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 321
if _libs["avcodec"].has("av_log_set_callback", "cdecl"):
    av_log_set_callback = _libs["avcodec"].get("av_log_set_callback", "cdecl")
    av_log_set_callback.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, String, c_void_p)]
    av_log_set_callback.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 336
if _libs["avcodec"].has("av_log_default_callback", "cdecl"):
    av_log_default_callback = _libs["avcodec"].get("av_log_default_callback", "cdecl")
    av_log_default_callback.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_log_default_callback.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 346
if _libs["avcodec"].has("av_default_item_name", "cdecl"):
    av_default_item_name = _libs["avcodec"].get("av_default_item_name", "cdecl")
    av_default_item_name.argtypes = [POINTER(None)]
    av_default_item_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/log.h: 347
if _libs["avcodec"].has("av_default_get_category", "cdecl"):
    av_default_get_category = _libs["avcodec"].get("av_default_get_category", "cdecl")
    av_default_get_category.argtypes = [POINTER(None)]
    av_default_get_category.restype = AVClassCategory

# /home/josiah/ctypesgen_test/av/log.h: 356
if _libs["avcodec"].has("av_log_format_line", "cdecl"):
    av_log_format_line = _libs["avcodec"].get("av_log_format_line", "cdecl")
    av_log_format_line.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 373
if _libs["avcodec"].has("av_log_format_line2", "cdecl"):
    av_log_format_line2 = _libs["avcodec"].get("av_log_format_line2", "cdecl")
    av_log_format_line2.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line2.restype = c_int

# /home/josiah/ctypesgen_test/av/log.h: 394
if _libs["avcodec"].has("av_log_set_flags", "cdecl"):
    av_log_set_flags = _libs["avcodec"].get("av_log_set_flags", "cdecl")
    av_log_set_flags.argtypes = [c_int]
    av_log_set_flags.restype = None

# /home/josiah/ctypesgen_test/av/log.h: 395
if _libs["avcodec"].has("av_log_get_flags", "cdecl"):
    av_log_get_flags = _libs["avcodec"].get("av_log_get_flags", "cdecl")
    av_log_get_flags.argtypes = []
    av_log_get_flags.restype = c_int

enum_AVPixelFormat = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NONE = (-1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P = (AV_PIX_FMT_NONE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUYV422 = (AV_PIX_FMT_YUV420P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB24 = (AV_PIX_FMT_YUYV422 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR24 = (AV_PIX_FMT_RGB24 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P = (AV_PIX_FMT_BGR24 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P = (AV_PIX_FMT_YUV422P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV410P = (AV_PIX_FMT_YUV444P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV411P = (AV_PIX_FMT_YUV410P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY8 = (AV_PIX_FMT_YUV411P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_MONOWHITE = (AV_PIX_FMT_GRAY8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_MONOBLACK = (AV_PIX_FMT_MONOWHITE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_PAL8 = (AV_PIX_FMT_MONOBLACK + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVJ420P = (AV_PIX_FMT_PAL8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVJ422P = (AV_PIX_FMT_YUVJ420P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVJ444P = (AV_PIX_FMT_YUVJ422P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_UYVY422 = (AV_PIX_FMT_YUVJ444P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_UYYVYY411 = (AV_PIX_FMT_UYVY422 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR8 = (AV_PIX_FMT_UYYVYY411 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR4 = (AV_PIX_FMT_BGR8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR4_BYTE = (AV_PIX_FMT_BGR4 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB8 = (AV_PIX_FMT_BGR4_BYTE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB4 = (AV_PIX_FMT_RGB8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB4_BYTE = (AV_PIX_FMT_RGB4 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV12 = (AV_PIX_FMT_RGB4_BYTE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV21 = (AV_PIX_FMT_NV12 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_ARGB = (AV_PIX_FMT_NV21 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGBA = (AV_PIX_FMT_ARGB + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_ABGR = (AV_PIX_FMT_RGBA + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGRA = (AV_PIX_FMT_ABGR + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY16BE = (AV_PIX_FMT_BGRA + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY16LE = (AV_PIX_FMT_GRAY16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV440P = (AV_PIX_FMT_GRAY16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVJ440P = (AV_PIX_FMT_YUV440P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P = (AV_PIX_FMT_YUVJ440P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB48BE = (AV_PIX_FMT_YUVA420P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB48LE = (AV_PIX_FMT_RGB48BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB565BE = (AV_PIX_FMT_RGB48LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB565LE = (AV_PIX_FMT_RGB565BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB555BE = (AV_PIX_FMT_RGB565LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB555LE = (AV_PIX_FMT_RGB555BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR565BE = (AV_PIX_FMT_RGB555LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR565LE = (AV_PIX_FMT_BGR565BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR555BE = (AV_PIX_FMT_BGR565LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR555LE = (AV_PIX_FMT_BGR555BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VAAPI_MOCO = (AV_PIX_FMT_BGR555LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VAAPI_IDCT = (AV_PIX_FMT_VAAPI_MOCO + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VAAPI_VLD = (AV_PIX_FMT_VAAPI_IDCT + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VAAPI = AV_PIX_FMT_VAAPI_VLD# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P16LE = (AV_PIX_FMT_VAAPI + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P16BE = (AV_PIX_FMT_YUV420P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P16LE = (AV_PIX_FMT_YUV420P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P16BE = (AV_PIX_FMT_YUV422P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P16LE = (AV_PIX_FMT_YUV422P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P16BE = (AV_PIX_FMT_YUV444P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_DXVA2_VLD = (AV_PIX_FMT_YUV444P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB444LE = (AV_PIX_FMT_DXVA2_VLD + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB444BE = (AV_PIX_FMT_RGB444LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR444LE = (AV_PIX_FMT_RGB444BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR444BE = (AV_PIX_FMT_BGR444LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YA8 = (AV_PIX_FMT_BGR444BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_Y400A = AV_PIX_FMT_YA8# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY8A = AV_PIX_FMT_YA8# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR48BE = (AV_PIX_FMT_GRAY8A + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR48LE = (AV_PIX_FMT_BGR48BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P9BE = (AV_PIX_FMT_BGR48LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P9LE = (AV_PIX_FMT_YUV420P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P10BE = (AV_PIX_FMT_YUV420P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P10LE = (AV_PIX_FMT_YUV420P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P10BE = (AV_PIX_FMT_YUV420P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P10LE = (AV_PIX_FMT_YUV422P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P9BE = (AV_PIX_FMT_YUV422P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P9LE = (AV_PIX_FMT_YUV444P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P10BE = (AV_PIX_FMT_YUV444P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P10LE = (AV_PIX_FMT_YUV444P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P9BE = (AV_PIX_FMT_YUV444P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P9LE = (AV_PIX_FMT_YUV422P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP = (AV_PIX_FMT_YUV422P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBR24P = AV_PIX_FMT_GBRP# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP9BE = (AV_PIX_FMT_GBR24P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP9LE = (AV_PIX_FMT_GBRP9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP10BE = (AV_PIX_FMT_GBRP9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP10LE = (AV_PIX_FMT_GBRP10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP16BE = (AV_PIX_FMT_GBRP10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP16LE = (AV_PIX_FMT_GBRP16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P = (AV_PIX_FMT_GBRP16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P = (AV_PIX_FMT_YUVA422P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P9BE = (AV_PIX_FMT_YUVA444P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P9LE = (AV_PIX_FMT_YUVA420P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P9BE = (AV_PIX_FMT_YUVA420P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P9LE = (AV_PIX_FMT_YUVA422P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P9BE = (AV_PIX_FMT_YUVA422P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P9LE = (AV_PIX_FMT_YUVA444P9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P10BE = (AV_PIX_FMT_YUVA444P9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P10LE = (AV_PIX_FMT_YUVA420P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P10BE = (AV_PIX_FMT_YUVA420P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P10LE = (AV_PIX_FMT_YUVA422P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P10BE = (AV_PIX_FMT_YUVA422P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P10LE = (AV_PIX_FMT_YUVA444P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P16BE = (AV_PIX_FMT_YUVA444P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA420P16LE = (AV_PIX_FMT_YUVA420P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P16BE = (AV_PIX_FMT_YUVA420P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P16LE = (AV_PIX_FMT_YUVA422P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P16BE = (AV_PIX_FMT_YUVA422P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P16LE = (AV_PIX_FMT_YUVA444P16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VDPAU = (AV_PIX_FMT_YUVA444P16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_XYZ12LE = (AV_PIX_FMT_VDPAU + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_XYZ12BE = (AV_PIX_FMT_XYZ12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV16 = (AV_PIX_FMT_XYZ12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV20LE = (AV_PIX_FMT_NV16 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV20BE = (AV_PIX_FMT_NV20LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGBA64BE = (AV_PIX_FMT_NV20BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGBA64LE = (AV_PIX_FMT_RGBA64BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGRA64BE = (AV_PIX_FMT_RGBA64LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGRA64LE = (AV_PIX_FMT_BGRA64BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YVYU422 = (AV_PIX_FMT_BGRA64LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YA16BE = (AV_PIX_FMT_YVYU422 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YA16LE = (AV_PIX_FMT_YA16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP = (AV_PIX_FMT_YA16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP16BE = (AV_PIX_FMT_GBRAP + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP16LE = (AV_PIX_FMT_GBRAP16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_QSV = (AV_PIX_FMT_GBRAP16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_MMAL = (AV_PIX_FMT_QSV + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_D3D11VA_VLD = (AV_PIX_FMT_MMAL + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_CUDA = (AV_PIX_FMT_D3D11VA_VLD + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_0RGB = (AV_PIX_FMT_CUDA + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_RGB0 = (AV_PIX_FMT_0RGB + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_0BGR = (AV_PIX_FMT_RGB0 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BGR0 = (AV_PIX_FMT_0BGR + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P12BE = (AV_PIX_FMT_BGR0 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P12LE = (AV_PIX_FMT_YUV420P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P14BE = (AV_PIX_FMT_YUV420P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV420P14LE = (AV_PIX_FMT_YUV420P14BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P12BE = (AV_PIX_FMT_YUV420P14LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P12LE = (AV_PIX_FMT_YUV422P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P14BE = (AV_PIX_FMT_YUV422P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV422P14LE = (AV_PIX_FMT_YUV422P14BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P12BE = (AV_PIX_FMT_YUV422P14LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P12LE = (AV_PIX_FMT_YUV444P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P14BE = (AV_PIX_FMT_YUV444P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV444P14LE = (AV_PIX_FMT_YUV444P14BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP12BE = (AV_PIX_FMT_YUV444P14LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP12LE = (AV_PIX_FMT_GBRP12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP14BE = (AV_PIX_FMT_GBRP12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRP14LE = (AV_PIX_FMT_GBRP14BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVJ411P = (AV_PIX_FMT_GBRP14LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR8 = (AV_PIX_FMT_YUVJ411P + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB8 = (AV_PIX_FMT_BAYER_BGGR8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG8 = (AV_PIX_FMT_BAYER_RGGB8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG8 = (AV_PIX_FMT_BAYER_GBRG8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR16LE = (AV_PIX_FMT_BAYER_GRBG8 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_BGGR16BE = (AV_PIX_FMT_BAYER_BGGR16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB16LE = (AV_PIX_FMT_BAYER_BGGR16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_RGGB16BE = (AV_PIX_FMT_BAYER_RGGB16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG16LE = (AV_PIX_FMT_BAYER_RGGB16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GBRG16BE = (AV_PIX_FMT_BAYER_GBRG16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG16LE = (AV_PIX_FMT_BAYER_GBRG16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_BAYER_GRBG16BE = (AV_PIX_FMT_BAYER_GRBG16LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_XVMC = (AV_PIX_FMT_BAYER_GRBG16BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV440P10LE = (AV_PIX_FMT_XVMC + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV440P10BE = (AV_PIX_FMT_YUV440P10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV440P12LE = (AV_PIX_FMT_YUV440P10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUV440P12BE = (AV_PIX_FMT_YUV440P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_AYUV64LE = (AV_PIX_FMT_YUV440P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_AYUV64BE = (AV_PIX_FMT_AYUV64LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VIDEOTOOLBOX = (AV_PIX_FMT_AYUV64BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_P010LE = (AV_PIX_FMT_VIDEOTOOLBOX + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_P010BE = (AV_PIX_FMT_P010LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP12BE = (AV_PIX_FMT_P010BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP12LE = (AV_PIX_FMT_GBRAP12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP10BE = (AV_PIX_FMT_GBRAP12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAP10LE = (AV_PIX_FMT_GBRAP10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_MEDIACODEC = (AV_PIX_FMT_GBRAP10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY12BE = (AV_PIX_FMT_MEDIACODEC + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY12LE = (AV_PIX_FMT_GRAY12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY10BE = (AV_PIX_FMT_GRAY12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY10LE = (AV_PIX_FMT_GRAY10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_P016LE = (AV_PIX_FMT_GRAY10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_P016BE = (AV_PIX_FMT_P016LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_D3D11 = (AV_PIX_FMT_P016BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY9BE = (AV_PIX_FMT_D3D11 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY9LE = (AV_PIX_FMT_GRAY9BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRPF32BE = (AV_PIX_FMT_GRAY9LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRPF32LE = (AV_PIX_FMT_GBRPF32BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAPF32BE = (AV_PIX_FMT_GBRPF32LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GBRAPF32LE = (AV_PIX_FMT_GBRAPF32BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_DRM_PRIME = (AV_PIX_FMT_GBRAPF32LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_OPENCL = (AV_PIX_FMT_DRM_PRIME + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY14BE = (AV_PIX_FMT_OPENCL + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAY14LE = (AV_PIX_FMT_GRAY14BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAYF32BE = (AV_PIX_FMT_GRAY14LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_GRAYF32LE = (AV_PIX_FMT_GRAYF32BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P12BE = (AV_PIX_FMT_GRAYF32LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA422P12LE = (AV_PIX_FMT_YUVA422P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P12BE = (AV_PIX_FMT_YUVA422P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_YUVA444P12LE = (AV_PIX_FMT_YUVA444P12BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV24 = (AV_PIX_FMT_YUVA444P12LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NV42 = (AV_PIX_FMT_NV24 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_VULKAN = (AV_PIX_FMT_NV42 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_Y210BE = (AV_PIX_FMT_VULKAN + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_Y210LE = (AV_PIX_FMT_Y210BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_X2RGB10LE = (AV_PIX_FMT_Y210LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_X2RGB10BE = (AV_PIX_FMT_X2RGB10LE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

AV_PIX_FMT_NB = (AV_PIX_FMT_X2RGB10BE + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 64

enum_AVColorPrimaries = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_RESERVED0 = 0# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_BT709 = 1# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_UNSPECIFIED = 2# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_RESERVED = 3# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_BT470M = 4# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_BT470BG = 5# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTE170M = 6# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTE240M = 7# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_FILM = 8# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_BT2020 = 9# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTE428 = 10# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTEST428_1 = AVCOL_PRI_SMPTE428# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTE431 = 11# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_SMPTE432 = 12# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_EBU3213 = 22# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_JEDEC_P22 = AVCOL_PRI_EBU3213# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

AVCOL_PRI_NB = (AVCOL_PRI_JEDEC_P22 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 458

enum_AVColorTransferCharacteristic = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_RESERVED0 = 0# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_BT709 = 1# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_UNSPECIFIED = 2# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_RESERVED = 3# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_GAMMA22 = 4# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_GAMMA28 = 5# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTE170M = 6# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTE240M = 7# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_LINEAR = 8# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_LOG = 9# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_LOG_SQRT = 10# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_IEC61966_2_4 = 11# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_BT1361_ECG = 12# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_IEC61966_2_1 = 13# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_BT2020_10 = 14# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_BT2020_12 = 15# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTE2084 = 16# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTEST2084 = AVCOL_TRC_SMPTE2084# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTE428 = 17# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_SMPTEST428_1 = AVCOL_TRC_SMPTE428# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_ARIB_STD_B67 = 18# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

AVCOL_TRC_NB = (AVCOL_TRC_ARIB_STD_B67 + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 483

enum_AVColorSpace = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_RGB = 0# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_BT709 = 1# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_UNSPECIFIED = 2# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_RESERVED = 3# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_FCC = 4# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_BT470BG = 5# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_SMPTE170M = 6# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_SMPTE240M = 7# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_YCGCO = 8# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_YCOCG = AVCOL_SPC_YCGCO# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_BT2020_NCL = 9# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_BT2020_CL = 10# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_SMPTE2085 = 11# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_CHROMA_DERIVED_NCL = 12# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_CHROMA_DERIVED_CL = 13# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_ICTCP = 14# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

AVCOL_SPC_NB = (AVCOL_SPC_ICTCP + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 512

enum_AVColorRange = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 551

AVCOL_RANGE_UNSPECIFIED = 0# /home/josiah/ctypesgen_test/av/pixfmt.h: 551

AVCOL_RANGE_MPEG = 1# /home/josiah/ctypesgen_test/av/pixfmt.h: 551

AVCOL_RANGE_JPEG = 2# /home/josiah/ctypesgen_test/av/pixfmt.h: 551

AVCOL_RANGE_NB = (AVCOL_RANGE_JPEG + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 551

enum_AVChromaLocation = c_int# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_UNSPECIFIED = 0# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_LEFT = 1# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_CENTER = 2# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_TOPLEFT = 3# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_TOP = 4# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_BOTTOMLEFT = 5# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_BOTTOM = 6# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

AVCHROMA_LOC_NB = (AVCHROMA_LOC_BOTTOM + 1)# /home/josiah/ctypesgen_test/av/pixfmt.h: 605

# /home/josiah/ctypesgen_test/av/avutil.h: 321
if _libs["avcodec"].has("av_int_list_length_for_size", "cdecl"):
    av_int_list_length_for_size = _libs["avcodec"].get("av_int_list_length_for_size", "cdecl")
    av_int_list_length_for_size.argtypes = [c_uint, POINTER(None), c_uint64]
    av_int_list_length_for_size.restype = c_uint

# /home/josiah/ctypesgen_test/av/avutil.h: 339
if _libs["avcodec"].has("av_fopen_utf8", "cdecl"):
    av_fopen_utf8 = _libs["avcodec"].get("av_fopen_utf8", "cdecl")
    av_fopen_utf8.argtypes = [String, String]
    av_fopen_utf8.restype = POINTER(FILE)

# /home/josiah/ctypesgen_test/av/avutil.h: 344
if _libs["avcodec"].has("av_get_time_base_q", "cdecl"):
    av_get_time_base_q = _libs["avcodec"].get("av_get_time_base_q", "cdecl")
    av_get_time_base_q.argtypes = []
    av_get_time_base_q.restype = AVRational

# /home/josiah/ctypesgen_test/av/avutil.h: 358
if _libs["avcodec"].has("av_fourcc_make_string", "cdecl"):
    av_fourcc_make_string = _libs["avcodec"].get("av_fourcc_make_string", "cdecl")
    av_fourcc_make_string.argtypes = [String, c_uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        av_fourcc_make_string.restype = ReturnString
    else:
        av_fourcc_make_string.restype = String
        av_fourcc_make_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/fifo.h: 35
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

AVFifoBuffer = struct_AVFifoBuffer# /home/josiah/ctypesgen_test/av/fifo.h: 35

# /home/josiah/ctypesgen_test/av/fifo.h: 42
if _libs["avcodec"].has("av_fifo_alloc", "cdecl"):
    av_fifo_alloc = _libs["avcodec"].get("av_fifo_alloc", "cdecl")
    av_fifo_alloc.argtypes = [c_uint]
    av_fifo_alloc.restype = POINTER(AVFifoBuffer)

# /home/josiah/ctypesgen_test/av/fifo.h: 50
if _libs["avcodec"].has("av_fifo_alloc_array", "cdecl"):
    av_fifo_alloc_array = _libs["avcodec"].get("av_fifo_alloc_array", "cdecl")
    av_fifo_alloc_array.argtypes = [c_size_t, c_size_t]
    av_fifo_alloc_array.restype = POINTER(AVFifoBuffer)

# /home/josiah/ctypesgen_test/av/fifo.h: 56
if _libs["avcodec"].has("av_fifo_free", "cdecl"):
    av_fifo_free = _libs["avcodec"].get("av_fifo_free", "cdecl")
    av_fifo_free.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_free.restype = None

# /home/josiah/ctypesgen_test/av/fifo.h: 62
if _libs["avcodec"].has("av_fifo_freep", "cdecl"):
    av_fifo_freep = _libs["avcodec"].get("av_fifo_freep", "cdecl")
    av_fifo_freep.argtypes = [POINTER(POINTER(AVFifoBuffer))]
    av_fifo_freep.restype = None

# /home/josiah/ctypesgen_test/av/fifo.h: 68
if _libs["avcodec"].has("av_fifo_reset", "cdecl"):
    av_fifo_reset = _libs["avcodec"].get("av_fifo_reset", "cdecl")
    av_fifo_reset.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_reset.restype = None

# /home/josiah/ctypesgen_test/av/fifo.h: 76
if _libs["avcodec"].has("av_fifo_size", "cdecl"):
    av_fifo_size = _libs["avcodec"].get("av_fifo_size", "cdecl")
    av_fifo_size.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_size.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 84
if _libs["avcodec"].has("av_fifo_space", "cdecl"):
    av_fifo_space = _libs["avcodec"].get("av_fifo_space", "cdecl")
    av_fifo_space.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_space.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 95
if _libs["avcodec"].has("av_fifo_generic_peek_at", "cdecl"):
    av_fifo_generic_peek_at = _libs["avcodec"].get("av_fifo_generic_peek_at", "cdecl")
    av_fifo_generic_peek_at.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek_at.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 105
if _libs["avcodec"].has("av_fifo_generic_peek", "cdecl"):
    av_fifo_generic_peek = _libs["avcodec"].get("av_fifo_generic_peek", "cdecl")
    av_fifo_generic_peek.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 114
if _libs["avcodec"].has("av_fifo_generic_read", "cdecl"):
    av_fifo_generic_read = _libs["avcodec"].get("av_fifo_generic_read", "cdecl")
    av_fifo_generic_read.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_read.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 129
if _libs["avcodec"].has("av_fifo_generic_write", "cdecl"):
    av_fifo_generic_write = _libs["avcodec"].get("av_fifo_generic_write", "cdecl")
    av_fifo_generic_write.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_write.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 139
if _libs["avcodec"].has("av_fifo_realloc2", "cdecl"):
    av_fifo_realloc2 = _libs["avcodec"].get("av_fifo_realloc2", "cdecl")
    av_fifo_realloc2.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_realloc2.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 150
if _libs["avcodec"].has("av_fifo_grow", "cdecl"):
    av_fifo_grow = _libs["avcodec"].get("av_fifo_grow", "cdecl")
    av_fifo_grow.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_grow.restype = c_int

# /home/josiah/ctypesgen_test/av/fifo.h: 157
if _libs["avcodec"].has("av_fifo_drain", "cdecl"):
    av_fifo_drain = _libs["avcodec"].get("av_fifo_drain", "cdecl")
    av_fifo_drain.argtypes = [POINTER(AVFifoBuffer), c_int]
    av_fifo_drain.restype = None

# /home/josiah/ctypesgen_test/av/fifo.h: 171
for _lib in _libs.values():
    try:
        ptr = (POINTER(c_uint8)).in_dll(_lib, "ptr")
        break
    except:
        pass

enum_AVSampleFormat = c_int# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_NONE = (-1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_U8 = (AV_SAMPLE_FMT_NONE + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S16 = (AV_SAMPLE_FMT_U8 + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S32 = (AV_SAMPLE_FMT_S16 + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_FLT = (AV_SAMPLE_FMT_S32 + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_DBL = (AV_SAMPLE_FMT_FLT + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_U8P = (AV_SAMPLE_FMT_DBL + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S16P = (AV_SAMPLE_FMT_U8P + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S32P = (AV_SAMPLE_FMT_S16P + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_FLTP = (AV_SAMPLE_FMT_S32P + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_DBLP = (AV_SAMPLE_FMT_FLTP + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S64 = (AV_SAMPLE_FMT_DBLP + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_S64P = (AV_SAMPLE_FMT_S64 + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

AV_SAMPLE_FMT_NB = (AV_SAMPLE_FMT_S64P + 1)# /home/josiah/ctypesgen_test/av/samplefmt.h: 58

# /home/josiah/ctypesgen_test/av/samplefmt.h: 81
if _libs["avcodec"].has("av_get_sample_fmt_name", "cdecl"):
    av_get_sample_fmt_name = _libs["avcodec"].get("av_get_sample_fmt_name", "cdecl")
    av_get_sample_fmt_name.argtypes = [enum_AVSampleFormat]
    av_get_sample_fmt_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/samplefmt.h: 87
if _libs["avcodec"].has("av_get_sample_fmt", "cdecl"):
    av_get_sample_fmt = _libs["avcodec"].get("av_get_sample_fmt", "cdecl")
    av_get_sample_fmt.argtypes = [String]
    av_get_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/samplefmt.h: 95
if _libs["avcodec"].has("av_get_alt_sample_fmt", "cdecl"):
    av_get_alt_sample_fmt = _libs["avcodec"].get("av_get_alt_sample_fmt", "cdecl")
    av_get_alt_sample_fmt.argtypes = [enum_AVSampleFormat, c_int]
    av_get_alt_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/samplefmt.h: 106
if _libs["avcodec"].has("av_get_packed_sample_fmt", "cdecl"):
    av_get_packed_sample_fmt = _libs["avcodec"].get("av_get_packed_sample_fmt", "cdecl")
    av_get_packed_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_packed_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/samplefmt.h: 117
if _libs["avcodec"].has("av_get_planar_sample_fmt", "cdecl"):
    av_get_planar_sample_fmt = _libs["avcodec"].get("av_get_planar_sample_fmt", "cdecl")
    av_get_planar_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_planar_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/samplefmt.h: 131
if _libs["avcodec"].has("av_get_sample_fmt_string", "cdecl"):
    av_get_sample_fmt_string = _libs["avcodec"].get("av_get_sample_fmt_string", "cdecl")
    av_get_sample_fmt_string.argtypes = [String, c_int, enum_AVSampleFormat]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_sample_fmt_string.restype = ReturnString
    else:
        av_get_sample_fmt_string.restype = String
        av_get_sample_fmt_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/samplefmt.h: 140
if _libs["avcodec"].has("av_get_bytes_per_sample", "cdecl"):
    av_get_bytes_per_sample = _libs["avcodec"].get("av_get_bytes_per_sample", "cdecl")
    av_get_bytes_per_sample.argtypes = [enum_AVSampleFormat]
    av_get_bytes_per_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 148
if _libs["avcodec"].has("av_sample_fmt_is_planar", "cdecl"):
    av_sample_fmt_is_planar = _libs["avcodec"].get("av_sample_fmt_is_planar", "cdecl")
    av_sample_fmt_is_planar.argtypes = [enum_AVSampleFormat]
    av_sample_fmt_is_planar.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 160
if _libs["avcodec"].has("av_samples_get_buffer_size", "cdecl"):
    av_samples_get_buffer_size = _libs["avcodec"].get("av_samples_get_buffer_size", "cdecl")
    av_samples_get_buffer_size.argtypes = [POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_get_buffer_size.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 202
if _libs["avcodec"].has("av_samples_fill_arrays", "cdecl"):
    av_samples_fill_arrays = _libs["avcodec"].get("av_samples_fill_arrays", "cdecl")
    av_samples_fill_arrays.argtypes = [POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_fill_arrays.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 226
if _libs["avcodec"].has("av_samples_alloc", "cdecl"):
    av_samples_alloc = _libs["avcodec"].get("av_samples_alloc", "cdecl")
    av_samples_alloc.argtypes = [POINTER(POINTER(c_uint8)), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 238
if _libs["avcodec"].has("av_samples_alloc_array_and_samples", "cdecl"):
    av_samples_alloc_array_and_samples = _libs["avcodec"].get("av_samples_alloc_array_and_samples", "cdecl")
    av_samples_alloc_array_and_samples.argtypes = [POINTER(POINTER(POINTER(c_uint8))), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc_array_and_samples.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 252
if _libs["avcodec"].has("av_samples_copy", "cdecl"):
    av_samples_copy = _libs["avcodec"].get("av_samples_copy", "cdecl")
    av_samples_copy.argtypes = [POINTER(POINTER(c_uint8)), POINTER(POINTER(c_uint8)), c_int, c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_copy.restype = c_int

# /home/josiah/ctypesgen_test/av/samplefmt.h: 265
if _libs["avcodec"].has("av_samples_set_silence", "cdecl"):
    av_samples_set_silence = _libs["avcodec"].get("av_samples_set_silence", "cdecl")
    av_samples_set_silence.argtypes = [POINTER(POINTER(c_uint8)), c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_set_silence.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 49
class struct_AVAudioFifo(Structure):
    pass

AVAudioFifo = struct_AVAudioFifo# /home/josiah/ctypesgen_test/av/audio_fifo.h: 49

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 56
if _libs["avcodec"].has("av_audio_fifo_free", "cdecl"):
    av_audio_fifo_free = _libs["avcodec"].get("av_audio_fifo_free", "cdecl")
    av_audio_fifo_free.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_free.restype = None

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 66
if _libs["avcodec"].has("av_audio_fifo_alloc", "cdecl"):
    av_audio_fifo_alloc = _libs["avcodec"].get("av_audio_fifo_alloc", "cdecl")
    av_audio_fifo_alloc.argtypes = [enum_AVSampleFormat, c_int, c_int]
    av_audio_fifo_alloc.restype = POINTER(AVAudioFifo)

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 77
if _libs["avcodec"].has("av_audio_fifo_realloc", "cdecl"):
    av_audio_fifo_realloc = _libs["avcodec"].get("av_audio_fifo_realloc", "cdecl")
    av_audio_fifo_realloc.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_realloc.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 95
if _libs["avcodec"].has("av_audio_fifo_write", "cdecl"):
    av_audio_fifo_write = _libs["avcodec"].get("av_audio_fifo_write", "cdecl")
    av_audio_fifo_write.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_write.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 111
if _libs["avcodec"].has("av_audio_fifo_peek", "cdecl"):
    av_audio_fifo_peek = _libs["avcodec"].get("av_audio_fifo_peek", "cdecl")
    av_audio_fifo_peek.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_peek.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 128
if _libs["avcodec"].has("av_audio_fifo_peek_at", "cdecl"):
    av_audio_fifo_peek_at = _libs["avcodec"].get("av_audio_fifo_peek_at", "cdecl")
    av_audio_fifo_peek_at.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int, c_int]
    av_audio_fifo_peek_at.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 144
if _libs["avcodec"].has("av_audio_fifo_read", "cdecl"):
    av_audio_fifo_read = _libs["avcodec"].get("av_audio_fifo_read", "cdecl")
    av_audio_fifo_read.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_read.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 155
if _libs["avcodec"].has("av_audio_fifo_drain", "cdecl"):
    av_audio_fifo_drain = _libs["avcodec"].get("av_audio_fifo_drain", "cdecl")
    av_audio_fifo_drain.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_drain.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 164
if _libs["avcodec"].has("av_audio_fifo_reset", "cdecl"):
    av_audio_fifo_reset = _libs["avcodec"].get("av_audio_fifo_reset", "cdecl")
    av_audio_fifo_reset.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_reset.restype = None

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 172
if _libs["avcodec"].has("av_audio_fifo_size", "cdecl"):
    av_audio_fifo_size = _libs["avcodec"].get("av_audio_fifo_size", "cdecl")
    av_audio_fifo_size.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_size.restype = c_int

# /home/josiah/ctypesgen_test/av/audio_fifo.h: 180
if _libs["avcodec"].has("av_audio_fifo_space", "cdecl"):
    av_audio_fifo_space = _libs["avcodec"].get("av_audio_fifo_space", "cdecl")
    av_audio_fifo_space.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_space.restype = c_int

# /home/josiah/ctypesgen_test/av/avassert.h: 73
if _libs["avcodec"].has("av_assert0_fpu", "cdecl"):
    av_assert0_fpu = _libs["avcodec"].get("av_assert0_fpu", "cdecl")
    av_assert0_fpu.argtypes = []
    av_assert0_fpu.restype = None

# /usr/include/bits/types/struct_tm.h: 7
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# /usr/include/bits/types/struct_itimerspec.h: 8
class struct_itimerspec(Structure):
    pass

struct_itimerspec.__slots__ = [
    'it_interval',
    'it_value',
]
struct_itimerspec._fields_ = [
    ('it_interval', struct_timespec),
    ('it_value', struct_timespec),
]

# /usr/include/time.h: 49
class struct_sigevent(Structure):
    pass

# /usr/include/time.h: 72
if _libs["avcodec"].has("clock", "cdecl"):
    clock = _libs["avcodec"].get("clock", "cdecl")
    clock.argtypes = []
    clock.restype = clock_t

# /usr/include/time.h: 75
if _libs["avcodec"].has("time", "cdecl"):
    time = _libs["avcodec"].get("time", "cdecl")
    time.argtypes = [POINTER(time_t)]
    time.restype = time_t

# /usr/include/time.h: 78
if _libs["avcodec"].has("difftime", "cdecl"):
    difftime = _libs["avcodec"].get("difftime", "cdecl")
    difftime.argtypes = [time_t, time_t]
    difftime.restype = c_double

# /usr/include/time.h: 82
if _libs["avcodec"].has("mktime", "cdecl"):
    mktime = _libs["avcodec"].get("mktime", "cdecl")
    mktime.argtypes = [POINTER(struct_tm)]
    mktime.restype = time_t

# /usr/include/time.h: 119
if _libs["avcodec"].has("gmtime", "cdecl"):
    gmtime = _libs["avcodec"].get("gmtime", "cdecl")
    gmtime.argtypes = [POINTER(time_t)]
    gmtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 123
if _libs["avcodec"].has("localtime", "cdecl"):
    localtime = _libs["avcodec"].get("localtime", "cdecl")
    localtime.argtypes = [POINTER(time_t)]
    localtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 139
if _libs["avcodec"].has("asctime", "cdecl"):
    asctime = _libs["avcodec"].get("asctime", "cdecl")
    asctime.argtypes = [POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime.restype = ReturnString
    else:
        asctime.restype = String
        asctime.errcheck = ReturnString

# /usr/include/time.h: 142
if _libs["avcodec"].has("ctime", "cdecl"):
    ctime = _libs["avcodec"].get("ctime", "cdecl")
    ctime.argtypes = [POINTER(time_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime.restype = ReturnString
    else:
        ctime.restype = String
        ctime.errcheck = ReturnString

# /usr/include/time.h: 159
try:
    __tzname = (POINTER(c_char) * int(2)).in_dll(_libs["avcodec"], "__tzname")
except:
    pass

# /usr/include/time.h: 160
try:
    __daylight = (c_int).in_dll(_libs["avcodec"], "__daylight")
except:
    pass

# /usr/include/time.h: 161
try:
    __timezone = (c_long).in_dll(_libs["avcodec"], "__timezone")
except:
    pass

# /usr/include/time.h: 166
try:
    tzname = (POINTER(c_char) * int(2)).in_dll(_libs["avcodec"], "tzname")
except:
    pass

# /usr/include/time.h: 170
if _libs["avcodec"].has("tzset", "cdecl"):
    tzset = _libs["avcodec"].get("tzset", "cdecl")
    tzset.argtypes = []
    tzset.restype = None

# /usr/include/time.h: 174
try:
    daylight = (c_int).in_dll(_libs["avcodec"], "daylight")
except:
    pass

# /usr/include/time.h: 175
try:
    timezone = (c_long).in_dll(_libs["avcodec"], "timezone")
except:
    pass

# /usr/include/time.h: 190
if _libs["avcodec"].has("timegm", "cdecl"):
    timegm = _libs["avcodec"].get("timegm", "cdecl")
    timegm.argtypes = [POINTER(struct_tm)]
    timegm.restype = time_t

# /usr/include/time.h: 193
if _libs["avcodec"].has("timelocal", "cdecl"):
    timelocal = _libs["avcodec"].get("timelocal", "cdecl")
    timelocal.argtypes = [POINTER(struct_tm)]
    timelocal.restype = time_t

# /usr/include/time.h: 196
if _libs["avcodec"].has("dysize", "cdecl"):
    dysize = _libs["avcodec"].get("dysize", "cdecl")
    dysize.argtypes = [c_int]
    dysize.restype = c_int

# /usr/include/time.h: 205
if _libs["avcodec"].has("nanosleep", "cdecl"):
    nanosleep = _libs["avcodec"].get("nanosleep", "cdecl")
    nanosleep.argtypes = [POINTER(struct_timespec), POINTER(struct_timespec)]
    nanosleep.restype = c_int

# /usr/include/time.h: 210
if _libs["avcodec"].has("clock_getres", "cdecl"):
    clock_getres = _libs["avcodec"].get("clock_getres", "cdecl")
    clock_getres.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_getres.restype = c_int

# /usr/include/time.h: 213
if _libs["avcodec"].has("clock_gettime", "cdecl"):
    clock_gettime = _libs["avcodec"].get("clock_gettime", "cdecl")
    clock_gettime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_gettime.restype = c_int

# /usr/include/time.h: 216
if _libs["avcodec"].has("clock_settime", "cdecl"):
    clock_settime = _libs["avcodec"].get("clock_settime", "cdecl")
    clock_settime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_settime.restype = c_int

# /usr/include/time.h: 224
if _libs["avcodec"].has("clock_nanosleep", "cdecl"):
    clock_nanosleep = _libs["avcodec"].get("clock_nanosleep", "cdecl")
    clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(struct_timespec), POINTER(struct_timespec)]
    clock_nanosleep.restype = c_int

# /usr/include/time.h: 229
if _libs["avcodec"].has("clock_getcpuclockid", "cdecl"):
    clock_getcpuclockid = _libs["avcodec"].get("clock_getcpuclockid", "cdecl")
    clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
    clock_getcpuclockid.restype = c_int

# /usr/include/time.h: 239
if _libs["avcodec"].has("timer_delete", "cdecl"):
    timer_delete = _libs["avcodec"].get("timer_delete", "cdecl")
    timer_delete.argtypes = [timer_t]
    timer_delete.restype = c_int

# /usr/include/time.h: 247
if _libs["avcodec"].has("timer_gettime", "cdecl"):
    timer_gettime = _libs["avcodec"].get("timer_gettime", "cdecl")
    timer_gettime.argtypes = [timer_t, POINTER(struct_itimerspec)]
    timer_gettime.restype = c_int

# /usr/include/time.h: 251
if _libs["avcodec"].has("timer_getoverrun", "cdecl"):
    timer_getoverrun = _libs["avcodec"].get("timer_getoverrun", "cdecl")
    timer_getoverrun.argtypes = [timer_t]
    timer_getoverrun.restype = c_int

# /usr/include/time.h: 257
if _libs["avcodec"].has("timespec_get", "cdecl"):
    timespec_get = _libs["avcodec"].get("timespec_get", "cdecl")
    timespec_get.argtypes = [POINTER(struct_timespec), c_int]
    timespec_get.restype = c_int

byte_t = u_int8_t# /usr/include/libraw1394/raw1394.h: 45

quadlet_t = u_int32_t# /usr/include/libraw1394/raw1394.h: 46

octlet_t = u_int64_t# /usr/include/libraw1394/raw1394.h: 47

nodeid_t = u_int16_t# /usr/include/libraw1394/raw1394.h: 49

# /usr/include/libraw1394/raw1394.h: 54
class struct_raw1394_handle(Structure):
    pass

raw1394handle_t = POINTER(struct_raw1394_handle)# /usr/include/libraw1394/raw1394.h: 54

enum_avc1394_measurement_unit = c_int# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_VIDEO_FRAME = 0# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_VIDEO_SCENE = (AVC1394_VCR_MEASUREMENT_VIDEO_FRAME + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_VISS = (AVC1394_VCR_MEASUREMENT_VIDEO_SCENE + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_GOP = (AVC1394_VCR_MEASUREMENT_VISS + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_INDEX = (AVC1394_VCR_MEASUREMENT_GOP + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_SKIP = (AVC1394_VCR_MEASUREMENT_INDEX + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

AVC1394_VCR_MEASUREMENT_PHOTO = (AVC1394_VCR_MEASUREMENT_SKIP + 1)# /home/josiah/ctypesgen_test/av/avc1394.h: 429

# /home/josiah/ctypesgen_test/av/avc1394.h: 444
if _libs["avdevice"].has("avc1394_send_command", "cdecl"):
    avc1394_send_command = _libs["avdevice"].get("avc1394_send_command", "cdecl")
    avc1394_send_command.argtypes = [raw1394handle_t, nodeid_t, quadlet_t]
    avc1394_send_command.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 447
if _libs["avdevice"].has("avc1394_send_command_block", "cdecl"):
    avc1394_send_command_block = _libs["avdevice"].get("avc1394_send_command_block", "cdecl")
    avc1394_send_command_block.argtypes = [raw1394handle_t, nodeid_t, POINTER(quadlet_t), c_int]
    avc1394_send_command_block.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 451
if _libs["avdevice"].has("avc1394_transaction", "cdecl"):
    avc1394_transaction = _libs["avdevice"].get("avc1394_transaction", "cdecl")
    avc1394_transaction.argtypes = [raw1394handle_t, nodeid_t, quadlet_t, c_int]
    avc1394_transaction.restype = quadlet_t

# /home/josiah/ctypesgen_test/av/avc1394.h: 454
if _libs["avdevice"].has("avc1394_transaction_block2", "cdecl"):
    avc1394_transaction_block2 = _libs["avdevice"].get("avc1394_transaction_block2", "cdecl")
    avc1394_transaction_block2.argtypes = [raw1394handle_t, nodeid_t, POINTER(quadlet_t), c_int, POINTER(c_uint), c_int]
    avc1394_transaction_block2.restype = POINTER(quadlet_t)

# /home/josiah/ctypesgen_test/av/avc1394.h: 458
if _libs["avdevice"].has("avc1394_transaction_block", "cdecl"):
    avc1394_transaction_block = _libs["avdevice"].get("avc1394_transaction_block", "cdecl")
    avc1394_transaction_block.argtypes = [raw1394handle_t, nodeid_t, POINTER(quadlet_t), c_int, c_int]
    avc1394_transaction_block.restype = POINTER(quadlet_t)

# /home/josiah/ctypesgen_test/av/avc1394.h: 463
if _libs["avdevice"].has("avc1394_transaction_block_close", "cdecl"):
    avc1394_transaction_block_close = _libs["avdevice"].get("avc1394_transaction_block_close", "cdecl")
    avc1394_transaction_block_close.argtypes = [raw1394handle_t]
    avc1394_transaction_block_close.restype = None

# /home/josiah/ctypesgen_test/av/avc1394.h: 466
if _libs["avdevice"].has("avc1394_open_descriptor", "cdecl"):
    avc1394_open_descriptor = _libs["avdevice"].get("avc1394_open_descriptor", "cdecl")
    avc1394_open_descriptor.argtypes = [raw1394handle_t, nodeid_t, quadlet_t, quadlet_t, POINTER(c_ubyte), c_int, c_ubyte]
    avc1394_open_descriptor.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 472
if _libs["avdevice"].has("avc1394_close_descriptor", "cdecl"):
    avc1394_close_descriptor = _libs["avdevice"].get("avc1394_close_descriptor", "cdecl")
    avc1394_close_descriptor.argtypes = [raw1394handle_t, nodeid_t, quadlet_t, quadlet_t, POINTER(c_ubyte), c_int]
    avc1394_close_descriptor.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 477
if _libs["avdevice"].has("avc1394_subunit_info", "cdecl"):
    avc1394_subunit_info = _libs["avdevice"].get("avc1394_subunit_info", "cdecl")
    avc1394_subunit_info.argtypes = [raw1394handle_t, nodeid_t, POINTER(quadlet_t)]
    avc1394_subunit_info.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 482
if _libs["avdevice"].has("avc1394_check_subunit_type", "cdecl"):
    avc1394_check_subunit_type = _libs["avdevice"].get("avc1394_check_subunit_type", "cdecl")
    avc1394_check_subunit_type.argtypes = [raw1394handle_t, nodeid_t, c_int]
    avc1394_check_subunit_type.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 484
if _libs["avdevice"].has("avc1394_unit_info", "cdecl"):
    avc1394_unit_info = _libs["avdevice"].get("avc1394_unit_info", "cdecl")
    avc1394_unit_info.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_unit_info.restype = POINTER(quadlet_t)

# /home/josiah/ctypesgen_test/av/avc1394.h: 491
class struct_avc1394_command_response(Structure):
    pass

struct_avc1394_command_response.__slots__ = [
    'status',
    'reserved',
    'subunit_id',
    'subunit_type',
    'opcode',
    'operand',
]
struct_avc1394_command_response._fields_ = [
    ('status', byte_t, 4),
    ('reserved', byte_t, 4),
    ('subunit_id', byte_t, 3),
    ('subunit_type', byte_t, 5),
    ('opcode', byte_t, 8),
    ('operand', byte_t * int(9)),
]

avc1394_cmd_rsp = struct_avc1394_command_response# /home/josiah/ctypesgen_test/av/avc1394.h: 499

avc1394_command_handler_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_avc1394_command_response))# /home/josiah/ctypesgen_test/av/avc1394.h: 502

# /home/josiah/ctypesgen_test/av/avc1394.h: 506
if _libs["avdevice"].has("avc1394_init_target", "cdecl"):
    avc1394_init_target = _libs["avdevice"].get("avc1394_init_target", "cdecl")
    avc1394_init_target.argtypes = [raw1394handle_t, avc1394_command_handler_t]
    avc1394_init_target.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394.h: 509
if _libs["avdevice"].has("avc1394_close_target", "cdecl"):
    avc1394_close_target = _libs["avdevice"].get("avc1394_close_target", "cdecl")
    avc1394_close_target.argtypes = [raw1394handle_t]
    avc1394_close_target.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 33
if _libs["avdevice"].has("avc1394_vcr_is_playing", "cdecl"):
    avc1394_vcr_is_playing = _libs["avdevice"].get("avc1394_vcr_is_playing", "cdecl")
    avc1394_vcr_is_playing.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_is_playing.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 37
if _libs["avdevice"].has("avc1394_vcr_is_recording", "cdecl"):
    avc1394_vcr_is_recording = _libs["avdevice"].get("avc1394_vcr_is_recording", "cdecl")
    avc1394_vcr_is_recording.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_is_recording.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 42
if _libs["avdevice"].has("avc1394_vcr_play", "cdecl"):
    avc1394_vcr_play = _libs["avdevice"].get("avc1394_vcr_play", "cdecl")
    avc1394_vcr_play.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_play.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 47
if _libs["avdevice"].has("avc1394_vcr_reverse", "cdecl"):
    avc1394_vcr_reverse = _libs["avdevice"].get("avc1394_vcr_reverse", "cdecl")
    avc1394_vcr_reverse.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_reverse.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 52
if _libs["avdevice"].has("avc1394_vcr_trick_play", "cdecl"):
    avc1394_vcr_trick_play = _libs["avdevice"].get("avc1394_vcr_trick_play", "cdecl")
    avc1394_vcr_trick_play.argtypes = [raw1394handle_t, nodeid_t, c_int]
    avc1394_vcr_trick_play.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 56
if _libs["avdevice"].has("avc1394_vcr_stop", "cdecl"):
    avc1394_vcr_stop = _libs["avdevice"].get("avc1394_vcr_stop", "cdecl")
    avc1394_vcr_stop.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_stop.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 60
if _libs["avdevice"].has("avc1394_vcr_rewind", "cdecl"):
    avc1394_vcr_rewind = _libs["avdevice"].get("avc1394_vcr_rewind", "cdecl")
    avc1394_vcr_rewind.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_rewind.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 64
if _libs["avdevice"].has("avc1394_vcr_pause", "cdecl"):
    avc1394_vcr_pause = _libs["avdevice"].get("avc1394_vcr_pause", "cdecl")
    avc1394_vcr_pause.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_pause.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 68
if _libs["avdevice"].has("avc1394_vcr_forward", "cdecl"):
    avc1394_vcr_forward = _libs["avdevice"].get("avc1394_vcr_forward", "cdecl")
    avc1394_vcr_forward.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_forward.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 72
if _libs["avdevice"].has("avc1394_vcr_next", "cdecl"):
    avc1394_vcr_next = _libs["avdevice"].get("avc1394_vcr_next", "cdecl")
    avc1394_vcr_next.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_next.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 76
if _libs["avdevice"].has("avc1394_vcr_next_index", "cdecl"):
    avc1394_vcr_next_index = _libs["avdevice"].get("avc1394_vcr_next_index", "cdecl")
    avc1394_vcr_next_index.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_next_index.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 80
if _libs["avdevice"].has("avc1394_vcr_previous", "cdecl"):
    avc1394_vcr_previous = _libs["avdevice"].get("avc1394_vcr_previous", "cdecl")
    avc1394_vcr_previous.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_previous.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 84
if _libs["avdevice"].has("avc1394_vcr_previous_index", "cdecl"):
    avc1394_vcr_previous_index = _libs["avdevice"].get("avc1394_vcr_previous_index", "cdecl")
    avc1394_vcr_previous_index.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_previous_index.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 88
if _libs["avdevice"].has("avc1394_vcr_eject", "cdecl"):
    avc1394_vcr_eject = _libs["avdevice"].get("avc1394_vcr_eject", "cdecl")
    avc1394_vcr_eject.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_eject.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 92
if _libs["avdevice"].has("avc1394_vcr_record", "cdecl"):
    avc1394_vcr_record = _libs["avdevice"].get("avc1394_vcr_record", "cdecl")
    avc1394_vcr_record.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_record.restype = None

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 96
if _libs["avdevice"].has("avc1394_vcr_status", "cdecl"):
    avc1394_vcr_status = _libs["avdevice"].get("avc1394_vcr_status", "cdecl")
    avc1394_vcr_status.argtypes = [raw1394handle_t, nodeid_t]
    avc1394_vcr_status.restype = quadlet_t

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 99
if _libs["avdevice"].has("avc1394_vcr_decode_status", "cdecl"):
    avc1394_vcr_decode_status = _libs["avdevice"].get("avc1394_vcr_decode_status", "cdecl")
    avc1394_vcr_decode_status.argtypes = [quadlet_t]
    if sizeof(c_int) == sizeof(c_void_p):
        avc1394_vcr_decode_status.restype = ReturnString
    else:
        avc1394_vcr_decode_status.restype = String
        avc1394_vcr_decode_status.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 105
if _libs["avdevice"].has("avc1394_vcr_get_timecode", "cdecl"):
    avc1394_vcr_get_timecode = _libs["avdevice"].get("avc1394_vcr_get_timecode", "cdecl")
    avc1394_vcr_get_timecode.argtypes = [raw1394handle_t, nodeid_t]
    if sizeof(c_int) == sizeof(c_void_p):
        avc1394_vcr_get_timecode.restype = ReturnString
    else:
        avc1394_vcr_get_timecode.restype = String
        avc1394_vcr_get_timecode.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 111
if _libs["avdevice"].has("avc1394_vcr_get_timecode2", "cdecl"):
    avc1394_vcr_get_timecode2 = _libs["avdevice"].get("avc1394_vcr_get_timecode2", "cdecl")
    avc1394_vcr_get_timecode2.argtypes = [raw1394handle_t, nodeid_t, String]
    avc1394_vcr_get_timecode2.restype = c_int

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 115
if _libs["avdevice"].has("avc1394_vcr_seek_timecode", "cdecl"):
    avc1394_vcr_seek_timecode = _libs["avdevice"].get("avc1394_vcr_seek_timecode", "cdecl")
    avc1394_vcr_seek_timecode.argtypes = [raw1394handle_t, nodeid_t, String]
    avc1394_vcr_seek_timecode.restype = None

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
if _libs["avcodec"].has("av_buffer_alloc", "cdecl"):
    av_buffer_alloc = _libs["avcodec"].get("av_buffer_alloc", "cdecl")
    av_buffer_alloc.argtypes = [c_int]
    av_buffer_alloc.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 119
if _libs["avcodec"].has("av_buffer_allocz", "cdecl"):
    av_buffer_allocz = _libs["avcodec"].get("av_buffer_allocz", "cdecl")
    av_buffer_allocz.argtypes = [c_int]
    av_buffer_allocz.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 146
if _libs["avcodec"].has("av_buffer_create", "cdecl"):
    av_buffer_create = _libs["avcodec"].get("av_buffer_create", "cdecl")
    av_buffer_create.argtypes = [POINTER(c_uint8), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(c_uint8)), POINTER(None), c_int]
    av_buffer_create.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 158
if _libs["avcodec"].has("av_buffer_default_free", "cdecl"):
    av_buffer_default_free = _libs["avcodec"].get("av_buffer_default_free", "cdecl")
    av_buffer_default_free.argtypes = [POINTER(None), POINTER(c_uint8)]
    av_buffer_default_free.restype = None

# /usr/include/libavutil/buffer.h: 166
if _libs["avcodec"].has("av_buffer_ref", "cdecl"):
    av_buffer_ref = _libs["avcodec"].get("av_buffer_ref", "cdecl")
    av_buffer_ref.argtypes = [POINTER(AVBufferRef)]
    av_buffer_ref.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 174
if _libs["avcodec"].has("av_buffer_unref", "cdecl"):
    av_buffer_unref = _libs["avcodec"].get("av_buffer_unref", "cdecl")
    av_buffer_unref.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_unref.restype = None

# /usr/include/libavutil/buffer.h: 182
if _libs["avcodec"].has("av_buffer_is_writable", "cdecl"):
    av_buffer_is_writable = _libs["avcodec"].get("av_buffer_is_writable", "cdecl")
    av_buffer_is_writable.argtypes = [POINTER(AVBufferRef)]
    av_buffer_is_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 187
if _libs["avcodec"].has("av_buffer_get_opaque", "cdecl"):
    av_buffer_get_opaque = _libs["avcodec"].get("av_buffer_get_opaque", "cdecl")
    av_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/buffer.h: 189
if _libs["avcodec"].has("av_buffer_get_ref_count", "cdecl"):
    av_buffer_get_ref_count = _libs["avcodec"].get("av_buffer_get_ref_count", "cdecl")
    av_buffer_get_ref_count.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_ref_count.restype = c_int

# /usr/include/libavutil/buffer.h: 200
if _libs["avcodec"].has("av_buffer_make_writable", "cdecl"):
    av_buffer_make_writable = _libs["avcodec"].get("av_buffer_make_writable", "cdecl")
    av_buffer_make_writable.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_make_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 218
if _libs["avcodec"].has("av_buffer_realloc", "cdecl"):
    av_buffer_realloc = _libs["avcodec"].get("av_buffer_realloc", "cdecl")
    av_buffer_realloc.argtypes = [POINTER(POINTER(AVBufferRef)), c_int]
    av_buffer_realloc.restype = c_int

# /usr/include/libavutil/buffer.h: 237
if _libs["avcodec"].has("av_buffer_replace", "cdecl"):
    av_buffer_replace = _libs["avcodec"].get("av_buffer_replace", "cdecl")
    av_buffer_replace.argtypes = [POINTER(POINTER(AVBufferRef)), POINTER(AVBufferRef)]
    av_buffer_replace.restype = c_int

# /usr/include/libavutil/buffer.h: 277
class struct_AVBufferPool(Structure):
    pass

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 277

# /usr/include/libavutil/buffer.h: 289
if _libs["avcodec"].has("av_buffer_pool_init", "cdecl"):
    av_buffer_pool_init = _libs["avcodec"].get("av_buffer_pool_init", "cdecl")
    av_buffer_pool_init.argtypes = [c_int, CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), c_int)]
    av_buffer_pool_init.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 310
if _libs["avcodec"].has("av_buffer_pool_init2", "cdecl"):
    av_buffer_pool_init2 = _libs["avcodec"].get("av_buffer_pool_init2", "cdecl")
    av_buffer_pool_init2.argtypes = [c_int, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), POINTER(None), c_int), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    av_buffer_pool_init2.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 326
if _libs["avcodec"].has("av_buffer_pool_uninit", "cdecl"):
    av_buffer_pool_uninit = _libs["avcodec"].get("av_buffer_pool_uninit", "cdecl")
    av_buffer_pool_uninit.argtypes = [POINTER(POINTER(AVBufferPool))]
    av_buffer_pool_uninit.restype = None

# /usr/include/libavutil/buffer.h: 334
if _libs["avcodec"].has("av_buffer_pool_get", "cdecl"):
    av_buffer_pool_get = _libs["avcodec"].get("av_buffer_pool_get", "cdecl")
    av_buffer_pool_get.argtypes = [POINTER(AVBufferPool)]
    av_buffer_pool_get.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 347
if _libs["avcodec"].has("av_buffer_pool_buffer_get_opaque", "cdecl"):
    av_buffer_pool_buffer_get_opaque = _libs["avcodec"].get("av_buffer_pool_buffer_get_opaque", "cdecl")
    av_buffer_pool_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_pool_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_pool_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/cpu.h: 83
if _libs["avcodec"].has("av_get_cpu_flags", "cdecl"):
    av_get_cpu_flags = _libs["avcodec"].get("av_get_cpu_flags", "cdecl")
    av_get_cpu_flags.argtypes = []
    av_get_cpu_flags.restype = c_int

# /usr/include/libavutil/cpu.h: 89
if _libs["avcodec"].has("av_force_cpu_flags", "cdecl"):
    av_force_cpu_flags = _libs["avcodec"].get("av_force_cpu_flags", "cdecl")
    av_force_cpu_flags.argtypes = [c_int]
    av_force_cpu_flags.restype = None

# /usr/include/libavutil/cpu.h: 96
if _libs["avcodec"].has("av_set_cpu_flags_mask", "cdecl"):
    av_set_cpu_flags_mask = _libs["avcodec"].get("av_set_cpu_flags_mask", "cdecl")
    av_set_cpu_flags_mask.argtypes = [c_int]
    av_set_cpu_flags_mask.restype = None

# /usr/include/libavutil/cpu.h: 108
if _libs["avcodec"].has("av_parse_cpu_flags", "cdecl"):
    av_parse_cpu_flags = _libs["avcodec"].get("av_parse_cpu_flags", "cdecl")
    av_parse_cpu_flags.argtypes = [String]
    av_parse_cpu_flags.restype = c_int

# /usr/include/libavutil/cpu.h: 115
if _libs["avcodec"].has("av_parse_cpu_caps", "cdecl"):
    av_parse_cpu_caps = _libs["avcodec"].get("av_parse_cpu_caps", "cdecl")
    av_parse_cpu_caps.argtypes = [POINTER(c_uint), String]
    av_parse_cpu_caps.restype = c_int

# /usr/include/libavutil/cpu.h: 120
if _libs["avcodec"].has("av_cpu_count", "cdecl"):
    av_cpu_count = _libs["avcodec"].get("av_cpu_count", "cdecl")
    av_cpu_count.argtypes = []
    av_cpu_count.restype = c_int

# /usr/include/libavutil/cpu.h: 131
if _libs["avcodec"].has("av_cpu_max_align", "cdecl"):
    av_cpu_max_align = _libs["avcodec"].get("av_cpu_max_align", "cdecl")
    av_cpu_max_align.argtypes = []
    av_cpu_max_align.restype = c_size_t

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
if _libs["avcodec"].has("av_get_channel_layout", "cdecl"):
    av_get_channel_layout = _libs["avcodec"].get("av_get_channel_layout", "cdecl")
    av_get_channel_layout.argtypes = [String]
    av_get_channel_layout.restype = c_uint64

# /usr/include/libavutil/channel_layout.h: 162
if _libs["avcodec"].has("av_get_extended_channel_layout", "cdecl"):
    av_get_extended_channel_layout = _libs["avcodec"].get("av_get_extended_channel_layout", "cdecl")
    av_get_extended_channel_layout.argtypes = [String, POINTER(c_uint64), POINTER(c_int)]
    av_get_extended_channel_layout.restype = c_int

# /usr/include/libavutil/channel_layout.h: 171
if _libs["avcodec"].has("av_get_channel_layout_string", "cdecl"):
    av_get_channel_layout_string = _libs["avcodec"].get("av_get_channel_layout_string", "cdecl")
    av_get_channel_layout_string.argtypes = [String, c_int, c_int, c_uint64]
    av_get_channel_layout_string.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 82
class struct_AVBPrint(Structure):
    pass

# /usr/include/libavutil/channel_layout.h: 177
if _libs["avcodec"].has("av_bprint_channel_layout", "cdecl"):
    av_bprint_channel_layout = _libs["avcodec"].get("av_bprint_channel_layout", "cdecl")
    av_bprint_channel_layout.argtypes = [POINTER(struct_AVBPrint), c_int, c_uint64]
    av_bprint_channel_layout.restype = None

# /usr/include/libavutil/channel_layout.h: 182
if _libs["avcodec"].has("av_get_channel_layout_nb_channels", "cdecl"):
    av_get_channel_layout_nb_channels = _libs["avcodec"].get("av_get_channel_layout_nb_channels", "cdecl")
    av_get_channel_layout_nb_channels.argtypes = [c_uint64]
    av_get_channel_layout_nb_channels.restype = c_int

# /usr/include/libavutil/channel_layout.h: 187
if _libs["avcodec"].has("av_get_default_channel_layout", "cdecl"):
    av_get_default_channel_layout = _libs["avcodec"].get("av_get_default_channel_layout", "cdecl")
    av_get_default_channel_layout.argtypes = [c_int]
    av_get_default_channel_layout.restype = c_int64

# /usr/include/libavutil/channel_layout.h: 198
if _libs["avcodec"].has("av_get_channel_layout_channel_index", "cdecl"):
    av_get_channel_layout_channel_index = _libs["avcodec"].get("av_get_channel_layout_channel_index", "cdecl")
    av_get_channel_layout_channel_index.argtypes = [c_uint64, c_uint64]
    av_get_channel_layout_channel_index.restype = c_int

# /usr/include/libavutil/channel_layout.h: 204
if _libs["avcodec"].has("av_channel_layout_extract_channel", "cdecl"):
    av_channel_layout_extract_channel = _libs["avcodec"].get("av_channel_layout_extract_channel", "cdecl")
    av_channel_layout_extract_channel.argtypes = [c_uint64, c_int]
    av_channel_layout_extract_channel.restype = c_uint64

# /usr/include/libavutil/channel_layout.h: 211
if _libs["avcodec"].has("av_get_channel_name", "cdecl"):
    av_get_channel_name = _libs["avcodec"].get("av_get_channel_name", "cdecl")
    av_get_channel_name.argtypes = [c_uint64]
    av_get_channel_name.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 219
if _libs["avcodec"].has("av_get_channel_description", "cdecl"):
    av_get_channel_description = _libs["avcodec"].get("av_get_channel_description", "cdecl")
    av_get_channel_description.argtypes = [c_uint64]
    av_get_channel_description.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 230
if _libs["avcodec"].has("av_get_standard_channel_layout", "cdecl"):
    av_get_standard_channel_layout = _libs["avcodec"].get("av_get_standard_channel_layout", "cdecl")
    av_get_standard_channel_layout.argtypes = [c_uint, POINTER(c_uint64), POINTER(POINTER(c_char))]
    av_get_standard_channel_layout.restype = c_int

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
if _libs["avcodec"].has("av_dict_get", "cdecl"):
    av_dict_get = _libs["avcodec"].get("av_dict_get", "cdecl")
    av_dict_get.argtypes = [POINTER(AVDictionary), String, POINTER(AVDictionaryEntry), c_int]
    av_dict_get.restype = POINTER(AVDictionaryEntry)

# /usr/include/libavutil/dict.h: 112
if _libs["avcodec"].has("av_dict_count", "cdecl"):
    av_dict_count = _libs["avcodec"].get("av_dict_count", "cdecl")
    av_dict_count.argtypes = [POINTER(AVDictionary)]
    av_dict_count.restype = c_int

# /usr/include/libavutil/dict.h: 130
if _libs["avcodec"].has("av_dict_set", "cdecl"):
    av_dict_set = _libs["avcodec"].get("av_dict_set", "cdecl")
    av_dict_set.argtypes = [POINTER(POINTER(AVDictionary)), String, String, c_int]
    av_dict_set.restype = c_int

# /usr/include/libavutil/dict.h: 138
if _libs["avcodec"].has("av_dict_set_int", "cdecl"):
    av_dict_set_int = _libs["avcodec"].get("av_dict_set_int", "cdecl")
    av_dict_set_int.argtypes = [POINTER(POINTER(AVDictionary)), String, c_int64, c_int]
    av_dict_set_int.restype = c_int

# /usr/include/libavutil/dict.h: 156
if _libs["avcodec"].has("av_dict_parse_string", "cdecl"):
    av_dict_parse_string = _libs["avcodec"].get("av_dict_parse_string", "cdecl")
    av_dict_parse_string.argtypes = [POINTER(POINTER(AVDictionary)), String, String, String, c_int]
    av_dict_parse_string.restype = c_int

# /usr/include/libavutil/dict.h: 170
if _libs["avcodec"].has("av_dict_copy", "cdecl"):
    av_dict_copy = _libs["avcodec"].get("av_dict_copy", "cdecl")
    av_dict_copy.argtypes = [POINTER(POINTER(AVDictionary)), POINTER(AVDictionary), c_int]
    av_dict_copy.restype = c_int

# /usr/include/libavutil/dict.h: 176
if _libs["avcodec"].has("av_dict_free", "cdecl"):
    av_dict_free = _libs["avcodec"].get("av_dict_free", "cdecl")
    av_dict_free.argtypes = [POINTER(POINTER(AVDictionary))]
    av_dict_free.restype = None

# /usr/include/libavutil/dict.h: 193
if _libs["avcodec"].has("av_dict_get_string", "cdecl"):
    av_dict_get_string = _libs["avcodec"].get("av_dict_get_string", "cdecl")
    av_dict_get_string.argtypes = [POINTER(AVDictionary), POINTER(POINTER(c_char)), c_char, c_char]
    av_dict_get_string.restype = c_int

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
if _libs["avcodec"].has("av_frame_get_best_effort_timestamp", "cdecl"):
    av_frame_get_best_effort_timestamp = _libs["avcodec"].get("av_frame_get_best_effort_timestamp", "cdecl")
    av_frame_get_best_effort_timestamp.argtypes = [POINTER(AVFrame)]
    av_frame_get_best_effort_timestamp.restype = c_int64

# /usr/include/libavutil/frame.h: 708
if _libs["avcodec"].has("av_frame_set_best_effort_timestamp", "cdecl"):
    av_frame_set_best_effort_timestamp = _libs["avcodec"].get("av_frame_set_best_effort_timestamp", "cdecl")
    av_frame_set_best_effort_timestamp.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_best_effort_timestamp.restype = None

# /usr/include/libavutil/frame.h: 710
if _libs["avcodec"].has("av_frame_get_pkt_duration", "cdecl"):
    av_frame_get_pkt_duration = _libs["avcodec"].get("av_frame_get_pkt_duration", "cdecl")
    av_frame_get_pkt_duration.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_duration.restype = c_int64

# /usr/include/libavutil/frame.h: 712
if _libs["avcodec"].has("av_frame_set_pkt_duration", "cdecl"):
    av_frame_set_pkt_duration = _libs["avcodec"].get("av_frame_set_pkt_duration", "cdecl")
    av_frame_set_pkt_duration.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_pkt_duration.restype = None

# /usr/include/libavutil/frame.h: 714
if _libs["avcodec"].has("av_frame_get_pkt_pos", "cdecl"):
    av_frame_get_pkt_pos = _libs["avcodec"].get("av_frame_get_pkt_pos", "cdecl")
    av_frame_get_pkt_pos.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_pos.restype = c_int64

# /usr/include/libavutil/frame.h: 716
if _libs["avcodec"].has("av_frame_set_pkt_pos", "cdecl"):
    av_frame_set_pkt_pos = _libs["avcodec"].get("av_frame_set_pkt_pos", "cdecl")
    av_frame_set_pkt_pos.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_pkt_pos.restype = None

# /usr/include/libavutil/frame.h: 718
if _libs["avcodec"].has("av_frame_get_channel_layout", "cdecl"):
    av_frame_get_channel_layout = _libs["avcodec"].get("av_frame_get_channel_layout", "cdecl")
    av_frame_get_channel_layout.argtypes = [POINTER(AVFrame)]
    av_frame_get_channel_layout.restype = c_int64

# /usr/include/libavutil/frame.h: 720
if _libs["avcodec"].has("av_frame_set_channel_layout", "cdecl"):
    av_frame_set_channel_layout = _libs["avcodec"].get("av_frame_set_channel_layout", "cdecl")
    av_frame_set_channel_layout.argtypes = [POINTER(AVFrame), c_int64]
    av_frame_set_channel_layout.restype = None

# /usr/include/libavutil/frame.h: 722
if _libs["avcodec"].has("av_frame_get_channels", "cdecl"):
    av_frame_get_channels = _libs["avcodec"].get("av_frame_get_channels", "cdecl")
    av_frame_get_channels.argtypes = [POINTER(AVFrame)]
    av_frame_get_channels.restype = c_int

# /usr/include/libavutil/frame.h: 724
if _libs["avcodec"].has("av_frame_set_channels", "cdecl"):
    av_frame_set_channels = _libs["avcodec"].get("av_frame_set_channels", "cdecl")
    av_frame_set_channels.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_channels.restype = None

# /usr/include/libavutil/frame.h: 726
if _libs["avcodec"].has("av_frame_get_sample_rate", "cdecl"):
    av_frame_get_sample_rate = _libs["avcodec"].get("av_frame_get_sample_rate", "cdecl")
    av_frame_get_sample_rate.argtypes = [POINTER(AVFrame)]
    av_frame_get_sample_rate.restype = c_int

# /usr/include/libavutil/frame.h: 728
if _libs["avcodec"].has("av_frame_set_sample_rate", "cdecl"):
    av_frame_set_sample_rate = _libs["avcodec"].get("av_frame_set_sample_rate", "cdecl")
    av_frame_set_sample_rate.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_sample_rate.restype = None

# /usr/include/libavutil/frame.h: 730
if _libs["avcodec"].has("av_frame_get_metadata", "cdecl"):
    av_frame_get_metadata = _libs["avcodec"].get("av_frame_get_metadata", "cdecl")
    av_frame_get_metadata.argtypes = [POINTER(AVFrame)]
    av_frame_get_metadata.restype = POINTER(AVDictionary)

# /usr/include/libavutil/frame.h: 732
if _libs["avcodec"].has("av_frame_set_metadata", "cdecl"):
    av_frame_set_metadata = _libs["avcodec"].get("av_frame_set_metadata", "cdecl")
    av_frame_set_metadata.argtypes = [POINTER(AVFrame), POINTER(AVDictionary)]
    av_frame_set_metadata.restype = None

# /usr/include/libavutil/frame.h: 734
if _libs["avcodec"].has("av_frame_get_decode_error_flags", "cdecl"):
    av_frame_get_decode_error_flags = _libs["avcodec"].get("av_frame_get_decode_error_flags", "cdecl")
    av_frame_get_decode_error_flags.argtypes = [POINTER(AVFrame)]
    av_frame_get_decode_error_flags.restype = c_int

# /usr/include/libavutil/frame.h: 736
if _libs["avcodec"].has("av_frame_set_decode_error_flags", "cdecl"):
    av_frame_set_decode_error_flags = _libs["avcodec"].get("av_frame_set_decode_error_flags", "cdecl")
    av_frame_set_decode_error_flags.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_decode_error_flags.restype = None

# /usr/include/libavutil/frame.h: 738
if _libs["avcodec"].has("av_frame_get_pkt_size", "cdecl"):
    av_frame_get_pkt_size = _libs["avcodec"].get("av_frame_get_pkt_size", "cdecl")
    av_frame_get_pkt_size.argtypes = [POINTER(AVFrame)]
    av_frame_get_pkt_size.restype = c_int

# /usr/include/libavutil/frame.h: 740
if _libs["avcodec"].has("av_frame_set_pkt_size", "cdecl"):
    av_frame_set_pkt_size = _libs["avcodec"].get("av_frame_set_pkt_size", "cdecl")
    av_frame_set_pkt_size.argtypes = [POINTER(AVFrame), c_int]
    av_frame_set_pkt_size.restype = None

# /usr/include/libavutil/frame.h: 743
if _libs["avcodec"].has("av_frame_get_qp_table", "cdecl"):
    av_frame_get_qp_table = _libs["avcodec"].get("av_frame_get_qp_table", "cdecl")
    av_frame_get_qp_table.argtypes = [POINTER(AVFrame), POINTER(c_int), POINTER(c_int)]
    av_frame_get_qp_table.restype = POINTER(c_int8)

# /usr/include/libavutil/frame.h: 745
if _libs["avcodec"].has("av_frame_set_qp_table", "cdecl"):
    av_frame_set_qp_table = _libs["avcodec"].get("av_frame_set_qp_table", "cdecl")
    av_frame_set_qp_table.argtypes = [POINTER(AVFrame), POINTER(AVBufferRef), c_int, c_int]
    av_frame_set_qp_table.restype = c_int

# /usr/include/libavutil/frame.h: 748
if _libs["avcodec"].has("av_frame_get_colorspace", "cdecl"):
    av_frame_get_colorspace = _libs["avcodec"].get("av_frame_get_colorspace", "cdecl")
    av_frame_get_colorspace.argtypes = [POINTER(AVFrame)]
    av_frame_get_colorspace.restype = enum_AVColorSpace

# /usr/include/libavutil/frame.h: 750
if _libs["avcodec"].has("av_frame_set_colorspace", "cdecl"):
    av_frame_set_colorspace = _libs["avcodec"].get("av_frame_set_colorspace", "cdecl")
    av_frame_set_colorspace.argtypes = [POINTER(AVFrame), enum_AVColorSpace]
    av_frame_set_colorspace.restype = None

# /usr/include/libavutil/frame.h: 752
if _libs["avcodec"].has("av_frame_get_color_range", "cdecl"):
    av_frame_get_color_range = _libs["avcodec"].get("av_frame_get_color_range", "cdecl")
    av_frame_get_color_range.argtypes = [POINTER(AVFrame)]
    av_frame_get_color_range.restype = enum_AVColorRange

# /usr/include/libavutil/frame.h: 754
if _libs["avcodec"].has("av_frame_set_color_range", "cdecl"):
    av_frame_set_color_range = _libs["avcodec"].get("av_frame_set_color_range", "cdecl")
    av_frame_set_color_range.argtypes = [POINTER(AVFrame), enum_AVColorRange]
    av_frame_set_color_range.restype = None

# /usr/include/libavutil/frame.h: 761
if _libs["avcodec"].has("av_get_colorspace_name", "cdecl"):
    av_get_colorspace_name = _libs["avcodec"].get("av_get_colorspace_name", "cdecl")
    av_get_colorspace_name.argtypes = [enum_AVColorSpace]
    av_get_colorspace_name.restype = c_char_p

# /usr/include/libavutil/frame.h: 773
if _libs["avcodec"].has("av_frame_alloc", "cdecl"):
    av_frame_alloc = _libs["avcodec"].get("av_frame_alloc", "cdecl")
    av_frame_alloc.argtypes = []
    av_frame_alloc.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 782
if _libs["avcodec"].has("av_frame_free", "cdecl"):
    av_frame_free = _libs["avcodec"].get("av_frame_free", "cdecl")
    av_frame_free.argtypes = [POINTER(POINTER(AVFrame))]
    av_frame_free.restype = None

# /usr/include/libavutil/frame.h: 799
if _libs["avcodec"].has("av_frame_ref", "cdecl"):
    av_frame_ref = _libs["avcodec"].get("av_frame_ref", "cdecl")
    av_frame_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_ref.restype = c_int

# /usr/include/libavutil/frame.h: 808
if _libs["avcodec"].has("av_frame_clone", "cdecl"):
    av_frame_clone = _libs["avcodec"].get("av_frame_clone", "cdecl")
    av_frame_clone.argtypes = [POINTER(AVFrame)]
    av_frame_clone.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 813
if _libs["avcodec"].has("av_frame_unref", "cdecl"):
    av_frame_unref = _libs["avcodec"].get("av_frame_unref", "cdecl")
    av_frame_unref.argtypes = [POINTER(AVFrame)]
    av_frame_unref.restype = None

# /usr/include/libavutil/frame.h: 822
if _libs["avcodec"].has("av_frame_move_ref", "cdecl"):
    av_frame_move_ref = _libs["avcodec"].get("av_frame_move_ref", "cdecl")
    av_frame_move_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_move_ref.restype = None

# /usr/include/libavutil/frame.h: 847
if _libs["avcodec"].has("av_frame_get_buffer", "cdecl"):
    av_frame_get_buffer = _libs["avcodec"].get("av_frame_get_buffer", "cdecl")
    av_frame_get_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_buffer.restype = c_int

# /usr/include/libavutil/frame.h: 861
if _libs["avcodec"].has("av_frame_is_writable", "cdecl"):
    av_frame_is_writable = _libs["avcodec"].get("av_frame_is_writable", "cdecl")
    av_frame_is_writable.argtypes = [POINTER(AVFrame)]
    av_frame_is_writable.restype = c_int

# /usr/include/libavutil/frame.h: 874
if _libs["avcodec"].has("av_frame_make_writable", "cdecl"):
    av_frame_make_writable = _libs["avcodec"].get("av_frame_make_writable", "cdecl")
    av_frame_make_writable.argtypes = [POINTER(AVFrame)]
    av_frame_make_writable.restype = c_int

# /usr/include/libavutil/frame.h: 887
if _libs["avcodec"].has("av_frame_copy", "cdecl"):
    av_frame_copy = _libs["avcodec"].get("av_frame_copy", "cdecl")
    av_frame_copy.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy.restype = c_int

# /usr/include/libavutil/frame.h: 897
if _libs["avcodec"].has("av_frame_copy_props", "cdecl"):
    av_frame_copy_props = _libs["avcodec"].get("av_frame_copy_props", "cdecl")
    av_frame_copy_props.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy_props.restype = c_int

# /usr/include/libavutil/frame.h: 907
if _libs["avcodec"].has("av_frame_get_plane_buffer", "cdecl"):
    av_frame_get_plane_buffer = _libs["avcodec"].get("av_frame_get_plane_buffer", "cdecl")
    av_frame_get_plane_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_plane_buffer.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/frame.h: 918
if _libs["avcodec"].has("av_frame_new_side_data", "cdecl"):
    av_frame_new_side_data = _libs["avcodec"].get("av_frame_new_side_data", "cdecl")
    av_frame_new_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, c_int]
    av_frame_new_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 938
if _libs["avcodec"].has("av_frame_new_side_data_from_buf", "cdecl"):
    av_frame_new_side_data_from_buf = _libs["avcodec"].get("av_frame_new_side_data_from_buf", "cdecl")
    av_frame_new_side_data_from_buf.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, POINTER(AVBufferRef)]
    av_frame_new_side_data_from_buf.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 946
if _libs["avcodec"].has("av_frame_get_side_data", "cdecl"):
    av_frame_get_side_data = _libs["avcodec"].get("av_frame_get_side_data", "cdecl")
    av_frame_get_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_get_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 952
if _libs["avcodec"].has("av_frame_remove_side_data", "cdecl"):
    av_frame_remove_side_data = _libs["avcodec"].get("av_frame_remove_side_data", "cdecl")
    av_frame_remove_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_remove_side_data.restype = None

enum_anon_26 = c_int# /usr/include/libavutil/frame.h: 958

AV_FRAME_CROP_UNALIGNED = (1 << 0)# /usr/include/libavutil/frame.h: 958

# /usr/include/libavutil/frame.h: 986
if _libs["avcodec"].has("av_frame_apply_cropping", "cdecl"):
    av_frame_apply_cropping = _libs["avcodec"].get("av_frame_apply_cropping", "cdecl")
    av_frame_apply_cropping.argtypes = [POINTER(AVFrame), c_int]
    av_frame_apply_cropping.restype = c_int

# /usr/include/libavutil/frame.h: 991
if _libs["avcodec"].has("av_frame_side_data_name", "cdecl"):
    av_frame_side_data_name = _libs["avcodec"].get("av_frame_side_data_name", "cdecl")
    av_frame_side_data_name.argtypes = [enum_AVFrameSideDataType]
    av_frame_side_data_name.restype = c_char_p

enum_AVHWDeviceType = c_int# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_NONE = 0# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_VDPAU = (AV_HWDEVICE_TYPE_NONE + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_CUDA = (AV_HWDEVICE_TYPE_VDPAU + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_VAAPI = (AV_HWDEVICE_TYPE_CUDA + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_DXVA2 = (AV_HWDEVICE_TYPE_VAAPI + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_QSV = (AV_HWDEVICE_TYPE_DXVA2 + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_VIDEOTOOLBOX = (AV_HWDEVICE_TYPE_QSV + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_D3D11VA = (AV_HWDEVICE_TYPE_VIDEOTOOLBOX + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_DRM = (AV_HWDEVICE_TYPE_D3D11VA + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_OPENCL = (AV_HWDEVICE_TYPE_DRM + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_MEDIACODEC = (AV_HWDEVICE_TYPE_OPENCL + 1)# /usr/include/libavutil/hwcontext.h: 27

AV_HWDEVICE_TYPE_VULKAN = (AV_HWDEVICE_TYPE_MEDIACODEC + 1)# /usr/include/libavutil/hwcontext.h: 27

# /usr/include/libavutil/hwcontext.h: 42
class struct_AVHWDeviceInternal(Structure):
    pass

AVHWDeviceInternal = struct_AVHWDeviceInternal# /usr/include/libavutil/hwcontext.h: 42

# /usr/include/libavutil/hwcontext.h: 61
class struct_AVHWDeviceContext(Structure):
    pass

struct_AVHWDeviceContext.__slots__ = [
    'av_class',
    'internal',
    'type',
    'hwctx',
    'free',
    'user_opaque',
]
struct_AVHWDeviceContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('internal', POINTER(AVHWDeviceInternal)),
    ('type', enum_AVHWDeviceType),
    ('hwctx', POINTER(None)),
    ('free', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVHWDeviceContext))),
    ('user_opaque', POINTER(None)),
]

AVHWDeviceContext = struct_AVHWDeviceContext# /usr/include/libavutil/hwcontext.h: 110

# /usr/include/libavutil/hwcontext.h: 112
class struct_AVHWFramesInternal(Structure):
    pass

AVHWFramesInternal = struct_AVHWFramesInternal# /usr/include/libavutil/hwcontext.h: 112

# /usr/include/libavutil/hwcontext.h: 124
class struct_AVHWFramesContext(Structure):
    pass

struct_AVHWFramesContext.__slots__ = [
    'av_class',
    'internal',
    'device_ref',
    'device_ctx',
    'hwctx',
    'free',
    'user_opaque',
    'pool',
    'initial_pool_size',
    'format',
    'sw_format',
    'width',
    'height',
]
struct_AVHWFramesContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('internal', POINTER(AVHWFramesInternal)),
    ('device_ref', POINTER(AVBufferRef)),
    ('device_ctx', POINTER(AVHWDeviceContext)),
    ('hwctx', POINTER(None)),
    ('free', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVHWFramesContext))),
    ('user_opaque', POINTER(None)),
    ('pool', POINTER(AVBufferPool)),
    ('initial_pool_size', c_int),
    ('format', enum_AVPixelFormat),
    ('sw_format', enum_AVPixelFormat),
    ('width', c_int),
    ('height', c_int),
]

AVHWFramesContext = struct_AVHWFramesContext# /usr/include/libavutil/hwcontext.h: 230

# /usr/include/libavutil/hwcontext.h: 239
if _libs["avcodec"].has("av_hwdevice_find_type_by_name", "cdecl"):
    av_hwdevice_find_type_by_name = _libs["avcodec"].get("av_hwdevice_find_type_by_name", "cdecl")
    av_hwdevice_find_type_by_name.argtypes = [String]
    av_hwdevice_find_type_by_name.restype = enum_AVHWDeviceType

# /usr/include/libavutil/hwcontext.h: 247
if _libs["avcodec"].has("av_hwdevice_get_type_name", "cdecl"):
    av_hwdevice_get_type_name = _libs["avcodec"].get("av_hwdevice_get_type_name", "cdecl")
    av_hwdevice_get_type_name.argtypes = [enum_AVHWDeviceType]
    av_hwdevice_get_type_name.restype = c_char_p

# /usr/include/libavutil/hwcontext.h: 257
if _libs["avcodec"].has("av_hwdevice_iterate_types", "cdecl"):
    av_hwdevice_iterate_types = _libs["avcodec"].get("av_hwdevice_iterate_types", "cdecl")
    av_hwdevice_iterate_types.argtypes = [enum_AVHWDeviceType]
    av_hwdevice_iterate_types.restype = enum_AVHWDeviceType

# /usr/include/libavutil/hwcontext.h: 266
if _libs["avcodec"].has("av_hwdevice_ctx_alloc", "cdecl"):
    av_hwdevice_ctx_alloc = _libs["avcodec"].get("av_hwdevice_ctx_alloc", "cdecl")
    av_hwdevice_ctx_alloc.argtypes = [enum_AVHWDeviceType]
    av_hwdevice_ctx_alloc.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/hwcontext.h: 276
if _libs["avcodec"].has("av_hwdevice_ctx_init", "cdecl"):
    av_hwdevice_ctx_init = _libs["avcodec"].get("av_hwdevice_ctx_init", "cdecl")
    av_hwdevice_ctx_init.argtypes = [POINTER(AVBufferRef)]
    av_hwdevice_ctx_init.restype = c_int

# /usr/include/libavutil/hwcontext.h: 303
if _libs["avcodec"].has("av_hwdevice_ctx_create", "cdecl"):
    av_hwdevice_ctx_create = _libs["avcodec"].get("av_hwdevice_ctx_create", "cdecl")
    av_hwdevice_ctx_create.argtypes = [POINTER(POINTER(AVBufferRef)), enum_AVHWDeviceType, String, POINTER(AVDictionary), c_int]
    av_hwdevice_ctx_create.restype = c_int

# /usr/include/libavutil/hwcontext.h: 327
if _libs["avcodec"].has("av_hwdevice_ctx_create_derived", "cdecl"):
    av_hwdevice_ctx_create_derived = _libs["avcodec"].get("av_hwdevice_ctx_create_derived", "cdecl")
    av_hwdevice_ctx_create_derived.argtypes = [POINTER(POINTER(AVBufferRef)), enum_AVHWDeviceType, POINTER(AVBufferRef), c_int]
    av_hwdevice_ctx_create_derived.restype = c_int

# /usr/include/libavutil/hwcontext.h: 347
if _libs["avcodec"].has("av_hwdevice_ctx_create_derived_opts", "cdecl"):
    av_hwdevice_ctx_create_derived_opts = _libs["avcodec"].get("av_hwdevice_ctx_create_derived_opts", "cdecl")
    av_hwdevice_ctx_create_derived_opts.argtypes = [POINTER(POINTER(AVBufferRef)), enum_AVHWDeviceType, POINTER(AVBufferRef), POINTER(AVDictionary), c_int]
    av_hwdevice_ctx_create_derived_opts.restype = c_int

# /usr/include/libavutil/hwcontext.h: 361
if _libs["avcodec"].has("av_hwframe_ctx_alloc", "cdecl"):
    av_hwframe_ctx_alloc = _libs["avcodec"].get("av_hwframe_ctx_alloc", "cdecl")
    av_hwframe_ctx_alloc.argtypes = [POINTER(AVBufferRef)]
    av_hwframe_ctx_alloc.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/hwcontext.h: 371
if _libs["avcodec"].has("av_hwframe_ctx_init", "cdecl"):
    av_hwframe_ctx_init = _libs["avcodec"].get("av_hwframe_ctx_init", "cdecl")
    av_hwframe_ctx_init.argtypes = [POINTER(AVBufferRef)]
    av_hwframe_ctx_init.restype = c_int

# /usr/include/libavutil/hwcontext.h: 382
if _libs["avcodec"].has("av_hwframe_get_buffer", "cdecl"):
    av_hwframe_get_buffer = _libs["avcodec"].get("av_hwframe_get_buffer", "cdecl")
    av_hwframe_get_buffer.argtypes = [POINTER(AVBufferRef), POINTER(AVFrame), c_int]
    av_hwframe_get_buffer.restype = c_int

# /usr/include/libavutil/hwcontext.h: 413
if _libs["avcodec"].has("av_hwframe_transfer_data", "cdecl"):
    av_hwframe_transfer_data = _libs["avcodec"].get("av_hwframe_transfer_data", "cdecl")
    av_hwframe_transfer_data.argtypes = [POINTER(AVFrame), POINTER(AVFrame), c_int]
    av_hwframe_transfer_data.restype = c_int

enum_AVHWFrameTransferDirection = c_int# /usr/include/libavutil/hwcontext.h: 415

AV_HWFRAME_TRANSFER_DIRECTION_FROM = 0# /usr/include/libavutil/hwcontext.h: 415

AV_HWFRAME_TRANSFER_DIRECTION_TO = (AV_HWFRAME_TRANSFER_DIRECTION_FROM + 1)# /usr/include/libavutil/hwcontext.h: 415

# /usr/include/libavutil/hwcontext.h: 442
if _libs["avcodec"].has("av_hwframe_transfer_get_formats", "cdecl"):
    av_hwframe_transfer_get_formats = _libs["avcodec"].get("av_hwframe_transfer_get_formats", "cdecl")
    av_hwframe_transfer_get_formats.argtypes = [POINTER(AVBufferRef), enum_AVHWFrameTransferDirection, POINTER(POINTER(enum_AVPixelFormat)), c_int]
    av_hwframe_transfer_get_formats.restype = c_int

# /usr/include/libavutil/hwcontext.h: 480
class struct_AVHWFramesConstraints(Structure):
    pass

struct_AVHWFramesConstraints.__slots__ = [
    'valid_hw_formats',
    'valid_sw_formats',
    'min_width',
    'min_height',
    'max_width',
    'max_height',
]
struct_AVHWFramesConstraints._fields_ = [
    ('valid_hw_formats', POINTER(enum_AVPixelFormat)),
    ('valid_sw_formats', POINTER(enum_AVPixelFormat)),
    ('min_width', c_int),
    ('min_height', c_int),
    ('max_width', c_int),
    ('max_height', c_int),
]

AVHWFramesConstraints = struct_AVHWFramesConstraints# /usr/include/libavutil/hwcontext.h: 480

# /usr/include/libavutil/hwcontext.h: 492
if _libs["avcodec"].has("av_hwdevice_hwconfig_alloc", "cdecl"):
    av_hwdevice_hwconfig_alloc = _libs["avcodec"].get("av_hwdevice_hwconfig_alloc", "cdecl")
    av_hwdevice_hwconfig_alloc.argtypes = [POINTER(AVBufferRef)]
    av_hwdevice_hwconfig_alloc.restype = POINTER(c_ubyte)
    av_hwdevice_hwconfig_alloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/hwcontext.h: 506
if _libs["avcodec"].has("av_hwdevice_get_hwframe_constraints", "cdecl"):
    av_hwdevice_get_hwframe_constraints = _libs["avcodec"].get("av_hwdevice_get_hwframe_constraints", "cdecl")
    av_hwdevice_get_hwframe_constraints.argtypes = [POINTER(AVBufferRef), POINTER(None)]
    av_hwdevice_get_hwframe_constraints.restype = POINTER(AVHWFramesConstraints)

# /usr/include/libavutil/hwcontext.h: 514
if _libs["avcodec"].has("av_hwframe_constraints_free", "cdecl"):
    av_hwframe_constraints_free = _libs["avcodec"].get("av_hwframe_constraints_free", "cdecl")
    av_hwframe_constraints_free.argtypes = [POINTER(POINTER(AVHWFramesConstraints))]
    av_hwframe_constraints_free.restype = None

enum_anon_27 = c_int# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_READ = (1 << 0)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_WRITE = (1 << 1)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_OVERWRITE = (1 << 2)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_DIRECT = (1 << 3)# /usr/include/libavutil/hwcontext.h: 520

# /usr/include/libavutil/hwcontext.h: 579
if _libs["avcodec"].has("av_hwframe_map", "cdecl"):
    av_hwframe_map = _libs["avcodec"].get("av_hwframe_map", "cdecl")
    av_hwframe_map.argtypes = [POINTER(AVFrame), POINTER(AVFrame), c_int]
    av_hwframe_map.restype = c_int

# /usr/include/libavutil/hwcontext.h: 599
if _libs["avcodec"].has("av_hwframe_ctx_create_derived", "cdecl"):
    av_hwframe_ctx_create_derived = _libs["avcodec"].get("av_hwframe_ctx_create_derived", "cdecl")
    av_hwframe_ctx_create_derived.argtypes = [POINTER(POINTER(AVBufferRef)), enum_AVPixelFormat, POINTER(AVBufferRef), POINTER(AVBufferRef), c_int]
    av_hwframe_ctx_create_derived.restype = c_int

enum_AVCodecID = c_int# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_NONE = 0# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEG1VIDEO = (AV_CODEC_ID_NONE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEG2VIDEO = (AV_CODEC_ID_MPEG1VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_H261 = (AV_CODEC_ID_MPEG2VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_H263 = (AV_CODEC_ID_H261 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RV10 = (AV_CODEC_ID_H263 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RV20 = (AV_CODEC_ID_RV10 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MJPEG = (AV_CODEC_ID_RV20 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MJPEGB = (AV_CODEC_ID_MJPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_LJPEG = (AV_CODEC_ID_MJPEGB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SP5X = (AV_CODEC_ID_LJPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_JPEGLS = (AV_CODEC_ID_SP5X + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEG4 = (AV_CODEC_ID_JPEGLS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RAWVIDEO = (AV_CODEC_ID_MPEG4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V1 = (AV_CODEC_ID_RAWVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V2 = (AV_CODEC_ID_MSMPEG4V1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSMPEG4V3 = (AV_CODEC_ID_MSMPEG4V2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMV1 = (AV_CODEC_ID_MSMPEG4V3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMV2 = (AV_CODEC_ID_WMV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_H263P = (AV_CODEC_ID_WMV2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_H263I = (AV_CODEC_ID_H263P + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FLV1 = (AV_CODEC_ID_H263I + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SVQ1 = (AV_CODEC_ID_FLV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SVQ3 = (AV_CODEC_ID_SVQ1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVVIDEO = (AV_CODEC_ID_SVQ3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HUFFYUV = (AV_CODEC_ID_DVVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CYUV = (AV_CODEC_ID_HUFFYUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_H264 = (AV_CODEC_ID_CYUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INDEO3 = (AV_CODEC_ID_H264 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP3 = (AV_CODEC_ID_INDEO3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_THEORA = (AV_CODEC_ID_VP3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ASV1 = (AV_CODEC_ID_THEORA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ASV2 = (AV_CODEC_ID_ASV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FFV1 = (AV_CODEC_ID_ASV2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_4XM = (AV_CODEC_ID_FFV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VCR1 = (AV_CODEC_ID_4XM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CLJR = (AV_CODEC_ID_VCR1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MDEC = (AV_CODEC_ID_CLJR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ROQ = (AV_CODEC_ID_MDEC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_VIDEO = (AV_CODEC_ID_ROQ + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XAN_WC3 = (AV_CODEC_ID_INTERPLAY_VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XAN_WC4 = (AV_CODEC_ID_XAN_WC3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RPZA = (AV_CODEC_ID_XAN_WC4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CINEPAK = (AV_CODEC_ID_RPZA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WS_VQA = (AV_CODEC_ID_CINEPAK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSRLE = (AV_CODEC_ID_WS_VQA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSVIDEO1 = (AV_CODEC_ID_MSRLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IDCIN = (AV_CODEC_ID_MSVIDEO1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_8BPS = (AV_CODEC_ID_IDCIN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMC = (AV_CODEC_ID_8BPS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FLIC = (AV_CODEC_ID_SMC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION1 = (AV_CODEC_ID_FLIC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VMDVIDEO = (AV_CODEC_ID_TRUEMOTION1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSZH = (AV_CODEC_ID_VMDVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ZLIB = (AV_CODEC_ID_MSZH + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QTRLE = (AV_CODEC_ID_ZLIB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TSCC = (AV_CODEC_ID_QTRLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ULTI = (AV_CODEC_ID_TSCC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QDRAW = (AV_CODEC_ID_ULTI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VIXL = (AV_CODEC_ID_QDRAW + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QPEG = (AV_CODEC_ID_VIXL + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PNG = (AV_CODEC_ID_QPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PPM = (AV_CODEC_ID_PNG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PBM = (AV_CODEC_ID_PPM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PGM = (AV_CODEC_ID_PBM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PGMYUV = (AV_CODEC_ID_PGM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PAM = (AV_CODEC_ID_PGMYUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FFVHUFF = (AV_CODEC_ID_PAM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RV30 = (AV_CODEC_ID_FFVHUFF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RV40 = (AV_CODEC_ID_RV30 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VC1 = (AV_CODEC_ID_RV40 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMV3 = (AV_CODEC_ID_VC1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_LOCO = (AV_CODEC_ID_WMV3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WNV1 = (AV_CODEC_ID_LOCO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AASC = (AV_CODEC_ID_WNV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INDEO2 = (AV_CODEC_ID_AASC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FRAPS = (AV_CODEC_ID_INDEO2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION2 = (AV_CODEC_ID_FRAPS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BMP = (AV_CODEC_ID_TRUEMOTION2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CSCD = (AV_CODEC_ID_BMP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MMVIDEO = (AV_CODEC_ID_CSCD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ZMBV = (AV_CODEC_ID_MMVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVS = (AV_CODEC_ID_ZMBV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMACKVIDEO = (AV_CODEC_ID_AVS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_NUV = (AV_CODEC_ID_SMACKVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_KMVC = (AV_CODEC_ID_NUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FLASHSV = (AV_CODEC_ID_KMVC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CAVS = (AV_CODEC_ID_FLASHSV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_JPEG2000 = (AV_CODEC_ID_CAVS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VMNC = (AV_CODEC_ID_JPEG2000 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP5 = (AV_CODEC_ID_VMNC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP6 = (AV_CODEC_ID_VP5 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP6F = (AV_CODEC_ID_VP6 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TARGA = (AV_CODEC_ID_VP6F + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSICINVIDEO = (AV_CODEC_ID_TARGA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TIERTEXSEQVIDEO = (AV_CODEC_ID_DSICINVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TIFF = (AV_CODEC_ID_TIERTEXSEQVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_GIF = (AV_CODEC_ID_TIFF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DXA = (AV_CODEC_ID_GIF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DNXHD = (AV_CODEC_ID_DXA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_THP = (AV_CODEC_ID_DNXHD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SGI = (AV_CODEC_ID_THP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_C93 = (AV_CODEC_ID_SGI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BETHSOFTVID = (AV_CODEC_ID_C93 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PTX = (AV_CODEC_ID_BETHSOFTVID + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TXD = (AV_CODEC_ID_PTX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP6A = (AV_CODEC_ID_TXD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AMV = (AV_CODEC_ID_VP6A + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VB = (AV_CODEC_ID_AMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCX = (AV_CODEC_ID_VB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SUNRAST = (AV_CODEC_ID_PCX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INDEO4 = (AV_CODEC_ID_SUNRAST + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INDEO5 = (AV_CODEC_ID_INDEO4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MIMIC = (AV_CODEC_ID_INDEO5 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RL2 = (AV_CODEC_ID_MIMIC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ESCAPE124 = (AV_CODEC_ID_RL2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DIRAC = (AV_CODEC_ID_ESCAPE124 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BFI = (AV_CODEC_ID_DIRAC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CMV = (AV_CODEC_ID_BFI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MOTIONPIXELS = (AV_CODEC_ID_CMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TGV = (AV_CODEC_ID_MOTIONPIXELS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TGQ = (AV_CODEC_ID_TGV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TQI = (AV_CODEC_ID_TGQ + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AURA = (AV_CODEC_ID_TQI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AURA2 = (AV_CODEC_ID_AURA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_V210X = (AV_CODEC_ID_AURA2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TMV = (AV_CODEC_ID_V210X + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_V210 = (AV_CODEC_ID_TMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DPX = (AV_CODEC_ID_V210 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MAD = (AV_CODEC_ID_DPX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FRWU = (AV_CODEC_ID_MAD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FLASHSV2 = (AV_CODEC_ID_FRWU + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CDGRAPHICS = (AV_CODEC_ID_FLASHSV2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_R210 = (AV_CODEC_ID_CDGRAPHICS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ANM = (AV_CODEC_ID_R210 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BINKVIDEO = (AV_CODEC_ID_ANM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IFF_ILBM = (AV_CODEC_ID_BINKVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_KGV1 = (AV_CODEC_ID_IFF_ILBM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_YOP = (AV_CODEC_ID_KGV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP8 = (AV_CODEC_ID_YOP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PICTOR = (AV_CODEC_ID_VP8 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ANSI = (AV_CODEC_ID_PICTOR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_A64_MULTI = (AV_CODEC_ID_ANSI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_A64_MULTI5 = (AV_CODEC_ID_A64_MULTI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_R10K = (AV_CODEC_ID_A64_MULTI5 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MXPEG = (AV_CODEC_ID_R10K + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_LAGARITH = (AV_CODEC_ID_MXPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PRORES = (AV_CODEC_ID_LAGARITH + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_JV = (AV_CODEC_ID_PRORES + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DFA = (AV_CODEC_ID_JV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMV3IMAGE = (AV_CODEC_ID_DFA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VC1IMAGE = (AV_CODEC_ID_WMV3IMAGE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_UTVIDEO = (AV_CODEC_ID_VC1IMAGE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BMV_VIDEO = (AV_CODEC_ID_UTVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VBLE = (AV_CODEC_ID_BMV_VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DXTORY = (AV_CODEC_ID_VBLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_V410 = (AV_CODEC_ID_DXTORY + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XWD = (AV_CODEC_ID_V410 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CDXL = (AV_CODEC_ID_XWD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XBM = (AV_CODEC_ID_CDXL + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ZEROCODEC = (AV_CODEC_ID_XBM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSS1 = (AV_CODEC_ID_ZEROCODEC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSA1 = (AV_CODEC_ID_MSS1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TSCC2 = (AV_CODEC_ID_MSA1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MTS2 = (AV_CODEC_ID_TSCC2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CLLC = (AV_CODEC_ID_MTS2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSS2 = (AV_CODEC_ID_CLLC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP9 = (AV_CODEC_ID_MSS2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AIC = (AV_CODEC_ID_VP9 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ESCAPE130 = (AV_CODEC_ID_AIC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_G2M = (AV_CODEC_ID_ESCAPE130 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WEBP = (AV_CODEC_ID_G2M + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HNM4_VIDEO = (AV_CODEC_ID_WEBP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HEVC = (AV_CODEC_ID_HNM4_VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FIC = (AV_CODEC_ID_HEVC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ALIAS_PIX = (AV_CODEC_ID_FIC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BRENDER_PIX = (AV_CODEC_ID_ALIAS_PIX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PAF_VIDEO = (AV_CODEC_ID_BRENDER_PIX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_EXR = (AV_CODEC_ID_PAF_VIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP7 = (AV_CODEC_ID_EXR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SANM = (AV_CODEC_ID_VP7 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SGIRLE = (AV_CODEC_ID_SANM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MVC1 = (AV_CODEC_ID_SGIRLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MVC2 = (AV_CODEC_ID_MVC1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HQX = (AV_CODEC_ID_MVC2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TDSC = (AV_CODEC_ID_HQX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HQ_HQA = (AV_CODEC_ID_TDSC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HAP = (AV_CODEC_ID_HQ_HQA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DDS = (AV_CODEC_ID_HAP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DXV = (AV_CODEC_ID_DDS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SCREENPRESSO = (AV_CODEC_ID_DXV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RSCC = (AV_CODEC_ID_SCREENPRESSO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVS2 = (AV_CODEC_ID_RSCC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PGX = (AV_CODEC_ID_AVS2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVS3 = (AV_CODEC_ID_PGX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSP2 = (AV_CODEC_ID_AVS3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VVC = (AV_CODEC_ID_MSP2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_Y41P = 32768# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVRP = (AV_CODEC_ID_Y41P + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_012V = (AV_CODEC_ID_AVRP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVUI = (AV_CODEC_ID_012V + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AYUV = (AV_CODEC_ID_AVUI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TARGA_Y216 = (AV_CODEC_ID_AYUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_V308 = (AV_CODEC_ID_TARGA_Y216 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_V408 = (AV_CODEC_ID_V308 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_YUV4 = (AV_CODEC_ID_V408 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AVRN = (AV_CODEC_ID_YUV4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CPIA = (AV_CODEC_ID_AVRN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XFACE = (AV_CODEC_ID_CPIA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SNOW = (AV_CODEC_ID_XFACE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMVJPEG = (AV_CODEC_ID_SNOW + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_APNG = (AV_CODEC_ID_SMVJPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DAALA = (AV_CODEC_ID_APNG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CFHD = (AV_CODEC_ID_DAALA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TRUEMOTION2RT = (AV_CODEC_ID_CFHD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_M101 = (AV_CODEC_ID_TRUEMOTION2RT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MAGICYUV = (AV_CODEC_ID_M101 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SHEERVIDEO = (AV_CODEC_ID_MAGICYUV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_YLC = (AV_CODEC_ID_SHEERVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PSD = (AV_CODEC_ID_YLC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PIXLET = (AV_CODEC_ID_PSD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SPEEDHQ = (AV_CODEC_ID_PIXLET + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FMVC = (AV_CODEC_ID_SPEEDHQ + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SCPR = (AV_CODEC_ID_FMVC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CLEARVIDEO = (AV_CODEC_ID_SCPR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XPM = (AV_CODEC_ID_CLEARVIDEO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AV1 = (AV_CODEC_ID_XPM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BITPACKED = (AV_CODEC_ID_AV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MSCC = (AV_CODEC_ID_BITPACKED + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SRGC = (AV_CODEC_ID_MSCC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SVG = (AV_CODEC_ID_SRGC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_GDV = (AV_CODEC_ID_SVG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FITS = (AV_CODEC_ID_GDV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IMM4 = (AV_CODEC_ID_FITS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PROSUMER = (AV_CODEC_ID_IMM4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MWSC = (AV_CODEC_ID_PROSUMER + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WCMV = (AV_CODEC_ID_MWSC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RASC = (AV_CODEC_ID_WCMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HYMT = (AV_CODEC_ID_RASC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ARBC = (AV_CODEC_ID_HYMT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AGM = (AV_CODEC_ID_ARBC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_LSCR = (AV_CODEC_ID_AGM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VP4 = (AV_CODEC_ID_LSCR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IMM5 = (AV_CODEC_ID_VP4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MVDV = (AV_CODEC_ID_IMM5 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MVHA = (AV_CODEC_ID_MVDV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CDTOONS = (AV_CODEC_ID_MVHA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MV30 = (AV_CODEC_ID_CDTOONS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_NOTCHLC = (AV_CODEC_ID_MV30 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PFM = (AV_CODEC_ID_NOTCHLC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MOBICLIP = (AV_CODEC_ID_PFM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PHOTOCD = (AV_CODEC_ID_MOBICLIP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IPU = (AV_CODEC_ID_PHOTOCD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ARGO = (AV_CODEC_ID_IPU + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CRI = (AV_CODEC_ID_ARGO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SIMBIOSIS_IMX = (AV_CODEC_ID_CRI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SGA_VIDEO = (AV_CODEC_ID_SIMBIOSIS_IMX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FIRST_AUDIO = 65536# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S16LE = 65536# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S16BE = (AV_CODEC_ID_PCM_S16LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U16LE = (AV_CODEC_ID_PCM_S16BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U16BE = (AV_CODEC_ID_PCM_U16LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S8 = (AV_CODEC_ID_PCM_U16BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U8 = (AV_CODEC_ID_PCM_S8 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_MULAW = (AV_CODEC_ID_PCM_U8 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_ALAW = (AV_CODEC_ID_PCM_MULAW + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S32LE = (AV_CODEC_ID_PCM_ALAW + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S32BE = (AV_CODEC_ID_PCM_S32LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U32LE = (AV_CODEC_ID_PCM_S32BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U32BE = (AV_CODEC_ID_PCM_U32LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S24LE = (AV_CODEC_ID_PCM_U32BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S24BE = (AV_CODEC_ID_PCM_S24LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U24LE = (AV_CODEC_ID_PCM_S24BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_U24BE = (AV_CODEC_ID_PCM_U24LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S24DAUD = (AV_CODEC_ID_PCM_U24BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_ZORK = (AV_CODEC_ID_PCM_S24DAUD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S16LE_PLANAR = (AV_CODEC_ID_PCM_ZORK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_DVD = (AV_CODEC_ID_PCM_S16LE_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F32BE = (AV_CODEC_ID_PCM_DVD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F32LE = (AV_CODEC_ID_PCM_F32BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F64BE = (AV_CODEC_ID_PCM_F32LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F64LE = (AV_CODEC_ID_PCM_F64BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_BLURAY = (AV_CODEC_ID_PCM_F64LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_LXF = (AV_CODEC_ID_PCM_BLURAY + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_S302M = (AV_CODEC_ID_PCM_LXF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S8_PLANAR = (AV_CODEC_ID_S302M + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S24LE_PLANAR = (AV_CODEC_ID_PCM_S8_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S32LE_PLANAR = (AV_CODEC_ID_PCM_S24LE_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S16BE_PLANAR = (AV_CODEC_ID_PCM_S32LE_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S64LE = 67584# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_S64BE = (AV_CODEC_ID_PCM_S64LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F16LE = (AV_CODEC_ID_PCM_S64BE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_F24LE = (AV_CODEC_ID_PCM_F16LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_VIDC = (AV_CODEC_ID_PCM_F24LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PCM_SGA = (AV_CODEC_ID_PCM_VIDC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_QT = 69632# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_WAV = (AV_CODEC_ID_ADPCM_IMA_QT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DK3 = (AV_CODEC_ID_ADPCM_IMA_WAV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DK4 = (AV_CODEC_ID_ADPCM_IMA_DK3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_WS = (AV_CODEC_ID_ADPCM_IMA_DK4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_SMJPEG = (AV_CODEC_ID_ADPCM_IMA_WS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_MS = (AV_CODEC_ID_ADPCM_IMA_SMJPEG + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_4XM = (AV_CODEC_ID_ADPCM_MS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_XA = (AV_CODEC_ID_ADPCM_4XM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_ADX = (AV_CODEC_ID_ADPCM_XA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA = (AV_CODEC_ID_ADPCM_ADX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_G726 = (AV_CODEC_ID_ADPCM_EA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_CT = (AV_CODEC_ID_ADPCM_G726 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_SWF = (AV_CODEC_ID_ADPCM_CT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_YAMAHA = (AV_CODEC_ID_ADPCM_SWF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_4 = (AV_CODEC_ID_ADPCM_YAMAHA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_3 = (AV_CODEC_ID_ADPCM_SBPRO_4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_SBPRO_2 = (AV_CODEC_ID_ADPCM_SBPRO_3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_THP = (AV_CODEC_ID_ADPCM_SBPRO_2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_AMV = (AV_CODEC_ID_ADPCM_THP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R1 = (AV_CODEC_ID_ADPCM_IMA_AMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R3 = (AV_CODEC_ID_ADPCM_EA_R1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_R2 = (AV_CODEC_ID_ADPCM_EA_R3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_EA_SEAD = (AV_CODEC_ID_ADPCM_EA_R2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_EA_EACS = (AV_CODEC_ID_ADPCM_IMA_EA_SEAD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_XAS = (AV_CODEC_ID_ADPCM_IMA_EA_EACS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_EA_MAXIS_XA = (AV_CODEC_ID_ADPCM_EA_XAS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_ISS = (AV_CODEC_ID_ADPCM_EA_MAXIS_XA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_G722 = (AV_CODEC_ID_ADPCM_IMA_ISS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_APC = (AV_CODEC_ID_ADPCM_G722 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_VIMA = (AV_CODEC_ID_ADPCM_IMA_APC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_AFC = 71680# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_OKI = (AV_CODEC_ID_ADPCM_AFC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_DTK = (AV_CODEC_ID_ADPCM_IMA_OKI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_RAD = (AV_CODEC_ID_ADPCM_DTK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_G726LE = (AV_CODEC_ID_ADPCM_IMA_RAD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_THP_LE = (AV_CODEC_ID_ADPCM_G726LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_PSX = (AV_CODEC_ID_ADPCM_THP_LE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_AICA = (AV_CODEC_ID_ADPCM_PSX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_DAT4 = (AV_CODEC_ID_ADPCM_AICA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_MTAF = (AV_CODEC_ID_ADPCM_IMA_DAT4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_AGM = (AV_CODEC_ID_ADPCM_MTAF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_ARGO = (AV_CODEC_ID_ADPCM_AGM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_SSI = (AV_CODEC_ID_ADPCM_ARGO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_ZORK = (AV_CODEC_ID_ADPCM_IMA_SSI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_APM = (AV_CODEC_ID_ADPCM_ZORK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_ALP = (AV_CODEC_ID_ADPCM_IMA_APM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_MTF = (AV_CODEC_ID_ADPCM_IMA_ALP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_CUNNING = (AV_CODEC_ID_ADPCM_IMA_MTF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ADPCM_IMA_MOFLEX = (AV_CODEC_ID_ADPCM_IMA_CUNNING + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AMR_NB = 73728# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AMR_WB = (AV_CODEC_ID_AMR_NB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RA_144 = 77824# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RA_288 = (AV_CODEC_ID_RA_144 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ROQ_DPCM = 81920# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_DPCM = (AV_CODEC_ID_ROQ_DPCM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XAN_DPCM = (AV_CODEC_ID_INTERPLAY_DPCM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SOL_DPCM = (AV_CODEC_ID_XAN_DPCM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SDX2_DPCM = 83968# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_GREMLIN_DPCM = (AV_CODEC_ID_SDX2_DPCM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DERF_DPCM = (AV_CODEC_ID_GREMLIN_DPCM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP2 = 86016# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP3 = (AV_CODEC_ID_MP2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AAC = (AV_CODEC_ID_MP3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AC3 = (AV_CODEC_ID_AAC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DTS = (AV_CODEC_ID_AC3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VORBIS = (AV_CODEC_ID_DTS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVAUDIO = (AV_CODEC_ID_VORBIS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMAV1 = (AV_CODEC_ID_DVAUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMAV2 = (AV_CODEC_ID_WMAV1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MACE3 = (AV_CODEC_ID_WMAV2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MACE6 = (AV_CODEC_ID_MACE3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VMDAUDIO = (AV_CODEC_ID_MACE6 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FLAC = (AV_CODEC_ID_VMDAUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP3ADU = (AV_CODEC_ID_FLAC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP3ON4 = (AV_CODEC_ID_MP3ADU + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SHORTEN = (AV_CODEC_ID_MP3ON4 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ALAC = (AV_CODEC_ID_SHORTEN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WESTWOOD_SND1 = (AV_CODEC_ID_ALAC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_GSM = (AV_CODEC_ID_WESTWOOD_SND1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QDM2 = (AV_CODEC_ID_GSM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_COOK = (AV_CODEC_ID_QDM2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TRUESPEECH = (AV_CODEC_ID_COOK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TTA = (AV_CODEC_ID_TRUESPEECH + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMACKAUDIO = (AV_CODEC_ID_TTA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QCELP = (AV_CODEC_ID_SMACKAUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WAVPACK = (AV_CODEC_ID_QCELP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSICINAUDIO = (AV_CODEC_ID_WAVPACK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IMC = (AV_CODEC_ID_DSICINAUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MUSEPACK7 = (AV_CODEC_ID_IMC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MLP = (AV_CODEC_ID_MUSEPACK7 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_GSM_MS = (AV_CODEC_ID_MLP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC3 = (AV_CODEC_ID_GSM_MS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_APE = (AV_CODEC_ID_ATRAC3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_NELLYMOSER = (AV_CODEC_ID_APE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MUSEPACK8 = (AV_CODEC_ID_NELLYMOSER + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SPEEX = (AV_CODEC_ID_MUSEPACK8 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMAVOICE = (AV_CODEC_ID_SPEEX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMAPRO = (AV_CODEC_ID_WMAVOICE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WMALOSSLESS = (AV_CODEC_ID_WMAPRO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC3P = (AV_CODEC_ID_WMALOSSLESS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_EAC3 = (AV_CODEC_ID_ATRAC3P + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SIPR = (AV_CODEC_ID_EAC3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP1 = (AV_CODEC_ID_SIPR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TWINVQ = (AV_CODEC_ID_MP1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TRUEHD = (AV_CODEC_ID_TWINVQ + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MP4ALS = (AV_CODEC_ID_TRUEHD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC1 = (AV_CODEC_ID_MP4ALS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BINKAUDIO_RDFT = (AV_CODEC_ID_ATRAC1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BINKAUDIO_DCT = (AV_CODEC_ID_BINKAUDIO_RDFT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_AAC_LATM = (AV_CODEC_ID_BINKAUDIO_DCT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_QDMC = (AV_CODEC_ID_AAC_LATM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CELT = (AV_CODEC_ID_QDMC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_G723_1 = (AV_CODEC_ID_CELT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_G729 = (AV_CODEC_ID_G723_1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_8SVX_EXP = (AV_CODEC_ID_G729 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_8SVX_FIB = (AV_CODEC_ID_8SVX_EXP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BMV_AUDIO = (AV_CODEC_ID_8SVX_FIB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_RALF = (AV_CODEC_ID_BMV_AUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IAC = (AV_CODEC_ID_RALF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ILBC = (AV_CODEC_ID_IAC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_OPUS = (AV_CODEC_ID_ILBC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_COMFORT_NOISE = (AV_CODEC_ID_OPUS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TAK = (AV_CODEC_ID_COMFORT_NOISE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_METASOUND = (AV_CODEC_ID_TAK + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PAF_AUDIO = (AV_CODEC_ID_METASOUND + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ON2AVC = (AV_CODEC_ID_PAF_AUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSS_SP = (AV_CODEC_ID_ON2AVC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_CODEC2 = (AV_CODEC_ID_DSS_SP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FFWAVESYNTH = 88064# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SONIC = (AV_CODEC_ID_FFWAVESYNTH + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SONIC_LS = (AV_CODEC_ID_SONIC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_EVRC = (AV_CODEC_ID_SONIC_LS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMV = (AV_CODEC_ID_EVRC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSD_LSBF = (AV_CODEC_ID_SMV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSD_MSBF = (AV_CODEC_ID_DSD_LSBF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSD_LSBF_PLANAR = (AV_CODEC_ID_DSD_MSBF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DSD_MSBF_PLANAR = (AV_CODEC_ID_DSD_LSBF_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_4GV = (AV_CODEC_ID_DSD_MSBF_PLANAR + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_INTERPLAY_ACM = (AV_CODEC_ID_4GV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XMA1 = (AV_CODEC_ID_INTERPLAY_ACM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XMA2 = (AV_CODEC_ID_XMA1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DST = (AV_CODEC_ID_XMA2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC3AL = (AV_CODEC_ID_DST + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC3PAL = (AV_CODEC_ID_ATRAC3AL + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DOLBY_E = (AV_CODEC_ID_ATRAC3PAL + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_APTX = (AV_CODEC_ID_DOLBY_E + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_APTX_HD = (AV_CODEC_ID_APTX + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SBC = (AV_CODEC_ID_APTX_HD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ATRAC9 = (AV_CODEC_ID_SBC + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HCOM = (AV_CODEC_ID_ATRAC9 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ACELP_KELVIN = (AV_CODEC_ID_HCOM + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEGH_3D_AUDIO = (AV_CODEC_ID_ACELP_KELVIN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SIREN = (AV_CODEC_ID_MPEGH_3D_AUDIO + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HCA = (AV_CODEC_ID_SIREN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FASTAUDIO = (AV_CODEC_ID_HCA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FIRST_SUBTITLE = 94208# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVD_SUBTITLE = 94208# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVB_SUBTITLE = (AV_CODEC_ID_DVD_SUBTITLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TEXT = (AV_CODEC_ID_DVB_SUBTITLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XSUB = (AV_CODEC_ID_TEXT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SSA = (AV_CODEC_ID_XSUB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MOV_TEXT = (AV_CODEC_ID_SSA + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HDMV_PGS_SUBTITLE = (AV_CODEC_ID_MOV_TEXT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVB_TELETEXT = (AV_CODEC_ID_HDMV_PGS_SUBTITLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SRT = (AV_CODEC_ID_DVB_TELETEXT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MICRODVD = 96256# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_EIA_608 = (AV_CODEC_ID_MICRODVD + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_JACOSUB = (AV_CODEC_ID_EIA_608 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SAMI = (AV_CODEC_ID_JACOSUB + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_REALTEXT = (AV_CODEC_ID_SAMI + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_STL = (AV_CODEC_ID_REALTEXT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SUBVIEWER1 = (AV_CODEC_ID_STL + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SUBVIEWER = (AV_CODEC_ID_SUBVIEWER1 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SUBRIP = (AV_CODEC_ID_SUBVIEWER + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WEBVTT = (AV_CODEC_ID_SUBRIP + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPL2 = (AV_CODEC_ID_WEBVTT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_VPLAYER = (AV_CODEC_ID_MPL2 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PJS = (AV_CODEC_ID_VPLAYER + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ASS = (AV_CODEC_ID_PJS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_HDMV_TEXT_SUBTITLE = (AV_CODEC_ID_ASS + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TTML = (AV_CODEC_ID_HDMV_TEXT_SUBTITLE + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_ARIB_CAPTION = (AV_CODEC_ID_TTML + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FIRST_UNKNOWN = 98304# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TTF = 98304# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SCTE_35 = (AV_CODEC_ID_TTF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_EPG = (AV_CODEC_ID_SCTE_35 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BINTEXT = 100352# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_XBIN = (AV_CODEC_ID_BINTEXT + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_IDF = (AV_CODEC_ID_XBIN + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_OTF = (AV_CODEC_ID_IDF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_SMPTE_KLV = (AV_CODEC_ID_OTF + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_DVD_NAV = (AV_CODEC_ID_SMPTE_KLV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_TIMED_ID3 = (AV_CODEC_ID_DVD_NAV + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_BIN_DATA = (AV_CODEC_ID_TIMED_ID3 + 1)# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_PROBE = 102400# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEG2TS = 131072# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_MPEG4SYSTEMS = 131073# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_FFMETADATA = 135168# /home/josiah/ctypesgen_test/av/codec_id.h: 46

AV_CODEC_ID_WRAPPED_AVFRAME = 135169# /home/josiah/ctypesgen_test/av/codec_id.h: 46

# /home/josiah/ctypesgen_test/av/codec_id.h: 580
if _libs["avcodec"].has("avcodec_get_type", "cdecl"):
    avcodec_get_type = _libs["avcodec"].get("avcodec_get_type", "cdecl")
    avcodec_get_type.argtypes = [enum_AVCodecID]
    avcodec_get_type.restype = enum_AVMediaType

# /home/josiah/ctypesgen_test/av/codec_id.h: 586
if _libs["avcodec"].has("avcodec_get_name", "cdecl"):
    avcodec_get_name = _libs["avcodec"].get("avcodec_get_name", "cdecl")
    avcodec_get_name.argtypes = [enum_AVCodecID]
    avcodec_get_name.restype = c_char_p

enum_AVFieldOrder = c_int# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_PROGRESSIVE = (AV_FIELD_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_TT = (AV_FIELD_PROGRESSIVE + 1)# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_BB = (AV_FIELD_TT + 1)# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_TB = (AV_FIELD_BB + 1)# /home/josiah/ctypesgen_test/av/codec_par.h: 36

AV_FIELD_BT = (AV_FIELD_TB + 1)# /home/josiah/ctypesgen_test/av/codec_par.h: 36

# /home/josiah/ctypesgen_test/av/codec_par.h: 201
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

AVCodecParameters = struct_AVCodecParameters# /home/josiah/ctypesgen_test/av/codec_par.h: 201

# /home/josiah/ctypesgen_test/av/codec_par.h: 208
if _libs["avcodec"].has("avcodec_parameters_alloc", "cdecl"):
    avcodec_parameters_alloc = _libs["avcodec"].get("avcodec_parameters_alloc", "cdecl")
    avcodec_parameters_alloc.argtypes = []
    avcodec_parameters_alloc.restype = POINTER(AVCodecParameters)

# /home/josiah/ctypesgen_test/av/codec_par.h: 214
if _libs["avcodec"].has("avcodec_parameters_free", "cdecl"):
    avcodec_parameters_free = _libs["avcodec"].get("avcodec_parameters_free", "cdecl")
    avcodec_parameters_free.argtypes = [POINTER(POINTER(AVCodecParameters))]
    avcodec_parameters_free.restype = None

# /home/josiah/ctypesgen_test/av/codec_par.h: 222
if _libs["avcodec"].has("avcodec_parameters_copy", "cdecl"):
    avcodec_parameters_copy = _libs["avcodec"].get("avcodec_parameters_copy", "cdecl")
    avcodec_parameters_copy.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecParameters)]
    avcodec_parameters_copy.restype = c_int

enum_AVPacketSideDataType = c_int# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_PALETTE = 0# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_NEW_EXTRADATA = (AV_PKT_DATA_PALETTE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_PARAM_CHANGE = (AV_PKT_DATA_NEW_EXTRADATA + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_H263_MB_INFO = (AV_PKT_DATA_PARAM_CHANGE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_REPLAYGAIN = (AV_PKT_DATA_H263_MB_INFO + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_DISPLAYMATRIX = (AV_PKT_DATA_REPLAYGAIN + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_STEREO3D = (AV_PKT_DATA_DISPLAYMATRIX + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_AUDIO_SERVICE_TYPE = (AV_PKT_DATA_STEREO3D + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_QUALITY_STATS = (AV_PKT_DATA_AUDIO_SERVICE_TYPE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_FALLBACK_TRACK = (AV_PKT_DATA_QUALITY_STATS + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_CPB_PROPERTIES = (AV_PKT_DATA_FALLBACK_TRACK + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_SKIP_SAMPLES = (AV_PKT_DATA_CPB_PROPERTIES + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_JP_DUALMONO = (AV_PKT_DATA_SKIP_SAMPLES + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_STRINGS_METADATA = (AV_PKT_DATA_JP_DUALMONO + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_SUBTITLE_POSITION = (AV_PKT_DATA_STRINGS_METADATA + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL = (AV_PKT_DATA_SUBTITLE_POSITION + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_WEBVTT_IDENTIFIER = (AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_WEBVTT_SETTINGS = (AV_PKT_DATA_WEBVTT_IDENTIFIER + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_METADATA_UPDATE = (AV_PKT_DATA_WEBVTT_SETTINGS + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_MPEGTS_STREAM_ID = (AV_PKT_DATA_METADATA_UPDATE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_MASTERING_DISPLAY_METADATA = (AV_PKT_DATA_MPEGTS_STREAM_ID + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_SPHERICAL = (AV_PKT_DATA_MASTERING_DISPLAY_METADATA + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_CONTENT_LIGHT_LEVEL = (AV_PKT_DATA_SPHERICAL + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_A53_CC = (AV_PKT_DATA_CONTENT_LIGHT_LEVEL + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_ENCRYPTION_INIT_INFO = (AV_PKT_DATA_A53_CC + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_ENCRYPTION_INFO = (AV_PKT_DATA_ENCRYPTION_INIT_INFO + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_AFD = (AV_PKT_DATA_ENCRYPTION_INFO + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_PRFT = (AV_PKT_DATA_AFD + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_ICC_PROFILE = (AV_PKT_DATA_PRFT + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_DOVI_CONF = (AV_PKT_DATA_ICC_PROFILE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_S12M_TIMECODE = (AV_PKT_DATA_DOVI_CONF + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

AV_PKT_DATA_NB = (AV_PKT_DATA_S12M_TIMECODE + 1)# /home/josiah/ctypesgen_test/av/packet.h: 40

# /home/josiah/ctypesgen_test/av/packet.h: 314
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

AVPacketSideData = struct_AVPacketSideData# /home/josiah/ctypesgen_test/av/packet.h: 314

# /home/josiah/ctypesgen_test/av/packet.h: 400
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

AVPacket = struct_AVPacket# /home/josiah/ctypesgen_test/av/packet.h: 400

# /home/josiah/ctypesgen_test/av/packet.h: 404
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

AVPacketList = struct_AVPacketList# /home/josiah/ctypesgen_test/av/packet.h: 407

enum_AVSideDataParamChangeFlags = c_int# /home/josiah/ctypesgen_test/av/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_COUNT = 1# /home/josiah/ctypesgen_test/av/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_LAYOUT = 2# /home/josiah/ctypesgen_test/av/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_SAMPLE_RATE = 4# /home/josiah/ctypesgen_test/av/packet.h: 431

AV_SIDE_DATA_PARAM_CHANGE_DIMENSIONS = 8# /home/josiah/ctypesgen_test/av/packet.h: 431

# /home/josiah/ctypesgen_test/av/packet.h: 449
if _libs["avcodec"].has("av_packet_alloc", "cdecl"):
    av_packet_alloc = _libs["avcodec"].get("av_packet_alloc", "cdecl")
    av_packet_alloc.argtypes = []
    av_packet_alloc.restype = POINTER(AVPacket)

# /home/josiah/ctypesgen_test/av/packet.h: 461
if _libs["avcodec"].has("av_packet_clone", "cdecl"):
    av_packet_clone = _libs["avcodec"].get("av_packet_clone", "cdecl")
    av_packet_clone.argtypes = [POINTER(AVPacket)]
    av_packet_clone.restype = POINTER(AVPacket)

# /home/josiah/ctypesgen_test/av/packet.h: 470
if _libs["avcodec"].has("av_packet_free", "cdecl"):
    av_packet_free = _libs["avcodec"].get("av_packet_free", "cdecl")
    av_packet_free.argtypes = [POINTER(POINTER(AVPacket))]
    av_packet_free.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 488
if _libs["avcodec"].has("av_init_packet", "cdecl"):
    av_init_packet = _libs["avcodec"].get("av_init_packet", "cdecl")
    av_init_packet.argtypes = [POINTER(AVPacket)]
    av_init_packet.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 499
if _libs["avcodec"].has("av_new_packet", "cdecl"):
    av_new_packet = _libs["avcodec"].get("av_new_packet", "cdecl")
    av_new_packet.argtypes = [POINTER(AVPacket), c_int]
    av_new_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 507
if _libs["avcodec"].has("av_shrink_packet", "cdecl"):
    av_shrink_packet = _libs["avcodec"].get("av_shrink_packet", "cdecl")
    av_shrink_packet.argtypes = [POINTER(AVPacket), c_int]
    av_shrink_packet.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 515
if _libs["avcodec"].has("av_grow_packet", "cdecl"):
    av_grow_packet = _libs["avcodec"].get("av_grow_packet", "cdecl")
    av_grow_packet.argtypes = [POINTER(AVPacket), c_int]
    av_grow_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 530
if _libs["avcodec"].has("av_packet_from_data", "cdecl"):
    av_packet_from_data = _libs["avcodec"].get("av_packet_from_data", "cdecl")
    av_packet_from_data.argtypes = [POINTER(AVPacket), POINTER(c_uint8), c_int]
    av_packet_from_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 540
if _libs["avcodec"].has("av_dup_packet", "cdecl"):
    av_dup_packet = _libs["avcodec"].get("av_dup_packet", "cdecl")
    av_dup_packet.argtypes = [POINTER(AVPacket)]
    av_dup_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 549
if _libs["avcodec"].has("av_copy_packet", "cdecl"):
    av_copy_packet = _libs["avcodec"].get("av_copy_packet", "cdecl")
    av_copy_packet.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_copy_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 559
if _libs["avcodec"].has("av_copy_packet_side_data", "cdecl"):
    av_copy_packet_side_data = _libs["avcodec"].get("av_copy_packet_side_data", "cdecl")
    av_copy_packet_side_data.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_copy_packet_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 569
if _libs["avcodec"].has("av_free_packet", "cdecl"):
    av_free_packet = _libs["avcodec"].get("av_free_packet", "cdecl")
    av_free_packet.argtypes = [POINTER(AVPacket)]
    av_free_packet.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 579
if _libs["avcodec"].has("av_packet_new_side_data", "cdecl"):
    av_packet_new_side_data = _libs["avcodec"].get("av_packet_new_side_data", "cdecl")
    av_packet_new_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_int]
    av_packet_new_side_data.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/packet.h: 599
if _libs["avcodec"].has("av_packet_add_side_data", "cdecl"):
    av_packet_add_side_data = _libs["avcodec"].get("av_packet_add_side_data", "cdecl")
    av_packet_add_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(c_uint8), c_size_t]
    av_packet_add_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 610
if _libs["avcodec"].has("av_packet_shrink_side_data", "cdecl"):
    av_packet_shrink_side_data = _libs["avcodec"].get("av_packet_shrink_side_data", "cdecl")
    av_packet_shrink_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_int]
    av_packet_shrink_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 626
if _libs["avcodec"].has("av_packet_get_side_data", "cdecl"):
    av_packet_get_side_data = _libs["avcodec"].get("av_packet_get_side_data", "cdecl")
    av_packet_get_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(c_int)]
    av_packet_get_side_data.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/packet.h: 635
if _libs["avcodec"].has("av_packet_merge_side_data", "cdecl"):
    av_packet_merge_side_data = _libs["avcodec"].get("av_packet_merge_side_data", "cdecl")
    av_packet_merge_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_merge_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 638
if _libs["avcodec"].has("av_packet_split_side_data", "cdecl"):
    av_packet_split_side_data = _libs["avcodec"].get("av_packet_split_side_data", "cdecl")
    av_packet_split_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_split_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 641
if _libs["avcodec"].has("av_packet_side_data_name", "cdecl"):
    av_packet_side_data_name = _libs["avcodec"].get("av_packet_side_data_name", "cdecl")
    av_packet_side_data_name.argtypes = [enum_AVPacketSideDataType]
    av_packet_side_data_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/packet.h: 651
if _libs["avcodec"].has("av_packet_pack_dictionary", "cdecl"):
    av_packet_pack_dictionary = _libs["avcodec"].get("av_packet_pack_dictionary", "cdecl")
    av_packet_pack_dictionary.argtypes = [POINTER(AVDictionary), POINTER(c_int)]
    av_packet_pack_dictionary.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/packet.h: 664
if _libs["avcodec"].has("av_packet_unpack_dictionary", "cdecl"):
    av_packet_unpack_dictionary = _libs["avcodec"].get("av_packet_unpack_dictionary", "cdecl")
    av_packet_unpack_dictionary.argtypes = [POINTER(c_uint8), c_int, POINTER(POINTER(AVDictionary))]
    av_packet_unpack_dictionary.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 676
if _libs["avcodec"].has("av_packet_free_side_data", "cdecl"):
    av_packet_free_side_data = _libs["avcodec"].get("av_packet_free_side_data", "cdecl")
    av_packet_free_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_free_side_data.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 695
if _libs["avcodec"].has("av_packet_ref", "cdecl"):
    av_packet_ref = _libs["avcodec"].get("av_packet_ref", "cdecl")
    av_packet_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_ref.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 705
if _libs["avcodec"].has("av_packet_unref", "cdecl"):
    av_packet_unref = _libs["avcodec"].get("av_packet_unref", "cdecl")
    av_packet_unref.argtypes = [POINTER(AVPacket)]
    av_packet_unref.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 715
if _libs["avcodec"].has("av_packet_move_ref", "cdecl"):
    av_packet_move_ref = _libs["avcodec"].get("av_packet_move_ref", "cdecl")
    av_packet_move_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_move_ref.restype = None

# /home/josiah/ctypesgen_test/av/packet.h: 728
if _libs["avcodec"].has("av_packet_copy_props", "cdecl"):
    av_packet_copy_props = _libs["avcodec"].get("av_packet_copy_props", "cdecl")
    av_packet_copy_props.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_copy_props.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 744
if _libs["avcodec"].has("av_packet_make_refcounted", "cdecl"):
    av_packet_make_refcounted = _libs["avcodec"].get("av_packet_make_refcounted", "cdecl")
    av_packet_make_refcounted.argtypes = [POINTER(AVPacket)]
    av_packet_make_refcounted.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 755
if _libs["avcodec"].has("av_packet_make_writable", "cdecl"):
    av_packet_make_writable = _libs["avcodec"].get("av_packet_make_writable", "cdecl")
    av_packet_make_writable.argtypes = [POINTER(AVPacket)]
    av_packet_make_writable.restype = c_int

# /home/josiah/ctypesgen_test/av/packet.h: 768
if _libs["avcodec"].has("av_packet_rescale_ts", "cdecl"):
    av_packet_rescale_ts = _libs["avcodec"].get("av_packet_rescale_ts", "cdecl")
    av_packet_rescale_ts.argtypes = [POINTER(AVPacket), AVRational, AVRational]
    av_packet_rescale_ts.restype = None

# /home/josiah/ctypesgen_test/av/bsf.h: 37
class struct_AVBSFInternal(Structure):
    pass

AVBSFInternal = struct_AVBSFInternal# /home/josiah/ctypesgen_test/av/bsf.h: 37

# /home/josiah/ctypesgen_test/av/bsf.h: 98
class struct_AVBitStreamFilter(Structure):
    pass

# /home/josiah/ctypesgen_test/av/bsf.h: 96
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

AVBSFContext = struct_AVBSFContext# /home/josiah/ctypesgen_test/av/bsf.h: 96

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

AVBitStreamFilter = struct_AVBitStreamFilter# /home/josiah/ctypesgen_test/av/bsf.h: 132

# /home/josiah/ctypesgen_test/av/bsf.h: 138
if _libs["avcodec"].has("av_bsf_get_by_name", "cdecl"):
    av_bsf_get_by_name = _libs["avcodec"].get("av_bsf_get_by_name", "cdecl")
    av_bsf_get_by_name.argtypes = [String]
    av_bsf_get_by_name.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/bsf.h: 149
if _libs["avcodec"].has("av_bsf_iterate", "cdecl"):
    av_bsf_iterate = _libs["avcodec"].get("av_bsf_iterate", "cdecl")
    av_bsf_iterate.argtypes = [POINTER(POINTER(None))]
    av_bsf_iterate.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/bsf.h: 163
if _libs["avcodec"].has("av_bsf_alloc", "cdecl"):
    av_bsf_alloc = _libs["avcodec"].get("av_bsf_alloc", "cdecl")
    av_bsf_alloc.argtypes = [POINTER(AVBitStreamFilter), POINTER(POINTER(AVBSFContext))]
    av_bsf_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 169
if _libs["avcodec"].has("av_bsf_init", "cdecl"):
    av_bsf_init = _libs["avcodec"].get("av_bsf_init", "cdecl")
    av_bsf_init.argtypes = [POINTER(AVBSFContext)]
    av_bsf_init.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 189
if _libs["avcodec"].has("av_bsf_send_packet", "cdecl"):
    av_bsf_send_packet = _libs["avcodec"].get("av_bsf_send_packet", "cdecl")
    av_bsf_send_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_send_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 215
if _libs["avcodec"].has("av_bsf_receive_packet", "cdecl"):
    av_bsf_receive_packet = _libs["avcodec"].get("av_bsf_receive_packet", "cdecl")
    av_bsf_receive_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_receive_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 220
if _libs["avcodec"].has("av_bsf_flush", "cdecl"):
    av_bsf_flush = _libs["avcodec"].get("av_bsf_flush", "cdecl")
    av_bsf_flush.argtypes = [POINTER(AVBSFContext)]
    av_bsf_flush.restype = None

# /home/josiah/ctypesgen_test/av/bsf.h: 226
if _libs["avcodec"].has("av_bsf_free", "cdecl"):
    av_bsf_free = _libs["avcodec"].get("av_bsf_free", "cdecl")
    av_bsf_free.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_free.restype = None

# /home/josiah/ctypesgen_test/av/bsf.h: 234
if _libs["avcodec"].has("av_bsf_get_class", "cdecl"):
    av_bsf_get_class = _libs["avcodec"].get("av_bsf_get_class", "cdecl")
    av_bsf_get_class.argtypes = []
    av_bsf_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/bsf.h: 240
class struct_AVBSFList(Structure):
    pass

AVBSFList = struct_AVBSFList# /home/josiah/ctypesgen_test/av/bsf.h: 240

# /home/josiah/ctypesgen_test/av/bsf.h: 249
if _libs["avcodec"].has("av_bsf_list_alloc", "cdecl"):
    av_bsf_list_alloc = _libs["avcodec"].get("av_bsf_list_alloc", "cdecl")
    av_bsf_list_alloc.argtypes = []
    av_bsf_list_alloc.restype = POINTER(AVBSFList)

# /home/josiah/ctypesgen_test/av/bsf.h: 256
if _libs["avcodec"].has("av_bsf_list_free", "cdecl"):
    av_bsf_list_free = _libs["avcodec"].get("av_bsf_list_free", "cdecl")
    av_bsf_list_free.argtypes = [POINTER(POINTER(AVBSFList))]
    av_bsf_list_free.restype = None

# /home/josiah/ctypesgen_test/av/bsf.h: 266
if _libs["avcodec"].has("av_bsf_list_append", "cdecl"):
    av_bsf_list_append = _libs["avcodec"].get("av_bsf_list_append", "cdecl")
    av_bsf_list_append.argtypes = [POINTER(AVBSFList), POINTER(AVBSFContext)]
    av_bsf_list_append.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 278
if _libs["avcodec"].has("av_bsf_list_append2", "cdecl"):
    av_bsf_list_append2 = _libs["avcodec"].get("av_bsf_list_append2", "cdecl")
    av_bsf_list_append2.argtypes = [POINTER(AVBSFList), String, POINTER(POINTER(AVDictionary))]
    av_bsf_list_append2.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 295
if _libs["avcodec"].has("av_bsf_list_finalize", "cdecl"):
    av_bsf_list_finalize = _libs["avcodec"].get("av_bsf_list_finalize", "cdecl")
    av_bsf_list_finalize.argtypes = [POINTER(POINTER(AVBSFList)), POINTER(POINTER(AVBSFContext))]
    av_bsf_list_finalize.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 310
if _libs["avcodec"].has("av_bsf_list_parse_str", "cdecl"):
    av_bsf_list_parse_str = _libs["avcodec"].get("av_bsf_list_parse_str", "cdecl")
    av_bsf_list_parse_str.argtypes = [String, POINTER(POINTER(AVBSFContext))]
    av_bsf_list_parse_str.restype = c_int

# /home/josiah/ctypesgen_test/av/bsf.h: 319
if _libs["avcodec"].has("av_bsf_get_null_filter", "cdecl"):
    av_bsf_get_null_filter = _libs["avcodec"].get("av_bsf_get_null_filter", "cdecl")
    av_bsf_get_null_filter.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_get_null_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/codec.h: 186
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

AVProfile = struct_AVProfile# /home/josiah/ctypesgen_test/av/codec.h: 186

# /home/josiah/ctypesgen_test/av/codec.h: 188
class struct_AVCodecDefault(Structure):
    pass

AVCodecDefault = struct_AVCodecDefault# /home/josiah/ctypesgen_test/av/codec.h: 188

# /home/josiah/ctypesgen_test/av/avcodec.h: 536
class struct_AVCodecContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2722
class struct_AVSubtitle(Structure):
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 197
class struct_AVCodec(Structure):
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 343
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

AVCodec = struct_AVCodec# /home/josiah/ctypesgen_test/av/codec.h: 349

# /home/josiah/ctypesgen_test/av/codec.h: 360
if _libs["avcodec"].has("av_codec_iterate", "cdecl"):
    av_codec_iterate = _libs["avcodec"].get("av_codec_iterate", "cdecl")
    av_codec_iterate.argtypes = [POINTER(POINTER(None))]
    av_codec_iterate.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/codec.h: 368
if _libs["avcodec"].has("avcodec_find_decoder", "cdecl"):
    avcodec_find_decoder = _libs["avcodec"].get("avcodec_find_decoder", "cdecl")
    avcodec_find_decoder.argtypes = [enum_AVCodecID]
    avcodec_find_decoder.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/codec.h: 376
if _libs["avcodec"].has("avcodec_find_decoder_by_name", "cdecl"):
    avcodec_find_decoder_by_name = _libs["avcodec"].get("avcodec_find_decoder_by_name", "cdecl")
    avcodec_find_decoder_by_name.argtypes = [String]
    avcodec_find_decoder_by_name.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/codec.h: 384
if _libs["avcodec"].has("avcodec_find_encoder", "cdecl"):
    avcodec_find_encoder = _libs["avcodec"].get("avcodec_find_encoder", "cdecl")
    avcodec_find_encoder.argtypes = [enum_AVCodecID]
    avcodec_find_encoder.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/codec.h: 392
if _libs["avcodec"].has("avcodec_find_encoder_by_name", "cdecl"):
    avcodec_find_encoder_by_name = _libs["avcodec"].get("avcodec_find_encoder_by_name", "cdecl")
    avcodec_find_encoder_by_name.argtypes = [String]
    avcodec_find_encoder_by_name.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/codec.h: 396
if _libs["avcodec"].has("av_codec_is_encoder", "cdecl"):
    av_codec_is_encoder = _libs["avcodec"].get("av_codec_is_encoder", "cdecl")
    av_codec_is_encoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_encoder.restype = c_int

# /home/josiah/ctypesgen_test/av/codec.h: 401
if _libs["avcodec"].has("av_codec_is_decoder", "cdecl"):
    av_codec_is_decoder = _libs["avcodec"].get("av_codec_is_decoder", "cdecl")
    av_codec_is_decoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_decoder.restype = c_int

enum_anon_28 = c_int# /home/josiah/ctypesgen_test/av/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_HW_DEVICE_CTX = 1# /home/josiah/ctypesgen_test/av/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_HW_FRAMES_CTX = 2# /home/josiah/ctypesgen_test/av/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_INTERNAL = 4# /home/josiah/ctypesgen_test/av/codec.h: 403

AV_CODEC_HW_CONFIG_METHOD_AD_HOC = 8# /home/josiah/ctypesgen_test/av/codec.h: 403

# /home/josiah/ctypesgen_test/av/codec.h: 465
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

AVCodecHWConfig = struct_AVCodecHWConfig# /home/josiah/ctypesgen_test/av/codec.h: 465

# /home/josiah/ctypesgen_test/av/codec.h: 474
if _libs["avcodec"].has("avcodec_get_hw_config", "cdecl"):
    avcodec_get_hw_config = _libs["avcodec"].get("avcodec_get_hw_config", "cdecl")
    avcodec_get_hw_config.argtypes = [POINTER(AVCodec), c_int]
    avcodec_get_hw_config.restype = POINTER(AVCodecHWConfig)

# /home/josiah/ctypesgen_test/av/codec_desc.h: 66
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

AVCodecDescriptor = struct_AVCodecDescriptor# /home/josiah/ctypesgen_test/av/codec_desc.h: 66

# /home/josiah/ctypesgen_test/av/codec_desc.h: 107
if _libs["avcodec"].has("avcodec_descriptor_get", "cdecl"):
    avcodec_descriptor_get = _libs["avcodec"].get("avcodec_descriptor_get", "cdecl")
    avcodec_descriptor_get.argtypes = [enum_AVCodecID]
    avcodec_descriptor_get.restype = POINTER(AVCodecDescriptor)

# /home/josiah/ctypesgen_test/av/codec_desc.h: 116
if _libs["avcodec"].has("avcodec_descriptor_next", "cdecl"):
    avcodec_descriptor_next = _libs["avcodec"].get("avcodec_descriptor_next", "cdecl")
    avcodec_descriptor_next.argtypes = [POINTER(AVCodecDescriptor)]
    avcodec_descriptor_next.restype = POINTER(AVCodecDescriptor)

# /home/josiah/ctypesgen_test/av/codec_desc.h: 122
if _libs["avcodec"].has("avcodec_descriptor_get_by_name", "cdecl"):
    avcodec_descriptor_get_by_name = _libs["avcodec"].get("avcodec_descriptor_get_by_name", "cdecl")
    avcodec_descriptor_get_by_name.argtypes = [String]
    avcodec_descriptor_get_by_name.restype = POINTER(AVCodecDescriptor)

enum_AVDiscard = c_int# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_NONE = (-16)# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_DEFAULT = 0# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_NONREF = 8# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_BIDIR = 16# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_NONINTRA = 24# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_NONKEY = 32# /home/josiah/ctypesgen_test/av/avcodec.h: 227

AVDISCARD_ALL = 48# /home/josiah/ctypesgen_test/av/avcodec.h: 227

enum_AVAudioServiceType = c_int# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_MAIN = 0# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_EFFECTS = 1# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_VISUALLY_IMPAIRED = 2# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_HEARING_IMPAIRED = 3# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_DIALOGUE = 4# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_COMMENTARY = 5# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_EMERGENCY = 6# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_VOICE_OVER = 7# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_KARAOKE = 8# /home/josiah/ctypesgen_test/av/avcodec.h: 239

AV_AUDIO_SERVICE_TYPE_NB = (AV_AUDIO_SERVICE_TYPE_KARAOKE + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 239

# /home/josiah/ctypesgen_test/av/avcodec.h: 260
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

RcOverride = struct_RcOverride# /home/josiah/ctypesgen_test/av/avcodec.h: 260

# /home/josiah/ctypesgen_test/av/avcodec.h: 446
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

AVPanScan = struct_AVPanScan# /home/josiah/ctypesgen_test/av/avcodec.h: 446

# /home/josiah/ctypesgen_test/av/avcodec.h: 496
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

AVCPBProperties = struct_AVCPBProperties# /home/josiah/ctypesgen_test/av/avcodec.h: 496

# /home/josiah/ctypesgen_test/av/avcodec.h: 509
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

AVProducerReferenceTime = struct_AVProducerReferenceTime# /home/josiah/ctypesgen_test/av/avcodec.h: 509

# /home/josiah/ctypesgen_test/av/avcodec.h: 521
class struct_AVCodecInternal(Structure):
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2438
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

AVCodecContext = struct_AVCodecContext# /home/josiah/ctypesgen_test/av/avcodec.h: 2385

# /home/josiah/ctypesgen_test/av/avcodec.h: 2393
if _libs["avcodec"].has("av_codec_get_pkt_timebase", "cdecl"):
    av_codec_get_pkt_timebase = _libs["avcodec"].get("av_codec_get_pkt_timebase", "cdecl")
    av_codec_get_pkt_timebase.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_pkt_timebase.restype = AVRational

# /home/josiah/ctypesgen_test/av/avcodec.h: 2395
if _libs["avcodec"].has("av_codec_set_pkt_timebase", "cdecl"):
    av_codec_set_pkt_timebase = _libs["avcodec"].get("av_codec_set_pkt_timebase", "cdecl")
    av_codec_set_pkt_timebase.argtypes = [POINTER(AVCodecContext), AVRational]
    av_codec_set_pkt_timebase.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2398
if _libs["avcodec"].has("av_codec_get_codec_descriptor", "cdecl"):
    av_codec_get_codec_descriptor = _libs["avcodec"].get("av_codec_get_codec_descriptor", "cdecl")
    av_codec_get_codec_descriptor.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_codec_descriptor.restype = POINTER(AVCodecDescriptor)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2400
if _libs["avcodec"].has("av_codec_set_codec_descriptor", "cdecl"):
    av_codec_set_codec_descriptor = _libs["avcodec"].get("av_codec_set_codec_descriptor", "cdecl")
    av_codec_set_codec_descriptor.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecDescriptor)]
    av_codec_set_codec_descriptor.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2403
if _libs["avcodec"].has("av_codec_get_codec_properties", "cdecl"):
    av_codec_get_codec_properties = _libs["avcodec"].get("av_codec_get_codec_properties", "cdecl")
    av_codec_get_codec_properties.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_codec_properties.restype = c_uint

# /home/josiah/ctypesgen_test/av/avcodec.h: 2406
if _libs["avcodec"].has("av_codec_get_lowres", "cdecl"):
    av_codec_get_lowres = _libs["avcodec"].get("av_codec_get_lowres", "cdecl")
    av_codec_get_lowres.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_lowres.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2408
if _libs["avcodec"].has("av_codec_set_lowres", "cdecl"):
    av_codec_set_lowres = _libs["avcodec"].get("av_codec_set_lowres", "cdecl")
    av_codec_set_lowres.argtypes = [POINTER(AVCodecContext), c_int]
    av_codec_set_lowres.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2411
if _libs["avcodec"].has("av_codec_get_seek_preroll", "cdecl"):
    av_codec_get_seek_preroll = _libs["avcodec"].get("av_codec_get_seek_preroll", "cdecl")
    av_codec_get_seek_preroll.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_seek_preroll.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2413
if _libs["avcodec"].has("av_codec_set_seek_preroll", "cdecl"):
    av_codec_set_seek_preroll = _libs["avcodec"].get("av_codec_set_seek_preroll", "cdecl")
    av_codec_set_seek_preroll.argtypes = [POINTER(AVCodecContext), c_int]
    av_codec_set_seek_preroll.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2416
if _libs["avcodec"].has("av_codec_get_chroma_intra_matrix", "cdecl"):
    av_codec_get_chroma_intra_matrix = _libs["avcodec"].get("av_codec_get_chroma_intra_matrix", "cdecl")
    av_codec_get_chroma_intra_matrix.argtypes = [POINTER(AVCodecContext)]
    av_codec_get_chroma_intra_matrix.restype = POINTER(c_uint16)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2418
if _libs["avcodec"].has("av_codec_set_chroma_intra_matrix", "cdecl"):
    av_codec_set_chroma_intra_matrix = _libs["avcodec"].get("av_codec_set_chroma_intra_matrix", "cdecl")
    av_codec_set_chroma_intra_matrix.argtypes = [POINTER(AVCodecContext), POINTER(c_uint16)]
    av_codec_set_chroma_intra_matrix.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2425
if _libs["avcodec"].has("av_codec_get_max_lowres", "cdecl"):
    av_codec_get_max_lowres = _libs["avcodec"].get("av_codec_get_max_lowres", "cdecl")
    av_codec_get_max_lowres.argtypes = [POINTER(AVCodec)]
    av_codec_get_max_lowres.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2428
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

AVHWAccel = struct_AVHWAccel# /home/josiah/ctypesgen_test/av/avcodec.h: 2598

# /home/josiah/ctypesgen_test/av/avcodec.h: 2660
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

AVPicture = struct_AVPicture# /home/josiah/ctypesgen_test/av/avcodec.h: 2660

enum_AVSubtitleType = c_int# /home/josiah/ctypesgen_test/av/avcodec.h: 2667

SUBTITLE_NONE = 0# /home/josiah/ctypesgen_test/av/avcodec.h: 2667

SUBTITLE_BITMAP = (SUBTITLE_NONE + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 2667

SUBTITLE_TEXT = (SUBTITLE_BITMAP + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 2667

SUBTITLE_ASS = (SUBTITLE_TEXT + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 2667

# /home/josiah/ctypesgen_test/av/avcodec.h: 2720
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

AVSubtitleRect = struct_AVSubtitleRect# /home/josiah/ctypesgen_test/av/avcodec.h: 2720

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

AVSubtitle = struct_AVSubtitle# /home/josiah/ctypesgen_test/av/avcodec.h: 2729

# /home/josiah/ctypesgen_test/av/avcodec.h: 2738
if _libs["avcodec"].has("av_codec_next", "cdecl"):
    av_codec_next = _libs["avcodec"].get("av_codec_next", "cdecl")
    av_codec_next.argtypes = [POINTER(AVCodec)]
    av_codec_next.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2744
if _libs["avcodec"].has("avcodec_version", "cdecl"):
    avcodec_version = _libs["avcodec"].get("avcodec_version", "cdecl")
    avcodec_version.argtypes = []
    avcodec_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/avcodec.h: 2749
if _libs["avcodec"].has("avcodec_configuration", "cdecl"):
    avcodec_configuration = _libs["avcodec"].get("avcodec_configuration", "cdecl")
    avcodec_configuration.argtypes = []
    avcodec_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avcodec.h: 2754
if _libs["avcodec"].has("avcodec_license", "cdecl"):
    avcodec_license = _libs["avcodec"].get("avcodec_license", "cdecl")
    avcodec_license.argtypes = []
    avcodec_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avcodec.h: 2761
if _libs["avcodec"].has("avcodec_register", "cdecl"):
    avcodec_register = _libs["avcodec"].get("avcodec_register", "cdecl")
    avcodec_register.argtypes = [POINTER(AVCodec)]
    avcodec_register.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2767
if _libs["avcodec"].has("avcodec_register_all", "cdecl"):
    avcodec_register_all = _libs["avcodec"].get("avcodec_register_all", "cdecl")
    avcodec_register_all.argtypes = []
    avcodec_register_all.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2783
if _libs["avcodec"].has("avcodec_alloc_context3", "cdecl"):
    avcodec_alloc_context3 = _libs["avcodec"].get("avcodec_alloc_context3", "cdecl")
    avcodec_alloc_context3.argtypes = [POINTER(AVCodec)]
    avcodec_alloc_context3.restype = POINTER(AVCodecContext)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2789
if _libs["avcodec"].has("avcodec_free_context", "cdecl"):
    avcodec_free_context = _libs["avcodec"].get("avcodec_free_context", "cdecl")
    avcodec_free_context.argtypes = [POINTER(POINTER(AVCodecContext))]
    avcodec_free_context.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2797
if _libs["avcodec"].has("avcodec_get_context_defaults3", "cdecl"):
    avcodec_get_context_defaults3 = _libs["avcodec"].get("avcodec_get_context_defaults3", "cdecl")
    avcodec_get_context_defaults3.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec)]
    avcodec_get_context_defaults3.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2806
if _libs["avcodec"].has("avcodec_get_class", "cdecl"):
    avcodec_get_class = _libs["avcodec"].get("avcodec_get_class", "cdecl")
    avcodec_get_class.argtypes = []
    avcodec_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2813
if _libs["avcodec"].has("avcodec_get_frame_class", "cdecl"):
    avcodec_get_frame_class = _libs["avcodec"].get("avcodec_get_frame_class", "cdecl")
    avcodec_get_frame_class.argtypes = []
    avcodec_get_frame_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2822
if _libs["avcodec"].has("avcodec_get_subtitle_rect_class", "cdecl"):
    avcodec_get_subtitle_rect_class = _libs["avcodec"].get("avcodec_get_subtitle_rect_class", "cdecl")
    avcodec_get_subtitle_rect_class.argtypes = []
    avcodec_get_subtitle_rect_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/avcodec.h: 2843
if _libs["avcodec"].has("avcodec_copy_context", "cdecl"):
    avcodec_copy_context = _libs["avcodec"].get("avcodec_copy_context", "cdecl")
    avcodec_copy_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecContext)]
    avcodec_copy_context.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2853
if _libs["avcodec"].has("avcodec_parameters_from_context", "cdecl"):
    avcodec_parameters_from_context = _libs["avcodec"].get("avcodec_parameters_from_context", "cdecl")
    avcodec_parameters_from_context.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecContext)]
    avcodec_parameters_from_context.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2864
if _libs["avcodec"].has("avcodec_parameters_to_context", "cdecl"):
    avcodec_parameters_to_context = _libs["avcodec"].get("avcodec_parameters_to_context", "cdecl")
    avcodec_parameters_to_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecParameters)]
    avcodec_parameters_to_context.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2904
if _libs["avcodec"].has("avcodec_open2", "cdecl"):
    avcodec_open2 = _libs["avcodec"].get("avcodec_open2", "cdecl")
    avcodec_open2.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec), POINTER(POINTER(AVDictionary))]
    avcodec_open2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2919
if _libs["avcodec"].has("avcodec_close", "cdecl"):
    avcodec_close = _libs["avcodec"].get("avcodec_close", "cdecl")
    avcodec_close.argtypes = [POINTER(AVCodecContext)]
    avcodec_close.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2926
if _libs["avcodec"].has("avsubtitle_free", "cdecl"):
    avsubtitle_free = _libs["avcodec"].get("avsubtitle_free", "cdecl")
    avsubtitle_free.argtypes = [POINTER(AVSubtitle)]
    avsubtitle_free.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2942
if _libs["avcodec"].has("avcodec_default_get_buffer2", "cdecl"):
    avcodec_default_get_buffer2 = _libs["avcodec"].get("avcodec_default_get_buffer2", "cdecl")
    avcodec_default_get_buffer2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), c_int]
    avcodec_default_get_buffer2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2949
if _libs["avcodec"].has("avcodec_default_get_encode_buffer", "cdecl"):
    avcodec_default_get_encode_buffer = _libs["avcodec"].get("avcodec_default_get_encode_buffer", "cdecl")
    avcodec_default_get_encode_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), c_int]
    avcodec_default_get_encode_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2958
if _libs["avcodec"].has("avcodec_align_dimensions", "cdecl"):
    avcodec_align_dimensions = _libs["avcodec"].get("avcodec_align_dimensions", "cdecl")
    avcodec_align_dimensions.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int)]
    avcodec_align_dimensions.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2967
if _libs["avcodec"].has("avcodec_align_dimensions2", "cdecl"):
    avcodec_align_dimensions2 = _libs["avcodec"].get("avcodec_align_dimensions2", "cdecl")
    avcodec_align_dimensions2.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int), c_int * int(8)]
    avcodec_align_dimensions2.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 2979
if _libs["avcodec"].has("avcodec_enum_to_chroma_pos", "cdecl"):
    avcodec_enum_to_chroma_pos = _libs["avcodec"].get("avcodec_enum_to_chroma_pos", "cdecl")
    avcodec_enum_to_chroma_pos.argtypes = [POINTER(c_int), POINTER(c_int), enum_AVChromaLocation]
    avcodec_enum_to_chroma_pos.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 2990
if _libs["avcodec"].has("avcodec_chroma_pos_to_enum", "cdecl"):
    avcodec_chroma_pos_to_enum = _libs["avcodec"].get("avcodec_chroma_pos_to_enum", "cdecl")
    avcodec_chroma_pos_to_enum.argtypes = [c_int, c_int]
    avcodec_chroma_pos_to_enum.restype = enum_AVChromaLocation

# /home/josiah/ctypesgen_test/av/avcodec.h: 3047
if _libs["avcodec"].has("avcodec_decode_audio4", "cdecl"):
    avcodec_decode_audio4 = _libs["avcodec"].get("avcodec_decode_audio4", "cdecl")
    avcodec_decode_audio4.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_audio4.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3096
if _libs["avcodec"].has("avcodec_decode_video2", "cdecl"):
    avcodec_decode_video2 = _libs["avcodec"].get("avcodec_decode_video2", "cdecl")
    avcodec_decode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_video2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3128
if _libs["avcodec"].has("avcodec_decode_subtitle2", "cdecl"):
    avcodec_decode_subtitle2 = _libs["avcodec"].get("avcodec_decode_subtitle2", "cdecl")
    avcodec_decode_subtitle2.argtypes = [POINTER(AVCodecContext), POINTER(AVSubtitle), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_subtitle2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3182
if _libs["avcodec"].has("avcodec_send_packet", "cdecl"):
    avcodec_send_packet = _libs["avcodec"].get("avcodec_send_packet", "cdecl")
    avcodec_send_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_send_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3205
if _libs["avcodec"].has("avcodec_receive_frame", "cdecl"):
    avcodec_receive_frame = _libs["avcodec"].get("avcodec_receive_frame", "cdecl")
    avcodec_receive_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_receive_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3242
if _libs["avcodec"].has("avcodec_send_frame", "cdecl"):
    avcodec_send_frame = _libs["avcodec"].get("avcodec_send_frame", "cdecl")
    avcodec_send_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_send_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3259
if _libs["avcodec"].has("avcodec_receive_packet", "cdecl"):
    avcodec_receive_packet = _libs["avcodec"].get("avcodec_receive_packet", "cdecl")
    avcodec_receive_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_receive_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3358
if _libs["avcodec"].has("avcodec_get_hw_frames_parameters", "cdecl"):
    avcodec_get_hw_frames_parameters = _libs["avcodec"].get("avcodec_get_hw_frames_parameters", "cdecl")
    avcodec_get_hw_frames_parameters.argtypes = [POINTER(AVCodecContext), POINTER(AVBufferRef), enum_AVPixelFormat, POINTER(POINTER(AVBufferRef))]
    avcodec_get_hw_frames_parameters.restype = c_int

enum_AVPictureStructure = c_int# /home/josiah/ctypesgen_test/av/avcodec.h: 3370

AV_PICTURE_STRUCTURE_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/avcodec.h: 3370

AV_PICTURE_STRUCTURE_TOP_FIELD = (AV_PICTURE_STRUCTURE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 3370

AV_PICTURE_STRUCTURE_BOTTOM_FIELD = (AV_PICTURE_STRUCTURE_TOP_FIELD + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 3370

AV_PICTURE_STRUCTURE_FRAME = (AV_PICTURE_STRUCTURE_BOTTOM_FIELD + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 3370

# /home/josiah/ctypesgen_test/av/avcodec.h: 3544
class struct_AVCodecParser(Structure):
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3542
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

AVCodecParserContext = struct_AVCodecParserContext# /home/josiah/ctypesgen_test/av/avcodec.h: 3542

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

AVCodecParser = struct_AVCodecParser# /home/josiah/ctypesgen_test/av/avcodec.h: 3560

# /home/josiah/ctypesgen_test/av/avcodec.h: 3571
if _libs["avcodec"].has("av_parser_iterate", "cdecl"):
    av_parser_iterate = _libs["avcodec"].get("av_parser_iterate", "cdecl")
    av_parser_iterate.argtypes = [POINTER(POINTER(None))]
    av_parser_iterate.restype = POINTER(AVCodecParser)

# /home/josiah/ctypesgen_test/av/avcodec.h: 3575
if _libs["avcodec"].has("av_parser_next", "cdecl"):
    av_parser_next = _libs["avcodec"].get("av_parser_next", "cdecl")
    av_parser_next.argtypes = [POINTER(AVCodecParser)]
    av_parser_next.restype = POINTER(AVCodecParser)

# /home/josiah/ctypesgen_test/av/avcodec.h: 3578
if _libs["avcodec"].has("av_register_codec_parser", "cdecl"):
    av_register_codec_parser = _libs["avcodec"].get("av_register_codec_parser", "cdecl")
    av_register_codec_parser.argtypes = [POINTER(AVCodecParser)]
    av_register_codec_parser.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3580
if _libs["avcodec"].has("av_parser_init", "cdecl"):
    av_parser_init = _libs["avcodec"].get("av_parser_init", "cdecl")
    av_parser_init.argtypes = [c_int]
    av_parser_init.restype = POINTER(AVCodecParserContext)

# /home/josiah/ctypesgen_test/av/avcodec.h: 3613
if _libs["avcodec"].has("av_parser_parse2", "cdecl"):
    av_parser_parse2 = _libs["avcodec"].get("av_parser_parse2", "cdecl")
    av_parser_parse2.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int64, c_int64, c_int64]
    av_parser_parse2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3627
if _libs["avcodec"].has("av_parser_change", "cdecl"):
    av_parser_change = _libs["avcodec"].get("av_parser_change", "cdecl")
    av_parser_change.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int]
    av_parser_change.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3632
if _libs["avcodec"].has("av_parser_close", "cdecl"):
    av_parser_close = _libs["avcodec"].get("av_parser_close", "cdecl")
    av_parser_close.argtypes = [POINTER(AVCodecParserContext)]
    av_parser_close.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3688
if _libs["avcodec"].has("avcodec_encode_audio2", "cdecl"):
    avcodec_encode_audio2 = _libs["avcodec"].get("avcodec_encode_audio2", "cdecl")
    avcodec_encode_audio2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
    avcodec_encode_audio2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3729
if _libs["avcodec"].has("avcodec_encode_video2", "cdecl"):
    avcodec_encode_video2 = _libs["avcodec"].get("avcodec_encode_video2", "cdecl")
    avcodec_encode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
    avcodec_encode_video2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3733
if _libs["avcodec"].has("avcodec_encode_subtitle", "cdecl"):
    avcodec_encode_subtitle = _libs["avcodec"].get("avcodec_encode_subtitle", "cdecl")
    avcodec_encode_subtitle.argtypes = [POINTER(AVCodecContext), POINTER(c_uint8), c_int, POINTER(AVSubtitle)]
    avcodec_encode_subtitle.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3751
if _libs["avcodec"].has("avpicture_alloc", "cdecl"):
    avpicture_alloc = _libs["avcodec"].get("avpicture_alloc", "cdecl")
    avpicture_alloc.argtypes = [POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    avpicture_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3757
if _libs["avcodec"].has("avpicture_free", "cdecl"):
    avpicture_free = _libs["avcodec"].get("avpicture_free", "cdecl")
    avpicture_free.argtypes = [POINTER(AVPicture)]
    avpicture_free.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3763
if _libs["avcodec"].has("avpicture_fill", "cdecl"):
    avpicture_fill = _libs["avcodec"].get("avpicture_fill", "cdecl")
    avpicture_fill.argtypes = [POINTER(AVPicture), POINTER(c_uint8), enum_AVPixelFormat, c_int, c_int]
    avpicture_fill.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3770
if _libs["avcodec"].has("avpicture_layout", "cdecl"):
    avpicture_layout = _libs["avcodec"].get("avpicture_layout", "cdecl")
    avpicture_layout.argtypes = [POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int, POINTER(c_ubyte), c_int]
    avpicture_layout.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3778
if _libs["avcodec"].has("avpicture_get_size", "cdecl"):
    avpicture_get_size = _libs["avcodec"].get("avpicture_get_size", "cdecl")
    avpicture_get_size.argtypes = [enum_AVPixelFormat, c_int, c_int]
    avpicture_get_size.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3784
if _libs["avcodec"].has("av_picture_copy", "cdecl"):
    av_picture_copy = _libs["avcodec"].get("av_picture_copy", "cdecl")
    av_picture_copy.argtypes = [POINTER(AVPicture), POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    av_picture_copy.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3791
if _libs["avcodec"].has("av_picture_crop", "cdecl"):
    av_picture_crop = _libs["avcodec"].get("av_picture_crop", "cdecl")
    av_picture_crop.argtypes = [POINTER(AVPicture), POINTER(AVPicture), enum_AVPixelFormat, c_int, c_int]
    av_picture_crop.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3798
if _libs["avcodec"].has("av_picture_pad", "cdecl"):
    av_picture_pad = _libs["avcodec"].get("av_picture_pad", "cdecl")
    av_picture_pad.argtypes = [POINTER(AVPicture), POINTER(AVPicture), c_int, c_int, enum_AVPixelFormat, c_int, c_int, c_int, c_int, POINTER(c_int)]
    av_picture_pad.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3828
if _libs["avcodec"].has("avcodec_get_chroma_sub_sample", "cdecl"):
    avcodec_get_chroma_sub_sample = _libs["avcodec"].get("avcodec_get_chroma_sub_sample", "cdecl")
    avcodec_get_chroma_sub_sample.argtypes = [enum_AVPixelFormat, POINTER(c_int), POINTER(c_int)]
    avcodec_get_chroma_sub_sample.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3836
if _libs["avcodec"].has("avcodec_pix_fmt_to_codec_tag", "cdecl"):
    avcodec_pix_fmt_to_codec_tag = _libs["avcodec"].get("avcodec_pix_fmt_to_codec_tag", "cdecl")
    avcodec_pix_fmt_to_codec_tag.argtypes = [enum_AVPixelFormat]
    avcodec_pix_fmt_to_codec_tag.restype = c_uint

# /home/josiah/ctypesgen_test/av/avcodec.h: 3855
if _libs["avcodec"].has("avcodec_find_best_pix_fmt_of_list", "cdecl"):
    avcodec_find_best_pix_fmt_of_list = _libs["avcodec"].get("avcodec_find_best_pix_fmt_of_list", "cdecl")
    avcodec_find_best_pix_fmt_of_list.argtypes = [POINTER(enum_AVPixelFormat), enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt_of_list.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/avcodec.h: 3864
if _libs["avcodec"].has("avcodec_get_pix_fmt_loss", "cdecl"):
    avcodec_get_pix_fmt_loss = _libs["avcodec"].get("avcodec_get_pix_fmt_loss", "cdecl")
    avcodec_get_pix_fmt_loss.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, c_int]
    avcodec_get_pix_fmt_loss.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3870
if _libs["avcodec"].has("avcodec_find_best_pix_fmt_of_2", "cdecl"):
    avcodec_find_best_pix_fmt_of_2 = _libs["avcodec"].get("avcodec_find_best_pix_fmt_of_2", "cdecl")
    avcodec_find_best_pix_fmt_of_2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt_of_2.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/avcodec.h: 3874
if _libs["avcodec"].has("avcodec_find_best_pix_fmt2", "cdecl"):
    avcodec_find_best_pix_fmt2 = _libs["avcodec"].get("avcodec_find_best_pix_fmt2", "cdecl")
    avcodec_find_best_pix_fmt2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt2.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/avcodec.h: 3878
if _libs["avcodec"].has("avcodec_default_get_format", "cdecl"):
    avcodec_default_get_format = _libs["avcodec"].get("avcodec_default_get_format", "cdecl")
    avcodec_default_get_format.argtypes = [POINTER(struct_AVCodecContext), POINTER(enum_AVPixelFormat)]
    avcodec_default_get_format.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/avcodec.h: 3897
if _libs["avcodec"].has("av_get_codec_tag_string", "cdecl"):
    av_get_codec_tag_string = _libs["avcodec"].get("av_get_codec_tag_string", "cdecl")
    av_get_codec_tag_string.argtypes = [String, c_size_t, c_uint]
    av_get_codec_tag_string.restype = c_size_t

# /home/josiah/ctypesgen_test/av/avcodec.h: 3900
if _libs["avcodec"].has("avcodec_string", "cdecl"):
    avcodec_string = _libs["avcodec"].get("avcodec_string", "cdecl")
    avcodec_string.argtypes = [String, c_int, POINTER(AVCodecContext), c_int]
    avcodec_string.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3909
if _libs["avcodec"].has("av_get_profile_name", "cdecl"):
    av_get_profile_name = _libs["avcodec"].get("av_get_profile_name", "cdecl")
    av_get_profile_name.argtypes = [POINTER(AVCodec), c_int]
    av_get_profile_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avcodec.h: 3922
if _libs["avcodec"].has("avcodec_profile_name", "cdecl"):
    avcodec_profile_name = _libs["avcodec"].get("avcodec_profile_name", "cdecl")
    avcodec_profile_name.argtypes = [enum_AVCodecID, c_int]
    avcodec_profile_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avcodec.h: 3924
if _libs["avcodec"].has("avcodec_default_execute", "cdecl"):
    avcodec_default_execute = _libs["avcodec"].get("avcodec_default_execute", "cdecl")
    avcodec_default_execute.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None)), POINTER(None), POINTER(c_int), c_int, c_int]
    avcodec_default_execute.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3925
if _libs["avcodec"].has("avcodec_default_execute2", "cdecl"):
    avcodec_default_execute2 = _libs["avcodec"].get("avcodec_default_execute2", "cdecl")
    avcodec_default_execute2.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None), c_int, c_int), POINTER(None), POINTER(c_int), c_int]
    avcodec_default_execute2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3951
if _libs["avcodec"].has("avcodec_fill_audio_frame", "cdecl"):
    avcodec_fill_audio_frame = _libs["avcodec"].get("avcodec_fill_audio_frame", "cdecl")
    avcodec_fill_audio_frame.argtypes = [POINTER(AVFrame), c_int, enum_AVSampleFormat, POINTER(c_uint8), c_int, c_int]
    avcodec_fill_audio_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3972
if _libs["avcodec"].has("avcodec_flush_buffers", "cdecl"):
    avcodec_flush_buffers = _libs["avcodec"].get("avcodec_flush_buffers", "cdecl")
    avcodec_flush_buffers.argtypes = [POINTER(AVCodecContext)]
    avcodec_flush_buffers.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 3980
if _libs["avcodec"].has("av_get_bits_per_sample", "cdecl"):
    av_get_bits_per_sample = _libs["avcodec"].get("av_get_bits_per_sample", "cdecl")
    av_get_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_bits_per_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 3988
if _libs["avcodec"].has("av_get_pcm_codec", "cdecl"):
    av_get_pcm_codec = _libs["avcodec"].get("av_get_pcm_codec", "cdecl")
    av_get_pcm_codec.argtypes = [enum_AVSampleFormat, c_int]
    av_get_pcm_codec.restype = enum_AVCodecID

# /home/josiah/ctypesgen_test/av/avcodec.h: 3998
if _libs["avcodec"].has("av_get_exact_bits_per_sample", "cdecl"):
    av_get_exact_bits_per_sample = _libs["avcodec"].get("av_get_exact_bits_per_sample", "cdecl")
    av_get_exact_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_exact_bits_per_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4008
if _libs["avcodec"].has("av_get_audio_frame_duration", "cdecl"):
    av_get_audio_frame_duration = _libs["avcodec"].get("av_get_audio_frame_duration", "cdecl")
    av_get_audio_frame_duration.argtypes = [POINTER(AVCodecContext), c_int]
    av_get_audio_frame_duration.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4014
if _libs["avcodec"].has("av_get_audio_frame_duration2", "cdecl"):
    av_get_audio_frame_duration2 = _libs["avcodec"].get("av_get_audio_frame_duration2", "cdecl")
    av_get_audio_frame_duration2.argtypes = [POINTER(AVCodecParameters), c_int]
    av_get_audio_frame_duration2.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4017
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

AVBitStreamFilterContext = struct_AVBitStreamFilterContext# /home/josiah/ctypesgen_test/av/avcodec.h: 4027

# /home/josiah/ctypesgen_test/av/avcodec.h: 4034
if _libs["avcodec"].has("av_register_bitstream_filter", "cdecl"):
    av_register_bitstream_filter = _libs["avcodec"].get("av_register_bitstream_filter", "cdecl")
    av_register_bitstream_filter.argtypes = [POINTER(AVBitStreamFilter)]
    av_register_bitstream_filter.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 4041
if _libs["avcodec"].has("av_bitstream_filter_init", "cdecl"):
    av_bitstream_filter_init = _libs["avcodec"].get("av_bitstream_filter_init", "cdecl")
    av_bitstream_filter_init.argtypes = [String]
    av_bitstream_filter_init.restype = POINTER(AVBitStreamFilterContext)

# /home/josiah/ctypesgen_test/av/avcodec.h: 4048
if _libs["avcodec"].has("av_bitstream_filter_filter", "cdecl"):
    av_bitstream_filter_filter = _libs["avcodec"].get("av_bitstream_filter_filter", "cdecl")
    av_bitstream_filter_filter.argtypes = [POINTER(AVBitStreamFilterContext), POINTER(AVCodecContext), String, POINTER(POINTER(c_uint8)), POINTER(c_int), POINTER(c_uint8), c_int, c_int]
    av_bitstream_filter_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4058
if _libs["avcodec"].has("av_bitstream_filter_close", "cdecl"):
    av_bitstream_filter_close = _libs["avcodec"].get("av_bitstream_filter_close", "cdecl")
    av_bitstream_filter_close.argtypes = [POINTER(AVBitStreamFilterContext)]
    av_bitstream_filter_close.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 4065
if _libs["avcodec"].has("av_bitstream_filter_next", "cdecl"):
    av_bitstream_filter_next = _libs["avcodec"].get("av_bitstream_filter_next", "cdecl")
    av_bitstream_filter_next.argtypes = [POINTER(AVBitStreamFilter)]
    av_bitstream_filter_next.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/avcodec.h: 4070
if _libs["avcodec"].has("av_bsf_next", "cdecl"):
    av_bsf_next = _libs["avcodec"].get("av_bsf_next", "cdecl")
    av_bsf_next.argtypes = [POINTER(POINTER(None))]
    av_bsf_next.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/avcodec.h: 4082
if _libs["avcodec"].has("av_fast_padded_malloc", "cdecl"):
    av_fast_padded_malloc = _libs["avcodec"].get("av_fast_padded_malloc", "cdecl")
    av_fast_padded_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_malloc.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 4088
if _libs["avcodec"].has("av_fast_padded_mallocz", "cdecl"):
    av_fast_padded_mallocz = _libs["avcodec"].get("av_fast_padded_mallocz", "cdecl")
    av_fast_padded_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_mallocz.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 4097
if _libs["avcodec"].has("av_xiphlacing", "cdecl"):
    av_xiphlacing = _libs["avcodec"].get("av_xiphlacing", "cdecl")
    av_xiphlacing.argtypes = [POINTER(c_ubyte), c_uint]
    av_xiphlacing.restype = c_uint

# /home/josiah/ctypesgen_test/av/avcodec.h: 4106
if _libs["avcodec"].has("av_register_hwaccel", "cdecl"):
    av_register_hwaccel = _libs["avcodec"].get("av_register_hwaccel", "cdecl")
    av_register_hwaccel.argtypes = [POINTER(AVHWAccel)]
    av_register_hwaccel.restype = None

# /home/josiah/ctypesgen_test/av/avcodec.h: 4117
if _libs["avcodec"].has("av_hwaccel_next", "cdecl"):
    av_hwaccel_next = _libs["avcodec"].get("av_hwaccel_next", "cdecl")
    av_hwaccel_next.argtypes = [POINTER(AVHWAccel)]
    av_hwaccel_next.restype = POINTER(AVHWAccel)

enum_AVLockOp = c_int# /home/josiah/ctypesgen_test/av/avcodec.h: 4126

AV_LOCK_CREATE = 0# /home/josiah/ctypesgen_test/av/avcodec.h: 4126

AV_LOCK_OBTAIN = (AV_LOCK_CREATE + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 4126

AV_LOCK_RELEASE = (AV_LOCK_OBTAIN + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 4126

AV_LOCK_DESTROY = (AV_LOCK_RELEASE + 1)# /home/josiah/ctypesgen_test/av/avcodec.h: 4126

# /home/josiah/ctypesgen_test/av/avcodec.h: 4160
if _libs["avcodec"].has("av_lockmgr_register", "cdecl"):
    av_lockmgr_register = _libs["avcodec"].get("av_lockmgr_register", "cdecl")
    av_lockmgr_register.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(None)), enum_AVLockOp)]
    av_lockmgr_register.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4167
if _libs["avcodec"].has("avcodec_is_open", "cdecl"):
    avcodec_is_open = _libs["avcodec"].get("avcodec_is_open", "cdecl")
    avcodec_is_open.argtypes = [POINTER(AVCodecContext)]
    avcodec_is_open.restype = c_int

# /home/josiah/ctypesgen_test/av/avcodec.h: 4178
if _libs["avcodec"].has("av_cpb_properties_alloc", "cdecl"):
    av_cpb_properties_alloc = _libs["avcodec"].get("av_cpb_properties_alloc", "cdecl")
    av_cpb_properties_alloc.argtypes = [POINTER(c_size_t)]
    av_cpb_properties_alloc.restype = POINTER(AVCPBProperties)

enum_AVOptionType = c_int# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_FLAGS = 0# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_INT = (AV_OPT_TYPE_FLAGS + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_INT64 = (AV_OPT_TYPE_INT + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_DOUBLE = (AV_OPT_TYPE_INT64 + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_FLOAT = (AV_OPT_TYPE_DOUBLE + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_STRING = (AV_OPT_TYPE_FLOAT + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_RATIONAL = (AV_OPT_TYPE_STRING + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_BINARY = (AV_OPT_TYPE_RATIONAL + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_DICT = (AV_OPT_TYPE_BINARY + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_UINT64 = (AV_OPT_TYPE_DICT + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_CONST = (AV_OPT_TYPE_UINT64 + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_IMAGE_SIZE = (AV_OPT_TYPE_CONST + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_PIXEL_FMT = (AV_OPT_TYPE_IMAGE_SIZE + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_SAMPLE_FMT = (AV_OPT_TYPE_PIXEL_FMT + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_VIDEO_RATE = (AV_OPT_TYPE_SAMPLE_FMT + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_DURATION = (AV_OPT_TYPE_VIDEO_RATE + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_COLOR = (AV_OPT_TYPE_DURATION + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_CHANNEL_LAYOUT = (AV_OPT_TYPE_COLOR + 1)# /usr/include/libavutil/opt.h: 223

AV_OPT_TYPE_BOOL = (AV_OPT_TYPE_CHANNEL_LAYOUT + 1)# /usr/include/libavutil/opt.h: 223

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

AVOptionRanges = struct_AVOptionRanges# /usr/include/libavutil/opt.h: 373

# /usr/include/libavutil/opt.h: 384
if _libs["avcodec"].has("av_opt_show2", "cdecl"):
    av_opt_show2 = _libs["avcodec"].get("av_opt_show2", "cdecl")
    av_opt_show2.argtypes = [POINTER(None), POINTER(None), c_int, c_int]
    av_opt_show2.restype = c_int

# /usr/include/libavutil/opt.h: 391
if _libs["avcodec"].has("av_opt_set_defaults", "cdecl"):
    av_opt_set_defaults = _libs["avcodec"].get("av_opt_set_defaults", "cdecl")
    av_opt_set_defaults.argtypes = [POINTER(None)]
    av_opt_set_defaults.restype = None

# /usr/include/libavutil/opt.h: 402
if _libs["avcodec"].has("av_opt_set_defaults2", "cdecl"):
    av_opt_set_defaults2 = _libs["avcodec"].get("av_opt_set_defaults2", "cdecl")
    av_opt_set_defaults2.argtypes = [POINTER(None), c_int, c_int]
    av_opt_set_defaults2.restype = None

# /usr/include/libavutil/opt.h: 421
if _libs["avcodec"].has("av_set_options_string", "cdecl"):
    av_set_options_string = _libs["avcodec"].get("av_set_options_string", "cdecl")
    av_set_options_string.argtypes = [POINTER(None), String, String, String]
    av_set_options_string.restype = c_int

# /usr/include/libavutil/opt.h: 451
if _libs["avcodec"].has("av_opt_set_from_string", "cdecl"):
    av_opt_set_from_string = _libs["avcodec"].get("av_opt_set_from_string", "cdecl")
    av_opt_set_from_string.argtypes = [POINTER(None), String, POINTER(POINTER(c_char)), String, String]
    av_opt_set_from_string.restype = c_int

# /usr/include/libavutil/opt.h: 457
if _libs["avcodec"].has("av_opt_free", "cdecl"):
    av_opt_free = _libs["avcodec"].get("av_opt_free", "cdecl")
    av_opt_free.argtypes = [POINTER(None)]
    av_opt_free.restype = None

# /usr/include/libavutil/opt.h: 467
if _libs["avcodec"].has("av_opt_flag_is_set", "cdecl"):
    av_opt_flag_is_set = _libs["avcodec"].get("av_opt_flag_is_set", "cdecl")
    av_opt_flag_is_set.argtypes = [POINTER(None), String, String]
    av_opt_flag_is_set.restype = c_int

# /usr/include/libavutil/opt.h: 483
if _libs["avcodec"].has("av_opt_set_dict", "cdecl"):
    av_opt_set_dict = _libs["avcodec"].get("av_opt_set_dict", "cdecl")
    av_opt_set_dict.argtypes = [POINTER(None), POINTER(POINTER(struct_AVDictionary))]
    av_opt_set_dict.restype = c_int

# /usr/include/libavutil/opt.h: 501
if _libs["avcodec"].has("av_opt_set_dict2", "cdecl"):
    av_opt_set_dict2 = _libs["avcodec"].get("av_opt_set_dict2", "cdecl")
    av_opt_set_dict2.argtypes = [POINTER(None), POINTER(POINTER(struct_AVDictionary)), c_int]
    av_opt_set_dict2.restype = c_int

# /usr/include/libavutil/opt.h: 522
if _libs["avcodec"].has("av_opt_get_key_value", "cdecl"):
    av_opt_get_key_value = _libs["avcodec"].get("av_opt_get_key_value", "cdecl")
    av_opt_get_key_value.argtypes = [POINTER(POINTER(c_char)), String, String, c_uint, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    av_opt_get_key_value.restype = c_int

enum_anon_30 = c_int# /usr/include/libavutil/opt.h: 527

AV_OPT_FLAG_IMPLICIT_KEY = 1# /usr/include/libavutil/opt.h: 527

# /usr/include/libavutil/opt.h: 550
if _libs["avcodec"].has("av_opt_eval_flags", "cdecl"):
    av_opt_eval_flags = _libs["avcodec"].get("av_opt_eval_flags", "cdecl")
    av_opt_eval_flags.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int)]
    av_opt_eval_flags.restype = c_int

# /usr/include/libavutil/opt.h: 551
if _libs["avcodec"].has("av_opt_eval_int", "cdecl"):
    av_opt_eval_int = _libs["avcodec"].get("av_opt_eval_int", "cdecl")
    av_opt_eval_int.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int)]
    av_opt_eval_int.restype = c_int

# /usr/include/libavutil/opt.h: 552
if _libs["avcodec"].has("av_opt_eval_int64", "cdecl"):
    av_opt_eval_int64 = _libs["avcodec"].get("av_opt_eval_int64", "cdecl")
    av_opt_eval_int64.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int64)]
    av_opt_eval_int64.restype = c_int

# /usr/include/libavutil/opt.h: 553
if _libs["avcodec"].has("av_opt_eval_float", "cdecl"):
    av_opt_eval_float = _libs["avcodec"].get("av_opt_eval_float", "cdecl")
    av_opt_eval_float.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_float)]
    av_opt_eval_float.restype = c_int

# /usr/include/libavutil/opt.h: 554
if _libs["avcodec"].has("av_opt_eval_double", "cdecl"):
    av_opt_eval_double = _libs["avcodec"].get("av_opt_eval_double", "cdecl")
    av_opt_eval_double.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_double)]
    av_opt_eval_double.restype = c_int

# /usr/include/libavutil/opt.h: 555
if _libs["avcodec"].has("av_opt_eval_q", "cdecl"):
    av_opt_eval_q = _libs["avcodec"].get("av_opt_eval_q", "cdecl")
    av_opt_eval_q.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(AVRational)]
    av_opt_eval_q.restype = c_int

# /usr/include/libavutil/opt.h: 605
if _libs["avcodec"].has("av_opt_find", "cdecl"):
    av_opt_find = _libs["avcodec"].get("av_opt_find", "cdecl")
    av_opt_find.argtypes = [POINTER(None), String, String, c_int, c_int]
    av_opt_find.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 629
if _libs["avcodec"].has("av_opt_find2", "cdecl"):
    av_opt_find2 = _libs["avcodec"].get("av_opt_find2", "cdecl")
    av_opt_find2.argtypes = [POINTER(None), String, String, c_int, c_int, POINTER(POINTER(None))]
    av_opt_find2.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 641
if _libs["avcodec"].has("av_opt_next", "cdecl"):
    av_opt_next = _libs["avcodec"].get("av_opt_next", "cdecl")
    av_opt_next.argtypes = [POINTER(None), POINTER(AVOption)]
    av_opt_next.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 649
if _libs["avcodec"].has("av_opt_child_next", "cdecl"):
    av_opt_child_next = _libs["avcodec"].get("av_opt_child_next", "cdecl")
    av_opt_child_next.argtypes = [POINTER(None), POINTER(None)]
    av_opt_child_next.restype = POINTER(c_ubyte)
    av_opt_child_next.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/opt.h: 661
if _libs["avcodec"].has("av_opt_child_class_next", "cdecl"):
    av_opt_child_class_next = _libs["avcodec"].get("av_opt_child_class_next", "cdecl")
    av_opt_child_class_next.argtypes = [POINTER(AVClass), POINTER(AVClass)]
    av_opt_child_class_next.restype = POINTER(AVClass)

# /usr/include/libavutil/opt.h: 670
if _libs["avcodec"].has("av_opt_child_class_iterate", "cdecl"):
    av_opt_child_class_iterate = _libs["avcodec"].get("av_opt_child_class_iterate", "cdecl")
    av_opt_child_class_iterate.argtypes = [POINTER(AVClass), POINTER(POINTER(None))]
    av_opt_child_class_iterate.restype = POINTER(AVClass)

# /usr/include/libavutil/opt.h: 701
if _libs["avcodec"].has("av_opt_set", "cdecl"):
    av_opt_set = _libs["avcodec"].get("av_opt_set", "cdecl")
    av_opt_set.argtypes = [POINTER(None), String, String, c_int]
    av_opt_set.restype = c_int

# /usr/include/libavutil/opt.h: 702
if _libs["avcodec"].has("av_opt_set_int", "cdecl"):
    av_opt_set_int = _libs["avcodec"].get("av_opt_set_int", "cdecl")
    av_opt_set_int.argtypes = [POINTER(None), String, c_int64, c_int]
    av_opt_set_int.restype = c_int

# /usr/include/libavutil/opt.h: 703
if _libs["avcodec"].has("av_opt_set_double", "cdecl"):
    av_opt_set_double = _libs["avcodec"].get("av_opt_set_double", "cdecl")
    av_opt_set_double.argtypes = [POINTER(None), String, c_double, c_int]
    av_opt_set_double.restype = c_int

# /usr/include/libavutil/opt.h: 704
if _libs["avcodec"].has("av_opt_set_q", "cdecl"):
    av_opt_set_q = _libs["avcodec"].get("av_opt_set_q", "cdecl")
    av_opt_set_q.argtypes = [POINTER(None), String, AVRational, c_int]
    av_opt_set_q.restype = c_int

# /usr/include/libavutil/opt.h: 705
if _libs["avcodec"].has("av_opt_set_bin", "cdecl"):
    av_opt_set_bin = _libs["avcodec"].get("av_opt_set_bin", "cdecl")
    av_opt_set_bin.argtypes = [POINTER(None), String, POINTER(c_uint8), c_int, c_int]
    av_opt_set_bin.restype = c_int

# /usr/include/libavutil/opt.h: 706
if _libs["avcodec"].has("av_opt_set_image_size", "cdecl"):
    av_opt_set_image_size = _libs["avcodec"].get("av_opt_set_image_size", "cdecl")
    av_opt_set_image_size.argtypes = [POINTER(None), String, c_int, c_int, c_int]
    av_opt_set_image_size.restype = c_int

# /usr/include/libavutil/opt.h: 707
if _libs["avcodec"].has("av_opt_set_pixel_fmt", "cdecl"):
    av_opt_set_pixel_fmt = _libs["avcodec"].get("av_opt_set_pixel_fmt", "cdecl")
    av_opt_set_pixel_fmt.argtypes = [POINTER(None), String, enum_AVPixelFormat, c_int]
    av_opt_set_pixel_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 708
if _libs["avcodec"].has("av_opt_set_sample_fmt", "cdecl"):
    av_opt_set_sample_fmt = _libs["avcodec"].get("av_opt_set_sample_fmt", "cdecl")
    av_opt_set_sample_fmt.argtypes = [POINTER(None), String, enum_AVSampleFormat, c_int]
    av_opt_set_sample_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 709
if _libs["avcodec"].has("av_opt_set_video_rate", "cdecl"):
    av_opt_set_video_rate = _libs["avcodec"].get("av_opt_set_video_rate", "cdecl")
    av_opt_set_video_rate.argtypes = [POINTER(None), String, AVRational, c_int]
    av_opt_set_video_rate.restype = c_int

# /usr/include/libavutil/opt.h: 710
if _libs["avcodec"].has("av_opt_set_channel_layout", "cdecl"):
    av_opt_set_channel_layout = _libs["avcodec"].get("av_opt_set_channel_layout", "cdecl")
    av_opt_set_channel_layout.argtypes = [POINTER(None), String, c_int64, c_int]
    av_opt_set_channel_layout.restype = c_int

# /usr/include/libavutil/opt.h: 715
if _libs["avcodec"].has("av_opt_set_dict_val", "cdecl"):
    av_opt_set_dict_val = _libs["avcodec"].get("av_opt_set_dict_val", "cdecl")
    av_opt_set_dict_val.argtypes = [POINTER(None), String, POINTER(AVDictionary), c_int]
    av_opt_set_dict_val.restype = c_int

# /usr/include/libavutil/opt.h: 757
if _libs["avcodec"].has("av_opt_get", "cdecl"):
    av_opt_get = _libs["avcodec"].get("av_opt_get", "cdecl")
    av_opt_get.argtypes = [POINTER(None), String, c_int, POINTER(POINTER(c_uint8))]
    av_opt_get.restype = c_int

# /usr/include/libavutil/opt.h: 758
if _libs["avcodec"].has("av_opt_get_int", "cdecl"):
    av_opt_get_int = _libs["avcodec"].get("av_opt_get_int", "cdecl")
    av_opt_get_int.argtypes = [POINTER(None), String, c_int, POINTER(c_int64)]
    av_opt_get_int.restype = c_int

# /usr/include/libavutil/opt.h: 759
if _libs["avcodec"].has("av_opt_get_double", "cdecl"):
    av_opt_get_double = _libs["avcodec"].get("av_opt_get_double", "cdecl")
    av_opt_get_double.argtypes = [POINTER(None), String, c_int, POINTER(c_double)]
    av_opt_get_double.restype = c_int

# /usr/include/libavutil/opt.h: 760
if _libs["avcodec"].has("av_opt_get_q", "cdecl"):
    av_opt_get_q = _libs["avcodec"].get("av_opt_get_q", "cdecl")
    av_opt_get_q.argtypes = [POINTER(None), String, c_int, POINTER(AVRational)]
    av_opt_get_q.restype = c_int

# /usr/include/libavutil/opt.h: 761
if _libs["avcodec"].has("av_opt_get_image_size", "cdecl"):
    av_opt_get_image_size = _libs["avcodec"].get("av_opt_get_image_size", "cdecl")
    av_opt_get_image_size.argtypes = [POINTER(None), String, c_int, POINTER(c_int), POINTER(c_int)]
    av_opt_get_image_size.restype = c_int

# /usr/include/libavutil/opt.h: 762
if _libs["avcodec"].has("av_opt_get_pixel_fmt", "cdecl"):
    av_opt_get_pixel_fmt = _libs["avcodec"].get("av_opt_get_pixel_fmt", "cdecl")
    av_opt_get_pixel_fmt.argtypes = [POINTER(None), String, c_int, POINTER(enum_AVPixelFormat)]
    av_opt_get_pixel_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 763
if _libs["avcodec"].has("av_opt_get_sample_fmt", "cdecl"):
    av_opt_get_sample_fmt = _libs["avcodec"].get("av_opt_get_sample_fmt", "cdecl")
    av_opt_get_sample_fmt.argtypes = [POINTER(None), String, c_int, POINTER(enum_AVSampleFormat)]
    av_opt_get_sample_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 764
if _libs["avcodec"].has("av_opt_get_video_rate", "cdecl"):
    av_opt_get_video_rate = _libs["avcodec"].get("av_opt_get_video_rate", "cdecl")
    av_opt_get_video_rate.argtypes = [POINTER(None), String, c_int, POINTER(AVRational)]
    av_opt_get_video_rate.restype = c_int

# /usr/include/libavutil/opt.h: 765
if _libs["avcodec"].has("av_opt_get_channel_layout", "cdecl"):
    av_opt_get_channel_layout = _libs["avcodec"].get("av_opt_get_channel_layout", "cdecl")
    av_opt_get_channel_layout.argtypes = [POINTER(None), String, c_int, POINTER(c_int64)]
    av_opt_get_channel_layout.restype = c_int

# /usr/include/libavutil/opt.h: 770
if _libs["avcodec"].has("av_opt_get_dict_val", "cdecl"):
    av_opt_get_dict_val = _libs["avcodec"].get("av_opt_get_dict_val", "cdecl")
    av_opt_get_dict_val.argtypes = [POINTER(None), String, c_int, POINTER(POINTER(AVDictionary))]
    av_opt_get_dict_val.restype = c_int

# /usr/include/libavutil/opt.h: 782
if _libs["avcodec"].has("av_opt_ptr", "cdecl"):
    av_opt_ptr = _libs["avcodec"].get("av_opt_ptr", "cdecl")
    av_opt_ptr.argtypes = [POINTER(AVClass), POINTER(None), String]
    av_opt_ptr.restype = POINTER(c_ubyte)
    av_opt_ptr.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/opt.h: 787
if _libs["avcodec"].has("av_opt_freep_ranges", "cdecl"):
    av_opt_freep_ranges = _libs["avcodec"].get("av_opt_freep_ranges", "cdecl")
    av_opt_freep_ranges.argtypes = [POINTER(POINTER(AVOptionRanges))]
    av_opt_freep_ranges.restype = None

# /usr/include/libavutil/opt.h: 802
if _libs["avcodec"].has("av_opt_query_ranges", "cdecl"):
    av_opt_query_ranges = _libs["avcodec"].get("av_opt_query_ranges", "cdecl")
    av_opt_query_ranges.argtypes = [POINTER(POINTER(AVOptionRanges)), POINTER(None), String, c_int]
    av_opt_query_ranges.restype = c_int

# /usr/include/libavutil/opt.h: 814
if _libs["avcodec"].has("av_opt_copy", "cdecl"):
    av_opt_copy = _libs["avcodec"].get("av_opt_copy", "cdecl")
    av_opt_copy.argtypes = [POINTER(None), POINTER(None)]
    av_opt_copy.restype = c_int

# /usr/include/libavutil/opt.h: 830
if _libs["avcodec"].has("av_opt_query_ranges_default", "cdecl"):
    av_opt_query_ranges_default = _libs["avcodec"].get("av_opt_query_ranges_default", "cdecl")
    av_opt_query_ranges_default.argtypes = [POINTER(POINTER(AVOptionRanges)), POINTER(None), String, c_int]
    av_opt_query_ranges_default.restype = c_int

# /usr/include/libavutil/opt.h: 844
if _libs["avcodec"].has("av_opt_is_set_to_default", "cdecl"):
    av_opt_is_set_to_default = _libs["avcodec"].get("av_opt_is_set_to_default", "cdecl")
    av_opt_is_set_to_default.argtypes = [POINTER(None), POINTER(AVOption)]
    av_opt_is_set_to_default.restype = c_int

# /usr/include/libavutil/opt.h: 856
if _libs["avcodec"].has("av_opt_is_set_to_default_by_name", "cdecl"):
    av_opt_is_set_to_default_by_name = _libs["avcodec"].get("av_opt_is_set_to_default_by_name", "cdecl")
    av_opt_is_set_to_default_by_name.argtypes = [POINTER(None), String, c_int]
    av_opt_is_set_to_default_by_name.restype = c_int

# /usr/include/libavutil/opt.h: 880
if _libs["avcodec"].has("av_opt_serialize", "cdecl"):
    av_opt_serialize = _libs["avcodec"].get("av_opt_serialize", "cdecl")
    av_opt_serialize.argtypes = [POINTER(None), c_int, c_int, POINTER(POINTER(c_char)), c_char, c_char]
    av_opt_serialize.restype = c_int

# /home/josiah/ctypesgen_test/av/avdct.h: 74
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

AVDCT = struct_AVDCT# /home/josiah/ctypesgen_test/av/avdct.h: 74

# /home/josiah/ctypesgen_test/av/avdct.h: 83
if _libs["avcodec"].has("avcodec_dct_alloc", "cdecl"):
    avcodec_dct_alloc = _libs["avcodec"].get("avcodec_dct_alloc", "cdecl")
    avcodec_dct_alloc.argtypes = []
    avcodec_dct_alloc.restype = POINTER(AVDCT)

# /home/josiah/ctypesgen_test/av/avdct.h: 84
if _libs["avcodec"].has("avcodec_dct_init", "cdecl"):
    avcodec_dct_init = _libs["avcodec"].get("avcodec_dct_init", "cdecl")
    avcodec_dct_init.argtypes = [POINTER(AVDCT)]
    avcodec_dct_init.restype = c_int

# /home/josiah/ctypesgen_test/av/avdct.h: 86
if _libs["avcodec"].has("avcodec_dct_get_class", "cdecl"):
    avcodec_dct_get_class = _libs["avcodec"].get("avcodec_dct_get_class", "cdecl")
    avcodec_dct_get_class.argtypes = []
    avcodec_dct_get_class.restype = POINTER(AVClass)

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

# /home/josiah/ctypesgen_test/av/avdevice.h: 465
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
    av_read_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
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

# /home/josiah/ctypesgen_test/av/avdevice.h: 56
if _libs["avdevice"].has("avdevice_version", "cdecl"):
    avdevice_version = _libs["avdevice"].get("avdevice_version", "cdecl")
    avdevice_version.argtypes = []
    avdevice_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/avdevice.h: 61
if _libs["avdevice"].has("avdevice_configuration", "cdecl"):
    avdevice_configuration = _libs["avdevice"].get("avdevice_configuration", "cdecl")
    avdevice_configuration.argtypes = []
    avdevice_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avdevice.h: 66
if _libs["avdevice"].has("avdevice_license", "cdecl"):
    avdevice_license = _libs["avdevice"].get("avdevice_license", "cdecl")
    avdevice_license.argtypes = []
    avdevice_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avdevice.h: 71
if _libs["avdevice"].has("avdevice_register_all", "cdecl"):
    avdevice_register_all = _libs["avdevice"].get("avdevice_register_all", "cdecl")
    avdevice_register_all.argtypes = []
    avdevice_register_all.restype = None

# /home/josiah/ctypesgen_test/av/avdevice.h: 80
if _libs["avdevice"].has("av_input_audio_device_next", "cdecl"):
    av_input_audio_device_next = _libs["avdevice"].get("av_input_audio_device_next", "cdecl")
    av_input_audio_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_audio_device_next.restype = POINTER(AVInputFormat)

# /home/josiah/ctypesgen_test/av/avdevice.h: 89
if _libs["avdevice"].has("av_input_video_device_next", "cdecl"):
    av_input_video_device_next = _libs["avdevice"].get("av_input_video_device_next", "cdecl")
    av_input_video_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_video_device_next.restype = POINTER(AVInputFormat)

# /home/josiah/ctypesgen_test/av/avdevice.h: 98
if _libs["avdevice"].has("av_output_audio_device_next", "cdecl"):
    av_output_audio_device_next = _libs["avdevice"].get("av_output_audio_device_next", "cdecl")
    av_output_audio_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_audio_device_next.restype = POINTER(AVOutputFormat)

# /home/josiah/ctypesgen_test/av/avdevice.h: 107
if _libs["avdevice"].has("av_output_video_device_next", "cdecl"):
    av_output_video_device_next = _libs["avdevice"].get("av_output_video_device_next", "cdecl")
    av_output_video_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_video_device_next.restype = POINTER(AVOutputFormat)

# /home/josiah/ctypesgen_test/av/avdevice.h: 114
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

AVDeviceRect = struct_AVDeviceRect# /home/josiah/ctypesgen_test/av/avdevice.h: 114

enum_AVAppToDevMessageType = c_int# /home/josiah/ctypesgen_test/av/avdevice.h: 119

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

enum_AVDevToAppMessageType = c_int# /home/josiah/ctypesgen_test/av/avdevice.h: 198

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

# /home/josiah/ctypesgen_test/av/avdevice.h: 306
if _libs["avdevice"].has("avdevice_app_to_dev_control_message", "cdecl"):
    avdevice_app_to_dev_control_message = _libs["avdevice"].get("avdevice_app_to_dev_control_message", "cdecl")
    avdevice_app_to_dev_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVAppToDevMessageType, POINTER(None), c_size_t]
    avdevice_app_to_dev_control_message.restype = c_int

# /home/josiah/ctypesgen_test/av/avdevice.h: 320
if _libs["avdevice"].has("avdevice_dev_to_app_control_message", "cdecl"):
    avdevice_dev_to_app_control_message = _libs["avdevice"].get("avdevice_dev_to_app_control_message", "cdecl")
    avdevice_dev_to_app_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVDevToAppMessageType, POINTER(None), c_size_t]
    avdevice_dev_to_app_control_message.restype = c_int

# /home/josiah/ctypesgen_test/av/avdevice.h: 460
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

AVDeviceInfo = struct_AVDeviceInfo# /home/josiah/ctypesgen_test/av/avdevice.h: 460

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

AVDeviceInfoList = struct_AVDeviceInfoList# /home/josiah/ctypesgen_test/av/avdevice.h: 469

# /home/josiah/ctypesgen_test/av/avdevice.h: 484
if _libs["avdevice"].has("avdevice_list_devices", "cdecl"):
    avdevice_list_devices = _libs["avdevice"].get("avdevice_list_devices", "cdecl")
    avdevice_list_devices.argtypes = [POINTER(struct_AVFormatContext), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_devices.restype = c_int

# /home/josiah/ctypesgen_test/av/avdevice.h: 491
if _libs["avdevice"].has("avdevice_free_list_devices", "cdecl"):
    avdevice_free_list_devices = _libs["avdevice"].get("avdevice_free_list_devices", "cdecl")
    avdevice_free_list_devices.argtypes = [POINTER(POINTER(AVDeviceInfoList))]
    avdevice_free_list_devices.restype = None

# /home/josiah/ctypesgen_test/av/avdevice.h: 510
if _libs["avdevice"].has("avdevice_list_input_sources", "cdecl"):
    avdevice_list_input_sources = _libs["avdevice"].get("avdevice_list_input_sources", "cdecl")
    avdevice_list_input_sources.argtypes = [POINTER(struct_AVInputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_input_sources.restype = c_int

# /home/josiah/ctypesgen_test/av/avdevice.h: 512
if _libs["avdevice"].has("avdevice_list_output_sinks", "cdecl"):
    avdevice_list_output_sinks = _libs["avdevice"].get("avdevice_list_output_sinks", "cdecl")
    avdevice_list_output_sinks.argtypes = [POINTER(struct_AVOutputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_output_sinks.restype = c_int

FFTSample = c_float# /home/josiah/ctypesgen_test/av/avfft.h: 35

# /home/josiah/ctypesgen_test/av/avfft.h: 39
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

FFTComplex = struct_FFTComplex# /home/josiah/ctypesgen_test/av/avfft.h: 39

# /home/josiah/ctypesgen_test/av/avfft.h: 41
class struct_FFTContext(Structure):
    pass

FFTContext = struct_FFTContext# /home/josiah/ctypesgen_test/av/avfft.h: 41

# /home/josiah/ctypesgen_test/av/avfft.h: 48
if _libs["avcodec"].has("av_fft_init", "cdecl"):
    av_fft_init = _libs["avcodec"].get("av_fft_init", "cdecl")
    av_fft_init.argtypes = [c_int, c_int]
    av_fft_init.restype = POINTER(FFTContext)

# /home/josiah/ctypesgen_test/av/avfft.h: 53
if _libs["avcodec"].has("av_fft_permute", "cdecl"):
    av_fft_permute = _libs["avcodec"].get("av_fft_permute", "cdecl")
    av_fft_permute.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_permute.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 59
if _libs["avcodec"].has("av_fft_calc", "cdecl"):
    av_fft_calc = _libs["avcodec"].get("av_fft_calc", "cdecl")
    av_fft_calc.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_calc.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 61
if _libs["avcodec"].has("av_fft_end", "cdecl"):
    av_fft_end = _libs["avcodec"].get("av_fft_end", "cdecl")
    av_fft_end.argtypes = [POINTER(FFTContext)]
    av_fft_end.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 63
if _libs["avcodec"].has("av_mdct_init", "cdecl"):
    av_mdct_init = _libs["avcodec"].get("av_mdct_init", "cdecl")
    av_mdct_init.argtypes = [c_int, c_int, c_double]
    av_mdct_init.restype = POINTER(FFTContext)

# /home/josiah/ctypesgen_test/av/avfft.h: 64
if _libs["avcodec"].has("av_imdct_calc", "cdecl"):
    av_imdct_calc = _libs["avcodec"].get("av_imdct_calc", "cdecl")
    av_imdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_calc.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 65
if _libs["avcodec"].has("av_imdct_half", "cdecl"):
    av_imdct_half = _libs["avcodec"].get("av_imdct_half", "cdecl")
    av_imdct_half.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_half.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 66
if _libs["avcodec"].has("av_mdct_calc", "cdecl"):
    av_mdct_calc = _libs["avcodec"].get("av_mdct_calc", "cdecl")
    av_mdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_mdct_calc.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 67
if _libs["avcodec"].has("av_mdct_end", "cdecl"):
    av_mdct_end = _libs["avcodec"].get("av_mdct_end", "cdecl")
    av_mdct_end.argtypes = [POINTER(FFTContext)]
    av_mdct_end.restype = None

enum_RDFTransformType = c_int# /home/josiah/ctypesgen_test/av/avfft.h: 71

DFT_R2C = 0# /home/josiah/ctypesgen_test/av/avfft.h: 71

IDFT_C2R = (DFT_R2C + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 71

IDFT_R2C = (IDFT_C2R + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 71

DFT_C2R = (IDFT_R2C + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 71

# /home/josiah/ctypesgen_test/av/avfft.h: 78
class struct_RDFTContext(Structure):
    pass

RDFTContext = struct_RDFTContext# /home/josiah/ctypesgen_test/av/avfft.h: 78

# /home/josiah/ctypesgen_test/av/avfft.h: 85
if _libs["avcodec"].has("av_rdft_init", "cdecl"):
    av_rdft_init = _libs["avcodec"].get("av_rdft_init", "cdecl")
    av_rdft_init.argtypes = [c_int, enum_RDFTransformType]
    av_rdft_init.restype = POINTER(RDFTContext)

# /home/josiah/ctypesgen_test/av/avfft.h: 86
if _libs["avcodec"].has("av_rdft_calc", "cdecl"):
    av_rdft_calc = _libs["avcodec"].get("av_rdft_calc", "cdecl")
    av_rdft_calc.argtypes = [POINTER(RDFTContext), POINTER(FFTSample)]
    av_rdft_calc.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 87
if _libs["avcodec"].has("av_rdft_end", "cdecl"):
    av_rdft_end = _libs["avcodec"].get("av_rdft_end", "cdecl")
    av_rdft_end.argtypes = [POINTER(RDFTContext)]
    av_rdft_end.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 91
class struct_DCTContext(Structure):
    pass

DCTContext = struct_DCTContext# /home/josiah/ctypesgen_test/av/avfft.h: 91

enum_DCTTransformType = c_int# /home/josiah/ctypesgen_test/av/avfft.h: 93

DCT_II = 0# /home/josiah/ctypesgen_test/av/avfft.h: 93

DCT_III = (DCT_II + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 93

DCT_I = (DCT_III + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 93

DST_I = (DCT_I + 1)# /home/josiah/ctypesgen_test/av/avfft.h: 93

# /home/josiah/ctypesgen_test/av/avfft.h: 110
if _libs["avcodec"].has("av_dct_init", "cdecl"):
    av_dct_init = _libs["avcodec"].get("av_dct_init", "cdecl")
    av_dct_init.argtypes = [c_int, enum_DCTTransformType]
    av_dct_init.restype = POINTER(DCTContext)

# /home/josiah/ctypesgen_test/av/avfft.h: 111
if _libs["avcodec"].has("av_dct_calc", "cdecl"):
    av_dct_calc = _libs["avcodec"].get("av_dct_calc", "cdecl")
    av_dct_calc.argtypes = [POINTER(DCTContext), POINTER(FFTSample)]
    av_dct_calc.restype = None

# /home/josiah/ctypesgen_test/av/avfft.h: 112
if _libs["avcodec"].has("av_dct_end", "cdecl"):
    av_dct_end = _libs["avcodec"].get("av_dct_end", "cdecl")
    av_dct_end.argtypes = [POINTER(DCTContext)]
    av_dct_end.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 55
if _libs["avdevice"].has("avfilter_version", "cdecl"):
    avfilter_version = _libs["avdevice"].get("avfilter_version", "cdecl")
    avfilter_version.argtypes = []
    avfilter_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/avfilter.h: 60
if _libs["avdevice"].has("avfilter_configuration", "cdecl"):
    avfilter_configuration = _libs["avdevice"].get("avfilter_configuration", "cdecl")
    avfilter_configuration.argtypes = []
    avfilter_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avfilter.h: 65
if _libs["avdevice"].has("avfilter_license", "cdecl"):
    avfilter_license = _libs["avdevice"].get("avfilter_license", "cdecl")
    avfilter_license.argtypes = []
    avfilter_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avfilter.h: 341
class struct_AVFilterContext(Structure):
    pass

AVFilterContext = struct_AVFilterContext# /home/josiah/ctypesgen_test/av/avfilter.h: 67

# /home/josiah/ctypesgen_test/av/avfilter.h: 471
class struct_AVFilterLink(Structure):
    pass

AVFilterLink = struct_AVFilterLink# /home/josiah/ctypesgen_test/av/avfilter.h: 68

# /home/josiah/ctypesgen_test/av/avfilter.h: 69
class struct_AVFilterPad(Structure):
    pass

AVFilterPad = struct_AVFilterPad# /home/josiah/ctypesgen_test/av/avfilter.h: 69

# /home/josiah/ctypesgen_test/av/avfilter.h: 70
class struct_AVFilterFormats(Structure):
    pass

AVFilterFormats = struct_AVFilterFormats# /home/josiah/ctypesgen_test/av/avfilter.h: 70

# /home/josiah/ctypesgen_test/av/avfilter.h: 71
class struct_AVFilterChannelLayouts(Structure):
    pass

AVFilterChannelLayouts = struct_AVFilterChannelLayouts# /home/josiah/ctypesgen_test/av/avfilter.h: 71

# /home/josiah/ctypesgen_test/av/avfilter.h: 77
if _libs["avdevice"].has("avfilter_pad_count", "cdecl"):
    avfilter_pad_count = _libs["avdevice"].get("avfilter_pad_count", "cdecl")
    avfilter_pad_count.argtypes = [POINTER(AVFilterPad)]
    avfilter_pad_count.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 88
if _libs["avdevice"].has("avfilter_pad_get_name", "cdecl"):
    avfilter_pad_get_name = _libs["avdevice"].get("avfilter_pad_get_name", "cdecl")
    avfilter_pad_get_name.argtypes = [POINTER(AVFilterPad), c_int]
    avfilter_pad_get_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avfilter.h: 99
if _libs["avdevice"].has("avfilter_pad_get_type", "cdecl"):
    avfilter_pad_get_type = _libs["avdevice"].get("avfilter_pad_get_type", "cdecl")
    avfilter_pad_get_type.argtypes = [POINTER(AVFilterPad), c_int]
    avfilter_pad_get_type.restype = enum_AVMediaType

# /home/josiah/ctypesgen_test/av/avfilter.h: 145
class struct_AVFilter(Structure):
    pass

struct_AVFilter.__slots__ = [
    'name',
    'description',
    'inputs',
    'outputs',
    'priv_class',
    'flags',
    'preinit',
    'init',
    'init_dict',
    'uninit',
    'query_formats',
    'priv_size',
    'flags_internal',
    'next',
    'process_command',
    'init_opaque',
    'activate',
]
struct_AVFilter._fields_ = [
    ('name', String),
    ('description', String),
    ('inputs', POINTER(AVFilterPad)),
    ('outputs', POINTER(AVFilterPad)),
    ('priv_class', POINTER(AVClass)),
    ('flags', c_int),
    ('preinit', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('init_dict', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(POINTER(AVDictionary)))),
    ('uninit', CFUNCTYPE(UNCHECKED(None), POINTER(AVFilterContext))),
    ('query_formats', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('priv_size', c_int),
    ('flags_internal', c_int),
    ('next', POINTER(struct_AVFilter)),
    ('process_command', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), String, String, String, c_int, c_int)),
    ('init_opaque', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(None))),
    ('activate', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
]

AVFilter = struct_AVFilter# /home/josiah/ctypesgen_test/av/avfilter.h: 331

# /home/josiah/ctypesgen_test/av/avfilter.h: 338
class struct_AVFilterInternal(Structure):
    pass

AVFilterInternal = struct_AVFilterInternal# /home/josiah/ctypesgen_test/av/avfilter.h: 338

# /home/josiah/ctypesgen_test/av/avfilter.h: 850
class struct_AVFilterGraph(Structure):
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 383
class struct_AVFilterCommand(Structure):
    pass

struct_AVFilterContext.__slots__ = [
    'av_class',
    'filter',
    'name',
    'input_pads',
    'inputs',
    'nb_inputs',
    'output_pads',
    'outputs',
    'nb_outputs',
    'priv',
    'graph',
    'thread_type',
    'internal',
    'command_queue',
    'enable_str',
    'enable',
    'var_values',
    'is_disabled',
    'hw_device_ctx',
    'nb_threads',
    'ready',
    'extra_hw_frames',
]
struct_AVFilterContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('filter', POINTER(AVFilter)),
    ('name', String),
    ('input_pads', POINTER(AVFilterPad)),
    ('inputs', POINTER(POINTER(AVFilterLink))),
    ('nb_inputs', c_uint),
    ('output_pads', POINTER(AVFilterPad)),
    ('outputs', POINTER(POINTER(AVFilterLink))),
    ('nb_outputs', c_uint),
    ('priv', POINTER(None)),
    ('graph', POINTER(struct_AVFilterGraph)),
    ('thread_type', c_int),
    ('internal', POINTER(AVFilterInternal)),
    ('command_queue', POINTER(struct_AVFilterCommand)),
    ('enable_str', String),
    ('enable', POINTER(None)),
    ('var_values', POINTER(c_double)),
    ('is_disabled', c_int),
    ('hw_device_ctx', POINTER(AVBufferRef)),
    ('nb_threads', c_int),
    ('ready', c_uint),
    ('extra_hw_frames', c_int),
]

# /home/josiah/ctypesgen_test/av/avfilter.h: 457
class struct_AVFilterFormatsConfig(Structure):
    pass

struct_AVFilterFormatsConfig.__slots__ = [
    'formats',
    'samplerates',
    'channel_layouts',
]
struct_AVFilterFormatsConfig._fields_ = [
    ('formats', POINTER(AVFilterFormats)),
    ('samplerates', POINTER(AVFilterFormats)),
    ('channel_layouts', POINTER(AVFilterChannelLayouts)),
]

AVFilterFormatsConfig = struct_AVFilterFormatsConfig# /home/josiah/ctypesgen_test/av/avfilter.h: 457

enum_anon_31 = c_int# /home/josiah/ctypesgen_test/av/avfilter.h: 518

AVLINK_UNINIT = 0# /home/josiah/ctypesgen_test/av/avfilter.h: 518

AVLINK_STARTINIT = (AVLINK_UNINIT + 1)# /home/josiah/ctypesgen_test/av/avfilter.h: 518

AVLINK_INIT = (AVLINK_STARTINIT + 1)# /home/josiah/ctypesgen_test/av/avfilter.h: 518

struct_AVFilterLink.__slots__ = [
    'src',
    'srcpad',
    'dst',
    'dstpad',
    'type',
    'w',
    'h',
    'sample_aspect_ratio',
    'channel_layout',
    'sample_rate',
    'format',
    'time_base',
    'incfg',
    'outcfg',
    'init_state',
    'graph',
    'current_pts',
    'current_pts_us',
    'age_index',
    'frame_rate',
    'partial_buf',
    'partial_buf_size',
    'min_samples',
    'max_samples',
    'channels',
    'frame_count_in',
    'frame_count_out',
    'frame_pool',
    'frame_wanted_out',
    'hw_frames_ctx',
    'reserved',
]
struct_AVFilterLink._fields_ = [
    ('src', POINTER(AVFilterContext)),
    ('srcpad', POINTER(AVFilterPad)),
    ('dst', POINTER(AVFilterContext)),
    ('dstpad', POINTER(AVFilterPad)),
    ('type', enum_AVMediaType),
    ('w', c_int),
    ('h', c_int),
    ('sample_aspect_ratio', AVRational),
    ('channel_layout', c_uint64),
    ('sample_rate', c_int),
    ('format', c_int),
    ('time_base', AVRational),
    ('incfg', AVFilterFormatsConfig),
    ('outcfg', AVFilterFormatsConfig),
    ('init_state', enum_anon_31),
    ('graph', POINTER(struct_AVFilterGraph)),
    ('current_pts', c_int64),
    ('current_pts_us', c_int64),
    ('age_index', c_int),
    ('frame_rate', AVRational),
    ('partial_buf', POINTER(AVFrame)),
    ('partial_buf_size', c_int),
    ('min_samples', c_int),
    ('max_samples', c_int),
    ('channels', c_int),
    ('frame_count_in', c_int64),
    ('frame_count_out', c_int64),
    ('frame_pool', POINTER(None)),
    ('frame_wanted_out', c_int),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('reserved', c_char * int(61440)),
]

# /home/josiah/ctypesgen_test/av/avfilter.h: 668
if _libs["avdevice"].has("avfilter_link", "cdecl"):
    avfilter_link = _libs["avdevice"].get("avfilter_link", "cdecl")
    avfilter_link.argtypes = [POINTER(AVFilterContext), c_uint, POINTER(AVFilterContext), c_uint]
    avfilter_link.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 674
if _libs["avdevice"].has("avfilter_link_free", "cdecl"):
    avfilter_link_free = _libs["avdevice"].get("avfilter_link_free", "cdecl")
    avfilter_link_free.argtypes = [POINTER(POINTER(AVFilterLink))]
    avfilter_link_free.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 682
if _libs["avdevice"].has("avfilter_link_get_channels", "cdecl"):
    avfilter_link_get_channels = _libs["avdevice"].get("avfilter_link_get_channels", "cdecl")
    avfilter_link_get_channels.argtypes = [POINTER(AVFilterLink)]
    avfilter_link_get_channels.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 691
if _libs["avdevice"].has("avfilter_link_set_closed", "cdecl"):
    avfilter_link_set_closed = _libs["avdevice"].get("avfilter_link_set_closed", "cdecl")
    avfilter_link_set_closed.argtypes = [POINTER(AVFilterLink), c_int]
    avfilter_link_set_closed.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 699
if _libs["avdevice"].has("avfilter_config_links", "cdecl"):
    avfilter_config_links = _libs["avdevice"].get("avfilter_config_links", "cdecl")
    avfilter_config_links.argtypes = [POINTER(AVFilterContext)]
    avfilter_config_links.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 708
if _libs["avdevice"].has("avfilter_process_command", "cdecl"):
    avfilter_process_command = _libs["avdevice"].get("avfilter_process_command", "cdecl")
    avfilter_process_command.argtypes = [POINTER(AVFilterContext), String, String, String, c_int, c_int]
    avfilter_process_command.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 719
if _libs["avdevice"].has("av_filter_iterate", "cdecl"):
    av_filter_iterate = _libs["avdevice"].get("av_filter_iterate", "cdecl")
    av_filter_iterate.argtypes = [POINTER(POINTER(None))]
    av_filter_iterate.restype = POINTER(AVFilter)

# /home/josiah/ctypesgen_test/av/avfilter.h: 724
if _libs["avdevice"].has("avfilter_register_all", "cdecl"):
    avfilter_register_all = _libs["avdevice"].get("avfilter_register_all", "cdecl")
    avfilter_register_all.argtypes = []
    avfilter_register_all.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 737
if _libs["avdevice"].has("avfilter_register", "cdecl"):
    avfilter_register = _libs["avdevice"].get("avfilter_register", "cdecl")
    avfilter_register.argtypes = [POINTER(AVFilter)]
    avfilter_register.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 745
if _libs["avdevice"].has("avfilter_next", "cdecl"):
    avfilter_next = _libs["avdevice"].get("avfilter_next", "cdecl")
    avfilter_next.argtypes = [POINTER(AVFilter)]
    avfilter_next.restype = POINTER(AVFilter)

# /home/josiah/ctypesgen_test/av/avfilter.h: 755
if _libs["avdevice"].has("avfilter_get_by_name", "cdecl"):
    avfilter_get_by_name = _libs["avdevice"].get("avfilter_get_by_name", "cdecl")
    avfilter_get_by_name.argtypes = [String]
    avfilter_get_by_name.restype = POINTER(AVFilter)

# /home/josiah/ctypesgen_test/av/avfilter.h: 768
if _libs["avdevice"].has("avfilter_init_str", "cdecl"):
    avfilter_init_str = _libs["avdevice"].get("avfilter_init_str", "cdecl")
    avfilter_init_str.argtypes = [POINTER(AVFilterContext), String]
    avfilter_init_str.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 790
if _libs["avdevice"].has("avfilter_init_dict", "cdecl"):
    avfilter_init_dict = _libs["avdevice"].get("avfilter_init_dict", "cdecl")
    avfilter_init_dict.argtypes = [POINTER(AVFilterContext), POINTER(POINTER(AVDictionary))]
    avfilter_init_dict.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 798
if _libs["avdevice"].has("avfilter_free", "cdecl"):
    avfilter_free = _libs["avdevice"].get("avfilter_free", "cdecl")
    avfilter_free.argtypes = [POINTER(AVFilterContext)]
    avfilter_free.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 809
if _libs["avdevice"].has("avfilter_insert_filter", "cdecl"):
    avfilter_insert_filter = _libs["avdevice"].get("avfilter_insert_filter", "cdecl")
    avfilter_insert_filter.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterContext), c_uint, c_uint]
    avfilter_insert_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 817
if _libs["avdevice"].has("avfilter_get_class", "cdecl"):
    avfilter_get_class = _libs["avdevice"].get("avfilter_get_class", "cdecl")
    avfilter_get_class.argtypes = []
    avfilter_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/avfilter.h: 819
class struct_AVFilterGraphInternal(Structure):
    pass

AVFilterGraphInternal = struct_AVFilterGraphInternal# /home/josiah/ctypesgen_test/av/avfilter.h: 819

avfilter_action_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(None), c_int, c_int)# /home/josiah/ctypesgen_test/av/avfilter.h: 833

avfilter_execute_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(avfilter_action_func), POINTER(None), POINTER(c_int), c_int)# /home/josiah/ctypesgen_test/av/avfilter.h: 847

struct_AVFilterGraph.__slots__ = [
    'av_class',
    'filters',
    'nb_filters',
    'scale_sws_opts',
    'resample_lavr_opts',
    'thread_type',
    'nb_threads',
    'internal',
    'opaque',
    'execute',
    'aresample_swr_opts',
    'sink_links',
    'sink_links_count',
    'disable_auto_convert',
]
struct_AVFilterGraph._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('filters', POINTER(POINTER(AVFilterContext))),
    ('nb_filters', c_uint),
    ('scale_sws_opts', String),
    ('resample_lavr_opts', String),
    ('thread_type', c_int),
    ('nb_threads', c_int),
    ('internal', POINTER(AVFilterGraphInternal)),
    ('opaque', POINTER(None)),
    ('execute', POINTER(avfilter_execute_func)),
    ('aresample_swr_opts', String),
    ('sink_links', POINTER(POINTER(AVFilterLink))),
    ('sink_links_count', c_int),
    ('disable_auto_convert', c_uint),
]

AVFilterGraph = struct_AVFilterGraph# /home/josiah/ctypesgen_test/av/avfilter.h: 920

# /home/josiah/ctypesgen_test/av/avfilter.h: 927
if _libs["avdevice"].has("avfilter_graph_alloc", "cdecl"):
    avfilter_graph_alloc = _libs["avdevice"].get("avfilter_graph_alloc", "cdecl")
    avfilter_graph_alloc.argtypes = []
    avfilter_graph_alloc.restype = POINTER(AVFilterGraph)

# /home/josiah/ctypesgen_test/av/avfilter.h: 943
if _libs["avdevice"].has("avfilter_graph_alloc_filter", "cdecl"):
    avfilter_graph_alloc_filter = _libs["avdevice"].get("avfilter_graph_alloc_filter", "cdecl")
    avfilter_graph_alloc_filter.argtypes = [POINTER(AVFilterGraph), POINTER(AVFilter), String]
    avfilter_graph_alloc_filter.restype = POINTER(AVFilterContext)

# /home/josiah/ctypesgen_test/av/avfilter.h: 955
if _libs["avdevice"].has("avfilter_graph_get_filter", "cdecl"):
    avfilter_graph_get_filter = _libs["avdevice"].get("avfilter_graph_get_filter", "cdecl")
    avfilter_graph_get_filter.argtypes = [POINTER(AVFilterGraph), String]
    avfilter_graph_get_filter.restype = POINTER(AVFilterContext)

# /home/josiah/ctypesgen_test/av/avfilter.h: 970
if _libs["avdevice"].has("avfilter_graph_create_filter", "cdecl"):
    avfilter_graph_create_filter = _libs["avdevice"].get("avfilter_graph_create_filter", "cdecl")
    avfilter_graph_create_filter.argtypes = [POINTER(POINTER(AVFilterContext)), POINTER(AVFilter), String, String, POINTER(None), POINTER(AVFilterGraph)]
    avfilter_graph_create_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 982
if _libs["avdevice"].has("avfilter_graph_set_auto_convert", "cdecl"):
    avfilter_graph_set_auto_convert = _libs["avdevice"].get("avfilter_graph_set_auto_convert", "cdecl")
    avfilter_graph_set_auto_convert.argtypes = [POINTER(AVFilterGraph), c_uint]
    avfilter_graph_set_auto_convert.restype = None

enum_anon_32 = c_int# /home/josiah/ctypesgen_test/av/avfilter.h: 984

AVFILTER_AUTO_CONVERT_ALL = 0# /home/josiah/ctypesgen_test/av/avfilter.h: 984

AVFILTER_AUTO_CONVERT_NONE = (-1)# /home/josiah/ctypesgen_test/av/avfilter.h: 984

# /home/josiah/ctypesgen_test/av/avfilter.h: 996
if _libs["avdevice"].has("avfilter_graph_config", "cdecl"):
    avfilter_graph_config = _libs["avdevice"].get("avfilter_graph_config", "cdecl")
    avfilter_graph_config.argtypes = [POINTER(AVFilterGraph), POINTER(None)]
    avfilter_graph_config.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1002
if _libs["avdevice"].has("avfilter_graph_free", "cdecl"):
    avfilter_graph_free = _libs["avdevice"].get("avfilter_graph_free", "cdecl")
    avfilter_graph_free.argtypes = [POINTER(POINTER(AVFilterGraph))]
    avfilter_graph_free.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 1013
class struct_AVFilterInOut(Structure):
    pass

struct_AVFilterInOut.__slots__ = [
    'name',
    'filter_ctx',
    'pad_idx',
    'next',
]
struct_AVFilterInOut._fields_ = [
    ('name', String),
    ('filter_ctx', POINTER(AVFilterContext)),
    ('pad_idx', c_int),
    ('next', POINTER(struct_AVFilterInOut)),
]

AVFilterInOut = struct_AVFilterInOut# /home/josiah/ctypesgen_test/av/avfilter.h: 1025

# /home/josiah/ctypesgen_test/av/avfilter.h: 1032
if _libs["avdevice"].has("avfilter_inout_alloc", "cdecl"):
    avfilter_inout_alloc = _libs["avdevice"].get("avfilter_inout_alloc", "cdecl")
    avfilter_inout_alloc.argtypes = []
    avfilter_inout_alloc.restype = POINTER(AVFilterInOut)

# /home/josiah/ctypesgen_test/av/avfilter.h: 1038
if _libs["avdevice"].has("avfilter_inout_free", "cdecl"):
    avfilter_inout_free = _libs["avdevice"].get("avfilter_inout_free", "cdecl")
    avfilter_inout_free.argtypes = [POINTER(POINTER(AVFilterInOut))]
    avfilter_inout_free.restype = None

# /home/josiah/ctypesgen_test/av/avfilter.h: 1058
if _libs["avdevice"].has("avfilter_graph_parse", "cdecl"):
    avfilter_graph_parse = _libs["avdevice"].get("avfilter_graph_parse", "cdecl")
    avfilter_graph_parse.argtypes = [POINTER(AVFilterGraph), String, POINTER(AVFilterInOut), POINTER(AVFilterInOut), POINTER(None)]
    avfilter_graph_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1079
if _libs["avdevice"].has("avfilter_graph_parse_ptr", "cdecl"):
    avfilter_graph_parse_ptr = _libs["avdevice"].get("avfilter_graph_parse_ptr", "cdecl")
    avfilter_graph_parse_ptr.argtypes = [POINTER(AVFilterGraph), String, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut)), POINTER(None)]
    avfilter_graph_parse_ptr.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1105
if _libs["avdevice"].has("avfilter_graph_parse2", "cdecl"):
    avfilter_graph_parse2 = _libs["avdevice"].get("avfilter_graph_parse2", "cdecl")
    avfilter_graph_parse2.argtypes = [POINTER(AVFilterGraph), String, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut))]
    avfilter_graph_parse2.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1124
if _libs["avdevice"].has("avfilter_graph_send_command", "cdecl"):
    avfilter_graph_send_command = _libs["avdevice"].get("avfilter_graph_send_command", "cdecl")
    avfilter_graph_send_command.argtypes = [POINTER(AVFilterGraph), String, String, String, String, c_int, c_int]
    avfilter_graph_send_command.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1141
if _libs["avdevice"].has("avfilter_graph_queue_command", "cdecl"):
    avfilter_graph_queue_command = _libs["avdevice"].get("avfilter_graph_queue_command", "cdecl")
    avfilter_graph_queue_command.argtypes = [POINTER(AVFilterGraph), String, String, String, c_int, c_double]
    avfilter_graph_queue_command.restype = c_int

# /home/josiah/ctypesgen_test/av/avfilter.h: 1152
if _libs["avdevice"].has("avfilter_graph_dump", "cdecl"):
    avfilter_graph_dump = _libs["avdevice"].get("avfilter_graph_dump", "cdecl")
    avfilter_graph_dump.argtypes = [POINTER(AVFilterGraph), String]
    if sizeof(c_int) == sizeof(c_void_p):
        avfilter_graph_dump.restype = ReturnString
    else:
        avfilter_graph_dump.restype = String
        avfilter_graph_dump.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avfilter.h: 1172
if _libs["avdevice"].has("avfilter_graph_request_oldest", "cdecl"):
    avfilter_graph_request_oldest = _libs["avdevice"].get("avfilter_graph_request_oldest", "cdecl")
    avfilter_graph_request_oldest.argtypes = [POINTER(AVFilterGraph)]
    avfilter_graph_request_oldest.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 43
if _libs["avcodec"].has("av_strstart", "cdecl"):
    av_strstart = _libs["avcodec"].get("av_strstart", "cdecl")
    av_strstart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_strstart.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 55
if _libs["avcodec"].has("av_stristart", "cdecl"):
    av_stristart = _libs["avcodec"].get("av_stristart", "cdecl")
    av_stristart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_stristart.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 69
if _libs["avcodec"].has("av_stristr", "cdecl"):
    av_stristr = _libs["avcodec"].get("av_stristr", "cdecl")
    av_stristr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_stristr.restype = ReturnString
    else:
        av_stristr.restype = String
        av_stristr.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 84
if _libs["avcodec"].has("av_strnstr", "cdecl"):
    av_strnstr = _libs["avcodec"].get("av_strnstr", "cdecl")
    av_strnstr.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strnstr.restype = ReturnString
    else:
        av_strnstr.restype = String
        av_strnstr.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 101
if _libs["avcodec"].has("av_strlcpy", "cdecl"):
    av_strlcpy = _libs["avcodec"].get("av_strlcpy", "cdecl")
    av_strlcpy.argtypes = [String, String, c_size_t]
    av_strlcpy.restype = c_size_t

# /home/josiah/ctypesgen_test/av/avstring.h: 119
if _libs["avcodec"].has("av_strlcat", "cdecl"):
    av_strlcat = _libs["avcodec"].get("av_strlcat", "cdecl")
    av_strlcat.argtypes = [String, String, c_size_t]
    av_strlcat.restype = c_size_t

# /home/josiah/ctypesgen_test/av/avstring.h: 133
if _libs["avcodec"].has("av_strlcatf", "cdecl"):
    _func = _libs["avcodec"].get("av_strlcatf", "cdecl")
    _restype = c_size_t
    _errcheck = None
    _argtypes = [String, c_size_t, String]
    av_strlcatf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/avstring.h: 143
for _lib in _libs.values():
    try:
        i = (c_size_t).in_dll(_lib, "i")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/avstring.h: 157
if _libs["avcodec"].has("av_asprintf", "cdecl"):
    _func = _libs["avcodec"].get("av_asprintf", "cdecl")
    _restype = String
    _errcheck = None
    _argtypes = [String]
    av_asprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/avstring.h: 165
if _libs["avcodec"].has("av_d2str", "cdecl"):
    av_d2str = _libs["avcodec"].get("av_d2str", "cdecl")
    av_d2str.argtypes = [c_double]
    if sizeof(c_int) == sizeof(c_void_p):
        av_d2str.restype = ReturnString
    else:
        av_d2str.restype = String
        av_d2str.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 182
if _libs["avcodec"].has("av_get_token", "cdecl"):
    av_get_token = _libs["avcodec"].get("av_get_token", "cdecl")
    av_get_token.argtypes = [POINTER(POINTER(c_char)), String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_token.restype = ReturnString
    else:
        av_get_token.restype = String
        av_get_token.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 206
if _libs["avcodec"].has("av_strtok", "cdecl"):
    av_strtok = _libs["avcodec"].get("av_strtok", "cdecl")
    av_strtok.argtypes = [String, String, POINTER(POINTER(c_char))]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strtok.restype = ReturnString
    else:
        av_strtok.restype = String
        av_strtok.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 266
if _libs["avcodec"].has("av_strcasecmp", "cdecl"):
    av_strcasecmp = _libs["avcodec"].get("av_strcasecmp", "cdecl")
    av_strcasecmp.argtypes = [String, String]
    av_strcasecmp.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 272
if _libs["avcodec"].has("av_strncasecmp", "cdecl"):
    av_strncasecmp = _libs["avcodec"].get("av_strncasecmp", "cdecl")
    av_strncasecmp.argtypes = [String, String, c_size_t]
    av_strncasecmp.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 278
if _libs["avcodec"].has("av_strireplace", "cdecl"):
    av_strireplace = _libs["avcodec"].get("av_strireplace", "cdecl")
    av_strireplace.argtypes = [String, String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strireplace.restype = ReturnString
    else:
        av_strireplace.restype = String
        av_strireplace.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/avstring.h: 288
if _libs["avcodec"].has("av_basename", "cdecl"):
    av_basename = _libs["avcodec"].get("av_basename", "cdecl")
    av_basename.argtypes = [String]
    av_basename.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avstring.h: 298
if _libs["avcodec"].has("av_dirname", "cdecl"):
    av_dirname = _libs["avcodec"].get("av_dirname", "cdecl")
    av_dirname.argtypes = [String]
    av_dirname.restype = c_char_p

# /home/josiah/ctypesgen_test/av/avstring.h: 311
if _libs["avcodec"].has("av_match_name", "cdecl"):
    av_match_name = _libs["avcodec"].get("av_match_name", "cdecl")
    av_match_name.argtypes = [String, String]
    av_match_name.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 321
if _libs["avcodec"].has("av_append_path_component", "cdecl"):
    av_append_path_component = _libs["avcodec"].get("av_append_path_component", "cdecl")
    av_append_path_component.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_append_path_component.restype = ReturnString
    else:
        av_append_path_component.restype = String
        av_append_path_component.errcheck = ReturnString

enum_AVEscapeMode = c_int# /home/josiah/ctypesgen_test/av/avstring.h: 323

AV_ESCAPE_MODE_AUTO = 0# /home/josiah/ctypesgen_test/av/avstring.h: 323

AV_ESCAPE_MODE_BACKSLASH = (AV_ESCAPE_MODE_AUTO + 1)# /home/josiah/ctypesgen_test/av/avstring.h: 323

AV_ESCAPE_MODE_QUOTE = (AV_ESCAPE_MODE_BACKSLASH + 1)# /home/josiah/ctypesgen_test/av/avstring.h: 323

AV_ESCAPE_MODE_XML = (AV_ESCAPE_MODE_QUOTE + 1)# /home/josiah/ctypesgen_test/av/avstring.h: 323

# /home/josiah/ctypesgen_test/av/avstring.h: 377
if _libs["avcodec"].has("av_escape", "cdecl"):
    av_escape = _libs["avcodec"].get("av_escape", "cdecl")
    av_escape.argtypes = [POINTER(POINTER(c_char)), String, String, enum_AVEscapeMode, c_int]
    av_escape.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 417
if _libs["avcodec"].has("av_utf8_decode", "cdecl"):
    av_utf8_decode = _libs["avcodec"].get("av_utf8_decode", "cdecl")
    av_utf8_decode.argtypes = [POINTER(c_int32), POINTER(POINTER(c_uint8)), POINTER(c_uint8), c_uint]
    av_utf8_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 425
if _libs["avcodec"].has("av_match_list", "cdecl"):
    av_match_list = _libs["avcodec"].get("av_match_list", "cdecl")
    av_match_list.argtypes = [String, String, c_char]
    av_match_list.restype = c_int

# /home/josiah/ctypesgen_test/av/avstring.h: 431
if _libs["avcodec"].has("av_sscanf", "cdecl"):
    _func = _libs["avcodec"].get("av_sscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    av_sscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/base64.h: 42
if _libs["avcodec"].has("av_base64_decode", "cdecl"):
    av_base64_decode = _libs["avcodec"].get("av_base64_decode", "cdecl")
    av_base64_decode.argtypes = [POINTER(c_uint8), String, c_int]
    av_base64_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/base64.h: 60
if _libs["avcodec"].has("av_base64_encode", "cdecl"):
    av_base64_encode = _libs["avcodec"].get("av_base64_encode", "cdecl")
    av_base64_encode.argtypes = [String, c_int, POINTER(c_uint8), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_base64_encode.restype = ReturnString
    else:
        av_base64_encode.restype = String
        av_base64_encode.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/blowfish.h: 38
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

AVBlowfish = struct_AVBlowfish# /home/josiah/ctypesgen_test/av/blowfish.h: 38

# /home/josiah/ctypesgen_test/av/blowfish.h: 43
if _libs["avcodec"].has("av_blowfish_alloc", "cdecl"):
    av_blowfish_alloc = _libs["avcodec"].get("av_blowfish_alloc", "cdecl")
    av_blowfish_alloc.argtypes = []
    av_blowfish_alloc.restype = POINTER(AVBlowfish)

# /home/josiah/ctypesgen_test/av/blowfish.h: 52
if _libs["avcodec"].has("av_blowfish_init", "cdecl"):
    av_blowfish_init = _libs["avcodec"].get("av_blowfish_init", "cdecl")
    av_blowfish_init.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint8), c_int]
    av_blowfish_init.restype = None

# /home/josiah/ctypesgen_test/av/blowfish.h: 62
if _libs["avcodec"].has("av_blowfish_crypt_ecb", "cdecl"):
    av_blowfish_crypt_ecb = _libs["avcodec"].get("av_blowfish_crypt_ecb", "cdecl")
    av_blowfish_crypt_ecb.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint32), POINTER(c_uint32), c_int]
    av_blowfish_crypt_ecb.restype = None

# /home/josiah/ctypesgen_test/av/blowfish.h: 75
if _libs["avcodec"].has("av_blowfish_crypt", "cdecl"):
    av_blowfish_crypt = _libs["avcodec"].get("av_blowfish_crypt", "cdecl")
    av_blowfish_crypt.argtypes = [POINTER(struct_AVBlowfish), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_blowfish_crypt.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 82
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

AVBPrint = struct_AVBPrint# /home/josiah/ctypesgen_test/av/bprint.h: 82

# /home/josiah/ctypesgen_test/av/bprint.h: 111
if _libs["avcodec"].has("av_bprint_init", "cdecl"):
    av_bprint_init = _libs["avcodec"].get("av_bprint_init", "cdecl")
    av_bprint_init.argtypes = [POINTER(AVBPrint), c_uint, c_uint]
    av_bprint_init.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 122
if _libs["avcodec"].has("av_bprint_init_for_buffer", "cdecl"):
    av_bprint_init_for_buffer = _libs["avcodec"].get("av_bprint_init_for_buffer", "cdecl")
    av_bprint_init_for_buffer.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_init_for_buffer.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 127
if _libs["avcodec"].has("av_bprintf", "cdecl"):
    _func = _libs["avcodec"].get("av_bprintf", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(AVBPrint), String]
    av_bprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/bprint.h: 132
if _libs["avcodec"].has("av_vbprintf", "cdecl"):
    av_vbprintf = _libs["avcodec"].get("av_vbprintf", "cdecl")
    av_vbprintf.argtypes = [POINTER(AVBPrint), String, c_void_p]
    av_vbprintf.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 137
if _libs["avcodec"].has("av_bprint_chars", "cdecl"):
    av_bprint_chars = _libs["avcodec"].get("av_bprint_chars", "cdecl")
    av_bprint_chars.argtypes = [POINTER(AVBPrint), c_char, c_uint]
    av_bprint_chars.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 146
if _libs["avcodec"].has("av_bprint_append_data", "cdecl"):
    av_bprint_append_data = _libs["avcodec"].get("av_bprint_append_data", "cdecl")
    av_bprint_append_data.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_append_data.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 160
if _libs["avcodec"].has("av_bprint_strftime", "cdecl"):
    av_bprint_strftime = _libs["avcodec"].get("av_bprint_strftime", "cdecl")
    av_bprint_strftime.argtypes = [POINTER(AVBPrint), String, POINTER(struct_tm)]
    av_bprint_strftime.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 171
if _libs["avcodec"].has("av_bprint_get_buffer", "cdecl"):
    av_bprint_get_buffer = _libs["avcodec"].get("av_bprint_get_buffer", "cdecl")
    av_bprint_get_buffer.argtypes = [POINTER(AVBPrint), c_uint, POINTER(POINTER(c_ubyte)), POINTER(c_uint)]
    av_bprint_get_buffer.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 177
if _libs["avcodec"].has("av_bprint_clear", "cdecl"):
    av_bprint_clear = _libs["avcodec"].get("av_bprint_clear", "cdecl")
    av_bprint_clear.argtypes = [POINTER(AVBPrint)]
    av_bprint_clear.restype = None

# /home/josiah/ctypesgen_test/av/bprint.h: 201
if _libs["avcodec"].has("av_bprint_finalize", "cdecl"):
    av_bprint_finalize = _libs["avcodec"].get("av_bprint_finalize", "cdecl")
    av_bprint_finalize.argtypes = [POINTER(AVBPrint), POINTER(POINTER(c_char))]
    av_bprint_finalize.restype = c_int

# /home/josiah/ctypesgen_test/av/bprint.h: 216
if _libs["avcodec"].has("av_bprint_escape", "cdecl"):
    av_bprint_escape = _libs["avcodec"].get("av_bprint_escape", "cdecl")
    av_bprint_escape.argtypes = [POINTER(AVBPrint), String, String, enum_AVEscapeMode, c_int]
    av_bprint_escape.restype = None

# /home/josiah/ctypesgen_test/av/buffersink.h: 82
if _libs["avdevice"].has("av_buffersink_get_frame_flags", "cdecl"):
    av_buffersink_get_frame_flags = _libs["avdevice"].get("av_buffersink_get_frame_flags", "cdecl")
    av_buffersink_get_frame_flags.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersink_get_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 104
class struct_AVBufferSinkParams(Structure):
    pass

struct_AVBufferSinkParams.__slots__ = [
    'pixel_fmts',
]
struct_AVBufferSinkParams._fields_ = [
    ('pixel_fmts', POINTER(enum_AVPixelFormat)),
]

AVBufferSinkParams = struct_AVBufferSinkParams# /home/josiah/ctypesgen_test/av/buffersink.h: 104

# /home/josiah/ctypesgen_test/av/buffersink.h: 112
if _libs["avdevice"].has("av_buffersink_params_alloc", "cdecl"):
    av_buffersink_params_alloc = _libs["avdevice"].get("av_buffersink_params_alloc", "cdecl")
    av_buffersink_params_alloc.argtypes = []
    av_buffersink_params_alloc.restype = POINTER(AVBufferSinkParams)

# /home/josiah/ctypesgen_test/av/buffersink.h: 123
class struct_AVABufferSinkParams(Structure):
    pass

struct_AVABufferSinkParams.__slots__ = [
    'sample_fmts',
    'channel_layouts',
    'channel_counts',
    'all_channel_counts',
    'sample_rates',
]
struct_AVABufferSinkParams._fields_ = [
    ('sample_fmts', POINTER(enum_AVSampleFormat)),
    ('channel_layouts', POINTER(c_int64)),
    ('channel_counts', POINTER(c_int)),
    ('all_channel_counts', c_int),
    ('sample_rates', POINTER(c_int)),
]

AVABufferSinkParams = struct_AVABufferSinkParams# /home/josiah/ctypesgen_test/av/buffersink.h: 123

# /home/josiah/ctypesgen_test/av/buffersink.h: 131
if _libs["avdevice"].has("av_abuffersink_params_alloc", "cdecl"):
    av_abuffersink_params_alloc = _libs["avdevice"].get("av_abuffersink_params_alloc", "cdecl")
    av_abuffersink_params_alloc.argtypes = []
    av_abuffersink_params_alloc.restype = POINTER(AVABufferSinkParams)

# /home/josiah/ctypesgen_test/av/buffersink.h: 141
if _libs["avdevice"].has("av_buffersink_set_frame_size", "cdecl"):
    av_buffersink_set_frame_size = _libs["avdevice"].get("av_buffersink_set_frame_size", "cdecl")
    av_buffersink_set_frame_size.argtypes = [POINTER(AVFilterContext), c_uint]
    av_buffersink_set_frame_size.restype = None

# /home/josiah/ctypesgen_test/av/buffersink.h: 149
if _libs["avdevice"].has("av_buffersink_get_type", "cdecl"):
    av_buffersink_get_type = _libs["avdevice"].get("av_buffersink_get_type", "cdecl")
    av_buffersink_get_type.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_type.restype = enum_AVMediaType

# /home/josiah/ctypesgen_test/av/buffersink.h: 150
if _libs["avdevice"].has("av_buffersink_get_time_base", "cdecl"):
    av_buffersink_get_time_base = _libs["avdevice"].get("av_buffersink_get_time_base", "cdecl")
    av_buffersink_get_time_base.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_time_base.restype = AVRational

# /home/josiah/ctypesgen_test/av/buffersink.h: 151
if _libs["avdevice"].has("av_buffersink_get_format", "cdecl"):
    av_buffersink_get_format = _libs["avdevice"].get("av_buffersink_get_format", "cdecl")
    av_buffersink_get_format.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_format.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 153
if _libs["avdevice"].has("av_buffersink_get_frame_rate", "cdecl"):
    av_buffersink_get_frame_rate = _libs["avdevice"].get("av_buffersink_get_frame_rate", "cdecl")
    av_buffersink_get_frame_rate.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_frame_rate.restype = AVRational

# /home/josiah/ctypesgen_test/av/buffersink.h: 154
if _libs["avdevice"].has("av_buffersink_get_w", "cdecl"):
    av_buffersink_get_w = _libs["avdevice"].get("av_buffersink_get_w", "cdecl")
    av_buffersink_get_w.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_w.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 155
if _libs["avdevice"].has("av_buffersink_get_h", "cdecl"):
    av_buffersink_get_h = _libs["avdevice"].get("av_buffersink_get_h", "cdecl")
    av_buffersink_get_h.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_h.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 156
if _libs["avdevice"].has("av_buffersink_get_sample_aspect_ratio", "cdecl"):
    av_buffersink_get_sample_aspect_ratio = _libs["avdevice"].get("av_buffersink_get_sample_aspect_ratio", "cdecl")
    av_buffersink_get_sample_aspect_ratio.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_sample_aspect_ratio.restype = AVRational

# /home/josiah/ctypesgen_test/av/buffersink.h: 158
if _libs["avdevice"].has("av_buffersink_get_channels", "cdecl"):
    av_buffersink_get_channels = _libs["avdevice"].get("av_buffersink_get_channels", "cdecl")
    av_buffersink_get_channels.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_channels.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 159
if _libs["avdevice"].has("av_buffersink_get_channel_layout", "cdecl"):
    av_buffersink_get_channel_layout = _libs["avdevice"].get("av_buffersink_get_channel_layout", "cdecl")
    av_buffersink_get_channel_layout.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_channel_layout.restype = c_uint64

# /home/josiah/ctypesgen_test/av/buffersink.h: 160
if _libs["avdevice"].has("av_buffersink_get_sample_rate", "cdecl"):
    av_buffersink_get_sample_rate = _libs["avdevice"].get("av_buffersink_get_sample_rate", "cdecl")
    av_buffersink_get_sample_rate.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_sample_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 162
if _libs["avdevice"].has("av_buffersink_get_hw_frames_ctx", "cdecl"):
    av_buffersink_get_hw_frames_ctx = _libs["avdevice"].get("av_buffersink_get_hw_frames_ctx", "cdecl")
    av_buffersink_get_hw_frames_ctx.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_hw_frames_ctx.restype = POINTER(AVBufferRef)

# /home/josiah/ctypesgen_test/av/buffersink.h: 180
if _libs["avdevice"].has("av_buffersink_get_frame", "cdecl"):
    av_buffersink_get_frame = _libs["avdevice"].get("av_buffersink_get_frame", "cdecl")
    av_buffersink_get_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersink_get_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersink.h: 199
if _libs["avdevice"].has("av_buffersink_get_samples", "cdecl"):
    av_buffersink_get_samples = _libs["avdevice"].get("av_buffersink_get_samples", "cdecl")
    av_buffersink_get_samples.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersink_get_samples.restype = c_int

enum_anon_33 = c_int# /home/josiah/ctypesgen_test/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_NO_CHECK_FORMAT = 1# /home/josiah/ctypesgen_test/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_PUSH = 4# /home/josiah/ctypesgen_test/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_KEEP_REF = 8# /home/josiah/ctypesgen_test/av/buffersrc.h: 36

# /home/josiah/ctypesgen_test/av/buffersrc.h: 64
if _libs["avdevice"].has("av_buffersrc_get_nb_failed_requests", "cdecl"):
    av_buffersrc_get_nb_failed_requests = _libs["avdevice"].get("av_buffersrc_get_nb_failed_requests", "cdecl")
    av_buffersrc_get_nb_failed_requests.argtypes = [POINTER(AVFilterContext)]
    av_buffersrc_get_nb_failed_requests.restype = c_uint

# /home/josiah/ctypesgen_test/av/buffersrc.h: 117
class struct_AVBufferSrcParameters(Structure):
    pass

struct_AVBufferSrcParameters.__slots__ = [
    'format',
    'time_base',
    'width',
    'height',
    'sample_aspect_ratio',
    'frame_rate',
    'hw_frames_ctx',
    'sample_rate',
    'channel_layout',
]
struct_AVBufferSrcParameters._fields_ = [
    ('format', c_int),
    ('time_base', AVRational),
    ('width', c_int),
    ('height', c_int),
    ('sample_aspect_ratio', AVRational),
    ('frame_rate', AVRational),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('sample_rate', c_int),
    ('channel_layout', c_uint64),
]

AVBufferSrcParameters = struct_AVBufferSrcParameters# /home/josiah/ctypesgen_test/av/buffersrc.h: 117

# /home/josiah/ctypesgen_test/av/buffersrc.h: 123
if _libs["avdevice"].has("av_buffersrc_parameters_alloc", "cdecl"):
    av_buffersrc_parameters_alloc = _libs["avdevice"].get("av_buffersrc_parameters_alloc", "cdecl")
    av_buffersrc_parameters_alloc.argtypes = []
    av_buffersrc_parameters_alloc.restype = POINTER(AVBufferSrcParameters)

# /home/josiah/ctypesgen_test/av/buffersrc.h: 138
if _libs["avdevice"].has("av_buffersrc_parameters_set", "cdecl"):
    av_buffersrc_parameters_set = _libs["avdevice"].get("av_buffersrc_parameters_set", "cdecl")
    av_buffersrc_parameters_set.argtypes = [POINTER(AVFilterContext), POINTER(AVBufferSrcParameters)]
    av_buffersrc_parameters_set.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersrc.h: 154
if _libs["avdevice"].has("av_buffersrc_write_frame", "cdecl"):
    av_buffersrc_write_frame = _libs["avdevice"].get("av_buffersrc_write_frame", "cdecl")
    av_buffersrc_write_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersrc_write_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersrc.h: 175
if _libs["avdevice"].has("av_buffersrc_add_frame", "cdecl"):
    av_buffersrc_add_frame = _libs["avdevice"].get("av_buffersrc_add_frame", "cdecl")
    av_buffersrc_add_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersrc_add_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersrc.h: 193
if _libs["avdevice"].has("av_buffersrc_add_frame_flags", "cdecl"):
    av_buffersrc_add_frame_flags = _libs["avdevice"].get("av_buffersrc_add_frame_flags", "cdecl")
    av_buffersrc_add_frame_flags.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersrc_add_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/buffersrc.h: 203
if _libs["avdevice"].has("av_buffersrc_close", "cdecl"):
    av_buffersrc_close = _libs["avdevice"].get("av_buffersrc_close", "cdecl")
    av_buffersrc_close.argtypes = [POINTER(AVFilterContext), c_int64, c_uint]
    av_buffersrc_close.restype = c_int

# /home/josiah/ctypesgen_test/av/camellia.h: 36
try:
    av_camellia_size = (c_int).in_dll(_libs["avcodec"], "av_camellia_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/camellia.h: 38
class struct_AVCAMELLIA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/camellia.h: 44
if _libs["avcodec"].has("av_camellia_alloc", "cdecl"):
    av_camellia_alloc = _libs["avcodec"].get("av_camellia_alloc", "cdecl")
    av_camellia_alloc.argtypes = []
    av_camellia_alloc.restype = POINTER(struct_AVCAMELLIA)

# /home/josiah/ctypesgen_test/av/camellia.h: 53
if _libs["avcodec"].has("av_camellia_init", "cdecl"):
    av_camellia_init = _libs["avcodec"].get("av_camellia_init", "cdecl")
    av_camellia_init.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(c_uint8), c_int]
    av_camellia_init.restype = c_int

# /home/josiah/ctypesgen_test/av/camellia.h: 65
if _libs["avcodec"].has("av_camellia_crypt", "cdecl"):
    av_camellia_crypt = _libs["avcodec"].get("av_camellia_crypt", "cdecl")
    av_camellia_crypt.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_camellia_crypt.restype = None

# /home/josiah/ctypesgen_test/av/cast5.h: 36
try:
    av_cast5_size = (c_int).in_dll(_libs["avcodec"], "av_cast5_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/cast5.h: 38
class struct_AVCAST5(Structure):
    pass

# /home/josiah/ctypesgen_test/av/cast5.h: 44
if _libs["avcodec"].has("av_cast5_alloc", "cdecl"):
    av_cast5_alloc = _libs["avcodec"].get("av_cast5_alloc", "cdecl")
    av_cast5_alloc.argtypes = []
    av_cast5_alloc.restype = POINTER(struct_AVCAST5)

# /home/josiah/ctypesgen_test/av/cast5.h: 53
if _libs["avcodec"].has("av_cast5_init", "cdecl"):
    av_cast5_init = _libs["avcodec"].get("av_cast5_init", "cdecl")
    av_cast5_init.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), c_int]
    av_cast5_init.restype = c_int

# /home/josiah/ctypesgen_test/av/cast5.h: 64
if _libs["avcodec"].has("av_cast5_crypt", "cdecl"):
    av_cast5_crypt = _libs["avcodec"].get("av_cast5_crypt", "cdecl")
    av_cast5_crypt.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), POINTER(c_uint8), c_int, c_int]
    av_cast5_crypt.restype = None

# /home/josiah/ctypesgen_test/av/cast5.h: 76
if _libs["avcodec"].has("av_cast5_crypt2", "cdecl"):
    av_cast5_crypt2 = _libs["avcodec"].get("av_cast5_crypt2", "cdecl")
    av_cast5_crypt2.argtypes = [POINTER(struct_AVCAST5), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_cast5_crypt2.restype = None

AVCRC = c_uint32# /home/josiah/ctypesgen_test/av/crc.h: 47

enum_anon_34 = c_int# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_8_ATM = 0# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_16_ANSI = (AV_CRC_8_ATM + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_16_CCITT = (AV_CRC_16_ANSI + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_32_IEEE = (AV_CRC_16_CCITT + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_32_IEEE_LE = (AV_CRC_32_IEEE + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_16_ANSI_LE = (AV_CRC_32_IEEE_LE + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_24_IEEE = (AV_CRC_16_ANSI_LE + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_8_EBU = (AV_CRC_24_IEEE + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AV_CRC_MAX = (AV_CRC_8_EBU + 1)# /home/josiah/ctypesgen_test/av/crc.h: 59

AVCRCId = enum_anon_34# /home/josiah/ctypesgen_test/av/crc.h: 59

# /home/josiah/ctypesgen_test/av/crc.h: 77
if _libs["avcodec"].has("av_crc_init", "cdecl"):
    av_crc_init = _libs["avcodec"].get("av_crc_init", "cdecl")
    av_crc_init.argtypes = [POINTER(AVCRC), c_int, c_int, c_uint32, c_int]
    av_crc_init.restype = c_int

# /home/josiah/ctypesgen_test/av/crc.h: 84
if _libs["avcodec"].has("av_crc_get_table", "cdecl"):
    av_crc_get_table = _libs["avcodec"].get("av_crc_get_table", "cdecl")
    av_crc_get_table.argtypes = [AVCRCId]
    av_crc_get_table.restype = POINTER(AVCRC)

# /home/josiah/ctypesgen_test/av/crc.h: 93
if _libs["avcodec"].has("av_crc", "cdecl"):
    av_crc = _libs["avcodec"].get("av_crc", "cdecl")
    av_crc.argtypes = [POINTER(AVCRC), c_uint32, POINTER(c_uint8), c_size_t]
    av_crc.restype = c_uint32

# /home/josiah/ctypesgen_test/av/des.h: 36
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

AVDES = struct_AVDES# /home/josiah/ctypesgen_test/av/des.h: 36

# /home/josiah/ctypesgen_test/av/des.h: 41
if _libs["avcodec"].has("av_des_alloc", "cdecl"):
    av_des_alloc = _libs["avcodec"].get("av_des_alloc", "cdecl")
    av_des_alloc.argtypes = []
    av_des_alloc.restype = POINTER(AVDES)

# /home/josiah/ctypesgen_test/av/des.h: 50
if _libs["avcodec"].has("av_des_init", "cdecl"):
    av_des_init = _libs["avcodec"].get("av_des_init", "cdecl")
    av_des_init.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), c_int, c_int]
    av_des_init.restype = c_int

# /home/josiah/ctypesgen_test/av/des.h: 62
if _libs["avcodec"].has("av_des_crypt", "cdecl"):
    av_des_crypt = _libs["avcodec"].get("av_des_crypt", "cdecl")
    av_des_crypt.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_des_crypt.restype = None

# /home/josiah/ctypesgen_test/av/des.h: 71
if _libs["avcodec"].has("av_des_mac", "cdecl"):
    av_des_mac = _libs["avcodec"].get("av_des_mac", "cdecl")
    av_des_mac.argtypes = [POINTER(struct_AVDES), POINTER(c_uint8), POINTER(c_uint8), c_int]
    av_des_mac.restype = None

enum_DiracParseCodes = c_int# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_SEQ_HEADER = 0# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_END_SEQ = 16# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_AUX = 32# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_PAD = 48# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_PICTURE_CODED = 8# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_PICTURE_RAW = 72# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_PICTURE_LOW_DEL = 200# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_PICTURE_HQ = 232# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTER_NOREF_CO1 = 10# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTER_NOREF_CO2 = 9# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTER_REF_CO1 = 13# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTER_REF_CO2 = 14# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_CO = 12# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_RAW = 76# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_PICT = 204# /home/josiah/ctypesgen_test/av/dirac.h: 57

DIRAC_PCODE_MAGIC = 1111638852# /home/josiah/ctypesgen_test/av/dirac.h: 57

# /home/josiah/ctypesgen_test/av/dirac.h: 79
class struct_DiracVersionInfo(Structure):
    pass

struct_DiracVersionInfo.__slots__ = [
    'major',
    'minor',
]
struct_DiracVersionInfo._fields_ = [
    ('major', c_int),
    ('minor', c_int),
]

DiracVersionInfo = struct_DiracVersionInfo# /home/josiah/ctypesgen_test/av/dirac.h: 79

# /home/josiah/ctypesgen_test/av/dirac.h: 114
class struct_AVDiracSeqHeader(Structure):
    pass

struct_AVDiracSeqHeader.__slots__ = [
    'width',
    'height',
    'chroma_format',
    'interlaced',
    'top_field_first',
    'frame_rate_index',
    'aspect_ratio_index',
    'clean_width',
    'clean_height',
    'clean_left_offset',
    'clean_right_offset',
    'pixel_range_index',
    'color_spec_index',
    'profile',
    'level',
    'framerate',
    'sample_aspect_ratio',
    'pix_fmt',
    'color_range',
    'color_primaries',
    'color_trc',
    'colorspace',
    'version',
    'bit_depth',
]
struct_AVDiracSeqHeader._fields_ = [
    ('width', c_uint),
    ('height', c_uint),
    ('chroma_format', c_uint8),
    ('interlaced', c_uint8),
    ('top_field_first', c_uint8),
    ('frame_rate_index', c_uint8),
    ('aspect_ratio_index', c_uint8),
    ('clean_width', c_uint16),
    ('clean_height', c_uint16),
    ('clean_left_offset', c_uint16),
    ('clean_right_offset', c_uint16),
    ('pixel_range_index', c_uint8),
    ('color_spec_index', c_uint8),
    ('profile', c_int),
    ('level', c_int),
    ('framerate', AVRational),
    ('sample_aspect_ratio', AVRational),
    ('pix_fmt', enum_AVPixelFormat),
    ('color_range', enum_AVColorRange),
    ('color_primaries', enum_AVColorPrimaries),
    ('color_trc', enum_AVColorTransferCharacteristic),
    ('colorspace', enum_AVColorSpace),
    ('version', DiracVersionInfo),
    ('bit_depth', c_int),
]

AVDiracSeqHeader = struct_AVDiracSeqHeader# /home/josiah/ctypesgen_test/av/dirac.h: 114

# /home/josiah/ctypesgen_test/av/dirac.h: 127
if _libs["avcodec"].has("av_dirac_parse_sequence_header", "cdecl"):
    av_dirac_parse_sequence_header = _libs["avcodec"].get("av_dirac_parse_sequence_header", "cdecl")
    av_dirac_parse_sequence_header.argtypes = [POINTER(POINTER(AVDiracSeqHeader)), POINTER(c_uint8), c_size_t, POINTER(None)]
    av_dirac_parse_sequence_header.restype = c_int

# /home/josiah/ctypesgen_test/av/display.h: 88
if _libs["avcodec"].has("av_display_rotation_get", "cdecl"):
    av_display_rotation_get = _libs["avcodec"].get("av_display_rotation_get", "cdecl")
    av_display_rotation_get.argtypes = [c_int32 * int(9)]
    av_display_rotation_get.restype = c_double

# /home/josiah/ctypesgen_test/av/display.h: 98
if _libs["avcodec"].has("av_display_rotation_set", "cdecl"):
    av_display_rotation_set = _libs["avcodec"].get("av_display_rotation_set", "cdecl")
    av_display_rotation_set.argtypes = [c_int32 * int(9), c_double]
    av_display_rotation_set.restype = None

# /home/josiah/ctypesgen_test/av/display.h: 107
if _libs["avcodec"].has("av_display_matrix_flip", "cdecl"):
    av_display_matrix_flip = _libs["avcodec"].get("av_display_matrix_flip", "cdecl")
    av_display_matrix_flip.argtypes = [c_int32 * int(9), c_int, c_int]
    av_display_matrix_flip.restype = None

# /home/josiah/ctypesgen_test/av/dovi_meta.h: 60
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

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /home/josiah/ctypesgen_test/av/dovi_meta.h: 60

# /home/josiah/ctypesgen_test/av/dovi_meta.h: 68
if _libs["avcodec"].has("av_dovi_alloc", "cdecl"):
    av_dovi_alloc = _libs["avcodec"].get("av_dovi_alloc", "cdecl")
    av_dovi_alloc.argtypes = [POINTER(c_size_t)]
    av_dovi_alloc.restype = POINTER(AVDOVIDecoderConfigurationRecord)

enum_AVDownmixType = c_int# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_LORO = (AV_DOWNMIX_TYPE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_LTRT = (AV_DOWNMIX_TYPE_LORO + 1)# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_DPLII = (AV_DOWNMIX_TYPE_LTRT + 1)# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_NB = (AV_DOWNMIX_TYPE_DPLII + 1)# /home/josiah/ctypesgen_test/av/downmix_info.h: 44

# /home/josiah/ctypesgen_test/av/downmix_info.h: 93
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

AVDownmixInfo = struct_AVDownmixInfo# /home/josiah/ctypesgen_test/av/downmix_info.h: 93

# /home/josiah/ctypesgen_test/av/downmix_info.h: 105
if _libs["avcodec"].has("av_downmix_info_update_side_data", "cdecl"):
    av_downmix_info_update_side_data = _libs["avcodec"].get("av_downmix_info_update_side_data", "cdecl")
    av_downmix_info_update_side_data.argtypes = [POINTER(AVFrame)]
    av_downmix_info_update_side_data.restype = POINTER(AVDownmixInfo)

# /home/josiah/ctypesgen_test/av/dv_profile.h: 59
class struct_AVDVProfile(Structure):
    pass

struct_AVDVProfile.__slots__ = [
    'dsf',
    'video_stype',
    'frame_size',
    'difseg_size',
    'n_difchan',
    'time_base',
    'ltc_divisor',
    'height',
    'width',
    'sar',
    'pix_fmt',
    'bpm',
    'block_sizes',
    'audio_stride',
    'audio_min_samples',
    'audio_samples_dist',
    'audio_shuffle',
]
struct_AVDVProfile._fields_ = [
    ('dsf', c_int),
    ('video_stype', c_int),
    ('frame_size', c_int),
    ('difseg_size', c_int),
    ('n_difchan', c_int),
    ('time_base', AVRational),
    ('ltc_divisor', c_int),
    ('height', c_int),
    ('width', c_int),
    ('sar', AVRational * int(2)),
    ('pix_fmt', enum_AVPixelFormat),
    ('bpm', c_int),
    ('block_sizes', POINTER(c_uint8)),
    ('audio_stride', c_int),
    ('audio_min_samples', c_int * int(3)),
    ('audio_samples_dist', c_int * int(5)),
    ('audio_shuffle', POINTER(c_uint8 * int(9))),
]

AVDVProfile = struct_AVDVProfile# /home/josiah/ctypesgen_test/av/dv_profile.h: 59

# /home/josiah/ctypesgen_test/av/dv_profile.h: 69
if _libs["avcodec"].has("av_dv_frame_profile", "cdecl"):
    av_dv_frame_profile = _libs["avcodec"].get("av_dv_frame_profile", "cdecl")
    av_dv_frame_profile.argtypes = [POINTER(AVDVProfile), POINTER(c_uint8), c_uint]
    av_dv_frame_profile.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/dv_profile.h: 75
if _libs["avcodec"].has("av_dv_codec_profile", "cdecl"):
    av_dv_codec_profile = _libs["avcodec"].get("av_dv_codec_profile", "cdecl")
    av_dv_codec_profile.argtypes = [c_int, c_int, enum_AVPixelFormat]
    av_dv_codec_profile.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/dv_profile.h: 81
if _libs["avcodec"].has("av_dv_codec_profile2", "cdecl"):
    av_dv_codec_profile2 = _libs["avcodec"].get("av_dv_codec_profile2", "cdecl")
    av_dv_codec_profile2.argtypes = [c_int, c_int, enum_AVPixelFormat, AVRational]
    av_dv_codec_profile2.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 35
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

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 35

# /home/josiah/ctypesgen_test/av/encryption_info.h: 81
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

AVEncryptionInfo = struct_AVEncryptionInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 81

# /home/josiah/ctypesgen_test/av/encryption_info.h: 88
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

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 123

# /home/josiah/ctypesgen_test/av/encryption_info.h: 136
if _libs["avcodec"].has("av_encryption_info_alloc", "cdecl"):
    av_encryption_info_alloc = _libs["avcodec"].get("av_encryption_info_alloc", "cdecl")
    av_encryption_info_alloc.argtypes = [c_uint32, c_uint32, c_uint32]
    av_encryption_info_alloc.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 142
if _libs["avcodec"].has("av_encryption_info_clone", "cdecl"):
    av_encryption_info_clone = _libs["avcodec"].get("av_encryption_info_clone", "cdecl")
    av_encryption_info_clone.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_clone.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 148
if _libs["avcodec"].has("av_encryption_info_free", "cdecl"):
    av_encryption_info_free = _libs["avcodec"].get("av_encryption_info_free", "cdecl")
    av_encryption_info_free.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_free.restype = None

# /home/josiah/ctypesgen_test/av/encryption_info.h: 157
if _libs["avcodec"].has("av_encryption_info_get_side_data", "cdecl"):
    av_encryption_info_get_side_data = _libs["avcodec"].get("av_encryption_info_get_side_data", "cdecl")
    av_encryption_info_get_side_data.argtypes = [POINTER(c_uint8), c_size_t]
    av_encryption_info_get_side_data.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 166
if _libs["avcodec"].has("av_encryption_info_add_side_data", "cdecl"):
    av_encryption_info_add_side_data = _libs["avcodec"].get("av_encryption_info_add_side_data", "cdecl")
    av_encryption_info_add_side_data.argtypes = [POINTER(AVEncryptionInfo), POINTER(c_size_t)]
    av_encryption_info_add_side_data.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 176
if _libs["avcodec"].has("av_encryption_init_info_alloc", "cdecl"):
    av_encryption_init_info_alloc = _libs["avcodec"].get("av_encryption_init_info_alloc", "cdecl")
    av_encryption_init_info_alloc.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
    av_encryption_init_info_alloc.restype = POINTER(AVEncryptionInitInfo)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 183
if _libs["avcodec"].has("av_encryption_init_info_free", "cdecl"):
    av_encryption_init_info_free = _libs["avcodec"].get("av_encryption_init_info_free", "cdecl")
    av_encryption_init_info_free.argtypes = [POINTER(AVEncryptionInitInfo)]
    av_encryption_init_info_free.restype = None

# /home/josiah/ctypesgen_test/av/encryption_info.h: 192
if _libs["avcodec"].has("av_encryption_init_info_get_side_data", "cdecl"):
    av_encryption_init_info_get_side_data = _libs["avcodec"].get("av_encryption_init_info_get_side_data", "cdecl")
    av_encryption_init_info_get_side_data.argtypes = [POINTER(c_uint8), c_size_t]
    av_encryption_init_info_get_side_data.restype = POINTER(AVEncryptionInitInfo)

# /home/josiah/ctypesgen_test/av/encryption_info.h: 202
if _libs["avcodec"].has("av_encryption_init_info_add_side_data", "cdecl"):
    av_encryption_init_info_add_side_data = _libs["avcodec"].get("av_encryption_init_info_add_side_data", "cdecl")
    av_encryption_init_info_add_side_data.argtypes = [POINTER(AVEncryptionInitInfo), POINTER(c_size_t)]
    av_encryption_init_info_add_side_data.restype = POINTER(c_uint8)

# /home/josiah/ctypesgen_test/av/eval.h: 31
class struct_AVExpr(Structure):
    pass

AVExpr = struct_AVExpr# /home/josiah/ctypesgen_test/av/eval.h: 31

# /home/josiah/ctypesgen_test/av/eval.h: 51
if _libs["avcodec"].has("av_expr_parse_and_eval", "cdecl"):
    av_expr_parse_and_eval = _libs["avcodec"].get("av_expr_parse_and_eval", "cdecl")
    av_expr_parse_and_eval.argtypes = [POINTER(c_double), String, POINTER(POINTER(c_char)), POINTER(c_double), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), POINTER(None), c_int, POINTER(None)]
    av_expr_parse_and_eval.restype = c_int

# /home/josiah/ctypesgen_test/av/eval.h: 74
if _libs["avcodec"].has("av_expr_parse", "cdecl"):
    av_expr_parse = _libs["avcodec"].get("av_expr_parse", "cdecl")
    av_expr_parse.argtypes = [POINTER(POINTER(AVExpr)), String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), c_int, POINTER(None)]
    av_expr_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/eval.h: 87
if _libs["avcodec"].has("av_expr_eval", "cdecl"):
    av_expr_eval = _libs["avcodec"].get("av_expr_eval", "cdecl")
    av_expr_eval.argtypes = [POINTER(AVExpr), POINTER(c_double), POINTER(None)]
    av_expr_eval.restype = c_double

# /home/josiah/ctypesgen_test/av/eval.h: 97
if _libs["avcodec"].has("av_expr_count_vars", "cdecl"):
    av_expr_count_vars = _libs["avcodec"].get("av_expr_count_vars", "cdecl")
    av_expr_count_vars.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int]
    av_expr_count_vars.restype = c_int

# /home/josiah/ctypesgen_test/av/eval.h: 111
if _libs["avcodec"].has("av_expr_count_func", "cdecl"):
    av_expr_count_func = _libs["avcodec"].get("av_expr_count_func", "cdecl")
    av_expr_count_func.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int, c_int]
    av_expr_count_func.restype = c_int

# /home/josiah/ctypesgen_test/av/eval.h: 116
if _libs["avcodec"].has("av_expr_free", "cdecl"):
    av_expr_free = _libs["avcodec"].get("av_expr_free", "cdecl")
    av_expr_free.argtypes = [POINTER(AVExpr)]
    av_expr_free.restype = None

# /home/josiah/ctypesgen_test/av/eval.h: 135
if _libs["avcodec"].has("av_strtod", "cdecl"):
    av_strtod = _libs["avcodec"].get("av_strtod", "cdecl")
    av_strtod.argtypes = [String, POINTER(POINTER(c_char))]
    av_strtod.restype = c_double

# /home/josiah/ctypesgen_test/av/file.h: 46
if _libs["avcodec"].has("av_file_map", "cdecl"):
    av_file_map = _libs["avcodec"].get("av_file_map", "cdecl")
    av_file_map.argtypes = [String, POINTER(POINTER(c_uint8)), POINTER(c_size_t), c_int, POINTER(None)]
    av_file_map.restype = c_int

# /home/josiah/ctypesgen_test/av/file.h: 55
if _libs["avcodec"].has("av_file_unmap", "cdecl"):
    av_file_unmap = _libs["avcodec"].get("av_file_unmap", "cdecl")
    av_file_unmap.argtypes = [POINTER(c_uint8), c_size_t]
    av_file_unmap.restype = None

# /home/josiah/ctypesgen_test/av/file.h: 69
if _libs["avcodec"].has("av_tempfile", "cdecl"):
    av_tempfile = _libs["avcodec"].get("av_tempfile", "cdecl")
    av_tempfile.argtypes = [String, POINTER(POINTER(c_char)), c_int, POINTER(None)]
    av_tempfile.restype = c_int

enum_AVFilmGrainParamsType = c_int# /home/josiah/ctypesgen_test/av/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_NONE = 0# /home/josiah/ctypesgen_test/av/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_AV1 = (AV_FILM_GRAIN_PARAMS_NONE + 1)# /home/josiah/ctypesgen_test/av/film_grain_params.h: 24

# /home/josiah/ctypesgen_test/av/film_grain_params.h: 118
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

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /home/josiah/ctypesgen_test/av/film_grain_params.h: 118

# /home/josiah/ctypesgen_test/av/film_grain_params.h: 144
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'aom',
]
union_anon_35._fields_ = [
    ('aom', AVFilmGrainAOMParams),
]

# /home/josiah/ctypesgen_test/av/film_grain_params.h: 147
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
    ('codec', union_anon_35),
]

AVFilmGrainParams = struct_AVFilmGrainParams# /home/josiah/ctypesgen_test/av/film_grain_params.h: 147

# /home/josiah/ctypesgen_test/av/film_grain_params.h: 157
if _libs["avcodec"].has("av_film_grain_params_alloc", "cdecl"):
    av_film_grain_params_alloc = _libs["avcodec"].get("av_film_grain_params_alloc", "cdecl")
    av_film_grain_params_alloc.argtypes = [POINTER(c_size_t)]
    av_film_grain_params_alloc.restype = POINTER(AVFilmGrainParams)

# /home/josiah/ctypesgen_test/av/film_grain_params.h: 166
if _libs["avcodec"].has("av_film_grain_params_create_side_data", "cdecl"):
    av_film_grain_params_create_side_data = _libs["avcodec"].get("av_film_grain_params_create_side_data", "cdecl")
    av_film_grain_params_create_side_data.argtypes = [POINTER(AVFrame)]
    av_film_grain_params_create_side_data.restype = POINTER(AVFilmGrainParams)

# /home/josiah/ctypesgen_test/av/hash.h: 117
class struct_AVHashContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/hash.h: 127
if _libs["avcodec"].has("av_hash_alloc", "cdecl"):
    av_hash_alloc = _libs["avcodec"].get("av_hash_alloc", "cdecl")
    av_hash_alloc.argtypes = [POINTER(POINTER(struct_AVHashContext)), String]
    av_hash_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/hash.h: 137
if _libs["avcodec"].has("av_hash_names", "cdecl"):
    av_hash_names = _libs["avcodec"].get("av_hash_names", "cdecl")
    av_hash_names.argtypes = [c_int]
    av_hash_names.restype = c_char_p

# /home/josiah/ctypesgen_test/av/hash.h: 142
if _libs["avcodec"].has("av_hash_get_name", "cdecl"):
    av_hash_get_name = _libs["avcodec"].get("av_hash_get_name", "cdecl")
    av_hash_get_name.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/hash.h: 169
if _libs["avcodec"].has("av_hash_get_size", "cdecl"):
    av_hash_get_size = _libs["avcodec"].get("av_hash_get_size", "cdecl")
    av_hash_get_size.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_size.restype = c_int

# /home/josiah/ctypesgen_test/av/hash.h: 176
if _libs["avcodec"].has("av_hash_init", "cdecl"):
    av_hash_init = _libs["avcodec"].get("av_hash_init", "cdecl")
    av_hash_init.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_init.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 186
if _libs["avcodec"].has("av_hash_update", "cdecl"):
    av_hash_update = _libs["avcodec"].get("av_hash_update", "cdecl")
    av_hash_update.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_update.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 205
if _libs["avcodec"].has("av_hash_final", "cdecl"):
    av_hash_final = _libs["avcodec"].get("av_hash_final", "cdecl")
    av_hash_final.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8)]
    av_hash_final.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 220
if _libs["avcodec"].has("av_hash_final_bin", "cdecl"):
    av_hash_final_bin = _libs["avcodec"].get("av_hash_final_bin", "cdecl")
    av_hash_final_bin.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_bin.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 238
if _libs["avcodec"].has("av_hash_final_hex", "cdecl"):
    av_hash_final_hex = _libs["avcodec"].get("av_hash_final_hex", "cdecl")
    av_hash_final_hex.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_hex.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 256
if _libs["avcodec"].has("av_hash_final_b64", "cdecl"):
    av_hash_final_b64 = _libs["avcodec"].get("av_hash_final_b64", "cdecl")
    av_hash_final_b64.argtypes = [POINTER(struct_AVHashContext), POINTER(c_uint8), c_int]
    av_hash_final_b64.restype = None

# /home/josiah/ctypesgen_test/av/hash.h: 263
if _libs["avcodec"].has("av_hash_freep", "cdecl"):
    av_hash_freep = _libs["avcodec"].get("av_hash_freep", "cdecl")
    av_hash_freep.argtypes = [POINTER(POINTER(struct_AVHashContext))]
    av_hash_freep.restype = None

enum_AVHDRPlusOverlapProcessOption = c_int# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_WEIGHTED_AVERAGING = 0# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_LAYERING = 1# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 30

# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 53
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

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 53

# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 230
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

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 230

# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 323
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

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 323

# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 332
if _libs["avcodec"].has("av_dynamic_hdr_plus_alloc", "cdecl"):
    av_dynamic_hdr_plus_alloc = _libs["avcodec"].get("av_dynamic_hdr_plus_alloc", "cdecl")
    av_dynamic_hdr_plus_alloc.argtypes = [POINTER(c_size_t)]
    av_dynamic_hdr_plus_alloc.restype = POINTER(AVDynamicHDRPlus)

# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 341
if _libs["avcodec"].has("av_dynamic_hdr_plus_create_side_data", "cdecl"):
    av_dynamic_hdr_plus_create_side_data = _libs["avcodec"].get("av_dynamic_hdr_plus_create_side_data", "cdecl")
    av_dynamic_hdr_plus_create_side_data.argtypes = [POINTER(AVFrame)]
    av_dynamic_hdr_plus_create_side_data.restype = POINTER(AVDynamicHDRPlus)

enum_AVHMACType = c_int# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_MD5 = 0# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_SHA1 = (AV_HMAC_MD5 + 1)# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_SHA224 = (AV_HMAC_SHA1 + 1)# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_SHA256 = (AV_HMAC_SHA224 + 1)# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_SHA384 = (AV_HMAC_SHA256 + 1)# /home/josiah/ctypesgen_test/av/hmac.h: 33

AV_HMAC_SHA512 = (AV_HMAC_SHA384 + 1)# /home/josiah/ctypesgen_test/av/hmac.h: 33

# /home/josiah/ctypesgen_test/av/hmac.h: 42
class struct_AVHMAC(Structure):
    pass

AVHMAC = struct_AVHMAC# /home/josiah/ctypesgen_test/av/hmac.h: 42

# /home/josiah/ctypesgen_test/av/hmac.h: 48
if _libs["avcodec"].has("av_hmac_alloc", "cdecl"):
    av_hmac_alloc = _libs["avcodec"].get("av_hmac_alloc", "cdecl")
    av_hmac_alloc.argtypes = [enum_AVHMACType]
    av_hmac_alloc.restype = POINTER(AVHMAC)

# /home/josiah/ctypesgen_test/av/hmac.h: 54
if _libs["avcodec"].has("av_hmac_free", "cdecl"):
    av_hmac_free = _libs["avcodec"].get("av_hmac_free", "cdecl")
    av_hmac_free.argtypes = [POINTER(AVHMAC)]
    av_hmac_free.restype = None

# /home/josiah/ctypesgen_test/av/hmac.h: 62
if _libs["avcodec"].has("av_hmac_init", "cdecl"):
    av_hmac_init = _libs["avcodec"].get("av_hmac_init", "cdecl")
    av_hmac_init.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_init.restype = None

# /home/josiah/ctypesgen_test/av/hmac.h: 70
if _libs["avcodec"].has("av_hmac_update", "cdecl"):
    av_hmac_update = _libs["avcodec"].get("av_hmac_update", "cdecl")
    av_hmac_update.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_update.restype = None

# /home/josiah/ctypesgen_test/av/hmac.h: 79
if _libs["avcodec"].has("av_hmac_final", "cdecl"):
    av_hmac_final = _libs["avcodec"].get("av_hmac_final", "cdecl")
    av_hmac_final.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint]
    av_hmac_final.restype = c_int

# /home/josiah/ctypesgen_test/av/hmac.h: 92
if _libs["avcodec"].has("av_hmac_calc", "cdecl"):
    av_hmac_calc = _libs["avcodec"].get("av_hmac_calc", "cdecl")
    av_hmac_calc.argtypes = [POINTER(AVHMAC), POINTER(c_uint8), c_uint, POINTER(c_uint8), c_uint, POINTER(c_uint8), c_uint]
    av_hmac_calc.restype = c_int

enum_anon_36 = c_int# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 35

AV_DRM_MAX_PLANES = 4# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 35

# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 66
class struct_AVDRMObjectDescriptor(Structure):
    pass

struct_AVDRMObjectDescriptor.__slots__ = [
    'fd',
    'size',
    'format_modifier',
]
struct_AVDRMObjectDescriptor._fields_ = [
    ('fd', c_int),
    ('size', c_size_t),
    ('format_modifier', c_uint64),
]

AVDRMObjectDescriptor = struct_AVDRMObjectDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 66

# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 88
class struct_AVDRMPlaneDescriptor(Structure):
    pass

struct_AVDRMPlaneDescriptor.__slots__ = [
    'object_index',
    'offset',
    'pitch',
]
struct_AVDRMPlaneDescriptor._fields_ = [
    ('object_index', c_int),
    ('offset', c_ptrdiff_t),
    ('pitch', c_ptrdiff_t),
]

AVDRMPlaneDescriptor = struct_AVDRMPlaneDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 88

# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 111
class struct_AVDRMLayerDescriptor(Structure):
    pass

struct_AVDRMLayerDescriptor.__slots__ = [
    'format',
    'nb_planes',
    'planes',
]
struct_AVDRMLayerDescriptor._fields_ = [
    ('format', c_uint32),
    ('nb_planes', c_int),
    ('planes', AVDRMPlaneDescriptor * int(AV_DRM_MAX_PLANES)),
]

AVDRMLayerDescriptor = struct_AVDRMLayerDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 111

# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 150
class struct_AVDRMFrameDescriptor(Structure):
    pass

struct_AVDRMFrameDescriptor.__slots__ = [
    'nb_objects',
    'objects',
    'nb_layers',
    'layers',
]
struct_AVDRMFrameDescriptor._fields_ = [
    ('nb_objects', c_int),
    ('objects', AVDRMObjectDescriptor * int(AV_DRM_MAX_PLANES)),
    ('nb_layers', c_int),
    ('layers', AVDRMLayerDescriptor * int(AV_DRM_MAX_PLANES)),
]

AVDRMFrameDescriptor = struct_AVDRMFrameDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 150

# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 167
class struct_AVDRMDeviceContext(Structure):
    pass

struct_AVDRMDeviceContext.__slots__ = [
    'fd',
]
struct_AVDRMDeviceContext._fields_ = [
    ('fd', c_int),
]

AVDRMDeviceContext = struct_AVDRMDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 167

# /home/josiah/ctypesgen_test/av/hwcontext_mediacodec.h: 34
class struct_AVMediaCodecDeviceContext(Structure):
    pass

struct_AVMediaCodecDeviceContext.__slots__ = [
    'surface',
]
struct_AVMediaCodecDeviceContext._fields_ = [
    ('surface', POINTER(None)),
]

AVMediaCodecDeviceContext = struct_AVMediaCodecDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_mediacodec.h: 34

# /usr/include/CL/cl.h: 30
class struct__cl_device_id(Structure):
    pass

cl_device_id = POINTER(struct__cl_device_id)# /usr/include/CL/cl.h: 30

# /usr/include/CL/cl.h: 31
class struct__cl_context(Structure):
    pass

cl_context = POINTER(struct__cl_context)# /usr/include/CL/cl.h: 31

# /usr/include/CL/cl.h: 32
class struct__cl_command_queue(Structure):
    pass

cl_command_queue = POINTER(struct__cl_command_queue)# /usr/include/CL/cl.h: 32

# /usr/include/CL/cl.h: 33
class struct__cl_mem(Structure):
    pass

cl_mem = POINTER(struct__cl_mem)# /usr/include/CL/cl.h: 33

# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 56
class struct_AVOpenCLFrameDescriptor(Structure):
    pass

struct_AVOpenCLFrameDescriptor.__slots__ = [
    'nb_planes',
    'planes',
]
struct_AVOpenCLFrameDescriptor._fields_ = [
    ('nb_planes', c_int),
    ('planes', cl_mem * int(8)),
]

AVOpenCLFrameDescriptor = struct_AVOpenCLFrameDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 56

# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 82
class struct_AVOpenCLDeviceContext(Structure):
    pass

struct_AVOpenCLDeviceContext.__slots__ = [
    'device_id',
    'context',
    'command_queue',
]
struct_AVOpenCLDeviceContext._fields_ = [
    ('device_id', cl_device_id),
    ('context', cl_context),
    ('command_queue', cl_command_queue),
]

AVOpenCLDeviceContext = struct_AVOpenCLDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 82

# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 98
class struct_AVOpenCLFramesContext(Structure):
    pass

struct_AVOpenCLFramesContext.__slots__ = [
    'command_queue',
]
struct_AVOpenCLFramesContext._fields_ = [
    ('command_queue', cl_command_queue),
]

AVOpenCLFramesContext = struct_AVOpenCLFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 98

mfxU8 = c_ubyte# /usr/include/mfx/mfxdefs.h: 152

mfxU16 = c_ushort# /usr/include/mfx/mfxdefs.h: 155

mfxU32 = c_uint# /usr/include/mfx/mfxdefs.h: 156

mfxU64 = c_ulonglong# /usr/include/mfx/mfxdefs.h: 167

mfxHDL = POINTER(None)# /usr/include/mfx/mfxdefs.h: 169

mfxMemId = mfxHDL# /usr/include/mfx/mfxdefs.h: 170

# /usr/include/mfx/mfxcommon.h: 40
class struct_anon_217(Structure):
    pass

struct_anon_217._pack_ = 4
struct_anon_217.__slots__ = [
    'BufferId',
    'BufferSz',
]
struct_anon_217._fields_ = [
    ('BufferId', mfxU32),
    ('BufferSz', mfxU32),
]

mfxExtBuffer = struct_anon_217# /usr/include/mfx/mfxcommon.h: 40

# /usr/include/mfx/mfxsession.h: 30
class struct__mfxSession(Structure):
    pass

mfxSession = POINTER(struct__mfxSession)# /usr/include/mfx/mfxsession.h: 30

# /usr/include/mfx/mfxstructures.h: 39
class struct_anon_234(Structure):
    pass

struct_anon_234._pack_ = 4
struct_anon_234.__slots__ = [
    'DependencyId',
    'QualityId',
]
struct_anon_234._fields_ = [
    ('DependencyId', mfxU16),
    ('QualityId', mfxU16),
]

# /usr/include/mfx/mfxstructures.h: 43
class struct_anon_235(Structure):
    pass

struct_anon_235._pack_ = 4
struct_anon_235.__slots__ = [
    'ViewId',
]
struct_anon_235._fields_ = [
    ('ViewId', mfxU16),
]

# /usr/include/mfx/mfxstructures.h: 38
class union_anon_236(Union):
    pass

union_anon_236._pack_ = 4
union_anon_236.__slots__ = [
    'unnamed_1',
    'unnamed_2',
]
union_anon_236._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
union_anon_236._fields_ = [
    ('unnamed_1', struct_anon_234),
    ('unnamed_2', struct_anon_235),
]

# /usr/include/mfx/mfxstructures.h: 47
class struct_anon_237(Structure):
    pass

struct_anon_237._pack_ = 4
struct_anon_237.__slots__ = [
    'TemporalId',
    'PriorityId',
    'unnamed_1',
]
struct_anon_237._anonymous_ = [
    'unnamed_1',
]
struct_anon_237._fields_ = [
    ('TemporalId', mfxU16),
    ('PriorityId', mfxU16),
    ('unnamed_1', union_anon_236),
]

mfxFrameId = struct_anon_237# /usr/include/mfx/mfxstructures.h: 47

# /usr/include/mfx/mfxstructures.h: 64
class struct_anon_238(Structure):
    pass

struct_anon_238._pack_ = 4
struct_anon_238.__slots__ = [
    'Width',
    'Height',
    'CropX',
    'CropY',
    'CropW',
    'CropH',
]
struct_anon_238._fields_ = [
    ('Width', mfxU16),
    ('Height', mfxU16),
    ('CropX', mfxU16),
    ('CropY', mfxU16),
    ('CropW', mfxU16),
    ('CropH', mfxU16),
]

# /usr/include/mfx/mfxstructures.h: 73
class struct_anon_239(Structure):
    pass

struct_anon_239._pack_ = 4
struct_anon_239.__slots__ = [
    'BufferSize',
    'reserved5',
]
struct_anon_239._fields_ = [
    ('BufferSize', mfxU64),
    ('reserved5', mfxU32),
]

# /usr/include/mfx/mfxstructures.h: 63
class union_anon_240(Union):
    pass

union_anon_240._pack_ = 4
union_anon_240.__slots__ = [
    'unnamed_1',
    'unnamed_2',
]
union_anon_240._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
union_anon_240._fields_ = [
    ('unnamed_1', struct_anon_238),
    ('unnamed_2', struct_anon_239),
]

# /usr/include/mfx/mfxstructures.h: 89
class struct_anon_241(Structure):
    pass

struct_anon_241._pack_ = 4
struct_anon_241.__slots__ = [
    'reserved',
    'reserved4',
    'BitDepthLuma',
    'BitDepthChroma',
    'Shift',
    'FrameId',
    'FourCC',
    'unnamed_1',
    'FrameRateExtN',
    'FrameRateExtD',
    'reserved3',
    'AspectRatioW',
    'AspectRatioH',
    'PicStruct',
    'ChromaFormat',
    'reserved2',
]
struct_anon_241._anonymous_ = [
    'unnamed_1',
]
struct_anon_241._fields_ = [
    ('reserved', mfxU32 * int(4)),
    ('reserved4', mfxU16),
    ('BitDepthLuma', mfxU16),
    ('BitDepthChroma', mfxU16),
    ('Shift', mfxU16),
    ('FrameId', mfxFrameId),
    ('FourCC', mfxU32),
    ('unnamed_1', union_anon_240),
    ('FrameRateExtN', mfxU32),
    ('FrameRateExtD', mfxU32),
    ('reserved3', mfxU16),
    ('AspectRatioW', mfxU16),
    ('AspectRatioH', mfxU16),
    ('PicStruct', mfxU16),
    ('ChromaFormat', mfxU16),
    ('reserved2', mfxU16),
]

mfxFrameInfo = struct_anon_241# /usr/include/mfx/mfxstructures.h: 89

# /usr/include/mfx/mfxstructures.h: 194
class struct_anon_249(Structure):
    pass

struct_anon_249._pack_ = 4
struct_anon_249.__slots__ = [
    'U',
    'Y',
    'V',
    'A',
]
struct_anon_249._fields_ = [
    ('U', mfxU32, 10),
    ('Y', mfxU32, 10),
    ('V', mfxU32, 10),
    ('A', mfxU32, 2),
]

mfxY410 = struct_anon_249# /usr/include/mfx/mfxstructures.h: 194

# /usr/include/mfx/mfxstructures.h: 206
class struct_anon_250(Structure):
    pass

struct_anon_250._pack_ = 4
struct_anon_250.__slots__ = [
    'B',
    'G',
    'R',
    'A',
]
struct_anon_250._fields_ = [
    ('B', mfxU32, 10),
    ('G', mfxU32, 10),
    ('R', mfxU32, 10),
    ('A', mfxU32, 2),
]

mfxA2RGB10 = struct_anon_250# /usr/include/mfx/mfxstructures.h: 206

# /usr/include/mfx/mfxstructures.h: 213
class union_anon_251(Union):
    pass

union_anon_251._pack_ = 8
union_anon_251.__slots__ = [
    'ExtParam',
    'reserved2',
]
union_anon_251._fields_ = [
    ('ExtParam', POINTER(POINTER(mfxExtBuffer))),
    ('reserved2', mfxU64),
]

# /usr/include/mfx/mfxstructures.h: 226
class union_anon_252(Union):
    pass

union_anon_252._pack_ = 8
union_anon_252.__slots__ = [
    'Pitch',
    'PitchLow',
]
union_anon_252._fields_ = [
    ('Pitch', mfxU16),
    ('PitchLow', mfxU16),
]

# /usr/include/mfx/mfxstructures.h: 232
class union_anon_253(Union):
    pass

union_anon_253._pack_ = 8
union_anon_253.__slots__ = [
    'Y',
    'Y16',
    'R',
]
union_anon_253._fields_ = [
    ('Y', POINTER(mfxU8)),
    ('Y16', POINTER(mfxU16)),
    ('R', POINTER(mfxU8)),
]

# /usr/include/mfx/mfxstructures.h: 237
class union_anon_254(Union):
    pass

union_anon_254._pack_ = 8
union_anon_254.__slots__ = [
    'UV',
    'VU',
    'CbCr',
    'CrCb',
    'Cb',
    'U',
    'U16',
    'G',
    'Y410',
]
union_anon_254._fields_ = [
    ('UV', POINTER(mfxU8)),
    ('VU', POINTER(mfxU8)),
    ('CbCr', POINTER(mfxU8)),
    ('CrCb', POINTER(mfxU8)),
    ('Cb', POINTER(mfxU8)),
    ('U', POINTER(mfxU8)),
    ('U16', POINTER(mfxU16)),
    ('G', POINTER(mfxU8)),
    ('Y410', POINTER(mfxY410)),
]

# /usr/include/mfx/mfxstructures.h: 250
class union_anon_255(Union):
    pass

union_anon_255._pack_ = 8
union_anon_255.__slots__ = [
    'Cr',
    'V',
    'V16',
    'B',
    'A2RGB10',
]
union_anon_255._fields_ = [
    ('Cr', POINTER(mfxU8)),
    ('V', POINTER(mfxU8)),
    ('V16', POINTER(mfxU16)),
    ('B', POINTER(mfxU8)),
    ('A2RGB10', POINTER(mfxA2RGB10)),
]

# /usr/include/mfx/mfxstructures.h: 265
class struct_anon_256(Structure):
    pass

struct_anon_256._pack_ = 8
struct_anon_256.__slots__ = [
    'unnamed_1',
    'NumExtParam',
    'reserved',
    'MemType',
    'PitchHigh',
    'TimeStamp',
    'FrameOrder',
    'Locked',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
    'A',
    'MemId',
    'Corrupted',
    'DataFlag',
]
struct_anon_256._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
    'unnamed_3',
    'unnamed_4',
    'unnamed_5',
]
struct_anon_256._fields_ = [
    ('unnamed_1', union_anon_251),
    ('NumExtParam', mfxU16),
    ('reserved', mfxU16 * int(9)),
    ('MemType', mfxU16),
    ('PitchHigh', mfxU16),
    ('TimeStamp', mfxU64),
    ('FrameOrder', mfxU32),
    ('Locked', mfxU16),
    ('unnamed_2', union_anon_252),
    ('unnamed_3', union_anon_253),
    ('unnamed_4', union_anon_254),
    ('unnamed_5', union_anon_255),
    ('A', POINTER(mfxU8)),
    ('MemId', mfxMemId),
    ('Corrupted', mfxU16),
    ('DataFlag', mfxU16),
]

mfxFrameData = struct_anon_256# /usr/include/mfx/mfxstructures.h: 265

# /usr/include/mfx/mfxstructures.h: 274
class struct_anon_257(Structure):
    pass

struct_anon_257._pack_ = 8
struct_anon_257.__slots__ = [
    'reserved',
    'Info',
    'Data',
]
struct_anon_257._fields_ = [
    ('reserved', mfxU32 * int(4)),
    ('Info', mfxFrameInfo),
    ('Data', mfxFrameData),
]

mfxFrameSurface1 = struct_anon_257# /usr/include/mfx/mfxstructures.h: 274

# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 37
class struct_AVQSVDeviceContext(Structure):
    pass

struct_AVQSVDeviceContext.__slots__ = [
    'session',
]
struct_AVQSVDeviceContext._fields_ = [
    ('session', mfxSession),
]

AVQSVDeviceContext = struct_AVQSVDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 37

# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 50
class struct_AVQSVFramesContext(Structure):
    pass

struct_AVQSVFramesContext.__slots__ = [
    'surfaces',
    'nb_surfaces',
    'frame_type',
]
struct_AVQSVFramesContext._fields_ = [
    ('surfaces', POINTER(mfxFrameSurface1)),
    ('nb_surfaces', c_int),
    ('frame_type', c_int),
]

AVQSVFramesContext = struct_AVQSVFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 50

VADisplay = POINTER(None)# /usr/include/va/va.h: 258

VAGenericID = c_uint# /usr/include/va/va.h: 1487

VAConfigID = VAGenericID# /usr/include/va/va.h: 1489

VASurfaceID = VAGenericID# /usr/include/va/va.h: 1552

enum_anon_450 = c_int# /usr/include/va/va.h: 1563

VAGenericValueType = enum_anon_450# /usr/include/va/va.h: 1563

VAGenericFunc = CFUNCTYPE(UNCHECKED(None), )# /usr/include/va/va.h: 1566

# /usr/include/va/va.h: 1573
class union_anon_451(Union):
    pass

union_anon_451.__slots__ = [
    'i',
    'f',
    'p',
    'fn',
]
union_anon_451._fields_ = [
    ('i', c_int32),
    ('f', c_float),
    ('p', POINTER(None)),
    ('fn', VAGenericFunc),
]

# /usr/include/va/va.h: 1583
class struct__VAGenericValue(Structure):
    pass

struct__VAGenericValue.__slots__ = [
    'type',
    'value',
]
struct__VAGenericValue._fields_ = [
    ('type', VAGenericValueType),
    ('value', union_anon_451),
]

VAGenericValue = struct__VAGenericValue# /usr/include/va/va.h: 1583

enum_anon_452 = c_int# /usr/include/va/va.h: 1637

VASurfaceAttribType = enum_anon_452# /usr/include/va/va.h: 1637

# /usr/include/va/va.h: 1647
class struct__VASurfaceAttrib(Structure):
    pass

struct__VASurfaceAttrib.__slots__ = [
    'type',
    'flags',
    'value',
]
struct__VASurfaceAttrib._fields_ = [
    ('type', VASurfaceAttribType),
    ('flags', c_uint32),
    ('value', VAGenericValue),
]

VASurfaceAttrib = struct__VASurfaceAttrib# /usr/include/va/va.h: 1647

enum_anon_614 = c_int# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_USER_SET = (1 << 0)# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_RENDER_PARAM_BUFFERS = (1 << 1)# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_ATTRIB_MEMTYPE = (1 << 2)# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_SURFACE_ATTRIBUTES = (1 << 3)# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 36

# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 81
class struct_AVVAAPIDeviceContext(Structure):
    pass

struct_AVVAAPIDeviceContext.__slots__ = [
    'display',
    'driver_quirks',
]
struct_AVVAAPIDeviceContext._fields_ = [
    ('display', VADisplay),
    ('driver_quirks', c_uint),
]

AVVAAPIDeviceContext = struct_AVVAAPIDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 81

# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 103
class struct_AVVAAPIFramesContext(Structure):
    pass

struct_AVVAAPIFramesContext.__slots__ = [
    'attributes',
    'nb_attributes',
    'surface_ids',
    'nb_surfaces',
]
struct_AVVAAPIFramesContext._fields_ = [
    ('attributes', POINTER(VASurfaceAttrib)),
    ('nb_attributes', c_int),
    ('surface_ids', POINTER(VASurfaceID)),
    ('nb_surfaces', c_int),
]

AVVAAPIFramesContext = struct_AVVAAPIFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 103

# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 115
class struct_AVVAAPIHWConfig(Structure):
    pass

struct_AVVAAPIHWConfig.__slots__ = [
    'config_id',
]
struct_AVVAAPIHWConfig._fields_ = [
    ('config_id', VAConfigID),
]

AVVAAPIHWConfig = struct_AVVAAPIHWConfig# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 115

VdpBool = c_int# /usr/include/vdpau/vdpau.h: 813

VdpChromaType = c_uint32# /usr/include/vdpau/vdpau.h: 839

VdpYCbCrFormat = c_uint32# /usr/include/vdpau/vdpau.h: 963

VdpRGBAFormat = c_uint32# /usr/include/vdpau/vdpau.h: 1119

VdpIndexedFormat = c_uint32# /usr/include/vdpau/vdpau.h: 1188

# /usr/include/vdpau/vdpau.h: 1251
class struct_anon_615(Structure):
    pass

struct_anon_615.__slots__ = [
    'x',
    'y',
]
struct_anon_615._fields_ = [
    ('x', c_uint32),
    ('y', c_uint32),
]

VdpPoint = struct_anon_615# /usr/include/vdpau/vdpau.h: 1251

# /usr/include/vdpau/vdpau.h: 1272
class struct_anon_616(Structure):
    pass

struct_anon_616.__slots__ = [
    'x0',
    'y0',
    'x1',
    'y1',
]
struct_anon_616._fields_ = [
    ('x0', c_uint32),
    ('y0', c_uint32),
    ('x1', c_uint32),
    ('y1', c_uint32),
]

VdpRect = struct_anon_616# /usr/include/vdpau/vdpau.h: 1272

# /usr/include/vdpau/vdpau.h: 1287
class struct_anon_617(Structure):
    pass

struct_anon_617.__slots__ = [
    'red',
    'green',
    'blue',
    'alpha',
]
struct_anon_617._fields_ = [
    ('red', c_float),
    ('green', c_float),
    ('blue', c_float),
    ('alpha', c_float),
]

VdpColor = struct_anon_617# /usr/include/vdpau/vdpau.h: 1287

enum_anon_618 = c_int# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_OK = 0# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_NO_IMPLEMENTATION = (VDP_STATUS_OK + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_DISPLAY_PREEMPTED = (VDP_STATUS_NO_IMPLEMENTATION + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_HANDLE = (VDP_STATUS_DISPLAY_PREEMPTED + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_POINTER = (VDP_STATUS_INVALID_HANDLE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_CHROMA_TYPE = (VDP_STATUS_INVALID_POINTER + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_Y_CB_CR_FORMAT = (VDP_STATUS_INVALID_CHROMA_TYPE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_RGBA_FORMAT = (VDP_STATUS_INVALID_Y_CB_CR_FORMAT + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_INDEXED_FORMAT = (VDP_STATUS_INVALID_RGBA_FORMAT + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_COLOR_STANDARD = (VDP_STATUS_INVALID_INDEXED_FORMAT + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_COLOR_TABLE_FORMAT = (VDP_STATUS_INVALID_COLOR_STANDARD + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_BLEND_FACTOR = (VDP_STATUS_INVALID_COLOR_TABLE_FORMAT + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_BLEND_EQUATION = (VDP_STATUS_INVALID_BLEND_FACTOR + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_FLAG = (VDP_STATUS_INVALID_BLEND_EQUATION + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_DECODER_PROFILE = (VDP_STATUS_INVALID_FLAG + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_VIDEO_MIXER_FEATURE = (VDP_STATUS_INVALID_DECODER_PROFILE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_VIDEO_MIXER_PARAMETER = (VDP_STATUS_INVALID_VIDEO_MIXER_FEATURE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_VIDEO_MIXER_ATTRIBUTE = (VDP_STATUS_INVALID_VIDEO_MIXER_PARAMETER + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_VIDEO_MIXER_PICTURE_STRUCTURE = (VDP_STATUS_INVALID_VIDEO_MIXER_ATTRIBUTE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_FUNC_ID = (VDP_STATUS_INVALID_VIDEO_MIXER_PICTURE_STRUCTURE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_SIZE = (VDP_STATUS_INVALID_FUNC_ID + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_VALUE = (VDP_STATUS_INVALID_SIZE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_INVALID_STRUCT_VERSION = (VDP_STATUS_INVALID_VALUE + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_RESOURCES = (VDP_STATUS_INVALID_STRUCT_VERSION + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_HANDLE_DEVICE_MISMATCH = (VDP_STATUS_RESOURCES + 1)# /usr/include/vdpau/vdpau.h: 1433

VDP_STATUS_ERROR = (VDP_STATUS_HANDLE_DEVICE_MISMATCH + 1)# /usr/include/vdpau/vdpau.h: 1433

VdpStatus = enum_anon_618# /usr/include/vdpau/vdpau.h: 1433

VdpGetErrorString = CFUNCTYPE(UNCHECKED(c_char_p), VdpStatus)# /usr/include/vdpau/vdpau.h: 1444

VdpGetApiVersion = CFUNCTYPE(UNCHECKED(VdpStatus), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1492

VdpGetInformationString = CFUNCTYPE(UNCHECKED(VdpStatus), POINTER(POINTER(c_char)))# /usr/include/vdpau/vdpau.h: 1514

VdpDevice = c_uint32# /usr/include/vdpau/vdpau.h: 1538

VdpDeviceDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice)# /usr/include/vdpau/vdpau.h: 1545

VdpCSCMatrix = (c_float * int(4)) * int(3)# /usr/include/vdpau/vdpau.h: 1587

# /usr/include/vdpau/vdpau.h: 1624
class struct_anon_619(Structure):
    pass

struct_anon_619.__slots__ = [
    'struct_version',
    'brightness',
    'contrast',
    'saturation',
    'hue',
]
struct_anon_619._fields_ = [
    ('struct_version', c_uint32),
    ('brightness', c_float),
    ('contrast', c_float),
    ('saturation', c_float),
    ('hue', c_float),
]

VdpProcamp = struct_anon_619# /usr/include/vdpau/vdpau.h: 1624

VdpColorStandard = c_uint32# /usr/include/vdpau/vdpau.h: 1632

VdpGenerateCSCMatrix = CFUNCTYPE(UNCHECKED(VdpStatus), POINTER(VdpProcamp), VdpColorStandard, POINTER(VdpCSCMatrix))# /usr/include/vdpau/vdpau.h: 1649

VdpVideoSurfaceQueryCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpChromaType, POINTER(VdpBool), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1700

VdpVideoSurfaceQueryGetPutBitsYCbCrCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpChromaType, VdpYCbCrFormat, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 1720

VdpVideoSurface = c_uint32# /usr/include/vdpau/vdpau.h: 1732

VdpVideoSurfaceCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpChromaType, c_uint32, c_uint32, POINTER(VdpVideoSurface))# /usr/include/vdpau/vdpau.h: 1779

VdpVideoSurfaceDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoSurface)# /usr/include/vdpau/vdpau.h: 1793

VdpVideoSurfaceGetParameters = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoSurface, POINTER(VdpChromaType), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1806

VdpVideoSurfaceGetBitsYCbCr = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoSurface, VdpYCbCrFormat, POINTER(POINTER(None)), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1832

VdpVideoSurfacePutBitsYCbCr = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoSurface, VdpYCbCrFormat, POINTER(POINTER(None)), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1857

VdpColorTableFormat = c_uint32# /usr/include/vdpau/vdpau.h: 1898

VdpOutputSurfaceQueryCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, POINTER(VdpBool), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 1926

VdpOutputSurfaceQueryGetPutBitsNativeCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 1945

VdpOutputSurfaceQueryPutBitsIndexedCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, VdpIndexedFormat, VdpColorTableFormat, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 1966

VdpOutputSurfaceQueryPutBitsYCbCrCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, VdpYCbCrFormat, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 1987

VdpOutputSurface = c_uint32# /usr/include/vdpau/vdpau.h: 1999

VdpOutputSurfaceCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, c_uint32, c_uint32, POINTER(VdpOutputSurface))# /usr/include/vdpau/vdpau.h: 2013

VdpOutputSurfaceDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface)# /usr/include/vdpau/vdpau.h: 2027

VdpOutputSurfaceGetParameters = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, POINTER(VdpRGBAFormat), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 2040

VdpOutputSurfaceGetBitsNative = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, POINTER(VdpRect), POINTER(POINTER(None)), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 2067

VdpOutputSurfacePutBitsNative = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, POINTER(POINTER(None)), POINTER(c_uint32), POINTER(VdpRect))# /usr/include/vdpau/vdpau.h: 2093

VdpOutputSurfacePutBitsIndexed = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, VdpIndexedFormat, POINTER(POINTER(None)), POINTER(c_uint32), POINTER(VdpRect), VdpColorTableFormat, POINTER(None))# /usr/include/vdpau/vdpau.h: 2125

VdpOutputSurfacePutBitsYCbCr = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, VdpYCbCrFormat, POINTER(POINTER(None)), POINTER(c_uint32), POINTER(VdpRect), POINTER(VdpCSCMatrix))# /usr/include/vdpau/vdpau.h: 2160

VdpBitmapSurfaceQueryCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, POINTER(VdpBool), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 2219

VdpBitmapSurface = c_uint32# /usr/include/vdpau/vdpau.h: 2232

VdpBitmapSurfaceCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpRGBAFormat, c_uint32, c_uint32, VdpBool, POINTER(VdpBitmapSurface))# /usr/include/vdpau/vdpau.h: 2251

VdpBitmapSurfaceDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpBitmapSurface)# /usr/include/vdpau/vdpau.h: 2266

VdpBitmapSurfaceGetParameters = CFUNCTYPE(UNCHECKED(VdpStatus), VdpBitmapSurface, POINTER(VdpRGBAFormat), POINTER(c_uint32), POINTER(c_uint32), POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 2281

VdpBitmapSurfacePutBitsNative = CFUNCTYPE(UNCHECKED(VdpStatus), VdpBitmapSurface, POINTER(POINTER(None)), POINTER(c_uint32), POINTER(VdpRect))# /usr/include/vdpau/vdpau.h: 2309

enum_anon_620 = c_int# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ZERO = 0# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE = 1# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_SRC_COLOR = 2# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_SRC_COLOR = 3# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_SRC_ALPHA = 4# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA = 5# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_DST_ALPHA = 6# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_DST_ALPHA = 7# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_DST_COLOR = 8# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_DST_COLOR = 9# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_SRC_ALPHA_SATURATE = 10# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_CONSTANT_COLOR = 11# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR = 12# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_CONSTANT_ALPHA = 13# /usr/include/vdpau/vdpau.h: 2348

VDP_OUTPUT_SURFACE_RENDER_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA = 14# /usr/include/vdpau/vdpau.h: 2348

VdpOutputSurfaceRenderBlendFactor = enum_anon_620# /usr/include/vdpau/vdpau.h: 2348

enum_anon_621 = c_int# /usr/include/vdpau/vdpau.h: 2360

VDP_OUTPUT_SURFACE_RENDER_BLEND_EQUATION_SUBTRACT = 0# /usr/include/vdpau/vdpau.h: 2360

VDP_OUTPUT_SURFACE_RENDER_BLEND_EQUATION_REVERSE_SUBTRACT = 1# /usr/include/vdpau/vdpau.h: 2360

VDP_OUTPUT_SURFACE_RENDER_BLEND_EQUATION_ADD = 2# /usr/include/vdpau/vdpau.h: 2360

VDP_OUTPUT_SURFACE_RENDER_BLEND_EQUATION_MIN = 3# /usr/include/vdpau/vdpau.h: 2360

VDP_OUTPUT_SURFACE_RENDER_BLEND_EQUATION_MAX = 4# /usr/include/vdpau/vdpau.h: 2360

VdpOutputSurfaceRenderBlendEquation = enum_anon_621# /usr/include/vdpau/vdpau.h: 2360

# /usr/include/vdpau/vdpau.h: 2395
class struct_anon_622(Structure):
    pass

struct_anon_622.__slots__ = [
    'struct_version',
    'blend_factor_source_color',
    'blend_factor_destination_color',
    'blend_factor_source_alpha',
    'blend_factor_destination_alpha',
    'blend_equation_color',
    'blend_equation_alpha',
    'blend_constant',
]
struct_anon_622._fields_ = [
    ('struct_version', c_uint32),
    ('blend_factor_source_color', VdpOutputSurfaceRenderBlendFactor),
    ('blend_factor_destination_color', VdpOutputSurfaceRenderBlendFactor),
    ('blend_factor_source_alpha', VdpOutputSurfaceRenderBlendFactor),
    ('blend_factor_destination_alpha', VdpOutputSurfaceRenderBlendFactor),
    ('blend_equation_color', VdpOutputSurfaceRenderBlendEquation),
    ('blend_equation_alpha', VdpOutputSurfaceRenderBlendEquation),
    ('blend_constant', VdpColor),
]

VdpOutputSurfaceRenderBlendState = struct_anon_622# /usr/include/vdpau/vdpau.h: 2395

VdpOutputSurfaceRenderOutputSurface = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, POINTER(VdpRect), VdpOutputSurface, POINTER(VdpRect), POINTER(VdpColor), POINTER(VdpOutputSurfaceRenderBlendState), c_uint32)# /usr/include/vdpau/vdpau.h: 2503

VdpOutputSurfaceRenderBitmapSurface = CFUNCTYPE(UNCHECKED(VdpStatus), VdpOutputSurface, POINTER(VdpRect), VdpBitmapSurface, POINTER(VdpRect), POINTER(VdpColor), POINTER(VdpOutputSurfaceRenderBlendState), c_uint32)# /usr/include/vdpau/vdpau.h: 2583

VdpDecoderProfile = c_uint32# /usr/include/vdpau/vdpau.h: 2613

enum_anon_623 = c_int# /usr/include/vdpau/vdpau.h: 2820

VDP_VIDEO_SURFACE_FIELD_STRUCTURE = (1 << 0)# /usr/include/vdpau/vdpau.h: 2820

VDP_VIDEO_SURFACE_FRAME_STRUCTURE = (1 << 1)# /usr/include/vdpau/vdpau.h: 2820

VdpVideoSurfaceSupportedPictureStructure = enum_anon_623# /usr/include/vdpau/vdpau.h: 2820

enum_anon_624 = c_int# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_MAX_LEVEL = 0# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_MAX_MACROBLOCKS = 1# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_MAX_WIDTH = 2# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_MAX_HEIGHT = 3# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_SUPPORTED_PICTURE_STRUCTURE = 4# /usr/include/vdpau/vdpau.h: 2836

VDP_DECODER_PROFILE_SUPPORTED_CHROMA_TYPES = 5# /usr/include/vdpau/vdpau.h: 2836

VdpDecoderCapability = enum_anon_624# /usr/include/vdpau/vdpau.h: 2836

VdpDecoderQueryProfileCapability = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpDecoderProfile, VdpDecoderCapability, POINTER(None))# /usr/include/vdpau/vdpau.h: 2849

VdpDecoderQueryCapabilities = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpDecoderProfile, POINTER(VdpBool), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 2875

VdpDecoder = c_uint32# /usr/include/vdpau/vdpau.h: 2889

VdpDecoderCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpDecoderProfile, c_uint32, c_uint32, c_uint32, POINTER(VdpDecoder))# /usr/include/vdpau/vdpau.h: 2907

VdpDecoderDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDecoder)# /usr/include/vdpau/vdpau.h: 2922

VdpDecoderGetParameters = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDecoder, POINTER(VdpDecoderProfile), POINTER(c_uint32), POINTER(c_uint32))# /usr/include/vdpau/vdpau.h: 2938

# /usr/include/vdpau/vdpau.h: 2961
class struct_anon_625(Structure):
    pass

struct_anon_625.__slots__ = [
    'struct_version',
    'bitstream',
    'bitstream_bytes',
]
struct_anon_625._fields_ = [
    ('struct_version', c_uint32),
    ('bitstream', POINTER(None)),
    ('bitstream_bytes', c_uint32),
]

VdpBitstreamBuffer = struct_anon_625# /usr/include/vdpau/vdpau.h: 2961

VdpPictureInfo = None# /usr/include/vdpau/vdpau.h: 2973

# /usr/include/vdpau/vdpau.h: 3021
class struct_anon_626(Structure):
    pass

struct_anon_626.__slots__ = [
    'forward_reference',
    'backward_reference',
    'slice_count',
    'picture_structure',
    'picture_coding_type',
    'intra_dc_precision',
    'frame_pred_frame_dct',
    'concealment_motion_vectors',
    'intra_vlc_format',
    'alternate_scan',
    'q_scale_type',
    'top_field_first',
    'full_pel_forward_vector',
    'full_pel_backward_vector',
    'f_code',
    'intra_quantizer_matrix',
    'non_intra_quantizer_matrix',
]
struct_anon_626._fields_ = [
    ('forward_reference', VdpVideoSurface),
    ('backward_reference', VdpVideoSurface),
    ('slice_count', c_uint32),
    ('picture_structure', c_uint8),
    ('picture_coding_type', c_uint8),
    ('intra_dc_precision', c_uint8),
    ('frame_pred_frame_dct', c_uint8),
    ('concealment_motion_vectors', c_uint8),
    ('intra_vlc_format', c_uint8),
    ('alternate_scan', c_uint8),
    ('q_scale_type', c_uint8),
    ('top_field_first', c_uint8),
    ('full_pel_forward_vector', c_uint8),
    ('full_pel_backward_vector', c_uint8),
    ('f_code', (c_uint8 * int(2)) * int(2)),
    ('intra_quantizer_matrix', c_uint8 * int(64)),
    ('non_intra_quantizer_matrix', c_uint8 * int(64)),
]

VdpPictureInfoMPEG1Or2 = struct_anon_626# /usr/include/vdpau/vdpau.h: 3021

# /usr/include/vdpau/vdpau.h: 3056
class struct_anon_627(Structure):
    pass

struct_anon_627.__slots__ = [
    'surface',
    'is_long_term',
    'top_is_reference',
    'bottom_is_reference',
    'field_order_cnt',
    'frame_idx',
]
struct_anon_627._fields_ = [
    ('surface', VdpVideoSurface),
    ('is_long_term', VdpBool),
    ('top_is_reference', VdpBool),
    ('bottom_is_reference', VdpBool),
    ('field_order_cnt', c_int32 * int(2)),
    ('frame_idx', c_uint16),
]

VdpReferenceFrameH264 = struct_anon_627# /usr/include/vdpau/vdpau.h: 3056

# /usr/include/vdpau/vdpau.h: 3124
class struct_anon_628(Structure):
    pass

struct_anon_628.__slots__ = [
    'slice_count',
    'field_order_cnt',
    'is_reference',
    'frame_num',
    'field_pic_flag',
    'bottom_field_flag',
    'num_ref_frames',
    'mb_adaptive_frame_field_flag',
    'constrained_intra_pred_flag',
    'weighted_pred_flag',
    'weighted_bipred_idc',
    'frame_mbs_only_flag',
    'transform_8x8_mode_flag',
    'chroma_qp_index_offset',
    'second_chroma_qp_index_offset',
    'pic_init_qp_minus26',
    'num_ref_idx_l0_active_minus1',
    'num_ref_idx_l1_active_minus1',
    'log2_max_frame_num_minus4',
    'pic_order_cnt_type',
    'log2_max_pic_order_cnt_lsb_minus4',
    'delta_pic_order_always_zero_flag',
    'direct_8x8_inference_flag',
    'entropy_coding_mode_flag',
    'pic_order_present_flag',
    'deblocking_filter_control_present_flag',
    'redundant_pic_cnt_present_flag',
    'scaling_lists_4x4',
    'scaling_lists_8x8',
    'referenceFrames',
]
struct_anon_628._fields_ = [
    ('slice_count', c_uint32),
    ('field_order_cnt', c_int32 * int(2)),
    ('is_reference', VdpBool),
    ('frame_num', c_uint16),
    ('field_pic_flag', c_uint8),
    ('bottom_field_flag', c_uint8),
    ('num_ref_frames', c_uint8),
    ('mb_adaptive_frame_field_flag', c_uint8),
    ('constrained_intra_pred_flag', c_uint8),
    ('weighted_pred_flag', c_uint8),
    ('weighted_bipred_idc', c_uint8),
    ('frame_mbs_only_flag', c_uint8),
    ('transform_8x8_mode_flag', c_uint8),
    ('chroma_qp_index_offset', c_int8),
    ('second_chroma_qp_index_offset', c_int8),
    ('pic_init_qp_minus26', c_int8),
    ('num_ref_idx_l0_active_minus1', c_uint8),
    ('num_ref_idx_l1_active_minus1', c_uint8),
    ('log2_max_frame_num_minus4', c_uint8),
    ('pic_order_cnt_type', c_uint8),
    ('log2_max_pic_order_cnt_lsb_minus4', c_uint8),
    ('delta_pic_order_always_zero_flag', c_uint8),
    ('direct_8x8_inference_flag', c_uint8),
    ('entropy_coding_mode_flag', c_uint8),
    ('pic_order_present_flag', c_uint8),
    ('deblocking_filter_control_present_flag', c_uint8),
    ('redundant_pic_cnt_present_flag', c_uint8),
    ('scaling_lists_4x4', (c_uint8 * int(16)) * int(6)),
    ('scaling_lists_8x8', (c_uint8 * int(64)) * int(2)),
    ('referenceFrames', VdpReferenceFrameH264 * int(16)),
]

VdpPictureInfoH264 = struct_anon_628# /usr/include/vdpau/vdpau.h: 3124

# /usr/include/vdpau/vdpau.h: 3155
class struct_anon_629(Structure):
    pass

struct_anon_629.__slots__ = [
    'pictureInfo',
    'qpprime_y_zero_transform_bypass_flag',
    'separate_colour_plane_flag',
]
struct_anon_629._fields_ = [
    ('pictureInfo', VdpPictureInfoH264),
    ('qpprime_y_zero_transform_bypass_flag', c_uint8),
    ('separate_colour_plane_flag', c_uint8),
]

VdpPictureInfoH264Predictive = struct_anon_629# /usr/include/vdpau/vdpau.h: 3155

# /usr/include/vdpau/vdpau.h: 3262
class struct_anon_630(Structure):
    pass

struct_anon_630.__slots__ = [
    'forward_reference',
    'backward_reference',
    'slice_count',
    'picture_type',
    'frame_coding_mode',
    'postprocflag',
    'pulldown',
    'interlace',
    'tfcntrflag',
    'finterpflag',
    'psf',
    'dquant',
    'panscan_flag',
    'refdist_flag',
    'quantizer',
    'extended_mv',
    'extended_dmv',
    'overlap',
    'vstransform',
    'loopfilter',
    'fastuvmc',
    'range_mapy_flag',
    'range_mapy',
    'range_mapuv_flag',
    'range_mapuv',
    'multires',
    'syncmarker',
    'rangered',
    'maxbframes',
    'deblockEnable',
    'pquant',
]
struct_anon_630._fields_ = [
    ('forward_reference', VdpVideoSurface),
    ('backward_reference', VdpVideoSurface),
    ('slice_count', c_uint32),
    ('picture_type', c_uint8),
    ('frame_coding_mode', c_uint8),
    ('postprocflag', c_uint8),
    ('pulldown', c_uint8),
    ('interlace', c_uint8),
    ('tfcntrflag', c_uint8),
    ('finterpflag', c_uint8),
    ('psf', c_uint8),
    ('dquant', c_uint8),
    ('panscan_flag', c_uint8),
    ('refdist_flag', c_uint8),
    ('quantizer', c_uint8),
    ('extended_mv', c_uint8),
    ('extended_dmv', c_uint8),
    ('overlap', c_uint8),
    ('vstransform', c_uint8),
    ('loopfilter', c_uint8),
    ('fastuvmc', c_uint8),
    ('range_mapy_flag', c_uint8),
    ('range_mapy', c_uint8),
    ('range_mapuv_flag', c_uint8),
    ('range_mapuv', c_uint8),
    ('multires', c_uint8),
    ('syncmarker', c_uint8),
    ('rangered', c_uint8),
    ('maxbframes', c_uint8),
    ('deblockEnable', c_uint8),
    ('pquant', c_uint8),
]

VdpPictureInfoVC1 = struct_anon_630# /usr/include/vdpau/vdpau.h: 3262

# /usr/include/vdpau/vdpau.h: 3305
class struct_anon_631(Structure):
    pass

struct_anon_631.__slots__ = [
    'forward_reference',
    'backward_reference',
    'trd',
    'trb',
    'vop_time_increment_resolution',
    'vop_coding_type',
    'vop_fcode_forward',
    'vop_fcode_backward',
    'resync_marker_disable',
    'interlaced',
    'quant_type',
    'quarter_sample',
    'short_video_header',
    'rounding_control',
    'alternate_vertical_scan_flag',
    'top_field_first',
    'intra_quantizer_matrix',
    'non_intra_quantizer_matrix',
]
struct_anon_631._fields_ = [
    ('forward_reference', VdpVideoSurface),
    ('backward_reference', VdpVideoSurface),
    ('trd', c_int32 * int(2)),
    ('trb', c_int32 * int(2)),
    ('vop_time_increment_resolution', c_uint16),
    ('vop_coding_type', c_uint8),
    ('vop_fcode_forward', c_uint8),
    ('vop_fcode_backward', c_uint8),
    ('resync_marker_disable', c_uint8),
    ('interlaced', c_uint8),
    ('quant_type', c_uint8),
    ('quarter_sample', c_uint8),
    ('short_video_header', c_uint8),
    ('rounding_control', c_uint8),
    ('alternate_vertical_scan_flag', c_uint8),
    ('top_field_first', c_uint8),
    ('intra_quantizer_matrix', c_uint8 * int(64)),
    ('non_intra_quantizer_matrix', c_uint8 * int(64)),
]

VdpPictureInfoMPEG4Part2 = struct_anon_631# /usr/include/vdpau/vdpau.h: 3305

VdpPictureInfoDivX4 = VdpPictureInfoMPEG4Part2# /usr/include/vdpau/vdpau.h: 3313

VdpPictureInfoDivX5 = VdpPictureInfoMPEG4Part2# /usr/include/vdpau/vdpau.h: 3321

# /usr/include/vdpau/vdpau.h: 3381
class struct_anon_632(Structure):
    pass

struct_anon_632.__slots__ = [
    'width',
    'height',
    'lastReference',
    'goldenReference',
    'altReference',
    'colorSpace',
    'profile',
    'frameContextIdx',
    'keyFrame',
    'showFrame',
    'errorResilient',
    'frameParallelDecoding',
    'subSamplingX',
    'subSamplingY',
    'intraOnly',
    'allowHighPrecisionMv',
    'refreshEntropyProbs',
    'refFrameSignBias',
    'bitDepthMinus8Luma',
    'bitDepthMinus8Chroma',
    'loopFilterLevel',
    'loopFilterSharpness',
    'modeRefLfEnabled',
    'log2TileColumns',
    'log2TileRows',
    'segmentEnabled',
    'segmentMapUpdate',
    'segmentMapTemporalUpdate',
    'segmentFeatureMode',
    'segmentFeatureEnable',
    'segmentFeatureData',
    'mbSegmentTreeProbs',
    'segmentPredProbs',
    'reservedSegment16Bits',
    'qpYAc',
    'qpYDc',
    'qpChDc',
    'qpChAc',
    'activeRefIdx',
    'resetFrameContext',
    'mcompFilterType',
    'mbRefLfDelta',
    'mbModeLfDelta',
    'uncompressedHeaderSize',
    'compressedHeaderSize',
]
struct_anon_632._fields_ = [
    ('width', c_uint),
    ('height', c_uint),
    ('lastReference', VdpVideoSurface),
    ('goldenReference', VdpVideoSurface),
    ('altReference', VdpVideoSurface),
    ('colorSpace', c_ubyte),
    ('profile', c_ushort),
    ('frameContextIdx', c_ushort),
    ('keyFrame', c_ushort),
    ('showFrame', c_ushort),
    ('errorResilient', c_ushort),
    ('frameParallelDecoding', c_ushort),
    ('subSamplingX', c_ushort),
    ('subSamplingY', c_ushort),
    ('intraOnly', c_ushort),
    ('allowHighPrecisionMv', c_ushort),
    ('refreshEntropyProbs', c_ushort),
    ('refFrameSignBias', c_ubyte * int(4)),
    ('bitDepthMinus8Luma', c_ubyte),
    ('bitDepthMinus8Chroma', c_ubyte),
    ('loopFilterLevel', c_ubyte),
    ('loopFilterSharpness', c_ubyte),
    ('modeRefLfEnabled', c_ubyte),
    ('log2TileColumns', c_ubyte),
    ('log2TileRows', c_ubyte),
    ('segmentEnabled', c_ubyte),
    ('segmentMapUpdate', c_ubyte),
    ('segmentMapTemporalUpdate', c_ubyte),
    ('segmentFeatureMode', c_ubyte),
    ('segmentFeatureEnable', (c_ubyte * int(4)) * int(8)),
    ('segmentFeatureData', (c_short * int(4)) * int(8)),
    ('mbSegmentTreeProbs', c_ubyte * int(7)),
    ('segmentPredProbs', c_ubyte * int(3)),
    ('reservedSegment16Bits', c_ubyte * int(2)),
    ('qpYAc', c_int),
    ('qpYDc', c_int),
    ('qpChDc', c_int),
    ('qpChAc', c_int),
    ('activeRefIdx', c_uint * int(3)),
    ('resetFrameContext', c_uint),
    ('mcompFilterType', c_uint),
    ('mbRefLfDelta', c_uint * int(4)),
    ('mbModeLfDelta', c_uint * int(2)),
    ('uncompressedHeaderSize', c_uint),
    ('compressedHeaderSize', c_uint),
]

VdpPictureInfoVP9 = struct_anon_632# /usr/include/vdpau/vdpau.h: 3381

# /usr/include/vdpau/vdpau.h: 3595
class struct_anon_633(Structure):
    pass

struct_anon_633.__slots__ = [
    'chroma_format_idc',
    'separate_colour_plane_flag',
    'pic_width_in_luma_samples',
    'pic_height_in_luma_samples',
    'bit_depth_luma_minus8',
    'bit_depth_chroma_minus8',
    'log2_max_pic_order_cnt_lsb_minus4',
    'sps_max_dec_pic_buffering_minus1',
    'log2_min_luma_coding_block_size_minus3',
    'log2_diff_max_min_luma_coding_block_size',
    'log2_min_transform_block_size_minus2',
    'log2_diff_max_min_transform_block_size',
    'max_transform_hierarchy_depth_inter',
    'max_transform_hierarchy_depth_intra',
    'scaling_list_enabled_flag',
    'ScalingList4x4',
    'ScalingList8x8',
    'ScalingList16x16',
    'ScalingList32x32',
    'ScalingListDCCoeff16x16',
    'ScalingListDCCoeff32x32',
    'amp_enabled_flag',
    'sample_adaptive_offset_enabled_flag',
    'pcm_enabled_flag',
    'pcm_sample_bit_depth_luma_minus1',
    'pcm_sample_bit_depth_chroma_minus1',
    'log2_min_pcm_luma_coding_block_size_minus3',
    'log2_diff_max_min_pcm_luma_coding_block_size',
    'pcm_loop_filter_disabled_flag',
    'num_short_term_ref_pic_sets',
    'long_term_ref_pics_present_flag',
    'num_long_term_ref_pics_sps',
    'sps_temporal_mvp_enabled_flag',
    'strong_intra_smoothing_enabled_flag',
    'dependent_slice_segments_enabled_flag',
    'output_flag_present_flag',
    'num_extra_slice_header_bits',
    'sign_data_hiding_enabled_flag',
    'cabac_init_present_flag',
    'num_ref_idx_l0_default_active_minus1',
    'num_ref_idx_l1_default_active_minus1',
    'init_qp_minus26',
    'constrained_intra_pred_flag',
    'transform_skip_enabled_flag',
    'cu_qp_delta_enabled_flag',
    'diff_cu_qp_delta_depth',
    'pps_cb_qp_offset',
    'pps_cr_qp_offset',
    'pps_slice_chroma_qp_offsets_present_flag',
    'weighted_pred_flag',
    'weighted_bipred_flag',
    'transquant_bypass_enabled_flag',
    'tiles_enabled_flag',
    'entropy_coding_sync_enabled_flag',
    'num_tile_columns_minus1',
    'num_tile_rows_minus1',
    'uniform_spacing_flag',
    'column_width_minus1',
    'row_height_minus1',
    'loop_filter_across_tiles_enabled_flag',
    'pps_loop_filter_across_slices_enabled_flag',
    'deblocking_filter_control_present_flag',
    'deblocking_filter_override_enabled_flag',
    'pps_deblocking_filter_disabled_flag',
    'pps_beta_offset_div2',
    'pps_tc_offset_div2',
    'lists_modification_present_flag',
    'log2_parallel_merge_level_minus2',
    'slice_segment_header_extension_present_flag',
    'IDRPicFlag',
    'RAPPicFlag',
    'CurrRpsIdx',
    'NumPocTotalCurr',
    'NumDeltaPocsOfRefRpsIdx',
    'NumShortTermPictureSliceHeaderBits',
    'NumLongTermPictureSliceHeaderBits',
    'CurrPicOrderCntVal',
    'RefPics',
    'PicOrderCntVal',
    'IsLongTerm',
    'NumPocStCurrBefore',
    'NumPocStCurrAfter',
    'NumPocLtCurr',
    'RefPicSetStCurrBefore',
    'RefPicSetStCurrAfter',
    'RefPicSetLtCurr',
]
struct_anon_633._fields_ = [
    ('chroma_format_idc', c_uint8),
    ('separate_colour_plane_flag', c_uint8),
    ('pic_width_in_luma_samples', c_uint32),
    ('pic_height_in_luma_samples', c_uint32),
    ('bit_depth_luma_minus8', c_uint8),
    ('bit_depth_chroma_minus8', c_uint8),
    ('log2_max_pic_order_cnt_lsb_minus4', c_uint8),
    ('sps_max_dec_pic_buffering_minus1', c_uint8),
    ('log2_min_luma_coding_block_size_minus3', c_uint8),
    ('log2_diff_max_min_luma_coding_block_size', c_uint8),
    ('log2_min_transform_block_size_minus2', c_uint8),
    ('log2_diff_max_min_transform_block_size', c_uint8),
    ('max_transform_hierarchy_depth_inter', c_uint8),
    ('max_transform_hierarchy_depth_intra', c_uint8),
    ('scaling_list_enabled_flag', c_uint8),
    ('ScalingList4x4', (c_uint8 * int(16)) * int(6)),
    ('ScalingList8x8', (c_uint8 * int(64)) * int(6)),
    ('ScalingList16x16', (c_uint8 * int(64)) * int(6)),
    ('ScalingList32x32', (c_uint8 * int(64)) * int(2)),
    ('ScalingListDCCoeff16x16', c_uint8 * int(6)),
    ('ScalingListDCCoeff32x32', c_uint8 * int(2)),
    ('amp_enabled_flag', c_uint8),
    ('sample_adaptive_offset_enabled_flag', c_uint8),
    ('pcm_enabled_flag', c_uint8),
    ('pcm_sample_bit_depth_luma_minus1', c_uint8),
    ('pcm_sample_bit_depth_chroma_minus1', c_uint8),
    ('log2_min_pcm_luma_coding_block_size_minus3', c_uint8),
    ('log2_diff_max_min_pcm_luma_coding_block_size', c_uint8),
    ('pcm_loop_filter_disabled_flag', c_uint8),
    ('num_short_term_ref_pic_sets', c_uint8),
    ('long_term_ref_pics_present_flag', c_uint8),
    ('num_long_term_ref_pics_sps', c_uint8),
    ('sps_temporal_mvp_enabled_flag', c_uint8),
    ('strong_intra_smoothing_enabled_flag', c_uint8),
    ('dependent_slice_segments_enabled_flag', c_uint8),
    ('output_flag_present_flag', c_uint8),
    ('num_extra_slice_header_bits', c_uint8),
    ('sign_data_hiding_enabled_flag', c_uint8),
    ('cabac_init_present_flag', c_uint8),
    ('num_ref_idx_l0_default_active_minus1', c_uint8),
    ('num_ref_idx_l1_default_active_minus1', c_uint8),
    ('init_qp_minus26', c_int8),
    ('constrained_intra_pred_flag', c_uint8),
    ('transform_skip_enabled_flag', c_uint8),
    ('cu_qp_delta_enabled_flag', c_uint8),
    ('diff_cu_qp_delta_depth', c_uint8),
    ('pps_cb_qp_offset', c_int8),
    ('pps_cr_qp_offset', c_int8),
    ('pps_slice_chroma_qp_offsets_present_flag', c_uint8),
    ('weighted_pred_flag', c_uint8),
    ('weighted_bipred_flag', c_uint8),
    ('transquant_bypass_enabled_flag', c_uint8),
    ('tiles_enabled_flag', c_uint8),
    ('entropy_coding_sync_enabled_flag', c_uint8),
    ('num_tile_columns_minus1', c_uint8),
    ('num_tile_rows_minus1', c_uint8),
    ('uniform_spacing_flag', c_uint8),
    ('column_width_minus1', c_uint16 * int(20)),
    ('row_height_minus1', c_uint16 * int(22)),
    ('loop_filter_across_tiles_enabled_flag', c_uint8),
    ('pps_loop_filter_across_slices_enabled_flag', c_uint8),
    ('deblocking_filter_control_present_flag', c_uint8),
    ('deblocking_filter_override_enabled_flag', c_uint8),
    ('pps_deblocking_filter_disabled_flag', c_uint8),
    ('pps_beta_offset_div2', c_int8),
    ('pps_tc_offset_div2', c_int8),
    ('lists_modification_present_flag', c_uint8),
    ('log2_parallel_merge_level_minus2', c_uint8),
    ('slice_segment_header_extension_present_flag', c_uint8),
    ('IDRPicFlag', c_uint8),
    ('RAPPicFlag', c_uint8),
    ('CurrRpsIdx', c_uint8),
    ('NumPocTotalCurr', c_uint32),
    ('NumDeltaPocsOfRefRpsIdx', c_uint32),
    ('NumShortTermPictureSliceHeaderBits', c_uint32),
    ('NumLongTermPictureSliceHeaderBits', c_uint32),
    ('CurrPicOrderCntVal', c_int32),
    ('RefPics', VdpVideoSurface * int(16)),
    ('PicOrderCntVal', c_int32 * int(16)),
    ('IsLongTerm', c_uint8 * int(16)),
    ('NumPocStCurrBefore', c_uint8),
    ('NumPocStCurrAfter', c_uint8),
    ('NumPocLtCurr', c_uint8),
    ('RefPicSetStCurrBefore', c_uint8 * int(8)),
    ('RefPicSetStCurrAfter', c_uint8 * int(8)),
    ('RefPicSetLtCurr', c_uint8 * int(8)),
]

VdpPictureInfoHEVC = struct_anon_633# /usr/include/vdpau/vdpau.h: 3595

# /usr/include/vdpau/vdpau.h: 3653
class struct_anon_634(Structure):
    pass

struct_anon_634.__slots__ = [
    'pictureInfo',
    'sps_range_extension_flag',
    'transformSkipRotationEnableFlag',
    'transformSkipContextEnableFlag',
    'implicitRdpcmEnableFlag',
    'explicitRdpcmEnableFlag',
    'extendedPrecisionProcessingFlag',
    'intraSmoothingDisabledFlag',
    'highPrecisionOffsetsEnableFlag',
    'persistentRiceAdaptationEnableFlag',
    'cabacBypassAlignmentEnableFlag',
    'intraBlockCopyEnableFlag',
    'pps_range_extension_flag',
    'log2MaxTransformSkipSize',
    'crossComponentPredictionEnableFlag',
    'chromaQpAdjustmentEnableFlag',
    'diffCuChromaQpAdjustmentDepth',
    'chromaQpAdjustmentTableSize',
    'log2SaoOffsetScaleLuma',
    'log2SaoOffsetScaleChroma',
    'cb_qp_adjustment',
    'cr_qp_adjustment',
]
struct_anon_634._fields_ = [
    ('pictureInfo', VdpPictureInfoHEVC),
    ('sps_range_extension_flag', c_uint8),
    ('transformSkipRotationEnableFlag', c_uint8),
    ('transformSkipContextEnableFlag', c_uint8),
    ('implicitRdpcmEnableFlag', c_uint8),
    ('explicitRdpcmEnableFlag', c_uint8),
    ('extendedPrecisionProcessingFlag', c_uint8),
    ('intraSmoothingDisabledFlag', c_uint8),
    ('highPrecisionOffsetsEnableFlag', c_uint8),
    ('persistentRiceAdaptationEnableFlag', c_uint8),
    ('cabacBypassAlignmentEnableFlag', c_uint8),
    ('intraBlockCopyEnableFlag', c_uint8),
    ('pps_range_extension_flag', c_uint8),
    ('log2MaxTransformSkipSize', c_uint8),
    ('crossComponentPredictionEnableFlag', c_uint8),
    ('chromaQpAdjustmentEnableFlag', c_uint8),
    ('diffCuChromaQpAdjustmentDepth', c_uint8),
    ('chromaQpAdjustmentTableSize', c_uint8),
    ('log2SaoOffsetScaleLuma', c_uint8),
    ('log2SaoOffsetScaleChroma', c_uint8),
    ('cb_qp_adjustment', c_int8 * int(6)),
    ('cr_qp_adjustment', c_int8 * int(6)),
]

VdpPictureInfoHEVC444 = struct_anon_634# /usr/include/vdpau/vdpau.h: 3653

VdpPictureInfoHEVCRangeExt = VdpPictureInfoHEVC444# /usr/include/vdpau/vdpau.h: 3663

VdpDecoderRender = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDecoder, VdpVideoSurface, POINTER(VdpPictureInfo), c_uint32, POINTER(VdpBitstreamBuffer))# /usr/include/vdpau/vdpau.h: 3683

VdpVideoMixerFeature = c_uint32# /usr/include/vdpau/vdpau.h: 3769

VdpVideoMixerParameter = c_uint32# /usr/include/vdpau/vdpau.h: 3925

VdpVideoMixerAttribute = c_uint32# /usr/include/vdpau/vdpau.h: 3999

VdpVideoMixerQueryFeatureSupport = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpVideoMixerFeature, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4121

VdpVideoMixerQueryParameterSupport = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpVideoMixerParameter, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4138

VdpVideoMixerQueryAttributeSupport = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpVideoMixerAttribute, POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4154

VdpVideoMixerQueryParameterValueRange = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpVideoMixerParameter, POINTER(None), POINTER(None))# /usr/include/vdpau/vdpau.h: 4171

VdpVideoMixerQueryAttributeValueRange = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpVideoMixerAttribute, POINTER(None), POINTER(None))# /usr/include/vdpau/vdpau.h: 4189

VdpVideoMixer = c_uint32# /usr/include/vdpau/vdpau.h: 4200

VdpVideoMixerCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, c_uint32, POINTER(VdpVideoMixerFeature), c_uint32, POINTER(VdpVideoMixerParameter), POINTER(POINTER(None)), POINTER(VdpVideoMixer))# /usr/include/vdpau/vdpau.h: 4222

VdpVideoMixerSetFeatureEnables = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerFeature), POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4245

VdpVideoMixerSetAttributeValues = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerAttribute), POINTER(POINTER(None)))# /usr/include/vdpau/vdpau.h: 4264

VdpVideoMixerGetFeatureSupport = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerFeature), POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4282

VdpVideoMixerGetFeatureEnables = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerFeature), POINTER(VdpBool))# /usr/include/vdpau/vdpau.h: 4299

VdpVideoMixerGetParameterValues = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerParameter), POINTER(POINTER(None)))# /usr/include/vdpau/vdpau.h: 4319

VdpVideoMixerGetAttributeValues = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, c_uint32, POINTER(VdpVideoMixerAttribute), POINTER(POINTER(None)))# /usr/include/vdpau/vdpau.h: 4339

VdpVideoMixerDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer)# /usr/include/vdpau/vdpau.h: 4352

enum_anon_635 = c_int# /usr/include/vdpau/vdpau.h: 4375

VDP_VIDEO_MIXER_PICTURE_STRUCTURE_TOP_FIELD = 0# /usr/include/vdpau/vdpau.h: 4375

VDP_VIDEO_MIXER_PICTURE_STRUCTURE_BOTTOM_FIELD = (VDP_VIDEO_MIXER_PICTURE_STRUCTURE_TOP_FIELD + 1)# /usr/include/vdpau/vdpau.h: 4375

VDP_VIDEO_MIXER_PICTURE_STRUCTURE_FRAME = (VDP_VIDEO_MIXER_PICTURE_STRUCTURE_BOTTOM_FIELD + 1)# /usr/include/vdpau/vdpau.h: 4375

VdpVideoMixerPictureStructure = enum_anon_635# /usr/include/vdpau/vdpau.h: 4375

# /usr/include/vdpau/vdpau.h: 4406
class struct_anon_636(Structure):
    pass

struct_anon_636.__slots__ = [
    'struct_version',
    'source_surface',
    'source_rect',
    'destination_rect',
]
struct_anon_636._fields_ = [
    ('struct_version', c_uint32),
    ('source_surface', VdpOutputSurface),
    ('source_rect', POINTER(VdpRect)),
    ('destination_rect', POINTER(VdpRect)),
]

VdpLayer = struct_anon_636# /usr/include/vdpau/vdpau.h: 4406

VdpVideoMixerRender = CFUNCTYPE(UNCHECKED(VdpStatus), VdpVideoMixer, VdpOutputSurface, POINTER(VdpRect), VdpVideoMixerPictureStructure, c_uint32, POINTER(VdpVideoSurface), VdpVideoSurface, c_uint32, POINTER(VdpVideoSurface), POINTER(VdpRect), VdpOutputSurface, POINTER(VdpRect), POINTER(VdpRect), c_uint32, POINTER(VdpLayer))# /usr/include/vdpau/vdpau.h: 4474

VdpTime = c_uint64# /usr/include/vdpau/vdpau.h: 4542

VdpPresentationQueueTarget = c_uint32# /usr/include/vdpau/vdpau.h: 4552

VdpPresentationQueueTargetDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueueTarget)# /usr/include/vdpau/vdpau.h: 4559

VdpPresentationQueue = c_uint32# /usr/include/vdpau/vdpau.h: 4567

VdpPresentationQueueCreate = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpPresentationQueueTarget, POINTER(VdpPresentationQueue))# /usr/include/vdpau/vdpau.h: 4580

VdpPresentationQueueDestroy = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue)# /usr/include/vdpau/vdpau.h: 4592

VdpPresentationQueueSetBackgroundColor = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, POINTER(VdpColor))# /usr/include/vdpau/vdpau.h: 4605

VdpPresentationQueueGetBackgroundColor = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, POINTER(VdpColor))# /usr/include/vdpau/vdpau.h: 4615

VdpPresentationQueueGetTime = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, POINTER(VdpTime))# /usr/include/vdpau/vdpau.h: 4627

VdpPresentationQueueDisplay = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, VdpOutputSurface, c_uint32, c_uint32, VdpTime)# /usr/include/vdpau/vdpau.h: 4673

VdpPresentationQueueBlockUntilSurfaceIdle = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, VdpOutputSurface, POINTER(VdpTime))# /usr/include/vdpau/vdpau.h: 4696

enum_anon_637 = c_int# /usr/include/vdpau/vdpau.h: 4714

VDP_PRESENTATION_QUEUE_STATUS_IDLE = 0# /usr/include/vdpau/vdpau.h: 4714

VDP_PRESENTATION_QUEUE_STATUS_QUEUED = (VDP_PRESENTATION_QUEUE_STATUS_IDLE + 1)# /usr/include/vdpau/vdpau.h: 4714

VDP_PRESENTATION_QUEUE_STATUS_VISIBLE = (VDP_PRESENTATION_QUEUE_STATUS_QUEUED + 1)# /usr/include/vdpau/vdpau.h: 4714

VdpPresentationQueueStatus = enum_anon_637# /usr/include/vdpau/vdpau.h: 4714

VdpPresentationQueueQuerySurfaceStatus = CFUNCTYPE(UNCHECKED(VdpStatus), VdpPresentationQueue, VdpOutputSurface, POINTER(VdpPresentationQueueStatus), POINTER(VdpTime))# /usr/include/vdpau/vdpau.h: 4727

VdpPreemptionCallback = CFUNCTYPE(UNCHECKED(None), VdpDevice, POINTER(None))# /usr/include/vdpau/vdpau.h: 4789

VdpPreemptionCallbackRegister = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpPreemptionCallback, POINTER(None))# /usr/include/vdpau/vdpau.h: 4804

VdpFuncId = c_uint32# /usr/include/vdpau/vdpau.h: 4827

VdpGetProcAddress = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpFuncId, POINTER(POINTER(None)))# /usr/include/vdpau/vdpau.h: 4965

# /home/josiah/ctypesgen_test/av/hwcontext_vdpau.h: 38
class struct_AVVDPAUDeviceContext(Structure):
    pass

struct_AVVDPAUDeviceContext.__slots__ = [
    'device',
    'get_proc_address',
]
struct_AVVDPAUDeviceContext._fields_ = [
    ('device', VdpDevice),
    ('get_proc_address', POINTER(VdpGetProcAddress)),
]

AVVDPAUDeviceContext = struct_AVVDPAUDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vdpau.h: 38

VkBool32 = c_uint32# /usr/include/vulkan/vulkan_core.h: 93

# /usr/include/vulkan/vulkan_core.h: 99
class struct_VkImage_T(Structure):
    pass

VkImage = POINTER(struct_VkImage_T)# /usr/include/vulkan/vulkan_core.h: 99

# /usr/include/vulkan/vulkan_core.h: 100
class struct_VkInstance_T(Structure):
    pass

VkInstance = POINTER(struct_VkInstance_T)# /usr/include/vulkan/vulkan_core.h: 100

# /usr/include/vulkan/vulkan_core.h: 101
class struct_VkPhysicalDevice_T(Structure):
    pass

VkPhysicalDevice = POINTER(struct_VkPhysicalDevice_T)# /usr/include/vulkan/vulkan_core.h: 101

# /usr/include/vulkan/vulkan_core.h: 102
class struct_VkDevice_T(Structure):
    pass

VkDevice = POINTER(struct_VkDevice_T)# /usr/include/vulkan/vulkan_core.h: 102

# /usr/include/vulkan/vulkan_core.h: 104
class struct_VkSemaphore_T(Structure):
    pass

VkSemaphore = POINTER(struct_VkSemaphore_T)# /usr/include/vulkan/vulkan_core.h: 104

# /usr/include/vulkan/vulkan_core.h: 107
class struct_VkDeviceMemory_T(Structure):
    pass

VkDeviceMemory = POINTER(struct_VkDeviceMemory_T)# /usr/include/vulkan/vulkan_core.h: 107

enum_VkStructureType = c_int# /usr/include/vulkan/vulkan_core.h: 965

VkStructureType = enum_VkStructureType# /usr/include/vulkan/vulkan_core.h: 965

enum_VkImageLayout = c_int# /usr/include/vulkan/vulkan_core.h: 1015

VkImageLayout = enum_VkImageLayout# /usr/include/vulkan/vulkan_core.h: 1015

enum_VkSystemAllocationScope = c_int# /usr/include/vulkan/vulkan_core.h: 1094

VkSystemAllocationScope = enum_VkSystemAllocationScope# /usr/include/vulkan/vulkan_core.h: 1094

enum_VkInternalAllocationType = c_int# /usr/include/vulkan/vulkan_core.h: 1099

VkInternalAllocationType = enum_VkInternalAllocationType# /usr/include/vulkan/vulkan_core.h: 1099

enum_VkFormat = c_int# /usr/include/vulkan/vulkan_core.h: 1384

VkFormat = enum_VkFormat# /usr/include/vulkan/vulkan_core.h: 1384

enum_VkImageTiling = c_int# /usr/include/vulkan/vulkan_core.h: 1391

VkImageTiling = enum_VkImageTiling# /usr/include/vulkan/vulkan_core.h: 1391

enum_VkAccessFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 1789

VkAccessFlagBits = enum_VkAccessFlagBits# /usr/include/vulkan/vulkan_core.h: 1789

enum_VkImageUsageFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 1936

VkImageUsageFlagBits = enum_VkImageUsageFlagBits# /usr/include/vulkan/vulkan_core.h: 1936

enum_VkMemoryPropertyFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 1959

VkMemoryPropertyFlagBits = enum_VkMemoryPropertyFlagBits# /usr/include/vulkan/vulkan_core.h: 1959

PFN_vkAllocationFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), c_size_t, c_size_t, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2443

PFN_vkFreeFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None))# /usr/include/vulkan/vulkan_core.h: 2449

PFN_vkInternalAllocationNotification = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_size_t, VkInternalAllocationType, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2453

PFN_vkInternalFreeNotification = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_size_t, VkInternalAllocationType, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2459

PFN_vkReallocationFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), POINTER(None), c_size_t, c_size_t, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2465

# /usr/include/vulkan/vulkan_core.h: 2480
class struct_VkAllocationCallbacks(Structure):
    pass

struct_VkAllocationCallbacks.__slots__ = [
    'pUserData',
    'pfnAllocation',
    'pfnReallocation',
    'pfnFree',
    'pfnInternalAllocation',
    'pfnInternalFree',
]
struct_VkAllocationCallbacks._fields_ = [
    ('pUserData', POINTER(None)),
    ('pfnAllocation', PFN_vkAllocationFunction),
    ('pfnReallocation', PFN_vkReallocationFunction),
    ('pfnFree', PFN_vkFreeFunction),
    ('pfnInternalAllocation', PFN_vkInternalAllocationNotification),
    ('pfnInternalFree', PFN_vkInternalFreeNotification),
]

VkAllocationCallbacks = struct_VkAllocationCallbacks# /usr/include/vulkan/vulkan_core.h: 2480

# /usr/include/vulkan/vulkan_core.h: 2583
class struct_VkPhysicalDeviceFeatures(Structure):
    pass

struct_VkPhysicalDeviceFeatures.__slots__ = [
    'robustBufferAccess',
    'fullDrawIndexUint32',
    'imageCubeArray',
    'independentBlend',
    'geometryShader',
    'tessellationShader',
    'sampleRateShading',
    'dualSrcBlend',
    'logicOp',
    'multiDrawIndirect',
    'drawIndirectFirstInstance',
    'depthClamp',
    'depthBiasClamp',
    'fillModeNonSolid',
    'depthBounds',
    'wideLines',
    'largePoints',
    'alphaToOne',
    'multiViewport',
    'samplerAnisotropy',
    'textureCompressionETC2',
    'textureCompressionASTC_LDR',
    'textureCompressionBC',
    'occlusionQueryPrecise',
    'pipelineStatisticsQuery',
    'vertexPipelineStoresAndAtomics',
    'fragmentStoresAndAtomics',
    'shaderTessellationAndGeometryPointSize',
    'shaderImageGatherExtended',
    'shaderStorageImageExtendedFormats',
    'shaderStorageImageMultisample',
    'shaderStorageImageReadWithoutFormat',
    'shaderStorageImageWriteWithoutFormat',
    'shaderUniformBufferArrayDynamicIndexing',
    'shaderSampledImageArrayDynamicIndexing',
    'shaderStorageBufferArrayDynamicIndexing',
    'shaderStorageImageArrayDynamicIndexing',
    'shaderClipDistance',
    'shaderCullDistance',
    'shaderFloat64',
    'shaderInt64',
    'shaderInt16',
    'shaderResourceResidency',
    'shaderResourceMinLod',
    'sparseBinding',
    'sparseResidencyBuffer',
    'sparseResidencyImage2D',
    'sparseResidencyImage3D',
    'sparseResidency2Samples',
    'sparseResidency4Samples',
    'sparseResidency8Samples',
    'sparseResidency16Samples',
    'sparseResidencyAliased',
    'variableMultisampleRate',
    'inheritedQueries',
]
struct_VkPhysicalDeviceFeatures._fields_ = [
    ('robustBufferAccess', VkBool32),
    ('fullDrawIndexUint32', VkBool32),
    ('imageCubeArray', VkBool32),
    ('independentBlend', VkBool32),
    ('geometryShader', VkBool32),
    ('tessellationShader', VkBool32),
    ('sampleRateShading', VkBool32),
    ('dualSrcBlend', VkBool32),
    ('logicOp', VkBool32),
    ('multiDrawIndirect', VkBool32),
    ('drawIndirectFirstInstance', VkBool32),
    ('depthClamp', VkBool32),
    ('depthBiasClamp', VkBool32),
    ('fillModeNonSolid', VkBool32),
    ('depthBounds', VkBool32),
    ('wideLines', VkBool32),
    ('largePoints', VkBool32),
    ('alphaToOne', VkBool32),
    ('multiViewport', VkBool32),
    ('samplerAnisotropy', VkBool32),
    ('textureCompressionETC2', VkBool32),
    ('textureCompressionASTC_LDR', VkBool32),
    ('textureCompressionBC', VkBool32),
    ('occlusionQueryPrecise', VkBool32),
    ('pipelineStatisticsQuery', VkBool32),
    ('vertexPipelineStoresAndAtomics', VkBool32),
    ('fragmentStoresAndAtomics', VkBool32),
    ('shaderTessellationAndGeometryPointSize', VkBool32),
    ('shaderImageGatherExtended', VkBool32),
    ('shaderStorageImageExtendedFormats', VkBool32),
    ('shaderStorageImageMultisample', VkBool32),
    ('shaderStorageImageReadWithoutFormat', VkBool32),
    ('shaderStorageImageWriteWithoutFormat', VkBool32),
    ('shaderUniformBufferArrayDynamicIndexing', VkBool32),
    ('shaderSampledImageArrayDynamicIndexing', VkBool32),
    ('shaderStorageBufferArrayDynamicIndexing', VkBool32),
    ('shaderStorageImageArrayDynamicIndexing', VkBool32),
    ('shaderClipDistance', VkBool32),
    ('shaderCullDistance', VkBool32),
    ('shaderFloat64', VkBool32),
    ('shaderInt64', VkBool32),
    ('shaderInt16', VkBool32),
    ('shaderResourceResidency', VkBool32),
    ('shaderResourceMinLod', VkBool32),
    ('sparseBinding', VkBool32),
    ('sparseResidencyBuffer', VkBool32),
    ('sparseResidencyImage2D', VkBool32),
    ('sparseResidencyImage3D', VkBool32),
    ('sparseResidency2Samples', VkBool32),
    ('sparseResidency4Samples', VkBool32),
    ('sparseResidency8Samples', VkBool32),
    ('sparseResidency16Samples', VkBool32),
    ('sparseResidencyAliased', VkBool32),
    ('variableMultisampleRate', VkBool32),
    ('inheritedQueries', VkBool32),
]

VkPhysicalDeviceFeatures = struct_VkPhysicalDeviceFeatures# /usr/include/vulkan/vulkan_core.h: 2583

# /usr/include/vulkan/vulkan_core.h: 4750
class struct_VkPhysicalDeviceFeatures2(Structure):
    pass

struct_VkPhysicalDeviceFeatures2.__slots__ = [
    'sType',
    'pNext',
    'features',
]
struct_VkPhysicalDeviceFeatures2._fields_ = [
    ('sType', VkStructureType),
    ('pNext', POINTER(None)),
    ('features', VkPhysicalDeviceFeatures),
]

VkPhysicalDeviceFeatures2 = struct_VkPhysicalDeviceFeatures2# /usr/include/vulkan/vulkan_core.h: 4750

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 107
class struct_AVVulkanDeviceContext(Structure):
    pass

struct_AVVulkanDeviceContext.__slots__ = [
    'alloc',
    'inst',
    'phys_dev',
    'act_dev',
    'queue_family_index',
    'nb_graphics_queues',
    'queue_family_tx_index',
    'nb_tx_queues',
    'queue_family_comp_index',
    'nb_comp_queues',
    'enabled_inst_extensions',
    'nb_enabled_inst_extensions',
    'enabled_dev_extensions',
    'nb_enabled_dev_extensions',
    'device_features',
]
struct_AVVulkanDeviceContext._fields_ = [
    ('alloc', POINTER(VkAllocationCallbacks)),
    ('inst', VkInstance),
    ('phys_dev', VkPhysicalDevice),
    ('act_dev', VkDevice),
    ('queue_family_index', c_int),
    ('nb_graphics_queues', c_int),
    ('queue_family_tx_index', c_int),
    ('nb_tx_queues', c_int),
    ('queue_family_comp_index', c_int),
    ('nb_comp_queues', c_int),
    ('enabled_inst_extensions', POINTER(POINTER(c_char))),
    ('nb_enabled_inst_extensions', c_int),
    ('enabled_dev_extensions', POINTER(POINTER(c_char))),
    ('nb_enabled_dev_extensions', c_int),
    ('device_features', VkPhysicalDeviceFeatures2),
]

AVVulkanDeviceContext = struct_AVVulkanDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 107

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 134
class struct_AVVulkanFramesContext(Structure):
    pass

struct_AVVulkanFramesContext.__slots__ = [
    'tiling',
    'usage',
    'create_pnext',
    'alloc_pnext',
]
struct_AVVulkanFramesContext._fields_ = [
    ('tiling', VkImageTiling),
    ('usage', VkImageUsageFlagBits),
    ('create_pnext', POINTER(None)),
    ('alloc_pnext', POINTER(None) * int(8)),
]

AVVulkanFramesContext = struct_AVVulkanFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 134

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 189
class struct_AVVkFrameInternal(Structure):
    pass

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 190
class struct_AVVkFrame(Structure):
    pass

struct_AVVkFrame.__slots__ = [
    'img',
    'tiling',
    'mem',
    'size',
    'flags',
    'access',
    'layout',
    'sem',
    'internal',
]
struct_AVVkFrame._fields_ = [
    ('img', VkImage * int(8)),
    ('tiling', VkImageTiling),
    ('mem', VkDeviceMemory * int(8)),
    ('size', c_size_t * int(8)),
    ('flags', VkMemoryPropertyFlagBits),
    ('access', VkAccessFlagBits * int(8)),
    ('layout', VkImageLayout * int(8)),
    ('sem', VkSemaphore * int(8)),
    ('internal', POINTER(struct_AVVkFrameInternal)),
]

AVVkFrame = struct_AVVkFrame# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 190

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 196
for _lib in _libs.values():
    if not _lib.has("av_vk_frame_alloc", "cdecl"):
        continue
    av_vk_frame_alloc = _lib.get("av_vk_frame_alloc", "cdecl")
    av_vk_frame_alloc.argtypes = []
    av_vk_frame_alloc.restype = POINTER(AVVkFrame)
    break

# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 202
for _lib in _libs.values():
    if not _lib.has("av_vkfmt_from_pixfmt", "cdecl"):
        continue
    av_vkfmt_from_pixfmt = _lib.get("av_vkfmt_from_pixfmt", "cdecl")
    av_vkfmt_from_pixfmt.argtypes = [enum_AVPixelFormat]
    av_vkfmt_from_pixfmt.restype = POINTER(VkFormat)
    break

# /home/josiah/ctypesgen_test/av/pixdesc.h: 70
class struct_AVComponentDescriptor(Structure):
    pass

struct_AVComponentDescriptor.__slots__ = [
    'plane',
    'step',
    'offset',
    'shift',
    'depth',
    'step_minus1',
    'depth_minus1',
    'offset_plus1',
]
struct_AVComponentDescriptor._fields_ = [
    ('plane', c_int),
    ('step', c_int),
    ('offset', c_int),
    ('shift', c_int),
    ('depth', c_int),
    ('step_minus1', c_int),
    ('depth_minus1', c_int),
    ('offset_plus1', c_int),
]

AVComponentDescriptor = struct_AVComponentDescriptor# /home/josiah/ctypesgen_test/av/pixdesc.h: 70

# /home/josiah/ctypesgen_test/av/pixdesc.h: 123
class struct_AVPixFmtDescriptor(Structure):
    pass

struct_AVPixFmtDescriptor.__slots__ = [
    'name',
    'nb_components',
    'log2_chroma_w',
    'log2_chroma_h',
    'flags',
    'comp',
    'alias',
]
struct_AVPixFmtDescriptor._fields_ = [
    ('name', String),
    ('nb_components', c_uint8),
    ('log2_chroma_w', c_uint8),
    ('log2_chroma_h', c_uint8),
    ('flags', c_uint64),
    ('comp', AVComponentDescriptor * int(4)),
    ('alias', String),
]

AVPixFmtDescriptor = struct_AVPixFmtDescriptor# /home/josiah/ctypesgen_test/av/pixdesc.h: 123

# /home/josiah/ctypesgen_test/av/pixdesc.h: 201
if _libs["avcodec"].has("av_get_bits_per_pixel", "cdecl"):
    av_get_bits_per_pixel = _libs["avcodec"].get("av_get_bits_per_pixel", "cdecl")
    av_get_bits_per_pixel.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_get_bits_per_pixel.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 207
if _libs["avcodec"].has("av_get_padded_bits_per_pixel", "cdecl"):
    av_get_padded_bits_per_pixel = _libs["avcodec"].get("av_get_padded_bits_per_pixel", "cdecl")
    av_get_padded_bits_per_pixel.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_get_padded_bits_per_pixel.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 213
if _libs["avcodec"].has("av_pix_fmt_desc_get", "cdecl"):
    av_pix_fmt_desc_get = _libs["avcodec"].get("av_pix_fmt_desc_get", "cdecl")
    av_pix_fmt_desc_get.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_desc_get.restype = POINTER(AVPixFmtDescriptor)

# /home/josiah/ctypesgen_test/av/pixdesc.h: 222
if _libs["avcodec"].has("av_pix_fmt_desc_next", "cdecl"):
    av_pix_fmt_desc_next = _libs["avcodec"].get("av_pix_fmt_desc_next", "cdecl")
    av_pix_fmt_desc_next.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_pix_fmt_desc_next.restype = POINTER(AVPixFmtDescriptor)

# /home/josiah/ctypesgen_test/av/pixdesc.h: 228
if _libs["avcodec"].has("av_pix_fmt_desc_get_id", "cdecl"):
    av_pix_fmt_desc_get_id = _libs["avcodec"].get("av_pix_fmt_desc_get_id", "cdecl")
    av_pix_fmt_desc_get_id.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_pix_fmt_desc_get_id.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/pixdesc.h: 240
if _libs["avcodec"].has("av_pix_fmt_get_chroma_sub_sample", "cdecl"):
    av_pix_fmt_get_chroma_sub_sample = _libs["avcodec"].get("av_pix_fmt_get_chroma_sub_sample", "cdecl")
    av_pix_fmt_get_chroma_sub_sample.argtypes = [enum_AVPixelFormat, POINTER(c_int), POINTER(c_int)]
    av_pix_fmt_get_chroma_sub_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 247
if _libs["avcodec"].has("av_pix_fmt_count_planes", "cdecl"):
    av_pix_fmt_count_planes = _libs["avcodec"].get("av_pix_fmt_count_planes", "cdecl")
    av_pix_fmt_count_planes.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_count_planes.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 252
if _libs["avcodec"].has("av_color_range_name", "cdecl"):
    av_color_range_name = _libs["avcodec"].get("av_color_range_name", "cdecl")
    av_color_range_name.argtypes = [enum_AVColorRange]
    av_color_range_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 257
if _libs["avcodec"].has("av_color_range_from_name", "cdecl"):
    av_color_range_from_name = _libs["avcodec"].get("av_color_range_from_name", "cdecl")
    av_color_range_from_name.argtypes = [String]
    av_color_range_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 262
if _libs["avcodec"].has("av_color_primaries_name", "cdecl"):
    av_color_primaries_name = _libs["avcodec"].get("av_color_primaries_name", "cdecl")
    av_color_primaries_name.argtypes = [enum_AVColorPrimaries]
    av_color_primaries_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 267
if _libs["avcodec"].has("av_color_primaries_from_name", "cdecl"):
    av_color_primaries_from_name = _libs["avcodec"].get("av_color_primaries_from_name", "cdecl")
    av_color_primaries_from_name.argtypes = [String]
    av_color_primaries_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 272
if _libs["avcodec"].has("av_color_transfer_name", "cdecl"):
    av_color_transfer_name = _libs["avcodec"].get("av_color_transfer_name", "cdecl")
    av_color_transfer_name.argtypes = [enum_AVColorTransferCharacteristic]
    av_color_transfer_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 277
if _libs["avcodec"].has("av_color_transfer_from_name", "cdecl"):
    av_color_transfer_from_name = _libs["avcodec"].get("av_color_transfer_from_name", "cdecl")
    av_color_transfer_from_name.argtypes = [String]
    av_color_transfer_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 282
if _libs["avcodec"].has("av_color_space_name", "cdecl"):
    av_color_space_name = _libs["avcodec"].get("av_color_space_name", "cdecl")
    av_color_space_name.argtypes = [enum_AVColorSpace]
    av_color_space_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 287
if _libs["avcodec"].has("av_color_space_from_name", "cdecl"):
    av_color_space_from_name = _libs["avcodec"].get("av_color_space_from_name", "cdecl")
    av_color_space_from_name.argtypes = [String]
    av_color_space_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 292
if _libs["avcodec"].has("av_chroma_location_name", "cdecl"):
    av_chroma_location_name = _libs["avcodec"].get("av_chroma_location_name", "cdecl")
    av_chroma_location_name.argtypes = [enum_AVChromaLocation]
    av_chroma_location_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 297
if _libs["avcodec"].has("av_chroma_location_from_name", "cdecl"):
    av_chroma_location_from_name = _libs["avcodec"].get("av_chroma_location_from_name", "cdecl")
    av_chroma_location_from_name.argtypes = [String]
    av_chroma_location_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 310
if _libs["avcodec"].has("av_get_pix_fmt", "cdecl"):
    av_get_pix_fmt = _libs["avcodec"].get("av_get_pix_fmt", "cdecl")
    av_get_pix_fmt.argtypes = [String]
    av_get_pix_fmt.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/pixdesc.h: 318
if _libs["avcodec"].has("av_get_pix_fmt_name", "cdecl"):
    av_get_pix_fmt_name = _libs["avcodec"].get("av_get_pix_fmt_name", "cdecl")
    av_get_pix_fmt_name.argtypes = [enum_AVPixelFormat]
    av_get_pix_fmt_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/pixdesc.h: 330
if _libs["avcodec"].has("av_get_pix_fmt_string", "cdecl"):
    av_get_pix_fmt_string = _libs["avcodec"].get("av_get_pix_fmt_string", "cdecl")
    av_get_pix_fmt_string.argtypes = [String, c_int, enum_AVPixelFormat]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_pix_fmt_string.restype = ReturnString
    else:
        av_get_pix_fmt_string.restype = String
        av_get_pix_fmt_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/pixdesc.h: 350
if _libs["avcodec"].has("av_read_image_line2", "cdecl"):
    av_read_image_line2 = _libs["avcodec"].get("av_read_image_line2", "cdecl")
    av_read_image_line2.argtypes = [POINTER(None), POINTER(c_uint8) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int, c_int]
    av_read_image_line2.restype = None

# /home/josiah/ctypesgen_test/av/pixdesc.h: 355
if _libs["avcodec"].has("av_read_image_line", "cdecl"):
    av_read_image_line = _libs["avcodec"].get("av_read_image_line", "cdecl")
    av_read_image_line.argtypes = [POINTER(c_uint16), POINTER(c_uint8) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int]
    av_read_image_line.restype = None

# /home/josiah/ctypesgen_test/av/pixdesc.h: 374
if _libs["avcodec"].has("av_write_image_line2", "cdecl"):
    av_write_image_line2 = _libs["avcodec"].get("av_write_image_line2", "cdecl")
    av_write_image_line2.argtypes = [POINTER(None), POINTER(c_uint8) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int]
    av_write_image_line2.restype = None

# /home/josiah/ctypesgen_test/av/pixdesc.h: 378
if _libs["avcodec"].has("av_write_image_line", "cdecl"):
    av_write_image_line = _libs["avcodec"].get("av_write_image_line", "cdecl")
    av_write_image_line.argtypes = [POINTER(c_uint16), POINTER(c_uint8) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int]
    av_write_image_line.restype = None

# /home/josiah/ctypesgen_test/av/pixdesc.h: 390
if _libs["avcodec"].has("av_pix_fmt_swap_endianness", "cdecl"):
    av_pix_fmt_swap_endianness = _libs["avcodec"].get("av_pix_fmt_swap_endianness", "cdecl")
    av_pix_fmt_swap_endianness.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_swap_endianness.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/pixdesc.h: 417
if _libs["avcodec"].has("av_get_pix_fmt_loss", "cdecl"):
    av_get_pix_fmt_loss = _libs["avcodec"].get("av_get_pix_fmt_loss", "cdecl")
    av_get_pix_fmt_loss.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, c_int]
    av_get_pix_fmt_loss.restype = c_int

# /home/josiah/ctypesgen_test/av/pixdesc.h: 439
if _libs["avcodec"].has("av_find_best_pix_fmt_of_2", "cdecl"):
    av_find_best_pix_fmt_of_2 = _libs["avcodec"].get("av_find_best_pix_fmt_of_2", "cdecl")
    av_find_best_pix_fmt_of_2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    av_find_best_pix_fmt_of_2.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/imgutils.h: 50
if _libs["avcodec"].has("av_image_fill_max_pixsteps", "cdecl"):
    av_image_fill_max_pixsteps = _libs["avcodec"].get("av_image_fill_max_pixsteps", "cdecl")
    av_image_fill_max_pixsteps.argtypes = [c_int * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor)]
    av_image_fill_max_pixsteps.restype = None

# /home/josiah/ctypesgen_test/av/imgutils.h: 59
if _libs["avcodec"].has("av_image_get_linesize", "cdecl"):
    av_image_get_linesize = _libs["avcodec"].get("av_image_get_linesize", "cdecl")
    av_image_get_linesize.argtypes = [enum_AVPixelFormat, c_int, c_int]
    av_image_get_linesize.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 68
if _libs["avcodec"].has("av_image_fill_linesizes", "cdecl"):
    av_image_fill_linesizes = _libs["avcodec"].get("av_image_fill_linesizes", "cdecl")
    av_image_fill_linesizes.argtypes = [c_int * int(4), enum_AVPixelFormat, c_int]
    av_image_fill_linesizes.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 81
if _libs["avcodec"].has("av_image_fill_plane_sizes", "cdecl"):
    av_image_fill_plane_sizes = _libs["avcodec"].get("av_image_fill_plane_sizes", "cdecl")
    av_image_fill_plane_sizes.argtypes = [c_size_t * int(4), enum_AVPixelFormat, c_int, c_ptrdiff_t * int(4)]
    av_image_fill_plane_sizes.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 95
if _libs["avcodec"].has("av_image_fill_pointers", "cdecl"):
    av_image_fill_pointers = _libs["avcodec"].get("av_image_fill_pointers", "cdecl")
    av_image_fill_pointers.argtypes = [POINTER(c_uint8) * int(4), enum_AVPixelFormat, c_int, POINTER(c_uint8), c_int * int(4)]
    av_image_fill_pointers.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 108
if _libs["avcodec"].has("av_image_alloc", "cdecl"):
    av_image_alloc = _libs["avcodec"].get("av_image_alloc", "cdecl")
    av_image_alloc.argtypes = [POINTER(c_uint8) * int(4), c_int * int(4), c_int, c_int, enum_AVPixelFormat, c_int]
    av_image_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 123
if _libs["avcodec"].has("av_image_copy_plane", "cdecl"):
    av_image_copy_plane = _libs["avcodec"].get("av_image_copy_plane", "cdecl")
    av_image_copy_plane.argtypes = [POINTER(c_uint8), c_int, POINTER(c_uint8), c_int, c_int, c_int]
    av_image_copy_plane.restype = None

# /home/josiah/ctypesgen_test/av/imgutils.h: 133
if _libs["avcodec"].has("av_image_copy", "cdecl"):
    av_image_copy = _libs["avcodec"].get("av_image_copy", "cdecl")
    av_image_copy.argtypes = [POINTER(c_uint8) * int(4), c_int * int(4), POINTER(c_uint8) * int(4), c_int * int(4), enum_AVPixelFormat, c_int, c_int]
    av_image_copy.restype = None

# /home/josiah/ctypesgen_test/av/imgutils.h: 151
if _libs["avcodec"].has("av_image_copy_uc_from", "cdecl"):
    av_image_copy_uc_from = _libs["avcodec"].get("av_image_copy_uc_from", "cdecl")
    av_image_copy_uc_from.argtypes = [POINTER(c_uint8) * int(4), c_ptrdiff_t * int(4), POINTER(c_uint8) * int(4), c_ptrdiff_t * int(4), enum_AVPixelFormat, c_int, c_int]
    av_image_copy_uc_from.restype = None

# /home/josiah/ctypesgen_test/av/imgutils.h: 181
if _libs["avcodec"].has("av_image_fill_arrays", "cdecl"):
    av_image_fill_arrays = _libs["avcodec"].get("av_image_fill_arrays", "cdecl")
    av_image_fill_arrays.argtypes = [POINTER(c_uint8) * int(4), c_int * int(4), POINTER(c_uint8), enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_fill_arrays.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 195
if _libs["avcodec"].has("av_image_get_buffer_size", "cdecl"):
    av_image_get_buffer_size = _libs["avcodec"].get("av_image_get_buffer_size", "cdecl")
    av_image_get_buffer_size.argtypes = [enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_get_buffer_size.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 214
if _libs["avcodec"].has("av_image_copy_to_buffer", "cdecl"):
    av_image_copy_to_buffer = _libs["avcodec"].get("av_image_copy_to_buffer", "cdecl")
    av_image_copy_to_buffer.argtypes = [POINTER(c_uint8), c_int, POINTER(c_uint8) * int(4), c_int * int(4), enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_copy_to_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 228
if _libs["avcodec"].has("av_image_check_size", "cdecl"):
    av_image_check_size = _libs["avcodec"].get("av_image_check_size", "cdecl")
    av_image_check_size.argtypes = [c_uint, c_uint, c_int, POINTER(None)]
    av_image_check_size.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 243
if _libs["avcodec"].has("av_image_check_size2", "cdecl"):
    av_image_check_size2 = _libs["avcodec"].get("av_image_check_size2", "cdecl")
    av_image_check_size2.argtypes = [c_uint, c_uint, c_int64, enum_AVPixelFormat, c_int, POINTER(None)]
    av_image_check_size2.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 257
if _libs["avcodec"].has("av_image_check_sar", "cdecl"):
    av_image_check_sar = _libs["avcodec"].get("av_image_check_sar", "cdecl")
    av_image_check_sar.argtypes = [c_uint, c_uint, AVRational]
    av_image_check_sar.restype = c_int

# /home/josiah/ctypesgen_test/av/imgutils.h: 282
if _libs["avcodec"].has("av_image_fill_black", "cdecl"):
    av_image_fill_black = _libs["avcodec"].get("av_image_fill_black", "cdecl")
    av_image_fill_black.argtypes = [POINTER(c_uint8) * int(4), c_ptrdiff_t * int(4), enum_AVPixelFormat, enum_AVColorRange, c_int, c_int]
    av_image_fill_black.restype = c_int

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 34
class union_anon_638(Union):
    pass

union_anon_638.__slots__ = [
    'u64',
    'u32',
    'u16',
    'u8',
    'f64',
    'f32',
]
union_anon_638._fields_ = [
    ('u64', c_uint64),
    ('u32', c_uint32 * int(2)),
    ('u16', c_uint16 * int(4)),
    ('u8', c_uint8 * int(8)),
    ('f64', c_double),
    ('f32', c_float * int(2)),
]

av_alias64 = union_anon_638# /home/josiah/ctypesgen_test/av/intreadwrite.h: 34

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 41
class union_anon_639(Union):
    pass

union_anon_639.__slots__ = [
    'u32',
    'u16',
    'u8',
    'f32',
]
union_anon_639._fields_ = [
    ('u32', c_uint32),
    ('u16', c_uint16 * int(2)),
    ('u8', c_uint8 * int(4)),
    ('f32', c_float),
]

av_alias32 = union_anon_639# /home/josiah/ctypesgen_test/av/intreadwrite.h: 41

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 46
class union_anon_640(Union):
    pass

union_anon_640.__slots__ = [
    'u16',
    'u8',
]
union_anon_640._fields_ = [
    ('u16', c_uint16),
    ('u8', c_uint8 * int(2)),
]

av_alias16 = union_anon_640# /home/josiah/ctypesgen_test/av/intreadwrite.h: 46

# /home/josiah/ctypesgen_test/av/jni.h: 36
if _libs["avcodec"].has("av_jni_set_java_vm", "cdecl"):
    av_jni_set_java_vm = _libs["avcodec"].get("av_jni_set_java_vm", "cdecl")
    av_jni_set_java_vm.argtypes = [POINTER(None), POINTER(None)]
    av_jni_set_java_vm.restype = c_int

# /home/josiah/ctypesgen_test/av/jni.h: 44
if _libs["avcodec"].has("av_jni_get_java_vm", "cdecl"):
    av_jni_get_java_vm = _libs["avcodec"].get("av_jni_get_java_vm", "cdecl")
    av_jni_get_java_vm.argtypes = [POINTER(None)]
    av_jni_get_java_vm.restype = POINTER(c_ubyte)
    av_jni_get_java_vm.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/lfg.h: 36
class struct_AVLFG(Structure):
    pass

struct_AVLFG.__slots__ = [
    'state',
    'index',
]
struct_AVLFG._fields_ = [
    ('state', c_uint * int(64)),
    ('index', c_int),
]

AVLFG = struct_AVLFG# /home/josiah/ctypesgen_test/av/lfg.h: 36

# /home/josiah/ctypesgen_test/av/lfg.h: 38
if _libs["avcodec"].has("av_lfg_init", "cdecl"):
    av_lfg_init = _libs["avcodec"].get("av_lfg_init", "cdecl")
    av_lfg_init.argtypes = [POINTER(AVLFG), c_uint]
    av_lfg_init.restype = None

# /home/josiah/ctypesgen_test/av/lfg.h: 45
if _libs["avcodec"].has("av_lfg_init_from_data", "cdecl"):
    av_lfg_init_from_data = _libs["avcodec"].get("av_lfg_init_from_data", "cdecl")
    av_lfg_init_from_data.argtypes = [POINTER(AVLFG), POINTER(c_uint8), c_uint]
    av_lfg_init_from_data.restype = c_int

# /home/josiah/ctypesgen_test/av/lfg.h: 54
for _lib in _libs.values():
    try:
        a = (c_uint).in_dll(_lib, "a")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/lfg.h: 65
for _lib in _libs.values():
    try:
        a = (c_uint).in_dll(_lib, "a")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/lfg.h: 66
for _lib in _libs.values():
    try:
        b = (c_uint).in_dll(_lib, "b")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/lfg.h: 78
if _libs["avcodec"].has("av_bmg_get", "cdecl"):
    av_bmg_get = _libs["avcodec"].get("av_bmg_get", "cdecl")
    av_bmg_get.argtypes = [POINTER(AVLFG), c_double * int(2)]
    av_bmg_get.restype = None

# /home/josiah/ctypesgen_test/av/lzo.h: 60
if _libs["avcodec"].has("av_lzo1x_decode", "cdecl"):
    av_lzo1x_decode = _libs["avcodec"].get("av_lzo1x_decode", "cdecl")
    av_lzo1x_decode.argtypes = [POINTER(None), POINTER(c_int), POINTER(None), POINTER(c_int)]
    av_lzo1x_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 69
class struct_AVMasteringDisplayMetadata(Structure):
    pass

struct_AVMasteringDisplayMetadata.__slots__ = [
    'display_primaries',
    'white_point',
    'min_luminance',
    'max_luminance',
    'has_primaries',
    'has_luminance',
]
struct_AVMasteringDisplayMetadata._fields_ = [
    ('display_primaries', (AVRational * int(2)) * int(3)),
    ('white_point', AVRational * int(2)),
    ('min_luminance', AVRational),
    ('max_luminance', AVRational),
    ('has_primaries', c_int),
    ('has_luminance', c_int),
]

AVMasteringDisplayMetadata = struct_AVMasteringDisplayMetadata# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 69

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 78
if _libs["avcodec"].has("av_mastering_display_metadata_alloc", "cdecl"):
    av_mastering_display_metadata_alloc = _libs["avcodec"].get("av_mastering_display_metadata_alloc", "cdecl")
    av_mastering_display_metadata_alloc.argtypes = []
    av_mastering_display_metadata_alloc.restype = POINTER(AVMasteringDisplayMetadata)

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 87
if _libs["avcodec"].has("av_mastering_display_metadata_create_side_data", "cdecl"):
    av_mastering_display_metadata_create_side_data = _libs["avcodec"].get("av_mastering_display_metadata_create_side_data", "cdecl")
    av_mastering_display_metadata_create_side_data.argtypes = [POINTER(AVFrame)]
    av_mastering_display_metadata_create_side_data.restype = POINTER(AVMasteringDisplayMetadata)

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 108
class struct_AVContentLightMetadata(Structure):
    pass

struct_AVContentLightMetadata.__slots__ = [
    'MaxCLL',
    'MaxFALL',
]
struct_AVContentLightMetadata._fields_ = [
    ('MaxCLL', c_uint),
    ('MaxFALL', c_uint),
]

AVContentLightMetadata = struct_AVContentLightMetadata# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 108

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 117
if _libs["avcodec"].has("av_content_light_metadata_alloc", "cdecl"):
    av_content_light_metadata_alloc = _libs["avcodec"].get("av_content_light_metadata_alloc", "cdecl")
    av_content_light_metadata_alloc.argtypes = [POINTER(c_size_t)]
    av_content_light_metadata_alloc.restype = POINTER(AVContentLightMetadata)

# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 126
if _libs["avcodec"].has("av_content_light_metadata_create_side_data", "cdecl"):
    av_content_light_metadata_create_side_data = _libs["avcodec"].get("av_content_light_metadata_create_side_data", "cdecl")
    av_content_light_metadata_create_side_data.argtypes = [POINTER(AVFrame)]
    av_content_light_metadata_create_side_data.restype = POINTER(AVContentLightMetadata)

# /home/josiah/ctypesgen_test/av/md5.h: 44
try:
    av_md5_size = (c_int).in_dll(_libs["avcodec"], "av_md5_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/md5.h: 46
class struct_AVMD5(Structure):
    pass

# /home/josiah/ctypesgen_test/av/md5.h: 51
if _libs["avcodec"].has("av_md5_alloc", "cdecl"):
    av_md5_alloc = _libs["avcodec"].get("av_md5_alloc", "cdecl")
    av_md5_alloc.argtypes = []
    av_md5_alloc.restype = POINTER(struct_AVMD5)

# /home/josiah/ctypesgen_test/av/md5.h: 58
if _libs["avcodec"].has("av_md5_init", "cdecl"):
    av_md5_init = _libs["avcodec"].get("av_md5_init", "cdecl")
    av_md5_init.argtypes = [POINTER(struct_AVMD5)]
    av_md5_init.restype = None

# /home/josiah/ctypesgen_test/av/md5.h: 68
if _libs["avcodec"].has("av_md5_update", "cdecl"):
    av_md5_update = _libs["avcodec"].get("av_md5_update", "cdecl")
    av_md5_update.argtypes = [POINTER(struct_AVMD5), POINTER(c_uint8), c_int]
    av_md5_update.restype = None

# /home/josiah/ctypesgen_test/av/md5.h: 79
if _libs["avcodec"].has("av_md5_final", "cdecl"):
    av_md5_final = _libs["avcodec"].get("av_md5_final", "cdecl")
    av_md5_final.argtypes = [POINTER(struct_AVMD5), POINTER(c_uint8)]
    av_md5_final.restype = None

# /home/josiah/ctypesgen_test/av/md5.h: 89
if _libs["avcodec"].has("av_md5_sum", "cdecl"):
    av_md5_sum = _libs["avcodec"].get("av_md5_sum", "cdecl")
    av_md5_sum.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int]
    av_md5_sum.restype = None

# /home/josiah/ctypesgen_test/av/mediacodec.h: 40
class struct_AVMediaCodecContext(Structure):
    pass

struct_AVMediaCodecContext.__slots__ = [
    'surface',
]
struct_AVMediaCodecContext._fields_ = [
    ('surface', POINTER(None)),
]

AVMediaCodecContext = struct_AVMediaCodecContext# /home/josiah/ctypesgen_test/av/mediacodec.h: 40

# /home/josiah/ctypesgen_test/av/mediacodec.h: 50
if _libs["avcodec"].has("av_mediacodec_alloc_context", "cdecl"):
    av_mediacodec_alloc_context = _libs["avcodec"].get("av_mediacodec_alloc_context", "cdecl")
    av_mediacodec_alloc_context.argtypes = []
    av_mediacodec_alloc_context.restype = POINTER(AVMediaCodecContext)

# /home/josiah/ctypesgen_test/av/mediacodec.h: 60
if _libs["avcodec"].has("av_mediacodec_default_init", "cdecl"):
    av_mediacodec_default_init = _libs["avcodec"].get("av_mediacodec_default_init", "cdecl")
    av_mediacodec_default_init.argtypes = [POINTER(AVCodecContext), POINTER(AVMediaCodecContext), POINTER(None)]
    av_mediacodec_default_init.restype = c_int

# /home/josiah/ctypesgen_test/av/mediacodec.h: 68
if _libs["avcodec"].has("av_mediacodec_default_free", "cdecl"):
    av_mediacodec_default_free = _libs["avcodec"].get("av_mediacodec_default_free", "cdecl")
    av_mediacodec_default_free.argtypes = [POINTER(AVCodecContext)]
    av_mediacodec_default_free.restype = None

# /home/josiah/ctypesgen_test/av/mediacodec.h: 73
class struct_MediaCodecBuffer(Structure):
    pass

AVMediaCodecBuffer = struct_MediaCodecBuffer# /home/josiah/ctypesgen_test/av/mediacodec.h: 73

# /home/josiah/ctypesgen_test/av/mediacodec.h: 86
if _libs["avcodec"].has("av_mediacodec_release_buffer", "cdecl"):
    av_mediacodec_release_buffer = _libs["avcodec"].get("av_mediacodec_release_buffer", "cdecl")
    av_mediacodec_release_buffer.argtypes = [POINTER(AVMediaCodecBuffer), c_int]
    av_mediacodec_release_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/mediacodec.h: 99
if _libs["avcodec"].has("av_mediacodec_render_buffer_at_time", "cdecl"):
    av_mediacodec_render_buffer_at_time = _libs["avcodec"].get("av_mediacodec_render_buffer_at_time", "cdecl")
    av_mediacodec_render_buffer_at_time.argtypes = [POINTER(AVMediaCodecBuffer), c_int64]
    av_mediacodec_render_buffer_at_time.restype = c_int

# /home/josiah/ctypesgen_test/av/motion_vector.h: 55
class struct_AVMotionVector(Structure):
    pass

struct_AVMotionVector.__slots__ = [
    'source',
    'w',
    'h',
    'src_x',
    'src_y',
    'dst_x',
    'dst_y',
    'flags',
    'motion_x',
    'motion_y',
    'motion_scale',
]
struct_AVMotionVector._fields_ = [
    ('source', c_int32),
    ('w', c_uint8),
    ('h', c_uint8),
    ('src_x', c_int16),
    ('src_y', c_int16),
    ('dst_x', c_int16),
    ('dst_y', c_int16),
    ('flags', c_uint64),
    ('motion_x', c_int32),
    ('motion_y', c_int32),
    ('motion_scale', c_uint16),
]

AVMotionVector = struct_AVMotionVector# /home/josiah/ctypesgen_test/av/motion_vector.h: 55

# /home/josiah/ctypesgen_test/av/murmur3.h: 69
class struct_AVMurMur3(Structure):
    pass

# /home/josiah/ctypesgen_test/av/murmur3.h: 69
if _libs["avcodec"].has("av_murmur3_alloc", "cdecl"):
    av_murmur3_alloc = _libs["avcodec"].get("av_murmur3_alloc", "cdecl")
    av_murmur3_alloc.argtypes = []
    av_murmur3_alloc.restype = POINTER(struct_AVMurMur3)

# /home/josiah/ctypesgen_test/av/murmur3.h: 81
if _libs["avcodec"].has("av_murmur3_init_seeded", "cdecl"):
    av_murmur3_init_seeded = _libs["avcodec"].get("av_murmur3_init_seeded", "cdecl")
    av_murmur3_init_seeded.argtypes = [POINTER(struct_AVMurMur3), c_uint64]
    av_murmur3_init_seeded.restype = None

# /home/josiah/ctypesgen_test/av/murmur3.h: 94
if _libs["avcodec"].has("av_murmur3_init", "cdecl"):
    av_murmur3_init = _libs["avcodec"].get("av_murmur3_init", "cdecl")
    av_murmur3_init.argtypes = [POINTER(struct_AVMurMur3)]
    av_murmur3_init.restype = None

# /home/josiah/ctypesgen_test/av/murmur3.h: 104
if _libs["avcodec"].has("av_murmur3_update", "cdecl"):
    av_murmur3_update = _libs["avcodec"].get("av_murmur3_update", "cdecl")
    av_murmur3_update.argtypes = [POINTER(struct_AVMurMur3), POINTER(c_uint8), c_int]
    av_murmur3_update.restype = None

# /home/josiah/ctypesgen_test/av/murmur3.h: 115
if _libs["avcodec"].has("av_murmur3_final", "cdecl"):
    av_murmur3_final = _libs["avcodec"].get("av_murmur3_final", "cdecl")
    av_murmur3_final.argtypes = [POINTER(struct_AVMurMur3), c_uint8 * int(16)]
    av_murmur3_final.restype = None

# /home/josiah/ctypesgen_test/av/parseutils.h: 49
if _libs["avcodec"].has("av_parse_ratio", "cdecl"):
    av_parse_ratio = _libs["avcodec"].get("av_parse_ratio", "cdecl")
    av_parse_ratio.argtypes = [POINTER(AVRational), String, c_int, c_int, POINTER(None)]
    av_parse_ratio.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 66
if _libs["avcodec"].has("av_parse_video_size", "cdecl"):
    av_parse_video_size = _libs["avcodec"].get("av_parse_video_size", "cdecl")
    av_parse_video_size.argtypes = [POINTER(c_int), POINTER(c_int), String]
    av_parse_video_size.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 77
if _libs["avcodec"].has("av_parse_video_rate", "cdecl"):
    av_parse_video_rate = _libs["avcodec"].get("av_parse_video_rate", "cdecl")
    av_parse_video_rate.argtypes = [POINTER(AVRational), String]
    av_parse_video_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 98
if _libs["avcodec"].has("av_parse_color", "cdecl"):
    av_parse_color = _libs["avcodec"].get("av_parse_color", "cdecl")
    av_parse_color.argtypes = [POINTER(c_uint8), String, c_int, POINTER(None)]
    av_parse_color.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 112
if _libs["avcodec"].has("av_get_known_color_name", "cdecl"):
    av_get_known_color_name = _libs["avcodec"].get("av_get_known_color_name", "cdecl")
    av_get_known_color_name.argtypes = [c_int, POINTER(POINTER(c_uint8))]
    av_get_known_color_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/parseutils.h: 146
if _libs["avcodec"].has("av_parse_time", "cdecl"):
    av_parse_time = _libs["avcodec"].get("av_parse_time", "cdecl")
    av_parse_time.argtypes = [POINTER(c_int64), String, c_int]
    av_parse_time.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 154
if _libs["avcodec"].has("av_find_info_tag", "cdecl"):
    av_find_info_tag = _libs["avcodec"].get("av_find_info_tag", "cdecl")
    av_find_info_tag.argtypes = [String, c_int, String, String]
    av_find_info_tag.restype = c_int

# /home/josiah/ctypesgen_test/av/parseutils.h: 186
if _libs["avcodec"].has("av_small_strptime", "cdecl"):
    av_small_strptime = _libs["avcodec"].get("av_small_strptime", "cdecl")
    av_small_strptime.argtypes = [String, String, POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        av_small_strptime.restype = ReturnString
    else:
        av_small_strptime.restype = String
        av_small_strptime.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/parseutils.h: 191
if _libs["avcodec"].has("av_timegm", "cdecl"):
    av_timegm = _libs["avcodec"].get("av_timegm", "cdecl")
    av_timegm.argtypes = [POINTER(struct_tm)]
    av_timegm.restype = time_t

av_pixelutils_sad_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(c_uint8), c_ptrdiff_t, POINTER(c_uint8), c_ptrdiff_t)# /home/josiah/ctypesgen_test/av/pixelutils.h: 29

# /home/josiah/ctypesgen_test/av/pixelutils.h: 49
if _libs["avcodec"].has("av_pixelutils_get_sad_fn", "cdecl"):
    av_pixelutils_get_sad_fn = _libs["avcodec"].get("av_pixelutils_get_sad_fn", "cdecl")
    av_pixelutils_get_sad_fn.argtypes = [c_int, c_int, c_int, POINTER(None)]
    av_pixelutils_get_sad_fn.restype = av_pixelutils_sad_fn

# /home/josiah/ctypesgen_test/av/qsv.h: 98
class struct_AVQSVContext(Structure):
    pass

struct_AVQSVContext.__slots__ = [
    'session',
    'iopattern',
    'ext_buffers',
    'nb_ext_buffers',
    'opaque_alloc',
    'nb_opaque_surfaces',
    'opaque_surfaces',
    'opaque_alloc_type',
]
struct_AVQSVContext._fields_ = [
    ('session', mfxSession),
    ('iopattern', c_int),
    ('ext_buffers', POINTER(POINTER(mfxExtBuffer))),
    ('nb_ext_buffers', c_int),
    ('opaque_alloc', c_int),
    ('nb_opaque_surfaces', c_int),
    ('opaque_surfaces', POINTER(AVBufferRef)),
    ('opaque_alloc_type', c_int),
]

AVQSVContext = struct_AVQSVContext# /home/josiah/ctypesgen_test/av/qsv.h: 98

# /home/josiah/ctypesgen_test/av/qsv.h: 105
if _libs["avcodec"].has("av_qsv_alloc_context", "cdecl"):
    av_qsv_alloc_context = _libs["avcodec"].get("av_qsv_alloc_context", "cdecl")
    av_qsv_alloc_context.argtypes = []
    av_qsv_alloc_context.restype = POINTER(AVQSVContext)

# /home/josiah/ctypesgen_test/av/random_seed.h: 37
if _libs["avcodec"].has("av_get_random_seed", "cdecl"):
    av_get_random_seed = _libs["avcodec"].get("av_get_random_seed", "cdecl")
    av_get_random_seed.argtypes = []
    av_get_random_seed.restype = c_uint32

# /home/josiah/ctypesgen_test/av/rc4.h: 35
class struct_AVRC4(Structure):
    pass

struct_AVRC4.__slots__ = [
    'state',
    'x',
    'y',
]
struct_AVRC4._fields_ = [
    ('state', c_uint8 * int(256)),
    ('x', c_int),
    ('y', c_int),
]

AVRC4 = struct_AVRC4# /home/josiah/ctypesgen_test/av/rc4.h: 35

# /home/josiah/ctypesgen_test/av/rc4.h: 40
if _libs["avcodec"].has("av_rc4_alloc", "cdecl"):
    av_rc4_alloc = _libs["avcodec"].get("av_rc4_alloc", "cdecl")
    av_rc4_alloc.argtypes = []
    av_rc4_alloc.restype = POINTER(AVRC4)

# /home/josiah/ctypesgen_test/av/rc4.h: 49
if _libs["avcodec"].has("av_rc4_init", "cdecl"):
    av_rc4_init = _libs["avcodec"].get("av_rc4_init", "cdecl")
    av_rc4_init.argtypes = [POINTER(struct_AVRC4), POINTER(c_uint8), c_int, c_int]
    av_rc4_init.restype = c_int

# /home/josiah/ctypesgen_test/av/rc4.h: 60
if _libs["avcodec"].has("av_rc4_crypt", "cdecl"):
    av_rc4_crypt = _libs["avcodec"].get("av_rc4_crypt", "cdecl")
    av_rc4_crypt.argtypes = [POINTER(struct_AVRC4), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_rc4_crypt.restype = None

# /home/josiah/ctypesgen_test/av/replaygain.h: 48
class struct_AVReplayGain(Structure):
    pass

struct_AVReplayGain.__slots__ = [
    'track_gain',
    'track_peak',
    'album_gain',
    'album_peak',
]
struct_AVReplayGain._fields_ = [
    ('track_gain', c_int32),
    ('track_peak', c_uint32),
    ('album_gain', c_int32),
    ('album_peak', c_uint32),
]

AVReplayGain = struct_AVReplayGain# /home/josiah/ctypesgen_test/av/replaygain.h: 48

# /home/josiah/ctypesgen_test/av/ripemd.h: 45
try:
    av_ripemd_size = (c_int).in_dll(_libs["avcodec"], "av_ripemd_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/ripemd.h: 47
class struct_AVRIPEMD(Structure):
    pass

# /home/josiah/ctypesgen_test/av/ripemd.h: 52
if _libs["avcodec"].has("av_ripemd_alloc", "cdecl"):
    av_ripemd_alloc = _libs["avcodec"].get("av_ripemd_alloc", "cdecl")
    av_ripemd_alloc.argtypes = []
    av_ripemd_alloc.restype = POINTER(struct_AVRIPEMD)

# /home/josiah/ctypesgen_test/av/ripemd.h: 61
if _libs["avcodec"].has("av_ripemd_init", "cdecl"):
    av_ripemd_init = _libs["avcodec"].get("av_ripemd_init", "cdecl")
    av_ripemd_init.argtypes = [POINTER(struct_AVRIPEMD), c_int]
    av_ripemd_init.restype = c_int

# /home/josiah/ctypesgen_test/av/ripemd.h: 71
if _libs["avcodec"].has("av_ripemd_update", "cdecl"):
    av_ripemd_update = _libs["avcodec"].get("av_ripemd_update", "cdecl")
    av_ripemd_update.argtypes = [POINTER(struct_AVRIPEMD), POINTER(c_uint8), c_uint]
    av_ripemd_update.restype = None

# /home/josiah/ctypesgen_test/av/ripemd.h: 82
if _libs["avcodec"].has("av_ripemd_final", "cdecl"):
    av_ripemd_final = _libs["avcodec"].get("av_ripemd_final", "cdecl")
    av_ripemd_final.argtypes = [POINTER(struct_AVRIPEMD), POINTER(c_uint8)]
    av_ripemd_final.restype = None

enum_rom1394_node_types_enum = c_int# /home/josiah/ctypesgen_test/av/rom1394.h: 49

ROM1394_NODE_TYPE_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/rom1394.h: 49

ROM1394_NODE_TYPE_DC = (ROM1394_NODE_TYPE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/rom1394.h: 49

ROM1394_NODE_TYPE_AVC = (ROM1394_NODE_TYPE_DC + 1)# /home/josiah/ctypesgen_test/av/rom1394.h: 49

ROM1394_NODE_TYPE_SBP2 = (ROM1394_NODE_TYPE_AVC + 1)# /home/josiah/ctypesgen_test/av/rom1394.h: 49

ROM1394_NODE_TYPE_CPU = (ROM1394_NODE_TYPE_SBP2 + 1)# /home/josiah/ctypesgen_test/av/rom1394.h: 49

rom1394_node_types = enum_rom1394_node_types_enum# /home/josiah/ctypesgen_test/av/rom1394.h: 49

# /home/josiah/ctypesgen_test/av/rom1394.h: 58
class struct_rom1394_bus_options_struct(Structure):
    pass

struct_rom1394_bus_options_struct.__slots__ = [
    'irmc',
    'cmc',
    'isc',
    'bmc',
    'cyc_clk_acc',
    'max_rec',
]
struct_rom1394_bus_options_struct._fields_ = [
    ('irmc', c_char),
    ('cmc', c_char),
    ('isc', c_char),
    ('bmc', c_char),
    ('cyc_clk_acc', c_ubyte),
    ('max_rec', c_int),
]

rom1394_bus_options = struct_rom1394_bus_options_struct# /home/josiah/ctypesgen_test/av/rom1394.h: 58

# /home/josiah/ctypesgen_test/av/rom1394.h: 70
class struct_rom1394_directory_struct(Structure):
    pass

struct_rom1394_directory_struct.__slots__ = [
    'node_capabilities',
    'vendor_id',
    'unit_spec_id',
    'unit_sw_version',
    'model_id',
    'nr_textual_leafs',
    'max_textual_leafs',
    'textual_leafs',
    'label',
]
struct_rom1394_directory_struct._fields_ = [
    ('node_capabilities', quadlet_t),
    ('vendor_id', quadlet_t),
    ('unit_spec_id', quadlet_t),
    ('unit_sw_version', quadlet_t),
    ('model_id', quadlet_t),
    ('nr_textual_leafs', c_int),
    ('max_textual_leafs', c_int),
    ('textual_leafs', POINTER(POINTER(c_char))),
    ('label', String),
]

rom1394_directory = struct_rom1394_directory_struct# /home/josiah/ctypesgen_test/av/rom1394.h: 70

# /home/josiah/ctypesgen_test/av/rom1394.h: 73
if _libs["avdevice"].has("rom1394_get_bus_info_block_length", "cdecl"):
    rom1394_get_bus_info_block_length = _libs["avdevice"].get("rom1394_get_bus_info_block_length", "cdecl")
    rom1394_get_bus_info_block_length.argtypes = [raw1394handle_t, nodeid_t]
    rom1394_get_bus_info_block_length.restype = c_int

# /home/josiah/ctypesgen_test/av/rom1394.h: 76
if _libs["avdevice"].has("rom1394_get_bus_id", "cdecl"):
    rom1394_get_bus_id = _libs["avdevice"].get("rom1394_get_bus_id", "cdecl")
    rom1394_get_bus_id.argtypes = [raw1394handle_t, nodeid_t]
    rom1394_get_bus_id.restype = quadlet_t

# /home/josiah/ctypesgen_test/av/rom1394.h: 79
if _libs["avdevice"].has("rom1394_get_bus_options", "cdecl"):
    rom1394_get_bus_options = _libs["avdevice"].get("rom1394_get_bus_options", "cdecl")
    rom1394_get_bus_options.argtypes = [raw1394handle_t, nodeid_t, POINTER(rom1394_bus_options)]
    rom1394_get_bus_options.restype = c_int

# /home/josiah/ctypesgen_test/av/rom1394.h: 82
if _libs["avdevice"].has("rom1394_get_guid", "cdecl"):
    rom1394_get_guid = _libs["avdevice"].get("rom1394_get_guid", "cdecl")
    rom1394_get_guid.argtypes = [raw1394handle_t, nodeid_t]
    rom1394_get_guid.restype = octlet_t

# /home/josiah/ctypesgen_test/av/rom1394.h: 85
if _libs["avdevice"].has("rom1394_get_directory", "cdecl"):
    rom1394_get_directory = _libs["avdevice"].get("rom1394_get_directory", "cdecl")
    rom1394_get_directory.argtypes = [raw1394handle_t, nodeid_t, POINTER(rom1394_directory)]
    rom1394_get_directory.restype = c_int

# /home/josiah/ctypesgen_test/av/rom1394.h: 88
if _libs["avdevice"].has("rom1394_get_node_type", "cdecl"):
    rom1394_get_node_type = _libs["avdevice"].get("rom1394_get_node_type", "cdecl")
    rom1394_get_node_type.argtypes = [POINTER(rom1394_directory)]
    rom1394_get_node_type.restype = rom1394_node_types

# /home/josiah/ctypesgen_test/av/rom1394.h: 91
if _libs["avdevice"].has("rom1394_free_directory", "cdecl"):
    rom1394_free_directory = _libs["avdevice"].get("rom1394_free_directory", "cdecl")
    rom1394_free_directory.argtypes = [POINTER(rom1394_directory)]
    rom1394_free_directory.restype = None

# /home/josiah/ctypesgen_test/av/rom1394.h: 97
if _libs["avdevice"].has("rom1394_get_size", "cdecl"):
    rom1394_get_size = _libs["avdevice"].get("rom1394_get_size", "cdecl")
    rom1394_get_size.argtypes = [POINTER(quadlet_t)]
    rom1394_get_size.restype = c_int

# /home/josiah/ctypesgen_test/av/rom1394.h: 100
if _libs["avdevice"].has("rom1394_set_directory", "cdecl"):
    rom1394_set_directory = _libs["avdevice"].get("rom1394_set_directory", "cdecl")
    rom1394_set_directory.argtypes = [POINTER(quadlet_t), POINTER(rom1394_directory)]
    rom1394_set_directory.restype = c_int

# /home/josiah/ctypesgen_test/av/rom1394.h: 103
if _libs["avdevice"].has("rom1394_add_unit", "cdecl"):
    rom1394_add_unit = _libs["avdevice"].get("rom1394_add_unit", "cdecl")
    rom1394_add_unit.argtypes = [POINTER(quadlet_t), POINTER(rom1394_directory)]
    rom1394_add_unit.restype = c_int

# /home/josiah/ctypesgen_test/av/sha512.h: 54
try:
    av_sha512_size = (c_int).in_dll(_libs["avcodec"], "av_sha512_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/sha512.h: 56
class struct_AVSHA512(Structure):
    pass

# /home/josiah/ctypesgen_test/av/sha512.h: 61
if _libs["avcodec"].has("av_sha512_alloc", "cdecl"):
    av_sha512_alloc = _libs["avcodec"].get("av_sha512_alloc", "cdecl")
    av_sha512_alloc.argtypes = []
    av_sha512_alloc.restype = POINTER(struct_AVSHA512)

# /home/josiah/ctypesgen_test/av/sha512.h: 70
if _libs["avcodec"].has("av_sha512_init", "cdecl"):
    av_sha512_init = _libs["avcodec"].get("av_sha512_init", "cdecl")
    av_sha512_init.argtypes = [POINTER(struct_AVSHA512), c_int]
    av_sha512_init.restype = c_int

# /home/josiah/ctypesgen_test/av/sha512.h: 80
if _libs["avcodec"].has("av_sha512_update", "cdecl"):
    av_sha512_update = _libs["avcodec"].get("av_sha512_update", "cdecl")
    av_sha512_update.argtypes = [POINTER(struct_AVSHA512), POINTER(c_uint8), c_uint]
    av_sha512_update.restype = None

# /home/josiah/ctypesgen_test/av/sha512.h: 91
if _libs["avcodec"].has("av_sha512_final", "cdecl"):
    av_sha512_final = _libs["avcodec"].get("av_sha512_final", "cdecl")
    av_sha512_final.argtypes = [POINTER(struct_AVSHA512), POINTER(c_uint8)]
    av_sha512_final.restype = None

# /home/josiah/ctypesgen_test/av/sha.h: 52
try:
    av_sha_size = (c_int).in_dll(_libs["avcodec"], "av_sha_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/sha.h: 54
class struct_AVSHA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/sha.h: 59
if _libs["avcodec"].has("av_sha_alloc", "cdecl"):
    av_sha_alloc = _libs["avcodec"].get("av_sha_alloc", "cdecl")
    av_sha_alloc.argtypes = []
    av_sha_alloc.restype = POINTER(struct_AVSHA)

# /home/josiah/ctypesgen_test/av/sha.h: 68
if _libs["avcodec"].has("av_sha_init", "cdecl"):
    av_sha_init = _libs["avcodec"].get("av_sha_init", "cdecl")
    av_sha_init.argtypes = [POINTER(struct_AVSHA), c_int]
    av_sha_init.restype = c_int

# /home/josiah/ctypesgen_test/av/sha.h: 78
if _libs["avcodec"].has("av_sha_update", "cdecl"):
    av_sha_update = _libs["avcodec"].get("av_sha_update", "cdecl")
    av_sha_update.argtypes = [POINTER(struct_AVSHA), POINTER(c_uint8), c_uint]
    av_sha_update.restype = None

# /home/josiah/ctypesgen_test/av/sha.h: 89
if _libs["avcodec"].has("av_sha_final", "cdecl"):
    av_sha_final = _libs["avcodec"].get("av_sha_final", "cdecl")
    av_sha_final.argtypes = [POINTER(struct_AVSHA), POINTER(c_uint8)]
    av_sha_final.restype = None

enum_AVSphericalProjection = c_int# /home/josiah/ctypesgen_test/av/spherical.h: 51

AV_SPHERICAL_EQUIRECTANGULAR = 0# /home/josiah/ctypesgen_test/av/spherical.h: 51

AV_SPHERICAL_CUBEMAP = (AV_SPHERICAL_EQUIRECTANGULAR + 1)# /home/josiah/ctypesgen_test/av/spherical.h: 51

AV_SPHERICAL_EQUIRECTANGULAR_TILE = (AV_SPHERICAL_CUBEMAP + 1)# /home/josiah/ctypesgen_test/av/spherical.h: 51

# /home/josiah/ctypesgen_test/av/spherical.h: 183
class struct_AVSphericalMapping(Structure):
    pass

struct_AVSphericalMapping.__slots__ = [
    'projection',
    'yaw',
    'pitch',
    'roll',
    'bound_left',
    'bound_top',
    'bound_right',
    'bound_bottom',
    'padding',
]
struct_AVSphericalMapping._fields_ = [
    ('projection', enum_AVSphericalProjection),
    ('yaw', c_int32),
    ('pitch', c_int32),
    ('roll', c_int32),
    ('bound_left', c_uint32),
    ('bound_top', c_uint32),
    ('bound_right', c_uint32),
    ('bound_bottom', c_uint32),
    ('padding', c_uint32),
]

AVSphericalMapping = struct_AVSphericalMapping# /home/josiah/ctypesgen_test/av/spherical.h: 183

# /home/josiah/ctypesgen_test/av/spherical.h: 191
if _libs["avcodec"].has("av_spherical_alloc", "cdecl"):
    av_spherical_alloc = _libs["avcodec"].get("av_spherical_alloc", "cdecl")
    av_spherical_alloc.argtypes = [POINTER(c_size_t)]
    av_spherical_alloc.restype = POINTER(AVSphericalMapping)

# /home/josiah/ctypesgen_test/av/spherical.h: 205
if _libs["avcodec"].has("av_spherical_tile_bounds", "cdecl"):
    av_spherical_tile_bounds = _libs["avcodec"].get("av_spherical_tile_bounds", "cdecl")
    av_spherical_tile_bounds.argtypes = [POINTER(AVSphericalMapping), c_size_t, c_size_t, POINTER(c_size_t), POINTER(c_size_t), POINTER(c_size_t), POINTER(c_size_t)]
    av_spherical_tile_bounds.restype = None

# /home/josiah/ctypesgen_test/av/spherical.h: 217
if _libs["avcodec"].has("av_spherical_projection_name", "cdecl"):
    av_spherical_projection_name = _libs["avcodec"].get("av_spherical_projection_name", "cdecl")
    av_spherical_projection_name.argtypes = [enum_AVSphericalProjection]
    av_spherical_projection_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/spherical.h: 226
if _libs["avcodec"].has("av_spherical_from_name", "cdecl"):
    av_spherical_from_name = _libs["avcodec"].get("av_spherical_from_name", "cdecl")
    av_spherical_from_name.argtypes = [String]
    av_spherical_from_name.restype = c_int

enum_AVStereo3DType = c_int# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_2D = 0# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_SIDEBYSIDE = (AV_STEREO3D_2D + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_TOPBOTTOM = (AV_STEREO3D_SIDEBYSIDE + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_FRAMESEQUENCE = (AV_STEREO3D_TOPBOTTOM + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_CHECKERBOARD = (AV_STEREO3D_FRAMESEQUENCE + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_SIDEBYSIDE_QUINCUNX = (AV_STEREO3D_CHECKERBOARD + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_LINES = (AV_STEREO3D_SIDEBYSIDE_QUINCUNX + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

AV_STEREO3D_COLUMNS = (AV_STEREO3D_LINES + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 51

enum_AVStereo3DView = c_int# /home/josiah/ctypesgen_test/av/stereo3d.h: 147

AV_STEREO3D_VIEW_PACKED = 0# /home/josiah/ctypesgen_test/av/stereo3d.h: 147

AV_STEREO3D_VIEW_LEFT = (AV_STEREO3D_VIEW_PACKED + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 147

AV_STEREO3D_VIEW_RIGHT = (AV_STEREO3D_VIEW_LEFT + 1)# /home/josiah/ctypesgen_test/av/stereo3d.h: 147

# /home/josiah/ctypesgen_test/av/stereo3d.h: 191
class struct_AVStereo3D(Structure):
    pass

struct_AVStereo3D.__slots__ = [
    'type',
    'flags',
    'view',
]
struct_AVStereo3D._fields_ = [
    ('type', enum_AVStereo3DType),
    ('flags', c_int),
    ('view', enum_AVStereo3DView),
]

AVStereo3D = struct_AVStereo3D# /home/josiah/ctypesgen_test/av/stereo3d.h: 191

# /home/josiah/ctypesgen_test/av/stereo3d.h: 199
if _libs["avcodec"].has("av_stereo3d_alloc", "cdecl"):
    av_stereo3d_alloc = _libs["avcodec"].get("av_stereo3d_alloc", "cdecl")
    av_stereo3d_alloc.argtypes = []
    av_stereo3d_alloc.restype = POINTER(AVStereo3D)

# /home/josiah/ctypesgen_test/av/stereo3d.h: 208
if _libs["avcodec"].has("av_stereo3d_create_side_data", "cdecl"):
    av_stereo3d_create_side_data = _libs["avcodec"].get("av_stereo3d_create_side_data", "cdecl")
    av_stereo3d_create_side_data.argtypes = [POINTER(AVFrame)]
    av_stereo3d_create_side_data.restype = POINTER(AVStereo3D)

# /home/josiah/ctypesgen_test/av/stereo3d.h: 217
if _libs["avcodec"].has("av_stereo3d_type_name", "cdecl"):
    av_stereo3d_type_name = _libs["avcodec"].get("av_stereo3d_type_name", "cdecl")
    av_stereo3d_type_name.argtypes = [c_uint]
    av_stereo3d_type_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/stereo3d.h: 226
if _libs["avcodec"].has("av_stereo3d_from_name", "cdecl"):
    av_stereo3d_from_name = _libs["avcodec"].get("av_stereo3d_from_name", "cdecl")
    av_stereo3d_from_name.argtypes = [String]
    av_stereo3d_from_name.restype = c_int

enum_SwrDitherType = c_int# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NONE = 0# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_RECTANGULAR = (SWR_DITHER_NONE + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_TRIANGULAR = (SWR_DITHER_RECTANGULAR + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_TRIANGULAR_HIGHPASS = (SWR_DITHER_TRIANGULAR + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS = 64# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_LIPSHITZ = (SWR_DITHER_NS + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_F_WEIGHTED = (SWR_DITHER_NS_LIPSHITZ + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_MODIFIED_E_WEIGHTED = (SWR_DITHER_NS_F_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_IMPROVED_E_WEIGHTED = (SWR_DITHER_NS_MODIFIED_E_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_SHIBATA = (SWR_DITHER_NS_IMPROVED_E_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_LOW_SHIBATA = (SWR_DITHER_NS_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NS_HIGH_SHIBATA = (SWR_DITHER_NS_LOW_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

SWR_DITHER_NB = (SWR_DITHER_NS_HIGH_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 141

enum_SwrEngine = c_int# /home/josiah/ctypesgen_test/av/swresample.h: 159

SWR_ENGINE_SWR = 0# /home/josiah/ctypesgen_test/av/swresample.h: 159

SWR_ENGINE_SOXR = (SWR_ENGINE_SWR + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 159

SWR_ENGINE_NB = (SWR_ENGINE_SOXR + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 159

enum_SwrFilterType = c_int# /home/josiah/ctypesgen_test/av/swresample.h: 166

SWR_FILTER_TYPE_CUBIC = 0# /home/josiah/ctypesgen_test/av/swresample.h: 166

SWR_FILTER_TYPE_BLACKMAN_NUTTALL = (SWR_FILTER_TYPE_CUBIC + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 166

SWR_FILTER_TYPE_KAISER = (SWR_FILTER_TYPE_BLACKMAN_NUTTALL + 1)# /home/josiah/ctypesgen_test/av/swresample.h: 166

# /home/josiah/ctypesgen_test/av/swresample.h: 182
class struct_SwrContext(Structure):
    pass

SwrContext = struct_SwrContext# /home/josiah/ctypesgen_test/av/swresample.h: 182

# /home/josiah/ctypesgen_test/av/swresample.h: 191
if _libs["avcodec"].has("swr_get_class", "cdecl"):
    swr_get_class = _libs["avcodec"].get("swr_get_class", "cdecl")
    swr_get_class.argtypes = []
    swr_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/swresample.h: 207
if _libs["avcodec"].has("swr_alloc", "cdecl"):
    swr_alloc = _libs["avcodec"].get("swr_alloc", "cdecl")
    swr_alloc.argtypes = []
    swr_alloc.restype = POINTER(struct_SwrContext)

# /home/josiah/ctypesgen_test/av/swresample.h: 219
if _libs["avcodec"].has("swr_init", "cdecl"):
    swr_init = _libs["avcodec"].get("swr_init", "cdecl")
    swr_init.argtypes = [POINTER(struct_SwrContext)]
    swr_init.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 228
if _libs["avcodec"].has("swr_is_initialized", "cdecl"):
    swr_is_initialized = _libs["avcodec"].get("swr_is_initialized", "cdecl")
    swr_is_initialized.argtypes = [POINTER(struct_SwrContext)]
    swr_is_initialized.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 250
if _libs["avcodec"].has("swr_alloc_set_opts", "cdecl"):
    swr_alloc_set_opts = _libs["avcodec"].get("swr_alloc_set_opts", "cdecl")
    swr_alloc_set_opts.argtypes = [POINTER(struct_SwrContext), c_int64, enum_AVSampleFormat, c_int, c_int64, enum_AVSampleFormat, c_int, c_int, POINTER(None)]
    swr_alloc_set_opts.restype = POINTER(struct_SwrContext)

# /home/josiah/ctypesgen_test/av/swresample.h: 267
if _libs["avcodec"].has("swr_free", "cdecl"):
    swr_free = _libs["avcodec"].get("swr_free", "cdecl")
    swr_free.argtypes = [POINTER(POINTER(struct_SwrContext))]
    swr_free.restype = None

# /home/josiah/ctypesgen_test/av/swresample.h: 279
if _libs["avcodec"].has("swr_close", "cdecl"):
    swr_close = _libs["avcodec"].get("swr_close", "cdecl")
    swr_close.argtypes = [POINTER(struct_SwrContext)]
    swr_close.restype = None

# /home/josiah/ctypesgen_test/av/swresample.h: 306
if _libs["avcodec"].has("swr_convert", "cdecl"):
    swr_convert = _libs["avcodec"].get("swr_convert", "cdecl")
    swr_convert.argtypes = [POINTER(struct_SwrContext), POINTER(POINTER(c_uint8)), c_int, POINTER(POINTER(c_uint8)), c_int]
    swr_convert.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 326
if _libs["avcodec"].has("swr_next_pts", "cdecl"):
    swr_next_pts = _libs["avcodec"].get("swr_next_pts", "cdecl")
    swr_next_pts.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_next_pts.restype = c_int64

# /home/josiah/ctypesgen_test/av/swresample.h: 353
if _libs["avcodec"].has("swr_set_compensation", "cdecl"):
    swr_set_compensation = _libs["avcodec"].get("swr_set_compensation", "cdecl")
    swr_set_compensation.argtypes = [POINTER(struct_SwrContext), c_int, c_int]
    swr_set_compensation.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 363
if _libs["avcodec"].has("swr_set_channel_mapping", "cdecl"):
    swr_set_channel_mapping = _libs["avcodec"].get("swr_set_channel_mapping", "cdecl")
    swr_set_channel_mapping.argtypes = [POINTER(struct_SwrContext), POINTER(c_int)]
    swr_set_channel_mapping.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 388
if _libs["avcodec"].has("swr_build_matrix", "cdecl"):
    swr_build_matrix = _libs["avcodec"].get("swr_build_matrix", "cdecl")
    swr_build_matrix.argtypes = [c_uint64, c_uint64, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), c_int, enum_AVMatrixEncoding, POINTER(None)]
    swr_build_matrix.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 404
if _libs["avcodec"].has("swr_set_matrix", "cdecl"):
    swr_set_matrix = _libs["avcodec"].get("swr_set_matrix", "cdecl")
    swr_set_matrix.argtypes = [POINTER(struct_SwrContext), POINTER(c_double), c_int]
    swr_set_matrix.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 424
if _libs["avcodec"].has("swr_drop_output", "cdecl"):
    swr_drop_output = _libs["avcodec"].get("swr_drop_output", "cdecl")
    swr_drop_output.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_drop_output.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 437
if _libs["avcodec"].has("swr_inject_silence", "cdecl"):
    swr_inject_silence = _libs["avcodec"].get("swr_inject_silence", "cdecl")
    swr_inject_silence.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_inject_silence.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 463
if _libs["avcodec"].has("swr_get_delay", "cdecl"):
    swr_get_delay = _libs["avcodec"].get("swr_get_delay", "cdecl")
    swr_get_delay.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_get_delay.restype = c_int64

# /home/josiah/ctypesgen_test/av/swresample.h: 481
if _libs["avcodec"].has("swr_get_out_samples", "cdecl"):
    swr_get_out_samples = _libs["avcodec"].get("swr_get_out_samples", "cdecl")
    swr_get_out_samples.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_get_out_samples.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 498
if _libs["avcodec"].has("swresample_version", "cdecl"):
    swresample_version = _libs["avcodec"].get("swresample_version", "cdecl")
    swresample_version.argtypes = []
    swresample_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/swresample.h: 505
if _libs["avcodec"].has("swresample_configuration", "cdecl"):
    swresample_configuration = _libs["avcodec"].get("swresample_configuration", "cdecl")
    swresample_configuration.argtypes = []
    swresample_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/swresample.h: 512
if _libs["avcodec"].has("swresample_license", "cdecl"):
    swresample_license = _libs["avcodec"].get("swresample_license", "cdecl")
    swresample_license.argtypes = []
    swresample_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/swresample.h: 555
if _libs["avcodec"].has("swr_convert_frame", "cdecl"):
    swr_convert_frame = _libs["avcodec"].get("swr_convert_frame", "cdecl")
    swr_convert_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_convert_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/swresample.h: 572
if _libs["avcodec"].has("swr_config_frame", "cdecl"):
    swr_config_frame = _libs["avcodec"].get("swr_config_frame", "cdecl")
    swr_config_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_config_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 45
if _libs["avdevice"].has("swscale_version", "cdecl"):
    swscale_version = _libs["avdevice"].get("swscale_version", "cdecl")
    swscale_version.argtypes = []
    swscale_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/swscale.h: 50
if _libs["avdevice"].has("swscale_configuration", "cdecl"):
    swscale_configuration = _libs["avdevice"].get("swscale_configuration", "cdecl")
    swscale_configuration.argtypes = []
    swscale_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/swscale.h: 55
if _libs["avdevice"].has("swscale_license", "cdecl"):
    swscale_license = _libs["avdevice"].get("swscale_license", "cdecl")
    swscale_license.argtypes = []
    swscale_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/swscale.h: 105
if _libs["avdevice"].has("sws_getCoefficients", "cdecl"):
    sws_getCoefficients = _libs["avdevice"].get("sws_getCoefficients", "cdecl")
    sws_getCoefficients.argtypes = [c_int]
    sws_getCoefficients.restype = POINTER(c_int)

# /home/josiah/ctypesgen_test/av/swscale.h: 112
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

SwsVector = struct_SwsVector# /home/josiah/ctypesgen_test/av/swscale.h: 112

# /home/josiah/ctypesgen_test/av/swscale.h: 120
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

SwsFilter = struct_SwsFilter# /home/josiah/ctypesgen_test/av/swscale.h: 120

# /home/josiah/ctypesgen_test/av/swscale.h: 122
class struct_SwsContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 128
if _libs["avdevice"].has("sws_isSupportedInput", "cdecl"):
    sws_isSupportedInput = _libs["avdevice"].get("sws_isSupportedInput", "cdecl")
    sws_isSupportedInput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedInput.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 134
if _libs["avdevice"].has("sws_isSupportedOutput", "cdecl"):
    sws_isSupportedOutput = _libs["avdevice"].get("sws_isSupportedOutput", "cdecl")
    sws_isSupportedOutput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedOutput.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 141
if _libs["avdevice"].has("sws_isSupportedEndiannessConversion", "cdecl"):
    sws_isSupportedEndiannessConversion = _libs["avdevice"].get("sws_isSupportedEndiannessConversion", "cdecl")
    sws_isSupportedEndiannessConversion.argtypes = [enum_AVPixelFormat]
    sws_isSupportedEndiannessConversion.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 148
if _libs["avdevice"].has("sws_alloc_context", "cdecl"):
    sws_alloc_context = _libs["avdevice"].get("sws_alloc_context", "cdecl")
    sws_alloc_context.argtypes = []
    sws_alloc_context.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/swscale.h: 157
if _libs["avdevice"].has("sws_init_context", "cdecl"):
    sws_init_context = _libs["avdevice"].get("sws_init_context", "cdecl")
    sws_init_context.argtypes = [POINTER(struct_SwsContext), POINTER(SwsFilter), POINTER(SwsFilter)]
    sws_init_context.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 163
if _libs["avdevice"].has("sws_freeContext", "cdecl"):
    sws_freeContext = _libs["avdevice"].get("sws_freeContext", "cdecl")
    sws_freeContext.argtypes = [POINTER(struct_SwsContext)]
    sws_freeContext.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 186
if _libs["avdevice"].has("sws_getContext", "cdecl"):
    sws_getContext = _libs["avdevice"].get("sws_getContext", "cdecl")
    sws_getContext.argtypes = [c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getContext.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/swscale.h: 217
if _libs["avdevice"].has("sws_scale", "cdecl"):
    sws_scale = _libs["avdevice"].get("sws_scale", "cdecl")
    sws_scale.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(c_uint8)), POINTER(c_int), c_int, c_int, POINTER(POINTER(c_uint8)), POINTER(c_int)]
    sws_scale.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 231
if _libs["avdevice"].has("sws_setColorspaceDetails", "cdecl"):
    sws_setColorspaceDetails = _libs["avdevice"].get("sws_setColorspaceDetails", "cdecl")
    sws_setColorspaceDetails.argtypes = [POINTER(struct_SwsContext), c_int * int(4), c_int, c_int * int(4), c_int, c_int, c_int, c_int]
    sws_setColorspaceDetails.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 238
if _libs["avdevice"].has("sws_getColorspaceDetails", "cdecl"):
    sws_getColorspaceDetails = _libs["avdevice"].get("sws_getColorspaceDetails", "cdecl")
    sws_getColorspaceDetails.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    sws_getColorspaceDetails.restype = c_int

# /home/josiah/ctypesgen_test/av/swscale.h: 245
if _libs["avdevice"].has("sws_allocVec", "cdecl"):
    sws_allocVec = _libs["avdevice"].get("sws_allocVec", "cdecl")
    sws_allocVec.argtypes = [c_int]
    sws_allocVec.restype = POINTER(SwsVector)

# /home/josiah/ctypesgen_test/av/swscale.h: 251
if _libs["avdevice"].has("sws_getGaussianVec", "cdecl"):
    sws_getGaussianVec = _libs["avdevice"].get("sws_getGaussianVec", "cdecl")
    sws_getGaussianVec.argtypes = [c_double, c_double]
    sws_getGaussianVec.restype = POINTER(SwsVector)

# /home/josiah/ctypesgen_test/av/swscale.h: 256
if _libs["avdevice"].has("sws_scaleVec", "cdecl"):
    sws_scaleVec = _libs["avdevice"].get("sws_scaleVec", "cdecl")
    sws_scaleVec.argtypes = [POINTER(SwsVector), c_double]
    sws_scaleVec.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 261
if _libs["avdevice"].has("sws_normalizeVec", "cdecl"):
    sws_normalizeVec = _libs["avdevice"].get("sws_normalizeVec", "cdecl")
    sws_normalizeVec.argtypes = [POINTER(SwsVector), c_double]
    sws_normalizeVec.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 274
if _libs["avdevice"].has("sws_freeVec", "cdecl"):
    sws_freeVec = _libs["avdevice"].get("sws_freeVec", "cdecl")
    sws_freeVec.argtypes = [POINTER(SwsVector)]
    sws_freeVec.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 276
if _libs["avdevice"].has("sws_getDefaultFilter", "cdecl"):
    sws_getDefaultFilter = _libs["avdevice"].get("sws_getDefaultFilter", "cdecl")
    sws_getDefaultFilter.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_int]
    sws_getDefaultFilter.restype = POINTER(SwsFilter)

# /home/josiah/ctypesgen_test/av/swscale.h: 280
if _libs["avdevice"].has("sws_freeFilter", "cdecl"):
    sws_freeFilter = _libs["avdevice"].get("sws_freeFilter", "cdecl")
    sws_freeFilter.argtypes = [POINTER(SwsFilter)]
    sws_freeFilter.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 294
if _libs["avdevice"].has("sws_getCachedContext", "cdecl"):
    sws_getCachedContext = _libs["avdevice"].get("sws_getCachedContext", "cdecl")
    sws_getCachedContext.argtypes = [POINTER(struct_SwsContext), c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getCachedContext.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/swscale.h: 310
if _libs["avdevice"].has("sws_convertPalette8ToPacked32", "cdecl"):
    sws_convertPalette8ToPacked32 = _libs["avdevice"].get("sws_convertPalette8ToPacked32", "cdecl")
    sws_convertPalette8ToPacked32.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8)]
    sws_convertPalette8ToPacked32.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 322
if _libs["avdevice"].has("sws_convertPalette8ToPacked24", "cdecl"):
    sws_convertPalette8ToPacked24 = _libs["avdevice"].get("sws_convertPalette8ToPacked24", "cdecl")
    sws_convertPalette8ToPacked24.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8)]
    sws_convertPalette8ToPacked24.restype = None

# /home/josiah/ctypesgen_test/av/swscale.h: 330
if _libs["avdevice"].has("sws_get_class", "cdecl"):
    sws_get_class = _libs["avdevice"].get("sws_get_class", "cdecl")
    sws_get_class.argtypes = []
    sws_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/tea.h: 35
try:
    av_tea_size = (c_int).in_dll(_libs["avcodec"], "av_tea_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/tea.h: 37
class struct_AVTEA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/tea.h: 43
if _libs["avcodec"].has("av_tea_alloc", "cdecl"):
    av_tea_alloc = _libs["avcodec"].get("av_tea_alloc", "cdecl")
    av_tea_alloc.argtypes = []
    av_tea_alloc.restype = POINTER(struct_AVTEA)

# /home/josiah/ctypesgen_test/av/tea.h: 52
if _libs["avcodec"].has("av_tea_init", "cdecl"):
    av_tea_init = _libs["avcodec"].get("av_tea_init", "cdecl")
    av_tea_init.argtypes = [POINTER(struct_AVTEA), c_uint8 * int(16), c_int]
    av_tea_init.restype = None

# /home/josiah/ctypesgen_test/av/tea.h: 64
if _libs["avcodec"].has("av_tea_crypt", "cdecl"):
    av_tea_crypt = _libs["avcodec"].get("av_tea_crypt", "cdecl")
    av_tea_crypt.argtypes = [POINTER(struct_AVTEA), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_tea_crypt.restype = None

# /home/josiah/ctypesgen_test/av/threadmessage.h: 22
class struct_AVThreadMessageQueue(Structure):
    pass

AVThreadMessageQueue = struct_AVThreadMessageQueue# /home/josiah/ctypesgen_test/av/threadmessage.h: 22

enum_AVThreadMessageFlags = c_int# /home/josiah/ctypesgen_test/av/threadmessage.h: 33

AV_THREAD_MESSAGE_NONBLOCK = 1# /home/josiah/ctypesgen_test/av/threadmessage.h: 33

AVThreadMessageFlags = enum_AVThreadMessageFlags# /home/josiah/ctypesgen_test/av/threadmessage.h: 33

# /home/josiah/ctypesgen_test/av/threadmessage.h: 44
if _libs["avcodec"].has("av_thread_message_queue_alloc", "cdecl"):
    av_thread_message_queue_alloc = _libs["avcodec"].get("av_thread_message_queue_alloc", "cdecl")
    av_thread_message_queue_alloc.argtypes = [POINTER(POINTER(AVThreadMessageQueue)), c_uint, c_uint]
    av_thread_message_queue_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/threadmessage.h: 53
if _libs["avcodec"].has("av_thread_message_queue_free", "cdecl"):
    av_thread_message_queue_free = _libs["avcodec"].get("av_thread_message_queue_free", "cdecl")
    av_thread_message_queue_free.argtypes = [POINTER(POINTER(AVThreadMessageQueue))]
    av_thread_message_queue_free.restype = None

# /home/josiah/ctypesgen_test/av/threadmessage.h: 58
if _libs["avcodec"].has("av_thread_message_queue_send", "cdecl"):
    av_thread_message_queue_send = _libs["avcodec"].get("av_thread_message_queue_send", "cdecl")
    av_thread_message_queue_send.argtypes = [POINTER(AVThreadMessageQueue), POINTER(None), c_uint]
    av_thread_message_queue_send.restype = c_int

# /home/josiah/ctypesgen_test/av/threadmessage.h: 65
if _libs["avcodec"].has("av_thread_message_queue_recv", "cdecl"):
    av_thread_message_queue_recv = _libs["avcodec"].get("av_thread_message_queue_recv", "cdecl")
    av_thread_message_queue_recv.argtypes = [POINTER(AVThreadMessageQueue), POINTER(None), c_uint]
    av_thread_message_queue_recv.restype = c_int

# /home/josiah/ctypesgen_test/av/threadmessage.h: 77
if _libs["avcodec"].has("av_thread_message_queue_set_err_send", "cdecl"):
    av_thread_message_queue_set_err_send = _libs["avcodec"].get("av_thread_message_queue_set_err_send", "cdecl")
    av_thread_message_queue_set_err_send.argtypes = [POINTER(AVThreadMessageQueue), c_int]
    av_thread_message_queue_set_err_send.restype = None

# /home/josiah/ctypesgen_test/av/threadmessage.h: 88
if _libs["avcodec"].has("av_thread_message_queue_set_err_recv", "cdecl"):
    av_thread_message_queue_set_err_recv = _libs["avcodec"].get("av_thread_message_queue_set_err_recv", "cdecl")
    av_thread_message_queue_set_err_recv.argtypes = [POINTER(AVThreadMessageQueue), c_int]
    av_thread_message_queue_set_err_recv.restype = None

# /home/josiah/ctypesgen_test/av/threadmessage.h: 95
if _libs["avcodec"].has("av_thread_message_queue_set_free_func", "cdecl"):
    av_thread_message_queue_set_free_func = _libs["avcodec"].get("av_thread_message_queue_set_free_func", "cdecl")
    av_thread_message_queue_set_free_func.argtypes = [POINTER(AVThreadMessageQueue), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    av_thread_message_queue_set_free_func.restype = None

# /home/josiah/ctypesgen_test/av/threadmessage.h: 104
if _libs["avcodec"].has("av_thread_message_queue_nb_elems", "cdecl"):
    av_thread_message_queue_nb_elems = _libs["avcodec"].get("av_thread_message_queue_nb_elems", "cdecl")
    av_thread_message_queue_nb_elems.argtypes = [POINTER(AVThreadMessageQueue)]
    av_thread_message_queue_nb_elems.restype = c_int

# /home/josiah/ctypesgen_test/av/threadmessage.h: 113
if _libs["avcodec"].has("av_thread_message_flush", "cdecl"):
    av_thread_message_flush = _libs["avcodec"].get("av_thread_message_flush", "cdecl")
    av_thread_message_flush.argtypes = [POINTER(AVThreadMessageQueue)]
    av_thread_message_flush.restype = None

enum_AVTimecodeFlag = c_int# /home/josiah/ctypesgen_test/av/timecode.h: 35

AV_TIMECODE_FLAG_DROPFRAME = (1 << 0)# /home/josiah/ctypesgen_test/av/timecode.h: 35

AV_TIMECODE_FLAG_24HOURSMAX = (1 << 1)# /home/josiah/ctypesgen_test/av/timecode.h: 35

AV_TIMECODE_FLAG_ALLOWNEGATIVE = (1 << 2)# /home/josiah/ctypesgen_test/av/timecode.h: 35

# /home/josiah/ctypesgen_test/av/timecode.h: 46
class struct_anon_641(Structure):
    pass

struct_anon_641.__slots__ = [
    'start',
    'flags',
    'rate',
    'fps',
]
struct_anon_641._fields_ = [
    ('start', c_int),
    ('flags', c_uint32),
    ('rate', AVRational),
    ('fps', c_uint),
]

AVTimecode = struct_anon_641# /home/josiah/ctypesgen_test/av/timecode.h: 46

# /home/josiah/ctypesgen_test/av/timecode.h: 56
if _libs["avcodec"].has("av_timecode_adjust_ntsc_framenum2", "cdecl"):
    av_timecode_adjust_ntsc_framenum2 = _libs["avcodec"].get("av_timecode_adjust_ntsc_framenum2", "cdecl")
    av_timecode_adjust_ntsc_framenum2.argtypes = [c_int, c_int]
    av_timecode_adjust_ntsc_framenum2.restype = c_int

# /home/josiah/ctypesgen_test/av/timecode.h: 83
if _libs["avcodec"].has("av_timecode_get_smpte_from_framenum", "cdecl"):
    av_timecode_get_smpte_from_framenum = _libs["avcodec"].get("av_timecode_get_smpte_from_framenum", "cdecl")
    av_timecode_get_smpte_from_framenum.argtypes = [POINTER(AVTimecode), c_int]
    av_timecode_get_smpte_from_framenum.restype = c_uint32

# /home/josiah/ctypesgen_test/av/timecode.h: 96
if _libs["avcodec"].has("av_timecode_get_smpte", "cdecl"):
    av_timecode_get_smpte = _libs["avcodec"].get("av_timecode_get_smpte", "cdecl")
    av_timecode_get_smpte.argtypes = [AVRational, c_int, c_int, c_int, c_int, c_int]
    av_timecode_get_smpte.restype = c_uint32

# /home/josiah/ctypesgen_test/av/timecode.h: 110
if _libs["avcodec"].has("av_timecode_make_string", "cdecl"):
    av_timecode_make_string = _libs["avcodec"].get("av_timecode_make_string", "cdecl")
    av_timecode_make_string.argtypes = [POINTER(AVTimecode), String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_string.restype = ReturnString
    else:
        av_timecode_make_string.restype = String
        av_timecode_make_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/timecode.h: 127
if _libs["avcodec"].has("av_timecode_make_smpte_tc_string2", "cdecl"):
    av_timecode_make_smpte_tc_string2 = _libs["avcodec"].get("av_timecode_make_smpte_tc_string2", "cdecl")
    av_timecode_make_smpte_tc_string2.argtypes = [String, AVRational, c_uint32, c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_smpte_tc_string2.restype = ReturnString
    else:
        av_timecode_make_smpte_tc_string2.restype = String
        av_timecode_make_smpte_tc_string2.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/timecode.h: 138
if _libs["avcodec"].has("av_timecode_make_smpte_tc_string", "cdecl"):
    av_timecode_make_smpte_tc_string = _libs["avcodec"].get("av_timecode_make_smpte_tc_string", "cdecl")
    av_timecode_make_smpte_tc_string.argtypes = [String, c_uint32, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_smpte_tc_string.restype = ReturnString
    else:
        av_timecode_make_smpte_tc_string.restype = String
        av_timecode_make_smpte_tc_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/timecode.h: 147
if _libs["avcodec"].has("av_timecode_make_mpeg_tc_string", "cdecl"):
    av_timecode_make_mpeg_tc_string = _libs["avcodec"].get("av_timecode_make_mpeg_tc_string", "cdecl")
    av_timecode_make_mpeg_tc_string.argtypes = [String, c_uint32]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_mpeg_tc_string.restype = ReturnString
    else:
        av_timecode_make_mpeg_tc_string.restype = String
        av_timecode_make_mpeg_tc_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/timecode.h: 161
if _libs["avcodec"].has("av_timecode_init", "cdecl"):
    av_timecode_init = _libs["avcodec"].get("av_timecode_init", "cdecl")
    av_timecode_init.argtypes = [POINTER(AVTimecode), AVRational, c_int, c_int, POINTER(None)]
    av_timecode_init.restype = c_int

# /home/josiah/ctypesgen_test/av/timecode.h: 178
if _libs["avcodec"].has("av_timecode_init_from_components", "cdecl"):
    av_timecode_init_from_components = _libs["avcodec"].get("av_timecode_init_from_components", "cdecl")
    av_timecode_init_from_components.argtypes = [POINTER(AVTimecode), AVRational, c_int, c_int, c_int, c_int, c_int, POINTER(None)]
    av_timecode_init_from_components.restype = c_int

# /home/josiah/ctypesgen_test/av/timecode.h: 190
if _libs["avcodec"].has("av_timecode_init_from_string", "cdecl"):
    av_timecode_init_from_string = _libs["avcodec"].get("av_timecode_init_from_string", "cdecl")
    av_timecode_init_from_string.argtypes = [POINTER(AVTimecode), AVRational, String, POINTER(None)]
    av_timecode_init_from_string.restype = c_int

# /home/josiah/ctypesgen_test/av/timecode.h: 197
if _libs["avcodec"].has("av_timecode_check_frame_rate", "cdecl"):
    av_timecode_check_frame_rate = _libs["avcodec"].get("av_timecode_check_frame_rate", "cdecl")
    av_timecode_check_frame_rate.argtypes = [AVRational]
    av_timecode_check_frame_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/time.h: 29
if _libs["avcodec"].has("av_gettime", "cdecl"):
    av_gettime = _libs["avcodec"].get("av_gettime", "cdecl")
    av_gettime.argtypes = []
    av_gettime.restype = c_int64

# /home/josiah/ctypesgen_test/av/time.h: 38
if _libs["avcodec"].has("av_gettime_relative", "cdecl"):
    av_gettime_relative = _libs["avcodec"].get("av_gettime_relative", "cdecl")
    av_gettime_relative.argtypes = []
    av_gettime_relative.restype = c_int64

# /home/josiah/ctypesgen_test/av/time.h: 44
if _libs["avcodec"].has("av_gettime_relative_is_monotonic", "cdecl"):
    av_gettime_relative_is_monotonic = _libs["avcodec"].get("av_gettime_relative_is_monotonic", "cdecl")
    av_gettime_relative_is_monotonic.argtypes = []
    av_gettime_relative_is_monotonic.restype = c_int

# /home/josiah/ctypesgen_test/av/time.h: 54
if _libs["avcodec"].has("av_usleep", "cdecl"):
    av_usleep = _libs["avcodec"].get("av_usleep", "cdecl")
    av_usleep.argtypes = [c_uint]
    av_usleep.restype = c_int

# /home/josiah/ctypesgen_test/av/tree.h: 45
class struct_AVTreeNode(Structure):
    pass

# /home/josiah/ctypesgen_test/av/tree.h: 46
try:
    av_tree_node_size = (c_int).in_dll(_libs["avcodec"], "av_tree_node_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/tree.h: 51
if _libs["avcodec"].has("av_tree_node_alloc", "cdecl"):
    av_tree_node_alloc = _libs["avcodec"].get("av_tree_node_alloc", "cdecl")
    av_tree_node_alloc.argtypes = []
    av_tree_node_alloc.restype = POINTER(struct_AVTreeNode)

# /home/josiah/ctypesgen_test/av/tree.h: 67
if _libs["avcodec"].has("av_tree_find", "cdecl"):
    av_tree_find = _libs["avcodec"].get("av_tree_find", "cdecl")
    av_tree_find.argtypes = [POINTER(struct_AVTreeNode), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), POINTER(None) * int(2)]
    av_tree_find.restype = POINTER(c_ubyte)
    av_tree_find.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/tree.h: 114
if _libs["avcodec"].has("av_tree_insert", "cdecl"):
    av_tree_insert = _libs["avcodec"].get("av_tree_insert", "cdecl")
    av_tree_insert.argtypes = [POINTER(POINTER(struct_AVTreeNode)), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), POINTER(POINTER(struct_AVTreeNode))]
    av_tree_insert.restype = POINTER(c_ubyte)
    av_tree_insert.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/tree.h: 118
if _libs["avcodec"].has("av_tree_destroy", "cdecl"):
    av_tree_destroy = _libs["avcodec"].get("av_tree_destroy", "cdecl")
    av_tree_destroy.argtypes = [POINTER(struct_AVTreeNode)]
    av_tree_destroy.restype = None

# /home/josiah/ctypesgen_test/av/tree.h: 130
if _libs["avcodec"].has("av_tree_enumerate", "cdecl"):
    av_tree_enumerate = _libs["avcodec"].get("av_tree_enumerate", "cdecl")
    av_tree_enumerate.argtypes = [POINTER(struct_AVTreeNode), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    av_tree_enumerate.restype = None

# /home/josiah/ctypesgen_test/av/twofish.h: 36
try:
    av_twofish_size = (c_int).in_dll(_libs["avcodec"], "av_twofish_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/twofish.h: 38
class struct_AVTWOFISH(Structure):
    pass

# /home/josiah/ctypesgen_test/av/twofish.h: 44
if _libs["avcodec"].has("av_twofish_alloc", "cdecl"):
    av_twofish_alloc = _libs["avcodec"].get("av_twofish_alloc", "cdecl")
    av_twofish_alloc.argtypes = []
    av_twofish_alloc.restype = POINTER(struct_AVTWOFISH)

# /home/josiah/ctypesgen_test/av/twofish.h: 53
if _libs["avcodec"].has("av_twofish_init", "cdecl"):
    av_twofish_init = _libs["avcodec"].get("av_twofish_init", "cdecl")
    av_twofish_init.argtypes = [POINTER(struct_AVTWOFISH), POINTER(c_uint8), c_int]
    av_twofish_init.restype = c_int

# /home/josiah/ctypesgen_test/av/twofish.h: 65
if _libs["avcodec"].has("av_twofish_crypt", "cdecl"):
    av_twofish_crypt = _libs["avcodec"].get("av_twofish_crypt", "cdecl")
    av_twofish_crypt.argtypes = [POINTER(struct_AVTWOFISH), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_twofish_crypt.restype = None

# /home/josiah/ctypesgen_test/av/tx.h: 25
class struct_AVTXContext(Structure):
    pass

AVTXContext = struct_AVTXContext# /home/josiah/ctypesgen_test/av/tx.h: 25

# /home/josiah/ctypesgen_test/av/tx.h: 29
class struct_AVComplexFloat(Structure):
    pass

struct_AVComplexFloat.__slots__ = [
    're',
    'im',
]
struct_AVComplexFloat._fields_ = [
    ('re', c_float),
    ('im', c_float),
]

AVComplexFloat = struct_AVComplexFloat# /home/josiah/ctypesgen_test/av/tx.h: 29

# /home/josiah/ctypesgen_test/av/tx.h: 33
class struct_AVComplexDouble(Structure):
    pass

struct_AVComplexDouble.__slots__ = [
    're',
    'im',
]
struct_AVComplexDouble._fields_ = [
    ('re', c_double),
    ('im', c_double),
]

AVComplexDouble = struct_AVComplexDouble# /home/josiah/ctypesgen_test/av/tx.h: 33

# /home/josiah/ctypesgen_test/av/tx.h: 37
class struct_AVComplexInt32(Structure):
    pass

struct_AVComplexInt32.__slots__ = [
    're',
    'im',
]
struct_AVComplexInt32._fields_ = [
    ('re', c_int32),
    ('im', c_int32),
]

AVComplexInt32 = struct_AVComplexInt32# /home/josiah/ctypesgen_test/av/tx.h: 37

enum_AVTXType = c_int# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_FLOAT_FFT = 0# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_FLOAT_MDCT = 1# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_DOUBLE_FFT = 2# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_DOUBLE_MDCT = 3# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_INT32_FFT = 4# /home/josiah/ctypesgen_test/av/tx.h: 39

AV_TX_INT32_MDCT = 5# /home/josiah/ctypesgen_test/av/tx.h: 39

av_tx_fn = CFUNCTYPE(UNCHECKED(None), POINTER(AVTXContext), POINTER(None), POINTER(None), c_ptrdiff_t)# /home/josiah/ctypesgen_test/av/tx.h: 99

enum_AVTXFlags = c_int# /home/josiah/ctypesgen_test/av/tx.h: 104

AV_TX_INPLACE = (1 << 0)# /home/josiah/ctypesgen_test/av/tx.h: 104

# /home/josiah/ctypesgen_test/av/tx.h: 127
if _libs["avcodec"].has("av_tx_init", "cdecl"):
    av_tx_init = _libs["avcodec"].get("av_tx_init", "cdecl")
    av_tx_init.argtypes = [POINTER(POINTER(AVTXContext)), POINTER(av_tx_fn), enum_AVTXType, c_int, c_int, POINTER(None), c_uint64]
    av_tx_init.restype = c_int

# /home/josiah/ctypesgen_test/av/tx.h: 133
if _libs["avcodec"].has("av_tx_uninit", "cdecl"):
    av_tx_uninit = _libs["avcodec"].get("av_tx_uninit", "cdecl")
    av_tx_uninit.argtypes = [POINTER(POINTER(AVTXContext))]
    av_tx_uninit.restype = None

# /home/josiah/ctypesgen_test/av/vaapi.h: 56
class struct_vaapi_context(Structure):
    pass

struct_vaapi_context.__slots__ = [
    'display',
    'config_id',
    'context_id',
]
struct_vaapi_context._fields_ = [
    ('display', POINTER(None)),
    ('config_id', c_uint32),
    ('context_id', c_uint32),
]

AVVDPAU_Render2 = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(struct_AVFrame), POINTER(VdpPictureInfo), c_uint32, POINTER(VdpBitstreamBuffer))# /home/josiah/ctypesgen_test/av/vdpau.h: 63

# /home/josiah/ctypesgen_test/av/vdpau.h: 97
class struct_AVVDPAUContext(Structure):
    pass

struct_AVVDPAUContext.__slots__ = [
    'decoder',
    'render',
    'render2',
]
struct_AVVDPAUContext._fields_ = [
    ('decoder', VdpDecoder),
    ('render', POINTER(VdpDecoderRender)),
    ('render2', AVVDPAU_Render2),
]

AVVDPAUContext = struct_AVVDPAUContext# /home/josiah/ctypesgen_test/av/vdpau.h: 97

# /home/josiah/ctypesgen_test/av/vdpau.h: 104
if _libs["avcodec"].has("av_alloc_vdpaucontext", "cdecl"):
    av_alloc_vdpaucontext = _libs["avcodec"].get("av_alloc_vdpaucontext", "cdecl")
    av_alloc_vdpaucontext.argtypes = []
    av_alloc_vdpaucontext.restype = POINTER(AVVDPAUContext)

# /home/josiah/ctypesgen_test/av/vdpau.h: 106
if _libs["avcodec"].has("av_vdpau_hwaccel_get_render2", "cdecl"):
    av_vdpau_hwaccel_get_render2 = _libs["avcodec"].get("av_vdpau_hwaccel_get_render2", "cdecl")
    av_vdpau_hwaccel_get_render2.argtypes = [POINTER(AVVDPAUContext)]
    av_vdpau_hwaccel_get_render2.restype = AVVDPAU_Render2

# /home/josiah/ctypesgen_test/av/vdpau.h: 107
if _libs["avcodec"].has("av_vdpau_hwaccel_set_render2", "cdecl"):
    av_vdpau_hwaccel_set_render2 = _libs["avcodec"].get("av_vdpau_hwaccel_set_render2", "cdecl")
    av_vdpau_hwaccel_set_render2.argtypes = [POINTER(AVVDPAUContext), AVVDPAU_Render2]
    av_vdpau_hwaccel_set_render2.restype = None

# /home/josiah/ctypesgen_test/av/vdpau.h: 126
if _libs["avcodec"].has("av_vdpau_bind_context", "cdecl"):
    av_vdpau_bind_context = _libs["avcodec"].get("av_vdpau_bind_context", "cdecl")
    av_vdpau_bind_context.argtypes = [POINTER(AVCodecContext), VdpDevice, POINTER(VdpGetProcAddress), c_uint]
    av_vdpau_bind_context.restype = c_int

# /home/josiah/ctypesgen_test/av/vdpau.h: 146
if _libs["avcodec"].has("av_vdpau_get_surface_parameters", "cdecl"):
    av_vdpau_get_surface_parameters = _libs["avcodec"].get("av_vdpau_get_surface_parameters", "cdecl")
    av_vdpau_get_surface_parameters.argtypes = [POINTER(AVCodecContext), POINTER(VdpChromaType), POINTER(c_uint32), POINTER(c_uint32)]
    av_vdpau_get_surface_parameters.restype = c_int

# /home/josiah/ctypesgen_test/av/vdpau.h: 154
if _libs["avcodec"].has("av_vdpau_alloc_context", "cdecl"):
    av_vdpau_alloc_context = _libs["avcodec"].get("av_vdpau_alloc_context", "cdecl")
    av_vdpau_alloc_context.argtypes = []
    av_vdpau_alloc_context.restype = POINTER(AVVDPAUContext)

# /home/josiah/ctypesgen_test/av/vdpau.h: 171
if _libs["avcodec"].has("av_vdpau_get_profile", "cdecl"):
    av_vdpau_get_profile = _libs["avcodec"].get("av_vdpau_get_profile", "cdecl")
    av_vdpau_get_profile.argtypes = [POINTER(AVCodecContext), POINTER(VdpDecoderProfile)]
    av_vdpau_get_profile.restype = c_int

enum_AVVideoEncParamsType = c_int# /home/josiah/ctypesgen_test/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_NONE = (-1)# /home/josiah/ctypesgen_test/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_VP9 = (AV_VIDEO_ENC_PARAMS_NONE + 1)# /home/josiah/ctypesgen_test/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_H264 = (AV_VIDEO_ENC_PARAMS_VP9 + 1)# /home/josiah/ctypesgen_test/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_MPEG2 = (AV_VIDEO_ENC_PARAMS_H264 + 1)# /home/josiah/ctypesgen_test/av/video_enc_params.h: 28

# /home/josiah/ctypesgen_test/av/video_enc_params.h: 110
class struct_AVVideoEncParams(Structure):
    pass

struct_AVVideoEncParams.__slots__ = [
    'nb_blocks',
    'blocks_offset',
    'block_size',
    'type',
    'qp',
    'delta_qp',
]
struct_AVVideoEncParams._fields_ = [
    ('nb_blocks', c_uint),
    ('blocks_offset', c_size_t),
    ('block_size', c_size_t),
    ('type', enum_AVVideoEncParamsType),
    ('qp', c_int32),
    ('delta_qp', (c_int32 * int(2)) * int(4)),
]

AVVideoEncParams = struct_AVVideoEncParams# /home/josiah/ctypesgen_test/av/video_enc_params.h: 110

# /home/josiah/ctypesgen_test/av/video_enc_params.h: 137
class struct_AVVideoBlockParams(Structure):
    pass

struct_AVVideoBlockParams.__slots__ = [
    'src_x',
    'src_y',
    'w',
    'h',
    'delta_qp',
]
struct_AVVideoBlockParams._fields_ = [
    ('src_x', c_int),
    ('src_y', c_int),
    ('w', c_int),
    ('h', c_int),
    ('delta_qp', c_int32),
]

AVVideoBlockParams = struct_AVVideoBlockParams# /home/josiah/ctypesgen_test/av/video_enc_params.h: 137

# /home/josiah/ctypesgen_test/av/video_enc_params.h: 158
if _libs["avcodec"].has("av_video_enc_params_alloc", "cdecl"):
    av_video_enc_params_alloc = _libs["avcodec"].get("av_video_enc_params_alloc", "cdecl")
    av_video_enc_params_alloc.argtypes = [enum_AVVideoEncParamsType, c_uint, POINTER(c_size_t)]
    av_video_enc_params_alloc.restype = POINTER(AVVideoEncParams)

# /home/josiah/ctypesgen_test/av/video_enc_params.h: 167
if _libs["avcodec"].has("av_video_enc_params_create_side_data", "cdecl"):
    av_video_enc_params_create_side_data = _libs["avcodec"].get("av_video_enc_params_create_side_data", "cdecl")
    av_video_enc_params_create_side_data.argtypes = [POINTER(AVFrame), enum_AVVideoEncParamsType, c_uint]
    av_video_enc_params_create_side_data.restype = POINTER(AVVideoEncParams)

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 31
class struct_AVVorbisParseContext(Structure):
    pass

AVVorbisParseContext = struct_AVVorbisParseContext# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 31

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 36
if _libs["avcodec"].has("av_vorbis_parse_init", "cdecl"):
    av_vorbis_parse_init = _libs["avcodec"].get("av_vorbis_parse_init", "cdecl")
    av_vorbis_parse_init.argtypes = [POINTER(c_uint8), c_int]
    av_vorbis_parse_init.restype = POINTER(AVVorbisParseContext)

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 42
if _libs["avcodec"].has("av_vorbis_parse_free", "cdecl"):
    av_vorbis_parse_free = _libs["avcodec"].get("av_vorbis_parse_free", "cdecl")
    av_vorbis_parse_free.argtypes = [POINTER(POINTER(AVVorbisParseContext))]
    av_vorbis_parse_free.restype = None

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 59
if _libs["avcodec"].has("av_vorbis_parse_frame_flags", "cdecl"):
    av_vorbis_parse_frame_flags = _libs["avcodec"].get("av_vorbis_parse_frame_flags", "cdecl")
    av_vorbis_parse_frame_flags.argtypes = [POINTER(AVVorbisParseContext), POINTER(c_uint8), c_int, POINTER(c_int)]
    av_vorbis_parse_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 69
if _libs["avcodec"].has("av_vorbis_parse_frame", "cdecl"):
    av_vorbis_parse_frame = _libs["avcodec"].get("av_vorbis_parse_frame", "cdecl")
    av_vorbis_parse_frame.argtypes = [POINTER(AVVorbisParseContext), POINTER(c_uint8), c_int]
    av_vorbis_parse_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 72
if _libs["avcodec"].has("av_vorbis_parse_reset", "cdecl"):
    av_vorbis_parse_reset = _libs["avcodec"].get("av_vorbis_parse_reset", "cdecl")
    av_vorbis_parse_reset.argtypes = [POINTER(AVVorbisParseContext)]
    av_vorbis_parse_reset.restype = None

# /home/josiah/ctypesgen_test/av/xtea.h: 37
class struct_AVXTEA(Structure):
    pass

struct_AVXTEA.__slots__ = [
    'key',
]
struct_AVXTEA._fields_ = [
    ('key', c_uint32 * int(16)),
]

AVXTEA = struct_AVXTEA# /home/josiah/ctypesgen_test/av/xtea.h: 37

# /home/josiah/ctypesgen_test/av/xtea.h: 42
if _libs["avcodec"].has("av_xtea_alloc", "cdecl"):
    av_xtea_alloc = _libs["avcodec"].get("av_xtea_alloc", "cdecl")
    av_xtea_alloc.argtypes = []
    av_xtea_alloc.restype = POINTER(AVXTEA)

# /home/josiah/ctypesgen_test/av/xtea.h: 51
if _libs["avcodec"].has("av_xtea_init", "cdecl"):
    av_xtea_init = _libs["avcodec"].get("av_xtea_init", "cdecl")
    av_xtea_init.argtypes = [POINTER(struct_AVXTEA), c_uint8 * int(16)]
    av_xtea_init.restype = None

# /home/josiah/ctypesgen_test/av/xtea.h: 60
if _libs["avcodec"].has("av_xtea_le_init", "cdecl"):
    av_xtea_le_init = _libs["avcodec"].get("av_xtea_le_init", "cdecl")
    av_xtea_le_init.argtypes = [POINTER(struct_AVXTEA), c_uint8 * int(16)]
    av_xtea_le_init.restype = None

# /home/josiah/ctypesgen_test/av/xtea.h: 73
if _libs["avcodec"].has("av_xtea_crypt", "cdecl"):
    av_xtea_crypt = _libs["avcodec"].get("av_xtea_crypt", "cdecl")
    av_xtea_crypt.argtypes = [POINTER(struct_AVXTEA), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_xtea_crypt.restype = None

# /home/josiah/ctypesgen_test/av/xtea.h: 87
if _libs["avcodec"].has("av_xtea_le_crypt", "cdecl"):
    av_xtea_le_crypt = _libs["avcodec"].get("av_xtea_le_crypt", "cdecl")
    av_xtea_le_crypt.argtypes = [POINTER(struct_AVXTEA), POINTER(c_uint8), POINTER(c_uint8), c_int, POINTER(c_uint8), c_int]
    av_xtea_le_crypt.restype = None

XID = c_ulong# /usr/include/X11/X.h: 66

# /usr/include/X11/extensions/XvMC.h: 96
class struct_anon_644(Structure):
    pass

struct_anon_644.__slots__ = [
    'surface_id',
    'context_id',
    'surface_type_id',
    'width',
    'height',
    'privData',
]
struct_anon_644._fields_ = [
    ('surface_id', XID),
    ('context_id', XID),
    ('surface_type_id', c_int),
    ('width', c_ushort),
    ('height', c_ushort),
    ('privData', POINTER(None)),
]

XvMCSurface = struct_anon_644# /usr/include/X11/extensions/XvMC.h: 96

# /usr/include/X11/extensions/XvMC.h: 128
class struct_anon_647(Structure):
    pass

struct_anon_647.__slots__ = [
    'x',
    'y',
    'macroblock_type',
    'motion_type',
    'motion_vertical_field_select',
    'dct_type',
    'PMV',
    'index',
    'coded_block_pattern',
    'pad0',
]
struct_anon_647._fields_ = [
    ('x', c_ushort),
    ('y', c_ushort),
    ('macroblock_type', c_ubyte),
    ('motion_type', c_ubyte),
    ('motion_vertical_field_select', c_ubyte),
    ('dct_type', c_ubyte),
    ('PMV', ((c_short * int(2)) * int(2)) * int(2)),
    ('index', c_uint),
    ('coded_block_pattern', c_ushort),
    ('pad0', c_ushort),
]

XvMCMacroBlock = struct_anon_647# /usr/include/X11/extensions/XvMC.h: 128

# /home/josiah/ctypesgen_test/av/xvmc.h: 46
class struct_xvmc_pix_fmt(Structure):
    pass

struct_xvmc_pix_fmt.__slots__ = [
    'xvmc_id',
    'data_blocks',
    'mv_blocks',
    'allocated_mv_blocks',
    'allocated_data_blocks',
    'idct',
    'unsigned_intra',
    'p_surface',
    'p_past_surface',
    'p_future_surface',
    'picture_structure',
    'flags',
    'start_mv_blocks_num',
    'filled_mv_blocks_num',
    'next_free_data_block_num',
]
struct_xvmc_pix_fmt._fields_ = [
    ('xvmc_id', c_int),
    ('data_blocks', POINTER(c_short)),
    ('mv_blocks', POINTER(XvMCMacroBlock)),
    ('allocated_mv_blocks', c_int),
    ('allocated_data_blocks', c_int),
    ('idct', c_int),
    ('unsigned_intra', c_int),
    ('p_surface', POINTER(XvMCSurface)),
    ('p_past_surface', POINTER(XvMCSurface)),
    ('p_future_surface', POINTER(XvMCSurface)),
    ('picture_structure', c_uint),
    ('flags', c_uint),
    ('start_mv_blocks_num', c_int),
    ('filled_mv_blocks_num', c_int),
    ('next_free_data_block_num', c_int),
]

# /home/josiah/ctypesgen_test/av/attributes.h: 33
def AV_GCC_VERSION_AT_LEAST(x, y):
    return 0

# /home/josiah/ctypesgen_test/av/attributes.h: 34
def AV_GCC_VERSION_AT_MOST(x, y):
    return 0

# /home/josiah/ctypesgen_test/av/attributes.h: 126
def AV_NOWARN_DEPRECATED(code):
    return code

# /home/josiah/ctypesgen_test/av/attributes.h: 156
def av_uninit(x):
    return x

# /home/josiah/ctypesgen_test/av/attributes.h: 163
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

# /home/josiah/ctypesgen_test/av/version.h: 30
try:
    LIBAVCODEC_VERSION_MAJOR = 58
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 31
try:
    LIBAVCODEC_VERSION_MINOR = 134
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 32
try:
    LIBAVCODEC_VERSION_MICRO = 100
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 34
try:
    LIBAVCODEC_VERSION_INT = (AV_VERSION_INT (LIBAVCODEC_VERSION_MAJOR, LIBAVCODEC_VERSION_MINOR, LIBAVCODEC_VERSION_MICRO))
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 40
try:
    LIBAVCODEC_BUILD = LIBAVCODEC_VERSION_INT
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 55
try:
    FF_API_AVCTX_TIMEBASE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 58
try:
    FF_API_CODED_FRAME = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 61
try:
    FF_API_SIDEDATA_ONLY_PKT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 64
try:
    FF_API_VDPAU_PROFILE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 67
try:
    FF_API_CONVERGENCE_DURATION = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 70
try:
    FF_API_AVPICTURE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 73
try:
    FF_API_AVPACKET_OLD_API = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 76
try:
    FF_API_RTP_CALLBACK = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 79
try:
    FF_API_VBV_DELAY = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 82
try:
    FF_API_CODER_TYPE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 85
try:
    FF_API_STAT_BITS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 88
try:
    FF_API_PRIVATE_OPT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 91
try:
    FF_API_ASS_TIMING = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 94
try:
    FF_API_OLD_BSF = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 97
try:
    FF_API_COPY_CONTEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 100
try:
    FF_API_GET_CONTEXT_DEFAULTS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 103
try:
    FF_API_NVENC_OLD_NAME = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 106
try:
    FF_API_STRUCT_VAAPI_CONTEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 109
try:
    FF_API_MERGE_SD_API = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 112
try:
    FF_API_TAG_STRING = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 115
try:
    FF_API_GETCHROMA = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 118
try:
    FF_API_CODEC_GET_SET = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 121
try:
    FF_API_USER_VISIBLE_AVHWACCEL = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 124
try:
    FF_API_LOCKMGR = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 127
try:
    FF_API_NEXT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 130
try:
    FF_API_UNSANITIZED_BITRATES = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 133
try:
    FF_API_OPENH264_SLICE_MODE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 136
try:
    FF_API_OPENH264_CABAC = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 139
try:
    FF_API_UNUSED_CODEC_CAPS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 142
try:
    FF_API_AVPRIV_PUT_BITS = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 145
try:
    FF_API_OLD_ENCDEC = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 148
try:
    FF_API_AVCODEC_PIX_FMT = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 151
try:
    FF_API_MPV_RC_STRATEGY = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 154
try:
    FF_API_PARSER_CHANGE = (LIBAVCODEC_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 157
try:
    FF_API_THREAD_SAFE_CALLBACKS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 160
try:
    FF_API_DEBUG_MV = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 163
try:
    FF_API_GET_FRAME_CLASS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 166
try:
    FF_API_AUTO_THREADS = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /home/josiah/ctypesgen_test/av/version.h: 169
try:
    FF_API_INIT_PACKET = (LIBAVCODEC_VERSION_MAJOR < 60)
except:
    pass

# /home/josiah/ctypesgen_test/av/adts_parser.h: 25
try:
    AV_AAC_ADTS_HEADER_SIZE = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 30
try:
    AES_CTR_KEY_SIZE = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/aes_ctr.h: 31
try:
    AES_CTR_IV_SIZE = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 225
try:
    FF_LAMBDA_SHIFT = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 226
try:
    FF_LAMBDA_SCALE = (1 << FF_LAMBDA_SHIFT)
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 227
try:
    FF_QP2LAMBDA = 118
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 228
try:
    FF_LAMBDA_MAX = ((256 * 128) - 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 230
try:
    FF_QUALITY_SCALE = FF_LAMBDA_SCALE
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 254
try:
    AV_TIME_BASE = 1000000
except:
    pass

# /usr/include/asm-generic/errno-base.h: 26
try:
    EINVAL = 22
except:
    pass

# /usr/include/limits.h: 81
try:
    INT_MAX = 2147483647
except:
    pass

# /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/include-fixed/limits.h: 119
# #undef INT_MAX
try:
    del INT_MAX
except NameError:
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

# /home/josiah/ctypesgen_test/av/common.h: 50
def AV_NE(be, le):
    return le

# /home/josiah/ctypesgen_test/av/common.h: 54
def RSHIFT(a, b):
    return (a > 0) and ((a + ((1 << b) >> 1)) >> b) or (((a + ((1 << b) >> 1)) - 1) >> b)

# /home/josiah/ctypesgen_test/av/common.h: 56
def ROUNDED_DIV(a, b):
    return ((a >= 0) and (a + (b >> 1)) or (a - (b >> 1)) / b)

# /home/josiah/ctypesgen_test/av/common.h: 58
def AV_CEIL_RSHIFT(a, b):
    return (not (av_builtin_constant_p (b))) and (-((-a) >> b)) or (((a + (1 << b)) - 1) >> b)

# /home/josiah/ctypesgen_test/av/common.h: 61
try:
    FF_CEIL_RSHIFT = AV_CEIL_RSHIFT
except:
    pass

# /home/josiah/ctypesgen_test/av/common.h: 63
def FFUDIV(a, b):
    return ((a > 0) and a or ((a - b) + 1) / b)

# /home/josiah/ctypesgen_test/av/common.h: 64
def FFUMOD(a, b):
    return (a - (b * (FFUDIV (a, b))))

# /home/josiah/ctypesgen_test/av/common.h: 72
def FFABS(a):
    return (a >= 0) and a or (-a)

# /home/josiah/ctypesgen_test/av/common.h: 73
def FFSIGN(a):
    return (a > 0) and 1 or (-1)

# /home/josiah/ctypesgen_test/av/common.h: 81
def FFNABS(a):
    return (a <= 0) and a or (-a)

# /home/josiah/ctypesgen_test/av/common.h: 89
def FFABSU(a):
    return (a <= 0) and (-(c_uint (ord_if_char(a))).value) or (c_uint (ord_if_char(a))).value

# /home/josiah/ctypesgen_test/av/common.h: 90
def FFABS64U(a):
    return (a <= 0) and (-(c_uint64 (ord_if_char(a))).value) or (c_uint64 (ord_if_char(a))).value

# /home/josiah/ctypesgen_test/av/common.h: 101
def FFDIFFSIGN(x, y):
    return ((x > y) - (x < y))

# /home/josiah/ctypesgen_test/av/common.h: 103
def FFMAX(a, b):
    return (a > b) and a or b

# /home/josiah/ctypesgen_test/av/common.h: 104
def FFMAX3(a, b, c):
    return (FFMAX ((FFMAX (a, b)), c))

# /home/josiah/ctypesgen_test/av/common.h: 105
def FFMIN(a, b):
    return (a > b) and b or a

# /home/josiah/ctypesgen_test/av/common.h: 106
def FFMIN3(a, b, c):
    return (FFMIN ((FFMIN (a, b)), c))

# /home/josiah/ctypesgen_test/av/common.h: 109
def FF_ARRAY_ELEMS(a):
    return (sizeof(a) / sizeof((a [0])))

# /home/josiah/ctypesgen_test/av/common.h: 478
def MKTAG(a, b, c, d):
    return (((a | (b << 8)) | (c << 16)) | ((c_uint (ord_if_char(d))).value << 24))

# /home/josiah/ctypesgen_test/av/common.h: 479
def MKBETAG(a, b, c, d):
    return (((d | (c << 8)) | (b << 16)) | ((c_uint (ord_if_char(a))).value << 24))

# /home/josiah/ctypesgen_test/av/error.h: 39
def AVERROR(e):
    return (-e)

# /home/josiah/ctypesgen_test/av/error.h: 40
def AVUNERROR(e):
    return (-e)

# /home/josiah/ctypesgen_test/av/error.h: 47
def FFERRTAG(a, b, c, d):
    return (-(c_int (ord_if_char((MKTAG (a, b, c, d))))).value)

# /home/josiah/ctypesgen_test/av/error.h: 49
try:
    AVERROR_BSF_NOT_FOUND = (FFERRTAG (248, b'B', b'S', b'F'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 50
try:
    AVERROR_BUG = (FFERRTAG (b'B', b'U', b'G', b'!'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 51
try:
    AVERROR_BUFFER_TOO_SMALL = (FFERRTAG (b'B', b'U', b'F', b'S'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 52
try:
    AVERROR_DECODER_NOT_FOUND = (FFERRTAG (248, b'D', b'E', b'C'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 53
try:
    AVERROR_DEMUXER_NOT_FOUND = (FFERRTAG (248, b'D', b'E', b'M'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 54
try:
    AVERROR_ENCODER_NOT_FOUND = (FFERRTAG (248, b'E', b'N', b'C'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 55
try:
    AVERROR_EOF = (FFERRTAG (b'E', b'O', b'F', b' '))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 56
try:
    AVERROR_EXIT = (FFERRTAG (b'E', b'X', b'I', b'T'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 57
try:
    AVERROR_EXTERNAL = (FFERRTAG (b'E', b'X', b'T', b' '))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 58
try:
    AVERROR_FILTER_NOT_FOUND = (FFERRTAG (248, b'F', b'I', b'L'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 59
try:
    AVERROR_INVALIDDATA = (FFERRTAG (b'I', b'N', b'D', b'A'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 60
try:
    AVERROR_MUXER_NOT_FOUND = (FFERRTAG (248, b'M', b'U', b'X'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 61
try:
    AVERROR_OPTION_NOT_FOUND = (FFERRTAG (248, b'O', b'P', b'T'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 62
try:
    AVERROR_PATCHWELCOME = (FFERRTAG (b'P', b'A', b'W', b'E'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 63
try:
    AVERROR_PROTOCOL_NOT_FOUND = (FFERRTAG (248, b'P', b'R', b'O'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 65
try:
    AVERROR_STREAM_NOT_FOUND = (FFERRTAG (248, b'S', b'T', b'R'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 70
try:
    AVERROR_BUG2 = (FFERRTAG (b'B', b'U', b'G', b' '))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 71
try:
    AVERROR_UNKNOWN = (FFERRTAG (b'U', b'N', b'K', b'N'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 72
try:
    AVERROR_EXPERIMENTAL = (-733130664)
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 73
try:
    AVERROR_INPUT_CHANGED = (-1668179713)
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 74
try:
    AVERROR_OUTPUT_CHANGED = (-1668179714)
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 76
try:
    AVERROR_HTTP_BAD_REQUEST = (FFERRTAG (248, b'4', b'0', b'0'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 77
try:
    AVERROR_HTTP_UNAUTHORIZED = (FFERRTAG (248, b'4', b'0', b'1'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 78
try:
    AVERROR_HTTP_FORBIDDEN = (FFERRTAG (248, b'4', b'0', b'3'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 79
try:
    AVERROR_HTTP_NOT_FOUND = (FFERRTAG (248, b'4', b'0', b'4'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 80
try:
    AVERROR_HTTP_OTHER_4XX = (FFERRTAG (248, b'4', b'X', b'X'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 81
try:
    AVERROR_HTTP_SERVER_ERROR = (FFERRTAG (248, b'5', b'X', b'X'))
except:
    pass

# /home/josiah/ctypesgen_test/av/error.h: 83
try:
    AV_ERROR_MAX_STRING_SIZE = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/mem.h: 125
def DECLARE_ALIGNED(n, t, v):
    return (t + v)

# /home/josiah/ctypesgen_test/av/mem.h: 126
def DECLARE_ASM_ALIGNED(n, t, v):
    return (t + v)

# /home/josiah/ctypesgen_test/av/mathematics.h: 46
try:
    M_LOG2_10 = 3.321928094887362
except:
    pass

# /home/josiah/ctypesgen_test/av/mathematics.h: 49
try:
    M_PHI = 1.618033988749895
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 50
def AV_IS_INPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_INPUT))

# /home/josiah/ctypesgen_test/av/log.h: 55
def AV_IS_OUTPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_OUTPUT))

# /home/josiah/ctypesgen_test/av/log.h: 176
try:
    AV_LOG_QUIET = (-8)
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 181
try:
    AV_LOG_PANIC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 188
try:
    AV_LOG_FATAL = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 194
try:
    AV_LOG_ERROR = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 200
try:
    AV_LOG_WARNING = 24
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 205
try:
    AV_LOG_INFO = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 210
try:
    AV_LOG_VERBOSE = 40
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 215
try:
    AV_LOG_DEBUG = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 220
try:
    AV_LOG_TRACE = 56
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 222
try:
    AV_LOG_MAX_OFFSET = (AV_LOG_TRACE - AV_LOG_QUIET)
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 236
def AV_LOG_C(x):
    return (x << 8)

# /home/josiah/ctypesgen_test/av/log.h: 384
try:
    AV_LOG_SKIP_REPEATED = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/log.h: 392
try:
    AV_LOG_PRINT_LEVEL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/pixfmt.h: 32
try:
    AVPALETTE_SIZE = 1024
except:
    pass

# /home/josiah/ctypesgen_test/av/pixfmt.h: 33
try:
    AVPALETTE_COUNT = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avutil.h: 331
def av_int_list_length(list, term):
    return (av_int_list_length_for_size (sizeof((list[0])), list, term))

# /home/josiah/ctypesgen_test/av/avutil.h: 346
try:
    AV_FOURCC_MAX_STRING_SIZE = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 23
try:
    AVC1394_H = 1
except:
    pass

# /usr/include/time.h: 23
try:
    _TIME_H = 1
except:
    pass

# /usr/include/bits/time.h: 24
try:
    _BITS_TIME_H = 1
except:
    pass

# /usr/include/bits/time.h: 34
try:
    CLOCKS_PER_SEC = (__clock_t (ord_if_char(1000000))).value
except:
    pass

# /usr/include/bits/time.h: 46
try:
    CLOCK_REALTIME = 0
except:
    pass

# /usr/include/bits/time.h: 48
try:
    CLOCK_MONOTONIC = 1
except:
    pass

# /usr/include/bits/time.h: 50
try:
    CLOCK_PROCESS_CPUTIME_ID = 2
except:
    pass

# /usr/include/bits/time.h: 52
try:
    CLOCK_THREAD_CPUTIME_ID = 3
except:
    pass

# /usr/include/bits/time.h: 54
try:
    CLOCK_MONOTONIC_RAW = 4
except:
    pass

# /usr/include/bits/time.h: 56
try:
    CLOCK_REALTIME_COARSE = 5
except:
    pass

# /usr/include/bits/time.h: 58
try:
    CLOCK_MONOTONIC_COARSE = 6
except:
    pass

# /usr/include/bits/time.h: 60
try:
    CLOCK_BOOTTIME = 7
except:
    pass

# /usr/include/bits/time.h: 62
try:
    CLOCK_REALTIME_ALARM = 8
except:
    pass

# /usr/include/bits/time.h: 64
try:
    CLOCK_BOOTTIME_ALARM = 9
except:
    pass

# /usr/include/bits/time.h: 66
try:
    CLOCK_TAI = 11
except:
    pass

# /usr/include/bits/time.h: 69
try:
    TIMER_ABSTIME = 1
except:
    pass

# /usr/include/time.h: 65
try:
    TIME_UTC = 1
except:
    pass

# /usr/include/time.h: 181
def __isleap(year):
    return (((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0)))

# /home/josiah/ctypesgen_test/av/avc1394.h: 29
try:
    AVC1394_RESPONSE_NOT_IMPLEMENTED = 134217728
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 30
try:
    AVC1394_RESPONSE_ACCEPTED = 150994944
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 31
try:
    AVC1394_RESPONSE_REJECTED = 167772160
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 32
try:
    AVC1394_RESPONSE_IN_TRANSITION = 184549376
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 33
try:
    AVC1394_RESPONSE_IMPLEMENTED = 201326592
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 34
try:
    AVC1394_RESPONSE_STABLE = 201326592
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 35
try:
    AVC1394_RESPONSE_CHANGED = 218103808
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 36
try:
    AVC1394_RESPONSE_INTERIM = 251658240
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 39
try:
    AVC1394_RESP_NOT_IMPLEMENTED = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 40
try:
    AVC1394_RESP_ACCEPTED = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 41
try:
    AVC1394_RESP_REJECTED = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 42
try:
    AVC1394_RESP_IN_TRANSITION = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 43
try:
    AVC1394_RESP_IMPLEMENTED = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 44
try:
    AVC1394_RESP_STABLE = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 45
try:
    AVC1394_RESP_CHANGED = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 46
try:
    AVC1394_RESP_INTERIM = 15
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 49
def AVC1394_MASK_START(x):
    return (x & 4026531840)

# /home/josiah/ctypesgen_test/av/avc1394.h: 50
def AVC1394_MASK_CTYPE(x):
    return (x & 251658240)

# /home/josiah/ctypesgen_test/av/avc1394.h: 51
def AVC1394_MASK_RESPONSE(x):
    return (x & 251658240)

# /home/josiah/ctypesgen_test/av/avc1394.h: 52
def AVC1394_MASK_SUBUNIT_TYPE(x):
    return (x & 16252928)

# /home/josiah/ctypesgen_test/av/avc1394.h: 53
def AVC1394_MASK_SUBUNIT_ID(x):
    return (x & 458752)

# /home/josiah/ctypesgen_test/av/avc1394.h: 54
def AVC1394_MASK_OPCODE(x):
    return (x & 65280)

# /home/josiah/ctypesgen_test/av/avc1394.h: 55
def AVC1394_MASK_OPERAND0(x):
    return (x & 255)

# /home/josiah/ctypesgen_test/av/avc1394.h: 56
def AVC1394_MASK_OPERAND(x, n):
    return (x & (4278190080 >> (((n - 1) % 4) * 8)))

# /home/josiah/ctypesgen_test/av/avc1394.h: 57
def AVC1394_MASK_RESPONSE_OPERAND(x, n):
    return (x & (4278190080 >> ((n % 4) * 8)))

# /home/josiah/ctypesgen_test/av/avc1394.h: 60
def AVC1394_GET_CTYPE(x):
    return ((x & 251658240) >> 24)

# /home/josiah/ctypesgen_test/av/avc1394.h: 61
def AVC1394_GET_RESPONSE(x):
    return ((x & 251658240) >> 24)

# /home/josiah/ctypesgen_test/av/avc1394.h: 62
def AVC1394_GET_SUBUNIT_TYPE(x):
    return ((x & 16252928) >> 19)

# /home/josiah/ctypesgen_test/av/avc1394.h: 63
def AVC1394_GET_SUBUNIT_ID(x):
    return ((x & 458752) >> 16)

# /home/josiah/ctypesgen_test/av/avc1394.h: 64
def AVC1394_GET_OPCODE(x):
    return ((x & 65280) >> 8)

# /home/josiah/ctypesgen_test/av/avc1394.h: 65
def AVC1394_GET_OPERAND0(x):
    return (x & 255)

# /home/josiah/ctypesgen_test/av/avc1394.h: 66
def AVC1394_GET_OPERAND(x, n):
    return ((x & (4278190080 >> (((n - 1) % 4) * 8))) >> (((n - 1) % 4) * 8))

# /home/josiah/ctypesgen_test/av/avc1394.h: 67
def AVC1394_GET_RESPONSE_OPERAND(x, n):
    return ((x & (4278190080 >> ((n % 4) * 8))) >> (((3 - n) % 4) * 8))

# /home/josiah/ctypesgen_test/av/avc1394.h: 70
try:
    AVC1394_CTYPE_CONTROL = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 71
try:
    AVC1394_CTYPE_STATUS = 16777216
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 72
try:
    AVC1394_CTYPE_SPECIFIC_INQUIRY = 33554432
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 73
try:
    AVC1394_CTYPE_NOTIFY = 50331648
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 74
try:
    AVC1394_CTYPE_GENERAL_INQUIRY = 67108864
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 76
try:
    AVC1394_CTYP_CONTROL = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 77
try:
    AVC1394_CTYP_STATUS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 78
try:
    AVC1394_CTYP_SPECIFIC_INQUIRY = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 79
try:
    AVC1394_CTYP_NOTIFY = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 80
try:
    AVC1394_CTYP_GENERAL_INQUIRY = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 83
try:
    AVC1394_SUBUNIT_TYPE_VIDEO_MONITOR = (0 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 84
try:
    AVC1394_SUBUNIT_TYPE_AUDIO = (1 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 85
try:
    AVC1394_SUBUNIT_TYPE_PRINTER = (2 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 86
try:
    AVC1394_SUBUNIT_TYPE_DISC_RECORDER = (3 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 87
try:
    AVC1394_SUBUNIT_TYPE_TAPE_RECORDER = (4 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 88
try:
    AVC1394_SUBUNIT_TYPE_VCR = (4 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 89
try:
    AVC1394_SUBUNIT_TYPE_TUNER = (5 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 90
try:
    AVC1394_SUBUNIT_TYPE_CA = (6 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 91
try:
    AVC1394_SUBUNIT_TYPE_VIDEO_CAMERA = (7 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 92
try:
    AVC1394_SUBUNIT_TYPE_PANEL = (9 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 93
try:
    AVC1394_SUBUNIT_TYPE_BULLETIN_BOARD = (10 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 94
try:
    AVC1394_SUBUNIT_TYPE_CAMERA_STORAGE = (11 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 95
try:
    AVC1394_SUBUNIT_TYPE_MUSIC = (12 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 96
try:
    AVC1394_SUBUNIT_TYPE_VENDOR_UNIQUE = (28 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 97
try:
    AVC1394_SUBUNIT_TYPE_EXTENDED = (30 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 98
try:
    AVC1394_SUBUNIT_TYPE_UNIT = (31 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 101
try:
    AVC1394_SUBUNIT_VIDEO_MONITOR = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 102
try:
    AVC1394_SUBUNIT_DISC_RECORDER = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 103
try:
    AVC1394_SUBUNIT_TAPE_RECORDER = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 104
try:
    AVC1394_SUBUNIT_VCR = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 105
try:
    AVC1394_SUBUNIT_TUNER = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 106
try:
    AVC1394_SUBUNIT_VIDEO_CAMERA = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 107
try:
    AVC1394_SUBUNIT_VENDOR_UNIQUE = 28
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 108
try:
    AVC1394_SUBUNIT_EXTENDED = 30
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 109
try:
    AVC1394_SUBUNIT_UNIT = 31
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 112
try:
    AVC1394_SUBUNIT_ID_0 = (0 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 113
try:
    AVC1394_SUBUNIT_ID_1 = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 114
try:
    AVC1394_SUBUNIT_ID_2 = (2 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 115
try:
    AVC1394_SUBUNIT_ID_3 = (3 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 116
try:
    AVC1394_SUBUNIT_ID_4 = (4 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 117
try:
    AVC1394_SUBUNIT_ID_EXTENDED = (5 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 118
try:
    AVC1394_SUBUNIT_ID_IGNORE = (7 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 121
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_GENERAL = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 122
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_AUDIO = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 123
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_MIDI = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 124
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_SMPTE = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 125
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_SAMPLECOUNT = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 126
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_AUDIOSYNC = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 127
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_RESERVED = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 128
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_MORE = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 130
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_NONBLOCKING = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 131
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_BLOCKING = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 133
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_AUDIOSYNC_BUS = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 134
try:
    AVC1394_SUBUNIT_MUSIC_CAPABILITY_AUDIOSYNC_EXTERNAL = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 137
try:
    AVC1394_COMMAND_CHANNEL_USAGE = 4608
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 138
try:
    AVC1394_COMMAND_CONNECT = 9216
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 139
try:
    AVC1394_COMMAND_CONNECT_AV = 8192
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 140
try:
    AVC1394_COMMAND_CONNECTIONS = 8704
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 141
try:
    AVC1394_COMMAND_DIGITAL_INPUT = 4352
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 142
try:
    AVC1394_COMMAND_DIGITAL_OUTPUT = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 143
try:
    AVC1394_COMMAND_DISCONNECT = 9472
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 144
try:
    AVC1394_COMMAND_DISCONNECT_AV = 8448
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 145
try:
    AVC1394_COMMAND_INPUT_PLUG_SIGNAL_FORMAT = 6400
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 146
try:
    AVC1394_COMMAND_OUTPUT_PLUG_SIGNAL_FORMAT = 6144
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 147
try:
    AVC1394_COMMAND_SUBUNIT_INFO = 12544
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 148
try:
    AVC1394_COMMAND_UNIT_INFO = 12288
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 151
try:
    AVC1394_CMD_CHANNEL_USAGE = 18
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 152
try:
    AVC1394_CMD_CONNECT = 36
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 153
try:
    AVC1394_CMD_CONNECT_AV = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 154
try:
    AVC1394_CMD_CONNECTIONS = 34
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 155
try:
    AVC1394_CMD_DIGITAL_INPUT = 17
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 156
try:
    AVC1394_CMD_DIGITAL_OUTPUT = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 157
try:
    AVC1394_CMD_DISCONNECT = 37
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 158
try:
    AVC1394_CMD_DISCONNECT_AV = 33
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 159
try:
    AVC1394_CMD_INPUT_PLUG_SIGNAL_FORMAT = 25
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 160
try:
    AVC1394_CMD_OUTPUT_PLUG_SIGNAL_FORMAT = 24
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 161
try:
    AVC1394_CMD_SUBUNIT_INFO = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 162
try:
    AVC1394_CMD_UNIT_INFO = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 165
try:
    AVC1394_COMMAND_OPEN_DESCRIPTOR = 2048
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 166
try:
    AVC1394_COMMAND_READ_DESCRIPTOR = 2304
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 167
try:
    AVC1394_COMMAND_WRITE_DESCRIPTOR = 2560
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 168
try:
    AVC1394_COMMAND_SEARCH_DESCRIPTOR = 2816
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 169
try:
    AVC1394_COMMAND_OBJECT_NUMBER_SELECT = 3328
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 170
try:
    AVC1394_COMMAND_POWER = 45568
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 171
try:
    AVC1394_COMMAND_RESERVE = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 172
try:
    AVC1394_COMMAND_PLUG_INFO = 512
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 173
try:
    AVC1394_COMMAND_VENDOR_DEPENDENT = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 176
try:
    AVC1394_CMD_OPEN_DESCRIPTOR = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 177
try:
    AVC1394_CMD_READ_DESCRIPTOR = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 178
try:
    AVC1394_CMD_WRITE_DESCRIPTOR = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 179
try:
    AVC1394_CMD_SEARCH_DESCRIPTOR = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 180
try:
    AVC1394_CMD_OBJECT_NUMBER_SELECT = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 181
try:
    AVC1394_CMD_POWER = 178
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 182
try:
    AVC1394_CMD_RESERVE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 183
try:
    AVC1394_CMD_PLUG_INFO = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 184
try:
    AVC1394_CMD_VENDOR_DEPENDENT = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 187
try:
    AVC1394_CMD_OPERAND_POWER_ON = 112
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 188
try:
    AVC1394_CMD_OPERAND_POWER_OFF = 96
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 190
try:
    AVC1394_OPERAND_UNIT_INFO_EXTENSION_CODE = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 193
try:
    AVC1394_OPERAND_DESCRIPTOR_TYPE_SUBUNIT_IDENTIFIER_DESCRIPTOR = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 194
try:
    AVC1394_OPERAND_DESCRIPTOR_TYPE_OBJECT_LIST_DESCRIPTOR_ID = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 195
try:
    AVC1394_OPERAND_DESCRIPTOR_TYPE_OBJECT_LIST_DESCRIPTOR_TYPE = 17
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 196
try:
    AVC1394_OPERAND_DESCRIPTOR_TYPE_OBJECT_ENTRY_DESCRIPTOR_POSITION = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 197
try:
    AVC1394_OPERAND_DESCRIPTOR_TYPE_OBJECT_ENTRY_DESCRIPTOR_ID = 33
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 198
try:
    AVC1394_OPERAND_DESCRIPTOR_SUBFUNCTION_CLOSE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 199
try:
    AVC1394_OPERAND_DESCRIPTOR_SUBFUNCTION_READ_OPEN = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 200
try:
    AVC1394_OPERAND_DESCRIPTOR_SUBFUNCTION_WRITE_OPEN = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 203
try:
    AVC1394_VCR_COMMAND_ANALOG_AUDIO_OUTPUT_MODE = 28672
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 204
try:
    AVC1394_VCR_COMMAND_AREA_MODE = 29184
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 205
try:
    AVC1394_VCR_COMMAND_ABSOLUTE_TRACK_NUMBER = 20992
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 206
try:
    AVC1394_VCR_COMMAND_AUDIO_MODE = 28928
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 207
try:
    AVC1394_VCR_COMMAND_BACKWARD = 22016
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 208
try:
    AVC1394_VCR_COMMAND_BINARY_GROUP = 23040
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 209
try:
    AVC1394_VCR_COMMAND_EDIT_MODE = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 210
try:
    AVC1394_VCR_COMMAND_FORWARD = 21760
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 211
try:
    AVC1394_VCR_COMMAND_INPUT_SIGNAL_MODE = 30976
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 212
try:
    AVC1394_VCR_COMMAND_LOAD_MEDIUM = 49408
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 213
try:
    AVC1394_VCR_COMMAND_MARKER = 51712
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 214
try:
    AVC1394_VCR_COMMAND_MEDIUM_INFO = 55808
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 215
try:
    AVC1394_VCR_COMMAND_OPEN_MIC = 24576
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 216
try:
    AVC1394_VCR_COMMAND_OUTPUT_SIGNAL_MODE = 30720
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 217
try:
    AVC1394_VCR_COMMAND_PLAY = 49920
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 218
try:
    AVC1394_VCR_COMMAND_PRESET = 17664
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 219
try:
    AVC1394_VCR_COMMAND_READ_MIC = 24832
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 220
try:
    AVC1394_VCR_COMMAND_RECORD = 49664
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 221
try:
    AVC1394_VCR_COMMAND_RECORDING_DATE = 21248
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 222
try:
    AVC1394_VCR_COMMAND_RECORDING_SPEED = 56064
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 223
try:
    AVC1394_VCR_COMMAND_RECORDING_TIME = 21504
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 224
try:
    AVC1394_VCR_COMMAND_RELATIVE_TIME_COUNTER = 22272
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 225
try:
    AVC1394_VCR_COMMAND_SEARCH_MODE = 20480
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 226
try:
    AVC1394_VCR_COMMAND_SMPTE_EBU_RECORDING_TIME = 23552
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 227
try:
    AVC1394_VCR_COMMAND_SMPTE_EBU_TIME_CODE = 22784
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 228
try:
    AVC1394_VCR_COMMAND_TAPE_PLAYBACK_FORMAT = 54016
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 229
try:
    AVC1394_VCR_COMMAND_TAPE_RECORDING_FORMAT = 53760
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 230
try:
    AVC1394_VCR_COMMAND_TIME_CODE = 20736
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 231
try:
    AVC1394_VCR_COMMAND_TRANSPORT_STATE = 53248
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 232
try:
    AVC1394_VCR_COMMAND_WIND = 50176
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 233
try:
    AVC1394_VCR_COMMAND_WRITE_MIC = 25088
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 236
try:
    AVC1394_VCR_CMD_ANALOG_AUDIO_OUTPUT_MODE = 112
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 237
try:
    AVC1394_VCR_CMD_AREA_MODE = 114
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 238
try:
    AVC1394_VCR_CMD_ABSOLUTE_TRACK_NUMBER = 82
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 239
try:
    AVC1394_VCR_CMD_AUDIO_MODE = 113
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 240
try:
    AVC1394_VCR_CMD_BACKWARD = 86
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 241
try:
    AVC1394_VCR_CMD_BINARY_GROUP = 90
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 242
try:
    AVC1394_VCR_CMD_EDIT_MODE = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 243
try:
    AVC1394_VCR_CMD_FORWARD = 85
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 244
try:
    AVC1394_VCR_CMD_INPUT_SIGNAL_MODE = 121
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 245
try:
    AVC1394_VCR_CMD_LOAD_MEDIUM = 193
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 246
try:
    AVC1394_VCR_CMD_MARKER = 202
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 247
try:
    AVC1394_VCR_CMD_MEDIUM_INFO = 218
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 248
try:
    AVC1394_VCR_CMD_OPEN_MIC = 96
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 249
try:
    AVC1394_VCR_CMD_OUTPUT_SIGNAL_MODE = 120
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 250
try:
    AVC1394_VCR_CMD_PLAY = 195
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 251
try:
    AVC1394_VCR_CMD_PRESET = 69
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 252
try:
    AVC1394_VCR_CMD_READ_MIC = 97
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 253
try:
    AVC1394_VCR_CMD_RECORD = 194
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 254
try:
    AVC1394_VCR_CMD_RECORDING_DATE = 83
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 255
try:
    AVC1394_VCR_CMD_RECORDING_SPEED = 219
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 256
try:
    AVC1394_VCR_CMD_RECORDING_TIME = 84
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 257
try:
    AVC1394_VCR_CMD_RELATIVE_TIME_COUNTER = 87
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 258
try:
    AVC1394_VCR_CMD_SEARCH_MODE = 80
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 259
try:
    AVC1394_VCR_CMD_SMPTE_EBU_RECORDING_TIME = 92
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 260
try:
    AVC1394_VCR_CMD_SMPTE_EBU_TIME_CODE = 89
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 261
try:
    AVC1394_VCR_CMD_TAPE_PLAYBACK_FORMAT = 211
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 262
try:
    AVC1394_VCR_CMD_TAPE_RECORDING_FORMAT = 210
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 263
try:
    AVC1394_VCR_CMD_TIME_CODE = 81
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 264
try:
    AVC1394_VCR_CMD_TRANSPORT_STATE = 208
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 265
try:
    AVC1394_VCR_CMD_WIND = 196
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 266
try:
    AVC1394_VCR_CMD_WRITE_MIC = 98
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 269
try:
    AVC1394_VCR_OPERAND_LOAD_MEDIUM_EJECT = 96
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 270
try:
    AVC1394_VCR_OPERAND_LOAD_MEDIUM_OPEN_TRAY = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 271
try:
    AVC1394_VCR_OPERAND_LOAD_MEDIUM_CLOSE_TRAY = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 272
try:
    AVC1394_VCR_OPERAND_PLAY_NEXT_FRAME = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 273
try:
    AVC1394_VCR_OPERAND_PLAY_SLOWEST_FORWARD = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 274
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_6 = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 275
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_5 = 51
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 276
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_4 = 52
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 277
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_3 = 53
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 278
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_2 = 54
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 279
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_FORWARD_1 = 55
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 280
try:
    AVC1394_VCR_OPERAND_PLAY_X1_FORWARD = 56
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 281
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_1 = 57
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 282
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_2 = 58
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 283
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_3 = 59
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 284
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_4 = 60
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 285
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_5 = 61
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 286
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_FORWARD_6 = 62
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 287
try:
    AVC1394_VCR_OPERAND_PLAY_FASTEST_FORWARD = 63
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 288
try:
    AVC1394_VCR_OPERAND_PLAY_PREVIOUS_FRAME = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 289
try:
    AVC1394_VCR_OPERAND_PLAY_SLOWEST_REVERSE = 65
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 290
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_6 = 66
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 291
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_5 = 67
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 292
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_4 = 68
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 293
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_3 = 69
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 294
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_2 = 70
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 295
try:
    AVC1394_VCR_OPERAND_PLAY_SLOW_REVERSE_1 = 71
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 296
try:
    AVC1394_VCR_OPERAND_PLAY_X1_REVERSE = 72
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 297
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_1 = 73
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 298
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_2 = 74
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 299
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_3 = 75
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 300
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_4 = 76
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 301
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_5 = 77
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 302
try:
    AVC1394_VCR_OPERAND_PLAY_FAST_REVERSE_6 = 78
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 303
try:
    AVC1394_VCR_OPERAND_PLAY_FASTEST_REVERSE = 79
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 304
try:
    AVC1394_VCR_OPERAND_PLAY_REVERSE = 101
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 305
try:
    AVC1394_VCR_OPERAND_PLAY_REVERSE_PAUSE = 109
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 306
try:
    AVC1394_VCR_OPERAND_PLAY_FORWARD = 117
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 307
try:
    AVC1394_VCR_OPERAND_PLAY_FORWARD_PAUSE = 125
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 309
try:
    AVC1394_VCR_OPERAND_RECORD_UNSPEC_INSERTED = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 310
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_23_INSERTED = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 311
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_1_INSERTED = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 312
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_123_INSERTED = 51
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 313
try:
    AVC1394_VCR_OPERAND_RECORD_UNSPEC_INSERTED_PAUSE = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 314
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_23_INSERTED_PAUSE = 65
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 315
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_1_INSERTED_PAUSE = 66
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 316
try:
    AVC1394_VCR_OPERAND_RECORD_AREA_123_INSERTED_PAUSE = 67
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 317
try:
    AVC1394_VCR_OPERAND_RECORD_RECORD = 117
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 318
try:
    AVC1394_VCR_OPERAND_RECORD_PAUSE = 125
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 320
try:
    AVC1394_VCR_OPERAND_TRANSPORT_STATE = 127
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 321
try:
    AVC1394_VCR_OPERAND_WIND_HIGH_SPEED_REWIND = 69
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 322
try:
    AVC1394_VCR_OPERAND_WIND_STOP = 96
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 323
try:
    AVC1394_VCR_OPERAND_WIND_REWIND = 101
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 324
try:
    AVC1394_VCR_OPERAND_WIND_FAST_FORWARD = 117
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 325
try:
    AVC1394_VCR_OPERAND_TIME_CODE_CONTROL = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 326
try:
    AVC1394_VCR_OPERAND_TIME_CODE_STATUS = 113
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 327
try:
    AVC1394_VCR_OPERAND_RELATIVE_TIME_COUNTER_CONTROL = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 328
try:
    AVC1394_VCR_OPERAND_RELATIVE_TIME_COUNTER_STATUS = 113
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 329
try:
    AVC1394_VCR_OPERAND_TRANSPORT_STATE = 127
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 330
try:
    AVC1394_VCR_OPERAND_RECORDING_TIME_STATUS = 113
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 333
try:
    AVC1394_VCR_OPERAND_RECORDING_SPEED_STANDARD = 111
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 335
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_DVCR_STD = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 336
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_DVCR_SMALL = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 337
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_DVCR_MEDIUM = 51
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 338
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_VHS = 34
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 339
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_VHSC = 35
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 340
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_8MM = 18
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 341
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_MICROMV = 65
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 342
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_NONE = 96
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 343
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_UNKNOWN = 126
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 346
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_VHS_OK = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 347
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_VHS_WP = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 348
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_SVHS_OK = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 349
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_SVHS_WP = 65
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 350
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_DVHS_OK = 80
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 351
try:
    AVC1394_VCR_OPERAND_MEDIUM_INFO_DVHS_WP = 81
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 353
try:
    AVC1394_VCR_RESPONSE_TRANSPORT_STATE_LOAD_MEDIUM = 49408
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 354
try:
    AVC1394_VCR_RESPONSE_TRANSPORT_STATE_RECORD = 49664
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 355
try:
    AVC1394_VCR_RESPONSE_TRANSPORT_STATE_PLAY = 49920
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 356
try:
    AVC1394_VCR_RESPONSE_TRANSPORT_STATE_WIND = 50176
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 359
try:
    AVC1394_TUNER_COMMAND_DIRECT_SELECT_INFORMATION_TYPE = 200
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 360
try:
    AVC1394_TUNER_COMMAND_DIRECT_SELECT_DATA = 203
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 361
try:
    AVC1394_TUNER_COMMAND_CA_ENABLE = 204
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 362
try:
    AVC1394_TUNER_COMMAND_AVC1394_TUNER_STATUS = 205
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 365
try:
    AVC1394_TUNER_COMMAND_DIRECT_SELECT_INFORMATION_TYPE = 200
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 366
try:
    AVC1394_TUNER_COMMAND_DIRECT_SELECT_DATA = 203
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 367
try:
    AVC1394_TUNER_COMMAND_CA_ENABLE = 204
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 368
try:
    AVC1394_TUNER_COMMAND_AVC1394_TUNER_STATUS = 205
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 371
try:
    AVC1394_PANEL_COMMAND_PASS_THROUGH = 31744
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 372
try:
    AVC1394_PANEL_CMD_PASS_THROUGH = 124
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 373
try:
    AVC1394_PANEL_OPERAND_PRESS = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 374
try:
    AVC1394_PANEL_OPERAND_RELEASE = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 376
try:
    AVC1394_PANEL_OPERATION_SELECT = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 377
try:
    AVC1394_PANEL_OPERATION_UP = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 378
try:
    AVC1394_PANEL_OPERATION_DOWN = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 379
try:
    AVC1394_PANEL_OPERATION_LEFT = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 380
try:
    AVC1394_PANEL_OPERATION_RIGHT = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 381
try:
    AVC1394_PANEL_OPERATION_RIGHT_UP = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 382
try:
    AVC1394_PANEL_OPERATION_RIGHT_DOWN = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 383
try:
    AVC1394_PANEL_OPERATION_LEFT_UP = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 384
try:
    AVC1394_PANEL_OPERATION_LEFT_DOWN = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 385
try:
    AVC1394_PANEL_OPERATION_ROOT_MENU = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 386
try:
    AVC1394_PANEL_OPERATION_SETUP_MENU = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 387
try:
    AVC1394_PANEL_OPERATION_CONTENTS_MENU = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 388
try:
    AVC1394_PANEL_OPERATION_FAVORITE_MENU = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 389
try:
    AVC1394_PANEL_OPERATION_EXIT = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 390
try:
    AVC1394_PANEL_OPERATION_0 = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 391
try:
    AVC1394_PANEL_OPERATION_1 = 33
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 392
try:
    AVC1394_PANEL_OPERATION_2 = 34
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 393
try:
    AVC1394_PANEL_OPERATION_3 = 35
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 394
try:
    AVC1394_PANEL_OPERATION_4 = 36
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 395
try:
    AVC1394_PANEL_OPERATION_5 = 37
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 396
try:
    AVC1394_PANEL_OPERATION_6 = 38
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 397
try:
    AVC1394_PANEL_OPERATION_7 = 39
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 398
try:
    AVC1394_PANEL_OPERATION_8 = 40
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 399
try:
    AVC1394_PANEL_OPERATION_9 = 41
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 400
try:
    AVC1394_PANEL_OPERATION_DOT = 42
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 401
try:
    AVC1394_PANEL_OPERATION_ENTER = 43
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 402
try:
    AVC1394_PANEL_OPERATION_CLEAR = 44
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 403
try:
    AVC1394_PANEL_OPERATION_CHANNEL_UP = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 404
try:
    AVC1394_PANEL_OPERATION_CHANNEL_DOWN = 49
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 405
try:
    AVC1394_PANEL_OPERATION_PREVIOUS_CHANNEL = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 406
try:
    AVC1394_PANEL_OPERATION_SOUND_SELECT = 51
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 407
try:
    AVC1394_PANEL_OPERATION_INPUT_SELECT = 52
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 408
try:
    AVC1394_PANEL_OPERATION_DISPLAY_INFO = 53
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 409
try:
    AVC1394_PANEL_OPERATION_HELP = 54
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 410
try:
    AVC1394_PANEL_OPERATION_PAGE_UP = 55
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 411
try:
    AVC1394_PANEL_OPERATION_PAGE_DOWN = 56
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 412
try:
    AVC1394_PANEL_OPERATION_POWER = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 413
try:
    AVC1394_PANEL_OPERATION_VOLUME_UP = 65
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 414
try:
    AVC1394_PANEL_OPERATION_VOLUME_DOWN = 66
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 415
try:
    AVC1394_PANEL_OPERATION_MUTE = 67
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 416
try:
    AVC1394_PANEL_OPERATION_PLAY = 68
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 417
try:
    AVC1394_PANEL_OPERATION_STOP = 69
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 418
try:
    AVC1394_PANEL_OPERATION_PAUSE = 70
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 419
try:
    AVC1394_PANEL_OPERATION_RECORD = 71
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 420
try:
    AVC1394_PANEL_OPERATION_REWIND = 72
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 421
try:
    AVC1394_PANEL_OPERATION_FASTFORWARD = 73
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 422
try:
    AVC1394_PANEL_OPERATION_EJECT = 74
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 423
try:
    AVC1394_PANEL_OPERATION_FORWARD = 75
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 424
try:
    AVC1394_PANEL_OPERATION_BACKWARD = 73
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 425
try:
    AVC1394_PANEL_OPERATION_ANGLE = 80
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394.h: 426
try:
    AVC1394_PANEL_OPERATION_SUBPICTURE = 81
except:
    pass

# /home/josiah/ctypesgen_test/av/avc1394_vcr.h: 23
try:
    AVC1394_VCR_H = 1
except:
    pass

# /usr/include/libavutil/buffer.h: 128
try:
    AV_BUFFER_FLAG_READONLY = (1 << 0)
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

# /home/josiah/ctypesgen_test/av/codec_id.h: 186
try:
    AV_CODEC_ID_IFF_BYTERUN1 = AV_CODEC_ID_IFF_ILBM
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_id.h: 224
try:
    AV_CODEC_ID_H265 = AV_CODEC_ID_HEVC
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_id.h: 248
try:
    AV_CODEC_ID_H266 = AV_CODEC_ID_VVC
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 304
try:
    AV_PKT_DATA_QUALITY_FACTOR = AV_PKT_DATA_QUALITY_STATS
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 410
try:
    AV_PKT_FLAG_KEY = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 411
try:
    AV_PKT_FLAG_CORRUPT = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 417
try:
    AV_PKT_FLAG_DISCARD = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 424
try:
    AV_PKT_FLAG_TRUSTED = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/packet.h: 429
try:
    AV_PKT_FLAG_DISPOSABLE = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 44
try:
    AV_CODEC_CAP_DRAW_HORIZ_BAND = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 52
try:
    AV_CODEC_CAP_DR1 = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 53
try:
    AV_CODEC_CAP_TRUNCATED = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 77
try:
    AV_CODEC_CAP_DELAY = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 82
try:
    AV_CODEC_CAP_SMALL_LAST_FRAME = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 95
try:
    AV_CODEC_CAP_SUBFRAMES = (1 << 8)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 100
try:
    AV_CODEC_CAP_EXPERIMENTAL = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 104
try:
    AV_CODEC_CAP_CHANNEL_CONF = (1 << 10)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 108
try:
    AV_CODEC_CAP_FRAME_THREADS = (1 << 12)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 112
try:
    AV_CODEC_CAP_SLICE_THREADS = (1 << 13)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 116
try:
    AV_CODEC_CAP_PARAM_CHANGE = (1 << 14)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 122
try:
    AV_CODEC_CAP_OTHER_THREADS = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 124
try:
    AV_CODEC_CAP_AUTO_THREADS = AV_CODEC_CAP_OTHER_THREADS
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 129
try:
    AV_CODEC_CAP_VARIABLE_FRAME_SIZE = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 139
try:
    AV_CODEC_CAP_AVOID_PROBING = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 145
try:
    AV_CODEC_CAP_INTRA_ONLY = 1073741824
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 149
try:
    AV_CODEC_CAP_LOSSLESS = 2147483648
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 157
try:
    AV_CODEC_CAP_HARDWARE = (1 << 18)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 164
try:
    AV_CODEC_CAP_HYBRID = (1 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 171
try:
    AV_CODEC_CAP_ENCODER_REORDERED_OPAQUE = (1 << 20)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec.h: 178
try:
    AV_CODEC_CAP_ENCODER_FLUSH = (1 << 21)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 72
try:
    AV_CODEC_PROP_INTRA_ONLY = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 78
try:
    AV_CODEC_PROP_LOSSY = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 82
try:
    AV_CODEC_PROP_LOSSLESS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 92
try:
    AV_CODEC_PROP_REORDER = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 97
try:
    AV_CODEC_PROP_BITMAP_SUB = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/codec_desc.h: 102
try:
    AV_CODEC_PROP_TEXT_SUB = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 215
try:
    AV_INPUT_BUFFER_PADDING_SIZE = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 222
try:
    AV_INPUT_BUFFER_MIN_SIZE = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 271
try:
    AV_CODEC_FLAG_UNALIGNED = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 275
try:
    AV_CODEC_FLAG_QSCALE = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 279
try:
    AV_CODEC_FLAG_4MV = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 283
try:
    AV_CODEC_FLAG_OUTPUT_CORRUPT = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 287
try:
    AV_CODEC_FLAG_QPEL = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 292
try:
    AV_CODEC_FLAG_DROPCHANGED = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 296
try:
    AV_CODEC_FLAG_PASS1 = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 300
try:
    AV_CODEC_FLAG_PASS2 = (1 << 10)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 304
try:
    AV_CODEC_FLAG_LOOP_FILTER = (1 << 11)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 308
try:
    AV_CODEC_FLAG_GRAY = (1 << 13)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 312
try:
    AV_CODEC_FLAG_PSNR = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 317
try:
    AV_CODEC_FLAG_TRUNCATED = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 321
try:
    AV_CODEC_FLAG_INTERLACED_DCT = (1 << 18)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 325
try:
    AV_CODEC_FLAG_LOW_DELAY = (1 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 329
try:
    AV_CODEC_FLAG_GLOBAL_HEADER = (1 << 22)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 333
try:
    AV_CODEC_FLAG_BITEXACT = (1 << 23)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 338
try:
    AV_CODEC_FLAG_AC_PRED = (1 << 24)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 342
try:
    AV_CODEC_FLAG_INTERLACED_ME = (1 << 29)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 343
try:
    AV_CODEC_FLAG_CLOSED_GOP = (1 << 31)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 348
try:
    AV_CODEC_FLAG2_FAST = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 352
try:
    AV_CODEC_FLAG2_NO_OUTPUT = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 356
try:
    AV_CODEC_FLAG2_LOCAL_HEADER = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 361
try:
    AV_CODEC_FLAG2_DROP_FRAME_TIMECODE = (1 << 13)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 367
try:
    AV_CODEC_FLAG2_CHUNKS = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 371
try:
    AV_CODEC_FLAG2_IGNORE_CROP = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 376
try:
    AV_CODEC_FLAG2_SHOW_ALL = (1 << 22)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 380
try:
    AV_CODEC_FLAG2_EXPORT_MVS = (1 << 28)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 384
try:
    AV_CODEC_FLAG2_SKIP_MANUAL = (1 << 29)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 388
try:
    AV_CODEC_FLAG2_RO_FLUSH_NOOP = (1 << 30)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 403
try:
    AV_CODEC_EXPORT_DATA_MVS = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 407
try:
    AV_CODEC_EXPORT_DATA_PRFT = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 412
try:
    AV_CODEC_EXPORT_DATA_VIDEO_ENC_PARAMS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 417
try:
    AV_CODEC_EXPORT_DATA_FILM_GRAIN = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 514
try:
    AV_GET_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 519
try:
    AV_GET_ENCODE_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 609
try:
    FF_COMPRESSION_DEFAULT = (-1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 896
try:
    FF_PRED_LEFT = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 897
try:
    FF_PRED_PLANE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 898
try:
    FF_PRED_MEDIAN = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 941
try:
    FF_CMP_SAD = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 942
try:
    FF_CMP_SSE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 943
try:
    FF_CMP_SATD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 944
try:
    FF_CMP_DCT = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 945
try:
    FF_CMP_PSNR = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 946
try:
    FF_CMP_BIT = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 947
try:
    FF_CMP_RD = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 948
try:
    FF_CMP_ZERO = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 949
try:
    FF_CMP_VSAD = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 950
try:
    FF_CMP_VSSE = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 951
try:
    FF_CMP_NSSE = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 952
try:
    FF_CMP_W53 = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 953
try:
    FF_CMP_W97 = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 954
try:
    FF_CMP_DCTMAX = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 955
try:
    FF_CMP_DCT264 = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 956
try:
    FF_CMP_MEDIAN_SAD = 15
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 957
try:
    FF_CMP_CHROMA = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1015
try:
    SLICE_FLAG_CODED_ORDER = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1016
try:
    SLICE_FLAG_ALLOW_FIELD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1017
try:
    SLICE_FLAG_ALLOW_PLANE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1025
try:
    FF_MB_DECISION_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1026
try:
    FF_MB_DECISION_BITS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1027
try:
    FF_MB_DECISION_RD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1447
try:
    FF_CODER_TYPE_VLC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1448
try:
    FF_CODER_TYPE_AC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1449
try:
    FF_CODER_TYPE_RAW = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1450
try:
    FF_CODER_TYPE_RLE = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1573
try:
    FF_BUG_AUTODETECT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1574
try:
    FF_BUG_XVID_ILACE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1575
try:
    FF_BUG_UMP4 = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1576
try:
    FF_BUG_NO_PADDING = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1577
try:
    FF_BUG_AMV = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1578
try:
    FF_BUG_QPEL_CHROMA = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1579
try:
    FF_BUG_STD_QPEL = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1580
try:
    FF_BUG_QPEL_CHROMA2 = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1581
try:
    FF_BUG_DIRECT_BLOCKSIZE = 512
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1582
try:
    FF_BUG_EDGE = 1024
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1583
try:
    FF_BUG_HPEL_CHROMA = 2048
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1584
try:
    FF_BUG_DC_CLIP = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1585
try:
    FF_BUG_MS = 8192
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1586
try:
    FF_BUG_TRUNCATED = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1587
try:
    FF_BUG_IEDGE = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1602
try:
    FF_COMPLIANCE_VERY_STRICT = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1603
try:
    FF_COMPLIANCE_STRICT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1604
try:
    FF_COMPLIANCE_NORMAL = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1605
try:
    FF_COMPLIANCE_UNOFFICIAL = (-1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1606
try:
    FF_COMPLIANCE_EXPERIMENTAL = (-2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1614
try:
    FF_EC_GUESS_MVS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1615
try:
    FF_EC_DEBLOCK = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1616
try:
    FF_EC_FAVOR_INTER = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1624
try:
    FF_DEBUG_PICT_INFO = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1625
try:
    FF_DEBUG_RC = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1626
try:
    FF_DEBUG_BITSTREAM = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1627
try:
    FF_DEBUG_MB_TYPE = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1628
try:
    FF_DEBUG_QP = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1629
try:
    FF_DEBUG_DCT_COEFF = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1630
try:
    FF_DEBUG_SKIP = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1631
try:
    FF_DEBUG_STARTCODE = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1632
try:
    FF_DEBUG_ER = 1024
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1633
try:
    FF_DEBUG_MMCO = 2048
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1634
try:
    FF_DEBUG_BUGS = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1635
try:
    FF_DEBUG_BUFFERS = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1636
try:
    FF_DEBUG_THREADS = 65536
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1637
try:
    FF_DEBUG_GREEN_MD = 8388608
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1638
try:
    FF_DEBUG_NOMC = 16777216
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1653
try:
    AV_EF_CRCCHECK = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1654
try:
    AV_EF_BITSTREAM = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1655
try:
    AV_EF_BUFFER = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1656
try:
    AV_EF_EXPLODE = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1658
try:
    AV_EF_IGNORE_ERR = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1659
try:
    AV_EF_CAREFUL = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1660
try:
    AV_EF_COMPLIANT = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1661
try:
    AV_EF_AGGRESSIVE = (1 << 18)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1707
try:
    FF_DCT_AUTO = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1708
try:
    FF_DCT_FASTINT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1709
try:
    FF_DCT_INT = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1710
try:
    FF_DCT_MMX = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1711
try:
    FF_DCT_ALTIVEC = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1712
try:
    FF_DCT_FAAN = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1720
try:
    FF_IDCT_AUTO = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1721
try:
    FF_IDCT_INT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1722
try:
    FF_IDCT_SIMPLE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1723
try:
    FF_IDCT_SIMPLEMMX = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1724
try:
    FF_IDCT_ARM = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1725
try:
    FF_IDCT_ALTIVEC = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1726
try:
    FF_IDCT_SIMPLEARM = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1727
try:
    FF_IDCT_XVID = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1728
try:
    FF_IDCT_SIMPLEARMV5TE = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1729
try:
    FF_IDCT_SIMPLEARMV6 = 17
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1730
try:
    FF_IDCT_FAAN = 20
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1731
try:
    FF_IDCT_SIMPLENEON = 22
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1732
try:
    FF_IDCT_NONE = 24
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1733
try:
    FF_IDCT_SIMPLEAUTO = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1784
try:
    FF_THREAD_FRAME = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1785
try:
    FF_THREAD_SLICE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1859
try:
    FF_PROFILE_UNKNOWN = (-99)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1860
try:
    FF_PROFILE_RESERVED = (-100)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1862
try:
    FF_PROFILE_AAC_MAIN = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1863
try:
    FF_PROFILE_AAC_LOW = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1864
try:
    FF_PROFILE_AAC_SSR = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1865
try:
    FF_PROFILE_AAC_LTP = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1866
try:
    FF_PROFILE_AAC_HE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1867
try:
    FF_PROFILE_AAC_HE_V2 = 28
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1868
try:
    FF_PROFILE_AAC_LD = 22
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1869
try:
    FF_PROFILE_AAC_ELD = 38
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1870
try:
    FF_PROFILE_MPEG2_AAC_LOW = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1871
try:
    FF_PROFILE_MPEG2_AAC_HE = 131
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1873
try:
    FF_PROFILE_DNXHD = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1874
try:
    FF_PROFILE_DNXHR_LB = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1875
try:
    FF_PROFILE_DNXHR_SQ = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1876
try:
    FF_PROFILE_DNXHR_HQ = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1877
try:
    FF_PROFILE_DNXHR_HQX = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1878
try:
    FF_PROFILE_DNXHR_444 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1880
try:
    FF_PROFILE_DTS = 20
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1881
try:
    FF_PROFILE_DTS_ES = 30
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1882
try:
    FF_PROFILE_DTS_96_24 = 40
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1883
try:
    FF_PROFILE_DTS_HD_HRA = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1884
try:
    FF_PROFILE_DTS_HD_MA = 60
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1885
try:
    FF_PROFILE_DTS_EXPRESS = 70
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1887
try:
    FF_PROFILE_MPEG2_422 = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1888
try:
    FF_PROFILE_MPEG2_HIGH = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1889
try:
    FF_PROFILE_MPEG2_SS = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1890
try:
    FF_PROFILE_MPEG2_SNR_SCALABLE = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1891
try:
    FF_PROFILE_MPEG2_MAIN = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1892
try:
    FF_PROFILE_MPEG2_SIMPLE = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1894
try:
    FF_PROFILE_H264_CONSTRAINED = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1895
try:
    FF_PROFILE_H264_INTRA = (1 << 11)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1897
try:
    FF_PROFILE_H264_BASELINE = 66
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1898
try:
    FF_PROFILE_H264_CONSTRAINED_BASELINE = (66 | FF_PROFILE_H264_CONSTRAINED)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1899
try:
    FF_PROFILE_H264_MAIN = 77
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1900
try:
    FF_PROFILE_H264_EXTENDED = 88
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1901
try:
    FF_PROFILE_H264_HIGH = 100
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1902
try:
    FF_PROFILE_H264_HIGH_10 = 110
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1903
try:
    FF_PROFILE_H264_HIGH_10_INTRA = (110 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1904
try:
    FF_PROFILE_H264_MULTIVIEW_HIGH = 118
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1905
try:
    FF_PROFILE_H264_HIGH_422 = 122
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1906
try:
    FF_PROFILE_H264_HIGH_422_INTRA = (122 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1907
try:
    FF_PROFILE_H264_STEREO_HIGH = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1908
try:
    FF_PROFILE_H264_HIGH_444 = 144
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1909
try:
    FF_PROFILE_H264_HIGH_444_PREDICTIVE = 244
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1910
try:
    FF_PROFILE_H264_HIGH_444_INTRA = (244 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1911
try:
    FF_PROFILE_H264_CAVLC_444 = 44
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1913
try:
    FF_PROFILE_VC1_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1914
try:
    FF_PROFILE_VC1_MAIN = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1915
try:
    FF_PROFILE_VC1_COMPLEX = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1916
try:
    FF_PROFILE_VC1_ADVANCED = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1918
try:
    FF_PROFILE_MPEG4_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1919
try:
    FF_PROFILE_MPEG4_SIMPLE_SCALABLE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1920
try:
    FF_PROFILE_MPEG4_CORE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1921
try:
    FF_PROFILE_MPEG4_MAIN = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1922
try:
    FF_PROFILE_MPEG4_N_BIT = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1923
try:
    FF_PROFILE_MPEG4_SCALABLE_TEXTURE = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1924
try:
    FF_PROFILE_MPEG4_SIMPLE_FACE_ANIMATION = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1925
try:
    FF_PROFILE_MPEG4_BASIC_ANIMATED_TEXTURE = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1926
try:
    FF_PROFILE_MPEG4_HYBRID = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1927
try:
    FF_PROFILE_MPEG4_ADVANCED_REAL_TIME = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1928
try:
    FF_PROFILE_MPEG4_CORE_SCALABLE = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1929
try:
    FF_PROFILE_MPEG4_ADVANCED_CODING = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1930
try:
    FF_PROFILE_MPEG4_ADVANCED_CORE = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1931
try:
    FF_PROFILE_MPEG4_ADVANCED_SCALABLE_TEXTURE = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1932
try:
    FF_PROFILE_MPEG4_SIMPLE_STUDIO = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1933
try:
    FF_PROFILE_MPEG4_ADVANCED_SIMPLE = 15
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1935
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_0 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1936
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_1 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1937
try:
    FF_PROFILE_JPEG2000_CSTREAM_NO_RESTRICTION = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1938
try:
    FF_PROFILE_JPEG2000_DCINEMA_2K = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1939
try:
    FF_PROFILE_JPEG2000_DCINEMA_4K = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1941
try:
    FF_PROFILE_VP9_0 = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1942
try:
    FF_PROFILE_VP9_1 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1943
try:
    FF_PROFILE_VP9_2 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1944
try:
    FF_PROFILE_VP9_3 = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1946
try:
    FF_PROFILE_HEVC_MAIN = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1947
try:
    FF_PROFILE_HEVC_MAIN_10 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1948
try:
    FF_PROFILE_HEVC_MAIN_STILL_PICTURE = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1949
try:
    FF_PROFILE_HEVC_REXT = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1951
try:
    FF_PROFILE_VVC_MAIN_10 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1952
try:
    FF_PROFILE_VVC_MAIN_10_444 = 33
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1954
try:
    FF_PROFILE_AV1_MAIN = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1955
try:
    FF_PROFILE_AV1_HIGH = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1956
try:
    FF_PROFILE_AV1_PROFESSIONAL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1958
try:
    FF_PROFILE_MJPEG_HUFFMAN_BASELINE_DCT = 192
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1959
try:
    FF_PROFILE_MJPEG_HUFFMAN_EXTENDED_SEQUENTIAL_DCT = 193
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1960
try:
    FF_PROFILE_MJPEG_HUFFMAN_PROGRESSIVE_DCT = 194
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1961
try:
    FF_PROFILE_MJPEG_HUFFMAN_LOSSLESS = 195
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1962
try:
    FF_PROFILE_MJPEG_JPEG_LS = 247
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1964
try:
    FF_PROFILE_SBC_MSBC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1966
try:
    FF_PROFILE_PRORES_PROXY = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1967
try:
    FF_PROFILE_PRORES_LT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1968
try:
    FF_PROFILE_PRORES_STANDARD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1969
try:
    FF_PROFILE_PRORES_HQ = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1970
try:
    FF_PROFILE_PRORES_4444 = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1971
try:
    FF_PROFILE_PRORES_XQ = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1973
try:
    FF_PROFILE_ARIB_PROFILE_A = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1974
try:
    FF_PROFILE_ARIB_PROFILE_C = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1976
try:
    FF_PROFILE_KLVA_SYNC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1977
try:
    FF_PROFILE_KLVA_ASYNC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 1985
try:
    FF_LEVEL_UNKNOWN = (-99)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2118
try:
    FF_SUB_CHARENC_MODE_DO_NOTHING = (-1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2119
try:
    FF_SUB_CHARENC_MODE_AUTOMATIC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2120
try:
    FF_SUB_CHARENC_MODE_PRE_DECODER = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2121
try:
    FF_SUB_CHARENC_MODE_IGNORE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2150
try:
    FF_DEBUG_VIS_MV_P_FOR = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2151
try:
    FF_DEBUG_VIS_MV_B_FOR = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2152
try:
    FF_DEBUG_VIS_MV_B_BACK = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2184
try:
    FF_CODEC_PROPERTY_LOSSLESS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2185
try:
    FF_CODEC_PROPERTY_CLOSED_CAPTIONS = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2226
try:
    FF_SUB_TEXT_FMT_ASS = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2228
try:
    FF_SUB_TEXT_FMT_ASS_WITH_TIMINGS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2604
try:
    AV_HWACCEL_CODEC_CAP_EXPERIMENTAL = 512
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2614
try:
    AV_HWACCEL_FLAG_IGNORE_LEVEL = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2620
try:
    AV_HWACCEL_FLAG_ALLOW_HIGH_DEPTH = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2634
try:
    AV_HWACCEL_FLAG_ALLOW_PROFILE_MISMATCH = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 2685
try:
    AV_SUBTITLE_FLAG_FORCED = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3404
try:
    AV_PARSER_PTS_NB = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3411
try:
    PARSER_FLAG_COMPLETE_FRAMES = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3412
try:
    PARSER_FLAG_ONCE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3414
try:
    PARSER_FLAG_FETCHED_OFFSET = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avcodec.h: 3415
try:
    PARSER_FLAG_USE_CODEC_TS = 4096
except:
    pass

# /usr/include/libavutil/opt.h: 278
try:
    AV_OPT_FLAG_ENCODING_PARAM = 1
except:
    pass

# /usr/include/libavutil/opt.h: 279
try:
    AV_OPT_FLAG_DECODING_PARAM = 2
except:
    pass

# /usr/include/libavutil/opt.h: 280
try:
    AV_OPT_FLAG_AUDIO_PARAM = 8
except:
    pass

# /usr/include/libavutil/opt.h: 281
try:
    AV_OPT_FLAG_VIDEO_PARAM = 16
except:
    pass

# /usr/include/libavutil/opt.h: 282
try:
    AV_OPT_FLAG_SUBTITLE_PARAM = 32
except:
    pass

# /usr/include/libavutil/opt.h: 286
try:
    AV_OPT_FLAG_EXPORT = 64
except:
    pass

# /usr/include/libavutil/opt.h: 291
try:
    AV_OPT_FLAG_READONLY = 128
except:
    pass

# /usr/include/libavutil/opt.h: 292
try:
    AV_OPT_FLAG_BSF_PARAM = (1 << 8)
except:
    pass

# /usr/include/libavutil/opt.h: 293
try:
    AV_OPT_FLAG_RUNTIME_PARAM = (1 << 15)
except:
    pass

# /usr/include/libavutil/opt.h: 294
try:
    AV_OPT_FLAG_FILTERING_PARAM = (1 << 16)
except:
    pass

# /usr/include/libavutil/opt.h: 295
try:
    AV_OPT_FLAG_DEPRECATED = (1 << 17)
except:
    pass

# /usr/include/libavutil/opt.h: 296
try:
    AV_OPT_FLAG_CHILD_CONSTS = (1 << 18)
except:
    pass

# /usr/include/libavutil/opt.h: 560
try:
    AV_OPT_SEARCH_CHILDREN = (1 << 0)
except:
    pass

# /usr/include/libavutil/opt.h: 568
try:
    AV_OPT_SEARCH_FAKE_OBJ = (1 << 1)
except:
    pass

# /usr/include/libavutil/opt.h: 574
try:
    AV_OPT_ALLOW_NULL = (1 << 2)
except:
    pass

# /usr/include/libavutil/opt.h: 581
try:
    AV_OPT_MULTI_COMPONENT_RANGE = (1 << 12)
except:
    pass

# /usr/include/libavutil/opt.h: 727
def av_opt_set_int_list(obj, name, val, term, flags):
    return ((av_int_list_length (val, term)) > (INT_MAX / sizeof((val[0])))) and (AVERROR (EINVAL)) or (av_opt_set_bin (obj, name, cast(val, POINTER(c_uint8)), ((av_int_list_length (val, term)) * sizeof((val[0]))), flags))

# /usr/include/libavutil/opt.h: 859
try:
    AV_OPT_SERIALIZE_SKIP_DEFAULTS = 1
except:
    pass

# /usr/include/libavutil/opt.h: 860
try:
    AV_OPT_SERIALIZE_OPT_FLAGS_EXACT = 2
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

# /usr/include/libavfilter/version.h: 32
try:
    LIBAVFILTER_VERSION_MAJOR = 7
except:
    pass

# /usr/include/libavfilter/version.h: 33
try:
    LIBAVFILTER_VERSION_MINOR = 110
except:
    pass

# /usr/include/libavfilter/version.h: 34
try:
    LIBAVFILTER_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavfilter/version.h: 37
try:
    LIBAVFILTER_VERSION_INT = (AV_VERSION_INT (LIBAVFILTER_VERSION_MAJOR, LIBAVFILTER_VERSION_MINOR, LIBAVFILTER_VERSION_MICRO))
except:
    pass

# /usr/include/libavfilter/version.h: 43
try:
    LIBAVFILTER_BUILD = LIBAVFILTER_VERSION_INT
except:
    pass

# /usr/include/libavfilter/version.h: 54
try:
    FF_API_OLD_FILTER_OPTS_ERROR = (LIBAVFILTER_VERSION_MAJOR < 8)
except:
    pass

# /usr/include/libavfilter/version.h: 57
try:
    FF_API_LAVR_OPTS = (LIBAVFILTER_VERSION_MAJOR < 8)
except:
    pass

# /usr/include/libavfilter/version.h: 60
try:
    FF_API_FILTER_GET_SET = (LIBAVFILTER_VERSION_MAJOR < 8)
except:
    pass

# /usr/include/libavfilter/version.h: 63
try:
    FF_API_SWS_PARAM_OPTION = (LIBAVFILTER_VERSION_MAJOR < 8)
except:
    pass

# /usr/include/libavfilter/version.h: 69
try:
    FF_API_FILTER_LINK_SET_CLOSED = (LIBAVFILTER_VERSION_MAJOR < 8)
except:
    pass

# /usr/include/libavfilter/version.h: 72
try:
    FF_API_BUFFERSINK_ALLOC = (LIBAVFILTER_VERSION_MAJOR < 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 106
try:
    AVFILTER_FLAG_DYNAMIC_INPUTS = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 112
try:
    AVFILTER_FLAG_DYNAMIC_OUTPUTS = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 117
try:
    AVFILTER_FLAG_SLICE_THREADS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 126
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 134
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 139
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE = (AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC | AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 336
try:
    AVFILTER_THREAD_SLICE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 701
try:
    AVFILTER_CMD_FLAG_ONE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avfilter.h: 702
try:
    AVFILTER_CMD_FLAG_FAST = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 338
try:
    AV_ESCAPE_FLAG_WHITESPACE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 345
try:
    AV_ESCAPE_FLAG_STRICT = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 351
try:
    AV_ESCAPE_FLAG_XML_SINGLE_QUOTES = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 357
try:
    AV_ESCAPE_FLAG_XML_DOUBLE_QUOTES = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 380
try:
    AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 381
try:
    AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 382
try:
    AV_UTF8_FLAG_ACCEPT_SURROGATES = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 383
try:
    AV_UTF8_FLAG_EXCLUDE_XML_INVALID_CONTROL_CODES = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/avstring.h: 385
try:
    AV_UTF8_FLAG_ACCEPT_ALL = ((AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES | AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS) | AV_UTF8_FLAG_ACCEPT_SURROGATES)
except:
    pass

# /home/josiah/ctypesgen_test/av/base64.h: 48
def AV_BASE64_DECODE_SIZE(x):
    return ((x * 3) / 4)

# /home/josiah/ctypesgen_test/av/base64.h: 66
def AV_BASE64_SIZE(x):
    return ((((x + 2) / 3) * 4) + 1)

# /home/josiah/ctypesgen_test/av/blowfish.h: 33
try:
    AV_BF_ROUNDS = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/bprint.h: 94
try:
    AV_BPRINT_SIZE_UNLIMITED = (c_uint (ord_if_char((-1)))).value
except:
    pass

# /home/josiah/ctypesgen_test/av/bprint.h: 95
try:
    AV_BPRINT_SIZE_AUTOMATIC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/bprint.h: 96
try:
    AV_BPRINT_SIZE_COUNT_ONLY = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/bswap.h: 51
def AV_BSWAP16C(x):
    return (((x << 8) & 65280) | ((x >> 8) & 255))

# /home/josiah/ctypesgen_test/av/bswap.h: 52
def AV_BSWAP32C(x):
    return (((AV_BSWAP16C (x)) << 16) | (AV_BSWAP16C ((x >> 16))))

# /home/josiah/ctypesgen_test/av/bswap.h: 53
def AV_BSWAP64C(x):
    return (((AV_BSWAP32C (x)) << 32) | (AV_BSWAP32C ((x >> 32))))

# /home/josiah/ctypesgen_test/av/bswap.h: 95
def av_le2ne16(x):
    return x

# /home/josiah/ctypesgen_test/av/bswap.h: 96
def av_le2ne32(x):
    return x

# /home/josiah/ctypesgen_test/av/bswap.h: 97
def av_le2ne64(x):
    return x

# /home/josiah/ctypesgen_test/av/bswap.h: 99
def AV_LE2NEC(s, x):
    return x

# /home/josiah/ctypesgen_test/av/bswap.h: 105
def AV_LE2NE16C(x):
    return (AV_LE2NEC (16, x))

# /home/josiah/ctypesgen_test/av/bswap.h: 106
def AV_LE2NE32C(x):
    return (AV_LE2NEC (32, x))

# /home/josiah/ctypesgen_test/av/bswap.h: 107
def AV_LE2NE64C(x):
    return (AV_LE2NEC (64, x))

# /home/josiah/ctypesgen_test/av/buffersink.h: 89
try:
    AV_BUFFERSINK_FLAG_PEEK = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/buffersink.h: 96
try:
    AV_BUFFERSINK_FLAG_NO_REQUEST = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/dirac.h: 45
try:
    MAX_DWT_LEVELS = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/dv_profile.h: 30
try:
    DV_PROFILE_BYTES = (6 * 80)
except:
    pass

# /home/josiah/ctypesgen_test/av/ffversion.h: 4
try:
    FFMPEG_VERSION = 'n4.4'
except:
    pass

# /home/josiah/ctypesgen_test/av/hash.h: 158
try:
    AV_HASH_MAX_SIZE = 64
except:
    pass

# /usr/include/vdpau/vdpau.h: 806
try:
    VDP_TRUE = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 808
try:
    VDP_FALSE = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 833
try:
    VDP_INVALID_HANDLE = 4294967295
except:
    pass

# /usr/include/vdpau/vdpau.h: 849
try:
    VDP_CHROMA_TYPE_420 = (VdpChromaType (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 858
try:
    VDP_CHROMA_TYPE_422 = (VdpChromaType (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 867
try:
    VDP_CHROMA_TYPE_444 = (VdpChromaType (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 873
try:
    VDP_CHROMA_TYPE_420_FIELD = (VdpChromaType (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 878
try:
    VDP_CHROMA_TYPE_422_FIELD = (VdpChromaType (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 883
try:
    VDP_CHROMA_TYPE_444_FIELD = (VdpChromaType (ord_if_char(5))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 889
try:
    VDP_CHROMA_TYPE_420_FRAME = (VdpChromaType (ord_if_char(6))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 894
try:
    VDP_CHROMA_TYPE_422_FRAME = (VdpChromaType (ord_if_char(7))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 899
try:
    VDP_CHROMA_TYPE_444_FRAME = (VdpChromaType (ord_if_char(8))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 908
try:
    VDP_CHROMA_TYPE_420_16 = (VdpChromaType (ord_if_char(9))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 917
try:
    VDP_CHROMA_TYPE_422_16 = (VdpChromaType (ord_if_char(10))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 926
try:
    VDP_CHROMA_TYPE_444_16 = (VdpChromaType (ord_if_char(11))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 932
try:
    VDP_CHROMA_TYPE_420_FIELD_16 = (VdpChromaType (ord_if_char(12))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 937
try:
    VDP_CHROMA_TYPE_422_FIELD_16 = (VdpChromaType (ord_if_char(13))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 942
try:
    VDP_CHROMA_TYPE_444_FIELD_16 = (VdpChromaType (ord_if_char(14))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 948
try:
    VDP_CHROMA_TYPE_420_FRAME_16 = (VdpChromaType (ord_if_char(15))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 953
try:
    VDP_CHROMA_TYPE_422_FRAME_16 = (VdpChromaType (ord_if_char(16))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 958
try:
    VDP_CHROMA_TYPE_444_FRAME_16 = (VdpChromaType (ord_if_char(17))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 978
try:
    VDP_YCBCR_FORMAT_NV12 = (VdpYCbCrFormat (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 990
try:
    VDP_YCBCR_FORMAT_YV12 = (VdpYCbCrFormat (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1004
try:
    VDP_YCBCR_FORMAT_UYVY = (VdpYCbCrFormat (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1018
try:
    VDP_YCBCR_FORMAT_YUYV = (VdpYCbCrFormat (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1031
try:
    VDP_YCBCR_FORMAT_Y8U8V8A8 = (VdpYCbCrFormat (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1044
try:
    VDP_YCBCR_FORMAT_V8U8Y8A8 = (VdpYCbCrFormat (ord_if_char(5))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1058
try:
    VDP_YCBCR_FORMAT_Y_UV_444 = (VdpYCbCrFormat (ord_if_char(6))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1070
try:
    VDP_YCBCR_FORMAT_Y_U_V_444 = (VdpYCbCrFormat (ord_if_char(7))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1088
try:
    VDP_YCBCR_FORMAT_P010 = (VdpYCbCrFormat (ord_if_char(8))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1102
try:
    VDP_YCBCR_FORMAT_P016 = (VdpYCbCrFormat (ord_if_char(9))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1114
try:
    VDP_YCBCR_FORMAT_Y_U_V_444_16 = (VdpYCbCrFormat (ord_if_char(11))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1133
try:
    VDP_RGBA_FORMAT_B8G8R8A8 = (VdpRGBAFormat (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1146
try:
    VDP_RGBA_FORMAT_R8G8B8A8 = (VdpRGBAFormat (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1159
try:
    VDP_RGBA_FORMAT_R10G10B10A2 = (VdpRGBAFormat (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1172
try:
    VDP_RGBA_FORMAT_B10G10R10A2 = (VdpRGBAFormat (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1183
try:
    VDP_RGBA_FORMAT_A8 = (VdpRGBAFormat (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1201
try:
    VDP_INDEXED_FORMAT_A4I4 = (VdpIndexedFormat (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1213
try:
    VDP_INDEXED_FORMAT_I4A4 = (VdpIndexedFormat (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1225
try:
    VDP_INDEXED_FORMAT_A8I8 = (VdpIndexedFormat (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1237
try:
    VDP_INDEXED_FORMAT_I8A8 = (VdpIndexedFormat (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1472
try:
    VDPAU_INTERFACE_VERSION = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 1485
try:
    VDPAU_VERSION = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 1589
try:
    VDP_PROCAMP_VERSION = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 1635
try:
    VDP_COLOR_STANDARD_ITUR_BT_601 = (VdpColorStandard (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1637
try:
    VDP_COLOR_STANDARD_ITUR_BT_709 = (VdpColorStandard (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1639
try:
    VDP_COLOR_STANDARD_SMPTE_240M = (VdpColorStandard (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 1911
try:
    VDP_COLOR_TABLE_FORMAT_B8G8R8X8 = (VdpColorTableFormat (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2362
try:
    VDP_OUTPUT_SURFACE_RENDER_BLEND_STATE_VERSION = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2401
try:
    VDP_OUTPUT_SURFACE_RENDER_ROTATE_0 = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2408
try:
    VDP_OUTPUT_SURFACE_RENDER_ROTATE_90 = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2415
try:
    VDP_OUTPUT_SURFACE_RENDER_ROTATE_180 = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2422
try:
    VDP_OUTPUT_SURFACE_RENDER_ROTATE_270 = 3
except:
    pass

# /usr/include/vdpau/vdpau.h: 2431
try:
    VDP_OUTPUT_SURFACE_RENDER_COLOR_PER_VERTEX = (1 << 2)
except:
    pass

# /usr/include/vdpau/vdpau.h: 2616
try:
    VDP_DECODER_PROFILE_MPEG1 = (VdpDecoderProfile (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2618
try:
    VDP_DECODER_PROFILE_MPEG2_SIMPLE = (VdpDecoderProfile (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2620
try:
    VDP_DECODER_PROFILE_MPEG2_MAIN = (VdpDecoderProfile (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2623
try:
    VDP_DECODER_PROFILE_H264_BASELINE = (VdpDecoderProfile (ord_if_char(6))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2625
try:
    VDP_DECODER_PROFILE_H264_MAIN = (VdpDecoderProfile (ord_if_char(7))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2627
try:
    VDP_DECODER_PROFILE_H264_HIGH = (VdpDecoderProfile (ord_if_char(8))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2629
try:
    VDP_DECODER_PROFILE_VC1_SIMPLE = (VdpDecoderProfile (ord_if_char(9))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2631
try:
    VDP_DECODER_PROFILE_VC1_MAIN = (VdpDecoderProfile (ord_if_char(10))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2633
try:
    VDP_DECODER_PROFILE_VC1_ADVANCED = (VdpDecoderProfile (ord_if_char(11))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2635
try:
    VDP_DECODER_PROFILE_MPEG4_PART2_SP = (VdpDecoderProfile (ord_if_char(12))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2637
try:
    VDP_DECODER_PROFILE_MPEG4_PART2_ASP = (VdpDecoderProfile (ord_if_char(13))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2639
try:
    VDP_DECODER_PROFILE_DIVX4_QMOBILE = (VdpDecoderProfile (ord_if_char(14))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2641
try:
    VDP_DECODER_PROFILE_DIVX4_MOBILE = (VdpDecoderProfile (ord_if_char(15))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2643
try:
    VDP_DECODER_PROFILE_DIVX4_HOME_THEATER = (VdpDecoderProfile (ord_if_char(16))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2645
try:
    VDP_DECODER_PROFILE_DIVX4_HD_1080P = (VdpDecoderProfile (ord_if_char(17))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2647
try:
    VDP_DECODER_PROFILE_DIVX5_QMOBILE = (VdpDecoderProfile (ord_if_char(18))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2649
try:
    VDP_DECODER_PROFILE_DIVX5_MOBILE = (VdpDecoderProfile (ord_if_char(19))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2651
try:
    VDP_DECODER_PROFILE_DIVX5_HOME_THEATER = (VdpDecoderProfile (ord_if_char(20))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2653
try:
    VDP_DECODER_PROFILE_DIVX5_HD_1080P = (VdpDecoderProfile (ord_if_char(21))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2655
try:
    VDP_DECODER_PROFILE_H264_CONSTRAINED_BASELINE = (VdpDecoderProfile (ord_if_char(22))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2657
try:
    VDP_DECODER_PROFILE_H264_EXTENDED = (VdpDecoderProfile (ord_if_char(23))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2659
try:
    VDP_DECODER_PROFILE_H264_PROGRESSIVE_HIGH = (VdpDecoderProfile (ord_if_char(24))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2661
try:
    VDP_DECODER_PROFILE_H264_CONSTRAINED_HIGH = (VdpDecoderProfile (ord_if_char(25))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2664
try:
    VDP_DECODER_PROFILE_H264_HIGH_444_PREDICTIVE = (VdpDecoderProfile (ord_if_char(26))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2666
try:
    VDP_DECODER_PROFILE_VP9_PROFILE_0 = (VdpDecoderProfile (ord_if_char(27))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2668
try:
    VDP_DECODER_PROFILE_VP9_PROFILE_1 = (VdpDecoderProfile (ord_if_char(28))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2670
try:
    VDP_DECODER_PROFILE_VP9_PROFILE_2 = (VdpDecoderProfile (ord_if_char(29))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2672
try:
    VDP_DECODER_PROFILE_VP9_PROFILE_3 = (VdpDecoderProfile (ord_if_char(30))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2675
try:
    VDP_DECODER_PROFILE_HEVC_MAIN = (VdpDecoderProfile (ord_if_char(100))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2677
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_10 = (VdpDecoderProfile (ord_if_char(101))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2679
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_STILL = (VdpDecoderProfile (ord_if_char(102))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2681
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_12 = (VdpDecoderProfile (ord_if_char(103))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2683
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_444 = (VdpDecoderProfile (ord_if_char(104))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2685
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_444_10 = (VdpDecoderProfile (ord_if_char(105))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2687
try:
    VDP_DECODER_PROFILE_HEVC_MAIN_444_12 = (VdpDecoderProfile (ord_if_char(106))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 2690
try:
    VDP_DECODER_LEVEL_MPEG1_NA = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2693
try:
    VDP_DECODER_LEVEL_MPEG2_LL = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2695
try:
    VDP_DECODER_LEVEL_MPEG2_ML = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2697
try:
    VDP_DECODER_LEVEL_MPEG2_HL14 = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2699
try:
    VDP_DECODER_LEVEL_MPEG2_HL = 3
except:
    pass

# /usr/include/vdpau/vdpau.h: 2702
try:
    VDP_DECODER_LEVEL_H264_1 = 10
except:
    pass

# /usr/include/vdpau/vdpau.h: 2704
try:
    VDP_DECODER_LEVEL_H264_1b = 9
except:
    pass

# /usr/include/vdpau/vdpau.h: 2706
try:
    VDP_DECODER_LEVEL_H264_1_1 = 11
except:
    pass

# /usr/include/vdpau/vdpau.h: 2708
try:
    VDP_DECODER_LEVEL_H264_1_2 = 12
except:
    pass

# /usr/include/vdpau/vdpau.h: 2710
try:
    VDP_DECODER_LEVEL_H264_1_3 = 13
except:
    pass

# /usr/include/vdpau/vdpau.h: 2712
try:
    VDP_DECODER_LEVEL_H264_2 = 20
except:
    pass

# /usr/include/vdpau/vdpau.h: 2714
try:
    VDP_DECODER_LEVEL_H264_2_1 = 21
except:
    pass

# /usr/include/vdpau/vdpau.h: 2716
try:
    VDP_DECODER_LEVEL_H264_2_2 = 22
except:
    pass

# /usr/include/vdpau/vdpau.h: 2718
try:
    VDP_DECODER_LEVEL_H264_3 = 30
except:
    pass

# /usr/include/vdpau/vdpau.h: 2720
try:
    VDP_DECODER_LEVEL_H264_3_1 = 31
except:
    pass

# /usr/include/vdpau/vdpau.h: 2722
try:
    VDP_DECODER_LEVEL_H264_3_2 = 32
except:
    pass

# /usr/include/vdpau/vdpau.h: 2724
try:
    VDP_DECODER_LEVEL_H264_4 = 40
except:
    pass

# /usr/include/vdpau/vdpau.h: 2726
try:
    VDP_DECODER_LEVEL_H264_4_1 = 41
except:
    pass

# /usr/include/vdpau/vdpau.h: 2728
try:
    VDP_DECODER_LEVEL_H264_4_2 = 42
except:
    pass

# /usr/include/vdpau/vdpau.h: 2730
try:
    VDP_DECODER_LEVEL_H264_5 = 50
except:
    pass

# /usr/include/vdpau/vdpau.h: 2732
try:
    VDP_DECODER_LEVEL_H264_5_1 = 51
except:
    pass

# /usr/include/vdpau/vdpau.h: 2735
try:
    VDP_DECODER_LEVEL_VC1_SIMPLE_LOW = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2737
try:
    VDP_DECODER_LEVEL_VC1_SIMPLE_MEDIUM = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2740
try:
    VDP_DECODER_LEVEL_VC1_MAIN_LOW = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2742
try:
    VDP_DECODER_LEVEL_VC1_MAIN_MEDIUM = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2744
try:
    VDP_DECODER_LEVEL_VC1_MAIN_HIGH = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2747
try:
    VDP_DECODER_LEVEL_VC1_ADVANCED_L0 = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2749
try:
    VDP_DECODER_LEVEL_VC1_ADVANCED_L1 = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2751
try:
    VDP_DECODER_LEVEL_VC1_ADVANCED_L2 = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2753
try:
    VDP_DECODER_LEVEL_VC1_ADVANCED_L3 = 3
except:
    pass

# /usr/include/vdpau/vdpau.h: 2755
try:
    VDP_DECODER_LEVEL_VC1_ADVANCED_L4 = 4
except:
    pass

# /usr/include/vdpau/vdpau.h: 2758
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_SP_L0 = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2760
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_SP_L1 = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2762
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_SP_L2 = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2764
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_SP_L3 = 3
except:
    pass

# /usr/include/vdpau/vdpau.h: 2767
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L0 = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2769
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L1 = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2771
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L2 = 2
except:
    pass

# /usr/include/vdpau/vdpau.h: 2773
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L3 = 3
except:
    pass

# /usr/include/vdpau/vdpau.h: 2775
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L4 = 4
except:
    pass

# /usr/include/vdpau/vdpau.h: 2777
try:
    VDP_DECODER_LEVEL_MPEG4_PART2_ASP_L5 = 5
except:
    pass

# /usr/include/vdpau/vdpau.h: 2780
try:
    VDP_DECODER_LEVEL_DIVX_NA = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 2783
try:
    VDP_DECODER_LEVEL_VP9_L1 = 1
except:
    pass

# /usr/include/vdpau/vdpau.h: 2791
try:
    VDP_DECODER_LEVEL_HEVC_1 = 30
except:
    pass

# /usr/include/vdpau/vdpau.h: 2793
try:
    VDP_DECODER_LEVEL_HEVC_2 = 60
except:
    pass

# /usr/include/vdpau/vdpau.h: 2795
try:
    VDP_DECODER_LEVEL_HEVC_2_1 = 63
except:
    pass

# /usr/include/vdpau/vdpau.h: 2797
try:
    VDP_DECODER_LEVEL_HEVC_3 = 90
except:
    pass

# /usr/include/vdpau/vdpau.h: 2799
try:
    VDP_DECODER_LEVEL_HEVC_3_1 = 93
except:
    pass

# /usr/include/vdpau/vdpau.h: 2801
try:
    VDP_DECODER_LEVEL_HEVC_4 = 120
except:
    pass

# /usr/include/vdpau/vdpau.h: 2803
try:
    VDP_DECODER_LEVEL_HEVC_4_1 = 123
except:
    pass

# /usr/include/vdpau/vdpau.h: 2805
try:
    VDP_DECODER_LEVEL_HEVC_5 = 150
except:
    pass

# /usr/include/vdpau/vdpau.h: 2807
try:
    VDP_DECODER_LEVEL_HEVC_5_1 = 153
except:
    pass

# /usr/include/vdpau/vdpau.h: 2809
try:
    VDP_DECODER_LEVEL_HEVC_5_2 = 156
except:
    pass

# /usr/include/vdpau/vdpau.h: 2811
try:
    VDP_DECODER_LEVEL_HEVC_6 = 180
except:
    pass

# /usr/include/vdpau/vdpau.h: 2813
try:
    VDP_DECODER_LEVEL_HEVC_6_1 = 183
except:
    pass

# /usr/include/vdpau/vdpau.h: 2815
try:
    VDP_DECODER_LEVEL_HEVC_6_2 = 186
except:
    pass

# /usr/include/vdpau/vdpau.h: 2946
try:
    VDP_BITSTREAM_BUFFER_VERSION = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 3782
try:
    VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL = (VdpVideoMixerFeature (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3795
try:
    VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL_SPATIAL = (VdpVideoMixerFeature (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3804
try:
    VDP_VIDEO_MIXER_FEATURE_INVERSE_TELECINE = (VdpVideoMixerFeature (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3812
try:
    VDP_VIDEO_MIXER_FEATURE_NOISE_REDUCTION = (VdpVideoMixerFeature (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3820
try:
    VDP_VIDEO_MIXER_FEATURE_SHARPNESS = (VdpVideoMixerFeature (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3833
try:
    VDP_VIDEO_MIXER_FEATURE_LUMA_KEY = (VdpVideoMixerFeature (ord_if_char(5))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3855
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L1 = (VdpVideoMixerFeature (ord_if_char(11))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3862
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L2 = (VdpVideoMixerFeature (ord_if_char(12))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3869
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L3 = (VdpVideoMixerFeature (ord_if_char(13))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3876
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L4 = (VdpVideoMixerFeature (ord_if_char(14))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3883
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L5 = (VdpVideoMixerFeature (ord_if_char(15))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3890
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L6 = (VdpVideoMixerFeature (ord_if_char(16))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3897
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L7 = (VdpVideoMixerFeature (ord_if_char(17))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3904
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L8 = (VdpVideoMixerFeature (ord_if_char(18))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3911
try:
    VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L9 = (VdpVideoMixerFeature (ord_if_char(19))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3939
try:
    VDP_VIDEO_MIXER_PARAMETER_VIDEO_SURFACE_WIDTH = (VdpVideoMixerParameter (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3952
try:
    VDP_VIDEO_MIXER_PARAMETER_VIDEO_SURFACE_HEIGHT = (VdpVideoMixerParameter (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3966
try:
    VDP_VIDEO_MIXER_PARAMETER_CHROMA_TYPE = (VdpVideoMixerParameter (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 3985
try:
    VDP_VIDEO_MIXER_PARAMETER_LAYERS = (VdpVideoMixerParameter (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4014
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_BACKGROUND_COLOR = (VdpVideoMixerAttribute (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4042
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_CSC_MATRIX = (VdpVideoMixerAttribute (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4055
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_NOISE_REDUCTION_LEVEL = (VdpVideoMixerAttribute (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4071
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_SHARPNESS_LEVEL = (VdpVideoMixerAttribute (ord_if_char(3))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4083
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_LUMA_KEY_MIN_LUMA = (VdpVideoMixerAttribute (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4095
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_LUMA_KEY_MAX_LUMA = (VdpVideoMixerAttribute (ord_if_char(5))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4110
try:
    VDP_VIDEO_MIXER_ATTRIBUTE_SKIP_CHROMA_DEINTERLACE = (VdpVideoMixerAttribute (ord_if_char(6))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4377
try:
    VDP_LAYER_VERSION = 0
except:
    pass

# /usr/include/vdpau/vdpau.h: 4830
try:
    VDP_FUNC_ID_GET_ERROR_STRING = (VdpFuncId (ord_if_char(0))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4832
try:
    VDP_FUNC_ID_GET_PROC_ADDRESS = (VdpFuncId (ord_if_char(1))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4834
try:
    VDP_FUNC_ID_GET_API_VERSION = (VdpFuncId (ord_if_char(2))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4836
try:
    VDP_FUNC_ID_GET_INFORMATION_STRING = (VdpFuncId (ord_if_char(4))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4838
try:
    VDP_FUNC_ID_DEVICE_DESTROY = (VdpFuncId (ord_if_char(5))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4840
try:
    VDP_FUNC_ID_GENERATE_CSC_MATRIX = (VdpFuncId (ord_if_char(6))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4842
try:
    VDP_FUNC_ID_VIDEO_SURFACE_QUERY_CAPABILITIES = (VdpFuncId (ord_if_char(7))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4844
try:
    VDP_FUNC_ID_VIDEO_SURFACE_QUERY_GET_PUT_BITS_Y_CB_CR_CAPABILITIES = (VdpFuncId (ord_if_char(8))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4846
try:
    VDP_FUNC_ID_VIDEO_SURFACE_CREATE = (VdpFuncId (ord_if_char(9))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4848
try:
    VDP_FUNC_ID_VIDEO_SURFACE_DESTROY = (VdpFuncId (ord_if_char(10))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4850
try:
    VDP_FUNC_ID_VIDEO_SURFACE_GET_PARAMETERS = (VdpFuncId (ord_if_char(11))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4852
try:
    VDP_FUNC_ID_VIDEO_SURFACE_GET_BITS_Y_CB_CR = (VdpFuncId (ord_if_char(12))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4854
try:
    VDP_FUNC_ID_VIDEO_SURFACE_PUT_BITS_Y_CB_CR = (VdpFuncId (ord_if_char(13))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4856
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_QUERY_CAPABILITIES = (VdpFuncId (ord_if_char(14))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4858
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_QUERY_GET_PUT_BITS_NATIVE_CAPABILITIES = (VdpFuncId (ord_if_char(15))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4860
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_QUERY_PUT_BITS_INDEXED_CAPABILITIES = (VdpFuncId (ord_if_char(16))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4862
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_QUERY_PUT_BITS_Y_CB_CR_CAPABILITIES = (VdpFuncId (ord_if_char(17))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4864
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_CREATE = (VdpFuncId (ord_if_char(18))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4866
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_DESTROY = (VdpFuncId (ord_if_char(19))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4868
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_GET_PARAMETERS = (VdpFuncId (ord_if_char(20))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4870
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_GET_BITS_NATIVE = (VdpFuncId (ord_if_char(21))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4872
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_PUT_BITS_NATIVE = (VdpFuncId (ord_if_char(22))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4874
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_PUT_BITS_INDEXED = (VdpFuncId (ord_if_char(23))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4876
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_PUT_BITS_Y_CB_CR = (VdpFuncId (ord_if_char(24))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4878
try:
    VDP_FUNC_ID_BITMAP_SURFACE_QUERY_CAPABILITIES = (VdpFuncId (ord_if_char(25))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4880
try:
    VDP_FUNC_ID_BITMAP_SURFACE_CREATE = (VdpFuncId (ord_if_char(26))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4882
try:
    VDP_FUNC_ID_BITMAP_SURFACE_DESTROY = (VdpFuncId (ord_if_char(27))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4884
try:
    VDP_FUNC_ID_BITMAP_SURFACE_GET_PARAMETERS = (VdpFuncId (ord_if_char(28))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4886
try:
    VDP_FUNC_ID_BITMAP_SURFACE_PUT_BITS_NATIVE = (VdpFuncId (ord_if_char(29))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4888
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_RENDER_OUTPUT_SURFACE = (VdpFuncId (ord_if_char(33))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4890
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_RENDER_BITMAP_SURFACE = (VdpFuncId (ord_if_char(34))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4892
try:
    VDP_FUNC_ID_OUTPUT_SURFACE_RENDER_VIDEO_SURFACE_LUMA = (VdpFuncId (ord_if_char(35))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4894
try:
    VDP_FUNC_ID_DECODER_QUERY_CAPABILITIES = (VdpFuncId (ord_if_char(36))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4896
try:
    VDP_FUNC_ID_DECODER_CREATE = (VdpFuncId (ord_if_char(37))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4898
try:
    VDP_FUNC_ID_DECODER_DESTROY = (VdpFuncId (ord_if_char(38))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4900
try:
    VDP_FUNC_ID_DECODER_GET_PARAMETERS = (VdpFuncId (ord_if_char(39))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4902
try:
    VDP_FUNC_ID_DECODER_RENDER = (VdpFuncId (ord_if_char(40))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4904
try:
    VDP_FUNC_ID_VIDEO_MIXER_QUERY_FEATURE_SUPPORT = (VdpFuncId (ord_if_char(41))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4906
try:
    VDP_FUNC_ID_VIDEO_MIXER_QUERY_PARAMETER_SUPPORT = (VdpFuncId (ord_if_char(42))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4908
try:
    VDP_FUNC_ID_VIDEO_MIXER_QUERY_ATTRIBUTE_SUPPORT = (VdpFuncId (ord_if_char(43))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4910
try:
    VDP_FUNC_ID_VIDEO_MIXER_QUERY_PARAMETER_VALUE_RANGE = (VdpFuncId (ord_if_char(44))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4912
try:
    VDP_FUNC_ID_VIDEO_MIXER_QUERY_ATTRIBUTE_VALUE_RANGE = (VdpFuncId (ord_if_char(45))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4914
try:
    VDP_FUNC_ID_VIDEO_MIXER_CREATE = (VdpFuncId (ord_if_char(46))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4916
try:
    VDP_FUNC_ID_VIDEO_MIXER_SET_FEATURE_ENABLES = (VdpFuncId (ord_if_char(47))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4918
try:
    VDP_FUNC_ID_VIDEO_MIXER_SET_ATTRIBUTE_VALUES = (VdpFuncId (ord_if_char(48))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4920
try:
    VDP_FUNC_ID_VIDEO_MIXER_GET_FEATURE_SUPPORT = (VdpFuncId (ord_if_char(49))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4922
try:
    VDP_FUNC_ID_VIDEO_MIXER_GET_FEATURE_ENABLES = (VdpFuncId (ord_if_char(50))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4924
try:
    VDP_FUNC_ID_VIDEO_MIXER_GET_PARAMETER_VALUES = (VdpFuncId (ord_if_char(51))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4926
try:
    VDP_FUNC_ID_VIDEO_MIXER_GET_ATTRIBUTE_VALUES = (VdpFuncId (ord_if_char(52))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4928
try:
    VDP_FUNC_ID_VIDEO_MIXER_DESTROY = (VdpFuncId (ord_if_char(53))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4930
try:
    VDP_FUNC_ID_VIDEO_MIXER_RENDER = (VdpFuncId (ord_if_char(54))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4932
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_TARGET_DESTROY = (VdpFuncId (ord_if_char(55))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4934
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_CREATE = (VdpFuncId (ord_if_char(56))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4936
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_DESTROY = (VdpFuncId (ord_if_char(57))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4938
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_SET_BACKGROUND_COLOR = (VdpFuncId (ord_if_char(58))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4940
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_GET_BACKGROUND_COLOR = (VdpFuncId (ord_if_char(59))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4942
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_GET_TIME = (VdpFuncId (ord_if_char(62))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4944
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_DISPLAY = (VdpFuncId (ord_if_char(63))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4946
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_BLOCK_UNTIL_SURFACE_IDLE = (VdpFuncId (ord_if_char(64))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4948
try:
    VDP_FUNC_ID_PRESENTATION_QUEUE_QUERY_SURFACE_STATUS = (VdpFuncId (ord_if_char(65))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4950
try:
    VDP_FUNC_ID_PREEMPTION_CALLBACK_REGISTER = (VdpFuncId (ord_if_char(66))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4952
try:
    VDP_FUNC_ID_DECODER_QUERY_CAPABILITY = (VdpFuncId (ord_if_char(67))).value
except:
    pass

# /usr/include/vdpau/vdpau.h: 4954
try:
    VDP_FUNC_ID_BASE_WINSYS = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 128
try:
    AV_PIX_FMT_FLAG_BE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 132
try:
    AV_PIX_FMT_FLAG_PAL = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 136
try:
    AV_PIX_FMT_FLAG_BITSTREAM = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 140
try:
    AV_PIX_FMT_FLAG_HWACCEL = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 144
try:
    AV_PIX_FMT_FLAG_PLANAR = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 148
try:
    AV_PIX_FMT_FLAG_RGB = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 167
try:
    AV_PIX_FMT_FLAG_PSEUDOPAL = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 179
try:
    AV_PIX_FMT_FLAG_ALPHA = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 184
try:
    AV_PIX_FMT_FLAG_BAYER = (1 << 8)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 190
try:
    AV_PIX_FMT_FLAG_FLOAT = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 392
try:
    FF_LOSS_RESOLUTION = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 393
try:
    FF_LOSS_DEPTH = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 394
try:
    FF_LOSS_COLORSPACE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 395
try:
    FF_LOSS_ALPHA = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 396
try:
    FF_LOSS_COLORQUANT = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/pixdesc.h: 397
try:
    FF_LOSS_CHROMA = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 395
def AV_RB8(x):
    return (cast(x, POINTER(c_uint8)) [0])

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 398
def AV_RL8(x):
    return (AV_RB8 (x))

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 444
def AV_RB24(x):
    return ((((cast(x, POINTER(c_uint8)) [0]) << 16) | ((cast(x, POINTER(c_uint8)) [1]) << 8)) | (cast(x, POINTER(c_uint8)) [2]))

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 458
def AV_RL24(x):
    return ((((cast(x, POINTER(c_uint8)) [2]) << 16) | ((cast(x, POINTER(c_uint8)) [1]) << 8)) | (cast(x, POINTER(c_uint8)) [0]))

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 472
def AV_RB48(x):
    return (((((((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [0])))).value << 40) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [1])))).value << 32)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [2])))).value << 24)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [3])))).value << 16)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [4])))).value << 8)) | (c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [5])))).value)

# /home/josiah/ctypesgen_test/av/intreadwrite.h: 493
def AV_RL48(x):
    return (((((((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [5])))).value << 40) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [4])))).value << 32)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [3])))).value << 24)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [2])))).value << 16)) | ((c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [1])))).value << 8)) | (c_uint64 (ord_if_char((cast(x, POINTER(c_uint8)) [0])))).value)

# /home/josiah/ctypesgen_test/av/lzo.h: 37
try:
    AV_LZO_INPUT_DEPLETED = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/lzo.h: 39
try:
    AV_LZO_OUTPUT_FULL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/lzo.h: 41
try:
    AV_LZO_INVALID_BACKPTR = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/lzo.h: 43
try:
    AV_LZO_ERROR = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/lzo.h: 46
try:
    AV_LZO_INPUT_PADDING = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/lzo.h: 47
try:
    AV_LZO_OUTPUT_PADDING = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 32
try:
    ROM1394_HEADER = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 33
try:
    ROM1394_BUS_ID = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 34
try:
    ROM1394_BUS_OPTIONS = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 35
try:
    ROM1394_GUID_HI = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 36
try:
    ROM1394_GUID_LO = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/rom1394.h: 37
try:
    ROM1394_ROOT_DIRECTORY = 20
except:
    pass

# /home/josiah/ctypesgen_test/av/stereo3d.h: 167
try:
    AV_STEREO3D_FLAG_INVERT = (1 << 0)
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

# /home/josiah/ctypesgen_test/av/swresample.h: 136
try:
    SWR_FLAG_RESAMPLE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 58
try:
    SWS_FAST_BILINEAR = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 59
try:
    SWS_BILINEAR = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 60
try:
    SWS_BICUBIC = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 61
try:
    SWS_X = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 62
try:
    SWS_POINT = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 63
try:
    SWS_AREA = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 64
try:
    SWS_BICUBLIN = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 65
try:
    SWS_GAUSS = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 66
try:
    SWS_SINC = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 67
try:
    SWS_LANCZOS = 512
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 68
try:
    SWS_SPLINE = 1024
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 70
try:
    SWS_SRC_V_CHR_DROP_MASK = 196608
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 71
try:
    SWS_SRC_V_CHR_DROP_SHIFT = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 73
try:
    SWS_PARAM_DEFAULT = 123456
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 75
try:
    SWS_PRINT_INFO = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 79
try:
    SWS_FULL_CHR_H_INT = 8192
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 81
try:
    SWS_FULL_CHR_H_INP = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 82
try:
    SWS_DIRECT_BGR = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 83
try:
    SWS_ACCURATE_RND = 262144
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 84
try:
    SWS_BITEXACT = 524288
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 85
try:
    SWS_ERROR_DIFFUSION = 8388608
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 87
try:
    SWS_MAX_REDUCE_CUTOFF = 0.002
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 89
try:
    SWS_CS_ITU709 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 90
try:
    SWS_CS_FCC = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 91
try:
    SWS_CS_ITU601 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 92
try:
    SWS_CS_ITU624 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 93
try:
    SWS_CS_SMPTE170M = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 94
try:
    SWS_CS_SMPTE240M = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 95
try:
    SWS_CS_DEFAULT = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/swscale.h: 96
try:
    SWS_CS_BT2020 = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/timecode.h: 33
try:
    AV_TIMECODE_STR_SIZE = 23
except:
    pass

# /home/josiah/ctypesgen_test/av/timestamp.h: 33
try:
    AV_TS_MAX_STRING_SIZE = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 44
try:
    VORBIS_FLAG_HEADER = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 45
try:
    VORBIS_FLAG_COMMENT = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 46
try:
    VORBIS_FLAG_SETUP = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/xvmc.h: 43
try:
    AV_XVMC_ID = 499585472
except:
    pass

AVAESCTR = struct_AVAESCTR# /home/josiah/ctypesgen_test/av/aes_ctr.h: 33

AVAES = struct_AVAES# /home/josiah/ctypesgen_test/av/aes.h: 37

AVRational = struct_AVRational# /home/josiah/ctypesgen_test/av/rational.h: 61

av_intfloat32 = union_av_intfloat32# /home/josiah/ctypesgen_test/av/intfloat.h: 27

av_intfloat64 = union_av_intfloat64# /home/josiah/ctypesgen_test/av/intfloat.h: 32

AVOptionRanges = struct_AVOptionRanges# /usr/include/libavutil/opt.h: 333

AVOption = struct_AVOption# /usr/include/libavutil/opt.h: 248

AVClass = struct_AVClass# /home/josiah/ctypesgen_test/av/log.h: 67

AVFifoBuffer = struct_AVFifoBuffer# /home/josiah/ctypesgen_test/av/fifo.h: 35

AVAudioFifo = struct_AVAudioFifo# /home/josiah/ctypesgen_test/av/audio_fifo.h: 49

sigevent = struct_sigevent# /usr/include/time.h: 49

avc1394_command_response = struct_avc1394_command_response# /home/josiah/ctypesgen_test/av/avc1394.h: 491

AVBuffer = struct_AVBuffer# /usr/include/libavutil/buffer.h: 76

AVBufferRef = struct_AVBufferRef# /usr/include/libavutil/buffer.h: 101

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 277

AVBPrint = struct_AVBPrint# /home/josiah/ctypesgen_test/av/bprint.h: 82

AVDictionaryEntry = struct_AVDictionaryEntry# /usr/include/libavutil/dict.h: 84

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 86

AVFrameSideData = struct_AVFrameSideData# /usr/include/libavutil/frame.h: 230

AVRegionOfInterest = struct_AVRegionOfInterest# /usr/include/libavutil/frame.h: 286

AVFrame = struct_AVFrame# /usr/include/libavutil/frame.h: 698

AVHWDeviceInternal = struct_AVHWDeviceInternal# /usr/include/libavutil/hwcontext.h: 42

AVHWDeviceContext = struct_AVHWDeviceContext# /usr/include/libavutil/hwcontext.h: 61

AVHWFramesInternal = struct_AVHWFramesInternal# /usr/include/libavutil/hwcontext.h: 112

AVHWFramesContext = struct_AVHWFramesContext# /usr/include/libavutil/hwcontext.h: 124

AVHWFramesConstraints = struct_AVHWFramesConstraints# /usr/include/libavutil/hwcontext.h: 480

AVCodecParameters = struct_AVCodecParameters# /home/josiah/ctypesgen_test/av/codec_par.h: 201

AVPacketSideData = struct_AVPacketSideData# /home/josiah/ctypesgen_test/av/packet.h: 314

AVPacket = struct_AVPacket# /home/josiah/ctypesgen_test/av/packet.h: 400

AVPacketList = struct_AVPacketList# /home/josiah/ctypesgen_test/av/packet.h: 404

AVBSFInternal = struct_AVBSFInternal# /home/josiah/ctypesgen_test/av/bsf.h: 37

AVBitStreamFilter = struct_AVBitStreamFilter# /home/josiah/ctypesgen_test/av/bsf.h: 98

AVBSFContext = struct_AVBSFContext# /home/josiah/ctypesgen_test/av/bsf.h: 96

AVBSFList = struct_AVBSFList# /home/josiah/ctypesgen_test/av/bsf.h: 240

AVProfile = struct_AVProfile# /home/josiah/ctypesgen_test/av/codec.h: 186

AVCodecDefault = struct_AVCodecDefault# /home/josiah/ctypesgen_test/av/codec.h: 188

AVCodecContext = struct_AVCodecContext# /home/josiah/ctypesgen_test/av/avcodec.h: 536

AVSubtitle = struct_AVSubtitle# /home/josiah/ctypesgen_test/av/avcodec.h: 2722

AVCodec = struct_AVCodec# /home/josiah/ctypesgen_test/av/codec.h: 197

AVCodecHWConfigInternal = struct_AVCodecHWConfigInternal# /home/josiah/ctypesgen_test/av/codec.h: 343

AVCodecHWConfig = struct_AVCodecHWConfig# /home/josiah/ctypesgen_test/av/codec.h: 465

AVCodecDescriptor = struct_AVCodecDescriptor# /home/josiah/ctypesgen_test/av/codec_desc.h: 66

RcOverride = struct_RcOverride# /home/josiah/ctypesgen_test/av/avcodec.h: 260

AVPanScan = struct_AVPanScan# /home/josiah/ctypesgen_test/av/avcodec.h: 446

AVCPBProperties = struct_AVCPBProperties# /home/josiah/ctypesgen_test/av/avcodec.h: 496

AVProducerReferenceTime = struct_AVProducerReferenceTime# /home/josiah/ctypesgen_test/av/avcodec.h: 509

AVCodecInternal = struct_AVCodecInternal# /home/josiah/ctypesgen_test/av/avcodec.h: 521

AVHWAccel = struct_AVHWAccel# /home/josiah/ctypesgen_test/av/avcodec.h: 2438

MpegEncContext = struct_MpegEncContext# /home/josiah/ctypesgen_test/av/avcodec.h: 2428

AVPicture = struct_AVPicture# /home/josiah/ctypesgen_test/av/avcodec.h: 2660

AVSubtitleRect = struct_AVSubtitleRect# /home/josiah/ctypesgen_test/av/avcodec.h: 2720

AVCodecParser = struct_AVCodecParser# /home/josiah/ctypesgen_test/av/avcodec.h: 3544

AVCodecParserContext = struct_AVCodecParserContext# /home/josiah/ctypesgen_test/av/avcodec.h: 3542

AVBitStreamFilterContext = struct_AVBitStreamFilterContext# /home/josiah/ctypesgen_test/av/avcodec.h: 4017

AVOptionRange = struct_AVOptionRange# /usr/include/libavutil/opt.h: 328

AVDCT = struct_AVDCT# /home/josiah/ctypesgen_test/av/avdct.h: 74

AVIOInterruptCB = struct_AVIOInterruptCB# /usr/include/libavformat/avio.h: 61

AVIODirEntry = struct_AVIODirEntry# /usr/include/libavformat/avio.h: 101

URLContext = struct_URLContext# /usr/include/libavformat/avio.h: 104

AVIODirContext = struct_AVIODirContext# /usr/include/libavformat/avio.h: 105

AVIOContext = struct_AVIOContext# /usr/include/libavformat/avio.h: 352

AVFormatContext = struct_AVFormatContext# /usr/include/libavformat/avformat.h: 1234

AVDeviceInfoList = struct_AVDeviceInfoList# /home/josiah/ctypesgen_test/av/avdevice.h: 465

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

AVDeviceRect = struct_AVDeviceRect# /home/josiah/ctypesgen_test/av/avdevice.h: 114

AVDeviceInfo = struct_AVDeviceInfo# /home/josiah/ctypesgen_test/av/avdevice.h: 460

FFTComplex = struct_FFTComplex# /home/josiah/ctypesgen_test/av/avfft.h: 39

FFTContext = struct_FFTContext# /home/josiah/ctypesgen_test/av/avfft.h: 41

RDFTContext = struct_RDFTContext# /home/josiah/ctypesgen_test/av/avfft.h: 78

DCTContext = struct_DCTContext# /home/josiah/ctypesgen_test/av/avfft.h: 91

AVFilterContext = struct_AVFilterContext# /home/josiah/ctypesgen_test/av/avfilter.h: 341

AVFilterLink = struct_AVFilterLink# /home/josiah/ctypesgen_test/av/avfilter.h: 471

AVFilterPad = struct_AVFilterPad# /home/josiah/ctypesgen_test/av/avfilter.h: 69

AVFilterFormats = struct_AVFilterFormats# /home/josiah/ctypesgen_test/av/avfilter.h: 70

AVFilterChannelLayouts = struct_AVFilterChannelLayouts# /home/josiah/ctypesgen_test/av/avfilter.h: 71

AVFilter = struct_AVFilter# /home/josiah/ctypesgen_test/av/avfilter.h: 145

AVFilterInternal = struct_AVFilterInternal# /home/josiah/ctypesgen_test/av/avfilter.h: 338

AVFilterGraph = struct_AVFilterGraph# /home/josiah/ctypesgen_test/av/avfilter.h: 850

AVFilterCommand = struct_AVFilterCommand# /home/josiah/ctypesgen_test/av/avfilter.h: 383

AVFilterFormatsConfig = struct_AVFilterFormatsConfig# /home/josiah/ctypesgen_test/av/avfilter.h: 457

AVFilterGraphInternal = struct_AVFilterGraphInternal# /home/josiah/ctypesgen_test/av/avfilter.h: 819

AVFilterInOut = struct_AVFilterInOut# /home/josiah/ctypesgen_test/av/avfilter.h: 1013

AVBlowfish = struct_AVBlowfish# /home/josiah/ctypesgen_test/av/blowfish.h: 38

ff_pad_helper_AVBPrint = struct_ff_pad_helper_AVBPrint# /home/josiah/ctypesgen_test/av/bprint.h: 82

AVBufferSinkParams = struct_AVBufferSinkParams# /home/josiah/ctypesgen_test/av/buffersink.h: 104

AVABufferSinkParams = struct_AVABufferSinkParams# /home/josiah/ctypesgen_test/av/buffersink.h: 123

AVBufferSrcParameters = struct_AVBufferSrcParameters# /home/josiah/ctypesgen_test/av/buffersrc.h: 117

AVCAMELLIA = struct_AVCAMELLIA# /home/josiah/ctypesgen_test/av/camellia.h: 38

AVCAST5 = struct_AVCAST5# /home/josiah/ctypesgen_test/av/cast5.h: 38

AVDES = struct_AVDES# /home/josiah/ctypesgen_test/av/des.h: 36

DiracVersionInfo = struct_DiracVersionInfo# /home/josiah/ctypesgen_test/av/dirac.h: 79

AVDiracSeqHeader = struct_AVDiracSeqHeader# /home/josiah/ctypesgen_test/av/dirac.h: 114

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /home/josiah/ctypesgen_test/av/dovi_meta.h: 60

AVDownmixInfo = struct_AVDownmixInfo# /home/josiah/ctypesgen_test/av/downmix_info.h: 93

AVDVProfile = struct_AVDVProfile# /home/josiah/ctypesgen_test/av/dv_profile.h: 59

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 35

AVEncryptionInfo = struct_AVEncryptionInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 81

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /home/josiah/ctypesgen_test/av/encryption_info.h: 88

AVExpr = struct_AVExpr# /home/josiah/ctypesgen_test/av/eval.h: 31

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /home/josiah/ctypesgen_test/av/film_grain_params.h: 118

AVFilmGrainParams = struct_AVFilmGrainParams# /home/josiah/ctypesgen_test/av/film_grain_params.h: 147

AVHashContext = struct_AVHashContext# /home/josiah/ctypesgen_test/av/hash.h: 117

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 53

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 230

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /home/josiah/ctypesgen_test/av/hdr_dynamic_metadata.h: 323

AVHMAC = struct_AVHMAC# /home/josiah/ctypesgen_test/av/hmac.h: 42

AVDRMObjectDescriptor = struct_AVDRMObjectDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 66

AVDRMPlaneDescriptor = struct_AVDRMPlaneDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 88

AVDRMLayerDescriptor = struct_AVDRMLayerDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 111

AVDRMFrameDescriptor = struct_AVDRMFrameDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 150

AVDRMDeviceContext = struct_AVDRMDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_drm.h: 167

AVMediaCodecDeviceContext = struct_AVMediaCodecDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_mediacodec.h: 34

AVOpenCLFrameDescriptor = struct_AVOpenCLFrameDescriptor# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 56

AVOpenCLDeviceContext = struct_AVOpenCLDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 82

AVOpenCLFramesContext = struct_AVOpenCLFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_opencl.h: 98

AVQSVDeviceContext = struct_AVQSVDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 37

AVQSVFramesContext = struct_AVQSVFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_qsv.h: 50

AVVAAPIDeviceContext = struct_AVVAAPIDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 81

AVVAAPIFramesContext = struct_AVVAAPIFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 103

AVVAAPIHWConfig = struct_AVVAAPIHWConfig# /home/josiah/ctypesgen_test/av/hwcontext_vaapi.h: 115

AVVDPAUDeviceContext = struct_AVVDPAUDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vdpau.h: 38

AVVulkanDeviceContext = struct_AVVulkanDeviceContext# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 107

AVVulkanFramesContext = struct_AVVulkanFramesContext# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 134

AVVkFrameInternal = struct_AVVkFrameInternal# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 189

AVVkFrame = struct_AVVkFrame# /home/josiah/ctypesgen_test/av/hwcontext_vulkan.h: 190

AVComponentDescriptor = struct_AVComponentDescriptor# /home/josiah/ctypesgen_test/av/pixdesc.h: 70

AVPixFmtDescriptor = struct_AVPixFmtDescriptor# /home/josiah/ctypesgen_test/av/pixdesc.h: 123

AVLFG = struct_AVLFG# /home/josiah/ctypesgen_test/av/lfg.h: 36

AVMasteringDisplayMetadata = struct_AVMasteringDisplayMetadata# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 69

AVContentLightMetadata = struct_AVContentLightMetadata# /home/josiah/ctypesgen_test/av/mastering_display_metadata.h: 108

AVMD5 = struct_AVMD5# /home/josiah/ctypesgen_test/av/md5.h: 46

AVMediaCodecContext = struct_AVMediaCodecContext# /home/josiah/ctypesgen_test/av/mediacodec.h: 40

MediaCodecBuffer = struct_MediaCodecBuffer# /home/josiah/ctypesgen_test/av/mediacodec.h: 73

AVMotionVector = struct_AVMotionVector# /home/josiah/ctypesgen_test/av/motion_vector.h: 55

AVMurMur3 = struct_AVMurMur3# /home/josiah/ctypesgen_test/av/murmur3.h: 69

AVQSVContext = struct_AVQSVContext# /home/josiah/ctypesgen_test/av/qsv.h: 98

AVRC4 = struct_AVRC4# /home/josiah/ctypesgen_test/av/rc4.h: 35

AVReplayGain = struct_AVReplayGain# /home/josiah/ctypesgen_test/av/replaygain.h: 48

AVRIPEMD = struct_AVRIPEMD# /home/josiah/ctypesgen_test/av/ripemd.h: 47

rom1394_bus_options_struct = struct_rom1394_bus_options_struct# /home/josiah/ctypesgen_test/av/rom1394.h: 58

rom1394_directory_struct = struct_rom1394_directory_struct# /home/josiah/ctypesgen_test/av/rom1394.h: 70

AVSHA512 = struct_AVSHA512# /home/josiah/ctypesgen_test/av/sha512.h: 56

AVSHA = struct_AVSHA# /home/josiah/ctypesgen_test/av/sha.h: 54

AVSphericalMapping = struct_AVSphericalMapping# /home/josiah/ctypesgen_test/av/spherical.h: 183

AVStereo3D = struct_AVStereo3D# /home/josiah/ctypesgen_test/av/stereo3d.h: 191

SwrContext = struct_SwrContext# /home/josiah/ctypesgen_test/av/swresample.h: 182

SwsVector = struct_SwsVector# /home/josiah/ctypesgen_test/av/swscale.h: 112

SwsFilter = struct_SwsFilter# /home/josiah/ctypesgen_test/av/swscale.h: 120

SwsContext = struct_SwsContext# /home/josiah/ctypesgen_test/av/swscale.h: 122

AVTEA = struct_AVTEA# /home/josiah/ctypesgen_test/av/tea.h: 37

AVThreadMessageQueue = struct_AVThreadMessageQueue# /home/josiah/ctypesgen_test/av/threadmessage.h: 22

AVTreeNode = struct_AVTreeNode# /home/josiah/ctypesgen_test/av/tree.h: 45

AVTWOFISH = struct_AVTWOFISH# /home/josiah/ctypesgen_test/av/twofish.h: 38

AVTXContext = struct_AVTXContext# /home/josiah/ctypesgen_test/av/tx.h: 25

AVComplexFloat = struct_AVComplexFloat# /home/josiah/ctypesgen_test/av/tx.h: 29

AVComplexDouble = struct_AVComplexDouble# /home/josiah/ctypesgen_test/av/tx.h: 33

AVComplexInt32 = struct_AVComplexInt32# /home/josiah/ctypesgen_test/av/tx.h: 37

vaapi_context = struct_vaapi_context# /home/josiah/ctypesgen_test/av/vaapi.h: 56

AVVDPAUContext = struct_AVVDPAUContext# /home/josiah/ctypesgen_test/av/vdpau.h: 97

AVVideoEncParams = struct_AVVideoEncParams# /home/josiah/ctypesgen_test/av/video_enc_params.h: 110

AVVideoBlockParams = struct_AVVideoBlockParams# /home/josiah/ctypesgen_test/av/video_enc_params.h: 137

AVVorbisParseContext = struct_AVVorbisParseContext# /home/josiah/ctypesgen_test/av/vorbis_parser.h: 31

AVXTEA = struct_AVXTEA# /home/josiah/ctypesgen_test/av/xtea.h: 37

xvmc_pix_fmt = struct_xvmc_pix_fmt# /home/josiah/ctypesgen_test/av/xvmc.h: 46

# No inserted files

# No prefix-stripping

