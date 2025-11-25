# Defining useful global variables and costants
board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

PLAYER = "X" #initializes the constant as "X"; The HUMAN IS X
COMPUTER = "O" #initializes the constant as "Y": THE COMPUTER IS Y

def reset_board():
    global board
    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def print_board():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def check_winner():
    #check rows:
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == PLAYER:
                return PLAYER
            elif board[i][0] == COMPUTER:
                return COMPUTER
        
    #check columns:
    for i in range(3):
        if board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == PLAYER:
                return PLAYER
            elif board[0][i] == COMPUTER:
                return COMPUTER
        
    #check diagonals:
    if board[1][1] != " " and board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return PLAYER
        elif board[0][0] == COMPUTER:
            return COMPUTER
    
    if board[1][1] != " " and board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return PLAYER
        elif board[0][2] == COMPUTER:
            return COMPUTER
    
    return None
    

def check_draw():
    if check_free_spaces() == 0:
        return True
    return False

def check_free_spaces():
    free_spaces = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":  #if the current space doesn't equal an empty space, 
                free_spaces -= 1    #subtract one from the remaining number of free spaces

    return free_spaces
    

def minimax_algorithm(depth, alpha, beta, is_maximizing):
    winner = check_winner()
    if winner == PLAYER:
        return -10 + depth
    if winner == COMPUTER:
        return 10 - depth
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = COMPUTER
                    score = minimax_algorithm(depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        return best_score
        return best_score
    
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = PLAYER
                    score = minimax_algorithm(depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        return best_score
        return best_score

def computer_move():
    best_score = -float("inf")
    best_move = None
    alpha = -float("inf")
    beta = float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = COMPUTER
                score = minimax_algorithm(0, alpha, beta, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # pruning at root
    x = best_move[0]
    y = best_move[1]
    board[x][y] = COMPUTER



def player_move():
    while True:
        x = input("Enter the row number, 1 - 3: ")
        while not x.isdigit() or not(1 <= int(x) <= 3):
            x = input("Please enter a valid row number, from 1 - 3: ")

        y = input("Enter the column number, 1 - 3: ")
        while not y.isdigit() or not (1 <= int(y) <= 3):
            y = input("Please enter a valid column number, from 1 - 3: ")

        x = int(x) - 1
        y = int(y) - 1

        if board[x][y] == " ":
            break
        else:
            print("Unfortunately, that spot is taken")
    board[x][y] = PLAYER

def main():
    winner = None
    reset_board() #resets the board to initial state and returns it
    while winner is None and check_free_spaces() != 0: #while the there is no winner and there is a move available
        print_board() #prints the board
        player_move()
        winner = check_winner()
        if winner is not None or check_free_spaces() == 0: #if there is a winner, or if there are no free spaces
            break
        computer_move()
        winner = check_winner()
        if winner is not None or check_free_spaces() == 0: #if there is a winner, or if there are no free spaces
            break
    print_board()
    if check_free_spaces() == 0:
        print("Unfortunately, the game ended in a draw!")
    elif winner == PLAYER:
        print("Congratulations! You won the game!")
    else: #winner == COMPUTER
        print("Too bad! You Lost!")

main()