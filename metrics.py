#!/usr/bin/python3

#psutil and sys modules import
import psutil
import sys

try:

    #CPU stats are printed if only: 1 extra parameter is passed; the parameter name equeils to 'cpu' 
    if sys.argv[1] == "cpu" and len(sys.argv) == 2: 
        print(psutil.cpu_times())
    
    #Memory stats are printed if only: 1 extra parameter is passed; the parameter name equeils to 'memory' 
    elif  sys.argv[1] == "mem" and len(sys.argv) == 2: 
        print(psutil.virtual_memory())
    
    #Information message to printed in other case
    else:
        print("Please, use 'cpu' or 'mem' system arguments.")

#An exception to hanlde an empty argument 
except IndexError:
        print("Please, use 'cpu' or 'mem' system arguments.")