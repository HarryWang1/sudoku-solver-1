def get_minimum_remaining_value(assignment, constraint):
    unassigned_variables = dict(
        (cell, len(constraint.board[cell])) for cell in constraint.board if
        cell not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv