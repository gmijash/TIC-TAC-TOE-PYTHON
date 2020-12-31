
#TIC TAC TOE GAME
#Student Western Oregon University
#Author Mijash Ghimire
#3/17/2020



def makeAMove (board, player):
    
    turn_complete = 0
    while turn_complete != 1:
        row = int(input('Enter a row for player {}: '.format(player)))
        while row > 3:
                row = int(input('Enter a row for player {}: '.format(player)))
        col = int(input('Enter a column for player {}: '.format(player)))
        while col > 3:
                col = int(input('Enter a column for player {}: '.format(player)))
        
        if board[row-1][col-1] != 'X' and board[row-1][col-1] != 'O':
            board[row-1][col-1] = player
            turn_complete += 1
        else:
            print('This cell is already occupied. Try a different cell')
        
    return board

def displayBoard(board):
    
    print()
    print('-' * 13)
    print('| {r1c1:^} | {r2c1:^} | {r3c1:^} |'.format(r1c1 = board[0][0], r2c1 = board[1][0], r3c1 = board[2][0]))
    print('-' * 13)
    print('| {r1c2:^} | {r2c2:^} | {r3c2:^} |'.format(r1c2 = board[0][1], r2c2 = board[1][1], r3c2 = board[2][1]))
    print('-' * 13)
    print('| {r1c3:^} | {r2c3:^} | {r3c3:^} |'.format(r1c3 = board[0][2], r2c3 = board[1][2], r3c3 = board[2][2]))
    print('-' * 13)
    return


def isWon (ch, board):
    if board[0][0] == ch and board[0][0] == board[0][1] and board[0][0] == board[0][2]:  
        return True
    elif board[1][0] == ch and board[1][0] == board[1][1] and board[1][0] == board[1][2]:  
        return True
    elif board[2][0] == ch and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return True
    elif board[0][0] == ch and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    elif board[0][2] == ch and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
    elif board[0][0] == ch and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return True
    elif board[0][1] == ch and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return True
    elif board[0][2] == ch and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return True
    else:
        return False


def isDraw(board):
    for l in board:
        for i in l:
            if i == ' ':
                return False
    return True



def playGame(board):
    while isDraw(board) is False:
        

        player = 'X'
        makeAMove(board, player)
        if isWon(player, board):
            displayBoard(board)
            break
        displayBoard(board)
        if isDraw(board):
            print("The game is a tie.")
            break

        player = 'O'
        makeAMove(board, player)
        if isWon(player, board):
            displayBoard(board)
            break
        displayBoard(board)
        if isDraw(board):
            print("The game is a tie.")
            break
    if isWon(player, board):
        print(" {} Player  won".format(player))
        print('****************************************************')


        


board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
playGame(board)
