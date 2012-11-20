#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Musio module.
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


""" Module for audio IO.

"""

from .io_util import open_file, open_device

__all__ = ['aac_file',
           'all_file',
           'alsa_io',
           'audiality_file',
           'conversion_util',
           'dumb_file',
           'dummy_file',
           'dummy_io',
           'espeak_file',
           'espeak_io',
           'ffmpeg_file',
           'fluidsynth_file',
           'gme_file',
           'import_util',
           'io_base',
           'io_util',
           'mikmod_file',
           'modplug_file',
           'mp4_file',
           'mpg123_file',
           'oss_io',
           'player_util',
           'portaudio_io',
           'queued_io',
           'raw_file',
           'text_file',
           'vorbis_file',
           'wave_file',
           'xmp_file']
