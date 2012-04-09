#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A module to handle the playback of midi music through fluidsynth.
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

""" Fluidsynth module.

"""

from functools import partial

from io_base import AudioIO, OnDemand, io_wrapper

_fluidsynth = OnDemand('fluidsynth.fluidsynth', globals(), locals(),
                       ['fluidsynth'], 0)


__supported_dict = {
        'ext': ['.mid', '.midi'],
        'handler': 'FluidsynthFile',
        }

# Interp constants
FLUID_INTERP_NONE = 0
FLUID_INTERP_LINEAR = 1
FLUID_INTERP_4THORDER = 4
FLUID_INTERP_7THORDER = 7

FLUID_INTERP_DEFAULT =  FLUID_INTERP_4THORDER
FLUID_INTERP_HIGHEST =  FLUID_INTERP_7THORDER

# Chorus constants
FLUID_CHORUS_MOD_SINE = 0
FLUID_CHORUS_MOD_TRIANGLE = 1

FLUID_CHORUS_DEFAULT_N = 3
FLUID_CHORUS_DEFAULT_LEVEL = 2.0
FLUID_CHORUS_DEFAULT_SPEED = 0.3
FLUID_CHORUS_DEFAULT_DEPTH = 8.0
FLUID_CHORUS_DEFAULT_TYPE = FLUID_CHORUS_MOD_SINE

# Reverb constants
FLUID_REVERB_DEFAULT_ROOMSIZE = 0.2
FLUID_REVERB_DEFAULT_DAMP = 0.0
FLUID_REVERB_DEFAULT_WIDTH = 0.5
FLUID_REVERB_DEFAULT_LEVEL = 0.9


class Settings(object):
    """ Fluidsynth settings wrapper.

    """

    def __init__(self):
        """ Create new fluidsynth settings.

        """

        self._settings = _fluidsynth.new_fluid_settings()

        self.setstr = partial(_fluidsynth.fluid_settings_setstr, self._settings)
        self.setint = partial(_fluidsynth.fluid_settings_setint, self._settings)
        self.setnum = partial(_fluidsynth.fluid_settings_setnum, self._settings)

        self.getstr = partial(_fluidsynth.fluid_settings_getstr, self._settings)
        self.getint = partial(_fluidsynth.fluid_settings_getint, self._settings)
        self.getnum = partial(_fluidsynth.fluid_settings_getnum, self._settings)

        self.delete = partial(_fluidsynth.delete_fluid_settings, self._settings)

    def set(self, key, value):
        """ Set the setting item 'key' to value 'value.'

        """

        if type(value) is str:
            set_func = self.setstr
        elif type(value) is int:
            set_func = self.setint
        elif type(value) is float:
            set_func = self.setnum
        else:
            return -1

        return set_func(key, value)
    __setitem__ = set

    def get(self, key):
        """ Return the current setting for 'key.'

        """

        key = key.encode('utf8', 'replace')
        key_type = _fluidsynth.fluid_settings_get_type(self._settings, key)
        if key_type == _fluidsynth.FLUID_NUM_TYPE:
            buffer = _fluidsynth.c_double()
            self.getnum(key, _fluidsynth.byref(buffer))
            return buffer.value
        elif key_type == _fluidsynth.FLUID_INT_TYPE:
            buffer = _fluidsynth.c_int()
            self.getint(key, _fluidsynth.byref(buffer))
            return buffer.value
        elif key_type == _fluidsynth.FLUID_STR_TYPE:
            buffer = _fluidsynth.c_char_p()
            self.getstr(key, _fluidsynth.byref(buffer))
            return _fluidsynth.string_at(buffer).decode('ascii', 'ignore')
        else:
            return -1
    __getitem__ = get

    @property
    def object(self):
        """ Return the settings object.

        """

        return self._settings


