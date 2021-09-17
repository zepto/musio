#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Wild midi midi playback module.
# Copyright (C) 2021 Josiah Gordon <josiahg@gmail.com>
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


"""Use libWildMidi to read midis."""

from os import get_terminal_size
from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

_wildmidi = LazyImport('wildmidi.wildmidi', globals(),
                       locals(), ['wildmidi'], 1)


__supported_dict = {
    'ext': ['.mid', '.kar', '.hmi', '.hmp', '.mus', '.xmi'],
    'handler': 'WildMidiFile',
    'dependencies': {
        'ctypes': ['WildMidi'],
        'python': []
    }
}


class WildMidiFile(AudioIO):
    """A file like object for reading media files with libWildMidi."""

    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, wildmidi_config: str, rate: int = 44100,
                 **_):
        """Initialize the playback settings of the player."""
        super(WildMidiFile, self).__init__(filename, mode='r', depth=16,
                                           rate=rate, channels=2)

        self._data_buffer = b''
        self._position = 0
        self._length = 0
        self._config = wildmidi_config
        self._lyric_column = 0

        self._midi_file = self._open(filename, wildmidi_config)
        if self._midi_file:
            info_ptr = _wildmidi.WildMidi_GetInfo(self._midi_file)
            self._length = info_ptr.contents.approx_total_samples
            self._info_dict |= self._update_info()

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'wildmidi_config={self._config}, rate={self._rate})')

    def to_seconds(self, position: int) -> float:
        """Return the position in seconds."""
        return position / self._rate

    def _get_position(self) -> int:
        """Update the position variable."""
        # Update the position.
        info_ptr = _wildmidi.WildMidi_GetInfo(self._midi_file)
        self._position = info_ptr.contents.current_sample
        return self._position

    def _set_position(self, position: int):
        """Change the position of playback."""
        position_l = _wildmidi.ctypes.c_ulong(position)
        _wildmidi.WildMidi_FastSeek(
            self._midi_file,
            _wildmidi.ctypes.byref(position_l)
        )

    def _update_info(self) -> dict:
        """Update the id3 info for the opened flac."""
        info_dict = {}
        info_ptr = _wildmidi.WildMidi_GetInfo(self._midi_file)

        copyright = info_ptr.contents.copyright
        if copyright:
            info_dict['copyright'] = copyright.decode()

        return info_dict

    def _open(self, filename: str, config: str) -> Any:
        """Open a midi file."""
        try:
            # Convert filename to bytes.
            filename_b = filename.encode('utf-8', 'surrogateescape')
            config_b = config.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()
            config_b = config.encode()

        ret = _wildmidi.WildMidi_Init(
            config_b,
            self._rate,
            _wildmidi.WM_MO_LOG_VOLUME
            | _wildmidi.WM_MO_ENHANCED_RESAMPLING
            | _wildmidi.WM_MO_REVERB
            | _wildmidi.WM_MO_ROUNDTEMPO
        )
        if ret < 0:
            err_msg = _wildmidi.ctypes.string_at(
                _wildmidi.WildMidi_GetError()
            ).decode()
            msg_out(f"Error initializing wildmidi: {err_msg}")
            return None

        midi = _wildmidi.WildMidi_Open(filename_b)
        if not midi:
            err_msg = _wildmidi.ctypes.string_at(
                _wildmidi.WildMidi_GetError()
            ).decode()
            msg_out(f"Error opening {filename}: {err_msg}")
            return None

        self._closed = False

        return midi

    def close(self):
        """Close the file and shutdown wildmidi."""
        if not self.closed and self._midi_file:
            _wildmidi.WildMidi_Close(self._midi_file)
            _wildmidi.WildMidi_Shutdown()
            self._closed = True
            del(self._midi_file)

    def print_midi_markers(self):
        """Print midi lyrics."""
        lyric_ptr = _wildmidi.WildMidi_GetLyric(self._midi_file)
        if lyric_ptr:
            lyric = _wildmidi.ctypes.string_at(lyric_ptr).decode()
            if self._lyric_column == 0:
                lyric += ' '
                print("\033[2K")
            print("\0337", end='', flush=True)
            print("\033[1A", end='', flush=True)
            print(f"\033[{self._lyric_column}G", end='', flush=True)
            print(f"\033[0K{lyric}", end='', flush=True)
            print("\0338", end='', flush=True)
            self._lyric_column += len(lyric)
            if self._lyric_column > get_terminal_size().columns:
                self._lyric_column = 0

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        buffer = _wildmidi.ctypes.create_string_buffer(self.buffer_size)

        data = self._data_buffer[:size]

        while len(data) < size:
            bytes_read = _wildmidi.WildMidi_GetOutput(
                self._midi_file,
                _wildmidi.ctypes.cast(
                    buffer,
                    _wildmidi.ctypes.POINTER(_wildmidi.ctypes.c_int8)
                ),
                self.buffer_size
            )

            if bytes_read < 0:
                err_msg = _wildmidi.ctypes.string_at(
                    _wildmidi.WildMidi_GetError()
                ).decode()
                msg_out(f"Error reading: {err_msg}")

            # Check for the end of the stream.
            if bytes_read == 0:
                # Get the last sample so we can pad it for output.
                data = self._data_buffer
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1
                    self.seek(0)
                    continue

            data += buffer.raw

        self._data_buffer = data[size:]

        return data[:size]
