#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt


class SGD:

    def __init__(self, lr=0.95):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0*y


init_pos = (-7.0, 2.0)
params = {}
params['x'], params['y'] = init_pos[0], init_pos[1]
grads = {}
grads['x'], grads['y'] = 0, 0


x_history = []
y_history = []
optimizer = SGD()

for i in range(30):
    x_history.append(params['x'])
    y_history.append(params['y'])
    grads['x'], grads['y'] = df(params['x'], params['y'])
    optimizer.update(params, grads)

x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
mask = X > 7
Z[mask] = 0

plt.plot(x_history, y_history, 'o-', color='red')
plt.contour(X, Y, Z)
plt.ylim(-5, 5)
plt.xlim(-5, 5)
plt.plot(0, 0, '+')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
