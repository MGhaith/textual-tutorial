from textual.widgets import Static

class Timer(Static):
    
    def compose(self):
        yield Static("Timer")