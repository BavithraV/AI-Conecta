# ----------------------------
# VARIABLES
# ----------------------------
PYTHON=python3
PIP=pip

# ----------------------------
# INSTALLATION
# ----------------------------
install:
	uv pip install -e .

install-dev:
	pip install .[dev]
	pre-commit install

# ----------------------------
# FORMAT & LINT
# ----------------------------
format:
	ruff format .
	black .

lint:
	ruff check .

fix:
	ruff check . --fix

# ----------------------------
# PRE-COMMIT
# ----------------------------
precommit:
	pre-commit run --all-files

# ----------------------------
# RUN APP
# ----------------------------
run:
	uvicorn app.main:app --reload

# ----------------------------
# TEST
# ----------------------------
test:
	pytest

# ----------------------------
# CLEAN
# ----------------------------
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

# ----------------------------
# FREEZE DEPENDENCIES
# ----------------------------
freeze:
	pip-compile --output-file=requirements.txt pyproject.toml

freeze-dev:
	pip-compile --extra dev --output-file=requirements-dev.txt pyproject.toml