from time import monotonic

from textual import on
from textual.app import App
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Footer, Header, Static, Button

# Custom time display widget
class TimeDisplay(Static):
    
    time_elapsed = reactive(0)

    def watch_time_elapsed(self):
        time = self.time_elapsed
        time, seconds = divmod(time, 60)
        hours, minutes = divmod(time, 60)
        time_str = f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"
        self.update(time_str)

    # Start timer
    def start(self):
        self.start_time = monotonic()

    # Stop timer
    def stop(self):
        self.time_elapsed = monotonic() - self.start_time

    # Reset timer
    def reset(self):
        pass

# Custom stopwatch widget
class Stopwatch(Static):

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")
        self.query_one(TimeDisplay).start()

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed, "#reset")
    def reset_stopwatch(self):
        self.query_one(TimeDisplay).reset()

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