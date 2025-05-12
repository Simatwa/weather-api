"""Routes implementation"""

from fastapi import APIRouter, Query, HTTPException
from typing import Annotated, Callable
from app.utils.openweathermap.urls import (
    current_weather_data_url,
    daily_weather_data_url,
    n_day_forecast_data_url,
)
from app.utils.openweathermap.http import WeatherRequest
from app.v1.models.response import (
    UnitsOfMeasurement,
    WeatherInfo,
    DailyForecast,
    NDayForecast,
)
import httpx
from functools import wraps

weather_request = WeatherRequest()

router = APIRouter(tags=["V1"], prefix="/v1")


def route_exception_handler(func: Callable):
    """Decorator for handling route exceptions"""

    @wraps(func)
    async def decorator(*args, **kwargs):
        try:
            response = await func(*args, **kwargs)
            return response
        except httpx.HTTPStatusError as e:
            json_body: dict = e.response.json()
            json_body.setdefault(
                "possible_reason",
                "You are using a Free subscription and try requesting data available in other subscriptions.",
            )
            raise HTTPException(
                status_code=e.response.status_code,
                detail=json_body,
            )

    return decorator


@router.get("/weather", name="Current Weather")
@route_exception_handler
async def get_current_weather(
    lat: Annotated[
        float,
        Query(..., description="Latitude of the location."),
    ],
    lon: Annotated[
        float,
        Query(
            ...,
            description="Longitude of the location.",
        ),
    ],
    units: Annotated[
        UnitsOfMeasurement,
        Query(..., description="Units of measurement: standard, metric, or imperial."),
    ] = UnitsOfMeasurement.STANDARD.value,
    lang: Annotated[str, Query(..., description="Output language.")] = None,
) -> WeatherInfo:
    """Get current weather details of a specific location"""
    weather_data = await weather_request.get(
        current_weather_data_url, lat=lat, lon=lon, units=units.value, lang=lang
    )
    return WeatherInfo(**weather_data)


@router.get("/forecast/daily", name="Daily forecast")
@route_exception_handler
async def get_daily_forecast(
    lat: Annotated[
        float,
        Query(..., description="Latitude of the location."),
    ],
    lon: Annotated[
        float,
        Query(..., description="Longitude of the location."),
    ],
    cnt: Annotated[
        int,
        Query(
            ...,
            description="Number of days to return in the forecast (1 to 16).",
            gt=0,
            lt=17,
        ),
    ] = 3,
    units: Annotated[
        UnitsOfMeasurement,
        Query(..., description="Units of measurement: standard, metric, or imperial."),
    ] = UnitsOfMeasurement.STANDARD.value,
    lang: Annotated[str, Query(..., description="Output language.")] = None,
) -> DailyForecast:
    """Get daily weather forecast for a specific location"""
    forecast_data = await weather_request.get(
        daily_weather_data_url, lat=lat, lon=lon, cnt=cnt, units=units.value, lang=lang
    )
    return DailyForecast(**forecast_data)


@router.get("/forecast", name="n-time forecast")
@route_exception_handler
async def get_n_time_forecast(
    lat: Annotated[
        float,
        Query(..., description="Latitude of the location."),
    ],
    lon: Annotated[
        float,
        Query(..., description="Longitude of the location."),
    ],
    cnt: Annotated[
        int,
        Query(
            ...,
            description="Number of timestamps to return in the forecast.",
            gt=0,
            lt=17,
        ),
    ] = 3,
    units: Annotated[
        UnitsOfMeasurement,
        Query(..., description="Units of measurement: standard, metric, or imperial."),
    ] = UnitsOfMeasurement.STANDARD.value,
    lang: Annotated[str, Query(..., description="Output language.")] = None,
) -> NDayForecast:
    """Get n-time weather forecast for a specific location"""
    forecast_data = await weather_request.get(
        n_day_forecast_data_url, lat=lat, lon=lon, cnt=cnt, units=units.value, lang=lang
    )
    return NDayForecast(**forecast_data)
