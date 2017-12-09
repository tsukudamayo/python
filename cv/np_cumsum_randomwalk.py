import numpy as np
import matplotlib.pyplot as plt

L = 1000
step = np.random.choice([-1,1], L)
position = np.cumsum(step)
plt.plot(position)
plt.savefig('np_cumsum_randomwalk.jpg')
plt.show()
