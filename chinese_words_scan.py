
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Scanner for contained chinese words in files.
 created by password123456
"""

import os,sys
import codecs
import argparse
import re


def do_scan_chinese(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    chinese_words_counter = 0
    chinese_detect = 'false'

    for n,line in enumerate(f.read().split('\n')):
        #print n, line
        n += 1
        if re.findall(ur'[\u4e00-\u9fff]+', line):
            chinese_detect = 'true'
            chinese_words_counter += 1
            #print "line:",n,line
    f.close()

    if chinese_detect.lower() in ['true']:
        print ' + [Chinese /',chinese_words_counter,'] ', filename
    else:
        print ' + [Chinese /',chinese_words_counter,'] ', filename


def scan_file(path):
    #print "Current Path: " + path
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
                        do_scan_chinese(file)
            except:
                continue


def main():
  opt=argparse.ArgumentParser(description="::::: Chinese Words Scanner :::::")
  opt.add_argument("scan_path", help="ex) /path_to_scan")
  opt.add_argument("-p", "--path", action="store_true", dest="path", help="ex) python chinese_words_scan_v0.1.py -p /path_to_scan")

  if len(sys.argv)<=2:
    opt.print_help()
    sys.exit(1)

  options= opt.parse_args()

  if options.path:
      path = (options.scan_path)
      scan_file(path)

  else:
      opt.print_help()
      sys.exit()


if __name__ == '__main__':
    main()
