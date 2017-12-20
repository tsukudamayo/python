# _*_ coding: utf-8 _*_
"""
Norm is the quantity which expresses "size" of various things.
for example norm of 2-dimentional vector expresses "length"
"""
import numpy as np

a = np.array([1, 1])
sample1 = np.linalg.norm(a)
print('test data : a =', a)
print('np.linalg.norm(a) :', sample1)
