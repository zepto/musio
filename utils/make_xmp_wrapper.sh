#!/bin/bash
h2xml.py -c /usr/include/xmp.h -o xmp.xml -D __STDC_CONSTANT_MACROS
xml2py xmp.xml -o xmp.py -l /usr/lib/libxmp.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' xmp.py
