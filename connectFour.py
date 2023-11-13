import Algorithms

#! /usr/bin/env python3
# REFERENCE https://gist.github.com/poke/6934842

from itertools import groupby, chain

def readBoard(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()  
    algorithm = lines[0]
    param = lines[1]
    player = lines[2]
    board = [list(row) for row in lines[3:]]

    return algorithm, param, player, board

def diagonalsPos (matrix, cols, rows):
	"""Get positive diagonals, going from bottom-left to top-right."""
	for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def diagonalsNeg (matrix, cols, rows):
	"""Get negative diagonals, going from top-left to bottom-right."""
	for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

class Game: 
    NONE = 'O'
    RED = 'R'
    YELLOW = 'Y'
    
    def __init__ (self, board, player, cols = 7, rows = 6, requiredToWin = 4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = requiredToWin
        self.board = board
        self.currentPlayer = player

    def legalMoves(self):
        legalMoves = [col for col in range(self.cols) if self.board[col][0]==Game.NONE]
        return legalMoves
    
    def insert (self, column, color):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != Game.NONE:
            raise Exception('Column is full')

        i = -1
        while c[i] != Game.NONE:
            i -= 1
        c[i] = color

        self.checkForWin()

    def checkForWin (self):
        """Check the current board for a winner."""
        w = self.getWinner()
        if w:
            self.printBoard()
            raise Exception(w + ' won!')

    def getWinner (self):
        """Get the winner on the current board."""
        lines = (
			self.board, # columns
			zip(*self.board), # rows
			diagonalsPos(self.board, self.cols, self.rows), # positive diagonals
			diagonalsNeg(self.board, self.cols, self.rows) # negative diagonals
		)

        for line in chain(*lines):
            for color, group in groupby(line):
                if color != Game.NONE and len(list(group)) >= self.win:
                    return color

    def printBoard (self):
        """Print the board."""
        print('  '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()