# Python Tic-Tac-Toe Simulation
This is a Tic-Tac-Toe Python simulation featuring an AI opponent using the minimax algorithm with alpha-beta pruning.

Note that the AI plays optimally, meaning, it will either win or force a draw.

## Features
* Human vs Computer gameplay.
* Perfect plays using the Minimax search algorithm.
* Alpha-beta pruning for faster decision-making and improved performance.
* Fully terminal-based, requiring no extra imports.


## How the AI Works
The AI uses Minimax, a decision rule used in game theory for minimizing the possible loss in a worst-case scenario.

### Roles:
* Maximizing Player: Computer (O) tries to achieve the highest score (a win).
* Minimizing Player: Human (X) tries to force the lowest score (a loss for the AI).

### Evaluation Function (Scoring):
The scores are adjusted by the search `depth` to encourage the AI to choose the **fastest** winning move:

| Scenario | Score |
| :--- | :--- |
| Computer Win | `+10 - depth` |
| Player Win | `-10 + depth` |
| Draw | `0` |

### Optimization: Alpha-Beta Pruning
Alpha-beta pruning is implemented to cut off search branches that cannot affect the final decision. This significantly reduces recursion and improves the game's overall performance.

## Running the Game
To get the game running on your local machine, follow these steps:

1. Clone the repository:
    * Copy the source code to your machine:
      ```bash
      git clone <repository-url>
      ```
2. Navigate to the project directory:
      ```bash
      cd "Tic-Tac-Toe"
      ```
3. Ensure Python is installed: Verify that you have a Python interpreter available on your system
4. Run the game:
    * Execute the Python script from your terminal
      ```bash
      python3 tictactoe.py
      ```
