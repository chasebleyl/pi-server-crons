import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database_interface import DatabaseInterface
from scripts.utils_requests_interface import RequestsInterface
from schemas.predecessor.PredPlayerEntity import PRED_PLAYER_IDS, PredPlayerResponse, PredPlayerEntity
from schemas.predecessor.PredHeroEntity import PredHeroResponse, PredHeroEntity
from schemas.predecessor.PredItemEntity import PredItemResponse, PredItemEntity

URL_BASE = "https://omeda.city"
URL_HEROES = f"{URL_BASE}/heroes.json"
URL_ITEMS = f"{URL_BASE}/items.json"
URL_PLAYERS_DETAILS = f"{URL_BASE}/players/PLAYER_ID.json"
URL_PLAYERS_MATCHES = f"{URL_BASE}/players/PLAYER_ID/matches.json"

def hydrate_pred_hero_data(db: DatabaseInterface, requests_client: RequestsInterface):
    """Hydrates predecessor hero data from the API into the database."""
    try:
        db.connect()
        
        # Fetch all heroes from the heroes endpoint
        heroes_response = requests_client.get_and_deserialize(URL_HEROES, list[PredHeroResponse])
        
        for hero_response in heroes_response:
            try:
                # Map response to entity
                hero_entity = PredHeroEntity.from_response(hero_response)
                
                # TODO: UPSERT hero_entity to the database when ready for integration
                # Example for hero table:
                # db.execute_query(
                #     "INSERT INTO pred_heroes (...) VALUES (...) ON CONFLICT (id) DO UPDATE SET ...",
                #     (hero_entity.id, hero_entity.name, hero_entity.display_name, ...)
                # )
                
                # TODO: UPSERT abilities to the database when ready for integration
                # for ability in hero_entity.abilities:
                #     db.execute_query(
                #         "INSERT INTO pred_hero_abilities (...) VALUES (...) ON CONFLICT (hero_id, key) DO UPDATE SET ...",
                #         (ability.hero_id, ability.display_name, ability.key, ...)
                #     )
                
                # TODO: UPSERT base_stats to the database when ready for integration
                # db.execute_query(
                #     "INSERT INTO pred_hero_base_stats (...) VALUES (...) ON CONFLICT (hero_id) DO UPDATE SET ...",
                #     (hero_entity.base_stats.hero_id, hero_entity.base_stats.max_health, ...)
                # )
                
                print(f"Successfully processed hero: {hero_entity.display_name} (ID: {hero_entity.id})")
                
            except Exception as e:
                print(f"Error processing hero {hero_response.id if hasattr(hero_response, 'id') else 'unknown'}: {e}")
                continue
        
        print("Successfully hydrated Predecessor hero data.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.disconnect()

def hydrate_pred_item_data(db: DatabaseInterface, requests_client: RequestsInterface):
    """Hydrates predecessor item data from the API into the database."""
    try:
        db.connect()
        
        # Fetch all items from the items endpoint
        items_response = requests_client.get_and_deserialize(URL_ITEMS, list[PredItemResponse])
        
        for item_response in items_response:
            try:
                # Map response to entity
                item_entity = PredItemEntity.from_response(item_response)
                
                # TODO: UPSERT item_entity to the database when ready for integration
                # Example for item table:
                # db.execute_query(
                #     "INSERT INTO pred_items (...) VALUES (...) ON CONFLICT (id) DO UPDATE SET ...",
                #     (item_entity.id, item_entity.name, item_entity.display_name, ...)
                # )
                
                # TODO: UPSERT effects to the database when ready for integration
                # for effect in item_entity.effects:
                #     db.execute_query(
                #         "INSERT INTO pred_item_effects (...) VALUES (...) ON CONFLICT (item_id, name) DO UPDATE SET ...",
                #         (effect.item_id, effect.name, effect.active, ...)
                #     )
                
                print(f"Successfully processed item: {item_entity.display_name} (ID: {item_entity.id})")
                
            except Exception as e:
                print(f"Error processing item {item_response.id if hasattr(item_response, 'id') else 'unknown'}: {e}")
                continue
        
        print("Successfully hydrated Predecessor item data.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.disconnect()

def hydrate_pred_player_data(db: DatabaseInterface, requests_client: RequestsInterface):
    """Hydrates predecessor player data from the API into the database."""
    try:
        db.connect()
        
        for player_id in PRED_PLAYER_IDS:
            try:
                # Construct the URL for this specific player
                player_url = URL_PLAYERS_DETAILS.replace("PLAYER_ID", player_id)
                
                # Fetch and deserialize player data
                player_response = requests_client.get_and_deserialize(player_url, PredPlayerResponse)
                
                # Map response to entity
                player_entity = PredPlayerEntity.from_response(player_response)
                
                # TODO: UPSERT player_entity to the database when ready for integration
                # Example:
                # db.execute_query(
                #     "INSERT INTO pred_players (...) VALUES (...) ON CONFLICT (id) DO UPDATE SET ...",
                #     (player_entity.id, player_entity.display_name, ...)
                # )
                
                print(f"Successfully processed player: {player_entity.display_name} (ID: {player_entity.id})")
                
            except Exception as e:
                print(f"Error processing player {player_id}: {e}")
                continue
        
        print("Successfully hydrated Predecessor player data.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    from db.database import Database
    from scripts.utils_requests import RequestsClient
    hydrate_pred_hero_data(Database(), RequestsClient())
    hydrate_pred_item_data(Database(), RequestsClient())
    hydrate_pred_player_data(Database(), RequestsClient())
