"""
output memory-usage log

summery
---------------------------------------
line[0]: date(%Y-%m-%d)
line[1]: time(%H:%M:%S)
line[2]: memory-usage-percent(%)
line[3]: memory-usage-total(byte)
line[4]: memory-usage-used(byte)
line[5]: memory-usage-free(byte)
line[6]: memory-usage-available(byte)
---------------------------------------
"""

import os,sys
import time
from datetime import datetime
import psutil

# get timestamp
start_time = datetime.now()
# get home directory
home = os.environ['HOMEPATH']
# make logfile
logfile = open(str(home) + '\\var\\log\\perf\\resource\\memory_usage_' + str(start_time.strftime('%Y%m%d')) + '.log', 'a')

# keep on outputting logfile, until pressed ctrl+C
while(True):
    try:
        now = datetime.now()
        mem = psutil.virtual_memory()
        log = str(now.strftime('%Y-%m-%d')) + ',' + \
              str(now.strftime('%H:%M:%S')) + ',' + \
              str(mem.percent) + ',' + \
              str(mem.total) + ',' + \
              str(mem.used) + ',' +  \
              str(mem.free) + ',' + \
              str(mem.available)
        print(log)
        logfile.write(log)
        logfile.write('\n')
        time.sleep(1)
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
