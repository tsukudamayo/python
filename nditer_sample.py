import numpy as np

sample = np.random.rand(2,2,3)
print(sample)

nditer = np.nditer(sample, flags=['multi_index'])
while not nditer.finished:
    print(nditer.multi_index)
    print(sample[nditer.multi_index])
    nditer.iternext()
