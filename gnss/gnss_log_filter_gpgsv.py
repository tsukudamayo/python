import sys,re

argvs = sys.argv
fnames = ['_1.log', '_2.log', '_3.log', '_4.log']
regexes = ["GPGSV,[0-9],1", "GPGSV,[0-9],2", "GPGSV,[0-9],3", "GPGSV,[0-9],4"]

ld = open(argvs[1], 'r')
lines = ld.readlines()
ld.close()

for fname, regex in zip(fnames, regexes):
    f = open(argvs[2] +str(fname), 'w')
    for line in lines:
        r = re.compile(regex)
        s = r.search(line)
        if s != None:
            f.write(line[:-1])
            f.write('\n')

