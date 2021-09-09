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


"""Player functions."""

import audioop
from functools import wraps as functools_wraps
from io import SEEK_CUR, SEEK_END, SEEK_SET
from multiprocessing import Manager, Pipe, Process
from multiprocessing.connection import Connection
from time import sleep as time_sleep
from typing import Callable

from .io_util import msg_out, open_device, open_file


def _play_proc(msg_dict: dict):
    """Player process."""
    # from oss_io import Oss as AudioIO
    # from alsa_io import Alsa as AudioIO
    from portaudio_io import Portaudio as AudioIO

    from all_file import AllFile as Music

    with Music(**msg_dict) as music, AudioIO(rate=music.rate,
                                             channels=music.channels,
                                             depth=music.depth,
                                             bigendian=music.bigendian,
                                             unsigned=music.unsigned) as \
            audio_out:

        music.loops = msg_dict.get('loops', -1)
        for buf in music:
            written = audio_out.write(buf)
            if not msg_dict['playing'] or not buf and not written:
                break


def play(filename: str, **kwargs) -> tuple[dict, Process]:
    """Play file <filename>.

    Starts playing filename and returns an object to send to stop to stop it
    playing.
    """
    playing = Manager().dict()
    playing['playing'] = True
    playing['filename'] = filename
    playing.update(kwargs)
    play_t = Process(target=_play_proc, args=(playing,))

    play_t.start()

    return playing, play_t


def stop(player_tup: tuple):
    """Stop the player."""
    playing, play_t = player_tup
    playing['playing'] = False
    play_t.join()


