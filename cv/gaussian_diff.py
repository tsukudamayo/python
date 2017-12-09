import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters
from PIL import Image

im = np.array(Image.open('empire.jpg').convert('L'))

sigma = 5 # standard debiation

imx = np.zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)
plt.imshow(imx)
plt.savefig('gaussian_filter_diff_x.jpg')
plt.show()

imy = np.zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (0,1), imy)
plt.imshow(imy)
plt.savefig('gaussian_filter_diff_y.jpg')
plt.show()

magnitude = (imx**2 + imy**2)
plt.imshow(magnitude)
plt.savefig('gaussian_filter_gradient.jpg')
plt.show()
