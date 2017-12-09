from PIL import Image

pil_im = Image.open('empire.jpg')
rotate_out = pil_im.rotate(45)
rotate_out.save('rotate_45.jpg')
