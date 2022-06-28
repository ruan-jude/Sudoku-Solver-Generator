import sys, os, glob, time, typing, copy
sys.path.append(".")
from src.BacktrackingSudoku import BacktrackingSudoku
from src.HeuristicSudoku import HeuristicSudoku

def openBoard(path : str) -> typing.Tuple[list, list]:
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

if __name__ == "__main__":
    os.chdir("./tests/sampleBoards") 
    print("Simple vs heuristic backtracking")
    print("---------------------------------")
    # Tests heuristic and simple backtracking method 
    # Printing solve count and time elapsed
    for file in glob.glob("*.txt"): 
        bo1, sol = openBoard(file)
        bo2 = copy.deepcopy(bo1)

        simpBo = BacktrackingSudoku(bo1)
        start = time.time()
        simpBo.solveBoard()
        simpTime = (time.time() - start) * 1000
        
        heurBo = HeuristicSudoku(bo2)
        start = time.time()
        heurBo.solveBoard()
        heurTime = (time.time() - start) * 1000
        
        print(file)
        if simpBo.getBoard() == sol and heurBo.getBoard() == sol:
            print("  Solve calls:\t\t%d\t\t%d" % (simpBo.solveCount, heurBo.solveCount))
            print("  Time elapsed (ms):\t%.2f\t\t%.2f" % (simpTime, heurTime))
            print()
        elif simpBo.getBoard() != sol: print("Simple backtracking solution incorrect.")
        else: print("Heuristic backtracking solution incorrect.")
