import unittest
from unittest.mock import patch
from typer.testing import CliRunner
from weather_forecast_cli.main import app

runner = CliRunner()

class TestMain(unittest.TestCase):
    """Test suite for the CLI (main.py)."""

    @patch('weather_forecast_cli.main.get_weather_data')
    def test_main_success(self, mock_get_weather):
        """
        Tests the CLI for a successful weather data retrieval.
        """
        # Arrange: Mock the core function's return value and the API key.
        mock_get_weather.return_value = {
            "weather": [{"description": "sunny"}],
            "main": {"temp": 25.5}
        }
        env_vars = {"OPENWEATHER_API_KEY": "fake_key"}

        # Act: Invoke the CLI with a city argument and the fake environment variable.
        result = runner.invoke(app, ["London"], env=env_vars)

        # Assert: Check exit code, output, and that our mock was called correctly.
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Current Weather: Sunny, 25.5°C", result.stdout)
        mock_get_weather.assert_called_once_with("London", "fake_key")

    @patch('weather_forecast_cli.main.get_weather_data')
    def test_main_failure(self, mock_get_weather):
        """
        Tests the CLI for a failed weather data retrieval.
        """
        # Arrange
        mock_get_weather.return_value = None
        env_vars = {"OPENWEATHER_API_KEY": "fake_key"}

        # Act
        result = runner.invoke(app, ["NotARealCity"], env=env_vars)

        # Assert
        self.assertEqual(result.exit_code, 1)
        self.assertIn("Could not retrieve weather data for NotARealCity", result.stdout)