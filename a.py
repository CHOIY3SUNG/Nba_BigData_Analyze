from nba_api.stats.endpoints import LeagueGameFinder
import result
import pandas as pd
import numpy as np

# Set the LeagueID to NBA (1)
league_id = "00"

# Retrieve all NBA games for the current season
game_finder = LeagueGameFinder(league_id_nullable=league_id)
games = game_finder.get_data_frames()[0]

# Filter games for the year 2023
games_2023 = games[games["GAME_DATE"].str[:4] == "2023"]

# Filter relevant columns for stats and outcomes
stats_and_outcomes = games_2023[
    [
        "GAME_DATE",
        "TEAM_NAME",
        "PTS",
        "FG_PCT",
        "FG3M",
        "FG3A",
        "FG3_PCT",
        "FTM",
        "FTA",
        "FT_PCT",
        "OREB",
        "DREB",
        "REB",
        "AST",
        "STL",
        "BLK",
        "TOV",
        "PF",
        "FGA",
        "WL",
    ]
]

# Replace "W" with 1 and "L" with 0 in the WL column
stats_and_outcomes["WL"] = stats_and_outcomes["WL"].replace({"W": 1, "L": 0})

# Filter for win games
win_games = stats_and_outcomes[stats_and_outcomes["WL"] == 1]

# Filter for loss games
loss_games = stats_and_outcomes[stats_and_outcomes["WL"] == 0]


game_data = pd.DataFrame(
    {
        "AST": [i for i in win_games["AST"]],
        "REB": [i for i in win_games["REB"]],
        "TOV": [i for i in win_games["TOV"]],
        "FG_PCT": [i for i in win_games["FG_PCT"]],
        "FG3A": [i for i in win_games["FG3A"]],
        "FGA": [i for i in win_games["FGA"]],
        "PF": [i for i in win_games["PF"]],
        "BLK": [i for i in win_games["BLK"]],
    }
)

game_data_l = pd.DataFrame(
    {
        "AST": [i for i in loss_games["AST"]],
        "REB": [i for i in loss_games["REB"]],
        "TOV": [i for i in loss_games["TOV"]],
        "FG_PCT": [i for i in loss_games["FG_PCT"]],
        "FG3A": [i for i in loss_games["FG3A"]],
        "FGA": [i for i in loss_games["FGA"]],
        "PF": [i for i in loss_games["PF"]],
        "BLK": [i for i in loss_games["BLK"]],
    }
)


def printf(game):
    res = result.predict_game_outcomes(game)
    w = 0
    l = 0

    for i in res:
        if i == "W":
            w += 1
        else:
            l += 1

    print(f"승리 : {w}\n패배 : {l}\n ")


printf(game_data)
