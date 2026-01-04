# Clock App as TUI
A simple stopwatches app created using Textual.

## Source
This app is based on the the Textual [Tutorial](https://textual.textualize.io/tutorial/).

## Features
- Start, stop, and reset multiple independent stopwatches.
- Add and remove stopwatches dynamically.
- Responsive terminal UI.
- Clean, modern interface using Textual CSS.

## Requirements
- [Python](https://www.python.org/downloads/)
- [Textual](https://textual.textualize.io/getting_started/)

## Application Tree
```bash
textual-tutorial/
└─ clock/
   ├─ clock.py                 # App entry point
   ├─ apps/
   │  └─ clock_app.py          #  Clock Textual App
   ├─ widgets/
   │  ├─ stopwatch.py          # Stopwatch Widget
   │  ├─ time_display.py       # Stopwatch Time Widget
   │  ├─ time_select.py        # Timer Time Selector Widget
   │  └─ timer.py              # Timer Widget
   └─ styles/
      └─ clock.tcss        # Textual CSS (layout and styling)
```

## Running the App
To start the app, install requirements and run the entry point:

```bash
cd clock
python clock.py
```

## Key Bindings
- d — Toggle dark mode
- a — Add a new stopwatch
- r — Remove last stopwatch
- q — Quit the app

## How It Works
- Clock App composes the UI with a header, tabs for both stopwatches and timer, and a footer.
- For Stopwatches, each widget wires buttons to start/stop/reset events and renders a TimeDisplay.
- TimeDisplay uses a high-resolution monotonic timer and updates ~60 times per second.
- For the Timer, it's composed of a time selector widget, start button, and a progress bar.
- TimeSelect is the time selector and it uses 3 inputs for hours, minutes, and seconds. it returns the selected time. 

## License
MIT — see [LICENSE](LICENSE) for details.
