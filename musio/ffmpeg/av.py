r"""Wrapper for ac3_parser.h

Generated with:
/home/josiah/.local/bin/ctypesgen -lavcodec -lavformat -lavutil -lavdevice -lswresample -lswscale av/ac3_parser.h av/adler32.h av/adts_parser.h av/aes_ctr.h av/aes.h av/attributes.h av/audio_fifo.h av/avassert.h av/avcodec.h av/avconfig.h av/avdct.h av/avdevice.h av/avfft.h av/avfilter.h av/avformat.h av/avio.h av/avstring.h av/avutil.h av/base64.h av/blowfish.h av/bprint.h av/bsf.h av/bswap.h av/buffer.h av/buffersink.h av/buffersrc.h av/camellia.h av/cast5.h av/channel_layout.h av/codec_desc.h av/codec.h av/codec_id.h av/codec_par.h av/common.h av/cpu.h av/crc.h av/des.h av/dict.h av/dirac.h av/display.h av/dovi_meta.h av/downmix_info.h av/dv_profile.h av/encryption_info.h av/error.h av/eval.h av/ffversion.h av/fifo.h av/file.h av/film_grain_params.h av/frame.h av/hash.h av/hdr_dynamic_metadata.h av/hmac.h av/hwcontext_drm.h av/hwcontext.h av/hwcontext_mediacodec.h av/hwcontext_opencl.h av/hwcontext_qsv.h av/hwcontext_vaapi.h av/hwcontext_vdpau.h av/hwcontext_vulkan.h av/imgutils.h av/intfloat.h av/intreadwrite.h av/jni.h av/lfg.h av/log.h av/lzo.h av/macros.h av/mastering_display_metadata.h av/mathematics.h av/md5.h av/mediacodec.h av/mem.h av/motion_vector.h av/murmur3.h av/opt.h av/packet.h av/parseutils.h av/pixdesc.h av/pixelutils.h av/pixfmt.h av/qsv.h av/random_seed.h av/rational.h av/rc4.h av/replaygain.h av/ripemd.h av/samplefmt.h av/sha512.h av/sha.h av/spherical.h av/stereo3d.h av/swresample.h av/swscale.h av/tea.h av/threadmessage.h av/timecode.h av/time.h av/timestamp.h av/tree.h av/twofish.h av/tx.h av/version.h av/video_enc_params.h av/vorbis_parser.h av/xtea.h av/xvmc.h -o av_test2.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
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


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

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
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
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
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


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

"""
Load libraries - appropriately for all our supported platforms
"""
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

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
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
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
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

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
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

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

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
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
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
            "SHLIB_PATH",  # HP-UX
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
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
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
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

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
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


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

__uint16_t = c_ushort# /usr/include/bits/types.h: 40

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

uint8_t = __uint8_t# /usr/include/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/bits/stdint-uintn.h: 27

# /home/josiah/ctypesgen_test/av/av/ac3_parser.h: 32
if _libs["avcodec"].has("av_ac3_parse_header", "cdecl"):
    av_ac3_parse_header = _libs["avcodec"].get("av_ac3_parse_header", "cdecl")
    av_ac3_parse_header.argtypes = [POINTER(uint8_t), c_size_t, POINTER(uint8_t), POINTER(uint16_t)]
    av_ac3_parse_header.restype = c_int

AVAdler = uint32_t# /home/josiah/ctypesgen_test/av/av/adler32.h: 42

# /home/josiah/ctypesgen_test/av/av/adler32.h: 56
if _libs["avcodec"].has("av_adler32_update", "cdecl"):
    av_adler32_update = _libs["avcodec"].get("av_adler32_update", "cdecl")
    av_adler32_update.argtypes = [AVAdler, POINTER(uint8_t), c_size_t]
    av_adler32_update.restype = AVAdler

# /home/josiah/ctypesgen_test/av/av/adts_parser.h: 34
if _libs["avcodec"].has("av_adts_header_parse", "cdecl"):
    av_adts_header_parse = _libs["avcodec"].get("av_adts_header_parse", "cdecl")
    av_adts_header_parse.argtypes = [POINTER(uint8_t), POINTER(uint32_t), POINTER(uint8_t)]
    av_adts_header_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 38
class struct_AVAESCTR(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 43
if _libs["avcodec"].has("av_aes_ctr_alloc", "cdecl"):
    av_aes_ctr_alloc = _libs["avcodec"].get("av_aes_ctr_alloc", "cdecl")
    av_aes_ctr_alloc.argtypes = []
    av_aes_ctr_alloc.restype = POINTER(struct_AVAESCTR)

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 51
if _libs["avcodec"].has("av_aes_ctr_init", "cdecl"):
    av_aes_ctr_init = _libs["avcodec"].get("av_aes_ctr_init", "cdecl")
    av_aes_ctr_init.argtypes = [POINTER(struct_AVAESCTR), POINTER(uint8_t)]
    av_aes_ctr_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 58
if _libs["avcodec"].has("av_aes_ctr_free", "cdecl"):
    av_aes_ctr_free = _libs["avcodec"].get("av_aes_ctr_free", "cdecl")
    av_aes_ctr_free.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_free.restype = None

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 68
if _libs["avcodec"].has("av_aes_ctr_crypt", "cdecl"):
    av_aes_ctr_crypt = _libs["avcodec"].get("av_aes_ctr_crypt", "cdecl")
    av_aes_ctr_crypt.argtypes = [POINTER(struct_AVAESCTR), POINTER(uint8_t), POINTER(uint8_t), c_int]
    av_aes_ctr_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 73
if _libs["avcodec"].has("av_aes_ctr_get_iv", "cdecl"):
    av_aes_ctr_get_iv = _libs["avcodec"].get("av_aes_ctr_get_iv", "cdecl")
    av_aes_ctr_get_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_get_iv.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 78
if _libs["avcodec"].has("av_aes_ctr_set_random_iv", "cdecl"):
    av_aes_ctr_set_random_iv = _libs["avcodec"].get("av_aes_ctr_set_random_iv", "cdecl")
    av_aes_ctr_set_random_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_set_random_iv.restype = None

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 83
if _libs["avcodec"].has("av_aes_ctr_set_iv", "cdecl"):
    av_aes_ctr_set_iv = _libs["avcodec"].get("av_aes_ctr_set_iv", "cdecl")
    av_aes_ctr_set_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(uint8_t)]
    av_aes_ctr_set_iv.restype = None

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 88
if _libs["avcodec"].has("av_aes_ctr_set_full_iv", "cdecl"):
    av_aes_ctr_set_full_iv = _libs["avcodec"].get("av_aes_ctr_set_full_iv", "cdecl")
    av_aes_ctr_set_full_iv.argtypes = [POINTER(struct_AVAESCTR), POINTER(uint8_t)]
    av_aes_ctr_set_full_iv.restype = None

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 93
if _libs["avcodec"].has("av_aes_ctr_increment_iv", "cdecl"):
    av_aes_ctr_increment_iv = _libs["avcodec"].get("av_aes_ctr_increment_iv", "cdecl")
    av_aes_ctr_increment_iv.argtypes = [POINTER(struct_AVAESCTR)]
    av_aes_ctr_increment_iv.restype = None

# /home/josiah/ctypesgen_test/av/av/aes.h: 34
try:
    av_aes_size = (c_int).in_dll(_libs["avcodec"], "av_aes_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/aes.h: 36
class struct_AVAES(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/aes.h: 41
if _libs["avcodec"].has("av_aes_alloc", "cdecl"):
    av_aes_alloc = _libs["avcodec"].get("av_aes_alloc", "cdecl")
    av_aes_alloc.argtypes = []
    av_aes_alloc.restype = POINTER(struct_AVAES)

# /home/josiah/ctypesgen_test/av/av/aes.h: 51
if _libs["avcodec"].has("av_aes_init", "cdecl"):
    av_aes_init = _libs["avcodec"].get("av_aes_init", "cdecl")
    av_aes_init.argtypes = [POINTER(struct_AVAES), POINTER(uint8_t), c_int, c_int]
    av_aes_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/aes.h: 63
if _libs["avcodec"].has("av_aes_crypt", "cdecl"):
    av_aes_crypt = _libs["avcodec"].get("av_aes_crypt", "cdecl")
    av_aes_crypt.argtypes = [POINTER(struct_AVAES), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_aes_crypt.restype = None

enum_AVSampleFormat = c_int# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_NONE = (-1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_U8 = (AV_SAMPLE_FMT_NONE + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S16 = (AV_SAMPLE_FMT_U8 + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S32 = (AV_SAMPLE_FMT_S16 + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_FLT = (AV_SAMPLE_FMT_S32 + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_DBL = (AV_SAMPLE_FMT_FLT + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_U8P = (AV_SAMPLE_FMT_DBL + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S16P = (AV_SAMPLE_FMT_U8P + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S32P = (AV_SAMPLE_FMT_S16P + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_FLTP = (AV_SAMPLE_FMT_S32P + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_DBLP = (AV_SAMPLE_FMT_FLTP + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S64 = (AV_SAMPLE_FMT_DBLP + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_S64P = (AV_SAMPLE_FMT_S64 + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

AV_SAMPLE_FMT_NB = (AV_SAMPLE_FMT_S64P + 1)# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 55

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 78
if _libs["avcodec"].has("av_get_sample_fmt_name", "cdecl"):
    av_get_sample_fmt_name = _libs["avcodec"].get("av_get_sample_fmt_name", "cdecl")
    av_get_sample_fmt_name.argtypes = [enum_AVSampleFormat]
    av_get_sample_fmt_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 84
if _libs["avcodec"].has("av_get_sample_fmt", "cdecl"):
    av_get_sample_fmt = _libs["avcodec"].get("av_get_sample_fmt", "cdecl")
    av_get_sample_fmt.argtypes = [String]
    av_get_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 92
if _libs["avcodec"].has("av_get_alt_sample_fmt", "cdecl"):
    av_get_alt_sample_fmt = _libs["avcodec"].get("av_get_alt_sample_fmt", "cdecl")
    av_get_alt_sample_fmt.argtypes = [enum_AVSampleFormat, c_int]
    av_get_alt_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 103
if _libs["avcodec"].has("av_get_packed_sample_fmt", "cdecl"):
    av_get_packed_sample_fmt = _libs["avcodec"].get("av_get_packed_sample_fmt", "cdecl")
    av_get_packed_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_packed_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 114
if _libs["avcodec"].has("av_get_planar_sample_fmt", "cdecl"):
    av_get_planar_sample_fmt = _libs["avcodec"].get("av_get_planar_sample_fmt", "cdecl")
    av_get_planar_sample_fmt.argtypes = [enum_AVSampleFormat]
    av_get_planar_sample_fmt.restype = enum_AVSampleFormat

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 128
if _libs["avcodec"].has("av_get_sample_fmt_string", "cdecl"):
    av_get_sample_fmt_string = _libs["avcodec"].get("av_get_sample_fmt_string", "cdecl")
    av_get_sample_fmt_string.argtypes = [String, c_int, enum_AVSampleFormat]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_sample_fmt_string.restype = ReturnString
    else:
        av_get_sample_fmt_string.restype = String
        av_get_sample_fmt_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 137
if _libs["avcodec"].has("av_get_bytes_per_sample", "cdecl"):
    av_get_bytes_per_sample = _libs["avcodec"].get("av_get_bytes_per_sample", "cdecl")
    av_get_bytes_per_sample.argtypes = [enum_AVSampleFormat]
    av_get_bytes_per_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 145
if _libs["avcodec"].has("av_sample_fmt_is_planar", "cdecl"):
    av_sample_fmt_is_planar = _libs["avcodec"].get("av_sample_fmt_is_planar", "cdecl")
    av_sample_fmt_is_planar.argtypes = [enum_AVSampleFormat]
    av_sample_fmt_is_planar.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 157
if _libs["avcodec"].has("av_samples_get_buffer_size", "cdecl"):
    av_samples_get_buffer_size = _libs["avcodec"].get("av_samples_get_buffer_size", "cdecl")
    av_samples_get_buffer_size.argtypes = [POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_get_buffer_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 198
if _libs["avcodec"].has("av_samples_fill_arrays", "cdecl"):
    av_samples_fill_arrays = _libs["avcodec"].get("av_samples_fill_arrays", "cdecl")
    av_samples_fill_arrays.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_fill_arrays.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 223
if _libs["avcodec"].has("av_samples_alloc", "cdecl"):
    av_samples_alloc = _libs["avcodec"].get("av_samples_alloc", "cdecl")
    av_samples_alloc.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 235
if _libs["avcodec"].has("av_samples_alloc_array_and_samples", "cdecl"):
    av_samples_alloc_array_and_samples = _libs["avcodec"].get("av_samples_alloc_array_and_samples", "cdecl")
    av_samples_alloc_array_and_samples.argtypes = [POINTER(POINTER(POINTER(uint8_t))), POINTER(c_int), c_int, c_int, enum_AVSampleFormat, c_int]
    av_samples_alloc_array_and_samples.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 249
if _libs["avcodec"].has("av_samples_copy", "cdecl"):
    av_samples_copy = _libs["avcodec"].get("av_samples_copy", "cdecl")
    av_samples_copy.argtypes = [POINTER(POINTER(uint8_t)), POINTER(POINTER(uint8_t)), c_int, c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_copy.restype = c_int

# /home/josiah/ctypesgen_test/av/av/samplefmt.h: 262
if _libs["avcodec"].has("av_samples_set_silence", "cdecl"):
    av_samples_set_silence = _libs["avcodec"].get("av_samples_set_silence", "cdecl")
    av_samples_set_silence.argtypes = [POINTER(POINTER(uint8_t)), c_int, c_int, c_int, enum_AVSampleFormat]
    av_samples_set_silence.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 48
class struct_AVAudioFifo(Structure):
    pass

AVAudioFifo = struct_AVAudioFifo# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 48

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 55
if _libs["avcodec"].has("av_audio_fifo_free", "cdecl"):
    av_audio_fifo_free = _libs["avcodec"].get("av_audio_fifo_free", "cdecl")
    av_audio_fifo_free.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_free.restype = None

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 65
if _libs["avcodec"].has("av_audio_fifo_alloc", "cdecl"):
    av_audio_fifo_alloc = _libs["avcodec"].get("av_audio_fifo_alloc", "cdecl")
    av_audio_fifo_alloc.argtypes = [enum_AVSampleFormat, c_int, c_int]
    av_audio_fifo_alloc.restype = POINTER(AVAudioFifo)

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 76
if _libs["avcodec"].has("av_audio_fifo_realloc", "cdecl"):
    av_audio_fifo_realloc = _libs["avcodec"].get("av_audio_fifo_realloc", "cdecl")
    av_audio_fifo_realloc.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_realloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 94
if _libs["avcodec"].has("av_audio_fifo_write", "cdecl"):
    av_audio_fifo_write = _libs["avcodec"].get("av_audio_fifo_write", "cdecl")
    av_audio_fifo_write.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_write.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 110
if _libs["avcodec"].has("av_audio_fifo_peek", "cdecl"):
    av_audio_fifo_peek = _libs["avcodec"].get("av_audio_fifo_peek", "cdecl")
    av_audio_fifo_peek.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_peek.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 127
if _libs["avcodec"].has("av_audio_fifo_peek_at", "cdecl"):
    av_audio_fifo_peek_at = _libs["avcodec"].get("av_audio_fifo_peek_at", "cdecl")
    av_audio_fifo_peek_at.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int, c_int]
    av_audio_fifo_peek_at.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 143
if _libs["avcodec"].has("av_audio_fifo_read", "cdecl"):
    av_audio_fifo_read = _libs["avcodec"].get("av_audio_fifo_read", "cdecl")
    av_audio_fifo_read.argtypes = [POINTER(AVAudioFifo), POINTER(POINTER(None)), c_int]
    av_audio_fifo_read.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 154
if _libs["avcodec"].has("av_audio_fifo_drain", "cdecl"):
    av_audio_fifo_drain = _libs["avcodec"].get("av_audio_fifo_drain", "cdecl")
    av_audio_fifo_drain.argtypes = [POINTER(AVAudioFifo), c_int]
    av_audio_fifo_drain.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 163
if _libs["avcodec"].has("av_audio_fifo_reset", "cdecl"):
    av_audio_fifo_reset = _libs["avcodec"].get("av_audio_fifo_reset", "cdecl")
    av_audio_fifo_reset.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_reset.restype = None

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 171
if _libs["avcodec"].has("av_audio_fifo_size", "cdecl"):
    av_audio_fifo_size = _libs["avcodec"].get("av_audio_fifo_size", "cdecl")
    av_audio_fifo_size.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 179
if _libs["avcodec"].has("av_audio_fifo_space", "cdecl"):
    av_audio_fifo_space = _libs["avcodec"].get("av_audio_fifo_space", "cdecl")
    av_audio_fifo_space.argtypes = [POINTER(AVAudioFifo)]
    av_audio_fifo_space.restype = c_int

pid_t = __pid_t# /usr/include/sys/types.h: 97

clock_t = __clock_t# /usr/include/bits/types/clock_t.h: 7

clockid_t = __clockid_t# /usr/include/bits/types/clockid_t.h: 7

time_t = __time_t# /usr/include/bits/types/time_t.h: 10

timer_t = __timer_t# /usr/include/bits/types/timer_t.h: 7

# /usr/include/bits/types/struct_timespec.h: 11
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

enum_anon_19 = c_int# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_NA = 0# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_INPUT = (AV_CLASS_CATEGORY_NA + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_OUTPUT = (AV_CLASS_CATEGORY_INPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_MUXER = (AV_CLASS_CATEGORY_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEMUXER = (AV_CLASS_CATEGORY_MUXER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_ENCODER = (AV_CLASS_CATEGORY_DEMUXER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DECODER = (AV_CLASS_CATEGORY_ENCODER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_FILTER = (AV_CLASS_CATEGORY_DECODER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_BITSTREAM_FILTER = (AV_CLASS_CATEGORY_FILTER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_SWSCALER = (AV_CLASS_CATEGORY_BITSTREAM_FILTER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_SWRESAMPLER = (AV_CLASS_CATEGORY_SWSCALER + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT = 40# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_OUTPUT = (AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_DEVICE_INPUT = (AV_CLASS_CATEGORY_DEVICE_OUTPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AV_CLASS_CATEGORY_NB = (AV_CLASS_CATEGORY_DEVICE_INPUT + 1)# /home/josiah/ctypesgen_test/av/av/log.h: 47

AVClassCategory = enum_anon_19# /home/josiah/ctypesgen_test/av/av/log.h: 47

# /usr/include/libavutil/opt.h: 336
class struct_AVOptionRanges(Structure):
    pass

# /usr/include/libavutil/opt.h: 251
class struct_AVOption(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 66
class struct_AVClass(Structure):
    pass

struct_AVClass.__slots__ = [
    'class_name',
    'item_name',
    'option',
    'version',
    'log_level_offset_offset',
    'parent_log_context_offset',
    'category',
    'get_category',
    'query_ranges',
    'child_next',
    'child_class_iterate',
]
struct_AVClass._fields_ = [
    ('class_name', String),
    ('item_name', CFUNCTYPE(UNCHECKED(c_char_p), POINTER(None))),
    ('option', POINTER(struct_AVOption)),
    ('version', c_int),
    ('log_level_offset_offset', c_int),
    ('parent_log_context_offset', c_int),
    ('category', AVClassCategory),
    ('get_category', CFUNCTYPE(UNCHECKED(AVClassCategory), POINTER(None))),
    ('query_ranges', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_AVOptionRanges)), POINTER(None), String, c_int)),
    ('child_next', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), POINTER(None))),
    ('child_class_iterate', CFUNCTYPE(UNCHECKED(POINTER(struct_AVClass)), POINTER(POINTER(None)))),
]

AVClass = struct_AVClass# /home/josiah/ctypesgen_test/av/av/log.h: 147

# /home/josiah/ctypesgen_test/av/av/log.h: 238
if _libs["avcodec"].has("av_log", "cdecl"):
    _func = _libs["avcodec"].get("av_log", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, String]
    av_log = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/log.h: 259
if _libs["avcodec"].has("av_log_once", "cdecl"):
    _func = _libs["avcodec"].get("av_log_once", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(None), c_int, c_int, POINTER(c_int), String]
    av_log_once = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/log.h: 277
if _libs["avcodec"].has("av_vlog", "cdecl"):
    av_vlog = _libs["avcodec"].get("av_vlog", "cdecl")
    av_vlog.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_vlog.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 286
if _libs["avcodec"].has("av_log_get_level", "cdecl"):
    av_log_get_level = _libs["avcodec"].get("av_log_get_level", "cdecl")
    av_log_get_level.argtypes = []
    av_log_get_level.restype = c_int

# /home/josiah/ctypesgen_test/av/av/log.h: 295
if _libs["avcodec"].has("av_log_set_level", "cdecl"):
    av_log_set_level = _libs["avcodec"].get("av_log_set_level", "cdecl")
    av_log_set_level.argtypes = [c_int]
    av_log_set_level.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 307
if _libs["avcodec"].has("av_log_set_callback", "cdecl"):
    av_log_set_callback = _libs["avcodec"].get("av_log_set_callback", "cdecl")
    av_log_set_callback.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, String, c_void_p)]
    av_log_set_callback.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 322
if _libs["avcodec"].has("av_log_default_callback", "cdecl"):
    av_log_default_callback = _libs["avcodec"].get("av_log_default_callback", "cdecl")
    av_log_default_callback.argtypes = [POINTER(None), c_int, String, c_void_p]
    av_log_default_callback.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 332
if _libs["avcodec"].has("av_default_item_name", "cdecl"):
    av_default_item_name = _libs["avcodec"].get("av_default_item_name", "cdecl")
    av_default_item_name.argtypes = [POINTER(None)]
    av_default_item_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/log.h: 333
if _libs["avcodec"].has("av_default_get_category", "cdecl"):
    av_default_get_category = _libs["avcodec"].get("av_default_get_category", "cdecl")
    av_default_get_category.argtypes = [POINTER(None)]
    av_default_get_category.restype = AVClassCategory

# /home/josiah/ctypesgen_test/av/av/log.h: 342
if _libs["avcodec"].has("av_log_format_line", "cdecl"):
    av_log_format_line = _libs["avcodec"].get("av_log_format_line", "cdecl")
    av_log_format_line.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 359
if _libs["avcodec"].has("av_log_format_line2", "cdecl"):
    av_log_format_line2 = _libs["avcodec"].get("av_log_format_line2", "cdecl")
    av_log_format_line2.argtypes = [POINTER(None), c_int, String, c_void_p, String, c_int, POINTER(c_int)]
    av_log_format_line2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/log.h: 380
if _libs["avcodec"].has("av_log_set_flags", "cdecl"):
    av_log_set_flags = _libs["avcodec"].get("av_log_set_flags", "cdecl")
    av_log_set_flags.argtypes = [c_int]
    av_log_set_flags.restype = None

# /home/josiah/ctypesgen_test/av/av/log.h: 381
if _libs["avcodec"].has("av_log_get_flags", "cdecl"):
    av_log_get_flags = _libs["avcodec"].get("av_log_get_flags", "cdecl")
    av_log_get_flags.argtypes = []
    av_log_get_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avassert.h: 73
if _libs["avcodec"].has("av_assert0_fpu", "cdecl"):
    av_assert0_fpu = _libs["avcodec"].get("av_assert0_fpu", "cdecl")
    av_assert0_fpu.argtypes = []
    av_assert0_fpu.restype = None

# /usr/include/libavutil/avutil.h: 171
if _libs["avcodec"].has("avutil_version", "cdecl"):
    avutil_version = _libs["avcodec"].get("avutil_version", "cdecl")
    avutil_version.argtypes = []
    avutil_version.restype = c_uint

# /usr/include/libavutil/avutil.h: 178
if _libs["avcodec"].has("av_version_info", "cdecl"):
    av_version_info = _libs["avcodec"].get("av_version_info", "cdecl")
    av_version_info.argtypes = []
    av_version_info.restype = c_char_p

# /usr/include/libavutil/avutil.h: 183
if _libs["avcodec"].has("avutil_configuration", "cdecl"):
    avutil_configuration = _libs["avcodec"].get("avutil_configuration", "cdecl")
    avutil_configuration.argtypes = []
    avutil_configuration.restype = c_char_p

# /usr/include/libavutil/avutil.h: 188
if _libs["avcodec"].has("avutil_license", "cdecl"):
    avutil_license = _libs["avcodec"].get("avutil_license", "cdecl")
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
if _libs["avcodec"].has("av_get_media_type_string", "cdecl"):
    av_get_media_type_string = _libs["avcodec"].get("av_get_media_type_string", "cdecl")
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

# /usr/include/bits/types/__locale_t.h: 30
class struct___locale_data(Structure):
    pass

# /usr/include/bits/types/__locale_t.h: 27
class struct___locale_struct(Structure):
    pass

struct___locale_struct.__slots__ = [
    '__locales',
    '__ctype_b',
    '__ctype_tolower',
    '__ctype_toupper',
    '__names',
]
struct___locale_struct._fields_ = [
    ('__locales', POINTER(struct___locale_data) * int(13)),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', POINTER(c_char) * int(13)),
]

__locale_t = POINTER(struct___locale_struct)# /usr/include/bits/types/__locale_t.h: 41

locale_t = __locale_t# /usr/include/bits/types/locale_t.h: 24

# /usr/include/libavutil/common.h: 159
if _libs["avcodec"].has("av_log2", "cdecl"):
    av_log2 = _libs["avcodec"].get("av_log2", "cdecl")
    av_log2.argtypes = [c_uint]
    av_log2.restype = c_int

# /usr/include/libavutil/common.h: 163
if _libs["avcodec"].has("av_log2_16bit", "cdecl"):
    av_log2_16bit = _libs["avcodec"].get("av_log2_16bit", "cdecl")
    av_log2_16bit.argtypes = [c_uint]
    av_log2_16bit.restype = c_int

# /usr/include/libavutil/common.h: 349
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /usr/include/libavutil/common.h: 368
for _lib in _libs.values():
    try:
        tmp = (c_int64).in_dll(_lib, "tmp")
        break
    except:
        pass

# /usr/include/libavutil/mem.h: 121
if _libs["avcodec"].has("av_malloc", "cdecl"):
    av_malloc = _libs["avcodec"].get("av_malloc", "cdecl")
    av_malloc.argtypes = [c_size_t]
    av_malloc.restype = POINTER(c_ubyte)
    av_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 132
if _libs["avcodec"].has("av_mallocz", "cdecl"):
    av_mallocz = _libs["avcodec"].get("av_mallocz", "cdecl")
    av_mallocz.argtypes = [c_size_t]
    av_mallocz.restype = POINTER(c_ubyte)
    av_mallocz.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 145
if _libs["avcodec"].has("av_malloc_array", "cdecl"):
    av_malloc_array = _libs["avcodec"].get("av_malloc_array", "cdecl")
    av_malloc_array.argtypes = [c_size_t, c_size_t]
    av_malloc_array.restype = POINTER(c_ubyte)
    av_malloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 160
if _libs["avcodec"].has("av_calloc", "cdecl"):
    av_calloc = _libs["avcodec"].get("av_calloc", "cdecl")
    av_calloc.argtypes = [c_size_t, c_size_t]
    av_calloc.restype = POINTER(c_ubyte)
    av_calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 182
if _libs["avcodec"].has("av_realloc", "cdecl"):
    av_realloc = _libs["avcodec"].get("av_realloc", "cdecl")
    av_realloc.argtypes = [POINTER(None), c_size_t]
    av_realloc.restype = POINTER(c_ubyte)
    av_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 204
if _libs["avcodec"].has("av_reallocp", "cdecl"):
    av_reallocp = _libs["avcodec"].get("av_reallocp", "cdecl")
    av_reallocp.argtypes = [POINTER(None), c_size_t]
    av_reallocp.restype = c_int

# /usr/include/libavutil/mem.h: 221
if _libs["avcodec"].has("av_realloc_f", "cdecl"):
    av_realloc_f = _libs["avcodec"].get("av_realloc_f", "cdecl")
    av_realloc_f.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_f.restype = POINTER(c_ubyte)
    av_realloc_f.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 241
if _libs["avcodec"].has("av_realloc_array", "cdecl"):
    av_realloc_array = _libs["avcodec"].get("av_realloc_array", "cdecl")
    av_realloc_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_realloc_array.restype = POINTER(c_ubyte)
    av_realloc_array.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 259
if _libs["avcodec"].has("av_reallocp_array", "cdecl"):
    av_reallocp_array = _libs["avcodec"].get("av_reallocp_array", "cdecl")
    av_reallocp_array.argtypes = [POINTER(None), c_size_t, c_size_t]
    av_reallocp_array.restype = c_int

# /usr/include/libavutil/mem.h: 293
if _libs["avcodec"].has("av_fast_realloc", "cdecl"):
    av_fast_realloc = _libs["avcodec"].get("av_fast_realloc", "cdecl")
    av_fast_realloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_realloc.restype = POINTER(c_ubyte)
    av_fast_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 324
if _libs["avcodec"].has("av_fast_malloc", "cdecl"):
    av_fast_malloc = _libs["avcodec"].get("av_fast_malloc", "cdecl")
    av_fast_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_malloc.restype = None

# /usr/include/libavutil/mem.h: 344
if _libs["avcodec"].has("av_fast_mallocz", "cdecl"):
    av_fast_mallocz = _libs["avcodec"].get("av_fast_mallocz", "cdecl")
    av_fast_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_mallocz.restype = None

# /usr/include/libavutil/mem.h: 357
if _libs["avcodec"].has("av_free", "cdecl"):
    av_free = _libs["avcodec"].get("av_free", "cdecl")
    av_free.argtypes = [POINTER(None)]
    av_free.restype = None

# /usr/include/libavutil/mem.h: 380
if _libs["avcodec"].has("av_freep", "cdecl"):
    av_freep = _libs["avcodec"].get("av_freep", "cdecl")
    av_freep.argtypes = [POINTER(None)]
    av_freep.restype = None

# /usr/include/libavutil/mem.h: 390
if _libs["avcodec"].has("av_strdup", "cdecl"):
    av_strdup = _libs["avcodec"].get("av_strdup", "cdecl")
    av_strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strdup.restype = ReturnString
    else:
        av_strdup.restype = String
        av_strdup.errcheck = ReturnString

# /usr/include/libavutil/mem.h: 401
if _libs["avcodec"].has("av_strndup", "cdecl"):
    av_strndup = _libs["avcodec"].get("av_strndup", "cdecl")
    av_strndup.argtypes = [String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strndup.restype = ReturnString
    else:
        av_strndup.restype = String
        av_strndup.errcheck = ReturnString

# /usr/include/libavutil/mem.h: 411
if _libs["avcodec"].has("av_memdup", "cdecl"):
    av_memdup = _libs["avcodec"].get("av_memdup", "cdecl")
    av_memdup.argtypes = [POINTER(None), c_size_t]
    av_memdup.restype = POINTER(c_ubyte)
    av_memdup.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 424
if _libs["avcodec"].has("av_memcpy_backptr", "cdecl"):
    av_memcpy_backptr = _libs["avcodec"].get("av_memcpy_backptr", "cdecl")
    av_memcpy_backptr.argtypes = [POINTER(uint8_t), c_int, c_int]
    av_memcpy_backptr.restype = None

# /usr/include/libavutil/mem.h: 526
if _libs["avcodec"].has("av_dynarray_add", "cdecl"):
    av_dynarray_add = _libs["avcodec"].get("av_dynarray_add", "cdecl")
    av_dynarray_add.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add.restype = None

# /usr/include/libavutil/mem.h: 539
if _libs["avcodec"].has("av_dynarray_add_nofree", "cdecl"):
    av_dynarray_add_nofree = _libs["avcodec"].get("av_dynarray_add_nofree", "cdecl")
    av_dynarray_add_nofree.argtypes = [POINTER(None), POINTER(c_int), POINTER(None)]
    av_dynarray_add_nofree.restype = c_int

# /usr/include/libavutil/mem.h: 564
if _libs["avcodec"].has("av_dynarray2_add", "cdecl"):
    av_dynarray2_add = _libs["avcodec"].get("av_dynarray2_add", "cdecl")
    av_dynarray2_add.argtypes = [POINTER(POINTER(None)), POINTER(c_int), c_size_t, POINTER(uint8_t)]
    av_dynarray2_add.restype = POINTER(c_ubyte)
    av_dynarray2_add.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/mem.h: 587
if _libs["avcodec"].has("av_size_mult", "cdecl"):
    av_size_mult = _libs["avcodec"].get("av_size_mult", "cdecl")
    av_size_mult.argtypes = [c_size_t, c_size_t, POINTER(c_size_t)]
    av_size_mult.restype = c_int

# /usr/include/libavutil/mem.h: 602
if _libs["avcodec"].has("av_max_alloc", "cdecl"):
    av_max_alloc = _libs["avcodec"].get("av_max_alloc", "cdecl")
    av_max_alloc.argtypes = [c_size_t]
    av_max_alloc.restype = None

# /usr/include/libavutil/error.h: 99
if _libs["avcodec"].has("av_strerror", "cdecl"):
    av_strerror = _libs["avcodec"].get("av_strerror", "cdecl")
    av_strerror.argtypes = [c_int, String, c_size_t]
    av_strerror.restype = c_int

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
if _libs["avcodec"].has("av_reduce", "cdecl"):
    av_reduce = _libs["avcodec"].get("av_reduce", "cdecl")
    av_reduce.argtypes = [POINTER(c_int), POINTER(c_int), c_int64, c_int64, c_int64]
    av_reduce.restype = c_int

# /usr/include/libavutil/rational.h: 128
if _libs["avcodec"].has("av_mul_q", "cdecl"):
    av_mul_q = _libs["avcodec"].get("av_mul_q", "cdecl")
    av_mul_q.argtypes = [AVRational, AVRational]
    av_mul_q.restype = AVRational

# /usr/include/libavutil/rational.h: 136
if _libs["avcodec"].has("av_div_q", "cdecl"):
    av_div_q = _libs["avcodec"].get("av_div_q", "cdecl")
    av_div_q.argtypes = [AVRational, AVRational]
    av_div_q.restype = AVRational

# /usr/include/libavutil/rational.h: 144
if _libs["avcodec"].has("av_add_q", "cdecl"):
    av_add_q = _libs["avcodec"].get("av_add_q", "cdecl")
    av_add_q.argtypes = [AVRational, AVRational]
    av_add_q.restype = AVRational

# /usr/include/libavutil/rational.h: 152
if _libs["avcodec"].has("av_sub_q", "cdecl"):
    av_sub_q = _libs["avcodec"].get("av_sub_q", "cdecl")
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
if _libs["avcodec"].has("av_d2q", "cdecl"):
    av_d2q = _libs["avcodec"].get("av_d2q", "cdecl")
    av_d2q.argtypes = [c_double, c_int]
    av_d2q.restype = AVRational

# /usr/include/libavutil/rational.h: 189
if _libs["avcodec"].has("av_nearer_q", "cdecl"):
    av_nearer_q = _libs["avcodec"].get("av_nearer_q", "cdecl")
    av_nearer_q.argtypes = [AVRational, AVRational, AVRational]
    av_nearer_q.restype = c_int

# /usr/include/libavutil/rational.h: 198
if _libs["avcodec"].has("av_find_nearest_q_idx", "cdecl"):
    av_find_nearest_q_idx = _libs["avcodec"].get("av_find_nearest_q_idx", "cdecl")
    av_find_nearest_q_idx.argtypes = [AVRational, POINTER(AVRational)]
    av_find_nearest_q_idx.restype = c_int

# /usr/include/libavutil/rational.h: 209
if _libs["avcodec"].has("av_q2intfloat", "cdecl"):
    av_q2intfloat = _libs["avcodec"].get("av_q2intfloat", "cdecl")
    av_q2intfloat.argtypes = [AVRational]
    av_q2intfloat.restype = uint32_t

# /usr/include/libavutil/rational.h: 215
if _libs["avcodec"].has("av_gcd_q", "cdecl"):
    av_gcd_q = _libs["avcodec"].get("av_gcd_q", "cdecl")
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
    ('i', uint32_t),
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
    ('i', uint64_t),
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

# /usr/include/libavutil/mathematics.h: 119
if _libs["avcodec"].has("av_gcd", "cdecl"):
    av_gcd = _libs["avcodec"].get("av_gcd", "cdecl")
    av_gcd.argtypes = [c_int64, c_int64]
    av_gcd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 131
if _libs["avcodec"].has("av_rescale", "cdecl"):
    av_rescale = _libs["avcodec"].get("av_rescale", "cdecl")
    av_rescale.argtypes = [c_int64, c_int64, c_int64]
    av_rescale.restype = c_int64

# /usr/include/libavutil/mathematics.h: 142
if _libs["avcodec"].has("av_rescale_rnd", "cdecl"):
    av_rescale_rnd = _libs["avcodec"].get("av_rescale_rnd", "cdecl")
    av_rescale_rnd.argtypes = [c_int64, c_int64, c_int64, enum_AVRounding]
    av_rescale_rnd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 153
if _libs["avcodec"].has("av_rescale_q", "cdecl"):
    av_rescale_q = _libs["avcodec"].get("av_rescale_q", "cdecl")
    av_rescale_q.argtypes = [c_int64, AVRational, AVRational]
    av_rescale_q.restype = c_int64

# /usr/include/libavutil/mathematics.h: 162
if _libs["avcodec"].has("av_rescale_q_rnd", "cdecl"):
    av_rescale_q_rnd = _libs["avcodec"].get("av_rescale_q_rnd", "cdecl")
    av_rescale_q_rnd.argtypes = [c_int64, AVRational, AVRational, enum_AVRounding]
    av_rescale_q_rnd.restype = c_int64

# /usr/include/libavutil/mathematics.h: 177
if _libs["avcodec"].has("av_compare_ts", "cdecl"):
    av_compare_ts = _libs["avcodec"].get("av_compare_ts", "cdecl")
    av_compare_ts.argtypes = [c_int64, AVRational, c_int64, AVRational]
    av_compare_ts.restype = c_int

# /usr/include/libavutil/mathematics.h: 198
if _libs["avcodec"].has("av_compare_mod", "cdecl"):
    av_compare_mod = _libs["avcodec"].get("av_compare_mod", "cdecl")
    av_compare_mod.argtypes = [uint64_t, uint64_t, uint64_t]
    av_compare_mod.restype = c_int64

# /usr/include/libavutil/mathematics.h: 225
if _libs["avcodec"].has("av_rescale_delta", "cdecl"):
    av_rescale_delta = _libs["avcodec"].get("av_rescale_delta", "cdecl")
    av_rescale_delta.argtypes = [AVRational, c_int64, AVRational, c_int, POINTER(c_int64), AVRational]
    av_rescale_delta.restype = c_int64

# /usr/include/libavutil/mathematics.h: 238
if _libs["avcodec"].has("av_add_stable", "cdecl"):
    av_add_stable = _libs["avcodec"].get("av_add_stable", "cdecl")
    av_add_stable.argtypes = [AVRational, c_int64, AVRational, c_int64]
    av_add_stable.restype = c_int64

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

AV_PIX_FMT_VAAPI = (AV_PIX_FMT_BGR555LE + 1)# /usr/include/libavutil/pixfmt.h: 64

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

AV_PIX_FMT_X2BGR10LE = (AV_PIX_FMT_X2RGB10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_X2BGR10BE = (AV_PIX_FMT_X2BGR10LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P210BE = (AV_PIX_FMT_X2BGR10BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P210LE = (AV_PIX_FMT_P210BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P410BE = (AV_PIX_FMT_P210LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P410LE = (AV_PIX_FMT_P410BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P216BE = (AV_PIX_FMT_P410LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P216LE = (AV_PIX_FMT_P216BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P416BE = (AV_PIX_FMT_P216LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P416LE = (AV_PIX_FMT_P416BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VUYA = (AV_PIX_FMT_P416LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBAF16BE = (AV_PIX_FMT_VUYA + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBAF16LE = (AV_PIX_FMT_RGBAF16BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_VUYX = (AV_PIX_FMT_RGBAF16LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P012LE = (AV_PIX_FMT_VUYX + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_P012BE = (AV_PIX_FMT_P012LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_Y212BE = (AV_PIX_FMT_P012BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_Y212LE = (AV_PIX_FMT_Y212BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XV30BE = (AV_PIX_FMT_Y212LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XV30LE = (AV_PIX_FMT_XV30BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XV36BE = (AV_PIX_FMT_XV30LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_XV36LE = (AV_PIX_FMT_XV36BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBF32BE = (AV_PIX_FMT_XV36LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBF32LE = (AV_PIX_FMT_RGBF32BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBAF32BE = (AV_PIX_FMT_RGBF32LE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_RGBAF32LE = (AV_PIX_FMT_RGBAF32BE + 1)# /usr/include/libavutil/pixfmt.h: 64

AV_PIX_FMT_NB = (AV_PIX_FMT_RGBAF32LE + 1)# /usr/include/libavutil/pixfmt.h: 64

enum_AVColorPrimaries = c_int# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_RESERVED0 = 0# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_BT709 = 1# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_BT470M = 4# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_BT470BG = 5# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_FILM = 8# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_BT2020 = 9# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTE428 = 10# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTEST428_1 = AVCOL_PRI_SMPTE428# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTE431 = 11# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_SMPTE432 = 12# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_EBU3213 = 22# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_JEDEC_P22 = AVCOL_PRI_EBU3213# /usr/include/libavutil/pixfmt.h: 533

AVCOL_PRI_NB = (AVCOL_PRI_JEDEC_P22 + 1)# /usr/include/libavutil/pixfmt.h: 533

enum_AVColorTransferCharacteristic = c_int# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_RESERVED0 = 0# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_BT709 = 1# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_GAMMA22 = 4# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_GAMMA28 = 5# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_LINEAR = 8# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_LOG = 9# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_LOG_SQRT = 10# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_IEC61966_2_4 = 11# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_BT1361_ECG = 12# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_IEC61966_2_1 = 13# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_BT2020_10 = 14# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_BT2020_12 = 15# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTE2084 = 16# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTEST2084 = AVCOL_TRC_SMPTE2084# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTE428 = 17# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_SMPTEST428_1 = AVCOL_TRC_SMPTE428# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_ARIB_STD_B67 = 18# /usr/include/libavutil/pixfmt.h: 558

AVCOL_TRC_NB = (AVCOL_TRC_ARIB_STD_B67 + 1)# /usr/include/libavutil/pixfmt.h: 558

enum_AVColorSpace = c_int# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_RGB = 0# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_BT709 = 1# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_UNSPECIFIED = 2# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_RESERVED = 3# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_FCC = 4# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_BT470BG = 5# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_SMPTE170M = 6# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_SMPTE240M = 7# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_YCGCO = 8# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_YCOCG = AVCOL_SPC_YCGCO# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_BT2020_NCL = 9# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_BT2020_CL = 10# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_SMPTE2085 = 11# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_CHROMA_DERIVED_NCL = 12# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_CHROMA_DERIVED_CL = 13# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_ICTCP = 14# /usr/include/libavutil/pixfmt.h: 587

AVCOL_SPC_NB = (AVCOL_SPC_ICTCP + 1)# /usr/include/libavutil/pixfmt.h: 587

enum_AVColorRange = c_int# /usr/include/libavutil/pixfmt.h: 626

AVCOL_RANGE_UNSPECIFIED = 0# /usr/include/libavutil/pixfmt.h: 626

AVCOL_RANGE_MPEG = 1# /usr/include/libavutil/pixfmt.h: 626

AVCOL_RANGE_JPEG = 2# /usr/include/libavutil/pixfmt.h: 626

AVCOL_RANGE_NB = (AVCOL_RANGE_JPEG + 1)# /usr/include/libavutil/pixfmt.h: 626

enum_AVChromaLocation = c_int# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_UNSPECIFIED = 0# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_LEFT = 1# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_CENTER = 2# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_TOPLEFT = 3# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_TOP = 4# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_BOTTOMLEFT = 5# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_BOTTOM = 6# /usr/include/libavutil/pixfmt.h: 680

AVCHROMA_LOC_NB = (AVCHROMA_LOC_BOTTOM + 1)# /usr/include/libavutil/pixfmt.h: 680

# /usr/include/libavutil/avutil.h: 321
if _libs["avcodec"].has("av_int_list_length_for_size", "cdecl"):
    av_int_list_length_for_size = _libs["avcodec"].get("av_int_list_length_for_size", "cdecl")
    av_int_list_length_for_size.argtypes = [c_uint, POINTER(None), uint64_t]
    av_int_list_length_for_size.restype = c_uint

# /usr/include/libavutil/avutil.h: 344
if _libs["avcodec"].has("av_fopen_utf8", "cdecl"):
    av_fopen_utf8 = _libs["avcodec"].get("av_fopen_utf8", "cdecl")
    av_fopen_utf8.argtypes = [String, String]
    av_fopen_utf8.restype = POINTER(FILE)

# /usr/include/libavutil/avutil.h: 350
if _libs["avcodec"].has("av_get_time_base_q", "cdecl"):
    av_get_time_base_q = _libs["avcodec"].get("av_get_time_base_q", "cdecl")
    av_get_time_base_q.argtypes = []
    av_get_time_base_q.restype = AVRational

# /usr/include/libavutil/avutil.h: 364
if _libs["avcodec"].has("av_fourcc_make_string", "cdecl"):
    av_fourcc_make_string = _libs["avcodec"].get("av_fourcc_make_string", "cdecl")
    av_fourcc_make_string.argtypes = [String, uint32_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_fourcc_make_string.restype = ReturnString
    else:
        av_fourcc_make_string.restype = String
        av_fourcc_make_string.errcheck = ReturnString

# /usr/include/libavutil/buffer.h: 74
class struct_AVBuffer(Structure):
    pass

AVBuffer = struct_AVBuffer# /usr/include/libavutil/buffer.h: 74

# /usr/include/libavutil/buffer.h: 95
class struct_AVBufferRef(Structure):
    pass

struct_AVBufferRef.__slots__ = [
    'buffer',
    'data',
    'size',
]
struct_AVBufferRef._fields_ = [
    ('buffer', POINTER(AVBuffer)),
    ('data', POINTER(uint8_t)),
    ('size', c_size_t),
]

AVBufferRef = struct_AVBufferRef# /usr/include/libavutil/buffer.h: 95

# /usr/include/libavutil/buffer.h: 102
if _libs["avcodec"].has("av_buffer_alloc", "cdecl"):
    av_buffer_alloc = _libs["avcodec"].get("av_buffer_alloc", "cdecl")
    av_buffer_alloc.argtypes = [c_size_t]
    av_buffer_alloc.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 108
if _libs["avcodec"].has("av_buffer_allocz", "cdecl"):
    av_buffer_allocz = _libs["avcodec"].get("av_buffer_allocz", "cdecl")
    av_buffer_allocz.argtypes = [c_size_t]
    av_buffer_allocz.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 131
if _libs["avcodec"].has("av_buffer_create", "cdecl"):
    av_buffer_create = _libs["avcodec"].get("av_buffer_create", "cdecl")
    av_buffer_create.argtypes = [POINTER(uint8_t), c_size_t, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t)), POINTER(None), c_int]
    av_buffer_create.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 140
if _libs["avcodec"].has("av_buffer_default_free", "cdecl"):
    av_buffer_default_free = _libs["avcodec"].get("av_buffer_default_free", "cdecl")
    av_buffer_default_free.argtypes = [POINTER(None), POINTER(uint8_t)]
    av_buffer_default_free.restype = None

# /usr/include/libavutil/buffer.h: 148
if _libs["avcodec"].has("av_buffer_ref", "cdecl"):
    av_buffer_ref = _libs["avcodec"].get("av_buffer_ref", "cdecl")
    av_buffer_ref.argtypes = [POINTER(AVBufferRef)]
    av_buffer_ref.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 156
if _libs["avcodec"].has("av_buffer_unref", "cdecl"):
    av_buffer_unref = _libs["avcodec"].get("av_buffer_unref", "cdecl")
    av_buffer_unref.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_unref.restype = None

# /usr/include/libavutil/buffer.h: 164
if _libs["avcodec"].has("av_buffer_is_writable", "cdecl"):
    av_buffer_is_writable = _libs["avcodec"].get("av_buffer_is_writable", "cdecl")
    av_buffer_is_writable.argtypes = [POINTER(AVBufferRef)]
    av_buffer_is_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 169
if _libs["avcodec"].has("av_buffer_get_opaque", "cdecl"):
    av_buffer_get_opaque = _libs["avcodec"].get("av_buffer_get_opaque", "cdecl")
    av_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/buffer.h: 171
if _libs["avcodec"].has("av_buffer_get_ref_count", "cdecl"):
    av_buffer_get_ref_count = _libs["avcodec"].get("av_buffer_get_ref_count", "cdecl")
    av_buffer_get_ref_count.argtypes = [POINTER(AVBufferRef)]
    av_buffer_get_ref_count.restype = c_int

# /usr/include/libavutil/buffer.h: 182
if _libs["avcodec"].has("av_buffer_make_writable", "cdecl"):
    av_buffer_make_writable = _libs["avcodec"].get("av_buffer_make_writable", "cdecl")
    av_buffer_make_writable.argtypes = [POINTER(POINTER(AVBufferRef))]
    av_buffer_make_writable.restype = c_int

# /usr/include/libavutil/buffer.h: 199
if _libs["avcodec"].has("av_buffer_realloc", "cdecl"):
    av_buffer_realloc = _libs["avcodec"].get("av_buffer_realloc", "cdecl")
    av_buffer_realloc.argtypes = [POINTER(POINTER(AVBufferRef)), c_size_t]
    av_buffer_realloc.restype = c_int

# /usr/include/libavutil/buffer.h: 215
if _libs["avcodec"].has("av_buffer_replace", "cdecl"):
    av_buffer_replace = _libs["avcodec"].get("av_buffer_replace", "cdecl")
    av_buffer_replace.argtypes = [POINTER(POINTER(AVBufferRef)), POINTER(AVBufferRef)]
    av_buffer_replace.restype = c_int

# /usr/include/libavutil/buffer.h: 255
class struct_AVBufferPool(Structure):
    pass

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 255

# /usr/include/libavutil/buffer.h: 266
if _libs["avcodec"].has("av_buffer_pool_init", "cdecl"):
    av_buffer_pool_init = _libs["avcodec"].get("av_buffer_pool_init", "cdecl")
    av_buffer_pool_init.argtypes = [c_size_t, CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), c_size_t)]
    av_buffer_pool_init.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 283
if _libs["avcodec"].has("av_buffer_pool_init2", "cdecl"):
    av_buffer_pool_init2 = _libs["avcodec"].get("av_buffer_pool_init2", "cdecl")
    av_buffer_pool_init2.argtypes = [c_size_t, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(AVBufferRef)), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    av_buffer_pool_init2.restype = POINTER(AVBufferPool)

# /usr/include/libavutil/buffer.h: 295
if _libs["avcodec"].has("av_buffer_pool_uninit", "cdecl"):
    av_buffer_pool_uninit = _libs["avcodec"].get("av_buffer_pool_uninit", "cdecl")
    av_buffer_pool_uninit.argtypes = [POINTER(POINTER(AVBufferPool))]
    av_buffer_pool_uninit.restype = None

# /usr/include/libavutil/buffer.h: 303
if _libs["avcodec"].has("av_buffer_pool_get", "cdecl"):
    av_buffer_pool_get = _libs["avcodec"].get("av_buffer_pool_get", "cdecl")
    av_buffer_pool_get.argtypes = [POINTER(AVBufferPool)]
    av_buffer_pool_get.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/buffer.h: 316
if _libs["avcodec"].has("av_buffer_pool_buffer_get_opaque", "cdecl"):
    av_buffer_pool_buffer_get_opaque = _libs["avcodec"].get("av_buffer_pool_buffer_get_opaque", "cdecl")
    av_buffer_pool_buffer_get_opaque.argtypes = [POINTER(AVBufferRef)]
    av_buffer_pool_buffer_get_opaque.restype = POINTER(c_ubyte)
    av_buffer_pool_buffer_get_opaque.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/dict.h: 92
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

AVDictionaryEntry = struct_AVDictionaryEntry# /usr/include/libavutil/dict.h: 92

# /usr/include/libavutil/dict.h: 94
class struct_AVDictionary(Structure):
    pass

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 94

# /usr/include/libavutil/dict.h: 110
if _libs["avcodec"].has("av_dict_get", "cdecl"):
    av_dict_get = _libs["avcodec"].get("av_dict_get", "cdecl")
    av_dict_get.argtypes = [POINTER(AVDictionary), String, POINTER(AVDictionaryEntry), c_int]
    av_dict_get.restype = POINTER(AVDictionaryEntry)

# /usr/include/libavutil/dict.h: 137
if _libs["avcodec"].has("av_dict_iterate", "cdecl"):
    av_dict_iterate = _libs["avcodec"].get("av_dict_iterate", "cdecl")
    av_dict_iterate.argtypes = [POINTER(AVDictionary), POINTER(AVDictionaryEntry)]
    av_dict_iterate.restype = POINTER(AVDictionaryEntry)

# /usr/include/libavutil/dict.h: 146
if _libs["avcodec"].has("av_dict_count", "cdecl"):
    av_dict_count = _libs["avcodec"].get("av_dict_count", "cdecl")
    av_dict_count.argtypes = [POINTER(AVDictionary)]
    av_dict_count.restype = c_int

# /usr/include/libavutil/dict.h: 165
if _libs["avcodec"].has("av_dict_set", "cdecl"):
    av_dict_set = _libs["avcodec"].get("av_dict_set", "cdecl")
    av_dict_set.argtypes = [POINTER(POINTER(AVDictionary)), String, String, c_int]
    av_dict_set.restype = c_int

# /usr/include/libavutil/dict.h: 173
if _libs["avcodec"].has("av_dict_set_int", "cdecl"):
    av_dict_set_int = _libs["avcodec"].get("av_dict_set_int", "cdecl")
    av_dict_set_int.argtypes = [POINTER(POINTER(AVDictionary)), String, c_int64, c_int]
    av_dict_set_int.restype = c_int

# /usr/include/libavutil/dict.h: 192
if _libs["avcodec"].has("av_dict_parse_string", "cdecl"):
    av_dict_parse_string = _libs["avcodec"].get("av_dict_parse_string", "cdecl")
    av_dict_parse_string.argtypes = [POINTER(POINTER(AVDictionary)), String, String, String, c_int]
    av_dict_parse_string.restype = c_int

# /usr/include/libavutil/dict.h: 209
if _libs["avcodec"].has("av_dict_copy", "cdecl"):
    av_dict_copy = _libs["avcodec"].get("av_dict_copy", "cdecl")
    av_dict_copy.argtypes = [POINTER(POINTER(AVDictionary)), POINTER(AVDictionary), c_int]
    av_dict_copy.restype = c_int

# /usr/include/libavutil/dict.h: 215
if _libs["avcodec"].has("av_dict_free", "cdecl"):
    av_dict_free = _libs["avcodec"].get("av_dict_free", "cdecl")
    av_dict_free.argtypes = [POINTER(POINTER(AVDictionary))]
    av_dict_free.restype = None

# /usr/include/libavutil/dict.h: 234
if _libs["avcodec"].has("av_dict_get_string", "cdecl"):
    av_dict_get_string = _libs["avcodec"].get("av_dict_get_string", "cdecl")
    av_dict_get_string.argtypes = [POINTER(AVDictionary), POINTER(POINTER(c_char)), c_char, c_char]
    av_dict_get_string.restype = c_int

enum_AVChannel = c_int# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_NONE = (-1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_FRONT_LEFT = (AV_CHAN_NONE + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_FRONT_RIGHT = (AV_CHAN_FRONT_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_FRONT_CENTER = (AV_CHAN_FRONT_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_LOW_FREQUENCY = (AV_CHAN_FRONT_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BACK_LEFT = (AV_CHAN_LOW_FREQUENCY + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BACK_RIGHT = (AV_CHAN_BACK_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_FRONT_LEFT_OF_CENTER = (AV_CHAN_BACK_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_FRONT_RIGHT_OF_CENTER = (AV_CHAN_FRONT_LEFT_OF_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BACK_CENTER = (AV_CHAN_FRONT_RIGHT_OF_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_SIDE_LEFT = (AV_CHAN_BACK_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_SIDE_RIGHT = (AV_CHAN_SIDE_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_CENTER = (AV_CHAN_SIDE_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_FRONT_LEFT = (AV_CHAN_TOP_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_FRONT_CENTER = (AV_CHAN_TOP_FRONT_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_FRONT_RIGHT = (AV_CHAN_TOP_FRONT_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_BACK_LEFT = (AV_CHAN_TOP_FRONT_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_BACK_CENTER = (AV_CHAN_TOP_BACK_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_BACK_RIGHT = (AV_CHAN_TOP_BACK_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_STEREO_LEFT = 29# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_STEREO_RIGHT = (AV_CHAN_STEREO_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_WIDE_LEFT = (AV_CHAN_STEREO_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_WIDE_RIGHT = (AV_CHAN_WIDE_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_SURROUND_DIRECT_LEFT = (AV_CHAN_WIDE_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_SURROUND_DIRECT_RIGHT = (AV_CHAN_SURROUND_DIRECT_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_LOW_FREQUENCY_2 = (AV_CHAN_SURROUND_DIRECT_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_SIDE_LEFT = (AV_CHAN_LOW_FREQUENCY_2 + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_TOP_SIDE_RIGHT = (AV_CHAN_TOP_SIDE_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BOTTOM_FRONT_CENTER = (AV_CHAN_TOP_SIDE_RIGHT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BOTTOM_FRONT_LEFT = (AV_CHAN_BOTTOM_FRONT_CENTER + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_BOTTOM_FRONT_RIGHT = (AV_CHAN_BOTTOM_FRONT_LEFT + 1)# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_UNUSED = 0x200# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_UNKNOWN = 0x300# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_AMBISONIC_BASE = 0x400# /usr/include/libavutil/channel_layout.h: 47

AV_CHAN_AMBISONIC_END = 0x7ff# /usr/include/libavutil/channel_layout.h: 47

enum_AVChannelOrder = c_int# /usr/include/libavutil/channel_layout.h: 107

AV_CHANNEL_ORDER_UNSPEC = 0# /usr/include/libavutil/channel_layout.h: 107

AV_CHANNEL_ORDER_NATIVE = (AV_CHANNEL_ORDER_UNSPEC + 1)# /usr/include/libavutil/channel_layout.h: 107

AV_CHANNEL_ORDER_CUSTOM = (AV_CHANNEL_ORDER_NATIVE + 1)# /usr/include/libavutil/channel_layout.h: 107

AV_CHANNEL_ORDER_AMBISONIC = (AV_CHANNEL_ORDER_CUSTOM + 1)# /usr/include/libavutil/channel_layout.h: 107

enum_AVMatrixEncoding = c_int# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_NONE = 0# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DOLBY = (AV_MATRIX_ENCODING_NONE + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DPLII = (AV_MATRIX_ENCODING_DOLBY + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DPLIIX = (AV_MATRIX_ENCODING_DPLII + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DPLIIZ = (AV_MATRIX_ENCODING_DPLIIX + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DOLBYEX = (AV_MATRIX_ENCODING_DPLIIZ + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_DOLBYHEADPHONE = (AV_MATRIX_ENCODING_DOLBYEX + 1)# /usr/include/libavutil/channel_layout.h: 242

AV_MATRIX_ENCODING_NB = (AV_MATRIX_ENCODING_DOLBYHEADPHONE + 1)# /usr/include/libavutil/channel_layout.h: 242

# /usr/include/libavutil/channel_layout.h: 269
class struct_AVChannelCustom(Structure):
    pass

struct_AVChannelCustom.__slots__ = [
    'id',
    'name',
    'opaque',
]
struct_AVChannelCustom._fields_ = [
    ('id', enum_AVChannel),
    ('name', c_char * int(16)),
    ('opaque', POINTER(None)),
]

AVChannelCustom = struct_AVChannelCustom# /usr/include/libavutil/channel_layout.h: 269

# /usr/include/libavutil/channel_layout.h: 318
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'mask',
    'map',
]
union_anon_24._fields_ = [
    ('mask', uint64_t),
    ('map', POINTER(AVChannelCustom)),
]

# /usr/include/libavutil/channel_layout.h: 359
class struct_AVChannelLayout(Structure):
    pass

struct_AVChannelLayout.__slots__ = [
    'order',
    'nb_channels',
    'u',
    'opaque',
]
struct_AVChannelLayout._fields_ = [
    ('order', enum_AVChannelOrder),
    ('nb_channels', c_int),
    ('u', union_anon_24),
    ('opaque', POINTER(None)),
]

AVChannelLayout = struct_AVChannelLayout# /usr/include/libavutil/channel_layout.h: 359

# /home/josiah/ctypesgen_test/av/av/bprint.h: 93
class struct_AVBPrint(Structure):
    pass

# /usr/include/libavutil/channel_layout.h: 431
if _libs["avcodec"].has("av_get_channel_layout", "cdecl"):
    av_get_channel_layout = _libs["avcodec"].get("av_get_channel_layout", "cdecl")
    av_get_channel_layout.argtypes = [String]
    av_get_channel_layout.restype = uint64_t

# /usr/include/libavutil/channel_layout.h: 447
if _libs["avcodec"].has("av_get_extended_channel_layout", "cdecl"):
    av_get_extended_channel_layout = _libs["avcodec"].get("av_get_extended_channel_layout", "cdecl")
    av_get_extended_channel_layout.argtypes = [String, POINTER(uint64_t), POINTER(c_int)]
    av_get_extended_channel_layout.restype = c_int

# /usr/include/libavutil/channel_layout.h: 460
if _libs["avcodec"].has("av_get_channel_layout_string", "cdecl"):
    av_get_channel_layout_string = _libs["avcodec"].get("av_get_channel_layout_string", "cdecl")
    av_get_channel_layout_string.argtypes = [String, c_int, c_int, uint64_t]
    av_get_channel_layout_string.restype = None

# /usr/include/libavutil/channel_layout.h: 467
if _libs["avcodec"].has("av_bprint_channel_layout", "cdecl"):
    av_bprint_channel_layout = _libs["avcodec"].get("av_bprint_channel_layout", "cdecl")
    av_bprint_channel_layout.argtypes = [POINTER(struct_AVBPrint), c_int, uint64_t]
    av_bprint_channel_layout.restype = None

# /usr/include/libavutil/channel_layout.h: 474
if _libs["avcodec"].has("av_get_channel_layout_nb_channels", "cdecl"):
    av_get_channel_layout_nb_channels = _libs["avcodec"].get("av_get_channel_layout_nb_channels", "cdecl")
    av_get_channel_layout_nb_channels.argtypes = [uint64_t]
    av_get_channel_layout_nb_channels.restype = c_int

# /usr/include/libavutil/channel_layout.h: 482
if _libs["avcodec"].has("av_get_default_channel_layout", "cdecl"):
    av_get_default_channel_layout = _libs["avcodec"].get("av_get_default_channel_layout", "cdecl")
    av_get_default_channel_layout.argtypes = [c_int]
    av_get_default_channel_layout.restype = c_int64

# /usr/include/libavutil/channel_layout.h: 497
if _libs["avcodec"].has("av_get_channel_layout_channel_index", "cdecl"):
    av_get_channel_layout_channel_index = _libs["avcodec"].get("av_get_channel_layout_channel_index", "cdecl")
    av_get_channel_layout_channel_index.argtypes = [uint64_t, uint64_t]
    av_get_channel_layout_channel_index.restype = c_int

# /usr/include/libavutil/channel_layout.h: 505
if _libs["avcodec"].has("av_channel_layout_extract_channel", "cdecl"):
    av_channel_layout_extract_channel = _libs["avcodec"].get("av_channel_layout_extract_channel", "cdecl")
    av_channel_layout_extract_channel.argtypes = [uint64_t, c_int]
    av_channel_layout_extract_channel.restype = uint64_t

# /usr/include/libavutil/channel_layout.h: 515
if _libs["avcodec"].has("av_get_channel_name", "cdecl"):
    av_get_channel_name = _libs["avcodec"].get("av_get_channel_name", "cdecl")
    av_get_channel_name.argtypes = [uint64_t]
    av_get_channel_name.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 525
if _libs["avcodec"].has("av_get_channel_description", "cdecl"):
    av_get_channel_description = _libs["avcodec"].get("av_get_channel_description", "cdecl")
    av_get_channel_description.argtypes = [uint64_t]
    av_get_channel_description.restype = c_char_p

# /usr/include/libavutil/channel_layout.h: 538
if _libs["avcodec"].has("av_get_standard_channel_layout", "cdecl"):
    av_get_standard_channel_layout = _libs["avcodec"].get("av_get_standard_channel_layout", "cdecl")
    av_get_standard_channel_layout.argtypes = [c_uint, POINTER(uint64_t), POINTER(POINTER(c_char))]
    av_get_standard_channel_layout.restype = c_int

# /usr/include/libavutil/channel_layout.h: 556
if _libs["avcodec"].has("av_channel_name", "cdecl"):
    av_channel_name = _libs["avcodec"].get("av_channel_name", "cdecl")
    av_channel_name.argtypes = [String, c_size_t, enum_AVChannel]
    av_channel_name.restype = c_int

# /usr/include/libavutil/channel_layout.h: 563
if _libs["avcodec"].has("av_channel_name_bprint", "cdecl"):
    av_channel_name_bprint = _libs["avcodec"].get("av_channel_name_bprint", "cdecl")
    av_channel_name_bprint.argtypes = [POINTER(struct_AVBPrint), enum_AVChannel]
    av_channel_name_bprint.restype = None

# /usr/include/libavutil/channel_layout.h: 575
if _libs["avcodec"].has("av_channel_description", "cdecl"):
    av_channel_description = _libs["avcodec"].get("av_channel_description", "cdecl")
    av_channel_description.argtypes = [String, c_size_t, enum_AVChannel]
    av_channel_description.restype = c_int

# /usr/include/libavutil/channel_layout.h: 582
if _libs["avcodec"].has("av_channel_description_bprint", "cdecl"):
    av_channel_description_bprint = _libs["avcodec"].get("av_channel_description_bprint", "cdecl")
    av_channel_description_bprint.argtypes = [POINTER(struct_AVBPrint), enum_AVChannel]
    av_channel_description_bprint.restype = None

# /usr/include/libavutil/channel_layout.h: 590
if _libs["avcodec"].has("av_channel_from_string", "cdecl"):
    av_channel_from_string = _libs["avcodec"].get("av_channel_from_string", "cdecl")
    av_channel_from_string.argtypes = [String]
    av_channel_from_string.restype = enum_AVChannel

# /usr/include/libavutil/channel_layout.h: 602
if _libs["avcodec"].has("av_channel_layout_from_mask", "cdecl"):
    av_channel_layout_from_mask = _libs["avcodec"].get("av_channel_layout_from_mask", "cdecl")
    av_channel_layout_from_mask.argtypes = [POINTER(AVChannelLayout), uint64_t]
    av_channel_layout_from_mask.restype = c_int

# /usr/include/libavutil/channel_layout.h: 621
if _libs["avcodec"].has("av_channel_layout_from_string", "cdecl"):
    av_channel_layout_from_string = _libs["avcodec"].get("av_channel_layout_from_string", "cdecl")
    av_channel_layout_from_string.argtypes = [POINTER(AVChannelLayout), String]
    av_channel_layout_from_string.restype = c_int

# /usr/include/libavutil/channel_layout.h: 630
if _libs["avcodec"].has("av_channel_layout_default", "cdecl"):
    av_channel_layout_default = _libs["avcodec"].get("av_channel_layout_default", "cdecl")
    av_channel_layout_default.argtypes = [POINTER(AVChannelLayout), c_int]
    av_channel_layout_default.restype = None

# /usr/include/libavutil/channel_layout.h: 641
if _libs["avcodec"].has("av_channel_layout_standard", "cdecl"):
    av_channel_layout_standard = _libs["avcodec"].get("av_channel_layout_standard", "cdecl")
    av_channel_layout_standard.argtypes = [POINTER(POINTER(None))]
    av_channel_layout_standard.restype = POINTER(AVChannelLayout)

# /usr/include/libavutil/channel_layout.h: 649
if _libs["avcodec"].has("av_channel_layout_uninit", "cdecl"):
    av_channel_layout_uninit = _libs["avcodec"].get("av_channel_layout_uninit", "cdecl")
    av_channel_layout_uninit.argtypes = [POINTER(AVChannelLayout)]
    av_channel_layout_uninit.restype = None

# /usr/include/libavutil/channel_layout.h: 661
if _libs["avcodec"].has("av_channel_layout_copy", "cdecl"):
    av_channel_layout_copy = _libs["avcodec"].get("av_channel_layout_copy", "cdecl")
    av_channel_layout_copy.argtypes = [POINTER(AVChannelLayout), POINTER(AVChannelLayout)]
    av_channel_layout_copy.restype = c_int

# /usr/include/libavutil/channel_layout.h: 676
if _libs["avcodec"].has("av_channel_layout_describe", "cdecl"):
    av_channel_layout_describe = _libs["avcodec"].get("av_channel_layout_describe", "cdecl")
    av_channel_layout_describe.argtypes = [POINTER(AVChannelLayout), String, c_size_t]
    av_channel_layout_describe.restype = c_int

# /usr/include/libavutil/channel_layout.h: 685
if _libs["avcodec"].has("av_channel_layout_describe_bprint", "cdecl"):
    av_channel_layout_describe_bprint = _libs["avcodec"].get("av_channel_layout_describe_bprint", "cdecl")
    av_channel_layout_describe_bprint.argtypes = [POINTER(AVChannelLayout), POINTER(struct_AVBPrint)]
    av_channel_layout_describe_bprint.restype = c_int

# /usr/include/libavutil/channel_layout.h: 698
if _libs["avcodec"].has("av_channel_layout_channel_from_index", "cdecl"):
    av_channel_layout_channel_from_index = _libs["avcodec"].get("av_channel_layout_channel_from_index", "cdecl")
    av_channel_layout_channel_from_index.argtypes = [POINTER(AVChannelLayout), c_uint]
    av_channel_layout_channel_from_index.restype = enum_AVChannel

# /usr/include/libavutil/channel_layout.h: 709
if _libs["avcodec"].has("av_channel_layout_index_from_channel", "cdecl"):
    av_channel_layout_index_from_channel = _libs["avcodec"].get("av_channel_layout_index_from_channel", "cdecl")
    av_channel_layout_index_from_channel.argtypes = [POINTER(AVChannelLayout), enum_AVChannel]
    av_channel_layout_index_from_channel.restype = c_int

# /usr/include/libavutil/channel_layout.h: 724
if _libs["avcodec"].has("av_channel_layout_index_from_string", "cdecl"):
    av_channel_layout_index_from_string = _libs["avcodec"].get("av_channel_layout_index_from_string", "cdecl")
    av_channel_layout_index_from_string.argtypes = [POINTER(AVChannelLayout), String]
    av_channel_layout_index_from_string.restype = c_int

# /usr/include/libavutil/channel_layout.h: 740
if _libs["avcodec"].has("av_channel_layout_channel_from_string", "cdecl"):
    av_channel_layout_channel_from_string = _libs["avcodec"].get("av_channel_layout_channel_from_string", "cdecl")
    av_channel_layout_channel_from_string.argtypes = [POINTER(AVChannelLayout), String]
    av_channel_layout_channel_from_string.restype = enum_AVChannel

# /usr/include/libavutil/channel_layout.h: 752
if _libs["avcodec"].has("av_channel_layout_subset", "cdecl"):
    av_channel_layout_subset = _libs["avcodec"].get("av_channel_layout_subset", "cdecl")
    av_channel_layout_subset.argtypes = [POINTER(AVChannelLayout), uint64_t]
    av_channel_layout_subset.restype = uint64_t

# /usr/include/libavutil/channel_layout.h: 762
if _libs["avcodec"].has("av_channel_layout_check", "cdecl"):
    av_channel_layout_check = _libs["avcodec"].get("av_channel_layout_check", "cdecl")
    av_channel_layout_check.argtypes = [POINTER(AVChannelLayout)]
    av_channel_layout_check.restype = c_int

# /usr/include/libavutil/channel_layout.h: 777
if _libs["avcodec"].has("av_channel_layout_compare", "cdecl"):
    av_channel_layout_compare = _libs["avcodec"].get("av_channel_layout_compare", "cdecl")
    av_channel_layout_compare.argtypes = [POINTER(AVChannelLayout), POINTER(AVChannelLayout)]
    av_channel_layout_compare.restype = c_int

enum_AVFrameSideDataType = c_int# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_PANSCAN = 0# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_A53_CC = (AV_FRAME_DATA_PANSCAN + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_STEREO3D = (AV_FRAME_DATA_A53_CC + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_MATRIXENCODING = (AV_FRAME_DATA_STEREO3D + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DOWNMIX_INFO = (AV_FRAME_DATA_MATRIXENCODING + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_REPLAYGAIN = (AV_FRAME_DATA_DOWNMIX_INFO + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DISPLAYMATRIX = (AV_FRAME_DATA_REPLAYGAIN + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_AFD = (AV_FRAME_DATA_DISPLAYMATRIX + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_MOTION_VECTORS = (AV_FRAME_DATA_AFD + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_SKIP_SAMPLES = (AV_FRAME_DATA_MOTION_VECTORS + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_AUDIO_SERVICE_TYPE = (AV_FRAME_DATA_SKIP_SAMPLES + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_MASTERING_DISPLAY_METADATA = (AV_FRAME_DATA_AUDIO_SERVICE_TYPE + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_GOP_TIMECODE = (AV_FRAME_DATA_MASTERING_DISPLAY_METADATA + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_SPHERICAL = (AV_FRAME_DATA_GOP_TIMECODE + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_CONTENT_LIGHT_LEVEL = (AV_FRAME_DATA_SPHERICAL + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_ICC_PROFILE = (AV_FRAME_DATA_CONTENT_LIGHT_LEVEL + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_S12M_TIMECODE = (AV_FRAME_DATA_ICC_PROFILE + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DYNAMIC_HDR_PLUS = (AV_FRAME_DATA_S12M_TIMECODE + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_REGIONS_OF_INTEREST = (AV_FRAME_DATA_DYNAMIC_HDR_PLUS + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_VIDEO_ENC_PARAMS = (AV_FRAME_DATA_REGIONS_OF_INTEREST + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_SEI_UNREGISTERED = (AV_FRAME_DATA_VIDEO_ENC_PARAMS + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_FILM_GRAIN_PARAMS = (AV_FRAME_DATA_SEI_UNREGISTERED + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DETECTION_BBOXES = (AV_FRAME_DATA_FILM_GRAIN_PARAMS + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DOVI_RPU_BUFFER = (AV_FRAME_DATA_DETECTION_BBOXES + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DOVI_METADATA = (AV_FRAME_DATA_DOVI_RPU_BUFFER + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_DYNAMIC_HDR_VIVID = (AV_FRAME_DATA_DOVI_METADATA + 1)# /usr/include/libavutil/frame.h: 49

AV_FRAME_DATA_AMBIENT_VIEWING_ENVIRONMENT = (AV_FRAME_DATA_DYNAMIC_HDR_VIVID + 1)# /usr/include/libavutil/frame.h: 49

enum_AVActiveFormatDescription = c_int# /usr/include/libavutil/frame.h: 219

AV_AFD_SAME = 8# /usr/include/libavutil/frame.h: 219

AV_AFD_4_3 = 9# /usr/include/libavutil/frame.h: 219

AV_AFD_16_9 = 10# /usr/include/libavutil/frame.h: 219

AV_AFD_14_9 = 11# /usr/include/libavutil/frame.h: 219

AV_AFD_4_3_SP_14_9 = 13# /usr/include/libavutil/frame.h: 219

AV_AFD_16_9_SP_14_9 = 14# /usr/include/libavutil/frame.h: 219

AV_AFD_SP_4_3 = 15# /usr/include/libavutil/frame.h: 219

# /usr/include/libavutil/frame.h: 242
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
    ('data', POINTER(uint8_t)),
    ('size', c_size_t),
    ('metadata', POINTER(AVDictionary)),
    ('buf', POINTER(AVBufferRef)),
]

AVFrameSideData = struct_AVFrameSideData# /usr/include/libavutil/frame.h: 242

# /usr/include/libavutil/frame.h: 298
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
    ('self_size', uint32_t),
    ('top', c_int),
    ('bottom', c_int),
    ('left', c_int),
    ('right', c_int),
    ('qoffset', AVRational),
]

AVRegionOfInterest = struct_AVRegionOfInterest# /usr/include/libavutil/frame.h: 298

# /usr/include/libavutil/frame.h: 729
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
    'pkt_dts',
    'time_base',
    'coded_picture_number',
    'display_picture_number',
    'quality',
    'opaque',
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
    'hw_frames_ctx',
    'opaque_ref',
    'crop_top',
    'crop_bottom',
    'crop_left',
    'crop_right',
    'private_ref',
    'ch_layout',
    'duration',
]
struct_AVFrame._fields_ = [
    ('data', POINTER(uint8_t) * int(8)),
    ('linesize', c_int * int(8)),
    ('extended_data', POINTER(POINTER(uint8_t))),
    ('width', c_int),
    ('height', c_int),
    ('nb_samples', c_int),
    ('format', c_int),
    ('key_frame', c_int),
    ('pict_type', enum_AVPictureType),
    ('sample_aspect_ratio', AVRational),
    ('pts', c_int64),
    ('pkt_dts', c_int64),
    ('time_base', AVRational),
    ('coded_picture_number', c_int),
    ('display_picture_number', c_int),
    ('quality', c_int),
    ('opaque', POINTER(None)),
    ('repeat_pict', c_int),
    ('interlaced_frame', c_int),
    ('top_field_first', c_int),
    ('palette_has_changed', c_int),
    ('reordered_opaque', c_int64),
    ('sample_rate', c_int),
    ('channel_layout', uint64_t),
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
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('opaque_ref', POINTER(AVBufferRef)),
    ('crop_top', c_size_t),
    ('crop_bottom', c_size_t),
    ('crop_left', c_size_t),
    ('crop_right', c_size_t),
    ('private_ref', POINTER(AVBufferRef)),
    ('ch_layout', AVChannelLayout),
    ('duration', c_int64),
]

AVFrame = struct_AVFrame# /usr/include/libavutil/frame.h: 729

# /usr/include/libavutil/frame.h: 742
if _libs["avcodec"].has("av_frame_alloc", "cdecl"):
    av_frame_alloc = _libs["avcodec"].get("av_frame_alloc", "cdecl")
    av_frame_alloc.argtypes = []
    av_frame_alloc.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 751
if _libs["avcodec"].has("av_frame_free", "cdecl"):
    av_frame_free = _libs["avcodec"].get("av_frame_free", "cdecl")
    av_frame_free.argtypes = [POINTER(POINTER(AVFrame))]
    av_frame_free.restype = None

# /usr/include/libavutil/frame.h: 768
if _libs["avcodec"].has("av_frame_ref", "cdecl"):
    av_frame_ref = _libs["avcodec"].get("av_frame_ref", "cdecl")
    av_frame_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_ref.restype = c_int

# /usr/include/libavutil/frame.h: 777
if _libs["avcodec"].has("av_frame_clone", "cdecl"):
    av_frame_clone = _libs["avcodec"].get("av_frame_clone", "cdecl")
    av_frame_clone.argtypes = [POINTER(AVFrame)]
    av_frame_clone.restype = POINTER(AVFrame)

# /usr/include/libavutil/frame.h: 782
if _libs["avcodec"].has("av_frame_unref", "cdecl"):
    av_frame_unref = _libs["avcodec"].get("av_frame_unref", "cdecl")
    av_frame_unref.argtypes = [POINTER(AVFrame)]
    av_frame_unref.restype = None

# /usr/include/libavutil/frame.h: 791
if _libs["avcodec"].has("av_frame_move_ref", "cdecl"):
    av_frame_move_ref = _libs["avcodec"].get("av_frame_move_ref", "cdecl")
    av_frame_move_ref.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_move_ref.restype = None

# /usr/include/libavutil/frame.h: 816
if _libs["avcodec"].has("av_frame_get_buffer", "cdecl"):
    av_frame_get_buffer = _libs["avcodec"].get("av_frame_get_buffer", "cdecl")
    av_frame_get_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_buffer.restype = c_int

# /usr/include/libavutil/frame.h: 830
if _libs["avcodec"].has("av_frame_is_writable", "cdecl"):
    av_frame_is_writable = _libs["avcodec"].get("av_frame_is_writable", "cdecl")
    av_frame_is_writable.argtypes = [POINTER(AVFrame)]
    av_frame_is_writable.restype = c_int

# /usr/include/libavutil/frame.h: 844
if _libs["avcodec"].has("av_frame_make_writable", "cdecl"):
    av_frame_make_writable = _libs["avcodec"].get("av_frame_make_writable", "cdecl")
    av_frame_make_writable.argtypes = [POINTER(AVFrame)]
    av_frame_make_writable.restype = c_int

# /usr/include/libavutil/frame.h: 857
if _libs["avcodec"].has("av_frame_copy", "cdecl"):
    av_frame_copy = _libs["avcodec"].get("av_frame_copy", "cdecl")
    av_frame_copy.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy.restype = c_int

# /usr/include/libavutil/frame.h: 867
if _libs["avcodec"].has("av_frame_copy_props", "cdecl"):
    av_frame_copy_props = _libs["avcodec"].get("av_frame_copy_props", "cdecl")
    av_frame_copy_props.argtypes = [POINTER(AVFrame), POINTER(AVFrame)]
    av_frame_copy_props.restype = c_int

# /usr/include/libavutil/frame.h: 878
if _libs["avcodec"].has("av_frame_get_plane_buffer", "cdecl"):
    av_frame_get_plane_buffer = _libs["avcodec"].get("av_frame_get_plane_buffer", "cdecl")
    av_frame_get_plane_buffer.argtypes = [POINTER(AVFrame), c_int]
    av_frame_get_plane_buffer.restype = POINTER(AVBufferRef)

# /usr/include/libavutil/frame.h: 889
if _libs["avcodec"].has("av_frame_new_side_data", "cdecl"):
    av_frame_new_side_data = _libs["avcodec"].get("av_frame_new_side_data", "cdecl")
    av_frame_new_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, c_size_t]
    av_frame_new_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 905
if _libs["avcodec"].has("av_frame_new_side_data_from_buf", "cdecl"):
    av_frame_new_side_data_from_buf = _libs["avcodec"].get("av_frame_new_side_data_from_buf", "cdecl")
    av_frame_new_side_data_from_buf.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType, POINTER(AVBufferRef)]
    av_frame_new_side_data_from_buf.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 913
if _libs["avcodec"].has("av_frame_get_side_data", "cdecl"):
    av_frame_get_side_data = _libs["avcodec"].get("av_frame_get_side_data", "cdecl")
    av_frame_get_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_get_side_data.restype = POINTER(AVFrameSideData)

# /usr/include/libavutil/frame.h: 919
if _libs["avcodec"].has("av_frame_remove_side_data", "cdecl"):
    av_frame_remove_side_data = _libs["avcodec"].get("av_frame_remove_side_data", "cdecl")
    av_frame_remove_side_data.argtypes = [POINTER(AVFrame), enum_AVFrameSideDataType]
    av_frame_remove_side_data.restype = None

enum_anon_25 = c_int# /usr/include/libavutil/frame.h: 925

AV_FRAME_CROP_UNALIGNED = (1 << 0)# /usr/include/libavutil/frame.h: 925

# /usr/include/libavutil/frame.h: 953
if _libs["avcodec"].has("av_frame_apply_cropping", "cdecl"):
    av_frame_apply_cropping = _libs["avcodec"].get("av_frame_apply_cropping", "cdecl")
    av_frame_apply_cropping.argtypes = [POINTER(AVFrame), c_int]
    av_frame_apply_cropping.restype = c_int

# /usr/include/libavutil/frame.h: 958
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

enum_anon_26 = c_int# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_READ = (1 << 0)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_WRITE = (1 << 1)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_OVERWRITE = (1 << 2)# /usr/include/libavutil/hwcontext.h: 520

AV_HWFRAME_MAP_DIRECT = (1 << 3)# /usr/include/libavutil/hwcontext.h: 520

# /usr/include/libavutil/hwcontext.h: 583
if _libs["avcodec"].has("av_hwframe_map", "cdecl"):
    av_hwframe_map = _libs["avcodec"].get("av_hwframe_map", "cdecl")
    av_hwframe_map.argtypes = [POINTER(AVFrame), POINTER(AVFrame), c_int]
    av_hwframe_map.restype = c_int

# /usr/include/libavutil/hwcontext.h: 604
if _libs["avcodec"].has("av_hwframe_ctx_create_derived", "cdecl"):
    av_hwframe_ctx_create_derived = _libs["avcodec"].get("av_hwframe_ctx_create_derived", "cdecl")
    av_hwframe_ctx_create_derived.argtypes = [POINTER(POINTER(AVBufferRef)), enum_AVPixelFormat, POINTER(AVBufferRef), POINTER(AVBufferRef), c_int]
    av_hwframe_ctx_create_derived.restype = c_int

enum_AVCodecID = c_int# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_NONE = 0# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEG1VIDEO = (AV_CODEC_ID_NONE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEG2VIDEO = (AV_CODEC_ID_MPEG1VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_H261 = (AV_CODEC_ID_MPEG2VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_H263 = (AV_CODEC_ID_H261 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RV10 = (AV_CODEC_ID_H263 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RV20 = (AV_CODEC_ID_RV10 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MJPEG = (AV_CODEC_ID_RV20 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MJPEGB = (AV_CODEC_ID_MJPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_LJPEG = (AV_CODEC_ID_MJPEGB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SP5X = (AV_CODEC_ID_LJPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_JPEGLS = (AV_CODEC_ID_SP5X + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEG4 = (AV_CODEC_ID_JPEGLS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RAWVIDEO = (AV_CODEC_ID_MPEG4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSMPEG4V1 = (AV_CODEC_ID_RAWVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSMPEG4V2 = (AV_CODEC_ID_MSMPEG4V1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSMPEG4V3 = (AV_CODEC_ID_MSMPEG4V2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMV1 = (AV_CODEC_ID_MSMPEG4V3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMV2 = (AV_CODEC_ID_WMV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_H263P = (AV_CODEC_ID_WMV2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_H263I = (AV_CODEC_ID_H263P + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FLV1 = (AV_CODEC_ID_H263I + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SVQ1 = (AV_CODEC_ID_FLV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SVQ3 = (AV_CODEC_ID_SVQ1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVVIDEO = (AV_CODEC_ID_SVQ3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HUFFYUV = (AV_CODEC_ID_DVVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CYUV = (AV_CODEC_ID_HUFFYUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_H264 = (AV_CODEC_ID_CYUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INDEO3 = (AV_CODEC_ID_H264 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP3 = (AV_CODEC_ID_INDEO3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_THEORA = (AV_CODEC_ID_VP3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ASV1 = (AV_CODEC_ID_THEORA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ASV2 = (AV_CODEC_ID_ASV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FFV1 = (AV_CODEC_ID_ASV2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_4XM = (AV_CODEC_ID_FFV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VCR1 = (AV_CODEC_ID_4XM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CLJR = (AV_CODEC_ID_VCR1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MDEC = (AV_CODEC_ID_CLJR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ROQ = (AV_CODEC_ID_MDEC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INTERPLAY_VIDEO = (AV_CODEC_ID_ROQ + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XAN_WC3 = (AV_CODEC_ID_INTERPLAY_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XAN_WC4 = (AV_CODEC_ID_XAN_WC3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RPZA = (AV_CODEC_ID_XAN_WC4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CINEPAK = (AV_CODEC_ID_RPZA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WS_VQA = (AV_CODEC_ID_CINEPAK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSRLE = (AV_CODEC_ID_WS_VQA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSVIDEO1 = (AV_CODEC_ID_MSRLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IDCIN = (AV_CODEC_ID_MSVIDEO1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_8BPS = (AV_CODEC_ID_IDCIN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMC = (AV_CODEC_ID_8BPS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FLIC = (AV_CODEC_ID_SMC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TRUEMOTION1 = (AV_CODEC_ID_FLIC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VMDVIDEO = (AV_CODEC_ID_TRUEMOTION1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSZH = (AV_CODEC_ID_VMDVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ZLIB = (AV_CODEC_ID_MSZH + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QTRLE = (AV_CODEC_ID_ZLIB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TSCC = (AV_CODEC_ID_QTRLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ULTI = (AV_CODEC_ID_TSCC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QDRAW = (AV_CODEC_ID_ULTI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VIXL = (AV_CODEC_ID_QDRAW + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QPEG = (AV_CODEC_ID_VIXL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PNG = (AV_CODEC_ID_QPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PPM = (AV_CODEC_ID_PNG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PBM = (AV_CODEC_ID_PPM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PGM = (AV_CODEC_ID_PBM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PGMYUV = (AV_CODEC_ID_PGM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PAM = (AV_CODEC_ID_PGMYUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FFVHUFF = (AV_CODEC_ID_PAM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RV30 = (AV_CODEC_ID_FFVHUFF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RV40 = (AV_CODEC_ID_RV30 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VC1 = (AV_CODEC_ID_RV40 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMV3 = (AV_CODEC_ID_VC1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_LOCO = (AV_CODEC_ID_WMV3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WNV1 = (AV_CODEC_ID_LOCO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AASC = (AV_CODEC_ID_WNV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INDEO2 = (AV_CODEC_ID_AASC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FRAPS = (AV_CODEC_ID_INDEO2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TRUEMOTION2 = (AV_CODEC_ID_FRAPS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BMP = (AV_CODEC_ID_TRUEMOTION2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CSCD = (AV_CODEC_ID_BMP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MMVIDEO = (AV_CODEC_ID_CSCD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ZMBV = (AV_CODEC_ID_MMVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVS = (AV_CODEC_ID_ZMBV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMACKVIDEO = (AV_CODEC_ID_AVS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_NUV = (AV_CODEC_ID_SMACKVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_KMVC = (AV_CODEC_ID_NUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FLASHSV = (AV_CODEC_ID_KMVC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CAVS = (AV_CODEC_ID_FLASHSV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_JPEG2000 = (AV_CODEC_ID_CAVS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VMNC = (AV_CODEC_ID_JPEG2000 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP5 = (AV_CODEC_ID_VMNC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP6 = (AV_CODEC_ID_VP5 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP6F = (AV_CODEC_ID_VP6 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TARGA = (AV_CODEC_ID_VP6F + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSICINVIDEO = (AV_CODEC_ID_TARGA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TIERTEXSEQVIDEO = (AV_CODEC_ID_DSICINVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TIFF = (AV_CODEC_ID_TIERTEXSEQVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GIF = (AV_CODEC_ID_TIFF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DXA = (AV_CODEC_ID_GIF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DNXHD = (AV_CODEC_ID_DXA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_THP = (AV_CODEC_ID_DNXHD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SGI = (AV_CODEC_ID_THP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_C93 = (AV_CODEC_ID_SGI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BETHSOFTVID = (AV_CODEC_ID_C93 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PTX = (AV_CODEC_ID_BETHSOFTVID + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TXD = (AV_CODEC_ID_PTX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP6A = (AV_CODEC_ID_TXD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AMV = (AV_CODEC_ID_VP6A + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VB = (AV_CODEC_ID_AMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCX = (AV_CODEC_ID_VB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SUNRAST = (AV_CODEC_ID_PCX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INDEO4 = (AV_CODEC_ID_SUNRAST + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INDEO5 = (AV_CODEC_ID_INDEO4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MIMIC = (AV_CODEC_ID_INDEO5 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RL2 = (AV_CODEC_ID_MIMIC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ESCAPE124 = (AV_CODEC_ID_RL2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DIRAC = (AV_CODEC_ID_ESCAPE124 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BFI = (AV_CODEC_ID_DIRAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CMV = (AV_CODEC_ID_BFI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MOTIONPIXELS = (AV_CODEC_ID_CMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TGV = (AV_CODEC_ID_MOTIONPIXELS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TGQ = (AV_CODEC_ID_TGV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TQI = (AV_CODEC_ID_TGQ + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AURA = (AV_CODEC_ID_TQI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AURA2 = (AV_CODEC_ID_AURA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_V210X = (AV_CODEC_ID_AURA2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TMV = (AV_CODEC_ID_V210X + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_V210 = (AV_CODEC_ID_TMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DPX = (AV_CODEC_ID_V210 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MAD = (AV_CODEC_ID_DPX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FRWU = (AV_CODEC_ID_MAD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FLASHSV2 = (AV_CODEC_ID_FRWU + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CDGRAPHICS = (AV_CODEC_ID_FLASHSV2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_R210 = (AV_CODEC_ID_CDGRAPHICS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ANM = (AV_CODEC_ID_R210 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BINKVIDEO = (AV_CODEC_ID_ANM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IFF_ILBM = (AV_CODEC_ID_BINKVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_KGV1 = (AV_CODEC_ID_IFF_ILBM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_YOP = (AV_CODEC_ID_KGV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP8 = (AV_CODEC_ID_YOP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PICTOR = (AV_CODEC_ID_VP8 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ANSI = (AV_CODEC_ID_PICTOR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_A64_MULTI = (AV_CODEC_ID_ANSI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_A64_MULTI5 = (AV_CODEC_ID_A64_MULTI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_R10K = (AV_CODEC_ID_A64_MULTI5 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MXPEG = (AV_CODEC_ID_R10K + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_LAGARITH = (AV_CODEC_ID_MXPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PRORES = (AV_CODEC_ID_LAGARITH + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_JV = (AV_CODEC_ID_PRORES + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DFA = (AV_CODEC_ID_JV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMV3IMAGE = (AV_CODEC_ID_DFA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VC1IMAGE = (AV_CODEC_ID_WMV3IMAGE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_UTVIDEO = (AV_CODEC_ID_VC1IMAGE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BMV_VIDEO = (AV_CODEC_ID_UTVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VBLE = (AV_CODEC_ID_BMV_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DXTORY = (AV_CODEC_ID_VBLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_V410 = (AV_CODEC_ID_DXTORY + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XWD = (AV_CODEC_ID_V410 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CDXL = (AV_CODEC_ID_XWD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XBM = (AV_CODEC_ID_CDXL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ZEROCODEC = (AV_CODEC_ID_XBM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSS1 = (AV_CODEC_ID_ZEROCODEC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSA1 = (AV_CODEC_ID_MSS1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TSCC2 = (AV_CODEC_ID_MSA1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MTS2 = (AV_CODEC_ID_TSCC2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CLLC = (AV_CODEC_ID_MTS2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSS2 = (AV_CODEC_ID_CLLC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP9 = (AV_CODEC_ID_MSS2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AIC = (AV_CODEC_ID_VP9 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ESCAPE130 = (AV_CODEC_ID_AIC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_G2M = (AV_CODEC_ID_ESCAPE130 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WEBP = (AV_CODEC_ID_G2M + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HNM4_VIDEO = (AV_CODEC_ID_WEBP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HEVC = (AV_CODEC_ID_HNM4_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FIC = (AV_CODEC_ID_HEVC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ALIAS_PIX = (AV_CODEC_ID_FIC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BRENDER_PIX = (AV_CODEC_ID_ALIAS_PIX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PAF_VIDEO = (AV_CODEC_ID_BRENDER_PIX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_EXR = (AV_CODEC_ID_PAF_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP7 = (AV_CODEC_ID_EXR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SANM = (AV_CODEC_ID_VP7 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SGIRLE = (AV_CODEC_ID_SANM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MVC1 = (AV_CODEC_ID_SGIRLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MVC2 = (AV_CODEC_ID_MVC1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HQX = (AV_CODEC_ID_MVC2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TDSC = (AV_CODEC_ID_HQX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HQ_HQA = (AV_CODEC_ID_TDSC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HAP = (AV_CODEC_ID_HQ_HQA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DDS = (AV_CODEC_ID_HAP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DXV = (AV_CODEC_ID_DDS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SCREENPRESSO = (AV_CODEC_ID_DXV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RSCC = (AV_CODEC_ID_SCREENPRESSO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVS2 = (AV_CODEC_ID_RSCC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PGX = (AV_CODEC_ID_AVS2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVS3 = (AV_CODEC_ID_PGX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSP2 = (AV_CODEC_ID_AVS3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VVC = (AV_CODEC_ID_MSP2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_Y41P = (AV_CODEC_ID_VVC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVRP = (AV_CODEC_ID_Y41P + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_012V = (AV_CODEC_ID_AVRP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVUI = (AV_CODEC_ID_012V + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AYUV = (AV_CODEC_ID_AVUI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TARGA_Y216 = (AV_CODEC_ID_AYUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_V308 = (AV_CODEC_ID_TARGA_Y216 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_V408 = (AV_CODEC_ID_V308 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_YUV4 = (AV_CODEC_ID_V408 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AVRN = (AV_CODEC_ID_YUV4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CPIA = (AV_CODEC_ID_AVRN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XFACE = (AV_CODEC_ID_CPIA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SNOW = (AV_CODEC_ID_XFACE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMVJPEG = (AV_CODEC_ID_SNOW + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_APNG = (AV_CODEC_ID_SMVJPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DAALA = (AV_CODEC_ID_APNG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CFHD = (AV_CODEC_ID_DAALA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TRUEMOTION2RT = (AV_CODEC_ID_CFHD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_M101 = (AV_CODEC_ID_TRUEMOTION2RT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MAGICYUV = (AV_CODEC_ID_M101 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SHEERVIDEO = (AV_CODEC_ID_MAGICYUV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_YLC = (AV_CODEC_ID_SHEERVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PSD = (AV_CODEC_ID_YLC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PIXLET = (AV_CODEC_ID_PSD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SPEEDHQ = (AV_CODEC_ID_PIXLET + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FMVC = (AV_CODEC_ID_SPEEDHQ + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SCPR = (AV_CODEC_ID_FMVC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CLEARVIDEO = (AV_CODEC_ID_SCPR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XPM = (AV_CODEC_ID_CLEARVIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AV1 = (AV_CODEC_ID_XPM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BITPACKED = (AV_CODEC_ID_AV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSCC = (AV_CODEC_ID_BITPACKED + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SRGC = (AV_CODEC_ID_MSCC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SVG = (AV_CODEC_ID_SRGC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GDV = (AV_CODEC_ID_SVG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FITS = (AV_CODEC_ID_GDV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IMM4 = (AV_CODEC_ID_FITS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PROSUMER = (AV_CODEC_ID_IMM4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MWSC = (AV_CODEC_ID_PROSUMER + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WCMV = (AV_CODEC_ID_MWSC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RASC = (AV_CODEC_ID_WCMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HYMT = (AV_CODEC_ID_RASC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ARBC = (AV_CODEC_ID_HYMT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AGM = (AV_CODEC_ID_ARBC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_LSCR = (AV_CODEC_ID_AGM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VP4 = (AV_CODEC_ID_LSCR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IMM5 = (AV_CODEC_ID_VP4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MVDV = (AV_CODEC_ID_IMM5 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MVHA = (AV_CODEC_ID_MVDV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CDTOONS = (AV_CODEC_ID_MVHA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MV30 = (AV_CODEC_ID_CDTOONS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_NOTCHLC = (AV_CODEC_ID_MV30 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PFM = (AV_CODEC_ID_NOTCHLC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MOBICLIP = (AV_CODEC_ID_PFM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PHOTOCD = (AV_CODEC_ID_MOBICLIP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IPU = (AV_CODEC_ID_PHOTOCD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ARGO = (AV_CODEC_ID_IPU + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CRI = (AV_CODEC_ID_ARGO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SIMBIOSIS_IMX = (AV_CODEC_ID_CRI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SGA_VIDEO = (AV_CODEC_ID_SIMBIOSIS_IMX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GEM = (AV_CODEC_ID_SGA_VIDEO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VBN = (AV_CODEC_ID_GEM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_JPEGXL = (AV_CODEC_ID_VBN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QOI = (AV_CODEC_ID_JPEGXL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PHM = (AV_CODEC_ID_QOI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RADIANCE_HDR = (AV_CODEC_ID_PHM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WBMP = (AV_CODEC_ID_RADIANCE_HDR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MEDIA100 = (AV_CODEC_ID_WBMP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VQC = (AV_CODEC_ID_MEDIA100 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FIRST_AUDIO = 0x10000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S16LE = 0x10000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S16BE = (AV_CODEC_ID_PCM_S16LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U16LE = (AV_CODEC_ID_PCM_S16BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U16BE = (AV_CODEC_ID_PCM_U16LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S8 = (AV_CODEC_ID_PCM_U16BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U8 = (AV_CODEC_ID_PCM_S8 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_MULAW = (AV_CODEC_ID_PCM_U8 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_ALAW = (AV_CODEC_ID_PCM_MULAW + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S32LE = (AV_CODEC_ID_PCM_ALAW + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S32BE = (AV_CODEC_ID_PCM_S32LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U32LE = (AV_CODEC_ID_PCM_S32BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U32BE = (AV_CODEC_ID_PCM_U32LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S24LE = (AV_CODEC_ID_PCM_U32BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S24BE = (AV_CODEC_ID_PCM_S24LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U24LE = (AV_CODEC_ID_PCM_S24BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_U24BE = (AV_CODEC_ID_PCM_U24LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S24DAUD = (AV_CODEC_ID_PCM_U24BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_ZORK = (AV_CODEC_ID_PCM_S24DAUD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S16LE_PLANAR = (AV_CODEC_ID_PCM_ZORK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_DVD = (AV_CODEC_ID_PCM_S16LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F32BE = (AV_CODEC_ID_PCM_DVD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F32LE = (AV_CODEC_ID_PCM_F32BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F64BE = (AV_CODEC_ID_PCM_F32LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F64LE = (AV_CODEC_ID_PCM_F64BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_BLURAY = (AV_CODEC_ID_PCM_F64LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_LXF = (AV_CODEC_ID_PCM_BLURAY + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_S302M = (AV_CODEC_ID_PCM_LXF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S8_PLANAR = (AV_CODEC_ID_S302M + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S24LE_PLANAR = (AV_CODEC_ID_PCM_S8_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S32LE_PLANAR = (AV_CODEC_ID_PCM_S24LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S16BE_PLANAR = (AV_CODEC_ID_PCM_S32LE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S64LE = (AV_CODEC_ID_PCM_S16BE_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_S64BE = (AV_CODEC_ID_PCM_S64LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F16LE = (AV_CODEC_ID_PCM_S64BE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_F24LE = (AV_CODEC_ID_PCM_F16LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_VIDC = (AV_CODEC_ID_PCM_F24LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PCM_SGA = (AV_CODEC_ID_PCM_VIDC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_QT = 0x11000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_WAV = (AV_CODEC_ID_ADPCM_IMA_QT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_DK3 = (AV_CODEC_ID_ADPCM_IMA_WAV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_DK4 = (AV_CODEC_ID_ADPCM_IMA_DK3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_WS = (AV_CODEC_ID_ADPCM_IMA_DK4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_SMJPEG = (AV_CODEC_ID_ADPCM_IMA_WS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_MS = (AV_CODEC_ID_ADPCM_IMA_SMJPEG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_4XM = (AV_CODEC_ID_ADPCM_MS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_XA = (AV_CODEC_ID_ADPCM_4XM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_ADX = (AV_CODEC_ID_ADPCM_XA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA = (AV_CODEC_ID_ADPCM_ADX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_G726 = (AV_CODEC_ID_ADPCM_EA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_CT = (AV_CODEC_ID_ADPCM_G726 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_SWF = (AV_CODEC_ID_ADPCM_CT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_YAMAHA = (AV_CODEC_ID_ADPCM_SWF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_SBPRO_4 = (AV_CODEC_ID_ADPCM_YAMAHA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_SBPRO_3 = (AV_CODEC_ID_ADPCM_SBPRO_4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_SBPRO_2 = (AV_CODEC_ID_ADPCM_SBPRO_3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_THP = (AV_CODEC_ID_ADPCM_SBPRO_2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_AMV = (AV_CODEC_ID_ADPCM_THP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA_R1 = (AV_CODEC_ID_ADPCM_IMA_AMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA_R3 = (AV_CODEC_ID_ADPCM_EA_R1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA_R2 = (AV_CODEC_ID_ADPCM_EA_R3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_EA_SEAD = (AV_CODEC_ID_ADPCM_EA_R2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_EA_EACS = (AV_CODEC_ID_ADPCM_IMA_EA_SEAD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA_XAS = (AV_CODEC_ID_ADPCM_IMA_EA_EACS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_EA_MAXIS_XA = (AV_CODEC_ID_ADPCM_EA_XAS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_ISS = (AV_CODEC_ID_ADPCM_EA_MAXIS_XA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_G722 = (AV_CODEC_ID_ADPCM_IMA_ISS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_APC = (AV_CODEC_ID_ADPCM_G722 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_VIMA = (AV_CODEC_ID_ADPCM_IMA_APC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_AFC = (AV_CODEC_ID_ADPCM_VIMA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_OKI = (AV_CODEC_ID_ADPCM_AFC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_DTK = (AV_CODEC_ID_ADPCM_IMA_OKI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_RAD = (AV_CODEC_ID_ADPCM_DTK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_G726LE = (AV_CODEC_ID_ADPCM_IMA_RAD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_THP_LE = (AV_CODEC_ID_ADPCM_G726LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_PSX = (AV_CODEC_ID_ADPCM_THP_LE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_AICA = (AV_CODEC_ID_ADPCM_PSX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_DAT4 = (AV_CODEC_ID_ADPCM_AICA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_MTAF = (AV_CODEC_ID_ADPCM_IMA_DAT4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_AGM = (AV_CODEC_ID_ADPCM_MTAF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_ARGO = (AV_CODEC_ID_ADPCM_AGM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_SSI = (AV_CODEC_ID_ADPCM_ARGO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_ZORK = (AV_CODEC_ID_ADPCM_IMA_SSI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_APM = (AV_CODEC_ID_ADPCM_ZORK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_ALP = (AV_CODEC_ID_ADPCM_IMA_APM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_MTF = (AV_CODEC_ID_ADPCM_IMA_ALP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_CUNNING = (AV_CODEC_ID_ADPCM_IMA_MTF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_MOFLEX = (AV_CODEC_ID_ADPCM_IMA_CUNNING + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_IMA_ACORN = (AV_CODEC_ID_ADPCM_IMA_MOFLEX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ADPCM_XMD = (AV_CODEC_ID_ADPCM_IMA_ACORN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AMR_NB = 0x12000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AMR_WB = (AV_CODEC_ID_AMR_NB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RA_144 = 0x13000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RA_288 = (AV_CODEC_ID_RA_144 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ROQ_DPCM = 0x14000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INTERPLAY_DPCM = (AV_CODEC_ID_ROQ_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XAN_DPCM = (AV_CODEC_ID_INTERPLAY_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SOL_DPCM = (AV_CODEC_ID_XAN_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SDX2_DPCM = (AV_CODEC_ID_SOL_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GREMLIN_DPCM = (AV_CODEC_ID_SDX2_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DERF_DPCM = (AV_CODEC_ID_GREMLIN_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WADY_DPCM = (AV_CODEC_ID_DERF_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CBD2_DPCM = (AV_CODEC_ID_WADY_DPCM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP2 = 0x15000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP3 = (AV_CODEC_ID_MP2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AAC = (AV_CODEC_ID_MP3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AC3 = (AV_CODEC_ID_AAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DTS = (AV_CODEC_ID_AC3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VORBIS = (AV_CODEC_ID_DTS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVAUDIO = (AV_CODEC_ID_VORBIS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMAV1 = (AV_CODEC_ID_DVAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMAV2 = (AV_CODEC_ID_WMAV1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MACE3 = (AV_CODEC_ID_WMAV2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MACE6 = (AV_CODEC_ID_MACE3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VMDAUDIO = (AV_CODEC_ID_MACE6 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FLAC = (AV_CODEC_ID_VMDAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP3ADU = (AV_CODEC_ID_FLAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP3ON4 = (AV_CODEC_ID_MP3ADU + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SHORTEN = (AV_CODEC_ID_MP3ON4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ALAC = (AV_CODEC_ID_SHORTEN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WESTWOOD_SND1 = (AV_CODEC_ID_ALAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GSM = (AV_CODEC_ID_WESTWOOD_SND1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QDM2 = (AV_CODEC_ID_GSM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_COOK = (AV_CODEC_ID_QDM2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TRUESPEECH = (AV_CODEC_ID_COOK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TTA = (AV_CODEC_ID_TRUESPEECH + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMACKAUDIO = (AV_CODEC_ID_TTA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QCELP = (AV_CODEC_ID_SMACKAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WAVPACK = (AV_CODEC_ID_QCELP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSICINAUDIO = (AV_CODEC_ID_WAVPACK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IMC = (AV_CODEC_ID_DSICINAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MUSEPACK7 = (AV_CODEC_ID_IMC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MLP = (AV_CODEC_ID_MUSEPACK7 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_GSM_MS = (AV_CODEC_ID_MLP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC3 = (AV_CODEC_ID_GSM_MS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_APE = (AV_CODEC_ID_ATRAC3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_NELLYMOSER = (AV_CODEC_ID_APE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MUSEPACK8 = (AV_CODEC_ID_NELLYMOSER + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SPEEX = (AV_CODEC_ID_MUSEPACK8 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMAVOICE = (AV_CODEC_ID_SPEEX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMAPRO = (AV_CODEC_ID_WMAVOICE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WMALOSSLESS = (AV_CODEC_ID_WMAPRO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC3P = (AV_CODEC_ID_WMALOSSLESS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_EAC3 = (AV_CODEC_ID_ATRAC3P + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SIPR = (AV_CODEC_ID_EAC3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP1 = (AV_CODEC_ID_SIPR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TWINVQ = (AV_CODEC_ID_MP1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TRUEHD = (AV_CODEC_ID_TWINVQ + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MP4ALS = (AV_CODEC_ID_TRUEHD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC1 = (AV_CODEC_ID_MP4ALS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BINKAUDIO_RDFT = (AV_CODEC_ID_ATRAC1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BINKAUDIO_DCT = (AV_CODEC_ID_BINKAUDIO_RDFT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_AAC_LATM = (AV_CODEC_ID_BINKAUDIO_DCT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_QDMC = (AV_CODEC_ID_AAC_LATM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CELT = (AV_CODEC_ID_QDMC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_G723_1 = (AV_CODEC_ID_CELT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_G729 = (AV_CODEC_ID_G723_1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_8SVX_EXP = (AV_CODEC_ID_G729 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_8SVX_FIB = (AV_CODEC_ID_8SVX_EXP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BMV_AUDIO = (AV_CODEC_ID_8SVX_FIB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RALF = (AV_CODEC_ID_BMV_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IAC = (AV_CODEC_ID_RALF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ILBC = (AV_CODEC_ID_IAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_OPUS = (AV_CODEC_ID_ILBC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_COMFORT_NOISE = (AV_CODEC_ID_OPUS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TAK = (AV_CODEC_ID_COMFORT_NOISE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_METASOUND = (AV_CODEC_ID_TAK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PAF_AUDIO = (AV_CODEC_ID_METASOUND + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ON2AVC = (AV_CODEC_ID_PAF_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSS_SP = (AV_CODEC_ID_ON2AVC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_CODEC2 = (AV_CODEC_ID_DSS_SP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FFWAVESYNTH = (AV_CODEC_ID_CODEC2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SONIC = (AV_CODEC_ID_FFWAVESYNTH + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SONIC_LS = (AV_CODEC_ID_SONIC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_EVRC = (AV_CODEC_ID_SONIC_LS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMV = (AV_CODEC_ID_EVRC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSD_LSBF = (AV_CODEC_ID_SMV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSD_MSBF = (AV_CODEC_ID_DSD_LSBF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSD_LSBF_PLANAR = (AV_CODEC_ID_DSD_MSBF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DSD_MSBF_PLANAR = (AV_CODEC_ID_DSD_LSBF_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_4GV = (AV_CODEC_ID_DSD_MSBF_PLANAR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_INTERPLAY_ACM = (AV_CODEC_ID_4GV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XMA1 = (AV_CODEC_ID_INTERPLAY_ACM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XMA2 = (AV_CODEC_ID_XMA1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DST = (AV_CODEC_ID_XMA2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC3AL = (AV_CODEC_ID_DST + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC3PAL = (AV_CODEC_ID_ATRAC3AL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DOLBY_E = (AV_CODEC_ID_ATRAC3PAL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_APTX = (AV_CODEC_ID_DOLBY_E + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_APTX_HD = (AV_CODEC_ID_APTX + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SBC = (AV_CODEC_ID_APTX_HD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ATRAC9 = (AV_CODEC_ID_SBC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HCOM = (AV_CODEC_ID_ATRAC9 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ACELP_KELVIN = (AV_CODEC_ID_HCOM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEGH_3D_AUDIO = (AV_CODEC_ID_ACELP_KELVIN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SIREN = (AV_CODEC_ID_MPEGH_3D_AUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HCA = (AV_CODEC_ID_SIREN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FASTAUDIO = (AV_CODEC_ID_HCA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MSNSIREN = (AV_CODEC_ID_FASTAUDIO + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DFPWM = (AV_CODEC_ID_MSNSIREN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BONK = (AV_CODEC_ID_DFPWM + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MISC4 = (AV_CODEC_ID_BONK + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_APAC = (AV_CODEC_ID_MISC4 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FTR = (AV_CODEC_ID_APAC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WAVARC = (AV_CODEC_ID_FTR + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_RKA = (AV_CODEC_ID_WAVARC + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FIRST_SUBTITLE = 0x17000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVD_SUBTITLE = 0x17000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVB_SUBTITLE = (AV_CODEC_ID_DVD_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TEXT = (AV_CODEC_ID_DVB_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XSUB = (AV_CODEC_ID_TEXT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SSA = (AV_CODEC_ID_XSUB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MOV_TEXT = (AV_CODEC_ID_SSA + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HDMV_PGS_SUBTITLE = (AV_CODEC_ID_MOV_TEXT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVB_TELETEXT = (AV_CODEC_ID_HDMV_PGS_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SRT = (AV_CODEC_ID_DVB_TELETEXT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MICRODVD = (AV_CODEC_ID_SRT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_EIA_608 = (AV_CODEC_ID_MICRODVD + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_JACOSUB = (AV_CODEC_ID_EIA_608 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SAMI = (AV_CODEC_ID_JACOSUB + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_REALTEXT = (AV_CODEC_ID_SAMI + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_STL = (AV_CODEC_ID_REALTEXT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SUBVIEWER1 = (AV_CODEC_ID_STL + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SUBVIEWER = (AV_CODEC_ID_SUBVIEWER1 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SUBRIP = (AV_CODEC_ID_SUBVIEWER + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WEBVTT = (AV_CODEC_ID_SUBRIP + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPL2 = (AV_CODEC_ID_WEBVTT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VPLAYER = (AV_CODEC_ID_MPL2 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PJS = (AV_CODEC_ID_VPLAYER + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ASS = (AV_CODEC_ID_PJS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_HDMV_TEXT_SUBTITLE = (AV_CODEC_ID_ASS + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TTML = (AV_CODEC_ID_HDMV_TEXT_SUBTITLE + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ARIB_CAPTION = (AV_CODEC_ID_TTML + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FIRST_UNKNOWN = 0x18000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TTF = 0x18000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SCTE_35 = (AV_CODEC_ID_TTF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_EPG = (AV_CODEC_ID_SCTE_35 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BINTEXT = (AV_CODEC_ID_EPG + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_XBIN = (AV_CODEC_ID_BINTEXT + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_IDF = (AV_CODEC_ID_XBIN + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_OTF = (AV_CODEC_ID_IDF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_SMPTE_KLV = (AV_CODEC_ID_OTF + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_DVD_NAV = (AV_CODEC_ID_SMPTE_KLV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_TIMED_ID3 = (AV_CODEC_ID_DVD_NAV + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_BIN_DATA = (AV_CODEC_ID_TIMED_ID3 + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_PROBE = 0x19000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEG2TS = 0x20000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_MPEG4SYSTEMS = 0x20001# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_FFMETADATA = 0x21000# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_WRAPPED_AVFRAME = 0x21001# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_VNULL = (AV_CODEC_ID_WRAPPED_AVFRAME + 1)# /usr/include/libavcodec/codec_id.h: 49

AV_CODEC_ID_ANULL = (AV_CODEC_ID_VNULL + 1)# /usr/include/libavcodec/codec_id.h: 49

# /usr/include/libavcodec/codec_id.h: 610
if _libs["avcodec"].has("avcodec_get_type", "cdecl"):
    avcodec_get_type = _libs["avcodec"].get("avcodec_get_type", "cdecl")
    avcodec_get_type.argtypes = [enum_AVCodecID]
    avcodec_get_type.restype = enum_AVMediaType

# /usr/include/libavcodec/codec_id.h: 616
if _libs["avcodec"].has("avcodec_get_name", "cdecl"):
    avcodec_get_name = _libs["avcodec"].get("avcodec_get_name", "cdecl")
    avcodec_get_name.argtypes = [enum_AVCodecID]
    avcodec_get_name.restype = c_char_p

# /usr/include/libavcodec/codec_id.h: 624
if _libs["avcodec"].has("av_get_bits_per_sample", "cdecl"):
    av_get_bits_per_sample = _libs["avcodec"].get("av_get_bits_per_sample", "cdecl")
    av_get_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_bits_per_sample.restype = c_int

# /usr/include/libavcodec/codec_id.h: 634
if _libs["avcodec"].has("av_get_exact_bits_per_sample", "cdecl"):
    av_get_exact_bits_per_sample = _libs["avcodec"].get("av_get_exact_bits_per_sample", "cdecl")
    av_get_exact_bits_per_sample.argtypes = [enum_AVCodecID]
    av_get_exact_bits_per_sample.restype = c_int

# /usr/include/libavcodec/codec_id.h: 647
if _libs["avcodec"].has("avcodec_profile_name", "cdecl"):
    avcodec_profile_name = _libs["avcodec"].get("avcodec_profile_name", "cdecl")
    avcodec_profile_name.argtypes = [enum_AVCodecID, c_int]
    avcodec_profile_name.restype = c_char_p

# /usr/include/libavcodec/codec_id.h: 655
if _libs["avcodec"].has("av_get_pcm_codec", "cdecl"):
    av_get_pcm_codec = _libs["avcodec"].get("av_get_pcm_codec", "cdecl")
    av_get_pcm_codec.argtypes = [enum_AVSampleFormat, c_int]
    av_get_pcm_codec.restype = enum_AVCodecID

# /home/josiah/ctypesgen_test/av/av/codec.h: 179
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

AVProfile = struct_AVProfile# /home/josiah/ctypesgen_test/av/av/codec.h: 179

# /home/josiah/ctypesgen_test/av/av/codec.h: 235
class struct_AVCodec(Structure):
    pass

struct_AVCodec.__slots__ = [
    'name',
    'long_name',
    'type',
    'id',
    'capabilities',
    'max_lowres',
    'supported_framerates',
    'pix_fmts',
    'supported_samplerates',
    'sample_fmts',
    'channel_layouts',
    'priv_class',
    'profiles',
    'wrapper_name',
    'ch_layouts',
]
struct_AVCodec._fields_ = [
    ('name', String),
    ('long_name', String),
    ('type', enum_AVMediaType),
    ('id', enum_AVCodecID),
    ('capabilities', c_int),
    ('max_lowres', uint8_t),
    ('supported_framerates', POINTER(AVRational)),
    ('pix_fmts', POINTER(enum_AVPixelFormat)),
    ('supported_samplerates', POINTER(c_int)),
    ('sample_fmts', POINTER(enum_AVSampleFormat)),
    ('channel_layouts', POINTER(uint64_t)),
    ('priv_class', POINTER(AVClass)),
    ('profiles', POINTER(AVProfile)),
    ('wrapper_name', String),
    ('ch_layouts', POINTER(AVChannelLayout)),
]

AVCodec = struct_AVCodec# /home/josiah/ctypesgen_test/av/av/codec.h: 235

# /home/josiah/ctypesgen_test/av/av/codec.h: 246
if _libs["avcodec"].has("av_codec_iterate", "cdecl"):
    av_codec_iterate = _libs["avcodec"].get("av_codec_iterate", "cdecl")
    av_codec_iterate.argtypes = [POINTER(POINTER(None))]
    av_codec_iterate.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/av/codec.h: 254
if _libs["avcodec"].has("avcodec_find_decoder", "cdecl"):
    avcodec_find_decoder = _libs["avcodec"].get("avcodec_find_decoder", "cdecl")
    avcodec_find_decoder.argtypes = [enum_AVCodecID]
    avcodec_find_decoder.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/av/codec.h: 262
if _libs["avcodec"].has("avcodec_find_decoder_by_name", "cdecl"):
    avcodec_find_decoder_by_name = _libs["avcodec"].get("avcodec_find_decoder_by_name", "cdecl")
    avcodec_find_decoder_by_name.argtypes = [String]
    avcodec_find_decoder_by_name.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/av/codec.h: 270
if _libs["avcodec"].has("avcodec_find_encoder", "cdecl"):
    avcodec_find_encoder = _libs["avcodec"].get("avcodec_find_encoder", "cdecl")
    avcodec_find_encoder.argtypes = [enum_AVCodecID]
    avcodec_find_encoder.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/av/codec.h: 278
if _libs["avcodec"].has("avcodec_find_encoder_by_name", "cdecl"):
    avcodec_find_encoder_by_name = _libs["avcodec"].get("avcodec_find_encoder_by_name", "cdecl")
    avcodec_find_encoder_by_name.argtypes = [String]
    avcodec_find_encoder_by_name.restype = POINTER(AVCodec)

# /home/josiah/ctypesgen_test/av/av/codec.h: 282
if _libs["avcodec"].has("av_codec_is_encoder", "cdecl"):
    av_codec_is_encoder = _libs["avcodec"].get("av_codec_is_encoder", "cdecl")
    av_codec_is_encoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_encoder.restype = c_int

# /home/josiah/ctypesgen_test/av/av/codec.h: 287
if _libs["avcodec"].has("av_codec_is_decoder", "cdecl"):
    av_codec_is_decoder = _libs["avcodec"].get("av_codec_is_decoder", "cdecl")
    av_codec_is_decoder.argtypes = [POINTER(AVCodec)]
    av_codec_is_decoder.restype = c_int

# /home/josiah/ctypesgen_test/av/av/codec.h: 296
if _libs["avcodec"].has("av_get_profile_name", "cdecl"):
    av_get_profile_name = _libs["avcodec"].get("av_get_profile_name", "cdecl")
    av_get_profile_name.argtypes = [POINTER(AVCodec), c_int]
    av_get_profile_name.restype = c_char_p

enum_anon_27 = c_int# /home/josiah/ctypesgen_test/av/av/codec.h: 298

AV_CODEC_HW_CONFIG_METHOD_HW_DEVICE_CTX = 0x01# /home/josiah/ctypesgen_test/av/av/codec.h: 298

AV_CODEC_HW_CONFIG_METHOD_HW_FRAMES_CTX = 0x02# /home/josiah/ctypesgen_test/av/av/codec.h: 298

AV_CODEC_HW_CONFIG_METHOD_INTERNAL = 0x04# /home/josiah/ctypesgen_test/av/av/codec.h: 298

AV_CODEC_HW_CONFIG_METHOD_AD_HOC = 0x08# /home/josiah/ctypesgen_test/av/av/codec.h: 298

# /home/josiah/ctypesgen_test/av/av/codec.h: 360
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

AVCodecHWConfig = struct_AVCodecHWConfig# /home/josiah/ctypesgen_test/av/av/codec.h: 360

# /home/josiah/ctypesgen_test/av/av/codec.h: 369
if _libs["avcodec"].has("avcodec_get_hw_config", "cdecl"):
    avcodec_get_hw_config = _libs["avcodec"].get("avcodec_get_hw_config", "cdecl")
    avcodec_get_hw_config.argtypes = [POINTER(AVCodec), c_int]
    avcodec_get_hw_config.restype = POINTER(AVCodecHWConfig)

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 66
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

AVCodecDescriptor = struct_AVCodecDescriptor# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 66

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 107
if _libs["avcodec"].has("avcodec_descriptor_get", "cdecl"):
    avcodec_descriptor_get = _libs["avcodec"].get("avcodec_descriptor_get", "cdecl")
    avcodec_descriptor_get.argtypes = [enum_AVCodecID]
    avcodec_descriptor_get.restype = POINTER(AVCodecDescriptor)

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 116
if _libs["avcodec"].has("avcodec_descriptor_next", "cdecl"):
    avcodec_descriptor_next = _libs["avcodec"].get("avcodec_descriptor_next", "cdecl")
    avcodec_descriptor_next.argtypes = [POINTER(AVCodecDescriptor)]
    avcodec_descriptor_next.restype = POINTER(AVCodecDescriptor)

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 122
if _libs["avcodec"].has("avcodec_descriptor_get_by_name", "cdecl"):
    avcodec_descriptor_get_by_name = _libs["avcodec"].get("avcodec_descriptor_get_by_name", "cdecl")
    avcodec_descriptor_get_by_name.argtypes = [String]
    avcodec_descriptor_get_by_name.restype = POINTER(AVCodecDescriptor)

enum_AVFieldOrder = c_int# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_PROGRESSIVE = (AV_FIELD_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_TT = (AV_FIELD_PROGRESSIVE + 1)# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_BB = (AV_FIELD_TT + 1)# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_TB = (AV_FIELD_BB + 1)# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

AV_FIELD_BT = (AV_FIELD_TB + 1)# /home/josiah/ctypesgen_test/av/av/codec_par.h: 38

# /home/josiah/ctypesgen_test/av/av/codec_par.h: 214
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
    'ch_layout',
]
struct_AVCodecParameters._fields_ = [
    ('codec_type', enum_AVMediaType),
    ('codec_id', enum_AVCodecID),
    ('codec_tag', uint32_t),
    ('extradata', POINTER(uint8_t)),
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
    ('channel_layout', uint64_t),
    ('channels', c_int),
    ('sample_rate', c_int),
    ('block_align', c_int),
    ('frame_size', c_int),
    ('initial_padding', c_int),
    ('trailing_padding', c_int),
    ('seek_preroll', c_int),
    ('ch_layout', AVChannelLayout),
]

AVCodecParameters = struct_AVCodecParameters# /home/josiah/ctypesgen_test/av/av/codec_par.h: 214

# /home/josiah/ctypesgen_test/av/av/codec_par.h: 221
if _libs["avcodec"].has("avcodec_parameters_alloc", "cdecl"):
    avcodec_parameters_alloc = _libs["avcodec"].get("avcodec_parameters_alloc", "cdecl")
    avcodec_parameters_alloc.argtypes = []
    avcodec_parameters_alloc.restype = POINTER(AVCodecParameters)

# /home/josiah/ctypesgen_test/av/av/codec_par.h: 227
if _libs["avcodec"].has("avcodec_parameters_free", "cdecl"):
    avcodec_parameters_free = _libs["avcodec"].get("avcodec_parameters_free", "cdecl")
    avcodec_parameters_free.argtypes = [POINTER(POINTER(AVCodecParameters))]
    avcodec_parameters_free.restype = None

# /home/josiah/ctypesgen_test/av/av/codec_par.h: 235
if _libs["avcodec"].has("avcodec_parameters_copy", "cdecl"):
    avcodec_parameters_copy = _libs["avcodec"].get("avcodec_parameters_copy", "cdecl")
    avcodec_parameters_copy.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecParameters)]
    avcodec_parameters_copy.restype = c_int

# /home/josiah/ctypesgen_test/av/av/codec_par.h: 241
if _libs["avcodec"].has("av_get_audio_frame_duration2", "cdecl"):
    av_get_audio_frame_duration2 = _libs["avcodec"].get("av_get_audio_frame_duration2", "cdecl")
    av_get_audio_frame_duration2.argtypes = [POINTER(AVCodecParameters), c_int]
    av_get_audio_frame_duration2.restype = c_int

enum_AVDiscard = c_int# /home/josiah/ctypesgen_test/av/av/defs.h: 67

enum_AVAudioServiceType = c_int# /home/josiah/ctypesgen_test/av/av/defs.h: 79

enum_AVPacketSideDataType = c_int# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_PALETTE = 0# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_NEW_EXTRADATA = (AV_PKT_DATA_PALETTE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_PARAM_CHANGE = (AV_PKT_DATA_NEW_EXTRADATA + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_H263_MB_INFO = (AV_PKT_DATA_PARAM_CHANGE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_REPLAYGAIN = (AV_PKT_DATA_H263_MB_INFO + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_DISPLAYMATRIX = (AV_PKT_DATA_REPLAYGAIN + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_STEREO3D = (AV_PKT_DATA_DISPLAYMATRIX + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_AUDIO_SERVICE_TYPE = (AV_PKT_DATA_STEREO3D + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_QUALITY_STATS = (AV_PKT_DATA_AUDIO_SERVICE_TYPE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_FALLBACK_TRACK = (AV_PKT_DATA_QUALITY_STATS + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_CPB_PROPERTIES = (AV_PKT_DATA_FALLBACK_TRACK + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_SKIP_SAMPLES = (AV_PKT_DATA_CPB_PROPERTIES + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_JP_DUALMONO = (AV_PKT_DATA_SKIP_SAMPLES + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_STRINGS_METADATA = (AV_PKT_DATA_JP_DUALMONO + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_SUBTITLE_POSITION = (AV_PKT_DATA_STRINGS_METADATA + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL = (AV_PKT_DATA_SUBTITLE_POSITION + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_WEBVTT_IDENTIFIER = (AV_PKT_DATA_MATROSKA_BLOCKADDITIONAL + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_WEBVTT_SETTINGS = (AV_PKT_DATA_WEBVTT_IDENTIFIER + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_METADATA_UPDATE = (AV_PKT_DATA_WEBVTT_SETTINGS + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_MPEGTS_STREAM_ID = (AV_PKT_DATA_METADATA_UPDATE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_MASTERING_DISPLAY_METADATA = (AV_PKT_DATA_MPEGTS_STREAM_ID + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_SPHERICAL = (AV_PKT_DATA_MASTERING_DISPLAY_METADATA + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_CONTENT_LIGHT_LEVEL = (AV_PKT_DATA_SPHERICAL + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_A53_CC = (AV_PKT_DATA_CONTENT_LIGHT_LEVEL + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_ENCRYPTION_INIT_INFO = (AV_PKT_DATA_A53_CC + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_ENCRYPTION_INFO = (AV_PKT_DATA_ENCRYPTION_INIT_INFO + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_AFD = (AV_PKT_DATA_ENCRYPTION_INFO + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_PRFT = (AV_PKT_DATA_AFD + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_ICC_PROFILE = (AV_PKT_DATA_PRFT + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_DOVI_CONF = (AV_PKT_DATA_ICC_PROFILE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_S12M_TIMECODE = (AV_PKT_DATA_DOVI_CONF + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_DYNAMIC_HDR10_PLUS = (AV_PKT_DATA_S12M_TIMECODE + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

AV_PKT_DATA_NB = (AV_PKT_DATA_DYNAMIC_HDR10_PLUS + 1)# /home/josiah/ctypesgen_test/av/av/packet.h: 41

# /home/josiah/ctypesgen_test/av/av/packet.h: 319
class struct_AVPacketSideData(Structure):
    pass

struct_AVPacketSideData.__slots__ = [
    'data',
    'size',
    'type',
]
struct_AVPacketSideData._fields_ = [
    ('data', POINTER(uint8_t)),
    ('size', c_size_t),
    ('type', enum_AVPacketSideDataType),
]

AVPacketSideData = struct_AVPacketSideData# /home/josiah/ctypesgen_test/av/av/packet.h: 319

# /home/josiah/ctypesgen_test/av/av/packet.h: 419
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
    'opaque',
    'opaque_ref',
    'time_base',
]
struct_AVPacket._fields_ = [
    ('buf', POINTER(AVBufferRef)),
    ('pts', c_int64),
    ('dts', c_int64),
    ('data', POINTER(uint8_t)),
    ('size', c_int),
    ('stream_index', c_int),
    ('flags', c_int),
    ('side_data', POINTER(AVPacketSideData)),
    ('side_data_elems', c_int),
    ('duration', c_int64),
    ('pos', c_int64),
    ('opaque', POINTER(None)),
    ('opaque_ref', POINTER(AVBufferRef)),
    ('time_base', AVRational),
]

AVPacket = struct_AVPacket# /home/josiah/ctypesgen_test/av/av/packet.h: 419

# /home/josiah/ctypesgen_test/av/av/packet.h: 423
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

AVPacketList = struct_AVPacketList# /home/josiah/ctypesgen_test/av/av/packet.h: 426

enum_AVSideDataParamChangeFlags = c_int# /home/josiah/ctypesgen_test/av/av/packet.h: 450

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_COUNT = 0x0001# /home/josiah/ctypesgen_test/av/av/packet.h: 450

AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_LAYOUT = 0x0002# /home/josiah/ctypesgen_test/av/av/packet.h: 450

AV_SIDE_DATA_PARAM_CHANGE_SAMPLE_RATE = 0x0004# /home/josiah/ctypesgen_test/av/av/packet.h: 450

AV_SIDE_DATA_PARAM_CHANGE_DIMENSIONS = 0x0008# /home/josiah/ctypesgen_test/av/av/packet.h: 450

# /home/josiah/ctypesgen_test/av/av/packet.h: 473
if _libs["avcodec"].has("av_packet_alloc", "cdecl"):
    av_packet_alloc = _libs["avcodec"].get("av_packet_alloc", "cdecl")
    av_packet_alloc.argtypes = []
    av_packet_alloc.restype = POINTER(AVPacket)

# /home/josiah/ctypesgen_test/av/av/packet.h: 485
if _libs["avcodec"].has("av_packet_clone", "cdecl"):
    av_packet_clone = _libs["avcodec"].get("av_packet_clone", "cdecl")
    av_packet_clone.argtypes = [POINTER(AVPacket)]
    av_packet_clone.restype = POINTER(AVPacket)

# /home/josiah/ctypesgen_test/av/av/packet.h: 494
if _libs["avcodec"].has("av_packet_free", "cdecl"):
    av_packet_free = _libs["avcodec"].get("av_packet_free", "cdecl")
    av_packet_free.argtypes = [POINTER(POINTER(AVPacket))]
    av_packet_free.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 512
if _libs["avcodec"].has("av_init_packet", "cdecl"):
    av_init_packet = _libs["avcodec"].get("av_init_packet", "cdecl")
    av_init_packet.argtypes = [POINTER(AVPacket)]
    av_init_packet.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 523
if _libs["avcodec"].has("av_new_packet", "cdecl"):
    av_new_packet = _libs["avcodec"].get("av_new_packet", "cdecl")
    av_new_packet.argtypes = [POINTER(AVPacket), c_int]
    av_new_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 531
if _libs["avcodec"].has("av_shrink_packet", "cdecl"):
    av_shrink_packet = _libs["avcodec"].get("av_shrink_packet", "cdecl")
    av_shrink_packet.argtypes = [POINTER(AVPacket), c_int]
    av_shrink_packet.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 539
if _libs["avcodec"].has("av_grow_packet", "cdecl"):
    av_grow_packet = _libs["avcodec"].get("av_grow_packet", "cdecl")
    av_grow_packet.argtypes = [POINTER(AVPacket), c_int]
    av_grow_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 554
if _libs["avcodec"].has("av_packet_from_data", "cdecl"):
    av_packet_from_data = _libs["avcodec"].get("av_packet_from_data", "cdecl")
    av_packet_from_data.argtypes = [POINTER(AVPacket), POINTER(uint8_t), c_int]
    av_packet_from_data.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 564
if _libs["avcodec"].has("av_packet_new_side_data", "cdecl"):
    av_packet_new_side_data = _libs["avcodec"].get("av_packet_new_side_data", "cdecl")
    av_packet_new_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_size_t]
    av_packet_new_side_data.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/packet.h: 580
if _libs["avcodec"].has("av_packet_add_side_data", "cdecl"):
    av_packet_add_side_data = _libs["avcodec"].get("av_packet_add_side_data", "cdecl")
    av_packet_add_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(uint8_t), c_size_t]
    av_packet_add_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 591
if _libs["avcodec"].has("av_packet_shrink_side_data", "cdecl"):
    av_packet_shrink_side_data = _libs["avcodec"].get("av_packet_shrink_side_data", "cdecl")
    av_packet_shrink_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, c_size_t]
    av_packet_shrink_side_data.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 603
if _libs["avcodec"].has("av_packet_get_side_data", "cdecl"):
    av_packet_get_side_data = _libs["avcodec"].get("av_packet_get_side_data", "cdecl")
    av_packet_get_side_data.argtypes = [POINTER(AVPacket), enum_AVPacketSideDataType, POINTER(c_size_t)]
    av_packet_get_side_data.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/packet.h: 606
if _libs["avcodec"].has("av_packet_side_data_name", "cdecl"):
    av_packet_side_data_name = _libs["avcodec"].get("av_packet_side_data_name", "cdecl")
    av_packet_side_data_name.argtypes = [enum_AVPacketSideDataType]
    av_packet_side_data_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/packet.h: 615
if _libs["avcodec"].has("av_packet_pack_dictionary", "cdecl"):
    av_packet_pack_dictionary = _libs["avcodec"].get("av_packet_pack_dictionary", "cdecl")
    av_packet_pack_dictionary.argtypes = [POINTER(AVDictionary), POINTER(c_size_t)]
    av_packet_pack_dictionary.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/packet.h: 624
if _libs["avcodec"].has("av_packet_unpack_dictionary", "cdecl"):
    av_packet_unpack_dictionary = _libs["avcodec"].get("av_packet_unpack_dictionary", "cdecl")
    av_packet_unpack_dictionary.argtypes = [POINTER(uint8_t), c_size_t, POINTER(POINTER(AVDictionary))]
    av_packet_unpack_dictionary.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 633
if _libs["avcodec"].has("av_packet_free_side_data", "cdecl"):
    av_packet_free_side_data = _libs["avcodec"].get("av_packet_free_side_data", "cdecl")
    av_packet_free_side_data.argtypes = [POINTER(AVPacket)]
    av_packet_free_side_data.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 652
if _libs["avcodec"].has("av_packet_ref", "cdecl"):
    av_packet_ref = _libs["avcodec"].get("av_packet_ref", "cdecl")
    av_packet_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_ref.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 662
if _libs["avcodec"].has("av_packet_unref", "cdecl"):
    av_packet_unref = _libs["avcodec"].get("av_packet_unref", "cdecl")
    av_packet_unref.argtypes = [POINTER(AVPacket)]
    av_packet_unref.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 672
if _libs["avcodec"].has("av_packet_move_ref", "cdecl"):
    av_packet_move_ref = _libs["avcodec"].get("av_packet_move_ref", "cdecl")
    av_packet_move_ref.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_move_ref.restype = None

# /home/josiah/ctypesgen_test/av/av/packet.h: 685
if _libs["avcodec"].has("av_packet_copy_props", "cdecl"):
    av_packet_copy_props = _libs["avcodec"].get("av_packet_copy_props", "cdecl")
    av_packet_copy_props.argtypes = [POINTER(AVPacket), POINTER(AVPacket)]
    av_packet_copy_props.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 701
if _libs["avcodec"].has("av_packet_make_refcounted", "cdecl"):
    av_packet_make_refcounted = _libs["avcodec"].get("av_packet_make_refcounted", "cdecl")
    av_packet_make_refcounted.argtypes = [POINTER(AVPacket)]
    av_packet_make_refcounted.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 712
if _libs["avcodec"].has("av_packet_make_writable", "cdecl"):
    av_packet_make_writable = _libs["avcodec"].get("av_packet_make_writable", "cdecl")
    av_packet_make_writable.argtypes = [POINTER(AVPacket)]
    av_packet_make_writable.restype = c_int

# /home/josiah/ctypesgen_test/av/av/packet.h: 725
if _libs["avcodec"].has("av_packet_rescale_ts", "cdecl"):
    av_packet_rescale_ts = _libs["avcodec"].get("av_packet_rescale_ts", "cdecl")
    av_packet_rescale_ts.argtypes = [POINTER(AVPacket), AVRational, AVRational]
    av_packet_rescale_ts.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 201
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

RcOverride = struct_RcOverride# /home/josiah/ctypesgen_test/av/av/avcodec.h: 201

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 411
class struct_AVCodecInternal(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 426
class struct_AVCodecContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2076
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
    'b_quant_offset',
    'has_b_frames',
    'i_quant_factor',
    'i_quant_offset',
    'lumi_masking',
    'temporal_cplx_masking',
    'spatial_cplx_masking',
    'p_masking',
    'dark_masking',
    'slice_count',
    'slice_offset',
    'sample_aspect_ratio',
    'me_cmp',
    'me_sub_cmp',
    'mb_cmp',
    'ildct_cmp',
    'dia_size',
    'last_predictor_count',
    'me_pre_cmp',
    'pre_dia_size',
    'me_subpel_quality',
    'me_range',
    'slice_flags',
    'mb_decision',
    'intra_matrix',
    'inter_matrix',
    'intra_dc_precision',
    'skip_top',
    'skip_bottom',
    'mb_lmin',
    'mb_lmax',
    'bidir_refine',
    'keyint_min',
    'refs',
    'mv0_threshold',
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
    'trellis',
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
    'thread_count',
    'thread_type',
    'active_thread_type',
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
    'chroma_intra_matrix',
    'dump_separator',
    'codec_whitelist',
    'properties',
    'coded_side_data',
    'nb_coded_side_data',
    'hw_frames_ctx',
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
    'ch_layout',
    'frame_num',
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
    ('extradata', POINTER(uint8_t)),
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
    ('b_quant_offset', c_float),
    ('has_b_frames', c_int),
    ('i_quant_factor', c_float),
    ('i_quant_offset', c_float),
    ('lumi_masking', c_float),
    ('temporal_cplx_masking', c_float),
    ('spatial_cplx_masking', c_float),
    ('p_masking', c_float),
    ('dark_masking', c_float),
    ('slice_count', c_int),
    ('slice_offset', POINTER(c_int)),
    ('sample_aspect_ratio', AVRational),
    ('me_cmp', c_int),
    ('me_sub_cmp', c_int),
    ('mb_cmp', c_int),
    ('ildct_cmp', c_int),
    ('dia_size', c_int),
    ('last_predictor_count', c_int),
    ('me_pre_cmp', c_int),
    ('pre_dia_size', c_int),
    ('me_subpel_quality', c_int),
    ('me_range', c_int),
    ('slice_flags', c_int),
    ('mb_decision', c_int),
    ('intra_matrix', POINTER(uint16_t)),
    ('inter_matrix', POINTER(uint16_t)),
    ('intra_dc_precision', c_int),
    ('skip_top', c_int),
    ('skip_bottom', c_int),
    ('mb_lmin', c_int),
    ('mb_lmax', c_int),
    ('bidir_refine', c_int),
    ('keyint_min', c_int),
    ('refs', c_int),
    ('mv0_threshold', c_int),
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
    ('channel_layout', uint64_t),
    ('request_channel_layout', uint64_t),
    ('audio_service_type', enum_AVAudioServiceType),
    ('request_sample_fmt', enum_AVSampleFormat),
    ('get_buffer2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(AVFrame), c_int)),
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
    ('trellis', c_int),
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
    ('error', uint64_t * int(8)),
    ('dct_algo', c_int),
    ('idct_algo', c_int),
    ('bits_per_coded_sample', c_int),
    ('bits_per_raw_sample', c_int),
    ('lowres', c_int),
    ('thread_count', c_int),
    ('thread_type', c_int),
    ('active_thread_type', c_int),
    ('execute', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(None)), POINTER(None), POINTER(c_int), c_int, c_int)),
    ('execute2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVCodecContext), POINTER(None), c_int, c_int), POINTER(None), POINTER(c_int), c_int)),
    ('nsse_weight', c_int),
    ('profile', c_int),
    ('level', c_int),
    ('skip_loop_filter', enum_AVDiscard),
    ('skip_idct', enum_AVDiscard),
    ('skip_frame', enum_AVDiscard),
    ('subtitle_header', POINTER(uint8_t)),
    ('subtitle_header_size', c_int),
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
    ('chroma_intra_matrix', POINTER(uint16_t)),
    ('dump_separator', POINTER(uint8_t)),
    ('codec_whitelist', String),
    ('properties', c_uint),
    ('coded_side_data', POINTER(AVPacketSideData)),
    ('nb_coded_side_data', c_int),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
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
    ('ch_layout', AVChannelLayout),
    ('frame_num', c_int64),
]

AVCodecContext = struct_AVCodecContext# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2066

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
    ('start_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(uint8_t), uint32_t)),
    ('decode_params', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), c_int, POINTER(uint8_t), uint32_t)),
    ('decode_slice', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(uint8_t), uint32_t)),
    ('end_frame', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('frame_priv_data_size', c_int),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('uninit', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext))),
    ('priv_data_size', c_int),
    ('caps_internal', c_int),
    ('frame_params', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(AVBufferRef))),
]

AVHWAccel = struct_AVHWAccel# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2224

enum_AVSubtitleType = c_int# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2282

SUBTITLE_NONE = 0# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2282

SUBTITLE_BITMAP = (SUBTITLE_NONE + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2282

SUBTITLE_TEXT = (SUBTITLE_BITMAP + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2282

SUBTITLE_ASS = (SUBTITLE_TEXT + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2282

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2328
class struct_AVSubtitleRect(Structure):
    pass

struct_AVSubtitleRect.__slots__ = [
    'x',
    'y',
    'w',
    'h',
    'nb_colors',
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
    ('data', POINTER(uint8_t) * int(4)),
    ('linesize', c_int * int(4)),
    ('type', enum_AVSubtitleType),
    ('text', String),
    ('ass', String),
    ('flags', c_int),
]

AVSubtitleRect = struct_AVSubtitleRect# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2328

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2337
class struct_AVSubtitle(Structure):
    pass

struct_AVSubtitle.__slots__ = [
    'format',
    'start_display_time',
    'end_display_time',
    'num_rects',
    'rects',
    'pts',
]
struct_AVSubtitle._fields_ = [
    ('format', uint16_t),
    ('start_display_time', uint32_t),
    ('end_display_time', uint32_t),
    ('num_rects', c_uint),
    ('rects', POINTER(POINTER(AVSubtitleRect))),
    ('pts', c_int64),
]

AVSubtitle = struct_AVSubtitle# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2337

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2342
if _libs["avcodec"].has("avcodec_version", "cdecl"):
    avcodec_version = _libs["avcodec"].get("avcodec_version", "cdecl")
    avcodec_version.argtypes = []
    avcodec_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2347
if _libs["avcodec"].has("avcodec_configuration", "cdecl"):
    avcodec_configuration = _libs["avcodec"].get("avcodec_configuration", "cdecl")
    avcodec_configuration.argtypes = []
    avcodec_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2352
if _libs["avcodec"].has("avcodec_license", "cdecl"):
    avcodec_license = _libs["avcodec"].get("avcodec_license", "cdecl")
    avcodec_license.argtypes = []
    avcodec_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2367
if _libs["avcodec"].has("avcodec_alloc_context3", "cdecl"):
    avcodec_alloc_context3 = _libs["avcodec"].get("avcodec_alloc_context3", "cdecl")
    avcodec_alloc_context3.argtypes = [POINTER(AVCodec)]
    avcodec_alloc_context3.restype = POINTER(AVCodecContext)

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2373
if _libs["avcodec"].has("avcodec_free_context", "cdecl"):
    avcodec_free_context = _libs["avcodec"].get("avcodec_free_context", "cdecl")
    avcodec_free_context.argtypes = [POINTER(POINTER(AVCodecContext))]
    avcodec_free_context.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2381
if _libs["avcodec"].has("avcodec_get_class", "cdecl"):
    avcodec_get_class = _libs["avcodec"].get("avcodec_get_class", "cdecl")
    avcodec_get_class.argtypes = []
    avcodec_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2389
if _libs["avcodec"].has("avcodec_get_subtitle_rect_class", "cdecl"):
    avcodec_get_subtitle_rect_class = _libs["avcodec"].get("avcodec_get_subtitle_rect_class", "cdecl")
    avcodec_get_subtitle_rect_class.argtypes = []
    avcodec_get_subtitle_rect_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2398
if _libs["avcodec"].has("avcodec_parameters_from_context", "cdecl"):
    avcodec_parameters_from_context = _libs["avcodec"].get("avcodec_parameters_from_context", "cdecl")
    avcodec_parameters_from_context.argtypes = [POINTER(AVCodecParameters), POINTER(AVCodecContext)]
    avcodec_parameters_from_context.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2409
if _libs["avcodec"].has("avcodec_parameters_to_context", "cdecl"):
    avcodec_parameters_to_context = _libs["avcodec"].get("avcodec_parameters_to_context", "cdecl")
    avcodec_parameters_to_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecParameters)]
    avcodec_parameters_to_context.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2447
if _libs["avcodec"].has("avcodec_open2", "cdecl"):
    avcodec_open2 = _libs["avcodec"].get("avcodec_open2", "cdecl")
    avcodec_open2.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec), POINTER(POINTER(AVDictionary))]
    avcodec_open2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2462
if _libs["avcodec"].has("avcodec_close", "cdecl"):
    avcodec_close = _libs["avcodec"].get("avcodec_close", "cdecl")
    avcodec_close.argtypes = [POINTER(AVCodecContext)]
    avcodec_close.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2469
if _libs["avcodec"].has("avsubtitle_free", "cdecl"):
    avsubtitle_free = _libs["avcodec"].get("avsubtitle_free", "cdecl")
    avsubtitle_free.argtypes = [POINTER(AVSubtitle)]
    avsubtitle_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2485
if _libs["avcodec"].has("avcodec_default_get_buffer2", "cdecl"):
    avcodec_default_get_buffer2 = _libs["avcodec"].get("avcodec_default_get_buffer2", "cdecl")
    avcodec_default_get_buffer2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), c_int]
    avcodec_default_get_buffer2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2492
if _libs["avcodec"].has("avcodec_default_get_encode_buffer", "cdecl"):
    avcodec_default_get_encode_buffer = _libs["avcodec"].get("avcodec_default_get_encode_buffer", "cdecl")
    avcodec_default_get_encode_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), c_int]
    avcodec_default_get_encode_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2501
if _libs["avcodec"].has("avcodec_align_dimensions", "cdecl"):
    avcodec_align_dimensions = _libs["avcodec"].get("avcodec_align_dimensions", "cdecl")
    avcodec_align_dimensions.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int)]
    avcodec_align_dimensions.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2510
if _libs["avcodec"].has("avcodec_align_dimensions2", "cdecl"):
    avcodec_align_dimensions2 = _libs["avcodec"].get("avcodec_align_dimensions2", "cdecl")
    avcodec_align_dimensions2.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int), c_int * int(8)]
    avcodec_align_dimensions2.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2525
if _libs["avcodec"].has("avcodec_enum_to_chroma_pos", "cdecl"):
    avcodec_enum_to_chroma_pos = _libs["avcodec"].get("avcodec_enum_to_chroma_pos", "cdecl")
    avcodec_enum_to_chroma_pos.argtypes = [POINTER(c_int), POINTER(c_int), enum_AVChromaLocation]
    avcodec_enum_to_chroma_pos.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2538
if _libs["avcodec"].has("avcodec_chroma_pos_to_enum", "cdecl"):
    avcodec_chroma_pos_to_enum = _libs["avcodec"].get("avcodec_chroma_pos_to_enum", "cdecl")
    avcodec_chroma_pos_to_enum.argtypes = [c_int, c_int]
    avcodec_chroma_pos_to_enum.restype = enum_AVChromaLocation

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2568
if _libs["avcodec"].has("avcodec_decode_subtitle2", "cdecl"):
    avcodec_decode_subtitle2 = _libs["avcodec"].get("avcodec_decode_subtitle2", "cdecl")
    avcodec_decode_subtitle2.argtypes = [POINTER(AVCodecContext), POINTER(AVSubtitle), POINTER(c_int), POINTER(AVPacket)]
    avcodec_decode_subtitle2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2617
if _libs["avcodec"].has("avcodec_send_packet", "cdecl"):
    avcodec_send_packet = _libs["avcodec"].get("avcodec_send_packet", "cdecl")
    avcodec_send_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_send_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2641
if _libs["avcodec"].has("avcodec_receive_frame", "cdecl"):
    avcodec_receive_frame = _libs["avcodec"].get("avcodec_receive_frame", "cdecl")
    avcodec_receive_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_receive_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2677
if _libs["avcodec"].has("avcodec_send_frame", "cdecl"):
    avcodec_send_frame = _libs["avcodec"].get("avcodec_send_frame", "cdecl")
    avcodec_send_frame.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
    avcodec_send_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2694
if _libs["avcodec"].has("avcodec_receive_packet", "cdecl"):
    avcodec_receive_packet = _libs["avcodec"].get("avcodec_receive_packet", "cdecl")
    avcodec_receive_packet.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket)]
    avcodec_receive_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2793
if _libs["avcodec"].has("avcodec_get_hw_frames_parameters", "cdecl"):
    avcodec_get_hw_frames_parameters = _libs["avcodec"].get("avcodec_get_hw_frames_parameters", "cdecl")
    avcodec_get_hw_frames_parameters.argtypes = [POINTER(AVCodecContext), POINTER(AVBufferRef), enum_AVPixelFormat, POINTER(POINTER(AVBufferRef))]
    avcodec_get_hw_frames_parameters.restype = c_int

enum_AVPictureStructure = c_int# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2805

AV_PICTURE_STRUCTURE_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2805

AV_PICTURE_STRUCTURE_TOP_FIELD = (AV_PICTURE_STRUCTURE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2805

AV_PICTURE_STRUCTURE_BOTTOM_FIELD = (AV_PICTURE_STRUCTURE_TOP_FIELD + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2805

AV_PICTURE_STRUCTURE_FRAME = (AV_PICTURE_STRUCTURE_BOTTOM_FIELD + 1)# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2805

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2971
class struct_AVCodecParser(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2969
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

AVCodecParserContext = struct_AVCodecParserContext# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2969

struct_AVCodecParser.__slots__ = [
    'codec_ids',
    'priv_data_size',
    'parser_init',
    'parser_parse',
    'parser_close',
    'split',
]
struct_AVCodecParser._fields_ = [
    ('codec_ids', c_int * int(7)),
    ('priv_data_size', c_int),
    ('parser_init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecParserContext))),
    ('parser_parse', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int)),
    ('parser_close', CFUNCTYPE(UNCHECKED(None), POINTER(AVCodecParserContext))),
    ('split', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(uint8_t), c_int)),
]

AVCodecParser = struct_AVCodecParser# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2983

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2994
if _libs["avcodec"].has("av_parser_iterate", "cdecl"):
    av_parser_iterate = _libs["avcodec"].get("av_parser_iterate", "cdecl")
    av_parser_iterate.argtypes = [POINTER(POINTER(None))]
    av_parser_iterate.restype = POINTER(AVCodecParser)

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2996
if _libs["avcodec"].has("av_parser_init", "cdecl"):
    av_parser_init = _libs["avcodec"].get("av_parser_init", "cdecl")
    av_parser_init.argtypes = [c_int]
    av_parser_init.restype = POINTER(AVCodecParserContext)

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3029
if _libs["avcodec"].has("av_parser_parse2", "cdecl"):
    av_parser_parse2 = _libs["avcodec"].get("av_parser_parse2", "cdecl")
    av_parser_parse2.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int64, c_int64, c_int64]
    av_parser_parse2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3036
if _libs["avcodec"].has("av_parser_close", "cdecl"):
    av_parser_close = _libs["avcodec"].get("av_parser_close", "cdecl")
    av_parser_close.argtypes = [POINTER(AVCodecParserContext)]
    av_parser_close.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3048
if _libs["avcodec"].has("avcodec_encode_subtitle", "cdecl"):
    avcodec_encode_subtitle = _libs["avcodec"].get("avcodec_encode_subtitle", "cdecl")
    avcodec_encode_subtitle.argtypes = [POINTER(AVCodecContext), POINTER(uint8_t), c_int, POINTER(AVSubtitle)]
    avcodec_encode_subtitle.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3077
if _libs["avcodec"].has("avcodec_pix_fmt_to_codec_tag", "cdecl"):
    avcodec_pix_fmt_to_codec_tag = _libs["avcodec"].get("avcodec_pix_fmt_to_codec_tag", "cdecl")
    avcodec_pix_fmt_to_codec_tag.argtypes = [enum_AVPixelFormat]
    avcodec_pix_fmt_to_codec_tag.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3096
if _libs["avcodec"].has("avcodec_find_best_pix_fmt_of_list", "cdecl"):
    avcodec_find_best_pix_fmt_of_list = _libs["avcodec"].get("avcodec_find_best_pix_fmt_of_list", "cdecl")
    avcodec_find_best_pix_fmt_of_list.argtypes = [POINTER(enum_AVPixelFormat), enum_AVPixelFormat, c_int, POINTER(c_int)]
    avcodec_find_best_pix_fmt_of_list.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3100
if _libs["avcodec"].has("avcodec_default_get_format", "cdecl"):
    avcodec_default_get_format = _libs["avcodec"].get("avcodec_default_get_format", "cdecl")
    avcodec_default_get_format.argtypes = [POINTER(struct_AVCodecContext), POINTER(enum_AVPixelFormat)]
    avcodec_default_get_format.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3106
if _libs["avcodec"].has("avcodec_string", "cdecl"):
    avcodec_string = _libs["avcodec"].get("avcodec_string", "cdecl")
    avcodec_string.argtypes = [String, c_int, POINTER(AVCodecContext), c_int]
    avcodec_string.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3108
if _libs["avcodec"].has("avcodec_default_execute", "cdecl"):
    avcodec_default_execute = _libs["avcodec"].get("avcodec_default_execute", "cdecl")
    avcodec_default_execute.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None)), POINTER(None), POINTER(c_int), c_int, c_int]
    avcodec_default_execute.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3109
if _libs["avcodec"].has("avcodec_default_execute2", "cdecl"):
    avcodec_default_execute2 = _libs["avcodec"].get("avcodec_default_execute2", "cdecl")
    avcodec_default_execute2.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(UNCHECKED(c_int), POINTER(AVCodecContext), POINTER(None), c_int, c_int), POINTER(None), POINTER(c_int), c_int]
    avcodec_default_execute2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3135
if _libs["avcodec"].has("avcodec_fill_audio_frame", "cdecl"):
    avcodec_fill_audio_frame = _libs["avcodec"].get("avcodec_fill_audio_frame", "cdecl")
    avcodec_fill_audio_frame.argtypes = [POINTER(AVFrame), c_int, enum_AVSampleFormat, POINTER(uint8_t), c_int, c_int]
    avcodec_fill_audio_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3153
if _libs["avcodec"].has("avcodec_flush_buffers", "cdecl"):
    avcodec_flush_buffers = _libs["avcodec"].get("avcodec_flush_buffers", "cdecl")
    avcodec_flush_buffers.argtypes = [POINTER(AVCodecContext)]
    avcodec_flush_buffers.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3163
if _libs["avcodec"].has("av_get_audio_frame_duration", "cdecl"):
    av_get_audio_frame_duration = _libs["avcodec"].get("av_get_audio_frame_duration", "cdecl")
    av_get_audio_frame_duration.argtypes = [POINTER(AVCodecContext), c_int]
    av_get_audio_frame_duration.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3174
if _libs["avcodec"].has("av_fast_padded_malloc", "cdecl"):
    av_fast_padded_malloc = _libs["avcodec"].get("av_fast_padded_malloc", "cdecl")
    av_fast_padded_malloc.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_malloc.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3180
if _libs["avcodec"].has("av_fast_padded_mallocz", "cdecl"):
    av_fast_padded_mallocz = _libs["avcodec"].get("av_fast_padded_mallocz", "cdecl")
    av_fast_padded_mallocz.argtypes = [POINTER(None), POINTER(c_uint), c_size_t]
    av_fast_padded_mallocz.restype = None

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 3186
if _libs["avcodec"].has("avcodec_is_open", "cdecl"):
    avcodec_is_open = _libs["avcodec"].get("avcodec_is_open", "cdecl")
    avcodec_is_open.argtypes = [POINTER(AVCodecContext)]
    avcodec_is_open.restype = c_int

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

AV_OPT_TYPE_CHLAYOUT = (AV_OPT_TYPE_BOOL + 1)# /usr/include/libavutil/opt.h: 223

# /usr/include/libavutil/opt.h: 270
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'i64',
    'dbl',
    'str',
    'q',
]
union_anon_28._fields_ = [
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
    ('default_val', union_anon_28),
    ('min', c_double),
    ('max', c_double),
    ('flags', c_int),
    ('unit', String),
]

AVOption = struct_AVOption# /usr/include/libavutil/opt.h: 308

# /usr/include/libavutil/opt.h: 331
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

AVOptionRange = struct_AVOptionRange# /usr/include/libavutil/opt.h: 331

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

AVOptionRanges = struct_AVOptionRanges# /usr/include/libavutil/opt.h: 376

# /usr/include/libavutil/opt.h: 387
if _libs["avcodec"].has("av_opt_show2", "cdecl"):
    av_opt_show2 = _libs["avcodec"].get("av_opt_show2", "cdecl")
    av_opt_show2.argtypes = [POINTER(None), POINTER(None), c_int, c_int]
    av_opt_show2.restype = c_int

# /usr/include/libavutil/opt.h: 394
if _libs["avcodec"].has("av_opt_set_defaults", "cdecl"):
    av_opt_set_defaults = _libs["avcodec"].get("av_opt_set_defaults", "cdecl")
    av_opt_set_defaults.argtypes = [POINTER(None)]
    av_opt_set_defaults.restype = None

# /usr/include/libavutil/opt.h: 405
if _libs["avcodec"].has("av_opt_set_defaults2", "cdecl"):
    av_opt_set_defaults2 = _libs["avcodec"].get("av_opt_set_defaults2", "cdecl")
    av_opt_set_defaults2.argtypes = [POINTER(None), c_int, c_int]
    av_opt_set_defaults2.restype = None

# /usr/include/libavutil/opt.h: 424
if _libs["avcodec"].has("av_set_options_string", "cdecl"):
    av_set_options_string = _libs["avcodec"].get("av_set_options_string", "cdecl")
    av_set_options_string.argtypes = [POINTER(None), String, String, String]
    av_set_options_string.restype = c_int

# /usr/include/libavutil/opt.h: 454
if _libs["avcodec"].has("av_opt_set_from_string", "cdecl"):
    av_opt_set_from_string = _libs["avcodec"].get("av_opt_set_from_string", "cdecl")
    av_opt_set_from_string.argtypes = [POINTER(None), String, POINTER(POINTER(c_char)), String, String]
    av_opt_set_from_string.restype = c_int

# /usr/include/libavutil/opt.h: 460
if _libs["avcodec"].has("av_opt_free", "cdecl"):
    av_opt_free = _libs["avcodec"].get("av_opt_free", "cdecl")
    av_opt_free.argtypes = [POINTER(None)]
    av_opt_free.restype = None

# /usr/include/libavutil/opt.h: 470
if _libs["avcodec"].has("av_opt_flag_is_set", "cdecl"):
    av_opt_flag_is_set = _libs["avcodec"].get("av_opt_flag_is_set", "cdecl")
    av_opt_flag_is_set.argtypes = [POINTER(None), String, String]
    av_opt_flag_is_set.restype = c_int

# /usr/include/libavutil/opt.h: 486
if _libs["avcodec"].has("av_opt_set_dict", "cdecl"):
    av_opt_set_dict = _libs["avcodec"].get("av_opt_set_dict", "cdecl")
    av_opt_set_dict.argtypes = [POINTER(None), POINTER(POINTER(struct_AVDictionary))]
    av_opt_set_dict.restype = c_int

# /usr/include/libavutil/opt.h: 504
if _libs["avcodec"].has("av_opt_set_dict2", "cdecl"):
    av_opt_set_dict2 = _libs["avcodec"].get("av_opt_set_dict2", "cdecl")
    av_opt_set_dict2.argtypes = [POINTER(None), POINTER(POINTER(struct_AVDictionary)), c_int]
    av_opt_set_dict2.restype = c_int

# /usr/include/libavutil/opt.h: 525
if _libs["avcodec"].has("av_opt_get_key_value", "cdecl"):
    av_opt_get_key_value = _libs["avcodec"].get("av_opt_get_key_value", "cdecl")
    av_opt_get_key_value.argtypes = [POINTER(POINTER(c_char)), String, String, c_uint, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    av_opt_get_key_value.restype = c_int

enum_anon_29 = c_int# /usr/include/libavutil/opt.h: 530

AV_OPT_FLAG_IMPLICIT_KEY = 1# /usr/include/libavutil/opt.h: 530

# /usr/include/libavutil/opt.h: 553
if _libs["avcodec"].has("av_opt_eval_flags", "cdecl"):
    av_opt_eval_flags = _libs["avcodec"].get("av_opt_eval_flags", "cdecl")
    av_opt_eval_flags.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int)]
    av_opt_eval_flags.restype = c_int

# /usr/include/libavutil/opt.h: 554
if _libs["avcodec"].has("av_opt_eval_int", "cdecl"):
    av_opt_eval_int = _libs["avcodec"].get("av_opt_eval_int", "cdecl")
    av_opt_eval_int.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int)]
    av_opt_eval_int.restype = c_int

# /usr/include/libavutil/opt.h: 555
if _libs["avcodec"].has("av_opt_eval_int64", "cdecl"):
    av_opt_eval_int64 = _libs["avcodec"].get("av_opt_eval_int64", "cdecl")
    av_opt_eval_int64.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_int64)]
    av_opt_eval_int64.restype = c_int

# /usr/include/libavutil/opt.h: 556
if _libs["avcodec"].has("av_opt_eval_float", "cdecl"):
    av_opt_eval_float = _libs["avcodec"].get("av_opt_eval_float", "cdecl")
    av_opt_eval_float.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_float)]
    av_opt_eval_float.restype = c_int

# /usr/include/libavutil/opt.h: 557
if _libs["avcodec"].has("av_opt_eval_double", "cdecl"):
    av_opt_eval_double = _libs["avcodec"].get("av_opt_eval_double", "cdecl")
    av_opt_eval_double.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(c_double)]
    av_opt_eval_double.restype = c_int

# /usr/include/libavutil/opt.h: 558
if _libs["avcodec"].has("av_opt_eval_q", "cdecl"):
    av_opt_eval_q = _libs["avcodec"].get("av_opt_eval_q", "cdecl")
    av_opt_eval_q.argtypes = [POINTER(None), POINTER(AVOption), String, POINTER(AVRational)]
    av_opt_eval_q.restype = c_int

# /usr/include/libavutil/opt.h: 608
if _libs["avcodec"].has("av_opt_find", "cdecl"):
    av_opt_find = _libs["avcodec"].get("av_opt_find", "cdecl")
    av_opt_find.argtypes = [POINTER(None), String, String, c_int, c_int]
    av_opt_find.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 632
if _libs["avcodec"].has("av_opt_find2", "cdecl"):
    av_opt_find2 = _libs["avcodec"].get("av_opt_find2", "cdecl")
    av_opt_find2.argtypes = [POINTER(None), String, String, c_int, c_int, POINTER(POINTER(None))]
    av_opt_find2.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 644
if _libs["avcodec"].has("av_opt_next", "cdecl"):
    av_opt_next = _libs["avcodec"].get("av_opt_next", "cdecl")
    av_opt_next.argtypes = [POINTER(None), POINTER(AVOption)]
    av_opt_next.restype = POINTER(AVOption)

# /usr/include/libavutil/opt.h: 652
if _libs["avcodec"].has("av_opt_child_next", "cdecl"):
    av_opt_child_next = _libs["avcodec"].get("av_opt_child_next", "cdecl")
    av_opt_child_next.argtypes = [POINTER(None), POINTER(None)]
    av_opt_child_next.restype = POINTER(c_ubyte)
    av_opt_child_next.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/opt.h: 660
if _libs["avcodec"].has("av_opt_child_class_iterate", "cdecl"):
    av_opt_child_class_iterate = _libs["avcodec"].get("av_opt_child_class_iterate", "cdecl")
    av_opt_child_class_iterate.argtypes = [POINTER(AVClass), POINTER(POINTER(None))]
    av_opt_child_class_iterate.restype = POINTER(AVClass)

# /usr/include/libavutil/opt.h: 691
if _libs["avcodec"].has("av_opt_set", "cdecl"):
    av_opt_set = _libs["avcodec"].get("av_opt_set", "cdecl")
    av_opt_set.argtypes = [POINTER(None), String, String, c_int]
    av_opt_set.restype = c_int

# /usr/include/libavutil/opt.h: 692
if _libs["avcodec"].has("av_opt_set_int", "cdecl"):
    av_opt_set_int = _libs["avcodec"].get("av_opt_set_int", "cdecl")
    av_opt_set_int.argtypes = [POINTER(None), String, c_int64, c_int]
    av_opt_set_int.restype = c_int

# /usr/include/libavutil/opt.h: 693
if _libs["avcodec"].has("av_opt_set_double", "cdecl"):
    av_opt_set_double = _libs["avcodec"].get("av_opt_set_double", "cdecl")
    av_opt_set_double.argtypes = [POINTER(None), String, c_double, c_int]
    av_opt_set_double.restype = c_int

# /usr/include/libavutil/opt.h: 694
if _libs["avcodec"].has("av_opt_set_q", "cdecl"):
    av_opt_set_q = _libs["avcodec"].get("av_opt_set_q", "cdecl")
    av_opt_set_q.argtypes = [POINTER(None), String, AVRational, c_int]
    av_opt_set_q.restype = c_int

# /usr/include/libavutil/opt.h: 695
if _libs["avcodec"].has("av_opt_set_bin", "cdecl"):
    av_opt_set_bin = _libs["avcodec"].get("av_opt_set_bin", "cdecl")
    av_opt_set_bin.argtypes = [POINTER(None), String, POINTER(uint8_t), c_int, c_int]
    av_opt_set_bin.restype = c_int

# /usr/include/libavutil/opt.h: 696
if _libs["avcodec"].has("av_opt_set_image_size", "cdecl"):
    av_opt_set_image_size = _libs["avcodec"].get("av_opt_set_image_size", "cdecl")
    av_opt_set_image_size.argtypes = [POINTER(None), String, c_int, c_int, c_int]
    av_opt_set_image_size.restype = c_int

# /usr/include/libavutil/opt.h: 697
if _libs["avcodec"].has("av_opt_set_pixel_fmt", "cdecl"):
    av_opt_set_pixel_fmt = _libs["avcodec"].get("av_opt_set_pixel_fmt", "cdecl")
    av_opt_set_pixel_fmt.argtypes = [POINTER(None), String, enum_AVPixelFormat, c_int]
    av_opt_set_pixel_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 698
if _libs["avcodec"].has("av_opt_set_sample_fmt", "cdecl"):
    av_opt_set_sample_fmt = _libs["avcodec"].get("av_opt_set_sample_fmt", "cdecl")
    av_opt_set_sample_fmt.argtypes = [POINTER(None), String, enum_AVSampleFormat, c_int]
    av_opt_set_sample_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 699
if _libs["avcodec"].has("av_opt_set_video_rate", "cdecl"):
    av_opt_set_video_rate = _libs["avcodec"].get("av_opt_set_video_rate", "cdecl")
    av_opt_set_video_rate.argtypes = [POINTER(None), String, AVRational, c_int]
    av_opt_set_video_rate.restype = c_int

# /usr/include/libavutil/opt.h: 702
if _libs["avcodec"].has("av_opt_set_channel_layout", "cdecl"):
    av_opt_set_channel_layout = _libs["avcodec"].get("av_opt_set_channel_layout", "cdecl")
    av_opt_set_channel_layout.argtypes = [POINTER(None), String, c_int64, c_int]
    av_opt_set_channel_layout.restype = c_int

# /usr/include/libavutil/opt.h: 704
if _libs["avcodec"].has("av_opt_set_chlayout", "cdecl"):
    av_opt_set_chlayout = _libs["avcodec"].get("av_opt_set_chlayout", "cdecl")
    av_opt_set_chlayout.argtypes = [POINTER(None), String, POINTER(AVChannelLayout), c_int]
    av_opt_set_chlayout.restype = c_int

# /usr/include/libavutil/opt.h: 709
if _libs["avcodec"].has("av_opt_set_dict_val", "cdecl"):
    av_opt_set_dict_val = _libs["avcodec"].get("av_opt_set_dict_val", "cdecl")
    av_opt_set_dict_val.argtypes = [POINTER(None), String, POINTER(AVDictionary), c_int]
    av_opt_set_dict_val.restype = c_int

# /usr/include/libavutil/opt.h: 751
if _libs["avcodec"].has("av_opt_get", "cdecl"):
    av_opt_get = _libs["avcodec"].get("av_opt_get", "cdecl")
    av_opt_get.argtypes = [POINTER(None), String, c_int, POINTER(POINTER(uint8_t))]
    av_opt_get.restype = c_int

# /usr/include/libavutil/opt.h: 752
if _libs["avcodec"].has("av_opt_get_int", "cdecl"):
    av_opt_get_int = _libs["avcodec"].get("av_opt_get_int", "cdecl")
    av_opt_get_int.argtypes = [POINTER(None), String, c_int, POINTER(c_int64)]
    av_opt_get_int.restype = c_int

# /usr/include/libavutil/opt.h: 753
if _libs["avcodec"].has("av_opt_get_double", "cdecl"):
    av_opt_get_double = _libs["avcodec"].get("av_opt_get_double", "cdecl")
    av_opt_get_double.argtypes = [POINTER(None), String, c_int, POINTER(c_double)]
    av_opt_get_double.restype = c_int

# /usr/include/libavutil/opt.h: 754
if _libs["avcodec"].has("av_opt_get_q", "cdecl"):
    av_opt_get_q = _libs["avcodec"].get("av_opt_get_q", "cdecl")
    av_opt_get_q.argtypes = [POINTER(None), String, c_int, POINTER(AVRational)]
    av_opt_get_q.restype = c_int

# /usr/include/libavutil/opt.h: 755
if _libs["avcodec"].has("av_opt_get_image_size", "cdecl"):
    av_opt_get_image_size = _libs["avcodec"].get("av_opt_get_image_size", "cdecl")
    av_opt_get_image_size.argtypes = [POINTER(None), String, c_int, POINTER(c_int), POINTER(c_int)]
    av_opt_get_image_size.restype = c_int

# /usr/include/libavutil/opt.h: 756
if _libs["avcodec"].has("av_opt_get_pixel_fmt", "cdecl"):
    av_opt_get_pixel_fmt = _libs["avcodec"].get("av_opt_get_pixel_fmt", "cdecl")
    av_opt_get_pixel_fmt.argtypes = [POINTER(None), String, c_int, POINTER(enum_AVPixelFormat)]
    av_opt_get_pixel_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 757
if _libs["avcodec"].has("av_opt_get_sample_fmt", "cdecl"):
    av_opt_get_sample_fmt = _libs["avcodec"].get("av_opt_get_sample_fmt", "cdecl")
    av_opt_get_sample_fmt.argtypes = [POINTER(None), String, c_int, POINTER(enum_AVSampleFormat)]
    av_opt_get_sample_fmt.restype = c_int

# /usr/include/libavutil/opt.h: 758
if _libs["avcodec"].has("av_opt_get_video_rate", "cdecl"):
    av_opt_get_video_rate = _libs["avcodec"].get("av_opt_get_video_rate", "cdecl")
    av_opt_get_video_rate.argtypes = [POINTER(None), String, c_int, POINTER(AVRational)]
    av_opt_get_video_rate.restype = c_int

# /usr/include/libavutil/opt.h: 761
if _libs["avcodec"].has("av_opt_get_channel_layout", "cdecl"):
    av_opt_get_channel_layout = _libs["avcodec"].get("av_opt_get_channel_layout", "cdecl")
    av_opt_get_channel_layout.argtypes = [POINTER(None), String, c_int, POINTER(c_int64)]
    av_opt_get_channel_layout.restype = c_int

# /usr/include/libavutil/opt.h: 763
if _libs["avcodec"].has("av_opt_get_chlayout", "cdecl"):
    av_opt_get_chlayout = _libs["avcodec"].get("av_opt_get_chlayout", "cdecl")
    av_opt_get_chlayout.argtypes = [POINTER(None), String, c_int, POINTER(AVChannelLayout)]
    av_opt_get_chlayout.restype = c_int

# /usr/include/libavutil/opt.h: 768
if _libs["avcodec"].has("av_opt_get_dict_val", "cdecl"):
    av_opt_get_dict_val = _libs["avcodec"].get("av_opt_get_dict_val", "cdecl")
    av_opt_get_dict_val.argtypes = [POINTER(None), String, c_int, POINTER(POINTER(AVDictionary))]
    av_opt_get_dict_val.restype = c_int

# /usr/include/libavutil/opt.h: 780
if _libs["avcodec"].has("av_opt_ptr", "cdecl"):
    av_opt_ptr = _libs["avcodec"].get("av_opt_ptr", "cdecl")
    av_opt_ptr.argtypes = [POINTER(AVClass), POINTER(None), String]
    av_opt_ptr.restype = POINTER(c_ubyte)
    av_opt_ptr.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/libavutil/opt.h: 785
if _libs["avcodec"].has("av_opt_freep_ranges", "cdecl"):
    av_opt_freep_ranges = _libs["avcodec"].get("av_opt_freep_ranges", "cdecl")
    av_opt_freep_ranges.argtypes = [POINTER(POINTER(AVOptionRanges))]
    av_opt_freep_ranges.restype = None

# /usr/include/libavutil/opt.h: 800
if _libs["avcodec"].has("av_opt_query_ranges", "cdecl"):
    av_opt_query_ranges = _libs["avcodec"].get("av_opt_query_ranges", "cdecl")
    av_opt_query_ranges.argtypes = [POINTER(POINTER(AVOptionRanges)), POINTER(None), String, c_int]
    av_opt_query_ranges.restype = c_int

# /usr/include/libavutil/opt.h: 819
if _libs["avcodec"].has("av_opt_copy", "cdecl"):
    av_opt_copy = _libs["avcodec"].get("av_opt_copy", "cdecl")
    av_opt_copy.argtypes = [POINTER(None), POINTER(None)]
    av_opt_copy.restype = c_int

# /usr/include/libavutil/opt.h: 835
if _libs["avcodec"].has("av_opt_query_ranges_default", "cdecl"):
    av_opt_query_ranges_default = _libs["avcodec"].get("av_opt_query_ranges_default", "cdecl")
    av_opt_query_ranges_default.argtypes = [POINTER(POINTER(AVOptionRanges)), POINTER(None), String, c_int]
    av_opt_query_ranges_default.restype = c_int

# /usr/include/libavutil/opt.h: 849
if _libs["avcodec"].has("av_opt_is_set_to_default", "cdecl"):
    av_opt_is_set_to_default = _libs["avcodec"].get("av_opt_is_set_to_default", "cdecl")
    av_opt_is_set_to_default.argtypes = [POINTER(None), POINTER(AVOption)]
    av_opt_is_set_to_default.restype = c_int

# /usr/include/libavutil/opt.h: 861
if _libs["avcodec"].has("av_opt_is_set_to_default_by_name", "cdecl"):
    av_opt_is_set_to_default_by_name = _libs["avcodec"].get("av_opt_is_set_to_default_by_name", "cdecl")
    av_opt_is_set_to_default_by_name.argtypes = [POINTER(None), String, c_int]
    av_opt_is_set_to_default_by_name.restype = c_int

# /usr/include/libavutil/opt.h: 885
if _libs["avcodec"].has("av_opt_serialize", "cdecl"):
    av_opt_serialize = _libs["avcodec"].get("av_opt_serialize", "cdecl")
    av_opt_serialize.argtypes = [POINTER(None), c_int, c_int, POINTER(POINTER(c_char)), c_char, c_char]
    av_opt_serialize.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdct.h: 74
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
    ('idct_permutation', uint8_t * int(64)),
    ('fdct', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16))),
    ('dct_algo', c_int),
    ('idct_algo', c_int),
    ('get_pixels', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16), POINTER(uint8_t), c_ptrdiff_t)),
    ('bits_per_sample', c_int),
    ('get_pixels_unaligned', CFUNCTYPE(UNCHECKED(None), POINTER(c_int16), POINTER(uint8_t), c_ptrdiff_t)),
]

AVDCT = struct_AVDCT# /home/josiah/ctypesgen_test/av/av/avdct.h: 74

# /home/josiah/ctypesgen_test/av/av/avdct.h: 83
if _libs["avcodec"].has("avcodec_dct_alloc", "cdecl"):
    avcodec_dct_alloc = _libs["avcodec"].get("avcodec_dct_alloc", "cdecl")
    avcodec_dct_alloc.argtypes = []
    avcodec_dct_alloc.restype = POINTER(AVDCT)

# /home/josiah/ctypesgen_test/av/av/avdct.h: 84
if _libs["avcodec"].has("avcodec_dct_init", "cdecl"):
    avcodec_dct_init = _libs["avcodec"].get("avcodec_dct_init", "cdecl")
    avcodec_dct_init.argtypes = [POINTER(AVDCT)]
    avcodec_dct_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdct.h: 86
if _libs["avcodec"].has("avcodec_dct_get_class", "cdecl"):
    avcodec_dct_get_class = _libs["avcodec"].get("avcodec_dct_get_class", "cdecl")
    avcodec_dct_get_class.argtypes = []
    avcodec_dct_get_class.restype = POINTER(AVClass)

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

# /usr/include/time.h: 76
if _libs["avcodec"].has("time", "cdecl"):
    time = _libs["avcodec"].get("time", "cdecl")
    time.argtypes = [POINTER(time_t)]
    time.restype = time_t

# /usr/include/time.h: 79
if _libs["avcodec"].has("difftime", "cdecl"):
    difftime = _libs["avcodec"].get("difftime", "cdecl")
    difftime.argtypes = [time_t, time_t]
    difftime.restype = c_double

# /usr/include/time.h: 83
if _libs["avcodec"].has("mktime", "cdecl"):
    mktime = _libs["avcodec"].get("mktime", "cdecl")
    mktime.argtypes = [POINTER(struct_tm)]
    mktime.restype = time_t

# /usr/include/time.h: 100
if _libs["avcodec"].has("strftime", "cdecl"):
    strftime = _libs["avcodec"].get("strftime", "cdecl")
    strftime.argtypes = [String, c_size_t, String, POINTER(struct_tm)]
    strftime.restype = c_size_t

# /usr/include/time.h: 116
if _libs["avcodec"].has("strftime_l", "cdecl"):
    strftime_l = _libs["avcodec"].get("strftime_l", "cdecl")
    strftime_l.argtypes = [String, c_size_t, String, POINTER(struct_tm), locale_t]
    strftime_l.restype = c_size_t

# /usr/include/time.h: 132
if _libs["avcodec"].has("gmtime", "cdecl"):
    gmtime = _libs["avcodec"].get("gmtime", "cdecl")
    gmtime.argtypes = [POINTER(time_t)]
    gmtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 136
if _libs["avcodec"].has("localtime", "cdecl"):
    localtime = _libs["avcodec"].get("localtime", "cdecl")
    localtime.argtypes = [POINTER(time_t)]
    localtime.restype = POINTER(struct_tm)

# /usr/include/time.h: 154
if _libs["avcodec"].has("gmtime_r", "cdecl"):
    gmtime_r = _libs["avcodec"].get("gmtime_r", "cdecl")
    gmtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    gmtime_r.restype = POINTER(struct_tm)

# /usr/include/time.h: 159
if _libs["avcodec"].has("localtime_r", "cdecl"):
    localtime_r = _libs["avcodec"].get("localtime_r", "cdecl")
    localtime_r.argtypes = [POINTER(time_t), POINTER(struct_tm)]
    localtime_r.restype = POINTER(struct_tm)

# /usr/include/time.h: 179
if _libs["avcodec"].has("asctime", "cdecl"):
    asctime = _libs["avcodec"].get("asctime", "cdecl")
    asctime.argtypes = [POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime.restype = ReturnString
    else:
        asctime.restype = String
        asctime.errcheck = ReturnString

# /usr/include/time.h: 183
if _libs["avcodec"].has("ctime", "cdecl"):
    ctime = _libs["avcodec"].get("ctime", "cdecl")
    ctime.argtypes = [POINTER(time_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime.restype = ReturnString
    else:
        ctime.restype = String
        ctime.errcheck = ReturnString

# /usr/include/time.h: 197
if _libs["avcodec"].has("asctime_r", "cdecl"):
    asctime_r = _libs["avcodec"].get("asctime_r", "cdecl")
    asctime_r.argtypes = [POINTER(struct_tm), String]
    if sizeof(c_int) == sizeof(c_void_p):
        asctime_r.restype = ReturnString
    else:
        asctime_r.restype = String
        asctime_r.errcheck = ReturnString

# /usr/include/time.h: 202
if _libs["avcodec"].has("ctime_r", "cdecl"):
    ctime_r = _libs["avcodec"].get("ctime_r", "cdecl")
    ctime_r.argtypes = [POINTER(time_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ctime_r.restype = ReturnString
    else:
        ctime_r.restype = String
        ctime_r.errcheck = ReturnString

# /usr/include/time.h: 217
try:
    __tzname = (POINTER(c_char) * int(2)).in_dll(_libs["avcodec"], "__tzname")
except:
    pass

# /usr/include/time.h: 218
try:
    __daylight = (c_int).in_dll(_libs["avcodec"], "__daylight")
except:
    pass

# /usr/include/time.h: 219
try:
    __timezone = (c_long).in_dll(_libs["avcodec"], "__timezone")
except:
    pass

# /usr/include/time.h: 224
try:
    tzname = (POINTER(c_char) * int(2)).in_dll(_libs["avcodec"], "tzname")
except:
    pass

# /usr/include/time.h: 228
if _libs["avcodec"].has("tzset", "cdecl"):
    tzset = _libs["avcodec"].get("tzset", "cdecl")
    tzset.argtypes = []
    tzset.restype = None

# /usr/include/time.h: 232
try:
    daylight = (c_int).in_dll(_libs["avcodec"], "daylight")
except:
    pass

# /usr/include/time.h: 233
try:
    timezone = (c_long).in_dll(_libs["avcodec"], "timezone")
except:
    pass

# /usr/include/time.h: 246
if _libs["avcodec"].has("timegm", "cdecl"):
    timegm = _libs["avcodec"].get("timegm", "cdecl")
    timegm.argtypes = [POINTER(struct_tm)]
    timegm.restype = time_t

# /usr/include/time.h: 263
if _libs["avcodec"].has("timelocal", "cdecl"):
    timelocal = _libs["avcodec"].get("timelocal", "cdecl")
    timelocal.argtypes = [POINTER(struct_tm)]
    timelocal.restype = time_t

# /usr/include/time.h: 271
if _libs["avcodec"].has("dysize", "cdecl"):
    dysize = _libs["avcodec"].get("dysize", "cdecl")
    dysize.argtypes = [c_int]
    dysize.restype = c_int

# /usr/include/time.h: 281
if _libs["avcodec"].has("nanosleep", "cdecl"):
    nanosleep = _libs["avcodec"].get("nanosleep", "cdecl")
    nanosleep.argtypes = [POINTER(struct_timespec), POINTER(struct_timespec)]
    nanosleep.restype = c_int

# /usr/include/time.h: 285
if _libs["avcodec"].has("clock_getres", "cdecl"):
    clock_getres = _libs["avcodec"].get("clock_getres", "cdecl")
    clock_getres.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_getres.restype = c_int

# /usr/include/time.h: 288
if _libs["avcodec"].has("clock_gettime", "cdecl"):
    clock_gettime = _libs["avcodec"].get("clock_gettime", "cdecl")
    clock_gettime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_gettime.restype = c_int

# /usr/include/time.h: 292
if _libs["avcodec"].has("clock_settime", "cdecl"):
    clock_settime = _libs["avcodec"].get("clock_settime", "cdecl")
    clock_settime.argtypes = [clockid_t, POINTER(struct_timespec)]
    clock_settime.restype = c_int

# /usr/include/time.h: 323
if _libs["avcodec"].has("clock_nanosleep", "cdecl"):
    clock_nanosleep = _libs["avcodec"].get("clock_nanosleep", "cdecl")
    clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(struct_timespec), POINTER(struct_timespec)]
    clock_nanosleep.restype = c_int

# /usr/include/time.h: 338
if _libs["avcodec"].has("clock_getcpuclockid", "cdecl"):
    clock_getcpuclockid = _libs["avcodec"].get("clock_getcpuclockid", "cdecl")
    clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
    clock_getcpuclockid.restype = c_int

# /usr/include/time.h: 343
if _libs["avcodec"].has("timer_create", "cdecl"):
    timer_create = _libs["avcodec"].get("timer_create", "cdecl")
    timer_create.argtypes = [clockid_t, POINTER(struct_sigevent), POINTER(timer_t)]
    timer_create.restype = c_int

# /usr/include/time.h: 348
if _libs["avcodec"].has("timer_delete", "cdecl"):
    timer_delete = _libs["avcodec"].get("timer_delete", "cdecl")
    timer_delete.argtypes = [timer_t]
    timer_delete.restype = c_int

# /usr/include/time.h: 352
if _libs["avcodec"].has("timer_settime", "cdecl"):
    timer_settime = _libs["avcodec"].get("timer_settime", "cdecl")
    timer_settime.argtypes = [timer_t, c_int, POINTER(struct_itimerspec), POINTER(struct_itimerspec)]
    timer_settime.restype = c_int

# /usr/include/time.h: 357
if _libs["avcodec"].has("timer_gettime", "cdecl"):
    timer_gettime = _libs["avcodec"].get("timer_gettime", "cdecl")
    timer_gettime.argtypes = [timer_t, POINTER(struct_itimerspec)]
    timer_gettime.restype = c_int

# /usr/include/time.h: 376
if _libs["avcodec"].has("timer_getoverrun", "cdecl"):
    timer_getoverrun = _libs["avcodec"].get("timer_getoverrun", "cdecl")
    timer_getoverrun.argtypes = [timer_t]
    timer_getoverrun.restype = c_int

# /usr/include/time.h: 383
if _libs["avcodec"].has("timespec_get", "cdecl"):
    timespec_get = _libs["avcodec"].get("timespec_get", "cdecl")
    timespec_get.argtypes = [POINTER(struct_timespec), c_int]
    timespec_get.restype = c_int

# /usr/include/libavformat/avio.h: 62
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

AVIOInterruptCB = struct_AVIOInterruptCB# /usr/include/libavformat/avio.h: 62

enum_AVIODirEntryType = c_int# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_UNKNOWN = 0# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_BLOCK_DEVICE = (AVIO_ENTRY_UNKNOWN + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_CHARACTER_DEVICE = (AVIO_ENTRY_BLOCK_DEVICE + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_DIRECTORY = (AVIO_ENTRY_CHARACTER_DEVICE + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_NAMED_PIPE = (AVIO_ENTRY_DIRECTORY + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_SYMBOLIC_LINK = (AVIO_ENTRY_NAMED_PIPE + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_SOCKET = (AVIO_ENTRY_SYMBOLIC_LINK + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_FILE = (AVIO_ENTRY_SOCKET + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_SERVER = (AVIO_ENTRY_FILE + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_SHARE = (AVIO_ENTRY_SERVER + 1)# /usr/include/libavformat/avio.h: 67

AVIO_ENTRY_WORKGROUP = (AVIO_ENTRY_SHARE + 1)# /usr/include/libavformat/avio.h: 67

# /usr/include/libavformat/avio.h: 102
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

AVIODirEntry = struct_AVIODirEntry# /usr/include/libavformat/avio.h: 102

# /usr/include/libavformat/avio.h: 106
class struct_URLContext(Structure):
    pass

# /usr/include/libavformat/avio.h: 107
class struct_AVIODirContext(Structure):
    pass

struct_AVIODirContext.__slots__ = [
    'url_context',
]
struct_AVIODirContext._fields_ = [
    ('url_context', POINTER(struct_URLContext)),
]

AVIODirContext = struct_AVIODirContext# /usr/include/libavformat/avio.h: 107

enum_AVIODataMarkerType = c_int# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_HEADER = 0# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_SYNC_POINT = (AVIO_DATA_MARKER_HEADER + 1)# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_BOUNDARY_POINT = (AVIO_DATA_MARKER_SYNC_POINT + 1)# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_UNKNOWN = (AVIO_DATA_MARKER_BOUNDARY_POINT + 1)# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_TRAILER = (AVIO_DATA_MARKER_UNKNOWN + 1)# /usr/include/libavformat/avio.h: 116

AVIO_DATA_MARKER_FLUSH_POINT = (AVIO_DATA_MARKER_TRAILER + 1)# /usr/include/libavformat/avio.h: 116

# /usr/include/libavformat/avio.h: 313
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
    'error',
    'write_flag',
    'max_packet_size',
    'min_packet_size',
    'checksum',
    'checksum_ptr',
    'update_checksum',
    'read_pause',
    'read_seek',
    'seekable',
    'direct',
    'protocol_whitelist',
    'protocol_blacklist',
    'write_data_type',
    'ignore_boundary_point',
    'buf_ptr_max',
    'bytes_read',
    'bytes_written',
]
struct_AVIOContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('buffer', POINTER(c_ubyte)),
    ('buffer_size', c_int),
    ('buf_ptr', POINTER(c_ubyte)),
    ('buf_end', POINTER(c_ubyte)),
    ('opaque', POINTER(None)),
    ('read_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(uint8_t), c_int)),
    ('write_packet', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(uint8_t), c_int)),
    ('seek', CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int64, c_int)),
    ('pos', c_int64),
    ('eof_reached', c_int),
    ('error', c_int),
    ('write_flag', c_int),
    ('max_packet_size', c_int),
    ('min_packet_size', c_int),
    ('checksum', c_ulong),
    ('checksum_ptr', POINTER(c_ubyte)),
    ('update_checksum', CFUNCTYPE(UNCHECKED(c_ulong), c_ulong, POINTER(uint8_t), c_uint)),
    ('read_pause', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int)),
    ('read_seek', CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int, c_int64, c_int)),
    ('seekable', c_int),
    ('direct', c_int),
    ('protocol_whitelist', String),
    ('protocol_blacklist', String),
    ('write_data_type', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(uint8_t), c_int, enum_AVIODataMarkerType, c_int64)),
    ('ignore_boundary_point', c_int),
    ('buf_ptr_max', POINTER(c_ubyte)),
    ('bytes_read', c_int64),
    ('bytes_written', c_int64),
]

AVIOContext = struct_AVIOContext# /usr/include/libavformat/avio.h: 313

# /usr/include/libavformat/avio.h: 322
if _libs["avformat"].has("avio_find_protocol_name", "cdecl"):
    avio_find_protocol_name = _libs["avformat"].get("avio_find_protocol_name", "cdecl")
    avio_find_protocol_name.argtypes = [String]
    avio_find_protocol_name.restype = c_char_p

# /usr/include/libavformat/avio.h: 336
if _libs["avformat"].has("avio_check", "cdecl"):
    avio_check = _libs["avformat"].get("avio_check", "cdecl")
    avio_check.argtypes = [String, c_int]
    avio_check.restype = c_int

# /usr/include/libavformat/avio.h: 348
if _libs["avformat"].has("avio_open_dir", "cdecl"):
    avio_open_dir = _libs["avformat"].get("avio_open_dir", "cdecl")
    avio_open_dir.argtypes = [POINTER(POINTER(AVIODirContext)), String, POINTER(POINTER(AVDictionary))]
    avio_open_dir.restype = c_int

# /usr/include/libavformat/avio.h: 361
if _libs["avformat"].has("avio_read_dir", "cdecl"):
    avio_read_dir = _libs["avformat"].get("avio_read_dir", "cdecl")
    avio_read_dir.argtypes = [POINTER(AVIODirContext), POINTER(POINTER(AVIODirEntry))]
    avio_read_dir.restype = c_int

# /usr/include/libavformat/avio.h: 372
if _libs["avformat"].has("avio_close_dir", "cdecl"):
    avio_close_dir = _libs["avformat"].get("avio_close_dir", "cdecl")
    avio_close_dir.argtypes = [POINTER(POINTER(AVIODirContext))]
    avio_close_dir.restype = c_int

# /usr/include/libavformat/avio.h: 379
if _libs["avformat"].has("avio_free_directory_entry", "cdecl"):
    avio_free_directory_entry = _libs["avformat"].get("avio_free_directory_entry", "cdecl")
    avio_free_directory_entry.argtypes = [POINTER(POINTER(AVIODirEntry))]
    avio_free_directory_entry.restype = None

# /usr/include/libavformat/avio.h: 404
if _libs["avformat"].has("avio_alloc_context", "cdecl"):
    avio_alloc_context = _libs["avformat"].get("avio_alloc_context", "cdecl")
    avio_alloc_context.argtypes = [POINTER(c_ubyte), c_int, c_int, POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(uint8_t), c_int), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(uint8_t), c_int), CFUNCTYPE(UNCHECKED(c_int64), POINTER(None), c_int64, c_int)]
    avio_alloc_context.restype = POINTER(AVIOContext)

# /usr/include/libavformat/avio.h: 419
if _libs["avformat"].has("avio_context_free", "cdecl"):
    avio_context_free = _libs["avformat"].get("avio_context_free", "cdecl")
    avio_context_free.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_context_free.restype = None

# /usr/include/libavformat/avio.h: 421
if _libs["avformat"].has("avio_w8", "cdecl"):
    avio_w8 = _libs["avformat"].get("avio_w8", "cdecl")
    avio_w8.argtypes = [POINTER(AVIOContext), c_int]
    avio_w8.restype = None

# /usr/include/libavformat/avio.h: 422
if _libs["avformat"].has("avio_write", "cdecl"):
    avio_write = _libs["avformat"].get("avio_write", "cdecl")
    avio_write.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_write.restype = None

# /usr/include/libavformat/avio.h: 423
if _libs["avformat"].has("avio_wl64", "cdecl"):
    avio_wl64 = _libs["avformat"].get("avio_wl64", "cdecl")
    avio_wl64.argtypes = [POINTER(AVIOContext), uint64_t]
    avio_wl64.restype = None

# /usr/include/libavformat/avio.h: 424
if _libs["avformat"].has("avio_wb64", "cdecl"):
    avio_wb64 = _libs["avformat"].get("avio_wb64", "cdecl")
    avio_wb64.argtypes = [POINTER(AVIOContext), uint64_t]
    avio_wb64.restype = None

# /usr/include/libavformat/avio.h: 425
if _libs["avformat"].has("avio_wl32", "cdecl"):
    avio_wl32 = _libs["avformat"].get("avio_wl32", "cdecl")
    avio_wl32.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl32.restype = None

# /usr/include/libavformat/avio.h: 426
if _libs["avformat"].has("avio_wb32", "cdecl"):
    avio_wb32 = _libs["avformat"].get("avio_wb32", "cdecl")
    avio_wb32.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb32.restype = None

# /usr/include/libavformat/avio.h: 427
if _libs["avformat"].has("avio_wl24", "cdecl"):
    avio_wl24 = _libs["avformat"].get("avio_wl24", "cdecl")
    avio_wl24.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl24.restype = None

# /usr/include/libavformat/avio.h: 428
if _libs["avformat"].has("avio_wb24", "cdecl"):
    avio_wb24 = _libs["avformat"].get("avio_wb24", "cdecl")
    avio_wb24.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb24.restype = None

# /usr/include/libavformat/avio.h: 429
if _libs["avformat"].has("avio_wl16", "cdecl"):
    avio_wl16 = _libs["avformat"].get("avio_wl16", "cdecl")
    avio_wl16.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wl16.restype = None

# /usr/include/libavformat/avio.h: 430
if _libs["avformat"].has("avio_wb16", "cdecl"):
    avio_wb16 = _libs["avformat"].get("avio_wb16", "cdecl")
    avio_wb16.argtypes = [POINTER(AVIOContext), c_uint]
    avio_wb16.restype = None

# /usr/include/libavformat/avio.h: 436
if _libs["avformat"].has("avio_put_str", "cdecl"):
    avio_put_str = _libs["avformat"].get("avio_put_str", "cdecl")
    avio_put_str.argtypes = [POINTER(AVIOContext), String]
    avio_put_str.restype = c_int

# /usr/include/libavformat/avio.h: 445
if _libs["avformat"].has("avio_put_str16le", "cdecl"):
    avio_put_str16le = _libs["avformat"].get("avio_put_str16le", "cdecl")
    avio_put_str16le.argtypes = [POINTER(AVIOContext), String]
    avio_put_str16le.restype = c_int

# /usr/include/libavformat/avio.h: 454
if _libs["avformat"].has("avio_put_str16be", "cdecl"):
    avio_put_str16be = _libs["avformat"].get("avio_put_str16be", "cdecl")
    avio_put_str16be.argtypes = [POINTER(AVIOContext), String]
    avio_put_str16be.restype = c_int

# /usr/include/libavformat/avio.h: 467
if _libs["avformat"].has("avio_write_marker", "cdecl"):
    avio_write_marker = _libs["avformat"].get("avio_write_marker", "cdecl")
    avio_write_marker.argtypes = [POINTER(AVIOContext), c_int64, enum_AVIODataMarkerType]
    avio_write_marker.restype = None

# /usr/include/libavformat/avio.h: 488
if _libs["avformat"].has("avio_seek", "cdecl"):
    avio_seek = _libs["avformat"].get("avio_seek", "cdecl")
    avio_seek.argtypes = [POINTER(AVIOContext), c_int64, c_int]
    avio_seek.restype = c_int64

# /usr/include/libavformat/avio.h: 494
if _libs["avformat"].has("avio_skip", "cdecl"):
    avio_skip = _libs["avformat"].get("avio_skip", "cdecl")
    avio_skip.argtypes = [POINTER(AVIOContext), c_int64]
    avio_skip.restype = c_int64

# /usr/include/libavformat/avio.h: 509
if _libs["avformat"].has("avio_size", "cdecl"):
    avio_size = _libs["avformat"].get("avio_size", "cdecl")
    avio_size.argtypes = [POINTER(AVIOContext)]
    avio_size.restype = c_int64

# /usr/include/libavformat/avio.h: 515
if _libs["avformat"].has("avio_feof", "cdecl"):
    avio_feof = _libs["avformat"].get("avio_feof", "cdecl")
    avio_feof.argtypes = [POINTER(AVIOContext)]
    avio_feof.restype = c_int

# /usr/include/libavformat/avio.h: 521
if _libs["avformat"].has("avio_vprintf", "cdecl"):
    avio_vprintf = _libs["avformat"].get("avio_vprintf", "cdecl")
    avio_vprintf.argtypes = [POINTER(AVIOContext), String, c_void_p]
    avio_vprintf.restype = c_int

# /usr/include/libavformat/avio.h: 527
if _libs["avformat"].has("avio_printf", "cdecl"):
    _func = _libs["avformat"].get("avio_printf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [POINTER(AVIOContext), String]
    avio_printf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /usr/include/libavformat/avio.h: 534
if _libs["avformat"].has("avio_print_string_array", "cdecl"):
    avio_print_string_array = _libs["avformat"].get("avio_print_string_array", "cdecl")
    avio_print_string_array.argtypes = [POINTER(AVIOContext), POINTER(POINTER(c_char))]
    avio_print_string_array.restype = None

# /usr/include/libavformat/avio.h: 556
if _libs["avformat"].has("avio_flush", "cdecl"):
    avio_flush = _libs["avformat"].get("avio_flush", "cdecl")
    avio_flush.argtypes = [POINTER(AVIOContext)]
    avio_flush.restype = None

# /usr/include/libavformat/avio.h: 562
if _libs["avformat"].has("avio_read", "cdecl"):
    avio_read = _libs["avformat"].get("avio_read", "cdecl")
    avio_read.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_read.restype = c_int

# /usr/include/libavformat/avio.h: 571
if _libs["avformat"].has("avio_read_partial", "cdecl"):
    avio_read_partial = _libs["avformat"].get("avio_read_partial", "cdecl")
    avio_read_partial.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
    avio_read_partial.restype = c_int

# /usr/include/libavformat/avio.h: 580
if _libs["avformat"].has("avio_r8", "cdecl"):
    avio_r8 = _libs["avformat"].get("avio_r8", "cdecl")
    avio_r8.argtypes = [POINTER(AVIOContext)]
    avio_r8.restype = c_int

# /usr/include/libavformat/avio.h: 581
if _libs["avformat"].has("avio_rl16", "cdecl"):
    avio_rl16 = _libs["avformat"].get("avio_rl16", "cdecl")
    avio_rl16.argtypes = [POINTER(AVIOContext)]
    avio_rl16.restype = c_uint

# /usr/include/libavformat/avio.h: 582
if _libs["avformat"].has("avio_rl24", "cdecl"):
    avio_rl24 = _libs["avformat"].get("avio_rl24", "cdecl")
    avio_rl24.argtypes = [POINTER(AVIOContext)]
    avio_rl24.restype = c_uint

# /usr/include/libavformat/avio.h: 583
if _libs["avformat"].has("avio_rl32", "cdecl"):
    avio_rl32 = _libs["avformat"].get("avio_rl32", "cdecl")
    avio_rl32.argtypes = [POINTER(AVIOContext)]
    avio_rl32.restype = c_uint

# /usr/include/libavformat/avio.h: 584
if _libs["avformat"].has("avio_rl64", "cdecl"):
    avio_rl64 = _libs["avformat"].get("avio_rl64", "cdecl")
    avio_rl64.argtypes = [POINTER(AVIOContext)]
    avio_rl64.restype = uint64_t

# /usr/include/libavformat/avio.h: 585
if _libs["avformat"].has("avio_rb16", "cdecl"):
    avio_rb16 = _libs["avformat"].get("avio_rb16", "cdecl")
    avio_rb16.argtypes = [POINTER(AVIOContext)]
    avio_rb16.restype = c_uint

# /usr/include/libavformat/avio.h: 586
if _libs["avformat"].has("avio_rb24", "cdecl"):
    avio_rb24 = _libs["avformat"].get("avio_rb24", "cdecl")
    avio_rb24.argtypes = [POINTER(AVIOContext)]
    avio_rb24.restype = c_uint

# /usr/include/libavformat/avio.h: 587
if _libs["avformat"].has("avio_rb32", "cdecl"):
    avio_rb32 = _libs["avformat"].get("avio_rb32", "cdecl")
    avio_rb32.argtypes = [POINTER(AVIOContext)]
    avio_rb32.restype = c_uint

# /usr/include/libavformat/avio.h: 588
if _libs["avformat"].has("avio_rb64", "cdecl"):
    avio_rb64 = _libs["avformat"].get("avio_rb64", "cdecl")
    avio_rb64.argtypes = [POINTER(AVIOContext)]
    avio_rb64.restype = uint64_t

# /usr/include/libavformat/avio.h: 605
if _libs["avformat"].has("avio_get_str", "cdecl"):
    avio_get_str = _libs["avformat"].get("avio_get_str", "cdecl")
    avio_get_str.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str.restype = c_int

# /usr/include/libavformat/avio.h: 613
if _libs["avformat"].has("avio_get_str16le", "cdecl"):
    avio_get_str16le = _libs["avformat"].get("avio_get_str16le", "cdecl")
    avio_get_str16le.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str16le.restype = c_int

# /usr/include/libavformat/avio.h: 614
if _libs["avformat"].has("avio_get_str16be", "cdecl"):
    avio_get_str16be = _libs["avformat"].get("avio_get_str16be", "cdecl")
    avio_get_str16be.argtypes = [POINTER(AVIOContext), c_int, String, c_int]
    avio_get_str16be.restype = c_int

# /usr/include/libavformat/avio.h: 666
if _libs["avformat"].has("avio_open", "cdecl"):
    avio_open = _libs["avformat"].get("avio_open", "cdecl")
    avio_open.argtypes = [POINTER(POINTER(AVIOContext)), String, c_int]
    avio_open.restype = c_int

# /usr/include/libavformat/avio.h: 686
if _libs["avformat"].has("avio_open2", "cdecl"):
    avio_open2 = _libs["avformat"].get("avio_open2", "cdecl")
    avio_open2.argtypes = [POINTER(POINTER(AVIOContext)), String, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary))]
    avio_open2.restype = c_int

# /usr/include/libavformat/avio.h: 699
if _libs["avformat"].has("avio_close", "cdecl"):
    avio_close = _libs["avformat"].get("avio_close", "cdecl")
    avio_close.argtypes = [POINTER(AVIOContext)]
    avio_close.restype = c_int

# /usr/include/libavformat/avio.h: 712
if _libs["avformat"].has("avio_closep", "cdecl"):
    avio_closep = _libs["avformat"].get("avio_closep", "cdecl")
    avio_closep.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_closep.restype = c_int

# /usr/include/libavformat/avio.h: 721
if _libs["avformat"].has("avio_open_dyn_buf", "cdecl"):
    avio_open_dyn_buf = _libs["avformat"].get("avio_open_dyn_buf", "cdecl")
    avio_open_dyn_buf.argtypes = [POINTER(POINTER(AVIOContext))]
    avio_open_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 733
if _libs["avformat"].has("avio_get_dyn_buf", "cdecl"):
    avio_get_dyn_buf = _libs["avformat"].get("avio_get_dyn_buf", "cdecl")
    avio_get_dyn_buf.argtypes = [POINTER(AVIOContext), POINTER(POINTER(uint8_t))]
    avio_get_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 744
if _libs["avformat"].has("avio_close_dyn_buf", "cdecl"):
    avio_close_dyn_buf = _libs["avformat"].get("avio_close_dyn_buf", "cdecl")
    avio_close_dyn_buf.argtypes = [POINTER(AVIOContext), POINTER(POINTER(uint8_t))]
    avio_close_dyn_buf.restype = c_int

# /usr/include/libavformat/avio.h: 757
if _libs["avformat"].has("avio_enum_protocols", "cdecl"):
    avio_enum_protocols = _libs["avformat"].get("avio_enum_protocols", "cdecl")
    avio_enum_protocols.argtypes = [POINTER(POINTER(None)), c_int]
    avio_enum_protocols.restype = c_char_p

# /usr/include/libavformat/avio.h: 764
if _libs["avformat"].has("avio_protocol_get_class", "cdecl"):
    avio_protocol_get_class = _libs["avformat"].get("avio_protocol_get_class", "cdecl")
    avio_protocol_get_class.argtypes = [String]
    avio_protocol_get_class.restype = POINTER(AVClass)

# /usr/include/libavformat/avio.h: 773
if _libs["avformat"].has("avio_pause", "cdecl"):
    avio_pause = _libs["avformat"].get("avio_pause", "cdecl")
    avio_pause.argtypes = [POINTER(AVIOContext), c_int]
    avio_pause.restype = c_int

# /usr/include/libavformat/avio.h: 794
if _libs["avformat"].has("avio_seek_time", "cdecl"):
    avio_seek_time = _libs["avformat"].get("avio_seek_time", "cdecl")
    avio_seek_time.argtypes = [POINTER(AVIOContext), c_int, c_int64, c_int]
    avio_seek_time.restype = c_int64

# /usr/include/libavformat/avio.h: 806
if _libs["avformat"].has("avio_read_to_bprint", "cdecl"):
    avio_read_to_bprint = _libs["avformat"].get("avio_read_to_bprint", "cdecl")
    avio_read_to_bprint.argtypes = [POINTER(AVIOContext), POINTER(struct_AVBPrint), c_size_t]
    avio_read_to_bprint.restype = c_int

# /usr/include/libavformat/avio.h: 815
if _libs["avformat"].has("avio_accept", "cdecl"):
    avio_accept = _libs["avformat"].get("avio_accept", "cdecl")
    avio_accept.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVIOContext))]
    avio_accept.restype = c_int

# /usr/include/libavformat/avio.h: 836
if _libs["avformat"].has("avio_handshake", "cdecl"):
    avio_handshake = _libs["avformat"].get("avio_handshake", "cdecl")
    avio_handshake.argtypes = [POINTER(AVIOContext)]
    avio_handshake.restype = c_int

# /usr/include/libavformat/avformat.h: 1110
class struct_AVFormatContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 343
class struct_AVDeviceInfoList(Structure):
    pass

# /usr/include/libavformat/avformat.h: 424
if _libs["avformat"].has("av_get_packet", "cdecl"):
    av_get_packet = _libs["avformat"].get("av_get_packet", "cdecl")
    av_get_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
    av_get_packet.restype = c_int

# /usr/include/libavformat/avformat.h: 441
if _libs["avformat"].has("av_append_packet", "cdecl"):
    av_append_packet = _libs["avformat"].get("av_append_packet", "cdecl")
    av_append_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
    av_append_packet.restype = c_int

# /usr/include/libavformat/avformat.h: 446
class struct_AVCodecTag(Structure):
    pass

# /usr/include/libavformat/avformat.h: 456
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

AVProbeData = struct_AVProbeData# /usr/include/libavformat/avformat.h: 456

# /usr/include/libavformat/avformat.h: 537
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
]

AVOutputFormat = struct_AVOutputFormat# /usr/include/libavformat/avformat.h: 537

# /usr/include/libavformat/avformat.h: 681
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
    'raw_codec_id',
    'priv_data_size',
    'flags_internal',
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
]
struct_AVInputFormat._fields_ = [
    ('name', String),
    ('long_name', String),
    ('flags', c_int),
    ('extensions', String),
    ('codec_tag', POINTER(POINTER(struct_AVCodecTag))),
    ('priv_class', POINTER(AVClass)),
    ('mime_type', String),
    ('raw_codec_id', c_int),
    ('priv_data_size', c_int),
    ('flags_internal', c_int),
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
]

AVInputFormat = struct_AVInputFormat# /usr/include/libavformat/avformat.h: 681

enum_AVStreamParseType = c_int# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_NONE = 0# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_FULL = (AVSTREAM_PARSE_NONE + 1)# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_HEADERS = (AVSTREAM_PARSE_FULL + 1)# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_TIMESTAMPS = (AVSTREAM_PARSE_HEADERS + 1)# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_FULL_ONCE = (AVSTREAM_PARSE_TIMESTAMPS + 1)# /usr/include/libavformat/avformat.h: 686

AVSTREAM_PARSE_FULL_RAW = (AVSTREAM_PARSE_FULL_ONCE + 1)# /usr/include/libavformat/avformat.h: 686

# /usr/include/libavformat/avformat.h: 712
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

AVIndexEntry = struct_AVIndexEntry# /usr/include/libavformat/avformat.h: 712

# /usr/include/libavformat/avformat.h: 816
if _libs["avformat"].has("av_disposition_from_string", "cdecl"):
    av_disposition_from_string = _libs["avformat"].get("av_disposition_from_string", "cdecl")
    av_disposition_from_string.argtypes = [String]
    av_disposition_from_string.restype = c_int

# /usr/include/libavformat/avformat.h: 824
if _libs["avformat"].has("av_disposition_to_string", "cdecl"):
    av_disposition_to_string = _libs["avformat"].get("av_disposition_to_string", "cdecl")
    av_disposition_to_string.argtypes = [c_int]
    av_disposition_to_string.restype = c_char_p

# /usr/include/libavformat/avformat.h: 1008
class struct_AVStream(Structure):
    pass

struct_AVStream.__slots__ = [
    'av_class',
    'index',
    'id',
    'codecpar',
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
    'pts_wrap_bits',
]
struct_AVStream._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('index', c_int),
    ('id', c_int),
    ('codecpar', POINTER(AVCodecParameters)),
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
    ('pts_wrap_bits', c_int),
]

AVStream = struct_AVStream# /usr/include/libavformat/avformat.h: 1008

# /usr/include/libavformat/avformat.h: 1010
if _libs["avformat"].has("av_stream_get_parser", "cdecl"):
    av_stream_get_parser = _libs["avformat"].get("av_stream_get_parser", "cdecl")
    av_stream_get_parser.argtypes = [POINTER(AVStream)]
    av_stream_get_parser.restype = POINTER(struct_AVCodecParserContext)

# /usr/include/libavformat/avformat.h: 1019
if _libs["avformat"].has("av_stream_get_end_pts", "cdecl"):
    av_stream_get_end_pts = _libs["avformat"].get("av_stream_get_end_pts", "cdecl")
    av_stream_get_end_pts.argtypes = [POINTER(AVStream)]
    av_stream_get_end_pts.restype = c_int64

# /usr/include/libavformat/avformat.h: 1023
if _libs["avformat"].has("av_stream_get_first_dts", "cdecl"):
    av_stream_get_first_dts = _libs["avformat"].get("av_stream_get_first_dts", "cdecl")
    av_stream_get_first_dts.argtypes = [POINTER(AVStream)]
    av_stream_get_first_dts.restype = c_int64

# /usr/include/libavformat/avformat.h: 1059
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

AVProgram = struct_AVProgram# /usr/include/libavformat/avformat.h: 1059

# /usr/include/libavformat/avformat.h: 1074
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
    ('id', c_int64),
    ('time_base', AVRational),
    ('start', c_int64),
    ('end', c_int64),
    ('metadata', POINTER(AVDictionary)),
]

AVChapter = struct_AVChapter# /usr/include/libavformat/avformat.h: 1074

av_format_control_message = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), c_int, POINTER(None), c_size_t)# /usr/include/libavformat/avformat.h: 1080

AVOpenCallback = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(POINTER(AVIOContext)), String, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary)))# /usr/include/libavformat/avformat.h: 1083

enum_AVDurationEstimationMethod = c_int# /usr/include/libavformat/avformat.h: 1090

AVFMT_DURATION_FROM_PTS = 0# /usr/include/libavformat/avformat.h: 1090

AVFMT_DURATION_FROM_STREAM = (AVFMT_DURATION_FROM_PTS + 1)# /usr/include/libavformat/avformat.h: 1090

AVFMT_DURATION_FROM_BITRATE = (AVFMT_DURATION_FROM_STREAM + 1)# /usr/include/libavformat/avformat.h: 1090

struct_AVFormatContext.__slots__ = [
    'av_class',
    'iformat',
    'oformat',
    'priv_data',
    'pb',
    'ctx_flags',
    'nb_streams',
    'streams',
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
    'protocol_whitelist',
    'io_open',
    'io_close',
    'protocol_blacklist',
    'max_streams',
    'skip_estimate_duration_from_pts',
    'max_probe_packets',
    'io_close2',
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
    ('url', String),
    ('start_time', c_int64),
    ('duration', c_int64),
    ('bit_rate', c_int64),
    ('packet_size', c_uint),
    ('max_delay', c_int),
    ('flags', c_int),
    ('probesize', c_int64),
    ('max_analyze_duration', c_int64),
    ('key', POINTER(uint8_t)),
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
    ('io_repositioned', c_int),
    ('video_codec', POINTER(AVCodec)),
    ('audio_codec', POINTER(AVCodec)),
    ('subtitle_codec', POINTER(AVCodec)),
    ('data_codec', POINTER(AVCodec)),
    ('metadata_header_padding', c_int),
    ('opaque', POINTER(None)),
    ('control_message_cb', av_format_control_message),
    ('output_ts_offset', c_int64),
    ('dump_separator', POINTER(uint8_t)),
    ('data_codec_id', enum_AVCodecID),
    ('protocol_whitelist', String),
    ('io_open', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(POINTER(AVIOContext)), String, c_int, POINTER(POINTER(AVDictionary)))),
    ('io_close', CFUNCTYPE(UNCHECKED(None), POINTER(struct_AVFormatContext), POINTER(AVIOContext))),
    ('protocol_blacklist', String),
    ('max_streams', c_int),
    ('skip_estimate_duration_from_pts', c_int),
    ('max_probe_packets', c_int),
    ('io_close2', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_AVFormatContext), POINTER(AVIOContext))),
]

AVFormatContext = struct_AVFormatContext# /usr/include/libavformat/avformat.h: 1720

# /usr/include/libavformat/avformat.h: 1726
if _libs["avformat"].has("av_format_inject_global_side_data", "cdecl"):
    av_format_inject_global_side_data = _libs["avformat"].get("av_format_inject_global_side_data", "cdecl")
    av_format_inject_global_side_data.argtypes = [POINTER(AVFormatContext)]
    av_format_inject_global_side_data.restype = None

# /usr/include/libavformat/avformat.h: 1733
if _libs["avformat"].has("av_fmt_ctx_get_duration_estimation_method", "cdecl"):
    av_fmt_ctx_get_duration_estimation_method = _libs["avformat"].get("av_fmt_ctx_get_duration_estimation_method", "cdecl")
    av_fmt_ctx_get_duration_estimation_method.argtypes = [POINTER(AVFormatContext)]
    av_fmt_ctx_get_duration_estimation_method.restype = enum_AVDurationEstimationMethod

# /usr/include/libavformat/avformat.h: 1747
if _libs["avformat"].has("avformat_version", "cdecl"):
    avformat_version = _libs["avformat"].get("avformat_version", "cdecl")
    avformat_version.argtypes = []
    avformat_version.restype = c_uint

# /usr/include/libavformat/avformat.h: 1752
if _libs["avformat"].has("avformat_configuration", "cdecl"):
    avformat_configuration = _libs["avformat"].get("avformat_configuration", "cdecl")
    avformat_configuration.argtypes = []
    avformat_configuration.restype = c_char_p

# /usr/include/libavformat/avformat.h: 1757
if _libs["avformat"].has("avformat_license", "cdecl"):
    avformat_license = _libs["avformat"].get("avformat_license", "cdecl")
    avformat_license.argtypes = []
    avformat_license.restype = c_char_p

# /usr/include/libavformat/avformat.h: 1773
if _libs["avformat"].has("avformat_network_init", "cdecl"):
    avformat_network_init = _libs["avformat"].get("avformat_network_init", "cdecl")
    avformat_network_init.argtypes = []
    avformat_network_init.restype = c_int

# /usr/include/libavformat/avformat.h: 1779
if _libs["avformat"].has("avformat_network_deinit", "cdecl"):
    avformat_network_deinit = _libs["avformat"].get("avformat_network_deinit", "cdecl")
    avformat_network_deinit.argtypes = []
    avformat_network_deinit.restype = c_int

# /usr/include/libavformat/avformat.h: 1790
if _libs["avformat"].has("av_muxer_iterate", "cdecl"):
    av_muxer_iterate = _libs["avformat"].get("av_muxer_iterate", "cdecl")
    av_muxer_iterate.argtypes = [POINTER(POINTER(None))]
    av_muxer_iterate.restype = POINTER(AVOutputFormat)

# /usr/include/libavformat/avformat.h: 1801
if _libs["avformat"].has("av_demuxer_iterate", "cdecl"):
    av_demuxer_iterate = _libs["avformat"].get("av_demuxer_iterate", "cdecl")
    av_demuxer_iterate.argtypes = [POINTER(POINTER(None))]
    av_demuxer_iterate.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 1808
if _libs["avformat"].has("avformat_alloc_context", "cdecl"):
    avformat_alloc_context = _libs["avformat"].get("avformat_alloc_context", "cdecl")
    avformat_alloc_context.argtypes = []
    avformat_alloc_context.restype = POINTER(AVFormatContext)

# /usr/include/libavformat/avformat.h: 1814
if _libs["avformat"].has("avformat_free_context", "cdecl"):
    avformat_free_context = _libs["avformat"].get("avformat_free_context", "cdecl")
    avformat_free_context.argtypes = [POINTER(AVFormatContext)]
    avformat_free_context.restype = None

# /usr/include/libavformat/avformat.h: 1822
if _libs["avformat"].has("avformat_get_class", "cdecl"):
    avformat_get_class = _libs["avformat"].get("avformat_get_class", "cdecl")
    avformat_get_class.argtypes = []
    avformat_get_class.restype = POINTER(AVClass)

# /usr/include/libavformat/avformat.h: 1830
if _libs["avformat"].has("av_stream_get_class", "cdecl"):
    av_stream_get_class = _libs["avformat"].get("av_stream_get_class", "cdecl")
    av_stream_get_class.argtypes = []
    av_stream_get_class.restype = POINTER(AVClass)

# /usr/include/libavformat/avformat.h: 1849
if _libs["avformat"].has("avformat_new_stream", "cdecl"):
    avformat_new_stream = _libs["avformat"].get("avformat_new_stream", "cdecl")
    avformat_new_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
    avformat_new_stream.restype = POINTER(AVStream)

# /usr/include/libavformat/avformat.h: 1864
if _libs["avformat"].has("av_stream_add_side_data", "cdecl"):
    av_stream_add_side_data = _libs["avformat"].get("av_stream_add_side_data", "cdecl")
    av_stream_add_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, POINTER(uint8_t), c_size_t]
    av_stream_add_side_data.restype = c_int

# /usr/include/libavformat/avformat.h: 1876
if _libs["avformat"].has("av_stream_new_side_data", "cdecl"):
    av_stream_new_side_data = _libs["avformat"].get("av_stream_new_side_data", "cdecl")
    av_stream_new_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, c_size_t]
    av_stream_new_side_data.restype = POINTER(uint8_t)

# /usr/include/libavformat/avformat.h: 1888
if _libs["avformat"].has("av_stream_get_side_data", "cdecl"):
    av_stream_get_side_data = _libs["avformat"].get("av_stream_get_side_data", "cdecl")
    av_stream_get_side_data.argtypes = [POINTER(AVStream), enum_AVPacketSideDataType, POINTER(c_size_t)]
    av_stream_get_side_data.restype = POINTER(uint8_t)

# /usr/include/libavformat/avformat.h: 1891
if _libs["avformat"].has("av_new_program", "cdecl"):
    av_new_program = _libs["avformat"].get("av_new_program", "cdecl")
    av_new_program.argtypes = [POINTER(AVFormatContext), c_int]
    av_new_program.restype = POINTER(AVProgram)

# /usr/include/libavformat/avformat.h: 1915
if _libs["avformat"].has("avformat_alloc_output_context2", "cdecl"):
    avformat_alloc_output_context2 = _libs["avformat"].get("avformat_alloc_output_context2", "cdecl")
    avformat_alloc_output_context2.argtypes = [POINTER(POINTER(AVFormatContext)), POINTER(AVOutputFormat), String, String]
    avformat_alloc_output_context2.restype = c_int

# /usr/include/libavformat/avformat.h: 1926
if _libs["avformat"].has("av_find_input_format", "cdecl"):
    av_find_input_format = _libs["avformat"].get("av_find_input_format", "cdecl")
    av_find_input_format.argtypes = [String]
    av_find_input_format.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 1935
if _libs["avformat"].has("av_probe_input_format", "cdecl"):
    av_probe_input_format = _libs["avformat"].get("av_probe_input_format", "cdecl")
    av_probe_input_format.argtypes = [POINTER(AVProbeData), c_int]
    av_probe_input_format.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 1949
if _libs["avformat"].has("av_probe_input_format2", "cdecl"):
    av_probe_input_format2 = _libs["avformat"].get("av_probe_input_format2", "cdecl")
    av_probe_input_format2.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
    av_probe_input_format2.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 1959
if _libs["avformat"].has("av_probe_input_format3", "cdecl"):
    av_probe_input_format3 = _libs["avformat"].get("av_probe_input_format3", "cdecl")
    av_probe_input_format3.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
    av_probe_input_format3.restype = POINTER(AVInputFormat)

# /usr/include/libavformat/avformat.h: 1979
if _libs["avformat"].has("av_probe_input_buffer2", "cdecl"):
    av_probe_input_buffer2 = _libs["avformat"].get("av_probe_input_buffer2", "cdecl")
    av_probe_input_buffer2.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVInputFormat)), String, POINTER(None), c_uint, c_uint]
    av_probe_input_buffer2.restype = c_int

# /usr/include/libavformat/avformat.h: 1986
if _libs["avformat"].has("av_probe_input_buffer", "cdecl"):
    av_probe_input_buffer = _libs["avformat"].get("av_probe_input_buffer", "cdecl")
    av_probe_input_buffer.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVInputFormat)), String, POINTER(None), c_uint, c_uint]
    av_probe_input_buffer.restype = c_int

# /usr/include/libavformat/avformat.h: 2012
if _libs["avformat"].has("avformat_open_input", "cdecl"):
    avformat_open_input = _libs["avformat"].get("avformat_open_input", "cdecl")
    avformat_open_input.argtypes = [POINTER(POINTER(AVFormatContext)), String, POINTER(AVInputFormat), POINTER(POINTER(AVDictionary))]
    avformat_open_input.restype = c_int

# /usr/include/libavformat/avformat.h: 2036
if _libs["avformat"].has("avformat_find_stream_info", "cdecl"):
    avformat_find_stream_info = _libs["avformat"].get("avformat_find_stream_info", "cdecl")
    avformat_find_stream_info.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_find_stream_info.restype = c_int

# /usr/include/libavformat/avformat.h: 2049
if _libs["avformat"].has("av_find_program_from_stream", "cdecl"):
    av_find_program_from_stream = _libs["avformat"].get("av_find_program_from_stream", "cdecl")
    av_find_program_from_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVProgram), c_int]
    av_find_program_from_stream.restype = POINTER(AVProgram)

# /usr/include/libavformat/avformat.h: 2051
if _libs["avformat"].has("av_program_add_stream_index", "cdecl"):
    av_program_add_stream_index = _libs["avformat"].get("av_program_add_stream_index", "cdecl")
    av_program_add_stream_index.argtypes = [POINTER(AVFormatContext), c_int, c_uint]
    av_program_add_stream_index.restype = None

# /usr/include/libavformat/avformat.h: 2079
if _libs["avformat"].has("av_find_best_stream", "cdecl"):
    av_find_best_stream = _libs["avformat"].get("av_find_best_stream", "cdecl")
    av_find_best_stream.argtypes = [POINTER(AVFormatContext), enum_AVMediaType, c_int, c_int, POINTER(POINTER(AVCodec)), c_int]
    av_find_best_stream.restype = c_int

# /usr/include/libavformat/avformat.h: 2113
if _libs["avformat"].has("av_read_frame", "cdecl"):
    av_read_frame = _libs["avformat"].get("av_read_frame", "cdecl")
    av_read_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
    av_read_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2129
if _libs["avformat"].has("av_seek_frame", "cdecl"):
    av_seek_frame = _libs["avformat"].get("av_seek_frame", "cdecl")
    av_seek_frame.argtypes = [POINTER(AVFormatContext), c_int, c_int64, c_int]
    av_seek_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2158
if _libs["avformat"].has("avformat_seek_file", "cdecl"):
    avformat_seek_file = _libs["avformat"].get("avformat_seek_file", "cdecl")
    avformat_seek_file.argtypes = [POINTER(AVFormatContext), c_int, c_int64, c_int64, c_int64, c_int]
    avformat_seek_file.restype = c_int

# /usr/include/libavformat/avformat.h: 2176
if _libs["avformat"].has("avformat_flush", "cdecl"):
    avformat_flush = _libs["avformat"].get("avformat_flush", "cdecl")
    avformat_flush.argtypes = [POINTER(AVFormatContext)]
    avformat_flush.restype = c_int

# /usr/include/libavformat/avformat.h: 2182
if _libs["avformat"].has("av_read_play", "cdecl"):
    av_read_play = _libs["avformat"].get("av_read_play", "cdecl")
    av_read_play.argtypes = [POINTER(AVFormatContext)]
    av_read_play.restype = c_int

# /usr/include/libavformat/avformat.h: 2189
if _libs["avformat"].has("av_read_pause", "cdecl"):
    av_read_pause = _libs["avformat"].get("av_read_pause", "cdecl")
    av_read_pause.argtypes = [POINTER(AVFormatContext)]
    av_read_pause.restype = c_int

# /usr/include/libavformat/avformat.h: 2195
if _libs["avformat"].has("avformat_close_input", "cdecl"):
    avformat_close_input = _libs["avformat"].get("avformat_close_input", "cdecl")
    avformat_close_input.argtypes = [POINTER(POINTER(AVFormatContext))]
    avformat_close_input.restype = None

# /usr/include/libavformat/avformat.h: 2237
if _libs["avformat"].has("avformat_write_header", "cdecl"):
    avformat_write_header = _libs["avformat"].get("avformat_write_header", "cdecl")
    avformat_write_header.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_write_header.restype = c_int

# /usr/include/libavformat/avformat.h: 2265
if _libs["avformat"].has("avformat_init_output", "cdecl"):
    avformat_init_output = _libs["avformat"].get("avformat_init_output", "cdecl")
    avformat_init_output.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
    avformat_init_output.restype = c_int

# /usr/include/libavformat/avformat.h: 2304
if _libs["avformat"].has("av_write_frame", "cdecl"):
    av_write_frame = _libs["avformat"].get("av_write_frame", "cdecl")
    av_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
    av_write_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2348
if _libs["avformat"].has("av_interleaved_write_frame", "cdecl"):
    av_interleaved_write_frame = _libs["avformat"].get("av_interleaved_write_frame", "cdecl")
    av_interleaved_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
    av_interleaved_write_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2358
if _libs["avformat"].has("av_write_uncoded_frame", "cdecl"):
    av_write_uncoded_frame = _libs["avformat"].get("av_write_uncoded_frame", "cdecl")
    av_write_uncoded_frame.argtypes = [POINTER(AVFormatContext), c_int, POINTER(AVFrame)]
    av_write_uncoded_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2377
if _libs["avformat"].has("av_interleaved_write_uncoded_frame", "cdecl"):
    av_interleaved_write_uncoded_frame = _libs["avformat"].get("av_interleaved_write_uncoded_frame", "cdecl")
    av_interleaved_write_uncoded_frame.argtypes = [POINTER(AVFormatContext), c_int, POINTER(AVFrame)]
    av_interleaved_write_uncoded_frame.restype = c_int

# /usr/include/libavformat/avformat.h: 2386
if _libs["avformat"].has("av_write_uncoded_frame_query", "cdecl"):
    av_write_uncoded_frame_query = _libs["avformat"].get("av_write_uncoded_frame_query", "cdecl")
    av_write_uncoded_frame_query.argtypes = [POINTER(AVFormatContext), c_int]
    av_write_uncoded_frame_query.restype = c_int

# /usr/include/libavformat/avformat.h: 2397
if _libs["avformat"].has("av_write_trailer", "cdecl"):
    av_write_trailer = _libs["avformat"].get("av_write_trailer", "cdecl")
    av_write_trailer.argtypes = [POINTER(AVFormatContext)]
    av_write_trailer.restype = c_int

# /usr/include/libavformat/avformat.h: 2411
if _libs["avformat"].has("av_guess_format", "cdecl"):
    av_guess_format = _libs["avformat"].get("av_guess_format", "cdecl")
    av_guess_format.argtypes = [String, String, String]
    av_guess_format.restype = POINTER(AVOutputFormat)

# /usr/include/libavformat/avformat.h: 2418
if _libs["avformat"].has("av_guess_codec", "cdecl"):
    av_guess_codec = _libs["avformat"].get("av_guess_codec", "cdecl")
    av_guess_codec.argtypes = [POINTER(AVOutputFormat), String, String, String, enum_AVMediaType]
    av_guess_codec.restype = enum_AVCodecID

# /usr/include/libavformat/avformat.h: 2439
if _libs["avformat"].has("av_get_output_timestamp", "cdecl"):
    av_get_output_timestamp = _libs["avformat"].get("av_get_output_timestamp", "cdecl")
    av_get_output_timestamp.argtypes = [POINTER(struct_AVFormatContext), c_int, POINTER(c_int64), POINTER(c_int64)]
    av_get_output_timestamp.restype = c_int

# /usr/include/libavformat/avformat.h: 2466
if _libs["avformat"].has("av_hex_dump", "cdecl"):
    av_hex_dump = _libs["avformat"].get("av_hex_dump", "cdecl")
    av_hex_dump.argtypes = [POINTER(FILE), POINTER(uint8_t), c_int]
    av_hex_dump.restype = None

# /usr/include/libavformat/avformat.h: 2480
if _libs["avformat"].has("av_hex_dump_log", "cdecl"):
    av_hex_dump_log = _libs["avformat"].get("av_hex_dump_log", "cdecl")
    av_hex_dump_log.argtypes = [POINTER(None), c_int, POINTER(uint8_t), c_int]
    av_hex_dump_log.restype = None

# /usr/include/libavformat/avformat.h: 2490
if _libs["avformat"].has("av_pkt_dump2", "cdecl"):
    av_pkt_dump2 = _libs["avformat"].get("av_pkt_dump2", "cdecl")
    av_pkt_dump2.argtypes = [POINTER(FILE), POINTER(AVPacket), c_int, POINTER(AVStream)]
    av_pkt_dump2.restype = None

# /usr/include/libavformat/avformat.h: 2504
if _libs["avformat"].has("av_pkt_dump_log2", "cdecl"):
    av_pkt_dump_log2 = _libs["avformat"].get("av_pkt_dump_log2", "cdecl")
    av_pkt_dump_log2.argtypes = [POINTER(None), c_int, POINTER(AVPacket), c_int, POINTER(AVStream)]
    av_pkt_dump_log2.restype = None

# /usr/include/libavformat/avformat.h: 2515
if _libs["avformat"].has("av_codec_get_id", "cdecl"):
    av_codec_get_id = _libs["avformat"].get("av_codec_get_id", "cdecl")
    av_codec_get_id.argtypes = [POINTER(POINTER(struct_AVCodecTag)), c_uint]
    av_codec_get_id.restype = enum_AVCodecID

# /usr/include/libavformat/avformat.h: 2525
if _libs["avformat"].has("av_codec_get_tag", "cdecl"):
    av_codec_get_tag = _libs["avformat"].get("av_codec_get_tag", "cdecl")
    av_codec_get_tag.argtypes = [POINTER(POINTER(struct_AVCodecTag)), enum_AVCodecID]
    av_codec_get_tag.restype = c_uint

# /usr/include/libavformat/avformat.h: 2536
if _libs["avformat"].has("av_codec_get_tag2", "cdecl"):
    av_codec_get_tag2 = _libs["avformat"].get("av_codec_get_tag2", "cdecl")
    av_codec_get_tag2.argtypes = [POINTER(POINTER(struct_AVCodecTag)), enum_AVCodecID, POINTER(c_uint)]
    av_codec_get_tag2.restype = c_int

# /usr/include/libavformat/avformat.h: 2539
if _libs["avformat"].has("av_find_default_stream_index", "cdecl"):
    av_find_default_stream_index = _libs["avformat"].get("av_find_default_stream_index", "cdecl")
    av_find_default_stream_index.argtypes = [POINTER(AVFormatContext)]
    av_find_default_stream_index.restype = c_int

# /usr/include/libavformat/avformat.h: 2552
if _libs["avformat"].has("av_index_search_timestamp", "cdecl"):
    av_index_search_timestamp = _libs["avformat"].get("av_index_search_timestamp", "cdecl")
    av_index_search_timestamp.argtypes = [POINTER(AVStream), c_int64, c_int]
    av_index_search_timestamp.restype = c_int

# /usr/include/libavformat/avformat.h: 2560
if _libs["avformat"].has("avformat_index_get_entries_count", "cdecl"):
    avformat_index_get_entries_count = _libs["avformat"].get("avformat_index_get_entries_count", "cdecl")
    avformat_index_get_entries_count.argtypes = [POINTER(AVStream)]
    avformat_index_get_entries_count.restype = c_int

# /usr/include/libavformat/avformat.h: 2573
if _libs["avformat"].has("avformat_index_get_entry", "cdecl"):
    avformat_index_get_entry = _libs["avformat"].get("avformat_index_get_entry", "cdecl")
    avformat_index_get_entry.argtypes = [POINTER(AVStream), c_int]
    avformat_index_get_entry.restype = POINTER(AVIndexEntry)

# /usr/include/libavformat/avformat.h: 2590
if _libs["avformat"].has("avformat_index_get_entry_from_timestamp", "cdecl"):
    avformat_index_get_entry_from_timestamp = _libs["avformat"].get("avformat_index_get_entry_from_timestamp", "cdecl")
    avformat_index_get_entry_from_timestamp.argtypes = [POINTER(AVStream), c_int64, c_int]
    avformat_index_get_entry_from_timestamp.restype = POINTER(AVIndexEntry)

# /usr/include/libavformat/avformat.h: 2599
if _libs["avformat"].has("av_add_index_entry", "cdecl"):
    av_add_index_entry = _libs["avformat"].get("av_add_index_entry", "cdecl")
    av_add_index_entry.argtypes = [POINTER(AVStream), c_int64, c_int64, c_int, c_int, c_int]
    av_add_index_entry.restype = c_int

# /usr/include/libavformat/avformat.h: 2622
if _libs["avformat"].has("av_url_split", "cdecl"):
    av_url_split = _libs["avformat"].get("av_url_split", "cdecl")
    av_url_split.argtypes = [String, c_int, String, c_int, String, c_int, POINTER(c_int), String, c_int, String]
    av_url_split.restype = None

# /usr/include/libavformat/avformat.h: 2640
if _libs["avformat"].has("av_dump_format", "cdecl"):
    av_dump_format = _libs["avformat"].get("av_dump_format", "cdecl")
    av_dump_format.argtypes = [POINTER(AVFormatContext), c_int, String, c_int]
    av_dump_format.restype = None

# /usr/include/libavformat/avformat.h: 2661
if _libs["avformat"].has("av_get_frame_filename2", "cdecl"):
    av_get_frame_filename2 = _libs["avformat"].get("av_get_frame_filename2", "cdecl")
    av_get_frame_filename2.argtypes = [String, c_int, String, c_int, c_int]
    av_get_frame_filename2.restype = c_int

# /usr/include/libavformat/avformat.h: 2664
if _libs["avformat"].has("av_get_frame_filename", "cdecl"):
    av_get_frame_filename = _libs["avformat"].get("av_get_frame_filename", "cdecl")
    av_get_frame_filename.argtypes = [String, c_int, String, c_int]
    av_get_frame_filename.restype = c_int

# /usr/include/libavformat/avformat.h: 2673
if _libs["avformat"].has("av_filename_number_test", "cdecl"):
    av_filename_number_test = _libs["avformat"].get("av_filename_number_test", "cdecl")
    av_filename_number_test.argtypes = [String]
    av_filename_number_test.restype = c_int

# /usr/include/libavformat/avformat.h: 2692
if _libs["avformat"].has("av_sdp_create", "cdecl"):
    av_sdp_create = _libs["avformat"].get("av_sdp_create", "cdecl")
    av_sdp_create.argtypes = [POINTER(POINTER(AVFormatContext)), c_int, String, c_int]
    av_sdp_create.restype = c_int

# /usr/include/libavformat/avformat.h: 2701
if _libs["avformat"].has("av_match_ext", "cdecl"):
    av_match_ext = _libs["avformat"].get("av_match_ext", "cdecl")
    av_match_ext.argtypes = [String, String]
    av_match_ext.restype = c_int

# /usr/include/libavformat/avformat.h: 2713
if _libs["avformat"].has("avformat_query_codec", "cdecl"):
    avformat_query_codec = _libs["avformat"].get("avformat_query_codec", "cdecl")
    avformat_query_codec.argtypes = [POINTER(AVOutputFormat), enum_AVCodecID, c_int]
    avformat_query_codec.restype = c_int

# /usr/include/libavformat/avformat.h: 2731
if _libs["avformat"].has("avformat_get_riff_video_tags", "cdecl"):
    avformat_get_riff_video_tags = _libs["avformat"].get("avformat_get_riff_video_tags", "cdecl")
    avformat_get_riff_video_tags.argtypes = []
    avformat_get_riff_video_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2735
if _libs["avformat"].has("avformat_get_riff_audio_tags", "cdecl"):
    avformat_get_riff_audio_tags = _libs["avformat"].get("avformat_get_riff_audio_tags", "cdecl")
    avformat_get_riff_audio_tags.argtypes = []
    avformat_get_riff_audio_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2739
if _libs["avformat"].has("avformat_get_mov_video_tags", "cdecl"):
    avformat_get_mov_video_tags = _libs["avformat"].get("avformat_get_mov_video_tags", "cdecl")
    avformat_get_mov_video_tags.argtypes = []
    avformat_get_mov_video_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2743
if _libs["avformat"].has("avformat_get_mov_audio_tags", "cdecl"):
    avformat_get_mov_audio_tags = _libs["avformat"].get("avformat_get_mov_audio_tags", "cdecl")
    avformat_get_mov_audio_tags.argtypes = []
    avformat_get_mov_audio_tags.restype = POINTER(struct_AVCodecTag)

# /usr/include/libavformat/avformat.h: 2766
if _libs["avformat"].has("av_guess_sample_aspect_ratio", "cdecl"):
    av_guess_sample_aspect_ratio = _libs["avformat"].get("av_guess_sample_aspect_ratio", "cdecl")
    av_guess_sample_aspect_ratio.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), POINTER(AVFrame)]
    av_guess_sample_aspect_ratio.restype = AVRational

# /usr/include/libavformat/avformat.h: 2776
if _libs["avformat"].has("av_guess_frame_rate", "cdecl"):
    av_guess_frame_rate = _libs["avformat"].get("av_guess_frame_rate", "cdecl")
    av_guess_frame_rate.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), POINTER(AVFrame)]
    av_guess_frame_rate.restype = AVRational

# /usr/include/libavformat/avformat.h: 2791
if _libs["avformat"].has("avformat_match_stream_specifier", "cdecl"):
    avformat_match_stream_specifier = _libs["avformat"].get("avformat_match_stream_specifier", "cdecl")
    avformat_match_stream_specifier.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), String]
    avformat_match_stream_specifier.restype = c_int

# /usr/include/libavformat/avformat.h: 2794
if _libs["avformat"].has("avformat_queue_attached_pictures", "cdecl"):
    avformat_queue_attached_pictures = _libs["avformat"].get("avformat_queue_attached_pictures", "cdecl")
    avformat_queue_attached_pictures.argtypes = [POINTER(AVFormatContext)]
    avformat_queue_attached_pictures.restype = c_int

enum_AVTimebaseSource = c_int# /usr/include/libavformat/avformat.h: 2796

AVFMT_TBCF_AUTO = (-1)# /usr/include/libavformat/avformat.h: 2796

AVFMT_TBCF_DECODER = (AVFMT_TBCF_AUTO + 1)# /usr/include/libavformat/avformat.h: 2796

AVFMT_TBCF_DEMUXER = (AVFMT_TBCF_DECODER + 1)# /usr/include/libavformat/avformat.h: 2796

AVFMT_TBCF_R_FRAMERATE = (AVFMT_TBCF_DEMUXER + 1)# /usr/include/libavformat/avformat.h: 2796

# /usr/include/libavformat/avformat.h: 2815
if _libs["avformat"].has("avformat_transfer_internal_stream_timing_info", "cdecl"):
    avformat_transfer_internal_stream_timing_info = _libs["avformat"].get("avformat_transfer_internal_stream_timing_info", "cdecl")
    avformat_transfer_internal_stream_timing_info.argtypes = [POINTER(AVOutputFormat), POINTER(AVStream), POINTER(AVStream), enum_AVTimebaseSource]
    avformat_transfer_internal_stream_timing_info.restype = c_int

# /usr/include/libavformat/avformat.h: 2824
if _libs["avformat"].has("av_stream_get_codec_timebase", "cdecl"):
    av_stream_get_codec_timebase = _libs["avformat"].get("av_stream_get_codec_timebase", "cdecl")
    av_stream_get_codec_timebase.argtypes = [POINTER(AVStream)]
    av_stream_get_codec_timebase.restype = AVRational

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 62
if _libs["avdevice"].has("avdevice_version", "cdecl"):
    avdevice_version = _libs["avdevice"].get("avdevice_version", "cdecl")
    avdevice_version.argtypes = []
    avdevice_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 67
if _libs["avdevice"].has("avdevice_configuration", "cdecl"):
    avdevice_configuration = _libs["avdevice"].get("avdevice_configuration", "cdecl")
    avdevice_configuration.argtypes = []
    avdevice_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 72
if _libs["avdevice"].has("avdevice_license", "cdecl"):
    avdevice_license = _libs["avdevice"].get("avdevice_license", "cdecl")
    avdevice_license.argtypes = []
    avdevice_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 77
if _libs["avdevice"].has("avdevice_register_all", "cdecl"):
    avdevice_register_all = _libs["avdevice"].get("avdevice_register_all", "cdecl")
    avdevice_register_all.argtypes = []
    avdevice_register_all.restype = None

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 86
if _libs["avdevice"].has("av_input_audio_device_next", "cdecl"):
    av_input_audio_device_next = _libs["avdevice"].get("av_input_audio_device_next", "cdecl")
    av_input_audio_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_audio_device_next.restype = POINTER(AVInputFormat)

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 95
if _libs["avdevice"].has("av_input_video_device_next", "cdecl"):
    av_input_video_device_next = _libs["avdevice"].get("av_input_video_device_next", "cdecl")
    av_input_video_device_next.argtypes = [POINTER(AVInputFormat)]
    av_input_video_device_next.restype = POINTER(AVInputFormat)

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 104
if _libs["avdevice"].has("av_output_audio_device_next", "cdecl"):
    av_output_audio_device_next = _libs["avdevice"].get("av_output_audio_device_next", "cdecl")
    av_output_audio_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_audio_device_next.restype = POINTER(AVOutputFormat)

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 113
if _libs["avdevice"].has("av_output_video_device_next", "cdecl"):
    av_output_video_device_next = _libs["avdevice"].get("av_output_video_device_next", "cdecl")
    av_output_video_device_next.argtypes = [POINTER(AVOutputFormat)]
    av_output_video_device_next.restype = POINTER(AVOutputFormat)

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 120
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

AVDeviceRect = struct_AVDeviceRect# /home/josiah/ctypesgen_test/av/av/avdevice.h: 120

enum_AVAppToDevMessageType = c_int# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_NONE = (((ord('E') | (ord('N') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(ord('N')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_WINDOW_SIZE = (((ord('M') | (ord('O') << 8)) | (ord('E') << 16)) | ((c_uint (ord_if_char(ord('G')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_WINDOW_REPAINT = (((ord('A') | (ord('P') << 8)) | (ord('E') << 16)) | ((c_uint (ord_if_char(ord('R')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_PAUSE = (((ord(' ') | (ord('U') << 8)) | (ord('A') << 16)) | ((c_uint (ord_if_char(ord('P')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_PLAY = (((ord('Y') | (ord('A') << 8)) | (ord('L') << 16)) | ((c_uint (ord_if_char(ord('P')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_TOGGLE_PAUSE = (((ord('T') | (ord('U') << 8)) | (ord('A') << 16)) | ((c_uint (ord_if_char(ord('P')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_SET_VOLUME = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(ord('S')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(ord(' ')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_UNMUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(ord('U')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_TOGGLE_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(ord('T')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_GET_VOLUME = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(ord('G')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

AV_APP_TO_DEV_GET_MUTE = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(ord('G')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 125

enum_AVDevToAppMessageType = c_int# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_NONE = (((ord('E') | (ord('N') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(ord('N')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_CREATE_WINDOW_BUFFER = (((ord('E') | (ord('R') << 8)) | (ord('C') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_PREPARE_WINDOW_BUFFER = (((ord('E') | (ord('R') << 8)) | (ord('P') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_DISPLAY_WINDOW_BUFFER = (((ord('S') | (ord('I') << 8)) | (ord('D') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_DESTROY_WINDOW_BUFFER = (((ord('S') | (ord('E') << 8)) | (ord('D') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_BUFFER_OVERFLOW = (((ord('L') | (ord('F') << 8)) | (ord('O') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_BUFFER_UNDERFLOW = (((ord('L') | (ord('F') << 8)) | (ord('U') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_BUFFER_READABLE = (((ord(' ') | (ord('D') << 8)) | (ord('R') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_BUFFER_WRITABLE = (((ord(' ') | (ord('R') << 8)) | (ord('W') << 16)) | ((c_uint (ord_if_char(ord('B')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_MUTE_STATE_CHANGED = (((ord('T') | (ord('U') << 8)) | (ord('M') << 16)) | ((c_uint (ord_if_char(ord('C')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

AV_DEV_TO_APP_VOLUME_LEVEL_CHANGED = (((ord('L') | (ord('O') << 8)) | (ord('V') << 16)) | ((c_uint (ord_if_char(ord('C')))).value << 24))# /home/josiah/ctypesgen_test/av/av/avdevice.h: 204

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 312
if _libs["avdevice"].has("avdevice_app_to_dev_control_message", "cdecl"):
    avdevice_app_to_dev_control_message = _libs["avdevice"].get("avdevice_app_to_dev_control_message", "cdecl")
    avdevice_app_to_dev_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVAppToDevMessageType, POINTER(None), c_size_t]
    avdevice_app_to_dev_control_message.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 326
if _libs["avdevice"].has("avdevice_dev_to_app_control_message", "cdecl"):
    avdevice_dev_to_app_control_message = _libs["avdevice"].get("avdevice_dev_to_app_control_message", "cdecl")
    avdevice_dev_to_app_control_message.argtypes = [POINTER(struct_AVFormatContext), enum_AVDevToAppMessageType, POINTER(None), c_size_t]
    avdevice_dev_to_app_control_message.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 338
class struct_AVDeviceInfo(Structure):
    pass

struct_AVDeviceInfo.__slots__ = [
    'device_name',
    'device_description',
    'media_types',
    'nb_media_types',
]
struct_AVDeviceInfo._fields_ = [
    ('device_name', String),
    ('device_description', String),
    ('media_types', POINTER(enum_AVMediaType)),
    ('nb_media_types', c_int),
]

AVDeviceInfo = struct_AVDeviceInfo# /home/josiah/ctypesgen_test/av/av/avdevice.h: 338

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

AVDeviceInfoList = struct_AVDeviceInfoList# /home/josiah/ctypesgen_test/av/av/avdevice.h: 347

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 362
if _libs["avdevice"].has("avdevice_list_devices", "cdecl"):
    avdevice_list_devices = _libs["avdevice"].get("avdevice_list_devices", "cdecl")
    avdevice_list_devices.argtypes = [POINTER(struct_AVFormatContext), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_devices.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 369
if _libs["avdevice"].has("avdevice_free_list_devices", "cdecl"):
    avdevice_free_list_devices = _libs["avdevice"].get("avdevice_free_list_devices", "cdecl")
    avdevice_free_list_devices.argtypes = [POINTER(POINTER(AVDeviceInfoList))]
    avdevice_free_list_devices.restype = None

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 388
if _libs["avdevice"].has("avdevice_list_input_sources", "cdecl"):
    avdevice_list_input_sources = _libs["avdevice"].get("avdevice_list_input_sources", "cdecl")
    avdevice_list_input_sources.argtypes = [POINTER(AVInputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_input_sources.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avdevice.h: 390
if _libs["avdevice"].has("avdevice_list_output_sinks", "cdecl"):
    avdevice_list_output_sinks = _libs["avdevice"].get("avdevice_list_output_sinks", "cdecl")
    avdevice_list_output_sinks.argtypes = [POINTER(AVOutputFormat), String, POINTER(AVDictionary), POINTER(POINTER(AVDeviceInfoList))]
    avdevice_list_output_sinks.restype = c_int

FFTSample = c_float# /home/josiah/ctypesgen_test/av/av/avfft.h: 35

# /home/josiah/ctypesgen_test/av/av/avfft.h: 39
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

FFTComplex = struct_FFTComplex# /home/josiah/ctypesgen_test/av/av/avfft.h: 39

# /home/josiah/ctypesgen_test/av/av/avfft.h: 41
class struct_FFTContext(Structure):
    pass

FFTContext = struct_FFTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 41

# /home/josiah/ctypesgen_test/av/av/avfft.h: 48
if _libs["avcodec"].has("av_fft_init", "cdecl"):
    av_fft_init = _libs["avcodec"].get("av_fft_init", "cdecl")
    av_fft_init.argtypes = [c_int, c_int]
    av_fft_init.restype = POINTER(FFTContext)

# /home/josiah/ctypesgen_test/av/av/avfft.h: 53
if _libs["avcodec"].has("av_fft_permute", "cdecl"):
    av_fft_permute = _libs["avcodec"].get("av_fft_permute", "cdecl")
    av_fft_permute.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_permute.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 59
if _libs["avcodec"].has("av_fft_calc", "cdecl"):
    av_fft_calc = _libs["avcodec"].get("av_fft_calc", "cdecl")
    av_fft_calc.argtypes = [POINTER(FFTContext), POINTER(FFTComplex)]
    av_fft_calc.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 61
if _libs["avcodec"].has("av_fft_end", "cdecl"):
    av_fft_end = _libs["avcodec"].get("av_fft_end", "cdecl")
    av_fft_end.argtypes = [POINTER(FFTContext)]
    av_fft_end.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 63
for _lib in _libs.values():
    if not _lib.has("av_mdct_init", "cdecl"):
        continue
    av_mdct_init = _lib.get("av_mdct_init", "cdecl")
    av_mdct_init.argtypes = [c_int, c_int, c_double]
    av_mdct_init.restype = POINTER(FFTContext)
    break

# /home/josiah/ctypesgen_test/av/av/avfft.h: 64
for _lib in _libs.values():
    if not _lib.has("av_imdct_calc", "cdecl"):
        continue
    av_imdct_calc = _lib.get("av_imdct_calc", "cdecl")
    av_imdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_calc.restype = None
    break

# /home/josiah/ctypesgen_test/av/av/avfft.h: 65
for _lib in _libs.values():
    if not _lib.has("av_imdct_half", "cdecl"):
        continue
    av_imdct_half = _lib.get("av_imdct_half", "cdecl")
    av_imdct_half.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_imdct_half.restype = None
    break

# /home/josiah/ctypesgen_test/av/av/avfft.h: 66
for _lib in _libs.values():
    if not _lib.has("av_mdct_calc", "cdecl"):
        continue
    av_mdct_calc = _lib.get("av_mdct_calc", "cdecl")
    av_mdct_calc.argtypes = [POINTER(FFTContext), POINTER(FFTSample), POINTER(FFTSample)]
    av_mdct_calc.restype = None
    break

# /home/josiah/ctypesgen_test/av/av/avfft.h: 67
for _lib in _libs.values():
    if not _lib.has("av_mdct_end", "cdecl"):
        continue
    av_mdct_end = _lib.get("av_mdct_end", "cdecl")
    av_mdct_end.argtypes = [POINTER(FFTContext)]
    av_mdct_end.restype = None
    break

enum_RDFTransformType = c_int# /home/josiah/ctypesgen_test/av/av/avfft.h: 71

DFT_R2C = 0# /home/josiah/ctypesgen_test/av/av/avfft.h: 71

IDFT_C2R = (DFT_R2C + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 71

IDFT_R2C = (IDFT_C2R + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 71

DFT_C2R = (IDFT_R2C + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 71

# /home/josiah/ctypesgen_test/av/av/avfft.h: 78
class struct_RDFTContext(Structure):
    pass

RDFTContext = struct_RDFTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 78

# /home/josiah/ctypesgen_test/av/av/avfft.h: 85
if _libs["avcodec"].has("av_rdft_init", "cdecl"):
    av_rdft_init = _libs["avcodec"].get("av_rdft_init", "cdecl")
    av_rdft_init.argtypes = [c_int, enum_RDFTransformType]
    av_rdft_init.restype = POINTER(RDFTContext)

# /home/josiah/ctypesgen_test/av/av/avfft.h: 86
if _libs["avcodec"].has("av_rdft_calc", "cdecl"):
    av_rdft_calc = _libs["avcodec"].get("av_rdft_calc", "cdecl")
    av_rdft_calc.argtypes = [POINTER(RDFTContext), POINTER(FFTSample)]
    av_rdft_calc.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 87
if _libs["avcodec"].has("av_rdft_end", "cdecl"):
    av_rdft_end = _libs["avcodec"].get("av_rdft_end", "cdecl")
    av_rdft_end.argtypes = [POINTER(RDFTContext)]
    av_rdft_end.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 91
class struct_DCTContext(Structure):
    pass

DCTContext = struct_DCTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 91

enum_DCTTransformType = c_int# /home/josiah/ctypesgen_test/av/av/avfft.h: 93

DCT_II = 0# /home/josiah/ctypesgen_test/av/av/avfft.h: 93

DCT_III = (DCT_II + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 93

DCT_I = (DCT_III + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 93

DST_I = (DCT_I + 1)# /home/josiah/ctypesgen_test/av/av/avfft.h: 93

# /home/josiah/ctypesgen_test/av/av/avfft.h: 110
if _libs["avcodec"].has("av_dct_init", "cdecl"):
    av_dct_init = _libs["avcodec"].get("av_dct_init", "cdecl")
    av_dct_init.argtypes = [c_int, enum_DCTTransformType]
    av_dct_init.restype = POINTER(DCTContext)

# /home/josiah/ctypesgen_test/av/av/avfft.h: 111
if _libs["avcodec"].has("av_dct_calc", "cdecl"):
    av_dct_calc = _libs["avcodec"].get("av_dct_calc", "cdecl")
    av_dct_calc.argtypes = [POINTER(DCTContext), POINTER(FFTSample)]
    av_dct_calc.restype = None

# /home/josiah/ctypesgen_test/av/av/avfft.h: 112
if _libs["avcodec"].has("av_dct_end", "cdecl"):
    av_dct_end = _libs["avcodec"].get("av_dct_end", "cdecl")
    av_dct_end.argtypes = [POINTER(DCTContext)]
    av_dct_end.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 61
if _libs["avdevice"].has("avfilter_version", "cdecl"):
    avfilter_version = _libs["avdevice"].get("avfilter_version", "cdecl")
    avfilter_version.argtypes = []
    avfilter_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 66
if _libs["avdevice"].has("avfilter_configuration", "cdecl"):
    avfilter_configuration = _libs["avdevice"].get("avfilter_configuration", "cdecl")
    avfilter_configuration.argtypes = []
    avfilter_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 71
if _libs["avdevice"].has("avfilter_license", "cdecl"):
    avfilter_license = _libs["avdevice"].get("avfilter_license", "cdecl")
    avfilter_license.argtypes = []
    avfilter_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 392
class struct_AVFilterContext(Structure):
    pass

AVFilterContext = struct_AVFilterContext# /home/josiah/ctypesgen_test/av/av/avfilter.h: 73

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 522
class struct_AVFilterLink(Structure):
    pass

AVFilterLink = struct_AVFilterLink# /home/josiah/ctypesgen_test/av/av/avfilter.h: 74

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 75
class struct_AVFilterPad(Structure):
    pass

AVFilterPad = struct_AVFilterPad# /home/josiah/ctypesgen_test/av/av/avfilter.h: 75

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 76
class struct_AVFilterFormats(Structure):
    pass

AVFilterFormats = struct_AVFilterFormats# /home/josiah/ctypesgen_test/av/av/avfilter.h: 76

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 77
class struct_AVFilterChannelLayouts(Structure):
    pass

AVFilterChannelLayouts = struct_AVFilterChannelLayouts# /home/josiah/ctypesgen_test/av/av/avfilter.h: 77

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 88
if _libs["avdevice"].has("avfilter_pad_get_name", "cdecl"):
    avfilter_pad_get_name = _libs["avdevice"].get("avfilter_pad_get_name", "cdecl")
    avfilter_pad_get_name.argtypes = [POINTER(AVFilterPad), c_int]
    avfilter_pad_get_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 99
if _libs["avdevice"].has("avfilter_pad_get_type", "cdecl"):
    avfilter_pad_get_type = _libs["avdevice"].get("avfilter_pad_get_type", "cdecl")
    avfilter_pad_get_type.argtypes = [POINTER(AVFilterPad), c_int]
    avfilter_pad_get_type.restype = enum_AVMediaType

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 285
class union_anon_30(Union):
    pass

union_anon_30.__slots__ = [
    'query_func',
    'pixels_list',
    'samples_list',
    'pix_fmt',
    'sample_fmt',
]
union_anon_30._fields_ = [
    ('query_func', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('pixels_list', POINTER(enum_AVPixelFormat)),
    ('samples_list', POINTER(enum_AVSampleFormat)),
    ('pix_fmt', enum_AVPixelFormat),
    ('sample_fmt', enum_AVSampleFormat),
]

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 377
class struct_AVFilter(Structure):
    pass

struct_AVFilter.__slots__ = [
    'name',
    'description',
    'inputs',
    'outputs',
    'priv_class',
    'flags',
    'nb_inputs',
    'nb_outputs',
    'formats_state',
    'preinit',
    'init',
    'uninit',
    'formats',
    'priv_size',
    'flags_internal',
    'process_command',
    'activate',
]
struct_AVFilter._fields_ = [
    ('name', String),
    ('description', String),
    ('inputs', POINTER(AVFilterPad)),
    ('outputs', POINTER(AVFilterPad)),
    ('priv_class', POINTER(AVClass)),
    ('flags', c_int),
    ('nb_inputs', uint8_t),
    ('nb_outputs', uint8_t),
    ('formats_state', uint8_t),
    ('preinit', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
    ('uninit', CFUNCTYPE(UNCHECKED(None), POINTER(AVFilterContext))),
    ('formats', union_anon_30),
    ('priv_size', c_int),
    ('flags_internal', c_int),
    ('process_command', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), String, String, String, c_int, c_int)),
    ('activate', CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext))),
]

AVFilter = struct_AVFilter# /home/josiah/ctypesgen_test/av/av/avfilter.h: 377

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 382
if _libs["avdevice"].has("avfilter_filter_pad_count", "cdecl"):
    avfilter_filter_pad_count = _libs["avdevice"].get("avfilter_filter_pad_count", "cdecl")
    avfilter_filter_pad_count.argtypes = [POINTER(AVFilter), c_int]
    avfilter_filter_pad_count.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 389
class struct_AVFilterInternal(Structure):
    pass

AVFilterInternal = struct_AVFilterInternal# /home/josiah/ctypesgen_test/av/av/avfilter.h: 389

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 855
class struct_AVFilterGraph(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 434
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

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 508
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

AVFilterFormatsConfig = struct_AVFilterFormatsConfig# /home/josiah/ctypesgen_test/av/av/avfilter.h: 508

enum_anon_31 = c_int# /home/josiah/ctypesgen_test/av/av/avfilter.h: 578

AVLINK_UNINIT = 0# /home/josiah/ctypesgen_test/av/av/avfilter.h: 578

AVLINK_STARTINIT = (AVLINK_UNINIT + 1)# /home/josiah/ctypesgen_test/av/av/avfilter.h: 578

AVLINK_INIT = (AVLINK_STARTINIT + 1)# /home/josiah/ctypesgen_test/av/av/avfilter.h: 578

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
    'ch_layout',
    'incfg',
    'outcfg',
    'init_state',
    'graph',
    'current_pts',
    'current_pts_us',
    'age_index',
    'frame_rate',
    'min_samples',
    'max_samples',
    'frame_count_in',
    'frame_count_out',
    'sample_count_in',
    'sample_count_out',
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
    ('channel_layout', uint64_t),
    ('sample_rate', c_int),
    ('format', c_int),
    ('time_base', AVRational),
    ('ch_layout', AVChannelLayout),
    ('incfg', AVFilterFormatsConfig),
    ('outcfg', AVFilterFormatsConfig),
    ('init_state', enum_anon_31),
    ('graph', POINTER(struct_AVFilterGraph)),
    ('current_pts', c_int64),
    ('current_pts_us', c_int64),
    ('age_index', c_int),
    ('frame_rate', AVRational),
    ('min_samples', c_int),
    ('max_samples', c_int),
    ('frame_count_in', c_int64),
    ('frame_count_out', c_int64),
    ('sample_count_in', c_int64),
    ('sample_count_out', c_int64),
    ('frame_pool', POINTER(None)),
    ('frame_wanted_out', c_int),
    ('hw_frames_ctx', POINTER(AVBufferRef)),
    ('reserved', c_char * int(0xF000)),
]

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 717
if _libs["avdevice"].has("avfilter_link", "cdecl"):
    avfilter_link = _libs["avdevice"].get("avfilter_link", "cdecl")
    avfilter_link.argtypes = [POINTER(AVFilterContext), c_uint, POINTER(AVFilterContext), c_uint]
    avfilter_link.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 723
if _libs["avdevice"].has("avfilter_link_free", "cdecl"):
    avfilter_link_free = _libs["avdevice"].get("avfilter_link_free", "cdecl")
    avfilter_link_free.argtypes = [POINTER(POINTER(AVFilterLink))]
    avfilter_link_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 731
if _libs["avdevice"].has("avfilter_config_links", "cdecl"):
    avfilter_config_links = _libs["avdevice"].get("avfilter_config_links", "cdecl")
    avfilter_config_links.argtypes = [POINTER(AVFilterContext)]
    avfilter_config_links.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 740
if _libs["avdevice"].has("avfilter_process_command", "cdecl"):
    avfilter_process_command = _libs["avdevice"].get("avfilter_process_command", "cdecl")
    avfilter_process_command.argtypes = [POINTER(AVFilterContext), String, String, String, c_int, c_int]
    avfilter_process_command.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 751
if _libs["avdevice"].has("av_filter_iterate", "cdecl"):
    av_filter_iterate = _libs["avdevice"].get("av_filter_iterate", "cdecl")
    av_filter_iterate.argtypes = [POINTER(POINTER(None))]
    av_filter_iterate.restype = POINTER(AVFilter)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 760
if _libs["avdevice"].has("avfilter_get_by_name", "cdecl"):
    avfilter_get_by_name = _libs["avdevice"].get("avfilter_get_by_name", "cdecl")
    avfilter_get_by_name.argtypes = [String]
    avfilter_get_by_name.restype = POINTER(AVFilter)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 773
if _libs["avdevice"].has("avfilter_init_str", "cdecl"):
    avfilter_init_str = _libs["avdevice"].get("avfilter_init_str", "cdecl")
    avfilter_init_str.argtypes = [POINTER(AVFilterContext), String]
    avfilter_init_str.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 795
if _libs["avdevice"].has("avfilter_init_dict", "cdecl"):
    avfilter_init_dict = _libs["avdevice"].get("avfilter_init_dict", "cdecl")
    avfilter_init_dict.argtypes = [POINTER(AVFilterContext), POINTER(POINTER(AVDictionary))]
    avfilter_init_dict.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 803
if _libs["avdevice"].has("avfilter_free", "cdecl"):
    avfilter_free = _libs["avdevice"].get("avfilter_free", "cdecl")
    avfilter_free.argtypes = [POINTER(AVFilterContext)]
    avfilter_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 814
if _libs["avdevice"].has("avfilter_insert_filter", "cdecl"):
    avfilter_insert_filter = _libs["avdevice"].get("avfilter_insert_filter", "cdecl")
    avfilter_insert_filter.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterContext), c_uint, c_uint]
    avfilter_insert_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 822
if _libs["avdevice"].has("avfilter_get_class", "cdecl"):
    avfilter_get_class = _libs["avdevice"].get("avfilter_get_class", "cdecl")
    avfilter_get_class.argtypes = []
    avfilter_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 824
class struct_AVFilterGraphInternal(Structure):
    pass

AVFilterGraphInternal = struct_AVFilterGraphInternal# /home/josiah/ctypesgen_test/av/av/avfilter.h: 824

avfilter_action_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(None), c_int, c_int)# /home/josiah/ctypesgen_test/av/av/avfilter.h: 838

avfilter_execute_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(AVFilterContext), POINTER(avfilter_action_func), POINTER(None), POINTER(c_int), c_int)# /home/josiah/ctypesgen_test/av/av/avfilter.h: 852

struct_AVFilterGraph.__slots__ = [
    'av_class',
    'filters',
    'nb_filters',
    'scale_sws_opts',
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

AVFilterGraph = struct_AVFilterGraph# /home/josiah/ctypesgen_test/av/av/avfilter.h: 922

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 929
if _libs["avdevice"].has("avfilter_graph_alloc", "cdecl"):
    avfilter_graph_alloc = _libs["avdevice"].get("avfilter_graph_alloc", "cdecl")
    avfilter_graph_alloc.argtypes = []
    avfilter_graph_alloc.restype = POINTER(AVFilterGraph)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 945
if _libs["avdevice"].has("avfilter_graph_alloc_filter", "cdecl"):
    avfilter_graph_alloc_filter = _libs["avdevice"].get("avfilter_graph_alloc_filter", "cdecl")
    avfilter_graph_alloc_filter.argtypes = [POINTER(AVFilterGraph), POINTER(AVFilter), String]
    avfilter_graph_alloc_filter.restype = POINTER(AVFilterContext)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 957
if _libs["avdevice"].has("avfilter_graph_get_filter", "cdecl"):
    avfilter_graph_get_filter = _libs["avdevice"].get("avfilter_graph_get_filter", "cdecl")
    avfilter_graph_get_filter.argtypes = [POINTER(AVFilterGraph), String]
    avfilter_graph_get_filter.restype = POINTER(AVFilterContext)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 972
if _libs["avdevice"].has("avfilter_graph_create_filter", "cdecl"):
    avfilter_graph_create_filter = _libs["avdevice"].get("avfilter_graph_create_filter", "cdecl")
    avfilter_graph_create_filter.argtypes = [POINTER(POINTER(AVFilterContext)), POINTER(AVFilter), String, String, POINTER(None), POINTER(AVFilterGraph)]
    avfilter_graph_create_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 984
if _libs["avdevice"].has("avfilter_graph_set_auto_convert", "cdecl"):
    avfilter_graph_set_auto_convert = _libs["avdevice"].get("avfilter_graph_set_auto_convert", "cdecl")
    avfilter_graph_set_auto_convert.argtypes = [POINTER(AVFilterGraph), c_uint]
    avfilter_graph_set_auto_convert.restype = None

enum_anon_32 = c_int# /home/josiah/ctypesgen_test/av/av/avfilter.h: 986

AVFILTER_AUTO_CONVERT_ALL = 0# /home/josiah/ctypesgen_test/av/av/avfilter.h: 986

AVFILTER_AUTO_CONVERT_NONE = (-1)# /home/josiah/ctypesgen_test/av/av/avfilter.h: 986

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 998
if _libs["avdevice"].has("avfilter_graph_config", "cdecl"):
    avfilter_graph_config = _libs["avdevice"].get("avfilter_graph_config", "cdecl")
    avfilter_graph_config.argtypes = [POINTER(AVFilterGraph), POINTER(None)]
    avfilter_graph_config.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1004
if _libs["avdevice"].has("avfilter_graph_free", "cdecl"):
    avfilter_graph_free = _libs["avdevice"].get("avfilter_graph_free", "cdecl")
    avfilter_graph_free.argtypes = [POINTER(POINTER(AVFilterGraph))]
    avfilter_graph_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1015
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

AVFilterInOut = struct_AVFilterInOut# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1027

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1034
if _libs["avdevice"].has("avfilter_inout_alloc", "cdecl"):
    avfilter_inout_alloc = _libs["avdevice"].get("avfilter_inout_alloc", "cdecl")
    avfilter_inout_alloc.argtypes = []
    avfilter_inout_alloc.restype = POINTER(AVFilterInOut)

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1040
if _libs["avdevice"].has("avfilter_inout_free", "cdecl"):
    avfilter_inout_free = _libs["avdevice"].get("avfilter_inout_free", "cdecl")
    avfilter_inout_free.argtypes = [POINTER(POINTER(AVFilterInOut))]
    avfilter_inout_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1060
if _libs["avdevice"].has("avfilter_graph_parse", "cdecl"):
    avfilter_graph_parse = _libs["avdevice"].get("avfilter_graph_parse", "cdecl")
    avfilter_graph_parse.argtypes = [POINTER(AVFilterGraph), String, POINTER(AVFilterInOut), POINTER(AVFilterInOut), POINTER(None)]
    avfilter_graph_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1081
if _libs["avdevice"].has("avfilter_graph_parse_ptr", "cdecl"):
    avfilter_graph_parse_ptr = _libs["avdevice"].get("avfilter_graph_parse_ptr", "cdecl")
    avfilter_graph_parse_ptr.argtypes = [POINTER(AVFilterGraph), String, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut)), POINTER(None)]
    avfilter_graph_parse_ptr.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1107
if _libs["avdevice"].has("avfilter_graph_parse2", "cdecl"):
    avfilter_graph_parse2 = _libs["avdevice"].get("avfilter_graph_parse2", "cdecl")
    avfilter_graph_parse2.argtypes = [POINTER(AVFilterGraph), String, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut))]
    avfilter_graph_parse2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1126
class struct_AVFilterPadParams(Structure):
    pass

struct_AVFilterPadParams.__slots__ = [
    'label',
]
struct_AVFilterPadParams._fields_ = [
    ('label', String),
]

AVFilterPadParams = struct_AVFilterPadParams# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1126

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1193
class struct_AVFilterParams(Structure):
    pass

struct_AVFilterParams.__slots__ = [
    'filter',
    'filter_name',
    'instance_name',
    'opts',
    'inputs',
    'nb_inputs',
    'outputs',
    'nb_outputs',
]
struct_AVFilterParams._fields_ = [
    ('filter', POINTER(AVFilterContext)),
    ('filter_name', String),
    ('instance_name', String),
    ('opts', POINTER(AVDictionary)),
    ('inputs', POINTER(POINTER(AVFilterPadParams))),
    ('nb_inputs', c_uint),
    ('outputs', POINTER(POINTER(AVFilterPadParams))),
    ('nb_outputs', c_uint),
]

AVFilterParams = struct_AVFilterParams# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1193

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1204
class struct_AVFilterChain(Structure):
    pass

struct_AVFilterChain.__slots__ = [
    'filters',
    'nb_filters',
]
struct_AVFilterChain._fields_ = [
    ('filters', POINTER(POINTER(AVFilterParams))),
    ('nb_filters', c_size_t),
]

AVFilterChain = struct_AVFilterChain# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1204

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1238
class struct_AVFilterGraphSegment(Structure):
    pass

struct_AVFilterGraphSegment.__slots__ = [
    'graph',
    'chains',
    'nb_chains',
    'scale_sws_opts',
]
struct_AVFilterGraphSegment._fields_ = [
    ('graph', POINTER(AVFilterGraph)),
    ('chains', POINTER(POINTER(AVFilterChain))),
    ('nb_chains', c_size_t),
    ('scale_sws_opts', String),
]

AVFilterGraphSegment = struct_AVFilterGraphSegment# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1238

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1264
if _libs["avdevice"].has("avfilter_graph_segment_parse", "cdecl"):
    avfilter_graph_segment_parse = _libs["avdevice"].get("avfilter_graph_segment_parse", "cdecl")
    avfilter_graph_segment_parse.argtypes = [POINTER(AVFilterGraph), String, c_int, POINTER(POINTER(AVFilterGraphSegment))]
    avfilter_graph_segment_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1292
if _libs["avdevice"].has("avfilter_graph_segment_create_filters", "cdecl"):
    avfilter_graph_segment_create_filters = _libs["avdevice"].get("avfilter_graph_segment_create_filters", "cdecl")
    avfilter_graph_segment_create_filters.argtypes = [POINTER(AVFilterGraphSegment), c_int]
    avfilter_graph_segment_create_filters.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1321
if _libs["avdevice"].has("avfilter_graph_segment_apply_opts", "cdecl"):
    avfilter_graph_segment_apply_opts = _libs["avdevice"].get("avfilter_graph_segment_apply_opts", "cdecl")
    avfilter_graph_segment_apply_opts.argtypes = [POINTER(AVFilterGraphSegment), c_int]
    avfilter_graph_segment_apply_opts.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1343
if _libs["avdevice"].has("avfilter_graph_segment_init", "cdecl"):
    avfilter_graph_segment_init = _libs["avdevice"].get("avfilter_graph_segment_init", "cdecl")
    avfilter_graph_segment_init.argtypes = [POINTER(AVFilterGraphSegment), c_int]
    avfilter_graph_segment_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1378
if _libs["avdevice"].has("avfilter_graph_segment_link", "cdecl"):
    avfilter_graph_segment_link = _libs["avdevice"].get("avfilter_graph_segment_link", "cdecl")
    avfilter_graph_segment_link.argtypes = [POINTER(AVFilterGraphSegment), c_int, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut))]
    avfilter_graph_segment_link.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1406
if _libs["avdevice"].has("avfilter_graph_segment_apply", "cdecl"):
    avfilter_graph_segment_apply = _libs["avdevice"].get("avfilter_graph_segment_apply", "cdecl")
    avfilter_graph_segment_apply.argtypes = [POINTER(AVFilterGraphSegment), c_int, POINTER(POINTER(AVFilterInOut)), POINTER(POINTER(AVFilterInOut))]
    avfilter_graph_segment_apply.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1420
if _libs["avdevice"].has("avfilter_graph_segment_free", "cdecl"):
    avfilter_graph_segment_free = _libs["avdevice"].get("avfilter_graph_segment_free", "cdecl")
    avfilter_graph_segment_free.argtypes = [POINTER(POINTER(AVFilterGraphSegment))]
    avfilter_graph_segment_free.restype = None

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1437
if _libs["avdevice"].has("avfilter_graph_send_command", "cdecl"):
    avfilter_graph_send_command = _libs["avdevice"].get("avfilter_graph_send_command", "cdecl")
    avfilter_graph_send_command.argtypes = [POINTER(AVFilterGraph), String, String, String, String, c_int, c_int]
    avfilter_graph_send_command.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1454
if _libs["avdevice"].has("avfilter_graph_queue_command", "cdecl"):
    avfilter_graph_queue_command = _libs["avdevice"].get("avfilter_graph_queue_command", "cdecl")
    avfilter_graph_queue_command.argtypes = [POINTER(AVFilterGraph), String, String, String, c_int, c_double]
    avfilter_graph_queue_command.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1465
if _libs["avdevice"].has("avfilter_graph_dump", "cdecl"):
    avfilter_graph_dump = _libs["avdevice"].get("avfilter_graph_dump", "cdecl")
    avfilter_graph_dump.argtypes = [POINTER(AVFilterGraph), String]
    if sizeof(c_int) == sizeof(c_void_p):
        avfilter_graph_dump.restype = ReturnString
    else:
        avfilter_graph_dump.restype = String
        avfilter_graph_dump.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1485
if _libs["avdevice"].has("avfilter_graph_request_oldest", "cdecl"):
    avfilter_graph_request_oldest = _libs["avdevice"].get("avfilter_graph_request_oldest", "cdecl")
    avfilter_graph_request_oldest.argtypes = [POINTER(AVFilterGraph)]
    avfilter_graph_request_oldest.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 43
if _libs["avcodec"].has("av_strstart", "cdecl"):
    av_strstart = _libs["avcodec"].get("av_strstart", "cdecl")
    av_strstart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_strstart.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 55
if _libs["avcodec"].has("av_stristart", "cdecl"):
    av_stristart = _libs["avcodec"].get("av_stristart", "cdecl")
    av_stristart.argtypes = [String, String, POINTER(POINTER(c_char))]
    av_stristart.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 69
if _libs["avcodec"].has("av_stristr", "cdecl"):
    av_stristr = _libs["avcodec"].get("av_stristr", "cdecl")
    av_stristr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_stristr.restype = ReturnString
    else:
        av_stristr.restype = String
        av_stristr.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avstring.h: 84
if _libs["avcodec"].has("av_strnstr", "cdecl"):
    av_strnstr = _libs["avcodec"].get("av_strnstr", "cdecl")
    av_strnstr.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strnstr.restype = ReturnString
    else:
        av_strnstr.restype = String
        av_strnstr.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avstring.h: 101
if _libs["avcodec"].has("av_strlcpy", "cdecl"):
    av_strlcpy = _libs["avcodec"].get("av_strlcpy", "cdecl")
    av_strlcpy.argtypes = [String, String, c_size_t]
    av_strlcpy.restype = c_size_t

# /home/josiah/ctypesgen_test/av/av/avstring.h: 119
if _libs["avcodec"].has("av_strlcat", "cdecl"):
    av_strlcat = _libs["avcodec"].get("av_strlcat", "cdecl")
    av_strlcat.argtypes = [String, String, c_size_t]
    av_strlcat.restype = c_size_t

# /home/josiah/ctypesgen_test/av/av/avstring.h: 133
if _libs["avcodec"].has("av_strlcatf", "cdecl"):
    _func = _libs["avcodec"].get("av_strlcatf", "cdecl")
    _restype = c_size_t
    _errcheck = None
    _argtypes = [String, c_size_t, String]
    av_strlcatf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/avstring.h: 144
for _lib in _libs.values():
    try:
        i = (c_size_t).in_dll(_lib, "i")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 158
if _libs["avcodec"].has("av_asprintf", "cdecl"):
    _func = _libs["avcodec"].get("av_asprintf", "cdecl")
    _restype = String
    _errcheck = None
    _argtypes = [String]
    av_asprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/avstring.h: 174
if _libs["avcodec"].has("av_get_token", "cdecl"):
    av_get_token = _libs["avcodec"].get("av_get_token", "cdecl")
    av_get_token.argtypes = [POINTER(POINTER(c_char)), String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_token.restype = ReturnString
    else:
        av_get_token.restype = String
        av_get_token.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avstring.h: 198
if _libs["avcodec"].has("av_strtok", "cdecl"):
    av_strtok = _libs["avcodec"].get("av_strtok", "cdecl")
    av_strtok.argtypes = [String, String, POINTER(POINTER(c_char))]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strtok.restype = ReturnString
    else:
        av_strtok.restype = String
        av_strtok.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avstring.h: 258
if _libs["avcodec"].has("av_strcasecmp", "cdecl"):
    av_strcasecmp = _libs["avcodec"].get("av_strcasecmp", "cdecl")
    av_strcasecmp.argtypes = [String, String]
    av_strcasecmp.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 264
if _libs["avcodec"].has("av_strncasecmp", "cdecl"):
    av_strncasecmp = _libs["avcodec"].get("av_strncasecmp", "cdecl")
    av_strncasecmp.argtypes = [String, String, c_size_t]
    av_strncasecmp.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 270
if _libs["avcodec"].has("av_strireplace", "cdecl"):
    av_strireplace = _libs["avcodec"].get("av_strireplace", "cdecl")
    av_strireplace.argtypes = [String, String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_strireplace.restype = ReturnString
    else:
        av_strireplace.restype = String
        av_strireplace.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/avstring.h: 280
if _libs["avcodec"].has("av_basename", "cdecl"):
    av_basename = _libs["avcodec"].get("av_basename", "cdecl")
    av_basename.argtypes = [String]
    av_basename.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avstring.h: 290
if _libs["avcodec"].has("av_dirname", "cdecl"):
    av_dirname = _libs["avcodec"].get("av_dirname", "cdecl")
    av_dirname.argtypes = [String]
    av_dirname.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/avstring.h: 303
if _libs["avcodec"].has("av_match_name", "cdecl"):
    av_match_name = _libs["avcodec"].get("av_match_name", "cdecl")
    av_match_name.argtypes = [String, String]
    av_match_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 313
if _libs["avcodec"].has("av_append_path_component", "cdecl"):
    av_append_path_component = _libs["avcodec"].get("av_append_path_component", "cdecl")
    av_append_path_component.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        av_append_path_component.restype = ReturnString
    else:
        av_append_path_component.restype = String
        av_append_path_component.errcheck = ReturnString

enum_AVEscapeMode = c_int# /home/josiah/ctypesgen_test/av/av/avstring.h: 315

AV_ESCAPE_MODE_AUTO = 0# /home/josiah/ctypesgen_test/av/av/avstring.h: 315

AV_ESCAPE_MODE_BACKSLASH = (AV_ESCAPE_MODE_AUTO + 1)# /home/josiah/ctypesgen_test/av/av/avstring.h: 315

AV_ESCAPE_MODE_QUOTE = (AV_ESCAPE_MODE_BACKSLASH + 1)# /home/josiah/ctypesgen_test/av/av/avstring.h: 315

AV_ESCAPE_MODE_XML = (AV_ESCAPE_MODE_QUOTE + 1)# /home/josiah/ctypesgen_test/av/av/avstring.h: 315

# /home/josiah/ctypesgen_test/av/av/avstring.h: 369
if _libs["avcodec"].has("av_escape", "cdecl"):
    av_escape = _libs["avcodec"].get("av_escape", "cdecl")
    av_escape.argtypes = [POINTER(POINTER(c_char)), String, String, enum_AVEscapeMode, c_int]
    av_escape.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 409
if _libs["avcodec"].has("av_utf8_decode", "cdecl"):
    av_utf8_decode = _libs["avcodec"].get("av_utf8_decode", "cdecl")
    av_utf8_decode.argtypes = [POINTER(c_int32), POINTER(POINTER(uint8_t)), POINTER(uint8_t), c_uint]
    av_utf8_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 417
if _libs["avcodec"].has("av_match_list", "cdecl"):
    av_match_list = _libs["avcodec"].get("av_match_list", "cdecl")
    av_match_list.argtypes = [String, String, c_char]
    av_match_list.restype = c_int

# /home/josiah/ctypesgen_test/av/av/avstring.h: 423
if _libs["avcodec"].has("av_sscanf", "cdecl"):
    _func = _libs["avcodec"].get("av_sscanf", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, String]
    av_sscanf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/base64.h: 42
if _libs["avcodec"].has("av_base64_decode", "cdecl"):
    av_base64_decode = _libs["avcodec"].get("av_base64_decode", "cdecl")
    av_base64_decode.argtypes = [POINTER(uint8_t), String, c_int]
    av_base64_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/av/base64.h: 60
if _libs["avcodec"].has("av_base64_encode", "cdecl"):
    av_base64_encode = _libs["avcodec"].get("av_base64_encode", "cdecl")
    av_base64_encode.argtypes = [String, c_int, POINTER(uint8_t), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_base64_encode.restype = ReturnString
    else:
        av_base64_encode.restype = String
        av_base64_encode.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 38
class struct_AVBlowfish(Structure):
    pass

struct_AVBlowfish.__slots__ = [
    'p',
    's',
]
struct_AVBlowfish._fields_ = [
    ('p', uint32_t * int((16 + 2))),
    ('s', (uint32_t * int(256)) * int(4)),
]

AVBlowfish = struct_AVBlowfish# /home/josiah/ctypesgen_test/av/av/blowfish.h: 38

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 43
if _libs["avcodec"].has("av_blowfish_alloc", "cdecl"):
    av_blowfish_alloc = _libs["avcodec"].get("av_blowfish_alloc", "cdecl")
    av_blowfish_alloc.argtypes = []
    av_blowfish_alloc.restype = POINTER(AVBlowfish)

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 52
if _libs["avcodec"].has("av_blowfish_init", "cdecl"):
    av_blowfish_init = _libs["avcodec"].get("av_blowfish_init", "cdecl")
    av_blowfish_init.argtypes = [POINTER(struct_AVBlowfish), POINTER(uint8_t), c_int]
    av_blowfish_init.restype = None

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 62
if _libs["avcodec"].has("av_blowfish_crypt_ecb", "cdecl"):
    av_blowfish_crypt_ecb = _libs["avcodec"].get("av_blowfish_crypt_ecb", "cdecl")
    av_blowfish_crypt_ecb.argtypes = [POINTER(struct_AVBlowfish), POINTER(uint32_t), POINTER(uint32_t), c_int]
    av_blowfish_crypt_ecb.restype = None

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 75
if _libs["avcodec"].has("av_blowfish_crypt", "cdecl"):
    av_blowfish_crypt = _libs["avcodec"].get("av_blowfish_crypt", "cdecl")
    av_blowfish_crypt.argtypes = [POINTER(struct_AVBlowfish), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_blowfish_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 93
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

AVBPrint = struct_AVBPrint# /home/josiah/ctypesgen_test/av/av/bprint.h: 93

# /home/josiah/ctypesgen_test/av/av/bprint.h: 141
if _libs["avcodec"].has("av_bprint_init", "cdecl"):
    av_bprint_init = _libs["avcodec"].get("av_bprint_init", "cdecl")
    av_bprint_init.argtypes = [POINTER(AVBPrint), c_uint, c_uint]
    av_bprint_init.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 152
if _libs["avcodec"].has("av_bprint_init_for_buffer", "cdecl"):
    av_bprint_init_for_buffer = _libs["avcodec"].get("av_bprint_init_for_buffer", "cdecl")
    av_bprint_init_for_buffer.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_init_for_buffer.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 157
if _libs["avcodec"].has("av_bprintf", "cdecl"):
    _func = _libs["avcodec"].get("av_bprintf", "cdecl")
    _restype = None
    _errcheck = None
    _argtypes = [POINTER(AVBPrint), String]
    av_bprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/josiah/ctypesgen_test/av/av/bprint.h: 162
if _libs["avcodec"].has("av_vbprintf", "cdecl"):
    av_vbprintf = _libs["avcodec"].get("av_vbprintf", "cdecl")
    av_vbprintf.argtypes = [POINTER(AVBPrint), String, c_void_p]
    av_vbprintf.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 167
if _libs["avcodec"].has("av_bprint_chars", "cdecl"):
    av_bprint_chars = _libs["avcodec"].get("av_bprint_chars", "cdecl")
    av_bprint_chars.argtypes = [POINTER(AVBPrint), c_char, c_uint]
    av_bprint_chars.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 176
if _libs["avcodec"].has("av_bprint_append_data", "cdecl"):
    av_bprint_append_data = _libs["avcodec"].get("av_bprint_append_data", "cdecl")
    av_bprint_append_data.argtypes = [POINTER(AVBPrint), String, c_uint]
    av_bprint_append_data.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 190
if _libs["avcodec"].has("av_bprint_strftime", "cdecl"):
    av_bprint_strftime = _libs["avcodec"].get("av_bprint_strftime", "cdecl")
    av_bprint_strftime.argtypes = [POINTER(AVBPrint), String, POINTER(struct_tm)]
    av_bprint_strftime.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 201
if _libs["avcodec"].has("av_bprint_get_buffer", "cdecl"):
    av_bprint_get_buffer = _libs["avcodec"].get("av_bprint_get_buffer", "cdecl")
    av_bprint_get_buffer.argtypes = [POINTER(AVBPrint), c_uint, POINTER(POINTER(c_ubyte)), POINTER(c_uint)]
    av_bprint_get_buffer.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 207
if _libs["avcodec"].has("av_bprint_clear", "cdecl"):
    av_bprint_clear = _libs["avcodec"].get("av_bprint_clear", "cdecl")
    av_bprint_clear.argtypes = [POINTER(AVBPrint)]
    av_bprint_clear.restype = None

# /home/josiah/ctypesgen_test/av/av/bprint.h: 231
if _libs["avcodec"].has("av_bprint_finalize", "cdecl"):
    av_bprint_finalize = _libs["avcodec"].get("av_bprint_finalize", "cdecl")
    av_bprint_finalize.argtypes = [POINTER(AVBPrint), POINTER(POINTER(c_char))]
    av_bprint_finalize.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bprint.h: 246
if _libs["avcodec"].has("av_bprint_escape", "cdecl"):
    av_bprint_escape = _libs["avcodec"].get("av_bprint_escape", "cdecl")
    av_bprint_escape.argtypes = [POINTER(AVBPrint), String, String, enum_AVEscapeMode, c_int]
    av_bprint_escape.restype = None

# /home/josiah/ctypesgen_test/av/av/bsf.h: 111
class struct_AVBitStreamFilter(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/bsf.h: 109
class struct_AVBSFContext(Structure):
    pass

struct_AVBSFContext.__slots__ = [
    'av_class',
    'filter',
    'priv_data',
    'par_in',
    'par_out',
    'time_base_in',
    'time_base_out',
]
struct_AVBSFContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('filter', POINTER(struct_AVBitStreamFilter)),
    ('priv_data', POINTER(None)),
    ('par_in', POINTER(AVCodecParameters)),
    ('par_out', POINTER(AVCodecParameters)),
    ('time_base_in', AVRational),
    ('time_base_out', AVRational),
]

AVBSFContext = struct_AVBSFContext# /home/josiah/ctypesgen_test/av/av/bsf.h: 109

struct_AVBitStreamFilter.__slots__ = [
    'name',
    'codec_ids',
    'priv_class',
]
struct_AVBitStreamFilter._fields_ = [
    ('name', String),
    ('codec_ids', POINTER(enum_AVCodecID)),
    ('priv_class', POINTER(AVClass)),
]

AVBitStreamFilter = struct_AVBitStreamFilter# /home/josiah/ctypesgen_test/av/av/bsf.h: 131

# /home/josiah/ctypesgen_test/av/av/bsf.h: 137
if _libs["avcodec"].has("av_bsf_get_by_name", "cdecl"):
    av_bsf_get_by_name = _libs["avcodec"].get("av_bsf_get_by_name", "cdecl")
    av_bsf_get_by_name.argtypes = [String]
    av_bsf_get_by_name.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/av/bsf.h: 148
if _libs["avcodec"].has("av_bsf_iterate", "cdecl"):
    av_bsf_iterate = _libs["avcodec"].get("av_bsf_iterate", "cdecl")
    av_bsf_iterate.argtypes = [POINTER(POINTER(None))]
    av_bsf_iterate.restype = POINTER(AVBitStreamFilter)

# /home/josiah/ctypesgen_test/av/av/bsf.h: 162
if _libs["avcodec"].has("av_bsf_alloc", "cdecl"):
    av_bsf_alloc = _libs["avcodec"].get("av_bsf_alloc", "cdecl")
    av_bsf_alloc.argtypes = [POINTER(AVBitStreamFilter), POINTER(POINTER(AVBSFContext))]
    av_bsf_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 170
if _libs["avcodec"].has("av_bsf_init", "cdecl"):
    av_bsf_init = _libs["avcodec"].get("av_bsf_init", "cdecl")
    av_bsf_init.argtypes = [POINTER(AVBSFContext)]
    av_bsf_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 193
if _libs["avcodec"].has("av_bsf_send_packet", "cdecl"):
    av_bsf_send_packet = _libs["avcodec"].get("av_bsf_send_packet", "cdecl")
    av_bsf_send_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_send_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 222
if _libs["avcodec"].has("av_bsf_receive_packet", "cdecl"):
    av_bsf_receive_packet = _libs["avcodec"].get("av_bsf_receive_packet", "cdecl")
    av_bsf_receive_packet.argtypes = [POINTER(AVBSFContext), POINTER(AVPacket)]
    av_bsf_receive_packet.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 227
if _libs["avcodec"].has("av_bsf_flush", "cdecl"):
    av_bsf_flush = _libs["avcodec"].get("av_bsf_flush", "cdecl")
    av_bsf_flush.argtypes = [POINTER(AVBSFContext)]
    av_bsf_flush.restype = None

# /home/josiah/ctypesgen_test/av/av/bsf.h: 233
if _libs["avcodec"].has("av_bsf_free", "cdecl"):
    av_bsf_free = _libs["avcodec"].get("av_bsf_free", "cdecl")
    av_bsf_free.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_free.restype = None

# /home/josiah/ctypesgen_test/av/av/bsf.h: 241
if _libs["avcodec"].has("av_bsf_get_class", "cdecl"):
    av_bsf_get_class = _libs["avcodec"].get("av_bsf_get_class", "cdecl")
    av_bsf_get_class.argtypes = []
    av_bsf_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/bsf.h: 247
class struct_AVBSFList(Structure):
    pass

AVBSFList = struct_AVBSFList# /home/josiah/ctypesgen_test/av/av/bsf.h: 247

# /home/josiah/ctypesgen_test/av/av/bsf.h: 256
if _libs["avcodec"].has("av_bsf_list_alloc", "cdecl"):
    av_bsf_list_alloc = _libs["avcodec"].get("av_bsf_list_alloc", "cdecl")
    av_bsf_list_alloc.argtypes = []
    av_bsf_list_alloc.restype = POINTER(AVBSFList)

# /home/josiah/ctypesgen_test/av/av/bsf.h: 263
if _libs["avcodec"].has("av_bsf_list_free", "cdecl"):
    av_bsf_list_free = _libs["avcodec"].get("av_bsf_list_free", "cdecl")
    av_bsf_list_free.argtypes = [POINTER(POINTER(AVBSFList))]
    av_bsf_list_free.restype = None

# /home/josiah/ctypesgen_test/av/av/bsf.h: 273
if _libs["avcodec"].has("av_bsf_list_append", "cdecl"):
    av_bsf_list_append = _libs["avcodec"].get("av_bsf_list_append", "cdecl")
    av_bsf_list_append.argtypes = [POINTER(AVBSFList), POINTER(AVBSFContext)]
    av_bsf_list_append.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 285
if _libs["avcodec"].has("av_bsf_list_append2", "cdecl"):
    av_bsf_list_append2 = _libs["avcodec"].get("av_bsf_list_append2", "cdecl")
    av_bsf_list_append2.argtypes = [POINTER(AVBSFList), String, POINTER(POINTER(AVDictionary))]
    av_bsf_list_append2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 302
if _libs["avcodec"].has("av_bsf_list_finalize", "cdecl"):
    av_bsf_list_finalize = _libs["avcodec"].get("av_bsf_list_finalize", "cdecl")
    av_bsf_list_finalize.argtypes = [POINTER(POINTER(AVBSFList)), POINTER(POINTER(AVBSFContext))]
    av_bsf_list_finalize.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 317
if _libs["avcodec"].has("av_bsf_list_parse_str", "cdecl"):
    av_bsf_list_parse_str = _libs["avcodec"].get("av_bsf_list_parse_str", "cdecl")
    av_bsf_list_parse_str.argtypes = [String, POINTER(POINTER(AVBSFContext))]
    av_bsf_list_parse_str.restype = c_int

# /home/josiah/ctypesgen_test/av/av/bsf.h: 326
if _libs["avcodec"].has("av_bsf_get_null_filter", "cdecl"):
    av_bsf_get_null_filter = _libs["avcodec"].get("av_bsf_get_null_filter", "cdecl")
    av_bsf_get_null_filter.argtypes = [POINTER(POINTER(AVBSFContext))]
    av_bsf_get_null_filter.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 81
if _libs["avdevice"].has("av_buffersink_get_frame_flags", "cdecl"):
    av_buffersink_get_frame_flags = _libs["avdevice"].get("av_buffersink_get_frame_flags", "cdecl")
    av_buffersink_get_frame_flags.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersink_get_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 104
if _libs["avdevice"].has("av_buffersink_set_frame_size", "cdecl"):
    av_buffersink_set_frame_size = _libs["avdevice"].get("av_buffersink_set_frame_size", "cdecl")
    av_buffersink_set_frame_size.argtypes = [POINTER(AVFilterContext), c_uint]
    av_buffersink_set_frame_size.restype = None

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 112
if _libs["avdevice"].has("av_buffersink_get_type", "cdecl"):
    av_buffersink_get_type = _libs["avdevice"].get("av_buffersink_get_type", "cdecl")
    av_buffersink_get_type.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_type.restype = enum_AVMediaType

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 113
if _libs["avdevice"].has("av_buffersink_get_time_base", "cdecl"):
    av_buffersink_get_time_base = _libs["avdevice"].get("av_buffersink_get_time_base", "cdecl")
    av_buffersink_get_time_base.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_time_base.restype = AVRational

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 114
if _libs["avdevice"].has("av_buffersink_get_format", "cdecl"):
    av_buffersink_get_format = _libs["avdevice"].get("av_buffersink_get_format", "cdecl")
    av_buffersink_get_format.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_format.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 116
if _libs["avdevice"].has("av_buffersink_get_frame_rate", "cdecl"):
    av_buffersink_get_frame_rate = _libs["avdevice"].get("av_buffersink_get_frame_rate", "cdecl")
    av_buffersink_get_frame_rate.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_frame_rate.restype = AVRational

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 117
if _libs["avdevice"].has("av_buffersink_get_w", "cdecl"):
    av_buffersink_get_w = _libs["avdevice"].get("av_buffersink_get_w", "cdecl")
    av_buffersink_get_w.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_w.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 118
if _libs["avdevice"].has("av_buffersink_get_h", "cdecl"):
    av_buffersink_get_h = _libs["avdevice"].get("av_buffersink_get_h", "cdecl")
    av_buffersink_get_h.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_h.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 119
if _libs["avdevice"].has("av_buffersink_get_sample_aspect_ratio", "cdecl"):
    av_buffersink_get_sample_aspect_ratio = _libs["avdevice"].get("av_buffersink_get_sample_aspect_ratio", "cdecl")
    av_buffersink_get_sample_aspect_ratio.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_sample_aspect_ratio.restype = AVRational

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 121
if _libs["avdevice"].has("av_buffersink_get_channels", "cdecl"):
    av_buffersink_get_channels = _libs["avdevice"].get("av_buffersink_get_channels", "cdecl")
    av_buffersink_get_channels.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_channels.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 124
if _libs["avdevice"].has("av_buffersink_get_channel_layout", "cdecl"):
    av_buffersink_get_channel_layout = _libs["avdevice"].get("av_buffersink_get_channel_layout", "cdecl")
    av_buffersink_get_channel_layout.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_channel_layout.restype = uint64_t

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 126
if _libs["avdevice"].has("av_buffersink_get_ch_layout", "cdecl"):
    av_buffersink_get_ch_layout = _libs["avdevice"].get("av_buffersink_get_ch_layout", "cdecl")
    av_buffersink_get_ch_layout.argtypes = [POINTER(AVFilterContext), POINTER(AVChannelLayout)]
    av_buffersink_get_ch_layout.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 128
if _libs["avdevice"].has("av_buffersink_get_sample_rate", "cdecl"):
    av_buffersink_get_sample_rate = _libs["avdevice"].get("av_buffersink_get_sample_rate", "cdecl")
    av_buffersink_get_sample_rate.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_sample_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 130
if _libs["avdevice"].has("av_buffersink_get_hw_frames_ctx", "cdecl"):
    av_buffersink_get_hw_frames_ctx = _libs["avdevice"].get("av_buffersink_get_hw_frames_ctx", "cdecl")
    av_buffersink_get_hw_frames_ctx.argtypes = [POINTER(AVFilterContext)]
    av_buffersink_get_hw_frames_ctx.restype = POINTER(AVBufferRef)

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 148
if _libs["avdevice"].has("av_buffersink_get_frame", "cdecl"):
    av_buffersink_get_frame = _libs["avdevice"].get("av_buffersink_get_frame", "cdecl")
    av_buffersink_get_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersink_get_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 167
if _libs["avdevice"].has("av_buffersink_get_samples", "cdecl"):
    av_buffersink_get_samples = _libs["avdevice"].get("av_buffersink_get_samples", "cdecl")
    av_buffersink_get_samples.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersink_get_samples.restype = c_int

enum_anon_33 = c_int# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_NO_CHECK_FORMAT = 1# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_PUSH = 4# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 36

AV_BUFFERSRC_FLAG_KEEP_REF = 8# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 36

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 64
if _libs["avdevice"].has("av_buffersrc_get_nb_failed_requests", "cdecl"):
    av_buffersrc_get_nb_failed_requests = _libs["avdevice"].get("av_buffersrc_get_nb_failed_requests", "cdecl")
    av_buffersrc_get_nb_failed_requests.argtypes = [POINTER(AVFilterContext)]
    av_buffersrc_get_nb_failed_requests.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 126
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
    'ch_layout',
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
    ('channel_layout', uint64_t),
    ('ch_layout', AVChannelLayout),
]

AVBufferSrcParameters = struct_AVBufferSrcParameters# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 126

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 132
if _libs["avdevice"].has("av_buffersrc_parameters_alloc", "cdecl"):
    av_buffersrc_parameters_alloc = _libs["avdevice"].get("av_buffersrc_parameters_alloc", "cdecl")
    av_buffersrc_parameters_alloc.argtypes = []
    av_buffersrc_parameters_alloc.restype = POINTER(AVBufferSrcParameters)

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 147
if _libs["avdevice"].has("av_buffersrc_parameters_set", "cdecl"):
    av_buffersrc_parameters_set = _libs["avdevice"].get("av_buffersrc_parameters_set", "cdecl")
    av_buffersrc_parameters_set.argtypes = [POINTER(AVFilterContext), POINTER(AVBufferSrcParameters)]
    av_buffersrc_parameters_set.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 163
if _libs["avdevice"].has("av_buffersrc_write_frame", "cdecl"):
    av_buffersrc_write_frame = _libs["avdevice"].get("av_buffersrc_write_frame", "cdecl")
    av_buffersrc_write_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersrc_write_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 184
if _libs["avdevice"].has("av_buffersrc_add_frame", "cdecl"):
    av_buffersrc_add_frame = _libs["avdevice"].get("av_buffersrc_add_frame", "cdecl")
    av_buffersrc_add_frame.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame)]
    av_buffersrc_add_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 202
if _libs["avdevice"].has("av_buffersrc_add_frame_flags", "cdecl"):
    av_buffersrc_add_frame_flags = _libs["avdevice"].get("av_buffersrc_add_frame_flags", "cdecl")
    av_buffersrc_add_frame_flags.argtypes = [POINTER(AVFilterContext), POINTER(AVFrame), c_int]
    av_buffersrc_add_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 212
if _libs["avdevice"].has("av_buffersrc_close", "cdecl"):
    av_buffersrc_close = _libs["avdevice"].get("av_buffersrc_close", "cdecl")
    av_buffersrc_close.argtypes = [POINTER(AVFilterContext), c_int64, c_uint]
    av_buffersrc_close.restype = c_int

# /home/josiah/ctypesgen_test/av/av/camellia.h: 36
try:
    av_camellia_size = (c_int).in_dll(_libs["avcodec"], "av_camellia_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/camellia.h: 38
class struct_AVCAMELLIA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/camellia.h: 44
if _libs["avcodec"].has("av_camellia_alloc", "cdecl"):
    av_camellia_alloc = _libs["avcodec"].get("av_camellia_alloc", "cdecl")
    av_camellia_alloc.argtypes = []
    av_camellia_alloc.restype = POINTER(struct_AVCAMELLIA)

# /home/josiah/ctypesgen_test/av/av/camellia.h: 53
if _libs["avcodec"].has("av_camellia_init", "cdecl"):
    av_camellia_init = _libs["avcodec"].get("av_camellia_init", "cdecl")
    av_camellia_init.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(uint8_t), c_int]
    av_camellia_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/camellia.h: 65
if _libs["avcodec"].has("av_camellia_crypt", "cdecl"):
    av_camellia_crypt = _libs["avcodec"].get("av_camellia_crypt", "cdecl")
    av_camellia_crypt.argtypes = [POINTER(struct_AVCAMELLIA), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_camellia_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/cast5.h: 36
try:
    av_cast5_size = (c_int).in_dll(_libs["avcodec"], "av_cast5_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cast5.h: 38
class struct_AVCAST5(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/cast5.h: 44
if _libs["avcodec"].has("av_cast5_alloc", "cdecl"):
    av_cast5_alloc = _libs["avcodec"].get("av_cast5_alloc", "cdecl")
    av_cast5_alloc.argtypes = []
    av_cast5_alloc.restype = POINTER(struct_AVCAST5)

# /home/josiah/ctypesgen_test/av/av/cast5.h: 53
if _libs["avcodec"].has("av_cast5_init", "cdecl"):
    av_cast5_init = _libs["avcodec"].get("av_cast5_init", "cdecl")
    av_cast5_init.argtypes = [POINTER(struct_AVCAST5), POINTER(uint8_t), c_int]
    av_cast5_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/cast5.h: 64
if _libs["avcodec"].has("av_cast5_crypt", "cdecl"):
    av_cast5_crypt = _libs["avcodec"].get("av_cast5_crypt", "cdecl")
    av_cast5_crypt.argtypes = [POINTER(struct_AVCAST5), POINTER(uint8_t), POINTER(uint8_t), c_int, c_int]
    av_cast5_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/cast5.h: 76
if _libs["avcodec"].has("av_cast5_crypt2", "cdecl"):
    av_cast5_crypt2 = _libs["avcodec"].get("av_cast5_crypt2", "cdecl")
    av_cast5_crypt2.argtypes = [POINTER(struct_AVCAST5), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_cast5_crypt2.restype = None

# /home/josiah/ctypesgen_test/av/av/cpu.h: 97
if _libs["avcodec"].has("av_get_cpu_flags", "cdecl"):
    av_get_cpu_flags = _libs["avcodec"].get("av_get_cpu_flags", "cdecl")
    av_get_cpu_flags.argtypes = []
    av_get_cpu_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/av/cpu.h: 103
if _libs["avcodec"].has("av_force_cpu_flags", "cdecl"):
    av_force_cpu_flags = _libs["avcodec"].get("av_force_cpu_flags", "cdecl")
    av_force_cpu_flags.argtypes = [c_int]
    av_force_cpu_flags.restype = None

# /home/josiah/ctypesgen_test/av/av/cpu.h: 110
if _libs["avcodec"].has("av_parse_cpu_caps", "cdecl"):
    av_parse_cpu_caps = _libs["avcodec"].get("av_parse_cpu_caps", "cdecl")
    av_parse_cpu_caps.argtypes = [POINTER(c_uint), String]
    av_parse_cpu_caps.restype = c_int

# /home/josiah/ctypesgen_test/av/av/cpu.h: 115
if _libs["avcodec"].has("av_cpu_count", "cdecl"):
    av_cpu_count = _libs["avcodec"].get("av_cpu_count", "cdecl")
    av_cpu_count.argtypes = []
    av_cpu_count.restype = c_int

# /home/josiah/ctypesgen_test/av/av/cpu.h: 121
if _libs["avcodec"].has("av_cpu_force_count", "cdecl"):
    av_cpu_force_count = _libs["avcodec"].get("av_cpu_force_count", "cdecl")
    av_cpu_force_count.argtypes = [c_int]
    av_cpu_force_count.restype = None

# /home/josiah/ctypesgen_test/av/av/cpu.h: 132
if _libs["avcodec"].has("av_cpu_max_align", "cdecl"):
    av_cpu_max_align = _libs["avcodec"].get("av_cpu_max_align", "cdecl")
    av_cpu_max_align.argtypes = []
    av_cpu_max_align.restype = c_size_t

AVCRC = uint32_t# /home/josiah/ctypesgen_test/av/av/crc.h: 46

enum_anon_34 = c_int# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_8_ATM = 0# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_16_ANSI = (AV_CRC_8_ATM + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_16_CCITT = (AV_CRC_16_ANSI + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_32_IEEE = (AV_CRC_16_CCITT + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_32_IEEE_LE = (AV_CRC_32_IEEE + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_16_ANSI_LE = (AV_CRC_32_IEEE_LE + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_24_IEEE = (AV_CRC_16_ANSI_LE + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_8_EBU = (AV_CRC_24_IEEE + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AV_CRC_MAX = (AV_CRC_8_EBU + 1)# /home/josiah/ctypesgen_test/av/av/crc.h: 58

AVCRCId = enum_anon_34# /home/josiah/ctypesgen_test/av/av/crc.h: 58

# /home/josiah/ctypesgen_test/av/av/crc.h: 76
if _libs["avcodec"].has("av_crc_init", "cdecl"):
    av_crc_init = _libs["avcodec"].get("av_crc_init", "cdecl")
    av_crc_init.argtypes = [POINTER(AVCRC), c_int, c_int, uint32_t, c_int]
    av_crc_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/crc.h: 83
if _libs["avcodec"].has("av_crc_get_table", "cdecl"):
    av_crc_get_table = _libs["avcodec"].get("av_crc_get_table", "cdecl")
    av_crc_get_table.argtypes = [AVCRCId]
    av_crc_get_table.restype = POINTER(AVCRC)

# /home/josiah/ctypesgen_test/av/av/crc.h: 95
if _libs["avcodec"].has("av_crc", "cdecl"):
    av_crc = _libs["avcodec"].get("av_crc", "cdecl")
    av_crc.argtypes = [POINTER(AVCRC), uint32_t, POINTER(uint8_t), c_size_t]
    av_crc.restype = uint32_t

# /home/josiah/ctypesgen_test/av/av/des.h: 36
class struct_AVDES(Structure):
    pass

struct_AVDES.__slots__ = [
    'round_keys',
    'triple_des',
]
struct_AVDES._fields_ = [
    ('round_keys', (uint64_t * int(16)) * int(3)),
    ('triple_des', c_int),
]

AVDES = struct_AVDES# /home/josiah/ctypesgen_test/av/av/des.h: 36

# /home/josiah/ctypesgen_test/av/av/des.h: 41
if _libs["avcodec"].has("av_des_alloc", "cdecl"):
    av_des_alloc = _libs["avcodec"].get("av_des_alloc", "cdecl")
    av_des_alloc.argtypes = []
    av_des_alloc.restype = POINTER(AVDES)

# /home/josiah/ctypesgen_test/av/av/des.h: 52
if _libs["avcodec"].has("av_des_init", "cdecl"):
    av_des_init = _libs["avcodec"].get("av_des_init", "cdecl")
    av_des_init.argtypes = [POINTER(struct_AVDES), POINTER(uint8_t), c_int, c_int]
    av_des_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/des.h: 65
if _libs["avcodec"].has("av_des_crypt", "cdecl"):
    av_des_crypt = _libs["avcodec"].get("av_des_crypt", "cdecl")
    av_des_crypt.argtypes = [POINTER(struct_AVDES), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_des_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/des.h: 75
if _libs["avcodec"].has("av_des_mac", "cdecl"):
    av_des_mac = _libs["avcodec"].get("av_des_mac", "cdecl")
    av_des_mac.argtypes = [POINTER(struct_AVDES), POINTER(uint8_t), POINTER(uint8_t), c_int]
    av_des_mac.restype = None

enum_DiracParseCodes = c_int# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_SEQ_HEADER = 0x00# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_END_SEQ = 0x10# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_AUX = 0x20# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_PAD = 0x30# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_PICTURE_CODED = 0x08# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_PICTURE_RAW = 0x48# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_PICTURE_LOW_DEL = 0xC8# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_PICTURE_HQ = 0xE8# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTER_NOREF_CO1 = 0x0A# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTER_NOREF_CO2 = 0x09# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTER_REF_CO1 = 0x0D# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTER_REF_CO2 = 0x0E# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_CO = 0x0C# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_RAW = 0x4C# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_INTRA_REF_PICT = 0xCC# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

DIRAC_PCODE_MAGIC = 0x42424344# /home/josiah/ctypesgen_test/av/av/dirac.h: 57

# /home/josiah/ctypesgen_test/av/av/dirac.h: 79
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

DiracVersionInfo = struct_DiracVersionInfo# /home/josiah/ctypesgen_test/av/av/dirac.h: 79

# /home/josiah/ctypesgen_test/av/av/dirac.h: 114
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
    ('chroma_format', uint8_t),
    ('interlaced', uint8_t),
    ('top_field_first', uint8_t),
    ('frame_rate_index', uint8_t),
    ('aspect_ratio_index', uint8_t),
    ('clean_width', uint16_t),
    ('clean_height', uint16_t),
    ('clean_left_offset', uint16_t),
    ('clean_right_offset', uint16_t),
    ('pixel_range_index', uint8_t),
    ('color_spec_index', uint8_t),
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

AVDiracSeqHeader = struct_AVDiracSeqHeader# /home/josiah/ctypesgen_test/av/av/dirac.h: 114

# /home/josiah/ctypesgen_test/av/av/dirac.h: 127
if _libs["avcodec"].has("av_dirac_parse_sequence_header", "cdecl"):
    av_dirac_parse_sequence_header = _libs["avcodec"].get("av_dirac_parse_sequence_header", "cdecl")
    av_dirac_parse_sequence_header.argtypes = [POINTER(POINTER(AVDiracSeqHeader)), POINTER(uint8_t), c_size_t, POINTER(None)]
    av_dirac_parse_sequence_header.restype = c_int

# /home/josiah/ctypesgen_test/av/av/display.h: 84
if _libs["avcodec"].has("av_display_rotation_get", "cdecl"):
    av_display_rotation_get = _libs["avcodec"].get("av_display_rotation_get", "cdecl")
    av_display_rotation_get.argtypes = [c_int32 * int(9)]
    av_display_rotation_get.restype = c_double

# /home/josiah/ctypesgen_test/av/av/display.h: 94
if _libs["avcodec"].has("av_display_rotation_set", "cdecl"):
    av_display_rotation_set = _libs["avcodec"].get("av_display_rotation_set", "cdecl")
    av_display_rotation_set.argtypes = [c_int32 * int(9), c_double]
    av_display_rotation_set.restype = None

# /home/josiah/ctypesgen_test/av/av/display.h: 103
if _libs["avcodec"].has("av_display_matrix_flip", "cdecl"):
    av_display_matrix_flip = _libs["avcodec"].get("av_display_matrix_flip", "cdecl")
    av_display_matrix_flip.argtypes = [c_int32 * int(9), c_int, c_int]
    av_display_matrix_flip.restype = None

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 61
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
    ('dv_version_major', uint8_t),
    ('dv_version_minor', uint8_t),
    ('dv_profile', uint8_t),
    ('dv_level', uint8_t),
    ('rpu_present_flag', uint8_t),
    ('el_present_flag', uint8_t),
    ('bl_present_flag', uint8_t),
    ('dv_bl_signal_compatibility_id', uint8_t),
]

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 61

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 69
if _libs["avcodec"].has("av_dovi_alloc", "cdecl"):
    av_dovi_alloc = _libs["avcodec"].get("av_dovi_alloc", "cdecl")
    av_dovi_alloc.argtypes = [POINTER(c_size_t)]
    av_dovi_alloc.restype = POINTER(AVDOVIDecoderConfigurationRecord)

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 92
class struct_AVDOVIRpuDataHeader(Structure):
    pass

struct_AVDOVIRpuDataHeader.__slots__ = [
    'rpu_type',
    'rpu_format',
    'vdr_rpu_profile',
    'vdr_rpu_level',
    'chroma_resampling_explicit_filter_flag',
    'coef_data_type',
    'coef_log2_denom',
    'vdr_rpu_normalized_idc',
    'bl_video_full_range_flag',
    'bl_bit_depth',
    'el_bit_depth',
    'vdr_bit_depth',
    'spatial_resampling_filter_flag',
    'el_spatial_resampling_filter_flag',
    'disable_residual_flag',
]
struct_AVDOVIRpuDataHeader._fields_ = [
    ('rpu_type', uint8_t),
    ('rpu_format', uint16_t),
    ('vdr_rpu_profile', uint8_t),
    ('vdr_rpu_level', uint8_t),
    ('chroma_resampling_explicit_filter_flag', uint8_t),
    ('coef_data_type', uint8_t),
    ('coef_log2_denom', uint8_t),
    ('vdr_rpu_normalized_idc', uint8_t),
    ('bl_video_full_range_flag', uint8_t),
    ('bl_bit_depth', uint8_t),
    ('el_bit_depth', uint8_t),
    ('vdr_bit_depth', uint8_t),
    ('spatial_resampling_filter_flag', uint8_t),
    ('el_spatial_resampling_filter_flag', uint8_t),
    ('disable_residual_flag', uint8_t),
]

AVDOVIRpuDataHeader = struct_AVDOVIRpuDataHeader# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 92

enum_AVDOVIMappingMethod = c_int# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 94

AV_DOVI_MAPPING_POLYNOMIAL = 0# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 94

AV_DOVI_MAPPING_MMR = 1# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 94

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 115
class struct_AVDOVIReshapingCurve(Structure):
    pass

struct_AVDOVIReshapingCurve.__slots__ = [
    'num_pivots',
    'pivots',
    'mapping_idc',
    'poly_order',
    'poly_coef',
    'mmr_order',
    'mmr_constant',
    'mmr_coef',
]
struct_AVDOVIReshapingCurve._fields_ = [
    ('num_pivots', uint8_t),
    ('pivots', uint16_t * int((8 + 1))),
    ('mapping_idc', enum_AVDOVIMappingMethod * int(8)),
    ('poly_order', uint8_t * int(8)),
    ('poly_coef', (c_int64 * int(3)) * int(8)),
    ('mmr_order', uint8_t * int(8)),
    ('mmr_constant', c_int64 * int(8)),
    ('mmr_coef', ((c_int64 * int(7)) * int(3)) * int(8)),
]

AVDOVIReshapingCurve = struct_AVDOVIReshapingCurve# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 115

enum_AVDOVINLQMethod = c_int# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 117

AV_DOVI_NLQ_NONE = (-1)# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 117

AV_DOVI_NLQ_LINEAR_DZ = 0# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 117

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 132
class struct_AVDOVINLQParams(Structure):
    pass

struct_AVDOVINLQParams.__slots__ = [
    'nlq_offset',
    'vdr_in_max',
    'linear_deadzone_slope',
    'linear_deadzone_threshold',
]
struct_AVDOVINLQParams._fields_ = [
    ('nlq_offset', uint16_t),
    ('vdr_in_max', uint64_t),
    ('linear_deadzone_slope', uint64_t),
    ('linear_deadzone_threshold', uint64_t),
]

AVDOVINLQParams = struct_AVDOVINLQParams# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 132

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 150
class struct_AVDOVIDataMapping(Structure):
    pass

struct_AVDOVIDataMapping.__slots__ = [
    'vdr_rpu_id',
    'mapping_color_space',
    'mapping_chroma_format_idc',
    'curves',
    'nlq_method_idc',
    'num_x_partitions',
    'num_y_partitions',
    'nlq',
]
struct_AVDOVIDataMapping._fields_ = [
    ('vdr_rpu_id', uint8_t),
    ('mapping_color_space', uint8_t),
    ('mapping_chroma_format_idc', uint8_t),
    ('curves', AVDOVIReshapingCurve * int(3)),
    ('nlq_method_idc', enum_AVDOVINLQMethod),
    ('num_x_partitions', uint32_t),
    ('num_y_partitions', uint32_t),
    ('nlq', AVDOVINLQParams * int(3)),
]

AVDOVIDataMapping = struct_AVDOVIDataMapping# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 150

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 187
class struct_AVDOVIColorMetadata(Structure):
    pass

struct_AVDOVIColorMetadata.__slots__ = [
    'dm_metadata_id',
    'scene_refresh_flag',
    'ycc_to_rgb_matrix',
    'ycc_to_rgb_offset',
    'rgb_to_lms_matrix',
    'signal_eotf',
    'signal_eotf_param0',
    'signal_eotf_param1',
    'signal_eotf_param2',
    'signal_bit_depth',
    'signal_color_space',
    'signal_chroma_format',
    'signal_full_range_flag',
    'source_min_pq',
    'source_max_pq',
    'source_diagonal',
]
struct_AVDOVIColorMetadata._fields_ = [
    ('dm_metadata_id', uint8_t),
    ('scene_refresh_flag', uint8_t),
    ('ycc_to_rgb_matrix', AVRational * int(9)),
    ('ycc_to_rgb_offset', AVRational * int(3)),
    ('rgb_to_lms_matrix', AVRational * int(9)),
    ('signal_eotf', uint16_t),
    ('signal_eotf_param0', uint16_t),
    ('signal_eotf_param1', uint16_t),
    ('signal_eotf_param2', uint32_t),
    ('signal_bit_depth', uint8_t),
    ('signal_color_space', uint8_t),
    ('signal_chroma_format', uint8_t),
    ('signal_full_range_flag', uint8_t),
    ('source_min_pq', uint16_t),
    ('source_max_pq', uint16_t),
    ('source_diagonal', uint16_t),
]

AVDOVIColorMetadata = struct_AVDOVIColorMetadata# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 187

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 205
class struct_AVDOVIMetadata(Structure):
    pass

struct_AVDOVIMetadata.__slots__ = [
    'header_offset',
    'mapping_offset',
    'color_offset',
]
struct_AVDOVIMetadata._fields_ = [
    ('header_offset', c_size_t),
    ('mapping_offset', c_size_t),
    ('color_offset', c_size_t),
]

AVDOVIMetadata = struct_AVDOVIMetadata# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 205

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 234
if _libs["avcodec"].has("av_dovi_metadata_alloc", "cdecl"):
    av_dovi_metadata_alloc = _libs["avcodec"].get("av_dovi_metadata_alloc", "cdecl")
    av_dovi_metadata_alloc.argtypes = [POINTER(c_size_t)]
    av_dovi_metadata_alloc.restype = POINTER(AVDOVIMetadata)

enum_AVDownmixType = c_int# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_UNKNOWN = 0# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_LORO = (AV_DOWNMIX_TYPE_UNKNOWN + 1)# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_LTRT = (AV_DOWNMIX_TYPE_LORO + 1)# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_DPLII = (AV_DOWNMIX_TYPE_LTRT + 1)# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

AV_DOWNMIX_TYPE_NB = (AV_DOWNMIX_TYPE_DPLII + 1)# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 44

# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 93
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

AVDownmixInfo = struct_AVDownmixInfo# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 93

# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 105
if _libs["avcodec"].has("av_downmix_info_update_side_data", "cdecl"):
    av_downmix_info_update_side_data = _libs["avcodec"].get("av_downmix_info_update_side_data", "cdecl")
    av_downmix_info_update_side_data.argtypes = [POINTER(AVFrame)]
    av_downmix_info_update_side_data.restype = POINTER(AVDownmixInfo)

# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 58
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
    ('block_sizes', POINTER(uint8_t)),
    ('audio_stride', c_int),
    ('audio_min_samples', c_int * int(3)),
    ('audio_samples_dist', c_int * int(5)),
    ('audio_shuffle', POINTER(uint8_t * int(9))),
]

AVDVProfile = struct_AVDVProfile# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 58

# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 68
if _libs["avcodec"].has("av_dv_frame_profile", "cdecl"):
    av_dv_frame_profile = _libs["avcodec"].get("av_dv_frame_profile", "cdecl")
    av_dv_frame_profile.argtypes = [POINTER(AVDVProfile), POINTER(uint8_t), c_uint]
    av_dv_frame_profile.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 74
if _libs["avcodec"].has("av_dv_codec_profile", "cdecl"):
    av_dv_codec_profile = _libs["avcodec"].get("av_dv_codec_profile", "cdecl")
    av_dv_codec_profile.argtypes = [c_int, c_int, enum_AVPixelFormat]
    av_dv_codec_profile.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 80
if _libs["avcodec"].has("av_dv_codec_profile2", "cdecl"):
    av_dv_codec_profile2 = _libs["avcodec"].get("av_dv_codec_profile2", "cdecl")
    av_dv_codec_profile2.argtypes = [c_int, c_int, enum_AVPixelFormat, AVRational]
    av_dv_codec_profile2.restype = POINTER(AVDVProfile)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 35
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

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 35

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 81
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
    ('scheme', uint32_t),
    ('crypt_byte_block', uint32_t),
    ('skip_byte_block', uint32_t),
    ('key_id', POINTER(uint8_t)),
    ('key_id_size', uint32_t),
    ('iv', POINTER(uint8_t)),
    ('iv_size', uint32_t),
    ('subsamples', POINTER(AVSubsampleEncryptionInfo)),
    ('subsample_count', uint32_t),
]

AVEncryptionInfo = struct_AVEncryptionInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 81

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 88
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
    ('system_id', POINTER(uint8_t)),
    ('system_id_size', uint32_t),
    ('key_ids', POINTER(POINTER(uint8_t))),
    ('num_key_ids', uint32_t),
    ('key_id_size', uint32_t),
    ('data', POINTER(uint8_t)),
    ('data_size', uint32_t),
    ('next', POINTER(struct_AVEncryptionInitInfo)),
]

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 123

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 136
if _libs["avcodec"].has("av_encryption_info_alloc", "cdecl"):
    av_encryption_info_alloc = _libs["avcodec"].get("av_encryption_info_alloc", "cdecl")
    av_encryption_info_alloc.argtypes = [uint32_t, uint32_t, uint32_t]
    av_encryption_info_alloc.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 142
if _libs["avcodec"].has("av_encryption_info_clone", "cdecl"):
    av_encryption_info_clone = _libs["avcodec"].get("av_encryption_info_clone", "cdecl")
    av_encryption_info_clone.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_clone.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 148
if _libs["avcodec"].has("av_encryption_info_free", "cdecl"):
    av_encryption_info_free = _libs["avcodec"].get("av_encryption_info_free", "cdecl")
    av_encryption_info_free.argtypes = [POINTER(AVEncryptionInfo)]
    av_encryption_info_free.restype = None

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 157
if _libs["avcodec"].has("av_encryption_info_get_side_data", "cdecl"):
    av_encryption_info_get_side_data = _libs["avcodec"].get("av_encryption_info_get_side_data", "cdecl")
    av_encryption_info_get_side_data.argtypes = [POINTER(uint8_t), c_size_t]
    av_encryption_info_get_side_data.restype = POINTER(AVEncryptionInfo)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 166
if _libs["avcodec"].has("av_encryption_info_add_side_data", "cdecl"):
    av_encryption_info_add_side_data = _libs["avcodec"].get("av_encryption_info_add_side_data", "cdecl")
    av_encryption_info_add_side_data.argtypes = [POINTER(AVEncryptionInfo), POINTER(c_size_t)]
    av_encryption_info_add_side_data.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 176
if _libs["avcodec"].has("av_encryption_init_info_alloc", "cdecl"):
    av_encryption_init_info_alloc = _libs["avcodec"].get("av_encryption_init_info_alloc", "cdecl")
    av_encryption_init_info_alloc.argtypes = [uint32_t, uint32_t, uint32_t, uint32_t]
    av_encryption_init_info_alloc.restype = POINTER(AVEncryptionInitInfo)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 183
if _libs["avcodec"].has("av_encryption_init_info_free", "cdecl"):
    av_encryption_init_info_free = _libs["avcodec"].get("av_encryption_init_info_free", "cdecl")
    av_encryption_init_info_free.argtypes = [POINTER(AVEncryptionInitInfo)]
    av_encryption_init_info_free.restype = None

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 192
if _libs["avcodec"].has("av_encryption_init_info_get_side_data", "cdecl"):
    av_encryption_init_info_get_side_data = _libs["avcodec"].get("av_encryption_init_info_get_side_data", "cdecl")
    av_encryption_init_info_get_side_data.argtypes = [POINTER(uint8_t), c_size_t]
    av_encryption_init_info_get_side_data.restype = POINTER(AVEncryptionInitInfo)

# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 202
if _libs["avcodec"].has("av_encryption_init_info_add_side_data", "cdecl"):
    av_encryption_init_info_add_side_data = _libs["avcodec"].get("av_encryption_init_info_add_side_data", "cdecl")
    av_encryption_init_info_add_side_data.argtypes = [POINTER(AVEncryptionInitInfo), POINTER(c_size_t)]
    av_encryption_init_info_add_side_data.restype = POINTER(uint8_t)

# /home/josiah/ctypesgen_test/av/av/eval.h: 29
class struct_AVExpr(Structure):
    pass

AVExpr = struct_AVExpr# /home/josiah/ctypesgen_test/av/av/eval.h: 29

# /home/josiah/ctypesgen_test/av/av/eval.h: 50
if _libs["avcodec"].has("av_expr_parse_and_eval", "cdecl"):
    av_expr_parse_and_eval = _libs["avcodec"].get("av_expr_parse_and_eval", "cdecl")
    av_expr_parse_and_eval.argtypes = [POINTER(c_double), String, POINTER(POINTER(c_char)), POINTER(c_double), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), POINTER(None), c_int, POINTER(None)]
    av_expr_parse_and_eval.restype = c_int

# /home/josiah/ctypesgen_test/av/av/eval.h: 74
if _libs["avcodec"].has("av_expr_parse", "cdecl"):
    av_expr_parse = _libs["avcodec"].get("av_expr_parse", "cdecl")
    av_expr_parse.argtypes = [POINTER(POINTER(AVExpr)), String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double)), POINTER(POINTER(c_char)), POINTER(CFUNCTYPE(UNCHECKED(c_double), POINTER(None), c_double, c_double)), c_int, POINTER(None)]
    av_expr_parse.restype = c_int

# /home/josiah/ctypesgen_test/av/av/eval.h: 88
if _libs["avcodec"].has("av_expr_eval", "cdecl"):
    av_expr_eval = _libs["avcodec"].get("av_expr_eval", "cdecl")
    av_expr_eval.argtypes = [POINTER(AVExpr), POINTER(c_double), POINTER(None)]
    av_expr_eval.restype = c_double

# /home/josiah/ctypesgen_test/av/av/eval.h: 99
if _libs["avcodec"].has("av_expr_count_vars", "cdecl"):
    av_expr_count_vars = _libs["avcodec"].get("av_expr_count_vars", "cdecl")
    av_expr_count_vars.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int]
    av_expr_count_vars.restype = c_int

# /home/josiah/ctypesgen_test/av/av/eval.h: 114
if _libs["avcodec"].has("av_expr_count_func", "cdecl"):
    av_expr_count_func = _libs["avcodec"].get("av_expr_count_func", "cdecl")
    av_expr_count_func.argtypes = [POINTER(AVExpr), POINTER(c_uint), c_int, c_int]
    av_expr_count_func.restype = c_int

# /home/josiah/ctypesgen_test/av/av/eval.h: 119
if _libs["avcodec"].has("av_expr_free", "cdecl"):
    av_expr_free = _libs["avcodec"].get("av_expr_free", "cdecl")
    av_expr_free.argtypes = [POINTER(AVExpr)]
    av_expr_free.restype = None

# /home/josiah/ctypesgen_test/av/av/eval.h: 138
if _libs["avcodec"].has("av_strtod", "cdecl"):
    av_strtod = _libs["avcodec"].get("av_strtod", "cdecl")
    av_strtod.argtypes = [String, POINTER(POINTER(c_char))]
    av_strtod.restype = c_double

# /home/josiah/ctypesgen_test/av/av/fifo.h: 42
class struct_AVFifo(Structure):
    pass

AVFifo = struct_AVFifo# /home/josiah/ctypesgen_test/av/av/fifo.h: 42

AVFifoCB = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(c_size_t))# /home/josiah/ctypesgen_test/av/av/fifo.h: 60

# /home/josiah/ctypesgen_test/av/av/fifo.h: 79
if _libs["avcodec"].has("av_fifo_alloc2", "cdecl"):
    av_fifo_alloc2 = _libs["avcodec"].get("av_fifo_alloc2", "cdecl")
    av_fifo_alloc2.argtypes = [c_size_t, c_size_t, c_uint]
    av_fifo_alloc2.restype = POINTER(AVFifo)

# /home/josiah/ctypesgen_test/av/av/fifo.h: 86
if _libs["avcodec"].has("av_fifo_elem_size", "cdecl"):
    av_fifo_elem_size = _libs["avcodec"].get("av_fifo_elem_size", "cdecl")
    av_fifo_elem_size.argtypes = [POINTER(AVFifo)]
    av_fifo_elem_size.restype = c_size_t

# /home/josiah/ctypesgen_test/av/av/fifo.h: 92
if _libs["avcodec"].has("av_fifo_auto_grow_limit", "cdecl"):
    av_fifo_auto_grow_limit = _libs["avcodec"].get("av_fifo_auto_grow_limit", "cdecl")
    av_fifo_auto_grow_limit.argtypes = [POINTER(AVFifo), c_size_t]
    av_fifo_auto_grow_limit.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 97
if _libs["avcodec"].has("av_fifo_can_read", "cdecl"):
    av_fifo_can_read = _libs["avcodec"].get("av_fifo_can_read", "cdecl")
    av_fifo_can_read.argtypes = [POINTER(AVFifo)]
    av_fifo_can_read.restype = c_size_t

# /home/josiah/ctypesgen_test/av/av/fifo.h: 108
if _libs["avcodec"].has("av_fifo_can_write", "cdecl"):
    av_fifo_can_write = _libs["avcodec"].get("av_fifo_can_write", "cdecl")
    av_fifo_can_write.argtypes = [POINTER(AVFifo)]
    av_fifo_can_write.restype = c_size_t

# /home/josiah/ctypesgen_test/av/av/fifo.h: 122
if _libs["avcodec"].has("av_fifo_grow2", "cdecl"):
    av_fifo_grow2 = _libs["avcodec"].get("av_fifo_grow2", "cdecl")
    av_fifo_grow2.argtypes = [POINTER(AVFifo), c_size_t]
    av_fifo_grow2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 140
if _libs["avcodec"].has("av_fifo_write", "cdecl"):
    av_fifo_write = _libs["avcodec"].get("av_fifo_write", "cdecl")
    av_fifo_write.argtypes = [POINTER(AVFifo), POINTER(None), c_size_t]
    av_fifo_write.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 155
if _libs["avcodec"].has("av_fifo_write_from_cb", "cdecl"):
    av_fifo_write_from_cb = _libs["avcodec"].get("av_fifo_write_from_cb", "cdecl")
    av_fifo_write_from_cb.argtypes = [POINTER(AVFifo), AVFifoCB, POINTER(None), POINTER(c_size_t)]
    av_fifo_write_from_cb.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 171
if _libs["avcodec"].has("av_fifo_read", "cdecl"):
    av_fifo_read = _libs["avcodec"].get("av_fifo_read", "cdecl")
    av_fifo_read.argtypes = [POINTER(AVFifo), POINTER(None), c_size_t]
    av_fifo_read.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 186
if _libs["avcodec"].has("av_fifo_read_to_cb", "cdecl"):
    av_fifo_read_to_cb = _libs["avcodec"].get("av_fifo_read_to_cb", "cdecl")
    av_fifo_read_to_cb.argtypes = [POINTER(AVFifo), AVFifoCB, POINTER(None), POINTER(c_size_t)]
    av_fifo_read_to_cb.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 203
if _libs["avcodec"].has("av_fifo_peek", "cdecl"):
    av_fifo_peek = _libs["avcodec"].get("av_fifo_peek", "cdecl")
    av_fifo_peek.argtypes = [POINTER(AVFifo), POINTER(None), c_size_t, c_size_t]
    av_fifo_peek.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 220
if _libs["avcodec"].has("av_fifo_peek_to_cb", "cdecl"):
    av_fifo_peek_to_cb = _libs["avcodec"].get("av_fifo_peek_to_cb", "cdecl")
    av_fifo_peek_to_cb.argtypes = [POINTER(AVFifo), AVFifoCB, POINTER(None), POINTER(c_size_t), c_size_t]
    av_fifo_peek_to_cb.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 228
if _libs["avcodec"].has("av_fifo_drain2", "cdecl"):
    av_fifo_drain2 = _libs["avcodec"].get("av_fifo_drain2", "cdecl")
    av_fifo_drain2.argtypes = [POINTER(AVFifo), c_size_t]
    av_fifo_drain2.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 234
if _libs["avcodec"].has("av_fifo_reset2", "cdecl"):
    av_fifo_reset2 = _libs["avcodec"].get("av_fifo_reset2", "cdecl")
    av_fifo_reset2.argtypes = [POINTER(AVFifo)]
    av_fifo_reset2.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 240
if _libs["avcodec"].has("av_fifo_freep2", "cdecl"):
    av_fifo_freep2 = _libs["avcodec"].get("av_fifo_freep2", "cdecl")
    av_fifo_freep2.argtypes = [POINTER(POINTER(AVFifo))]
    av_fifo_freep2.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 248
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
    ('buffer', POINTER(uint8_t)),
    ('rptr', POINTER(uint8_t)),
    ('wptr', POINTER(uint8_t)),
    ('end', POINTER(uint8_t)),
    ('rndx', uint32_t),
    ('wndx', uint32_t),
]

AVFifoBuffer = struct_AVFifoBuffer# /home/josiah/ctypesgen_test/av/av/fifo.h: 248

# /home/josiah/ctypesgen_test/av/av/fifo.h: 257
if _libs["avcodec"].has("av_fifo_alloc", "cdecl"):
    av_fifo_alloc = _libs["avcodec"].get("av_fifo_alloc", "cdecl")
    av_fifo_alloc.argtypes = [c_uint]
    av_fifo_alloc.restype = POINTER(AVFifoBuffer)

# /home/josiah/ctypesgen_test/av/av/fifo.h: 267
if _libs["avcodec"].has("av_fifo_alloc_array", "cdecl"):
    av_fifo_alloc_array = _libs["avcodec"].get("av_fifo_alloc_array", "cdecl")
    av_fifo_alloc_array.argtypes = [c_size_t, c_size_t]
    av_fifo_alloc_array.restype = POINTER(AVFifoBuffer)

# /home/josiah/ctypesgen_test/av/av/fifo.h: 275
if _libs["avcodec"].has("av_fifo_free", "cdecl"):
    av_fifo_free = _libs["avcodec"].get("av_fifo_free", "cdecl")
    av_fifo_free.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_free.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 283
if _libs["avcodec"].has("av_fifo_freep", "cdecl"):
    av_fifo_freep = _libs["avcodec"].get("av_fifo_freep", "cdecl")
    av_fifo_freep.argtypes = [POINTER(POINTER(AVFifoBuffer))]
    av_fifo_freep.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 291
if _libs["avcodec"].has("av_fifo_reset", "cdecl"):
    av_fifo_reset = _libs["avcodec"].get("av_fifo_reset", "cdecl")
    av_fifo_reset.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_reset.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 301
if _libs["avcodec"].has("av_fifo_size", "cdecl"):
    av_fifo_size = _libs["avcodec"].get("av_fifo_size", "cdecl")
    av_fifo_size.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 311
if _libs["avcodec"].has("av_fifo_space", "cdecl"):
    av_fifo_space = _libs["avcodec"].get("av_fifo_space", "cdecl")
    av_fifo_space.argtypes = [POINTER(AVFifoBuffer)]
    av_fifo_space.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 328
if _libs["avcodec"].has("av_fifo_generic_peek_at", "cdecl"):
    av_fifo_generic_peek_at = _libs["avcodec"].get("av_fifo_generic_peek_at", "cdecl")
    av_fifo_generic_peek_at.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek_at.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 344
if _libs["avcodec"].has("av_fifo_generic_peek", "cdecl"):
    av_fifo_generic_peek = _libs["avcodec"].get("av_fifo_generic_peek", "cdecl")
    av_fifo_generic_peek.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_peek.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 359
if _libs["avcodec"].has("av_fifo_generic_read", "cdecl"):
    av_fifo_generic_read = _libs["avcodec"].get("av_fifo_generic_read", "cdecl")
    av_fifo_generic_read.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_read.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 378
if _libs["avcodec"].has("av_fifo_generic_write", "cdecl"):
    av_fifo_generic_write = _libs["avcodec"].get("av_fifo_generic_write", "cdecl")
    av_fifo_generic_write.argtypes = [POINTER(AVFifoBuffer), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), c_int)]
    av_fifo_generic_write.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 392
if _libs["avcodec"].has("av_fifo_realloc2", "cdecl"):
    av_fifo_realloc2 = _libs["avcodec"].get("av_fifo_realloc2", "cdecl")
    av_fifo_realloc2.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_realloc2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 407
if _libs["avcodec"].has("av_fifo_grow", "cdecl"):
    av_fifo_grow = _libs["avcodec"].get("av_fifo_grow", "cdecl")
    av_fifo_grow.argtypes = [POINTER(AVFifoBuffer), c_uint]
    av_fifo_grow.restype = c_int

# /home/josiah/ctypesgen_test/av/av/fifo.h: 417
if _libs["avcodec"].has("av_fifo_drain", "cdecl"):
    av_fifo_drain = _libs["avcodec"].get("av_fifo_drain", "cdecl")
    av_fifo_drain.argtypes = [POINTER(AVFifoBuffer), c_int]
    av_fifo_drain.restype = None

# /home/josiah/ctypesgen_test/av/av/fifo.h: 434
for _lib in _libs.values():
    try:
        ptr = (POINTER(uint8_t)).in_dll(_lib, "ptr")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/file.h: 51
if _libs["avcodec"].has("av_file_map", "cdecl"):
    av_file_map = _libs["avcodec"].get("av_file_map", "cdecl")
    av_file_map.argtypes = [String, POINTER(POINTER(uint8_t)), POINTER(c_size_t), c_int, POINTER(None)]
    av_file_map.restype = c_int

# /home/josiah/ctypesgen_test/av/av/file.h: 61
if _libs["avcodec"].has("av_file_unmap", "cdecl"):
    av_file_unmap = _libs["avcodec"].get("av_file_unmap", "cdecl")
    av_file_unmap.argtypes = [POINTER(uint8_t), c_size_t]
    av_file_unmap.restype = None

# /home/josiah/ctypesgen_test/av/av/file.h: 77
if _libs["avcodec"].has("av_tempfile", "cdecl"):
    av_tempfile = _libs["avcodec"].get("av_tempfile", "cdecl")
    av_tempfile.argtypes = [String, POINTER(POINTER(c_char)), c_int, POINTER(None)]
    av_tempfile.restype = c_int

enum_AVFilmGrainParamsType = c_int# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_NONE = 0# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_AV1 = (AV_FILM_GRAIN_PARAMS_NONE + 1)# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 24

AV_FILM_GRAIN_PARAMS_H274 = (AV_FILM_GRAIN_PARAMS_AV1 + 1)# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 24

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 123
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
    ('y_points', (uint8_t * int(2)) * int(14)),
    ('chroma_scaling_from_luma', c_int),
    ('num_uv_points', c_int * int(2)),
    ('uv_points', ((uint8_t * int(2)) * int(10)) * int(2)),
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

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 123

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 206
class struct_AVFilmGrainH274Params(Structure):
    pass

struct_AVFilmGrainH274Params.__slots__ = [
    'model_id',
    'bit_depth_luma',
    'bit_depth_chroma',
    'color_range',
    'color_primaries',
    'color_trc',
    'color_space',
    'blending_mode_id',
    'log2_scale_factor',
    'component_model_present',
    'num_intensity_intervals',
    'num_model_values',
    'intensity_interval_lower_bound',
    'intensity_interval_upper_bound',
    'comp_model_value',
]
struct_AVFilmGrainH274Params._fields_ = [
    ('model_id', c_int),
    ('bit_depth_luma', c_int),
    ('bit_depth_chroma', c_int),
    ('color_range', enum_AVColorRange),
    ('color_primaries', enum_AVColorPrimaries),
    ('color_trc', enum_AVColorTransferCharacteristic),
    ('color_space', enum_AVColorSpace),
    ('blending_mode_id', c_int),
    ('log2_scale_factor', c_int),
    ('component_model_present', c_int * int(3)),
    ('num_intensity_intervals', uint16_t * int(3)),
    ('num_model_values', uint8_t * int(3)),
    ('intensity_interval_lower_bound', (uint8_t * int(256)) * int(3)),
    ('intensity_interval_upper_bound', (uint8_t * int(256)) * int(3)),
    ('comp_model_value', ((c_int16 * int(6)) * int(256)) * int(3)),
]

AVFilmGrainH274Params = struct_AVFilmGrainH274Params# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 206

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 235
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'aom',
    'h274',
]
union_anon_35._fields_ = [
    ('aom', AVFilmGrainAOMParams),
    ('h274', AVFilmGrainH274Params),
]

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 239
class struct_AVFilmGrainParams(Structure):
    pass

struct_AVFilmGrainParams.__slots__ = [
    'type',
    'seed',
    'codec',
]
struct_AVFilmGrainParams._fields_ = [
    ('type', enum_AVFilmGrainParamsType),
    ('seed', uint64_t),
    ('codec', union_anon_35),
]

AVFilmGrainParams = struct_AVFilmGrainParams# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 239

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 249
if _libs["avcodec"].has("av_film_grain_params_alloc", "cdecl"):
    av_film_grain_params_alloc = _libs["avcodec"].get("av_film_grain_params_alloc", "cdecl")
    av_film_grain_params_alloc.argtypes = [POINTER(c_size_t)]
    av_film_grain_params_alloc.restype = POINTER(AVFilmGrainParams)

# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 258
if _libs["avcodec"].has("av_film_grain_params_create_side_data", "cdecl"):
    av_film_grain_params_create_side_data = _libs["avcodec"].get("av_film_grain_params_create_side_data", "cdecl")
    av_film_grain_params_create_side_data.argtypes = [POINTER(AVFrame)]
    av_film_grain_params_create_side_data.restype = POINTER(AVFilmGrainParams)

# /home/josiah/ctypesgen_test/av/av/hash.h: 115
class struct_AVHashContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/hash.h: 125
if _libs["avcodec"].has("av_hash_alloc", "cdecl"):
    av_hash_alloc = _libs["avcodec"].get("av_hash_alloc", "cdecl")
    av_hash_alloc.argtypes = [POINTER(POINTER(struct_AVHashContext)), String]
    av_hash_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/hash.h: 135
if _libs["avcodec"].has("av_hash_names", "cdecl"):
    av_hash_names = _libs["avcodec"].get("av_hash_names", "cdecl")
    av_hash_names.argtypes = [c_int]
    av_hash_names.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/hash.h: 140
if _libs["avcodec"].has("av_hash_get_name", "cdecl"):
    av_hash_get_name = _libs["avcodec"].get("av_hash_get_name", "cdecl")
    av_hash_get_name.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/hash.h: 167
if _libs["avcodec"].has("av_hash_get_size", "cdecl"):
    av_hash_get_size = _libs["avcodec"].get("av_hash_get_size", "cdecl")
    av_hash_get_size.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_get_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/hash.h: 174
if _libs["avcodec"].has("av_hash_init", "cdecl"):
    av_hash_init = _libs["avcodec"].get("av_hash_init", "cdecl")
    av_hash_init.argtypes = [POINTER(struct_AVHashContext)]
    av_hash_init.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 183
if _libs["avcodec"].has("av_hash_update", "cdecl"):
    av_hash_update = _libs["avcodec"].get("av_hash_update", "cdecl")
    av_hash_update.argtypes = [POINTER(struct_AVHashContext), POINTER(uint8_t), c_size_t]
    av_hash_update.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 199
if _libs["avcodec"].has("av_hash_final", "cdecl"):
    av_hash_final = _libs["avcodec"].get("av_hash_final", "cdecl")
    av_hash_final.argtypes = [POINTER(struct_AVHashContext), POINTER(uint8_t)]
    av_hash_final.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 214
if _libs["avcodec"].has("av_hash_final_bin", "cdecl"):
    av_hash_final_bin = _libs["avcodec"].get("av_hash_final_bin", "cdecl")
    av_hash_final_bin.argtypes = [POINTER(struct_AVHashContext), POINTER(uint8_t), c_int]
    av_hash_final_bin.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 232
if _libs["avcodec"].has("av_hash_final_hex", "cdecl"):
    av_hash_final_hex = _libs["avcodec"].get("av_hash_final_hex", "cdecl")
    av_hash_final_hex.argtypes = [POINTER(struct_AVHashContext), POINTER(uint8_t), c_int]
    av_hash_final_hex.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 250
if _libs["avcodec"].has("av_hash_final_b64", "cdecl"):
    av_hash_final_b64 = _libs["avcodec"].get("av_hash_final_b64", "cdecl")
    av_hash_final_b64.argtypes = [POINTER(struct_AVHashContext), POINTER(uint8_t), c_int]
    av_hash_final_b64.restype = None

# /home/josiah/ctypesgen_test/av/av/hash.h: 257
if _libs["avcodec"].has("av_hash_freep", "cdecl"):
    av_hash_freep = _libs["avcodec"].get("av_hash_freep", "cdecl")
    av_hash_freep.argtypes = [POINTER(POINTER(struct_AVHashContext))]
    av_hash_freep.restype = None

enum_AVHDRPlusOverlapProcessOption = c_int# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_WEIGHTED_AVERAGING = 0# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 30

AV_HDR_PLUS_OVERLAP_PROCESS_LAYERING = 1# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 30

# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 53
class struct_AVHDRPlusPercentile(Structure):
    pass

struct_AVHDRPlusPercentile.__slots__ = [
    'percentage',
    'percentile',
]
struct_AVHDRPlusPercentile._fields_ = [
    ('percentage', uint8_t),
    ('percentile', AVRational),
]

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 53

# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 230
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
    ('center_of_ellipse_x', uint16_t),
    ('center_of_ellipse_y', uint16_t),
    ('rotation_angle', uint8_t),
    ('semimajor_axis_internal_ellipse', uint16_t),
    ('semimajor_axis_external_ellipse', uint16_t),
    ('semiminor_axis_external_ellipse', uint16_t),
    ('overlap_process_option', enum_AVHDRPlusOverlapProcessOption),
    ('maxscl', AVRational * int(3)),
    ('average_maxrgb', AVRational),
    ('num_distribution_maxrgb_percentiles', uint8_t),
    ('distribution_maxrgb', AVHDRPlusPercentile * int(15)),
    ('fraction_bright_pixels', AVRational),
    ('tone_mapping_flag', uint8_t),
    ('knee_point_x', AVRational),
    ('knee_point_y', AVRational),
    ('num_bezier_curve_anchors', uint8_t),
    ('bezier_curve_anchors', AVRational * int(15)),
    ('color_saturation_mapping_flag', uint8_t),
    ('color_saturation_weight', AVRational),
]

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 230

# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 323
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
    ('itu_t_t35_country_code', uint8_t),
    ('application_version', uint8_t),
    ('num_windows', uint8_t),
    ('params', AVHDRPlusColorTransformParams * int(3)),
    ('targeted_system_display_maximum_luminance', AVRational),
    ('targeted_system_display_actual_peak_luminance_flag', uint8_t),
    ('num_rows_targeted_system_display_actual_peak_luminance', uint8_t),
    ('num_cols_targeted_system_display_actual_peak_luminance', uint8_t),
    ('targeted_system_display_actual_peak_luminance', (AVRational * int(25)) * int(25)),
    ('mastering_display_actual_peak_luminance_flag', uint8_t),
    ('num_rows_mastering_display_actual_peak_luminance', uint8_t),
    ('num_cols_mastering_display_actual_peak_luminance', uint8_t),
    ('mastering_display_actual_peak_luminance', (AVRational * int(25)) * int(25)),
]

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 323

# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 332
if _libs["avcodec"].has("av_dynamic_hdr_plus_alloc", "cdecl"):
    av_dynamic_hdr_plus_alloc = _libs["avcodec"].get("av_dynamic_hdr_plus_alloc", "cdecl")
    av_dynamic_hdr_plus_alloc.argtypes = [POINTER(c_size_t)]
    av_dynamic_hdr_plus_alloc.restype = POINTER(AVDynamicHDRPlus)

# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 341
if _libs["avcodec"].has("av_dynamic_hdr_plus_create_side_data", "cdecl"):
    av_dynamic_hdr_plus_create_side_data = _libs["avcodec"].get("av_dynamic_hdr_plus_create_side_data", "cdecl")
    av_dynamic_hdr_plus_create_side_data.argtypes = [POINTER(AVFrame)]
    av_dynamic_hdr_plus_create_side_data.restype = POINTER(AVDynamicHDRPlus)

enum_AVHMACType = c_int# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_MD5 = 0# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_SHA1 = (AV_HMAC_MD5 + 1)# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_SHA224 = (AV_HMAC_SHA1 + 1)# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_SHA256 = (AV_HMAC_SHA224 + 1)# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_SHA384 = (AV_HMAC_SHA256 + 1)# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

AV_HMAC_SHA512 = (AV_HMAC_SHA384 + 1)# /home/josiah/ctypesgen_test/av/av/hmac.h: 32

# /home/josiah/ctypesgen_test/av/av/hmac.h: 41
class struct_AVHMAC(Structure):
    pass

AVHMAC = struct_AVHMAC# /home/josiah/ctypesgen_test/av/av/hmac.h: 41

# /home/josiah/ctypesgen_test/av/av/hmac.h: 47
if _libs["avcodec"].has("av_hmac_alloc", "cdecl"):
    av_hmac_alloc = _libs["avcodec"].get("av_hmac_alloc", "cdecl")
    av_hmac_alloc.argtypes = [enum_AVHMACType]
    av_hmac_alloc.restype = POINTER(AVHMAC)

# /home/josiah/ctypesgen_test/av/av/hmac.h: 53
if _libs["avcodec"].has("av_hmac_free", "cdecl"):
    av_hmac_free = _libs["avcodec"].get("av_hmac_free", "cdecl")
    av_hmac_free.argtypes = [POINTER(AVHMAC)]
    av_hmac_free.restype = None

# /home/josiah/ctypesgen_test/av/av/hmac.h: 61
if _libs["avcodec"].has("av_hmac_init", "cdecl"):
    av_hmac_init = _libs["avcodec"].get("av_hmac_init", "cdecl")
    av_hmac_init.argtypes = [POINTER(AVHMAC), POINTER(uint8_t), c_uint]
    av_hmac_init.restype = None

# /home/josiah/ctypesgen_test/av/av/hmac.h: 69
if _libs["avcodec"].has("av_hmac_update", "cdecl"):
    av_hmac_update = _libs["avcodec"].get("av_hmac_update", "cdecl")
    av_hmac_update.argtypes = [POINTER(AVHMAC), POINTER(uint8_t), c_uint]
    av_hmac_update.restype = None

# /home/josiah/ctypesgen_test/av/av/hmac.h: 78
if _libs["avcodec"].has("av_hmac_final", "cdecl"):
    av_hmac_final = _libs["avcodec"].get("av_hmac_final", "cdecl")
    av_hmac_final.argtypes = [POINTER(AVHMAC), POINTER(uint8_t), c_uint]
    av_hmac_final.restype = c_int

# /home/josiah/ctypesgen_test/av/av/hmac.h: 91
if _libs["avcodec"].has("av_hmac_calc", "cdecl"):
    av_hmac_calc = _libs["avcodec"].get("av_hmac_calc", "cdecl")
    av_hmac_calc.argtypes = [POINTER(AVHMAC), POINTER(uint8_t), c_uint, POINTER(uint8_t), c_uint, POINTER(uint8_t), c_uint]
    av_hmac_calc.restype = c_int

enum_anon_36 = c_int# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 35

AV_DRM_MAX_PLANES = 4# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 35

# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 66
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
    ('format_modifier', uint64_t),
]

AVDRMObjectDescriptor = struct_AVDRMObjectDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 66

# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 88
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

AVDRMPlaneDescriptor = struct_AVDRMPlaneDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 88

# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 111
class struct_AVDRMLayerDescriptor(Structure):
    pass

struct_AVDRMLayerDescriptor.__slots__ = [
    'format',
    'nb_planes',
    'planes',
]
struct_AVDRMLayerDescriptor._fields_ = [
    ('format', uint32_t),
    ('nb_planes', c_int),
    ('planes', AVDRMPlaneDescriptor * int(AV_DRM_MAX_PLANES)),
]

AVDRMLayerDescriptor = struct_AVDRMLayerDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 111

# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 150
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

AVDRMFrameDescriptor = struct_AVDRMFrameDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 150

# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 167
class struct_AVDRMDeviceContext(Structure):
    pass

struct_AVDRMDeviceContext.__slots__ = [
    'fd',
]
struct_AVDRMDeviceContext._fields_ = [
    ('fd', c_int),
]

AVDRMDeviceContext = struct_AVDRMDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 167

# /home/josiah/ctypesgen_test/av/av/hwcontext_mediacodec.h: 59
class struct_AVMediaCodecDeviceContext(Structure):
    pass

struct_AVMediaCodecDeviceContext.__slots__ = [
    'surface',
    'native_window',
    'create_window',
]
struct_AVMediaCodecDeviceContext._fields_ = [
    ('surface', POINTER(None)),
    ('native_window', POINTER(None)),
    ('create_window', c_int),
]

AVMediaCodecDeviceContext = struct_AVMediaCodecDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_mediacodec.h: 59

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

# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 56
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

AVOpenCLFrameDescriptor = struct_AVOpenCLFrameDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 56

# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 82
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

AVOpenCLDeviceContext = struct_AVOpenCLDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 82

# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 98
class struct_AVOpenCLFramesContext(Structure):
    pass

struct_AVOpenCLFramesContext.__slots__ = [
    'command_queue',
]
struct_AVOpenCLFramesContext._fields_ = [
    ('command_queue', cl_command_queue),
]

AVOpenCLFramesContext = struct_AVOpenCLFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 98

# /home/josiah/ctypesgen_test/av/av/hwcontext_qsv.h: 47
for _lib in _libs.values():
    try:
        loader = (POINTER(None)).in_dll(_lib, "loader")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/hwcontext_qsv.h: 55
for _lib in _libs.values():
    try:
        nb_surfaces = (c_int).in_dll(_lib, "nb_surfaces")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/hwcontext_qsv.h: 60
for _lib in _libs.values():
    try:
        frame_type = (c_int).in_dll(_lib, "frame_type")
        break
    except:
        pass

VADisplay = POINTER(None)# /usr/include/va/va.h: 259

VAGenericID = c_uint# /usr/include/va/va.h: 1531

VAConfigID = VAGenericID# /usr/include/va/va.h: 1533

VASurfaceID = VAGenericID# /usr/include/va/va.h: 1596

enum_anon_225 = c_int# /usr/include/va/va.h: 1607

VAGenericValueType = enum_anon_225# /usr/include/va/va.h: 1607

VAGenericFunc = CFUNCTYPE(UNCHECKED(None), )# /usr/include/va/va.h: 1610

# /usr/include/va/va.h: 1617
class union_anon_226(Union):
    pass

union_anon_226.__slots__ = [
    'i',
    'f',
    'p',
    'fn',
]
union_anon_226._fields_ = [
    ('i', c_int32),
    ('f', c_float),
    ('p', POINTER(None)),
    ('fn', VAGenericFunc),
]

# /usr/include/va/va.h: 1627
class struct__VAGenericValue(Structure):
    pass

struct__VAGenericValue.__slots__ = [
    'type',
    'value',
]
struct__VAGenericValue._fields_ = [
    ('type', VAGenericValueType),
    ('value', union_anon_226),
]

VAGenericValue = struct__VAGenericValue# /usr/include/va/va.h: 1627

enum_anon_227 = c_int# /usr/include/va/va.h: 1681

VASurfaceAttribType = enum_anon_227# /usr/include/va/va.h: 1681

# /usr/include/va/va.h: 1691
class struct__VASurfaceAttrib(Structure):
    pass

struct__VASurfaceAttrib.__slots__ = [
    'type',
    'flags',
    'value',
]
struct__VASurfaceAttrib._fields_ = [
    ('type', VASurfaceAttribType),
    ('flags', uint32_t),
    ('value', VAGenericValue),
]

VASurfaceAttrib = struct__VASurfaceAttrib# /usr/include/va/va.h: 1691

enum_anon_412 = c_int# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_USER_SET = (1 << 0)# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_RENDER_PARAM_BUFFERS = (1 << 1)# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_ATTRIB_MEMTYPE = (1 << 2)# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 36

AV_VAAPI_DRIVER_QUIRK_SURFACE_ATTRIBUTES = (1 << 3)# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 36

# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 81
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

AVVAAPIDeviceContext = struct_AVVAAPIDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 81

# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 103
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

AVVAAPIFramesContext = struct_AVVAAPIFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 103

# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 115
class struct_AVVAAPIHWConfig(Structure):
    pass

struct_AVVAAPIHWConfig.__slots__ = [
    'config_id',
]
struct_AVVAAPIHWConfig._fields_ = [
    ('config_id', VAConfigID),
]

AVVAAPIHWConfig = struct_AVVAAPIHWConfig# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 115

enum_anon_416 = c_int# /usr/include/vdpau/vdpau.h: 1433

VdpStatus = enum_anon_416# /usr/include/vdpau/vdpau.h: 1433

VdpDevice = uint32_t# /usr/include/vdpau/vdpau.h: 1538

VdpFuncId = uint32_t# /usr/include/vdpau/vdpau.h: 5050

VdpGetProcAddress = CFUNCTYPE(UNCHECKED(VdpStatus), VdpDevice, VdpFuncId, POINTER(POINTER(None)))# /usr/include/vdpau/vdpau.h: 5188

# /home/josiah/ctypesgen_test/av/av/hwcontext_vdpau.h: 38
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

AVVDPAUDeviceContext = struct_AVVDPAUDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vdpau.h: 38

VkBool32 = uint32_t# /usr/include/vulkan/vulkan_core.h: 93

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

enum_VkStructureType = c_int# /usr/include/vulkan/vulkan_core.h: 1197

VkStructureType = enum_VkStructureType# /usr/include/vulkan/vulkan_core.h: 1197

enum_VkImageLayout = c_int# /usr/include/vulkan/vulkan_core.h: 1249

VkImageLayout = enum_VkImageLayout# /usr/include/vulkan/vulkan_core.h: 1249

enum_VkSystemAllocationScope = c_int# /usr/include/vulkan/vulkan_core.h: 1325

VkSystemAllocationScope = enum_VkSystemAllocationScope# /usr/include/vulkan/vulkan_core.h: 1325

enum_VkInternalAllocationType = c_int# /usr/include/vulkan/vulkan_core.h: 1330

VkInternalAllocationType = enum_VkInternalAllocationType# /usr/include/vulkan/vulkan_core.h: 1330

enum_VkFormat = c_int# /usr/include/vulkan/vulkan_core.h: 1636

VkFormat = enum_VkFormat# /usr/include/vulkan/vulkan_core.h: 1636

enum_VkImageTiling = c_int# /usr/include/vulkan/vulkan_core.h: 1643

VkImageTiling = enum_VkImageTiling# /usr/include/vulkan/vulkan_core.h: 1643

enum_VkAccessFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 2101

VkAccessFlagBits = enum_VkAccessFlagBits# /usr/include/vulkan/vulkan_core.h: 2101

enum_VkImageUsageFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 2247

VkImageUsageFlagBits = enum_VkImageUsageFlagBits# /usr/include/vulkan/vulkan_core.h: 2247

enum_VkMemoryPropertyFlagBits = c_int# /usr/include/vulkan/vulkan_core.h: 2275

VkMemoryPropertyFlagBits = enum_VkMemoryPropertyFlagBits# /usr/include/vulkan/vulkan_core.h: 2275

PFN_vkAllocationFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), c_size_t, c_size_t, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2823

PFN_vkFreeFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None))# /usr/include/vulkan/vulkan_core.h: 2829

PFN_vkInternalAllocationNotification = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_size_t, VkInternalAllocationType, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2833

PFN_vkInternalFreeNotification = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_size_t, VkInternalAllocationType, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2839

PFN_vkReallocationFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None), POINTER(None), c_size_t, c_size_t, VkSystemAllocationScope)# /usr/include/vulkan/vulkan_core.h: 2845

PFN_vkVoidFunction = CFUNCTYPE(UNCHECKED(None), )# /usr/include/vulkan/vulkan_core.h: 2852

# /usr/include/vulkan/vulkan_core.h: 2860
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

VkAllocationCallbacks = struct_VkAllocationCallbacks# /usr/include/vulkan/vulkan_core.h: 2860

# /usr/include/vulkan/vulkan_core.h: 2963
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

VkPhysicalDeviceFeatures = struct_VkPhysicalDeviceFeatures# /usr/include/vulkan/vulkan_core.h: 2963

PFN_vkGetInstanceProcAddr = CFUNCTYPE(UNCHECKED(PFN_vkVoidFunction), VkInstance, String)# /usr/include/vulkan/vulkan_core.h: 3849

# /usr/include/vulkan/vulkan_core.h: 5130
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

VkPhysicalDeviceFeatures2 = struct_VkPhysicalDeviceFeatures2# /usr/include/vulkan/vulkan_core.h: 5130

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 138
class struct_AVVulkanDeviceContext(Structure):
    pass

struct_AVVulkanDeviceContext.__slots__ = [
    'alloc',
    'get_proc_addr',
    'inst',
    'phys_dev',
    'act_dev',
    'device_features',
    'enabled_inst_extensions',
    'nb_enabled_inst_extensions',
    'enabled_dev_extensions',
    'nb_enabled_dev_extensions',
    'queue_family_index',
    'nb_graphics_queues',
    'queue_family_tx_index',
    'nb_tx_queues',
    'queue_family_comp_index',
    'nb_comp_queues',
    'queue_family_encode_index',
    'nb_encode_queues',
    'queue_family_decode_index',
    'nb_decode_queues',
]
struct_AVVulkanDeviceContext._fields_ = [
    ('alloc', POINTER(VkAllocationCallbacks)),
    ('get_proc_addr', PFN_vkGetInstanceProcAddr),
    ('inst', VkInstance),
    ('phys_dev', VkPhysicalDevice),
    ('act_dev', VkDevice),
    ('device_features', VkPhysicalDeviceFeatures2),
    ('enabled_inst_extensions', POINTER(POINTER(c_char))),
    ('nb_enabled_inst_extensions', c_int),
    ('enabled_dev_extensions', POINTER(POINTER(c_char))),
    ('nb_enabled_dev_extensions', c_int),
    ('queue_family_index', c_int),
    ('nb_graphics_queues', c_int),
    ('queue_family_tx_index', c_int),
    ('nb_tx_queues', c_int),
    ('queue_family_comp_index', c_int),
    ('nb_comp_queues', c_int),
    ('queue_family_encode_index', c_int),
    ('nb_encode_queues', c_int),
    ('queue_family_decode_index', c_int),
    ('nb_decode_queues', c_int),
]

AVVulkanDeviceContext = struct_AVVulkanDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 138

enum_AVVkFrameFlags = c_int# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 152

AV_VK_FRAME_FLAG_NONE = (1 << 0)# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 152

AV_VK_FRAME_FLAG_CONTIGUOUS_MEMORY = (1 << 1)# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 152

AVVkFrameFlags = enum_AVVkFrameFlags# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 152

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 198
class struct_AVVulkanFramesContext(Structure):
    pass

struct_AVVulkanFramesContext.__slots__ = [
    'tiling',
    'usage',
    'create_pnext',
    'alloc_pnext',
    'flags',
]
struct_AVVulkanFramesContext._fields_ = [
    ('tiling', VkImageTiling),
    ('usage', VkImageUsageFlagBits),
    ('create_pnext', POINTER(None)),
    ('alloc_pnext', POINTER(None) * int(8)),
    ('flags', AVVkFrameFlags),
]

AVVulkanFramesContext = struct_AVVulkanFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 198

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 261
class struct_AVVkFrameInternal(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 267
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
    'sem_value',
    'internal',
    'offset',
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
    ('sem_value', uint64_t * int(8)),
    ('internal', POINTER(struct_AVVkFrameInternal)),
    ('offset', c_ptrdiff_t * int(8)),
]

AVVkFrame = struct_AVVkFrame# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 267

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 273
if _libs["avcodec"].has("av_vk_frame_alloc", "cdecl"):
    av_vk_frame_alloc = _libs["avcodec"].get("av_vk_frame_alloc", "cdecl")
    av_vk_frame_alloc.argtypes = []
    av_vk_frame_alloc.restype = POINTER(AVVkFrame)

# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 279
if _libs["avcodec"].has("av_vkfmt_from_pixfmt", "cdecl"):
    av_vkfmt_from_pixfmt = _libs["avcodec"].get("av_vkfmt_from_pixfmt", "cdecl")
    av_vkfmt_from_pixfmt.argtypes = [enum_AVPixelFormat]
    av_vkfmt_from_pixfmt.restype = POINTER(VkFormat)

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 58
class struct_AVComponentDescriptor(Structure):
    pass

struct_AVComponentDescriptor.__slots__ = [
    'plane',
    'step',
    'offset',
    'shift',
    'depth',
]
struct_AVComponentDescriptor._fields_ = [
    ('plane', c_int),
    ('step', c_int),
    ('offset', c_int),
    ('shift', c_int),
    ('depth', c_int),
]

AVComponentDescriptor = struct_AVComponentDescriptor# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 58

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 111
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
    ('nb_components', uint8_t),
    ('log2_chroma_w', uint8_t),
    ('log2_chroma_h', uint8_t),
    ('flags', uint64_t),
    ('comp', AVComponentDescriptor * int(4)),
    ('alias', String),
]

AVPixFmtDescriptor = struct_AVPixFmtDescriptor# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 111

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 169
if _libs["avcodec"].has("av_get_bits_per_pixel", "cdecl"):
    av_get_bits_per_pixel = _libs["avcodec"].get("av_get_bits_per_pixel", "cdecl")
    av_get_bits_per_pixel.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_get_bits_per_pixel.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 175
if _libs["avcodec"].has("av_get_padded_bits_per_pixel", "cdecl"):
    av_get_padded_bits_per_pixel = _libs["avcodec"].get("av_get_padded_bits_per_pixel", "cdecl")
    av_get_padded_bits_per_pixel.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_get_padded_bits_per_pixel.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 181
if _libs["avcodec"].has("av_pix_fmt_desc_get", "cdecl"):
    av_pix_fmt_desc_get = _libs["avcodec"].get("av_pix_fmt_desc_get", "cdecl")
    av_pix_fmt_desc_get.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_desc_get.restype = POINTER(AVPixFmtDescriptor)

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 190
if _libs["avcodec"].has("av_pix_fmt_desc_next", "cdecl"):
    av_pix_fmt_desc_next = _libs["avcodec"].get("av_pix_fmt_desc_next", "cdecl")
    av_pix_fmt_desc_next.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_pix_fmt_desc_next.restype = POINTER(AVPixFmtDescriptor)

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 196
if _libs["avcodec"].has("av_pix_fmt_desc_get_id", "cdecl"):
    av_pix_fmt_desc_get_id = _libs["avcodec"].get("av_pix_fmt_desc_get_id", "cdecl")
    av_pix_fmt_desc_get_id.argtypes = [POINTER(AVPixFmtDescriptor)]
    av_pix_fmt_desc_get_id.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 208
if _libs["avcodec"].has("av_pix_fmt_get_chroma_sub_sample", "cdecl"):
    av_pix_fmt_get_chroma_sub_sample = _libs["avcodec"].get("av_pix_fmt_get_chroma_sub_sample", "cdecl")
    av_pix_fmt_get_chroma_sub_sample.argtypes = [enum_AVPixelFormat, POINTER(c_int), POINTER(c_int)]
    av_pix_fmt_get_chroma_sub_sample.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 215
if _libs["avcodec"].has("av_pix_fmt_count_planes", "cdecl"):
    av_pix_fmt_count_planes = _libs["avcodec"].get("av_pix_fmt_count_planes", "cdecl")
    av_pix_fmt_count_planes.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_count_planes.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 220
if _libs["avcodec"].has("av_color_range_name", "cdecl"):
    av_color_range_name = _libs["avcodec"].get("av_color_range_name", "cdecl")
    av_color_range_name.argtypes = [enum_AVColorRange]
    av_color_range_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 225
if _libs["avcodec"].has("av_color_range_from_name", "cdecl"):
    av_color_range_from_name = _libs["avcodec"].get("av_color_range_from_name", "cdecl")
    av_color_range_from_name.argtypes = [String]
    av_color_range_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 230
if _libs["avcodec"].has("av_color_primaries_name", "cdecl"):
    av_color_primaries_name = _libs["avcodec"].get("av_color_primaries_name", "cdecl")
    av_color_primaries_name.argtypes = [enum_AVColorPrimaries]
    av_color_primaries_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 235
if _libs["avcodec"].has("av_color_primaries_from_name", "cdecl"):
    av_color_primaries_from_name = _libs["avcodec"].get("av_color_primaries_from_name", "cdecl")
    av_color_primaries_from_name.argtypes = [String]
    av_color_primaries_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 240
if _libs["avcodec"].has("av_color_transfer_name", "cdecl"):
    av_color_transfer_name = _libs["avcodec"].get("av_color_transfer_name", "cdecl")
    av_color_transfer_name.argtypes = [enum_AVColorTransferCharacteristic]
    av_color_transfer_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 245
if _libs["avcodec"].has("av_color_transfer_from_name", "cdecl"):
    av_color_transfer_from_name = _libs["avcodec"].get("av_color_transfer_from_name", "cdecl")
    av_color_transfer_from_name.argtypes = [String]
    av_color_transfer_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 250
if _libs["avcodec"].has("av_color_space_name", "cdecl"):
    av_color_space_name = _libs["avcodec"].get("av_color_space_name", "cdecl")
    av_color_space_name.argtypes = [enum_AVColorSpace]
    av_color_space_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 255
if _libs["avcodec"].has("av_color_space_from_name", "cdecl"):
    av_color_space_from_name = _libs["avcodec"].get("av_color_space_from_name", "cdecl")
    av_color_space_from_name.argtypes = [String]
    av_color_space_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 260
if _libs["avcodec"].has("av_chroma_location_name", "cdecl"):
    av_chroma_location_name = _libs["avcodec"].get("av_chroma_location_name", "cdecl")
    av_chroma_location_name.argtypes = [enum_AVChromaLocation]
    av_chroma_location_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 265
if _libs["avcodec"].has("av_chroma_location_from_name", "cdecl"):
    av_chroma_location_from_name = _libs["avcodec"].get("av_chroma_location_from_name", "cdecl")
    av_chroma_location_from_name.argtypes = [String]
    av_chroma_location_from_name.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 276
if _libs["avcodec"].has("av_chroma_location_enum_to_pos", "cdecl"):
    av_chroma_location_enum_to_pos = _libs["avcodec"].get("av_chroma_location_enum_to_pos", "cdecl")
    av_chroma_location_enum_to_pos.argtypes = [POINTER(c_int), POINTER(c_int), enum_AVChromaLocation]
    av_chroma_location_enum_to_pos.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 287
if _libs["avcodec"].has("av_chroma_location_pos_to_enum", "cdecl"):
    av_chroma_location_pos_to_enum = _libs["avcodec"].get("av_chroma_location_pos_to_enum", "cdecl")
    av_chroma_location_pos_to_enum.argtypes = [c_int, c_int]
    av_chroma_location_pos_to_enum.restype = enum_AVChromaLocation

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 300
if _libs["avcodec"].has("av_get_pix_fmt", "cdecl"):
    av_get_pix_fmt = _libs["avcodec"].get("av_get_pix_fmt", "cdecl")
    av_get_pix_fmt.argtypes = [String]
    av_get_pix_fmt.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 308
if _libs["avcodec"].has("av_get_pix_fmt_name", "cdecl"):
    av_get_pix_fmt_name = _libs["avcodec"].get("av_get_pix_fmt_name", "cdecl")
    av_get_pix_fmt_name.argtypes = [enum_AVPixelFormat]
    av_get_pix_fmt_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 320
if _libs["avcodec"].has("av_get_pix_fmt_string", "cdecl"):
    av_get_pix_fmt_string = _libs["avcodec"].get("av_get_pix_fmt_string", "cdecl")
    av_get_pix_fmt_string.argtypes = [String, c_int, enum_AVPixelFormat]
    if sizeof(c_int) == sizeof(c_void_p):
        av_get_pix_fmt_string.restype = ReturnString
    else:
        av_get_pix_fmt_string.restype = String
        av_get_pix_fmt_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 340
if _libs["avcodec"].has("av_read_image_line2", "cdecl"):
    av_read_image_line2 = _libs["avcodec"].get("av_read_image_line2", "cdecl")
    av_read_image_line2.argtypes = [POINTER(None), POINTER(uint8_t) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int, c_int]
    av_read_image_line2.restype = None

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 345
if _libs["avcodec"].has("av_read_image_line", "cdecl"):
    av_read_image_line = _libs["avcodec"].get("av_read_image_line", "cdecl")
    av_read_image_line.argtypes = [POINTER(uint16_t), POINTER(uint8_t) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int]
    av_read_image_line.restype = None

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 364
if _libs["avcodec"].has("av_write_image_line2", "cdecl"):
    av_write_image_line2 = _libs["avcodec"].get("av_write_image_line2", "cdecl")
    av_write_image_line2.argtypes = [POINTER(None), POINTER(uint8_t) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int, c_int]
    av_write_image_line2.restype = None

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 368
if _libs["avcodec"].has("av_write_image_line", "cdecl"):
    av_write_image_line = _libs["avcodec"].get("av_write_image_line", "cdecl")
    av_write_image_line.argtypes = [POINTER(uint16_t), POINTER(uint8_t) * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor), c_int, c_int, c_int, c_int]
    av_write_image_line.restype = None

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 380
if _libs["avcodec"].has("av_pix_fmt_swap_endianness", "cdecl"):
    av_pix_fmt_swap_endianness = _libs["avcodec"].get("av_pix_fmt_swap_endianness", "cdecl")
    av_pix_fmt_swap_endianness.argtypes = [enum_AVPixelFormat]
    av_pix_fmt_swap_endianness.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 410
if _libs["avcodec"].has("av_get_pix_fmt_loss", "cdecl"):
    av_get_pix_fmt_loss = _libs["avcodec"].get("av_get_pix_fmt_loss", "cdecl")
    av_get_pix_fmt_loss.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, c_int]
    av_get_pix_fmt_loss.restype = c_int

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 432
if _libs["avcodec"].has("av_find_best_pix_fmt_of_2", "cdecl"):
    av_find_best_pix_fmt_of_2 = _libs["avcodec"].get("av_find_best_pix_fmt_of_2", "cdecl")
    av_find_best_pix_fmt_of_2.argtypes = [enum_AVPixelFormat, enum_AVPixelFormat, enum_AVPixelFormat, c_int, POINTER(c_int)]
    av_find_best_pix_fmt_of_2.restype = enum_AVPixelFormat

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 53
if _libs["avcodec"].has("av_image_fill_max_pixsteps", "cdecl"):
    av_image_fill_max_pixsteps = _libs["avcodec"].get("av_image_fill_max_pixsteps", "cdecl")
    av_image_fill_max_pixsteps.argtypes = [c_int * int(4), c_int * int(4), POINTER(AVPixFmtDescriptor)]
    av_image_fill_max_pixsteps.restype = None

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 62
if _libs["avcodec"].has("av_image_get_linesize", "cdecl"):
    av_image_get_linesize = _libs["avcodec"].get("av_image_get_linesize", "cdecl")
    av_image_get_linesize.argtypes = [enum_AVPixelFormat, c_int, c_int]
    av_image_get_linesize.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 73
if _libs["avcodec"].has("av_image_fill_linesizes", "cdecl"):
    av_image_fill_linesizes = _libs["avcodec"].get("av_image_fill_linesizes", "cdecl")
    av_image_fill_linesizes.argtypes = [c_int * int(4), enum_AVPixelFormat, c_int]
    av_image_fill_linesizes.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 88
if _libs["avcodec"].has("av_image_fill_plane_sizes", "cdecl"):
    av_image_fill_plane_sizes = _libs["avcodec"].get("av_image_fill_plane_sizes", "cdecl")
    av_image_fill_plane_sizes.argtypes = [c_size_t * int(4), enum_AVPixelFormat, c_int, c_ptrdiff_t * int(4)]
    av_image_fill_plane_sizes.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 104
if _libs["avcodec"].has("av_image_fill_pointers", "cdecl"):
    av_image_fill_pointers = _libs["avcodec"].get("av_image_fill_pointers", "cdecl")
    av_image_fill_pointers.argtypes = [POINTER(uint8_t) * int(4), enum_AVPixelFormat, c_int, POINTER(uint8_t), c_int * int(4)]
    av_image_fill_pointers.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 122
if _libs["avcodec"].has("av_image_alloc", "cdecl"):
    av_image_alloc = _libs["avcodec"].get("av_image_alloc", "cdecl")
    av_image_alloc.argtypes = [POINTER(uint8_t) * int(4), c_int * int(4), c_int, c_int, enum_AVPixelFormat, c_int]
    av_image_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 140
if _libs["avcodec"].has("av_image_copy_plane", "cdecl"):
    av_image_copy_plane = _libs["avcodec"].get("av_image_copy_plane", "cdecl")
    av_image_copy_plane.argtypes = [POINTER(uint8_t), c_int, POINTER(uint8_t), c_int, c_int, c_int]
    av_image_copy_plane.restype = None

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 158
if _libs["avcodec"].has("av_image_copy_plane_uc_from", "cdecl"):
    av_image_copy_plane_uc_from = _libs["avcodec"].get("av_image_copy_plane_uc_from", "cdecl")
    av_image_copy_plane_uc_from.argtypes = [POINTER(uint8_t), c_ptrdiff_t, POINTER(uint8_t), c_ptrdiff_t, c_ptrdiff_t, c_int]
    av_image_copy_plane_uc_from.restype = None

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 173
if _libs["avcodec"].has("av_image_copy", "cdecl"):
    av_image_copy = _libs["avcodec"].get("av_image_copy", "cdecl")
    av_image_copy.argtypes = [POINTER(uint8_t) * int(4), c_int * int(4), POINTER(uint8_t) * int(4), c_int * int(4), enum_AVPixelFormat, c_int, c_int]
    av_image_copy.restype = None

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 191
if _libs["avcodec"].has("av_image_copy_uc_from", "cdecl"):
    av_image_copy_uc_from = _libs["avcodec"].get("av_image_copy_uc_from", "cdecl")
    av_image_copy_uc_from.argtypes = [POINTER(uint8_t) * int(4), c_ptrdiff_t * int(4), POINTER(uint8_t) * int(4), c_ptrdiff_t * int(4), enum_AVPixelFormat, c_int, c_int]
    av_image_copy_uc_from.restype = None

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 221
if _libs["avcodec"].has("av_image_fill_arrays", "cdecl"):
    av_image_fill_arrays = _libs["avcodec"].get("av_image_fill_arrays", "cdecl")
    av_image_fill_arrays.argtypes = [POINTER(uint8_t) * int(4), c_int * int(4), POINTER(uint8_t), enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_fill_arrays.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 235
if _libs["avcodec"].has("av_image_get_buffer_size", "cdecl"):
    av_image_get_buffer_size = _libs["avcodec"].get("av_image_get_buffer_size", "cdecl")
    av_image_get_buffer_size.argtypes = [enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_get_buffer_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 254
if _libs["avcodec"].has("av_image_copy_to_buffer", "cdecl"):
    av_image_copy_to_buffer = _libs["avcodec"].get("av_image_copy_to_buffer", "cdecl")
    av_image_copy_to_buffer.argtypes = [POINTER(uint8_t), c_int, POINTER(uint8_t) * int(4), c_int * int(4), enum_AVPixelFormat, c_int, c_int, c_int]
    av_image_copy_to_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 268
if _libs["avcodec"].has("av_image_check_size", "cdecl"):
    av_image_check_size = _libs["avcodec"].get("av_image_check_size", "cdecl")
    av_image_check_size.argtypes = [c_uint, c_uint, c_int, POINTER(None)]
    av_image_check_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 283
if _libs["avcodec"].has("av_image_check_size2", "cdecl"):
    av_image_check_size2 = _libs["avcodec"].get("av_image_check_size2", "cdecl")
    av_image_check_size2.argtypes = [c_uint, c_uint, c_int64, enum_AVPixelFormat, c_int, POINTER(None)]
    av_image_check_size2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 297
if _libs["avcodec"].has("av_image_check_sar", "cdecl"):
    av_image_check_sar = _libs["avcodec"].get("av_image_check_sar", "cdecl")
    av_image_check_sar.argtypes = [c_uint, c_uint, AVRational]
    av_image_check_sar.restype = c_int

# /home/josiah/ctypesgen_test/av/av/imgutils.h: 322
if _libs["avcodec"].has("av_image_fill_black", "cdecl"):
    av_image_fill_black = _libs["avcodec"].get("av_image_fill_black", "cdecl")
    av_image_fill_black.argtypes = [POINTER(uint8_t) * int(4), c_ptrdiff_t * int(4), enum_AVPixelFormat, enum_AVColorRange, c_int, c_int]
    av_image_fill_black.restype = c_int

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 34
class union_anon_439(Union):
    pass

union_anon_439.__slots__ = [
    'u64',
    'u32',
    'u16',
    'u8',
    'f64',
    'f32',
]
union_anon_439._fields_ = [
    ('u64', uint64_t),
    ('u32', uint32_t * int(2)),
    ('u16', uint16_t * int(4)),
    ('u8', uint8_t * int(8)),
    ('f64', c_double),
    ('f32', c_float * int(2)),
]

av_alias64 = union_anon_439# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 34

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 41
class union_anon_440(Union):
    pass

union_anon_440.__slots__ = [
    'u32',
    'u16',
    'u8',
    'f32',
]
union_anon_440._fields_ = [
    ('u32', uint32_t),
    ('u16', uint16_t * int(2)),
    ('u8', uint8_t * int(4)),
    ('f32', c_float),
]

av_alias32 = union_anon_440# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 41

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 46
class union_anon_441(Union):
    pass

union_anon_441.__slots__ = [
    'u16',
    'u8',
]
union_anon_441._fields_ = [
    ('u16', uint16_t),
    ('u8', uint8_t * int(2)),
]

av_alias16 = union_anon_441# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 46

# /home/josiah/ctypesgen_test/av/av/jni.h: 36
if _libs["avcodec"].has("av_jni_set_java_vm", "cdecl"):
    av_jni_set_java_vm = _libs["avcodec"].get("av_jni_set_java_vm", "cdecl")
    av_jni_set_java_vm.argtypes = [POINTER(None), POINTER(None)]
    av_jni_set_java_vm.restype = c_int

# /home/josiah/ctypesgen_test/av/av/jni.h: 44
if _libs["avcodec"].has("av_jni_get_java_vm", "cdecl"):
    av_jni_get_java_vm = _libs["avcodec"].get("av_jni_get_java_vm", "cdecl")
    av_jni_get_java_vm.argtypes = [POINTER(None)]
    av_jni_get_java_vm.restype = POINTER(c_ubyte)
    av_jni_get_java_vm.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/av/lfg.h: 36
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

AVLFG = struct_AVLFG# /home/josiah/ctypesgen_test/av/av/lfg.h: 36

# /home/josiah/ctypesgen_test/av/av/lfg.h: 38
if _libs["avcodec"].has("av_lfg_init", "cdecl"):
    av_lfg_init = _libs["avcodec"].get("av_lfg_init", "cdecl")
    av_lfg_init.argtypes = [POINTER(AVLFG), c_uint]
    av_lfg_init.restype = None

# /home/josiah/ctypesgen_test/av/av/lfg.h: 45
if _libs["avcodec"].has("av_lfg_init_from_data", "cdecl"):
    av_lfg_init_from_data = _libs["avcodec"].get("av_lfg_init_from_data", "cdecl")
    av_lfg_init_from_data.argtypes = [POINTER(AVLFG), POINTER(uint8_t), c_uint]
    av_lfg_init_from_data.restype = c_int

# /home/josiah/ctypesgen_test/av/av/lfg.h: 54
for _lib in _libs.values():
    try:
        a = (c_uint).in_dll(_lib, "a")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/lfg.h: 65
for _lib in _libs.values():
    try:
        a = (c_uint).in_dll(_lib, "a")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/lfg.h: 66
for _lib in _libs.values():
    try:
        b = (c_uint).in_dll(_lib, "b")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/lfg.h: 79
if _libs["avcodec"].has("av_bmg_get", "cdecl"):
    av_bmg_get = _libs["avcodec"].get("av_bmg_get", "cdecl")
    av_bmg_get.argtypes = [POINTER(AVLFG), c_double * int(2)]
    av_bmg_get.restype = None

# /home/josiah/ctypesgen_test/av/av/lzo.h: 60
if _libs["avcodec"].has("av_lzo1x_decode", "cdecl"):
    av_lzo1x_decode = _libs["avcodec"].get("av_lzo1x_decode", "cdecl")
    av_lzo1x_decode.argtypes = [POINTER(None), POINTER(c_int), POINTER(None), POINTER(c_int)]
    av_lzo1x_decode.restype = c_int

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 69
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

AVMasteringDisplayMetadata = struct_AVMasteringDisplayMetadata# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 69

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 78
if _libs["avcodec"].has("av_mastering_display_metadata_alloc", "cdecl"):
    av_mastering_display_metadata_alloc = _libs["avcodec"].get("av_mastering_display_metadata_alloc", "cdecl")
    av_mastering_display_metadata_alloc.argtypes = []
    av_mastering_display_metadata_alloc.restype = POINTER(AVMasteringDisplayMetadata)

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 87
if _libs["avcodec"].has("av_mastering_display_metadata_create_side_data", "cdecl"):
    av_mastering_display_metadata_create_side_data = _libs["avcodec"].get("av_mastering_display_metadata_create_side_data", "cdecl")
    av_mastering_display_metadata_create_side_data.argtypes = [POINTER(AVFrame)]
    av_mastering_display_metadata_create_side_data.restype = POINTER(AVMasteringDisplayMetadata)

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 108
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

AVContentLightMetadata = struct_AVContentLightMetadata# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 108

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 117
if _libs["avcodec"].has("av_content_light_metadata_alloc", "cdecl"):
    av_content_light_metadata_alloc = _libs["avcodec"].get("av_content_light_metadata_alloc", "cdecl")
    av_content_light_metadata_alloc.argtypes = [POINTER(c_size_t)]
    av_content_light_metadata_alloc.restype = POINTER(AVContentLightMetadata)

# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 126
if _libs["avcodec"].has("av_content_light_metadata_create_side_data", "cdecl"):
    av_content_light_metadata_create_side_data = _libs["avcodec"].get("av_content_light_metadata_create_side_data", "cdecl")
    av_content_light_metadata_create_side_data.argtypes = [POINTER(AVFrame)]
    av_content_light_metadata_create_side_data.restype = POINTER(AVContentLightMetadata)

# /home/josiah/ctypesgen_test/av/av/md5.h: 43
try:
    av_md5_size = (c_int).in_dll(_libs["avcodec"], "av_md5_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/md5.h: 45
class struct_AVMD5(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/md5.h: 50
if _libs["avcodec"].has("av_md5_alloc", "cdecl"):
    av_md5_alloc = _libs["avcodec"].get("av_md5_alloc", "cdecl")
    av_md5_alloc.argtypes = []
    av_md5_alloc.restype = POINTER(struct_AVMD5)

# /home/josiah/ctypesgen_test/av/av/md5.h: 57
if _libs["avcodec"].has("av_md5_init", "cdecl"):
    av_md5_init = _libs["avcodec"].get("av_md5_init", "cdecl")
    av_md5_init.argtypes = [POINTER(struct_AVMD5)]
    av_md5_init.restype = None

# /home/josiah/ctypesgen_test/av/av/md5.h: 66
if _libs["avcodec"].has("av_md5_update", "cdecl"):
    av_md5_update = _libs["avcodec"].get("av_md5_update", "cdecl")
    av_md5_update.argtypes = [POINTER(struct_AVMD5), POINTER(uint8_t), c_size_t]
    av_md5_update.restype = None

# /home/josiah/ctypesgen_test/av/av/md5.h: 74
if _libs["avcodec"].has("av_md5_final", "cdecl"):
    av_md5_final = _libs["avcodec"].get("av_md5_final", "cdecl")
    av_md5_final.argtypes = [POINTER(struct_AVMD5), POINTER(uint8_t)]
    av_md5_final.restype = None

# /home/josiah/ctypesgen_test/av/av/md5.h: 83
if _libs["avcodec"].has("av_md5_sum", "cdecl"):
    av_md5_sum = _libs["avcodec"].get("av_md5_sum", "cdecl")
    av_md5_sum.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_size_t]
    av_md5_sum.restype = None

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 40
class struct_AVMediaCodecContext(Structure):
    pass

struct_AVMediaCodecContext.__slots__ = [
    'surface',
]
struct_AVMediaCodecContext._fields_ = [
    ('surface', POINTER(None)),
]

AVMediaCodecContext = struct_AVMediaCodecContext# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 40

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 50
if _libs["avcodec"].has("av_mediacodec_alloc_context", "cdecl"):
    av_mediacodec_alloc_context = _libs["avcodec"].get("av_mediacodec_alloc_context", "cdecl")
    av_mediacodec_alloc_context.argtypes = []
    av_mediacodec_alloc_context.restype = POINTER(AVMediaCodecContext)

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 60
if _libs["avcodec"].has("av_mediacodec_default_init", "cdecl"):
    av_mediacodec_default_init = _libs["avcodec"].get("av_mediacodec_default_init", "cdecl")
    av_mediacodec_default_init.argtypes = [POINTER(AVCodecContext), POINTER(AVMediaCodecContext), POINTER(None)]
    av_mediacodec_default_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 68
if _libs["avcodec"].has("av_mediacodec_default_free", "cdecl"):
    av_mediacodec_default_free = _libs["avcodec"].get("av_mediacodec_default_free", "cdecl")
    av_mediacodec_default_free.argtypes = [POINTER(AVCodecContext)]
    av_mediacodec_default_free.restype = None

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 73
class struct_MediaCodecBuffer(Structure):
    pass

AVMediaCodecBuffer = struct_MediaCodecBuffer# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 73

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 86
if _libs["avcodec"].has("av_mediacodec_release_buffer", "cdecl"):
    av_mediacodec_release_buffer = _libs["avcodec"].get("av_mediacodec_release_buffer", "cdecl")
    av_mediacodec_release_buffer.argtypes = [POINTER(AVMediaCodecBuffer), c_int]
    av_mediacodec_release_buffer.restype = c_int

# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 101
if _libs["avcodec"].has("av_mediacodec_render_buffer_at_time", "cdecl"):
    av_mediacodec_render_buffer_at_time = _libs["avcodec"].get("av_mediacodec_render_buffer_at_time", "cdecl")
    av_mediacodec_render_buffer_at_time.argtypes = [POINTER(AVMediaCodecBuffer), c_int64]
    av_mediacodec_render_buffer_at_time.restype = c_int

# /home/josiah/ctypesgen_test/av/av/motion_vector.h: 55
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
    ('w', uint8_t),
    ('h', uint8_t),
    ('src_x', c_int16),
    ('src_y', c_int16),
    ('dst_x', c_int16),
    ('dst_y', c_int16),
    ('flags', uint64_t),
    ('motion_x', c_int32),
    ('motion_y', c_int32),
    ('motion_scale', uint16_t),
]

AVMotionVector = struct_AVMotionVector# /home/josiah/ctypesgen_test/av/av/motion_vector.h: 55

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 67
class struct_AVMurMur3(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 67
if _libs["avcodec"].has("av_murmur3_alloc", "cdecl"):
    av_murmur3_alloc = _libs["avcodec"].get("av_murmur3_alloc", "cdecl")
    av_murmur3_alloc.argtypes = []
    av_murmur3_alloc.restype = POINTER(struct_AVMurMur3)

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 79
if _libs["avcodec"].has("av_murmur3_init_seeded", "cdecl"):
    av_murmur3_init_seeded = _libs["avcodec"].get("av_murmur3_init_seeded", "cdecl")
    av_murmur3_init_seeded.argtypes = [POINTER(struct_AVMurMur3), uint64_t]
    av_murmur3_init_seeded.restype = None

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 92
if _libs["avcodec"].has("av_murmur3_init", "cdecl"):
    av_murmur3_init = _libs["avcodec"].get("av_murmur3_init", "cdecl")
    av_murmur3_init.argtypes = [POINTER(struct_AVMurMur3)]
    av_murmur3_init.restype = None

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 101
if _libs["avcodec"].has("av_murmur3_update", "cdecl"):
    av_murmur3_update = _libs["avcodec"].get("av_murmur3_update", "cdecl")
    av_murmur3_update.argtypes = [POINTER(struct_AVMurMur3), POINTER(uint8_t), c_size_t]
    av_murmur3_update.restype = None

# /home/josiah/ctypesgen_test/av/av/murmur3.h: 109
if _libs["avcodec"].has("av_murmur3_final", "cdecl"):
    av_murmur3_final = _libs["avcodec"].get("av_murmur3_final", "cdecl")
    av_murmur3_final.argtypes = [POINTER(struct_AVMurMur3), uint8_t * int(16)]
    av_murmur3_final.restype = None

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 49
if _libs["avcodec"].has("av_parse_ratio", "cdecl"):
    av_parse_ratio = _libs["avcodec"].get("av_parse_ratio", "cdecl")
    av_parse_ratio.argtypes = [POINTER(AVRational), String, c_int, c_int, POINTER(None)]
    av_parse_ratio.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 66
if _libs["avcodec"].has("av_parse_video_size", "cdecl"):
    av_parse_video_size = _libs["avcodec"].get("av_parse_video_size", "cdecl")
    av_parse_video_size.argtypes = [POINTER(c_int), POINTER(c_int), String]
    av_parse_video_size.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 77
if _libs["avcodec"].has("av_parse_video_rate", "cdecl"):
    av_parse_video_rate = _libs["avcodec"].get("av_parse_video_rate", "cdecl")
    av_parse_video_rate.argtypes = [POINTER(AVRational), String]
    av_parse_video_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 102
if _libs["avcodec"].has("av_parse_color", "cdecl"):
    av_parse_color = _libs["avcodec"].get("av_parse_color", "cdecl")
    av_parse_color.argtypes = [POINTER(uint8_t), String, c_int, POINTER(None)]
    av_parse_color.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 116
if _libs["avcodec"].has("av_get_known_color_name", "cdecl"):
    av_get_known_color_name = _libs["avcodec"].get("av_get_known_color_name", "cdecl")
    av_get_known_color_name.argtypes = [c_int, POINTER(POINTER(uint8_t))]
    av_get_known_color_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 150
if _libs["avcodec"].has("av_parse_time", "cdecl"):
    av_parse_time = _libs["avcodec"].get("av_parse_time", "cdecl")
    av_parse_time.argtypes = [POINTER(c_int64), String, c_int]
    av_parse_time.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 158
if _libs["avcodec"].has("av_find_info_tag", "cdecl"):
    av_find_info_tag = _libs["avcodec"].get("av_find_info_tag", "cdecl")
    av_find_info_tag.argtypes = [String, c_int, String, String]
    av_find_info_tag.restype = c_int

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 190
if _libs["avcodec"].has("av_small_strptime", "cdecl"):
    av_small_strptime = _libs["avcodec"].get("av_small_strptime", "cdecl")
    av_small_strptime.argtypes = [String, String, POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        av_small_strptime.restype = ReturnString
    else:
        av_small_strptime.restype = String
        av_small_strptime.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/parseutils.h: 195
if _libs["avcodec"].has("av_timegm", "cdecl"):
    av_timegm = _libs["avcodec"].get("av_timegm", "cdecl")
    av_timegm.argtypes = [POINTER(struct_tm)]
    av_timegm.restype = time_t

av_pixelutils_sad_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(uint8_t), c_ptrdiff_t, POINTER(uint8_t), c_ptrdiff_t)# /home/josiah/ctypesgen_test/av/av/pixelutils.h: 28

# /home/josiah/ctypesgen_test/av/av/pixelutils.h: 48
if _libs["avcodec"].has("av_pixelutils_get_sad_fn", "cdecl"):
    av_pixelutils_get_sad_fn = _libs["avcodec"].get("av_pixelutils_get_sad_fn", "cdecl")
    av_pixelutils_get_sad_fn.argtypes = [c_int, c_int, c_int, POINTER(None)]
    av_pixelutils_get_sad_fn.restype = av_pixelutils_sad_fn

# /home/josiah/ctypesgen_test/av/av/qsv.h: 46
for _lib in _libs.values():
    try:
        iopattern = (c_int).in_dll(_lib, "iopattern")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/qsv.h: 52
for _lib in _libs.values():
    try:
        nb_ext_buffers = (c_int).in_dll(_lib, "nb_ext_buffers")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/qsv.h: 67
for _lib in _libs.values():
    try:
        opaque_alloc = (c_int).in_dll(_lib, "opaque_alloc")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/qsv.h: 78
for _lib in _libs.values():
    try:
        nb_opaque_surfaces = (c_int).in_dll(_lib, "nb_opaque_surfaces")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/qsv.h: 92
for _lib in _libs.values():
    try:
        opaque_surfaces = (POINTER(AVBufferRef)).in_dll(_lib, "opaque_surfaces")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/qsv.h: 99
for _lib in _libs.values():
    try:
        opaque_alloc_type = (c_int).in_dll(_lib, "opaque_alloc_type")
        break
    except:
        pass

# /home/josiah/ctypesgen_test/av/av/random_seed.h: 37
if _libs["avcodec"].has("av_get_random_seed", "cdecl"):
    av_get_random_seed = _libs["avcodec"].get("av_get_random_seed", "cdecl")
    av_get_random_seed.argtypes = []
    av_get_random_seed.restype = uint32_t

# /home/josiah/ctypesgen_test/av/av/rc4.h: 35
class struct_AVRC4(Structure):
    pass

struct_AVRC4.__slots__ = [
    'state',
    'x',
    'y',
]
struct_AVRC4._fields_ = [
    ('state', uint8_t * int(256)),
    ('x', c_int),
    ('y', c_int),
]

AVRC4 = struct_AVRC4# /home/josiah/ctypesgen_test/av/av/rc4.h: 35

# /home/josiah/ctypesgen_test/av/av/rc4.h: 40
if _libs["avcodec"].has("av_rc4_alloc", "cdecl"):
    av_rc4_alloc = _libs["avcodec"].get("av_rc4_alloc", "cdecl")
    av_rc4_alloc.argtypes = []
    av_rc4_alloc.restype = POINTER(AVRC4)

# /home/josiah/ctypesgen_test/av/av/rc4.h: 51
if _libs["avcodec"].has("av_rc4_init", "cdecl"):
    av_rc4_init = _libs["avcodec"].get("av_rc4_init", "cdecl")
    av_rc4_init.argtypes = [POINTER(struct_AVRC4), POINTER(uint8_t), c_int, c_int]
    av_rc4_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/rc4.h: 63
if _libs["avcodec"].has("av_rc4_crypt", "cdecl"):
    av_rc4_crypt = _libs["avcodec"].get("av_rc4_crypt", "cdecl")
    av_rc4_crypt.argtypes = [POINTER(struct_AVRC4), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_rc4_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/replaygain.h: 48
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
    ('track_peak', uint32_t),
    ('album_gain', c_int32),
    ('album_peak', uint32_t),
]

AVReplayGain = struct_AVReplayGain# /home/josiah/ctypesgen_test/av/av/replaygain.h: 48

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 44
try:
    av_ripemd_size = (c_int).in_dll(_libs["avcodec"], "av_ripemd_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 46
class struct_AVRIPEMD(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 51
if _libs["avcodec"].has("av_ripemd_alloc", "cdecl"):
    av_ripemd_alloc = _libs["avcodec"].get("av_ripemd_alloc", "cdecl")
    av_ripemd_alloc.argtypes = []
    av_ripemd_alloc.restype = POINTER(struct_AVRIPEMD)

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 60
if _libs["avcodec"].has("av_ripemd_init", "cdecl"):
    av_ripemd_init = _libs["avcodec"].get("av_ripemd_init", "cdecl")
    av_ripemd_init.argtypes = [POINTER(struct_AVRIPEMD), c_int]
    av_ripemd_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 69
if _libs["avcodec"].has("av_ripemd_update", "cdecl"):
    av_ripemd_update = _libs["avcodec"].get("av_ripemd_update", "cdecl")
    av_ripemd_update.argtypes = [POINTER(struct_AVRIPEMD), POINTER(uint8_t), c_size_t]
    av_ripemd_update.restype = None

# /home/josiah/ctypesgen_test/av/av/ripemd.h: 77
if _libs["avcodec"].has("av_ripemd_final", "cdecl"):
    av_ripemd_final = _libs["avcodec"].get("av_ripemd_final", "cdecl")
    av_ripemd_final.argtypes = [POINTER(struct_AVRIPEMD), POINTER(uint8_t)]
    av_ripemd_final.restype = None

# /home/josiah/ctypesgen_test/av/av/sha512.h: 53
try:
    av_sha512_size = (c_int).in_dll(_libs["avcodec"], "av_sha512_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/sha512.h: 55
class struct_AVSHA512(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/sha512.h: 60
if _libs["avcodec"].has("av_sha512_alloc", "cdecl"):
    av_sha512_alloc = _libs["avcodec"].get("av_sha512_alloc", "cdecl")
    av_sha512_alloc.argtypes = []
    av_sha512_alloc.restype = POINTER(struct_AVSHA512)

# /home/josiah/ctypesgen_test/av/av/sha512.h: 69
if _libs["avcodec"].has("av_sha512_init", "cdecl"):
    av_sha512_init = _libs["avcodec"].get("av_sha512_init", "cdecl")
    av_sha512_init.argtypes = [POINTER(struct_AVSHA512), c_int]
    av_sha512_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/sha512.h: 78
if _libs["avcodec"].has("av_sha512_update", "cdecl"):
    av_sha512_update = _libs["avcodec"].get("av_sha512_update", "cdecl")
    av_sha512_update.argtypes = [POINTER(struct_AVSHA512), POINTER(uint8_t), c_size_t]
    av_sha512_update.restype = None

# /home/josiah/ctypesgen_test/av/av/sha512.h: 86
if _libs["avcodec"].has("av_sha512_final", "cdecl"):
    av_sha512_final = _libs["avcodec"].get("av_sha512_final", "cdecl")
    av_sha512_final.argtypes = [POINTER(struct_AVSHA512), POINTER(uint8_t)]
    av_sha512_final.restype = None

# /home/josiah/ctypesgen_test/av/av/sha.h: 51
try:
    av_sha_size = (c_int).in_dll(_libs["avcodec"], "av_sha_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/sha.h: 53
class struct_AVSHA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/sha.h: 58
if _libs["avcodec"].has("av_sha_alloc", "cdecl"):
    av_sha_alloc = _libs["avcodec"].get("av_sha_alloc", "cdecl")
    av_sha_alloc.argtypes = []
    av_sha_alloc.restype = POINTER(struct_AVSHA)

# /home/josiah/ctypesgen_test/av/av/sha.h: 67
if _libs["avcodec"].has("av_sha_init", "cdecl"):
    av_sha_init = _libs["avcodec"].get("av_sha_init", "cdecl")
    av_sha_init.argtypes = [POINTER(struct_AVSHA), c_int]
    av_sha_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/sha.h: 76
if _libs["avcodec"].has("av_sha_update", "cdecl"):
    av_sha_update = _libs["avcodec"].get("av_sha_update", "cdecl")
    av_sha_update.argtypes = [POINTER(struct_AVSHA), POINTER(uint8_t), c_size_t]
    av_sha_update.restype = None

# /home/josiah/ctypesgen_test/av/av/sha.h: 84
if _libs["avcodec"].has("av_sha_final", "cdecl"):
    av_sha_final = _libs["avcodec"].get("av_sha_final", "cdecl")
    av_sha_final.argtypes = [POINTER(struct_AVSHA), POINTER(uint8_t)]
    av_sha_final.restype = None

enum_AVSphericalProjection = c_int# /home/josiah/ctypesgen_test/av/av/spherical.h: 47

AV_SPHERICAL_EQUIRECTANGULAR = 0# /home/josiah/ctypesgen_test/av/av/spherical.h: 47

AV_SPHERICAL_CUBEMAP = (AV_SPHERICAL_EQUIRECTANGULAR + 1)# /home/josiah/ctypesgen_test/av/av/spherical.h: 47

AV_SPHERICAL_EQUIRECTANGULAR_TILE = (AV_SPHERICAL_CUBEMAP + 1)# /home/josiah/ctypesgen_test/av/av/spherical.h: 47

# /home/josiah/ctypesgen_test/av/av/spherical.h: 179
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
    ('bound_left', uint32_t),
    ('bound_top', uint32_t),
    ('bound_right', uint32_t),
    ('bound_bottom', uint32_t),
    ('padding', uint32_t),
]

AVSphericalMapping = struct_AVSphericalMapping# /home/josiah/ctypesgen_test/av/av/spherical.h: 179

# /home/josiah/ctypesgen_test/av/av/spherical.h: 187
if _libs["avcodec"].has("av_spherical_alloc", "cdecl"):
    av_spherical_alloc = _libs["avcodec"].get("av_spherical_alloc", "cdecl")
    av_spherical_alloc.argtypes = [POINTER(c_size_t)]
    av_spherical_alloc.restype = POINTER(AVSphericalMapping)

# /home/josiah/ctypesgen_test/av/av/spherical.h: 201
if _libs["avcodec"].has("av_spherical_tile_bounds", "cdecl"):
    av_spherical_tile_bounds = _libs["avcodec"].get("av_spherical_tile_bounds", "cdecl")
    av_spherical_tile_bounds.argtypes = [POINTER(AVSphericalMapping), c_size_t, c_size_t, POINTER(c_size_t), POINTER(c_size_t), POINTER(c_size_t), POINTER(c_size_t)]
    av_spherical_tile_bounds.restype = None

# /home/josiah/ctypesgen_test/av/av/spherical.h: 213
if _libs["avcodec"].has("av_spherical_projection_name", "cdecl"):
    av_spherical_projection_name = _libs["avcodec"].get("av_spherical_projection_name", "cdecl")
    av_spherical_projection_name.argtypes = [enum_AVSphericalProjection]
    av_spherical_projection_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/spherical.h: 222
if _libs["avcodec"].has("av_spherical_from_name", "cdecl"):
    av_spherical_from_name = _libs["avcodec"].get("av_spherical_from_name", "cdecl")
    av_spherical_from_name.argtypes = [String]
    av_spherical_from_name.restype = c_int

enum_AVStereo3DType = c_int# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_2D = 0# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_SIDEBYSIDE = (AV_STEREO3D_2D + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_TOPBOTTOM = (AV_STEREO3D_SIDEBYSIDE + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_FRAMESEQUENCE = (AV_STEREO3D_TOPBOTTOM + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_CHECKERBOARD = (AV_STEREO3D_FRAMESEQUENCE + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_SIDEBYSIDE_QUINCUNX = (AV_STEREO3D_CHECKERBOARD + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_LINES = (AV_STEREO3D_SIDEBYSIDE_QUINCUNX + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

AV_STEREO3D_COLUMNS = (AV_STEREO3D_LINES + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 48

enum_AVStereo3DView = c_int# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 144

AV_STEREO3D_VIEW_PACKED = 0# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 144

AV_STEREO3D_VIEW_LEFT = (AV_STEREO3D_VIEW_PACKED + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 144

AV_STEREO3D_VIEW_RIGHT = (AV_STEREO3D_VIEW_LEFT + 1)# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 144

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 188
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

AVStereo3D = struct_AVStereo3D# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 188

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 196
if _libs["avcodec"].has("av_stereo3d_alloc", "cdecl"):
    av_stereo3d_alloc = _libs["avcodec"].get("av_stereo3d_alloc", "cdecl")
    av_stereo3d_alloc.argtypes = []
    av_stereo3d_alloc.restype = POINTER(AVStereo3D)

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 205
if _libs["avcodec"].has("av_stereo3d_create_side_data", "cdecl"):
    av_stereo3d_create_side_data = _libs["avcodec"].get("av_stereo3d_create_side_data", "cdecl")
    av_stereo3d_create_side_data.argtypes = [POINTER(AVFrame)]
    av_stereo3d_create_side_data.restype = POINTER(AVStereo3D)

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 214
if _libs["avcodec"].has("av_stereo3d_type_name", "cdecl"):
    av_stereo3d_type_name = _libs["avcodec"].get("av_stereo3d_type_name", "cdecl")
    av_stereo3d_type_name.argtypes = [c_uint]
    av_stereo3d_type_name.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 223
if _libs["avcodec"].has("av_stereo3d_from_name", "cdecl"):
    av_stereo3d_from_name = _libs["avcodec"].get("av_stereo3d_from_name", "cdecl")
    av_stereo3d_from_name.argtypes = [String]
    av_stereo3d_from_name.restype = c_int

enum_SwrDitherType = c_int# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NONE = 0# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_RECTANGULAR = (SWR_DITHER_NONE + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_TRIANGULAR = (SWR_DITHER_RECTANGULAR + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_TRIANGULAR_HIGHPASS = (SWR_DITHER_TRIANGULAR + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS = 64# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_LIPSHITZ = (SWR_DITHER_NS + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_F_WEIGHTED = (SWR_DITHER_NS_LIPSHITZ + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_MODIFIED_E_WEIGHTED = (SWR_DITHER_NS_F_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_IMPROVED_E_WEIGHTED = (SWR_DITHER_NS_MODIFIED_E_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_SHIBATA = (SWR_DITHER_NS_IMPROVED_E_WEIGHTED + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_LOW_SHIBATA = (SWR_DITHER_NS_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NS_HIGH_SHIBATA = (SWR_DITHER_NS_LOW_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

SWR_DITHER_NB = (SWR_DITHER_NS_HIGH_SHIBATA + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 148

enum_SwrEngine = c_int# /home/josiah/ctypesgen_test/av/av/swresample.h: 166

SWR_ENGINE_SWR = 0# /home/josiah/ctypesgen_test/av/av/swresample.h: 166

SWR_ENGINE_SOXR = (SWR_ENGINE_SWR + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 166

SWR_ENGINE_NB = (SWR_ENGINE_SOXR + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 166

enum_SwrFilterType = c_int# /home/josiah/ctypesgen_test/av/av/swresample.h: 173

SWR_FILTER_TYPE_CUBIC = 0# /home/josiah/ctypesgen_test/av/av/swresample.h: 173

SWR_FILTER_TYPE_BLACKMAN_NUTTALL = (SWR_FILTER_TYPE_CUBIC + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 173

SWR_FILTER_TYPE_KAISER = (SWR_FILTER_TYPE_BLACKMAN_NUTTALL + 1)# /home/josiah/ctypesgen_test/av/av/swresample.h: 173

# /home/josiah/ctypesgen_test/av/av/swresample.h: 189
class struct_SwrContext(Structure):
    pass

SwrContext = struct_SwrContext# /home/josiah/ctypesgen_test/av/av/swresample.h: 189

# /home/josiah/ctypesgen_test/av/av/swresample.h: 198
if _libs["avcodec"].has("swr_get_class", "cdecl"):
    swr_get_class = _libs["avcodec"].get("swr_get_class", "cdecl")
    swr_get_class.argtypes = []
    swr_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/swresample.h: 214
if _libs["avcodec"].has("swr_alloc", "cdecl"):
    swr_alloc = _libs["avcodec"].get("swr_alloc", "cdecl")
    swr_alloc.argtypes = []
    swr_alloc.restype = POINTER(struct_SwrContext)

# /home/josiah/ctypesgen_test/av/av/swresample.h: 226
if _libs["avcodec"].has("swr_init", "cdecl"):
    swr_init = _libs["avcodec"].get("swr_init", "cdecl")
    swr_init.argtypes = [POINTER(struct_SwrContext)]
    swr_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 235
if _libs["avcodec"].has("swr_is_initialized", "cdecl"):
    swr_is_initialized = _libs["avcodec"].get("swr_is_initialized", "cdecl")
    swr_is_initialized.argtypes = [POINTER(struct_SwrContext)]
    swr_is_initialized.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 260
if _libs["avcodec"].has("swr_alloc_set_opts", "cdecl"):
    swr_alloc_set_opts = _libs["avcodec"].get("swr_alloc_set_opts", "cdecl")
    swr_alloc_set_opts.argtypes = [POINTER(struct_SwrContext), c_int64, enum_AVSampleFormat, c_int, c_int64, enum_AVSampleFormat, c_int, c_int, POINTER(None)]
    swr_alloc_set_opts.restype = POINTER(struct_SwrContext)

# /home/josiah/ctypesgen_test/av/av/swresample.h: 288
if _libs["avcodec"].has("swr_alloc_set_opts2", "cdecl"):
    swr_alloc_set_opts2 = _libs["avcodec"].get("swr_alloc_set_opts2", "cdecl")
    swr_alloc_set_opts2.argtypes = [POINTER(POINTER(struct_SwrContext)), POINTER(AVChannelLayout), enum_AVSampleFormat, c_int, POINTER(AVChannelLayout), enum_AVSampleFormat, c_int, c_int, POINTER(None)]
    swr_alloc_set_opts2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 304
if _libs["avcodec"].has("swr_free", "cdecl"):
    swr_free = _libs["avcodec"].get("swr_free", "cdecl")
    swr_free.argtypes = [POINTER(POINTER(struct_SwrContext))]
    swr_free.restype = None

# /home/josiah/ctypesgen_test/av/av/swresample.h: 316
if _libs["avcodec"].has("swr_close", "cdecl"):
    swr_close = _libs["avcodec"].get("swr_close", "cdecl")
    swr_close.argtypes = [POINTER(struct_SwrContext)]
    swr_close.restype = None

# /home/josiah/ctypesgen_test/av/av/swresample.h: 343
if _libs["avcodec"].has("swr_convert", "cdecl"):
    swr_convert = _libs["avcodec"].get("swr_convert", "cdecl")
    swr_convert.argtypes = [POINTER(struct_SwrContext), POINTER(POINTER(uint8_t)), c_int, POINTER(POINTER(uint8_t)), c_int]
    swr_convert.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 363
if _libs["avcodec"].has("swr_next_pts", "cdecl"):
    swr_next_pts = _libs["avcodec"].get("swr_next_pts", "cdecl")
    swr_next_pts.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_next_pts.restype = c_int64

# /home/josiah/ctypesgen_test/av/av/swresample.h: 390
if _libs["avcodec"].has("swr_set_compensation", "cdecl"):
    swr_set_compensation = _libs["avcodec"].get("swr_set_compensation", "cdecl")
    swr_set_compensation.argtypes = [POINTER(struct_SwrContext), c_int, c_int]
    swr_set_compensation.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 400
if _libs["avcodec"].has("swr_set_channel_mapping", "cdecl"):
    swr_set_channel_mapping = _libs["avcodec"].get("swr_set_channel_mapping", "cdecl")
    swr_set_channel_mapping.argtypes = [POINTER(struct_SwrContext), POINTER(c_int)]
    swr_set_channel_mapping.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 428
if _libs["avcodec"].has("swr_build_matrix", "cdecl"):
    swr_build_matrix = _libs["avcodec"].get("swr_build_matrix", "cdecl")
    swr_build_matrix.argtypes = [uint64_t, uint64_t, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), c_int, enum_AVMatrixEncoding, POINTER(None)]
    swr_build_matrix.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 459
if _libs["avcodec"].has("swr_build_matrix2", "cdecl"):
    swr_build_matrix2 = _libs["avcodec"].get("swr_build_matrix2", "cdecl")
    swr_build_matrix2.argtypes = [POINTER(AVChannelLayout), POINTER(AVChannelLayout), c_double, c_double, c_double, c_double, c_double, POINTER(c_double), c_ptrdiff_t, enum_AVMatrixEncoding, POINTER(None)]
    swr_build_matrix2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 475
if _libs["avcodec"].has("swr_set_matrix", "cdecl"):
    swr_set_matrix = _libs["avcodec"].get("swr_set_matrix", "cdecl")
    swr_set_matrix.argtypes = [POINTER(struct_SwrContext), POINTER(c_double), c_int]
    swr_set_matrix.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 495
if _libs["avcodec"].has("swr_drop_output", "cdecl"):
    swr_drop_output = _libs["avcodec"].get("swr_drop_output", "cdecl")
    swr_drop_output.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_drop_output.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 508
if _libs["avcodec"].has("swr_inject_silence", "cdecl"):
    swr_inject_silence = _libs["avcodec"].get("swr_inject_silence", "cdecl")
    swr_inject_silence.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_inject_silence.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 534
if _libs["avcodec"].has("swr_get_delay", "cdecl"):
    swr_get_delay = _libs["avcodec"].get("swr_get_delay", "cdecl")
    swr_get_delay.argtypes = [POINTER(struct_SwrContext), c_int64]
    swr_get_delay.restype = c_int64

# /home/josiah/ctypesgen_test/av/av/swresample.h: 552
if _libs["avcodec"].has("swr_get_out_samples", "cdecl"):
    swr_get_out_samples = _libs["avcodec"].get("swr_get_out_samples", "cdecl")
    swr_get_out_samples.argtypes = [POINTER(struct_SwrContext), c_int]
    swr_get_out_samples.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 569
if _libs["avcodec"].has("swresample_version", "cdecl"):
    swresample_version = _libs["avcodec"].get("swresample_version", "cdecl")
    swresample_version.argtypes = []
    swresample_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/swresample.h: 576
if _libs["avcodec"].has("swresample_configuration", "cdecl"):
    swresample_configuration = _libs["avcodec"].get("swresample_configuration", "cdecl")
    swresample_configuration.argtypes = []
    swresample_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/swresample.h: 583
if _libs["avcodec"].has("swresample_license", "cdecl"):
    swresample_license = _libs["avcodec"].get("swresample_license", "cdecl")
    swresample_license.argtypes = []
    swresample_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/swresample.h: 626
if _libs["avcodec"].has("swr_convert_frame", "cdecl"):
    swr_convert_frame = _libs["avcodec"].get("swr_convert_frame", "cdecl")
    swr_convert_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_convert_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swresample.h: 643
if _libs["avcodec"].has("swr_config_frame", "cdecl"):
    swr_config_frame = _libs["avcodec"].get("swr_config_frame", "cdecl")
    swr_config_frame.argtypes = [POINTER(SwrContext), POINTER(AVFrame), POINTER(AVFrame)]
    swr_config_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 52
if _libs["avdevice"].has("swscale_version", "cdecl"):
    swscale_version = _libs["avdevice"].get("swscale_version", "cdecl")
    swscale_version.argtypes = []
    swscale_version.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/swscale.h: 57
if _libs["avdevice"].has("swscale_configuration", "cdecl"):
    swscale_configuration = _libs["avdevice"].get("swscale_configuration", "cdecl")
    swscale_configuration.argtypes = []
    swscale_configuration.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/swscale.h: 62
if _libs["avdevice"].has("swscale_license", "cdecl"):
    swscale_license = _libs["avdevice"].get("swscale_license", "cdecl")
    swscale_license.argtypes = []
    swscale_license.restype = c_char_p

# /home/josiah/ctypesgen_test/av/av/swscale.h: 112
if _libs["avdevice"].has("sws_getCoefficients", "cdecl"):
    sws_getCoefficients = _libs["avdevice"].get("sws_getCoefficients", "cdecl")
    sws_getCoefficients.argtypes = [c_int]
    sws_getCoefficients.restype = POINTER(c_int)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 119
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

SwsVector = struct_SwsVector# /home/josiah/ctypesgen_test/av/av/swscale.h: 119

# /home/josiah/ctypesgen_test/av/av/swscale.h: 127
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

SwsFilter = struct_SwsFilter# /home/josiah/ctypesgen_test/av/av/swscale.h: 127

# /home/josiah/ctypesgen_test/av/av/swscale.h: 129
class struct_SwsContext(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 135
if _libs["avdevice"].has("sws_isSupportedInput", "cdecl"):
    sws_isSupportedInput = _libs["avdevice"].get("sws_isSupportedInput", "cdecl")
    sws_isSupportedInput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedInput.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 141
if _libs["avdevice"].has("sws_isSupportedOutput", "cdecl"):
    sws_isSupportedOutput = _libs["avdevice"].get("sws_isSupportedOutput", "cdecl")
    sws_isSupportedOutput.argtypes = [enum_AVPixelFormat]
    sws_isSupportedOutput.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 148
if _libs["avdevice"].has("sws_isSupportedEndiannessConversion", "cdecl"):
    sws_isSupportedEndiannessConversion = _libs["avdevice"].get("sws_isSupportedEndiannessConversion", "cdecl")
    sws_isSupportedEndiannessConversion.argtypes = [enum_AVPixelFormat]
    sws_isSupportedEndiannessConversion.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 155
if _libs["avdevice"].has("sws_alloc_context", "cdecl"):
    sws_alloc_context = _libs["avdevice"].get("sws_alloc_context", "cdecl")
    sws_alloc_context.argtypes = []
    sws_alloc_context.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 164
if _libs["avdevice"].has("sws_init_context", "cdecl"):
    sws_init_context = _libs["avdevice"].get("sws_init_context", "cdecl")
    sws_init_context.argtypes = [POINTER(struct_SwsContext), POINTER(SwsFilter), POINTER(SwsFilter)]
    sws_init_context.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 170
if _libs["avdevice"].has("sws_freeContext", "cdecl"):
    sws_freeContext = _libs["avdevice"].get("sws_freeContext", "cdecl")
    sws_freeContext.argtypes = [POINTER(struct_SwsContext)]
    sws_freeContext.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 193
if _libs["avdevice"].has("sws_getContext", "cdecl"):
    sws_getContext = _libs["avdevice"].get("sws_getContext", "cdecl")
    sws_getContext.argtypes = [c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getContext.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 224
if _libs["avdevice"].has("sws_scale", "cdecl"):
    sws_scale = _libs["avdevice"].get("sws_scale", "cdecl")
    sws_scale.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, POINTER(POINTER(uint8_t)), POINTER(c_int)]
    sws_scale.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 244
if _libs["avdevice"].has("sws_scale_frame", "cdecl"):
    sws_scale_frame = _libs["avdevice"].get("sws_scale_frame", "cdecl")
    sws_scale_frame.argtypes = [POINTER(struct_SwsContext), POINTER(AVFrame), POINTER(AVFrame)]
    sws_scale_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 271
if _libs["avdevice"].has("sws_frame_start", "cdecl"):
    sws_frame_start = _libs["avdevice"].get("sws_frame_start", "cdecl")
    sws_frame_start.argtypes = [POINTER(struct_SwsContext), POINTER(AVFrame), POINTER(AVFrame)]
    sws_frame_start.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 281
if _libs["avdevice"].has("sws_frame_end", "cdecl"):
    sws_frame_end = _libs["avdevice"].get("sws_frame_end", "cdecl")
    sws_frame_end.argtypes = [POINTER(struct_SwsContext)]
    sws_frame_end.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 295
if _libs["avdevice"].has("sws_send_slice", "cdecl"):
    sws_send_slice = _libs["avdevice"].get("sws_send_slice", "cdecl")
    sws_send_slice.argtypes = [POINTER(struct_SwsContext), c_uint, c_uint]
    sws_send_slice.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 315
if _libs["avdevice"].has("sws_receive_slice", "cdecl"):
    sws_receive_slice = _libs["avdevice"].get("sws_receive_slice", "cdecl")
    sws_receive_slice.argtypes = [POINTER(struct_SwsContext), c_uint, c_uint]
    sws_receive_slice.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 326
if _libs["avdevice"].has("sws_receive_slice_alignment", "cdecl"):
    sws_receive_slice_alignment = _libs["avdevice"].get("sws_receive_slice_alignment", "cdecl")
    sws_receive_slice_alignment.argtypes = [POINTER(struct_SwsContext)]
    sws_receive_slice_alignment.restype = c_uint

# /home/josiah/ctypesgen_test/av/av/swscale.h: 341
if _libs["avdevice"].has("sws_setColorspaceDetails", "cdecl"):
    sws_setColorspaceDetails = _libs["avdevice"].get("sws_setColorspaceDetails", "cdecl")
    sws_setColorspaceDetails.argtypes = [POINTER(struct_SwsContext), c_int * int(4), c_int, c_int * int(4), c_int, c_int, c_int, c_int]
    sws_setColorspaceDetails.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 349
if _libs["avdevice"].has("sws_getColorspaceDetails", "cdecl"):
    sws_getColorspaceDetails = _libs["avdevice"].get("sws_getColorspaceDetails", "cdecl")
    sws_getColorspaceDetails.argtypes = [POINTER(struct_SwsContext), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    sws_getColorspaceDetails.restype = c_int

# /home/josiah/ctypesgen_test/av/av/swscale.h: 356
if _libs["avdevice"].has("sws_allocVec", "cdecl"):
    sws_allocVec = _libs["avdevice"].get("sws_allocVec", "cdecl")
    sws_allocVec.argtypes = [c_int]
    sws_allocVec.restype = POINTER(SwsVector)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 362
if _libs["avdevice"].has("sws_getGaussianVec", "cdecl"):
    sws_getGaussianVec = _libs["avdevice"].get("sws_getGaussianVec", "cdecl")
    sws_getGaussianVec.argtypes = [c_double, c_double]
    sws_getGaussianVec.restype = POINTER(SwsVector)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 367
if _libs["avdevice"].has("sws_scaleVec", "cdecl"):
    sws_scaleVec = _libs["avdevice"].get("sws_scaleVec", "cdecl")
    sws_scaleVec.argtypes = [POINTER(SwsVector), c_double]
    sws_scaleVec.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 372
if _libs["avdevice"].has("sws_normalizeVec", "cdecl"):
    sws_normalizeVec = _libs["avdevice"].get("sws_normalizeVec", "cdecl")
    sws_normalizeVec.argtypes = [POINTER(SwsVector), c_double]
    sws_normalizeVec.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 374
if _libs["avdevice"].has("sws_freeVec", "cdecl"):
    sws_freeVec = _libs["avdevice"].get("sws_freeVec", "cdecl")
    sws_freeVec.argtypes = [POINTER(SwsVector)]
    sws_freeVec.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 376
if _libs["avdevice"].has("sws_getDefaultFilter", "cdecl"):
    sws_getDefaultFilter = _libs["avdevice"].get("sws_getDefaultFilter", "cdecl")
    sws_getDefaultFilter.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_int]
    sws_getDefaultFilter.restype = POINTER(SwsFilter)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 380
if _libs["avdevice"].has("sws_freeFilter", "cdecl"):
    sws_freeFilter = _libs["avdevice"].get("sws_freeFilter", "cdecl")
    sws_freeFilter.argtypes = [POINTER(SwsFilter)]
    sws_freeFilter.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 394
if _libs["avdevice"].has("sws_getCachedContext", "cdecl"):
    sws_getCachedContext = _libs["avdevice"].get("sws_getCachedContext", "cdecl")
    sws_getCachedContext.argtypes = [POINTER(struct_SwsContext), c_int, c_int, enum_AVPixelFormat, c_int, c_int, enum_AVPixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
    sws_getCachedContext.restype = POINTER(struct_SwsContext)

# /home/josiah/ctypesgen_test/av/av/swscale.h: 410
if _libs["avdevice"].has("sws_convertPalette8ToPacked32", "cdecl"):
    sws_convertPalette8ToPacked32 = _libs["avdevice"].get("sws_convertPalette8ToPacked32", "cdecl")
    sws_convertPalette8ToPacked32.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t)]
    sws_convertPalette8ToPacked32.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 422
if _libs["avdevice"].has("sws_convertPalette8ToPacked24", "cdecl"):
    sws_convertPalette8ToPacked24 = _libs["avdevice"].get("sws_convertPalette8ToPacked24", "cdecl")
    sws_convertPalette8ToPacked24.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t)]
    sws_convertPalette8ToPacked24.restype = None

# /home/josiah/ctypesgen_test/av/av/swscale.h: 430
if _libs["avdevice"].has("sws_get_class", "cdecl"):
    sws_get_class = _libs["avdevice"].get("sws_get_class", "cdecl")
    sws_get_class.argtypes = []
    sws_get_class.restype = POINTER(AVClass)

# /home/josiah/ctypesgen_test/av/av/tea.h: 35
try:
    av_tea_size = (c_int).in_dll(_libs["avcodec"], "av_tea_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/tea.h: 37
class struct_AVTEA(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/tea.h: 43
if _libs["avcodec"].has("av_tea_alloc", "cdecl"):
    av_tea_alloc = _libs["avcodec"].get("av_tea_alloc", "cdecl")
    av_tea_alloc.argtypes = []
    av_tea_alloc.restype = POINTER(struct_AVTEA)

# /home/josiah/ctypesgen_test/av/av/tea.h: 52
if _libs["avcodec"].has("av_tea_init", "cdecl"):
    av_tea_init = _libs["avcodec"].get("av_tea_init", "cdecl")
    av_tea_init.argtypes = [POINTER(struct_AVTEA), uint8_t * int(16), c_int]
    av_tea_init.restype = None

# /home/josiah/ctypesgen_test/av/av/tea.h: 64
if _libs["avcodec"].has("av_tea_crypt", "cdecl"):
    av_tea_crypt = _libs["avcodec"].get("av_tea_crypt", "cdecl")
    av_tea_crypt.argtypes = [POINTER(struct_AVTEA), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_tea_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 22
class struct_AVThreadMessageQueue(Structure):
    pass

AVThreadMessageQueue = struct_AVThreadMessageQueue# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 22

enum_AVThreadMessageFlags = c_int# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 33

AV_THREAD_MESSAGE_NONBLOCK = 1# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 33

AVThreadMessageFlags = enum_AVThreadMessageFlags# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 33

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 44
if _libs["avcodec"].has("av_thread_message_queue_alloc", "cdecl"):
    av_thread_message_queue_alloc = _libs["avcodec"].get("av_thread_message_queue_alloc", "cdecl")
    av_thread_message_queue_alloc.argtypes = [POINTER(POINTER(AVThreadMessageQueue)), c_uint, c_uint]
    av_thread_message_queue_alloc.restype = c_int

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 53
if _libs["avcodec"].has("av_thread_message_queue_free", "cdecl"):
    av_thread_message_queue_free = _libs["avcodec"].get("av_thread_message_queue_free", "cdecl")
    av_thread_message_queue_free.argtypes = [POINTER(POINTER(AVThreadMessageQueue))]
    av_thread_message_queue_free.restype = None

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 58
if _libs["avcodec"].has("av_thread_message_queue_send", "cdecl"):
    av_thread_message_queue_send = _libs["avcodec"].get("av_thread_message_queue_send", "cdecl")
    av_thread_message_queue_send.argtypes = [POINTER(AVThreadMessageQueue), POINTER(None), c_uint]
    av_thread_message_queue_send.restype = c_int

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 65
if _libs["avcodec"].has("av_thread_message_queue_recv", "cdecl"):
    av_thread_message_queue_recv = _libs["avcodec"].get("av_thread_message_queue_recv", "cdecl")
    av_thread_message_queue_recv.argtypes = [POINTER(AVThreadMessageQueue), POINTER(None), c_uint]
    av_thread_message_queue_recv.restype = c_int

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 77
if _libs["avcodec"].has("av_thread_message_queue_set_err_send", "cdecl"):
    av_thread_message_queue_set_err_send = _libs["avcodec"].get("av_thread_message_queue_set_err_send", "cdecl")
    av_thread_message_queue_set_err_send.argtypes = [POINTER(AVThreadMessageQueue), c_int]
    av_thread_message_queue_set_err_send.restype = None

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 88
if _libs["avcodec"].has("av_thread_message_queue_set_err_recv", "cdecl"):
    av_thread_message_queue_set_err_recv = _libs["avcodec"].get("av_thread_message_queue_set_err_recv", "cdecl")
    av_thread_message_queue_set_err_recv.argtypes = [POINTER(AVThreadMessageQueue), c_int]
    av_thread_message_queue_set_err_recv.restype = None

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 95
if _libs["avcodec"].has("av_thread_message_queue_set_free_func", "cdecl"):
    av_thread_message_queue_set_free_func = _libs["avcodec"].get("av_thread_message_queue_set_free_func", "cdecl")
    av_thread_message_queue_set_free_func.argtypes = [POINTER(AVThreadMessageQueue), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    av_thread_message_queue_set_free_func.restype = None

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 104
if _libs["avcodec"].has("av_thread_message_queue_nb_elems", "cdecl"):
    av_thread_message_queue_nb_elems = _libs["avcodec"].get("av_thread_message_queue_nb_elems", "cdecl")
    av_thread_message_queue_nb_elems.argtypes = [POINTER(AVThreadMessageQueue)]
    av_thread_message_queue_nb_elems.restype = c_int

# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 113
if _libs["avcodec"].has("av_thread_message_flush", "cdecl"):
    av_thread_message_flush = _libs["avcodec"].get("av_thread_message_flush", "cdecl")
    av_thread_message_flush.argtypes = [POINTER(AVThreadMessageQueue)]
    av_thread_message_flush.restype = None

enum_AVTimecodeFlag = c_int# /home/josiah/ctypesgen_test/av/av/timecode.h: 35

AV_TIMECODE_FLAG_DROPFRAME = (1 << 0)# /home/josiah/ctypesgen_test/av/av/timecode.h: 35

AV_TIMECODE_FLAG_24HOURSMAX = (1 << 1)# /home/josiah/ctypesgen_test/av/av/timecode.h: 35

AV_TIMECODE_FLAG_ALLOWNEGATIVE = (1 << 2)# /home/josiah/ctypesgen_test/av/av/timecode.h: 35

# /home/josiah/ctypesgen_test/av/av/timecode.h: 46
class struct_anon_442(Structure):
    pass

struct_anon_442.__slots__ = [
    'start',
    'flags',
    'rate',
    'fps',
]
struct_anon_442._fields_ = [
    ('start', c_int),
    ('flags', uint32_t),
    ('rate', AVRational),
    ('fps', c_uint),
]

AVTimecode = struct_anon_442# /home/josiah/ctypesgen_test/av/av/timecode.h: 46

# /home/josiah/ctypesgen_test/av/av/timecode.h: 56
if _libs["avcodec"].has("av_timecode_adjust_ntsc_framenum2", "cdecl"):
    av_timecode_adjust_ntsc_framenum2 = _libs["avcodec"].get("av_timecode_adjust_ntsc_framenum2", "cdecl")
    av_timecode_adjust_ntsc_framenum2.argtypes = [c_int, c_int]
    av_timecode_adjust_ntsc_framenum2.restype = c_int

# /home/josiah/ctypesgen_test/av/av/timecode.h: 83
if _libs["avcodec"].has("av_timecode_get_smpte_from_framenum", "cdecl"):
    av_timecode_get_smpte_from_framenum = _libs["avcodec"].get("av_timecode_get_smpte_from_framenum", "cdecl")
    av_timecode_get_smpte_from_framenum.argtypes = [POINTER(AVTimecode), c_int]
    av_timecode_get_smpte_from_framenum.restype = uint32_t

# /home/josiah/ctypesgen_test/av/av/timecode.h: 96
if _libs["avcodec"].has("av_timecode_get_smpte", "cdecl"):
    av_timecode_get_smpte = _libs["avcodec"].get("av_timecode_get_smpte", "cdecl")
    av_timecode_get_smpte.argtypes = [AVRational, c_int, c_int, c_int, c_int, c_int]
    av_timecode_get_smpte.restype = uint32_t

# /home/josiah/ctypesgen_test/av/av/timecode.h: 110
if _libs["avcodec"].has("av_timecode_make_string", "cdecl"):
    av_timecode_make_string = _libs["avcodec"].get("av_timecode_make_string", "cdecl")
    av_timecode_make_string.argtypes = [POINTER(AVTimecode), String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_string.restype = ReturnString
    else:
        av_timecode_make_string.restype = String
        av_timecode_make_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/timecode.h: 127
if _libs["avcodec"].has("av_timecode_make_smpte_tc_string2", "cdecl"):
    av_timecode_make_smpte_tc_string2 = _libs["avcodec"].get("av_timecode_make_smpte_tc_string2", "cdecl")
    av_timecode_make_smpte_tc_string2.argtypes = [String, AVRational, uint32_t, c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_smpte_tc_string2.restype = ReturnString
    else:
        av_timecode_make_smpte_tc_string2.restype = String
        av_timecode_make_smpte_tc_string2.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/timecode.h: 138
if _libs["avcodec"].has("av_timecode_make_smpte_tc_string", "cdecl"):
    av_timecode_make_smpte_tc_string = _libs["avcodec"].get("av_timecode_make_smpte_tc_string", "cdecl")
    av_timecode_make_smpte_tc_string.argtypes = [String, uint32_t, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_smpte_tc_string.restype = ReturnString
    else:
        av_timecode_make_smpte_tc_string.restype = String
        av_timecode_make_smpte_tc_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/timecode.h: 147
if _libs["avcodec"].has("av_timecode_make_mpeg_tc_string", "cdecl"):
    av_timecode_make_mpeg_tc_string = _libs["avcodec"].get("av_timecode_make_mpeg_tc_string", "cdecl")
    av_timecode_make_mpeg_tc_string.argtypes = [String, uint32_t]
    if sizeof(c_int) == sizeof(c_void_p):
        av_timecode_make_mpeg_tc_string.restype = ReturnString
    else:
        av_timecode_make_mpeg_tc_string.restype = String
        av_timecode_make_mpeg_tc_string.errcheck = ReturnString

# /home/josiah/ctypesgen_test/av/av/timecode.h: 161
if _libs["avcodec"].has("av_timecode_init", "cdecl"):
    av_timecode_init = _libs["avcodec"].get("av_timecode_init", "cdecl")
    av_timecode_init.argtypes = [POINTER(AVTimecode), AVRational, c_int, c_int, POINTER(None)]
    av_timecode_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/timecode.h: 178
if _libs["avcodec"].has("av_timecode_init_from_components", "cdecl"):
    av_timecode_init_from_components = _libs["avcodec"].get("av_timecode_init_from_components", "cdecl")
    av_timecode_init_from_components.argtypes = [POINTER(AVTimecode), AVRational, c_int, c_int, c_int, c_int, c_int, POINTER(None)]
    av_timecode_init_from_components.restype = c_int

# /home/josiah/ctypesgen_test/av/av/timecode.h: 190
if _libs["avcodec"].has("av_timecode_init_from_string", "cdecl"):
    av_timecode_init_from_string = _libs["avcodec"].get("av_timecode_init_from_string", "cdecl")
    av_timecode_init_from_string.argtypes = [POINTER(AVTimecode), AVRational, String, POINTER(None)]
    av_timecode_init_from_string.restype = c_int

# /home/josiah/ctypesgen_test/av/av/timecode.h: 197
if _libs["avcodec"].has("av_timecode_check_frame_rate", "cdecl"):
    av_timecode_check_frame_rate = _libs["avcodec"].get("av_timecode_check_frame_rate", "cdecl")
    av_timecode_check_frame_rate.argtypes = [AVRational]
    av_timecode_check_frame_rate.restype = c_int

# /home/josiah/ctypesgen_test/av/av/time.h: 29
if _libs["avcodec"].has("av_gettime", "cdecl"):
    av_gettime = _libs["avcodec"].get("av_gettime", "cdecl")
    av_gettime.argtypes = []
    av_gettime.restype = c_int64

# /home/josiah/ctypesgen_test/av/av/time.h: 38
if _libs["avcodec"].has("av_gettime_relative", "cdecl"):
    av_gettime_relative = _libs["avcodec"].get("av_gettime_relative", "cdecl")
    av_gettime_relative.argtypes = []
    av_gettime_relative.restype = c_int64

# /home/josiah/ctypesgen_test/av/av/time.h: 44
if _libs["avcodec"].has("av_gettime_relative_is_monotonic", "cdecl"):
    av_gettime_relative_is_monotonic = _libs["avcodec"].get("av_gettime_relative_is_monotonic", "cdecl")
    av_gettime_relative_is_monotonic.argtypes = []
    av_gettime_relative_is_monotonic.restype = c_int

# /home/josiah/ctypesgen_test/av/av/time.h: 54
if _libs["avcodec"].has("av_usleep", "cdecl"):
    av_usleep = _libs["avcodec"].get("av_usleep", "cdecl")
    av_usleep.argtypes = [c_uint]
    av_usleep.restype = c_int

# /home/josiah/ctypesgen_test/av/av/tree.h: 44
class struct_AVTreeNode(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/tree.h: 45
try:
    av_tree_node_size = (c_int).in_dll(_libs["avcodec"], "av_tree_node_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/tree.h: 50
if _libs["avcodec"].has("av_tree_node_alloc", "cdecl"):
    av_tree_node_alloc = _libs["avcodec"].get("av_tree_node_alloc", "cdecl")
    av_tree_node_alloc.argtypes = []
    av_tree_node_alloc.restype = POINTER(struct_AVTreeNode)

# /home/josiah/ctypesgen_test/av/av/tree.h: 66
if _libs["avcodec"].has("av_tree_find", "cdecl"):
    av_tree_find = _libs["avcodec"].get("av_tree_find", "cdecl")
    av_tree_find.argtypes = [POINTER(struct_AVTreeNode), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), POINTER(None) * int(2)]
    av_tree_find.restype = POINTER(c_ubyte)
    av_tree_find.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/av/tree.h: 113
if _libs["avcodec"].has("av_tree_insert", "cdecl"):
    av_tree_insert = _libs["avcodec"].get("av_tree_insert", "cdecl")
    av_tree_insert.argtypes = [POINTER(POINTER(struct_AVTreeNode)), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), POINTER(POINTER(struct_AVTreeNode))]
    av_tree_insert.restype = POINTER(c_ubyte)
    av_tree_insert.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/josiah/ctypesgen_test/av/av/tree.h: 117
if _libs["avcodec"].has("av_tree_destroy", "cdecl"):
    av_tree_destroy = _libs["avcodec"].get("av_tree_destroy", "cdecl")
    av_tree_destroy.argtypes = [POINTER(struct_AVTreeNode)]
    av_tree_destroy.restype = None

# /home/josiah/ctypesgen_test/av/av/tree.h: 129
if _libs["avcodec"].has("av_tree_enumerate", "cdecl"):
    av_tree_enumerate = _libs["avcodec"].get("av_tree_enumerate", "cdecl")
    av_tree_enumerate.argtypes = [POINTER(struct_AVTreeNode), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    av_tree_enumerate.restype = None

# /home/josiah/ctypesgen_test/av/av/twofish.h: 36
try:
    av_twofish_size = (c_int).in_dll(_libs["avcodec"], "av_twofish_size")
except:
    pass

# /home/josiah/ctypesgen_test/av/av/twofish.h: 38
class struct_AVTWOFISH(Structure):
    pass

# /home/josiah/ctypesgen_test/av/av/twofish.h: 44
if _libs["avcodec"].has("av_twofish_alloc", "cdecl"):
    av_twofish_alloc = _libs["avcodec"].get("av_twofish_alloc", "cdecl")
    av_twofish_alloc.argtypes = []
    av_twofish_alloc.restype = POINTER(struct_AVTWOFISH)

# /home/josiah/ctypesgen_test/av/av/twofish.h: 53
if _libs["avcodec"].has("av_twofish_init", "cdecl"):
    av_twofish_init = _libs["avcodec"].get("av_twofish_init", "cdecl")
    av_twofish_init.argtypes = [POINTER(struct_AVTWOFISH), POINTER(uint8_t), c_int]
    av_twofish_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/twofish.h: 65
if _libs["avcodec"].has("av_twofish_crypt", "cdecl"):
    av_twofish_crypt = _libs["avcodec"].get("av_twofish_crypt", "cdecl")
    av_twofish_crypt.argtypes = [POINTER(struct_AVTWOFISH), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_twofish_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/tx.h: 25
class struct_AVTXContext(Structure):
    pass

AVTXContext = struct_AVTXContext# /home/josiah/ctypesgen_test/av/av/tx.h: 25

# /home/josiah/ctypesgen_test/av/av/tx.h: 29
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

AVComplexFloat = struct_AVComplexFloat# /home/josiah/ctypesgen_test/av/av/tx.h: 29

# /home/josiah/ctypesgen_test/av/av/tx.h: 33
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

AVComplexDouble = struct_AVComplexDouble# /home/josiah/ctypesgen_test/av/av/tx.h: 33

# /home/josiah/ctypesgen_test/av/av/tx.h: 37
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

AVComplexInt32 = struct_AVComplexInt32# /home/josiah/ctypesgen_test/av/av/tx.h: 37

enum_AVTXType = c_int# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_FLOAT_FFT = 0# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_DOUBLE_FFT = 2# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_INT32_FFT = 4# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_FLOAT_MDCT = 1# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_DOUBLE_MDCT = 3# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_INT32_MDCT = 5# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_FLOAT_RDFT = 6# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_DOUBLE_RDFT = 7# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_INT32_RDFT = 8# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_FLOAT_DCT = 9# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_DOUBLE_DCT = 10# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_INT32_DCT = 11# /home/josiah/ctypesgen_test/av/av/tx.h: 39

AV_TX_NB = (AV_TX_INT32_DCT + 1)# /home/josiah/ctypesgen_test/av/av/tx.h: 39

av_tx_fn = CFUNCTYPE(UNCHECKED(None), POINTER(AVTXContext), POINTER(None), POINTER(None), c_ptrdiff_t)# /home/josiah/ctypesgen_test/av/av/tx.h: 127

enum_AVTXFlags = c_int# /home/josiah/ctypesgen_test/av/av/tx.h: 132

AV_TX_INPLACE = (1 << 0)# /home/josiah/ctypesgen_test/av/av/tx.h: 132

AV_TX_UNALIGNED = (1 << 1)# /home/josiah/ctypesgen_test/av/av/tx.h: 132

AV_TX_FULL_IMDCT = (1 << 2)# /home/josiah/ctypesgen_test/av/av/tx.h: 132

# /home/josiah/ctypesgen_test/av/av/tx.h: 168
if _libs["avcodec"].has("av_tx_init", "cdecl"):
    av_tx_init = _libs["avcodec"].get("av_tx_init", "cdecl")
    av_tx_init.argtypes = [POINTER(POINTER(AVTXContext)), POINTER(av_tx_fn), enum_AVTXType, c_int, c_int, POINTER(None), uint64_t]
    av_tx_init.restype = c_int

# /home/josiah/ctypesgen_test/av/av/tx.h: 174
if _libs["avcodec"].has("av_tx_uninit", "cdecl"):
    av_tx_uninit = _libs["avcodec"].get("av_tx_uninit", "cdecl")
    av_tx_uninit.argtypes = [POINTER(POINTER(AVTXContext))]
    av_tx_uninit.restype = None

enum_AVVideoEncParamsType = c_int# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_NONE = (-1)# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_VP9 = (AV_VIDEO_ENC_PARAMS_NONE + 1)# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_H264 = (AV_VIDEO_ENC_PARAMS_VP9 + 1)# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 28

AV_VIDEO_ENC_PARAMS_MPEG2 = (AV_VIDEO_ENC_PARAMS_H264 + 1)# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 28

# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 110
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

AVVideoEncParams = struct_AVVideoEncParams# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 110

# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 137
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

AVVideoBlockParams = struct_AVVideoBlockParams# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 137

# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 158
if _libs["avcodec"].has("av_video_enc_params_alloc", "cdecl"):
    av_video_enc_params_alloc = _libs["avcodec"].get("av_video_enc_params_alloc", "cdecl")
    av_video_enc_params_alloc.argtypes = [enum_AVVideoEncParamsType, c_uint, POINTER(c_size_t)]
    av_video_enc_params_alloc.restype = POINTER(AVVideoEncParams)

# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 167
if _libs["avcodec"].has("av_video_enc_params_create_side_data", "cdecl"):
    av_video_enc_params_create_side_data = _libs["avcodec"].get("av_video_enc_params_create_side_data", "cdecl")
    av_video_enc_params_create_side_data.argtypes = [POINTER(AVFrame), enum_AVVideoEncParamsType, c_uint]
    av_video_enc_params_create_side_data.restype = POINTER(AVVideoEncParams)

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 31
class struct_AVVorbisParseContext(Structure):
    pass

AVVorbisParseContext = struct_AVVorbisParseContext# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 31

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 36
if _libs["avcodec"].has("av_vorbis_parse_init", "cdecl"):
    av_vorbis_parse_init = _libs["avcodec"].get("av_vorbis_parse_init", "cdecl")
    av_vorbis_parse_init.argtypes = [POINTER(uint8_t), c_int]
    av_vorbis_parse_init.restype = POINTER(AVVorbisParseContext)

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 42
if _libs["avcodec"].has("av_vorbis_parse_free", "cdecl"):
    av_vorbis_parse_free = _libs["avcodec"].get("av_vorbis_parse_free", "cdecl")
    av_vorbis_parse_free.argtypes = [POINTER(POINTER(AVVorbisParseContext))]
    av_vorbis_parse_free.restype = None

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 59
if _libs["avcodec"].has("av_vorbis_parse_frame_flags", "cdecl"):
    av_vorbis_parse_frame_flags = _libs["avcodec"].get("av_vorbis_parse_frame_flags", "cdecl")
    av_vorbis_parse_frame_flags.argtypes = [POINTER(AVVorbisParseContext), POINTER(uint8_t), c_int, POINTER(c_int)]
    av_vorbis_parse_frame_flags.restype = c_int

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 69
if _libs["avcodec"].has("av_vorbis_parse_frame", "cdecl"):
    av_vorbis_parse_frame = _libs["avcodec"].get("av_vorbis_parse_frame", "cdecl")
    av_vorbis_parse_frame.argtypes = [POINTER(AVVorbisParseContext), POINTER(uint8_t), c_int]
    av_vorbis_parse_frame.restype = c_int

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 72
if _libs["avcodec"].has("av_vorbis_parse_reset", "cdecl"):
    av_vorbis_parse_reset = _libs["avcodec"].get("av_vorbis_parse_reset", "cdecl")
    av_vorbis_parse_reset.argtypes = [POINTER(AVVorbisParseContext)]
    av_vorbis_parse_reset.restype = None

# /home/josiah/ctypesgen_test/av/av/xtea.h: 37
class struct_AVXTEA(Structure):
    pass

struct_AVXTEA.__slots__ = [
    'key',
]
struct_AVXTEA._fields_ = [
    ('key', uint32_t * int(16)),
]

AVXTEA = struct_AVXTEA# /home/josiah/ctypesgen_test/av/av/xtea.h: 37

# /home/josiah/ctypesgen_test/av/av/xtea.h: 42
if _libs["avcodec"].has("av_xtea_alloc", "cdecl"):
    av_xtea_alloc = _libs["avcodec"].get("av_xtea_alloc", "cdecl")
    av_xtea_alloc.argtypes = []
    av_xtea_alloc.restype = POINTER(AVXTEA)

# /home/josiah/ctypesgen_test/av/av/xtea.h: 51
if _libs["avcodec"].has("av_xtea_init", "cdecl"):
    av_xtea_init = _libs["avcodec"].get("av_xtea_init", "cdecl")
    av_xtea_init.argtypes = [POINTER(struct_AVXTEA), uint8_t * int(16)]
    av_xtea_init.restype = None

# /home/josiah/ctypesgen_test/av/av/xtea.h: 60
if _libs["avcodec"].has("av_xtea_le_init", "cdecl"):
    av_xtea_le_init = _libs["avcodec"].get("av_xtea_le_init", "cdecl")
    av_xtea_le_init.argtypes = [POINTER(struct_AVXTEA), uint8_t * int(16)]
    av_xtea_le_init.restype = None

# /home/josiah/ctypesgen_test/av/av/xtea.h: 73
if _libs["avcodec"].has("av_xtea_crypt", "cdecl"):
    av_xtea_crypt = _libs["avcodec"].get("av_xtea_crypt", "cdecl")
    av_xtea_crypt.argtypes = [POINTER(struct_AVXTEA), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_xtea_crypt.restype = None

# /home/josiah/ctypesgen_test/av/av/xtea.h: 87
if _libs["avcodec"].has("av_xtea_le_crypt", "cdecl"):
    av_xtea_le_crypt = _libs["avcodec"].get("av_xtea_le_crypt", "cdecl")
    av_xtea_le_crypt.argtypes = [POINTER(struct_AVXTEA), POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t), c_int]
    av_xtea_le_crypt.restype = None

XID = c_ulong# /usr/include/X11/X.h: 66

# /usr/include/X11/extensions/XvMC.h: 96
class struct_anon_445(Structure):
    pass

struct_anon_445.__slots__ = [
    'surface_id',
    'context_id',
    'surface_type_id',
    'width',
    'height',
    'privData',
]
struct_anon_445._fields_ = [
    ('surface_id', XID),
    ('context_id', XID),
    ('surface_type_id', c_int),
    ('width', c_ushort),
    ('height', c_ushort),
    ('privData', POINTER(None)),
]

XvMCSurface = struct_anon_445# /usr/include/X11/extensions/XvMC.h: 96

# /usr/include/X11/extensions/XvMC.h: 128
class struct_anon_448(Structure):
    pass

struct_anon_448.__slots__ = [
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
struct_anon_448._fields_ = [
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

XvMCMacroBlock = struct_anon_448# /usr/include/X11/extensions/XvMC.h: 128

# /home/josiah/ctypesgen_test/av/av/xvmc.h: 47
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

# /home/josiah/ctypesgen_test/av/av/attributes.h: 33
def AV_GCC_VERSION_AT_LEAST(x, y):
    return 0

# /home/josiah/ctypesgen_test/av/av/attributes.h: 34
def AV_GCC_VERSION_AT_MOST(x, y):
    return 0

# /home/josiah/ctypesgen_test/av/av/attributes.h: 126
def AV_NOWARN_DEPRECATED(code):
    return code

# /home/josiah/ctypesgen_test/av/av/attributes.h: 156
def av_uninit(x):
    return x

# /home/josiah/ctypesgen_test/av/av/attributes.h: 163
def av_builtin_constant_p(x):
    return 0

# /home/josiah/ctypesgen_test/av/av/adts_parser.h: 25
try:
    AV_AAC_ADTS_HEADER_SIZE = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 35
try:
    AES_CTR_KEY_SIZE = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 36
try:
    AES_CTR_IV_SIZE = 8
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

# /usr/include/libavutil/macros.h: 33
def AV_NE(be, le):
    return le

# /usr/include/libavutil/macros.h: 45
def FFDIFFSIGN(x, y):
    return ((x > y) - (x < y))

# /usr/include/libavutil/macros.h: 47
def FFMAX(a, b):
    return (a > b) and a or b

# /usr/include/libavutil/macros.h: 48
def FFMAX3(a, b, c):
    return (FFMAX ((FFMAX (a, b)), c))

# /usr/include/libavutil/macros.h: 49
def FFMIN(a, b):
    return (a > b) and b or a

# /usr/include/libavutil/macros.h: 50
def FFMIN3(a, b, c):
    return (FFMIN ((FFMIN (a, b)), c))

# /usr/include/libavutil/macros.h: 53
def FF_ARRAY_ELEMS(a):
    return (sizeof(a) / sizeof((a [0])))

# /usr/include/libavutil/macros.h: 55
def MKTAG(a, b, c, d):
    return (((a | (b << 8)) | (c << 16)) | ((c_uint (ord_if_char(d))).value << 24))

# /usr/include/libavutil/macros.h: 56
def MKBETAG(a, b, c, d):
    return (((d | (c << 8)) | (b << 16)) | ((c_uint (ord_if_char(a))).value << 24))

# /usr/include/libavutil/macros.h: 66
def AV_STRINGIFY(s):
    return (AV_TOSTRING (s))

# /usr/include/libavutil/macros.h: 67
def AV_TOSTRING(s):
    return s

# /usr/include/libavutil/macros.h: 78
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
    return ((a & 0x00FF00) >> 8)

# /usr/include/libavutil/version.h: 66
def AV_VERSION_MICRO(a):
    return (a & 0xFF)

# /usr/include/libavutil/version.h: 81
try:
    LIBAVUTIL_VERSION_MAJOR = 58
except:
    pass

# /usr/include/libavutil/version.h: 82
try:
    LIBAVUTIL_VERSION_MINOR = 2
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

# /usr/include/libavutil/version.h: 108
try:
    FF_API_FIFO_PEEK2 = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 109
try:
    FF_API_FIFO_OLD_API = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 110
try:
    FF_API_XVMC = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 111
try:
    FF_API_OLD_CHANNEL_LAYOUT = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 112
try:
    FF_API_AV_FOPEN_UTF8 = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 113
try:
    FF_API_PKT_DURATION = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 114
try:
    FF_API_REORDERED_OPAQUE = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /usr/include/libavutil/version.h: 115
try:
    FF_API_FRAME_PICTURE_NUMBER = (LIBAVUTIL_VERSION_MAJOR < 59)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/version_major.h: 28
try:
    LIBAVCODEC_VERSION_MAJOR = 60
except:
    pass

# /home/josiah/ctypesgen_test/av/av/version.h: 32
try:
    LIBAVCODEC_VERSION_MINOR = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/version.h: 33
try:
    LIBAVCODEC_VERSION_MICRO = 100
except:
    pass

# /home/josiah/ctypesgen_test/av/av/version.h: 35
try:
    LIBAVCODEC_VERSION_INT = (AV_VERSION_INT (LIBAVCODEC_VERSION_MAJOR, LIBAVCODEC_VERSION_MINOR, LIBAVCODEC_VERSION_MICRO))
except:
    pass

# /home/josiah/ctypesgen_test/av/av/version.h: 41
try:
    LIBAVCODEC_BUILD = LIBAVCODEC_VERSION_INT
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 49
def AV_IS_INPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_INPUT))

# /home/josiah/ctypesgen_test/av/av/log.h: 54
def AV_IS_OUTPUT_DEVICE(category):
    return (((category == AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT) or (category == AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT)) or (category == AV_CLASS_CATEGORY_DEVICE_OUTPUT))

# /home/josiah/ctypesgen_test/av/av/log.h: 162
try:
    AV_LOG_QUIET = (-8)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 167
try:
    AV_LOG_PANIC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 174
try:
    AV_LOG_FATAL = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 180
try:
    AV_LOG_ERROR = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 186
try:
    AV_LOG_WARNING = 24
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 191
try:
    AV_LOG_INFO = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 196
try:
    AV_LOG_VERBOSE = 40
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 201
try:
    AV_LOG_DEBUG = 48
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 206
try:
    AV_LOG_TRACE = 56
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 208
try:
    AV_LOG_MAX_OFFSET = (AV_LOG_TRACE - AV_LOG_QUIET)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 222
def AV_LOG_C(x):
    return (x << 8)

# /home/josiah/ctypesgen_test/av/av/log.h: 370
try:
    AV_LOG_SKIP_REPEATED = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/log.h: 378
try:
    AV_LOG_PRINT_LEVEL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avassert.h: 53
def av_assert1(cond):
    return None

# /home/josiah/ctypesgen_test/av/av/avassert.h: 64
def av_assert2(cond):
    return None

# /home/josiah/ctypesgen_test/av/av/avassert.h: 65
try:
    av_assert2_fpu = None
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

# /usr/lib/gcc/x86_64-pc-linux-gnu/12.2.1/include-fixed/limits.h: 119
# #undef INT_MAX
try:
    del INT_MAX
except NameError:
    pass

# /usr/include/libavutil/common.h: 46
def RSHIFT(a, b):
    return (a > 0) and ((a + ((1 << b) >> 1)) >> b) or (((a + ((1 << b) >> 1)) - 1) >> b)

# /usr/include/libavutil/common.h: 48
def ROUNDED_DIV(a, b):
    return ((a >= 0) and (a + (b >> 1)) or (a - (b >> 1)) / b)

# /usr/include/libavutil/common.h: 50
def AV_CEIL_RSHIFT(a, b):
    return (not (av_builtin_constant_p (b))) and (-((-a) >> b)) or (((a + (1 << b)) - 1) >> b)

# /usr/include/libavutil/common.h: 53
try:
    FF_CEIL_RSHIFT = AV_CEIL_RSHIFT
except:
    pass

# /usr/include/libavutil/common.h: 55
def FFUDIV(a, b):
    return ((a > 0) and a or ((a - b) + 1) / b)

# /usr/include/libavutil/common.h: 56
def FFUMOD(a, b):
    return (a - (b * (FFUDIV (a, b))))

# /usr/include/libavutil/common.h: 64
def FFABS(a):
    return (a >= 0) and a or (-a)

# /usr/include/libavutil/common.h: 65
def FFSIGN(a):
    return (a > 0) and 1 or (-1)

# /usr/include/libavutil/common.h: 73
def FFNABS(a):
    return (a <= 0) and a or (-a)

# /usr/include/libavutil/common.h: 81
def FFABSU(a):
    return (a <= 0) and (-(c_uint (ord_if_char(a))).value) or (c_uint (ord_if_char(a))).value

# /usr/include/libavutil/common.h: 82
def FFABS64U(a):
    return (a <= 0) and (-(uint64_t (ord_if_char(a))).value) or (uint64_t (ord_if_char(a))).value

# /usr/include/libavutil/error.h: 41
def AVERROR(e):
    return (-e)

# /usr/include/libavutil/error.h: 42
def AVUNERROR(e):
    return (-e)

# /usr/include/libavutil/error.h: 49
def FFERRTAG(a, b, c, d):
    return (-(c_int (ord_if_char((MKTAG (a, b, c, d))))).value)

# /usr/include/libavutil/error.h: 51
try:
    AVERROR_BSF_NOT_FOUND = (FFERRTAG (0xF8, 'B', 'S', 'F'))
except:
    pass

# /usr/include/libavutil/error.h: 52
try:
    AVERROR_BUG = (FFERRTAG ('B', 'U', 'G', '!'))
except:
    pass

# /usr/include/libavutil/error.h: 53
try:
    AVERROR_BUFFER_TOO_SMALL = (FFERRTAG ('B', 'U', 'F', 'S'))
except:
    pass

# /usr/include/libavutil/error.h: 54
try:
    AVERROR_DECODER_NOT_FOUND = (FFERRTAG (0xF8, 'D', 'E', 'C'))
except:
    pass

# /usr/include/libavutil/error.h: 55
try:
    AVERROR_DEMUXER_NOT_FOUND = (FFERRTAG (0xF8, 'D', 'E', 'M'))
except:
    pass

# /usr/include/libavutil/error.h: 56
try:
    AVERROR_ENCODER_NOT_FOUND = (FFERRTAG (0xF8, 'E', 'N', 'C'))
except:
    pass

# /usr/include/libavutil/error.h: 57
try:
    AVERROR_EOF = (FFERRTAG ('E', 'O', 'F', ' '))
except:
    pass

# /usr/include/libavutil/error.h: 58
try:
    AVERROR_EXIT = (FFERRTAG ('E', 'X', 'I', 'T'))
except:
    pass

# /usr/include/libavutil/error.h: 59
try:
    AVERROR_EXTERNAL = (FFERRTAG ('E', 'X', 'T', ' '))
except:
    pass

# /usr/include/libavutil/error.h: 60
try:
    AVERROR_FILTER_NOT_FOUND = (FFERRTAG (0xF8, 'F', 'I', 'L'))
except:
    pass

# /usr/include/libavutil/error.h: 61
try:
    AVERROR_INVALIDDATA = (FFERRTAG ('I', 'N', 'D', 'A'))
except:
    pass

# /usr/include/libavutil/error.h: 62
try:
    AVERROR_MUXER_NOT_FOUND = (FFERRTAG (0xF8, 'M', 'U', 'X'))
except:
    pass

# /usr/include/libavutil/error.h: 63
try:
    AVERROR_OPTION_NOT_FOUND = (FFERRTAG (0xF8, 'O', 'P', 'T'))
except:
    pass

# /usr/include/libavutil/error.h: 64
try:
    AVERROR_PATCHWELCOME = (FFERRTAG ('P', 'A', 'W', 'E'))
except:
    pass

# /usr/include/libavutil/error.h: 65
try:
    AVERROR_PROTOCOL_NOT_FOUND = (FFERRTAG (0xF8, 'P', 'R', 'O'))
except:
    pass

# /usr/include/libavutil/error.h: 67
try:
    AVERROR_STREAM_NOT_FOUND = (FFERRTAG (0xF8, 'S', 'T', 'R'))
except:
    pass

# /usr/include/libavutil/error.h: 72
try:
    AVERROR_BUG2 = (FFERRTAG ('B', 'U', 'G', ' '))
except:
    pass

# /usr/include/libavutil/error.h: 73
try:
    AVERROR_UNKNOWN = (FFERRTAG ('U', 'N', 'K', 'N'))
except:
    pass

# /usr/include/libavutil/error.h: 74
try:
    AVERROR_EXPERIMENTAL = (-0x2bb2afa8)
except:
    pass

# /usr/include/libavutil/error.h: 75
try:
    AVERROR_INPUT_CHANGED = (-0x636e6701)
except:
    pass

# /usr/include/libavutil/error.h: 76
try:
    AVERROR_OUTPUT_CHANGED = (-0x636e6702)
except:
    pass

# /usr/include/libavutil/error.h: 78
try:
    AVERROR_HTTP_BAD_REQUEST = (FFERRTAG (0xF8, '4', '0', '0'))
except:
    pass

# /usr/include/libavutil/error.h: 79
try:
    AVERROR_HTTP_UNAUTHORIZED = (FFERRTAG (0xF8, '4', '0', '1'))
except:
    pass

# /usr/include/libavutil/error.h: 80
try:
    AVERROR_HTTP_FORBIDDEN = (FFERRTAG (0xF8, '4', '0', '3'))
except:
    pass

# /usr/include/libavutil/error.h: 81
try:
    AVERROR_HTTP_NOT_FOUND = (FFERRTAG (0xF8, '4', '0', '4'))
except:
    pass

# /usr/include/libavutil/error.h: 82
try:
    AVERROR_HTTP_OTHER_4XX = (FFERRTAG (0xF8, '4', 'X', 'X'))
except:
    pass

# /usr/include/libavutil/error.h: 83
try:
    AVERROR_HTTP_SERVER_ERROR = (FFERRTAG (0xF8, '5', 'X', 'X'))
except:
    pass

# /usr/include/libavutil/error.h: 85
try:
    AV_ERROR_MAX_STRING_SIZE = 64
except:
    pass

# /usr/include/libavutil/mathematics.h: 46
try:
    M_LOG2_10 = 3.32192809488736234787
except:
    pass

# /usr/include/libavutil/mathematics.h: 49
try:
    M_PHI = 1.61803398874989484820
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

# /usr/include/libavutil/avutil.h: 352
try:
    AV_FOURCC_MAX_STRING_SIZE = 32
except:
    pass

# /usr/include/libavutil/buffer.h: 114
try:
    AV_BUFFER_FLAG_READONLY = (1 << 0)
except:
    pass

# /usr/include/libavutil/dict.h: 74
try:
    AV_DICT_MATCH_CASE = 1
except:
    pass

# /usr/include/libavutil/dict.h: 75
try:
    AV_DICT_IGNORE_SUFFIX = 2
except:
    pass

# /usr/include/libavutil/dict.h: 77
try:
    AV_DICT_DONT_STRDUP_KEY = 4
except:
    pass

# /usr/include/libavutil/dict.h: 79
try:
    AV_DICT_DONT_STRDUP_VAL = 8
except:
    pass

# /usr/include/libavutil/dict.h: 81
try:
    AV_DICT_DONT_OVERWRITE = 16
except:
    pass

# /usr/include/libavutil/dict.h: 82
try:
    AV_DICT_APPEND = 32
except:
    pass

# /usr/include/libavutil/dict.h: 84
try:
    AV_DICT_MULTIKEY = 64
except:
    pass

# /usr/include/libavutil/channel_layout.h: 164
try:
    AV_CH_FRONT_LEFT = (1 << AV_CHAN_FRONT_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 165
try:
    AV_CH_FRONT_RIGHT = (1 << AV_CHAN_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 166
try:
    AV_CH_FRONT_CENTER = (1 << AV_CHAN_FRONT_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 167
try:
    AV_CH_LOW_FREQUENCY = (1 << AV_CHAN_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 168
try:
    AV_CH_BACK_LEFT = (1 << AV_CHAN_BACK_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 169
try:
    AV_CH_BACK_RIGHT = (1 << AV_CHAN_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 170
try:
    AV_CH_FRONT_LEFT_OF_CENTER = (1 << AV_CHAN_FRONT_LEFT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 171
try:
    AV_CH_FRONT_RIGHT_OF_CENTER = (1 << AV_CHAN_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 172
try:
    AV_CH_BACK_CENTER = (1 << AV_CHAN_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 173
try:
    AV_CH_SIDE_LEFT = (1 << AV_CHAN_SIDE_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 174
try:
    AV_CH_SIDE_RIGHT = (1 << AV_CHAN_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 175
try:
    AV_CH_TOP_CENTER = (1 << AV_CHAN_TOP_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 176
try:
    AV_CH_TOP_FRONT_LEFT = (1 << AV_CHAN_TOP_FRONT_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 177
try:
    AV_CH_TOP_FRONT_CENTER = (1 << AV_CHAN_TOP_FRONT_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 178
try:
    AV_CH_TOP_FRONT_RIGHT = (1 << AV_CHAN_TOP_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 179
try:
    AV_CH_TOP_BACK_LEFT = (1 << AV_CHAN_TOP_BACK_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 180
try:
    AV_CH_TOP_BACK_CENTER = (1 << AV_CHAN_TOP_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 181
try:
    AV_CH_TOP_BACK_RIGHT = (1 << AV_CHAN_TOP_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 182
try:
    AV_CH_STEREO_LEFT = (1 << AV_CHAN_STEREO_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 183
try:
    AV_CH_STEREO_RIGHT = (1 << AV_CHAN_STEREO_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 184
try:
    AV_CH_WIDE_LEFT = (1 << AV_CHAN_WIDE_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 185
try:
    AV_CH_WIDE_RIGHT = (1 << AV_CHAN_WIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 186
try:
    AV_CH_SURROUND_DIRECT_LEFT = (1 << AV_CHAN_SURROUND_DIRECT_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 187
try:
    AV_CH_SURROUND_DIRECT_RIGHT = (1 << AV_CHAN_SURROUND_DIRECT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 188
try:
    AV_CH_LOW_FREQUENCY_2 = (1 << AV_CHAN_LOW_FREQUENCY_2)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 189
try:
    AV_CH_TOP_SIDE_LEFT = (1 << AV_CHAN_TOP_SIDE_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 190
try:
    AV_CH_TOP_SIDE_RIGHT = (1 << AV_CHAN_TOP_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 191
try:
    AV_CH_BOTTOM_FRONT_CENTER = (1 << AV_CHAN_BOTTOM_FRONT_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 192
try:
    AV_CH_BOTTOM_FRONT_LEFT = (1 << AV_CHAN_BOTTOM_FRONT_LEFT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 193
try:
    AV_CH_BOTTOM_FRONT_RIGHT = (1 << AV_CHAN_BOTTOM_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 202
try:
    AV_CH_LAYOUT_NATIVE = 0x8000000000000000
except:
    pass

# /usr/include/libavutil/channel_layout.h: 210
try:
    AV_CH_LAYOUT_MONO = AV_CH_FRONT_CENTER
except:
    pass

# /usr/include/libavutil/channel_layout.h: 211
try:
    AV_CH_LAYOUT_STEREO = (AV_CH_FRONT_LEFT | AV_CH_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 212
try:
    AV_CH_LAYOUT_2POINT1 = (AV_CH_LAYOUT_STEREO | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 213
try:
    AV_CH_LAYOUT_2_1 = (AV_CH_LAYOUT_STEREO | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 214
try:
    AV_CH_LAYOUT_SURROUND = (AV_CH_LAYOUT_STEREO | AV_CH_FRONT_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 215
try:
    AV_CH_LAYOUT_3POINT1 = (AV_CH_LAYOUT_SURROUND | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 216
try:
    AV_CH_LAYOUT_4POINT0 = (AV_CH_LAYOUT_SURROUND | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 217
try:
    AV_CH_LAYOUT_4POINT1 = (AV_CH_LAYOUT_4POINT0 | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 218
try:
    AV_CH_LAYOUT_2_2 = ((AV_CH_LAYOUT_STEREO | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 219
try:
    AV_CH_LAYOUT_QUAD = ((AV_CH_LAYOUT_STEREO | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 220
try:
    AV_CH_LAYOUT_5POINT0 = ((AV_CH_LAYOUT_SURROUND | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 221
try:
    AV_CH_LAYOUT_5POINT1 = (AV_CH_LAYOUT_5POINT0 | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 222
try:
    AV_CH_LAYOUT_5POINT0_BACK = ((AV_CH_LAYOUT_SURROUND | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 223
try:
    AV_CH_LAYOUT_5POINT1_BACK = (AV_CH_LAYOUT_5POINT0_BACK | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 224
try:
    AV_CH_LAYOUT_6POINT0 = (AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 225
try:
    AV_CH_LAYOUT_6POINT0_FRONT = ((AV_CH_LAYOUT_2_2 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 226
try:
    AV_CH_LAYOUT_HEXAGONAL = (AV_CH_LAYOUT_5POINT0_BACK | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 227
try:
    AV_CH_LAYOUT_6POINT1 = (AV_CH_LAYOUT_5POINT1 | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 228
try:
    AV_CH_LAYOUT_6POINT1_BACK = (AV_CH_LAYOUT_5POINT1_BACK | AV_CH_BACK_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 229
try:
    AV_CH_LAYOUT_6POINT1_FRONT = (AV_CH_LAYOUT_6POINT0_FRONT | AV_CH_LOW_FREQUENCY)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 230
try:
    AV_CH_LAYOUT_7POINT0 = ((AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 231
try:
    AV_CH_LAYOUT_7POINT0_FRONT = ((AV_CH_LAYOUT_5POINT0 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 232
try:
    AV_CH_LAYOUT_7POINT1 = ((AV_CH_LAYOUT_5POINT1 | AV_CH_BACK_LEFT) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 233
try:
    AV_CH_LAYOUT_7POINT1_WIDE = ((AV_CH_LAYOUT_5POINT1 | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 234
try:
    AV_CH_LAYOUT_7POINT1_WIDE_BACK = ((AV_CH_LAYOUT_5POINT1_BACK | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 235
try:
    AV_CH_LAYOUT_7POINT1_TOP_BACK = ((AV_CH_LAYOUT_5POINT1_BACK | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 236
try:
    AV_CH_LAYOUT_OCTAGONAL = (((AV_CH_LAYOUT_5POINT0 | AV_CH_BACK_LEFT) | AV_CH_BACK_CENTER) | AV_CH_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 237
try:
    AV_CH_LAYOUT_CUBE = ((((AV_CH_LAYOUT_QUAD | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT) | AV_CH_TOP_BACK_LEFT) | AV_CH_TOP_BACK_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 238
try:
    AV_CH_LAYOUT_HEXADECAGONAL = ((((((((AV_CH_LAYOUT_OCTAGONAL | AV_CH_WIDE_LEFT) | AV_CH_WIDE_RIGHT) | AV_CH_TOP_BACK_LEFT) | AV_CH_TOP_BACK_RIGHT) | AV_CH_TOP_BACK_CENTER) | AV_CH_TOP_FRONT_CENTER) | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 239
try:
    AV_CH_LAYOUT_STEREO_DOWNMIX = (AV_CH_STEREO_LEFT | AV_CH_STEREO_RIGHT)
except:
    pass

# /usr/include/libavutil/channel_layout.h: 240
try:
    AV_CH_LAYOUT_22POINT2 = ((((((((((((((((((AV_CH_LAYOUT_5POINT1_BACK | AV_CH_FRONT_LEFT_OF_CENTER) | AV_CH_FRONT_RIGHT_OF_CENTER) | AV_CH_BACK_CENTER) | AV_CH_LOW_FREQUENCY_2) | AV_CH_SIDE_LEFT) | AV_CH_SIDE_RIGHT) | AV_CH_TOP_FRONT_LEFT) | AV_CH_TOP_FRONT_RIGHT) | AV_CH_TOP_FRONT_CENTER) | AV_CH_TOP_CENTER) | AV_CH_TOP_BACK_LEFT) | AV_CH_TOP_BACK_RIGHT) | AV_CH_TOP_SIDE_LEFT) | AV_CH_TOP_SIDE_RIGHT) | AV_CH_TOP_BACK_CENTER) | AV_CH_BOTTOM_FRONT_CENTER) | AV_CH_BOTTOM_FRONT_LEFT) | AV_CH_BOTTOM_FRONT_RIGHT)
except:
    pass

# /usr/include/libavutil/frame.h: 331
try:
    AV_NUM_DATA_POINTERS = 8
except:
    pass

# /usr/include/libavutil/frame.h: 573
try:
    AV_FRAME_FLAG_CORRUPT = (1 << 0)
except:
    pass

# /usr/include/libavutil/frame.h: 577
try:
    AV_FRAME_FLAG_DISCARD = (1 << 2)
except:
    pass

# /usr/include/libavutil/frame.h: 649
try:
    FF_DECODE_ERROR_INVALID_BITSTREAM = 1
except:
    pass

# /usr/include/libavutil/frame.h: 650
try:
    FF_DECODE_ERROR_MISSING_REFERENCE = 2
except:
    pass

# /usr/include/libavutil/frame.h: 651
try:
    FF_DECODE_ERROR_CONCEALMENT_ACTIVE = 4
except:
    pass

# /usr/include/libavutil/frame.h: 652
try:
    FF_DECODE_ERROR_DECODE_SLICES = 8
except:
    pass

# /usr/include/libavcodec/codec_id.h: 189
try:
    AV_CODEC_ID_IFF_BYTERUN1 = AV_CODEC_ID_IFF_ILBM
except:
    pass

# /usr/include/libavcodec/codec_id.h: 227
try:
    AV_CODEC_ID_H265 = AV_CODEC_ID_HEVC
except:
    pass

# /usr/include/libavcodec/codec_id.h: 251
try:
    AV_CODEC_ID_H266 = AV_CODEC_ID_VVC
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 44
try:
    AV_CODEC_CAP_DRAW_HORIZ_BAND = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 52
try:
    AV_CODEC_CAP_DR1 = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 76
try:
    AV_CODEC_CAP_DELAY = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 81
try:
    AV_CODEC_CAP_SMALL_LAST_FRAME = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 94
try:
    AV_CODEC_CAP_SUBFRAMES = (1 << 8)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 99
try:
    AV_CODEC_CAP_EXPERIMENTAL = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 103
try:
    AV_CODEC_CAP_CHANNEL_CONF = (1 << 10)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 107
try:
    AV_CODEC_CAP_FRAME_THREADS = (1 << 12)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 111
try:
    AV_CODEC_CAP_SLICE_THREADS = (1 << 13)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 115
try:
    AV_CODEC_CAP_PARAM_CHANGE = (1 << 14)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 121
try:
    AV_CODEC_CAP_OTHER_THREADS = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 125
try:
    AV_CODEC_CAP_VARIABLE_FRAME_SIZE = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 135
try:
    AV_CODEC_CAP_AVOID_PROBING = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 142
try:
    AV_CODEC_CAP_HARDWARE = (1 << 18)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 149
try:
    AV_CODEC_CAP_HYBRID = (1 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 156
try:
    AV_CODEC_CAP_ENCODER_REORDERED_OPAQUE = (1 << 20)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 163
try:
    AV_CODEC_CAP_ENCODER_FLUSH = (1 << 21)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec.h: 171
try:
    AV_CODEC_CAP_ENCODER_RECON_FRAME = (1 << 22)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 72
try:
    AV_CODEC_PROP_INTRA_ONLY = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 78
try:
    AV_CODEC_PROP_LOSSY = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 82
try:
    AV_CODEC_PROP_LOSSLESS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 92
try:
    AV_CODEC_PROP_REORDER = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 97
try:
    AV_CODEC_PROP_BITMAP_SUB = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 102
try:
    AV_CODEC_PROP_TEXT_SUB = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 313
try:
    AV_PKT_DATA_QUALITY_FACTOR = AV_PKT_DATA_QUALITY_STATS
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 429
try:
    AV_PKT_FLAG_KEY = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 430
try:
    AV_PKT_FLAG_CORRUPT = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 436
try:
    AV_PKT_FLAG_DISCARD = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 443
try:
    AV_PKT_FLAG_TRUSTED = 0x0008
except:
    pass

# /home/josiah/ctypesgen_test/av/av/packet.h: 448
try:
    AV_PKT_FLAG_DISPOSABLE = 0x0010
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 191
try:
    AV_INPUT_BUFFER_MIN_SIZE = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 212
try:
    AV_CODEC_FLAG_UNALIGNED = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 216
try:
    AV_CODEC_FLAG_QSCALE = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 220
try:
    AV_CODEC_FLAG_4MV = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 224
try:
    AV_CODEC_FLAG_OUTPUT_CORRUPT = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 228
try:
    AV_CODEC_FLAG_QPEL = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 233
try:
    AV_CODEC_FLAG_DROPCHANGED = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 243
try:
    AV_CODEC_FLAG_RECON_FRAME = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 278
try:
    AV_CODEC_FLAG_COPY_OPAQUE = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 285
try:
    AV_CODEC_FLAG_FRAME_DURATION = (1 << 8)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 289
try:
    AV_CODEC_FLAG_PASS1 = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 293
try:
    AV_CODEC_FLAG_PASS2 = (1 << 10)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 297
try:
    AV_CODEC_FLAG_LOOP_FILTER = (1 << 11)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 301
try:
    AV_CODEC_FLAG_GRAY = (1 << 13)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 305
try:
    AV_CODEC_FLAG_PSNR = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 309
try:
    AV_CODEC_FLAG_INTERLACED_DCT = (1 << 18)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 313
try:
    AV_CODEC_FLAG_LOW_DELAY = (1 << 19)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 317
try:
    AV_CODEC_FLAG_GLOBAL_HEADER = (1 << 22)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 321
try:
    AV_CODEC_FLAG_BITEXACT = (1 << 23)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 326
try:
    AV_CODEC_FLAG_AC_PRED = (1 << 24)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 330
try:
    AV_CODEC_FLAG_INTERLACED_ME = (1 << 29)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 331
try:
    AV_CODEC_FLAG_CLOSED_GOP = (1 << 31)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 336
try:
    AV_CODEC_FLAG2_FAST = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 340
try:
    AV_CODEC_FLAG2_NO_OUTPUT = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 344
try:
    AV_CODEC_FLAG2_LOCAL_HEADER = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 350
try:
    AV_CODEC_FLAG2_CHUNKS = (1 << 15)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 354
try:
    AV_CODEC_FLAG2_IGNORE_CROP = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 359
try:
    AV_CODEC_FLAG2_SHOW_ALL = (1 << 22)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 363
try:
    AV_CODEC_FLAG2_EXPORT_MVS = (1 << 28)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 367
try:
    AV_CODEC_FLAG2_SKIP_MANUAL = (1 << 29)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 371
try:
    AV_CODEC_FLAG2_RO_FLUSH_NOOP = (1 << 30)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 377
try:
    AV_CODEC_FLAG2_ICC_PROFILES = (1 << 31)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 385
try:
    AV_CODEC_EXPORT_DATA_MVS = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 389
try:
    AV_CODEC_EXPORT_DATA_PRFT = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 394
try:
    AV_CODEC_EXPORT_DATA_VIDEO_ENC_PARAMS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 399
try:
    AV_CODEC_EXPORT_DATA_FILM_GRAIN = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 404
try:
    AV_GET_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 409
try:
    AV_GET_ENCODE_BUFFER_FLAG_REF = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 499
try:
    FF_COMPRESSION_DEFAULT = (-1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 821
try:
    FF_CMP_SAD = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 822
try:
    FF_CMP_SSE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 823
try:
    FF_CMP_SATD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 824
try:
    FF_CMP_DCT = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 825
try:
    FF_CMP_PSNR = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 826
try:
    FF_CMP_BIT = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 827
try:
    FF_CMP_RD = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 828
try:
    FF_CMP_ZERO = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 829
try:
    FF_CMP_VSAD = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 830
try:
    FF_CMP_VSSE = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 831
try:
    FF_CMP_NSSE = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 832
try:
    FF_CMP_W53 = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 833
try:
    FF_CMP_W97 = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 834
try:
    FF_CMP_DCTMAX = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 835
try:
    FF_CMP_DCT264 = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 836
try:
    FF_CMP_MEDIAN_SAD = 15
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 837
try:
    FF_CMP_CHROMA = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 889
try:
    SLICE_FLAG_CODED_ORDER = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 890
try:
    SLICE_FLAG_ALLOW_FIELD = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 891
try:
    SLICE_FLAG_ALLOW_PLANE = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 899
try:
    FF_MB_DECISION_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 900
try:
    FF_MB_DECISION_BITS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 901
try:
    FF_MB_DECISION_RD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1312
try:
    FF_BUG_AUTODETECT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1313
try:
    FF_BUG_XVID_ILACE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1314
try:
    FF_BUG_UMP4 = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1315
try:
    FF_BUG_NO_PADDING = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1316
try:
    FF_BUG_AMV = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1317
try:
    FF_BUG_QPEL_CHROMA = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1318
try:
    FF_BUG_STD_QPEL = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1319
try:
    FF_BUG_QPEL_CHROMA2 = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1320
try:
    FF_BUG_DIRECT_BLOCKSIZE = 512
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1321
try:
    FF_BUG_EDGE = 1024
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1322
try:
    FF_BUG_HPEL_CHROMA = 2048
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1323
try:
    FF_BUG_DC_CLIP = 4096
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1324
try:
    FF_BUG_MS = 8192
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1325
try:
    FF_BUG_TRUNCATED = 16384
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1326
try:
    FF_BUG_IEDGE = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1349
try:
    FF_EC_GUESS_MVS = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1350
try:
    FF_EC_DEBLOCK = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1351
try:
    FF_EC_FAVOR_INTER = 256
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1359
try:
    FF_DEBUG_PICT_INFO = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1360
try:
    FF_DEBUG_RC = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1361
try:
    FF_DEBUG_BITSTREAM = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1362
try:
    FF_DEBUG_MB_TYPE = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1363
try:
    FF_DEBUG_QP = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1364
try:
    FF_DEBUG_DCT_COEFF = 0x00000040
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1365
try:
    FF_DEBUG_SKIP = 0x00000080
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1366
try:
    FF_DEBUG_STARTCODE = 0x00000100
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1367
try:
    FF_DEBUG_ER = 0x00000400
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1368
try:
    FF_DEBUG_MMCO = 0x00000800
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1369
try:
    FF_DEBUG_BUGS = 0x00001000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1370
try:
    FF_DEBUG_BUFFERS = 0x00008000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1371
try:
    FF_DEBUG_THREADS = 0x00010000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1372
try:
    FF_DEBUG_GREEN_MD = 0x00800000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1373
try:
    FF_DEBUG_NOMC = 0x01000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1444
try:
    FF_DCT_AUTO = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1445
try:
    FF_DCT_FASTINT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1446
try:
    FF_DCT_INT = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1447
try:
    FF_DCT_MMX = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1448
try:
    FF_DCT_ALTIVEC = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1449
try:
    FF_DCT_FAAN = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1457
try:
    FF_IDCT_AUTO = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1458
try:
    FF_IDCT_INT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1459
try:
    FF_IDCT_SIMPLE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1460
try:
    FF_IDCT_SIMPLEMMX = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1461
try:
    FF_IDCT_ARM = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1462
try:
    FF_IDCT_ALTIVEC = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1463
try:
    FF_IDCT_SIMPLEARM = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1464
try:
    FF_IDCT_XVID = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1465
try:
    FF_IDCT_SIMPLEARMV5TE = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1466
try:
    FF_IDCT_SIMPLEARMV6 = 17
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1467
try:
    FF_IDCT_FAAN = 20
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1468
try:
    FF_IDCT_SIMPLENEON = 22
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1471
try:
    FF_IDCT_NONE = 24
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1473
try:
    FF_IDCT_SIMPLEAUTO = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1513
try:
    FF_THREAD_FRAME = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1514
try:
    FF_THREAD_SLICE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1566
try:
    FF_PROFILE_UNKNOWN = (-99)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1567
try:
    FF_PROFILE_RESERVED = (-100)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1569
try:
    FF_PROFILE_AAC_MAIN = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1570
try:
    FF_PROFILE_AAC_LOW = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1571
try:
    FF_PROFILE_AAC_SSR = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1572
try:
    FF_PROFILE_AAC_LTP = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1573
try:
    FF_PROFILE_AAC_HE = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1574
try:
    FF_PROFILE_AAC_HE_V2 = 28
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1575
try:
    FF_PROFILE_AAC_LD = 22
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1576
try:
    FF_PROFILE_AAC_ELD = 38
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1577
try:
    FF_PROFILE_MPEG2_AAC_LOW = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1578
try:
    FF_PROFILE_MPEG2_AAC_HE = 131
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1580
try:
    FF_PROFILE_DNXHD = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1581
try:
    FF_PROFILE_DNXHR_LB = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1582
try:
    FF_PROFILE_DNXHR_SQ = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1583
try:
    FF_PROFILE_DNXHR_HQ = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1584
try:
    FF_PROFILE_DNXHR_HQX = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1585
try:
    FF_PROFILE_DNXHR_444 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1587
try:
    FF_PROFILE_DTS = 20
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1588
try:
    FF_PROFILE_DTS_ES = 30
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1589
try:
    FF_PROFILE_DTS_96_24 = 40
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1590
try:
    FF_PROFILE_DTS_HD_HRA = 50
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1591
try:
    FF_PROFILE_DTS_HD_MA = 60
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1592
try:
    FF_PROFILE_DTS_EXPRESS = 70
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1594
try:
    FF_PROFILE_MPEG2_422 = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1595
try:
    FF_PROFILE_MPEG2_HIGH = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1596
try:
    FF_PROFILE_MPEG2_SS = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1597
try:
    FF_PROFILE_MPEG2_SNR_SCALABLE = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1598
try:
    FF_PROFILE_MPEG2_MAIN = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1599
try:
    FF_PROFILE_MPEG2_SIMPLE = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1601
try:
    FF_PROFILE_H264_CONSTRAINED = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1602
try:
    FF_PROFILE_H264_INTRA = (1 << 11)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1604
try:
    FF_PROFILE_H264_BASELINE = 66
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1605
try:
    FF_PROFILE_H264_CONSTRAINED_BASELINE = (66 | FF_PROFILE_H264_CONSTRAINED)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1606
try:
    FF_PROFILE_H264_MAIN = 77
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1607
try:
    FF_PROFILE_H264_EXTENDED = 88
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1608
try:
    FF_PROFILE_H264_HIGH = 100
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1609
try:
    FF_PROFILE_H264_HIGH_10 = 110
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1610
try:
    FF_PROFILE_H264_HIGH_10_INTRA = (110 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1611
try:
    FF_PROFILE_H264_MULTIVIEW_HIGH = 118
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1612
try:
    FF_PROFILE_H264_HIGH_422 = 122
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1613
try:
    FF_PROFILE_H264_HIGH_422_INTRA = (122 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1614
try:
    FF_PROFILE_H264_STEREO_HIGH = 128
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1615
try:
    FF_PROFILE_H264_HIGH_444 = 144
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1616
try:
    FF_PROFILE_H264_HIGH_444_PREDICTIVE = 244
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1617
try:
    FF_PROFILE_H264_HIGH_444_INTRA = (244 | FF_PROFILE_H264_INTRA)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1618
try:
    FF_PROFILE_H264_CAVLC_444 = 44
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1620
try:
    FF_PROFILE_VC1_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1621
try:
    FF_PROFILE_VC1_MAIN = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1622
try:
    FF_PROFILE_VC1_COMPLEX = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1623
try:
    FF_PROFILE_VC1_ADVANCED = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1625
try:
    FF_PROFILE_MPEG4_SIMPLE = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1626
try:
    FF_PROFILE_MPEG4_SIMPLE_SCALABLE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1627
try:
    FF_PROFILE_MPEG4_CORE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1628
try:
    FF_PROFILE_MPEG4_MAIN = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1629
try:
    FF_PROFILE_MPEG4_N_BIT = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1630
try:
    FF_PROFILE_MPEG4_SCALABLE_TEXTURE = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1631
try:
    FF_PROFILE_MPEG4_SIMPLE_FACE_ANIMATION = 6
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1632
try:
    FF_PROFILE_MPEG4_BASIC_ANIMATED_TEXTURE = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1633
try:
    FF_PROFILE_MPEG4_HYBRID = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1634
try:
    FF_PROFILE_MPEG4_ADVANCED_REAL_TIME = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1635
try:
    FF_PROFILE_MPEG4_CORE_SCALABLE = 10
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1636
try:
    FF_PROFILE_MPEG4_ADVANCED_CODING = 11
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1637
try:
    FF_PROFILE_MPEG4_ADVANCED_CORE = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1638
try:
    FF_PROFILE_MPEG4_ADVANCED_SCALABLE_TEXTURE = 13
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1639
try:
    FF_PROFILE_MPEG4_SIMPLE_STUDIO = 14
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1640
try:
    FF_PROFILE_MPEG4_ADVANCED_SIMPLE = 15
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1642
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_0 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1643
try:
    FF_PROFILE_JPEG2000_CSTREAM_RESTRICTION_1 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1644
try:
    FF_PROFILE_JPEG2000_CSTREAM_NO_RESTRICTION = 32768
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1645
try:
    FF_PROFILE_JPEG2000_DCINEMA_2K = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1646
try:
    FF_PROFILE_JPEG2000_DCINEMA_4K = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1648
try:
    FF_PROFILE_VP9_0 = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1649
try:
    FF_PROFILE_VP9_1 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1650
try:
    FF_PROFILE_VP9_2 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1651
try:
    FF_PROFILE_VP9_3 = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1653
try:
    FF_PROFILE_HEVC_MAIN = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1654
try:
    FF_PROFILE_HEVC_MAIN_10 = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1655
try:
    FF_PROFILE_HEVC_MAIN_STILL_PICTURE = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1656
try:
    FF_PROFILE_HEVC_REXT = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1658
try:
    FF_PROFILE_VVC_MAIN_10 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1659
try:
    FF_PROFILE_VVC_MAIN_10_444 = 33
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1661
try:
    FF_PROFILE_AV1_MAIN = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1662
try:
    FF_PROFILE_AV1_HIGH = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1663
try:
    FF_PROFILE_AV1_PROFESSIONAL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1665
try:
    FF_PROFILE_MJPEG_HUFFMAN_BASELINE_DCT = 0xc0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1666
try:
    FF_PROFILE_MJPEG_HUFFMAN_EXTENDED_SEQUENTIAL_DCT = 0xc1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1667
try:
    FF_PROFILE_MJPEG_HUFFMAN_PROGRESSIVE_DCT = 0xc2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1668
try:
    FF_PROFILE_MJPEG_HUFFMAN_LOSSLESS = 0xc3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1669
try:
    FF_PROFILE_MJPEG_JPEG_LS = 0xf7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1671
try:
    FF_PROFILE_SBC_MSBC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1673
try:
    FF_PROFILE_PRORES_PROXY = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1674
try:
    FF_PROFILE_PRORES_LT = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1675
try:
    FF_PROFILE_PRORES_STANDARD = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1676
try:
    FF_PROFILE_PRORES_HQ = 3
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1677
try:
    FF_PROFILE_PRORES_4444 = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1678
try:
    FF_PROFILE_PRORES_XQ = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1680
try:
    FF_PROFILE_ARIB_PROFILE_A = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1681
try:
    FF_PROFILE_ARIB_PROFILE_C = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1683
try:
    FF_PROFILE_KLVA_SYNC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1684
try:
    FF_PROFILE_KLVA_ASYNC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1692
try:
    FF_LEVEL_UNKNOWN = (-99)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1797
try:
    FF_SUB_CHARENC_MODE_DO_NOTHING = (-1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1798
try:
    FF_SUB_CHARENC_MODE_AUTOMATIC = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1799
try:
    FF_SUB_CHARENC_MODE_PRE_DECODER = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1800
try:
    FF_SUB_CHARENC_MODE_IGNORE = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1852
try:
    FF_CODEC_PROPERTY_LOSSLESS = 0x00000001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1853
try:
    FF_CODEC_PROPERTY_CLOSED_CAPTIONS = 0x00000002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 1854
try:
    FF_CODEC_PROPERTY_FILM_GRAIN = 0x00000004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2230
try:
    AV_HWACCEL_CODEC_CAP_EXPERIMENTAL = 0x0200
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2240
try:
    AV_HWACCEL_FLAG_IGNORE_LEVEL = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2246
try:
    AV_HWACCEL_FLAG_ALLOW_HIGH_DEPTH = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2260
try:
    AV_HWACCEL_FLAG_ALLOW_PROFILE_MISMATCH = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2276
try:
    AV_HWACCEL_FLAG_UNSAFE_OUTPUT = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2300
try:
    AV_SUBTITLE_FLAG_FORCED = 0x00000001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2839
try:
    AV_PARSER_PTS_NB = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2846
try:
    PARSER_FLAG_COMPLETE_FRAMES = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2847
try:
    PARSER_FLAG_ONCE = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2849
try:
    PARSER_FLAG_FETCHED_OFFSET = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2850
try:
    PARSER_FLAG_USE_CODEC_TS = 0x1000
except:
    pass

# /usr/include/libavutil/opt.h: 281
try:
    AV_OPT_FLAG_ENCODING_PARAM = 1
except:
    pass

# /usr/include/libavutil/opt.h: 282
try:
    AV_OPT_FLAG_DECODING_PARAM = 2
except:
    pass

# /usr/include/libavutil/opt.h: 283
try:
    AV_OPT_FLAG_AUDIO_PARAM = 8
except:
    pass

# /usr/include/libavutil/opt.h: 284
try:
    AV_OPT_FLAG_VIDEO_PARAM = 16
except:
    pass

# /usr/include/libavutil/opt.h: 285
try:
    AV_OPT_FLAG_SUBTITLE_PARAM = 32
except:
    pass

# /usr/include/libavutil/opt.h: 289
try:
    AV_OPT_FLAG_EXPORT = 64
except:
    pass

# /usr/include/libavutil/opt.h: 294
try:
    AV_OPT_FLAG_READONLY = 128
except:
    pass

# /usr/include/libavutil/opt.h: 295
try:
    AV_OPT_FLAG_BSF_PARAM = (1 << 8)
except:
    pass

# /usr/include/libavutil/opt.h: 296
try:
    AV_OPT_FLAG_RUNTIME_PARAM = (1 << 15)
except:
    pass

# /usr/include/libavutil/opt.h: 297
try:
    AV_OPT_FLAG_FILTERING_PARAM = (1 << 16)
except:
    pass

# /usr/include/libavutil/opt.h: 298
try:
    AV_OPT_FLAG_DEPRECATED = (1 << 17)
except:
    pass

# /usr/include/libavutil/opt.h: 299
try:
    AV_OPT_FLAG_CHILD_CONSTS = (1 << 18)
except:
    pass

# /usr/include/libavutil/opt.h: 563
try:
    AV_OPT_SEARCH_CHILDREN = (1 << 0)
except:
    pass

# /usr/include/libavutil/opt.h: 571
try:
    AV_OPT_SEARCH_FAKE_OBJ = (1 << 1)
except:
    pass

# /usr/include/libavutil/opt.h: 577
try:
    AV_OPT_ALLOW_NULL = (1 << 2)
except:
    pass

# /usr/include/libavutil/opt.h: 584
try:
    AV_OPT_MULTI_COMPONENT_RANGE = (1 << 12)
except:
    pass

# /usr/include/libavutil/opt.h: 721
def av_opt_set_int_list(obj, name, val, term, flags):
    return ((av_int_list_length (val, term)) > (INT_MAX / sizeof((val[0])))) and (AVERROR (EINVAL)) or (av_opt_set_bin (obj, name, cast(val, POINTER(uint8_t)), ((av_int_list_length (val, term)) * sizeof((val[0]))), flags))

# /usr/include/libavutil/opt.h: 864
try:
    AV_OPT_SERIALIZE_SKIP_DEFAULTS = 0x00000001
except:
    pass

# /usr/include/libavutil/opt.h: 865
try:
    AV_OPT_SERIALIZE_OPT_FLAGS_EXACT = 0x00000002
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

# /usr/include/time.h: 239
def __isleap(year):
    return (((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0)))

# /usr/include/libavformat/version_major.h: 32
try:
    LIBAVFORMAT_VERSION_MAJOR = 60
except:
    pass

# /usr/include/libavformat/avio.h: 41
try:
    AVIO_SEEKABLE_NORMAL = (1 << 0)
except:
    pass

# /usr/include/libavformat/avio.h: 46
try:
    AVIO_SEEKABLE_TIME = (1 << 1)
except:
    pass

# /usr/include/libavformat/avio.h: 474
try:
    AVSEEK_SIZE = 0x10000
except:
    pass

# /usr/include/libavformat/avio.h: 482
try:
    AVSEEK_FORCE = 0x20000
except:
    pass

# /usr/include/libavformat/avio.h: 623
try:
    AVIO_FLAG_READ = 1
except:
    pass

# /usr/include/libavformat/avio.h: 624
try:
    AVIO_FLAG_WRITE = 2
except:
    pass

# /usr/include/libavformat/avio.h: 625
try:
    AVIO_FLAG_READ_WRITE = (AVIO_FLAG_READ | AVIO_FLAG_WRITE)
except:
    pass

# /usr/include/libavformat/avio.h: 642
try:
    AVIO_FLAG_NONBLOCK = 8
except:
    pass

# /usr/include/libavformat/avio.h: 650
try:
    AVIO_FLAG_DIRECT = 0x8000
except:
    pass

# /usr/include/libavformat/version.h: 34
try:
    LIBAVFORMAT_VERSION_MINOR = 3
except:
    pass

# /usr/include/libavformat/version.h: 35
try:
    LIBAVFORMAT_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavformat/version.h: 37
try:
    LIBAVFORMAT_VERSION_INT = (AV_VERSION_INT (LIBAVFORMAT_VERSION_MAJOR, LIBAVFORMAT_VERSION_MINOR, LIBAVFORMAT_VERSION_MICRO))
except:
    pass

# /usr/include/libavformat/version.h: 43
try:
    LIBAVFORMAT_BUILD = LIBAVFORMAT_VERSION_INT
except:
    pass

# /usr/include/libavformat/avformat.h: 458
try:
    AVPROBE_SCORE_RETRY = (AVPROBE_SCORE_MAX / 4)
except:
    pass

# /usr/include/libavformat/avformat.h: 459
try:
    AVPROBE_SCORE_STREAM_RETRY = ((AVPROBE_SCORE_MAX / 4) - 1)
except:
    pass

# /usr/include/libavformat/avformat.h: 461
try:
    AVPROBE_SCORE_EXTENSION = 50
except:
    pass

# /usr/include/libavformat/avformat.h: 462
try:
    AVPROBE_SCORE_MIME = 75
except:
    pass

# /usr/include/libavformat/avformat.h: 463
try:
    AVPROBE_SCORE_MAX = 100
except:
    pass

# /usr/include/libavformat/avformat.h: 465
try:
    AVPROBE_PADDING_SIZE = 32
except:
    pass

# /usr/include/libavformat/avformat.h: 468
try:
    AVFMT_NOFILE = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 469
try:
    AVFMT_NEEDNUMBER = 0x0002
except:
    pass

# /usr/include/libavformat/avformat.h: 476
try:
    AVFMT_EXPERIMENTAL = 0x0004
except:
    pass

# /usr/include/libavformat/avformat.h: 477
try:
    AVFMT_SHOW_IDS = 0x0008
except:
    pass

# /usr/include/libavformat/avformat.h: 478
try:
    AVFMT_GLOBALHEADER = 0x0040
except:
    pass

# /usr/include/libavformat/avformat.h: 479
try:
    AVFMT_NOTIMESTAMPS = 0x0080
except:
    pass

# /usr/include/libavformat/avformat.h: 480
try:
    AVFMT_GENERIC_INDEX = 0x0100
except:
    pass

# /usr/include/libavformat/avformat.h: 481
try:
    AVFMT_TS_DISCONT = 0x0200
except:
    pass

# /usr/include/libavformat/avformat.h: 482
try:
    AVFMT_VARIABLE_FPS = 0x0400
except:
    pass

# /usr/include/libavformat/avformat.h: 483
try:
    AVFMT_NODIMENSIONS = 0x0800
except:
    pass

# /usr/include/libavformat/avformat.h: 484
try:
    AVFMT_NOSTREAMS = 0x1000
except:
    pass

# /usr/include/libavformat/avformat.h: 485
try:
    AVFMT_NOBINSEARCH = 0x2000
except:
    pass

# /usr/include/libavformat/avformat.h: 486
try:
    AVFMT_NOGENSEARCH = 0x4000
except:
    pass

# /usr/include/libavformat/avformat.h: 487
try:
    AVFMT_NO_BYTE_SEEK = 0x8000
except:
    pass

# /usr/include/libavformat/avformat.h: 488
try:
    AVFMT_ALLOW_FLUSH = 0x10000
except:
    pass

# /usr/include/libavformat/avformat.h: 489
try:
    AVFMT_TS_NONSTRICT = 0x20000
except:
    pass

# /usr/include/libavformat/avformat.h: 492
try:
    AVFMT_TS_NEGATIVE = 0x40000
except:
    pass

# /usr/include/libavformat/avformat.h: 501
try:
    AVFMT_SEEK_TO_PTS = 0x4000000
except:
    pass

# /usr/include/libavformat/avformat.h: 705
try:
    AVINDEX_KEYFRAME = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 706
try:
    AVINDEX_DISCARD_FRAME = 0x0002
except:
    pass

# /usr/include/libavformat/avformat.h: 718
try:
    AV_DISPOSITION_DEFAULT = (1 << 0)
except:
    pass

# /usr/include/libavformat/avformat.h: 726
try:
    AV_DISPOSITION_DUB = (1 << 1)
except:
    pass

# /usr/include/libavformat/avformat.h: 732
try:
    AV_DISPOSITION_ORIGINAL = (1 << 2)
except:
    pass

# /usr/include/libavformat/avformat.h: 736
try:
    AV_DISPOSITION_COMMENT = (1 << 3)
except:
    pass

# /usr/include/libavformat/avformat.h: 740
try:
    AV_DISPOSITION_LYRICS = (1 << 4)
except:
    pass

# /usr/include/libavformat/avformat.h: 744
try:
    AV_DISPOSITION_KARAOKE = (1 << 5)
except:
    pass

# /usr/include/libavformat/avformat.h: 751
try:
    AV_DISPOSITION_FORCED = (1 << 6)
except:
    pass

# /usr/include/libavformat/avformat.h: 755
try:
    AV_DISPOSITION_HEARING_IMPAIRED = (1 << 7)
except:
    pass

# /usr/include/libavformat/avformat.h: 759
try:
    AV_DISPOSITION_VISUAL_IMPAIRED = (1 << 8)
except:
    pass

# /usr/include/libavformat/avformat.h: 763
try:
    AV_DISPOSITION_CLEAN_EFFECTS = (1 << 9)
except:
    pass

# /usr/include/libavformat/avformat.h: 771
try:
    AV_DISPOSITION_ATTACHED_PIC = (1 << 10)
except:
    pass

# /usr/include/libavformat/avformat.h: 776
try:
    AV_DISPOSITION_TIMED_THUMBNAILS = (1 << 11)
except:
    pass

# /usr/include/libavformat/avformat.h: 783
try:
    AV_DISPOSITION_NON_DIEGETIC = (1 << 12)
except:
    pass

# /usr/include/libavformat/avformat.h: 789
try:
    AV_DISPOSITION_CAPTIONS = (1 << 16)
except:
    pass

# /usr/include/libavformat/avformat.h: 795
try:
    AV_DISPOSITION_DESCRIPTIONS = (1 << 17)
except:
    pass

# /usr/include/libavformat/avformat.h: 800
try:
    AV_DISPOSITION_METADATA = (1 << 18)
except:
    pass

# /usr/include/libavformat/avformat.h: 806
try:
    AV_DISPOSITION_DEPENDENT = (1 << 19)
except:
    pass

# /usr/include/libavformat/avformat.h: 810
try:
    AV_DISPOSITION_STILL_IMAGE = (1 << 20)
except:
    pass

# /usr/include/libavformat/avformat.h: 829
try:
    AV_PTS_WRAP_IGNORE = 0
except:
    pass

# /usr/include/libavformat/avformat.h: 830
try:
    AV_PTS_WRAP_ADD_OFFSET = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 831
try:
    AV_PTS_WRAP_SUB_OFFSET = (-1)
except:
    pass

# /usr/include/libavformat/avformat.h: 982
try:
    AVSTREAM_EVENT_FLAG_METADATA_UPDATED = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 988
try:
    AVSTREAM_EVENT_FLAG_NEW_PACKETS = (1 << 1)
except:
    pass

# /usr/include/libavformat/avformat.h: 1026
try:
    AV_PROGRAM_RUNNING = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1061
try:
    AVFMTCTX_NOHEADER = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 1063
try:
    AVFMTCTX_UNSEEKABLE = 0x0002
except:
    pass

# /usr/include/libavformat/avformat.h: 1229
try:
    AVFMT_FLAG_GENPTS = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 1230
try:
    AVFMT_FLAG_IGNIDX = 0x0002
except:
    pass

# /usr/include/libavformat/avformat.h: 1231
try:
    AVFMT_FLAG_NONBLOCK = 0x0004
except:
    pass

# /usr/include/libavformat/avformat.h: 1232
try:
    AVFMT_FLAG_IGNDTS = 0x0008
except:
    pass

# /usr/include/libavformat/avformat.h: 1233
try:
    AVFMT_FLAG_NOFILLIN = 0x0010
except:
    pass

# /usr/include/libavformat/avformat.h: 1234
try:
    AVFMT_FLAG_NOPARSE = 0x0020
except:
    pass

# /usr/include/libavformat/avformat.h: 1235
try:
    AVFMT_FLAG_NOBUFFER = 0x0040
except:
    pass

# /usr/include/libavformat/avformat.h: 1236
try:
    AVFMT_FLAG_CUSTOM_IO = 0x0080
except:
    pass

# /usr/include/libavformat/avformat.h: 1237
try:
    AVFMT_FLAG_DISCARD_CORRUPT = 0x0100
except:
    pass

# /usr/include/libavformat/avformat.h: 1238
try:
    AVFMT_FLAG_FLUSH_PACKETS = 0x0200
except:
    pass

# /usr/include/libavformat/avformat.h: 1245
try:
    AVFMT_FLAG_BITEXACT = 0x0400
except:
    pass

# /usr/include/libavformat/avformat.h: 1246
try:
    AVFMT_FLAG_SORT_DTS = 0x10000
except:
    pass

# /usr/include/libavformat/avformat.h: 1247
try:
    AVFMT_FLAG_FAST_SEEK = 0x80000
except:
    pass

# /usr/include/libavformat/avformat.h: 1248
try:
    AVFMT_FLAG_SHORTEST = 0x100000
except:
    pass

# /usr/include/libavformat/avformat.h: 1249
try:
    AVFMT_FLAG_AUTO_BSF = 0x200000
except:
    pass

# /usr/include/libavformat/avformat.h: 1380
try:
    FF_FDEBUG_TS = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 1424
try:
    AVFMT_EVENT_FLAG_METADATA_UPDATED = 0x0001
except:
    pass

# /usr/include/libavformat/avformat.h: 1440
try:
    AVFMT_AVOID_NEG_TS_AUTO = (-1)
except:
    pass

# /usr/include/libavformat/avformat.h: 1441
try:
    AVFMT_AVOID_NEG_TS_DISABLED = 0
except:
    pass

# /usr/include/libavformat/avformat.h: 1442
try:
    AVFMT_AVOID_NEG_TS_MAKE_NON_NEGATIVE = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 1443
try:
    AVFMT_AVOID_NEG_TS_MAKE_ZERO = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 2200
try:
    AVSEEK_FLAG_BACKWARD = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 2201
try:
    AVSEEK_FLAG_BYTE = 2
except:
    pass

# /usr/include/libavformat/avformat.h: 2202
try:
    AVSEEK_FLAG_ANY = 4
except:
    pass

# /usr/include/libavformat/avformat.h: 2203
try:
    AVSEEK_FLAG_FRAME = 8
except:
    pass

# /usr/include/libavformat/avformat.h: 2210
try:
    AVSTREAM_INIT_IN_WRITE_HEADER = 0
except:
    pass

# /usr/include/libavformat/avformat.h: 2211
try:
    AVSTREAM_INIT_IN_INIT_OUTPUT = 1
except:
    pass

# /usr/include/libavformat/avformat.h: 2646
try:
    AV_FRAME_FILENAME_FLAGS_MULTIPLE = 1
except:
    pass

# /usr/include/libavfilter/version_major.h: 30
try:
    LIBAVFILTER_VERSION_MAJOR = 9
except:
    pass

# /usr/include/libavfilter/version.h: 34
try:
    LIBAVFILTER_VERSION_MINOR = 3
except:
    pass

# /usr/include/libavfilter/version.h: 35
try:
    LIBAVFILTER_VERSION_MICRO = 100
except:
    pass

# /usr/include/libavfilter/version.h: 38
try:
    LIBAVFILTER_VERSION_INT = (AV_VERSION_INT (LIBAVFILTER_VERSION_MAJOR, LIBAVFILTER_VERSION_MINOR, LIBAVFILTER_VERSION_MICRO))
except:
    pass

# /usr/include/libavfilter/version.h: 44
try:
    LIBAVFILTER_BUILD = LIBAVFILTER_VERSION_INT
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 106
try:
    AVFILTER_FLAG_DYNAMIC_INPUTS = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 112
try:
    AVFILTER_FLAG_DYNAMIC_OUTPUTS = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 117
try:
    AVFILTER_FLAG_SLICE_THREADS = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 133
try:
    AVFILTER_FLAG_METADATA_ONLY = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 142
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 150
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL = (1 << 17)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 155
try:
    AVFILTER_FLAG_SUPPORT_TIMELINE = (AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC | AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 387
try:
    AVFILTER_THREAD_SLICE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 733
try:
    AVFILTER_CMD_FLAG_ONE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avfilter.h: 734
try:
    AVFILTER_CMD_FLAG_FAST = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 330
try:
    AV_ESCAPE_FLAG_WHITESPACE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 337
try:
    AV_ESCAPE_FLAG_STRICT = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 343
try:
    AV_ESCAPE_FLAG_XML_SINGLE_QUOTES = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 349
try:
    AV_ESCAPE_FLAG_XML_DOUBLE_QUOTES = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 372
try:
    AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 373
try:
    AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 374
try:
    AV_UTF8_FLAG_ACCEPT_SURROGATES = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 375
try:
    AV_UTF8_FLAG_EXCLUDE_XML_INVALID_CONTROL_CODES = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/avstring.h: 377
try:
    AV_UTF8_FLAG_ACCEPT_ALL = ((AV_UTF8_FLAG_ACCEPT_INVALID_BIG_CODES | AV_UTF8_FLAG_ACCEPT_NON_CHARACTERS) | AV_UTF8_FLAG_ACCEPT_SURROGATES)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/base64.h: 48
def AV_BASE64_DECODE_SIZE(x):
    return ((x * 3) / 4)

# /home/josiah/ctypesgen_test/av/av/base64.h: 66
def AV_BASE64_SIZE(x):
    return ((((x + 2) / 3) * 4) + 1)

# /home/josiah/ctypesgen_test/av/av/blowfish.h: 33
try:
    AV_BF_ROUNDS = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/bprint.h: 111
try:
    AV_BPRINT_SIZE_UNLIMITED = (c_uint (ord_if_char((-1)))).value
except:
    pass

# /home/josiah/ctypesgen_test/av/av/bprint.h: 118
try:
    AV_BPRINT_SIZE_AUTOMATIC = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/bprint.h: 125
try:
    AV_BPRINT_SIZE_COUNT_ONLY = 0
except:
    pass

# /home/josiah/ctypesgen_test/av/av/bswap.h: 53
def AV_BSWAP16C(x):
    return (((x << 8) & 0xff00) | ((x >> 8) & 0x00ff))

# /home/josiah/ctypesgen_test/av/av/bswap.h: 54
def AV_BSWAP32C(x):
    return (((AV_BSWAP16C (x)) << 16) | (AV_BSWAP16C ((x >> 16))))

# /home/josiah/ctypesgen_test/av/av/bswap.h: 55
def AV_BSWAP64C(x):
    return (((AV_BSWAP32C (x)) << 32) | (AV_BSWAP32C ((x >> 32))))

# /home/josiah/ctypesgen_test/av/av/bswap.h: 97
def av_le2ne16(x):
    return x

# /home/josiah/ctypesgen_test/av/av/bswap.h: 98
def av_le2ne32(x):
    return x

# /home/josiah/ctypesgen_test/av/av/bswap.h: 99
def av_le2ne64(x):
    return x

# /home/josiah/ctypesgen_test/av/av/bswap.h: 101
def AV_LE2NEC(s, x):
    return x

# /home/josiah/ctypesgen_test/av/av/bswap.h: 107
def AV_LE2NE16C(x):
    return (AV_LE2NEC (16, x))

# /home/josiah/ctypesgen_test/av/av/bswap.h: 108
def AV_LE2NE32C(x):
    return (AV_LE2NEC (32, x))

# /home/josiah/ctypesgen_test/av/av/bswap.h: 109
def AV_LE2NE64C(x):
    return (AV_LE2NEC (64, x))

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 88
try:
    AV_BUFFERSINK_FLAG_PEEK = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/buffersink.h: 95
try:
    AV_BUFFERSINK_FLAG_NO_REQUEST = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 26
try:
    AV_CPU_FLAG_FORCE = 0x80000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 29
try:
    AV_CPU_FLAG_MMX = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 30
try:
    AV_CPU_FLAG_MMXEXT = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 31
try:
    AV_CPU_FLAG_MMX2 = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 32
try:
    AV_CPU_FLAG_3DNOW = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 33
try:
    AV_CPU_FLAG_SSE = 0x0008
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 34
try:
    AV_CPU_FLAG_SSE2 = 0x0010
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 35
try:
    AV_CPU_FLAG_SSE2SLOW = 0x40000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 37
try:
    AV_CPU_FLAG_3DNOWEXT = 0x0020
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 38
try:
    AV_CPU_FLAG_SSE3 = 0x0040
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 39
try:
    AV_CPU_FLAG_SSE3SLOW = 0x20000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 41
try:
    AV_CPU_FLAG_SSSE3 = 0x0080
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 42
try:
    AV_CPU_FLAG_SSSE3SLOW = 0x4000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 43
try:
    AV_CPU_FLAG_ATOM = 0x10000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 44
try:
    AV_CPU_FLAG_SSE4 = 0x0100
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 45
try:
    AV_CPU_FLAG_SSE42 = 0x0200
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 46
try:
    AV_CPU_FLAG_AESNI = 0x80000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 47
try:
    AV_CPU_FLAG_AVX = 0x4000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 48
try:
    AV_CPU_FLAG_AVXSLOW = 0x8000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 49
try:
    AV_CPU_FLAG_XOP = 0x0400
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 50
try:
    AV_CPU_FLAG_FMA4 = 0x0800
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 51
try:
    AV_CPU_FLAG_CMOV = 0x1000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 52
try:
    AV_CPU_FLAG_AVX2 = 0x8000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 53
try:
    AV_CPU_FLAG_FMA3 = 0x10000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 54
try:
    AV_CPU_FLAG_BMI1 = 0x20000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 55
try:
    AV_CPU_FLAG_BMI2 = 0x40000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 56
try:
    AV_CPU_FLAG_AVX512 = 0x100000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 57
try:
    AV_CPU_FLAG_AVX512ICL = 0x200000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 58
try:
    AV_CPU_FLAG_SLOW_GATHER = 0x2000000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 60
try:
    AV_CPU_FLAG_ALTIVEC = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 61
try:
    AV_CPU_FLAG_VSX = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 62
try:
    AV_CPU_FLAG_POWER8 = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 64
try:
    AV_CPU_FLAG_ARMV5TE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 65
try:
    AV_CPU_FLAG_ARMV6 = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 66
try:
    AV_CPU_FLAG_ARMV6T2 = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 67
try:
    AV_CPU_FLAG_VFP = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 68
try:
    AV_CPU_FLAG_VFPV3 = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 69
try:
    AV_CPU_FLAG_NEON = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 70
try:
    AV_CPU_FLAG_ARMV8 = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 71
try:
    AV_CPU_FLAG_VFP_VM = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 72
try:
    AV_CPU_FLAG_SETEND = (1 << 16)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 74
try:
    AV_CPU_FLAG_MMI = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 75
try:
    AV_CPU_FLAG_MSA = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 78
try:
    AV_CPU_FLAG_LSX = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 79
try:
    AV_CPU_FLAG_LASX = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 82
try:
    AV_CPU_FLAG_RVI = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 83
try:
    AV_CPU_FLAG_RVF = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 84
try:
    AV_CPU_FLAG_RVD = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 85
try:
    AV_CPU_FLAG_RVV_I32 = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 86
try:
    AV_CPU_FLAG_RVV_F32 = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 87
try:
    AV_CPU_FLAG_RVV_I64 = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 88
try:
    AV_CPU_FLAG_RVV_F64 = (1 << 6)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/cpu.h: 89
try:
    AV_CPU_FLAG_RVB_BASIC = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/dirac.h: 45
try:
    MAX_DWT_LEVELS = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 103
try:
    AV_DOVI_MAX_PIECES = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 29
try:
    DV_PROFILE_BYTES = (6 * 80)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/ffversion.h: 4
try:
    FFMPEG_VERSION = 'n6.0'
except:
    pass

# /home/josiah/ctypesgen_test/av/av/fifo.h: 67
try:
    AV_FIFO_FLAG_AUTO_GROW = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/hash.h: 156
try:
    AV_HASH_MAX_SIZE = 64
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 116
try:
    AV_PIX_FMT_FLAG_BE = (1 << 0)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 120
try:
    AV_PIX_FMT_FLAG_PAL = (1 << 1)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 124
try:
    AV_PIX_FMT_FLAG_BITSTREAM = (1 << 2)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 128
try:
    AV_PIX_FMT_FLAG_HWACCEL = (1 << 3)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 132
try:
    AV_PIX_FMT_FLAG_PLANAR = (1 << 4)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 136
try:
    AV_PIX_FMT_FLAG_RGB = (1 << 5)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 147
try:
    AV_PIX_FMT_FLAG_ALPHA = (1 << 7)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 152
try:
    AV_PIX_FMT_FLAG_BAYER = (1 << 8)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 158
try:
    AV_PIX_FMT_FLAG_FLOAT = (1 << 9)
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 382
try:
    FF_LOSS_RESOLUTION = 0x0001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 383
try:
    FF_LOSS_DEPTH = 0x0002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 384
try:
    FF_LOSS_COLORSPACE = 0x0004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 385
try:
    FF_LOSS_ALPHA = 0x0008
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 386
try:
    FF_LOSS_COLORQUANT = 0x0010
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 387
try:
    FF_LOSS_CHROMA = 0x0020
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 388
try:
    FF_LOSS_EXCESS_RESOLUTION = 0x0040
except:
    pass

# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 389
try:
    FF_LOSS_EXCESS_DEPTH = 0x0080
except:
    pass

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 395
def AV_RB8(x):
    return (cast(x, POINTER(uint8_t)) [0])

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 398
def AV_RL8(x):
    return (AV_RB8 (x))

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 444
def AV_RB24(x):
    return ((((cast(x, POINTER(uint8_t)) [0]) << 16) | ((cast(x, POINTER(uint8_t)) [1]) << 8)) | (cast(x, POINTER(uint8_t)) [2]))

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 458
def AV_RL24(x):
    return ((((cast(x, POINTER(uint8_t)) [2]) << 16) | ((cast(x, POINTER(uint8_t)) [1]) << 8)) | (cast(x, POINTER(uint8_t)) [0]))

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 472
def AV_RB48(x):
    return (((((((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [0])))).value << 40) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [1])))).value << 32)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [2])))).value << 24)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [3])))).value << 16)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [4])))).value << 8)) | (uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [5])))).value)

# /home/josiah/ctypesgen_test/av/av/intreadwrite.h: 493
def AV_RL48(x):
    return (((((((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [5])))).value << 40) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [4])))).value << 32)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [3])))).value << 24)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [2])))).value << 16)) | ((uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [1])))).value << 8)) | (uint64_t (ord_if_char((cast(x, POINTER(uint8_t)) [0])))).value)

# /home/josiah/ctypesgen_test/av/av/lzo.h: 37
try:
    AV_LZO_INPUT_DEPLETED = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/lzo.h: 39
try:
    AV_LZO_OUTPUT_FULL = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/lzo.h: 41
try:
    AV_LZO_INVALID_BACKPTR = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/lzo.h: 43
try:
    AV_LZO_ERROR = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/lzo.h: 46
try:
    AV_LZO_INPUT_PADDING = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/lzo.h: 47
try:
    AV_LZO_OUTPUT_PADDING = 12
except:
    pass

# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 164
try:
    AV_STEREO3D_FLAG_INVERT = (1 << 0)
except:
    pass

# /usr/include/libswresample/version_major.h: 29
try:
    LIBSWRESAMPLE_VERSION_MAJOR = 4
except:
    pass

# /usr/include/libswresample/version.h: 33
try:
    LIBSWRESAMPLE_VERSION_MINOR = 10
except:
    pass

# /usr/include/libswresample/version.h: 34
try:
    LIBSWRESAMPLE_VERSION_MICRO = 100
except:
    pass

# /usr/include/libswresample/version.h: 36
try:
    LIBSWRESAMPLE_VERSION_INT = (AV_VERSION_INT (LIBSWRESAMPLE_VERSION_MAJOR, LIBSWRESAMPLE_VERSION_MINOR, LIBSWRESAMPLE_VERSION_MICRO))
except:
    pass

# /usr/include/libswresample/version.h: 42
try:
    LIBSWRESAMPLE_BUILD = LIBSWRESAMPLE_VERSION_INT
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swresample.h: 143
try:
    SWR_FLAG_RESAMPLE = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 65
try:
    SWS_FAST_BILINEAR = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 66
try:
    SWS_BILINEAR = 2
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 67
try:
    SWS_BICUBIC = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 68
try:
    SWS_X = 8
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 69
try:
    SWS_POINT = 0x10
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 70
try:
    SWS_AREA = 0x20
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 71
try:
    SWS_BICUBLIN = 0x40
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 72
try:
    SWS_GAUSS = 0x80
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 73
try:
    SWS_SINC = 0x100
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 74
try:
    SWS_LANCZOS = 0x200
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 75
try:
    SWS_SPLINE = 0x400
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 77
try:
    SWS_SRC_V_CHR_DROP_MASK = 0x30000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 78
try:
    SWS_SRC_V_CHR_DROP_SHIFT = 16
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 80
try:
    SWS_PARAM_DEFAULT = 123456
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 82
try:
    SWS_PRINT_INFO = 0x1000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 86
try:
    SWS_FULL_CHR_H_INT = 0x2000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 88
try:
    SWS_FULL_CHR_H_INP = 0x4000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 89
try:
    SWS_DIRECT_BGR = 0x8000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 90
try:
    SWS_ACCURATE_RND = 0x40000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 91
try:
    SWS_BITEXACT = 0x80000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 92
try:
    SWS_ERROR_DIFFUSION = 0x800000
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 94
try:
    SWS_MAX_REDUCE_CUTOFF = 0.002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 96
try:
    SWS_CS_ITU709 = 1
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 97
try:
    SWS_CS_FCC = 4
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 98
try:
    SWS_CS_ITU601 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 99
try:
    SWS_CS_ITU624 = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 100
try:
    SWS_CS_SMPTE170M = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 101
try:
    SWS_CS_SMPTE240M = 7
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 102
try:
    SWS_CS_DEFAULT = 5
except:
    pass

# /home/josiah/ctypesgen_test/av/av/swscale.h: 103
try:
    SWS_CS_BT2020 = 9
except:
    pass

# /home/josiah/ctypesgen_test/av/av/timecode.h: 33
try:
    AV_TIMECODE_STR_SIZE = 23
except:
    pass

# /home/josiah/ctypesgen_test/av/av/timestamp.h: 33
try:
    AV_TS_MAX_STRING_SIZE = 32
except:
    pass

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 44
try:
    VORBIS_FLAG_HEADER = 0x00000001
except:
    pass

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 45
try:
    VORBIS_FLAG_COMMENT = 0x00000002
except:
    pass

# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 46
try:
    VORBIS_FLAG_SETUP = 0x00000004
except:
    pass

# /home/josiah/ctypesgen_test/av/av/xvmc.h: 44
try:
    AV_XVMC_ID = 0x1DC711C0
except:
    pass

AVAESCTR = struct_AVAESCTR# /home/josiah/ctypesgen_test/av/av/aes_ctr.h: 38

AVAES = struct_AVAES# /home/josiah/ctypesgen_test/av/av/aes.h: 36

AVAudioFifo = struct_AVAudioFifo# /home/josiah/ctypesgen_test/av/av/audio_fifo.h: 48

AVOptionRanges = struct_AVOptionRanges# /usr/include/libavutil/opt.h: 336

AVOption = struct_AVOption# /usr/include/libavutil/opt.h: 251

AVClass = struct_AVClass# /home/josiah/ctypesgen_test/av/av/log.h: 66

AVRational = struct_AVRational# /usr/include/libavutil/rational.h: 61

av_intfloat32 = union_av_intfloat32# /usr/include/libavutil/intfloat.h: 27

av_intfloat64 = union_av_intfloat64# /usr/include/libavutil/intfloat.h: 32

AVBuffer = struct_AVBuffer# /usr/include/libavutil/buffer.h: 74

AVBufferRef = struct_AVBufferRef# /usr/include/libavutil/buffer.h: 95

AVBufferPool = struct_AVBufferPool# /usr/include/libavutil/buffer.h: 255

AVDictionaryEntry = struct_AVDictionaryEntry# /usr/include/libavutil/dict.h: 92

AVDictionary = struct_AVDictionary# /usr/include/libavutil/dict.h: 94

AVChannelCustom = struct_AVChannelCustom# /usr/include/libavutil/channel_layout.h: 269

AVChannelLayout = struct_AVChannelLayout# /usr/include/libavutil/channel_layout.h: 359

AVBPrint = struct_AVBPrint# /home/josiah/ctypesgen_test/av/av/bprint.h: 93

AVFrameSideData = struct_AVFrameSideData# /usr/include/libavutil/frame.h: 242

AVRegionOfInterest = struct_AVRegionOfInterest# /usr/include/libavutil/frame.h: 298

AVFrame = struct_AVFrame# /usr/include/libavutil/frame.h: 729

AVHWDeviceInternal = struct_AVHWDeviceInternal# /usr/include/libavutil/hwcontext.h: 42

AVHWDeviceContext = struct_AVHWDeviceContext# /usr/include/libavutil/hwcontext.h: 61

AVHWFramesInternal = struct_AVHWFramesInternal# /usr/include/libavutil/hwcontext.h: 112

AVHWFramesContext = struct_AVHWFramesContext# /usr/include/libavutil/hwcontext.h: 124

AVHWFramesConstraints = struct_AVHWFramesConstraints# /usr/include/libavutil/hwcontext.h: 480

AVProfile = struct_AVProfile# /home/josiah/ctypesgen_test/av/av/codec.h: 179

AVCodec = struct_AVCodec# /home/josiah/ctypesgen_test/av/av/codec.h: 235

AVCodecHWConfig = struct_AVCodecHWConfig# /home/josiah/ctypesgen_test/av/av/codec.h: 360

AVCodecDescriptor = struct_AVCodecDescriptor# /home/josiah/ctypesgen_test/av/av/codec_desc.h: 66

AVCodecParameters = struct_AVCodecParameters# /home/josiah/ctypesgen_test/av/av/codec_par.h: 214

AVPacketSideData = struct_AVPacketSideData# /home/josiah/ctypesgen_test/av/av/packet.h: 319

AVPacket = struct_AVPacket# /home/josiah/ctypesgen_test/av/av/packet.h: 419

AVPacketList = struct_AVPacketList# /home/josiah/ctypesgen_test/av/av/packet.h: 423

RcOverride = struct_RcOverride# /home/josiah/ctypesgen_test/av/av/avcodec.h: 201

AVCodecInternal = struct_AVCodecInternal# /home/josiah/ctypesgen_test/av/av/avcodec.h: 411

AVCodecContext = struct_AVCodecContext# /home/josiah/ctypesgen_test/av/av/avcodec.h: 426

AVHWAccel = struct_AVHWAccel# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2076

AVSubtitleRect = struct_AVSubtitleRect# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2328

AVSubtitle = struct_AVSubtitle# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2337

AVCodecParser = struct_AVCodecParser# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2971

AVCodecParserContext = struct_AVCodecParserContext# /home/josiah/ctypesgen_test/av/av/avcodec.h: 2969

AVOptionRange = struct_AVOptionRange# /usr/include/libavutil/opt.h: 331

AVDCT = struct_AVDCT# /home/josiah/ctypesgen_test/av/av/avdct.h: 74

sigevent = struct_sigevent# /usr/include/time.h: 49

AVIOInterruptCB = struct_AVIOInterruptCB# /usr/include/libavformat/avio.h: 62

AVIODirEntry = struct_AVIODirEntry# /usr/include/libavformat/avio.h: 102

URLContext = struct_URLContext# /usr/include/libavformat/avio.h: 106

AVIODirContext = struct_AVIODirContext# /usr/include/libavformat/avio.h: 107

AVIOContext = struct_AVIOContext# /usr/include/libavformat/avio.h: 313

AVFormatContext = struct_AVFormatContext# /usr/include/libavformat/avformat.h: 1110

AVDeviceInfoList = struct_AVDeviceInfoList# /home/josiah/ctypesgen_test/av/av/avdevice.h: 343

AVCodecTag = struct_AVCodecTag# /usr/include/libavformat/avformat.h: 446

AVProbeData = struct_AVProbeData# /usr/include/libavformat/avformat.h: 456

AVOutputFormat = struct_AVOutputFormat# /usr/include/libavformat/avformat.h: 537

AVInputFormat = struct_AVInputFormat# /usr/include/libavformat/avformat.h: 681

AVIndexEntry = struct_AVIndexEntry# /usr/include/libavformat/avformat.h: 712

AVStream = struct_AVStream# /usr/include/libavformat/avformat.h: 1008

AVProgram = struct_AVProgram# /usr/include/libavformat/avformat.h: 1059

AVChapter = struct_AVChapter# /usr/include/libavformat/avformat.h: 1074

AVDeviceRect = struct_AVDeviceRect# /home/josiah/ctypesgen_test/av/av/avdevice.h: 120

AVDeviceInfo = struct_AVDeviceInfo# /home/josiah/ctypesgen_test/av/av/avdevice.h: 338

FFTComplex = struct_FFTComplex# /home/josiah/ctypesgen_test/av/av/avfft.h: 39

FFTContext = struct_FFTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 41

RDFTContext = struct_RDFTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 78

DCTContext = struct_DCTContext# /home/josiah/ctypesgen_test/av/av/avfft.h: 91

AVFilterContext = struct_AVFilterContext# /home/josiah/ctypesgen_test/av/av/avfilter.h: 392

AVFilterLink = struct_AVFilterLink# /home/josiah/ctypesgen_test/av/av/avfilter.h: 522

AVFilterPad = struct_AVFilterPad# /home/josiah/ctypesgen_test/av/av/avfilter.h: 75

AVFilterFormats = struct_AVFilterFormats# /home/josiah/ctypesgen_test/av/av/avfilter.h: 76

AVFilterChannelLayouts = struct_AVFilterChannelLayouts# /home/josiah/ctypesgen_test/av/av/avfilter.h: 77

AVFilter = struct_AVFilter# /home/josiah/ctypesgen_test/av/av/avfilter.h: 377

AVFilterInternal = struct_AVFilterInternal# /home/josiah/ctypesgen_test/av/av/avfilter.h: 389

AVFilterGraph = struct_AVFilterGraph# /home/josiah/ctypesgen_test/av/av/avfilter.h: 855

AVFilterCommand = struct_AVFilterCommand# /home/josiah/ctypesgen_test/av/av/avfilter.h: 434

AVFilterFormatsConfig = struct_AVFilterFormatsConfig# /home/josiah/ctypesgen_test/av/av/avfilter.h: 508

AVFilterGraphInternal = struct_AVFilterGraphInternal# /home/josiah/ctypesgen_test/av/av/avfilter.h: 824

AVFilterInOut = struct_AVFilterInOut# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1015

AVFilterPadParams = struct_AVFilterPadParams# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1126

AVFilterParams = struct_AVFilterParams# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1193

AVFilterChain = struct_AVFilterChain# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1204

AVFilterGraphSegment = struct_AVFilterGraphSegment# /home/josiah/ctypesgen_test/av/av/avfilter.h: 1238

AVBlowfish = struct_AVBlowfish# /home/josiah/ctypesgen_test/av/av/blowfish.h: 38

ff_pad_helper_AVBPrint = struct_ff_pad_helper_AVBPrint# /home/josiah/ctypesgen_test/av/av/bprint.h: 93

AVBitStreamFilter = struct_AVBitStreamFilter# /home/josiah/ctypesgen_test/av/av/bsf.h: 111

AVBSFContext = struct_AVBSFContext# /home/josiah/ctypesgen_test/av/av/bsf.h: 109

AVBSFList = struct_AVBSFList# /home/josiah/ctypesgen_test/av/av/bsf.h: 247

AVBufferSrcParameters = struct_AVBufferSrcParameters# /home/josiah/ctypesgen_test/av/av/buffersrc.h: 126

AVCAMELLIA = struct_AVCAMELLIA# /home/josiah/ctypesgen_test/av/av/camellia.h: 38

AVCAST5 = struct_AVCAST5# /home/josiah/ctypesgen_test/av/av/cast5.h: 38

AVDES = struct_AVDES# /home/josiah/ctypesgen_test/av/av/des.h: 36

DiracVersionInfo = struct_DiracVersionInfo# /home/josiah/ctypesgen_test/av/av/dirac.h: 79

AVDiracSeqHeader = struct_AVDiracSeqHeader# /home/josiah/ctypesgen_test/av/av/dirac.h: 114

AVDOVIDecoderConfigurationRecord = struct_AVDOVIDecoderConfigurationRecord# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 61

AVDOVIRpuDataHeader = struct_AVDOVIRpuDataHeader# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 92

AVDOVIReshapingCurve = struct_AVDOVIReshapingCurve# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 115

AVDOVINLQParams = struct_AVDOVINLQParams# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 132

AVDOVIDataMapping = struct_AVDOVIDataMapping# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 150

AVDOVIColorMetadata = struct_AVDOVIColorMetadata# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 187

AVDOVIMetadata = struct_AVDOVIMetadata# /home/josiah/ctypesgen_test/av/av/dovi_meta.h: 205

AVDownmixInfo = struct_AVDownmixInfo# /home/josiah/ctypesgen_test/av/av/downmix_info.h: 93

AVDVProfile = struct_AVDVProfile# /home/josiah/ctypesgen_test/av/av/dv_profile.h: 58

AVSubsampleEncryptionInfo = struct_AVSubsampleEncryptionInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 35

AVEncryptionInfo = struct_AVEncryptionInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 81

AVEncryptionInitInfo = struct_AVEncryptionInitInfo# /home/josiah/ctypesgen_test/av/av/encryption_info.h: 88

AVExpr = struct_AVExpr# /home/josiah/ctypesgen_test/av/av/eval.h: 29

AVFifo = struct_AVFifo# /home/josiah/ctypesgen_test/av/av/fifo.h: 42

AVFifoBuffer = struct_AVFifoBuffer# /home/josiah/ctypesgen_test/av/av/fifo.h: 248

AVFilmGrainAOMParams = struct_AVFilmGrainAOMParams# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 123

AVFilmGrainH274Params = struct_AVFilmGrainH274Params# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 206

AVFilmGrainParams = struct_AVFilmGrainParams# /home/josiah/ctypesgen_test/av/av/film_grain_params.h: 239

AVHashContext = struct_AVHashContext# /home/josiah/ctypesgen_test/av/av/hash.h: 115

AVHDRPlusPercentile = struct_AVHDRPlusPercentile# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 53

AVHDRPlusColorTransformParams = struct_AVHDRPlusColorTransformParams# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 230

AVDynamicHDRPlus = struct_AVDynamicHDRPlus# /home/josiah/ctypesgen_test/av/av/hdr_dynamic_metadata.h: 323

AVHMAC = struct_AVHMAC# /home/josiah/ctypesgen_test/av/av/hmac.h: 41

AVDRMObjectDescriptor = struct_AVDRMObjectDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 66

AVDRMPlaneDescriptor = struct_AVDRMPlaneDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 88

AVDRMLayerDescriptor = struct_AVDRMLayerDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 111

AVDRMFrameDescriptor = struct_AVDRMFrameDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 150

AVDRMDeviceContext = struct_AVDRMDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_drm.h: 167

AVMediaCodecDeviceContext = struct_AVMediaCodecDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_mediacodec.h: 59

AVOpenCLFrameDescriptor = struct_AVOpenCLFrameDescriptor# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 56

AVOpenCLDeviceContext = struct_AVOpenCLDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 82

AVOpenCLFramesContext = struct_AVOpenCLFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_opencl.h: 98

AVVAAPIDeviceContext = struct_AVVAAPIDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 81

AVVAAPIFramesContext = struct_AVVAAPIFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 103

AVVAAPIHWConfig = struct_AVVAAPIHWConfig# /home/josiah/ctypesgen_test/av/av/hwcontext_vaapi.h: 115

AVVDPAUDeviceContext = struct_AVVDPAUDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vdpau.h: 38

AVVulkanDeviceContext = struct_AVVulkanDeviceContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 138

AVVulkanFramesContext = struct_AVVulkanFramesContext# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 198

AVVkFrameInternal = struct_AVVkFrameInternal# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 261

AVVkFrame = struct_AVVkFrame# /home/josiah/ctypesgen_test/av/av/hwcontext_vulkan.h: 267

AVComponentDescriptor = struct_AVComponentDescriptor# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 58

AVPixFmtDescriptor = struct_AVPixFmtDescriptor# /home/josiah/ctypesgen_test/av/av/pixdesc.h: 111

AVLFG = struct_AVLFG# /home/josiah/ctypesgen_test/av/av/lfg.h: 36

AVMasteringDisplayMetadata = struct_AVMasteringDisplayMetadata# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 69

AVContentLightMetadata = struct_AVContentLightMetadata# /home/josiah/ctypesgen_test/av/av/mastering_display_metadata.h: 108

AVMD5 = struct_AVMD5# /home/josiah/ctypesgen_test/av/av/md5.h: 45

AVMediaCodecContext = struct_AVMediaCodecContext# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 40

MediaCodecBuffer = struct_MediaCodecBuffer# /home/josiah/ctypesgen_test/av/av/mediacodec.h: 73

AVMotionVector = struct_AVMotionVector# /home/josiah/ctypesgen_test/av/av/motion_vector.h: 55

AVMurMur3 = struct_AVMurMur3# /home/josiah/ctypesgen_test/av/av/murmur3.h: 67

AVRC4 = struct_AVRC4# /home/josiah/ctypesgen_test/av/av/rc4.h: 35

AVReplayGain = struct_AVReplayGain# /home/josiah/ctypesgen_test/av/av/replaygain.h: 48

AVRIPEMD = struct_AVRIPEMD# /home/josiah/ctypesgen_test/av/av/ripemd.h: 46

AVSHA512 = struct_AVSHA512# /home/josiah/ctypesgen_test/av/av/sha512.h: 55

AVSHA = struct_AVSHA# /home/josiah/ctypesgen_test/av/av/sha.h: 53

AVSphericalMapping = struct_AVSphericalMapping# /home/josiah/ctypesgen_test/av/av/spherical.h: 179

AVStereo3D = struct_AVStereo3D# /home/josiah/ctypesgen_test/av/av/stereo3d.h: 188

SwrContext = struct_SwrContext# /home/josiah/ctypesgen_test/av/av/swresample.h: 189

SwsVector = struct_SwsVector# /home/josiah/ctypesgen_test/av/av/swscale.h: 119

SwsFilter = struct_SwsFilter# /home/josiah/ctypesgen_test/av/av/swscale.h: 127

SwsContext = struct_SwsContext# /home/josiah/ctypesgen_test/av/av/swscale.h: 129

AVTEA = struct_AVTEA# /home/josiah/ctypesgen_test/av/av/tea.h: 37

AVThreadMessageQueue = struct_AVThreadMessageQueue# /home/josiah/ctypesgen_test/av/av/threadmessage.h: 22

AVTreeNode = struct_AVTreeNode# /home/josiah/ctypesgen_test/av/av/tree.h: 44

AVTWOFISH = struct_AVTWOFISH# /home/josiah/ctypesgen_test/av/av/twofish.h: 38

AVTXContext = struct_AVTXContext# /home/josiah/ctypesgen_test/av/av/tx.h: 25

AVComplexFloat = struct_AVComplexFloat# /home/josiah/ctypesgen_test/av/av/tx.h: 29

AVComplexDouble = struct_AVComplexDouble# /home/josiah/ctypesgen_test/av/av/tx.h: 33

AVComplexInt32 = struct_AVComplexInt32# /home/josiah/ctypesgen_test/av/av/tx.h: 37

AVVideoEncParams = struct_AVVideoEncParams# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 110

AVVideoBlockParams = struct_AVVideoBlockParams# /home/josiah/ctypesgen_test/av/av/video_enc_params.h: 137

AVVorbisParseContext = struct_AVVorbisParseContext# /home/josiah/ctypesgen_test/av/av/vorbis_parser.h: 31

AVXTEA = struct_AVXTEA# /home/josiah/ctypesgen_test/av/av/xtea.h: 37

xvmc_pix_fmt = struct_xvmc_pix_fmt# /home/josiah/ctypesgen_test/av/av/xvmc.h: 47

# No inserted files

# No prefix-stripping

