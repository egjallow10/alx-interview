#!/usr/bin/python3
"""
The N Queens puzzle is a game where you need to
place N chess queens on an N x N chessboard
"""
import sys


def is_valid(board, row, col, N):
    """ function checks if it's valid to place a queen in a given cell"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """function is a recursive function that places queens on the board"""
    if row == N:
        print([[r, c] for r, c in enumerate(board)])
        return
    for col in range(N):
        if is_valid(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def main():
    """function checks if the program is called with  a right arg"""
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
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
