from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Import separate entities for database normalization
from .PredItemEffectEntity import PredItemEffectEntity

class PredItemEntity(BaseModel):
    id: int
    game_id: int
    name: str
    display_name: str
    image: str
    price: Optional[int]
    total_price: int
    slot_type: str
    rarity: Optional[str]
    aggression_type: Optional[str]
    hero_class: Optional[str]
    required_level: Optional[int]
    # Stats can be stored as a JSONB field in PostgreSQL
    stats: Optional[Dict[str, Any]]
    effects: List[PredItemEffectEntity]
    requirements: List[str]
    build_paths: List[str]

    @classmethod
    def from_response(cls, response: 'PredItemResponse') -> 'PredItemEntity':
        """
        Create a PredItemEntity from a PredItemResponse.
        Maps nested response objects to their corresponding entities with foreign keys.
        """
        # Map effects to entities with item_id foreign key
        effects = [
            PredItemEffectEntity(
                item_id=response.id,
                name=effect.name,
                active=effect.active,
                condition=effect.condition,
                cooldown=effect.cooldown,
                menu_description=effect.menu_description
            )
            for effect in response.effects
        ]
        
        return cls(
            id=response.id,
            game_id=response.game_id,
            name=response.name,
            display_name=response.display_name,
            image=response.image,
            price=response.price,
            total_price=response.total_price,
            slot_type=response.slot_type,
            rarity=response.rarity,
            aggression_type=response.aggression_type,
            hero_class=response.hero_class,
            required_level=response.required_level,
            stats=response.stats,
            effects=effects,
            requirements=response.requirements,
            build_paths=response.build_paths
        )

# Denormalized version for API responses (without foreign keys)
class PredItemEffectResponse(BaseModel):
    name: str
    active: bool
    condition: Optional[str]
    cooldown: Optional[str]
    menu_description: Optional[str]

class PredItemResponse(BaseModel):
    id: int
    game_id: int
    name: str
    display_name: str
    image: str
    price: Optional[int]
    total_price: int
    slot_type: str
    rarity: Optional[str]
    aggression_type: Optional[str]
    hero_class: Optional[str]
    required_level: Optional[int]
    stats: Optional[Dict[str, Any]]
    effects: List[PredItemEffectResponse]
    requirements: List[str]
    build_paths: List[str]
