PYTHON = python3
SCRIPT = src/pac-man.py
CONFIG_FILE ?= config.json

.PHONY: install run debug clean lint
.SILENT:

run:
	$(PYTHON) $(SCRIPT) $(CONFIG_FILE)

clean:
	rm -rf src/__pycache__
	rm -rf __pycache__

.PHONY: all run clean