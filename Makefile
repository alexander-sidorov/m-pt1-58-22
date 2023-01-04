.PHONY: format
format:
	black hw/ project/ app_*/
	isort --virtual-env="$(shell poetry env info --path)" hw/ project/ app_*/


.PHONY: qa
qa:
	black --check hw/ project/ app_*/
	isort --check-only --virtual-env="$(shell poetry env info --path)" hw/ project/ app_*/
	mypy
	flake8
	pytest
