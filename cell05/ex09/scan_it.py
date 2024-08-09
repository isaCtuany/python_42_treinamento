#!/usr/bin/python3 

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    procure_string = sys.argv[2]
    procurar = re.findall(keyword, procure_string)
    print(len(procurar))

    #Poderia colocar os argumentos diretamente no re.findall