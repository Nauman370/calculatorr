import math
import sys
import os
from PIL import Image
from rich_pixels import Pixels
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Button, Footer, Input
from textual.containers import Grid, Vertical, Horizontal

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename


class TrackedInput(Input):
    def on_focus(self, event: events.Focus) -> None:
        self.app.last_active_input_id = self.id


def clean_result(value) -> str:
    if isinstance(value, float):
        value = round(value, 10)
        if value.is_integer():
            return str(int(value))
    return str(value)

def show_result(self,text):
    self.query_one("#result-box",Static).update(text)
    self.history.append(text)
    latest=self.history[-5:]
    self.query_one("#history-box",Static).update("\n".join(latest))


def factorial(v):
    if v < 0 or not v.is_integer():
        raise ValueError("Math error")
    return math.factorial(int(v))
def Quadratic_Formula(a,b,c):
    discriminant= b**2-4*a*c
    if discriminant<0:
        result=None
        return(result)
    else:
        root=math.sqrt(discriminant)
        result_x1=(-b+root)/(2*a)
        result_x2=(-b-root)/(2*a)
        return (result_x1,result_x2)
Functions = {
    "sqrt": lambda x: math.sqrt(x),
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": lambda x: math.log10(x),
    "fact": factorial,
    "ln": lambda x: math.log(x),
    "square": lambda x: (x * x),
}
Operations ={
    "operation-1": lambda a, b : a+b,
    "operation-2": lambda a,b : a-b,
    "operation-3": lambda a,b : a*b,
    "operation-4": lambda a,b :a/b,
    "operation-5": lambda a,b :a%b,
    "operation-6": lambda a,b :math.pow(a,b),
}

