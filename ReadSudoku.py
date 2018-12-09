"""
    Reads the Sudoku Quiz from a text file and its corresponding solution, returns a dictionary
"""

import math
from CUtil import CUtil


class ReadSudoku:
    def __init__(self, path):

        self.sudokus = []  # an array containing all the sudokus from file
        self.grid_sizes = []  # grid size for each sudoku
        self.boards = []  # an array containing all sudokus represented as dictionary

        fp = open(path, "r")
        contents = fp.readlines()

        for line in contents:
            line = line.strip()  # strip the trailing "\n"
            size_of_sudoku = len(line)

            sudoku_size = int(math.sqrt(size_of_sudoku))
            grid_size = int(math.sqrt(sudoku_size))

            self.grid_sizes.append(grid_size)

            constructed_sudoku = self.construct_sudoku(line, sudoku_size)
            self.sudokus.append(constructed_sudoku)

            board = CUtil.generate_board(constructed_sudoku, grid_size)
            self.boards.append(board)

        print(len(self.sudokus) , "sudoku board(s) constructed")

    def get_initial_boards(self):
        return self.sudokus

    def get_grid_sizes(self):
        return self.grid_sizes

    def get_boards(self):
        return self.boards

    @staticmethod
    def construct_sudoku(line, sudoku_size):
        sudoku = []
        for i in range(sudoku_size):
            start = i * sudoku_size
            end = sudoku_size * (i+1)
            split_on_size = line[start: end]
            row = ReadSudoku.get_array(split_on_size)
            sudoku.append(row)

        return sudoku

    @staticmethod
    def get_array(strings):
        array = []
        for string in strings:
            array.append(int(string))

        return array
