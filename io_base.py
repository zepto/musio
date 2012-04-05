#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Abstract classes for audio file/device io.
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
    io_wrapper      Function for wrapping audio io functions

    AudioIO         Abstract class for audio file IO
    DevIO           Abstract class for audio device IO
    OnDemand        Load libraries when they are accessed

"""

from functools import wraps as functools_wraps


# If True errors will only print a message.
IO_SOFT_ERRORS = True

# Codec cache dictionary
__codec_cache = {}

# Audio IO device cache dictionary
__io_cache = {}

def get_codec(filename, mod_path=[], cached=True, blacklist=[]):
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
    from sys import path as sys_path
    from os import listdir as os_listdir
    from os.path import splitext as os_splitext
    from os.path import isdir as os_isdir
    from os.path import join as os_join
    from os.path import abspath as os_abspath
    from os.path import dirname as os_dirname
    from urllib.parse import urlparse

    # Add the path of this file to the search path.
    mod_path.append(os_abspath(os_dirname(__file__)))

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

    mod_path = [mod_path] if type(mod_path) is str else mod_path

    # Add the path(s) in mod_path to sys.path so we can import from
    # them.
    [sys_path.append(path) for path in mod_path if path not in sys_path]

    # Build the list of modules ending in '_file.py' in the mod_path(s).
    mod_list = ((path, name) for path in sys_path \
                                if os_isdir(path) \
                                    for name in os_listdir(path) \
                                        if name.endswith('_file.py') and \
                                           name not in blacklist)

    Music = None

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Load the module.
        module = import_module(os_splitext(name)[0])

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})
        ext = supported_dict.get('ext', [])
        protocol = supported_dict.get('protocol', [])

        default = supported_dict.get('default', False)

        if 'handler' not in supported_dict:
            continue

        handler = getattr(module, supported_dict.get('handler'))

        # Add filetype handlers to the codec cache.
        if ext:
            __codec_cache.update(((key, handler) for key in ext))

        # Add protocol handlers to the codec cache.
        if protocol:
            __codec_cache.update(((key, handler) for key in protocol))

        # Check if filename is supported.
        if file_ext in ext or file_prot in protocol:
            Music = handler
            if default: break
        elif not Music and '.*' in ext:
            Music = handler

    return Music

def get_io(fileobj, mod_path=[], cached=True, blacklist=[]):
    """ get_io(fileobj, mod_path=[], cached=True, blacklist=[]) -> Finds a
    audio device that can take the data read from fileobj and returns it.

    """

    # IO device cache dictionary
    global __io_cache

    from importlib import import_module
    from sys import path as sys_path
    from os import listdir as os_listdir
    from os.path import splitext as os_splitext
    from os.path import isdir as os_isdir
    from os.path import join as os_join
    from os.path import abspath as os_abspath
    from os.path import dirname as os_dirname
    from urllib.parse import urlparse

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

    # Make mod_path a list
    mod_path = [mod_path] if type(mod_path) is str else mod_path

    # Add the path of this file to the search path.
    mod_path.append(os_abspath(os_dirname(__file__)))

    # Add the path(s) in mod_path to sys.path so we can import from
    # them.
    [sys_path.append(path) for path in mod_path if path not in sys_path]

    # Build the list of modules ending in '_file.py' in the mod_path(s).
    mod_list = ((path, name) for path in sys_path \
                                if os_isdir(path) \
                                    for name in os_listdir(path) \
                                        if name.endswith('_io.py') and \
                                           name not in blacklist)

    device = None

    # Load the codec module that can handle file.
    for path, name in mod_list:
        # Load the module.
        module = import_module(os_splitext(name)[0])

        # Get the filetypes and handler from module.
        supported_dict = getattr(module, '__supported_dict', {})
        input_t = supported_dict.get('input', [])
        output_t = supported_dict.get('output', [])

        default = supported_dict.get('default', False)

        if 'handler' not in supported_dict:
            continue

        handler = getattr(module, supported_dict.get('handler'))

        # Add filetype handlers to the codec cache.
        if input_t:
            __io_cache.update(((key, handler) for key in input_t))

        # Add protocol handlers to the codec cache.
        if output_t:
            __io_cache.update(((key, handler) for key in output_t))

        # Check if filename is supported.
        if file_input in input_t or file_output in output_t:
            device = handler
            if default: break

    return device

def open_file(filename):
    """ open_file(filename) -> Returns the open file.

    """

    codec = get_codec(filename)

    if not codec:
        print("Filetype not supported.")
        return None

    return codec(filename)

def io_wrapper(func):
    """ Wrap io methods.

    """

    @functools_wraps(func)
    def wrapper(self, *args):
        """ Call the wrapped function.

        """

        class_name = self.__class__.__name__
        func_name = func.__name__

        if self._closed:
            err_str = "({class_name}) Can't {func_name}, file/device is closed.".format(**locals())
            raise IOError(err_str)

        if func.__name__ == 'read':
            if self._mode == 'w':
                raise IOError("(%s) Open for writing.  Unable to read." % class_name)

            # No size was given so read until EOF.
            if not args:
                return self.readall()
        elif func.__name__ == 'write':
            if self._mode == 'r':
                raise IOError("(%s) Open for reading.  Unable to write." % class_name)

            # Don't even call the function if there is no data to write.
            if not args:
                return func.__annotations__.get('return', int)(0)
            elif not args[0]:
                args = (func.__annotations__.get('data', bytes)(), )

        try:
            return func(self, *args)
        except IOError as err:
            if IO_SOFT_ERRORS:
                # Only print the error message.
                print("(%s.%s) %s" % (class_name, func_name, err))
            else:
                # Re-raise the error.
                raise

            return func.__annotations__.get('return', int)(0)

    return wrapper


class AudioIO(object):
    """ File like access for audio files.

    """

    # Valid bit depths
    _valid_depth = (32, 16, 8)

    # Both reading and writing are supported
    _supported_modes = 'rw'

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2):
        """ AudioIO(filename, [mode='r', depth=16, rate=44100, channels=2])
        -> Open an audio file for file like access to audio files.

        """

        if mode not in self._supported_modes:
            raise ValueError("(%s) Mode has to be one of %s." % \
                             (self.__class__.__name__,
                             self._supported_modes))

        if depth not in self._valid_depth:
            raise ValueError("(%s) Invalid depth %s, valid depths are %s" % \
                             (self.__class__.__name__,
                              depth,
                              self._valid_depth))

        super(AudioIO, self).__init__()

        self._buffer_size = 8192 #16384 // (depth // (8 // channels))

        self._filename = filename
        self._mode = mode

        self._depth = depth
        self._rate = rate
        self._channels = channels

        self._width = self._depth // 8

        self._length = 0

        self._bigendian = False
        self._unsigned = False

        self._loops = -1
        self._loop_count = 0

        self._closed = True

        self._info_dict = {}

    def __str__(self) -> str:
        """ __str__ -> Return a string representation of the module
        information.

        """

        str_list = ['\n']

        for key, value in self._info_dict.items():
            if not str(value).strip():
                continue

            if type(value) in (list, tuple, set):
                str_list.insert(0, '\t%s' % '\n\t'.join(value))
                str_list.insert(0, "\n%s" % key.lower().capitalize())
                continue
            value = str(value).strip()
            str_list.append("%-12s: %s" % (key.lower().capitalize(), value))

        return '\n'.join(str_list)

    def __repr__(self) -> str:
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='{_filename}', depth={_depth}, rate={_rate}, channels={_channels}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def __enter__(self):
        """ Provides the ability to use pythons with statement.

        """

        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """ Close the file when finished.

        """

        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False

    def __iter__(self):
        """ Returns an iter of this object.

        """

        return self

    def __next__(self) -> bytes:
        """ Return the next buffer.

        """

        data = self.read(self._buffer_size)

        if not data:
            raise StopIteration
        else:
            return data

    def seek(self, position : int):
        """ seek(position) -> Seek to position in mod.

        """

        self.position = position

    def tell(self) -> int:
        """ tell -> Returns the current position.

        """

        return self.position

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        raise NotImplementedError("Read method not implemented.")

    @io_wrapper
    def readall(self) -> bytes:
        """ readall() -> Read the entire buffer and return the result.

        """

        # Return the entire buffer.
        return b''.join([i for i in self])

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write data to file.

        """

        raise NotImplementedError("Write method not implemented.")

    def _open(self):
        """ _open() -> Open the classes file and set it up for read/write
        access.

        """

        raise NotImplementedError("Open method not implemented.")

    def close(self):
        """ close -> Closes and cleans up.

        """

        raise NotImplementedError("Close method not implemented.")

    def _set_position(self, position: int):
        """ Change the position of playback.

        """

        pass

    def _get_position(self) -> int:
        """ Returns the current position.

        """

        return 0

    @property
    def closed(self):
        """ Return true if closed.

        """

        return self._closed

    @property
    def loops(self) -> int:
        """ How many times the file should loop.

        """

        return self._loops

    @loops.setter
    def loops(self, value: int):
        """ Set how many times the file should loop.

        To play forever use a value of -1.

        """

        self._loops = value

    @property
    def position(self) -> int:
        """ Get the current position.

        """

        return self._get_position()

    @position.setter
    def position(self, position: int):
        """ Set the position.

        """

        self._set_position(int(position))

    @property
    def length(self) -> int:
        """ Get the length.

        """

        return self._length

    @property
    def depth(self) -> int:
        """ Get the current bit depth.

        """

        return self._depth

    @property
    def rate(self) -> int:
        """ The current sample rate.

        """

        return self._rate

    @property
    def channels(self) -> int:
        """ Get the current channel count.

        """

        return self._channels

    @property
    def buffer_size(self) -> int:
        """ Get the current buffer size.

        """

        return self._buffer_size

    @property
    def unsigned(self) -> bool:
        """ Whether the player is producing signed data.

        """

        return self._unsigned

    @property
    def bigendian(self) -> bool:
        """ Whether the player is using bigendian.

        """

        return self._bigendian


