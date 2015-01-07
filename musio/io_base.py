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


""" io_wrapper      Function for wrapping audio io functions

    AudioIO         Abstract class for audio file IO
    DevIO           Abstract class for audio device IO

"""

from functools import wraps as functools_wraps
from io import RawIOBase, SEEK_SET, SEEK_CUR, SEEK_END
from os.path import basename as os_basename
from os.path import isfile as os_isfile

# If True errors will only print a message.
IO_SOFT_ERRORS = True


def io_wrapper(func):
    """ Wrap io methods.

    """

    @functools_wraps(func)
    def wrapper(self, *args):
        """ Call the wrapped function.

        """

        class_name = self.__class__.__name__
        func_name = func.__name__
        func_annotations = getattr(func, '__annotations__', {})

        # No Errors at the start.
        err_str = ''

        if self._closed:
            # Don't close the stream more than once.
            if func_name == 'close': return None

            # Don't operate on a closed stream.
            err_str = "({class_name}) Can't {func_name}, stream is closed."

        # Validate the mode and function.
        if 'read' in func_name and 'r' not in self._mode:
            err_str = "({class_name}) Write-only stream.  Unable to read."
        elif 'write' in func_name and 'w' not in self._mode:
            err_str = "({class_name}) Read-only stream.  Unable to write."

        # Raise any errors detected.
        if err_str:
            raise IOError(err_str.format(**locals()))

        if func_name == 'read':
            # No size was given or size is -1, so read until EOF.
            if not args or args[1:] == -1:
                return self.readall()
        elif func_name == 'write':
            if not args:
                # Don't even call the function if there is no data to write.
                return func_annotations.get('return', int)(0)
            elif not args[0]:
                # Send the appropriate data type.
                args = (func_annotations.get('data', bytes)(), )

        # Finaly call the function and catch any IOErrors.
        try:
            return func(self, *args)
        except IOError as err:
            if IO_SOFT_ERRORS:
                # Only print the error message.
                print("(%s.%s) %s" % (class_name, func_name, err))
            else:
                # Re-raise the error.
                raise

            # Always return the correct return type.
            return func_annotations.get('return', int)(0)

    return wrapper


