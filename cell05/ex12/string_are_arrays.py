#!/usr/bin/python3 

import sys
if len(sys.argv) != 2:
    print("none")
else:
    word = (sys.argv[1])
    for char in word:
        if char == 'z':
            print('z', end = "")
    print()

