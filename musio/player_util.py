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
import weakref
from functools import wraps as functools_wraps
from io import SEEK_CUR, SEEK_END, SEEK_SET
from multiprocessing import Manager, Pipe, Process
from multiprocessing.connection import Connection
from pathlib import Path
from time import sleep
from typing import Any, Callable

from .dummy_file import DummyFile
from .io_util import get_codec, msg_out, open_device, open_file
from .portaudio_io import Portaudio


def _play_proc(msg_dict: dict):
    """Player process."""
    # from oss_io import Oss as AudioIO
    # from alsa_io import Alsa as AudioIO
    from .all_file import AllFile as Music
    from .portaudio_io import Portaudio as AudioIO

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


def get_files(file_list):
    """Return a list of all the files in filename."""
    from os import walk
    from os.path import isdir, join
    from pathlib import Path

    out_list = []
    ext = ['.mp3', '.flac', '.ogg', '.s3m', '.mod', '.xm',
           '.it', '.opus', '.wav', '.mid', '.imf', '.nsf',
           '.wma', '.wlf', '.mtm', '.flv', '.wav']

    for name in file_list:
        if isdir(name):
            for root, _, files in walk(name):
                join_list = [join(root, f) for f in files
                             if Path(f.lower()).suffix in ext]
                out_list.extend(join_list)
        else:
            out_list.append(name)

    return out_list


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
        self.close()

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

                            sleep(0.05)

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

        # Skip non-files.
        if not Path(filename).is_file():
            raise(IOError(f"{filename} is not a file."))

        # Skip unsupported files.
        if get_codec(
            filename,
            blacklist=[*kwargs.get('blacklist', []), 'all']
        ) == DummyFile:
            raise(IOError(f"File {filename} not supported."))

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

    def close(self):
        """Close the audio file and device."""
        if self._control_dict.get('playing', False):
            try:
                self.stop()
            except IOError:
                pass


