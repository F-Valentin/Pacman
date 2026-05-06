NAME = pac_man
PYTHON = python3
VENV = venv
BIN = $(VENV)/bin
MAIN = src/pac-man.py
CONFIG_FILE ?= config.json

.PHONY: install run debug clean lint
.SILENT:

install:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

run:
	$(BIN)/python $(MAIN) $(CONFIG_FILE)

clean:
	rm -rf $(VENV)
	rm -rf .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

.PHONY: all run clean