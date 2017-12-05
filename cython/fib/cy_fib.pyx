#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import time

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


if __name__ == '__main__':
    start_time = time.time()
    calc = fib(10000000000)
    exec_time = time.time() - start_time
    print("time : %d" % exec_time)
