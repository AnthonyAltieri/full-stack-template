import os
from enum import Enum
from typing import Any


class Environment(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"


def get_environment() -> Environment:
    if "env" in os.environ:
        environment_string = os.environ["env"]
    elif "environment" in os.environ:
        environment_string = os.environ["environment"]
    else:
        environment_string = ""

    # normalize environment string
    environment_string = environment_string.strip().lower()

    if environment_string in ("production", "prod"):
        return Environment.PRODUCTION
    elif environment_string in ("staging",):
        return Environment.STAGING
    else:
        return Environment.DEVELOPMENT


def value_by_environment(
    development: Any,
    staging: Any,
    production: Any,
    is_function: bool = False,
) -> Any:

    environment = get_environment()
    if environment == Environment.PRODUCTION:
        value = production
    elif environment == Environment.STAGING:
        value = staging
    elif environment == Environment.DEVELOPMENT:
        value = development
    else:
        raise ValueError(f"Unknown environment {environment}")

    if is_function:
        return value()
    else:
        return value
