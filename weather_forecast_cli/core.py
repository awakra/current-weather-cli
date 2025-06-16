import requests

API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str, api_key: str) -> dict | None:
    """
    Fetches weather data for a specified city from the OpenWeatherMap API.

    Args:
        city: The name of the city.
        api_key: The API key for authenticating with the OpenWeatherMap service.

    Returns:
        A dictionary containing the weather data if the request is successful,
        otherwise None.
    """
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    
    try:
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None