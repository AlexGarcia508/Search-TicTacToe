"""
Tic Tac Toe Player
"""

"""
CECS 451 Sec 02
Student Names:
Alex Garcia 
Chase Calero 
Shivkumar Manek 
Travis Nguyen 
Vincent Tran

Summary:
Most of the coding was straight forward. All of the functions were names what they were suppose to do. The only ones that was confusing was actions, results, and minimax.
Actions and results were a bit confusing because we didn't realized that it was suppose to use player(board) to decide who's turn it is. While minimax was confusing because
that was the actual AI part. Thanks to the help of the sides, we were able to figure out that min and max was suppose to increase or decrease the chances of X or O winning.
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

    #If X is equal to the amount of O's, it is X's turn. This is mainly for the bot.
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
    rows = 3
    cols = 3

    actions = set()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action == None) or (board[action[0]][action[1]] is not EMPTY):
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check horizontally
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] is not EMPTY:
                return row[0]
        
    #Checks vertically
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] is not EMPTY:
                return board[0][col]
    
    #Checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    #If tie/no three in a row
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Three in a row is found
    if winner(board) is not None:
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
    if terminal(board):
        return None

    #Checks who's turn it in
    if player(board) == X:
        #If AI is X, uses min_value to decrease chances of X winning
        calucation = -math.inf
        best_action = None
        for action in actions(board):
            #Calculates min by taking each avaiable action of board and putting it into results
            min = min_value(result(board, action))
            if min > calucation:
                calucation = min
                best_action = action
        return best_action
    else: 
        #If AI is O, uses max_value to increase chances of X winning
        calucation = math.inf
        best_action = None
        for action in actions(board):
            #Calculates max by taking each avaiable action of board and putting it into results
            max = max_value(result(board, action))
            if max < calucation:
                calucation = max
                best_action = action
        return best_action



def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v