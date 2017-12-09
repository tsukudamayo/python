from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

im = np.array(Image.open('empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 5)
plt.imshow(im)
plt.savefig('gaussian_filter_before.jpg')
plt.show()
plt.imshow(im2)
plt.savefig('gaussian_filter_after.jpg')
plt.show()
