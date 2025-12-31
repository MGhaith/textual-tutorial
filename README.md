# Stopwatch App as TUI
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
   │  └─ stopwatch_app.py      #  Stopwatch Textual App
   ├─ widgets/
   │  ├─ stopwatch.py          # Stopwatch Widget
   │  └─ time_display.py       # Timer Widget
   └─ styles/
      └─ stopwatch.tcss        # Textual CSS (layout and styling)
```

## Running the App
To start the app, install requirements and run the entry point:

```bash
cd clock
python clock.py
```
