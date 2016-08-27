"""Functions for text in terminals!."""
import consolesize
import colorama


def set_color(color):
    """Set text color."""
    if color == "BLACK":
        return colorama.Back.BLACK + colorama.Fore.WHITE
    elif color == "RED":
        return colorama.Back.RED + colorama.Fore.WHITE
    elif color == "GREEN":
        return colorama.Back.GREEN + colorama.Fore.WHITE
    elif color == "YELLOW":
        return colorama.Back.YELLOW + colorama.Fore.BLACK
    elif color == "BLUE":
        return colorama.Back.BLUE + colorama.Fore.WHITE
    elif color == "MAGENTA":
        return colorama.Back.MAGENTA + colorama.Fore.WHITE
    elif color == "CYAN":
        return colorama.Back.CYAN + colorama.Fore.BLACK
    elif color == "WHITE":
        return colorama.Back.WHITE + colorama.Fore.BLACK
    else:
        return colorama.Back.BLACK + colorama.Fore.WHITE


def center(text):
        """Center text."""
        padding = (_width() / 2) - (len(text) / 2)
        padding = int(padding)
        s = " "
        for x in range(0, padding):
            s += " "
        s += text
        return s


def _width():
    x, y = consolesize.get_size()
    return x


def _main():
    print(center("Centered text."))

if __name__ == '__main__':
    _main()
