from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandingsv3

# 팀 정보 가져오기
team_info = teams.get_teams()

# 팀 ID 가져오기
team_ids = [team['id'] for team in team_info]

# 현재 시즌 팀 순위 가져오기
standings = leaguestandingsv3.LeagueStandingsV3(season='2022-23')
standings = standings.get_data_frames()[0]

print(standings)