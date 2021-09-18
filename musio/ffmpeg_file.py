#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the reading of media files using ffmpeg.
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


"""A module for reading media files using ffmpeg."""

import sys
from array import array
from typing import Any, Callable

from .import_util import LazyImport
from .io_base import AudioIO, io_wrapper
from .io_util import msg_out, silence

_av = LazyImport('ffmpeg.av', globals(), locals(), ['av'], 1)

__supported_dict = {
    "in_ext": [".str", ".aa", ".aac", ".aax", ".ac3", ".acm", ".adf", ".adp",
               ".dtk", ".ads", ".ss2", ".adx", ".aea", ".afc", ".aix", ".al",
               ".ape", ".apl", ".mac", ".aptx", ".aptxhd", ".aqt", ".ast",
               ".obu", ".avi", ".avs", ".avr", ".avs", ".avs2", ".avs3",
               ".bfstm", ".bcstm", ".binka", ".bit", ".bmv", ".brstm", ".cdg",
               ".cdxl", ".xl", ".c2", ".302", ".daud", ".str", ".adp", ".dav",
               ".dss", ".dts", ".dtshd", ".dv", ".dif", ".cdata", ".eac3",
               ".paf", ".fap", ".flm", ".flac", ".flv", ".fsb", ".fwse",
               ".g722", ".722", ".tco", ".rco", ".g723_1", ".g729", ".genh",
               ".gsm", ".h261", ".h26l", ".h264", ".264", ".avc", ".hca",
               ".hevc", ".h265", ".265", ".idf", ".ifv", ".cgi", ".ipu",
               ".sf", ".ircam", ".ivr", ".kux", ".669", ".abc", ".amf",
               ".ams", ".dbm", ".dmf", ".dsm", ".far", ".it", ".mdl", ".med",
               ".mid", ".mod", ".mt2", ".mtm", ".okt", ".psm", ".ptm", ".s3m",
               ".stm", ".ult", ".umx", ".xm", ".itgz", ".itr", ".itz",
               ".mdgz", ".mdr", ".mdz", ".s3gz", ".s3r", ".s3z", ".xmgz",
               ".xmr", ".xmz", ".flv", ".dat", ".lvf", ".m4v", ".mkv",
               ".mk3d", ".mka", ".mks", ".webm", ".mca", ".mcc", ".mjpg",
               ".mjpeg", ".mpo", ".j2k", ".mlp", ".mods", ".moflex", ".mov",
               ".mp4", ".m4a", ".3gp", ".3g2", ".mj2", ".psp", ".m4b", ".ism",
               ".ismv", ".isma", ".f4v", ".mp2", ".mp3", ".m2a", ".mpa",
               ".mpc", ".mjpg", ".mpl2", ".sub", ".msf", ".mtaf",
               ".ul", ".musx", ".mvi", ".mxg", ".v", ".nist", ".sph", ".nsp",
               ".nut", ".obu", ".ogg", ".oma", ".omg", ".aa3", ".pjs", ".pvf",
               ".yuv", ".cif", ".qcif", ".rgb", ".rt", ".rsd", ".rsd", ".rso",
               ".sw", ".sb", ".smi", ".sami", ".sbc", ".msbc", ".sbg", ".scc",
               ".sdr2", ".sds", ".sdx", ".ser", ".sga", ".shn", ".vb", ".son",
               ".imx", ".sln", ".mjpg", ".stl", ".sub", ".sub", ".sup",
               ".svag", ".svs", ".tak", ".thd", ".tta", ".ans", ".art",
               ".asc", ".diz", ".ice", ".nfo", ".vt", ".ty", ".ty+",
               ".uw", ".ub", ".v210", ".yuv10", ".vag", ".vc1", ".rcv",
               ".viv", ".idx", ".vpk", ".vqf", ".vql", ".vqe", ".vtt",
               ".wsd", ".xmv", ".xvag", ".yop", ".y4m"],
    "out_ext": [".3g2", ".3gp", ".a64", ".ac3", ".aac", ".adts", ".adx",
                ".aif", ".aiff", ".afc", ".aifc", ".al", ".tun", ".pcm",
                ".amr", ".amv", ".apm", ".apng", ".aptx", ".aptxhd", ".asf",
                ".wmv", ".wma", ".asf", ".wmv", ".wma", ".ass", ".ssa",
                ".ast", ".au", ".avi", ".avs", ".avs2", ".bit", ".caf",
                ".cavs", ".c2", ".mpd", ".302", ".drc", ".vc2", ".dnxhd",
                ".dnxhr", ".dts", ".dv", ".dvd", ".eac3", ".f4v", ".ffmeta",
                ".cpk", ".flm", ".fits", ".flac", ".flv", ".g722", ".tco",
                ".rco", ".gif", ".gsm", ".gxf", ".h261", ".h263", ".h264",
                ".264", ".hevc", ".h265", ".265", ".m3u8", ".ico", ".lbc",
                ".bmp", ".dpx", ".exr", ".jls", ".jpeg", ".jpg", ".ljpg",
                ".pam", ".pbm", ".pcx", ".pfm", ".pgm", ".pgmyuv", ".png",
                ".ppm", ".sgi", ".tga", ".tif", ".tiff", ".jp2", ".j2c",
                ".j2k", ".xwd", ".sun", ".ras", ".rs", ".im1", ".im8",
                ".im24", ".sunras", ".xbm", ".xface", ".pix", ".y", ".m4v",
                ".m4a", ".m4b", ".sf", ".ircam", ".ismv", ".isma", ".ivf",
                ".jss", ".js", ".vag", ".latm", ".loas", ".lrc", ".m4v",
                ".mkv", ".sub", ".mjpg", ".mjpeg", ".mlp", ".mmf", ".mov",
                ".mp2", ".m2a", ".mpa", ".mp3", ".mp4", ".mpg", ".mpeg",
                ".mpg", ".mpeg", ".m1v", ".m2v", ".ts", ".m2t", ".m2ts",
                ".mts", ".mjpg", ".ul", ".mxf", ".mxf", ".nut", ".oga",
                ".ogg", ".ogv", ".oma", ".opus", ".mp4", ".psp", ".yuv",
                ".rgb", ".rm", ".ra", ".roq", ".rso", ".sw", ".sb", ".sbc",
                ".msbc", ".scc", ".sox", ".spdif", ".spx", ".srt", ".sup",
                ".vob", ".swf", ".thd", ".tta", ".ttml", ".uw", ".ub", ".vc1",
                ".rcv", ".vob", ".voc", ".w64", ".wav", ".webm", ".chk",
                ".webp", ".vtt", ".wtv", ".wv", ".y4m"],
    "ext": [],
    'protocol': ['http'],
    'handler': 'FFmpegFile',
    'dependencies': {
        'ctypes': ['avcodec', 'avdevice', 'avformat', 'swresample', 'swscale'],
        'python': []
    }
}
__supported_dict["ext"] = set(
    __supported_dict["out_ext"] + __supported_dict["in_ext"]
)


