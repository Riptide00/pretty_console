"""Pretty console for Windows."""
import colorama
import _thread
import os
try:
    import pretty_console.consolesize as consolesize
    import pretty_console.cursor as cursor
except:
    import consolesize
    import cursor


class Console(object):
    """Console."""

    def __init__(self,
                 title='',
                 color="WHITE",
                 ps1=' > '):
        """Initiation."""
        super(Console, self).__init__()
        self.color = color.upper()
        self.title = title
        self.ps1 = ps1
        self.console_buffer = list()
        colorama.init()
        cursor.hide()

    def gui(self):
        """Spa."""
        self._update()
        _thread.start_new_thread(self._detect_change, ())

    def out(self, output):
        """Console io should be directed here."""
        self.console_buffer.append(output)
        self._update_console_out()

    def clear(self):
        """Clear console."""
        self.console_buffer = list()
        self._update_console_out()

    def _detect_change(self):
        w, h = consolesize.get_console_size()
        while True:
            if w is not self._get_width() or h is not self._get_height():
                w = self._get_width()
                h = self._get_height()
                self._update()

    def _update(self):
        os.system('cls')
        self._update_title_bar()
        self._update_console_out()

    def _update_console_out(self):
        cursor.hide()
        w, h = consolesize.get_console_size()
        for b in range(0, h - 7):
            print(self._get_color("BLACK") +
                  self._set_cursor(1, 3 + b) + (" " * w))
        rang = self.console_buffer[-(self._get_height() - 8):]
        blob = "\n".join(rang)
        print(self._set_cursor(1, 4) +
              self._get_color("BLACK") +
              blob)
        cursor.show()

    def _update_title_bar(self):
        cursor.hide()
        padding = int((self._get_width() / 2) - (len(self.title) / 2))
        s = (self._get_color(self.color) +
             self._set_cursor(1, 1) +
             (" " * padding) +
             self.title +
             (" " * padding))
        print(s)
        cursor.show()

    def get_input(self):
        """Return user input."""
        cursor.show()
        h = self._get_height()
        c = input(self._get_color("BLACK") +
                  self._set_cursor(1, (h - 3)) +
                  "_" * self._get_width() + '\n' + self.ps1)
        cursor.hide()
        print(self._get_color("BLACK") +
              self._set_cursor(1, (h - 3)) +
              " " * self._get_width() + '\n' +
              " " * (len(c) + 3))
        return c

    def set_title(self, title):
        """Set a new title."""
        self.title = title
        self._update_title_bar()

    def set_color(self, color):
        """Set a new color."""
        self.color = color.upper()
        self._update_title_bar()

    def _set_cursor(self, x, y):
        return "\033[" + str(y) + ";" + str(x) + "H"

    def _get_height(self):
        x, y = consolesize.get_console_size()
        return y

    def _get_width(self):
        x, y = consolesize.get_console_size()
        return x

    def _get_color(self, color):
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
            self._get_color("BLACK")


def _main():
    import sys
    c = Console()
    c.gui()
    get_input = True
    while True:
        while get_input:
            inp = c.get_input()
            com = inp.split(" ")[0]
            arg = inp.split(" ")[1:]
            if com == 'clear' or com == 'cls':
                c.clear()
            elif com == 'set_color':
                c.set_color(arg[0])
            elif com == 'set_title':
                s = ""
                for a in arg:
                    s += a + " "
                c.set_title(s)
            elif com == 'echo':
                s = ""
                for a in arg:
                    s += a + " "
                c.out(s)
            elif com == 'lorem':
                for x in range(0, 50):
                    c.out(str(x))
            elif com == 'exit':
                os.system('cls')
                sys.exit(0)
            elif com == 'disable_input':
                get_input = False
            else:
                pass


if __name__ == '__main__':
    try:
        _main()
    except:
        cursor.show()
