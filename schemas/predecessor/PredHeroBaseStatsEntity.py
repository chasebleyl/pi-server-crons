from pydantic import BaseModel
from typing import List, Union

class PredHeroBaseStatsEntity(BaseModel):
    hero_id: int  # Foreign key to PredHeroEntity
    max_health: List[Union[int, float]]
    base_health_regeneration: List[Union[int, float]]
    max_mana: List[Union[int, float]]
    base_mana_regeneration: List[Union[int, float]]
    attack_speed: List[Union[int, float]]
    physical_armor: List[Union[int, float]]
    magical_armor: List[Union[int, float]]
    basic_attack_time: List[Union[int, float]]
    physical_power: List[Union[int, float]]
    base_movement_speed: List[Union[int, float]]
    cleave: List[Union[int, float]]
    attack_range: List[Union[int, float]] 