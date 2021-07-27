#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Provides a access to the alsa mixer.
# using with the 'with' statement.
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


"""An alsa mixer."""

from typing import Any

from .import_util import LazyImport
from .io_util import _check_dependencies

_alsamixer = LazyImport('alsa.mixer', globals(), locals(), ['mixer'], 1)

_dependencies = {
    'ctypes': ['asound'],
    'python': []
}

if not _check_dependencies(_dependencies):
    print("Mixer disabled: missing dependencies.")


class Mixer(object):
    """Mixer object to control the alsa mixer."""

    def __init__(self, card: str = 'default', mixer: str = 'PCM'):
        """Open the mixer on the specified card."""
        self._card, self._mixer = card, mixer
        self._mixer_t, self._mixer_selem, self._mixer_elem = self._open(card,
                                                                        mixer)

    def __repr__(self) -> str:
        """Get the python execable representation of self."""
        return (f"{__class__.__name__}(card='{self._card}', "
                f"mixer='{self._mixer}')")

    def _test(self, value: Any):
        """Test if the value is valid.  If it is not raise and error."""
        assert(not value)

    def _open(self, card: str, mixer: str) -> tuple[Any, Any, Any]:
        """Open the mixer."""
        mixer_t = _alsamixer.POINTER(_alsamixer.snd_mixer_t)()
        self._test(_alsamixer.snd_mixer_open(_alsamixer.byref(mixer_t), 0))
        self._test(_alsamixer.snd_mixer_attach(mixer_t, card.encode()))
        self._test(_alsamixer.snd_mixer_selem_register(mixer_t, None, None))
        self._test(_alsamixer.snd_mixer_load(mixer_t))

        mixer_selem = _alsamixer.POINTER(_alsamixer.snd_mixer_selem_id_t)()
        self._test(_alsamixer.snd_mixer_selem_id_malloc(
            _alsamixer.byref(mixer_selem)))
        self._test(_alsamixer.snd_mixer_selem_id_set_index(mixer_selem, 0))
        self._test(_alsamixer.snd_mixer_selem_id_set_name(
            mixer_selem, mixer.encode()))

        mixer_elem = _alsamixer.snd_mixer_find_selem(mixer_t, mixer_selem)

        return (mixer_t, mixer_selem, mixer_elem)

    def get_volume(self, channel: int) -> int:
        """Return the volume of the specified channel.

        (0, 1) left or right.  return -1 if not volume control exists
        """
        if _alsamixer.snd_mixer_selem_has_playback_volume(self._mixer_elem):
            left_vol = _alsamixer.c_long()
            self._test(_alsamixer.snd_mixer_selem_get_playback_volume(
                self._mixer_elem, channel, left_vol))

            return left_vol.value
        else:
            return -1

    def get_volume_range(self) -> tuple[int, int]:
        """Return a tuple of the volume range.

        Return (-1, -1) if not volume control exists
        """
        if _alsamixer.snd_mixer_selem_has_playback_volume(self._mixer_elem):
            min_vol = _alsamixer.c_long()
            max_vol = _alsamixer.c_long()
            self._test(_alsamixer.snd_mixer_selem_get_playback_volume_range(
                self._mixer_elem,
                _alsamixer.byref(min_vol),
                _alsamixer.byref(max_vol)
            ))

            return (min_vol.value, max_vol.value)
        else:
            return (-1, -1)

    def get_volume_percent(self, channel: int) -> int:
        """Return a percentage volume.

        Return the volume as a percent of the specified channel (0, 1) left or
        right.  return -1 if not volume control exists
        """
        if _alsamixer.snd_mixer_selem_has_playback_volume(self._mixer_elem):
            return round(
                (100 / self.get_volume_range()[-1]) * self.get_volume(channel)
            )
        else:
            return -1

    def set_volume(self, value: int, channel: int = -1):
        """Set the volume to value.

        Set channel to 0 for left channel, 1 for right channel, and -1 for
        both.
        """
        assert(
            _alsamixer.snd_mixer_selem_has_playback_volume(self._mixer_elem)
        )

        c_value = _alsamixer.c_long(value)

        if channel == -1:
            self._test(_alsamixer.snd_mixer_selem_set_playback_volume_all(
                self._mixer_elem, c_value))
        else:
            self._test(_alsamixer.snd_mixer_selem_set_playback_volume(
                self._mixer_elem, channel, c_value))

    def is_muted(self, channel) -> bool:
        """Return True if muted els False.

        Channel = (0, 1) left or right.
        """
        assert(
            _alsamixer.snd_mixer_selem_has_playback_switch(self._mixer_elem)
        )

        left_vol = _alsamixer.c_int()
        self._test(_alsamixer.snd_mixer_selem_get_playback_switch(
            self._mixer_elem, channel, left_vol))

        return left_vol.value == 0

    def set_mute(self, switch: bool, channel: int = -1):
        """Set mute status for channel to switch.

        channel = (0, 1) left or right.
        """
        assert(
            _alsamixer.snd_mixer_selem_has_playback_switch(self._mixer_elem)
        )

        if channel == -1:
            self._test(_alsamixer.snd_mixer_selem_set_playback_switch_all(
                self._mixer_elem, 0 if switch else 1))
        else:
            self._test(_alsamixer.snd_mixer_selem_set_playback_switch(
                self._mixer_elem, channel, 0 if switch else 1))

    def close(self):
        """Close the mixer."""
        self._test(_alsamixer.snd_mixer_close(self._mixer_t))
        self._test(_alsamixer.snd_mixer_selem_id_free(self._mixer_selem))

    def __enter__(self) -> object:
        """Provide the ability to use pythons with statement."""
        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Close the pcm when finished."""
        try:
            self.close()
            return not bool(exc_type)
        except Exception as err:
            print(err)
            return False
