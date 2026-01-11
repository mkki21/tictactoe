"""
Tic Tac Toe Player
"""

import math
import copy

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

    count_X = 0
    count_O = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_X = count_X + 1
            elif board[i][j] == O:
                count_O = count_O + 1

    # if the number of count for X and O are the same, then X will have the next move, becasue X always makes the first move
    if count_X == count_O:
        return X
    else:
        return O                


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    move = set()

    # Loop through the whole board to see what cells are empty (i.e., available for next move)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                move.add((i, j))
    return move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if board[i][j] != EMPTY:
        raise Exception("Invalid move!")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None

    # Check rows
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None

    # Check diagonals (From top left to bottom right)
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None

    # Check diagonals (From top right to bottom left)
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Either X or O has won
    if winner(board) == X or winner(board) == O:
        return True

    # If no winner, check for any empty cells
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False

    # If no winner and no empty cell, then it's tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)
    
    if win == X:
        return 1
    if win == O:
        return -1
    else:
        return 0


def Max_Value(board):

    if terminal(board):
        return utility(board), None
    
    best_move = None
    best_value = float('-inf')

    # Loop through all moves to determine next best move (i.e. the move with the maximum value)
    for action in actions(board):
        output_value, unused = Min_Value(result(board, action))
        if output_value > best_value:
            best_value = output_value
            best_move = action
            
    return [best_value, best_move]

def Min_Value(board):

    if terminal(board):
        return utility(board), None
    
    best_move = None
    best_value = float('inf')

    # Loop through all moves to determine next best move (i.e. the move with the minimum value)
    for action in actions(board):
        output_value, unused = Max_Value(result(board, action))
        if output_value < best_value:
            best_value = output_value
            best_move = action
            
    return [best_value, best_move]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    if player(board) == X:
        value, move = Max_Value(board)
        return move
    else:
        value, move = Min_Value(board)
        return move
