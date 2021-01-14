import time
import backtraking_solver

def read_from_txt(txt_file):
    fp = open(txt_file, "r")
    boards = fp.readlines()

    return boards


def solve_all(boards, solver):

    if solver == 'backtraking':
        backtraking_solver.Backtraking_solver(boards, print_to_screen=True, arc=False, forward_check=True, mrv=True).solve()


def main():
    sudoku_fils = "sudoku_boards.txt"
    boards = read_from_txt(sudoku_fils)

    solver = "backtraking" #Todo Change to class

    solve_all(boards, solver)



if __name__ == '__main__':
    main()
