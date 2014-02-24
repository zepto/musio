#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Test the vorbis encoder.
# Copyright (C) 2013 Josiah Gordon <josiahg@gmail.com>
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


""" Test the vorbis encoder.

"""


def main(args: dict) -> None:
    """ Encode args['filename'] times.

    """

    from os.path import basename as os_basename
    from os.path import isfile as os_isfile
    from sys import stdin as sys_stdin
    from select import select
    from time import sleep as time_sleep
    from termios import tcgetattr, tcsetattr, ECHO, ICANON, TCSANOW
    from termios import VMIN, VTIME

    from musio import open_file, open_device

    if args['debug']:
        from musio import io_util
        io_util.DEBUG = True

    filename = args['filename']
    output = os_basename(filename).rsplit('.')[0] + '.' + args['filetype']
    if os_isfile(output):
        if input("Overwrite %s (y/n): " % output).lower().startswith('n'):
            return

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

    quality = args['quality'] / 10 if args['quality'] in range(-1, 11) else 0.5

    try:
        with open_file(**args) as in_file:
            with open_file(output, 'w', depth=in_file.depth, rate=in_file.rate,
                        channels=in_file.channels, quality=quality) as out_file:
                in_file.loops = 0

                if args['show_position']:
                    print("Encoding: %s to %s" % (filename, output))
                    print(in_file)

                for data in in_file:
                    if args['show_position']:
                        if in_file.length > 0:
                            # Calculate the percentage played.
                            pos = (in_file.position * 100) / in_file.length

                            # Make the string.
                            pos_str = 'Position: %.2f%%' % pos

                            # Find the length of the string.
                            format_len = len(pos_str) + 2

                            # Print the string and after erasing the old
                            # one using ansi escapes.
                            print('\033[%dD\033[K%s' % (format_len, pos_str),
                                  end='', flush=True)
                    out_file.write(data)

                    # Check for input.
                    r, _, _ = select([sys_stdin], [], [], 0)

                    # Get input if there was any otherwise continue.
                    if r:
                        command = r[0].readline().lower()
                        # Handle input commands.
                        if command.startswith('q'):
                            quit_val = False
                            break
                        elif command == '\n':
                            break

    except Exception as err:
        print("Error: %s" % err, flush=True)
        raise(err)
    finally:
        # Re-set the terminal state.
        tcsetattr(sys_stdin, TCSANOW, normal)

    if args['show_position']:
        print("\nDone.")

    return quit_val


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Musio vorbis encoder")
    parser.add_argument('-e', '--quality', action='store', default=5, type=int,
                        help='Encoding quality (1-10)', dest='quality')
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
    parser.add_argument('-f', '--filetype', action='store',
                        default='ogg',
                        help='The output format',
                        dest='filetype')
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
