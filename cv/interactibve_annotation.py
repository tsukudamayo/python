from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = np.array(Image.open('empire.jpg'))
plt.imshow(im)
print('click 3 points')
x = plt.ginput(3)
print('result click:', x)
plt.show()
