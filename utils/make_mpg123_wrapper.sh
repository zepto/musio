#!/bin/bash
h2xml.py -c /usr/include/mpg123.h -o mpg123.xml -D __STDC_CONSTANT_MACROS
xml2py mpg123.xml -o mpg123.py -l /usr/lib/libmpg123.so
sed -i 's/\([[:digit:]]\)L\>/\1/g' mpg123.py
