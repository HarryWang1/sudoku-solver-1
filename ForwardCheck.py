
class ForwardCheck:
    """
        Forward checking is mainly used for early detection of failures.
        Terminate search when any variable has no legal values.

        1. assign value to a variable[a square or a box]
        2. iterate over the peers of the square
        3. if the peers is not already assigned a value and if the given value is in probable list of values (domain)
            for the neighbour, remove that value from the neighbour's probable list(domain)

            In other words, remove values for neighbour from domain that are inconsistent with A
    """

    def inference(self, assignment, inferences, constraint, var, value):
        inferences[var] = value

        for neighbor in constraint.neighbour[var]:
            if neighbor not in assignment and value in constraint.board[neighbor]:
                if len(constraint.board[neighbor]) == 1:
                    return -1

                remaining = constraint.board[neighbor] = constraint.board[neighbor].replace(value, "")
                if len(remaining) == 1:
                    flag = self.inference(assignment, inferences, constraint, neighbor, remaining)
                    if flag == -1:
                        return -1
        return inferences