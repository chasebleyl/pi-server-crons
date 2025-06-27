from abc import ABC, abstractmethod
from typing import TypeVar, Type
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class RequestsInterface(ABC):
    """
    Abstract base class defining the interface for HTTP request operations.
    This allows for easy mocking and testing of HTTP-dependent code.
    """
    
    @abstractmethod
    def get_and_deserialize(self, url: str, target_type: Type[T], timeout: int = 30) -> T:
        """
        Makes a GET request to the specified URL and deserializes the response to the target type.
        
        Args:
            url: The URL to make the GET request to
            target_type: The Pydantic model type to deserialize the response to
            timeout: Request timeout in seconds
            
        Returns:
            An instance of the target type with the deserialized data
            
        Raises:
            requests.RequestException: If the HTTP request fails
            ValidationError: If the response data cannot be deserialized to the target type
            ValueError: If the response is not valid JSON or other validation errors
        """
        pass 