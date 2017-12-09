from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# read image as array
im = np.array(Image.open('empire.jpg').convert('L'))

# make new figure
plt.figure()

# without color
plt.gray()

# display contour as upper left is (0,0)

# contour
plt.contour(im, origin='image')
plt.axis('equal')
plt.axis('off')
plt.savefig('contour.jpg')
plt.show()

# histgram
plt.figure()
plt.hist(im.flatten(),128)
plt.savefig('histgram.jpg')
plt.show()

