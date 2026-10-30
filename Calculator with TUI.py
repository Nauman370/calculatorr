import math
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Button, Footer, Input
from textual.containers import Grid, Vertical, Horizontal


class TrackedInput(Input):
    def on_focus(self, event: events.Focus) -> None:
     self.app.last_active_input_id = self.id
def clean_result(value)-> str:
    if isinstance(value, float):
        value = round(value,10)
        if value.is_integer():
            return str(int(value))
    return str(value)
def factorial(v):
    if v<0 or not v.is_integer():
        raise ValueError("Math error")
    return math.factorial(int(v))
Functions={
    "sqrt": lambda x : math.sqrt(x),
    "sin": lambda x : math.sin(math.radians(x)),
    "cos": lambda x : math.cos(math.radians(x)),
    "tan": lambda x : math.tan(math.radians(x)),
    "log": lambda x : math.log10(x),
    "fact":factorial,
    "ln": lambda x : math.log(x),
    "square": lambda x: (x*x)
}
Shift_Functions={
    "sin": lambda x : math.degrees(math.asin(x)),
    "cos": lambda x : math.degrees(math.acos(x)),
    "tan": lambda x : math.degrees(math.atan(x)),
    "log": lambda x : 10**x
}  
class Calculator(App):
    CSS = """
    Screen{
        align: center middle;
    }
    Vertical{
        width: 72;
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
    #result-box {
        margin-top: 1;
        padding: 1;
        text-align: center;
        text-style: italic;
        content-align: center middle;
        background: $surface;
        border: round white;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static("Calculator", id="title")
            yield TrackedInput(placeholder="Enter your first number", id="first-number")
            yield TrackedInput(placeholder="Enter your second number", id="second-number")
            yield Static("Enter your numbers:")
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
                yield Button(".",variant="primary",id="decimal")
                yield Button("+/-",variant="primary", id="plus-minus")
            yield Static("Select your operation:", id="selected-operation")
            with Horizontal():
                yield Button("sin",variant="success",id="func-sin")
                yield Button("cos",variant="success",id="func-cos")
                yield Button("tan",variant="success",id="func-tan")
                yield Button("√",variant="success",id="func-sqrt")
                yield Button("SHIFT",variant="success",id="shift-toggle")
            with Horizontal():
                yield Button("log",variant="success",id="func-log")
                yield Button("n!",variant="success",id="func-fact")
                yield Button("ln",variant="success",id="func-ln")
                yield Button("a^2",variant="success",id="func-square")
            with Horizontal():
                yield Button("+", variant="primary", id="operation-1")
                yield Button("-", variant="primary", id="operation-2")
                yield Button("*", variant="primary", id="operation-3")
                yield Button("/", variant="primary", id="operation-4")
                yield Button("%", variant="primary", id="operation-5")
                yield Button("x^y",variant="primary",id="operation-6")
            yield Static("Answer", id="result-box")
            yield Button("Exit", variant="error", id="quit-button")
        yield Footer()
    def on_mount(self) -> None:
        self.last_active_input_id = "first-number"
        self.shift_on=False
    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id
        if btn_id =="quit-button":
            self.exit()
        if btn_id=="shift-toggle":
            self.shift_on=not self.shift_on
            labels = {
                "sin":("sin","sin^-1"),
                "cos":("cos","cos^-1"),
                "tan":("tan","tan^-1"),
                "log":("log","10^x")
            }
            for name, (normal,shifted) in labels.items():
                self.query_one(f"#func-{name}",Button).label=shifted if self.shift_on else normal
            return
        focused_widget = self.query_one(f"#{self.last_active_input_id}", Input)
        if btn_id.startswith("num-") or btn_id in ["remove-everything", "delete","decimal","plus-minus"]:
            if btn_id == "remove-everything":
                focused_widget.value = ""
            elif btn_id == "delete":
                focused_widget.value = focused_widget.value[:-1]
            elif btn_id=="plus-minus":
                if focused_widget.value.startswith("-"):
                    focused_widget.value=focused_widget.value[1:]
                else:
                    focused_widget.value = "-" + focused_widget.value
            elif btn_id=="decimal":
                if "." not in focused_widget.value:
                    focused_widget.value+="."
            else:
                digit = btn_id.split("-")[1]
                focused_widget.value += digit
            return
        result_box=self.query_one("#result-box", Static)
        if btn_id.startswith("func-"):
            name= btn_id.split("-")[1]
            try:
                x=float(self.query_one("#first-number",Input).value)
                if self.shift_on and name in Shift_Functions:
                    answer=Shift_Functions[name](x)
                else:
                    answer=Functions[name](x)
                result_box.update(f"result:{clean_result(answer)}")
            except(ValueError,ZeroDivisionError):
                result_box.update("Math Error")
            return
        Number_1st = self.query_one("#first-number", Input).value
        Number_2nd = self.query_one("#second-number", Input).value
        result_box = self.query_one("#result-box", Static)
        try:
            x = float(Number_1st)
            y = float(Number_2nd)
        except ValueError:
            result_box.update("Please enter a number")
            return
        try:

         if y == 0 and btn_id in ["operation-4", "operation-5"]:
            result_box.update("Math error")
            return
         if btn_id == "operation-1":
            answer=x+y
         elif btn_id == "operation-2":
            answer=x-y
         elif btn_id == "operation-3":
            answer=x*y
         elif btn_id == "operation-4":
            answer=x/y
         elif btn_id == "operation-5":
            answer=x%y
         elif btn_id == "operation-6":
            answer=math.pow(x,y)
         result_box.update(f"result:{clean_result(answer)}")
        except(ValueError,ZeroDivisionError):
            result_box.update("Math error")
if __name__ == "__main__":
    app = Calculator()
    app.run()
