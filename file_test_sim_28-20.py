import os
import sys
import glob

logfiles = [ '\*sdte_mram_log*', '\*sdte_backup_log*', '\*boom_norflash_log*',
            '\*gps_mram_log*', '\*gps_norflash_log*',
            '\*safea_mram_log*', '\*safea_norflash_log*',
            '\*safeb_mram_log*', '\*safeb_norflash_log*',
            '\*smbc_mram_log*', '\*smbc_norflash_log*',
            '\*boom_mram_log*', '\*boom_norflash_log*',
            '\*smbc_log_motor*'
            ]

print(os.listdir(sys.argv[1]))


for logfile in logfiles:
    result = glob.glob(sys.argv[1] + logfile)
    if result == []:
        print(logfile + 'NG')
    else:
        print(logfile + 'OK')
    print(result)
