import Algorithms

#! /usr/bin/env python3
# REFERENCE https://gist.github.com/poke/6934842

from itertools import groupby, chain

# read board info from the txt file
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

    def __init__(self, board, player, cols=7, rows=6, requiredToWin=4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = requiredToWin
        self.board = board
        self.currentPlayer = player
        self.simulationcounter = 0
    
    def simulations_counter(self):
        self.simulationcounter += 1

    def get_simulations(self):
        return self.simulationcounter

    def legalMoves(self):
        legalMoves = [col for col in range(self.cols) if self.board[col][0] == Game.NONE]
        return legalMoves

    # Make a move by inserting the color in the given column.
    # Inside the Game class
    def makeMove(self, column, color):
        c = self.board[column]

        if c[0] != Game.NONE:
            return self.board, False  #game hasn't ended

        # Find the first empty slot in the column and fill it with the current player's color
        for i in range(self.rows - 1, -1, -1):
            if self.board[column][i] == Game.NONE:
                self.board[column][i] = color
                break

        if self.isWinner(color):
            return self.board, True  #game has ended

        if self.isFull():
            return self.board, True

        # Switch to the next player
        self.currentPlayer = Game.RED if self.currentPlayer == Game.YELLOW else Game.YELLOW

        return self.board, False 
    
    # checks the winner
    def isWinner(self, color):
        """Check if the specified color is the winner on the current board."""
        lines = (
            self.board,  # columns
            zip(*self.board),  # rows
            diagonalsPos(self.board, self.cols, self.rows),  # positive diagonals
            diagonalsNeg(self.board, self.cols, self.rows)  # negative diagonals
        )

        for line in chain(*lines):
            for c, group in groupby(line):
                if c == color and len(list(group)) >= self.win:
                    return True
        return False

    # Check if the board is full.
    def isFull(self):
        return all(cell != Game.NONE for col in self.board for cell in col)

    # Print the board.
    def printBoard(self):
        print('  '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.cols)))
    
    #Create a copy of the current game state.
    def copy(self):
        new_game = Game(
            board=[row[:] for row in self.board],
            player=self.currentPlayer,
            cols=self.cols,
            rows=self.rows,
            requiredToWin=self.win
        )
        return new_game
