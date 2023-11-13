import sys
import connectFour
import Algorithms
import random
         
def readBoard(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()  
    algorithm = lines[0]
    param = lines[1]
    player = lines[2]
    board = [list(row) for row in lines[3:]]

    return algorithm, param, player, board

def main():
    if len(sys.argv) != 3:
        print("only two arguements allowed")
        sys.exit()
        
    filename = sys.argv[1]
    verboseType = sys.argv[2]
    
    algorithm, param, player, board = readBoard(filename)
    
    #call connectFour class with board state
    gamePlay = connectFour.Game(board)
    
    #call methods according to the algorithm type
    if algorithm == "UR":
        output = Algorithms.uniformRandom(algorithm, param)
    elif algorithm == "DLMM":
        output = Algorithms.dLMinMax(gamePlay, int(param))
    elif algorithm == "PMCGS":
        output = Algorithms.monteCarloGS(algorithm, param)
    elif algorithm == "UCT":
        output = Algorithms.upperConfidenceBound(algorithm, param)
        
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
        
    
        