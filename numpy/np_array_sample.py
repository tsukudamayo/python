# _*_ coding: utf-8 _*_
import numpy as np

# 1dim
a = np.arange(20, 0, -2)
sample1 = np.where(a < 10)
sample2 = a[np.where(a < 10)]

print("test data: ", a)
print("np.where(a < 10): ", sample1)
print("a[np.where(a < 10)]: ", sample2)

# 2dim
a = np.arange(12).reshape((3, 4))
sample3 = np.where(a % 2 == 0)

print("test data: \n", a)
print("get only even number")
print("np.where(a % 2 == 0): ", sample3)

# ternary operator
sample4 = np.where(a % 2 == 0, 'even', 'odd')

print("example ternary operator")
print("return even if even number")
print("return odd if odd number")
print("np.where(a % 2 == 0, 'even', 'odd'): ")
print(sample4)

# assign to element
b = np.reshape(a, (3,4))
c = b**2
sample5 = np.where(b % 2 == 0, b, c)

print("assign elements of c only with odd numbers")
print("c is: \n", c)
print("np.where(b % 2 == 0, b, c): \n", sample5)

# bloadcast
sample6 = np.where(b % 2 == 0, b, (1000, 8000, 6000, 4000))

print("  if an itrable value such as an array or tuple")
print("is specified as the last argument,")
print("  the value at index access when iterating is used")
print("np.where(b % 2 == 0, b, (1000, 8000, 6000, 4000)) :\n", sample6)

