#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of module music.
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


""" Base classes for file like access to music files and a player class.

"""

from os.path import isfile as os_isfile
from functools import wraps as functools_wraps

# If True only errors will only print a message not fail.
IO_SOFT_ERRORS = True

# Codec cache dictionary
__codec_cache = {}

def get_codec(filename, mod_path=[]):
    """ get_codec(filename, mod_path=[]) -> Load all the codecs in the path
    and return the one that can play the file.

    """

    global __codec_cache

    from importlib import import_module
    from sys import path as sys_path
    from os import listdir as os_listdir
    from os.path import splitext as os_splitext
    from os.path import isdir as os_isdir
    from os.path import join as os_join
    from urllib.parse import urlparse

    # Get the file extension.
    file_ext = os_splitext(filename)[1].lower()

    # Get protocol.
    file_prot = urlparse(filename).scheme

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
                                        if name.endswith('_file.py'))

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

            if not args:
                args = (self._buffer_size,)

            # print(self._buffer_size, args)
        elif func.__name__ == 'write':
            if self._mode == 'r':
                raise IOError("(%s) Open for reading.  Unable to write." % class_name)

            # Don't even call the function if there is no data to write.
            if not args:
                return 0
            elif not args[0]:
                args = (b'',)

        try:
            return func(self, *args)
        except IOError as err:
            if IO_SOFT_ERRORS:
                # Only print the error message.
                print("(%s.%s) %s" % (class_name, func_name, err))
            else:
                # Re-raise the error.
                raise

    return wrapper


class MusicIO(object):
    """ File like access for audio files.

    """

    def __init__(self, filename, mode='r', depth=16, rate=44100, channels=2):
        """ MusicIO(filename, [mode='r', depth=16, rate=44100, channels=2])
        -> Open an audio file for file like access to audio files.

        """

        if mode not in 'rw':
            raise ValueError("Mode has to be either 'r' or 'w'.")

        if 'r' in mode and not os_isfile(filename):
            raise OSError("(%s) File not found: %s" % (self.__class__.__name__,
                                                       filename))

        if depth != 32 and depth != 16 and depth != 8:
            raise ValueError("Invalid depth %s, should be 32, 16 or 8." % \
                             depth)

        super(MusicIO, self).__init__()

        self._buffer_size = 16384 // (depth // (8 // channels))

        self._filename = filename
        self._mode = mode

        self._depth = depth
        self._rate = rate
        self._channels = channels

        self._width = self._depth // 8

        self._volume = 1
        self._length = 0

        self._bigendian = False
        self._unsigned = False

        self._loops = -1
        self._loop_count = 0

        self._closed = True

        self._info_dict = {}

    def __str__(self):
        """ __str__ -> Return a string representation of the module
        information.

        """

        str_list = ['\n']

        for key, value in self._info_dict.items():
            if type(value) in (list, tuple, set):
                str_list.insert(0, '\t%s' % '\n\t'.join(value))
                str_list.insert(0, "\n%s" % key.lower().capitalize())
                continue
            value = str(value).strip()
            str_list.append("%-12s: %s" % (key.lower().capitalize(), value))

        return '\n'.join(str_list)

    def __repr__(self):
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

    def __next__(self):
        """ Return the next buffer.

        """

        return self.read()

    def seek(self, position):
        """ seek(position) -> Seek to position in mod.

        """

        self.position = position

    def tell(self):
        """ tell -> Returns the current position.

        """

        return self.position

    @io_wrapper
    def read(self, size=None):
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        raise NotImplementedError("Read method not implemented.")

    @io_wrapper
    def write(self, data):
        """ write(data) -> Write data to file.

        """

        raise NotImplementedError("Write method not implemented.")

    def close(self):
        """ close -> Closes and cleans up.

        """

        raise NotImplementedError("Close method not implemented.")

    def _open(self):
        """ _open() -> Open the classes file and set it up for read/write
        access.

        """

        raise NotImplementedError("Open method not implemented.")

    def _endian_changed(self):
        """ Setup the conversion function when the endian changes.

        """

        pass

    def _set_position(self, position):
        """ Change the position of playback.

        """

        pass

    def _get_position(self):
        """ Returns the current position.

        """

        return 0

    @property
    def closed(self):
        """ Return true if closed.

        """

        return self._closed

    @property
    def volume(self):
        """ Get the current volume.

        """

        return self._volume

    @volume.setter
    def volume(self, value):
        """ Set the volume.

        """

        self._volume = value

    @property
    def loops(self):
        """ How many times the file should loop.

        """

        return self._loops

    @loops.setter
    def loops(self, value):
        """ Set how many times the file should loop.

        To play forever use a value of -1.

        """

        self._loops = value

    @property
    def unsigned(self):
        """ Whether the player is producing signed data.

        """

        return self._unsigned

    @unsigned.setter
    def unsigned(self, value):
        """ unsigned(value) -> Set to use unsigned data.  By default it
        produces signed data.

        """

        self._unsigned = value

    @property
    def bigendian(self):
        """ Whether the player is using bigendian.

        """

        return self._bigendian

    @bigendian.setter
    def bigendian(self, value):
        """ bigendian(value) -> Set to produce bigendian data.  By default
        it produces little endian data.

        """

        self._bigendian = value
        self._endian_changed()

    @property
    def position(self):
        """ Get the current position.

        """

        return self._get_position()

    @position.setter
    def position(self, position):
        """ Set the position.

        """

        self._set_position(int(position))

    @property
    def length(self):
        """ Get the length.

        """

        return self._length

    @property
    def depth(self):
        """ Get the current bit depth.

        """

        return self._depth

    @property
    def rate(self):
        """ The current sample rate.

        """

        return self._rate

    @property
    def channels(self):
        """ Get the current channel count.

        """

        return self._channels

    @property
    def buffer_size(self):
        """ Get the current buffer size.

        """

        return self._buffer_size


class AudioIO(object):
    """ File like access to audio output.

    """

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
            bigendian=False, unsigned=False, buffer_size=None, latency=500000):
        """ Alsa(depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None, latency=500000) -> Initialize an
        audio device for either reading or writing.

        """

        if depth != 32 and depth != 16 and depth != 8:
            raise ValueError("Invalid depth %s, should be 32, 16 or 8." % \
                             depth)

        super(AudioIO, self).__init__()

        if not buffer_size:
            buffer_size = 16384 // (depth // (8 // channels))

        self._buffer_size = buffer_size

        self._mode = mode
        self._depth = depth
        self._rate = rate
        self._bigendian = bigendian
        self._unsigned = unsigned
        self._channels = channels
        self._latency = latency

        self._closed = True

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

    def read(self, length):
        """ read(length) -> Read from pcm.

        """

        raise NotImplementedError("Read method not implemented.")

    def write(self, data):
        """ write(data) -> Write to the pcm device.

        """

        raise NotImplementedError("Write method not implemented.")

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
    """ Load modules on demand.

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
        """ Import the module.contents

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
