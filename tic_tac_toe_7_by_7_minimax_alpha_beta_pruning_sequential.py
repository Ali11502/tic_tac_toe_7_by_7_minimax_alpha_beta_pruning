import math


def alpha_beta(board, alpha, beta, depth, is_maximizing):
    if game_over(board) or depth == 0:
        return None, evaluate(board)

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '-':
                    board[row][col] = 'X'
                    score = alpha_beta(board, alpha, beta, depth - 1, False)[1]
                    board[row][col] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                    score = alpha_beta(board, alpha, beta, depth - 1, True)[1]
                    board[row][col] = '-'
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_move, best_score


def evaluate(board):
    # calculate score based on the number of pieces on the board
    x_count = 0
    o_count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'X':
                x_count += 1
            elif board[row][col] == 'O':
                o_count += 1
    score = x_count - o_count

    # check for win conditions
    winner = check_winner(board)
    if winner == 'X':
        score += 100
    elif winner == 'O':
        score -= 100

    return score


def check_winner(board):
    # check rows
    for row in range(7):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][
                col] != '-':
                return board[row][col]

    # check columns
    for col in range(7):
        for row in range(4):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][
                col] != '-':
                return board[row][col]

    # check diagonals
    for row in range(4):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and \
                    board[row][col] != '-':
                return board[row][col]
            if board[row + 3][col] == board[row + 2][col + 1] == board[row + 1][col + 2] == board[row][col + 3] and \
                    board[row + 3][col] != '-':
                return board[row + 3][col]

    # check for tie
    for row in range(7):
        for col in range(7):
            if board[row][col] == '-':
                return None
    return '-'


def game_over(board):
    if check_winner(board) is not None:
        return True
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '-':
                return False
    return True


board = [['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-']
         ]


def print_board(board):
    for row in range(7):
        for col in range(7):
            print(board[row][col], end=' ')
        print()


# This is the main function for playing the game
def play_game():
    print('Note: You may feel program is not running when you play it but it will you will have to wait!! thank you')
    board = [
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-']
    ]
    player = 'X'

    while not game_over(board):
        if player == 'X':
            print("Player X's turn.")
            depth = 5  # adjust depth based on difficulty level
            move = alpha_beta(board, -math.inf, math.inf, depth, True)[0]
            board[move[0]][move[1]] = 'X'
            player = 'O'
        else:
            print("Player O's turn.")
            row = int(input("Enter row number (0-6): "))
            col = int(input("Enter column number (0-6): "))
            while board[row][col] != '-':
                print("Invalid move. Please try again.")
                row = int(input("Enter row number (0-6): "))
                col = int(input("Enter column number (0-6): "))
            board[row][col] = 'O'
            player = 'X'
        print("Current board:")
        print_board(board)

    winner = check_winner(board)
    if winner is None:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")


def print_board(board):
    for row in range(7):
        for col in range(7):
            print(board[row][col], end=' ')
        print()


play_game()
