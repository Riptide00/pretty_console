
![Mac](https://img.shields.io/badge/OS X-Unavailable-red.svg)
![Windows](https://img.shields.io/badge/Windows-Supported-brightgreen.svg)
![Linux](https://img.shields.io/badge/Linux-Unavailable-red.svg)
![Development](https://img.shields.io/badge/Development-busy-brightgreen.svg)
![Version](https://img.shields.io/badge/Latest-1.0.0/dev-blue.svg)
![Repo size](https://reposs.herokuapp.com/?path=riptide00/pretty_console)

# Pretty

Do stuff in the console! set cursor position, console size or 
read values like the console width and or height.

## Installation

    > pip install -r requirements.txt

## Use

    ### console.Console()

    ### console.start()

    ### console.stop()

    ### console.title("title")

    ### console.color("COLOR")

    ### console.out("Wabelabedubdub")

    ### console.get_input()

    ### consolesize.get()

    ### consolesize.get_height()

    ### consolesize.get_width()

    ### consolesize.set(12, 20)

    ### consolesize.set_height(12)

    ### consolesize.set_width(20)

    ### cursor.set(10, 20)

    ### cursor.show()

    ### cursor.hide()

    ### text.center("help")

    ### text.color("red", "color this text")

## Todo

- [ ] Get cursor position (impossible?)
- [ ] Smooth output
- [ ] Catch std.out and redirect to console.buffer
- [ ] Refactor 'pretty_console' to just 'pretty'
- [ ] Make this a package (Research '__init__.py' and such ...)
- [ ] Cleanup! IMPORTANT (Threads are spawned without any 'control' atm)

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

v1.0.0/dev: Development build.

# License

[__License__](/LICENSE)
