import json
from sudoku_board import SudokuBoard
file = open("sudokuPuzzle.json", 'r')
json_parser = json.load(file)
SudokuBoard(json_parser)
