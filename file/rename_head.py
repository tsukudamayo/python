import os
import glob

files = glob.glob("*.log")
for file in files:
    oldname = file
    newname = '20160917_gnss' + file
    os.rename(oldname,newname)
