import os
from app.config.dev import DevConfig
from app.config.prod import ProdConfig


def get_settings():
    env = os.getenv("ENV", "dev")
    return ProdConfig() if env == "prod" else DevConfig()


settings = get_settings()
