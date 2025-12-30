from textual.app import App
from textual.widgets import Footer, Header

class StopwatchApp(App):
    # Bindings is a tuple: (key, action name, description), 
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    # Action method (starts with: action_)
    # Toggle dark mode
    def action_toggle_dark_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    StopwatchApp().run()