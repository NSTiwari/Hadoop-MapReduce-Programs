#!/usr/bin/python
import sys

for line in sys.stdin:
   if line.startswith('#'):
      continue
   else:
      print("%s" % (",".join(line.strip().split())))
