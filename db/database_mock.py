from typing import Optional, List, Tuple, Any
from .database_interface import DatabaseInterface

class DatabaseMock(DatabaseInterface):
    """
    Mock implementation of DatabaseInterface for testing purposes.
    """
    
    def __init__(self):
        self.conn = None
        self.executed_queries = []
        self.fetch_results = {}
        self.connect_called = False
        self.disconnect_called = False
        self.connection_errors = []
        self.query_errors = {}
    
    def connect(self) -> None:
        """Mock database connection."""
        self.connect_called = True
        self.conn = "mock_connection"
        print("Mock database connection established.")
    
    def disconnect(self) -> None:
        """Mock database disconnection."""
        self.disconnect_called = True
        self.conn = None
        print("Mock database connection closed.")
    
    def execute_query(self, query: str, params: Optional[tuple] = None) -> None:
        """Mock query execution - records the query for testing."""
        if self.conn is None:
            self.connect()
        
        # Check if this query should raise an error
        if query in self.query_errors:
            raise self.query_errors[query]
        
        self.executed_queries.append((query, params))
    
    def fetch_query(self, query: str, params: Optional[tuple] = None) -> Optional[List[Tuple[Any, ...]]]:
        """Mock query fetching - returns predefined results."""
        if self.conn is None:
            self.connect()
        
        # Check if this query should raise an error
        if query in self.query_errors:
            raise self.query_errors[query]
        
        return self.fetch_results.get(query, [])
    
    # Test helper methods
    def set_fetch_result(self, query: str, result: List[Tuple[Any, ...]]) -> None:
        """Set a mock result for a specific query."""
        self.fetch_results[query] = result
    
    def set_query_error(self, query: str, error: Exception) -> None:
        """Set an error to be raised when a specific query is executed."""
        self.query_errors[query] = error
    
    def get_executed_queries(self) -> List[Tuple[str, Optional[tuple]]]:
        """Get all executed queries for verification."""
        return self.executed_queries.copy()
    
    def was_connect_called(self) -> bool:
        """Check if connect was called."""
        return self.connect_called
    
    def was_disconnect_called(self) -> bool:
        """Check if disconnect was called."""
        return self.disconnect_called
    
    def reset(self) -> None:
        """Reset all mock state for clean testing."""
        self.executed_queries.clear()
        self.fetch_results.clear()
        self.query_errors.clear()
        self.connect_called = False
        self.disconnect_called = False
        self.conn = None
