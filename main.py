import sys
import connectFour
from Algorithms import Algorithms
import random

def main():
    if len(sys.argv) != 3:
        print("only two arguements allowed")
        sys.exit()
        
    filename = sys.argv[1]
    verboseType = sys.argv[2]
    
    algorithm, param, player, board = connectFour.readBoard(filename)
    
    #call connectFour class with board state
    gamePlay = connectFour.Game(board,player)
    
    Algorithms_inst = Algorithms(gamePlay)
    print(algorithm)
    # output = output.uniformRandom()
    # print(output)
    
    #call methods according to the algorithm type
    try:
        if algorithm == "UR":
            print("works")
            output = Algorithms_inst.uniformRandom()
            print(output)
        # elif algorithm == "DLMM":
        #     output = Algorithms.dLMinMax(gamePlay, int(param))
        # elif algorithm == "PMCGS":
        #     output = Algorithms.monteCarloGS(gamePlay, int(param))  # Fix: Pass gamePlay instead of algorithm
        # elif algorithm == "UCT":
        #     output = Algorithms.upperConfidenceBound(gamePlay, int(param))
        else:
            print("Invalid algorithm:", algorithm)
            sys.exit(1)
            
        print("FINAL Move selected:", output)
    except Exception as e:
        print("An exception occurred: {}".format(e))

    # print(Algorithms.uniformRandom(gamePlay))   
    #Verbosity type = controls what your algorithm will print for output
    if verboseType == "Verbose":# Print detailed info
        print("Verbose output")
    elif verboseType == "Brief": # a brief summary 
        print("Brief output")
    elif verboseType == "None": #nothing
         pass
    else:
        print("Invalid output mode.")
        sys.exit(1) 

if __name__ == "__main__":
        main() 
        
    
        