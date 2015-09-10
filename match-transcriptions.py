#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The following code won't be generally useful. It's basically a method
# I devised to see if the notes I took at the BPL contain a transcription
# of an item that has been uploaded to the Internet Archive

import os
import pymarc
import csv

base_path = '/Users/wcm1/programming/abolitionist-letters/'
path_to_marcs = base_path + 'marc/'
path_to_transcripts = base_path + 'transcriptions/'

csv_file = open(base_path + 'matches.csv', 'wb')
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

matches = 0
doubles = 0

def strip_call_no(callno):
    # return filter(str.isdigit, callno)
    return str(callno.translate(None, ' MsSvoln,p()'))

def make_url(marcfile):
    return 'http://archive.org/details/' + marcfile.split('_')[0]

def get_call_no(record):
    global tempcall
    try:
       tempcall = strip_call_no(str(record['099']['a']))
    except Exception as e:
       return e

def check_call_no(record):
    global matches
    global doubles
    try: 
       callno = strip_call_no(str(record['099']['a']))
       if callno in s:
          doubles += 1
       elif callno in l:
          matches += 1
          csv_writer.writerow([d[callno], make_url(fd[callno])])
       else:
	      pass
    except Exception as e:
       print e

# List of transcript filenames with everything but digits stripped from names
l = [strip_call_no(f) for f in os.listdir(path_to_transcripts) if f.startswith('Ms')]

# Set of duplicates found in the above list
s = set([x for x in l if l.count(x) > 1])

# Dictionary mapping digit-only transcript filename to full filename (if not a duplicate)
d = {strip_call_no(f): f for f in os.listdir(path_to_transcripts) if f.startswith('Ms') and strip_call_no(f) not in s}

# Dictionary mapping digit-only MARC Call No. to MARC filename.
fd = {}

tempcall = ''

print 'Looking for matching transcription files ...'

for file in os.listdir(path_to_marcs):
    if file.endswith('.xml'):
        pymarc.map_xml(get_call_no, path_to_marcs + file)
        fd[tempcall] = file
        pymarc.map_xml(check_call_no, path_to_marcs + file)

print 'There are '  + str(matches) + ' matching records.'
print 'There are ' + str(doubles) + ' records with potential matches.'

csv_file.close()
