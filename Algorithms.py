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

    @staticmethod
    def dLMinMax(game_play, param):
        goal = connectFour.Game.win
        legal_moves = [col for col in range(connectFour.Game.cols) if connectFour.Game.board[col][0] == "O"]
        best_move = None
        best_value = float('-inf')

        for move in legal_moves:
            new_board = connectFour.Game.makeMove(move, connectFour.Game.currentPlayer)
            value = Algorithms.minmax(new_board, goal, param - 1, float('-inf'), float('+inf'), False)

            if value > best_value:
                best_value = value
                best_move = move

        print("Player's selected move:", best_move)
        return best_move

    @staticmethod
    def minmax(board, goal, depth, alpha, beta, max_player):
        if depth == 0 or connectFour.Game.isWinner() or connectFour.Game.isFull():
            return Algorithms.evaluate(board)

        if max_player:
            max_eval = float('-inf')
            for move in connectFour.Game.legalMoves():
                new_board = connectFour.Game.makeMove(move, connectFour.Game.currentPlayer)
                eval = Algorithms.minmax(new_board, goal, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('+inf')
            for move in connectFour.Game.legalMoves():
                new_board = connectFour.Game.makeMove(move, connectFour.Game.currentPlayer)
                eval = Algorithms.minmax(new_board, goal, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    @staticmethod
    def evaluate(board):
        # You need to implement a proper evaluation function based on the state of the board.
        # Return a value representing the desirability of the board state for the current player.
        pass

    @staticmethod
    def monteCarloGS(algo, param):
        return

    @staticmethod
    def upperConfidenceBound(algo, param):
        return
