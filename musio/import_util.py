#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# Import utility functions and classes
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


""" Import utility functions and classes

    LazyImport      Import modules when they are accessed
    OnDemand        Load modules when they are accessed

"""


from os import walk as os_walk
from os.path import isdir as os_isdir
from os.path import abspath as os_abspath
from os.path import dirname as os_dirname
from os.path import basename as os_basename
from types import ModuleType as types_ModuleType
import sys


class Module(types_ModuleType):
    pass


class LazyImport(types_ModuleType):
    """ LazyImport only loads the module when one of its attributes is
    accessed.

    """

    def __init__(self, name, globals={}, locals={}, fromlist=[], level=0):
        """ LazyImport(module_name, globals={}, locals={}, fromlist=[],
        level=0) -> Load module only when it is needed.

        """

        super(LazyImport, self).__init__(name)

        # package = os_basename(os_dirname(__file__))
        # print(package, name)
        # if name.startswith('.'):
        #     name = '%s%s' % (package, name)

        self._globals = globals
        self._locals = locals

        if not fromlist:
            # Build the sub-modules list from the name.
            fromlist = name.split('.')[1:]

        self._fromlist = fromlist

        self._level = level
        self.__mod__ = None
        # self.__name__ = name

    def __getattribute__(self, attr):
        """ Import the module and set __getattribute__ so this method is not
        called again.

        """

        # Set the class to a new empty module so getattr will work.
        self.__class__ = type('Module', (types_ModuleType,), {})

        # print('__getattribute__: ', self.__name__, attr)
        # if attr == "__package__":
        #     return getattr(self, "__package__", None)

        # Test if this method has been called.
        if not getattr(self, '__mod__', None):
            # Remove previous occurance of module from sys.modules.
            if self.__name__ in sys.modules:
                sys.modules.pop(self.__name__)

            # Import the module.
            self.__mod__ = __import__(self.__name__, self._globals,
                                      self._locals, self._fromlist,
                                      self._level)

            # Add the modules dict items to this module.
            self.__dict__.update(self.__mod__.__dict__)

            # The next time getattribute is called it will be for the
            # loaded module not this one.
            self.__getattribute__ = self.__mod__.__getattribute__

            # Add the module back into sys.modules.
            sys.modules[self.__name__] = self.__mod__

        # Return the item.
        return getattr(self, attr)


class OnDemand(object):
    """ Load modules when accessed.

    """

    def __init__(self, module_name, globals={}, locals={}, fromlist=[],
                 level=0):
        """ OnDemand(module_name, globals={}, locals={}, fromlist=[], level=0)
        -> Load module only when it is needed.

        """

        self._module_name = module_name
        self._globals = globals
        self._locals = locals
        self._fromlist = fromlist
        self._level = level
        self._module = None

    def _import(self):
        """ Import the module.

        """

        self._module = __import__(self._module_name, self._globals,
                                  self._locals, self._fromlist, self._level)

    def __getattr__(self, attr):
        """ Load the module if it is not already loaded.  Returns the modules
        attributes.

        """

        if not self._module:
            self._import()

        return getattr(self._module, attr)

    @property
    def __dict__(self):
        """ Load the module if it is not already loaded.  Returns the modules
        __dict__.

        """

        if not self._module:
            self._import()

        return vars(self._module)

# Try to make a lazy module.
class LazyModule(types_ModuleType):
    """ LazyModule only loads the module when one of its attributes is
    accessed.

    """

    def __getattribute__(self, attr):
        """ Initialize the module and add it to sys.modules.

        """

        self.__class__ = Module
        print(self.__name__, 'get', attr)
        exec('import %s' % self.__name__)
        # self.__mod__ = __import__(self.__name__, {}, {}, [])
        # self.__loader__ = super(LazyImporter, self.__loader__)
        # self.__loader__.load_module(self.__name__)
        return getattr(self, attr, None)

# Test class
class LazyImp(object):
    """ LazyImporter uses LazyModule to load the module when one of its
    attributes is accessed.

    """

    def __init__(self):
        self._loaded = []

    def find_module(self, fullname, path=None):
        """ Used LazyLoader.

        """

        if fullname in self._loaded:
            return None

        print(self, fullname, path)
        return self

    # @importlib_util.module_for_loader
    def load_module(self, fullname):
        """ Load the module.

        """

        print(fullname, dir(fullname))
        self._loaded.append(fullname)

        if fullname in sys.modules:
            return sys.modules[fullname]

        __import__(fullname, {}, {}, [])
        return sys.modules[fullname]


def _build_mod_list(mod_path: list) -> list:
    """ _build_mod_list(mod_path, suffix) -> Add all the paths in mod_path to
    sys.path and return a list of all modules in sys.path ending in suffix.

    """

    mod_path = [mod_path] if type(mod_path) is str else mod_path

    # Add the path of this file to the search path.
    mod_path.append(os_abspath(os_dirname(__file__)))

    # Build the list of modules in mod_path(s).
    mod_list = ('{0}.{1}.{2}'.format(os_basename(path), \
                    os_basename(root).replace(os_basename(path), ''), \
                    name.rsplit('.', 1)[0]).replace('..', '.') \
                    for path in mod_path \
                        if os_isdir(path) \
                            for root, dirs, files in os_walk(path) \
                                for name in files \
                                    if name.endswith('.py'))

    return mod_list


class LazyImporter(object):
    """ LazyImporter uses LazyImport to load the module when one of its
    attributes is accessed.

    """

    def __init__(self, skip=[], mod_path=[]):
        """ LazyImporter() -> Initialize the lazy importer.

        """

        # List to hold module names that were already loaded.
        self._loaded = skip

        self._mods = tuple(_build_mod_list(mod_path))

    def find_module(self, fullname, path=None):
        """ Use self.

        """

        # Use pythons importer if fullname is asked for more than once,
        # because it will mean that an attribute was requested from the
        # lazy module.
        if fullname in self._loaded or fullname not in self._mods:
            return None

        return self

    def load_module(self, fullname):
        """ Load the module.

        """

        # Log that this module has been handled so it can load.
        self._loaded.append(fullname)

        # Return the module if it is already loaded.
        if fullname in sys.modules:
            return sys.modules[fullname]

        # Create a new lazy module.
        module = LazyImport(fullname)

        module.__loader__ = self

        # Add the usual stuff.
        module.__file__ = self.__class__.__name__
        if '.' not in fullname:
            module.__package__ = None
        else:
            module.__package__ == fullname.rpartition('.')[0]
            module.__path__ = []


        # Add the module to sys.modules.
        sys.modules[fullname] = module

        # Return the lazy module.
        return module


def load_lazy_import(skip=[], mod_path=[]):
    """ Insert the lazy importer.

    """

    # Make LazyImporter the default importer.
    sys.meta_path.insert(0, LazyImporter(skip, mod_path))


def unload_lazy_import():
    """ Remove lazy importer.

    """

    # Remove LazyImporter from sys.meta_path.
    [sys.meta_path.remove(i) for i in sys.meta_path if type(i) is LazyImporter]
