# represents Season entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLSeasonRecordEntity(BaseModel):
    status: str 
    season: int
    week: int
    week_day: str
    event_date: str
    game_time: str
    tm_nano: str
    tm_market: str
    tm_name: str
    tm_alias: str 
    tm_alt_market: str 
    tm_alt_alias: str 
    opp_nano: str 
    opp_market: str 
    opp_name: str
    opp_alias: str
    opp_alt_market: str
    opp_alt_alias: str
    tm_location: str
    opp_location: str
    tm_score: int
    opp_score: int
    boxscore_stats_link: str
    