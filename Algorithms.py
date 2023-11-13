import main
import connectFour
import random

class Algorithms:
    def __init__(self, connectFour):
        self.connectFour = connectFour

    def select_move(self):
        pass   
    
#Algo1
def uniformRandom(algo, param):
    legalMoves = [col for col in range(connectFour.Game.cols) if connectFour.Game.board[col][0]=="O"]
    selectedMoves = random.choice(legalMoves)
    print("Players selected moves: ", selectedMoves)
    return 

#Algo2
def dLMinMax(algo, param):
    currpos=0
    goal =4
    minmax(currpos, goal, param, float('-inf'), float('+inf'), True)
    return

def minmax(pos, goal, depth, alpha, beta, maxPlayer):
    if depth == 0 or pos == goal:
        return pos
    
    if maxPlayer:
        maxEval = float('-inf')
        for child in pos:
            eval=minmax(child,goal,depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return maxEval
    else:
        minEval =float('+inf')
        for child in pos:
            eval=minmax(child,goal,depth-1,alpha,beta,True)
            minEval = min(minEval, eval)
            beta= min(beta, eval)
            if beta<=alpha:
                break
        return minEval 
    
        
#Algo3
def monteCarloGS(algo, param):
    return

#Algo4
def upperConfidenceBound(algo, param):
    return
