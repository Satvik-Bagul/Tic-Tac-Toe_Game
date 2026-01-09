# Tic Tac Toe
<pre>
A terminal-based interactive Tic-Tac-Toe game implemented in Python. This project 
  demonstrates core computer science principles such as modular programming, data 
  structures, input validation, control flow, and algorithmic problem-solving, while 
  providing an engaging multiplayer game experience.

Features:
  Dynamic n×n Board:
    Board size is user-defined, making the game scalable beyond the traditional 3×3 format.
    ASCII-style rendering for a clean and intuitive visual representation.

  Robust User Input Handling:
    Validates row and column indices to prevent out-of-bounds moves.
    Ensures chosen cells are available and rejects invalid or duplicate entries.

  Win Detection Algorithms:
    Checks rows, columns, and both diagonals for victory conditions.
    Modular functions (row_win, column_win, diag_win, anti_diag_win) enhance readability and maintainability.

  Tie Detection:
    Automatically identifies when all cells are filled without a winner.

  Two-Player Gameplay:
    Alternates turns between Player X and Player O.
    Prints the updated board after every move for clarity.

Core Concepts Demonstrated:
  Modular Functions: print_board, make_empty_board, get_location, has_won, play_game
  Loops & Conditionals: Manage alternating turns, board updates, and game state checks
  Data Structures: 2D lists for board representation, counters for win detection
  Algorithmic Thinking: Implements scalable win/tie evaluation for any n×n board
  Input Validation & Error Handling: Prevents invalid moves and ensures smooth gameplay

Extensions:
  Implement AI opponent using minimax or other algorithms
  Add a GUI version with Tkinter or PyGame
  Track player statistics and game history
  Introduce customizable winning conditions, e.g., k-in-a-row for larger boards
  Include unit tests to verify game logic

Tech Stack & Concepts:
  Python 3.x
  2D Lists & Nested Loops
  Modular function design
  Control flow and algorithmic logic
  Terminal-based interactive applications
</pre>
