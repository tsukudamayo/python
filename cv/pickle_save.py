from PIL import Image
import numpy as np
import pca
import glob
import pickle

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

# open file and save
with open('font_pca_model.pkl', 'wb') as f:
    pickle.dump(immean, f)
    pickle.dump(V,f)
