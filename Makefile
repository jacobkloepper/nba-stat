SOURCE_DIR = src
SCRIPT_DIR = scripts

SOURCES = $(wildcard $(SOURCE_DIR)/*.py)

.PHONY: all run setup

all: setup run

run:
	python3 $(SOURCE_DIR)/main.py
	python3 $(SOURCE_DIR)/update.py

setup:
	@echo Setting up
	@sh $(SCRIPT_DIR)/setup.sh

