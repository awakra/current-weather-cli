import os
import typer
from dotenv import load_dotenv
from current_weather_cli.core import get_weather_data


load_dotenv()
app = typer.Typer()

def format_weather_display(data: dict) -> str:
    """Formats the raw weather data"""
    description = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    return f"Current Weather: {description}, {temp}°C"

@app.command()
def main(
    city: str = typer.Argument(..., help="The city you want to check the weather for."),
):
    """
    A simple CLI to get the current weather for a city.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        raise typer.Exit(code=1)

    weather_data = get_weather_data(city, api_key)

    if weather_data:
        display_text = format_weather_display(weather_data)
        print(display_text)
    else:
        print(f"Could not retrieve weather data for {city}.")
        raise typer.Exit(code=1)