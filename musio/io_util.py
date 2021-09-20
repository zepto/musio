#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# I/O Utility functions.
# Copyright (C) 2012 Josiah Gordon <josiahg@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Convienience functions for audio file and device opening.

get_codec       Function for loading the default/first filetype codecs
get_io       Function for loading the default/first device
"""

from contextlib import contextmanager
from ctypes.util import find_library
from importlib import import_module
from os import listdir
from os.path import abspath, basename, dirname, isdir, splitext
from typing import IO, Any, Generator, Union

try:
    from .magic import magic as _magic
except OSError:
    _magic = None

from .io_base import AudioIO, DevIO

# Codec cache dictionary
__codec_cache = {}

# Audio IO device cache dictionary
__io_cache = {}

# Set to True to enable debut output
DEBUG = False


class Magic(object):
    """Magic object for testing string encoding."""

    def __init__(self, flags: int = 1024):
        """Object for testing text encoding.

        Default flags: magic.MAGIC_MIME_ENCODING
        """
        if not _magic:
            return None

        self._magic = _magic.magic_open(flags)
        if _magic.magic_load(self._magic, None) != 0:
            print(f"Error: {_magic.magic_error(self._magic).decode()}")

    def check(self, data):
        """Return the encoding of data."""
        if not _magic:
            return b'utf8'

        return _magic.magic_buffer(self._magic, data, len(data))


def msg_out(message: str, *args):
    """Print message if DEBUG is True."""
    if DEBUG:
        print(message, *args)


def slice_buffer(data: bytes, size: int) -> Generator[bytes, None, None]:
    """Generate slices of bytes from the data buffer."""
    for i in range(0, len(data), size):
        yield data[i:i + size]


def _build_mod_list(
    mod_path: list[str],
    suffix: str,
    blacklist: list[str]
) -> Generator[tuple[str, str], None, None]:
    """Build a list of modules.

    Add all the paths in mod_path to sys.path and return a list of all modules
    in sys.path ending in suffix.
    """
    from sys import path as sys_path

    mod_path = [mod_path] if type(mod_path) is str else mod_path
    blacklist = [blacklist] if type(blacklist) is str else blacklist

    # Add suffix to all names in blacklist.
    blacklist.extend(
        [f"{name}{suffix}" for name in blacklist if not name.endswith(suffix)]
    )

    # Add the path of this file to the search path.
    mod_path.append(abspath(dirname(__file__)))

    # Add the path(s) in mod_path to sys.path so we can import from
    # them.
    for path in mod_path:
        if path not in sys_path:
            sys_path.extend((path, dirname(path.rstrip('/'))))

    def isdir_list(path: str) -> list[str]:
        """Return a list of files from path if path is a directory."""
        return listdir(path) if isdir(path) else []

    # Return a genorator list of modules ending in suffix in the mod_path(s).
    return (
        (path, name) for path in sys_path for name in isdir_list(path)
        if name not in blacklist and name.endswith(suffix)
    )


def _check_dependencies(dependencies: dict) -> bool:
    """Return True if all the dependencies pass."""
    # Loop through the dependencies and check each one.
    for key, value in dependencies.items():
        if key == 'ctypes':
            # Check for c libraries.
            if not all((find_library(lib) for lib in value)):
                return False
        elif key == 'python':
            # Check for python modules.
            try:
                [__import__(mod) for mod in value]
            except ImportError:
                return False

    # Everything passed.
    return True


def get_codec(filename: str, mod_path: list[str] = [], cached: bool = True,
              blacklist: list[str] = []) -> Union[AudioIO, None]:
    """Load a codec that can handle the file.

    Load the codecs in the path and return the first one that can play the
    file, or the one with the default attribute set.

    filename        The file the codec needs to handle
    mod_path        Additional search paths for modules
    cached          Use cached codecs if available
    blacklist       Modules not to load
    """
    # Codec cache dictionary
    global __codec_cache

    from urllib.parse import urlparse

    # Get the file extension.
    file_ext = splitext(filename)[1].lower()

    # Get protocol.
    file_prot = urlparse(filename).scheme

    if cached:
        # Load and already cached codec.
        if file_ext in __codec_cache:
            return __codec_cache[file_ext]
        elif file_prot in __codec_cache:
            return __codec_cache[file_prot]

    # Get a list of modules ending in '_file.py'
    mod_list = _build_mod_list(mod_path, '_file.py', blacklist)

    codec = None
    dummy = None

    # This packages name.
    this_pkgname = __name__.split('.', 1)[0]

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Get the package name from path.
        pkgname = basename(path.rstrip('/'))

        # Import the package if it is different from this one.
        if pkgname != this_pkgname and pkgname:
            try:
                __import__(pkgname)
            except ImportError:
                continue

        # Load the module.
        try:
            module = import_module(f'.{splitext(name)[0]}', pkgname)
        except ImportError as err:
            print(f"Skipping module: ({name}) because of error: {err}")
            continue

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        # Get the handler.
        handler = getattr(
            module,
            supported_dict.get('handler', 'dummy'),
            None
        )

        # Don't even check this module if it does not have a handler.
        if not handler:
            continue

        # Try not to use the dummy handler.
        if 'dummy' in name:
            dummy = handler
            continue

        # Check the module dependencies.
        dependencies = supported_dict.get('dependencies', {})
        if not _check_dependencies(dependencies):
            continue

        issupported = supported_dict.get('issupported', lambda *_: False)
        ext = supported_dict.get('ext', [])
        protocol = supported_dict.get('protocol', [])

        default = supported_dict.get('default', False)

        # Add filetype handlers to the codec cache.
        __codec_cache.update(((key, handler) for key in ext))

        # Add protocol handlers to the codec cache.
        __codec_cache.update(((key, handler) for key in protocol))

        # Check if filename is supported.
        if issupported(filename) or file_ext in ext or file_prot in protocol:
            codec = handler
            if default:
                break
        elif not codec and '.*' in ext:
            codec = handler

    # No codec was found so default to the dummy codec.
    if not codec:
        codec = dummy

    return codec


def get_io(fileobj: AudioIO, mod_path: list[str] = [], cached: bool = True,
           blacklist: list[str] = []) -> Union[Any, DevIO, None]:
    """Get a matching audio device.

    Find a audio device that can take the data read from fileobj and returns
    it.
    """
    # IO device cache dictionary
    global __io_cache

    # Get the file input data type.
    annotations = getattr(getattr(fileobj, 'read'), '__annotations__', {})
    file_input = annotations.get('return', str)

    # Get the file output data type.
    annotations = getattr(getattr(fileobj, 'write'), '__annotations__', {})
    file_output = annotations.get('data', str)

    if cached:
        # Load and already cached audio device.
        if file_input in __io_cache:
            return __io_cache[file_input]
        elif file_output in __io_cache:
            return __io_cache[file_output]

    # Get a list of modules ending in '_io.py'
    mod_list = _build_mod_list(mod_path, '_io.py', blacklist)

    device = None
    dummy = None

    # This packages name.
    this_pkgname = __name__.split('.', 1)[0]

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Get the package name from path.
        pkgname = basename(path.rstrip('/'))

        # Import the package if it is different from this one.
        if pkgname != this_pkgname and pkgname:
            try:
                __import__(pkgname)
            except ImportError:
                continue

        # Load the module.
        module = import_module(f'.{splitext(name)[0]}', pkgname)

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        handler = getattr(
            module,
            supported_dict.get('handler', 'dummy'),
            None
        )

        if not handler:
            continue

        # Try not to use the dummy.
        if 'dummy' in name:
            dummy = handler
            continue

        # Check the module dependencies.
        dependencies = supported_dict.get('dependencies', {})
        if not _check_dependencies(dependencies):
            continue

        input_t = supported_dict.get('input', [])
        output_t = supported_dict.get('output', [])

        default = supported_dict.get('default', False)

        # Add device input to io cache
        __io_cache.update(((key, handler) for key in input_t))

        # Add device output to io cache.
        __io_cache.update(((key, handler) for key in output_t))

        # Check if filename is supported.
        if 'r' in fileobj.mode and file_input in output_t:
            device = handler
            if default:
                break
        elif 'w' in fileobj.mode and file_output in input_t:
            device = handler
            if default:
                break

    # No device was found so use the dummy_io.
    if not device:
        device = dummy

    return device


def open_file(filename: str, mode: str = 'r', mod_path: list[str] = [],
              blacklist: list[str] = [], **kwargs: dict) -> AudioIO:
    """Return the open file."""
    open_codec = None

    # Loop until a codec is found that can open the file.
    while not open_codec:
        codec = get_codec(
            filename,
            mod_path=mod_path,
            blacklist=blacklist,
            cached=False
        )

        if not codec:
            import sys
            print("No valid codec was found.")
            sys.exit()

        try:
            open_codec = codec(filename, mode=mode, **kwargs)
            open_codec.loops = kwargs.get('loops', -1)
        except IOError as err:
            print(f"Blacklisting ({codec}) because of error: {err}")

            mod_name = f"{codec.__module__.split('.')[-1]}.py"

            # Add the module to the blacklist.
            blacklist.append(mod_name)

    return open_codec


def open_device(fileobj: AudioIO, mode: str = 'w', mod_path: list[str] = [],
                blacklist: list[str] = [], **kwargs: dict) -> DevIO:
    """Return an open audio device."""
    dev_name = kwargs.get('device', b'default')
    rate = kwargs.get('rate', fileobj.rate)

    while True:
        # Get the supported device
        device = get_io(
            fileobj,
            mod_path=mod_path,
            blacklist=blacklist,
            cached=False
        )

        if not device:
            raise IOError(f"Error opening device {device}.")

        # Open and return the device.
        try:
            result = device(
                mode=mode,
                rate=rate,
                channels=fileobj.channels,
                depth=fileobj.depth,
                bigendian=fileobj.bigendian,
                unsigned=fileobj.unsigned,
                floatp=fileobj.floatp,
                device=dev_name,
                three_byte=fileobj.three_byte
            )
            break
        except Exception as err:
            print(f"Blacklisting ({device}) because of error: {err}.")

            mod_name = f"{device.__module__.split('.')[-1]}.py"

            # Add the module to the blacklist.
            blacklist.append(mod_name)
            continue

    return result


@contextmanager
def silence(fd: IO):
    """Silence any output from fd."""
    from os import close, dup, dup2, fdopen, pipe

    # Do not silence when debugging.
    if not DEBUG:
        # Backup the file
        old_fd = fd

        # Flush the file so it can be silenced properly.
        fd.flush()

        # Create a duplicate of fd
        new_fd = dup(fd.fileno())

        # Create a pipe to write to.
        read, write = pipe()

        # Set the write to the fd filenumber
        dup2(write, fd.fileno())

        # Close the pipe.
        close(write)
        close(read)

        # Set fd to the new fd
        fd = fdopen(new_fd, 'w')

    try:
        # Run the commands in the 'with' statement.
        yield
    finally:
        if not DEBUG:
            # Return the fd back to its original state.
            dup2(fd.fileno(), old_fd.fileno())
            fd = old_fd


@contextmanager
def py_silence(new_stdout: IO = None, new_stderr: IO = None):
    """Silence any output from fd.  In python."""
    import sys

    # Backup the file
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    # Flush the file so it can be silenced properly.
    sys.stdout.flush()
    sys.stderr.flush()

    sys.stdout, sys.stderr = new_stdout, new_stderr

    try:
        # Run the commands in the 'with' statement.
        yield
    finally:
        old_stdout.flush()
        old_stderr.flush()

        # Return the fd back to its original state.
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def bytes_to_str(data: bytes, codec_list: list = ['ascii', 'utf-8', 'latin-1',
                                                  'cp437']) -> str:
    """Decode bytes data in to a string.

    Try utf-8 first then latin-1 then cp437 and finally just use
    surrogateescape.
    """
    # Try to detect the encoding of the data.
    codec_type = Magic().check(data).decode()
    # Loop over each codec, and return the first one that works.
    for codec in [codec_type, *codec_list]:
        try:
            return data.decode(codec)
        except UnicodeDecodeError:
            continue
    # If all else fails try utf-8 escaping characters that cannot be decoded.
    return data.decode('utf-8', 'surrogateescape')
