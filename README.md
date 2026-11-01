# Scientific Calculator (TUI)

A scientific calculator with a TUI, built in Python with [Textual](https://github.com/Textualize/textual).

I initially created it without a TUI and with only basic arithmetic I then developed a basic TUI and then later remade it with a completely new look and new buttons and everything hence it grew into a keypad after that I added decimal and sign support, and a set of scientific functions. Now i have added quadratic formula, an expression box, a shift key for inverse trigonometric functions and antilog, calculation history, memory button


## Features

- On-screen keypad (0-9, decimal point, +/- sign flip, AC, Remove)
- Three number input boxes
- Basic operations: `+`, `-`, `*`, `/`, `%`
- Scientific functions (applied to the first three boxes): `sin`, `cos`, `tan`, `√`, `log`, `ln`, `n!`, `x²`
- Error handling for invalid input, division by zero, and invalid function input (e.g. negative square roots)
- Quadratic formula solver (Q.F): enter a, b, c into the three number boxes
Expression evaluator: type a full expression (e.g. sin(30)+2*4/12) into any box and press =; supports + - * / % **, parentheses. Currently trigonometric functions are not supported
Operator buttons (+ - * / % x^y) either insert a symbol (when the expression box is focused) or compute directly across however many number boxes are filled
Memory buttons: M+, M-, MR, MC
Calculation history, showing the last 5 results, with a Clear History button
π insert button
Percent key (divides the focused box's value by 100)
Error handling throughout: invalid input, division by zero, invalid function input (e.g. negative square roots), an oversized factorial, and invalid expressions all show a clear message instead of crashing
Optional background image, rendered with rich-pixels, that resizes with the window

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
- Python's standard library: math for the scientific functions, ast and operator to safely parse and evaluate typed expressions without using eval(), os and sys for file paths and bundling the background image into the executable
