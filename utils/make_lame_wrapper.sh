#!/bin/bash
h2xml.py -c /usr/include/lame/lame.h -o lame.xml -D __STDC_CONSTANT_MACROS
xml2py lame.xml -o lame.py -l /usr/lib/libmp3lame.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' lame.py
