# Makefile for Polynomial Equation Solver

# Configuration
POETRY := poetry
PYTHON := $(POETRY) run python3
PACKAGE_NAME := cubic_solver
SRC_DIR := cubic_solver
TEST_DIR := tests

# Default target
.DEFAULT_GOAL := help

# Targets
.PHONY: help install install-dev run test lint format clean check-env

help:  ## Display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

check-env:  ## Verify environment setup
	@which poetry >/dev/null || (echo "Poetry not installed. See https://python-poetry.org/docs/"; exit 1)

install: check-env  ## Install production dependencies
	$(POETRY) install --without dev

install-dev: check-env  ## Install development dependencies
	$(POETRY) install

run:  ## Run solver with coefficients (A B C D, default: 0 0 0 0) and number of digits after decimal point to compute and display (default: 10 4)
	$(PYTHON) -m $(PACKAGE_NAME) $(or $(A),0) $(or $(B),0) $(or $(C),0) $(or $(D),0) --n_digits=$(or $(N_DIGITS), 10) --display_digits=$(or $(DISPLAY_DIGITS), 4)

test:  ## Run tests
	$(POETRY) run pytest -v -s $(TEST_DIR) --cov=$(SRC_DIR)

lint:  ## Run static code analysis
	$(POETRY) run flake8 $(SRC_DIR) $(TEST_DIR)
	$(POETRY) run pyright $(SRC_DIR) $(TEST_DIR)

format:  ## Format code automatically
	$(POETRY) run black $(PACKAGE_NAME) $(TEST_DIR)
	$(POETRY) run isort $(PACKAGE_NAME) $(TEST_DIR)

clean:  ## Clean project artifacts
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .coverage htmlcov/ .mypy_cache/ .pytest_cache/
