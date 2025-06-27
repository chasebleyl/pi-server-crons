from pydantic import BaseModel
from typing import List, Optional

class RawPredMatch(BaseModel):
    """Raw match data from API response."""
    id: str
    date: str
    duration: int
    map: str
    mode: str
    result: str
    score: str
    hero: str
    kills: int
    deaths: int
    assists: int
    cs: int
    gold: int
    damage: int
    healing: int
    damage_taken: int
    wards_placed: int
    wards_destroyed: int

class RawPredPlayerStats(BaseModel):
    """Raw player statistics from API response."""
    kills: int
    deaths: int
    assists: int
    cs: int
    gold: int
    damage: int
    healing: int
    damage_taken: int
    wards_placed: int
    wards_destroyed: int

class RawPredPlayerMatchesEntity(BaseModel):
    """Raw player matches entity from API response."""
    player_id: str
    matches: List[RawPredMatch]
    total_matches: int
    win_rate: float
    average_kills: float
    average_deaths: float
    average_assists: float
    average_cs: float
    average_gold: float
    average_damage: float
    average_healing: float
    average_damage_taken: float
    average_wards_placed: float
    average_wards_destroyed: float 