import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imsave
from scipy.ndimage import filters
from PIL import Image


def denoise(im, U_init, tolerance=0.1, tau=0.125, tv_weight=100):

    m, n = im.shape

    # init
    U = U_init
    Px = im
    Py = im
    error = 1

    while(error > tolerance):
        Uold = U

        # grad
        GradUx = np.roll(U, -1, axis=1) - U
        GradUy = np.roll(U, -1, axis=0) - U

        # update
        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = np.maximum(1, np.sqrt(PxNew**2 + PyNew**2))

        Px = PxNew/NormNew
        Py = PyNew/NormNew

        RxPx = np.roll(Px, 1, axis=1)
        RyPy = np.roll(Py, 1, axis=0)

        DivP = (Px - RxPx) + (Py-RyPy)

        U = im + tv_weight * DivP

        error = np.linalg.norm(U - Uold) / np.sqrt(n*m)

    return U, im - U


if __name__ == '__main__':
    
    im = np.zeros((500,500))
    im[100:400, 100:400] = 128
    im[200:300, 200:300] = 255
    im = im + 30 * np.random.standard_normal((500,500))
    plt.imshow(im)
    plt.show()

    U, T = denoise(im, im)
    G = filters.gaussian_filter(im, 10)
    plt.imshow(U)
    plt.show()
    plt.imshow(G)
    plt.show()

    imsave('synth_rof.pdf', U)
    imsave('symth_gaussian.pdf', G)

    im = np.array(Image.open('empire.jpg').convert('L'))
    U, T = denoise(im, im)
    fig = plt.figure()
    plt.gray()
    plt.imshow(U)
    plt.axis('equal')
    plt.axis('off')
    plt.show()



