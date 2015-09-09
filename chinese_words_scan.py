#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Scanner for contained chinese words in files.
 created by password123456
"""

import os
import sys
import codecs
import argparse
import re

def DO_SCAN_CHINESE(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    iCHINESE_WORDS_COUNT = 0
    bCHINESE_DETECT = 'false'

    for n,line in enumerate(f.read().split('\n')):
        #print n, line
        n += 1
        if re.findall(ur'[\u4e00-\u9fff]+', line):
            bCHINESE_DETECT = 'true'
            iCHINESE_WORDS_COUNT += 1
            #print "line:",n,line
        else:
            pass

    f.close()

    if bCHINESE_DETECT.lower() in ['true']:
        print ' + [Chinese /',iCHINESE_WORDS_COUNT,'] ', filename
    else:
        print ' + [Chinese /',iCHINESE_WORDS_COUNT,'] ', filename

def SCAN_TEXTFILE(path):
    if os.path.exists(path):
	    for root, dirs, files in os.walk(path):

	        for filename in files:
	            file = os.path.realpath(os.path.join(root,filename))
	            try:
	                with open(file, 'rb') as f:
	                    if b'\x00' in f.read():
	                        continue
	                        #print('The file is binary!', file)
	                    else:
	                        #print('The file is not binary!', file)
	                        DO_SCAN_CHINESE(file)
	            except:
	                pass
    else:
        print "\n[-] [ %s ] not exits.! Check directory.!! " % (path)
        sys.exit()

def main():
    opt=argparse.ArgumentParser(description="::::: Chinese Words Scanner :::::")
    opt.add_argument("scan_path", help="ex) /chinese_textable_path")
    opt.add_argument("-p", "--path", action="store_true", dest="path", help="ex) python chinese_words_scan_v0.2.py -p /chinese_textable_path")

    if len(sys.argv)<=2:
        opt.print_help()
        sys.exit(1)
    else:
        options= opt.parse_args()

    if options.path:
        path = (options.scan_path)
        SCAN_TEXTFILE(path)

    else:
        opt.print_help()
        sys.exit()

if __name__ == '__main__':
    main()
