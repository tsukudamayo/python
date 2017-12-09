import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters
from PIL import Image

im = np.array(Image.open('empire.jpg').convert('L'))

# x 
imx = np.zeros(im.shape)
filters.sobel(im, 1, imx)
plt.imshow(imx)
plt.savefig('sobel_diff_x.jpg')
plt.show()

# gradient y
imy = np.zeros(im.shape)
filters.sobel(im, 0, imy)
plt.imshow(imy)
plt.savefig('sobel_diff_y.jpg')
plt.show()

magnitude = np.sqrt(imx**2 + imy**2)
plt.imshow(magnitude)
plt.savefig('sobel_gradient.jpg')
plt.show()
