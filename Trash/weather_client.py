import requests
import json

# API client for weather service
# Need to add better error handling and retries

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com/v1"
        # TODO: add timeout configuration
    
    def get_current_weather(self, city):
        """Get current weather for a city"""
        endpoint = f"{self.base_url}/current"
        params = {
            'city': city,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            # TODO: check status code before returning
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def get_forecast(self, city, days=5):
        """Get weather forecast"""
        # TODO: implement this method
        pass
    
    def _make_request(self, endpoint, params):
        """Helper method for making requests"""
        # TODO: add retry logic
        # TODO: add rate limiting
        # TODO: add proper logging
        pass

# Usage example
if __name__ == "__main__":
    # FIXME: API key is hardcoded - should use env variable
    client = WeatherClient("test_api_key_12345")
    
    weather = client.get_current_weather("New York")
    # print(weather)  # this crashes if request fails
    
    # TODO: add command line arguments
    # TODO: save results to database
