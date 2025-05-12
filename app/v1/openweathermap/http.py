"""Makes actual http requests"""

from app.v1.openweathermap.urls import BASE_URL
from app.utils import env_config

from httpx import Client


class WeatherRequest:
    """Requests wrapper"""

    def __init__(self, api_key: str):
        """Constructor for `WeatherRequest`

        Args:
            api_key (str): OpenWeatherMap API key
        """
        self.api_key = api_key
        self.client = Client(
            base_url=BASE_URL,
            headers={"Content-Type": "application/json"},
            params={"appid": env_config.OPEN_WEATHER_MAP_API_KEY},
        )

    def get(self, url: str, /, **params) -> dict:
        """Makes http get request

        url (str): Endpoint url without base-url
        params: Request parameters

        Returns:
            dict: Http response
        """
        request = self.client.get(url, params=params)
        request.raise_for_status()
        return request.json()
