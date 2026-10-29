import sys
from textual.app import App , ComposeResult
from textual.widgets import Header,Static,Button,Footer,Input
from textual.containers import Grid, Vertical, Horizontal
class Calculator(App):
    "A Basic Calculator"
    CSS = """
    Screen{
        align: center middle;
    }
    Vertical{
        width: 60;
        height: auto;
        background: purple;
        border: $primary;
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
        grid-size: 3 4;
        grid-gutter: 1;
        height: 12;
        margin-bottom: 1;
    }
    Grid Button{
        width: 100%;
        height: 100%;
    }
    #result-box {
        margin-top: 1;
        padding: 1;
        text-align: center;
        text-style: italic;
        content-align: center middle;
        background: $surface;
        border: $success;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static("Calculator",id="title")
                 
            yield Input(placeholder="Enter your first number",id="first-number")
            yield Input(placeholder="Enter your second number",id="second-number")
            yield Static("Enter your numbers:")
            with Grid():
                yield Button("1",variant="primary",id="num-1")
                yield Button("2",variant="primary",id="num-2")
                yield Button("3",variant="primary",id="num-3")
                yield Button("4",variant="primary",id="num-4")
                yield Button("5",variant="primary",id="num-5")
                yield Button("6",variant="primary",id="num-6")
                yield Button("7",variant="primary",id="num-7")
                yield Button("8",variant="primary",id="num-8")
                yield Button("9",variant="primary",id="num-9")
                yield Button("0",variant="primary",id="num-0")
                yield Button("AC",variant="error",id="remove-everything")
                yield Button("Remove",variant="error",id="delete")
            yield Static("Select your operation:",id="selected-operation")
            with Horizontal():
                yield Button("+",variant="primary",id="operation-1")
                yield Button("-",variant="primary",id="operation-2")
                yield Button("*",variant="primary",id="operation-3")
                yield Button("/",variant="primary",id="operation-4")
                yield Button("%",variant="primary",id="operation-5")
            yield Static("Answer",id="result-box")
            yield Button("Exit",variant="error",id="quit-button")
        yield Footer()
    def on_button_pressed(self,event:Button.Pressed)-> None:
        btn_id=event.button.id
        if btn_id=="quit-button":
            sys.exit()
        if btn_id.startswith("num-") or btn_id in ["remove-everything","delete"]:
            



        
        Number_1st=self.query_one("#first-number",Input).value
        Number_2nd=self.query_one("#second-number",Input).value
        result_box=self.query_one("#result-box",Static)
        try:
            x=int(Number_1st)
            y=int(Number_2nd)
        except ValueError:
            result_box.update("Invalid number,Please enter a valid number")
            return
        if y==0 and btn_id in ["operation-4","operation-5"]:
            result_box.update("Math error")
            return
        addition=x+y
        subtraction=x-y
        multiplication=x*y
        division=x/y
        remainder=x%y
        if btn_id=="operation-1":
            result_box.update(f"result:{addition}")
        elif btn_id=="operation-2":
            result_box.update(f"result:{subtraction}")
        elif btn_id=="operation-3":
            result_box.update(f"result:{multiplication}")
        elif btn_id=="operation-4":
            result_box.update(f"result:{division}")
        elif btn_id=="operation-5":
            result_box.update(f"result:{remainder}")
if __name__=="__main__":
    app=Calculator()
    app.run()




