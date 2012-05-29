from musio.io_base import AudioIO, io_wrapper
from musio.mp4v2 import _mp4v2
from musio.mp4_file import Mp4

class Mp4File(AudioIO):
    """ A file like object for reading aac audio from mp4s.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, depth=16, rate=44100, channels=2, **kwargs):
        """ Mpg4File(filename, depth=16, rate=44100, channels=2) -> Initialize
        the playback settings of the player.

        """

        super(Mp4File, self).__init__(filename, 'r', depth, rate, channels)

        self._tags_dict = {}

        self._mp4_handle = self._open(filename)

        self._update_info()

        self._length = self._mp4_handle.sample_count

        self._data = b''

    def _set_position(self, position):
        """ Change the position of playback.

        """

        self._mp4_handle.current_sample = position

    def _get_position(self):
        """ Updates the position variable.

        """

        # Update the position.
        return self._mp4_handle.current_sample

    def _open(self, filename):
        """ _open(filename) -> Load the specified file.

        """

        mp4_handle = Mp4(filename.encode())

        # Get the aac decoder.

        self._closed = False

        return mp4_handle

    def _update_info(self):
        """ Updates the id3 info for the opened mp3.

        """

        tags_dict = self._mp4_handle.get_tag_dict()

        info_dict = self._info_dict

        for i in ['name', 'artist', 'albumArtist', 'album', 'composer',
                'comments', 'genre', 'releaseDate', 'track', 'disk',
                'description', 'longDescription', 'lyrics', 'copyright',
                'encodedBy']:
            value = getattr(tags_dict, i, None)
            if value:
                info_dict[i] = value
            elif hasattr(value, 'value'):
                info_dict[i] = value.value

        self._tags_dict = self._info_dict = info_dict

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.  If
        size is None then read a buffer size.

        """

        data = self._data

        while len(data) < size:
            # Read the next sample.
            sample = self._mp4_handle.read()

            if sample.size.value == 0:
                if self._loops != -1 and self._loop_count >= self._loops:
                    if len(data) != 0:
                        # Fill data buffer until it is the requested
                        # size.
                        data += b'\x00' * (size - len(data))
                    break
                else:
                    self._loop_count += 1
                    self.seek(1)
                    continue

            # Append decoded data to the data buffer.
            data += _mp4v2.string_at(sample.data, sample.size.value)

        # Store extra data for next read.
        self._data = data[size:]

        # Only return the requested amount of data.
        return data[:size]

    def close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            self._mp4_handle.close()

            self._closed = True

if __name__ == '__main__':
    from sys import argv as sys_argv
    if sys_argv[1:]:
        filename = sys_argv[1]
        with Mp4File(filename) as mp4, open('test.aac', 'wb') as aac:
            mp4.loops = 0
            # buf, size = mp4._mp4_handle.get_configuration()
            # aac.write(_mp4v2.string_at(buf, size.value))
            for i in mp4:
                aac.write(i)
