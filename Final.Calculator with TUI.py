import math
import ast
import operator
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
def factorial(v):
    if v < 0 or not v.is_integer() or v>10000:
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
Shift_Functions = {
    "sin": lambda x: math.degrees(math.asin(x)),
    "cos": lambda x: math.degrees(math.acos(x)),
    "tan": lambda x: math.degrees(math.atan(x)),
    "log": lambda x: 10 ** x,
}
Safe_Operators ={
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub:operator.neg
}
Symbols={
    "new-plus":"+",
    "new-minus":"-" ,
    "new-multi":"*",
    "new-div":"/",
    "bracket-1":"(",
    "bracket-2": ")",
    "new-mod":"%",
    "new-pow":"**"

    }
Symbols_ops={
    "new-plus": operator.add,
    "new-minus": operator.sub,
    "new-multi": operator.mul,
    "new-div": operator.truediv,
    "new-mod": operator.mod,
    "new-pow": operator.pow,
    "new-USub": operator.neg,
}
def safe_eval(expr):
    tree=ast.parse(expr,mode="eval")
    return _eval_node(tree.body)
def _eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value,(int,float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in Safe_Operators:
        return Safe_Operators[type(node.op)](_eval_node(node.left),_eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in Safe_Operators:
        return Safe_Operators[type(node.op)] (_eval_node(node.operand))
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in Functions:
            raise ValueError("Unknown Function")
        if len(node.args) !=1 or node.keywords:
            raise ValueError("Incorrect Expression")
        arg=_eval_node(node.args[0])
        return Functions[node.func.id](arg)
    if isinstance (node, ast.Name):
        if node.id=="pi":

            return math.pi
        if node.id== "e":
            return math.e
        raise ValueError("Wrong Name")
    raise ValueError("Invalid Expression")
    
    
    
    
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
        width: 120;
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
        grid-size: 3 6;
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
    #history-box{
        margin-top: 1;
        padding: 1;
        text-align: left;
        text-style: bold;
        background: $surface;
        border: round green;
        }
    #memory-box{
        margin-top: 1;
        padding: 1;
        text-align: center;
        background: $surface;
        text-style: italic;
        border: round blue;
        }
    """
    def __init__(self):
        super().__init__()
        self.bg_image = None
        self.last_active_input_id = "first-number"
        self.shift_on = False
        self.history=[]
        self.memory=0.0
        self.memory_set=False


    def compose(self) -> ComposeResult:
        yield Static(id="bg")
        yield Header()
        with Vertical():
            yield Static("Calculator", id="title")
            yield TrackedInput(placeholder="First number (No brackets )", id="first-number")
            yield TrackedInput(placeholder="Enter your second number (No brackets)", id="second-number")
            yield TrackedInput(placeholder="Enter your third number(No brackets)" , id="third-number")
            yield TrackedInput(placeholder="Only enter Expressions here, not single numbers and no trigonometric functios too",id="expression-box")
            yield Static("Enter your numbers:")
            yield Static("History",id="history-box")
            yield Button("Clear History",variant="error", id="clear-history")
            yield Static("Current_Memory",id="memory-box")
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
                yield Button("%",variant="primary",id="percentage")
                yield Button("π",variant="primary",id="pi")
                yield Button("e",variant="primary",id="eul-number")
                yield Button("=",variant="primary",id="equals")
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
                yield Button("MC",variant="primary", id="memory-clear")
                yield Button("M+",variant="primary", id="memory-add")
                yield Button("M-",variant="primary", id="memory-sub")
                yield Button("MR",variant="primary", id="memory-recall")
            with Horizontal():
                yield Button("+", variant="primary", id="new-plus")
                yield Button("-", variant="primary", id="new-minus")
                yield Button("*", variant="primary", id="new-multi")
                yield Button("/", variant="primary", id="new-div")
                yield Button("%", variant="primary", id="new-mod")
                yield Button("x^y", variant="primary", id="new-pow")
                yield Button("Q.F", variant="primary",id="operation-7")
                yield Button("(",variant="primary",id="bracket-1")
                yield Button(")",variant="primary",id="bracket-2")
            yield Static("Answer", id="result-box")
            yield Button("Exit", variant="error", id="quit-button")
        yield Footer()

    def show_result(self,text):
         self.query_one("#result-box",Static).update(text)
         self.history.append(text)
         latest=self.history[-5:]
         self.query_one("#history-box",Static).update("\n".join(latest))
    def ent_equals(self):
        active=self.query_one(f"#{self.last_active_input_id}",Input)
        expr=active.value
        try:
            answer=safe_eval(expr)
            active.value=clean_result(answer)
            self.show_result(f"result:{clean_result(answer)}")
        except:
            self.query_one(f"#result-box",Static).update("Invalid Expression")
    
    def action_submit(self)-> None:
        self.ent_equals()
    
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
    def on_input_submitted(self,event: Input.Submitted)-> None:
        self.ent_equals()
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
        if btn_id=="clear-history":
            self.history=[]
            self.query_one("#history-box",Static).update("")
            return
        if btn_id.startswith("memory-"):
            result_box= self.query_one("#result-box",Static)
            active=self.query_one(f"#{self.last_active_input_id}",Input)
            if btn_id=="memory-clear":
                self.memory=0.0
                self.memory_set=False
            elif btn_id=="memory-recall":
                if not self.memory_set:
                    result_box.update("Memory is Empty")
                    return
                active.value= clean_result(self.memory)
            else:
                try:
                    value=float(active.value)
                except ValueError:
                    result_box.update("Enter a Number")
                    return
                if btn_id=="memory-add":
                    self.memory+=value
                if btn_id=="memory-sub":
                    self.memory-=value
                self.memory_set= True
            text=f"Memory:{clean_result(self.memory)}" if self.memory_set else "Memory:Empty"
            self.query_one("#memory-box",Static).update (text)
            return
        if btn_id=="percentage":
            try:

                x= float(self.query_one(f"#{self.last_active_input_id}",Input).value)
                self.show_result(f"result:{clean_result(x/100)}")
            except ValueError:
                self.query_one("#result-box",Static).update("Please Enter a Number")
            return
        if btn_id in ("bracket-1","bracket-2"):
            focused_widget=self.query_one(f"#{self.last_active_input_id}",Input)
            focused_widget.value+=Symbols[btn_id]
            return
        if btn_id in Symbols_ops:
            if self.last_active_input_id=="expression-box":
                focused_widget=self.query_one("#expression-box",Input)
                focused_widget.value+=Symbols[btn_id]
                return
            ids =["first-number","second-number","third-number"]
            raw = [self.query_one(f"#{i}",Input).value.strip() for i in ids]
            filled=[v for v in raw if v!=""]
            if len(filled)<2:
                self.query_one("#result-box",Static).update("Please Enter a Number")
                return

            try:
                numbers=[float(v) for v in filled]

            except ValueError:
                self.query_one("#result-box",Static).update("Please Enter a number")
                return
            try:
                answer = numbers[0]
                for n in numbers[1:]:
                    answer=Symbols_ops[btn_id](answer,n)
                self.show_result (f"#result:{clean_result(answer)}")
            except(ZeroDivisionError,ValueError,OverflowError):
                self.query_one("#result-box",Static).update("Math Error")
                return
            return

        focused_widget = self.query_one(f"#{self.last_active_input_id}", Input)
        if btn_id.startswith("num-") or btn_id in ["remove-everything", "delete", "decimal", "plus-minus","pi","eul-number"]:
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
            elif btn_id=="pi":
                focused_widget.value=str(math.pi)
            elif btn_id=="eul-number":
                focused_widget.value=str(math.e)
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
        if btn_id =="equals":
            self.ent_equals()
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
                self.show_result(f"# x1:{clean_result(x1)} x2: {clean_result(x2)}")
            return
if __name__ == "__main__":
    app = Calculator()
    app.run()
