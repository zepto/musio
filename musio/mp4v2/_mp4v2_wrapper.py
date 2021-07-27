#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# mp4v2 object oriented wrapper module.
# Copyright (C) 2010 Josiah Gordon <josiahg@gmail.com>
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


"""Wrap various mp4v2 functions into python classes."""

from functools import partial
from typing import Any, Generator

from . import _mp4v2


class Mp4Handle(object):
    """Wraps the mp4v2 mp4 file handle object."""

    def __init__(self, filename: str):
        """Initialize and create partial functions."""
        self._mp4_handle = _mp4v2.MP4FileHandle(_mp4v2.MP4Read(filename, 0))

        self.track_read_sample = partial(
            _mp4v2.MP4ReadSample,
            self._mp4_handle
        )
        self.track_es_configuration = partial(
            _mp4v2.MP4GetTrackESConfiguration,
            self._mp4_handle
        )
        self.track_type = partial(_mp4v2.MP4GetTrackType, self._mp4_handle)
        self.track_esds_object_type = partial(
            _mp4v2.MP4GetTrackEsdsObjectTypeId,
            self._mp4_handle
        )
        self.track_audio_mpeg4_type = partial(
            _mp4v2.MP4GetTrackAudioMpeg4Type,
            self._mp4_handle
        )
        self.track_sample_count = partial(
            _mp4v2.MP4GetTrackNumberOfSamples,
            self._mp4_handle
        )
        self.track_rate = partial(_mp4v2.MP4GetTrackBitRate, self._mp4_handle)
        self.track_name = partial(_mp4v2.MP4GetTrackName, self._mp4_handle)

        self._closed = False

        self._number_of_tracks = _mp4v2.MP4GetNumberOfTracks(
            self._mp4_handle,
            None,
            0
        )
        self._tags = _mp4v2.MP4TagsAlloc()
        _mp4v2.MP4TagsFetch(self._tags, self._mp4_handle)

    def close(self):
        """Close the mp4 handle."""
        if not self._closed:
            _mp4v2.MP4Close(
                self._mp4_handle,
                _mp4v2.MP4_CLOSE_DO_NOT_COMPUTE_BITRATE
            )
            _mp4v2.MP4TagsFree(self._tags)

            self._closed = True

    @property
    def tags(self) -> Any:
        """Get the mp4 tags."""
        return self._tags

    @property
    def track_count(self) -> int:
        """Get the number of tracks in this mp4."""
        return self._number_of_tracks

    def tracks(self) -> Generator[Any, None, None]:
        """Yield a track object for each track."""
        for track in range(1, self.track_count + 1):
            yield Mp4Track(self, track)

    def get_aac_track(self) -> Any:
        """Return the AAC track in the mp4 or None."""
        # Tracks start at 1.
        for track in self.tracks():
            track_type = track.type.decode()

            # Only use audio tracks.
            if not track_type or _mp4v2.MP4_IS_AUDIO_TRACK_TYPE(track_type):
                continue

            object_type = track.object_type

            # Only return audio if it is AAC encoded.
            if object_type == _mp4v2.MP4_MPEG4_AUDIO_TYPE:
                object_type = track.audio_mpeg4_type

                # Check for AAC encoding.
                if _mp4v2.MP4_IS_MPEG4_AAC_AUDIO_TYPE(object_type):
                    return track
            elif _mp4v2.MP4_IS_AAC_AUDIO_TYPE(object_type):
                return track

        # An invalid track.
        raise(Exception('Invalid AAC track.'))


