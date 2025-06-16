import unittest
import requests
from unittest.mock import patch, Mock
from current_weather_cli.core import get_weather_data

class TestCore(unittest.TestCase):
    """Test suite for the core weather fetching logic."""

    @patch('current_weather_cli.core.requests.get')
    def test_get_weather_data_success(self, mock_get):
        """
        Tests the successful retrieval of weather data for a city.
        """
        # Arrange: Configure the mock to simulate a successful API response.
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 282.55}
        }
        mock_get.return_value = mock_response

        # Act: Call the function we are testing.
        city = "London"
        api_key = "fake_api_key"
        weather_data = get_weather_data(city, api_key)

        # Assert: Check if the function returned the expected data.
        self.assertIsNotNone(weather_data)
        self.assertEqual(weather_data['weather'][0]['description'], 'clear sky')
        self.assertEqual(weather_data['main']['temp'], 282.55)
        
    @patch('current_weather_cli.core.requests.get')
    def test_get_weather_data_failure(self, mock_get):
        """
        Tests the function's behavior when the API call fails.
        """
        # Arrange: Configure the mock to raise a RequestException,
        # simulating a network error.
        mock_get.side_effect = requests.exceptions.RequestException("API call failed")

        # Act: Call the function we are testing.
        city = "InvalidCity"
        api_key = "fake_api_key"
        weather_data = get_weather_data(city, api_key)

        # Assert: Check that the function handled the error gracefully
        # by returning None, as designed.
        self.assertIsNone(weather_data)
        
    @patch('current_weather_cli.core.requests.get')
    def test_get_weather_data_http_error(self, mock_get):
        """
        Tests the function's behavior for a 404 HTTP error (e.g., city not found).
        """
        # Arrange: Configure the mock to simulate a 404 response.
        mock_response = Mock()
        mock_response.status_code = 404
        # We also need to simulate the behavior of raise_for_status(),
        # which should raise an HTTPError for a 404 status.
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Client Error: Not Found"
        )
        mock_get.return_value = mock_response

        # Act: Call the function we are testing.
        city = "NotARealCity"
        api_key = "fake_api_key"
        weather_data = get_weather_data(city, api_key)

        # Assert: Check that the function handled the HTTPError gracefully
        # by returning None.
        self.assertIsNone(weather_data)