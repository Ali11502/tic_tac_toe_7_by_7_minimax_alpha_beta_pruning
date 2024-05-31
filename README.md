# 7 by 7 tic-tac-toe (Connect Four) with Alpha-Beta Pruning

This is a Python implementation of the classic 7 by 7 tic-tac-toe (Connect Four)  game, featuring an AI opponent using the Alpha-Beta pruning algorithm for optimal move selection. The game allows a human player to compete against the AI.

## Features

- **AI Opponent**: Uses the Alpha-Beta pruning algorithm to select the best move.
- **Human Player**: The human player can input their moves via the console.
- **Multiprocessing**: Utilizes multiprocessing to parallelize the AI's move calculations for improved performance.
- **Win Detection**: Automatically detects the winner or a tie after each move.
- **Game Board Printing**: Displays the current state of the game board after each turn.

   
2. **Gameplay Instructions**:
   - The game starts with the AI (Player 'X') making the first move.
   - After the AI's move, the game board is displayed.
   - The human player (Player 'O') is prompted to enter the row and column numbers for their move.
   - The game continues alternating turns between the AI and the human player until there is a winner or a tie.

## Functions

Here is a list of key functions used in the game:

- **`check_winner(board)`**: Checks if there is a winner on the game board.
- **`alpha_beta_wrapper(args)`**: Wrapper function for multiprocessing.
- **`evaluate(board)`**: Evaluates the current game state and assigns a score.
- **`alpha_beta(board, alpha, beta, depth, is_maximizing)`**: Implements the Alpha-Beta pruning algorithm for optimal move selection.
- **`get_valid_moves(board)`**: Gets a list of valid moves (columns) on the game board.
- **`get_next_open_row(board, col)`**: Gets the next available row for a move in a specific column.
- **`game_over(board)`**: Checks if the game is over (winner or tie).
- **`print_board(board)`**: Prints the current game board.
- **`play_game()`**: Main function to play the game.

## Example Gameplay

1. **AI's Move**:
   ```
   Time taken for move: 0.1234 seconds
   Total time so far: 0.1234 seconds
   ```
   ```
   Current board:
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - X - - - - -
   ```

2. **Human's Move**:
   ```
   Player O's turn.
   Enter row number (0-6): 6
   Enter column number (0-6): 1
   ```
   ```
   Current board:
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - - - - - - -
   - X O - - - -
   ```

## Notes

- The game board is a 7x7 grid.
- The AI uses a depth of 5 for the Alpha-Beta search, which can be adjusted for different levels of difficulty and performance.
- The game uses multiprocessing to improve the performance of the AI's move calculations.
