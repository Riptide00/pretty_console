"""Pretty console for Windows."""
import colorama
import _thread
import os
import consolesize
import cursor
import text


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

    def start(self):
        """Initiate gui."""
        self._update()
        _thread.start_new_thread(self._detect_change, ())

    def stop(self):
        """Stop gui."""
        pass

    def out(self, output):
        """Console io should be directed here."""
        self.console_buffer.append(output)
        self._update_console_out()

    def clear(self):
        """Clear console."""
        self.console_buffer = list()
        self._update_console_out()

    def get_input(self):
        """Return user input."""
        cursor.show()
        h = consolesize.get_height()
        c = input(text.set_color("BLACK") +
                 cursor.set(1, (h - 3)) +
                 "_" * consolesize.get_width() + '\n' + self.ps1)
        cursor.hide()
        print((text.set_color("BLACK") +
              cursor.set(1, (h - 3)) +
              " " * consolesize.get_width() + '\n' +
              " " * (len(c) + 3)))
        return c

    def set_title(self, title):
        """Set a new title."""
        self.title = title
        self._update_title_bar()

    def set_color(self, color):
        """Set a new color."""
        self.color = color.upper()
        self._update_title_bar()

    def _detect_change(self):
        """Detect width or height changing."""
        w, h = consolesize.get_console_size()
        while True:
            if w is not consolesize.get_width() \
            or h is not consolesize.get_height():
                w = consolesize.get_width()
                h = consolesize.get_height()
                self._update()

    def _update(self):
        """Complete refresh."""
        os.system('cls')
        self._update_title_bar()
        self._update_console_out()

    def _update_console_out(self):
        """Refresh output."""
        cursor.hide()
        w, h = consolesize.get_console_size()
        for b in range(0, h - 7):
            print((text.set_color("BLACK") +
                  cursor.set(1, 3 + b) + (" " * w)))
        rang = self.console_buffer[-(consolesize.get_height() - 8):]
        blob = "\n".join(rang)
        print((cursor.set(1, 4) +
              text.set_color("BLACK") +
              blob))
        cursor.show()

    def _update_title_bar(self):
        """Refresh titlebar."""
        cursor.hide()
        padding = int((consolesize.get_width() / 2) - (len(self.title) / 2))
        s = (text.set_color(self.color) +
             cursor.set(1, 1) +
             (" " * padding) +
             self.title +
             (" " * padding))
        print(s)
        cursor.show()


def _main():
    """Builtin console."""
    import sys
    c = Console()
    c.start()
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