class AudioIO(RawIOBase):
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

        if not all([i in self._supported_modes for i in mode]):
            raise ValueError("(%s) Mode has to be one of %s." %
                             (self.__class__.__name__,
                             self._supported_modes))

        if depth not in self._valid_depth:
            raise ValueError("(%s) Invalid depth %s, valid depths are %s" %
                             (self.__class__.__name__,
                              depth,
                              self._valid_depth))

        super(AudioIO, self).__init__()

        if 'r' in mode and not os_isfile(filename):
            raise(IOError("No such file or directory"))

        self.three_byte = False

        # self._buffer_size = 8192  # 16384 // (depth // (8 // channels))
        self._buffer_size = 0 #16384 // (depth // (8 // channels))

        self._filename = filename
        self._mode = mode

        self._depth = depth
        self._rate = rate
        self._channels = channels
        self._floatp = False

        self._width = self._depth // 8

        self._length = -1

        self._bigendian = False
        self._unsigned = False

        self._loops = -1
        self._loop_count = 0

        self._closed = True

        # The default name is the filename minus the extension.
        name = os_basename(self._filename.rsplit('.', 1)[0])

        self._info_dict = {'name': name}

    def __str__(self) -> str:
        """ __str__ -> Return a string representation of the module
        information.

        """

        str_list = ['\n']

        max_key_len = max(len(key) for key in self._info_dict.keys())

        for key, value in self._info_dict.items():
            if not str(value).strip():
                continue

            if type(value) in (list, tuple, set):
                str_list.insert(0, '\t%s' % '\n\t'.join(value))
                str_list.insert(0, "\n%s" % key.lower().capitalize())
                continue
            value = str(value).strip()

            # str_list.append("%-*s: %s" % (max_key_len,
            #                               key.lower().capitalize(), value))

            # Format the info in a list as follows:
            # key (right align by space max_key_len): value
            str_list.append("{1:<{0}}: {2}".format(max_key_len,
                                                   key.lower().capitalize(),
                                                   value))

        return '\n'.join(str_list)

    def __repr__(self) -> str:
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def __getitem__(self, item):
        """ Return the attribute.

        """

        return getattr(self, item)

    def __len__(self):
        """ The length of the file if it has one.

        """

        return self._length if self._length >= 0 else 0

    def __bool__(self):
        """ Always return True.

        """

        return True

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

        data = self.read(self.buffer_size)

        if not data:
            raise StopIteration
        else:
            return data

    def writable(self) -> bool:
        """ Return wether this device is writable.

        """

        return 'w' in self._mode

    def readable(self) -> bool:
        """ Return wether this device is readable.

        """

        return 'r' in self._mode

    def seekable(self) -> bool:
        """ The file is seekable if self._length is > 0

        """

        return self._length >= 0

    @io_wrapper
    def seek(self, offset: int, whence: int = SEEK_SET) -> int:
        """ seek(offset, whence) -> Seek to position in mod.

        """

        if whence == SEEK_CUR:
            self.position += offset
        elif whence == SEEK_END:
            self.position = self._length - offset
        else:
            self.position = offset

        return self.position

    @io_wrapper
    def tell(self) -> int:
        """ tell -> Returns the current position.

        """

        return self.position

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size) -> Reads size amount of data and returns it.

        """

        raise NotImplementedError("Read method not implemented.")

    @io_wrapper
    def readall(self):
        """ readall() -> Read and return all the data until the end of the
        stream.

        """

        # Get the return type of the read method or bytes.
        annotations = getattr(self.read, '__annotations__', {})
        return_type = annotations.get('return', bytes)

        # Don't loop temporarily
        temp_loops, self.loops = self.loops, 0

        # Read till the end of the file.
        data = return_type().join([i for i in self])

        # Reset loops
        self.loops = temp_loops

        # Return the rest of the file.
        return data

    @io_wrapper
    def readinto(self, barray: bytearray) -> int:
        """ Read up to len(barray) into bytearray barray and return the number
        of bytes read otherwise returns None.

        """

        # Read len(barray) number of bytes.
        data = self.read(len(barray))

        # Return None if no data was read.
        if not data: return None

        bytes_read = len(data)

        # Convert string data to bytes
        if type(data) is str: data = data.encode()

        # Set barray to data.
        barray[:bytes_read] = data

        # Return the number of bytes read
        return bytes_read

    @io_wrapper
    def readline(self, size: int = -1) -> str:
        """ readline(size=-1) -> Returns the next line or size bytes.

        """

        if size == -1:
            # Return a whole buffer.
            return self.read(self.buffer_size)
        else:
            # Return size bytes.
            return self.read(size)

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write data to file.

        """

        raise NotImplementedError("Write method not implemented.")

    @property
    def closed(self):
        """ Return true if closed.

        """

        return self._closed

    def _open(self):
        """ _open() -> Open the classes file and set it up for read/write
        access.

        """

        raise NotImplementedError("Open method not implemented.")

    def to_seconds(self, position: int) -> int:
        """ Convert the provided position/length to seconds.

        """

        return position

    def _set_position(self, position: int):
        """ Change the position of playback.

        """

        pass

    def _get_position(self) -> int:
        """ Returns the current position.

        """

        return 0

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
    @io_wrapper
    def position(self) -> int:
        """ Get the current position.

        """

        return self._get_position()

    @position.setter
    @io_wrapper
    def position(self, position: int):
        """ Set the position.

        """

        self._set_position(int(position))

    @property
    def mode(self) -> str:
        """ Get the mode.

        """

        return self._mode

    @property
    def loop_count(self) -> int:
        """ How many times the stream has looped.

        """

        return self._loop_count

    @property
    def length(self) -> int:
        """ Get the length.

        """

        return self._length

    @property
    def floatp(self) -> int:
        """ Get the if the audio is floating point.

        """

        return self._floatp

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

        if self._buffer_size <= 0:
            self._buffer_size = 16384 // (self._depth // (8 // self._channels))

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


