# represents Game Roster entity from https://github.com/blnkpagelabs/nflscraPy

from pydantic import BaseModel

class RawNFLGameRosterEntity(BaseModel):
    season: int
    event_date: str
    nano: str
    market: str
    name: str
    alias: str
    player_href: str
    player: str
    position: str
    boxscore_stats_link: str
    