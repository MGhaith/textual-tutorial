from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Static, Button

# Costum stopwatch widget
class Stopwatch(Static):
    def compose(self):
        yield Button("Start", variant="success")
        yield Button("Stop", variant="error")
        yield Button("Reset")

class StopwatchApp(App):

    CSS_PATH = "stopwatch.css"
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