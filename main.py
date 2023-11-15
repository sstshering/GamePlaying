import sys
import connectFour
from Algorithms import Algorithms

def main():
    if len(sys.argv) == 3 and sys.argv[1]!="tournament":
        filename = sys.argv[1]
        verboseType = sys.argv[2]

        algorithm, param, player, board = connectFour.readBoard(filename)

        # Call connectFour class with the board state
        gamePlay = connectFour.Game(board, player, cols=len(board), rows=len(board[0]), requiredToWin=4)

        # create an instance of the game
        Algorithms_inst = Algorithms(gamePlay)

        # call methods according to the algorithm type
        try:
            if algorithm == "UR":
                output = Algorithms_inst.uniformRandom()
            elif algorithm == "DLMM":
                output = Algorithms_inst.dLMinMax(int(param), verboseType)
            elif algorithm == "PMCGS" or algorithm == "UCT":
                output = Algorithms_inst.MCGSUCT(int(param), verboseType, algorithm)
            else:
                print("Invalid algorithm:", algorithm)
                sys.exit(1)

            # Verbosity type = controls what your algorithm will print for output
            if verboseType != "None":
                print("FINAL Move selected:", output)
            elif verboseType == "None":  # Nothing
                pass
            else:
                print("Invalid output mode.")
                sys.exit(1)

        except Exception as e:
            print("An exception occurred: {}".format(e))

    elif len(sys.argv) == 3 and sys.argv[1] == "tournament":
        filename = sys.argv[2]
        run_tournament(filename)

    else:
        print("Invalid number of arguments")
        sys.exit(1)

def run_tournament(filename):
    algorithms = [
        ("UR", None),
        ("DLMM", 5),
        ("PMCGS", 500),
        ("PMCGS", 10000),
        ("UCT", 500),
        ("UCT", 10000)
    ]

    total_games = len(algorithms) * (len(algorithms) - 1)  # Number of games in the tournament

    results = {algo: 0 for algo, _ in algorithms}

    for i in range(len(algorithms)):
        for j in range(i + 1, len(algorithms)):
            algo1, param1 = algorithms[i]
            algo2, param2 = algorithms[j]

            # Run 100 games between the two algorithms
            for _ in range(100):
                winner = play_game(algo1, param1, algo2, param2, filename)

                if winner == algo1:
                    results[algo1] += 1
                elif winner == algo2:
                    results[algo2] += 1

    print_results(results, total_games)

def play_game(algo1, param1, algo2, param2, filename):
    game_play = connectFour.Game(*connectFour.readBoard(filename))
    algo_inst1 = Algorithms(game_play)
    algo_inst2 = Algorithms(game_play)

    while not game_play.isFull():
        move1 = get_next_move(algo_inst1, algo1, param1)
        game_play.makeMove(move1, game_play.currentPlayer)

        if game_play.isWinner(game_play.currentPlayer):
            return algo1

        move2 = get_next_move(algo_inst2, algo2, param2)
        game_play.makeMove(move2, game_play.currentPlayer)

        if game_play.isWinner(game_play.currentPlayer):
            return algo2

    return "Draw"

def get_next_move(algo_instance, algo_type, param):
    if algo_type == "UR":
        return algo_instance.uniformRandom()
    elif algo_type == "DLMM":
        return algo_instance.dLMinMax(param, "None")
    elif algo_type == "PMCGS" or algo_type == "UCT":
        return algo_instance.MCGSUCT(param, "None", algo_type)

def print_results(results, total_games):
    print("\nResults of the Tournament:")
    print("{:<10} {:<10} {:<10}".format("Algorithm", "Wins", "Winning %"))
    for algo, wins in results.items():
        winning_percentage = (wins / total_games) * 100
        print("{:<10} {:<10} {:.2f}%".format(algo, wins, winning_percentage))

if __name__ == "__main__":
    main()
