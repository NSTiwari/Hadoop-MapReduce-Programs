#!/usr/bin/python
  
from operator import itemgetter
import sys

maximum=0
M=0

for line in sys.stdin:
	num,binary,trailing_zero=line.split('\t')
	if int(maximum)<int(trailing_zero):
	    maximum=trailing_zero

M=2**int(maximum)
print("Maximum trailing zeros = %sApproximate unique data elements = %s" % (maximum, M))