class Mp4Track(object):
    """Wraps the mp4v2 track object."""

    def __init__(self, mp4_handle: Any, track: int = 1):
        """Initialize the track and create partial functions."""
        self._mp4_handle = mp4_handle
        self._mp4_track = track
        self._mp4_track_id = _mp4v2.MP4TrackId(track)

        self._read_sample = partial(mp4_handle.track_read_sample,
                                    self._mp4_track_id)
        self._es_configuration = partial(mp4_handle.track_es_configuration,
                                         self._mp4_track_id)

        self._type = mp4_handle.track_type(self._mp4_track_id)
        self._esds_object_type = mp4_handle.track_esds_object_type(
            self._mp4_track_id)
        self._audio_mpeg4_type = mp4_handle.track_audio_mpeg4_type(
            self._mp4_track_id)

        self._sample_count = mp4_handle.track_sample_count(self._mp4_track_id)
        self._rate = mp4_handle.track_rate(self._mp4_track_id)

        name = _mp4v2.c_char_p()
        _ = mp4_handle.track_name(self._mp4_track_id, name)

        self._name = name

    @property
    def track_id(self) -> int:
        """Get the mp4 track id."""
        return self._mp4_track_id.value

    def read_sample(self, sample_id: int) -> Any:
        """Return the sample and its size."""
        # Is this the last sample.
        last = (sample_id == self._sample_count)

        data_buffer = _mp4v2.POINTER(_mp4v2.c_uint8)()
        buffer_size = _mp4v2.c_uint32()

        # Don't read past the end of the file.
        if sample_id <= self._sample_count:
            self._read_sample(
                sample_id,
                _mp4v2.byref(data_buffer),
                _mp4v2.byref(buffer_size),
                None,
                None,
                None,
                None
            )

        # Return a sample object.
        return Mp4Sample(sample_id, data_buffer, buffer_size, last)

    def get_configuration(self) -> tuple[Any, Any]:
        """Get the configuration.

        Return a buffer and size to use with faad init functions to find the
        sample rate and channels.
        """
        data_buffer = _mp4v2.POINTER(_mp4v2.c_ubyte)()
        buffer_size = _mp4v2.c_uint32()

        ret = self._es_configuration(_mp4v2.byref(data_buffer), buffer_size)

        # Reset the buffer and size if there was no configuration data.
        if not ret:
            data_buffer = _mp4v2.POINTER(_mp4v2.c_ubyte)()
            buffer_size = _mp4v2.c_uint32()

        return (data_buffer, _mp4v2.c_ulong(buffer_size.value))

    @property
    def sample_count(self) -> int:
        """Get the number of samples in the track."""
        return self._sample_count

    @property
    def type(self) -> bytes:
        """Get the type of the current track."""
        return self._type

    @property
    def object_type(self) -> int:
        """Get the track object type."""
        return self._esds_object_type

    @property
    def audio_mpeg4_type(self) -> int:
        """Get the type of mpeg4 audio for the track."""
        return self._audio_mpeg4_type


class Mp4Sample(object):
    """An mp4 sample contains the data and size."""

    def __init__(self, sample_id: int, data: Any, size: Any,
                 last: bool = False):
        """Initialize the sample."""
        self._mp4_sample_id = _mp4v2.MP4SampleId(sample_id)

        self._data = data
        self._size = size
        self._id = sample_id
        self._last = last

    @property
    def sample_id(self) -> int:
        """Get the mp4 sample id."""
        return self._mp4_sample_id.value

    def islast(self) -> bool:
        """Return True if this is a the last sample."""
        return self._last

    @property
    def id(self) -> int:
        """Get the current sample id."""
        return self._id

    @property
    def data(self) -> bytes:
        """Get the sample data."""
        return self._data

    @property
    def size(self) -> int:
        """Get the size of the sample."""
        return self._size


class Mp4(object):
    """Provides easy access to the AAC audio in mp4s."""

    def __init__(self, filename: str):
        """Initialize class variables."""
        self._mp4_handle = Mp4Handle(filename)

        self._aac_track = self._mp4_handle.get_aac_track()
        if not self._aac_track:
            raise Exception(f"No AAC track in {filename}")

        self._sample_count = self._aac_track.sample_count
        self._current_sample = 1

    def close(self):
        """Close the mp4."""
        self._mp4_handle.close()
        del(self._mp4_handle)

    def get_tag_dict(self) -> dict:
        """Return a dictionary of tags from the mp4 or an empty dict."""
        tag_dict = {}

        tags = self._mp4_handle.tags
        for i in dir(tags.contents):
            item = getattr(tags.contents, i)
            if item:
                if hasattr(item, 'contents'):
                    tag_dict[i] = item.contents
                elif hasattr(item, 'value'):
                    tag_dict[i] = item.value
                else:
                    tag_dict[i] = item
            # try:
            #     if item.contents:
            #         tag_dict[i] = item.contents
            # except Exception as err:
            #     try:
            #         if item.value:
            #             tag_dict[i] = item.value
            #     except Exception as err:
            #         if item:
            #             tag_dict[i] = item

        return tag_dict

    def get_configuration(self):
        """Get config.

        Return a buffer and size to use with faad init functions to find the
        sample rate and channels.
        """
        return self._aac_track.get_configuration()

    def read(self) -> Mp4Sample:
        """Read the next sample from the aac audio in the open mp4."""
        sample = self._aac_track.read_sample(self._current_sample)

        self._current_sample += 1

        return sample

    @property
    def current_sample(self) -> int:
        """Get the next sample to read."""
        return self._current_sample

    @current_sample.setter
    def current_sample(self, value: int):
        """Set the next sample to read."""
        if value in range(1, self._sample_count):
            self._current_sample = value
        else:
            self._current_sample = 1

    @property
    def sample_count(self) -> int:
        """Get the number of samples in the aac track."""
        return self._sample_count
