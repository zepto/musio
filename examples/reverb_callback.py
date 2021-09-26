#!/usr/bin/env python
# This is a test program to test coc.nvim.
# Copyright © 2021 Bif
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see < http: // www.gnu.org/licenses/>.

"""Test player."""


import audioop
from typing import Any

import musio.player_util as player_util


def reverb(player: Any, audio_data: bytes, user_data: list) -> bytes:
    """Hello world."""
    data_list = user_data[0]
    decay = 0.5
    delay = 0
    if delay and not .5 % delay:
        data_size = len(audio_data)
        step = int(data_size * delay)
        if data_list:
            audio_data = audioop.add(
                audio_data[:step],
                audioop.mul(data_list.pop(0), player.width, decay),
                player.width
            ) + audio_data[step:]
        temp_array = bytearray(audio_data)
        for i in range(step, data_size, step):
            temp_array[i:i + step] = audioop.add(
                temp_array[i:i + step],
                audioop.mul(temp_array[i - step:i], player.width, decay),
                player.width
            )
        audio_data = bytes(temp_array)
        data_list.append(audio_data[-step:])
    else:
        if len(data_list) > delay:
            audio_data = audioop.add(
                audio_data,
                audioop.mul(data_list.pop(0), player.width, decay),
                player.width
            )
        data_list.append(audio_data)
    return audio_data


if __name__ == "__main__":
    from sys import argv

    if argv[1:]:
        with player_util.PortAudioPlayer() as player:
            player.show_position = True
            player.loops = 0
            data_list = []
            for filename in argv[1:]:
                player.open(filename, callback=reverb, user_data=data_list)
                print(player)
                player.play()
                if input() == 'q':
                    break
                player.stop()
