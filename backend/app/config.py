import os
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv

parent_dir = Path(__file__).parent
backend_dir = parent_dir.parent
load_dotenv(backend_dir / ".env")


class Config:

    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP", parent_dir.name)
    FLASK_ENV = os.environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", True)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS", False
    )


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


def get_config_by_current_environment() -> ClassVar[Config]:
    from utils import environment_utils

    return environment_utils.value_by_environment(
        production=ProductionConfig,
        staging=DevelopmentConfig,
        development=DevelopmentConfig,
    )
