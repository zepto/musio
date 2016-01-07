import flac
import audioop
from itertools import compress, cycle
from array import array
from musio.portaudio_io import Portaudio
from musio.alsa_io import Alsa
# p = Portaudio(device=5, depth=24,channels=2,rate=44100)
# p = Portaudio(device=5, depth=24,channels=2,rate=44100, unsigned=False)
# print(p._format)
p = Alsa(unsigned=False,depth=24,channels=2,rate=44100, three_byte=True)
print(p)

def read_status(sdec, buf, buf_size, client_data):
    print(dir(client_data))
    # return flac.FLAC__STREAM_DECODER_READ_STATUS_CONTINUE
    return flac.FLAC__STREAM_DECODER_READ_STATUS_ABORT
    # return flac.FLAC__STREAM_DECODER_READ_STATUS_END_OF_STREAM

total_samples = 0
bps = 0
f = open('test.raw', 'wb')
def write_status(sdec, frame, buf, client_data):
    global total_samples, bps
    global f
    # print('write status')
    # print(dir(client_data))
    # print(dir(frame.contents.subframes))
    # print(frame.contents.header.bits_per_sample)
    # print(frame.contents.header.sample_rate)
    # print(frame.contents.header.channels)
    channels = frame.contents.header.channels
    depth = frame.contents.header.bits_per_sample
    rate = frame.contents.header.sample_rate
    size = frame.contents.header.blocksize
    total_size= total_samples * channels * (bps/8)

    data = array('i', bytearray(((size * channels) * 4)))
    for i in range(size):
        for j in range(channels):
            data[i * channels + j] = buf[j][i]
    data = bytearray(data.tostring())
    sample = size * channels
    data = compress(data, cycle([1,1,1,0]))
    data = bytes(data)
    f.write(data[:sample*3])
    p.write(data[:sample*3])
    # print(frame.contents.header.number.sample_number, total_samples)
    return flac.FLAC__STREAM_DECODER_WRITE_STATUS_CONTINUE
    # return flac.FLAC__STREAM_DECODER_WRITE_STATUS_ABORT

def metadata_status(sdec, metadata, client_data):
    global total_samples, bps, f, s
    print('metadata')
    # print(dir(client_data))
    # print(dir(metadata.contents))
    channels = metadata.contents.data.stream_info.channels
    rate = metadata.contents.data.stream_info.sample_rate
    total_samples = metadata.contents.data.stream_info.total_samples
    bps = metadata.contents.data.stream_info.bits_per_sample
    # print(total_samples, bps)
    total_size= total_samples * channels * (bps//8)
    for i in range(metadata.contents.data.vorbis_comment.num_comments):
        comment = metadata.contents.data.vorbis_comment.comments[i]
        # print(comment.length, dir(comment))


    s = b'RIFF' + bytes(flac.c_uint32(total_size + 36)) + b'WAVEfmt ' + bytes(flac.c_uint32(16)) + bytes(flac.c_uint16(1)) + bytes(flac.c_uint16(channels)) + bytes(flac.c_uint32(rate)) + bytes(flac.c_uint32(rate * channels * (bps//8))) + bytes(flac.c_uint16(channels * (bps//8))) + bytes(flac.c_uint16(bps)) + b'data' + bytes(flac.c_uint32(total_size))
    print(s)
    f.write(s)
    print(metadata.contents.data.stream_info.channels)

def error_status(sdec, errorstat, client_data):
    print('error status')
    print(dir(client_data))
    print(dir(errorstat))
    print(errorstat)

read_status_callback = flac.FLAC__StreamDecoderReadCallback(read_status)
write_status_callback = flac.FLAC__StreamDecoderWriteCallback(write_status)
metadata_callback = flac.FLAC__StreamDecoderMetadataCallback(metadata_status)
error_callback = flac.FLAC__StreamDecoderErrorCallback(error_status)
fdec = flac.FLAC__stream_decoder_new()
print(fdec)
stat = flac.FLAC__stream_decoder_init_file(fdec, b'test3.flac',
        write_status_callback, metadata_callback, error_callback, None)
print(stat)
# print(flac.FLAC__stream_decoder_process_single(fdec))
print(flac.FLAC__stream_decoder_process_until_end_of_stream(fdec))
print(flac.FLAC__stream_decoder_finish(fdec))
flac.FLAC__stream_decoder_delete(fdec)
