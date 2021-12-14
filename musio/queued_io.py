#!/usr/bin/env python
# vim: sw=4:ts=4:sts=4:fdm=indent:fdl=0:
# -*- coding: UTF8 -*-
#
# A queued writer object for when the writing takes longer than the
# reading.
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


"""QueuedWriter.

An object for using multiprocesses to write instead of blocking and clogging up
the read.
"""

from multiprocessing import Process, Queue
from queue import Empty
from typing import Callable


def _queue_writer(func: Callable, in_queue: Queue, out_queue: Queue):
    """Read data from queue and send it to func until 'EOF' is received.

    When exiting it puts the sum of the return values of func in out_queue.
    """
    written = 0

    while True:
        try:
            data = in_queue.get()

            if not data:
                continue
            if data == 'EOF':
                break

            # Send data to the writer function and add the return value
            # to written.
            written += func(data)
        except Empty as err:
            print(f"Empty queue: {err}")

    # Return the number of bytes written.
    out_queue.put(written)


class QueuedWriter:
    """A queued multiprocess writter."""

    def __init__(self, func: Callable):
        """Fill a queue and call func with data as it is able to use it."""
        self._func = func

        # Queue to fill with data to be written.
        self._data_queue = Queue()

        # Queue to get the return value from the write function.
        self._return_queue = Queue()

        # Create the writer process.
        self._writer_p = Process(target=_queue_writer,
                                 args=(func, self._data_queue,
                                       self._return_queue))
        self._writer_p.start()

    def __repr__(self):
        """Return a python expression to recreate this instance."""
        return f"{self.__class__.__name__}(func={self._func})"

    def write(self, data: str | bytes):
        """Send more data down the queue to the processing function."""
        self._data_queue.put(data)

        return len(data)

    __call__ = write

    def close(self):
        """Close the queue and writer process."""
        # Send EOF to end the writer process.
        self._data_queue.put('EOF')

        # Close the queue.
        self._data_queue.close()

        # Wait for the queue buffer to empty.
        self._data_queue.join_thread()

        # Get the return value from the writer process.
        ret_val = self._return_queue.get()

        # Close the return queue.
        self._return_queue.close()

        # Wait for the writer process to exit.
        self._writer_p.join()

        # Return the writer result.
        return ret_val

    def __enter__(self) -> object:
        """Provide the ability to use pythons with statement."""
        try:
            return self
        except Exception as err:
            print(err)
            return None

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """Close the file when finished."""
        try:
            return bool(self.close()) or not bool(exc_type)
        except Exception as err:
            print(err)
            return False
