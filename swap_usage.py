"""
output swap memory-usage log

summery
---------------------------------------
line[0]: date(%Y-%m-%d)
line[1]: time(%H:%M:%S)
line[2]: swap memory-usage-percent(%)
line[3]: swap memory-usage-total(byte)
line[4]: swap memory-usage-used(byte)
line[5]: swap memory-usage-free(byte)
line[6]: swap memory-usage-sin(byte)
line[7]: swap memory-usage-sout(byte)
---------------------------------------
"""

import os,sys
import time
from datetime import datetime
import psutil

# get timestamp
start_time = datetime.now()
# get home directory
home = os.environ['HOME']
# make logfile
logfile = open(str(home) + '\\var\\log\\perf\\resource\\swap_usage_' + str(start_time.strftime('%Y%m%d')) + '.log', 'a')

# keep on outputtnig logfile, until pressed ctrl+C
while(True):
    try:
        now = datetime.now()
        mem = psutil.swap_memory()
        log = str(now.strftime('%Y-%m-%d')) + ',' + \
              str(now.strftime('%H:%M:%S')) + ',' + \
              str(mem.percent) + ',' + \
              str(mem.total) + ',' + \
              str(mem.used) + ',' +  \
              str(mem.free) + ',' + \
              str(mem.sin) + ',' + \
              str(mem.sout)
        print(log)
        logfile.write(log)
        logfile.write('\n')
        time.sleep(1)
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
