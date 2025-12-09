# Dynamic GitHub Profile Generator
# Makefile for common development tasks

.PHONY: help install test lint format clean build docs serve

# Default target
help: ## Show this help message
	@echo "Dynamic GitHub Profile Generator - Development Commands"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

# Installation
install: ## Install development dependencies
	pip install -r requirements-dev.txt
	pre-commit install

install-prod: ## Install production dependencies (none required)
	@echo "No production dependencies required - pure Python standard library"

# Testing
test: ## Run all tests
	pytest

test-verbose: ## Run tests with verbose output
	pytest -v

test-coverage: ## Run tests with coverage report
	pytest --cov=. --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

test-unit: ## Run unit tests only
	pytest -m "not integration"

test-integration: ## Run integration tests only
	pytest -m integration

# Code Quality
lint: ## Run all linting tools
	flake8 profile_generator.py templates/ tests/
	mypy profile_generator.py templates/

format: ## Format code with Black and isort
	black .
	isort .

check-format: ## Check code formatting without making changes
	black --check .
	isort --check-only .

# Pre-commit
pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

pre-commit-install: ## Install pre-commit hooks
	pre-commit install

# Building
build: ## Build the package
	python -m build

build-check: ## Check build without creating files
	python -m build --dry-run

# Documentation
docs: ## Build documentation with MkDocs
	mkdocs build

docs-serve: ## Serve documentation locally
	mkdocs serve

docs-deploy: ## Deploy documentation to GitHub Pages
	mkdocs gh-deploy

# Generator
generate: ## Generate README with current configuration
	python profile_generator.py

generate-test: ## Generate README and show diff
	python profile_generator.py
	git diff README.md

# Cleaning
clean: ## Clean up build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf __pycache__/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

clean-all: clean ## Clean everything including virtual environment
	rm -rf venv/
	rm -rf .venv/

# Development setup
setup: ## Complete development setup
	python -m venv venv
	source venv/bin/activate && make install
	make pre-commit-install
	@echo "Development environment setup complete!"

# CI/CD simulation
ci: ## Run full CI pipeline locally
	make lint
	make test-coverage
	make build-check
	@echo "CI pipeline completed successfully!"

# Utility
count-lines: ## Count lines of code
	find . -name "*.py" -not -path "./venv/*" -not -path "./.venv/*" | xargs wc -l

deps-update: ## Update all dependencies
	pip install --upgrade pip
	pip install --upgrade -r requirements-dev.txt

# Release helpers
bump-patch: ## Bump patch version
	bump2version patch

bump-minor: ## Bump minor version
	bump2version minor

bump-major: ## Bump major version
	bump2version major

# Docker (future feature)
docker-build: ## Build Docker image
	docker build -t dynamic-profile-generator .

docker-run: ## Run in Docker container
	docker run --rm dynamic-profile-generator

# Help for Windows users
windows-setup: ## Windows-specific setup instructions
	@echo "Windows Development Setup:"
	@echo "1. Install Python 3.7+ from https://python.org"
	@echo "2. Clone repository: git clone <url>"
	@echo "3. Create venv: python -m venv venv"
	@echo "4. Activate venv: venv\\Scripts\\activate"
	@echo "5. Install deps: pip install -r requirements-dev.txt"
	@echo "6. Install hooks: pre-commit install"
	@echo "7. Run tests: pytest"

# Emergency commands
emergency-clean: ## Nuclear option - clean everything
	git clean -fdx
	git reset --hard HEAD

# Aliases for common tasks
t: test  ## Alias for test
c: clean  ## Alias for clean
f: format  ## Alias for format
l: lint  ## Alias for lint