from pydantic import BaseModel

class NFLGameEntity(BaseModel):
    game_id: str
    date: str
    home_team_name: str
    away_team_name: str
    home_score: int
    away_score: int
    home_passing_yards: int
    home_rushing_yards: int
    away_passing_yards: int
    away_rushing_yards: int
