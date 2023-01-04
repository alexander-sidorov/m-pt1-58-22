.PHONY: format
format:
	black hw/
	isort --virtual-env="$(shell poetry env info --path)" hw/


.PHONY: qa
qa:
	black --check hw/
	isort --check-only --virtual-env="$(shell poetry env info --path)" hw/
	mypy
	flake8
	pytest
