#!/usr/bin/env bash

if [[ ! $(which poetry) ]]; then
  dir_venv=""
else
  dir_venv="$(poetry env info --path)"
fi

ret=0

black --check hw/ || ret=1
isort --check-only --virtual-env="${dir_venv}" hw/ || ret=1
mypy || ret=1
flake8 || ret=1
pytest || ret=1

if [[ "${ret}" -ne 0 ]]; then
  exit 1
fi

