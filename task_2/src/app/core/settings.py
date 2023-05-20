from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database settings
    POSTGRES_DB: str = 'db'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_SERVER: str = 'localhost'
    DB_PORT: int = 5432

    # Path and URL settings
    BASE_DIR = Path(__file__).resolve().parent.parent
    STATIC_DIR = BASE_DIR / 'static'
    STATIC_URL = '/static/'
    TEMP_DIR = BASE_DIR / 'temp'

    API_HOST: str = 'http://localhost:8000'
    DOWNLOAD_URL: str = f'{API_HOST}/record'


settings = Settings()
