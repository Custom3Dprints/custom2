board = [
    ["X",0,"X","X"],
    [0,"O","X","O"],
    [0,"X","O",0],
    ["X",0,"X",0]
    ]

def determineWinner(board, last_play, y): # y = column
    Wins = [last_play, last_play, last_play, last_play]
    column = [board[i][y] for i in range(len(board))]
    D = [board[i][i] for i in range(4)]
    D2 = [board[3-i][i] for i in range(4)] #Diagonal
    
    for r_num, row in enumerate(board): # checks the first top row
        if column == Wins or row == Wins or D == Wins or D2 == Wins:
            return f"{last_play} wins"
        return False 

print(determineWinner(board, "X", 0))
#print(determineWinner(board, "X", 3, 0))
