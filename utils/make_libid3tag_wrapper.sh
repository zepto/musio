#!/bin/bash
h2xml.py -c /usr/include/id3tag.h -o id3tag.xml -D __STDC_CONSTANT_MACROS
xml2py id3tag.xml -o id3tag.py -l /usr/lib/libid3tag.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' id3tag.py
