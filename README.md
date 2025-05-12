<h1 align="center">Weather-API</h1>

<p align="center">
  <a href="#"><img alt="Python Version" src="https://img.shields.io/static/v1?logo=python&color=Blue&message=3.13&label=Python"/></a>
  <a href="#"><img alt="Backend API - FastAPI" src="https://img.shields.io/static/v1?logo=fastapi&color=Blue&message=0.115.11&label=FastAPI"/></a>
  <a href="https://github.com/Simatwa/weather-api/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/static/v1?logo=MIT&color=Blue&message=MIT&label=License"/></a>
</p>

This is a FastAPI-based implementation that interacts with the OpenWeatherMap API. It provides a modern, efficient, and user-friendly way to fetch and serve weather data using FastAPI's robust web framework.


## Prerequisites

Before you begin, ensure you have the following:

- [Python >= 3.13](https://python.org) installed on your system.
- An API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).


## Installation

Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/Simatwa/weather-api.git
    cd weather-api
    ```

2. Install the required dependencies:
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows
    venv\Scripts\activate
    # On *nix
    source venv/bin/activate

    # Install the required dependencies
    pip install -r requirements.txt
    ```

## Configuration

To use the API, you need to configure your OpenWeatherMap API key:

1. Obtain your API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
2. Create a `.env` file in the project root (you can use the provided `.env.example` as a template).
3. Add your API key to the `.env` file using the key `OPEN_WEATHER_MAP_API_KEY`.

## Starting the Server

Once configured, you can start the server by running:

```bash
$ fastapi run app
```

The server will start on `http://localhost:8000`.


## API Documentation

The Weather-API provides interactive documentation for its endpoints:

| Documentation Type | URL                                |
| ------------------ | ---------------------------------- |
| Swagger UI         | [http://localhost:8000/api/docs](http://localhost:8000/api/docs) |
| ReDoc              | [http://localhost:8000/api/redoc](http://localhost:8000/api/redoc) |


## Notes

> **Important:**  
> The `/forecast` endpoint has periodic request limitations for non-premium OpenWeatherMap accounts. Consider upgrading your account for higher request limits.

# License

This project is licensed under [MIT License](LICENSE)