# represents Expected Points entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLExpectedPointsEntity(BaseModel):
    season: int
    event_date: str
    nano: str
    market: str
    name: str
    alias: str
    exp_pts: float
    exp_pts_off: float
    exp_pts_off_pass: float
    exp_pts_off_rush: float
    exp_pts_off_turnover: float
    exp_pts_def: float
    exp_pts_def_pass: float
    exp_pts_def_rush: float
    exp_pts_def_turnover: float
    exp_pts_st: float
    exp_pts_kickoff: float
    exp_pts_kick_return: float
    exp_pts_punt: float
    exp_pts_punt_return: float
    exp_pts_fg_xp: float
    boxscore_stats_link: str
    