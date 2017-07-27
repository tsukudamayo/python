import windowhandleenumerator
import windowtext

if __name__ == '__main__':
    handles = windowhandleenumerator.enum_top_level_windows()
    for handle in handles:
        print("\"{text}\" ({handle:0>8x})".format(\
                handle=handle,\
                text=windowtext.get_window_text_length_w(handle)))
