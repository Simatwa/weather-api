"""API outgoing response models"""

from pydantic import BaseModel
from typing import Optional
from enum import Enum


class UnitsOfMeasurement(str, Enum):
    STANDARD = "standard"
    METRIC = "metric"
    IMPERIAL = "imperial"


class Coordinates(BaseModel):
    lat: float
    lon: float


class WeatherInfo(BaseModel):
    coord: Coordinates
    weather: list[dict]
    base: str
    main: "MainInfo"
    visibility: int
    wind: "WindInfo"
    rain: Optional["RainInfo"] = None
    clouds: "CloudInfo"
    dt: int
    sys: "SysInfo"
    timezone: int
    id: int
    name: str
    cod: int

    class Config:
        json_schema_extra = {
            "example": {
                "coord": {"lat": 0.142, "lon": 37.01},
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03d",
                    }
                ],
                "base": "stations",
                "main": {
                    "temp": 298.27,
                    "feels_like": 297.93,
                    "temp_min": 298.27,
                    "temp_max": 298.27,
                    "pressure": 1014,
                    "humidity": 42,
                    "sea_level": 1014,
                    "grnd_level": 831,
                },
                "visibility": 10000,
                "wind": {"speed": 4.38, "deg": 30, "gust": 4.5},
                "rain": None,
                "clouds": {"all": 31},
                "dt": 1747040921,
                "sys": {
                    "type": None,
                    "id": None,
                    "country": "KE",
                    "sunrise": 1747020281,
                    "sunset": 1747063923,
                },
                "timezone": 10800,
                "id": 184433,
                "name": "Nanyuki",
                "cod": 200,
            }
        }


class WeatherDetail(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainInfo(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int | None = None
    grnd_level: int | None = None


class WindInfo(BaseModel):
    speed: float
    deg: int
    gust: float | None = None


class RainInfo(BaseModel):
    one_hour: float | None = None

    class Config:
        fields = {"one_hour": "1h"}


class CloudInfo(BaseModel):
    all: int


class SysInfo(BaseModel):
    type: int | None = None
    id: int | None = None
    country: str
    sunrise: int
    sunset: int


class DailyForecast(BaseModel):
    city: dict
    cod: str
    message: float
    cnt: int
    list: list["DailyWeather"]

    class Config:
        json_schema_extra = {
            "example": {
                "city": {
                    "id": 3163858,
                    "name": "Zocca",
                    "coord": {"lon": 10.99, "lat": 44.34},
                    "country": "IT",
                    "population": 4593,
                    "timezone": 7200,
                },
                "cod": "200",
                "message": 0.0582563,
                "cnt": 7,
                "list": [
                    {
                        "dt": 1661857200,
                        "sunrise": 1661834187,
                        "sunset": 1661882248,
                        "temp": {
                            "day": 299.66,
                            "min": 288.93,
                            "max": 299.66,
                            "night": 290.31,
                            "eve": 297.16,
                            "morn": 288.93,
                        },
                        "feels_like": {
                            "day": 299.66,
                            "night": 290.3,
                            "eve": 297.1,
                            "morn": 288.73,
                        },
                        "pressure": 1017,
                        "humidity": 44,
                        "weather": [
                            {
                                "id": 500,
                                "main": "Rain",
                                "description": "light rain",
                                "icon": "10d",
                            }
                        ],
                        "speed": 2.7,
                        "deg": 209,
                        "gust": 3.58,
                        "clouds": 53,
                        "pop": 0.7,
                        "rain": 2.51,
                    }
                ],
            }
        }


class DailyWeather(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: "TemperatureInfo"
    feels_like: "FeelsLikeInfo"
    pressure: int
    humidity: int
    weather: list[WeatherDetail]
    speed: float
    deg: int
    gust: float | None = None
    clouds: int
    pop: float
    rain: float | None = None


class TemperatureInfo(BaseModel):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


class FeelsLikeInfo(BaseModel):
    day: float
    night: float
    eve: float
    morn: float


class NDayForecast(BaseModel):
    cod: str
    message: float
    cnt: int
    list: list["ForecastDetail"]
    city: dict

    class Config:
        json_schema_extra = {
            "example": {
                "cod": "200",
                "message": 0,
                "cnt": 40,
                "list": [
                    {
                        "dt": 1661871600,
                        "main": {
                            "temp": 296.76,
                            "feels_like": 296.98,
                            "temp_min": 296.76,
                            "temp_max": 297.87,
                            "pressure": 1015,
                            "sea_level": 1015,
                            "grnd_level": 933,
                            "humidity": 69,
                            "temp_kf": -1.11,
                        },
                        "weather": [
                            {
                                "id": 500,
                                "main": "Rain",
                                "description": "light rain",
                                "icon": "10d",
                            }
                        ],
                        "clouds": {"all": 100},
                        "wind": {"speed": 0.62, "deg": 349, "gust": 1.18},
                        "visibility": 10000,
                        "pop": 0.32,
                        "rain": {"3h": 0.26},
                        "sys": {"pod": "d"},
                        "dt_txt": "2022-08-30 15:00:00",
                    }
                ],
                "city": {
                    "id": 3163858,
                    "name": "Zocca",
                    "coord": {"lat": 44.34, "lon": 10.99},
                    "country": "IT",
                    "population": 4593,
                    "timezone": 7200,
                    "sunrise": 1661834187,
                    "sunset": 1661882248,
                },
            }
        }


class ForecastDetail(BaseModel):
    dt: int
    main: "MainInfo"
    weather: list[WeatherDetail]
    clouds: CloudInfo
    wind: WindInfo
    visibility: int
    pop: float
    rain: Optional[dict] = None
    sys: dict
    dt_txt: str
