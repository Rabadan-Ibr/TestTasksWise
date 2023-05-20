from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str = 'db'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_SERVER: str = 'localhost'
    DB_PORT = 5432

    QUESTIONS_SERVICE_URL: str = 'https://jservice.io/api/random?count='


settings = Settings()
