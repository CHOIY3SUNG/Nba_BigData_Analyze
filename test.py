from nba_api.stats.endpoints import LeagueGameFinder
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set the LeagueID to NBA (1)
league_id = '00'

# Retrieve all NBA games for the current season
game_finder = LeagueGameFinder(league_id_nullable=league_id)
games = game_finder.get_data_frames()[0]

# Filter relevant columns for stats and outcomes
stats_and_outcomes = games[['GAME_DATE', 'TEAM_NAME', 'PTS', 'AST', 'REB', 'TOV', 'FG_PCT', 'FG3A', 'FGA', 'PF', 'BLK', 'WL']]

# Drop rows with missing values
stats_and_outcomes = stats_and_outcomes.dropna()

# Separate features and target variable
X = stats_and_outcomes[['AST', 'REB', 'TOV', 'FG_PCT', 'FG3A', 'FGA', 'PF', 'BLK']]
y = stats_and_outcomes['WL']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predict the outcomes for test set
y_pred = model.predict(X_test_scaled)

# Calculate the accuracy of the model
accuracy = (y_pred == y_test).mean()
print("Accuracy:", accuracy)

# Example game data for prediction
game_data = pd.DataFrame({
    'AST': [21, 18],
    'REB': [57, 44],
    'TOV': [14, 8],
    'FG_PCT': [0.451, 0.344],
    'FG3A': [28, 35],
    'FGA': [84, 96],
    'PF': [13, 21],
    'BLK': [7, 7]
})

# Scale the game data
game_data_scaled = scaler.transform(game_data)

# Predict the outcomes for game data
game_prediction = model.predict(game_data_scaled)
print("Game Prediction:", game_prediction)
