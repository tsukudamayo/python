from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = np.array(Image.open('empire.jpg').convert('L'))
im2 = 255 - im                  # incvert image
im3 = (100.0/255.0) * im + 100  # fit between 100 and 200
im4 = 255.0 * (im/255.0)**2     # 2乗する

# returning from a one-dimentional array to a two-dimensional array 
#_im = Image.fromarray(np.uint8(im))
#_im2 = Image.fromarray(np.uint8(im2))
_im3 = Image.fromarray(np.uint8(im3))
_im4 = Image.fromarray(np.uint8(im4))

ims = [_im, _im2, _im3, _im4]

# save image which conv graylevel
for idx, i in enumerate(ims):
    plt.imshow(i)
    plt.savefig('graylevel_sample_' + str(idx+1) + '.jpg')
    plt.show()

images = {
        'x' : im,
        '255 - x' : im2,
        '(100.0 / 255.9)*x + 100' : im3 ,
        '255.0 * ((x / 255.0) * (x/255.0)**2)' : im4
}

# print min value and max value that return from function
for e, v in images.items():
    print('f(x) = ' + e\
            + '\n min, max : ', int(v.min()), int(v.max()))

# x -> 0~255
x = np.arange(1,255)

# plot
plt.plot(x, x, label='f(x)=x')
plt.plot(x, (255 - x) , label='f(x)=255-x')
plt.plot(x, ((100.0 / 255.9)*x + 100), label='f(x)=(100.0/255.0)*x + 100')
plt.plot(x, (255.0 * ((x / 255.0) * (x/255.0)**2)) ,label='f(x)=255.0*(x/255.0)^2')
plt.legend()
plt.tight_layout()
plt.savefig('conv_greylevel.jpg')
plt.show()
