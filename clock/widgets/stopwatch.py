from widgets.time_display import TimeDisplay

from textual import on
from textual.widgets import Static, Button

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