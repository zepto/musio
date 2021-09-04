from musio.portaudio_io import Portaudio

import opnmidi

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        filename = sys.argv[1]

        mplay = opnmidi.opn2_init(44100)
        opnmidi.opn2_openBankFile(mplay, '/home/josiah/Music/Tunes/fm_banks/adljack/wopn_files/xg.wopn')
        opnmidi.opn2_openFile(mplay, filename.encode())
        p = Portaudio(mode='w', rate=44100, device='default')
        d = opnmidi.create_string_buffer(4096 * 2)
        # d = b'\x00' * (4096 * 2)
        dl = 4096
        while True:
            g = opnmidi.opn2_play(mplay, dl, opnmidi.cast(d, opnmidi.POINTER(opnmidi.c_short)))
            if g <= 0:
                break
            p.write(d)

        p.close()
        opnmidi.opn2_close(mplay)
