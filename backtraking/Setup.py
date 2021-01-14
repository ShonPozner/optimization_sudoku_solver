from ReadSudoku import ReadSudoku
from Constraint import *
from ArcConsistency import *
from BackTrack import *
import time
import os

read_pointer = ReadSudoku("sudoku-quiz.txt")

boards = read_pointer.get_boards()
grid_sizes = read_pointer.get_grid_sizes()

board_constraints = CUtil.generate_constraint_dictionary(3)  # for a 9x9 Sudoku

counter = 0
arc_consistency_time = []
backtrack_mrv_forward_checking_time = []
backtrack_time = []


def solve_using_arc_consistency(constraint, start_time):
    arc = ArcConsistency(constraint)
    arc_consistent_sudoku = arc.ac3(constraint)
    check_complete = arc.is_complete(constraint)
    if check_complete and arc_consistent_sudoku:
        running_time = time.time() - start_time
        print(" solve_using_arc : Running time: ", running_time, "\n")
        arc_consistency_time.append(running_time)


def solve_using_backtrack_and_mrv(constraint, start_time):
    back_track = BackTracking()
    backtrack_sudoku = back_track.backtracking_search(constraint, True)
    if backtrack_sudoku != -1:
        running_time = time.time() - start_time
        print("backtrack_and_mrv : Running time: ", running_time, "\n")
        backtrack_mrv_forward_checking_time.append(running_time)


def solve_using_backtrack(constraint, start_time):
    back_track = BackTracking()
    backtrack_sudoku = back_track.backtracking_search(constraint, False)
    if backtrack_sudoku != -1:
        running_time = time.time() - start_time
        print("backtrack : Running time: ", running_time, "\n")
        backtrack_time.append(running_time)


for index, board in enumerate(boards):
    constraint = Constraint(board, board_constraints, grid_sizes[index])

    start_time = time.time()
    solve_using_arc_consistency(constraint, start_time)

    # backtrack_mrv_start_time = time.time()
    # solve_using_backtrack_and_mrv(constraint, backtrack_mrv_start_time)

    backtract_start_time = time.time()
    solve_using_backtrack(constraint, backtract_start_time)

file = open("arc_consistency_time.txt", "w")
for time in arc_consistency_time:
    file.write(str(time) + "\n")

backtrack__mrv_file = open("backtrack_mrv_forward_check_time.txt", "w")
for time in backtrack_mrv_forward_checking_time:
    backtrack__mrv_file.write(str(time) + "\n")

backtrack_file = open("backtrack_without_mrv_time.txt", "w")
for time in backtrack_time:
    backtrack_file.write(str(time) + "\n")
