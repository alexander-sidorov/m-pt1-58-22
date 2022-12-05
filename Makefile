.PHONY: format
format:
	black hw/
	isort --virtual-env="$(poetry env info --path)" hw/


.PHONY: qa
qa:
	mypy
	flake8
	pytest
