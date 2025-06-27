from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Union

# Import separate entities for database normalization
from .PredHeroAbilityEntity import PredHeroAbilityEntity
from .PredHeroBaseStatsEntity import PredHeroBaseStatsEntity

class PredHeroEntity(BaseModel):
    id: int
    game_id: Optional[int]
    name: str
    display_name: str
    image: str
    stats: List[int]  # [10, 2, 1, 1] format
    classes: List[str]
    roles: List[str]
    abilities: List[PredHeroAbilityEntity]
    base_stats: PredHeroBaseStatsEntity

    @classmethod
    def from_response(cls, response: 'PredHeroResponse') -> 'PredHeroEntity':
        """
        Create a PredHeroEntity from a PredHeroResponse.
        Maps nested response objects to their corresponding entities with foreign keys.
        """
        # Map abilities to entities with hero_id foreign key
        abilities = [
            PredHeroAbilityEntity(
                hero_id=response.id,
                display_name=ability.display_name,
                image=ability.image,
                game_description=ability.game_description,
                menu_description=ability.menu_description,
                cooldown=ability.cooldown,
                cost=ability.cost,
                key=ability.key
            )
            for ability in response.abilities
        ]
        
        # Map base_stats to entity with hero_id foreign key
        base_stats = PredHeroBaseStatsEntity(
            hero_id=response.id,
            max_health=response.base_stats.max_health,
            base_health_regeneration=response.base_stats.base_health_regeneration,
            max_mana=response.base_stats.max_mana,
            base_mana_regeneration=response.base_stats.base_mana_regeneration,
            attack_speed=response.base_stats.attack_speed,
            physical_armor=response.base_stats.physical_armor,
            magical_armor=response.base_stats.magical_armor,
            basic_attack_time=response.base_stats.basic_attack_time,
            physical_power=response.base_stats.physical_power,
            base_movement_speed=response.base_stats.base_movement_speed,
            cleave=response.base_stats.cleave,
            attack_range=response.base_stats.attack_range
        )
        
        return cls(
            id=response.id,
            game_id=response.game_id,
            name=response.name,
            display_name=response.display_name,
            image=response.image,
            stats=response.stats,
            classes=response.classes,
            roles=response.roles,
            abilities=abilities,
            base_stats=base_stats
        )

# Denormalized version for API responses (without foreign keys)
class PredHeroAbilityResponse(BaseModel):
    display_name: str
    image: str
    game_description: str
    menu_description: str
    cooldown: List[Union[int, float]]
    cost: List[Union[int, float]]
    key: str

class PredHeroBaseStatsResponse(BaseModel):
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

class PredHeroResponse(BaseModel):
    id: int
    game_id: Optional[int]
    name: str
    display_name: str
    image: str
    stats: List[int]
    classes: List[str]
    roles: List[str]
    abilities: List[PredHeroAbilityResponse]
    base_stats: PredHeroBaseStatsResponse
