from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = np.array(Image.open('empire.jpg'))
plt.imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plt.plot(x, y, 'r*')
plt.plot(x[:2], y[:2])
plt.axis('off')
plt.title('Plotting: "empire.jpg"')
plt.savefig('plot2img_axis-off.jpg')
plt.show()
