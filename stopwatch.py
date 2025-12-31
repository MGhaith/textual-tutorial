from time import monotonic

from textual import on
from textual.app import App
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Footer, Header, Static, Button

# Custom time display widget
class TimeDisplay(Static):
    
    accumelated_time = 0
    start_time = monotonic()
    time_elapsed = reactive(0)

    def _on_mount(self):
        self.update_timer = self.set_interval(1/60, self.update_time_elapsed, pause=True)

    def update_time_elapsed(self):
        self.time_elapsed = self.accumelated_time + monotonic() - self.start_time

    def watch_time_elapsed(self):
        time = self.time_elapsed
        time, seconds = divmod(time, 60)
        hours, minutes = divmod(time, 60)
        time_str = f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"
        self.update(time_str)

    # Start timer
    def start(self):
        self.start_time = monotonic()
        self.update_timer.resume()

    # Stop timer
    def stop(self):
        self.accumelated_time = self.time_elapsed
        self.update_timer.pause()

    # Reset timer
    def reset(self):
        self.accumelated_time = 0
        self.time_elapsed = 0

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
        ("a", "add_stopwatch", "Add a new stopwatch"),
        ("r", "remove_stopwatch", "Remove stopwatch")
    ]

    def compose(self):
        yield Header(show_clock=True)

        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch()
            yield Stopwatch()
            yield Stopwatch()

        yield Footer()

    ## Action methods (starts with: action_)
    # Toggle dark mode
    def action_toggle_dark_mode(self):
        self.theme = ( 
            "textual-dark" if self.theme == "textual-light" else "textual-light"
         )
        
    # Add stopwatch
    def action_add_stopwatch(self):
        stopwatch = Stopwatch()
        container = self.query_one("#stopwatches")
        container.mount(stopwatch)
        stopwatch.scroll_visible()

    # Remove stopwatch
    def action_remove_stopwatch(self):
        stopwatches = self.query(Stopwatch)
        if stopwatches:
            stopwatches.last().remove()

if __name__ == "__main__":
    StopwatchApp().run()