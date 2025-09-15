import math

# Initialize board
board = [" " for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

# Check for a winner
def check_winner(board):
    # Winning combinations
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    for (x,y,z) in win_conditions:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    return None

# Check if board is full
def is_full(board):
    return " " not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# AI move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move(board)
        print("AI made a move:")
        print_board(board)

        if check_winner(board) == "O":
            print("😈 AI wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()
