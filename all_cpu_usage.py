import sys
from datetime import datetime
import psutil

start_time = datetime.now()
logfile = open('C:\\Users\\lx15120118\\var\\log\\sim\\perf\\resource\\cpu _usage_' + str(start_time.strftime('%Y%m%d_%H%M%S')) + '.log', 'a')

while(True):
    try:
        now = datetime.now()
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        log = str(now.strftime('%Y-%m-%d')) + ',' + str(now.strftime('%H:%M:%S')) + ',' + str(cpu_usage[0]) + ',' + str(cpu_usage[1]) + ',' + str(cpu_usage[2]) + ',' + str(cpu_usage[3])
        print(log)
        logfile.write(log)
        logfile.write('\n')
    except KeyboardInterrupt:
        logfile.close()
        sys.exit()
