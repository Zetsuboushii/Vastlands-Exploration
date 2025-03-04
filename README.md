# Vastlands Exploration

data exploration for tome of vastlands 

**Requirements:**
- Python 3 installed (including the venv package)

There are 3 main commands (each called by ```python3 main.py <command>```:
- _-e_: Export all plots rendered via the _plot_ command in the ./data/plots
- _-h_: When rendering plots, don't show the matplotlib window (but export anyway)
- _--format_: Image format for exported plots (e.g. png or svg)

**Example**: ```python3 main.py -e -h --format jpg```