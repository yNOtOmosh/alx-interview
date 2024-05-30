#!/usr/bin/env python3
"""N queens."""
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    backtrack(n, 0, [], solutions)

    for solution in solutions:
        print(solution)

def backtrack(n, row, current_solution, solutions):
    if row == n:
        solutions.append(current_solution.copy())
        return

    for col in range(n):
        if is_safe(current_solution, row, col):
            current_solution.append(col)
            backtrack(n, row + 1, current_solution, solutions)
            current_solution.pop()

def is_safe(current_solution, row, col):
    for i in range(len(current_solution)):
        if current_solution[i] == col or abs(current_solution[i] - col) == abs(i - row):
            return False

    return True

if __name__ == "__main__":
    main()