Shift_Functions = {
    "sin": lambda x: math.degrees(math.asin(x)),
    "cos": lambda x: math.degrees(math.acos(x)),
    "tan": lambda x: math.degrees(math.atan(x)),
    "log": lambda x: 10 ** x,
}
class Calculator(App):
    CSS = """
    Screen{
        layers: bg ui;
        align: center middle;
    }
    #bg{
        layer: bg;
        dock: top;
        width: 100%;
        height: 100%;
    }
    Header, Footer{
        layer: ui;
    }
    Vertical{
        layer: ui;
        width: 100;
        height: auto;
        background: black;
        border: round white;
        padding: 1 2;
    }
    Input{
        margin-bottom: 1;
    }
    Horizontal{
        height: auto;
        margin-top: 1;
        margin-bottom: 1;
        align: center middle;
    }
    Horizontal Button{
        margin: 0 1;
        min-width: 10;
    }
    Grid{
        grid-size: 3 5;
        grid-gutter: 1;
        height: 25;
        margin-bottom: 1;
    }
    Grid Button{
        width: 100%;
        height: 3;
    }
    #result-box{
        margin-top: 1;
        padding: 1;
        text-align: center;
        text-style: italic;
        content-align: center middle;
        background: $surface;
        border: round white;
    }
    """

    def __init__(self):
        super().__init__()
        self.bg_image = None
        self.last_active_input_id = "first-number"
        self.shift_on = False
        self.history[]

    def compose(self) -> ComposeResult:
        yield Static(id="bg")
        yield Header()
        with Vertical():
            yield Static("Calculator", id="title")
            yield TrackedInput(placeholder="Enter your first number", id="first-number")
            yield TrackedInput(placeholder="Enter your second number", id="second-number")
            yield TrackedInput(placeholder="Enter your third number", id="third-number")
            yield Static("Enter your numbers:")
            yield Static(placeholder="History",id="history-box")
            with Grid():
                yield Button("1", variant="primary", id="num-1")
                yield Button("2", variant="primary", id="num-2")
                yield Button("3", variant="primary", id="num-3")
                yield Button("4", variant="primary", id="num-4")
                yield Button("5", variant="primary", id="num-5")
                yield Button("6", variant="primary", id="num-6")
                yield Button("7", variant="primary", id="num-7")
                yield Button("8", variant="primary", id="num-8")
                yield Button("9", variant="primary", id="num-9")
                yield Button("0", variant="primary", id="num-0")
                yield Button("AC", variant="error", id="remove-everything")
                yield Button("Remove", variant="error", id="delete")
                yield Button(".", variant="primary", id="decimal")
                yield Button("+/-", variant="primary", id="plus-minus")
            yield Static("Select your operation:", id="selected-operation")
            with Horizontal():
                yield Button("sin", variant="success", id="func-sin")
                yield Button("cos", variant="success", id="func-cos")
                yield Button("tan", variant="success", id="func-tan")
                yield Button("√", variant="success", id="func-sqrt")
                yield Button("SHIFT", variant="success", id="shift-toggle")
            with Horizontal():
                yield Button("log", variant="success", id="func-log")
                yield Button("n!", variant="success", id="func-fact")
                yield Button("ln", variant="success", id="func-ln")
                yield Button("a^2", variant="success", id="func-square")
            with Horizontal():
                yield Button("+", variant="primary", id="operation-1")
                yield Button("-", variant="primary", id="operation-2")
                yield Button("*", variant="primary", id="operation-3")
                yield Button("/", variant="primary", id="operation-4")
                yield Button("%", variant="primary", id="operation-5")
                yield Button("x^y", variant="primary", id="operation-6")
                yield Button ("Q.F", variant="primary",id="operation-7")
            yield Static("Answer", id="result-box")
            yield Button("Exit", variant="error", id="quit-button")
        yield Footer()

    def on_mount(self) -> None:

        bg_path = resource_path("bg.png")
        if os.path.exists(bg_path):
            self.bg_image = Image.open(bg_path).convert("RGB")
            self.call_after_refresh(self.update_background)

    def on_resize(self, event:events.Resize) -> None:
        self.call_after_refresh(self.update_background)

    def update_background(self) -> None:
        if not self.bg_image:
            return
        try:
            w, h = self.size
            if w <= 0 or h <= 0:
                return
            self.query_one("#bg", Static).update(
                Pixels.from_image(self.bg_image, resize=(w, h * 2))
            )
        except Exception:
            return

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "quit-button":
            self.exit()
            return

        if btn_id == "shift-toggle":
            self.shift_on = not self.shift_on
            labels = {
                "sin": ("sin", "sin^-1"),
                "cos": ("cos", "cos^-1"),
                "tan": ("tan", "tan^-1"),
                "log": ("log", "10^x"),
            }
            for name, (normal, shifted) in labels.items():
                self.query_one(f"#func-{name}", Button).label = shifted if self.shift_on else normal
            return

        focused_widget = self.query_one(f"#{self.last_active_input_id}", Input)
        if btn_id.startswith("num-") or btn_id in ["remove-everything", "delete", "decimal", "plus-minus"]:
            if btn_id == "remove-everything":
                focused_widget.value = ""
            elif btn_id == "delete":
                focused_widget.value = focused_widget.value[:-1]
            elif btn_id == "plus-minus":
                if focused_widget.value.startswith("-"):
                    focused_widget.value = focused_widget.value[1:]
                else:
                    focused_widget.value = "-" + focused_widget.value
            elif btn_id == "decimal":
                if "." not in focused_widget.value:
                    focused_widget.value += "."
            else:
                digit = btn_id.split("-")[1]
                focused_widget.value += digit
            return

        result_box = self.query_one("#result-box", Static)

        if btn_id.startswith("func-"):
            name = btn_id.split("-")[1]
            try:
                x = float(self.query_one(f"#{self.last_active_input_id}", Input).value)
                if self.shift_on and name in Shift_Functions:
                    answer = Shift_Functions[name](x)
                else:
                    answer = Functions[name](x)
                self.show_result(f"result:{clean_result(answer)}")
            except (ValueError, ZeroDivisionError, OverflowError):
                result_box.update("Math Error")
            return
        ids=["first-number","second-number","third-number"]
        raw=[self.query_one(f"#{i}",Input).value.strip() for i in ids]
        filled=[v for v in  raw if v!=""]
        if len(filled)< 2:
            result_box.update("Please Enter numbers")
            return
        try:
            numbers=[float (v) for v in filled]
        except ValueError:
            result_box.update("Please Enter a Number")
            return
        if btn_id=="operation-7":
            if len(numbers) !=3:
                result_box.update("Quadratic formula needs three numbers")
                return
            a,b,c=numbers
            if a==0:
                result_box.update("This is not a Quadratic Equation")
                return
            result=Quadratic_Formula(a,b,c)
            if result is None:
                result_box.update("Roots are imaginary")
            else:
                x1,x2=result
                result_box.update(f"# x1:{clean_result(x1)} x2: {clean_result(x2)}")
            return
        if btn_id not in Operations:
            return
        op=Operations[btn_id]
        try:
            answer = numbers[0]
            for n in numbers[1:]:
                answer = op(answer,n)
                result_box.update(f"result:{clean_result(answer)}")
        except (ValueError, ZeroDivisionError, OverflowError):
            result_box.update("Math error")
if __name__ == "__main__":
    app = Calculator()
    app.run()
