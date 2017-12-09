from PIL import Image

pil_im = Image.open('empire.jpg')
resize_out = pil_im.resize((128, 128))
resize_out.save('resize.jpg')
