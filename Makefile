# Makefile

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python

.PHONY: run

run:
	@echo "Ativando o ambiente virtual e executando o script..."
	. $(VENV_DIR)/bin/activate && $(PYTHON) main.py