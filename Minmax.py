# Function to check if there is a winner or the game is a draw
def check_winner(board):
    winning_combinations = [
        [board[0], board[1], board[2]],  # Row 1
        [board[3], board[4], board[5]],  # Row 2
        [board[6], board[7], board[8]],  # Row 3
        [board[0], board[3], board[6]],  # Column 1
        [board[1], board[4], board[7]],  # Column 2
        [board[2], board[5], board[8]],  # Column 3
        [board[0], board[4], board[8]],  # Diagonal 1
        [board[2], board[4], board[6]],  # Diagonal 2
    ]

    for combo in winning_combinations:
        if combo[0] == combo[1] == combo[2] and combo[0] != ' ':
            return combo[0]

    if ' ' not in board:
        return 'Draw'
    
    return None

# Minimax function to evaluate each move
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function to find the best move for 'X' and return the optimal score and move as (row, col)
def find_best_move(board):
    best_score = -float('inf')
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        row = best_move // 3
        col = best_move % 3
        print(f"Best move for 'X' is at row: {row}, column: {col} with optimal value: {best_score}")
        return (best_score, row, col)

    return None

# Example usage
board = [
    'X', 'O', 'X',
    'O', 'X', ' ',
    ' ', ' ', 'O'
]

find_best_move(board)
