from musio.io_util import open_file
from musio.sndfile_file import SndfileFile

if __name__ == '__main__':
    from sys import argv
    if argv[1:]:
        filename = argv[1]

        # with AdlmidiFile(filename, rate=48000) as in_file:
        with open_file(filename, blacklist=['sndfile','fluidsynth']) as in_file:
            in_file.loops = 0
            with SndfileFile(f"{filename}.flac", mode='w', rate=in_file.rate, channels=in_file.channels, depth=in_file.depth, comment_dict=in_file._info_dict) as out_file:
                for buffer in in_file:
                    out_written = out_file.write(buffer)
