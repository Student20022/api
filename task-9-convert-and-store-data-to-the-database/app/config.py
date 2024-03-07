import sys
from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict
)


ENGINE_OPTIONS = {"echo": True}


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_POSTGRES: str

    @property
    def DATABASE_URL_psycopg(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_POSTGRES}"

    if any("pytest" in arg for arg in sys.argv):
        model_config = SettingsConfigDict(env_file=".env.test")
    else:
        model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
