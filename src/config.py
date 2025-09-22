from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    token: str

class DBConfig(BaseSettings):
    url: str

class Settings(BaseSettings):
    bot_config: BotConfig
    db_config: DBConfig

    model_config = SettingsConfigDict(
        env_file=(
            ".env.template",
            ".env",
        ),
        env_nested_delimiter="__",
    )


settings = Settings()
