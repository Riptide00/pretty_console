"""Console size module."""
import struct
import os


def get_size():
    """Get console width and height."""
    try:
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass


def get_height():
    """Get console height."""
    x, y = get_size()
    return y


def get_width():
    """Get console width."""
    x, y = get_size()
    return x


def set(x, y):
    """Set console width and height."""
    os.system("mode con: cols=" + str(x) + "lines=" + str(y)


def set_width(x):
    """Set console width."""
    os.system("mode con: cols=" + str(x))


def set_height(y):
    """Set console height."""
    os.system("mode con: lines=" + y)

if __name__ == '__main__':
    while True:
        print("Height: " + str(get_height()) + " " +
              "Width: " + str(get_width()) + "\r")
