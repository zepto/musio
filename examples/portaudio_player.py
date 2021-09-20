"""Play music."""
import atexit
import time
from pathlib import Path
from select import select
from sys import stdin
from termios import ECHO, ICANON, TCSANOW, VMIN, VTIME, tcgetattr, tcsetattr

from musio import open_file
from musio.portaudio_io import Portaudio

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:

        def callback(framecount, _, userdata):
            """Portaudio callback."""
            audio_file = userdata
            buffer_size = framecount * ((audio_file.depth // 8)
                                        * audio_file.channels)
            return audio_file.read(buffer_size)

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

        quit_command = False

        for filename in sys.argv[1:]:
            if quit_command:
                break
            if not Path(filename).is_file():
                continue
            with open_file(filename) as audio_file:
                audio_file.loops = 0
                print(audio_file)
                with Portaudio(
                    mode="w",
                    rate=audio_file.rate,
                    channels=audio_file.channels,
                    device="default",
                    floatp=audio_file.floatp,
                    unsigned=audio_file.unsigned,
                    depth=audio_file.depth,
                    callback=callback,
                    callback_data=audio_file,
                ) as device:

                    while True:
                        # Calculate the percentage played.
                        pos = (audio_file.position * 100) / audio_file.length

                        # Make the string.
                        pos_str = f"Position: {pos:.2f}%"

                        # Find the length of the string.
                        format_len = len(pos_str) + 2

                        # Print the string and after erasing the old
                        # one using ansi escapes.
                        print(f"\033[{format_len}D\033[K{pos_str}", end="",
                              flush=True)

                        if audio_file.position == audio_file.length:
                            if audio_file.loop_count == audio_file.loops:
                                break

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
                            (
                                device.stop_stream()
                                if device.is_stream_active
                                else device.start_stream()
                            )
                        if (command.startswith("l")
                                or command.endswith("\033[c")):
                            audio_file.position += audio_file.length / 100
                        if (command.startswith("h")
                                or command.endswith("\033[d")):
                            audio_file.position -= audio_file.length / 100
                        elif command == "\n":
                            break
                        elif command.startswith("q"):
                            quit_command = True
                            break

                    print("\nDone.")
