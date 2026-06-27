import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('texans_game_data.csv')

sns.set_theme(style='whitegrid')
TEXANS_BLUE = '#03224C'
TEXANS_RED = '#C41230'

# -----------------------------------------------
# CHART 1: Total ticket revenue by season
# -----------------------------------------------
revenue_by_season = df.groupby('season')['total_ticket_revenue'].sum() / 1_000_000

plt.figure(figsize=(8, 5))
bars = plt.bar(
    revenue_by_season.index.astype(str),
    revenue_by_season.values,
    color=[TEXANS_BLUE, TEXANS_RED, TEXANS_BLUE]
)
plt.title('Total Ticket Revenue by Season (in Millions)', fontsize=14, fontweight='bold')
plt.xlabel('Season')
plt.ylabel('Revenue ($M)')
for bar, val in zip(bars, revenue_by_season.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
             f'${val:.1f}M', ha='center', fontsize=11)
plt.tight_layout()
plt.savefig('chart1_revenue_by_season.png', dpi=150)
plt.show()
print("✅ Chart 1 saved")

# -----------------------------------------------
# CHART 2: Average attendance by opponent
# -----------------------------------------------
att_by_opp = df.groupby('opponent')['tickets_sold'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=att_by_opp.index, y=att_by_opp.values, palette='Blues_r')
plt.title('Average Attendance by Opponent', fontsize=14, fontweight='bold')
plt.xlabel('Opponent')
plt.ylabel('Avg Tickets Sold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart2_attendance_by_opponent.png', dpi=150)
plt.show()
print("✅ Chart 2 saved")

# -----------------------------------------------
# CHART 3: Occupancy rate by game with threshold line
# -----------------------------------------------
plt.figure(figsize=(12, 5))
colors = [TEXANS_RED if x < 0.85 else TEXANS_BLUE for x in df['occupancy_rate']]
plt.bar(df['game_id'], df['occupancy_rate'] * 100, color=colors)
plt.axhline(y=85, color='black', linestyle='--', linewidth=2, label='85% threshold')
plt.title('Stadium Occupancy Rate by Game', fontsize=14, fontweight='bold')
plt.xlabel('Game ID')
plt.ylabel('Occupancy Rate (%)')
plt.legend()
plt.tight_layout()
plt.savefig('chart3_occupancy_by_game.png', dpi=150)
plt.show()
print("✅ Chart 3 saved")

# -----------------------------------------------
# CHART 4: Sponsorship revenue vs digital impressions
# -----------------------------------------------
colors_season = {2021: TEXANS_BLUE, 2022: TEXANS_RED, 2023: 'gray'}

plt.figure(figsize=(8, 5))
for season, group in df.groupby('season'):
    plt.scatter(
        group['digital_impressions'] / 1_000_000,
        group['sponsorship_revenue'] / 1_000,
        label=str(season),
        color=colors_season[season],
        s=80,
        alpha=0.8
    )
plt.title('Sponsorship Revenue vs. Digital Impressions', fontsize=14, fontweight='bold')
plt.xlabel('Digital Impressions (Millions)')
plt.ylabel('Sponsorship Revenue ($K)')
plt.legend(title='Season')
plt.tight_layout()
plt.savefig('chart4_sponsorship_vs_digital.png', dpi=150)
plt.show()
print("✅ Chart 4 saved")

print("\n🎉 All 4 charts saved to your project folder!")