# represents Five Thirty Eight entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLFiveThirtyEightEntity(BaseModel):
    event_date: str
    season: int
    neutral: int
    playoff: Optional[str] = None 
    tm_nano: str
    tm_market: str
    tm_name: str
    tm_alias: str
    tm_alt_alias: str
    opp_nano: str
    opp_market: str
    opp_name: str
    opp_alias: str
    opp_alt_alias: str
    tm_score: int
    opp_score: int
    tm_elo_pre: float
    opp_elo_pre: float
    tm_elo_win_prob: float
    opp_elo_win_prob: float
    tm_elo_post: float
    opp_elo_post: float
    tm_qb_elo_pre: float
    opp_qb_elo_pre: float
    tm_qb: str
    opp_qb: str
    tm_qb_elo_value_pre: float
    opp_qb_elo_value_pre: float
    tm_qb_elo_adj: float
    opp_qb_elo_adj: float
    tm_qb_elo_win_prob: float
    opp_qb_elo_win_prob: float
    tm_qb_game_value: float
    opp_qb_game_value: float
    team_qb_post_game_value: float
    opp_qb_post_game_value: float
    team_qb_elo_post_game: float
    opp_qb_elo_post_game: float
    quality: int
    importance: Optional[int] = None
    total_rating: Optional[int] = None
    