from textual.containers import HorizontalGroup
from textual.widgets import Static, Input

class TimeSelect(Static):

    def compose(self):
        with HorizontalGroup():
            yield Input(value="00", id="hours", type="number")
            yield Input(value="01", id="minutes", type="number")
            yield Input(value="00", id="seconds", type="number")

    def get_seleted_time(self) -> int:
        time: int = 0

        inputs= self.query(Input)

        if len(inputs) > 0:
            for x in inputs:
                if x.id == "hours" and x.value != '':
                    time += int(x.value) * 3600
                if x.id == "minutes" and x.value != '':
                    time += int(x.value) * 60
                if x.id == "seconds" and x.value != '':
                    time += int(x.value)

        return time