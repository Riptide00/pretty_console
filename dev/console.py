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
                 name='',
                 titlebar_color="WHITE",
                 ps1=' > '):
        """Initiation."""
        super(Console, self).__init__()
        self.titlebar_color = titlebar_color.upper()
        self.name = name
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
        os.system('cls')

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
        h = consolesize.height() - 3
        w = consolesize.width()
        c = input(cursor.set(1, h) +
                  text.color("BLACK",
                             "_" * w + '\n' + self.ps1))
        cursor.hide()
        blackout = " " * len(c + self.ps1)
        print(cursor.set(1, h) +
              text.color("BLACK",
                         " " * w + '\n' + blackout))
        return c

    def title(self, name):
        """Set a new title."""
        self.name = name
        self._update_title_bar()

    def color(self, new_color):
        """Set a new color."""
        self.titlebar_color = new_color.upper()
        self._update_title_bar()

    def _detect_change(self):
        """Detect width or height changing."""
        w, h = consolesize.get()
        while True:
            if w is not consolesize.width() \
               or h is not consolesize.height():
                w = consolesize.width()
                h = consolesize.height()
                self._update()

    def _update(self):
        """Complete refresh."""
        os.system('cls')
        self._update_title_bar()
        self._update_console_out()

    def _update_console_out(self):
        """Refresh output."""
        cursor.hide()
        w, h = consolesize.get()
        for b in range(0, h - 7):
            print(cursor.set(1, 3 + b) +
                  text.color("BLACK",
                  " " * w))
        rang = self.console_buffer[-(h - 8):]
        blob = "\n".join(rang)
        print(cursor.set(1, 4) +
              text.color("BLACK", blob))
        cursor.show()

    def _update_title_bar(self):
        """Refresh titlebar."""
        cursor.hide()
        s = (cursor.set(1, 1) +
             text.color(self.titlebar_color,
                        text.center(self.name)))
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
            elif com == 'color':
                c.color(arg[0])
            elif com == 'title':
                s = ""
                for a in arg:
                    s += a + " "
                c.title(s)
            elif com == 'echo':
                s = ""
                for a in arg:
                    s += a + " "
                c.out(s)
            elif com == 'lorem':
                for x in range(0, 50):
                    c.out(str(x))
            elif com == 'size':
                try:
                    x = arg[0]
                    y = arg[1]
                    consolesize.set(x, y)
                except:
                    pass
            elif com == 'exit':
                os.system('cls')
                sys.exit(0)
            elif com == 'disable':
                c.out("Press 'CRTL + C' to quit.")
                get_input = False
            else:
                pass


if __name__ == '__main__':
    try:
        _main()
    except:
        cursor.show()