class AudioPlayer(object):
    """AudioPlayer.

    An audio player object.
    """

    def __init__(self, filename: str = '', show_position: bool = False,
                 **kwargs):
        """__init__.

        Parameters
        ----------
        self :
            self
        filename : str
            filename
        show_position : bool
            show_position
        kwargs :
            kwargs
        """
        self._filename = filename
        self._show_position = show_position

        # Setup the msg_dict for sending messages to the child process.
        self._msg_dict = Manager().dict()

        self._control_dict = {}

        # Create a pipe for sending and receiving messages.
        self._control_conn, self._player_conn = Pipe()

        # Open the file.
        if filename:
            self.open(filename, **kwargs)

    def __str__(self) -> str:
        """Get the information about the open file."""
        # Return nothing if no file is open.
        if not self._filename:
            return ''

        # Wait for the stream to open.
        while 'info' not in self._msg_dict:
            pass

        # Return the info string.
        return self._msg_dict.get('info', '')

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        return f"{self.__class__.__name__}(filename={self._filename})"

    def __enter__(self) -> 'AudioPlayer':
        """Provide the ability to use pythons with statement."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Stop playback when finished."""
        try:
            self.stop()
            self._control_conn.close()
            self._player_conn.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False

    def __del__(self):
        """Stop playback before deleting."""
        if self._control_dict.get('playing', False):
            try:
                self.stop()
            except IOError:
                pass

    def __len__(self) -> int:
        """Get the length of the file if it has one."""
        return self.length if self.length >= 0 else 0

    def playing_wrapper(func: Callable) -> Callable:
        """Wrap methods and only call them if the stream is playing."""
        @functools_wraps(func)
        def wrapper(self, *args, **kwargs) -> Callable:
            """Check if stream is playing.

            Check if stream is playing and if it is then call func otherwise
            print a message and exit.
            """
            if not self.playing:
                print(f"{self._msg_dict['filename']} is not playing.")
                return lambda **a: print(a)

            return func(self, *args, **kwargs)

        return wrapper

    def _play_proc(self, msg_dict: dict, pipe: Connection):
        """Player process."""
        # Open the file to play.
        try:
            with open_file(**msg_dict) as fileobj:
                # Put the file info in msg_dict.
                msg_dict['info'] = str(fileobj)
                msg_dict['length'] = fileobj.length

                state = None

                # Open an audio output device that can handle the data
                # from fileobj.
                device = open_device(fileobj, 'w', **msg_dict)

                msg_out(f"\nFile: {repr(fileobj)}\n")
                msg_out(f"\nDevice: {repr(device)}\n")

                try:

                    # Set the default number of loops to infinite.
                    fileobj.loops = msg_dict.get('loops', -1)

                    # Initialize variable.
                    buf = b'\x00' * device.buffer_size

                    # Loop until stopped.
                    while msg_dict.get('playing', True):
                        # Stop if the read buffer is empty or player is
                        # not paused.
                        if not (buf or msg_dict.get('paused', False)):
                            break

                        # Print the stream position.
                        if msg_dict.get('show_position', False):
                            # Only print the position if the stream has a
                            # length.
                            if fileobj.length > 0:
                                fileobj.print_midi_markers()

                                # Calculate the percentage played.
                                pos = (fileobj.position * 100) / fileobj.length

                                # Make the string.
                                pos_str = f"Position: {pos:.2f}%"

                                # Find the length of the string.
                                format_len = len(pos_str) + 2

                                # Print the string and after erasing the old
                                # one using ansi escapes.
                                print(f"\033[{format_len}D\033[K{pos_str}",
                                      end='', flush=True)

                        # Keep playing if not paused.
                        if not msg_dict.get('paused', False):
                            # Re-open the device after comming out of
                            # paused state.
                            if device.closed:
                                device = open_device(
                                    fileobj,
                                    'w',
                                    cached=True,
                                    **msg_dict
                                )

                            # Read the next buffer full of data.
                            try:
                                buf = fileobj.readline()
                            except KeyboardInterrupt:
                                break

                            # Sometimes a read needs to be made before the
                            # length is available.
                            if not msg_dict['length']:
                                msg_dict['length'] = fileobj.length

                            if device._rate != fileobj._rate \
                                    and fileobj._rate != 0:
                                # Convert the input sample rate to that of
                                # the output device.
                                buf, state = audioop.ratecv(
                                    buf,
                                    fileobj._width,
                                    fileobj._channels,
                                    fileobj._rate,
                                    int(device._rate),
                                    state
                                )

                            # Filler for end of partial buffer to elminiate
                            # end of audio noise.
                            if type(buf) == bytes:
                                filler = b'\x00' * \
                                    (device.buffer_size - len(buf))
                            else:
                                filler = ''

                            # Write buf.
                            try:
                                _ = device.write(buf + filler)
                            except KeyboardInterrupt:
                                break
                        else:
                            # Close the device when paused and sleep to
                            # open the audio for another process and
                            # save cpu cycles.
                            if not device.closed:
                                device.close()

                            time_sleep(0.05)

                            # Write a buffer of null bytes so the audio
                            # system can keep its buffer full.
                            # device.write(b'\x00' * device.buffer_size)

                        # Get and process any commands from the parent process.
                        if pipe.poll():
                            # Get the data into temp.
                            command = pipe.recv()

                            if 'getposition' in command:
                                pipe.send(fileobj.position)
                            elif 'setposition' in command:
                                fileobj.position = command['setposition']
                            elif 'getloops' in command:
                                pipe.send(fileobj.loops)
                            elif 'setloops' in command:
                                fileobj.loops = command['setloops']
                            elif 'getloopcount' in command:
                                pipe.send(fileobj.loop_count)
                            elif 'getlength' in command:
                                pipe.send(fileobj.length)
                except Exception as err:
                    print(err)
                finally:
                    if not device.closed:
                        device.close()

        except IOError as err:
            msg_dict['error'] = err
            msg_dict['info'] = ''
            msg_dict['length'] = 0
            print(err)
        finally:
            try:
                # Set playing to False for the parent.
                msg_dict['playing'] = False
            except BrokenPipeError:
                pass

    def open(self, filename: str, **kwargs):
        """Open an audio file to play."""
        # Stop the current file from playing.
        self.stop()

        # Set the new filename.
        self._filename = filename

        # Reset the message dictionary so none of the old info is
        # re-used.
        self._msg_dict.clear()

        # Fill the message dictionary with the new info.
        self._msg_dict['show_position'] = self._show_position
        self._msg_dict['filename'] = filename
        self._msg_dict.update(kwargs)

        self._control_dict.update(self._msg_dict)

        # Pause it so when we call play later it will start the player
        # but not the audio playback.  Call play again to start audio
        # playback.
        self.pause()

        # Start the playback process in a paused state.  Requires a
        # second call to play to un-pause.
        self.play()

    def play(self):
        """Start playback."""
        if not self._msg_dict.get('playing', False):
            # Set playing to True for the child process.
            self._msg_dict['playing'] = True

            # Open a new process to play a file in the background.
            self._play_p = Process(
                target=self._play_proc,
                args=(self._msg_dict, self._player_conn)
            )

            # Start the process.
            self._play_p.start()
        elif self._msg_dict.get('paused', True):
            # Un-pause if paused.
            self._msg_dict['paused'] = False

        self._control_dict.update(self._msg_dict)

    def stop(self):
        """Stop playback."""
        if self._msg_dict.get('playing', False):
            # Stop playback.
            self._msg_dict['playing'] = False

            # Wait for the player process to stop.
            self._play_p.join()

            # Un-Pause.
            self._msg_dict['paused'] = False

        self._control_dict.update(self._msg_dict)

    def pause(self):
        """Pause playback."""
        # Pause playback.
        self._msg_dict['paused'] = True
        self._control_dict.update(self._msg_dict)

    @property
    def error(self) -> bool:
        """Return True if playing."""
        return self._msg_dict.get('error', False)

    @property
    def paused(self) -> bool:
        """Return True if playback is paused."""
        return self._msg_dict.get('paused', False)

    @property
    def playing(self) -> bool:
        """Return True if playing."""
        return self._msg_dict.get('playing', False)

    @property
    def length(self) -> int:
        """Get the length of audio."""
        # self._control_conn.send('getlength')
        # return self._control_conn.recv()
        return self._msg_dict.get('length', 0)

    @property
    @playing_wrapper
    def position(self) -> int:
        """Get the current position."""
        self._control_conn.send('getposition')
        return self._control_conn.recv()

    @position.setter
    @playing_wrapper
    def position(self, value: int):
        """Set the current position."""
        self._control_conn.send({'setposition': value})

    @property
    @playing_wrapper
    def loops(self) -> int:
        """Get the number of times to loop (playback time + 1)."""
        self._control_conn.send('getloops')
        return self._control_conn.recv()

    @loops.setter
    @playing_wrapper
    def loops(self, value: int):
        """Set the number of times to loop (playback time + 1)."""
        self._control_conn.send({'setloops': int(value)})

    @property
    @playing_wrapper
    def loop_count(self) -> int:
        """Get the number of times the player has looped."""
        self._control_conn.send('getloopcount')
        return self._control_conn.recv()

    @playing_wrapper
    def seek(self, offset: int, whence: int = SEEK_SET) -> int:
        """Seek to position in mod."""
        if whence == SEEK_CUR:
            self.position += offset
        elif whence == SEEK_END:
            self.position = self.length - offset
        else:
            self.position = offset

        return self.position

    @playing_wrapper
    def tell(self) -> int:
        """Return the current position."""
        return self.position
