import os
import numpy as np
from PIL import Image

def get_imlist(path):

    """ return lists of filename all jpg file in specified directory """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]

def imresize(im ,sz):

    """ change size array of image via PIL """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):

    """ do normalization histgram of grayscale image """
    imhist,bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1] # normalization

    """ get new pixel value interpolated by linear """
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf
    

def compute_average(imlist):

    """ calucurate average arrays of image file """
    averageim = np.array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += np.array(Image.open(imname))
        except:
            print(imname + '...skippeed')
    
    averageim /= len(imlist)

    return np.array(averageim, 'uint8')