class Synth(object):
    """ Fluidsynth synth wrapper.

    """

    def __init__(self, settings, address=None):
        """ Synth(settings) -> Create a new fluid synth object, with the 
        settings 'settings.'

        """

        self._reverb = {
                'roomsize': 0.2,
                'damping': 0.0,
                'width': 0.5,
                'level': 0.9
                }

        self._chorus = {
                'nr': 3,
                'level': 2.0,
                'speed': 0.3,
                'depth_ms': 8.0,
                'type': 0
                }

        self._settings = settings

        if address:
            self._synth = _fluidsynth.fluid_synth_t.from_address(address)
        else:
            self._synth = _fluidsynth.new_fluid_synth(settings.object)

        # Reverb setting methods
        self.enable_reverb = partial(_fluidsynth.fluid_synth_set_reverb_on,
                                     self.object)
        self.set_reverb = partial(_fluidsynth.fluid_synth_set_reverb,
                                  self.object)
        self.get_reverb_roomsize = partial(
                _fluidsynth.fluid_synth_get_reverb_roomsize, self.object)
        self.get_reverb_damp = partial(_fluidsynth.fluid_synth_get_reverb_damp,
                                  self.object)
        self.get_reverb_level = partial(
                _fluidsynth.fluid_synth_get_reverb_level, self.object)
        self.get_reverb_width = partial(
                _fluidsynth.fluid_synth_get_reverb_width, self.object)

        # Chorus setting methods
        self.enable_chorus = partial(_fluidsynth.fluid_synth_set_chorus_on,
                                     self.object)
        self.set_chorus = partial(_fluidsynth.fluid_synth_set_chorus,
                                  self.object)
        self.get_chorus_nr = partial(_fluidsynth.fluid_synth_get_chorus_nr,
                                     self.object)
        self.get_chorus_level = partial(
                _fluidsynth.fluid_synth_get_chorus_level, self.object)
        self.get_chorus_speed_Hz = partial(
                _fluidsynth.fluid_synth_get_chorus_speed_Hz, self.object)
        self.get_chorus_depth_ms = partial(
                _fluidsynth.fluid_synth_get_chorus_depth_ms, self.object)
        self.get_chorus_type = partial(_fluidsynth.fluid_synth_get_chorus_type,
                                       self.object)

        # Soundfont methods
        self.is_soundfont = _fluidsynth.fluid_is_soundfont
        self.load_soundfont = partial(_fluidsynth.fluid_synth_sfload,
                                      self.object)
        self.load_soundfont.__doc__ = \
                """ load_soundfont(filename, reset) -> Load the specified
        soundfont.  If reset is 1 then reset all channels.

        """

        # Gain setting methods
        self.get_gain = partial(_fluidsynth.fluid_synth_get_gain, self.object)
        self.set_gain = partial(_fluidsynth.fluid_synth_set_gain, self.object)

        self.process = partial(_fluidsynth.fluid_synth_process, self._synth)
        self.write_s16 = partial(_fluidsynth.fluid_synth_write_s16, 
                                 self.object)
        self.write_float = partial(_fluidsynth.fluid_synth_write_float, 
                                   self.object)

        self.delete = partial(_fluidsynth.delete_fluid_synth, self._synth)
        self.set_sample_rate = partial(_fluidsynth.fluid_synth_set_sample_rate,
                                       self.object)

        self.set_interp_method = partial(
                _fluidsynth.fluid_synth_set_interp_method.restype, self.object)

    def read_s16(self, size):
        """ read_s16(size) -> Read size amount of signed 16 bit data and
        return it.

        """

        multiplier = self._settings.get('synth.audio-channels') * 4
        buf = _fluidsynth.create_string_buffer(size * multiplier)
        self.write_s16(size, buf, 0, 2, buf, 1, 2)
        return _fluidsynth.string_at(buf, _fluidsynth.sizeof(buf))

    def read_float(self, size):
        """ read_float(size) -> Read size amount of floating point data and
        return it.

        """

        multiplier = self._settings.get('synth.audio-channels') * 2
        buf = (_fluidsynth.c_float * size)()
        self.write_float(size / multiplier, buf, 0, 2, buf, 1, 2)
        return _fluidsynth.string_at(buf, _fluidsynth.sizeof(buf))

    @property
    def gain(self):
        """ The synth gain.

        """

        return self.get_gain()

    @gain.setter
    def gain(self, value):
        """ Set the gain.

        """

        if value < 0.0 or value > 10.0:
            print("Value must be in range 0.0-10.0")
            return
        self.set_gain(float(value))

    @property
    def reverb(self):
        """ A tuple representing the current reverb settings.
            (roomsize, damping, width, level)

        """

        return dict(zip(('roomsize', 'damping', 'width', 'level'),
                         (self.get_reverb_roomsize(), self.get_reverb_damp(),
                          self.get_reverb_width(), self.get_reverb_level())))

    def _dict_to_tup(self, value_dict, keys_tup, defaults):
        """ _dict_to_tup(value_dict, keys_tup, defaults) -> Returns a tuple of
        the values of value_dict and default combined and in the order of
        keys_tups.

        """

        # Make a temporary dict for faster access.
        temp_dict = defaults

        # Update the temp dict with the new values.
        temp_dict.update(value_dict)

        # Convert the temp dict to a tuple sorted by keys according to
        # keys_tup, and return it.
        return (temp_dict.get(i, 0) for i in keys_tup)

    @reverb.setter
    def reverb(self, value):
        """ A tuple representing the current reverb settings.
            (roomsize, damping, width, level)

        """

        if hasattr(value, 'get'):
            name_tup = ('roomsize', 'damping', 'width', 'level')
            value = self._dict_to_tup(value, name_tup, self._reverb)

        self.set_reverb(*value)

        # Update object variable so we can use the new values next time.
        self._reverb = self.reverb

    @property
    def chorus(self):
        """ A tuple representing the current chorus settings.
            (level, speed, depth_ms, type)

        """

        return dict(zip(('nr', 'level', 'speed', 'depth_ms', 'type'),
                         (self.get_chorus_nr(), self.get_chorus_level(),
                          self.get_chorus_speed_Hz(),
                          self.get_chorus_depth_ms(), self.get_chorus_type())))

    @chorus.setter
    def chorus(self, value):
        """ A tuple representing the current chorus settings.
            (level, speed, depth_ms, type)

        """

        if hasattr(value, 'get'):
            name_tup = ('nr', 'level', 'speed', 'depth_ms', 'type')
            value = self._dict_to_tup(value, name_tup, self._chorus)

        self.set_chorus(*value)

        # Update object variable so we can use the new values next time.
        self._chorus = self.chorus

    @property
    def object(self):
        """ The synth object.

        """

        return self._synth

    @classmethod
    def process(cls, synth, length, num_in, in_data, num_out, out_data):
        """ Process midi event to produce audio.

        """

        return _fluidsynth.fluid_synth_process(synth, length, num_in, in_data,
                                               num_out, out_data)

    @classmethod
    def from_address(cls, address):
        """ Return the synth object at the given address.

        """

        return _fluidsynth.fluid_synth_t.from_address(address)


