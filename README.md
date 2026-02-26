# Vastlands Exploration

data exploration for tome of vastlands 

**Requirements:**
- Python 3 installed (including the venv package)

**Getting started (Unix)**: Run ```getting-started.sh```

To edit the configuration values for the database, edit `infrastructure/.env` and apply the changes (e.g. `export $(cat infrastructure/.env)`)

There are 3 main commands (each called by ```python3 main.py <command>```:
- _load_: load all necessary data into the database
- _plot_: render and show the plots locally
- _serve_: start the server for hosting the interactive User Interface

For each, you can specify the following global arguments like this: ```python3 main.py <global options> <command>```
- _-u_: URL to fetch the faergria map data from (defaults to http://localhost:1338). **This requires that you start the server for the map API (https://github.com/Zetsuboushii/faergriaMap) locally.**
- _-s_: Skip loading and showing faergria map data (use when faergria map server is **not** available)
- _-f_: Force refresh data (bypass database cache))

For the _load_ command, you can additonally specify arguments like so: ```python3 main.py <global options> load <arguments>```
- _-e_: Export all plots rendered via the _plot_ command in the ./data/plots
- _-h_: When rendering plots, don't show the matplotlib window (but export anyway)
- _--format_: Image format for exported plots (e.g. png or svg)

**Example**: ```python3 main.py -s -f plot -e --format jpg```

You can also see this information when running ```python3 main.py --help```