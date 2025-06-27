from pydantic import BaseModel
from typing import Dict

class RawNFLTeamStats(BaseModel):
    passing_yards: int
    rushing_yards: int

class RawNFLTeam(BaseModel):
    name: str
    score: int
    stats: RawNFLTeamStats

class RawNFLGameEntity(BaseModel):
    game_id: str
    date: str
    home_team: RawNFLTeam
    away_team: RawNFLTeam
