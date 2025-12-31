from time import monotonic

from textual.reactive import reactive
from textual.widgets import Static

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