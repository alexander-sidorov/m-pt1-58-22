#!/usr/bin/env bash

if [[ ! $(which poetry) ]]; then
  dir_venv=""
else
  dir_venv="$(poetry env info --path)"
fi

black --check hw/
isort --virtual-env="${dir_venv}" hw/
mypy
flake8
pytest
