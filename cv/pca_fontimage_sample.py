from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pca
import glob

# generate fontimage list
imlist = [r for r in glob.glob('./a_thumbs/*.jpg')]

im = np.array(Image.open(imlist[0]))    # open img
m, n = im.shape[0:2]                    # get size of img
imnbr = len(imlist)                     # get number of pixel

# generate metrics which heve all normalized image
immatrix = np.array(\
        [np.array(Image.open(im)).flatten() for im in imlist]\
        , 'f')

# exec pca
V, S, immean = pca.pca(immatrix)

# show image
fig = plt.figure()
plt.gray()
plt.subplot(2,4,1)
plt.imshow(immean.reshape(m, n))
for i in range(7):
    plt.subplot(2, 4, i+2)
    plt.imshow(V[i].reshape(m,n))
fig.savefig('pca_fontimage.jpg')
plt.show()
