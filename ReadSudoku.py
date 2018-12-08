"""
    Reads the Sudoku Quiz from a text file and its corresponding solution, returns a dictionary
"""

import math
from PrintSudoku import PrintSudoko

class ReadSudoku:
    def __init__(self, path):

        self.sudokus = []
        self.grid_sizes = []

        fp = open(path, "r")
        contents = fp.readlines()

        for line in contents:
            # the first line is the quiz and the second line is its solution
            line = line.strip()  # strip the trailing "\n"
            size_of_sudoku = len(line)

            sudoku_size = int(math.sqrt(size_of_sudoku))
            grid_size = int(math.sqrt(sudoku_size))
            constructed_sudoku = self.construct_sudoku(line, sudoku_size)
            self.sudokus.append(constructed_sudoku)
            self.grid_sizes.append(grid_size)

        print(len(self.sudokus) , "sudoku board constructed")


    def construct_sudoku(self, line, sudoku_size):
        sudoku = []
        for i in range(sudoku_size):
            start = i * sudoku_size
            end = sudoku_size * (i+1)
            split_on_size = line[start: end]
            row = self.get_array(split_on_size)
            sudoku.append(row)

        return sudoku


    def get_array(self, strings):
        array = []
        for string in strings:
            array.append(int(string))

        return array

    def get_initial_boards(self):
        return self.sudokus

    def get_grid_sizes(self):
        return self.grid_sizes


#ReadSudoku("sudoku-quiz.txt")