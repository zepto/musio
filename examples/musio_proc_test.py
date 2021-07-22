from multiprocessing import Process, Pipe
import select
import time

from musio import open_file, open_device

class Player(Process):
    """ Music player process.

    """

    def __init__(self, loops: int = -1):
        """ Start the player.

        """

        super(Player, self).__init__()

        in_pipe, out_pipe = Pipe()
        self._com_pipe = in_pipe
        self._proc_pipe = out_pipe
        self._playing = False
        self._open = False

    def run(self):
        """ Start the player.

        """

        self._main_loop(self._proc_pipe)

    def _main_loop(self, pipe):
        """ The main loop.

        """

        mus_file = mus_dev = None

        playing = False
        while True:
            if mus_file and playing:
                buf = mus_file.readline()
                if not buf:
                    mus_file.close()
                    mus_dev.close()
                    mus_file = mus_dev = None
                    playing = False
                    continue
                mus_dev.write(buf)
            else:
                time.sleep(0.05)

            if pipe.poll():
                signal, data = pipe.recv()
            else:
                continue

            if signal == 'open':
                if mus_file: mus_file.close()
                if mus_dev: mus_dev.close()
                mus_file = open_file(data, soundfont='/usr/share/soundfonts/FluidR3_GM2-2.sf2')
                mus_dev = open_device(mus_file)
                pipe.send(('open', True))
            if signal == 'play':
                if mus_file:
                    if mus_dev.closed: mus_dev = open_device(mus_file)
                    playing = True
                pipe.send(('playing', playing))
            if signal == 'pause' and playing:
                playing = False
                if not mus_dev.closed:
                    mus_dev.close()
                pipe.send(('playing', playing))
            if signal == 'stop':
                playing = False
                if mus_file:
                    mus_file.seek(0)
                if not mus_dev.closed:
                    mus_dev.close()
                pipe.send(('playing', playing))
            if signal == 'quit':
                break

            if signal == 'is-playing':
                pipe.send(('playing', playing))
            if signal == 'is-open':
                pipe.send(('open', not mus_file.closed if mus_file else False))

            if signal == 'set-position':
                if mus_file: mus_file.position = data
            if signal == 'set-loops':
                if mus_file: mus_file.loops = data

            if signal == 'get-position':
                pipe.send(('position', mus_file.position if mus_file else 0))
            if signal == 'get-length':
                pipe.send(('length', mus_file.length if mus_file else 0))
            if signal == 'get-loops':
                pipe.send(('loops', mus_file.loops if mus_file else -1))
            if signal == 'get-str':
                pipe.send(('str', str(mus_file)))

        if mus_file: mus_file.close()
        if mus_dev: mus_dev.close()

    def open_wrapper(func):
        """ Wrapper.

        """

        def wrapper(self, *args, **kwargs):
            """ Check for playing.

            """

            if self._open:
                return func(self, *args, **kwargs)
            else:
                return None

        return wrapper

    def playing_wrapper(func):
        """ Wrapper.

        """

        def wrapper(self, *args, **kwargs):
            """ Check for playing.

            """

            if self._playing:
                return func(self, *args, **kwargs)
            else:
                return None

        return wrapper

    @open_wrapper
    def __str__(self):
        """ Print a string representation of Player.

        """

        self._com_pipe.send(('get-str', True))
        return self._com_pipe.recv()[1]

    def open(self, filename: str):
        """ Open a file.

        """

        self._com_pipe.send(('open', filename))
        self._open = self._com_pipe.recv()[1]

    @open_wrapper
    def is_playing(self):
        """ Return playing.

        """

        self._com_pipe.send(('is-playing', True))
        return self._com_pipe.recv()[1]

    @open_wrapper
    def play(self):
        """ Start playback.

        """

        self._com_pipe.send(('play', True))
        self._playing = self._com_pipe.recv()[1]

    @playing_wrapper
    @open_wrapper
    def stop(self):
        """ Stop playback.

        """

        self._com_pipe.send(('stop', True))
        self._playing = self._com_pipe.recv()[1]

    @playing_wrapper
    @open_wrapper
    def pause(self):
        """ Pause playback.

        """

        self._com_pipe.send(('pause', True))
        self._playing = self._com_pipe.recv()[1]

    @property
    @open_wrapper
    def position(self):
        """ Return the position.

        """

        self._com_pipe.send(('get-position', True))
        return self._com_pipe.recv()[1]

    @position.setter
    @open_wrapper
    def position(self, position):
        """ Set the position.

        """

        self._com_pipe.send(('set-position', position))

    @property
    @open_wrapper
    def length(self):
        """ Return the length.

        """

        self._com_pipe.send(('get-length', True))
        return self._com_pipe.recv()[1]

    @property
    @open_wrapper
    def loops(self):
        """ get loops

        """

        self._com_pipe.send(('get-loops', True))
        return self._com_pipe.recv()[1]

    @loops.setter
    @open_wrapper
    def loops(self, loops: int):
        """ get loops

        """

        self._com_pipe.send(('set-loops', loops))

    @open_wrapper
    def close(self):
        """ Close the main loop.

        """

        self._com_pipe.send(('quit', True))
        self._open = False

if __name__ == '__main__':
    import sys
    from termios import tcgetattr, tcsetattr, ECHO, ICANON, TCSANOW
    from termios import VMIN, VTIME
    from sys import stdin as sys_stdin
    from select import select
    if sys.argv[1:]:
        # Save the current terminal state.
        normal = tcgetattr(sys_stdin)
        quiet = tcgetattr(sys_stdin)

        # Do not wait for key press and don't echo.
        quiet[3] &= ~(ECHO | ICANON)
        quiet[6][VMIN] = 0
        quiet[6][VTIME] = 0

        # Set the new terminal state.
        tcsetattr(sys_stdin, TCSANOW, quiet)

        p = Player()
        p.start()
        quit = False
        for filename in sys.argv[1:]:
            print('Playing {filename}'.format(**locals()))
            p.open(filename)
            p.loops = 0
            print(p)
            p.play()
            # Process user input until song finishes.
            while p.is_playing():
                if p.length > 0:
                    # Calculate the percentage played.
                    pos = (p.position * 100) / p.length

                    # Make the string.
                    pos_str = 'Position: %.2f%%' % pos

                    # Find the length of the string.
                    format_len = len(pos_str) + 2

                    print('\033[%dD\033[K%s' % (format_len, pos_str),
                            end='', flush=True)
                # Check for input.
                r, _, _ = select([sys_stdin], [], [], 0)

                # Get input if there was any otherwise continue.
                if r:
                    command = r[0].readline().lower()
                else:
                    continue

                # Handle input commands.
                if command.startswith('q'):
                    quit = True
                    break
                if command.startswith('l') or command.endswith('\033[c'):
                    p.position += (p.length // 100) * 2
                if command.startswith('h') or command.endswith('\033[d'):
                    p.position -= (p.length // 100) * 2
                elif command == '\n':
                    break
                elif command.startswith('p') or command.startswith(' '):
                    p.pause() if p.is_playing() else p.play()

            print('\nDone.')
            if quit: break
        # Re-set the terminal state.
        tcsetattr(sys_stdin, TCSANOW, normal)
        p.close()
