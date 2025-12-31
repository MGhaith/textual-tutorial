from textual import on
from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Static, Button

# Custom time display widget
class TimeDisplay(Static):
    pass

# Custom stopwatch widget
class Stopwatch(Static):

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")

    def compose(self):
        yield Button("Start", id= "start" ,variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id= "reset")
        yield TimeDisplay("00:00:00.00")

class StopwatchApp(App):

    CSS_PATH = "stopwatch.tcss"
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        yield Header(show_clock=True)

        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch()
            yield Stopwatch()
            yield Stopwatch()

        yield Footer()

    # Action method (starts with: action_)
    # Toggle dark mode
    def action_toggle_dark_mode(self):
        self.theme = ( 
            "textual-dark" if self.theme == "textual-light" else "textual-light"
         )

if __name__ == "__main__":
    StopwatchApp().run()