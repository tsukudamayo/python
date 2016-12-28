from PIL import ImageGrab
import sys
from datetime import datetime as dt
import time


def loop(times, sleep, x1, y1, x2, y2):

    now = dt.now()
    f_name = now.strftime('%Y%m%d_%H%M%S')
    
    for i in range(int(times)):
        im = ImageGrab.grab((int(x1),
                             int(y1),
                             int(x2), 
                             int(y2)))

        im.save('C:/Users/lx15120118/Pictures/' + str(f_name) + '_' + str('{0:04d}'.format(i)) + '.png')
        time.sleep(float(sleep))

