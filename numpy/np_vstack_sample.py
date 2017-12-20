# _*_ coding: utf-8 _*_
import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print("test data1 :", a)
print("test data2 :", b)

sample1 = np.vstack((a, b))
print("np.vstack((a, b)) :\n",sample1)


a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
print("test data1 :\n", a)
print("test data2 :\n", b)

sample2 = np.vstack((a, b))
print("np.vstack((a, b)) :\n",sample2)
