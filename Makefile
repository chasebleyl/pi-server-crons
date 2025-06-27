.PHONY: help install install-dev test test-cov test-unit test-integration clean setup-windows setup-linux verify-setup

# Default target
help:
	@echo "Available commands:"
	@echo "  setup-windows  - Setup development environment on Windows"
	@echo "  setup-linux    - Setup development environment on Linux"
	@echo "  install        - Install Python dependencies"
	@echo "  install-dev    - Install development dependencies"
	@echo "  test           - Run all tests"
	@echo "  test-cov       - Run tests with coverage report"
	@echo "  test-unit      - Run only unit tests"
	@echo "  test-integration - Run only integration tests"
	@echo "  test-scripts   - Run tests in scripts directory"
	@echo "  test-db        - Run tests in db directory"
	@echo "  clean          - Clean up test artifacts"
	@echo "  verify-setup   - Verify that setup is correct"
	@echo "  help           - Show this help message"

# Setup commands for different environments
setup-windows:
	@echo "Setting up development environment on Windows..."
	@echo "1. Installing Python dependencies..."
	@pip install -r requirements.txt
	@echo "Setup complete! You can now run 'make test' to run tests."

setup-linux:
	@echo "Setting up development environment on Linux..."
	@echo "1. Installing Python dependencies..."
	@pip install -r requirements.txt
	@echo "Setup complete! You can now run 'make test' to run tests."

# Python dependency installation
install:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt

install-dev:
	@echo "Installing development dependencies..."
	@pip install -r requirements.txt

# Test commands
test:
	@echo "Running all tests..."
	@python -m pytest -v

test-cov:
	@echo "Running tests with coverage..."
	@python -m pytest -v --cov=. --cov-report=term-missing --cov-report=html:htmlcov

test-unit:
	@echo "Running unit tests..."
	@python -m pytest -m unit -v

test-integration:
	@echo "Running integration tests..."
	@python -m pytest -m integration -v

test-scripts:
	@echo "Running tests in scripts directory..."
	@python -m pytest scripts/ -v

test-db:
	@echo "Running tests in db directory..."
	@python -m pytest db/ -v

# Cleanup
clean:
	@echo "Cleaning test artifacts..."
	@rm -rf .coverage htmlcov/ .pytest_cache/ __pycache__/ reports/
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Verify setup
verify-setup:
	@echo "Verifying setup..."
	@echo "Checking for make..."
	@make --version
	@echo "Checking for Python..."
	@python --version
	@echo "Checking for pip..."
	@pip --version
	@echo "Checking for pytest..."
	@python -c "import pytest; print(f'pytest version: {pytest.__version__}')"
	@echo "Setup verification complete!" 