import sys, os, glob, time
sys.path.append(".")
from typing import Tuple
from src.BacktrackingSudoku import BacktrackingSudoku
from src.HeuristicSudoku import HeuristicSudoku

def openBoard(path : str) -> Tuple:
    '''
    Retrieves the board written in the path file

    ...

    Returns
        bo      Original board
        sol     Board solution
    '''
    f = open(path, "r")

    # reads and stores unsolved board
    bo = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        line = f.readline()
        for j in range(9):
            bo[i][j] = int(line[j])

    f.readline()

    # reads and stores solution board
    sol = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        line = f.readline()
        for j in range(9):
            sol[i][j] = int(line[j])
    
    return (bo, sol)

def backtrackingTest() -> None:
    ''' Tests backtracking method printing solve count and time elapsed '''
    print("Backtracking Tests")
    print("------------------")
    for file in glob.glob("*.txt"): 
        bo, sol = openBoard(file)
        board = BacktrackingSudoku(bo)
        start = time.time()
        board.solveBoard()
        end = time.time()

        if board.getBoard() == sol:
            print(file)
            print("  Solve calls: %d" % board.solveCount)
            print("  Time elapsed: %f milliseconds" % ((end - start) * 1000))
            print()
        else: 
            print("Board solution incorrect.")

def heuristicTest():
    ''' Tests heuristic method printing solve count and time elapsed '''
    print("Heuristic Tests")
    print("------------------")
    for file in glob.glob("*.txt"): 
        bo, sol = openBoard(file)
        board = HeuristicSudoku(bo)
        start = time.time()
        board.solveBoard()
        end = time.time()

        if board.getBoard() == sol:
            print(file)
            print("  Solve calls: %d" % board.solveCount)
            print("  Time elapsed: %f milliseconds" % ((end - start) * 1000))
            print()
        else: 
            print("Board solution incorrect.")

if __name__ == "__main__":
    os.chdir("./tests/sampleBoards") 
    backtrackingTest()
    print("****************\n")
    #heuristicTest()
