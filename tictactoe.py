"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #If X is equal to the amount of O's, it is X's turn
    X_num = sum(row.count(X) for row in board)
    O_num = sum(row.count(O) for row in board)

    if X_num <= O_num:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check horizontally
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] is not None:
                return row[0]
        
    #Checks vertically
    for col in range(3):
        if board[col][0] == board[col][1] == board[col][2]:
            if board[col][0] is not None:
                return board[col][0]
    
    #Checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    #If tie/no three in a row
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Three in a row is found
    if winner(board) == True:
        return True
    
    #There is still an empty spot
    for row in board:
        if EMPTY in row:
            return False
    
    #Will return True if all rows are filled
    return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    #If X wonw
    if winner(board) == X:
        return 1
    
    #If O won
    elif winner(board) == O:
        return -1

    #If tie
    else: 
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
