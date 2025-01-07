#!/usr/bin/python3
"""
    The “0x05. N queens” project is a classic problem in computer science
    and mathematics, known for its application of the backtracking algorithm
    to place N non-attacking queens on an N×N chessboard.
"""

import sys


def print_solution(board):
    """Prints the solution board."""
    print(board)


def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at the given row and column."""
    for i in range(row):
        if board[i][1] == col or \
           board[i][1] - i == col - row or \
           board[i][1] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board):
    """Solves the N Queens problem using backtracking."""
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board.append([row, col])
            solve_nqueens(N, row + 1, board)
            board.pop()


def main():
    """Main function"""
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

    board = []
    solve_nqueens(N, 0, board)


if __name__ == "__main__":
    main()
