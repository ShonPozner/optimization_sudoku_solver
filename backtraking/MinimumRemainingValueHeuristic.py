def get_minimum_remaining_value(state, constraint):
    unassigned_cell = {}
    for cell in constraint.board:
        if cell not in state.keys():
            unassigned_cell.update({cell: len(constraint.board[cell])})
    minimum_remaining_value = min(unassigned_cell, key=unassigned_cell.get)
    return minimum_remaining_value