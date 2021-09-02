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


"""Test the player object."""


def main(args: dict) -> int:
    """Play args['filename'] args['loops'] times."""
    from select import select
    from sys import stdin
    from termios import (ECHO, ICANON, TCSANOW, VMIN, VTIME, tcgetattr,
                         tcsetattr)
    from time import sleep

    from musio.dummy_file import DummyFile
    from musio.io_util import get_codec
    from musio.player_util import AudioPlayer

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
    normal = tcgetattr(stdin)
    quiet = tcgetattr(stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(stdin, TCSANOW, quiet)

    # Value to break out of outer loop and quit all playback.
    quit_command = False

    try:
        # Loop over the filenames playing each one with the same
        # AudioPlayer object.
        for filename in filenames:
            # Skip unsupported files.
            try:
                temp = get_codec(filename, blacklist=['all'])
                if temp == DummyFile:
                    raise(IOError(f"File {filename} not supported."))
            except Exception as err:
                print(err)
                continue

            filename_bytes = filename.encode('utf-8', 'surrogateescape')
            filename_printable = filename_bytes.decode('utf-8', 'ignore')

            # Open next file.
            try:
                player.open(filename, **args)
                player.loops = args['loops']
            except IOError:
                print(f"Unsupported audio format: {filename_printable}")
                return 1

            if args['show_position']:
                print(f"\nPlaying: {filename_printable}")
                print(player)

            # Start the playback.
            player.play()

            # Process user input until song finishes.
            while player.playing:
                # Check for input.
                r, _, _ = select([stdin], [], [], 0)

                # Get input if there was any otherwise continue.
                if r:
                    command = r[0].readline().lower()
                else:
                    try:
                        sleep(0.1)
                        continue
                    except KeyboardInterrupt:
                        break

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

            if quit_command:
                break

    except Exception as err:
        print(f"Error: {err}", flush=True)
    finally:
        try:
            # Always stop the player.
            if player.playing:
                player.stop()
        except BrokenPipeError:
            pass

        # Re-set the terminal state.
        tcsetattr(stdin, TCSANOW, normal)

    return 0


def get_files(file_list):
    """Return a list of all the files in filename."""
    from os import walk
    from os.path import isdir, join
    from pathlib import Path

    out_list = []
    ext = ['.mp3', '.flac', '.ogg', '.s3m', '.mod', '.xm', '.it']

    for name in file_list:
        if isdir(name):
            for root, _, files in walk(name):
                join_list = [join(root, f) for f in files
                             if Path(f.lower()).suffix in ext]
                out_list.extend(join_list)
        else:
            out_list.append(name)

    return out_list


if __name__ == '__main__':
    from argparse import ArgumentParser
    from typing import Union
    def bank(value: Union[str, int]) -> Union[str, int]:
        return value
        try:
            return int(value)
        except TypeError:
            return value
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
    parser.add_argument(dest='filename', nargs='+')
    args = parser.parse_args()

    if args.list_devices:
        try:
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
        except Exception:
            from musio.alsa import control
            hints = control.POINTER(control.c_void_p)()
            err = control.snd_device_name_hint(-1, b'pcm',
                                               control.byref(hints))
            for i in hints:
                if not i:
                    break
                name = control.snd_device_name_get_hint(i, b'NAME').decode()
                desc = control.snd_device_name_get_hint(i, b'DESC').decode()
                print('%s: %s' % (name, desc))
    elif args.list_banks:
        from musio.adlmidi_file import AdlmidiFile
        AdlmidiFile.print_bank_list()
    else:
        if args.filename:
            if args.blacklist:
                # Fix comma seperated input.
                for i, j in enumerate(args.blacklist):
                    if ',' in j:
                        args.blacklist.extend(args.blacklist.pop(i).split(','))
            main(args.__dict__)
