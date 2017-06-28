import sys
import time
from datetime import datetime
import psutil

start_time = datetime.now()
logfile = open('C:\\Users\\lx15120118\\var\\log\\sim\\perf\\resource\\swap_usage_' + str(start_time.strftime('%Y%m%d')) + '.log', 'a')

while(True):
    try:
        now = datetime.now()
        mem = psutil.swap_memory()
        log = str(now.strftime('%Y-%m-%d')) + ',' + str(now.strftime('%H:%M:%S')) + ',' + str(mem.percent) + ',' + str(mem.total) + ',' + str(mem.used) + ',' +  str(mem.free) + ',' + str(mem.sin) + ',' + str(mem.sout)
        print(log)
        logfile.write(log)
        logfile.write('\n')
        time.sleep(1)
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
