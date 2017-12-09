import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# define filaname
BEFORE_IMG = 'histogram_flatten_before.jpg'
AFTER_IMG = 'histogram_flatten_after.jpg'

BEFORE_PLOT = 'histogram_flatten_before_plot.jpg'
BEFORE_BAR = 'histogram_flatten_before_bar.jpg'
AFTER_PLOT = 'histogram_flatten_after_plot.jpg'
AFTER_BAR = 'histogram_flatten_after_bar.jpg'

BEFORE_NORM = 'histogram_flatten_cumsum_before_norm.jpg'
AFTER_NORM = 'histogram_flatten_cumsum_after_norm.jpg'

# show plot bar
def hist_plot_show(bins, hist, plot_save_file, bar_save_file):
    plt.plot(bins, hist)
    plt.savefig(str(plot_save_file))
    plt.show()
    plt.bar(bins, hist)
    plt.savefig(str(bar_save_file))
    plt.show()


# show image
def img_show(im, filename):
    plt.imshow(im)
    plt.savefig(str(filename))
    plt.show()

# plot show
def plot_show(bins, hist, filename):
    plt.plot(bins, hist)
    plt.savefig(str(filename))
    plt.show()


if __name__ == '__main__':
    """ グレースケール画像のヒストグラム平坦化 """
    im = np.array(Image.open('empire.jpg').convert('L'), 'f')
    img_show(im, BEFORE_IMG)
    
    # 画像のヒストグラムを得る
    imhist, bins = np.histogram(\
            im.flatten(),\
            256,\
            normed=True)    # this keyword deplicated in numpy 1.6.0
    
    # 平坦化前
    print('plot before flatten')
    hist_plot_show(bins[:-1], imhist, BEFORE_PLOT, BEFORE_BAR)
    
    # 正規化前
    print('cunsum before nomarization')
    cdf = imhist.cumsum()   # cumulative distribution function
    plot_show(bins[:-1], cdf, BEFORE_NORM)
    
    # 正規化後
    cdf2 = 255 * cdf / cdf[-1]
    plot_show(bins[:-1], cdf2, AFTER_NORM)
    
    # cdfを線形補間し、新しいピクセル値とする
    im2 = np.interp(\
            im.flatten(),\
            bins[:-1],\
            cdf2)

    # 正規化後のデータをヒストグラムにする
    im2hist, bins2 = np.histogram(\
            im2,\
            256,\
            normed=True)
    # show plot and bar
    print('plot after flatten')
    hist_plot_show(bins2[:-1], im2hist, AFTER_PLOT, AFTER_BAR)
    
    # im2 conv 1-dimension to 2-dimention
    im2 = im2.reshape(im.shape)
    
    # plot after
    img_show(im2, AFTER_IMG)
