"""
output cpu-usage(include logical core) log

this program is written for 2Core CPU(logical 4Core)
if target PC is not 2Core CPU, variable "log" is need to be fixed

summery
---------------------------------------
line[0]: date(%Y-%m-%d)
line[1]: time(%H:%M:%S)
line[2]: cpu1-usage-percent(%)
line[3]: cpu2(logical1)-usage-total(%)
line[4]: cpu3-usage-used(%)
line[5]: cpu4(logical2)-usage-free(%)
---------------------------------------
"""

import os,sys
from datetime import datetime
import psutil

# get timestamp
start_time = datetime.now()
# get home directory
home = os.environ['HOME']
# make logfile
logfile = open(str(home) + '\\var\\log\\perf\\resource\\cpu _usage_all_' + str(start_time.strftime('%Y%m%d')) + '.log', 'a')

# keep on output logfile, until press ctrl+C
while(True):
    try:
        now = datetime.now()
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        log = str(now.strftime('%Y-%m-%d')) + ',' + \
              str(now.strftime('%H:%M:%S')) + ',' + \
              str(cpu_usage[0]) + ',' + \
              str(cpu_usage[1]) + ',' + \
              str(cpu_usage[2]) + ',' + \
              str(cpu_usage[3])
        print(log)
        logfile.write(log)
        logfile.write('\n')
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
