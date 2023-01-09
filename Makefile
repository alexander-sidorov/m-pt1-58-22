.PHONY: format
format:
	black .
	isort --virtual-env="$(shell poetry env info --path)" .


.PHONY: qa
qa:
	black --check .
	isort --check-only --virtual-env="$(shell poetry env info --path)" .
	mypy
	flake8
	pytest
