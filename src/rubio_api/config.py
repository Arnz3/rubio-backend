"""
Configuration for the API
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


    APP_TITLE: str = "Rubio backend"
    API_VERSION: str = "0.1.0"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_HOST: str
    DATABASE_PORT: int


    @computed_field
    def database_url(self) -> str:
        return (
            "postgresql://"
            + f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            + f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}"
            + f"/{self.POSTGRES_DB}"
        )




settings = Settings()