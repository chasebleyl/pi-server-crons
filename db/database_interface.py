from abc import ABC, abstractmethod
from typing import Optional, List, Tuple, Any

class DatabaseInterface(ABC):
    """
    Abstract base class defining the interface for database operations.
    This allows for easy mocking and testing of database-dependent code.
    """
    
    @abstractmethod
    def connect(self) -> None:
        """Connect to the database server."""
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the database server."""
        pass
    
    @abstractmethod
    def execute_query(self, query: str, params: Optional[tuple] = None) -> None:
        """
        Execute a SQL query that doesn't return results (INSERT, UPDATE, DELETE, etc.).
        
        Args:
            query: SQL query string
            params: Optional parameters for the query
        """
        pass
    
    @abstractmethod
    def fetch_query(self, query: str, params: Optional[tuple] = None) -> Optional[List[Tuple[Any, ...]]]:
        """
        Execute a SQL query and return results (SELECT).
        
        Args:
            query: SQL query string
            params: Optional parameters for the query
            
        Returns:
            List of tuples containing query results, or None if error
        """
        pass 