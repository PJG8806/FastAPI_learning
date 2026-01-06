from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from query.app.configs import config

TORTOISE_APP_MODELS = [
    "query.app.tortoise_models.meeting",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": config.MYSQL_HOST,
                "port": config.MYSQL_PORT,
                "user": config.MYSQL_USER,
                "password": config.MYSQL_PASSWORD,
                "database": config.MYSQL_DB,
                "connect_timeout": config.MYSQL_CONNECT_TIMEOUT,
                "maxsize": config.CONNECTION_POOL_MAXSIZE,
            },
        },
    },
    "apps": {
        "models": {
            "models": TORTOISE_APP_MODELS,
            "default_connection": "default",
        },
    },
    "timezone": "Asia/Seoul",
}


"""
def initialize_tortoise(app: FastAPI) -> None:
    Tortoise.init_models(TORTOISE_APP_MODELS, "models")
    register_tortoise(app, config=TORTOISE_ORM)
"""


def initialize_tortoise(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,  # 운영환경 권장
        add_exception_handlers=True,
    )


# tortoise 설정
