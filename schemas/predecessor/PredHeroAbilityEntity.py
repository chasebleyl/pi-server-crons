from pydantic import BaseModel
from typing import List, Union

class PredHeroAbilityEntity(BaseModel):
    hero_id: int  # Foreign key to PredHeroEntity
    display_name: str
    image: str
    game_description: str
    menu_description: str
    cooldown: List[Union[int, float]]
    cost: List[Union[int, float]]
    key: str 