import codecs
import re
import sys

with codecs.open(sys.argv[1] + '.log', 'r', 'Shift-JIS', 'ignore') as ld:
    lines = ld.readlines()
ld.close()

f = open(sys.argv[1] + '_del_cs.log', 'w')
for line in lines:
    if line.find('*') >= 0:
        r = re.compile("(.*)(\*)(.*)")
        m = r.match(line)
        f.write(m.group(1))
        f.write('\n')
