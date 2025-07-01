# represents Scoring Event entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLScoringEventEntity(BaseModel):
    season: int
    event_date: str
    tm_nano: str
    tm_market: str
    tm_name: str
    tm_alias: str
    opp_nano: str
    opp_market: str
    opp_name: str
    opp_alias: str
    scoring_order: int
    quarter: int
    time: int
    scoring_team: str
    tm_score: int
    tm_score_margin: int
    opp_score: int
    opp_score_margin: int
    description: str
    boxscore_stats_link: str
    