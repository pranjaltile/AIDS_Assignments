N = 8

def is_safe(board, row, col):
    # Check if there's a queen in the same row to the left
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check if there's a queen in the upper left diagonal
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check if there's a queen in the lower left diagonal
    for x, y in zip(range(row, N), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # If all queens are placed, print the board
    if col == N:
        for row in board:
            print(row)
        print()
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack

    return False

if __name__ == "__main__":
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution found")
