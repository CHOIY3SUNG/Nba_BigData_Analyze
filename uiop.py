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

# Calculate the correlation coefficients between win rate and each statistic
correlation_coeffs = stats_and_outcomes[['PTS', 'AST', 'REB', 'TOV', 'BLK', 'PF', 'FGA', 'FG3A', 'FG_PCT', 'WL']].corr()['WL'].drop('WL')

# Find the statistic with the highest correlation coefficient
most_correlated_stat = correlation_coeffs.abs().idxmax()

# Print the most correlated statistic
print(f"The most correlated statistic with win rate is: {most_correlated_stat} (correlation coefficient: {correlation_coeffs[most_correlated_stat]})")
