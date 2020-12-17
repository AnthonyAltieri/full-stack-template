import os
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv

if "DOT_ENV_DIRECTORY" in os.environ:
    dot_env_directory = Path(os.environ["DOT_ENV_DIRECTORY"])
else:
    parent_directory = Path(__file__).parent
    backend_directory = parent_directory.parent
    dot_env_directory = backend_directory

load_dotenv(dot_env_directory / ".env")


class Config:

    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP", parent_directory.name)
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
    from utils import environment

    return environment.value_by_environment(
        production=ProductionConfig,
        staging=DevelopmentConfig,
        development=DevelopmentConfig,
    )
