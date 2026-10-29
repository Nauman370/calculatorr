import sys
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Button, Footer, Input
from textual.containers import Grid, Vertical, Horizontal


class TrackedInput(Input):
    def on_focus(self, event: events.Focus) -> None:

     self.app.last_active_input_id = self.id


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
        height: 15;
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
        border: $success;
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
            yield Static("Select your operation:", id="selected-operation")
            with Horizontal():
                yield Button("+", variant="primary", id="operation-1")
                yield Button("-", variant="primary", id="operation-2")
                yield Button("*", variant="primary", id="operation-3")
                yield Button("/", variant="primary", id="operation-4")
                yield Button("%", variant="primary", id="operation-5")
            yield Static("Answer", id="result-box")
            yield Button("Exit", variant="error", id="quit-button")
        yield Footer()

    def on_mount(self) -> None:
        # Default starting point when app opens
        self.last_active_input_id = "first-number"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "quit-button":
            sys.exit()

        # Target the text box that was highlighted last
        focused_widget = self.query_one(f"#{self.last_active_input_id}", Input)

        if btn_id.startswith("num-") or btn_id in ["remove-everything", "delete"]:
            if btn_id == "remove-everything":
                focused_widget.value = ""
            elif btn_id == "delete":
                focused_widget.value = focused_widget.value[:-1]
            else:
                digit = btn_id.split("-")[1]
                focused_widget.value += digit
            return

        Number_1st = self.query_one("#first-number", Input).value
        Number_2nd = self.query_one("#second-number", Input).value
        result_box = self.query_one("#result-box", Static)

        try:
            x = int(Number_1st)
            y = int(Number_2nd)
        except ValueError:
            result_box.update("Please enter a number")
            return

        if y == 0 and btn_id in ["operation-4", "operation-5"]:
            result_box.update("Math error")
            return

        addition = x + y
        subtraction = x - y
        multiplication = x * y
        division = x / y
        remainder = x % y

        if btn_id == "operation-1":
            result_box.update(f"result:{addition}")
        elif btn_id == "operation-2":
            result_box.update(f"result:{subtraction}")
        elif btn_id == "operation-3":
            result_box.update(f"result:{multiplication}")
        elif btn_id == "operation-4":
            result_box.update(f"result:{division}")
        elif btn_id == "operation-5":
            result_box.update(f"result:{remainder}")


if __name__ == "__main__":
    app = Calculator()
    app.run()



