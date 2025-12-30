from textual.app import App
from textual.widgets import Footer, Header

class StopwatchApp(App):
    def compose(self):
        yield Header()
        yield Footer()

if __name__ == "__main__":
    StopwatchApp().run()