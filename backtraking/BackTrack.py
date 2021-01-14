from copy import deepcopy
from backtraking import MinimumRemainingValueHeuristic
from backtraking.ForwardCheck import *
import random

"""
    By now we have a Constraint satisfaction problem. Now we have to assign values to each variable by 
    satisfying all the constraints.
"""
class BackTracking():
    def __init__(self, forward_check=True):
        if forward_check:
            self.forward_check = ForwardCheck()
        else:
            self.forward_check = None
    """
        In Backtracking, we start with a empty state. (No values to the variables).
        We then pick one variable from the set.

        The order of picking the variables[the square to be filled in sudoku] depends on the heuristics used.
        Here we have used Minimum Remaining Value Heuristic to select the variable.

        The steps for back tracking:
        1. Choose a variable (square in a sudoku)
        2. Pick a value from the domain(1..9)
        3. Check if the picked value satisfies the constraints.
        4. If it does, pick another variable and repeat the process.
        5. If somewhere in the tree if the constraint satisfaction is broken, back track to the parent and try
            replacing the value for the parent variable until all the variables are filled and is consistent with the
            constraints established.
    """

    def backtracking_search(self, constraint, mrv=True):
        return self.backtrack({}, constraint, mrv)

    def backtrack(self, state, constraint, mrv):
        """
        if state is complete, then return state (If all the variable has a particular value)
        :param mrv: flag
        :param state:
        :param constraint:
        :return:
        """
        if self.is_complete(state, constraint):
            return state

        """
            select unassigned variable and assign values to it
            Heuristics -> MRV (Minimum remaining value)
        """
        if mrv:
            cell = MinimumRemainingValueHeuristic.get_minimum_remaining_value(state, constraint)
        else:
            cell = self.next_cell(state, constraint)

        # deep copy
        domain = deepcopy(constraint.board)

        for value in constraint.board[cell]:

            """
                check if the value is consistent, given the restrictions
            """
            if self.is_consistent(cell, value, state, constraint):

                """
                    add cell = val to state
                """
                state[cell] = value

                if self.forward_check is not None:
                    deductions = {}
                    deductions = self.forward_check.infer(state, deductions, constraint, cell, value)
                    if deductions != -1:
                        result = self.backtrack(state, constraint, mrv)
                        if result != -1:
                            return result

                    del state[cell]
                    constraint.board.update(domain)

                else:
                    result = self.backtrack(state, constraint, mrv)
                    if result != -1:
                        return result
                    del state[cell]
                    constraint.board.update(domain)

        return -1

    def is_complete(self, assignment, constraint):
        return set(assignment.keys()) == set(constraint.board.keys())


    def next_cell(self, state, constraint):
        unassigned_cell = {}
        for cell in constraint.board:
            if cell not in state.keys():
                return cell

    def select_random_variables(self, state, constraint):
        unassigned_cell = {}
        for cell in constraint.board:
            if cell not in state.keys():
                unassigned_cell.update({cell: len(constraint.board[cell])})
        return list(unassigned_cell.keys())[random.randint(0,len(unassigned_cell) - 1)]

    def is_consistent(self, var, value, assignment, constraint):
        for neighbor in constraint.neighbour[var]:
            if neighbor in assignment.keys() and assignment[neighbor] == value:
                return False
        return True
