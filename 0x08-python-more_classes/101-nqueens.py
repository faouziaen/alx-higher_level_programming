#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == col - i:
            return False
    return True


def solve_queens(board, col, N, solutions):
    if col == N:
        solutions.append(board[:])
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_queens(board, col + 1, N, solutions)


def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    solutions = []
    solve_queens(board, 0, N, solutions)
    print_solutions(solutions)
