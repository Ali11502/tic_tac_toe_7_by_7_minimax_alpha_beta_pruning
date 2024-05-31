
import math
import time
import multiprocessing
total_processes=4

def check_winner(board):
    # Check rows
    for row in range(7):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] != '-':
                return board[row][col]

    # Check columns
    for col in range(7):
        for row in range(4):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] != '-':
                return board[row][col]

    # Check diagonals
    for row in range(4):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] != '-':
                return board[row][col]
            if board[row + 3][col] == board[row + 2][col + 1] == board[row + 1][col + 2] == board[row][col + 3] and board[row + 3][col] != '-':
                return board[row + 3][col]

    # Check for tie
    for row in range(7):
        for col in range(7):
            if board[row][col] == '-':
                return None
    return '-'

def alpha_beta_wrapper(args):
    # Wrapper function for multiprocessing
    board, alpha, beta, depth, is_maximizing = args
    return alpha_beta(board, alpha, beta, depth, is_maximizing)

def evaluate(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    score = x_count - o_count

    winner = check_winner(board)
    if winner == 'X':
        score += 100
    elif winner == 'O':
        score -= 100

    return score


def alpha_beta(board, alpha, beta, depth, is_maximizing):
    if game_over(board) or depth == 0:
        return None, evaluate(board)

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for col in get_valid_moves(board):
            row = get_next_open_row(board, col)
            board[row][col] = 'X'
            score = alpha_beta(board, alpha, beta, depth - 1, False)[1]
            board[row][col] = '-'
            if score > best_score:
                best_score = score
                best_move = col
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for col in get_valid_moves(board):
            row = get_next_open_row(board, col)
            board[row][col] = 'O'
            score = alpha_beta(board, alpha, beta, depth - 1, True)[1]
            board[row][col] = '-'
            if score < best_score:
                best_score = score
                best_move = col
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_move, best_score


def get_valid_moves(board):
    return [col for col in range(7) if board[0][col] == '-']


def get_next_open_row(board, col):
    for row in range(7):  # Start from the first row (index 0) and go downwards to the last row (index 6)
        if board[row][col] == '-':
            return row
    return None  # Column is full




def game_over(board):
    winner = check_winner(board)
    if winner is not None:
        return True

    return all(cell != '-' for row in board for cell in row)


def print_board(board):
    for row in board:
        print(' '.join(row))

# Main function to play the game
def play_game():
    # Initialize the game board and variables
    board = [['-' for _ in range(7)] for _ in range(7)]
    player = 'X'
    total_time = 0

    # Continue playing until the game is over
    while not game_over(board):
        if player == 'X':
            # AI's turn (Player X)
            depth = 5  # Set the depth for alpha-beta search
            start_time = time.time()
            pool = multiprocessing.Pool(processes=total_processes)
            moves = []
            for col in range(len(board)):
                row = get_next_open_row(board, col)  # Get the open row for this move
                if row is not None:  # Check if a valid open row is found
                    board_copy = [row[:] for row in board]  # Create a copy of the board
                    board_copy[row][col] = 'X'  # Make the move
                    moves.append((board_copy, -math.inf, math.inf, depth - 1, False))


            # Use multiprocessing to parallelize alpha-beta search for each move
            results = pool.map(alpha_beta_wrapper, moves)
            pool.close()
            pool.join()

            # if results:
        # Select the best move based on the results
            best_move_idx = max(enumerate(results), key=lambda x: x[1][1])[0]
            best_move = moves[best_move_idx][0]
            board = best_move  # Update the board with the best move    
            # else:
            #     print("No valid moves found. Choosing a default move.")
            #     # Choose a default move strategy: picking the first available move
            #     for move in moves:
            #         if move[0]:
            #             board = move[0]  # Update the board with the default move
            #             break  # Exit the loop after finding the first valid move

            end_time = time.time()
            move_time = end_time - start_time
            total_time += move_time
            print(f"Time taken for move: {move_time:.4f} seconds")
            print(f"Total time so far: {total_time:.4f} seconds")
            player = 'O'  # Switch to Player O's turn
        else:
            # Human player's turn (Player O)
            print("Player O's turn.")
            row = int(input("Enter row number (0-6): "))
            col = int(input("Enter column number (0-6): "))

            # Validate the move
            while board[row][col] != '-':
                print("Invalid move. Please try again.")
                row = int(input("Enter row number (0-6): "))
                col = int(input("Enter column number (0-6): "))

            # Apply the move to the board
            board[row][col] = 'O'
            player = 'X'  # Switch to Player X's turn

        print("Current board:")
        print_board(board)  # Print the current board state

    # Game is over, determine the winner or if it's a tie
    winner = check_winner(board)
    if winner is None:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

    print(f"Total time taken for the game: {total_time:.4f} seconds")

# Entry point of the script
if __name__ == "__main__":
    play_game()