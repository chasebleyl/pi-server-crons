# represents Boxscore Statistics entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLBoxscoreStatsEntity(BaseModel):
    season: int
    event_date: str
    nano: str
    market: str
    name: str
    alias: str
    rush_att: int
    rush_yds: int
    rush_tds: int
    pass_cmp: int
    pass_att: int
    pass_cmp_pct: float
    pass_yds: int
    pass_tds: int
    pass_int: int
    passer_rating: float
    net_pass_yds: int
    total_yds: int
    times_sacked: int
    yds_sacked_for: int
    fumbles: int
    fumbles_lost: int
    turnovers: int
    penalties: int
    penalty_yds: int
    first_downs: int
    third_down_conv: int
    third_down_att: int
    third_down_conv_pct: float
    fourth_down_conv: int
    fourth_down_att: int
    fourth_down_conv_pct: float
    time_of_possession: int
    boxscore_stats_link: str
    