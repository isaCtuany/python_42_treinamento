#!/usr/bin/python3 

import sys

if len(sys.argv) != 2:
    print("none")
else:
    inserir_palavra = input("What was the parameter?")
    if inserir_palavra == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
    
    
    

        