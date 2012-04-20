#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Test the player object.
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


""" Test the player object.

"""

if __name__ == '__main__':
    from sys import argv as sys_argv

    if sys_argv[1:]:

        args = {}
        args['filename'] = sys_argv[1]

        if sys_argv[2:]:
            if sys_argv[2].isdigit():
                args['track'] = int(sys_argv[2])
            else:
                args['soundfont'] = sys_argv[2]

        from player_util import AudioPlayer

        print("Playing: %(filename)s" % args)

        player = AudioPlayer(show_position=True, **args)

        print(player)

        player.play()

        while True:
            command = input().lower()
            if command.startswith('p'):
                player.play() if player.paused else player.pause()
            elif not command:
                break

        print("\nDone.")

        player.stop()
