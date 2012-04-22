#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# ogg types
# Copyright (C) 2010 Josiah Gordon <josiahg@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


""" ogg types

"""

from ctypes import *

class FILE(Structure):
    _fields_ = [
            ]

# these are filled in by configure
ogg_int16_t = c_int16
ogg_uint16_t = c_uint16
ogg_int32_t = c_int32
ogg_uint32_t = c_uint32
ogg_int64_t = c_int64
