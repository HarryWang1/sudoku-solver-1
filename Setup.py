from ReadSudoku import ReadSudoku
from Constraint import *

read_pointer = ReadSudoku("sudoku-quiz.txt")

boards = read_pointer.get_boards()
grid_sizes = read_pointer.get_grid_sizes()

board_constraints = CUtil.generate_constraint_dictionary(3)  # for a 9x9 Sudoku

for index, board in enumerate(boards):
    Constraint(board, board_constraints, grid_sizes[index])
