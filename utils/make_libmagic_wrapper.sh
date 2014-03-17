#!/bin/bash
h2xml.py -c /usr/include/magic.h -o magic.xml -D __STDC_CONSTANT_MACROS
xml2py magic.xml -o magic.py -l /usr/lib/libmagic.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' magic.py
