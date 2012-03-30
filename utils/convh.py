import sys
import re
from optparse import OptionParser

if __name__ == '__main__':
    opts = OptionParser("usage: %prog [options]")
    opts.add_option("-i", "--input", action="store", type="string", dest="input", 
            help="Input File")
    opts.add_option("-n", "--name", action="store", type="string", dest="name", 
            help="Library Name")
    opts.add_option("-r", "--remove", action="store", type="string", dest="remove", 
            help="Remove list")
    opts.add_option("-o", "--output", action="store", type="string", dest="output", 
            help="Output File")

    options, args = opts.parse_args()
    if args:
        opts.print_help()
        exit(1)

    if options.remove:
        remove_list = options.remove.split(',')
    else:
        remove_list = []
    libname = options.name
    tests = 'int snd_pcm_hw_params_get_buffer_time_min(const snd_pcm_hw_params_t *params, unsigned int *val, int *dir);'
    fr = re.compile('([^ ]+)[ ]([^\(]+)\(([^\)]*)\).*', re.I)
    #m = fr.match(tests)
    #print m.groups()
    #sys.exit(0)
    
    type_dict = {
            'unsigned int': 'c_uint',
            'int': 'c_int',
            'u_int8_t': 'c_uint8',
            'u_int16_t': 'c_uint16',
            'u_int32_t': 'c_uint32',
            'u_int64_t': 'c_uint64',
            'Uint32': 'c_uint32',
            'long': 'c_long',
            'signed long': 'c_long',
            'unsigned long': 'c_ulong',
            'long long': 'c_longlong',
            'short': 'c_short',
            'unsigned short': 'c_ushort',
            'double': 'c_double',
            'float': 'c_float',
            'unsigned char': 'c_ubyte',
            'size_t': 'c_size_t',
            'ssize_t': 'c_size_t',
            'char*': 'c_char_p',
            'char': 'c_char',
            }

    with open(options.input, 'r') as infile:
        for line in infile.readlines():
            m = fr.match(line)
            c_str = ''
            if m:
                res, name, args = m.groups()
                name = name.strip()
                res = res.strip()
                while res.split(' ')[0] in remove_list:
                    res = name.split(' ', 1)[0].strip()
                    name = ' '.join(name.split(' ', 1)[1:]).strip()
                if ' ' in name:
                    res = '%s %s' % (res, name.rsplit(' ', 1)[0])
                    name = name.rsplit(' ', 1)[-1]
                if res.endswith('*'):
                    res = res[:-1].strip()
                    name = '*%s' % name
                if res.startswith('const '):
                    res = res[6:]
                elif res.startswith('struct '):
                    res = res[7:]
                if res == 'const':
                    res = name.split(' ')[0]
                    name = name.split(' ', 1)[1]
                elif res.startswith('struct'):
                    res = name.split(' ')[0]
                    name = name.split(' ', 1)[1]
                if res == 'unsigned':
                    res = '%s %s' % (res, name.split(' ')[0])
                    name = name.split(' ', 1)[1]
                if res == 'char' and name.startswith('*'):
                    res = 'c_char_p'
                    name = name[1:]
                if name.startswith('*'):
                    if res == 'void':
                        res = 'c_void_p'
                    else:
                        res = '%s%s%s' % ('POINTER(' * name.count('*'), res, ')' * name.count('*'))
                    name = name[name.count('*'):]
                name = name.strip()
                res = res.strip()
                argsl = []
                args = args.strip()
                for arg in args.split(','):
                    arg = arg.strip()
                    if arg.startswith('const '):
                        arg = arg[6:]
                    elif arg.startswith('struct '):
                        arg = arg[7:]
                    argl = arg.rsplit(' ', 1)
                    t = argl[0]
                    if t.endswith('*'):
                        pointer_c = t.count('*')
                        t = t[:-pointer_c].strip()
                    else:
                        pointer_c = argl[-1].count('*')

                    if t == 'void' and args != 'void':
                        pointer_c -= 1
                        t = 'c_void_p'
                    elif args == 'void':
                        t = ''
                    elif t == 'char' and argl[-1].startswith('*'):
                        pointer_c -= 1
                        t = 'c_char_p'
                    else:
                        t = type_dict.get(t, t)
                    args = '%s%s%s' % ('POINTER(' * pointer_c, t, ')' * pointer_c)
                    argsl.append(args)
                arg_str = '[%s]' % ', '.join(argsl)
                str1 = '%s = %s.%s' % (name, libname, name)
                str2 = '%s.argtypes = %s' % (name, arg_str)
                if res.strip() == 'void':
                    res = 'None'
                else:
                    res = type_dict.get(res, res)
                str3 = '%s.restype = %s' % (name, res)
                c_str = '#%s%s\n%s\n%s\n' % (line, str1, str2, str3)
                #print str1
                #print str2
                #print str3
            if c_str:
                print c_str
            else:
                print line,

