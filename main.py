from nba_api.stats.endpoints import LeagueGameFinder
import pandas as pd

# Set the LeagueID to NBA (1)
league_id = '00'

# Retrieve all NBA games for the current season
game_finder = LeagueGameFinder(league_id_nullable=league_id)
games = game_finder.get_data_frames()[0]

# Filter relevant columns for stats and outcomes
stats_and_outcomes = games[['GAME_DATE', 'TEAM_NAME', 'PTS', 'AST', 'REB', 'TOV', 'FG_PCT', 'FG3A', 'FGA', 'PF', 'BLK', 'WL']]

# Print the statistics and outcomes
print(stats_and_outcomes)

# Filter data for the past three seasons
recent_stats = stats_and_outcomes[stats_and_outcomes['GAME_DATE'].str[:4].astype(int) >= 2020]

# Calculate average statistics for winning and losing games
avg_stats = recent_stats.groupby('WL').mean()

# Calculate the difference between average statistics of winning and losing games
diff_stats = avg_stats.loc['W'] - avg_stats.loc['L']

# Sort the differences in descending order
sorted_diff_stats = diff_stats.abs().sort_values(ascending=False)

# Print the differences in descending order
print("Difference in Average Statistics (Winning - Losing):")
for stat in sorted_diff_stats.index:
    print(f"{stat}: {diff_stats[stat]}")


