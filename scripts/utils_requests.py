import requests
from typing import TypeVar, Type
from pydantic import BaseModel, ValidationError
import logging

# Type variable for generic Pydantic models
T = TypeVar('T', bound=BaseModel)

def get_and_deserialize(url: str, target_type: Type[T], timeout: int = 30) -> T:
    """
    Makes a GET request to the specified URL and deserializes the response to the target type.
    
    Args:
        url (str): The URL to make the GET request to
        target_type (Type[T]): The Pydantic model type to deserialize the response to
        timeout (int): Request timeout in seconds (default: 30)
    
    Returns:
        T: An instance of the target type with the deserialized data
        
    Raises:
        requests.RequestException: If the HTTP request fails
        ValidationError: If the response data cannot be deserialized to the target type
        ValueError: If the response is not valid JSON or other validation errors
    """
    try:
        # Make the GET request
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Deserialize to target type
        return target_type(**data)
        
    except requests.RequestException as e:
        logging.error(f"HTTP request failed for URL {url}: {str(e)}")
        raise
    except ValueError as e:
        logging.error(f"Invalid JSON response from URL {url}: {str(e)}")
        raise
    except ValidationError as e:
        logging.error(f"Failed to deserialize response from URL {url} to {target_type.__name__}: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error processing request to URL {url}: {str(e)}")
        raise
