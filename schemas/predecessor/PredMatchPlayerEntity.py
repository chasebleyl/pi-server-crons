from pydantic import BaseModel
from typing import List, Optional

class PredMatchPlayerEntity(BaseModel):
    # Foreign keys
    match_id: str  # Foreign key to PredMatchEntity
    player_id: str # Foreign key to PredPlayerEntity
    hero_id: int   # Foreign key to PredHeroEntity
    
    # Match context
    team: str
    role: str
    
    # Combat stats
    kills: int
    deaths: int
    assists: int
    largest_killing_spree: int
    largest_multi_kill: int
    objective_kills: int
    
    # Minion stats
    minions_killed: int
    lane_minions_killed: int
    neutral_minions_killed: int
    neutral_minions_team_jungle: int
    neutral_minions_enemy_jungle: int
    
    # Damage stats
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
    
    # Damage taken stats
    total_damage_taken: int
    physical_damage_taken: int
    magical_damage_taken: int
    true_damage_taken: int
    total_damage_taken_from_heroes: int
    physical_damage_taken_from_heroes: int
    magical_damage_taken_from_heroes: int
    true_damage_taken_from_heroes: int
    total_damage_mitigated: int
    
    # Healing and utility stats
    total_healing_done: int
    item_healing_done: int
    crest_healing_done: int
    utility_healing_done: int
    total_shielding_received: int
    
    # Vision stats
    wards_placed: int
    wards_destroyed: int
    
    # Economy stats
    gold_earned: int
    gold_spent: int
    gold_earned_at_interval: List[int]
    inventory_data: List[int]
    
    # Performance stats
    performance_score: Optional[float] = None
    performance_title: Optional[str] = None
    vp: Optional[int] = None
    rank: Optional[int] = None
    rank_new: Optional[int] = None
    vp_total: int
    vp_change: int
    
    # Level stats
    hero_level: int
    level: int
