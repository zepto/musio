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

from io_base import AudioIO, DevIO

# Codec cache dictionary
__codec_cache = {}

# Audio IO device cache dictionary
__io_cache = {}

def _build_mod_list(mod_path: list, suffix: str, blacklist: list) -> list:
    """ _build_mod_list(mod_path, suffix) -> Add all the paths in mod_path to
    sys.path and return a list of all modules in sys.path ending in suffix.

    """

    from sys import path as sys_path
    from os import listdir as os_listdir
    from os.path import isdir as os_isdir
    from os.path import abspath as os_abspath
    from os.path import dirname as os_dirname

    mod_path = [mod_path] if type(mod_path) is str else mod_path

    # Add the path of this file to the search path.
    mod_path.append(os_abspath(os_dirname(__file__)))

    # Add the path(s) in mod_path to sys.path so we can import from
    # them.
    [sys_path.append(path) for path in mod_path if path not in sys_path]

    # Build the list of modules ending in suffix in the mod_path(s).
    mod_list = ((path, name) for path in sys_path \
                                if os_isdir(path) \
                                    for name in os_listdir(path) \
                                        if name.endswith(suffix) and \
                                           name not in blacklist)

    return mod_list

def get_codec(filename: str, mod_path=[], cached=True, blacklist=[]) -> AudioIO:
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

    from importlib import import_module
    from os.path import splitext as os_splitext
    from os.path import join as os_join
    from urllib.parse import urlparse

    from import_util import load_lazy_import, unload_lazy_import

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

    # Make importing lazy.
    load_lazy_import(mod_path=mod_path)

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Load the module.
        module = import_module(os_splitext(name)[0])

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        if 'handler' not in supported_dict:
            continue

        issupported = supported_dict.get('issupported', lambda *a: False)
        ext = supported_dict.get('ext', [])
        protocol = supported_dict.get('protocol', [])

        default = supported_dict.get('default', False)

        handler = getattr(module, supported_dict.get('handler'))

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
    unload_lazy_import()

    return codec

def get_io(fileobj, mod_path=[], cached=True, blacklist=[]) -> DevIO:
    """ get_io(fileobj, mod_path=[], cached=True, blacklist=[]) -> Finds a
    audio device that can take the data read from fileobj and returns it.

    """

    # IO device cache dictionary
    global __io_cache

    from importlib import import_module
    from os.path import splitext as os_splitext

    from import_util import load_lazy_import, unload_lazy_import

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

    # Make importing lazy.
    load_lazy_import(mod_path=mod_path)

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Load the module.
        module = import_module(os_splitext(name)[0])

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})

        if 'handler' not in supported_dict:
            continue

        input_t = supported_dict.get('input', [])
        output_t = supported_dict.get('output', [])

        default = supported_dict.get('default', False)

        handler = getattr(module, supported_dict.get('handler'))

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
    unload_lazy_import()

    return device

def open_file(filename: str, mode='r', **kwargs) -> AudioIO:
    """ open_file(filename, mode='r') -> Returns the open file.

    """

    codec = get_codec(filename)

    if not codec:
        print("Filetype not supported.")
        return None

    return codec(filename, mode=mode, **kwargs)

def open_io(fileobj: AudioIO, mode='r') -> DevIO:
    """ open_io(fileobj, mode='r') -> Returns an open audio device.

    """

    # Get the supported device
    device = get_io(fileobj)

    if not device:
        print("Audio format not supported.")
        return None

    # Open and return the device.
    return device(mode=mode, rate=fileobj.rate, channels=fileobj.channels,
                  depth=fileobj.depth, bigendian=fileobj.bigendian,
                  unsigned=fileobj.unsigned)

@contextmanager
def silence(fd):
    """ silence(fd) -> Silence any output from fd.

    """

    from os import dup as os_dup
    from os  import pipe as os_pipe
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
