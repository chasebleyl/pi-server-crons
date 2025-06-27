import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import Database
from schemas.responses.FFBHeadToHead import ffb_head_to_head_response # Mock API response
from schemas.entities.RawFFBHeadToHeadEntity import RawFFBHeadToHeadEntity
from schemas.entities.FFBHeadToHeadEntity import FFBHeadToHeadEntity, FFBTeamEntity, FFBPlayerEntity

def hydrate_ffb_data():
    """Hydrates ffb data from an API into the database."""
    db = Database()
    try:
        db.connect()

        # 1. Fetch data from the API (using mock data here)
        api_data = ffb_head_to_head_response

        # 2. Validate the raw API data
        raw_entity = RawFFBHeadToHeadEntity(**api_data)

        # 3. Transform and normalize the data into your final entity models
        matchup_entity = FFBHeadToHeadEntity(
            matchup_id=raw_entity.matchup_id,
            week=raw_entity.week
        )

        team_entities = []
        player_entities = []
        for team in raw_entity.teams:
            team_entities.append(FFBTeamEntity(
                team_id=team.team_id,
                points=team.points,
                matchup_id=raw_entity.matchup_id
            ))
            for player in team.players:
                player_entities.append(FFBPlayerEntity(
                    player_id=player.player_id,
                    score=player.score,
                    team_id=team.team_id,
                    matchup_id=raw_entity.matchup_id
                ))

        # 4. Write the entities to the database
        # (You would have separate tables for matchups, teams, and players)
        # Example for the main matchup entity:
        db.execute_query(
            "INSERT INTO ffb_matchups (matchup_id, week) VALUES (%s, %s) ON CONFLICT (matchup_id) DO NOTHING;",
            (matchup_entity.matchup_id, matchup_entity.week)
        )

        # Example for team entities:
        for team in team_entities:
            db.execute_query(
                "INSERT INTO ffb_teams (team_id, points, matchup_id) VALUES (%s, %s, %s) ON CONFLICT (team_id, matchup_id) DO NOTHING;",
                (team.team_id, team.points, team.matchup_id)
            )

        # Example for player entities:
        for player in player_entities:
            db.execute_query(
                "INSERT INTO ffb_players (player_id, score, team_id, matchup_id) VALUES (%s, %s, %s, %s) ON CONFLICT (player_id, matchup_id) DO NOTHING;",
                (player.player_id, player.score, player.team_id, player.matchup_id)
            )

        print("Successfully hydrated FFB data.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    hydrate_ffb_data()