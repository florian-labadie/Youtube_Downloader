PYTHON = python

TESTS_DIR = tests

MAIN_SCRIPT = main.py

help:
	@echo "Available options:"
	@echo "  run   - Run the main application"
	@echo "  run_CI/CD - Run the main application for CI/CD"
	@echo "  clean - Clean Python cache files"

run:
	$(PYTHON) $(MAIN_SCRIPT)

run_CI-CD:
	$(PYTHON) $(MAIN_SCRIPT) --non-interactive

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: help run test clean