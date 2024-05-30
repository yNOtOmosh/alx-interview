#!/usr/bin/env python3
"""N queens."""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row, solutions):
    """Solve the N queens problem using backtracking."""
    if row == len(board):
        solutions.append(board[:])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1

def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
