import math

# Initialize board
board = [' ' for _ in range(9)]


# Display board
def print_board():
    for i in range(3):
        print(board[i * 3:(i + 1) * 3])
    print()


# Check winner
def check_winner():
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pos in win_positions:
        if (board[pos[0]] == board[pos[1]] == board[pos[2]]
                and board[pos[0]] != ' '):
            return board[pos[0]]

    if ' ' not in board:
        return "Draw"

    return None


# Minimax with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    result = check_winner()

    if result == 'X':
        return 10 - depth
    elif result == 'O':
        return depth - 10
    elif result == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'

                eval = minimax(
                    depth + 1, False, alpha, beta
                )

                board[i] = ' '

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

        return max_eval

    else:
        min_eval = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'

                eval = minimax(
                    depth + 1, True, alpha, beta
                )

                board[i] = ' '

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                if beta <= alpha:
                    break

        return min_eval


# Find best move for AI
def best_move():
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'

            move_val = minimax(
                0, False, -math.inf, math.inf
            )

            board[i] = ' '

            if move_val > best_val:
                best_val = move_val
                move = i

    return move


# Game loop
def play_game():
    print("Positions are 0 to 8")
    print_board()

    while True:

        # Human move
        pos = int(input("Enter your move (0-8): "))

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move!")
            continue

        board[pos] = 'O'
        print_board()

        result = check_winner()
        if result:
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'X'

        print("AI chooses:", ai_move)
        print_board()

        result = check_winner()
        if result:
            break

    if result == "Draw":
        print("It's a Draw!")
    else:
        print(result, "wins!")


# Run game
play_game()

