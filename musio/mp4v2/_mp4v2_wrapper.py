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


""" Wrap various mp4v2 functions into python classes.

"""

from functools import partial

from . import _mp4v2


class Mp4Handle(_mp4v2.MP4FileHandle):
    """ Wraps the mp4v2 mp4 file handle object.

    """

    def __init__(self, filename):
        """ Initializes and creates partial functions.

        """

        super(Mp4Handle, self).__init__(_mp4v2.MP4Read(filename, 0))

        self.track_read_sample = partial(_mp4v2.MP4ReadSample, self)
        self.track_es_configuration = partial(_mp4v2.MP4GetTrackESConfiguration,
                                              self)
        self.track_type = partial(_mp4v2.MP4GetTrackType, self)
        self.track_esds_object_type = partial(_mp4v2.MP4GetTrackEsdsObjectTypeId,
                                              self)
        self.track_audio_mpeg4_type = partial(_mp4v2.MP4GetTrackAudioMpeg4Type,
                                              self)
        self.track_sample_count = partial(_mp4v2.MP4GetTrackNumberOfSamples,
                                          self)
        self.track_rate = partial(_mp4v2.MP4GetTrackBitRate, self)
        self.track_name = partial(_mp4v2.MP4GetTrackName, self)

        self._closed = False

        self._number_of_tracks = _mp4v2.MP4GetNumberOfTracks(self, None, 0)
        self._tags = _mp4v2.MP4TagsAlloc()
        _mp4v2.MP4TagsFetch(self._tags, self)

    def close(self):
        """ Close the mp4 handle.

        """

        if not self._closed:
            _mp4v2.MP4Close(self, _mp4v2.MP4_CLOSE_DO_NOT_COMPUTE_BITRATE)
            _mp4v2.MP4TagsFree(self._tags)

            self._closed = True

    @property
    def tags(self):
        """ The mp4 tags.

        """

        return self._tags

    @property
    def track_count(self):
        """ The number of tracks in this mp4.

        """

        return self._number_of_tracks

    def tracks(self):
        """ Yield a track object for each track.

        """

        for track in range(1, self.track_count + 1):
            yield Mp4Track(self, track)

    def get_aac_track(self):
        """ Returns the AAC track in the mp4 if there is any otherwise it
        returns 0.

        """

        # Tracks start at 1.
        for track in self.tracks():
            track_type = track.type

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
        return None


class Mp4Track(_mp4v2.MP4TrackId):
    """ Wraps the mp4v2 track object.

    """

    def __init__(self, mp4_handle, track=1):
        """ Initializes the track and creates partial functions.

        """

        super(Mp4Track, self).__init__(track)

        self._mp4_handle = mp4_handle
        self._mp4_track = track

        self._read_sample = partial(mp4_handle.track_read_sample, self)
        self._es_configuration = partial(mp4_handle.track_es_configuration,
                                         self)

        self._type = mp4_handle.track_type(self)
        self._esds_object_type = mp4_handle.track_esds_object_type(self)
        self._audio_mpeg4_type = mp4_handle.track_audio_mpeg4_type(self)

        self._sample_count = mp4_handle.track_sample_count(self)
        self._rate = mp4_handle.track_rate(self)

        name = _mp4v2.c_char_p()
        ret = mp4_handle.track_name(self, name)

        self._name = name

    def read_sample(self, sample_id):
        """ Return the sample and its size.

        """

        # Is this the last sample.
        last = (sample_id == self._sample_count)

        data_buffer = _mp4v2.POINTER(_mp4v2.c_uint8)()
        buffer_size = _mp4v2.c_uint32()

        # Don't read past the end of the file.
        if sample_id <= self._sample_count:
            self._read_sample(sample_id, _mp4v2.byref(data_buffer),
                              _mp4v2.byref(buffer_size), None, None, None,
                              None)

        # Return a sample object.
        return Mp4Sample(sample_id, data_buffer, buffer_size, last)

    def get_configuration(self):
        """ Return a buffer and size to use with faad init functions to find
        the sample rate and channels.

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
    def sample_count(self):
        """ The number of samples in the track.

        """

        return self._sample_count

    @property
    def type(self):
        """ The type of the current track.

        """

        return self._type

    @property
    def object_type(self):
        """ The track object type.

        """

        return self._esds_object_type

    @property
    def audio_mpeg4_type(self):
        """ The type of mpeg4 audio for the track.

        """

        return self._audio_mpeg4_type


class Mp4Sample(_mp4v2.MP4SampleId):
    """ An mp4 sample contains the data and size.

    """

    def __init__(self, sample_id, data, size, last=False):
        """ Initialize the sample.

        """

        super(Mp4Sample, self).__init__(sample_id)

        self._data = data
        self._size = size
        self._id = sample_id
        self._last = last

    def islast(self):
        """ True if this is a the last sample.

        """

        return self._last

    @property
    def id(self):
        """ The current sample id.

        """

        return self._id

    @property
    def data(self):
        """ The sample data.

        """

        return self._data

    @property
    def size(self):
        """ The size of the sample.

        """

        return self._size


class Mp4(object):
    """ Provides easy access to the AAC audio in mp4s.

    """

    def __init__(self, filename):
        """ Initialize class variables.

        """

        self._mp4_handle = Mp4Handle(filename)

        self._aac_track = self._mp4_handle.get_aac_track()
        if not self._aac_track:
            raise Exception("No AAC track in %s" % filename)

        self._sample_count = self._aac_track.sample_count
        self._current_sample = 1

    def close(self):
        """ Close the mp4.

        """

        self._mp4_handle.close()
        self._mp4_handle = None

    def get_tag_dict(self):
        """ Returns a dictionary of tags from the mp4 or an empty dict.

        """

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
        """ Return a buffer and size to use with faad init functions to find
        the sample rate and channels.

        """

        return self._aac_track.get_configuration()

    def read(self):
        """ Read the next sample from the aac audio in the open mp4.

        """

        if not self._mp4_handle:
            return (b'', 0)

        sample = self._aac_track.read_sample(self._current_sample)

        self._current_sample += 1

        return sample

    @property
    def current_sample(self):
        """ The next sample to read.

        """

        return self._current_sample

    @current_sample.setter
    def current_sample(self, value):
        """ The next sample to read.

        """

        if value in range(1, self._sample_count):
            self._current_sample = value
        else:
            self._current_sample = 1

    @property
    def sample_count(self):
        """ Number of samples in the aac track.

        """

        return self._sample_count
