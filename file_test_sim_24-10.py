import os
import sys
import glob

logfiles = [ '\*sdte.bin*', 
            '\*safea.bin*',
            '\*safeb.bin*',
            '\*smbc.bin*', 
            '\*boom.bin*' 
            ]

print(os.listdir(sys.argv[1]))


for logfile in logfiles:
    result = glob.glob(sys.argv[1] + logfile)
    if result == []:
        print(logfile + 'NG')
    else:
        print(logfile + 'OK')
    print(result)
