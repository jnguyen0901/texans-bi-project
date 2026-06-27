import pandas as pd
import numpy as np

np.random.seed(42)

num_games = 27

games = pd.DataFrame({
    'game_id': range(1, num_games + 1),
    'season': ([2021] * 9 + [2022] * 9 + [2023] * 9),
    'week': list(range(1, 10)) * 3,
    'opponent': [
        'Chiefs', 'Ravens', 'Cowboys', 'Eagles', 'Bills',
        'Bengals', 'Chargers', 'Steelers', 'Patriots',
        'Cowboys', 'Bills', 'Chiefs', 'Dolphins', 'Broncos',
        'Raiders', 'Ravens', 'Titans', 'Colts',
        'Eagles', 'Chiefs', 'Bengals', 'Cowboys', 'Jaguars',
        'Titans', 'Colts', 'Patriots', 'Steelers'
    ],
    'day_of_week': np.random.choice(
        ['Sunday', 'Monday', 'Thursday'],
        num_games, p=[0.70, 0.20, 0.10]
    ),
    'tickets_sold': np.random.randint(56000, 72220, num_games),
    'capacity': 72220,
    'avg_ticket_price': np.random.uniform(90, 310, num_games).round(2),
    'sponsorship_revenue': np.random.uniform(250000, 850000, num_games).round(2),
    'digital_impressions': np.random.randint(600000, 3500000, num_games),
})

games['occupancy_rate'] = (games['tickets_sold'] / games['capacity']).round(3)
games['total_ticket_revenue'] = (games['tickets_sold'] * games['avg_ticket_price']).round(2)
games['revenue_per_impression'] = (games['sponsorship_revenue'] / games['digital_impressions']).round(4)

games.to_csv('texans_game_data.csv', index=False)

print("✅ Data created successfully!")
print(f"\nShape: {games.shape[0]} rows, {games.shape[1]} columns")
print("\nFirst 5 rows:")
print(games.head())