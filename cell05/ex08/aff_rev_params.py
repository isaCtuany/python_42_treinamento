#!/usr/bin/python3 

import sys

if len(sys.argv) < 3:
    print("none")
else:
  for element in reversed(sys.argv[1:]):
     print (element)