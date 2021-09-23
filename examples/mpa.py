#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Example of portaudio callback player.
# Copyright (C) 2012-2021 Josiah Gordon <josiahg@gmail.com>
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


"""Example of portaudio callback player."""


def main(args: dict):
    """Play args['filenames'] args['loops'] times."""
    import atexit
    import time
    from select import select
    from sys import stdin
    from termios import (ECHO, ICANON, TCSANOW, VMIN, VTIME, tcgetattr,
                         tcsetattr)

    from musio.player_util import AudioPlayer, PortAudioPlayer, get_files

    if args['debug']:
        from musio import io_util
        io_util.DEBUG = True

    # Save the current terminal state.
    normal = tcgetattr(stdin)
    quiet = tcgetattr(stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(stdin, TCSANOW, quiet)

    # Re-set the terminal state.
    atexit.register(tcsetattr, stdin, TCSANOW, normal)

    # Pop the filenames list out of the args dict.
    filenames = args.pop('filenames')

    # Recursively get all the files.
    recurse = args.pop('recurse')
    if recurse:
        filenames = get_files(filenames)

    quit_command = False

    # Start player with no filename, and set the loops.
    if 'portaudio' in args['blacklist'] or 'portaudio_io' in args['blacklist']:
        player_cls = AudioPlayer
    else:
        player_cls = PortAudioPlayer

    with player_cls(**args) as player:
        for filename in filenames:
            if quit_command:
                break

            # Open the file.
            try:
                player.open(filename, **args)
            except Exception as err:
                print(err)
                continue

            if args['show_position']:
                print(f"\nPlaying: {filename}")
                print(f"\n{player}")

            # Start playback.
            player.play()

            while player.playing or player.paused:
                # Check for input.
                r, _, _ = select([stdin], [], [], 0)

                # Get input if there was any otherwise continue.
                if r:
                    command = r[0].readline().lower()
                else:
                    try:
                        time.sleep(0.1)
                        continue
                    except KeyboardInterrupt:
                        break

                # Handle input commands.
                if command.startswith("p") or command.startswith(" "):
                    player.play() if player.paused else player.pause()
                elif (command.startswith("l") or command.endswith("\033[c")):
                    player.position += player.length / 100
                elif (command.startswith("h") or command.endswith("\033[d")):
                    player.position -= player.length / 100
                elif command == "\n" or command.startswith("q"):
                    quit_command = command.startswith("q")
                    break

            player.stop()

            if args['show_position']:
                print("\nDone.")


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
    parser.add_argument('-b', '--blacklist', action='append', default=[],
                        help='Blacklist a Codec',
                        dest='blacklist')
    parser.add_argument('-s', '--soundfont', action='store',
                        default='/usr/share/soundfonts/FluidR3_GM.sf2',
                        help='Soundfont to use when playing midis',
                        dest='soundfont')
    parser.add_argument('-ab', '--bank', action='store', type=str,
                        default='-1',
                        help='Bank used by adlmidi.',
                        dest='bank')
    parser.add_argument('-av', '--volume-model', action='store', type=int,
                        default=0,
                        help=('Set the volume range model. (0-11) '
                              '0 = Auto, '
                              '1 = Generic, '
                              '2 = NativeOPL3, '
                              '3 = DMX, '
                              '4 = APPOGEE, '
                              '5 = 9x, '
                              '6 = DMX Fixed, '
                              '7 = APPOGEE Fixed, '
                              '8 = AIL, '
                              '9 = 9X Generic FM, '
                              '10 = HMI, '
                              '11 = HMI Old.'),
                        dest='volume_model')
    parser.add_argument('-ac', '--chips', action='store', type=int,
                        default=-1,
                        help='Number of chips for adlmidi to emulate. (1-100)',
                        dest='num_chips')
    parser.add_argument('-af', '--four-ops', action='store', type=int,
                        default=-1,
                        help=('Number of four-op channels for adlmidi to '
                              'emulate. (1-100)'),
                        dest='four_ops')
    parser.add_argument('-ae', '--opl3-emu', action='store', type=int,
                        default=0,
                        help=("Select OPL3 emulator for adlmidi.  "
                              "Nuked = 0, Nuked 1.74 = 1, Dosbox = 2, "
                              "Opal = 3, Java = 4"),
                        dest='emulator')
    parser.add_argument('-q', '--quiet', action='store_false', default=True,
                        help='Don\'t show playback percentage.',
                        dest='show_position')
    parser.add_argument('-fp', '--floating-point', action='store_true',
                        default=False,
                        help="Use floating point playback when possible.",
                        dest="floatp")
    parser.add_argument('--debug', action='store_true', default=False,
                        help='Enable debug error messages.',
                        dest='debug')
    parser.add_argument('-d', '--device', action='store', default='default',
                        help='Specify the device.',
                        dest='device')
    parser.add_argument('-r', '--recursive', action='store_true',
                        default=False, help='Recurse through all directories.',
                        dest='recurse')
    parser.add_argument('--list-devices', action='store_true', default=False,
                        help='List available devices.',
                        dest='list_devices')
    parser.add_argument('--list-banks', action='store_true', default=False,
                        help='List available banks (adlmidi).',
                        dest='list_banks')
    parser.add_argument('-wc', '--wildmidi-config', action='store',
                        default='', help='Specify the wildmidi config.',
                        dest='wildmidi_config')
    parser.add_argument(dest='filenames', nargs='+')
    args = parser.parse_args()

    if args.list_devices:
        from sys import stderr

        from musio.io_util import silence
        from musio.portaudio import portaudio

        _portaudio = portaudio.Portaudio()

        # Silence stderr
        with silence(stderr):
            _portaudio.initialize()
            dev_count = _portaudio.device_count
            for i in range(dev_count):
                dev_name = _portaudio.device_name(i)
                print(i, dev_name)
    elif args.list_banks:
        from musio.adlmidi_file import AdlmidiFile
        AdlmidiFile.print_bank_list()
    else:
        if args.filenames:
            if args.blacklist:
                # Fix comma seperated input.
                for i, j in enumerate(args.blacklist):
                    if ',' in j:
                        args.blacklist.extend(args.blacklist.pop(i).split(','))
            main(args.__dict__)
