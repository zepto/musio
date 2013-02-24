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


""" get_codec       Function for loading the default/first filetype codecs
    get_io       Function for loading the default/first device

"""

from contextlib import contextmanager
from importlib import import_module
from os.path import splitext as os_splitext
from os.path import join as os_join
from os.path import basename as os_basename
from os import listdir as os_listdir
from os.path import isdir as os_isdir
from os.path import abspath as os_abspath
from os.path import dirname as os_dirname
from ctypes.util import find_library as ctypes_find_library

from .io_base import AudioIO, DevIO

# Codec cache dictionary
__codec_cache = {}

# Audio IO device cache dictionary
__io_cache = {}

# Set to True to enable debut output
DEBUG=False


def msg_out(message: str, *args):
    """ Print message if DEBUG is True.

    """

    if DEBUG:
        print(message, *args)


def slice_buffer(data: bytes, size: int) -> bytes:
    """ slice_buffer(data, size) -> A generator that yields slices of bytes
    from the data buffer.

    """

    for i in range(0, len(data), size):
        yield data[i:i + size]


def _build_mod_list(mod_path: list, suffix: str, blacklist: list) -> list:
    """ _build_mod_list(mod_path, suffix) -> Add all the paths in mod_path to
    sys.path and return a list of all modules in sys.path ending in suffix.

    """

    from sys import path as sys_path

    mod_path = [mod_path] if type(mod_path) is str else mod_path
    blacklist = [blacklist] if type(blacklist) is str else blacklist

    # Add suffix to all names in blacklist.
    blacklist.extend(['%s%s' % (name, suffix) for name in blacklist
                                                if not name.endswith(suffix)])

    # Add the path of this file to the search path.
    mod_path.append(os_abspath(os_dirname(__file__)))

    # Add the path(s) in mod_path to sys.path so we can import from
    # them.
    [sys_path.extend((path, os_dirname(path.rstrip('/'))))
                        for path in mod_path
                            if path not in sys_path]

    # Build the list of modules ending in suffix in the mod_path(s).
    mod_list = ((path, name) for path in sys_path
                                if os_isdir(path)
                                    for name in os_listdir(path)
                                        if name.endswith(suffix) and
                                           name not in blacklist)

    return mod_list


def _check_dependencies(dependencies: dict) -> bool:
    """ Returns True if all the dependencies pass.

    """

    # Loop through the dependencies and check each one.
    for key, value in dependencies.items():
        if key == 'ctypes':
            # Check for c libraries.
            if not all((ctypes_find_library(lib) for lib in value)):
                return False
        elif key == 'python':
            # Check for python modules.
            try:
                [__import__(mod) for mod in value]
            except ImportError as err:
                return False

    # Everything passed.
    return True


def get_codec(filename: str, mod_path: list = [], cached: bool = True,
              blacklist: list = []) -> AudioIO:
    """ get_codec(filename, mod_path=[], cached=True, blacklist=[]) -> Load the
    codecs in the path and return the first one that can play the file, or the
    one with the default attribute set.

        filename        The file the codec needs to handle
        mod_path        Additional search paths for modules
        cached          Use cached codecs if available
        blacklist       Modules not to load

    """

    # Codec cache dictionary
    global __codec_cache

    from urllib.parse import urlparse

    from .import_util import load_lazy_import, unload_lazy_import

    # Get the file extension.
    file_ext = os_splitext(filename)[1].lower()

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

    # Make importing lazy.
    # load_lazy_import(mod_path=mod_path)

    # This packages name.
    this_pkgname = __name__.split('.', 1)[0]

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Get the package name from path.
        pkgname = os_basename(path.rstrip('/'))

        # Import the package if it is different from this one.
        if pkgname != this_pkgname and pkgname:
            try:
                __import__(pkgname)
            except ImportError as err:
                continue

        # Load the module.
        module = import_module('.%s' % os_splitext(name)[0], pkgname)

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        # Get the handler.
        handler = getattr(module, supported_dict.get('handler', 'dummy'), None)

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

        issupported = supported_dict.get('issupported', lambda *a: False)
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
            if default: break
        elif not codec and '.*' in ext:
            codec = handler

    # Turn off lazy imports.
    # unload_lazy_import()

    # No codec was found so default to the dummy codec.
    if not codec: codec = dummy

    return codec


