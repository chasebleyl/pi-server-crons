import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Adjust the path to include the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database_mock import DatabaseMock
from scripts.utils_requests_mock import RequestsMock
from schemas.predecessor.PredHeroEntity import PredHeroResponse
from schemas.predecessor.PredItemEntity import PredItemResponse
from schemas.predecessor.PredPlayerEntity import PredPlayerResponse

class TestHydratePredecessorData(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.db_mock = DatabaseMock()
        self.requests_mock = RequestsMock()
    
    def tearDown(self):
        """Clean up after each test method."""
        self.db_mock.reset()
        self.requests_mock.reset()
    
    def test_hydrate_pred_hero_data_success(self):
        """Test successful hero data hydration."""
        # Setup mock responses
        mock_heroes_data = [
            {"id": 1, "name": "hero1", "display_name": "Hero 1"},
            {"id": 2, "name": "hero2", "display_name": "Hero 2"}
        ]
        self.requests_mock.set_response("https://omeda.city/heroes.json", mock_heroes_data)
        
        # Import and call the function
        from scripts.hydrate_predecessor_data import hydrate_pred_hero_data
        hydrate_pred_hero_data(self.db_mock, self.requests_mock)
        
        # Assertions
        self.assertTrue(self.db_mock.was_connect_called())
        self.assertTrue(self.db_mock.was_disconnect_called())
        self.assertTrue(self.requests_mock.was_url_called("https://omeda.city/heroes.json"))
        
        # Verify the correct number of heroes were processed
        called_urls = self.requests_mock.get_called_urls()
        self.assertEqual(len(called_urls), 1)
        self.assertEqual(called_urls[0][0], "https://omeda.city/heroes.json")
    
    def test_hydrate_pred_hero_data_api_error(self):
        """Test hero data hydration with API error."""
        # Setup mock to raise an error
        self.requests_mock.set_request_error("https://omeda.city/heroes.json", Exception("API Error"))
        
        # Import and call the function
        from scripts.hydrate_predecessor_data import hydrate_pred_hero_data
        hydrate_pred_hero_data(self.db_mock, self.requests_mock)
        
        # Assertions
        self.assertTrue(self.db_mock.was_connect_called())
        self.assertTrue(self.db_mock.was_disconnect_called())
        self.assertTrue(self.requests_mock.was_url_called("https://omeda.city/heroes.json"))
    
    def test_hydrate_pred_item_data_success(self):
        """Test successful item data hydration."""
        # Setup mock responses
        mock_items_data = [
            {"id": 1, "name": "item1", "display_name": "Item 1"},
            {"id": 2, "name": "item2", "display_name": "Item 2"}
        ]
        self.requests_mock.set_response("https://omeda.city/items.json", mock_items_data)
        
        # Import and call the function
        from scripts.hydrate_predecessor_data import hydrate_pred_item_data
        hydrate_pred_item_data(self.db_mock, self.requests_mock)
        
        # Assertions
        self.assertTrue(self.db_mock.was_connect_called())
        self.assertTrue(self.db_mock.was_disconnect_called())
        self.assertTrue(self.requests_mock.was_url_called("https://omeda.city/items.json"))
    
    def test_hydrate_pred_player_data_success(self):
        """Test successful player data hydration."""
        # Setup mock responses for each player
        mock_player_data = {"id": "player1", "display_name": "Player 1"}
        self.requests_mock.set_response("https://omeda.city/players/player1.json", mock_player_data)
        
        # Import and call the function
        from scripts.hydrate_predecessor_data import hydrate_pred_player_data
        hydrate_pred_player_data(self.db_mock, self.requests_mock)
        
        # Assertions
        self.assertTrue(self.db_mock.was_connect_called())
        self.assertTrue(self.db_mock.was_disconnect_called())
        self.assertTrue(self.requests_mock.was_url_called("https://omeda.city/players/player1.json"))
    
    def test_database_operations_when_implemented(self):
        """Test database operations when they are implemented."""
        # This test will be useful when you implement the actual database operations
        mock_heroes_data = [{"id": 1, "name": "hero1", "display_name": "Hero 1"}]
        self.requests_mock.set_response("https://omeda.city/heroes.json", mock_heroes_data)
        
        # Import and call the function
        from scripts.hydrate_predecessor_data import hydrate_pred_hero_data
        hydrate_pred_hero_data(self.db_mock, self.requests_mock)
        
        # When you implement database operations, you can verify them like this:
        # executed_queries = self.db_mock.get_executed_queries()
        # self.assertGreater(len(executed_queries), 0)
        # self.assertTrue(any("INSERT INTO pred_heroes" in query for query, _ in executed_queries))

if __name__ == '__main__':
    unittest.main()
