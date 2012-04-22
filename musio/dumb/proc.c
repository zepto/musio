/* C proccessing function.  
 * Compile with: gcc -shared -o proc.so proc.c -I/usr/include/python2.7
 * Copyright (C) 2008 2010 Josiah Gordon <josiahg@gmail.com>
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <Python.h>

PyObject *convert_data(int depth, int bigendian, size_t size, void* data);

PyObject *convert_data(int depth, int bigendian, size_t size, void* data)
{
    int i = 0;
    char * buffer = (char*)data;

    if (depth == 16) {
        short* s_data = (short*)data;
        if (bigendian) {
            for (i = 0; i < size / 2; i++) {
                short val = s_data[i];
                buffer[i*2] = (char)(val >> 8);
                buffer[i*2+1] = (char)val;
            }
        } else {
            for (i = 0; i < size / 2; i++) {
                short val = s_data[i];
                buffer[i*2] = (char)val;
                buffer[i*2+1] = (char)(val >> 8);
            }
        }
    }

    return PyBytes_FromStringAndSize((char*)buffer, size);
}
