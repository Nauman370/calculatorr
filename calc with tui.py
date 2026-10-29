import sys
from textual.app import App , ComposeResult
from textual.widgets import Header,Static,Button,Footer,Input
from textual.containers import Vertical, Horizontal
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
            yield Static("==================",id="line")
            
            yield Input(placeholder="Enter your first number",id="first-number")
            yield Input(placeholder="Enter your second number",id="second-number")
            yield Static("1=addition,2=subtraction,3=multiplication,4=division,5=remainder",id="operations")
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





