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


def main(args: dict) -> int:
    """ Play args['filename'] args['loops'] times.

    """

    from sys import stdin as sys_stdin
    from select import select
    from time import sleep as time_sleep
    from termios import tcgetattr, tcsetattr, ECHO, ICANON, TCSANOW
    from termios import VMIN, VTIME
    from os.path import splitext as os_splitext

    from musio.player_util import AudioPlayer
    from musio.io_util import open_file

    if args['debug']:
        from musio import io_util
        io_util.DEBUG = True

    # Pop the filenames list out of the args dict.
    filenames = args.pop('filename')

    # Recursively get all the files.
    recurse = args.pop('recurse')
    if recurse:
        filenames = get_files(filenames)

    # Start player with no filename, and set the loops.
    player = AudioPlayer(**args)

    # Save the current terminal state.
    normal = tcgetattr(sys_stdin)
    quiet = tcgetattr(sys_stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(sys_stdin, TCSANOW, quiet)

    # Value to break out of outer loop and quit all playback.
    quit_command = False

    try:
        # Loop over the filenames playing each one with the same
        # AudioPlayer object.
        for filename in filenames:
            # if filename[-3:] not in ['mp3']:
            #     continue
            # Skip unsupported files.
            try:
                temp = open_file(filename)
                temp.close()
            except:
                continue

            filename_bytes = filename.encode('utf-8', 'surrogateescape')
            filename_printable = filename_bytes.decode('utf-8', 'ignore')

            # Open next file.
            try:
                player.open(filename, **args)
                player.loops = args['loops']
            except IOError as err:
                print("Unsupported audio format: %s" % filename_printable)
                return 1

            if args['show_position']:
                print("\nPlaying: %s" % filename_printable)
                print(player)

            # Start the playback.
            player.play()

            # Process user input until song finishes.
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
                elif command == '\n':
                    break
                elif command.startswith('q'):
                    quit_command = True
                    break

            if args['show_position']:
                player.stop()
                print("\nDone.")

            if quit_command: break

    except Exception as err:
        print("Error: %s" % err, flush=True)
    finally:
        # Always stop the player.
        if player.playing:
            player.stop()

        # Re-set the terminal state.
        tcsetattr(sys_stdin, TCSANOW, normal)

    return 0


def get_files(file_list):
    """ Returns a list of all the files in filename.

    """

    from os.path import isdir as os_isdir
    from os.path import isdir as os_isfile
    from os.path import join as os_join
    from os import walk as os_walk

    out_list = []

    for name in file_list:
        if os_isdir(name):
            for root, sub, files in os_walk(name):
                join_list = [os_join(root, f) for f in files]
                out_list.extend(join_list)
        else:
            out_list.append(name)

    return out_list


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
    parser.add_argument('--debug', action='store_true', default=False,
                        help='Enable debug error messages.',
                        dest='debug')
    parser.add_argument('-d', '--device', action='store', default='default',
                        help='Specify the device.',
                        dest='device')
    parser.add_argument('-r', '--recursive', action='store_true', default=False,
                        help='Recurse through all directories.',
                        dest='recurse')
    parser.add_argument('--list-devices', action='store_true', default=False,
                        help='List available devices.',
                        dest='list_devices')
    parser.add_argument(dest='filename', nargs='+')
    args = parser.parse_args()

    if args.list_devices:
        try:
            from musio.portaudio import portaudio
            from musio.io_util import silence
            from sys import stderr as sys_stderr

            _portaudio = portaudio.Portaudio()

            # Silence stderr
            with silence(sys_stderr):
                _portaudio.initialize()
                dev_count = _portaudio.device_count
                for i in range(dev_count):
                    dev_name = _portaudio.device_name(i)
                    print(i, dev_name)
        except:
            from musio.alsa import control
            hints = control.POINTER(control.c_void_p)()
            err = control.snd_device_name_hint(-1, b'pcm', control.byref(hints))
            for i in hints:
                if not i:
                    break
                name = control.snd_device_name_get_hint(i, b'NAME').decode()
                desc = control.snd_device_name_get_hint(i, b'DESC').decode()
                print('%s: %s' % (name, desc))
    else:
        if args.filename:
            main(args.__dict__)
