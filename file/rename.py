import os
import glob

files = glob.glob("*.log")
for oldname in files:
    newname = oldname.replace('_','')
    os.rename(oldname,newname)
