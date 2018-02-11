# _*_ coding: utf-8 _*_
import ctypes
import time
from datetime import datetime
import math
import argparse


# dll library load
user32 = ctypes.windll.user32


def set_start_time():
    start_time = time.time()
    start_time_now = datetime.now().strftime('%Y%m%d-%H%M%S')
    print('\nstart:', start_time_now)

    return start_time


def set_end_time():
    end_time = time.time()
    end_time_now = datetime.now().strftime('%Y%m%d-%H%M%S')
    print('\nend:', end_time_now)

    return end_time


def calc_total_time(start, end):
    total_time = end - start 
    print('total:', total_time)


def main(t):
    # settings start time
    start_time = set_start_time()

    # measure time and stdout time in progress bar
    bar_range = 50
    progress_bar = "\r>>{0}/{1} [{2}]"
    for i in range(t):
        bar = "#" * math.ceil(i / (t / bar_range)) \
          + " " * math.ceil((t-i) / (t/bar_range))
        print(progress_bar.format(i, t, bar), end="")
        time.sleep(1)

    # setting and time and calc total time
    end_time = set_end_time()
    calc_total_time = (start_time, end_time)

    # popup message
    user32.MessageBoxA(0,
                       "finish",
                       "popup timer",
                       0x00000040
    )


if __name__ == '__main__':
    # settings args
    parser = argparse.ArgumentParser(
        description='pass setting time by seconds(int)'
    )
    parser.add_argument('time',
                        nargs=1,
                        default=None,
                        type=int,
                        help='example: python popup.py 300(5minutes)')
    args = parser.parse_args()

    # main
    main(args.time[0])

