class FFmpegFile(AudioIO):
    """A file like object for reading media files with ffmpeg."""

    # Only reading is supported
    _supported_modes = 'rw'

    def __init__(self, filename: str, mode: str = 'r', depth: int = 16,
                 rate: int = 44100, channels: int = 2, floatp: bool = False,
                 unsigned: bool = False, resample: bool = True,
                 bit_rate: int = 12800, comment_dict: dict = {}, **_):
        """Initialize the playback settings of the player.

        filename -> The file to play.
        depth    -> The bit depth to output when read is called.
        rate     -> The sample rate to output on read.
        channels -> The number of channels in output data.
        floatp   -> Output floating point data.
        unsigned -> Output unsigned data.
        resample -> Resample audio to the specified values if True
                    else use the files values.
        """
        super(FFmpegFile, self).__init__(filename, mode=mode, depth=depth,
                                         rate=rate, channels=channels)

        # Initialize ffmpeg.
        _av.avdevice_register_all()

        self.__network_stream = False
        self._resample_data = resample
        self._unsigned = unsigned
        self._floatp = floatp
        self._depth = 32 if self._floatp else depth
        self._bit_rate = bit_rate
        self._channel_layout = _av.av_get_default_channel_layout(
            self._channels
        )

        self._position = 0
        self._seek_pos = -1

        self._data = b''

        # Open the file.
        if mode == 'r':
            (
                self.__codec_context_ptr,
                self.__audio_stream_index,
                self.__format_context_ptr
            ) = self._read_open(filename)

            self._bit_rate = self.__codec_context_ptr.contents.bit_rate

            # Update the file info.
            if not resample:
                self._rate = int(self.__codec_context_ptr.contents.sample_rate)
                self._channels = int(
                    self.__codec_context_ptr.contents.channels
                )

                # Get the bit depth.
                codec_depth = _av.av_get_bytes_per_sample(
                    self.__codec_context_ptr.contents.sample_fmt
                )

                self._depth = codec_depth * 8

                # Use the sample format string to determine the depth and
                # whether it is signed.
                d_str = _av.av_get_sample_fmt_name(
                    self.__codec_context_ptr.contents.sample_fmt
                )
                d_str = d_str.decode()

                # Extract the signed and depth properties from the sample
                # format string.
                self._unsigned = 'u' in d_str.lower()
                # self._floatp = (
                #     d_str.lower() in ['fltp', 'flt', 'dblp', 'dbl']
                # )
                # self._sample_fmt = self.__codec_context.contents.sample_fmt

            self._sample_fmt = self._get_sample_fmt()

            # Create the resampling context.
            self.__swr_ptr = self._get_swr(self.__codec_context_ptr.contents)

            # The length of the file is in av time base units.  To get the
            # actual time devide it by 1000, but we use this to seek.
            self._length = self.__format_context_ptr.contents.duration
        else:
            # Open the file for encoding.
            self._comment_dict = comment_dict
            (
                self.__format_context_ptr,
                self.__codec_context_ptr
            ) = self._write_open(filename)

            self._unsigned = True if depth < 16 else self._unsigned
            self._sample_fmt = self._get_sample_fmt()

            # Create the resampling context.
            self.__swr_ptr = self._get_swr(self.__codec_context_ptr.contents)

            # Create the frame to hold the output data for encoding.
            self.__frame_ptr = self._alloc_frame(
                self.__codec_context_ptr.contents.sample_rate,
                self.__codec_context_ptr.contents.sample_fmt,
                self.__codec_context_ptr.contents.channel_layout,
                self.__codec_context_ptr.contents.channels
            )

            sample_size = _av.av_get_bytes_per_sample(self._sample_fmt)

            # The size of the input buffer is the number of samples per channel
            # times the number of channels times the sample size.
            self._buffer_len = (
                self.__frame_ptr.contents.nb_samples
                * self._channels * sample_size
            )

            # Create the frame to hold the input data for resampling.
            self.__input_frame_ptr = self._alloc_frame(
                self._rate,
                self._sample_fmt,
                self._channel_layout,
                self._channels
            )

            _ = self._check(
                _av.av_frame_make_writable(self.__input_frame_ptr),
                "Unable to make input frame writable.",
                IOError
            )

            self._next_pts = 0
            self._samples_count = 0

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
                        f"floatp={self._floatp}, unsigned={self._unsigned}, "
                        f"comment_dict={self._comment_dict}")

        return f"{self.__class__.__name__}({repr_str})"

    def _check(self, ret: int, msg: str = '',
               raise_err: Callable = None) -> int:
        """Check if there was an error and print the result."""
        if ret < 0:
            errbuf = _av.create_string_buffer(128)
            _av.av_strerror(ret, errbuf, _av.sizeof(errbuf))
            msg_out(f"{ret}: {errbuf.raw.decode('utf8', 'replace')}")
            if raise_err:
                raise(raise_err(msg))

        return ret

    def _get_sample_fmt(self) -> int:
        """Return the sample format of the output audio."""
        signed_char = ('' if self._floatp else
                       'U' if self._unsigned else 'S')
        return getattr(
            _av,
            f"AV_SAMPLE_FMT_{signed_char}"
            f"{'FLT' if self._floatp else self._depth}"
        )

    def _set_position(self, position: int):
        """Change the position of playback."""
        # We have to seek when the stream is ready not now.
        self._seek_pos = position

    def _get_position(self) -> int:
        """Return the current position."""
        return self._position
        # return _av.avio_seek(
        #     self.__format_context.contents.pb,
        #     0,
        #     1  # SEEK_CUR
        # )

        # Update the position.
        # stream = self.__format_context.contents.streams[self.__audio_stream]
        # We have to multiply the current position by the time base units so it
        # will correspond to the duration, and allow us to seek.
        # return stream.contents.cur_dts * stream.contents.time_base.den
        # return stream.contents.cur_dts * stream.contents.time_base.den

    def _set_metadata(self, metadata: Any):
        """Set the metadata from the comments dict."""
        for key, value in self._comment_dict.items():
            _ = self._check(_av.av_dict_set(
                metadata,
                key.encode(),
                value.encode(),
                0
            ))

    def _get_metadata(self, metadata: Any) -> dict:
        """Get the metadata from the metadata AVDictionary."""
        return_dict = {}

        # Get the first item.
        prev_item = _av.av_dict_get(
            metadata,
            "",
            None,
            _av.AV_DICT_IGNORE_SUFFIX
        )
        # Loop over all the items.
        while prev_item:
            try:
                key = prev_item.contents.key.data.decode()
            except UnicodeDecodeError:
                try:
                    key = prev_item.contents.key.data.decode(
                        'cp437',
                        'replace'
                    )
                except UnicodeDecodeError:
                    continue

            try:
                value = prev_item.contents.value.data.decode()
            except UnicodeDecodeError:
                try:
                    value = prev_item.contents.value.data.decode(
                        'cp437',
                        'replace'
                    )
                except UnicodeDecodeError:
                    continue

            return_dict[key] = value
            # Get the next item.
            prev_item = _av.av_dict_get(
                metadata,
                "",
                prev_item,
                _av.AV_DICT_IGNORE_SUFFIX
            )

        return return_dict

    def _write_open(self, filename: str) -> tuple[Any, Any]:
        """Open the specified file."""
        # Create a bytes version of the filename to use with ctypes functions.
        filename_b = filename.encode('utf-8', 'surrogateescape')

        format_context_ptr = _av.POINTER(_av.AVFormatContext)()
        ret = self._check(_av.avformat_alloc_output_context2(
            _av.byref(format_context_ptr),
            None,
            None,
            filename_b
        ))

        if ret < 0:
            print("Could not deduce output format from filename: using opus.")
            ret = self._check(_av.avformat_alloc_output_context2(
                _av.byref(format_context_ptr),
                None,
                b'opus',
                filename_b
            ), "avformat failed to allocat context", Exception)

        codec_id = format_context_ptr.contents.oformat.contents.audio_codec
        if codec_id == _av.AV_CODEC_ID_NONE:
            raise(Exception("No output codec found."))

        codec = _av.avcodec_find_encoder(codec_id)
        if not codec:
            raise(Exception(f"No encoder found for "
                            f"{_av.avcodec_get_name(codec_id)}"))

        output_stream_ptr = _av.avformat_new_stream(format_context_ptr, None)
        if not output_stream_ptr:
            raise(Exception("Could not create stream."))

        codec_context_ptr = _av.avcodec_alloc_context3(codec)
        if not codec_context_ptr:
            raise(Exception("Could not create codec context."))

        codec_sample_fmts = codec.contents.sample_fmts
        if codec_sample_fmts:
            codec_context_ptr.contents.sample_fmt = codec_sample_fmts[0]
        else:
            codec_context_ptr.contents.sample_fmt = _av.AV_SAMPLE_FMT_FLTP

        codec_context_ptr.contents.bit_rate = self._bit_rate

        codec_context_ptr.contents.sample_rate = self._rate
        if codec.contents.supported_samplerates:
            codec_context_ptr.contents.sample_rate = (
                codec.contents.supported_samplerates[0]
            )
            i = 0
            while codec.contents.supported_samplerates[i]:
                if codec.contents.supported_samplerates[i] == self._rate:
                    codec_context_ptr.contents.sample_rate = self._rate
                i += 1

        codec_context_ptr.contents.channels = self._channels

        codec_context_ptr.contents.channel_layout = self._channel_layout
        codec_channel_layouts = codec.contents.channel_layouts
        if codec_channel_layouts:
            codec_context_ptr.contents.channel_layout = (
                codec_channel_layouts[0]
            )
            i = 0
            while codec_channel_layouts[i]:
                if codec_channel_layouts[i] == self._channel_layout:
                    codec_context_ptr.contents.channel_layout = (
                        self._channel_layout
                    )
                i += 1
        codec_context_ptr.contents.channels = (
            _av.av_get_channel_layout_nb_channels(
                codec_context_ptr.contents.channel_layout
            )
        )

        time_base = _av.AVRational()
        time_base.num = 1
        time_base.den = codec_context_ptr.contents.sample_rate
        codec_context_ptr.contents.time_base = time_base

        # Open the codec context.
        self._check(_av.avcodec_open2(codec_context_ptr, codec, None))

        # Set the stream parameters from the codec_context.
        self._check(_av.avcodec_parameters_from_context(
            output_stream_ptr.contents.codecpar, codec_context_ptr
        ))

        # Show the format information.
        with silence(sys.stderr):
            _av.av_dump_format(
                format_context_ptr,
                0,
                filename_b,
                1
            )

        ret = self._check(_av.avio_open(
            _av.byref(format_context_ptr.contents.pb),
            filename_b,
            _av.AVIO_FLAG_WRITE
        ), f"Error opening {filename}", IOError)

        # Set the metadata.
        self._set_metadata(format_context_ptr.contents.metadata)

        # Write the header.
        ret = self._check(_av.avformat_write_header(format_context_ptr, None),
                          f"Error writing the header in {filename}", IOError)

        self._closed = False

        return format_context_ptr, codec_context_ptr

    def _alloc_frame(self, sample_rate: int, sample_fmt: int,
                     channel_layout: int, channels: int) -> Any:
        """Allocate a frame and set its parameters."""
        if (self.__codec_context_ptr.contents.codec.contents.capabilities
                & _av.AV_CODEC_CAP_VARIABLE_FRAME_SIZE):
            nb_samples = 10000
        else:
            nb_samples = self.__codec_context_ptr.contents.frame_size

        frame = _av.av_frame_alloc()

        frame.contents.sample_rate = sample_rate
        frame.contents.nb_samples = nb_samples
        frame.contents.format = sample_fmt
        frame.contents.channel_layout = channel_layout
        frame.contents.channels = channels

        if nb_samples:
            ret = _av.av_frame_get_buffer(frame, 0)
            if ret < 0:
                raise(MemoryError("Unable to allocate frame buffer."))

        return frame

    def write(self, data: bytes) -> int:
        """Write data to file and return how much was written."""
        self._data += data
        if len(self._data) < self._buffer_len:
            return 0
        out_data = self._data[:self._buffer_len]
        self._data = self._data[self._buffer_len:]

        return self._encode(out_data)

    def _encode(self, data: bytes) -> int:
        """Encode the data and return the length."""
        self.__frame_ptr.contents.pts = self._next_pts
        self._next_pts += self.__frame_ptr.contents.nb_samples

        out_linesize = self._resample_from_bytes(data)

        if out_linesize < 0:
            raise(BufferError("Error resampling."))
        elif not out_linesize and not data:
            return 0

        ret = self._check(_av.avcodec_send_frame(
            self.__codec_context_ptr,
            self.__frame_ptr
        ), "avcodec_send_frame failed", Exception)
        packet_ptr = _av.av_packet_alloc()
        stream_ptr = self.__format_context_ptr.contents.streams[0]
        while ret >= 0:
            ret = self._check(_av.avcodec_receive_packet(
                self.__codec_context_ptr,
                packet_ptr
            ))
            if ret in (-11, -541478725):  # EAGAIN, AVERROR_EOF
                break
            elif ret < 0:
                print("Error in recieve packet.")
                break

            _av.av_packet_rescale_ts(
                packet_ptr,
                self.__codec_context_ptr.contents.time_base,
                stream_ptr.contents.time_base
            )
            packet_ptr.contents.stream_index = 0

            ret = self._check(_av.av_interleaved_write_frame(
                self.__format_context_ptr,
                packet_ptr if data else None
            ))
            if ret < 0:
                print("Error writing frame.")
            _av.av_packet_unref(packet_ptr)

        return len(data)

    def _read_open(self, filename: str) -> tuple[Any, int, Any]:
        """Load the specified file."""
        # Create a bytes version of the filename to use with ctypes functions.
        filename_b = filename.encode('utf-8', 'surrogateescape')

        # Check if it is a network stream.
        if b'://' in filename_b:
            _av.avformat_network_init()
            self.__network_stream = True

        # Create a format context, and open the file.
        format_context_ptr = _av.avformat_alloc_context()
        self._check(_av.avformat_open_input(
            format_context_ptr,
            filename_b,
            None,
            None
        ))
        # Find the stream info.
        self._check(_av.avformat_find_stream_info(format_context_ptr, None))

        # Temorary variables used for finding the audio stream.
        # nb_streams = format_context.contents.nb_streams
        # streams = format_context.contents.streams

        # audio_stream_index = 0
        # stream = _av.AVStream()
        # for i in range(nb_streams):
        #     codec_type = streams[i].contents.codec.contents.codec_type
        #     if codec_type == _av.AVMEDIA_TYPE_AUDIO:
        #         # Remember audio stream index.
        #         audio_stream_index = i
        #         # Save the audio stream and exit the loop.
        #         stream = streams[i]
        #         break

        # Allocate space for the decoder codec.
        codec_ptr = _av.POINTER(_av.AVCodec)()

        # Determine which stream is the audio stream and put the decoder for it
        # in codec.
        audio_stream_index = self._check(_av.av_find_best_stream(
            format_context_ptr,
            _av.AVMEDIA_TYPE_AUDIO,
            -1,
            -1,
            _av.byref(codec_ptr),
            0
        ), "No audio stream was found.", Exception)

        with silence(sys.stderr):
            _av.av_dump_format(
                format_context_ptr,
                audio_stream_index,
                filename_b,
                0
            )

        # Get the stream.
        stream_ptr = format_context_ptr.contents.streams[audio_stream_index]

        # Grab the files metadata.
        self._info_dict.update(self._get_metadata(
            format_context_ptr.contents.metadata
        ))
        # Grab the stream metadata.
        self._info_dict.update(self._get_metadata(
            stream_ptr.contents.metadata
        ))

        # Allocate space for the codec context.
        codec_context_ptr = _av.avcodec_alloc_context3(None)

        # Create a codec context from the stream parameters.
        self._check(_av.avcodec_parameters_to_context(
            codec_context_ptr,
            stream_ptr.contents.codecpar
        ))
        codec_context_ptr.contents.pkt_timebase = stream_ptr.contents.time_base

        # Find the codec to decode the audio.
        # codec = _av.avcodec_find_decoder(
        #     stream.contents.codec.contents.codec_id
        # )

        # Get the codec and open a codec context from it.
        self._check(_av.avcodec_open2(
            codec_context_ptr,
            codec_ptr,
            None
        ), "avcodec_open2 Failed to open codec_context", IOError)

        # The file is now open.
        self._closed = False

        return codec_context_ptr, audio_stream_index, format_context_ptr

    def _get_swr(self, codec_context: Any) -> Any:
        """Return an allocated SWResamleContext."""
        swr_ptr = _av.swr_alloc()
        if not swr_ptr:
            raise(Exception("Unable to allocate avresample context"))

        if self._mode == 'r':
            if codec_context.channel_layout == 0:
                # If the channel layout is invalid set it based on the number
                # of channels defined in the codec_context.
                in_channel_layout = _av.av_get_default_channel_layout(
                    codec_context.channels
                )
            else:
                in_channel_layout = codec_context.channel_layout
            in_sample_fmt = codec_context.sample_fmt
            in_sample_rate = codec_context.sample_rate

            out_channel_layout = self._channel_layout
            out_sample_fmt = self._sample_fmt
            out_sample_rate = self._rate
        else:
            in_channel_layout = self._channel_layout
            in_sample_fmt = self._sample_fmt
            in_sample_rate = self._rate

            out_channel_layout = codec_context.channel_layout
            out_sample_fmt = codec_context.sample_fmt
            out_sample_rate = codec_context.sample_rate

        _av.swr_alloc_set_opts(
            swr_ptr,
            # Output options.
            out_channel_layout,
            out_sample_fmt,
            out_sample_rate,
            # Input options
            in_channel_layout,
            in_sample_fmt,
            in_sample_rate,
            # Logging options
            0,
            None
        )

        self._check(_av.swr_init(swr_ptr), "Failed to initialize swr context",
                    Exception)

        return swr_ptr

    def _drain_decoder(self, av_packet: Any, frame: Any) -> bytes:
        """Drain the decoder and return the resulting bytes."""
        # Send packet to the decoder to decode.
        ret = self._check(_av.avcodec_send_packet(
            self.__codec_context_ptr, av_packet
        ))
        if ret == 0:
            # Recieve the decoded data, from the decoder, into frame.
            ret = self._check(_av.avcodec_receive_frame(
                self.__codec_context_ptr,
                frame
            ))
            # Return nothing on and error other than EOF and EAGAIN.
            if ret < 0 and ret not in (-11, -541478725):
                return b''
        else:
            return b''

        # Resample or return interleaved data.
        if self._resample_data or (self._sample_fmt != frame.contents.format):
            return self._resample_from_frame(frame)
        else:
            return self._get_interleaved_data(frame)

    @io_wrapper
    def read(self, size: int) -> bytes:
        """Read size amount of data and return it.

        If size is -1 read the entire file.
        """
        data = self._data

        # Create the packet to decode from.
        av_packet = _av.av_packet_alloc()

        # Create and setup a frame to read the data into.
        frame = _av.av_frame_alloc()

        # Seek before next read begins.
        if self._seek_pos > -1:
            with silence(sys.stderr):
                ret = _av.avformat_seek_file(
                    self.__format_context_ptr,
                    -1,
                    -sys.maxsize - 1,
                    self._seek_pos,
                    sys.maxsize,
                    1
                )
            self._check(ret)

            _av.avcodec_flush_buffers(self.__codec_context_ptr)

            # Reset the seek so we don't continue seeking.
            self._seek_pos = -1

        while not data or len(data) < size:
            # Read the next frame.
            if _av.av_read_frame(self.__format_context_ptr, av_packet) < 0:
                data += self._drain_decoder(av_packet, frame)
                # If no data was read then we have reached the end of the
                # file so restart or exit.
                if self._loops != -1 and self._loop_count >= self._loops:
                    # Fill the data buffer with nothing so it will be a
                    # frame size for output.
                    if len(data) != 0:
                        data += b'\x00' * (size - len(data))
                else:
                    # Fill the buffer so we return the requested size.
                    data += b'\x00' * (size - len(data))

                    # Update the loop count and seek to the start.
                    self._loop_count += 1
                    self.seek(0)

                # Exit.
                break

            # Calculate the current position.
            stream = self.__format_context_ptr.contents.streams[
                self.__audio_stream_index
            ]
            self._position = (1000000 *
                              (av_packet.contents.pts *
                               (stream.contents.time_base.num /
                                stream.contents.time_base.den)))

            # If the packet read is not audio then skip it.
            if av_packet.contents.stream_index != self.__audio_stream_index:
                _av.av_packet_unref(av_packet)
                continue

            # Reset the frame, (I don't know if this is necessary).
            _av.av_frame_unref(frame)

            # data_size = _av.av_samples_get_buffer_size(
            #     None,
            #     frame.contents.channels,
            #     frame.contents.nb_samples,
            #     frame.contents.format,
            #     1
            # )

            # Get the decoded data.
            data += self._drain_decoder(av_packet, frame)

            # Unreference the packet resetting it to default.
            _av.av_packet_unref(av_packet)

        # Free the frame and packet.
        _av.av_frame_unref(frame)
        _av.av_frame_free(_av.byref(frame))
        _av.av_packet_unref(av_packet)
        _av.av_packet_free(_av.byref(av_packet))

        # Store extra data for next time.
        self._data = data[size:]

        # Make sure we return only the number of bytes requested.
        return data[:size]

    def _get_interleaved_data(self, frame: Any) -> bytes:
        """Process the data in frame and return it.

        If the data in frame is planar data, interleave it and return the
        result.  If it is already interleaved, than just return it as a bytes
        object.
        """
        if _av.av_sample_fmt_is_planar(frame.contents.format):
            # Get the sample_size to determint the data type for the output.
            sample_size = _av.av_get_bytes_per_sample(frame.contents.format)
            # Array to hold the output data.
            data_array = array('l' if sample_size == 8 else
                               'i' if sample_size == 4 else
                               'h' if sample_size == 2 else
                               'b')
            # The data type to cast the data to.
            cast_to_type = (_av.c_int64 if sample_size == 8 else
                            _av.c_int32 if sample_size == 4 else
                            _av.c_int16 if sample_size == 2 else
                            _av.c_uint8)

            nb_samples = frame.contents.nb_samples

            # Loop over the number of samples and interleave data into
            # data_array
            for s in range(nb_samples):
                # Loop over the channels.
                for c in range(frame.contents.channels):
                    # Cast the data to the correct size data type.
                    temp_data = _av.cast(
                        frame.contents.extended_data[c],
                        _av.POINTER(cast_to_type)
                    )[s]
                    # Append the data to the array
                    data_array.append(temp_data)
            # Return the data_array as bytes.
            return data_array.tobytes()
        else:
            # The input was already interleaved so just send it back.
            return _av.string_at(
                frame.contents.extended_data[0],
                frame.contents.linesize[0]
            )

    def _resample_from_bytes(self, data: bytes) -> int:
        """Resample the data into self.__frame and return out_linesize."""
        _ = self._check(
            _av.av_frame_make_writable(self.__frame_ptr),
            "av_frame_make_writable Failed", Exception
        )

        self.__input_frame_ptr.contents.extended_data[0] = _av.cast(
            _av.create_string_buffer(data),
            _av.POINTER(_av.c_uint8)
        )

        return _av.swr_convert_frame(
            self.__swr_ptr,
            self.__frame_ptr,
            self.__input_frame_ptr if data else None
        )

        # out_samples = _av.av_rescale_rnd(
        #     # Set the delay to output samples.
        #     _av.swr_get_delay(
        #         self.__swr_ptr,
        #         self._rate
        #     ) + self.__frame_ptr.contents.nb_samples,
        #     self.__codec_context_ptr.contents.sample_rate,
        #     self._rate,
        #     _av.AV_ROUND_UP
        # )
        # assert(self.__frame_ptr.contents.nb_samples == out_samples)
        #
        # # Resample the data.
        # return _av.swr_convert(
        #     self.__swr_ptr,
        #     # Output.
        #     self.__frame_ptr.contents.extended_data,
        #     out_samples,
        #     # Input.
        #     _av.cast(
        #         _av.create_string_buffer(data),
        #         _av.POINTER(_av.c_uint8)
        #     ) if data else None,
        #     self.__frame_ptr.contents.nb_samples if data else 0
        # )

    def _resample_from_frame(self, frame: Any) -> bytes:
        """Resample the data in frame and return it."""
        # Don't resample null data.
        if not frame.contents.linesize[0]:
            return b''

        output = _av.POINTER(_av.c_uint8)()
        dest_linesize = _av.c_int()

        # Calculate how many resampled samples there will be.
        out_samples = _av.av_rescale_rnd(
            # Set the delay to output samples.
            _av.swr_get_delay(
                self.__swr_ptr,
                self.__codec_context_ptr.contents.sample_rate
            ) + frame.contents.nb_samples,
            self._rate,
            self.__codec_context_ptr.contents.sample_rate,
            _av.AV_ROUND_UP
        )

        # Allocate a buffer large enough to hold the resampled data.
        _av.av_samples_alloc(
            _av.byref(output),          # Array for pointers to each channel.
            _av.byref(dest_linesize),   # Aligned size of audio buffers.
            # None,
            self._channels,             # Use output channels here.
            out_samples,                # Number of samples per channel.
            self._sample_fmt,           # Output sample format.
            0                           # Buffer size alignment.
        )

        # Resample the data in the frame to match the settings in avr.
        out_linesize = _av.swr_convert(
            self.__swr_ptr,
            # Output.
            _av.byref(output),             # Destination of the resampled data.
            out_samples,                   # Number of samples per channel.
            # Input.
            frame.contents.extended_data,  # Input data.
            frame.contents.nb_samples      # Number of samples per channel.
        )

        data = b''
        while out_linesize > 0:
            data_size = _av.av_samples_get_buffer_size(
                _av.byref(dest_linesize),
                self._channels,
                out_linesize,
                self._sample_fmt,
                1
            )
            data += _av.string_at(output, data_size)

            # Get the bytes in the output buffer.
            # data += _av.string_at(
            #     output,
            #     out_linesize
            #     * self._channels
            #     * _av.av_get_bytes_per_sample(self._sample_fmt)
            # )

            # Flush the resample buffer.
            out_linesize = _av.swr_convert(
                self.__swr_ptr,
                # Output.
                _av.byref(output),    # Destination of the resampled data.
                out_samples,          # Number of samples per channel.
                # Input.
                None,                 # Input data.
                0                     # Number of samples per channel.
            )

        # Free the output buffer.
        _av.av_freep(_av.byref(output))

        return data

    def close(self):
        """Close and cleans up."""
        if not self.closed:
            if self._mode == 'w':
                while self.write(b''):
                    pass
                self._encode(b'')

                _av.av_write_trailer(self.__format_context_ptr)

            # Close and free the resample context.
            _av.swr_close(self.__swr_ptr)
            _av.swr_free(self.__swr_ptr)

            # Close the file and free all other contexts.
            if self._mode == 'w':
                _av.av_frame_free(_av.byref(self.__frame_ptr))
                _av.av_frame_free(self.__input_frame_ptr)
                _av.avio_closep(_av.byref(
                    self.__format_context_ptr.contents.pb
                ))
            else:
                _av.avformat_close_input(self.__format_context_ptr)

            _av.avcodec_free_context(self.__codec_context_ptr)

            _av.avformat_free_context(self.__format_context_ptr)

            # Delete the data structures.
            del(self.__format_context_ptr)
            del(self.__codec_context_ptr)

            # Deinit the network if the file read was a network stream.
            if self.__network_stream:
                _av.avformat_network_deinit()

            # This file is closed.
            self._closed = True
