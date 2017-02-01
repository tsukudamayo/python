import os, sys
from PIL import Image

pictures = os.listdir(sys.argv[1])
print(pictures)

for i, picture in enumerate(pictures):
    Image.open(str(sys.argv[1]) + '\\' + str(picture)).resize((480, 360)).save(str(sys.argv[1]) + '\\' + str(i) + '.png')
