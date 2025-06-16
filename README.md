# Current Weather CLI

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)

A simple, modern command-line tool to fetch the current weather for a given city, built with Python, Typer, and Poetry.

This project was developed following professional software engineering practices, including Test-Driven Development (TDD) and dependency management with Poetry.

---

## Key Features

* Fetch current weather descriptions and temperatures.
* Clean, user-friendly command-line interface powered by Typer.
* Secure API key management using `.env` files.
* Developed using TDD with 100% test coverage on the core logic.
* Modern project and dependency management with Poetry.

---

## Installation

To get this project up and running on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/awakra/current-weather-cli.git
   cd current-weather-cli
   ```

2. **Install dependencies:**

   This project uses [Poetry](https://python-poetry.org/) for dependency management. Make sure you have it installed, then run:

   ```bash
   poetry install
   ```

   This command will create a virtual environment and install all necessary packages like `requests`, `typer`, and `pytest`.

---

## Configuration

This application requires an API key from [OpenWeatherMap](https://openweathermap.org/api) to function.

1. **Get your API Key:**
   Sign up for a free account on OpenWeatherMap and get your API key.

2. **Create a `.env` file:**

   ```bash
   cp .env.example .env
   ```

3. **Add your API Key:**
   Edit the `.env` file and add your API key like this:

   ```
   OPENWEATHER_API_KEY="your_actual_api_key_from_the_website"
   ```

   > **Note:** The `.env` file is listed in `.gitignore` and will **not** be committed to the repository, keeping your secrets safe.

---

## Usage

Once installed and configured, you can run the application using Poetry:

**Get the weather for a city:**

```bash
poetry run weather "New York"
```

**Expected Output:**

```
Current Weather: Clear Sky, 18.5°C
```

**Get help and see all options:**

```bash
poetry run weather --help
```

---

## Development

This project was built with testing in mind. To run the test suite, use pytest.

**Run all tests:**

```bash
poetry run pytest
```

**Run tests with a coverage report:**

```bash
poetry run pytest --cov=current_weather_cli
```

This will show you how much of the application code is covered by the tests.

---

## Technology Stack

* **Language:** Python 3.12+
* **CLI Framework:** Typer
* **Dependency Management:** Poetry
* **Testing:** Pytest
* **HTTP Requests:** Requests
