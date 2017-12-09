import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import measurements, morphology

im = np.array(Image.open('houses.png').convert('L'))
plt.imshow(im)
plt.show()
im = 1 * (im<128)

labels, nbr_objects = measurements.label(im)
print('Number of objects: ', nbr_objects)
