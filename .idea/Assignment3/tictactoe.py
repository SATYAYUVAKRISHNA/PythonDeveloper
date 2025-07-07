import math

# Initialize the board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for a winner
def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for cond in win_conditions:
        if all(brd[i] == player for i in cond):
            return True
    return False

# Check for tie
def is_full(brd):
    return " " not in brd

# Get available moves
def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == " "]

# Minimax algorithm
def minimax(brd, is_maximizing):
    if check_winner(brd, "O"):
        return {"score": 1}
    elif check_winner(brd, "X"):
        return {"score": -1}
    elif is_full(brd):
        return {"score": 0}

    if is_maximizing:
        best = {"score": -math.inf}
        for move in get_available_moves(brd):
            brd[move] = "O"
            sim_score = minimax(brd, False)
            brd[move] = " "
            sim_score["move"] = move
            if sim_score["score"] > best["score"]:
                best = sim_score
        return best
    else:
        best = {"score": math.inf}
        for move in get_available_moves(brd):
            brd[move] = "X"
            sim_score = minimax(brd, True)
            brd[move] = " "
            sim_score["move"] = move
            if sim_score["score"] < best["score"]:
                best = sim_score
        return best

# Player move
def player_move():
    move = -1
    while move not in get_available_moves(board):
        try:
            move = int(input("Enter your move (0-8): "))
        except ValueError:
            continue
    board[move] = "X"

# AI move
def ai_move():
    print("AI is thinking...")
    move = minimax(board, True)["move"]
    board[move] = "O"

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        if is_full(board):
            print("It's a tie!")
            break

        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("AI wins! 🤖")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()