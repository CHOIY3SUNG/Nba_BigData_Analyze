from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats

# 팀 코드와 시즌 연도 설정
team_id = teams.find_teams_by_full_name("Boston Celtics")[0]["id"]
season = "2020-21"

# 팀의 시즌별 스탯 가져오기
team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
team_stats_df = team_stats.get_data_frames()[0]

# 특정 시즌의 스탯 가져오기
season_stats = team_stats_df[team_stats_df["YEAR"] == season]

# 데이터를 보기 쉽게 출력
for index, row in season_stats.iterrows():
    print("Season:", row["YEAR"])
    print("Field Goal Percentage:", row["FG_PCT"])
    print("3-Point Attempts:", row["FG3A"])
    print("2-Point Attempts:", row["FGA"])
    print("Rebounds:", row["REB"])
    print("Turnovers:", row["TOV"])
    print("Personal Fouls:", row["PF"])
    print("Points:", row["PTS"])
    print("Wins:", row["WINS"])
    print("Losses:", row["LOSSES"])
    print("Win Percentage:", row["WIN_PCT"])
    print("-------------------------------------")
    print(row)
