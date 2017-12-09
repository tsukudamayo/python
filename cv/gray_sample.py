from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('empire.jpg').convert('L')
plt.imshow(im)
plt.show()
