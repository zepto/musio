#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Musio pipe reads/writes from/to a unix pipe.
# Copyright (C) 2016 Josiah Gordon <josiahg@gmail.com>
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


"""Musio pipe utility.

Musio pipe either reads a file or files and writes raw audio data to
stdout, or it reads from stdin and writes to an audio device.
"""


import select
from sys import stdin as sys_stdin
from sys import stderr as sys_stderr
from sys import stdout as sys_stdout


def pipe_in() -> int:
    """ Read from stdin and write to an audio device.

    """

    from musio import alsa_io

    # Open the alsa output device.
    with alsa_io.Alsa() as out_dev:
        # Setup polling to look for a hung up event.
        poll_obj = select.poll()
        poll_obj.register(sys_stdin.buffer, select.POLLHUP)

        # Loop until the input pipe ends.
        while not poll_obj.poll(1):
            data = sys_stdin.buffer.read(out_dev.buffer_size)
            count = out_dev.write(data)

    return 0


def pipe_out(filename_list: list) -> int:
    """ Read from the specified file and write to stdout.

    """

    if filename_list:
        from musio import open_file

        # Loop throuth all the filenames supplied.
        for filename in filename_list:
            # Don't loop over one file.
            with open_file(filename, loops=0) as infile:
                # Loop until the end of the file.
                for data in infile:
                    sys_stdout.buffer.write(data)

    return 0


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Pipe music to stdout or read from \
                                         stdin and write to an audio device")
    parser.add_argument('-f', '--filename', dest='filename', nargs='+',
                        help='The filename(s) of the audio files to write to \
                              stdout')

    args = parser.parse_args()

    try:
        # If a filename was given then this is the output side of the pipe.
        # Otherwise it is the input side.
        pipe_out(args.filename) if args.filename else pipe_in()
    except KeyboardInterrupt:
        # Exit on keyboard interrupt.
        pass
