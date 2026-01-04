from textual.containers import Center, Middle, VerticalGroup, HorizontalGroup
from textual.widgets import Static, ProgressBar, Input, Button

class Timer(Static):
    
    def compose(self):
        with Center():
            with Middle():
                with VerticalGroup():
                    with HorizontalGroup():
                        yield Input(value="00", id="hours", type="number")
                        yield Input(value="01", id="minutes", type="number")
                        yield Input(value="00", id="seconds", type="number")
                    yield Button("Start", id="start_timer", variant="success")

                yield ProgressBar(classes="hidden")
