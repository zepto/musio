#!/bin/bash
h2xml.py -c /usr/include/FLAC/all.h -o flac.xml -D __STDC_CONSTANT_MACROS
xml2py flac.xml -o flac.py -l /usr/lib/libFLAC.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' flac.py
