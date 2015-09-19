#!/usr/bin/env python

import internetarchive
import os
import time

base_path = '/Users/wcm1/programming/abolitionist-letters/'
error_log = open(base_path + 'bpl-marcs-errors.log', 'a')
marcs_dir = base_path + 'marc'

# Here we're going to download the MARC XML file for all of the letters
# in the `bplscas` collection using the internetarchive Python module.
# For more info see https://pypi.python.org/pypi/internetarchive/0.4.3

search = internetarchive.search_items('collection:bplscas')

print "There are " + str(search.num_found) + " items in the collection."

for result in search:
    itemid = result['identifier']
    if itemid.count('letter') > 0 and not os.path.isfile(marcs_dir + itemid + '_marc.xml'):
        time.sleep(1)
        item = internetarchive.get_item(itemid)
        marc = item.get_file(itemid + '_marc.xml')
        try:
            marc.download(marcs_dir + itemid + '_marc.xml')
        except Exception as e:
            error_log.write('Could not download ' + itemid + ': %s\n' % e)
        else:
            print "Downloading " + itemid + " ..."
