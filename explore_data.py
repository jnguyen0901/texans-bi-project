import pandas as pd

df = pd.read_csv('texans_game_data.csv')

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n" + "=" * 50)
print("MISSING VALUES (data quality check)")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)
print(df.describe().round(2))

print("\n" + "=" * 50)
print("GAMES PER SEASON")
print("=" * 50)
print(df['season'].value_counts().sort_index())

print("\n" + "=" * 50)
print("GAMES BY DAY OF WEEK")
print("=" * 50)
print(df['day_of_week'].value_counts())