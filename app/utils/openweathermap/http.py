"""Makes actual http requests"""

from app.utils.openweathermap.urls import BASE_URL
from app.utils import env_config

from httpx import AsyncClient


class WeatherRequest:
    """Requests wrapper"""

    def __init__(self):
        """Constructor for `WeatherRequest`"""
        self.client = AsyncClient(
            base_url=BASE_URL,
            headers={"Content-Type": "application/json"},
            params={"appid": env_config.OPEN_WEATHER_MAP_API_KEY},
        )

    async def get(self, url: str, /, **params) -> dict:
        """Makes http get request

        url (str): Endpoint url without base-url
        params: Request parameters

        Returns:
            dict: Http response
        """
        request = await self.client.get(url, params=params)
        request.raise_for_status()
        return request.json()
