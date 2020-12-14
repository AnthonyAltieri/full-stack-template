#!/bin/bash

CURRENT_DIRECTORY="$(pwd)"
SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${SCRIPTS_DIRECTORY}"/.. || exit 1

echo ">>> Running pytest"
poetry run pytest tests

cd "${CURRENT_DIRECTORY}" || exit 1

exit 0

