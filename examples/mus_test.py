def play_proc(msg_dict):
    """ Player process

    """

    print("Playing: %s" % msg_dict['filename'])
    with AudioIO(**msg_dict) as file:
        DevIO = get_io(file)
        with DevIO(rate=file.rate, channels=file.channels,
                   depth=file.depth, bigendian=file.bigendian,
                   unsigned=file.unsigned) as device:
            file.loops = 2
            print(repr(device))
            print(repr(file))
            print(file)
            for buf in file:
                # print(len(buf))
                written = device.write(buf)
                # print(written, 'bytes written')
                if not msg_dict['playing'] or not buf and not written:
                    stdout.flush()
                    break
                while msg_dict.get('paused', False):
                    time_sleep(0.1)
                if file.length > 0:
                    perc_done = (file.position * 100) / file.length
                    perc_str = 'Position: %.2f%%' % perc_done
                    format_len = len(perc_str) + 2
                    print('\033[%dD\033[K%s' % (format_len, perc_str), end='')
                    stdout.flush()
            device.flush()
    print("\nDone.")

def rec_proc(msg_dict):
    """ Record process

    """

    filename = msg_dict['filename']
    comment_dict = msg_dict.get('comment_dict', {})
    kwargs = {'filename': filename, 'mode': 'w', 'depth':16, 'channels':2} #, 'comment_dict': comment_dict}

    # from oss_io import Oss as DevIO
    from alsa_io import Alsa as DevIO
    # from portaudio_io import Portaudio as DevIO

    print("Recording to: %s" % filename)
    with AudioIO(**kwargs) as file, DevIO(mode='rw', rate=file.rate,
                                           channels=file.channels,
                                           depth=file.depth,
                                           unsigned=file.unsigned) as device:

        writer = QueuedWriter(file.write)
        print(writer)
        print(repr(file))
        print(repr(device))
        print(file)
        bytes_read = 0

        for buf in device:
            bytes_read += writer.write(buf)
            # bytes_read += file.write(buf)
            status_str = 'Read: %d' % bytes_read
            format_len = len(status_str) + 2
            print('\033[%dD\033[K%s' % (format_len, status_str), end='')
            stdout.flush()
            if not msg_dict['recording']:
                print("\n%s written.\n" % writer.close())
                break
    print("Done.")


if __name__ == '__main__':
    from sys import argv as sys_argv
    if sys_argv[1:]:
        from sys import stdout, exit
        from time import sleep as time_sleep
        import multiprocessing

        from musio.io_util import get_codec, get_io
        from musio.queued_io import QueuedWriter

        filename = sys_argv[1]
        # AudioIO = get_codec(filename)
        from musio.mp4_file import Mp4File as AudioIO
        # from musio.all_file import AllFile as AudioIO

        if not AudioIO:
            print("Filetype not supported.")
            exit()

        # recording = multiprocessing.Manager().dict()
        # recording['recording'] = True
        # recording['filename'] = sys_argv[1]
        # recording['comment_dict'] = {
        #         'name': 'temp',
        #         'message': "This is a test ogg"
        #         }
        # record_t = multiprocessing.Process(target=rec_proc, args=(recording,))
        # record_t.start()
        # input()
        # recording['recording'] = False
        # record_t.join()
        # exit()

        playing = multiprocessing.Manager().dict()
        playing['playing'] = True
        playing['filename'] = sys_argv[1]
        if sys_argv[2:]:
            if sys_argv[2].isdigit():
                playing['track'] = int(sys_argv[2])
            else:
                playing['soundfont'] = sys_argv[2]
        play_t = multiprocessing.Process(target=play_proc, args=(playing,))

        play_t.start()
        input()
        playing['playing'] = False
        play_t.join()
