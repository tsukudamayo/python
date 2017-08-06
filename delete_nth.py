import sys
from collections import deque

def delete_nth(d, n):
    d = deque(d)
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
    
    return d


if __name__ == '__main__':
    _input = sys.argv[1]
    nth = int(sys.argv[2])
    print(delete_nth(_input, nth))

