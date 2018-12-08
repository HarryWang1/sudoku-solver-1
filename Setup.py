from ReadSudoku import ReadSudoku
from PrintSudoku import PrintSudoko
from Constraint import *

read_pointer = ReadSudoku("sudoku-quiz.txt")

initial_boards = read_pointer.get_initial_boards()
grid_sizes = read_pointer.get_grid_sizes()

for index, board in enumerate(initial_boards):
    Constraint(board)

    #PrintSudoko(board, grid_sizes[index])

