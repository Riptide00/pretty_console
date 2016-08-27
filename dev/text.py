"""Functions for text in terminals!."""
import consolesize
import colorama


def color(color, text):
    """Set text color."""
    color = color.upper()
    if color == "BLACK":
        return (colorama.Back.BLACK + colorama.Fore.WHITE + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "RED":
        return (colorama.Back.RED + colorama.Fore.WHITE + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "GREEN":
        return (colorama.Back.GREEN + colorama.Fore.WHITE + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "YELLOW":
        return (colorama.Back.YELLOW + colorama.Fore.BLACK + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "BLUE":
        return (colorama.Back.BLUE + colorama.Fore.WHITE + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "MAGENTA":
        return (colorama.Back.MAGENTA + colorama.Fore.WHITE + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "CYAN":
        return (colorama.Back.CYAN + colorama.Fore.BLACK + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    elif color == "WHITE":
        return (colorama.Back.WHITE + colorama.Fore.BLACK + text +
                colorama.Back.BLACK + colorama.Fore.WHITE)
    else:
        return(colorama.Back.BLACK + colorama.Fore.WHITE + text +
               colorama.Back.BLACK + colorama.Fore.WHITE)


def center(text):
        """Center text."""
        padding = (consolesize.width() / 2) - (len(text) / 2)
        padding = int(padding)
        s = " " * padding
        s += text
        s += " " * padding
        return s


def main():
    """Example."""
    print(color("Red",
                center("Centered text.")))

if __name__ == '__main__':
    main()
