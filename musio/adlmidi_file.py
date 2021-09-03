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

from typing import Any, Union

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

    def __init__(self, filename: str, bank: str = '-1',
                 emulator: int = 0, num_chips: int = -1, four_ops: int = -1,
                 volume_model: int = 0, rate: int = 44100, **_):
        """Initialize the playback settings of the player."""
        super(AdlmidiFile, self).__init__(filename, 'r', 16, rate, 2)

        self._rate = rate
        self._markers = []
        self._data_buffer = b''
        self._position = 0
        self._length = 0
        self._bank = int(bank) if bank == '-1' or bank.isdigit() else bank

        self._adlmidi_device = _adlmidi.adl_init(self._rate)

        if self._adlmidi_device:
            callback = _adlmidi.CFUNCTYPE(_adlmidi.c_void_p, _adlmidi.c_uint,
                                          _adlmidi.c_size_t)
            self._callback_f = callback(self._callback)
            _adlmidi.adl_setTriggerHandler(self._adlmidi_device,
                                           self._callback_f, filename)

            # Set options.
            _adlmidi.adl_setLoopEnabled(self._adlmidi_device, 1)
            _adlmidi.adl_setSoftPanEnabled(self._adlmidi_device, 1)
            _adlmidi.adl_setAutoArpeggio(self._adlmidi_device, 1)
            _adlmidi.adl_setFullRangeBrightness(self._adlmidi_device, 1)

            self._emulator = self.switch_emulator(emulator)
            self.set_bank(self._bank)
            self._num_chips = self.set_num_chips(num_chips)
            self._volume_model = self.set_volume_model(volume_model)
            self._four_ops = self.set_four_ops(four_ops)
            if self._open(filename):
                self._length = _adlmidi.adl_totalTimeLength(
                    self._adlmidi_device
                )
                self._closed = False
                self._info_dict.update(self._update_info())
            else:
                raise(OSError(f"Failed to open adlib midi: {filename}."))
        else:
            raise(Exception("Failed to init adlmidi"))

    def _get_position(self) -> float:
        """Update the position variable."""
        # Update the position.
        self._position = _adlmidi.adl_positionTell(self._adlmidi_device)
        return self._position

    def _set_position(self, position: float):
        """Change the position of playback."""
        _adlmidi.adl_positionSeek(self._adlmidi_device, position)

    def switch_emulator(self, emulator: int = 0) -> int:
        """Switch the emulator core."""
        if emulator in range(0, 5):
            _adlmidi.adl_switchEmulator(self._adlmidi_device, emulator)
        return _adlmidi.adl_chipEmulatorName(self._adlmidi_device).decode()

    def set_volume_model(self, volume_model: int) -> int:
        """Set the volume model."""
        if volume_model not in range(0, 12):
            return 0
        _adlmidi.adl_setVolumeRangeModel(self._adlmidi_device,
                                         volume_model)
        return _adlmidi.adl_getVolumeRangeModel(self._adlmidi_device)

    def set_num_chips(self, num_chips: int) -> int:
        """Set the number of chips to emulate.

        Returns the number of chips obtained.
        """
        num_chips = num_chips if num_chips in range(1, 101) else 4

        _adlmidi.adl_setNumChips(self._adlmidi_device, num_chips)

        return _adlmidi.adl_getNumChipsObtained(self._adlmidi_device)

    def set_four_ops(self, four_ops: int) -> int:
        """Set the number of four-op channesl to use.

        Returns the number of four-ops being used.
        """
        if four_ops > 0:
            _adlmidi.adl_setNumFourOpsChn(self._adlmidi_device, four_ops)

        return _adlmidi.adl_getNumFourOpsChnObtained(self._adlmidi_device)

    @classmethod
    def print_bank_list(cls):
        """Print a list of bank names."""
        banknames = _adlmidi.adl_getBankNames()
        # print(f"{'Number':<12}Name")
        print("Bank:", end="")
        for i in range(_adlmidi.adl_getBanksCount()):
            name = _adlmidi.string_at(banknames[i]).decode()
            print(f"\t{i:02}{' ':<10}{name}")

    def set_bank(self, bank: Union[int, str]):
        """Set the bank."""
        err = -1
        if type(bank) == str:
            err = _adlmidi.adl_openBankFile(self._adlmidi_device, bank)
        # elif bank in range(_adlmidi.adl_getBanksCount()):
        else:
            err = _adlmidi.adl_setBank(self._adlmidi_device, bank)
        if err < 0:
            self._bank = -1
        else:
            _adlmidi.adl_reset(self._adlmidi_device)

    def _update_info(self) -> dict:
        """Update the id3 info for the opened flac."""
        info_dict = {}

        if self._bank in range(_adlmidi.adl_getBanksCount()):
            banknames = _adlmidi.adl_getBankNames()
            info_dict['bank'] = _adlmidi.string_at(
                banknames[self._bank]
            ).decode()
        elif type(self._bank) == str:
            info_dict['bank'] = self._bank

        volume_model_list = [
            'Auto',
            'Generic',
            'Native OPL3',
            'DMX',
            'Apogee Sound System',
            '9X (SB16)',
            'DMX (fixed AM voices)',
            'Apogee Sound System (fixed AM voices)',
            'Audio Interface Library (AIL)',
            '9X (Generic FM)',
            'HMI Sound Operating System'
            'HMI Sound Operating System (old)'
        ]
        info_dict['volume model'] = volume_model_list[self._volume_model]
        info_dict['chips'] = self._num_chips
        info_dict['four-op channels'] = self._four_ops
        info_dict['emulator'] = self._emulator

        track_count = _adlmidi.adl_trackCount(self._adlmidi_device)
        info_dict['tracks'] = track_count

        title = _adlmidi.adl_metaMusicTitle(self._adlmidi_device)
        if title:
            info_dict['name'] = title.decode()

        copyright = _adlmidi.adl_metaMusicCopyright(self._adlmidi_device)
        if copyright:
            info_dict['copyright'] = copyright.decode()

        title_count = _adlmidi.adl_metaTrackTitleCount(self._adlmidi_device)
        for i in range(title_count):
            track_title = _adlmidi.adl_metaTrackTitle(self._adlmidi_device, i)
            info_dict[f"Track {i}"] = track_title.decode()

        marker_count = _adlmidi.adl_metaMarkerCount(self._adlmidi_device)
        if marker_count:
            for i in range(marker_count):
                marker = _adlmidi.adl_metaMarker(self._adlmidi_device, i)
                # info_dict[f"marker {marker.pos_time}"] = marker.label
                self._markers.append([marker.pos_time, marker.label, False])

        return info_dict

    def _callback(self, user_data: Any, trigger: int, track: int):
        """Trigger callback."""
        print(f"Trigger Callback: {user_data=}, {trigger=}, {track=}")

    def _open(self, filename: str) -> bool:
        """Open a adlib midi file."""
        try:
            # Convert filename to bytes.
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()

        if _adlmidi.adl_openFile(self._adlmidi_device, filename_b) < 0:
            msg_out(_adlmidi.adl_errorInfo(self._adlmidi_device))
            return False

        return True

    def close(self):
        """Close the adlib midi file."""
        if not self.closed and self._adlmidi_device:
            _adlmidi.adl_close(self._adlmidi_device)
            self._closed = True
            del(self._adlmidi_device)

    @property
    def loops(self) -> int:
        """Return the number of requested loops."""
        return self._loops

    @loops.setter
    def loops(self, value: int):
        """Override loops setter so internal looping can be changed."""
        self._loops = value
        if self._loops == 0:
            _adlmidi.adl_setLoopEnabled(self._adlmidi_device, 0)
        else:
            _adlmidi.adl_setLoopEnabled(self._adlmidi_device, 1)

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
                self._adlmidi_device,
                buf_size,
                _adlmidi.cast(byte_buffer, _adlmidi.POINTER(_adlmidi.c_short))
            )

            # Print some midi info about the correct time.
            for marker in self._markers:
                if int(self.position) == int(marker[0]) and not marker[2]:
                    print(f"({marker[1]}) ", end='', flush=True)
                    marker[2] = True
                elif int(self.position) < int(marker[0]) and marker[2]:
                    marker[2] = False

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
                    _adlmidi.adl_setLoopEnabled(self._adlmidi_device, 0)
                self._loop_count += 1

            # Keep track of the position so we know when it loops.
            old_position = self.position

            # Grab decoded data into data buffer.
            data += byte_buffer.raw

        self._data_buffer = data[size:]

        return data[:size]
