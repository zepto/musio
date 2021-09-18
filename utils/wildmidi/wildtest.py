import wildmidi as wildmidi
from musio.portaudio_io import Portaudio
import ctypes

if __name__ == '__main__':
    import sys
    if sys.argv[:1]:
        with Portaudio() as dev:
            ret = wildmidi.WildMidi_Init(
                b'/home/josiah/gus/Scc1t2.cfg',
                44100,
                wildmidi.WM_MO_LOG_VOLUME
                | wildmidi.WM_MO_ENHANCED_RESAMPLING
                | wildmidi.WM_MO_REVERB
                | wildmidi.WM_MO_ROUNDTEMPO
                # | wildmidi.WM_MO_TEXTASLYRIC
            )
            print(f"{ret=}")
            for filename in sys.argv[1:]:
                filename_b = filename.encode()
                midi = wildmidi.WildMidi_Open(filename_b)
                # wildmidi.WildMidi_SetOption(
                #     midi,
                #     wildmidi.WM_MO_LOG_VOLUME
                #     & wildmidi.WM_MO_ENHANCED_RESAMPLING
                #     & wildmidi.WM_MO_REVERB
                #     & wildmidi.WM_MO_ROUNDTEMPO
                #     & wildmidi.WM_MO_TEXTASLYRIC,
                #     1
                # )
                print(midi)
                buffer_size = 4096
                buffer = ctypes.create_string_buffer(buffer_size)
                info = wildmidi.WildMidi_GetInfo(midi)
                copyright = info.contents.copyright
                if copyright:
                    print(ctypes.string_at(copyright))
                while True:
                    info = wildmidi.WildMidi_GetInfo(midi)
                    ret = wildmidi.WildMidi_GetOutput(
                        midi,
                        ctypes.cast(
                            buffer,
                            ctypes.POINTER(ctypes.c_int8)
                        ),
                        buffer_size
                    )
                    if ret == 0:
                        break
                    elif ret < 0:
                        print(ctypes.string_at(wildmidi.WildMidi_GetError()).decode())
                        break
                    # print(info.contents.current_sample / 44100)
                    lyric = wildmidi.WildMidi_GetLyric(midi)
                    if lyric:
                        print(ctypes.string_at(lyric).decode(), end='', flush=True)
                    dev.write(buffer.raw)
                wildmidi.WildMidi_Close(midi)
            wildmidi.WildMidi_Shutdown()


