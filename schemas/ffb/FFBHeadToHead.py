from typing import List, Dict, Any

# Mock FFB API response for a head-to-head matchup
# This is a simplified example
ffb_head_to_head_response: Dict[str, Any] = {
    "matchup_id": "ffb_12345",
    "week": 1,
    "teams": [
        {
            "team_id": "team_a",
            "points": 120.5,
            "players": [
                {"player_id": "p1", "score": 25.5},
                {"player_id": "p2", "score": 15.0}
            ]
        },
        {
            "team_id": "team_b",
            "points": 110.0,
            "players": [
                {"player_id": "p3", "score": 22.0},
                {"player_id": "p4", "score": 18.5}
            ]
        }
    ]
}
