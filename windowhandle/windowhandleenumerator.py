import array
import ctypes

def enum_top_level_windows():
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(\
            ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not(ctypes.windll.user32.EnumWindows(\
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),\
            ctypes.py_object(handles))):
        raise WindowsError()
    return handles


def enum_child_windows(handle):
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(\
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not(ctypes.windll.user32.EnumChildWindows(\
            ctypes.c_uint(handle),\
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),\
            ctypes.py_object(handles))):
        raise WindowsError()
    return handles


def enum_thread_windows(handle):
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(\
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not(ctypes.windll.user32.EnumThreadWindows(\
            ctypes.c_uint32(thread_id),\
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),\
            ctypes.py_object(handles))):
        raise WindowsError()
    return handles


def _enumtopwindows_enumproc(handle, list):
    list.append(handle)
    return 1
