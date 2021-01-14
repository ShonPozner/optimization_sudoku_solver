import time
import backtracking_solver as bk_solver


def read_from_txt(txt_file):
    fp = open(txt_file, "r")
    boards = fp.readlines()

    return boards


def solve_all(solver):
    start = time.time()
    status = solver.solve()
    end = time.time()
    print(f"\tsolver: {solver}\t Time: {end - start}\t Result: [{status[0]}:{status[1]}]\n")


def main():
    sudoku_fils = "sudoku_boards.txt"
    boards = read_from_txt(sudoku_fils)

    back_tracking_solver_solver = bk_solver.Backtracking_solver(boards, print_to_screen=True, arc=True,
                                                                forward_check=True, mrv=False)

    solve_all(back_tracking_solver_solver)



if __name__ == '__main__':
    main()
