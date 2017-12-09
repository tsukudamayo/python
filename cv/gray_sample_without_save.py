from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('AquaTermi_lowcontrast.jpg').convert('L')
plt.imshow(im)
plt.show()
