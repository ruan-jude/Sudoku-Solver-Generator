from cmath import inf
import numpy as np
import typing

class HeuristicSudoku:
    """

    A class used to represent a Sudoku Board with backtracking implementation
    Heuristics used to reduce runtime (testing)

    ---
    
    Attributes
        bo : list
            2D array which holds current state of Sudoku board 
        solveCount : int
            Counts how many time solve is called
        numSetCount : dictionary
            Counts the number of times a value is placed in board
        cellRemVals : list
            2D array where each cell holds a set of possible values for that cell
        cellRemCount : list
            2D array which holds the count for remaining values for each board cell
            Value set to 'inf' if the number is set
        

    ---

    Methods
        returnRemVals(self, updatedCells : set, num : int) -> None
            Returns the num to each cell listed in updatedCells
        findEmpty(self) -> typing.Tuple[int, int]
            Finds empty cell to test, will prioritize lowest value
        printBoard(self) -> None
            Prints the current state of the board with proper spacing
        printSolveCount(self) -> None
            Prints the number of times Solve is called 
        getBoard(self) -> list
            Returns board

    """
    
    def __init__(self, board : list):
        '''
        Each instance represents a single Sudoku board
        Sets board to example board
        '''
        self.bo = board
        self.solveCount = 0
        self.numSetCount = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        self.cellRemVals = [[set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for __ in range(9)] for _ in range(9)]
        self.cellRemCount = [[9]*9 for _ in range(9)]

        # sets cellRemCount for all set cells to 'inf'
        # initializes remVals, numCount, and valueSetCount
        for r in range(9):
            for c in range(9):
                n = self.bo[r][c]
                if n != 0:
                    self.cellRemCount[r][c] = inf
                    self.numSetCount[n] += 1
                    self.updateRemVals(n, r, c)
                    
    
    def solveBoard(self) -> bool:
        ''' 
        Solves instantiated board through backtracking with heuristics
        '''
        self.solveCount += 1
        emptyCell = self.findEmpty()

        # if there is a cell with insufficient remaining values
        if emptyCell == False: return False
        # if there are no empty cells, board must be complete
        if emptyCell == None: return True
        # otherwise, set row and col
        row, col = emptyCell
        
        for n in self.cellRemVals[row][col]:
            # update Board
            self.bo[row][col] = n
            # save/update cellRemCount[row][col]
            prevRemCount = self.cellRemCount[row][col]
            self.cellRemCount[row][col] = inf
            # update numSetCount
            self.numSetCount[n] += 1
            # update cellRemVals
            updatedCells = self.updateRemVals(n, row, col)

            if self.solveBoard(): return True

            # reset Board
            self.bo[row][col] = 0
            # reset cellRemCount[row][col]
            self.cellRemCount[row][col] = prevRemCount
            # reset numSetCount
            self.numSetCount[n] -= 1
            # reset cellRemVals that were changed
            self.returnRemVals(updatedCells, n)
        
        return False

    def updateRemVals(self, num : int, row : int, col : int) -> set:
        ''' 
        Updates remaining values for all cells in row, col, and box

        ---

        Returns
            updatedCells    set of cells that were updated with the values
        '''
        updatedCells = set()

        # row update
        for c in range(9):
            if c != col and num in self.cellRemVals[row][c]:
                updatedCells.add((row, c))
                self.cellRemCount[row][c] -= 1
                self.cellRemVals[row][c].discard(num)

        # col update
        for r in range(9):
            if r != row and num in self.cellRemVals[r][col]:
                updatedCells.add((r, col))
                self.cellRemCount[r][col] -= 1
                self.cellRemVals[r][col].discard(num)
        
        # box update
        boxRow, boxCol = row // 3, col // 3
        for r in range(boxRow * 3, boxRow * 3 + 3):
            for c in range(boxCol * 3, boxCol * 3 + 3):
                if (r, c) != (row, col) and num in self.cellRemVals[r][c]:
                    updatedCells.add((r, c))
                    self.cellRemCount[r][c] -= 1
                    self.cellRemVals[r][c].discard(num)

        return updatedCells

    def returnRemVals(self, updatedCells : set, num : int) -> None:
        '''
        Returns the num to each cell listed in updatedCells
        Updates numCount as well

        ---

        Parameters
            updatedCells
                set containing all cells to return num into
        ''' 
        for cell in updatedCells:
            row, col = cell
            self.cellRemVals[row][col].add(num)
            self.cellRemCount[row][col] += 1

    def findEmpty(self) -> typing.Tuple[int, int]:
        '''
        Finds empty cell to test, prioritizing lowest value
        '''
        
        # check to find if a value has only one remaining position
        #res = dict((val, key) for key, val in self.valueSetCount.items()).get(1)
        #if res != None: 
        # finds the index with the smallest remaining value count
        arr = np.array(self.cellRemCount)
        smallestInd = np.unravel_index(arr.argmin(), arr.shape)

        if self.cellRemCount[smallestInd[0]][smallestInd[1]] == 0: return False
        if self.cellRemCount[smallestInd[0]][smallestInd[1]] == inf: return None

        smallestInd = (smallestInd[0], smallestInd[1])

        return smallestInd
        '''

        arr = np.array(self.numCount)
        smallestInd = np.unravel_index(arr.argmin(), arr.shape)

        if self.numCount[smallestInd[0]][smallestInd[1]] == 0: return False
        if self.numCount[smallestInd[0]][smallestInd[1]] == inf: return None

        smallestInd = (smallestInd[0], smallestInd[1], -1)

        return smallestInd
        '''

    def printBoard(self) -> None:
        ''' Prints the current state of the board with proper spacing '''
        for r in range(9):
            if r % 3 == 0 and r != 0: print("- - - - - - - - - - - - ")

            for c in range(9):
                if c % 3 == 0 and c != 0: print(" | ", end="")

                if c == 8: print(self.bo[r][c])
                else: print(str(self.bo[r][c]) + " ", end="")
        
        print()

    def getSolveCount(self) -> None:
        ''' Prints the number of times Solve is called '''
        return self.solveCount 

    def getBoard(self) -> list:
        ''' Returns board list ''' 
        return self.bo  