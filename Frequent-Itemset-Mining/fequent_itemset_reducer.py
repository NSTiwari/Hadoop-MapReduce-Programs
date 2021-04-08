#!/usr/bin/env python

import sys
item1 = None
item2 = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	key1, key2, count = line.split('\t', 2)
	#print(key1, key2, count)

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, ignore
		continue

	if item1 == key1 and item2 == key2:
		current_count += count
	else:
		if item1!=None and item2!=None and current_count>=2: 
			# output as a frequent 2 itemset if support>2
			print('%s\t%s' % (item1, item2))
		current_count = count
		item1 = key1
		item2 = key2

# last itemset
if item1 == key1 and item2 == key2 and current_count>=2:
	print('%s\t%s' % (item1, item2))