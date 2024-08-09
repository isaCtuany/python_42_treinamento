#!/usr/bin/python3 
import sys
if len(sys.argv) > 1:
    print("None")
else:
    k = 0
    while k < 11:
        print(f"Table de {k}:", end = "")
        i = 0
        while i < 11:
            result = k * i
            print(f" {result}", end = "")
            i += 1
        k += 1
        print()
