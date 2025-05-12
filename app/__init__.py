"""
Weather API module. Uses FastAPI.
"""

import time
from pathlib import Path

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.v1 import router as v1_router


api_module_path = Path(__file__).parent

api_prefix = "/api"

app = FastAPI(
    title="Weather API",
    version=api_module_path.joinpath("VERSION").read_text().strip(),
    description=api_module_path.joinpath("README.md").read_text(),
    license_info={
        "name": "MIT License",
        "url": "https://raw.githubusercontent.com/Simatwa/weather-api/refs/heads/main/LICENSE",
    },
    docs_url=api_prefix + "/docs",
    redoc_url=api_prefix + "/redoc",
    openapi_url=api_prefix + "/openapi.json",
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# Include API router

app.include_router(v1_router, prefix=api_prefix)
