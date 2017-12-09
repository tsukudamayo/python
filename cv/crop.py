from PIL import Image

pil_im = Image.open('empire.jpg')

box = (100, 100, 400, 400)
region = pil_im.crop(box)
region.save('crop.jpg')
