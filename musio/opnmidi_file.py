#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playing midi files using libopnmidi.
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


"""A module for playing midi files through opnmidi."""

from os import get_terminal_size

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import bytes_to_str, msg_out

_opnmidi = LazyImport('opnmidi.opnmidi', globals(), locals(), ['opnmidi'], 1)


__supported_dict = {
    'ext': ['.mus', '.mid', '.midi'],
    'handler': 'OpnmidiFile',
    'dependencies': {
        'ctypes': ['OPNMIDI'],
        'python': []
    }
}


class OpnmidiFile(AudioIO):
    """A file like object for reading media files with opus."""

    _valid_depth = (16,)

    # Only reading is supported
    _supported_modes = 'r'

    volume_model_list = [
        'Auto',
        'Generic',
        'Native OPN2',
        'DMX',
        'Apogee Sound System',
        '9X (SB16)',
    ]

    def __init__(self, filename: str,
                 bank: str = '/usr/share/sounds/wopn/xg.wopn',
                 emulator: int = 0, num_chips: int = -1,
                 volume_model: int = 0, rate: int = 44100, **_):
        """Initialize the playback settings of the player."""
        super(OpnmidiFile, self).__init__(filename, 'r', 16, rate, 2)

        self._rate = rate
        self._data_buffer = b''
        self._position = 0
        self._length = 0

        self._markers = []
        self._emulator = emulator

        try:
            assert(int(bank))
            self._bank = '/usr/share/sounds/wopn/xg.wopn'
        except ValueError:
            self._bank = bank

        self._opnmidi_device = _opnmidi.opn2_init(self._rate)

        if self._opnmidi_device:
            # Set options.
            _opnmidi.opn2_setLoopEnabled(self._opnmidi_device, 1)
            _opnmidi.opn2_setSoftPanEnabled(self._opnmidi_device, 1)
            _opnmidi.opn2_setAutoArpeggio(self._opnmidi_device, 1)
            _opnmidi.opn2_setFullRangeBrightness(self._opnmidi_device, 1)

            self.switch_emulator(emulator)
            self.set_bank(self._bank)
            self.num_chips = num_chips
            self.volume_model = volume_model

            if self._open(filename):
                self._length = _opnmidi.opn2_totalTimeLength(
                    self._opnmidi_device
                )
                self._closed = False
                self._info_dict.update(self._update_info())
            else:
                err_b = _opnmidi.opn2_errorInfo(self._opnmidi_device)
                raise(OSError(
                    f"Failed to open midi: {filename}."
                    f" {bytes_to_str(err_b)}"
                ))
        else:
            raise(Exception("Failed to init opnmidi"))

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return (f'{self.__class__.__name__}(filename="{self._filename}", '
                f'bank="{self._bank}", emulator={self._emulator}, '
                f"num_chips={self.num_chips}, "
                f"volume_model={self.volume_model}, rate={self._rate})")

    def to_seconds(self, _: int) -> float:
        """Return the curren position."""
        return self.position

    def _get_position(self) -> float:
        """Update the position variable."""
        # Update the position.
        self._position = _opnmidi.opn2_positionTell(self._opnmidi_device)
        return self._position

    def _set_position(self, position: float):
        """Change the position of playback."""
        _opnmidi.opn2_positionSeek(self._opnmidi_device, position)

    def switch_emulator(self, emulator: int = 0):
        """Switch the emulator core."""
        if emulator in range(0, 8):
            err = _opnmidi.opn2_switchEmulator(self._opnmidi_device, emulator)
            if err < 0:
                err_b = _opnmidi.opn2_errorInfo(self._opnmidi_device)
                print(f"{bytes_to_str(err_b)}")
                self._emulator = 0
            else:
                self._emulator = emulator

    @property
    def emulator_name(self) -> str:
        """Get the current emulator name."""
        return bytes_to_str(_opnmidi.opn2_chipEmulatorName(
            self._opnmidi_device
        ))

    @property
    def volume_model_name(self) -> str:
        """Get the volume model name."""
        return self.volume_model_list[self.volume_model]

    @property
    def volume_model(self) -> int:
        """Get the volume model number."""
        return _opnmidi.opn2_getVolumeRangeModel(self._opnmidi_device)

    @volume_model.setter
    def volume_model(self, volume_model: int):
        """Set the volume model."""
        if volume_model not in range(0, 6):
            return 0
        _opnmidi.opn2_setVolumeRangeModel(self._opnmidi_device,
                                          volume_model)

    @property
    def num_chips(self) -> int:
        """Return the number of chips obtained."""
        return _opnmidi.opn2_getNumChipsObtained(self._opnmidi_device)

    @num_chips.setter
    def num_chips(self, num_chips: int):
        """Set the number of chips to emulate."""
        num_chips = num_chips if num_chips in range(1, 101) else 4
        _opnmidi.opn2_setNumChips(self._opnmidi_device, num_chips)

    def set_bank(self, bank: str):
        """Set the bank."""
        err = _opnmidi.opn2_openBankFile(self._opnmidi_device, bank)
        if err < 0:
            self._bank = -1
        else:
            _opnmidi.opn2_reset(self._opnmidi_device)

    def _update_info(self) -> dict:
        """Update the id3 info for the opened flac."""
        info_dict = {}

        info_dict['bank'] = self._bank

        info_dict['volume model'] = self.volume_model_name
        info_dict['chips'] = self.num_chips
        info_dict['emulator'] = self.emulator_name

        track_count = _opnmidi.opn2_trackCount(self._opnmidi_device)
        info_dict['tracks'] = track_count

        title = _opnmidi.opn2_metaMusicTitle(self._opnmidi_device)
        if title:
            info_dict['name'] = bytes_to_str(title)

        copyright = _opnmidi.opn2_metaMusicCopyright(self._opnmidi_device)
        if copyright:
            info_dict['copyright'] = bytes_to_str(copyright)

        title_count = _opnmidi.opn2_metaTrackTitleCount(self._opnmidi_device)
        for i in range(title_count):
            track_title = _opnmidi.opn2_metaTrackTitle(self._opnmidi_device, i)
            info_dict[f"Track {i}"] = bytes_to_str(track_title)

        marker_count = _opnmidi.opn2_metaMarkerCount(self._opnmidi_device)
        if marker_count:
            column = 0
            for i in range(marker_count):
                marker = _opnmidi.opn2_metaMarker(self._opnmidi_device, i)
                label = f"({marker.label}) "
                if column + len(label) > get_terminal_size().columns:
                    column = 0
                    self._markers[i - 1]['label'] += '\n'
                if column == 0:
                    label += ' '
                marker_dict = {
                    'pos_time': marker.pos_time,
                    'label': label,
                    'shown': False,
                    'column': column,
                }
                self._markers.append(marker_dict)
                column += len(marker_dict['label'])

        return info_dict

    def _open(self, filename: str) -> bool:
        """Open a adlib midi file."""
        try:
            # Convert filename to bytes.
            filename_b = filename.encode('utf-8', 'surrogateescape')
        except AttributeError:
            filename_b = filename.encode()

        if _opnmidi.opn2_openFile(self._opnmidi_device, filename_b) < 0:
            msg_out(_opnmidi.opn2_errorInfo(self._opnmidi_device))
            return False

        return True

    def close(self):
        """Close the adlib midi file."""
        if not self.closed and self._opnmidi_device:
            _opnmidi.opn2_close(self._opnmidi_device)
            self._closed = True
            del(self._opnmidi_device)

    @property
    def loops(self) -> int:
        """Return the number of requested loops."""
        return self._loops

    @loops.setter
    def loops(self, value: int):
        """Override loops setter so internal looping can be changed."""
        self._loops = value if self._emulator != 7 else 0
        if self._loops == 0:
            _opnmidi.opn2_setLoopEnabled(self._opnmidi_device, 0)
        else:
            _opnmidi.opn2_setLoopEnabled(self._opnmidi_device, 1)

    def print_midi_markers(self):
        """Print midi marker info."""
        # Print some midi info at the correct time.
        for marker in self._markers:
            marker_time = int(marker['pos_time'])
            if int(self.position) == marker_time and not marker['shown']:
                if marker['column'] == 0:
                    print("\033[2K")
                print("\0337", end='', flush=True)
                print("\033[1A", end='', flush=True)
                print(f"\033[{marker['column']}G", end='', flush=True)
                print(f"\033[0K{marker['label']}", end='', flush=True)
                print("\0338", end='', flush=True)
                marker['shown'] = True
            elif int(self.position) < marker_time and marker['shown']:
                marker['shown'] = False

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        buf_size = 4096
        byte_buffer = _opnmidi.create_string_buffer(buf_size * 2)

        data = self._data_buffer

        old_position = self.position

        while len(data) < size:
            bytes_read = _opnmidi.opn2_play(
                self._opnmidi_device,
                buf_size,
                _opnmidi.cast(byte_buffer, _opnmidi.POINTER(_opnmidi.c_short))
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
                    _opnmidi.opn2_setLoopEnabled(self._opnmidi_device, 0)
                self._loop_count += 1

            # Keep track of the position so we know when it loops.
            old_position = self.position

            # Grab decoded data into data buffer.
            data += byte_buffer.raw

        self._data_buffer = data[size:]

        if self._emulator == 7 and len(data):
            return b'\x00' * size

        return data[:size]
