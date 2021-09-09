from musio.portaudio_io import Portaudio

import sndfile
import time

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        filename = sys.argv[1]

        def callback(framecount, _, userdata):
            """Portaudio callback."""
            snd, sf_info = userdata
            buf = (sndfile.c_float * (framecount * sf_info.channels))()
            num_read = sndfile.sf_read_float(
                snd,
                buf,
                framecount * sf_info.channels
            )
            if num_read < framecount:
                return b''
            return sndfile.string_at(buf, num_read *
                                     sndfile.sizeof(sndfile.c_float))

        sf_info = sndfile.SF_INFO()
        snd = sndfile.sf_open(filename, sndfile.SFM_READ, sf_info)

        b = sndfile.create_string_buffer(1 << 16)
        sndfile.sf_command(snd, sndfile.SFC_GET_LOG_INFO, b, 1 << 16)
        b_str = sndfile.string_at(b).decode()
        for l in b_str.split('\n'):
            if l.lower().strip().startswith('bit'):
                print(l.split()[-1])
        tag_list = [
            'title',
            'copyright',
            'software',
            'artist',
            'comment',
            'date',
            'album',
            'license',
            'tracknumber'
        ]
        for i, name in enumerate(tag_list):
            snd_str = sndfile.sf_get_string(snd, i + 1)
            if snd_str:
                print(f"{name.capitalize():<15}: "
                      f"{snd_str.decode().strip(chr(34))}")
        genre_str = sndfile.sf_get_string(snd, 16)
        if genre_str:
            print(f"{'Genre':<15}: {genre_str.decode().strip(chr(34))}")

        p = Portaudio(
            mode='w',
            rate=sf_info.samplerate,
            channels=sf_info.channels,
            device='default',
            floatp=False,
            depth=16,
            # callback=callback,
            # callback_data=(snd, sf_info)
        )
        print(p)
        print(p.buffer_size, sf_info.samplerate, sf_info.channels)
        print(sf_info.format)
        # buf = (sndfile.c_int * (p.buffer_size * sf_info.channels))()
        # buf = (sndfile.c_float * (p.buffer_size * sf_info.channels))()
        # buf = sndfile.create_string_buffer(p.buffer_size * sf_info.channels)
        buf = (sndfile.c_short * (p.buffer_size * sf_info.channels))()
        length = sf_info.frames
        count = 0
        while p.is_stream_active:
            position = (sndfile.sf_seek(snd, 0, sndfile.SF_SEEK_CUR))

            # Calculate the percentage played.
            pos = (position * 100) / length

            # Make the string.
            pos_str = f"Position: {pos:.2f}%"

            # Find the length of the string.
            format_len = len(pos_str) + 2

            # Print the string and after erasing the old
            # one using ansi escapes.
            print(f"\033[{format_len}D\033[K{pos_str}",
                  end='', flush=True)

            # num_read = sndfile.sf_read_float(
            # num_read = sndfile.sf_read_raw(
            num_read = sndfile.sf_read_short(
            # num_read = sndfile.sf_read_int(
                snd,
                buf,
                p.buffer_size * sf_info.channels
            )
            if num_read < p.buffer_size:
                break

            try:
                # time.sleep(0.1)
                p.write(sndfile.string_at(
                    buf,
                    num_read * sndfile.sizeof(sndfile.c_short)
                ))
            except KeyboardInterrupt:
                break

        print("\nDone.")
        p.close()
        sndfile.sf_close(snd)
