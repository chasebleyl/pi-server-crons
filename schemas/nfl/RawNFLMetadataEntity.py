# represents Metadata entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLMetadataEntity(BaseModel):
    season: int
    event_date: str
    game_time: str
    tm_nano: str
    tm_market: str
    tm_name: str
    tm_alias: str 
    opp_nano: str 
    opp_market: str 
    opp_name: str
    opp_alias: str
    tm_spread: float
    opp_spread: float
    total: float
    attendance: int
    duration: int
    roof_type: Optional[str] = None
    surface_type: Optional[str] = None
    won_toss: str
    won_toss_decision: str
    won_toss_overtime: Optional[str] = None
    temperature: Optional[int] = None
    humidity_pct: Optional[int] = None
    wind_speed: Optional[int] = None
    boxscore_stats_link: str
    