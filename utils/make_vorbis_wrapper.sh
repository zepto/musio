#!/bin/bash
h2xml.py -c -I/usr/include/vorbis -I/usr/include/ogg /usr/include/vorbis/vorbisenc.h /usr/include/vorbis/codec.h /usr/include/vorbis/vorbisfile.h /usr/include/ogg/ogg.h -o vorbis.xml
xml2py vorbis.xml -o vorbis.py -l /usr/lib/libvorbis.so -l /usr/lib/libvorbisenc.so -l /usr/lib/libvorbisfile.so -l /usr/lib/libogg.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' vorbis.py
