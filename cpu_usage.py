"""
output cpu-usage log

summery
---------------------------------------
line[0]: date(%Y-%m-%d)
line[1]: time(%H:%M:%S)
line[2]: cpu-usage-percent(%)
---------------------------------------
"""

import os,sys
from datetime import datetime
import psutil

# get timestamp
start_time = datetime.now()
# get home_directory
home = os.environ['HOME']
# make logfile
logfile = open(str(home) + '\\var\\log\\perf\\resource\\cpu_usage_' + str(start_time.strftime('%Y%m%d')) + '.log', 'a')

# keep on that output logfile, until press ctrl+C
while(True):
    try:
        now = datetime.now()
        log = str(now.strftime('%Y-%m-%d')) + ',' + \
              str(now.strftime('%H:%M:%S')) + ',' + \
              str(psutil.cpu_percent(interval=1))
        print(log)
        logfile.write(log)
        logfile.write('\n')
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
