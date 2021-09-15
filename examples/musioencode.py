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


"""Test the vorbis encoder."""


def main(args: dict) -> bool:
    """Encode args['filename'] times."""
    from os.path import basename, isfile, splitext
    from select import select
    from sys import stdin
    from termios import (ECHO, ICANON, TCSANOW, VMIN, VTIME, tcgetattr,
                         tcsetattr)

    from musio import open_file

    if args['debug']:
        from musio import io_util
        io_util.DEBUG = True

    filename = args['filename']
    output = splitext(basename(filename))[0] + '.' + args['filetype']
    output_bytes = output.encode('utf-8', 'surrogateescape')
    output_printable = output_bytes.decode('utf-8', 'ignore')
    if isfile(output):
        overwrite = input(f"Overwrite {output_printable} (y/n): ").lower()
        if overwrite.startswith("n"):
            return False

    # Save the current terminal state.
    normal = tcgetattr(stdin)
    quiet = tcgetattr(stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(stdin, TCSANOW, quiet)

    # Value returned to tell the calling function whether to quit or
    # not.
    quit_val = True

    if args['filetype'].lower() == 'ogg':
        quality = args['quality'] / 10 if args['quality'] in range(-1, 11) else 0.5
    elif args['filetype'].lower() == 'mp3':
        quality = args['quality'] if args['quality'] in range(0, 10) else 2
    else:
        quality = 5

    try:
        with open_file(**args) as in_file:
            in_file_title = in_file._info_dict.get('title',
                                                   in_file._info_dict['name'])
            comment_dict = {'title': in_file_title}
            comment_dict.update(in_file._info_dict)
            for i in ['title', 'artist', 'album', 'year', 'comment',
                      'track', 'genre']:
                if args.get(i, ''):
                    comment_dict[i] = args[i]

            with open_file(output, 'w', depth=in_file.depth,
                           rate=in_file.rate, channels=in_file.channels,
                           quality=quality, floatp=in_file._floatp,
                           unsigned=in_file._unsigned,
                           comment_dict=comment_dict,
                           bit_rate=args['bit_rate'],
                           blacklist=args['blacklist']
                           ) as out_file:
                in_file.loops = 0
                if args['debug']:
                    print(repr(in_file))
                    print(repr(out_file))

                if args['show_position']:
                    filename_bytes = filename.encode('utf-8',
                                                     'surrogateescape')
                    filename_printable = filename_bytes.decode('utf-8',
                                                               'ignore')
                    print(f"Encoding: {filename_printable} to "
                          f"{output_printable}")
                    print(in_file)

                for data in in_file:
                    if args['show_position']:
                        if in_file.length > 0:
                            # Calculate the percentage played.
                            pos = (in_file.position * 100) / in_file.length

                            # Make the string.
                            pos_str = f"Position: {pos:.2f}%"

                            # Find the length of the string.
                            format_len = len(pos_str) + 2

                            # Print the string and after erasing the old
                            # one using ansi escapes.
                            print(f"\033[{format_len}D\033[K{pos_str}", end='',
                                  flush=True)
                    out_file.write(data)

                    # Check for input.
                    r, _, _ = select([stdin], [], [], 0)

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
        tcsetattr(stdin, TCSANOW, normal)

    if args['show_position']:
        print("\nDone.")

    return quit_val


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Musio encoder")
    parser.add_argument('-e', '--quality', action='store', default=-10,
                        type=int, help='Encoding quality (1-10)',
                        dest='quality')
    parser.add_argument('-t', '--track', action='store', default=0, type=int,
                        help='Track to play', dest='track')
    parser.add_argument('-tt', '--title', action='store', default='',
                        help='id3 Title tag', dest='title')
    parser.add_argument('-ta', '--artist', action='store', default='',
                        help='id3 Artist tag', dest='artist')
    parser.add_argument('-tl', '--album', action='store', default='',
                        help='id3 Album tag', dest='album')
    parser.add_argument('-ty', '--year', action='store', default='',
                        help='id3 Year tag', dest='year')
    parser.add_argument('-tc', '--comment', action='store', default='',
                        help='id3 Comment tag', dest='comment')
    parser.add_argument('-tr', '--id3track', action='store', default='',
                        help='id3 Track tag', dest='track')
    parser.add_argument('-tg', '--genre', action='store', default=0,
                        help='id3 Genre tag', dest='genre')
    parser.add_argument('-p', '--path', action='store', default=[],
                        type=lambda a: a.split(','), help='Codec path',
                        dest='mod_path')
    parser.add_argument('-b', '--blacklist', action='extend',
                        default=['dummy'],
                        type=lambda a: a.split(','),
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
    parser.add_argument('-f', '--filetype', action='store',
                        default='ogg',
                        help='The output format',
                        dest='filetype')
    parser.add_argument('-q', '--quiet', action='store_false', default=True,
                        help='Don\'t show playback percentage.',
                        dest='show_position')
    parser.add_argument('-lg', '--list-genres', action='store_true',
                        default=False,
                        help='Print a list of valid genres and exit.',
                        dest='list_genres')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Enable debug error messages.',
                        dest='debug')
    parser.add_argument('-fp', '--floating-point', action='store_true',
                        default=False,
                        help=("Use floating point for the input file when "
                              "possible."),
                        dest="floatp")
    parser.add_argument('-br', '--bit-rate', action='store',
                        default=128000, type=int,
                        help=("Set the output bit rate."),
                        dest="bit_rate")
    parser.add_argument('-i', '--input', dest='input_filename', nargs='+')
    args = parser.parse_args()

    if args.list_genres:
        # Print out valid genres.
        from musio.mp3_file import get_genre_list
        print("ID\tGenre")
        for genre_id, genre in enumerate(get_genre_list()):
            if genre:
                print("%s\t%s" % (genre_id, genre))
    elif args.input_filename:
        # Copy the args dict to use later
        args_dict = args.__dict__

        # Pop the filenames list out of the args dict.
        filenames = args_dict.pop('input_filename')

        # Loop over all the filenames playing each one.
        for filename in filenames:
            # Pass only one filename to the main function.
            args_dict['filename'] = filename
            if not main(args_dict):
                break
