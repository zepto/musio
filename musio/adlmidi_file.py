#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of adlib midi files.
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


"""A module for reading adlib midi files."""

from typing import Any

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

_adlmidi = LazyImport('adlmidi.adlmidi', globals(), locals(), ['adlmidi'], 1)


__supported_dict = {
    'ext': ['.imf', '.wlf', '.mus', '.mid', '.midi'],
    'handler': 'AdlmidiFile',
    'dependencies': {
        'ctypes': ['ADLMIDI'],
        'python': []
    }
}


class AdlmidiFile(AudioIO):
    """A file like object for reading media files with opus."""

    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename: str, bank: int = -1, emulator: int = 0, **_):
        """Initialize the playback settings of the player."""
        super(AdlmidiFile, self).__init__(filename, 'r', 16, 44100, 2)

        self._rate = 44100
        self._data_buffer = b''
        self._position = 0
        self._length = 0
        self._bank = bank

        self._adlmidi_file = self._open(filename)

        if self._adlmidi_file:
            callback = _adlmidi.CFUNCTYPE(_adlmidi.c_void_p, _adlmidi.c_uint,
                                          _adlmidi.c_size_t)
            self._callback_f = callback(self._callback)
            _adlmidi.adl_setTriggerHandler(self._adlmidi_file,
                                           self._callback_f, filename)

            self.set_bank(bank)
            self.switch_emulator(emulator)
            self._length = _adlmidi.adl_totalTimeLength(self._adlmidi_file)
            self._closed = False
            self._info_dict.update(self._update_info())
        else:
            raise(OSError(f"Failed to open adlib midi: {filename}."))

    def _get_position(self) -> int:
        """Update the position variable."""
        # Update the position.
        self._position = _adlmidi.adl_positionTell(self._adlmidi_file)
        return self._position

    def _set_position(self, position: int):
        """Change the position of playback."""
        _adlmidi.adl_positionSeek(self._adlmidi_file, position)

    def switch_emulator(self, emulator: int = 0) -> int:
        """Switch the emulator core."""
        if emulator not in range(0, 5) or not hasattr(self, '_adlmidi_file'):
            return -1
        return _adlmidi.adl_switchEmulator(self._adlmidi_file, emulator)

    @classmethod
    def print_bank_list(cls):
        """Print a list of bank names."""
        banknames = _adlmidi.adl_getBankNames()
        print(f"{'Number':<12}Name")
        for i in range(_adlmidi.adl_getBanksCount()):
            name = _adlmidi.string_at(banknames[i]).decode()
            print(f"{i:02}{' ':<10}{name}")

    def set_bank(self, bank_num: int):
        """Set the bank."""
        if bank_num in range(_adlmidi.adl_getBanksCount()):
            _adlmidi.adl_setBank(self._adlmidi_file, bank_num)
            _adlmidi.adl_reset(self._adlmidi_file)

    def _update_info(self) -> dict:
        """Update the id3 info for the opened flac."""
        info_dict = {}

        if self._bank in range(_adlmidi.adl_getBanksCount()):
            banknames = _adlmidi.adl_getBankNames()
            info_dict['bank'] = _adlmidi.string_at(
                banknames[self._bank]
            ).decode()

        emulator = _adlmidi.adl_chipEmulatorName(self._adlmidi_file)
        info_dict['emulator'] = emulator.decode()

        track_count = _adlmidi.adl_trackCount(self._adlmidi_file)
        info_dict['tracks'] = track_count

        title = _adlmidi.adl_metaMusicTitle(self._adlmidi_file)
        if title:
            info_dict['name'] = title.decode()

        copyright = _adlmidi.adl_metaMusicCopyright(self._adlmidi_file)
        if copyright:
            info_dict['copyright'] = copyright.decode()

        title_count = _adlmidi.adl_metaTrackTitleCount(self._adlmidi_file)
        for i in range(title_count):
            track_title = _adlmidi.adl_metaTrackTitle(self._adlmidi_file, i)
            info_dict[f"Track {i}"] = track_title.decode()

        marker_count = _adlmidi.adl_metaMarkerCount(self._adlmidi_file)
        if marker_count:
            print(f"{marker_count=}")
            for i in range(marker_count):
                marker = _adlmidi.adl_metaMarker(self._adlmidi_file, i)
                print(dir(marker))

        return info_dict

    def _callback(self, user_data: Any, trigger: int, track: int):
        """Trigger callback."""
        print(f"Trigger Callback: {user_data=}, {trigger=}, {track=}")

    def _open(self, filename: str) -> Any:
        """Open a adlib midi file."""
        try:
            # Convert filename to bytes.
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()

        adlmidi_file = _adlmidi.adl_init(self.rate)
        if _adlmidi.adl_openFile(adlmidi_file, filename_b) < 0:
            msg_out(_adlmidi.adl_errorInfo(adlmidi_file))
            return None

        # Set options.
        _adlmidi.adl_setLoopEnabled(adlmidi_file, 1)
        _adlmidi.adl_setSoftPanEnabled(adlmidi_file, 1)
        _adlmidi.adl_setAutoArpeggio(adlmidi_file, 1)
        _adlmidi.adl_setFullRangeBrightness(adlmidi_file, 1)

        return adlmidi_file

    def close(self):
        """Close the adlib midi file."""
        if not self.closed and self._adlmidi_file:
            _adlmidi.adl_close(self._adlmidi_file)
            self._closed = True
            del(self._adlmidi_file)

    @property
    def loops(self) -> int:
        """Return the number of requested loops."""
        return self._loops

    @loops.setter
    def loops(self, value: int):
        """Override loops setter so internal looping can be changed."""
        self._loops = value
        if self._loops == 0:
            _adlmidi.adl_setLoopEnabled(self._adlmidi_file, 0)
        else:
            _adlmidi.adl_setLoopEnabled(self._adlmidi_file, 1)

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        buf_size = 4096
        byte_buffer = _adlmidi.create_string_buffer(buf_size * 2)

        data = self._data_buffer

        old_position = self.position

        while len(data) < size:
            bytes_read = _adlmidi.adl_play(
                self._adlmidi_file,
                buf_size,
                _adlmidi.cast(byte_buffer, _adlmidi.POINTER(_adlmidi.c_short))
            )

            # Check for the end of the stream.
            if old_position > self.position or bytes_read <= 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                elif self._loops != -1:
                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Disable internal looping so the song can end naturally.
                    _adlmidi.adl_setLoopEnabled(self._adlmidi_file, 0)
                self._loop_count += 1

            # Keep track of the position so we know when it loops.
            old_position = self.position

            # Grab decoded data into data buffer.
            data += byte_buffer.raw

        self._data_buffer = data[size:]

        return data[:size]
