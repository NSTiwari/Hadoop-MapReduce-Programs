#!/usr/bin/python

import sys

cur_node = None
prev_node = None
contrib_sum = 0
damping_factor = 0.85

for line in sys.stdin:
   cur_node, contrib = line.strip().split(',')
   print("\nCurrent node: %s\nContribution by this node: %s" % (cur_node, contrib))

   if cur_node == prev_node:
      contrib_sum += float(contrib)
   else:
      if prev_node:
         new_pr = (1 - damping_factor) + (damping_factor * contrib_sum)
         new_pr = round(new_pr, 5)
         print("Previous node: %s\nNew page rank of node %s: %s" % (prev_node, cur_node, new_pr))

      prev_node = cur_node
      contrib_sum = float(contrib)

if cur_node == prev_node:
   new_pr = (1 - damping_factor) + (damping_factor * contrib_sum)
   new_pr = round(new_pr, 5)
   print("Previous node: %s\nNew page rank of node %s: %s" % (prev_node, cur_node, new_pr))



