def print_board(board):
    print("------------------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------------")

def check_win(board, player):
    #check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][1] == player and board[1][i] == player and board[2][1] == player):
           return True
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
           return True
        return False
def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = 0
    print_board(board)
    while True:
        row = int(input("Player " + players[current_player] + ", choose a row (1-3): ")) -1
        col = int(input("Player " + players[current_player] + ", choose a column (1-3): ")) -1
        if board[row] [col] != ' ':
           print("That space is already taken.Try again.")
           continue
        board[row] [col] = players[current_player]
        print_board(board)
        if check_win(board, players[current_player]):
            print("player " + player[current_player] + " wins!")
            break
        if all ([space != ' ' for row in board for space in row]):
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2

tic_tac_toe()        

        
           
