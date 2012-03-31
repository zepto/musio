def play_proc(msg_dict):
    """ Player process

    """

    filename = msg_dict['filename']
    soundfont = msg_dict.get('soundfont', '')
    if soundfont:
        args = (filename, soundfont)
    else:
        args = (filename,)

    # from oss_io import Oss as AudioIO
    # from alsa_io import Alsa as AudioIO
    from portaudio_io import Portaudio as AudioIO

    print("Playing: %s" % filename)
    with Music(depth=16, channels=2, *args) as music, AudioIO(rate=music.rate,
                                        channels=music.channels,
                                        depth=music.depth,
                                        # bigendian=music.bigendian,
                                        unsigned=music.unsigned) as audio_out:
        music.loops = 1
        print(repr(audio_out))
        print(repr(music))
        print(music)
        for buf in music:
            written = audio_out.write(buf)
            # print(written, 'bytes written')
            if music.length > 0:
                perc_done = (music.position * 100) / music.length
                perc_str = 'Position: %.2f%%' % perc_done
                format_len = len(perc_str) + 2
                print('\033[%dD\033[K%s' % (format_len, perc_str), end='')
                stdout.flush()
            if not msg_dict['playing'] or not buf and not written:
                stdout.flush()
                break
    print("\nDone.")

def rec_proc(msg_dict):
    """ Record process

    """

    filename = msg_dict['filename']
    comment_dict = msg_dict.get('comment_dict', {})
    kwargs = {'filename': filename, 'mode': 'w', 'depth':16, 'channels':2} #, 'comment_dict': comment_dict}

    # from oss_io import Oss as AudioIO
    # from alsa_io import Alsa as AudioIO
    from portaudio_io import Portaudio as AudioIO

    print("Recording to: %s" % filename)
    with Music(**kwargs) as music, AudioIO(mode='rw', rate=music.rate,
                                           channels=music.channels,
                                           depth=music.depth,
                                           unsigned=music.unsigned) as audio_in:

        writer = QueuedWriter(music.write)
        print(writer)
        print(repr(music))
        print(repr(audio_in))
        print(music)
        bytes_read = 0

        for buf in audio_in:
            writer(buf)
            bytes_read += len(buf)
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
        import multiprocessing

        from io_base import get_codec
        from queued_io import QueuedWriter

        filename = sys_argv[1]
        Music = get_codec(filename)

        if not Music:
            print("Filetype not supported.")
            exit()

        recording = multiprocessing.Manager().dict()
        recording['recording'] = True
        recording['filename'] = sys_argv[1]
        recording['comment_dict'] = {
                'name': 'temp',
                'message': "This is a test ogg"
                }
        record_t = multiprocessing.Process(target=rec_proc, args=(recording,))
        record_t.start()
        input()
        recording['recording'] = False
        record_t.join()
        exit()

        playing = multiprocessing.Manager().dict()
        playing['playing'] = True
        playing['filename'] = sys_argv[1]
        if sys_argv[2:]:
            playing['soundfont'] = sys_argv[2]
        play_t = multiprocessing.Process(target=play_proc, args=(playing,))

        play_t.start()
        input()
        playing['playing'] = False
        play_t.join()

