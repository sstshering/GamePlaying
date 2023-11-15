import sys
import connectFour
from Algorithms import Algorithms

def main():
    if len(sys.argv) != 3:
        print("Only two arguments allowed")
        sys.exit()

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

if __name__ == "__main__":
    main()