class PortAudioPlayer():
    """An audio player."""

    def __init__(self, **kwargs):
        """Audio player.

        Plays audio in the background using the portaudio callback.
        """
        self._kwargs = kwargs

        self._cmd_dict = {
            "position": [],
        }

        self._device = None
        self._audio_file = None

        if kwargs.get("filename", ""):
            self.open(self._kwargs.pop('filename'), **self._kwargs)

        # Make sure close is called before exiting.
        weakref.finalize(self, self.close)

    def __pa_callback_f(self, frame_count: int, _, userdata: tuple) -> bytes:
        """Read and return audio data."""
        audio_file, cmd_dict = userdata

        # Check and run each command in cmd_dict.
        for command, args in cmd_dict.items():
            if command == 'position' and args:
                audio_file.position = args[0]
                args.clear()

        # Only print the position if the stream has a length.
        if self._kwargs.get('show_position', False) and audio_file.length > 0:
            audio_file.print_midi_markers()

            # Calculate the percentage played.
            pos = (audio_file.position * 100) / audio_file.length

            # Make the string.
            pos_str = f"Position: {pos:.2f}%"

            # Find the length of the string.
            format_len = len(pos_str) + 2

            # Print the string after erasing the old one using ansi escapes.
            print(f"\033[{format_len}D\033[K{pos_str}", end='', flush=True)

        buffer_size = frame_count * ((audio_file.depth // 8)
                                     * audio_file.channels)
        return audio_file.read(buffer_size)

    def __str__(self) -> str:
        """Return string representation of audio file."""
        if self._audio_file:
            return str(self._audio_file)
        return "No open file."

    def __repr__(self) -> str:
        """Return a python expression to recreate this instance."""
        kwargs_lst = []
        for key, value in self._kwargs.items():
            if type(value) == str:
                value = f'"{value}"'
            kwargs_lst.append(f"{key}={value}")

        return f"{self.__class__.__name__}({', '.join(kwargs_lst)})"

    def __del__(self):
        """Stop playback before deleting."""
        self.close()

    def __bool__(self) -> bool:
        """Return True."""
        return True

    def __len__(self) -> int:
        """Get the length of the file if it has one."""
        return self.length

    def _open_device(self) -> Any:
        """Return an opened portaudio device."""
        callback_tuple = (self._audio_file, self._cmd_dict)
        return self._device if self._device else Portaudio(
            mode="w",
            device=self._kwargs.get("device", "default"),
            rate=self._audio_file.rate,
            channels=self._audio_file.channels,
            depth=self._audio_file.depth,
            unsigned=self._audio_file.unsigned,
            floatp=self._audio_file.floatp,
            callback=self.__pa_callback_f,
            callback_data=callback_tuple
        )

    def open(self, filename: str, **kwargs):
        """Open the named file and return True on success False otherwise."""
        # Close all open devices and files first.
        self.close()

        # Update arguments.
        self._kwargs |= kwargs

        # Make sure these are always blacklisted.
        self._kwargs |= {
            'blacklist': self._kwargs.get("blacklist", []) + [
                'all', 'dummy', 'text'
            ]
        }

        # Skip non-files.
        if not Path(filename).is_file():
            raise(IOError(f"{filename} is not a file."))

        self._audio_file = open_file(filename, **self._kwargs)
        if not self._audio_file:
            raise(IOError(f"Could not open {filename}."))

    @property
    def loop_count(self) -> int:
        """Return the number of times the song has looped."""
        return self._audio_file.loop_count

    @property
    def loops(self) -> int:
        """Get the number of times the playback should loop.

        -1 = infinite looping.
        """
        return self._kwargs.get('loops', self._audio_file.loops)

    @loops.setter
    def loops(self, loops):
        """Set the number of times playback should loop.

        -1 = infinite looping.
        """
        self._audio_file.loops = self._kwargs['loops'] = loops

    @property
    def position(self) -> int:
        """Get the current position."""
        if not self._audio_file:
            position_list = self._cmd_dict.get('position', [])
            return position_list[0] if position_list else 0

        return self._audio_file.position

    @position.setter
    def position(self, position):
        """Set the current position."""
        self._cmd_dict.get('position', []).insert(0, position)

    @property
    def show_position(self) -> bool:
        """Return whether the position will be shown."""
        return self._kwargs.get("show_position", False)

    @show_position.setter
    def show_position(self, show: bool):
        """Set whether the position will be shown."""
        self._kwargs["show_position"] = show

    @property
    def playing(self) -> bool:
        """Return true if playing otherwise false."""
        if not self._device:
            return False
        return (self._device.is_stream_active
                and not self._device.is_stream_stopped)

    @property
    def paused(self) -> bool:
        """Return true if paused else false."""
        if not self._device:
            return False
        return (not self._device.is_stream_active
                and self._device.is_stream_stopped)

    @property
    def done(self) -> bool:
        """Return true if playback has finished."""
        if not self._device:
            return True
        return (not self._device.is_stream_active
                and not self._device.is_stream_stopped)

    def restart(self):
        """Restart playback."""
        if self.done:
            self._device.close()
            self._device = None
            self.seek(0)
            self.play()
        else:
            self.stop()
            self.play()

    def play(self):
        """Open the device and start the playback."""
        if not self._audio_file:
            print("No file opened.")
        elif not self._device:
            self._device = self._open_device()

            # Print out some debug information.
            msg_out(f"\n{repr(self._audio_file)}\n"
                    f"\n{repr(self._device)}\n")
        elif not self.playing and not self.done:
            self._device.start_stream()

    def stop(self):
        """Stop the playback and rewind the file to the start."""
        if not self._device or not self._audio_file:
            msg_out("No file or no device open.")
        elif (self._device.is_stream_active
                and not self._device.is_stream_stopped):
            self._device.abort_stream()
            self._audio_file.seek(0)

    def pause(self):
        """Pause audio playback."""
        if not self._device or not self._audio_file:
            msg_out("No file or no device open.")

        if (self._device.is_stream_active
                and not self._device.is_stream_stopped):
            self._device.stop_stream()

    def seek(self, offset: int, whence: int = SEEK_SET) -> int:
        """Seek to position in mod."""
        if whence == SEEK_CUR:
            self.position += offset
        elif whence == SEEK_END:
            self.position = self.length - offset
        else:
            self.position = offset

        return self.position

    def tell(self) -> int:
        """Return the position in the file."""
        return self.position

    @property
    def length(self) -> int:
        """Get the audio_file length."""
        return self._audio_file.length if self._audio_file else 0

    def close(self):
        """Close the audio file and device."""
        if self._device:
            self._device.abort_stream()
            self._device.close()
        if self._audio_file:
            self._audio_file.close()

        self._device = None
        self._audio_file = None

    def __enter__(self) -> Any:
        """Provide the ability to use pythons with statement."""
        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Close the pcm when finished."""
        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False
