from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# read img as array
im = np.array(Image.open('empire.jpg'))

# display img
plt.imshow(im)

# position of point
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# plot as marking of star of red color
plt.plot(x,y, 'r*')

# plot between of two points
plt.plot(x[:2], y[:2])

# add title and, display result of plotting
plt.title('Plotting: "empire.jpg"')
plt.show()

