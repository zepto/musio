#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A mikmod MDRIVER
# Copyright (C) 2012 Josiah Gordon <josiahg@gmail.com>
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


""" Custom Mikmod MDRIVER.

"""

from ctypes import *

from ._mikmod import *


def mikmod_init():
    return VC_Init()


def mikmod_exit():
    VC_Exit()


def mikmod_update():
    pass


def mikmod_is_present():
    return True


drv_musio = MDRIVER()

drv_musio.next = None
drv_musio.Name = b'drv_musio'
drv_musio.Version = b'1.0.0'
drv_musio.HardVoiceLimit = 0
drv_musio.SoftVoiceLimit = 255
drv_musio.Alias = b'musio'
drv_musio.CmdLineHelp = None
# drv_musio.CommandLine = POINTER(None)
drv_musio.IsPresent = CFUNCTYPE(BOOL)(mikmod_is_present)
drv_musio.SampleLoad = CFUNCTYPE(SWORD, POINTER(SAMPLOAD), c_int)(VC_SampleLoad)
drv_musio.SampleUnload = CFUNCTYPE(None, SWORD)(VC_SampleUnload)
drv_musio.FreeSampleSpace = CFUNCTYPE(ULONG, c_int)(VC_SampleSpace)
drv_musio.RealSampleLength = CFUNCTYPE(ULONG, c_int, POINTER(SAMPLE))(VC_SampleLength)
drv_musio.Init = CFUNCTYPE(c_int)(mikmod_init)
drv_musio.Exit = CFUNCTYPE(None)(mikmod_exit)
# drv_musio.Reset = None
drv_musio.SetNumVoices = CFUNCTYPE(c_int)(VC_SetNumVoices)
drv_musio.PlayStart = CFUNCTYPE(c_int)(VC_PlayStart)
drv_musio.PlayStop = CFUNCTYPE(None)(VC_PlayStop)
drv_musio.Update = CFUNCTYPE(None)(mikmod_update)
# drv_musio.Pause = POINTER(None)
drv_musio.VoiceSetVolume = CFUNCTYPE(None, UBYTE, UWORD)(VC_VoiceSetVolume)
drv_musio.VoiceGetVolume = CFUNCTYPE(UWORD, UBYTE)(VC_VoiceGetVolume)
drv_musio.VoiceSetFrequency = CFUNCTYPE(None, UBYTE, ULONG)(VC_VoiceSetFrequency)
drv_musio.VoiceGetFrequency = CFUNCTYPE(ULONG, UBYTE)(VC_VoiceGetFrequency)
drv_musio.VoiceSetPanning = CFUNCTYPE(None, UBYTE, ULONG)(VC_VoiceSetPanning)
drv_musio.VoiceGetPanning = CFUNCTYPE(ULONG, UBYTE)(VC_VoiceGetPanning)
drv_musio.VoicePlay = CFUNCTYPE(None, UBYTE, SWORD, ULONG, ULONG, ULONG, ULONG, UWORD)(VC_VoicePlay)
drv_musio.VoiceStop = CFUNCTYPE(None, UBYTE)(VC_VoiceStop)
drv_musio.VoiceStopped = CFUNCTYPE(BOOL, UBYTE)(VC_VoiceStopped)
drv_musio.VoiceGetPosition = CFUNCTYPE(SLONG, UBYTE)(VC_VoiceGetPosition)
drv_musio.VoiceRealVolume = CFUNCTYPE(ULONG, UBYTE)(VC_VoiceRealVolume)
