def Grid():
    Board = []
    for i in range(8):
        Board.append([0]*8)
    return Board
Grid = Grid()

def oddnum(x):
    odd_nums =[]
    index = -1
    for i in range(x):
        index += 2
        if index <= x:
            odd_nums.append(index)
    return (odd_nums)

def evennum(y):
    even_nums =[]
    var = -2
    for v in range(y):
        var += 2
        if var <= (y - 1):
            even_nums.append(var)
    return (even_nums)

def print_board(board):
    for row_num, row in enumerate(board):
        for i in range(len(row)): # i = 0-7 row
            if i in oddnum(len(row)): #[1,3,5,7] column
                for e_num in evennum(len(row)): #separate evennum list
                    if e_num != 4: #keeps row 4 = 0
                        board[e_num][i] = 1 #board[even row #'s][i]
            if i in evennum(len(row)): # [0,2,4,6] column
                for o_num in oddnum(len(row)): # separate oddnum list
                    if o_num != 3: #keeps row 3 = 0
                        board[o_num][i] = 1
    
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]])) # [i = row_num 0-7]

print_board(Grid)