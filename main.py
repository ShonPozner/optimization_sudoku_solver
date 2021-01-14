import time
import BacktrackSolver as BkSolver
import LinearProgrammingSolver as LpSolver


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
    sudoku_fils = "sudoku_boards_txt/sudoku_25.txt"
    boards = read_from_txt(sudoku_fils)

    backtracking_solver = BkSolver.BacktrackingSolver(boards, print_to_screen=True, arc=True,
                                                      forward_check=True, mrv=True)

    Lp_solver = LpSolver.LinearProgrammingSolver(boards, print_to_screen=False)

    solve_all(Lp_solver)


if __name__ == '__main__':
    main()
