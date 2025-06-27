from pydantic import BaseModel
from typing import Optional

class PredItemEffectEntity(BaseModel):
    item_id: int  # Foreign key to PredItemEntity
    name: str
    active: bool
    condition: Optional[str]
    cooldown: Optional[str]
    menu_description: Optional[str] 