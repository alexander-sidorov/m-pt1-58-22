#!/usr/bin/env bash

black --check hw/
isort --virtual-env="$(poetry env info --path)" hw/
mypy
flake8
pytest
