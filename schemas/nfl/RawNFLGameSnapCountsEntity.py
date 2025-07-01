# represents Game Snap Counts entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel

class RawNFLGameSnapCountsEntity(BaseModel):
    season: int
    event_date: str
    nano: str
    market: str
    name: str
    alias: str
    player_href: str
    player: str
    position: str
    snap_count_offense: int
    snap_count_offense_pct: float
    snap_count_defense: int
    snap_count_defense_pct: float
    snap_count_special_teams: int
    snap_count_special_teams_pct: float
    boxscore_stats_link: str
    