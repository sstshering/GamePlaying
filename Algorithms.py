import connectFour 
import random
from itertools import chain
import copy
class Algorithms:
    def __init__(self, game):
        self.game = game

    def select_move(self):
        pass
    
    # Algo 1
    def uniformRandom(self):
        legal_moves = self.game.legalMoves()
        selected_move = random.choice(legal_moves)
        return selected_move
    
    #Algo2
    def dLMinMax(self, param, verboseType):
        goal = self.game.win
        legal_moves = self.game.legalMoves()

        scores = []
        
        for move in legal_moves:
            new_board = self.game.makeMove(move, self.game.currentPlayer)
            value = self.minmax(new_board, goal, param - 1, float('-inf'), float('+inf'), False)

            if value is not None:
                scores.append(value)
                if verboseType == "Verbose":
                    print("Column {}: {:.2f}".format(int(move) + 1, float(value)))
            else:
                if verboseType == "Verbose":
                    print("Column {}: Null".format(float(move) + 1))

        if scores:
            best_move = legal_moves[scores.index(max(scores))]
            return best_move
        else:
            return None

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

    # Evaluate the desirability of the board state for the current player.
    def evaluate(self, board):
        player = self.game.currentPlayer
        opponent = connectFour.Game.RED if player == connectFour.Game.YELLOW else connectFour.Game.YELLOW

        player_score = self.count_lines(board, player)
        opponent_score = self.count_lines(board, opponent)

        # Simple heuristic: difference between player's and opponent's line counts
        heuristic_value = player_score - opponent_score

        return heuristic_value / 10.0  # Scale the value between -1 and 1

    # counts the occurences of each color
    def count_lines(self, board, color):
        lines = (
            board,  # columns
            zip(*board),  # rows
            connectFour.diagonalsPos(board, self.game.cols, self.game.rows),  # positive diagonals
            connectFour.diagonalsNeg(board, self.game.cols, self.game.rows)  # negative diagonals
        )

        color_count = 0
        for line in chain(*lines):
            color_count += line.count(color)

        return color_count
    
    #Algo 3
    def monteCarloGS(self, param, verboseType):
        legal_moves = self.game.legalMoves()

        if not legal_moves:
            return None

        scores = []
        total_simulations = 0

        for move in legal_moves:
            simulations = 0
            wins = 0

            for _ in range(param):
                new_board, game_ended = self.game.makeMove(move, self.game.currentPlayer)

                # Check if the game has ended
                if game_ended:
                    break

                result = self.rolloutRandom()
                simulations += 1

                if result == 1:
                    wins += 1

            if verboseType == "Verbose":
                print("wi:{} ".format(wins))
                print("ni: {}".format(simulations))
                print("Move selected: {}".format(move))

            # Avoid division by zero
            score = wins / simulations if simulations > 0 else 0
            scores.append(score)
            total_simulations += simulations

            # Check if the game has ended
            if game_ended:
                break

        if verboseType == "Verbose":
            for i, move in enumerate(legal_moves):
                print("Column " + str(move + 1) + ": " + str(scores[i]))

        if total_simulations == 0:
            return None

        best_move = legal_moves[scores.index(max(scores))]

        return best_move

    def rolloutRandom(self):
        # Create a copy of the game object to avoid modifying the original state
        game_copy = self.game.copy()

        while True:
            legal_moves = game_copy.legalMoves()

            if not legal_moves:
                return 0  # Draw

            move = random.choice(legal_moves)
            game_copy.makeMove(move, game_copy.currentPlayer)

            if game_copy.isWinner(game_copy.currentPlayer):
                return 1  # Win
            elif game_copy.isFull():
                return 0  # Draw

            # Update the player after making a move
            game_copy.currentPlayer = (
                game_copy.RED if game_copy.currentPlayer == game_copy.YELLOW else game_copy.YELLOW
            )

    # Algo 4
    def upperConfidenceBound(self, param, verboseType):
        pass
       