class DevIO(object):
    """ File like access to audio device.

    """

    _valid_depth = (32, 24, 16, 8)
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
            bigendian=False, unsigned=False, buffer_size=None, latency=500000):
        """ DevIO(depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None, latency=500000) -> Initialize an
        audio device for either reading or writing.

        """

        if mode not in self._supported_modes:
            raise ValueError("(%s) Mode has to be one of %s." % \
                             self.__class__.__name__,
                             self._supported_modes)

        if depth not in self._valid_depth:
            raise ValueError("(%s) Invalid depth %s.  Valid depths are: %s" % \
                             (self.__class__.__name__,
                             depth,
                             self._valid_depth))

        super(DevIO, self).__init__()

        self._mode = mode
        self._depth = depth
        self._rate = rate
        self._channels = channels
        self._bigendian = bigendian
        self._unsigned = unsigned

        if not buffer_size:
            # Set buffer_size to a sane default.
            buffer_size = 16384 // (depth // (8 // channels))

        self._buffer_size = buffer_size

        self._latency = latency

        self._closed = True

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='{_mode}', depth={_depth}, rate={_rate}, channels={_channels}, bigendian={_bigendian}, unsigned={_unsigned}, buffer_size={_buffer_size}".format(**self.__dict__)

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    @property
    def closed(self):
        """ Return true if closed.

        """

        return self._closed

    @property
    def depth(self):
        """ The current depth rate.

        """

        return self._depth

    @property
    def unsigned(self):
        """ The sample current sample rate.

        """

        return self._unsigned

    @property
    def rate(self):
        """ The sample current sample rate.

        """

        return self._rate

    @property
    def channels(self):
        """ The number of output channels.

        """

        return self._channels

    @property
    def buffer_size(self):
        """ The buffer size.

        """

        return self._buffer_size

    @io_wrapper
    def read(self, length: int) -> bytes:
        """ read(length) -> Read from pcm.

        """

        raise NotImplementedError("Read method not implemented.")

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        raise NotImplementedError("Write method not implemented.")

    def flush(self):
        """ Flush output buffer.

        """

        pass

    def _open(self):
        """ open -> Open the pcm audio output.

        """

        raise NotImplementedError("Open method not implemented.")

    def close(self):
        """ close -> Close the pcm.

        """

        raise NotImplementedError("Close method not implemented.")

    def __iter__(self):
        """ Returns an iter of this object.

        """

        return self

    def __next__(self):
        """ Return the next buffer.

        """

        return self.read()

    def __enter__(self):
        """ Provides the ability to use pythons with statement.

        """

        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """ Close the pcm when finished.

        """

        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False


class OnDemand(object):
    """ Load modules when accessed.

    """

    def __init__(self, module_name, globals={}, locals={}, fromlist=[], level=0):
        """ OnDemand(module_name, globals={}, locals={}, fromlist=[], level=0)
        -> Load module only when it is needed.

        """

        self._module_name = module_name
        self._globals = globals
        self._locals = locals
        self._fromlist = fromlist
        self._level = level
        self._module = None

    def _import(self):
        """ Import the module.

        """

        self._module = __import__(self._module_name, self._globals,
                                  self._locals, self._fromlist, self._level)

    def __getattr__(self, attr):
        """ Load the module if it is not already loaded.  Returns the modules
        attributes.

        """

        if not self._module:
            self._import()

        return getattr(self._module, attr)

    @property
    def __dict__(self):
        """ Load the module if it is not already loaded.  Returns the modules
        __dict__.

        """

        if not self._module:
            self._import()

        return vars(self._module)
