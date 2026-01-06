from pydantic_settings import BaseSettings

class Config(BaseSettings):
    SECRET_KEY: str = "default_secret_key"

    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "flaskuser"
    MYSQL_PASSWORD: str = "flaskpass"
    MYSQL_DATABASE: str = "oz"
    MYSQL_CONNECT_TIMEOUT: int = 5
    CONNECTION_POOL_MAXSIZE: int = 10