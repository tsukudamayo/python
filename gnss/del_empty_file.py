import os.path, glob

for f in glob.glob("./*.log"):
    if os.path.getsize(f) == 0:
        os.remove(f)
