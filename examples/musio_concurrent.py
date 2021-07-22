import asyncio

async def test(filenames: list, queue):
    """ Try playing in a coroutine.

    """

    import musio

    for filename in filenames:
        with musio.open_file(filename, blacklist=['text'], loops=0) as music:
            print(music)
            dev = musio.open_device(music)
            paused = False
            while True:
                if not paused:
                    if dev.closed:
                        dev = musio.open_device(music)

                    buf = music.readline()
                    if not buf: break
                    buf += type(buf)(max(0, dev.buffer_size - len(buf)))
                    dev.write(buf)

                    if music.length > 0:
                        # Calculate the percentage played.
                        pos = (music.position * 100) / music.length

                        # Make the string.
                        pos_str = 'Position: %.2f%%' % pos

                        # Find the length of the string.
                        format_len = len(pos_str) + 2

                        print('\033[%dD\033[K%s' % (format_len, pos_str),
                                end='', flush=True)
                else:
                    if not dev.closed:
                        dev.close()

                await asyncio.sleep(0.001)

                if not queue.empty():
                    data = await queue.get()
                    if data == 'Quit':
                        await queue.put('Done.')
                        return
                    elif data.startswith('C'):
                        break
                    elif data.startswith('P'):
                        paused = not paused
                    elif data.startswith('F'):
                        music.position += ((music.length // 100) * 2)
                    elif data.startswith('B'):
                        music.position -= ((music.length // 100) * 2)

    await queue.put('Done.')


async def get_keys(queue):
    """ Stop on key interupt

    """

    from termios import tcgetattr, tcsetattr, ECHO, ICANON, TCSANOW
    from termios import VMIN, VTIME
    from sys import stdin as sys_stdin
    from select import select

    # Save the current terminal state.
    normal = tcgetattr(sys_stdin)
    quiet = tcgetattr(sys_stdin)

    # Do not wait for key press and don't echo.
    quiet[3] &= ~(ECHO | ICANON)
    quiet[6][VMIN] = 0
    quiet[6][VTIME] = 0

    # Set the new terminal state.
    tcsetattr(sys_stdin, TCSANOW, quiet)

    # Process user input until song finishes.
    while True:
        # Check for input.
        r, _, _ = select([sys_stdin], [], [], 0)

        # Get input if there was any otherwise continue.
        if r:
            command = r[0].readline().lower()
        else:
            if not queue.empty():
                data = await queue.get()
                if data == 'Done.':
                    break
                else:
                    await queue.put(data)
            try:
                await asyncio.sleep(0.001)
                continue
            except KeyboardInterrupt:
                break

        # Handle input commands.
        if command.startswith('q'):
            break
        if command.startswith('l') or command.endswith('\033[c'):
            await queue.put('Forward')
        if command.startswith('h') or command.endswith('\033[d'):
            await queue.put('Back')
        elif command == '\n':
            await queue.put('Continue')
        elif command.startswith('p') or command.startswith(' '):
            await queue.put('Play/Pause')

    # Re-set the terminal state.
    tcsetattr(sys_stdin, TCSANOW, normal)
    await queue.put('Quit')


def main(filenames: list) -> int:
    """ Main function

    """

    try:
        queue = asyncio.Queue()
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(get_keys(queue))
        loop.run_until_complete(test(filenames, queue))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        print("\nDone.", flush=True)
        return 0

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        main(sys.argv[1:])


