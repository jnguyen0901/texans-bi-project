# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a small data-analytics portfolio project, not a software application. It simulates 3 seasons (2021–2023) of Houston Texans NFL game data — ticket sales, attendance, and sponsorship — and turns it into business insights via Python scripts, a SQLite database, and a public Tableau dashboard. There is no test suite, build step, package manifest, or web server in this repo.

## Commands

There is no dependency manifest (no `requirements.txt`/`pyproject.toml`) — scripts assume `pandas`, `numpy`, `matplotlib`, and `seaborn` are already available in the environment.

Run the pipeline in this order, since each stage depends on the previous stage's output file:

```bash
python3 create_data.py     # generates texans_game_data.csv (regenerates it if it already exists)
python3 explore_data.py    # prints data-quality checks and summary stats from the CSV
python3 visualize.py       # reads the CSV, writes chart1-4 PNGs to the repo root, and calls plt.show()
```

`texans.db` (SQLite) holds the same data in a single `games` table, used for the SQL analysis queries referenced in the README. There is no `.sql` file in the repo — inspect/query it directly, e.g.:

```bash
python3 -c "import sqlite3; print(sqlite3.connect('texans.db').execute('SELECT * FROM games LIMIT 5').fetchall())"
```

## Architecture / Data Flow

The three Python scripts form a linear pipeline, not a package — there are no shared modules or imports between them:

1. **`create_data.py`** — generates the synthetic dataset with `np.random.seed(42)` (so output is reproducible), computes derived columns (`occupancy_rate`, `total_ticket_revenue`, `revenue_per_impression`), and writes `texans_game_data.csv`. This is the source of truth; `texans.db`'s `games` table mirrors its schema/columns.
2. **`explore_data.py`** — reads the CSV and prints data-quality/summary output to stdout only (no file output).
3. **`visualize.py`** — reads the CSV and produces the 4 PNG charts described in the README, using the Texans brand colors `TEXANS_BLUE = '#03224C'` and `TEXANS_RED = '#C41230'` for consistency across charts.

Regenerating `texans_game_data.csv` via `create_data.py` will produce identical data (fixed seed), but if the schema/columns change, `texans.db` and the chart scripts must be updated to match.

## Conventions

- Keep the `TEXANS_BLUE`/`TEXANS_RED` palette when adding or editing charts in `visualize.py`, matching the existing brand styling.
- The README's "Files" table and "Key Findings" describe the current state of the analysis — update `README.md` when scripts or findings change materially (e.g., new charts, updated numbers).
