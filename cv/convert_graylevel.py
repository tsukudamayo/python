from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# FIXME
# cannot convert gray 
im = np.array(Image.open('empire.jpg').convert('L'))
print("default: ", int(im.min()), int(im.max())) 

# reverse image
im2 = 255 - im
print("reverse image: ", int(im2.min()), int(im2.max())) 

# compress to a value between 100 and 200
im3 = (100.0 / 255) * im + 100
print("compress to a value between 100 and 200: ", int(im3.min()), int(im3.max())) 

# square values
im4 = 255.0 * (im/255.0)**2
print("square values: ", int(im4.min()), int(im4.max())) 

# show image
pil_im = Image.fromarray(im)
plt.imshow(pil_im)
plt.show()

pil_im2 = Image.fromarray(im2)
plt.imshow(pil_im2)
plt.show()

pil_im3 = Image.fromarray(np.uint8(im3))
plt.imshow(pil_im3)
plt.show()

pil_im4 = Image.fromarray(np.uint8(im4))
plt.imshow(pil_im4)
plt.show()
