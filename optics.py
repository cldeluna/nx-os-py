
#!/usr/bin/env python

import re
import sys

TX=0
SX=0
LH=0

file_name = sys.argv[1]
print file_name

show = open(file_name, "r")

for line in show:
    if re.match("(.*)connected(.*)",line):
		if re.match("(.*)1000BaseSX(.*)", line):
			print "match" + line
			SX=SX+1
			print "Number of SX Optics: " + str(SX)
		if re.match("(.*)1000BaseLH(.*)", line):
			print "match" + line
			LH=LH+1
			print "Number of LH Optics: " + str(LH)
		if re.match("(.*)1000BaseTX(.*)", line):
			print "match" + line
			TX=TX+1
			print "Number of TX Optics: " + str(TX)
print "*********************************"
print file_name			
print "Number of SX Optics: " + str(SX/3)
print "Number of LH Optics: " + str(LH/3)         
print "Number of TX Optics: " + str(TX)
