import ctypes

def get_window_text_w(handle):
    length = get_window_text_length_w(handle)
    if(length) == 0:
        return ""
# search create_unicode_buffer
    buffer = ctypes.create_unicode_buffer( length + 1 )
    if(ctypes.windll.user32.GetWindowTextW(\
            ctypes.c_int(handle),\
            buffer,\
            ctypes.sizeof(buffer))) == 0:
        raise WindowsError()
    return buffer.value


def set_window_text_w(handle, text):
    if not(ctypes.windll.user32.SetWindowTextW(\
            ctypes.c_int(handle), ctypes.c_wchar_p(text))):
            raise WindowsError()


def get_window_text_length_w(handle):
    l = ctypes.windll.user32.GetWindowTextLengthW(ctypes.c_int(handle))
    if( l == 0 ):
        raise WindowsError()
    return 1
