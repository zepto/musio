"""Test espeaktext module."""

from audioop import add

from musio.espeak_text import EspeakText
from musio.io_util import open_device

with EspeakText("") as e:
    e.loops = 0
    e.speed /= 1.5
    data = e.read()
    with open_device(e) as d:
        print(d)
        print(repr(e))
        while True:
            try:
                d.stop_stream()
                text = input()
                d.start_stream()
            except (KeyboardInterrupt, EOFError):
                break
            e.pitch = 50
            e.range = 50
            e.write(text)
            data = e.read()
            e.pitch = 100
            e.range = 20
            e.write(text)
            data2 = e.read()
            if len(data) > len(data2):
                data2 += bytearray(len(data) - len(data2))
            elif len(data2) > len(data):
                data += bytearray(len(data2) - len(data))
            data3 = add(data, data2, 1)
            d.write(data3)
