from widgets.stopwatch import Stopwatch
from widgets.timer import Timer

from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Tabs, Tab, ContentSwitcher

Apps = [
    "Stopwatch",
    "Timer"
]

class ClockApp(App):

    CSS_PATH = "../styles/clock.tcss"
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
        ("a", "add_stopwatch", "Add a new stopwatch"),
        ("r", "remove_stopwatch", "Remove stopwatch"),
        ("q", "quit_app", "Quit Clock")
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Tabs(
            Tab(Apps[0], id="stopwatchs"),
            Tab(Apps[1], id="timers"),
            active="stopwatchs"
        )

        with ContentSwitcher(initial="stopwatchs"):
                with ScrollableContainer(id="stopwatchs"):
                    yield Stopwatch()

                with ScrollableContainer(id="timers"):
                    yield Timer()

        yield Footer()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        self.query_one(ContentSwitcher).current = event.tab.id

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
    
    # Quit Clock
    def action_quit_app(self):
        self.exit() 
