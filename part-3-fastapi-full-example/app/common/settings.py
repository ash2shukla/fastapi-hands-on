# one great way to handle your settings with modern web python stack is using pydantic settings
import os
from typing import Annotated

from pydantic import AnyUrl, UrlConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_PATH = os.getenv("MYAPP_ENV")

PostgresDsnWithDriver = Annotated[
    AnyUrl,
    UrlConstraints(allowed_schemes=["postgresql+psycopg"]),
]


class _BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_prefix="MYAPP_",
        extra="ignore",
        env_file_encoding="utf-8",
    )


class Settings(_BaseSettings):
    SOME_SETTING: int = 1
    DB_DSN: PostgresDsnWithDriver = AnyUrl(
        "postgresql+psycopg://user:pass@localhost:5432/db"
    )
    WITH_SQLALCHEMY: bool = True


settings = Settings()
