import sys
import connectFour
         
def readBoard(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        
    algorithm = lines[0]
    param = lines[1]
    player = lines[2]
    board = [list(row) for row in lines[3:]]

    return algorithm, param, player, board

class Algorithms:
    def __init__(self, connectFour):
        self.connectFour = connectFour

    def select_move(self):
        pass   
    
#Algo1
def uniformRandom(algo, param):
    return

#Algo2
def dLMinMax(algo, param):
    
    return
def minmax(pos, goal, depth, maxPlayer):
    if depth == 0 or pos == goal:
        return pos
    
    if maxPlayer:
        maxEval = float('-inf')
        for child in pos:
            eval=minmax(child,goal,depth-1,False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval =float('+inf')
        for child in pos:
            eval=minmax(child,goal,depth-1,True)
            minEval = min(minEval, eval)
        return minEval 
    
        
#Algo3
def monteCarloGS(algo, param):
    return

#Algo4
def upperConfidenceBound(algo, param):
    return


def main():
    if len(sys.argv) != 3:
        print("only two arguements allowed")
        sys.exit()
        
    filename = sys.argv[1]
    verboseType = sys.argv[2]
    
    algorithm, param, player, *board = readBoard(filename)
    
    #call connectFour class with board state
    gamePlay = connectFour.ConnectFour(board)
    
    #call methods according to the algorithm type
    if algorithm == "UR":
        output = uniformRandom(algorithm, param)
    elif algorithm == "DLMM":
        output = dLMinMax(gamePlay, int(param))
    elif algorithm == "PMCGS":
        output = monteCarloGS(algorithm, param)
    elif algorithm == "UCT":
        output = upperConfidenceBound(algorithm, param)
        
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
        
    
        