import os, sys
from PIL import Image

pictures = os.listdir(sys.argv[1])
print(pictures)

for i, picture in enumerate(pictures):
    Image.open(picture).resize((480, 360)).save(str(i) + '.png')
