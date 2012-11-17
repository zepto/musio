#!/bin/bash
h2xml.py -c -I/usr/include/mp4v2 /usr/include/mp4v2/mp4v2.h -o mp4v2.xml -D __STDC_CONSTANT_MACROS
xml2py mp4v2.xml -o mp4v2.py -l /usr/lib/libmp4v2.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' mp4v2.py
