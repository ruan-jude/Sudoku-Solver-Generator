from src.HeuristicSudoku import HeuristicSudoku
from src.BacktrackingSudoku import BacktrackingSudoku
import time

def main():
    board = HeuristicSudoku()
    #start = time.time()
    #board = BacktrackingSudoku()
    #print(time.time() - start)
    board.printBoard()
    board.solveBoard()
    board.printBoard()

if __name__ == "__main__":
    main()