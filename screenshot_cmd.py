from PIL import ImageGrab
import sys
from datetime import datetime as dt
import time


def loop():

    now = dt.now()
    f_name = now.strftime('%Y%m%d_%H%M%S')
    
    for i in range(int(sys.argv[1])):
        im = ImageGrab.grab((int(sys.argv[3]),
                             int(sys.argv[4]),
                             int(sys.argv[5]), 
                             int(sys.argv[6])))

        im.save('C:/Users/lx15120118/Pictures/' + str(f_name) + '_' + str('{0:04d}'.format(i)) + '.png')
        time.sleep(float(sys.argv[2]))


if __name__ == '__main__':
    loop()
