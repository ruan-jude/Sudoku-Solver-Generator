VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PATH = /Users/ruanjude/home/code/python/Sudoku-Solver-Generator

run: $(VENV)/bin/activate
	$(PYTHON) $(PATH)/tests/SudokuTest.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf src/__pycache__
	rm -rf $(VENV)