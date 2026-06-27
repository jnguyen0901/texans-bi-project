# Houston Texans — Business Intelligence Portfolio Project

## Project Summary
Analyzed 3 seasons of NFL ticket sales, attendance, and sponsorship 
data to surface actionable business insights for the Houston Texans 
organization using Python, SQL, and Tableau.

## Business Questions Answered
- Is ticket revenue growing season over season?
- Which opponent matchups drive the highest attendance and revenue?
- Which games fell below 85% capacity and need a promotion strategy?
- How does digital reach correlate with sponsorship revenue?

## Key Findings
- Ticket revenue grew 22% from 2021 to 2023 ($108M to $132M)
- Monday Night games have highest attendance but lowest revenue — underpriced by $5.4M vs Sunday games
- 5 games fell below 85% occupancy — Bengals and Ravens matchups consistently underperform
- Ravens game generates highest digital impressions but lowest sponsorship revenue per impression

## Tools Used
- Python (Pandas, Matplotlib, Seaborn) — data creation, cleaning, visualization
- SQL (SQLite) — 5 business analysis queries
- Tableau Public — interactive executive dashboard

## Tableau Dashboard
[View Live Dashboard Here](https://public.tableau.com/app/profile/dung.nguyen1105/viz/HoustonTexansBIDashboard/Dashboard1)

## Files
| File | Description |
|---|---|
| create_data.py | Generates simulated NFL game dataset |
| explore_data.py | Data quality checks and exploration |
| visualize.py | Creates 4 business charts in Texans colors |
| texans_game_data.csv | Dataset — 27 games across 3 seasons |
