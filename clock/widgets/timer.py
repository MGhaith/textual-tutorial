from time import monotonic

from .time_select import TimeSelect

from textual.containers import Center, Middle, VerticalGroup, HorizontalGroup
from textual.timer import Timer as TextualTimer
from textual import on
from textual.widgets import Static, ProgressBar, Input, Button

class Timer(Static):
    
    start_time = monotonic()
    selected_time = 60
    progress_timer: TextualTimer

    @on(Button.Pressed, "#start_timer")
    def start_timer(self):
        self.start_time = monotonic()
        time_select = self.query_one(TimeSelect)
        self.selected_time = time_select.get_seleted_time()
        self.query_one(ProgressBar).update(total=100, progress=100)
        self.query_one(VerticalGroup).add_class("hidden")
        self.query_one(ProgressBar).remove_class("hidden")
        self.progress_timer.resume()


    def compose(self):
        with Center():
            with Middle():
                with VerticalGroup():
                    yield TimeSelect()
                    yield Button("Start", id="start_timer", variant="success")

                yield ProgressBar(classes="hidden")
                
    def on_mount(self) -> None:
        # Set up a timer to simulate progess happening.
        self.progress_timer = self.set_interval(1 / 60, self.make_progress, pause=True)

    def make_progress(self) -> None:
        # Called automatically to advance the progress bar.
        elapsed = monotonic() - self.start_time
        print(TimeSelect().get_seleted_time())
        remaining_percent = max(0, ((self.selected_time - elapsed) / self.selected_time) * 100)
        self.query_one(ProgressBar).update(progress=remaining_percent)

        # Stop timer if done
        if remaining_percent <= 0:
            self.progress_timer.pause()
            self.query_one(VerticalGroup).remove_class("hidden")
            self.query_one(ProgressBar).add_class("hidden")
