#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) safely.

    Args:
        board (list): List where board[i] is the column of the
            queen placed in row i (for rows already filled).
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        True if no other queen attacks this position, else False.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively try to place queens row by row.

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen in.
        board (list): Current partial solution (column per row).
        solutions (list): Accumulator for complete solutions found.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Parse arguments and print all N queens solutions."""
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

    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        formatted = [[i, solution[i]] for i in range(n)]
        print(formatted)


if __name__ == "__main__":
    main()
