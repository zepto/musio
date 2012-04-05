#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Player functions
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


""" Player functions

"""

def _play_proc(msg_dict):
    """ Player process

    """

    # from oss_io import Oss as AudioIO
    # from alsa_io import Alsa as AudioIO
    from portaudio_io import Portaudio as AudioIO

    from all_file import AllFile as Music

    with Music(**msg_dict) as music, AudioIO(rate=music.rate,
                                        channels=music.channels,
                                        depth=music.depth,
                                        bigendian=music.bigendian,
                                        unsigned=music.unsigned) as audio_out:
        music.loops = msg_dict.get('loops', -1)
        for buf in music:
            written = audio_out.write(buf)
            if not msg_dict['playing'] or not buf and not written:
                break

def play(filename, **kwargs):
    """ play(filename, soundfont=None, loops=-1) -> Starts playing filename and
    returns an object to send to stop to stop it playing.

    """

    from multiprocessing import Process, Manager

    playing = Manager().dict()
    playing['playing'] = True
    playing['filename'] = filename
    playing.update(kwargs)
    play_t = Process(target=_play_proc, args=(playing,))

    play_t.start()

    return playing, play_t

def stop(player_tup):
    """ stop(player_tup) -> Stop the player.

    """

    playing, play_t = player_tup
    playing['playing'] = False
    play_t.join()

