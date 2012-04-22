#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Build musio package.
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


""" Build musio package.

"""

from distutils.core import setup

setup(
        name = 'musio',
        packages = ['musio', 'musio.alsa', 'musio.dumb', 'musio.espeak',
            'musio.faad', 'musio.ffmpeg', 'musio.fluidsynth', 'musio.gme',
            'musio.mikmod', 'musio.modplug', 'musio.mp4v2', 'musio.mpg123',
            'musio.ogg', 'musio.portaudio'],
        version = '0.5.0',
        description = 'Audio I/O library',
        author = 'Josiah Gordon',
        author_email = 'josiahg@gmail.com',
        url = '',
        download_url = '',
        keywords = ['audio', 'portaudio', 'alsa', 'ffmpeg'],
        classifiers = [
            'Programming Language :: Python :: 3',
            'Development  Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: Linux',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Audio Processing',
            ],
        long_description = ''' Audio I/O ''',
        )
