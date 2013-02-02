#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Test the player object.
# Copyright (C) 2012-2013 Josiah Gordon <josiahg@gmail.com>
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


def main(args: dict) -> None:
    """ Play args['filename'] args['loops'] times.

    """

    from sys import stdin as sys_stdin
    from select import select
    from time import sleep as time_sleep
    from termios import tcgetattr, tcsetattr, ECHO, ICANON, TCSANOW
    from termios import VMIN, VTIME

    from musio.player_util import AudioPlayer

    if args['debug']:
        from musio import io_util
        io_util.DEBUG = True

    try:
        player = AudioPlayer(**args)
    except IOError as err:
        print("Unsupported audio format: %s" % args['filename'])
        return 1

    player.loops = args['loops']

    if args['show_position']:
        print("Playing: %(filename)s" % args)
        print(player)

    player.play()

    # Save the current terminal state.
    normal = tcgetattr(sys_stdin)
    quiet = tcgetattr(sys_stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(sys_stdin, TCSANOW, quiet)

    # Value returned to tell the calling function whether to quit or
    # not.
    quit_val = True

    try:
        while player.playing:
            # Check for input.
            r, _, _ = select([sys_stdin], [], [], 0)

            # Get input if there was any otherwise continue.
            if r:
                command = r[0].readline().lower()
            else:
                time_sleep(0.1)
                continue

            # Handle input commands.
            if command.startswith('p') or command.startswith(' '):
                player.play() if player.paused else player.pause()
            if command.startswith('l') or command.endswith('\033[c'):
                player.position += player.length / 100
            if command.startswith('h') or command.endswith('\033[d'):
                player.position -= player.length / 100
            elif command.startswith('q'):
                quit_val = False
                break
            elif command == '\n':
                break
    except Exception as err:
        print("Error: %s", flush=True)
    finally:
        # Re-set the terminal state.
        tcsetattr(sys_stdin, TCSANOW, normal)

    if args['show_position']:
        print("\nDone.")

    player.stop()

    return quit_val


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Musio music player")
    parser.add_argument('-l', '--loops', action='store', default=-1, type=int,
                        help='How many times to loop (-1 = infinite)',
                        dest='loops')
    parser.add_argument('-t', '--track', action='store', default=0, type=int,
                        help='Track to play', dest='track')
    parser.add_argument('-p', '--path', action='store', default=[],
                        type=lambda a: a.split(','), help='Codec path',
                        dest='mod_path')
    parser.add_argument('-b', '--blacklist', action='store', default=[],
                        type=lambda a: a.split(','), help='Blacklist a Codec',
                        dest='blacklist')
    parser.add_argument('-s', '--soundfont', action='store',
                        default='/usr/share/soundfonts/fluidr3/FluidR3GM.SF2',
                        help='Soundfont to use when playing midis',
                        dest='soundfont')
    parser.add_argument('-q', '--quiet', action='store_false', default=True,
                        help='Don\'t show playback percentage.',
                        dest='show_position')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Enable debug error messages.',
                        dest='debug')
    parser.add_argument(dest='filename', nargs='+')
    args = parser.parse_args()

    if args.filename:
        # Copy the args dict to use later
        args_dict = args.__dict__

        # Pop the filenames list out of the args dict.
        filenames = args_dict.pop('filename')

        # Loop over all the filenames playing each one.
        for filename in filenames:
            # Pass only one filename to the main function.
            args_dict['filename'] = filename
            if not main(args_dict):
                break
