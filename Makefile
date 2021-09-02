.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

setup: setup-test ## Setup a dev environment for working in this repo. Assumes in a venv or other isolation
	pip install -r requirements-dev.txt
	pre-commit install
	pip install -e .

setup-test: ## Setup a testing environment for working in this repo. Assumes in a venv or other isolation
	pip install -r requirements-test.txt

test: setup-test ## run python tests
	pytest

tox: setup-test
	tox

build: setup ## build python packages
	pip install twine build
	python -m build --sdist --wheel --outdir dist/
	twine check dist/*

lint: setup blacken flake8 mypy pylint ## run python linting

blacken: ## Runs black on our code
	-python -m black geekbot_api

blacken-ci: 
	python -m black geekbot_api

flake8: ## Runs flake8 on our code
	-python -m flake8 geekbot_api

flake8-ci: 
	python -m flake8 geekbot_api

mypy: ## Runs mypy on our code
	-python -m mypy geekbot_api --no-strict-optional

mypy-ci: 
	python -m mypy geekbot_api --no-strict-optional

pylint: ## Runs pylint on our code
	-python -m pylint geekbot_api -E -r y -s y

pylint-ci: 
	python -m pylint geekbot_api -E -r y -s y

check-version: setup ## Check the version of the pydantic-aioredis package
	python setup.py --version
