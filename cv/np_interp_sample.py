import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10)     # x は 0~(2x(3.14)x10)までの10点
y = np.sin(x)                       # y = sin(x)

xvals = np.linspace(0, 2*np.pi, 50) # xよりさらに細かく50点
yinterp = np.interp(xvals, x, y)    # x,yについて50点で線形補間

plt.plot(x, y, 'o')                 # x,yを点でプロット
plt.plot(xvals, yinterp, '-x')      # 線形補間の区間をXと線でプロット
plt.savefig('np_interp_sample.jpg')
plt.show()
