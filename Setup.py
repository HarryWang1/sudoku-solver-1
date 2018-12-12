from ReadSudoku import ReadSudoku
from Constraint import *
from ArcConsistency import *
from BackTrack import *
import time

read_pointer = ReadSudoku("sudoku-quiz.txt")

boards = read_pointer.get_boards()
grid_sizes = read_pointer.get_grid_sizes()

board_constraints = CUtil.generate_constraint_dictionary(3)  # for a 9x9 Sudoku

counter = 0
for index, board in enumerate(boards):
    prev = time.time()
    constraint = Constraint(board, board_constraints, grid_sizes[index])
    # arc = ArcConsistency(constraint)
    # arc_consistent_sudoku = arc.ac3(constraint)
    # check_complete = arc.is_complete(constraint)
    # if check_complete and arc_consistent_sudoku:
    #     print("After solving: ", constraint.board)
    #     print("Running time: ", time.time() - prev, "\n")

    back_track = BackTracking()
    backtrack_sudoku = back_track.backtracking_search(constraint)
    if backtrack_sudoku != "FAILURE":
        # print("After solving: ", constraint.board)
        print("Running time: ", time.time() - prev, "\n")
