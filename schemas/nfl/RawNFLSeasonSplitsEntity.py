# represents Season Splits entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel
from typing import List, Optional

class RawNFLSeasonSplitsEntity(BaseModel):
    season: int
    nano: str
    market: str
    name: str
    alias: str
    splits_by: str
    splits_type: str
    splits_side: str
    total_plays: int  # NOT nullable; if 0, that means the rest are null
    yds_to_go: Optional[float] = None
    avg_yds_gained: Optional[float] = None
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_yds_per_att: Optional[float] = None
    rush_tds: Optional[int] = None
    rush_first_downs: Optional[int] = None
    pass_cmp: Optional[int] = None
    pass_cmp_pct: Optional[float] = None
    pass_att: Optional[int] = None
    pass_yds: Optional[int] = None
    pass_yds_per_att: Optional[float] = None
    pass_adj_net_yds_per_att: Optional[float] = None
    pass_int: Optional[int] = None
    pass_tds: Optional[int] = None
    pass_first_downs: Optional[int] = None
    passer_rating: Optional[float] = None
    times_sacked: Optional[int] = None
    boxscore_stats_link: str
    