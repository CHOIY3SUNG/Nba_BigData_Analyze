import pandas as pd
from nba_api.stats.endpoints import LeagueGameFinder

# Set the LeagueID to NBA (1)
league_id = "00"

# Retrieve all NBA games for the current season
game_finder = LeagueGameFinder(league_id_nullable=league_id)
games = game_finder.get_data_frames()[0]

# Filter relevant columns for stats and outcomes
stats_and_outcomes = games[
    [
        "GAME_DATE",
        "TEAM_NAME",
        "PTS",
        "AST",
        "REB",
        "TOV",
        "FG_PCT",
        "FG3A",
        "FGA",
        "PF",
        "BLK",
        "WL",
    ]
]

# Replace "W" with 1 and "L" with 0 in the WL column
stats_and_outcomes["WL"] = stats_and_outcomes["WL"].replace({"W": 1, "L": 0})

# Save the statistics and outcomes as a CSV file
# stats_and_outcomes.to_csv("nba_stats.csv", index=False)

print(stats_and_outcomes)
