import connectFour 
import random

class Algorithms:
    def __init__(self, game):
        self.game = game

    def select_move(self):
        pass
    
    def uniformRandom(self):
        legal_moves = self.game.legalMoves()
        selected_move = random.choice(legal_moves)
        print("Player's selected move:", selected_move)
        return selected_move

    def dLMinMax(self, param):
        goal = self.game.win
        legal_moves = self.game.legalMoves()

        print("Column:\tScore")
        scores = []

        for move in legal_moves:
            new_board = self.game.makeMove(move, self.game.currentPlayer)
            value = self.minmax(new_board, goal, param - 1, float('-inf'), float('+inf'), False)
            scores.append(value)
            print("Column {}: {:.2f}".format(int(move) + 1, float(str(value))))

        best_move = legal_moves[scores.index(max(scores))]

        print("FINAL Move selected: {}".format(float(best_move)))
        return best_move


    def minmax(self, board, goal, depth, alpha, beta, max_player):
        if depth == 0 or self.game.isWinner(self.game.currentPlayer) or self.game.isFull():
            return self.evaluate(board)

        if max_player:
            max_eval = float('-inf')
            for move in self.game.legalMoves():
                new_board = self.game.makeMove(move, self.game.currentPlayer)
                eval = self.minmax(new_board, goal, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('+inf')
            for move in self.game.legalMoves():
                new_board = self.game.makeMove(move, self.game.currentPlayer)
                eval = self.minmax(new_board, goal, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def evaluate(self, board):
        # You need to implement a proper evaluation function based on the state of the board.
        # Return a value representing the desirability of the board state for the current player.
        pass

    def monteCarloGS(self, param):
        return

    def upperConfidenceBound(self,param):
        return
