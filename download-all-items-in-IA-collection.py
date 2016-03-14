## Updated by Robert Orr, 2016-Mar-14 - apparently the IA api changed!

## Original code from :
## Robin Camille Davis
## March 24, 2014
## downloads all items in a given Internet Archive collection
## !! will probably crash after 10 or so items !! feel free to edit the script to make it better for bigger collections
## See http://programminghistorian.org/lessons/data-mining-the-internet-archive for more detailed info
import os
import internetarchive as ia
from internetarchive.session import ArchiveSession
from internetarchive import get_item
from internetarchive import download
s = ArchiveSession()
coll = ia.Search(s, 'collection:xxxxxxxx') #fill this in -- searches for the ID of a collection in IA
## example of collection page: https://archive.org/details/johnjaycollegeofcriminaljustice
## the collection ID for that page is johnjaycollegeofcriminaljustice
## you can tell a page is a collection if it has a 'Spotlight Item' on the left

num = 0

for result in coll: #for all items in a collection
    num = num + 1 #item count
    itemid = result['identifier']
    print 'Downloading: #' + str(num) + '\t' + itemid
    try:
	download(itemid) 
        print '\t\t Download success.'
    except Exception , e:
        print "Error Occurred downloading () = {}".format(itemid, e) 
    print 'Pausing for 40 minutes'
    time.sleep(2400) # IA restricts the number of things you can download. Be nice to 
                     # their servers -- limit how much you download, too. For me, this
                     # time restriction is still not polite enough, and my connection gets
                     # cut off all the dang time.
    
    
    
