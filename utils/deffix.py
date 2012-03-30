import sys
import re
from optparse import OptionParser

if __name__ == '__main__':
    opts = OptionParser("usage: %prog [options]")
    opts.add_option("-i", "--input", action="store", type="string", dest="input", 
            help="Input File")
    opts.add_option("-o", "--output", action="store", type="string", dest="output", 
            help="Output File")

    options, args = opts.parse_args()
    if args:
        opts.print_help()
        exit(1)

    tests = '#define IEC958_AES0_PROFESSIONAL	(1<<0)	/**< 0 = consumer, 1 = professional */'
    #spacefix = re.compile('[^\w\(\)#]+')
    #spacefix = re.compile('[\t]+')

    spacefix = re.compile('[ ]+')
    #print tests
    #tests = tests[8:]
    #tests = tests.replace('\t', ' ')
    #tests = spacefix.sub(' ', tests, count=2)
    #print tests.split(' ', 2)
    #sys.exit()
    
    with open(options.input, 'r') as infile:
        for line in infile.readlines():
            o_str = ''
            if line.startswith('#define '):
                w_line = line[8:].replace('\t', ' ')
                w_line = spacefix.sub(' ', w_line, count=2)
                def_list = w_line.split(' ', 2)
                if len(def_list) == 3:
                    o_str = '%s = %s\t# %s' % tuple(def_list)
                else:
                    o_str = w_line
            if o_str:
                print o_str,
            else:
                print line,
