"""Center text in terminals!."""
import pretty_console.consolesize as consolesize


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
    x, y = consolesize.get_console_size()
    return x


def _main():
    print(center("Centered text."))

if __name__ == '__main__':
    _main()
