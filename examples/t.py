# import ctypes
# xmp = ctypes.cdll.LoadLibrary('./libxmp.so')
# with open('test.raw', 'wb') as out:
#     m = xmp.xmp_create_context()
#     o = xmp.xmp_load_module(m, '/home/josiah/sshfs/cherry/share/Tunes/adlib/The!Complete.hsc')
#     if o != 0:
#         print("error loading")
#     else:
#         print(xmp.xmp_player_start(m, 44100, 0))
#         input()
#         print(xmp.xmp_player_end(m))
from sys import argv as sys_argv
from sys import exit as sys_exit
from musio import alsa_io
alsa = alsa_io.Alsa()
import xmp
mi = xmp.xmp_module_info()
print(mi)
# c = xmp.xmp_create_context()
c = (xmp.c_char * 4096)()
print(c)
print(sys_argv[1])
if xmp.xmp_load_module(c, sys_argv[1].encode()) != 0:
    print("can't load module")
    sys_exit()

print(xmp.xmp_player_start(c, 44100, 0))
while (xmp.xmp_player_frame(c) == 0):
    xmp.xmp_player_get_info(c, xmp.byref(mi))
    # print(mi.order)
    if (mi.loop_count > 0):
        break
    data = xmp.string_at(mi.buffer, mi.buffer_size)
    alsa.write(data)
xmp.xmp_player_end(c)
xmp.xmp_release_module(c)
xmp.xmp_free_context(c)
