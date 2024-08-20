import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count=0
    o_count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                x_count +=1
            elif board[i][j]== O:
                o_count +=1
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):

    available_moves= set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.add((i,j))
    return available_moves


def result(board, action):
    
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action, spot already taken.")

    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
  
    lines = []
    lines.extend(board)
    lines.extend([[board[i][j] for i in range(3)] for j in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    return None
def terminal(board):
    count=0
    if winner(board) is not None:
        return True
    for row in board:
        if not EMPTY in row:
            count+=1
    if count ==3:
        return True
    return False



def utility(board):
 
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def minimax(board):
   
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v, move = min_val, action
            if v == 1:
                break
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v, move = max_val, action
            if v == -1:
                break
    return v, move
