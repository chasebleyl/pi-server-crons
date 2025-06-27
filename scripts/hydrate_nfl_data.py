import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import Database

def hydrate_nfl_data():
    """Hydrates NFL data from an API into the database."""
    db = Database()
    try:
        db.connect()
        # TODO: Hit the NFL API, normalize the data, and write to the database
        # Example:
        # api_data = fetch_nfl_api_data()
        # normalized_data = normalize_nfl_data(api_data)
        # for item in normalized_data:
        #     db.execute_query("INSERT INTO nfl_table (...) VALUES (...);", (item.field1, item.field2))
        print("Successfully hydrated NFL data.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    hydrate_nfl_data()