class Player(object):
    """ A fluidsynth player.

    """

    def __init__(self, synth):
        """ Player(synth) -> Create a new fluidsynth player.

        """

        self._player = _fluidsynth.new_fluid_player(synth.object)

        self.play = partial(_fluidsynth.fluid_player_play, self.object)
        self.stop = partial(_fluidsynth.fluid_player_stop, self.object)
        self.join = partial(_fluidsynth.fluid_player_join, self.object)
        self.set_loop = partial(_fluidsynth.fluid_player_set_loop, self.object)
        self.set_loop.__doc__ = \
                """ set_loop(loop) -> Set the number of times to loop.  A
        loop value of -1 means to loop forever.

        """

        self.set_tempo = partial(_fluidsynth.fluid_player_set_midi_tempo, 
                                 self.object)
        self.set_bpm = partial(_fluidsynth.fluid_player_set_bpm, self.object)

        self.is_midifile = _fluidsynth.fluid_is_midifile

        self.load_midi = partial(_fluidsynth.fluid_player_add, self.object)
        self.load_midi.__doc__ = \
                """ load_midi(filename) -> Load the specified midi file.

        """

        self.get_status = partial(_fluidsynth.fluid_player_get_status, 
                                  self.object)

        self.delete = partial(_fluidsynth.delete_fluid_player, self._player)

    @property
    def object(self):
        """ The player object.

        """

        return self._player

    @property
    def done(self):
        """ True if player is done.

        """

        return self.get_status() == _fluidsynth.FLUID_PLAYER_DONE


class AudioDriver(object):
    """ A fluidsynth audio driver.

    """

    def __init__(self, settings, synth, process_func=None):
        """ AudioDriver(settings, synth, process_func=None) -> Create a new
        fluidsynth audio driver.  Process_func can be None or a function to
        process audio data before it is played.

        """

        self._settings = settings
        self._synth = synth
        self._process_func = process_func

        if not process_func:
            self._adriver = \
                    _fluidsynth.new_fluid_audio_driver(settings.object,
                                                       synth.object)
        else:
            self._process_callback = \
                    _fluidsynth.fluid_audio_func_t(self._process_callback_f)
            self._adriver = \
                    _fluidsynth.new_fluid_audio_driver2(settings.object,
                                                        self._process_callback,
                                                        synth.object)

        self.delete = partial(_fluidsynth.delete_fluid_audio_driver,
                              self._adriver)

    def _process_callback_f(self, synth_p, length, num_in, in_data, num_out,
                            out_data):
        """ Process audio data before it is played.

        """

        synth = Synth(self._settings, synth_p)
        if synth.process(length, num_in, in_data, num_out, out_data) != 0:
            return -1
        return self._process_func(synth, length, num_in, in_data, num_out,
                                  out_data)

    @property
    def object(self):
        """ The audio driver object.

        """

        return self._adriver


