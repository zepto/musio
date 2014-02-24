#!/bin/bash
h2xml.py -c /usr/include/mikmod.h -o mikmod.xml -D __STDC_CONSTANT_MACROS
xml2py mikmod.xml -o mikmod.py -l /usr/lib/libmikmod.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' mikmod.py
