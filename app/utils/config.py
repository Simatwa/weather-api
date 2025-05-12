"""Configuration for the API"""

from pydantic import BaseModel, Field
from dotenv import dotenv_values


class Config(BaseModel):
    """Env Config"""

    OPEN_WEATHER_MAP_API_KEY: str = Field(
        min_length=32, max_length=32, description="API Key"
    )


env_config = Config(**dotenv_values())
"""Loaded Config from .env file"""
