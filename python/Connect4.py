def Board():
    board = [[0]*13 for v in range(1,8)]
    num = 1
    for a,b in enumerate(board):
        for c,d in enumerate(b):
            if c % 2 != 0:
                board[a][c] = "|"
       
    for n, lastrow in enumerate(board[-1]): #numbered last list
        if lastrow != "|":
            board[-1][n] = num
            num += 1
    return board


def get_turn(i):
    if i % 2 != 0:
        return "X"
    else:
        return "O"

def True_iput(turn):
    value = False
    while value == False:
        try:
            play = int(input(f"Enter where you want {turn} to go: "))
            if play in range(1, 8):
                value = True
                return play
            else:
                value = False
        except ValueError:
            value = False

def get_place(Input, turn, board): #replaces number with "X", "O"
    for rnum, row in enumerate(board):
        for cnum, column in enumerate(row):
            if column == Input: # Input == number
                board[rnum][cnum] = turn 
                board[rnum - 1][cnum] = Input #replaces row above with coordnating number
    for a in board:
        print(" ".join([str(c) for c in a]))
    
    return board

def Check_board(board):
    board2 = []
    for a,b in enumerate(board):
        board2.append([c for c in b if c != "|"])
    return board2

#determine winner still need work on 4 placers in a row in a list lenght of 7
def determine_winner(board, last_play):
    Wins = [last_play]*4
    print(board)
    for index in range(7):
        row = board[index]
        column = [board[i][index] for i in range(7)]
        diagonal = [board[i][i] for i in range(7)]
        diagonal2 = [board[2-i][i] for i in range(7)]

        if column == Wins or row == Wins or diagonal == Wins or diagonal2 == Wins:
            return(f"{last_play} Won")

def output():
    board = (Board())
    for a in board:
        print(" ".join([str(c) for c in a]))
   
    for i in range(1, 50): # 1,8
        Turn = get_turn(i) # X or O
        Input = True_iput(Turn) # gets valid number input
        Place = get_place(Input, Turn, board)
        check_board = Check_board(Place)
        winner = determine_winner(check_board, Turn)
        if type(winner) == str:
            return winner
        if i == 8 and type(winner) == None:
            return "\nCongrats you both lose"
print(output())

