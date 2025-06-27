from pydantic import BaseModel
from typing import List, Optional

PRED_PLAYER_IDS = [
    "f7ca293e-6cce-49ba-a635-cd52375b9532", # charvin13
    "b16d580e-087c-4cbd-83ee-e9d8e3a8f84c", # Goodnight M00n
    "36000630-da35-4df4-af3d-fe41c0681df1", # Havingfun73566
    "23df91be-cb50-4f09-99d6-38f600676492", # psychomain
    "a5771e4a-facd-4d1d-947e-e9b601c59ed9", # Shammey
    "4e7a979b-c335-4c73-b154-da4438f57159", # socerfanatic95
    "c5744def-6d38-4aca-97fa-d38c48bd4c06", # Zovengrogg
]

# Database entity for normalized player data
class PredPlayerEntity(BaseModel):
    id: str
    display_name: str
    region: str
    leaderboard_rank: Optional[int] = None
    top_percentage: Optional[float] = None
    vp_total: int
    vp_current: int
    is_active: bool
    rank: int
    rank_title: str
    rank_image: str

    @classmethod
    def from_response(cls, response: 'PredPlayerResponse') -> 'PredPlayerEntity':
        """
        Create a PredPlayerEntity from a PredPlayerResponse.
        Excludes the flags field which is not part of the entity.
        """
        return cls(
            id=response.id,
            display_name=response.display_name,
            region=response.region,
            leaderboard_rank=response.leaderboard_rank,
            top_percentage=response.top_percentage,
            vp_total=response.vp_total,
            vp_current=response.vp_current,
            is_active=response.is_active,
            rank=response.rank,
            rank_title=response.rank_title,
            rank_image=response.rank_image
        )

# API Response model for deserializing player API data
class PredPlayerResponse(BaseModel):
    id: str
    display_name: str
    region: str
    leaderboard_rank: Optional[int] = None
    top_percentage: Optional[float] = None
    vp_total: int
    vp_current: int
    is_active: bool
    rank: int
    rank_title: str
    rank_image: str
    flags: List[str]
