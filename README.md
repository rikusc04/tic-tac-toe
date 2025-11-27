# Tic-Tac-Toe
This is a tic-tac-toe Python simulation featuring an AI opponent using the minimax algorithm with alpha-beta pruning. Note that the AI plays optimally, meaning, it will either win or force a draw.

Features:
- Human vs Computer
- Perfect plays using minimax search
- Alpha-beta pruning for faster decision making
- Fully terminal based, so no extra imports needed

How the AI workd:
- The AI uses minimax, a decision rule used in AI, decision/game theory, etc. for minimizing the possible loss for a maximum loss scenario
- Maximizing player: Computer (O) tries to get the highest score
- Minimizing player: Human (X) tries to force the lowest score
- Evaluation function:
  - Computer win —> +10 - depth
  - Player win —> -10 + depth
  - Draw → 0
- Alpha-beta pruning cuts off branches that can’t affect the final decision which reduces recursion and improves performance

Running the Game:
- Make sure you have Python installed
- Then run: python3 tictactoe.py
