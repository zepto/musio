#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of audio using libsndfile.
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


"""Read and write audio using libsndfile."""

import audioop
import math
from array import array
from os.path import isfile
from pathlib import Path
from typing import Any, Callable

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out

_sndfile = LazyImport('sndfile.sndfile', globals(), locals(),
                      ['_sndfile'], 1)


__supported_dict = {
    "ext": [
        ".wav", ".aif", ".au", ".snd", ".raw", ".gsm", ".vox", ".paf", ".fap",
        ".svx", ".nist", ".sph", ".voc", ".ircam", ".sf", ".w64", ".mat",
        ".mat4", ".mat5", ".pvf", ".xi", ".htk", ".sds", ".avr", ".wavex",
        ".sd2", ".flac", ".caf", ".wve", ".prc", ".oga", ".ogg", ".opus",
        ".mpc", ".rf64"
    ],
    "handler": "SndfileFile",
    "dependencies": {
        "ctypes": ["sndfile"],
        "python": []
    }
}


class SndfileFile(AudioIO):
    """Read and write using sndfile."""

    # Valid bit depths
    _valid_depth = (32, 24, 16, 8)

    # Both reading and writing are supported
    _supported_modes = 'rw'

    # Sndfile tags list.
    _tags_dict = {
        'title': 1,
        'copyright': 2,
        'software': 3,
        'artist': 4,
        'comment': 5,
        'date': 6,
        'album': 7,
        'license': 8,
        'tracknumber': 9,
        'genre': 16
    }

    # Sndfile format dict.
    _format_dict = {
        "wav": _sndfile.SF_FORMAT_WAV,
        "aif": _sndfile.SF_FORMAT_AIFF,
        "au": _sndfile.SF_FORMAT_AU,
        "snd": _sndfile.SF_FORMAT_AU,
        "raw": _sndfile.SF_FORMAT_RAW,
        "gsm": _sndfile.SF_FORMAT_RAW | _sndfile.SF_FORMAT_GSM610,
        "vox": _sndfile.SF_FORMAT_RAW | _sndfile.SF_FORMAT_VOX_ADPCM,
        "paf": _sndfile.SF_FORMAT_PAF | _sndfile.SF_ENDIAN_BIG,
        "fap": _sndfile.SF_FORMAT_PAF | _sndfile.SF_ENDIAN_LITTLE,
        "svx": _sndfile.SF_FORMAT_SVX,
        "nist": _sndfile.SF_FORMAT_NIST,
        "sph": _sndfile.SF_FORMAT_NIST,
        "voc": _sndfile.SF_FORMAT_VOC,
        "ircam": _sndfile.SF_FORMAT_IRCAM,
        "sf": _sndfile.SF_FORMAT_IRCAM,
        "w64": _sndfile.SF_FORMAT_W64,
        "mat": _sndfile.SF_FORMAT_MAT4,
        "mat4": _sndfile.SF_FORMAT_MAT4,
        "mat5": _sndfile.SF_FORMAT_MAT5,
        "pvf": _sndfile.SF_FORMAT_PVF,
        "xi": _sndfile.SF_FORMAT_XI,
        "htk": _sndfile.SF_FORMAT_HTK,
        "sds": _sndfile.SF_FORMAT_SDS,
        "avr": _sndfile.SF_FORMAT_AVR,
        "wavex": _sndfile.SF_FORMAT_WAVEX,
        "sd2": _sndfile.SF_FORMAT_SD2,
        "flac": _sndfile.SF_FORMAT_FLAC,
        "caf": _sndfile.SF_FORMAT_CAF,
        "wve": _sndfile.SF_FORMAT_WVE,
        "prc": _sndfile.SF_FORMAT_WVE,
        "oga": _sndfile.SF_FORMAT_OGG,
        "ogg": _sndfile.SF_FORMAT_OGG | _sndfile.SF_FORMAT_VORBIS,
        "opus": _sndfile.SF_FORMAT_OGG | _sndfile.SF_FORMAT_OPUS,
        "mpc": _sndfile.SF_FORMAT_MPC2K,
        "rf64": _sndfile.SF_FORMAT_RF64,
        # "mp3": _sndfile.SF_FORMAT_MPEG | _sndfile.SF_FORMAT_MPEG_LAYER_III,
    }

    _container_name = {
        _sndfile.SF_FORMAT_WAV: "WAV",
        _sndfile.SF_FORMAT_AIFF: "AIFF",
        _sndfile.SF_FORMAT_AU: "AU",
        _sndfile.SF_FORMAT_RAW: "RAW",
        _sndfile.SF_FORMAT_PAF: "PAF",
        _sndfile.SF_FORMAT_SVX: "SVX",
        _sndfile.SF_FORMAT_NIST: "NIST",
        _sndfile.SF_FORMAT_VOC: "VOC",
        _sndfile.SF_FORMAT_IRCAM: "IRCAM",
        _sndfile.SF_FORMAT_W64: "W64",
        _sndfile.SF_FORMAT_MAT4: "MAT4",
        _sndfile.SF_FORMAT_MAT5: "MAT5",
        _sndfile.SF_FORMAT_PVF: "PVF",
        _sndfile.SF_FORMAT_XI: "XI",
        _sndfile.SF_FORMAT_HTK: "HTK",
        _sndfile.SF_FORMAT_SDS: "SDS",
        _sndfile.SF_FORMAT_AVR: "AVR",
        _sndfile.SF_FORMAT_WAVEX: "WAVEX",
        _sndfile.SF_FORMAT_SD2: "SD2",
        _sndfile.SF_FORMAT_FLAC: "FLAC",
        _sndfile.SF_FORMAT_CAF: "CAF",
        _sndfile.SF_FORMAT_WVE: "WVE",
        _sndfile.SF_FORMAT_OGG: "OGG",
        _sndfile.SF_FORMAT_MPC2K: "MPC2K",
        _sndfile.SF_FORMAT_RF64: "RF64",
        # _sndfile.SF_FORMAT_MPEG: "MPEG",
    }

    _codec_name = {
        _sndfile.SF_FORMAT_PCM_S8: "signed 8 bit PCM",
        _sndfile.SF_FORMAT_PCM_16: "16 bit PCM",
        _sndfile.SF_FORMAT_PCM_24: "24 bit PCM",
        _sndfile.SF_FORMAT_PCM_32: "32 bit PCM",
        _sndfile.SF_FORMAT_PCM_U8: "unsigned 8 bit PCM",
        _sndfile.SF_FORMAT_FLOAT: "32 bit float",
        _sndfile.SF_FORMAT_DOUBLE: "64 bit double",
        _sndfile.SF_FORMAT_ULAW: "u-law",
        _sndfile.SF_FORMAT_ALAW: "a-law",
        _sndfile.SF_FORMAT_IMA_ADPCM: "IMA ADPCM",
        _sndfile.SF_FORMAT_MS_ADPCM: "MS ADPCM",
        _sndfile.SF_FORMAT_GSM610: "gsm610",
        _sndfile.SF_FORMAT_VOX_ADPCM: "Vox ADPCM",
        _sndfile.SF_FORMAT_G721_32: "g721 32kbps",
        _sndfile.SF_FORMAT_G723_24: "g723 24kbps",
        _sndfile.SF_FORMAT_G723_40: "g723 40kbps",
        _sndfile.SF_FORMAT_DWVW_12: "12 bit DWVW",
        _sndfile.SF_FORMAT_DWVW_16: "16 bit DWVW",
        _sndfile.SF_FORMAT_DWVW_24: "14 bit DWVW",
        _sndfile.SF_FORMAT_DWVW_N: "DWVW",
        _sndfile.SF_FORMAT_DPCM_8: "8 bit DPCM",
        _sndfile.SF_FORMAT_DPCM_16: "16 bit DPCM",
        _sndfile.SF_FORMAT_VORBIS: "Vorbis",
        _sndfile.SF_FORMAT_ALAC_16: "16 bit ALAC",
        _sndfile.SF_FORMAT_ALAC_20: "20 bit ALAC",
        _sndfile.SF_FORMAT_ALAC_24: "24 bit ALAC",
        _sndfile.SF_FORMAT_ALAC_32: "32 bit ALAC",
        _sndfile.SF_FORMAT_OPUS: "Opus",
        # _sndfile.SF_FORMAT_MPEG_LAYER_I: "MPEG layer 1",
        # _sndfile.SF_FORMAT_MPEG_LAYER_II: "MPEG layer 2",
        # _sndfile.SF_FORMAT_MPEG_LAYER_III: "MPEG layer 3",
    }

    def __init__(self, filename: str, mode: str = 'r', depth: int = 32,
                 rate: int = 48000, channels: int = 2, unsigned: bool = False,
                 floatp: bool = False, comment_dict: dict[str, Any] = {}, **_):
        """Initialize the file object for reading and writing."""
        super(SndfileFile, self).__init__(filename=filename,
                                          mode=mode, depth=depth, rate=rate,
                                          channels=channels)

        self._unsigned = unsigned
        self._floatp = floatp
        self._state = None
        self._out_depth = self._depth

        if mode == 'r':
            if not isfile(filename):
                raise OSError(f"File not found: {filename}")

            self._snd_file, self._snd_info = self._read_open(filename)

            # Set the channels and rate to match the opened file.
            self._channels = self._snd_info.channels
            self._rate = self._snd_info.samplerate

            # Get the format info from the file.
            log_len = 1 << 16
            log_buf = _sndfile.create_string_buffer(log_len)
            _sndfile.sf_command(
                self._snd_file,
                _sndfile.SFC_GET_LOG_INFO,
                log_buf,
                log_len
            )
            # Extract the bit-width value from the log.
            log_str = _sndfile.string_at(log_buf).decode()
            for line in log_str.split('\n'):
                if line.lower().strip().startswith('bit'):
                    bit_depth = line.split()[-1]
                    if bit_depth.isdigit():
                        self._depth = 32 if int(bit_depth) > 16 else 16
                        self._floatp = floatp if self._depth > 16 else False
                        break

            # Set floatp and scale values based on the codec type.
            subformat = self._snd_info.format & _sndfile.SF_FORMAT_SUBMASK
            if subformat in [_sndfile.SF_FORMAT_FLOAT,
                             _sndfile.SF_FORMAT_DOUBLE]:
                self._scale = _sndfile.c_double()
                _sndfile.sf_command(
                    self._snd_file,
                    _sndfile.SFC_CALC_SIGNAL_MAX,
                    _sndfile.byref(self._scale),
                    _sndfile.sizeof(self._scale)
                )
                if self._scale.value > 1.0:
                    self._scale = 1.0 / self._scale.value
                else:
                    self._scale = 1.0

                self._depth = 32
                self._floatp = True
            else:
                self._scale = 0.0

            if self._snd_info.seekable:
                self._length = self._snd_info.frames

            self._data = b''
        else:
            self._to_alaw = False
            self._to_unsigned = False
            self._from_float = False
            self._comment_dict = comment_dict
            self._info_dict.update(self._comment_dict)

            self._snd_file, self._snd_info = self._write_open(filename)

            # subformat = self._snd_info.format & _sndfile.SF_FORMAT_SUBMASK
            # if subformat in [_sndfile.SF_FORMAT_FLOAT,
            #                  _sndfile.SF_FORMAT_DOUBLE,
            #                  _sndfile.SF_FORMAT_VORBIS,
            #                  _sndfile.SF_FORMAT_OPUS]:
            #     self._depth = 32
            #     self._floatp = True

            self._write_tags()

    @property
    def _read_func(self) -> Callable:
        """Return a function to read sound data of the correct type."""
        if self._depth <= 16:
            return _sndfile.sf_read_short
        elif self._floatp:
            return _sndfile.sf_read_float
        else:
            return _sndfile.sf_read_int

    @property
    def _write_func(self) -> Callable:
        """Return a function to write sound data of the correct type."""
        if self._out_depth <= 16:
            return _sndfile.sf_write_short
        elif self._floatp:
            # print('float write')
            return _sndfile.sf_write_float
        else:
            return _sndfile.sf_write_int

    @property
    def _buffer_func(self) -> Any:
        """Return a function to create read/write buffer."""
        depth_to_check = self._depth if self._mode == 'r' else self._out_depth
        if depth_to_check <= 16:
            return _sndfile.c_short
        elif self._floatp:
            return _sndfile.c_float
        else:
            return _sndfile.c_int

    def close(self):
        """Close and cleans up."""
        if self._mode == 'r':
            self._read_close()
        else:
            self._write_close()

    def to_seconds(self, position: int) -> float:
        """Convert the provided position/length to seconds."""
        return position / self._rate

    def _set_position(self, position: int):
        """Change the position of playback."""
        if self._snd_info.seekable:
            _sndfile.sf_seek(
                self._snd_file,
                position - self.position,
                _sndfile.SF_SEEK_CUR
            )

    def _get_position(self) -> int:
        """Get the current position."""
        self._position = _sndfile.sf_seek(
            self._snd_file,
            0,
            _sndfile.SF_SEEK_CUR
        )
        return self._position

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        if self._mode == 'r':
            repr_str = (f"filename='{self._filename}', mode={self._mode}, "
                        f"depth={self._depth}, rate={self._rate}, "
                        f"channels={self._channels}, floatp={self._floatp}, "
                        f"unsigned={self._unsigned}")
        else:
            repr_str = (f"filename='{self._filename}', mode={self._mode}, "
                        f"depth={self._depth}, rate={self._rate}, "
                        f"channels={self._channels}, "
                        f"unsigned={self._unsigned}, floatp={self._floatp}, "
                        f"comment_dict={self._comment_dict}")

        return f"{self.__class__.__name__}({repr_str})"

    def _read_open(self, filename: str) -> tuple[Any, Any]:
        """Load the specified file."""
        filename_b = filename.encode('utf-8', 'surrogateescape')

        snd_info = _sndfile.SF_INFO()
        snd = _sndfile.sf_open(filename_b, _sndfile.SFM_READ, snd_info)

        if not snd:
            print(f"Error: unable to open {filename}: "
                  f"{_sndfile.sf_strerror(None).decode()}")
            import sys
            sys.exit()

        # Read the tag information.
        for name, i in self._tags_dict.items():
            snd_str = _sndfile.sf_get_string(snd, i)
            if snd_str:
                self._info_dict[name] = snd_str.decode().strip(chr(34))

        # The file is now open.
        self._closed = False

        return snd, snd_info

    @io_wrapper
    def read(self, size: int = -1) -> bytes:
        """Read size amount of data and returns it.

        If size is None then read a buffer size.
        """
        bytes_read = -1

        # Create the read buffer.
        # data_buffer = (self._buffer_func * (self._buffer_size *
        #                                     self._channels))()
        data_buffer = _sndfile.create_string_buffer(
            self._buffer_size * _sndfile.sizeof(self._buffer_func)
        )

        # Start with any unused data from the last read.
        data = self._data

        while len(data) < size:
            # Read the data from the file.
            bytes_read = self._read_func(
                self._snd_file,
                _sndfile.cast(
                    data_buffer, _sndfile.POINTER(self._buffer_func)
                ),
                self._buffer_size
                # data_buffer,
                # self._buffer_size * self._channels
            )

            # Scale the output.
            if self._scale:
                for i in range(bytes_read):
                    data_buffer[i] *= self._scale

            # Catch and print any error strings.
            if _sndfile.sf_error(self._snd_file):
                msg_out(f"Error while reading ({bytes_read} bytes read):  "
                        f"{_sndfile.sf_strerror(self._snd_file).decode()}")

            # Check how many bytes were read.
            if bytes_read == 0 and self.position >= self._length:
                # Check if we should loop.
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the rest of the buffer with blank data and
                    # exit.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    # Increment the loop counter.
                    self._loop_count += 1

                    # Seek to the start and continue reading.
                    self.seek(0)
                    continue

            # append the data read to the buffer.
            # data += _sndfile.string_at(
            #     data_buffer,
            #     bytes_read * _sndfile.sizeof(self._buffer_func)
            # )
            data += data_buffer.raw

        # Store extra data for the next read.
        self._data = data[size:]

        # Only return the amount asked for.
        return data[:size]

    def _read_close(self):
        """Close and cleans up."""
        if not self.closed:
            _sndfile.sf_close(self._snd_file)
            del(self._snd_file)
            del(self._snd_info)

            self._closed = True

    def _convert_data(self, data: bytes, to_depth: int, to_channels: int,
                      to_rate: int, to_unsigned: bool = False) -> bytes:
        """Convert audio data."""
        out_width = to_depth // 8

        if self._from_float:
            ldata = audioop.tomono(data, self._width, 1, 0)
            rdata = audioop.tomono(data, self._width, 0, 1)
            for mono_data in [ldata, rdata]:
                float_array = array('f', mono_data)
                out_array = array('i' if self._out_depth > 16 else 'h')
                for i in float_array:
                    if i > 1.0:
                        i = 1.0
                    elif i < -1.0:
                        i = -1.0
                    out_array.append(round(i * 32767.0))
                mono_data = out_array.tobytes()
            ldata = audioop.tostereo(ldata, self._width, 1, 0)
            rdata = audioop.tostereo(rdata, self._width, 0, 1)
            data = audioop.add(ldata, rdata, self._width)

        if self._to_alaw:
            data = audioop.lin2alaw(data, self._width)

        if self._depth != to_depth:
            data = audioop.lin2lin(
                data,
                self._width,
                out_width
            )

        if self._unsigned != to_unsigned:
            data = audioop.bias(data, out_width, 128)

        # Make it stereo
        if self._channels < to_channels:
            data = audioop.tostereo(data, out_width, 1, 1)
        # Make it mono
        elif self._channels > to_channels:
            data = audioop.tomono(data, out_width, 1, 1)

        # Convert the sample rate of the data to the requested rate.
        if self._rate != to_rate and data:
            data, self._state = audioop.ratecv(
                data,
                out_width,
                to_channels,
                self._rate,
                to_rate,
                self._state,
            )

        return data

    def _write_open(self, filename: str) -> Any:
        """Load the specified file."""
        filename_b = filename.encode('utf-8', 'surrogateescape')

        self._info_dict['software'] = __name__

        snd_info = _sndfile.SF_INFO()

        # Set the sample rate and channels of the output.
        snd_info.samplerate = self._rate
        snd_info.channels = self._channels

        # Try to get a container and encoding format from the file extension.
        # If none is found use a wav container and a codec that matches the
        # bit-depth.
        file_format = self._format_dict.get(
            Path(filename).suffix.strip('.'),
            _sndfile.SF_FORMAT_WAV
        )

        # The container format.
        format_major = file_format & (_sndfile.SF_FORMAT_TYPEMASK |
                                      _sndfile.SF_FORMAT_ENDMASK)
        # The audio codec.
        format_minor = file_format & _sndfile.SF_FORMAT_SUBMASK

        if format_minor:
            snd_info.format = file_format
            if format_minor == _sndfile.SF_FORMAT_OPUS:
                # Pick the closest samplerate that is greater than or equal to
                # the source audio rate.
                for i in [8000, 12000, 16000, 24000, 48000]:
                    snd_info.samplerate = i
                    if self._rate <= i:
                        break
            elif format_minor == _sndfile.SF_FORMAT_GSM610:
                snd_info.channels = 1
                snd_info.samplerate = 8000
                self._floatp = False
        else:
            # If there is no codec set then set an appropriate one.
            if format_major == _sndfile.SF_FORMAT_OGG:
                if self._rate in [8000, 12000, 16000, 24000, 48000]:
                    snd_info.format = file_format | _sndfile.SF_FORMAT_OPUS
                else:
                    snd_info.format = file_format | _sndfile.SF_FORMAT_VORBIS
            elif format_major == _sndfile.SF_FORMAT_XI:
                self._out_depth = 16 if self._depth > 8 else 8
                snd_info.format = file_format | getattr(
                    _sndfile, (f"SF_FORMAT_DPCM_{self._out_depth}")
                )
                snd_info.channels = 1
                snd_info.samplerate = (44100 if self._rate > 44100
                                       else self._rate)
            elif format_major == _sndfile.SF_FORMAT_WAVEX:
                snd_info.format = file_format | _sndfile.SF_FORMAT_FLOAT
            elif format_major == _sndfile.SF_FORMAT_WVE:
                snd_info.format = file_format | _sndfile.SF_FORMAT_ALAW
                snd_info.samplerate = 8000
                snd_info.channels = 1
                self._floatp = False
            else:
                if format_major == _sndfile.SF_FORMAT_WAV and self._depth == 8:
                    self._unsigned = True
                elif format_major == _sndfile.SF_FORMAT_FLAC:
                    self._unsigned = False
                    if self._depth == 32:
                        self._out_depth = self._depth = 24
                elif format_major in [_sndfile.SF_FORMAT_SVX,
                                      _sndfile.SF_FORMAT_HTK,
                                      _sndfile.SF_FORMAT_SDS]:
                    snd_info.channels = 1
                    self._out_depth = 16 if self._depth > 8 else 8
                elif format_major in [_sndfile.SF_FORMAT_VOC,
                                      _sndfile.SF_FORMAT_AVR,
                                      _sndfile.SF_FORMAT_MPC2K]:
                    self._out_depth = 16 if self._depth > 8 else 8
                signed_char = ('' if self._out_depth != 8
                               else 'U' if self._unsigned else 'S')
                snd_info.format = (
                    file_format | getattr(
                        _sndfile, (
                            f"SF_FORMAT_PCM_{signed_char}{self._out_depth}"
                        )
                    )
                )

        if not _sndfile.sf_format_check(snd_info):
            snd_info.format &= (
                _sndfile.SF_FORMAT_TYPEMASK | _sndfile.SF_FORMAT_SUBMASK
            )
            snd_info.channels = 1
            if _sndfile.sf_format_check(snd_info):
                print(f"Output format does not support {self._channels} "
                      f"channels.")
            else:
                container = snd_info.format & _sndfile.SF_FORMAT_TYPEMASK
                codec = snd_info.format & _sndfile.SF_FORMAT_SUBMASK
                print(f"The '{self._container_name[container]}' "
                      f"container does not support "
                      f"'{self._codec_name[codec]}' codec data.")

            import sys
            sys.exit()

        snd_file = _sndfile.sf_open(
            filename_b,
            _sndfile.SFM_WRITE,
            snd_info
        )

        # The file is now open.
        self._closed = False

        return snd_file, snd_info

    def _write_tags(self):
        """Write tags to output file."""
        for name, value in self._info_dict.items():
            name_lower = name.lower()
            if name_lower == 'author':
                name_lower = 'artist'
            elif name_lower == 'game':
                name_lower = 'album'
            str_num = self._tags_dict.get(name_lower, 0)
            if not str_num:
                continue
            err_no = _sndfile.sf_set_string(
                self._snd_file,
                str_num,
                value.encode()
            )
            if err_no:
                msg_out(_sndfile.sf_error_number(err_no).decode())

    @io_wrapper
    def write(self, data: bytes) -> int:
        """Encode and writes str to an ogg file."""
        data = self._convert_data(
            data,
            self._out_depth,
            self._snd_info.channels,
            self._snd_info.samplerate,
            self._to_unsigned
        )

        # Create an array sized according to the bit-width.
        # data_array = array('B' if self._out_depth < 16 and not self._unsigned
        #                    else 'b' if self._out_depth == 8 and self.unsigned
        #                    else 'h' if self._out_depth == 16
        #                    else 'f' if self._floatp else 'i', data)
        # out_buffer = (self._buffer_func * len(data))(*data_array)

        # out_buffer = (self._buffer_func * len(data))()
        out_buffer = _sndfile.create_string_buffer(data)

        # Move the bytes data from data to out_buffer.
        # _sndfile.memmove(
        #     out_buffer,
        #     _sndfile.create_string_buffer(data),
        #     len(out_buffer)
        # )

        # Write out_buffer to snd_file.
        written = self._write_func(
            self._snd_file,
            # out_buffer,
            _sndfile.cast(out_buffer, _sndfile.POINTER(self._buffer_func)),
            len(out_buffer) // _sndfile.sizeof(self._buffer_func)
        )

        # Catch and print any error strings.
        if _sndfile.sf_error(self._snd_file):
            msg_out(f"Error while writing ({written} bytes written):  "
                    f"{_sndfile.sf_strerror(self._snd_file).decode()}")

        # Return how much was written.
        return written

    def _write_close(self):
        """Close and cleans up."""
        if not self.closed:
            # Finalize the file.
            _sndfile.sf_write_sync(self._snd_file)

            # Close and clear everything.
            _sndfile.sf_close(self._snd_file)

            del(self._snd_file)
            del(self._snd_info)

            # The file is closed.
            self._closed = True
