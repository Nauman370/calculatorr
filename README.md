# Scientific Calculator (TUI)

A scientific calculator with a TUI, built in Python with [Textual](https://github.com/Textualize/textual).

I initially created it without a TUI and with only basic arithmetic I then developed a basic TUI and then later remade it with a completely new look and new buttons and everything hence it grew into a keypad after that i added decimal and sign support, and a set of scientific functions.


## Features

- On-screen keypad (0-9, decimal point, +/- sign flip, AC, Remove)
- Two number input boxes
- Basic operations: `+`, `-`, `*`, `/`, `%`
- Scientific functions (applied to the first number box): `sin`, `cos`, `tan`, `√`, `log`, `ln`, `n!`, `x²`
- Error handling for invalid input, division by zero, and invalid function input (e.g. negative square roots)

## Running from source

Requires Python 3.10+ and [Textual](https://textual.textualize.io/).
Requires the libraries rich-pixels and pillow


```bash
pip install textual
pip install pillow rich-pixels
python "Final.Calculator with TUI.py"
```

## Download a prebuilt app (no Python required)

A standalone Windows executable is available on the [Releases page](../../releases/latest), built with [PyInstaller](https://pyinstaller.org/).

> **Note:** If the borders render as odd tiled symbols instead of clean lines, it is due to the limitation of the Windows console. Run the .exe inside Windows Terminal instead.

## Built with

- [Python](https://www.python.org/)
- [Textual](https://github.com/Textualize/textual) — TUI framework
- [PyInstaller](https://pyinstaller.org/) — packaging into a standalone executable
