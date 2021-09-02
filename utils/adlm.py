from musio.portaudio_io import Portaudio

import adlmidi

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        filename = sys.argv[1]

        mplay = adlmidi.adl_init(44100)
        adlmidi.adl_openFile(mplay, filename.encode())
        p = Portaudio(mode='w', rate=44100, device='default')
        d = adlmidi.create_string_buffer(4096 * 2)
        # d = b'\x00' * (4096 * 2)
        dl = 4096
        while True:
            g = adlmidi.adl_play(mplay, dl, adlmidi.cast(d, adlmidi.POINTER(adlmidi.c_short)))
            if g <= 0:
                break
            p.write(d)

        p.close()
        adlmidi.adl_close(mplay)
