#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to read id3 tags from files.
# Copyright (C) 2014 Josiah Gordon <josiahg@gmail.com>
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


""" A module for reading id3 tags.

"""

from .import_util import LazyImport

_id3tag = LazyImport('id3tag.id3tag', globals(), locals(),
                     ['id3tag'], 1)


class ID3Tags(dict):
    """ A dictionary of the id3 tags in a file.

    """

    def __init__(self, filename):
        """ ID3Tags(filename) -> A dictionary of the id3 tags in the file.

        """

        self.update(self._get_id3tags(filename))

    def _get_id3tags(self, filename):
        """ Use libid3tag to read the id3tags.

        """

        bytes_filename = filename.encode('utf-8', 'surrogateescape')
        id3_file = _id3tag.id3_file_open(bytes_filename, 0)
        id3_tag = _id3tag.id3_file_tag(id3_file)
        fields_dict = {
                'title': b'TIT2',
                'artist': b'TPE1',
                'album': b'TALB',
                'track': b'TRCK',
                'year': b'TDRC',
                'genre': b'TCON',
                'subtitle': b'TIT3',
                'copyright': b'TCOP',
                'produced': b'TPRO',
                'orchestra': b'TPE2',
                'conductor': b'TPE3',
                'lyricist': b'TEXT',
                'publisher': b'TPUB',
                'station': b'TRSN',
                'encoder': b'TENC',
                }

        id3_dict = {}

        for tag_name, tag_id in fields_dict.items():
            id3_frame = _id3tag.id3_tag_findframe(id3_tag, tag_id, 0)
            try:
                assert(id3_frame.contents)
            except ValueError:
                continue
            field = id3_frame.contents.fields[1]
            ucs4 = field.stringlist.strings.contents
            if tag_name == 'genre':
                ucs4 = _id3tag.id3_genre_name(ucs4)
            field_val = _id3tag.id3_ucs4_utf8duplicate(ucs4)
            tag_val = _id3tag.string_at(field_val).decode('utf8', 'replace')
            id3_dict[tag_name] = tag_val

        i = 0
        while True:
            frame = _id3tag.id3_tag_findframe(id3_tag, b'COMM', i)
            try:
                assert(frame.contents)
            except ValueError:
                break
            i += 1
            # ucs4 = _id3tag.id3_field_getstring(_id3tag.id3_frame_field(frame, 2))
            ucs4 = _id3tag.id3_field_getfullstring(_id3tag.id3_frame_field(frame, 3))
            field_val = _id3tag.id3_ucs4_utf8duplicate(ucs4)
            tag_val = _id3tag.string_at(field_val).decode('utf8', 'replace')
            id3_dict['comment'] = tag_val
            break

        _id3tag.id3_file_close(id3_file)

        return id3_dict
