from pydantic import BaseModel
from typing import List, Dict, Any

class RawFFBPlayer(BaseModel):
    player_id: str
    score: float

class RawFFBTeam(BaseModel):
    team_id: str
    points: float
    players: List[RawFFBPlayer]

class RawFFBHeadToHeadEntity(BaseModel):
    matchup_id: str
    week: int
    teams: List[RawFFBTeam]
