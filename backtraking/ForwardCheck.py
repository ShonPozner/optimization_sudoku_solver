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

    def infer(self, state, deductions, constraint, cell, value):
        deductions[cell] = value

        for neighbor in constraint.neighbour[cell]:
            if neighbor not in state and value in constraint.board[neighbor]:
                if len(constraint.board[neighbor]) == 1:
                    return -1
                left_over_values = self.get_left_over_values_in_domain(constraint, neighbor, value)

                if len(left_over_values) == 1:
                    check = self.infer(state, deductions, constraint, neighbor, left_over_values)
                    if check == -1:
                        return -1
        return deductions

    def get_left_over_values_in_domain(self, constraint, neighbor, value):
        constraint.board[neighbor] = constraint.board[neighbor].replace(value, "")
        return constraint.board[neighbor]
