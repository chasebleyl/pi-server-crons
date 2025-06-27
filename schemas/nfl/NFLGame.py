from typing import Dict, Any

# Mock NFL API response for a single game
# This is a simplified example
nfl_game_response: Dict[str, Any] = {
    "game_id": "nfl_67890",
    "date": "2025-09-07",
    "home_team": {
        "name": "Green Bay Packers",
        "score": 28,
        "stats": {"passing_yards": 300, "rushing_yards": 150}
    },
    "away_team": {
        "name": "Chicago Bears",
        "score": 21,
        "stats": {"passing_yards": 250, "rushing_yards": 100}
    }
}
