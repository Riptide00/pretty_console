"""Hide/ show cursor on Windows."""
import ctypes


class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]


def hide():
    """Hide cursor."""
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


def show():
    """Show cursor."""
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = True
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


def set(x, y):
    """Set cursor position."""
    return "\033[" + str(y) + ";" + str(x) + "H"
