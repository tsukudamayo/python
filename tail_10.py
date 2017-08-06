import sys
from collections import deque

def tail(filename, n=10):
    return deque(open(filename), n)

if __name__ == '__main__':
    filename = str(sys.argv[1])
    print(tail(filename))
