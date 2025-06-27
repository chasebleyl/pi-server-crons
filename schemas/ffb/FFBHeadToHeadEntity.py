from pydantic import BaseModel
from typing import List

class FFBPlayerEntity(BaseModel):
    player_id: str
    score: float
    team_id: str # Denormalized for easier querying
    matchup_id: str # Denormalized for easier querying

class FFBTeamEntity(BaseModel):
    team_id: str
    points: float
    matchup_id: str # Denormalized for easier querying

class FFBHeadToHeadEntity(BaseModel):
    matchup_id: str
    week: int
