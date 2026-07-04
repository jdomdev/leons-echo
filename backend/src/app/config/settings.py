from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, extra="ignore")

    app_env: str | None = Field(default=None, validation_alias="APP_ENV")


@lru_cache
def get_settings() -> Settings:
    return Settings()