class DevIO(RawIOBase):
    """ File like access to audio device.

    """

    _valid_depth = (32, 24, 16, 8)
    _supported_modes = 'rw'

    def __init__(self, mode='w', depth=16, rate=44100, channels=2,
                 bigendian=False, unsigned=False, buffer_size=None,
                 latency=500000):
        """ DevIO(depth=16, rate=44100, channels=2, bigendian=False,
        unsigned=False, buffer_size=None, latency=500000) -> Initialize an
        audio device for either reading or writing.

        """

        if mode not in self._supported_modes:
            raise ValueError("(%s) Mode has to be one of %s." %
                             self.__class__.__name__,
                             self._supported_modes)

        if depth not in self._valid_depth:
            raise ValueError("(%s) Invalid depth %s.  Valid depths are: %s" %
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

    def __repr__(self) -> str:
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "mode='%(_mode)s', depth=%(_depth)s, rate=%(_rate)s, channels=%(_channels)s, bigendian=%(_bigendian)s, unsigned=%(_unsigned)s, buffer_size=%(_buffer_size)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    def __getitem__(self, item) -> object:
        """ Return the attribute.

        """

        return getattr(self, item)

    def writable(self) -> bool:
        """ Return wether this device is writable.

        """

        return 'w' in self._mode

    def readable(self) -> bool:
        """ Return wether this device is readable.

        """

        return 'r' in self._mode

    def seekable(self) -> bool:
        """ Is this stream seekable.

        """

        # It is a device it can't be seeked.
        return False

    @property
    def closed(self) -> bool:
        """ Return true if closed.

        """

        return self._closed

    def _open(self) -> object:
        """ open -> Open the pcm audio output.

        """

        raise NotImplementedError("Open method not implemented.")

    def __iter__(self) -> iter:
        """ Returns an iter of this object.

        """

        return self

    def __next__(self) -> str:
        """ Return the next buffer.

        """

        return self.read(self.buffer_size)

    def __enter__(self) -> object:
        """ Provides the ability to use pythons with statement.

        """

        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """ Close the pcm when finished.

        """

        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False

    @io_wrapper
    def read(self, length: int) -> bytes:
        """ read(length) -> Read from pcm.

        """

        raise NotImplementedError("Read method not implemented.")

    @io_wrapper
    def readinto(self, barray: bytearray) -> int:
        """ Read up to len(barray) into bytearray barray and return the number
        of bytes read otherwise returns None.

        """

        # Read len(barray) number of bytes.
        data = self.read(len(barray))

        # Return None if no data was read.
        if not data: return None

        bytes_read = len(data)

        # Set barray to data.
        barray[:bytes_read] = data

        # Return the number of bytes read
        return bytes_read

    @io_wrapper
    def write(self, data: bytes) -> int:
        """ write(data) -> Write to the pcm device.

        """

        raise NotImplementedError("Write method not implemented.")

    @property
    def mode(self) -> str:
        """ Get the mode.

        """

        return self._mode

    @property
    def depth(self) -> int:
        """ The current depth rate.

        """

        return self._depth

    @property
    def unsigned(self) -> int:
        """ The sample current sample rate.

        """

        return self._unsigned

    @property
    def rate(self) -> int:
        """ The sample current sample rate.

        """

        return self._rate

    @property
    def channels(self) -> int:
        """ The number of output channels.

        """

        return self._channels

    @property
    def buffer_size(self) -> int:
        """ The buffer size.

        """

        if self._buffer_size <= 0:
            self._buffer_size = 16384 // (self._depth // (8 // self._channels))

        return self._buffer_size