def get_io(fileobj: AudioIO, mod_path: list = [], cached: bool = True,
           blacklist: list = []) -> DevIO:
    """ get_io(fileobj, mod_path=[], cached=True, blacklist=[]) -> Finds a
    audio device that can take the data read from fileobj and returns it.

    """

    # IO device cache dictionary
    global __io_cache

    from .import_util import load_lazy_import, unload_lazy_import

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

    # Make importing lazy.
    # load_lazy_import(mod_path=mod_path)

    # This packages name.
    this_pkgname = __name__.split('.', 1)[0]

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Get the package name from path.
        pkgname = os_basename(path.rstrip('/'))

        # Import the package if it is different from this one.
        if pkgname != this_pkgname and pkgname:
            try:
                __import__(pkgname)
            except ImportError as err:
                continue

        # Load the module.
        module = import_module('.%s' % os_splitext(name)[0], pkgname)

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        handler = getattr(module, supported_dict.get('handler', 'dummy'), None)

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
            if default: break
        elif 'w' in fileobj.mode and file_output in input_t:
            device = handler
            if default: break

    # Turn off lazy imports.
    # unload_lazy_import()

    # No device was found so use the dummy_io.
    if not device: device = dummy

    return device


def open_file(filename: str, mode: str = 'r', mod_path: list = [],
              **kwargs: dict) -> AudioIO:
    """ open_file(filename, mode='r') -> Returns the open file.

    """

    blacklist = kwargs.get('blacklist', [])

    open_codec = None

    # Loop until a codec is found that can open the file.
    while not open_codec:
        codec = get_codec(filename, mod_path=mod_path, blacklist=blacklist,
                          cached=False)
        if not codec:
            raise IOError("Filetype not supported.")

        try:
            open_codec = codec(filename, mode=mode, **kwargs)
        except IOError as err:
            mod_name = '%s.py' % codec.__module__.split('.')[-1]

            # Add the module to the blacklist.
            blacklist.append(mod_name)

    return open_codec


def open_device(fileobj: AudioIO, mode: str = 'w', mod_path: list = [],
                **kwargs: dict) -> DevIO:
    """ open_device(fileobj, mode='r') -> Returns an open audio device.

    """

    blacklist = kwargs.get('blacklist', [])

    # Get the supported device
    device = get_io(fileobj, mod_path=mod_path, blacklist=blacklist)

    if not device:
        print("Audio format not supported.")
        return None

    # Open and return the device.
    return device(mode=mode, rate=fileobj.rate, channels=fileobj.channels,
                  depth=fileobj.depth, bigendian=fileobj.bigendian,
                  unsigned=fileobj.unsigned, floatp=fileobj.floatp)


@contextmanager
def silence(fd: "File descripter"):
    """ silence(fd) -> Silence any output from fd.

    """

    from os import dup as os_dup
    from os import pipe as os_pipe
    from os import dup2 as os_dup2
    from os import close as os_close
    from os import fdopen as os_fdopen

    # Backup the file
    old_fd = fd

    # Flush the file so it can be silenced properly.
    fd.flush()

    # Create a duplicate of fd
    new_fd = os_dup(fd.fileno())

    # Create a pipe to write to.
    read, write = os_pipe()

    # Set the write to the fd filenumber
    os_dup2(write, fd.fileno())

    # Close the pipe.
    os_close(write)
    os_close(read)

    # Set fd to the new fd
    fd = os_fdopen(new_fd, 'w')

    try:
        # Run the commands in the 'with' statement.
        yield
    finally:
        # Return the fd back to its original state.
        os_dup2(fd.fileno(), old_fd.fileno())
        fd = old_fd

@contextmanager
def py_silence(new_stdout: "File descripter"=None,
               new_stderr: "File descripter"=None):
    """ py_silence(new_stdout, new_stderr) -> Silence any output from fd.  In
    python.

    """

    from os import devnull as os_devnull
    import sys

    stdout = new_stdout or sys.stdout
    stderr = new_stderr or sys.stderr

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
