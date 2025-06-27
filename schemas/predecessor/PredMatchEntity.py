from pydantic import BaseModel, Field
from typing import List, Optional, Any
import datetime

# Database entity for normalized match data
class PredMatchEntity(BaseModel):
    id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    game_duration: int
    game_region: str
    region: str
    winning_team: str
    game_mode: str

# API Response models for deserializing API data
class PredPlayerStatsResponse(BaseModel):
    id: str
    display_name: str = Field(..., alias='display_name')
    flags: List[str]
    team: str
    hero_id: int
    role: str
    minions_killed: int
    lane_minions_killed: int
    neutral_minions_killed: int
    neutral_minions_team_jungle: int
    neutral_minions_enemy_jungle: int
    kills: int
    deaths: int
    assists: int
    largest_killing_spree: int
    largest_multi_kill: int
    total_damage_dealt: int
    physical_damage_dealt: int
    magical_damage_dealt: int
    true_damage_dealt: int
    largest_critical_strike: int
    total_damage_dealt_to_heroes: int
    physical_damage_dealt_to_heroes: int
    magical_damage_dealt_to_heroes: int
    true_damage_dealt_to_heroes: int
    total_damage_dealt_to_structures: int
    total_damage_dealt_to_objectives: int
    total_damage_taken: int
    physical_damage_taken: int
    magical_damage_taken: int
    true_damage_taken: int
    total_damage_taken_from_heroes: int
    physical_damage_taken_from_heroes: int
    magical_damage_taken_from_heroes: int
    true_damage_taken_from_heroes: int
    total_damage_mitigated: int
    total_healing_done: int
    item_healing_done: int
    crest_healing_done: int
    utility_healing_done: int
    total_shielding_received: int
    wards_placed: int
    wards_destroyed: int
    gold_earned: int
    gold_spent: int
    gold_earned_at_interval: List[int]
    inventory_data: List[int]
    performance_score: Optional[float] = None
    performance_title: Optional[str] = None
    vp: Optional[int] = None
    rank: Optional[int] = None
    rank_new: Optional[int] = None
    vp_total: int
    hero_level: int
    level: int
    objective_kills: int
    vp_change: int

class PredMatchResponse(BaseModel):
    id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    game_duration: int
    game_region: str
    region: str
    winning_team: str
    game_mode: str
    players: List[PredPlayerStatsResponse]

class PredPlayerMatchesResponseEntity(BaseModel):
    matches: List[PredMatchResponse]