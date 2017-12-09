from PIL import Image

pil_im = Image.open('empire.jpg').convert('L').save('empire_convert_L.jpg')