class FluidsynthFile(AudioIO):
    """ Access a midi file like a regular file.

    """

    # Only reading is supported
    _supported_modes = 'r'

    def __init__(self, filename, soundfont, rate=44100, gain=0.2,
                 reverb={'roomsize': 0.2, 'damping': 0.0, 'width': 0.5,
                         'level': 0.9}, 
                 chorus={'nr': 3, 'level': 2.0, 'speed': 0.3, 'depth_ms': 8.0,
                         'type': 0}, **kwargs):
        """ FluidsynthFile(filename, soundfont, rate=44100, gain=0.2,
        reverb=(0.2, 0.0, 0.5, 0.9), chorus=(3, 2.0, 0.3, 8.0, 0)) ->
        Initialize the playback settings of the player.

        """

        super(FluidsynthFile, self).__init__(filename=filename, mode='r',
                                             rate=rate, depth=16,
                                             channels=2)

        self._soundfont = soundfont

        self._gain = gain
        self._reverb = reverb
        self._chorus = chorus

        # Create settings object to use when creating a synth object.
        self._settings = Settings()

        # Setup the synth object.
        self._synth = Synth(self._settings)

        self._synth.gain = gain
        self._synth.set_sample_rate(rate)

        # Enable and set reverb.
        self._synth.enable_reverb(True)
        self.reverb = reverb

        # Enable and set chorus.
        self._synth.enable_chorus(True)
        self.chorus = chorus

        # Create player object using synth.
        self._player = Player(self._synth)

        # Load the midi and soundfont.
        if not self._open(filename, soundfont):
            raise IOError("Error loading midi '%s' and soundfont '%s'" % \
                          (filename, soundfont))

        # Start rendering the midi to audio data that we can read when
        # we want it.
        self._player.play()

    def __repr__(self):
        """ __repr__ -> Returns a python expression to recreate this instance.

        """

        repr_str = "filename='%(_filename)s', soundfont='%(_soundfont)s', rate=%(_rate)s, gain=%(_gain)s, reverb=%(_reverb)s, chorus=%(_chorus)s" % self

        return '%s(%s)' % (self.__class__.__name__, repr_str)

    @property
    def loops(self):
        """ How many times the module should play.

        """

        return self._loops

    @loops.setter
    def loops(self, value):
        """ Set how many times the module should play.

        To play forever use a value of -1.

        """

        self._loops = value
        self._player.set_loop(value)

    @property
    def gain(self):
        """ The current gain.

        """

        return self._synth.gain

    @gain.setter
    def gain(self, value):
        """ Set the volume.

        """

        self._synth.gain = value

    @property
    def reverb(self):
        """ A tuple representing the current reverb settings.
            (roomsize, damping, width, level)

        """

        return self._synth.reverb

    @reverb.setter
    def reverb(self, value):
        """ A tuple representing the current reverb settings.
            (roomsize, damping, width, level)

        """

        self._synth.reverb = value
        self._reverb = self._synth._reverb

    @property
    def chorus(self):
        """ A tuple representing the current chorus settings.
            (level, speed, depth_ms, type)

        """

        return self._synth.chorus

    @chorus.setter
    def chorus(self, value):
        """ A tuple representing the current chorus settings.
            (level, speed, depth_ms, type)

        """

        self._synth.chorus = value
        self._chorus = self._synth._chorus

    def _open(self, filename, soundfont):
        """ _load(filename) -> Load the specified file.

        """

        # Convert midi name to bytes object so the ctypes function can use it.
        filename = filename.encode('utf8', 'replace')

        # Check if filename is a valid midi.
        if not self._player.is_midifile(filename):
            raise IOError("Not a midi file: %s" % filename)

        # Load midi.
        if self._player.load_midi(filename) < 0:
            return False

        # Convert soundfont name to bytes object so the ctypes function
        # can use it.
        soundfont = soundfont.encode('utf8', 'replace')

        # Check if soundfont is a soundfont.
        if not self._synth.is_soundfont(soundfont):
            raise IOError("Not a soundfont: %s" % soundfont)

        # Load soundfont.
        if self._synth.load_soundfont(soundfont, True) < 0:
            return False

        self._closed = False

        return True

    @io_wrapper
    def read(self, size: int) -> bytes:
        """ read(size=None) -> Reads size amount of data and returns it.

        """

        size //= self._channels * 2

        return self._synth.read_s16(size)

    def close(self):
        """ close -> Closes and cleans up.

        """

        if not self.closed:
            self._player.stop()
            self._player.delete()
            self._synth.delete()
            self._settings.delete()

            self._closed = True
