#!/usr/bin/python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys

number={}
hash_values = {}
binary={}
trailing_zero={}
count=0

def trailing(s):
    return len(s) - len(s.rstrip('0'))

for line in sys.stdin:
	temp = 0
	number[count] = int(line)
	hash_values[count] = ((6 + number[count])) % 32
	binary[count]=bin(hash_values[count])[2:]
	trailing_zero[count]=int(trailing(str(binary[count])))
	print("%s\t%s\t%s" % (number[count], binary[count], trailing_zero[count])) 
	count = count + 1
