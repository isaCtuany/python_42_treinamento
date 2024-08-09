#!/usr/bin/python3 

import sys
if len(sys.argv) != 3:
    print("none")
else:
    lista = list(range(int(sys.argv[1]),int(sys.argv[2])+1))
    print(lista)
