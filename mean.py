#!/usr/bin/env python
import sys
import numpy as np

std_array = [float(line) for line in sys.stdin.readlines()]

print(np.mean(std_array))
