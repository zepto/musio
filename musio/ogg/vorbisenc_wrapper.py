#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# vorbisenc object oriented wrapper module.
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


""" Wrap various vorbis encoder functions into python classes.

"""

from functools import partial
from random import randint, seed
from time import time

from . import vorbisenc as _vorbisenc


class OggStreamState(_vorbisenc.ogg_stream_state):
    """ An ogg stream state wrapper.

    """

    def __init__(self, serialno=None):
        """ Initialize the stream state with the serial number serial no.
        If serialno is not set than a random number is used.

        """

        super(OggStreamState, self).__init__()

        if not serialno:
            seed(time())
            serialno = randint(0, 32767)
        _vorbisenc.ogg_stream_init(self, serialno)

        self.packetin = partial(_vorbisenc.ogg_stream_packetin, self)
        self.pageout = partial(_vorbisenc.ogg_stream_pageout, self)
        self.flush = partial(_vorbisenc.ogg_stream_flush, self)

        self.clear = partial(_vorbisenc.ogg_stream_clear, self)


class OggPacket(_vorbisenc.ogg_packet):
    """ An ogg packet wrapper.

    """

    def __init__(self):
        """ Create an ogg packet.

        """

        super(OggPacket, self).__init__()


class OggPage(_vorbisenc.ogg_page):
    """ Ogg page wrapper.

    """

    def __init__(self):
        """ Create an ogg page.

        """

        super(OggPage, self).__init__()

    def __str__(self):
        """ The header and body.

        """

        return bytes(self.header_str + self.body_str)
    __bytes__ = __str__

    @property
    def header_str(self):
        """ The page header.

        """

        return _vorbisenc.string_at(self.header, self.header_len)

    @property
    def body_str(self):
        """ The page body.

        """

        return _vorbisenc.string_at(self.body, self.body_len)

    @property
    def eos(self):
        """ True if the end of stream was reached.

        """

        return _vorbisenc.ogg_page_eos(self)


class DspState(_vorbisenc.vorbis_dsp_state):
    """ DspState wrapper.

    """

    def __init__(self):
        """ Create a dsp state.

        """

        super(DspState, self).__init__()

        self.analysis_init = partial(_vorbisenc.vorbis_analysis_init, self)
        self.analysis_buffer = partial(_vorbisenc.vorbis_analysis_buffer, self)
        self.block_init = partial(_vorbisenc.vorbis_block_init, self)
        self.headerout = partial(_vorbisenc.vorbis_analysis_headerout, self)
        self.blockout = partial(_vorbisenc.vorbis_analysis_blockout, self)
        self.get_buffer = partial(_vorbisenc.vorbis_analysis_buffer, self)
        self.wrote = partial(_vorbisenc.vorbis_analysis_wrote, self)
        self.bitrate_flushpacket = partial(_vorbisenc.vorbis_bitrate_flushpacket, self)

        self.clear = partial(_vorbisenc.vorbis_dsp_clear, self)


class VorbisInfo(_vorbisenc.vorbis_info):
    """ Vorbis info wrapper.

    """

    def __init__(self):
        """ Initialize the vorbis info.

        """

        super(VorbisInfo, self).__init__()
        _vorbisenc.vorbis_info_init(_vorbisenc.byref(self))

        self.encode_init_vbr = partial(_vorbisenc.vorbis_encode_init_vbr,
                                       _vorbisenc.byref(self))
        self.encode_setup_vbr = partial(_vorbisenc.vorbis_encode_setup_vbr,
                                        _vorbisenc.byref(self))
        self.encode_setup_init = partial(_vorbisenc.vorbis_encode_setup_init,
                                         _vorbisenc.byref(self))
        self.clear = partial(_vorbisenc.vorbis_info_clear,
                             _vorbisenc.byref(self))


class VorbisComment(_vorbisenc.vorbis_comment):
    """ Vorbis comment wrapper.

    """

    def __init__(self):
        """ Create and initialize a vorbis comment.

        """

        _vorbisenc.vorbis_comment_init(self)

        self.clear = partial(_vorbisenc.vorbis_comment_clear, self)

    def __str__(self):
        """ A String representation of the comment dict.

        """

        return str(self.__dict__)

    def __repr__(self):
        """ Python expression to recreate this object.__init__

        """

        return '%s()' % self.__class__.__name__

    def __setitem__(self, key, value):
        """ Add a tag to the comment.

        """

        self.__dict__[key] = value

        key = key.encode('utf8', 'replace')
        value = value.encode('utf8', 'replace')

        return _vorbisenc.vorbis_comment_add_tag(self, key, value)

    def __getitem__(self, key):
        """ Return the value key.

        """

        return self.__dict__.get(key, None)

    def update(self, updates_dict):
        """ update(self, updates_dict) -> Update the internal dict with values
        from updates_dict.

        """

        for key, value in updates_dict.items():
            self[key] = str(value)


class VorbisBlock(_vorbisenc.vorbis_block):
    """ Vorbis block wrapper.

    """

    def __init__(self):
        """ Create a vorbis block.

        """

        super(VorbisBlock, self).__init__()

        self.analysis = partial(_vorbisenc.vorbis_analysis, self)
        self.bitrate_addblock = partial(_vorbisenc.vorbis_bitrate_addblock, self)
        self.clear = partial(_vorbisenc.vorbis_block_clear, self)
