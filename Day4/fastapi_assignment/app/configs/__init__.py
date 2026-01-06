
from Day4.fastapi_assignment.app.configs.base import Config


def get_config() -> Config:
    return Config(_env_file=".env", _env_file_encoding="utf-8")


config = get_config()
