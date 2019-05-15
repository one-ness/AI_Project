import math as m
from enum import Enum

class MoveType(Enum):
    UNABLE = -1
    REGULAR = 0
    JUMP = 1

def canMove(board, piece, move, turn):
    row = piece[0] + move[0]
    col = piece[1] + move[1]
    if col >= board.width or row >= board.height or board[row][col] == turn:
        return MoveType.UNABLE
    if board[row][col] != ' ':
        return MoveType.JUMP
    
def move(board, piece, move, turn):
    col = piece[0] + move[0]
    row = piece[1] + move[1]
    board.board[piece[0]][piece[1]] = ' '
    if turn == board.BLACK:
        board.board[row][col] = u'◇'
    else:
        board.board[row][col] = u'◆'

def findBestMove(board, turn):
    bestScore = -m.inf
    bestMove;
    bestMoveCol = -1
    bestMoveRow = -1
    turns = 0
    
    # max
    if turn == board.BLACK:
        for piece in board.blacks:
            moveType = canMove(board, piece, (1,-1), board.BLACK)
            if moveType == MoveType.JUMP:
                move(board, piece, (1,-1), board.BLACK)
            elif moveType == MoveType.REGULAR:
                move(board, piece, (1,-1), board.BLACK)
                turns = turns + 1
            val = minimax(board, piece, turns, board.BLACK)
            
            moveType = canMove(board, piece, (1,1), board.BLACK)
            if moveType == MoveType.JUMP:
                move(board, piece, (1,-1), board.BLACK)
            elif moveType == MoveType.REGULAR:
                move(board, piece, (1,-1), board.BLACK)
                turns = turns + 1
    # min
    if turn == board.WHITE:
        None
def client():
    b = Board(8,8)
    turn = b.WHITE
    b.printBoard()
    while(True):
        print('Select a piece to move (eg. "a5"):')
        moveFrom = input().lower()
        if len(moveFrom) != 2:
            continue
        xFrom = ord(moveFrom[0])-97
        yFrom = int(moveFrom[1])
        if ((xFrom,yFrom) not in b.whites and turn == b.WHITE) or ((xFrom,yFrom) not in b.blacks and turn == b.BLACK) or xFrom > b.height - 1 or yFrom > b.width - 1 or xFrom < 0 or yFrom < 0:
            print("That isn't your piece")
            continue
        print('Make a move ("cancel" to re-select):')
        moveTo = input().lower()
        if moveTo == "cancel" or len(moveTo) != 2:
            continue
        xTo = ord(moveTo[0])-97
        yTo = int(moveTo[1])
        if (xTo, yTo) in b.whites or (xTo, yTo) in b.blacks or xTo > b.height - 1 or yTo > b.width - 1 or xTo < 0 or yTo < 0:
            print('Invalid move.')
            continue
        if turn == b.WHITE:
            b.whites.remove((xFrom, yFrom))
            b.whites.add((xTo, yTo))
            b.board[xFrom][yFrom] = ' '
            b.board[xTo][yTo] = u'◆'
            turn = b.BLACK
        else:
            b.blacks.remove((xFrom, yFrom))
            b.blacks.add((xTo, yTo))
            b.board[xFrom][yFrom] = ' '
            b.board[xTo][yTo] = u'◇'
            turn = b.WHITE
        b.printBoard()
class Board(object):
    BLACK = 1
    WHITE = 0
    
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.blacks = {(0, 1), (0, 3), (0, 5), (0, 7), (2, 1), (2, 3),
                       (2, 5), (2, 7), (1, 0), (1, 2), (1, 4), (1, 6)}
        self.whites = {(6, 1), (6, 3), (6, 5), (6, 7), (5, 0), (5, 2),
                       (5, 4), (5, 6), (7, 0), (7, 2), (7, 4), (7, 6)}
        # initialize board
        self.board = [[' '] * self.width for x in range(self.width)]
        # pieces setup
        for i in range(8):
            for j in range(8):
                if (i,j) in self.blacks:
                    self.board[i][j] = u'◇'
                elif (i,j) in self.whites:
                    self.board[i][j] = u'◆'
    
    def printBoard(self):
        print(str(self))
        
    def __str__(self):
        lines = []
        # This prints the numbers at the top of the Game Board
        lines.append('    ' + '   '.join(map(str, range(self.width))))
        # Prints the top of the gameboard in unicode
        lines.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')
        
        # Print the boards rows
        for num, row in enumerate(self.board[:-1]):
            lines.append(chr(num+65) + u' │ ' + u' │ '.join(row) + u' │')
            lines.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
        
        #Print the last row
        lines.append(chr(self.height+64) + u' │ ' + u' │ '.join(self.board[-1]) + u' │')

        # Prints the final line in the board
        lines.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
        return '\n'.join(lines)
client()
