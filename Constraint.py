"""
    This class sets the constraints for our sudoku.

                11 12  13 14
                21 22  23 24

                31 32  33 34
                41 42  43 44

    In the above 4x4 sudoku grid,
    The grid for 11 is: 12 21 22
    The explicit constraint is given as follows:
        1. The numbers in the following pairs of squares cannot be the same:
            (11,12), (11,13), (11, 14), (11,21), (11,31), (11,41), (11,22)

        The above constraints needs to be written for every cell in the sudoku. This can be extended similarly
        for NxN sudoku.
"""
class Constraint:

    def __init__(self, intial_board):
        print(intial_board)