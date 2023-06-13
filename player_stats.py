from nba_api.stats.static import players
from nba_api.stats.endpoints import playerdashboardbyyearoveryear

# 선수 이름으로 선수 ID 가져오기
player_name = 'LeBron James'
player_info = players.find_players_by_full_name(player_name)
player_id = player_info[0]['id']

# 해당 선수의 전체 경기 평균 기록 가져오기
player_dashboard = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id)
player_dashboard = player_dashboard.get_data_frames()[0]

# 선수의 전체 경기 평균 기록 출력
print(f"선수 이름: {player_name}")
print("전체 경기 평균 기록:")
print(player_dashboard)

############################################################################################################

# 선수 이름으로 선수 ID 가져오기
player_name = 'LeBron James'
player_info = players.find_players_by_full_name(player_name)
player_id = player_info[0]['id']

# 해당 선수의 전체 시즌 평균 스탯 가져오기
player_dashboard = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player_id)
player_stats = player_dashboard.get_data_frames()[1]

# 평균 득점 계산
average_points = player_stats['PTS'].mean()

# 슛 성공률 계산
field_goal_percentage = player_stats['FG_PCT'].mean()

# 선수의 평균 득점 및 슛 성공률 출력
print(f"선수 이름: {player_name}")
print("평균 득점:", average_points)
print("슛 성공률:", field_goal_percentage)
