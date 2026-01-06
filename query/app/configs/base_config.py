from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Config(BaseSettings):
    ENV: Env = Env.LOCAL

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "flaskuser"
    MYSQL_PASSWORD: str = "flaskpass"
    MYSQL_DB: str = "OZ"
    MYSQL_CONNECT_TIMEOUT: int = 5
    CONNECTION_POOL_MAXSIZE: int = 30
