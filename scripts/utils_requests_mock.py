from typing import TypeVar, Type, Any, Dict, List
from pydantic import BaseModel, ValidationError
import requests
from .utils_requests_interface import RequestsInterface

T = TypeVar('T', bound=BaseModel)

class RequestsMock(RequestsInterface):
    """
    Mock implementation of RequestsInterface for testing purposes.
    """
    
    def __init__(self):
        self.responses: Dict[str, Any] = {}
        self.called_urls = []
        self.request_errors = {}
        self.validation_errors = {}
    
    def get_and_deserialize(self, url: str, target_type: Type[T], timeout: int = 30) -> T:
        """
        Mock implementation that returns predefined responses.
        """
        self.called_urls.append((url, target_type, timeout))
        
        # Check if this URL should raise a request error
        if url in self.request_errors:
            raise self.request_errors[url]
        
        # Check if this URL should raise a validation error
        if url in self.validation_errors:
            raise self.validation_errors[url]
        
        if url not in self.responses:
            raise ValueError(f"No mock response configured for URL: {url}")
        
        mock_data = self.responses[url]
        
        # Handle list responses
        if hasattr(target_type, '__origin__') and target_type.__origin__ is list:
            item_type = target_type.__args__[0]
            return [item_type(**item) for item in mock_data]
        
        # Handle single object responses
        return target_type(**mock_data)
    
    # Test helper methods
    def set_response(self, url: str, data: Any) -> None:
        """Set a mock response for a specific URL."""
        self.responses[url] = data
    
    def set_request_error(self, url: str, error: Exception) -> None:
        """Set an error to be raised when a specific URL is requested."""
        self.request_errors[url] = error
    
    def set_validation_error(self, url: str, error: ValidationError) -> None:
        """Set a validation error to be raised when a specific URL is requested."""
        self.validation_errors[url] = error
    
    def get_called_urls(self) -> List[tuple]:
        """Get all called URLs for verification."""
        return self.called_urls.copy()
    
    def was_url_called(self, url: str) -> bool:
        """Check if a specific URL was called."""
        return any(called_url == url for called_url, _, _ in self.called_urls)
    
    def reset(self) -> None:
        """Reset all mock state for clean testing."""
        self.responses.clear()
        self.called_urls.clear()
        self.request_errors.clear()
        self.validation_errors.clear()
