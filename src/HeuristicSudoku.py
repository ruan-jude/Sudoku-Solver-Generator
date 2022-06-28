from cmath import inf
import numpy as np
import typing

class HeuristicSudoku:
    """

    A class used to represent a Sudoku Board with backtracking implementation
    Heuristics used to reduce runtime (testing)

    ...
    
    Attributes
        bo : list
            2D array which holds current state of Sudoku board 
        remVals : list
            2D array where each cell holds a set of possible values for that cell
        numCount : list
            2D array which holds the count for remaining values for each board cell
            Value set to 'inf' if the number is set
        valueCount : dictionary
            Holds the count for each possible Sudoku board value
            Equals 0 when the cell is set
        solveCount : int
            Counts how many time solve is called

    ...

    Methods
        solveBoard(self) -> bool
            Solves instantiated board through backtracking with heuristics
        updateRemVals(self, num : int, row : int, col : int) -> set
            Updates remaining values for all cells in row, col, and box
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
        self.remVals = [[set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for __ in range(9)] for _ in range(9)]
        self.numCount = [[9]*9 for _ in range(9)]
        self.valueCount = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        self.solveCount = 0

        # sets numCount for all set cells to 'inf'
        for r in range(9):
            for c in range(9):
                if self.bo[r][c] != 0:
                    self.numCount[r][c] = inf
        
        # initial remVals, numCount, and valueCount
        for r in range(9):
            for c in range(9):
                n = self.bo[r][c]
                if n != 0:
                    self.valueCount[n] += 1
                    self.updateRemVals(n, r, c)
    
    def solveBoard(self):
        ''' 
        Solves instantiated board through backtracking with heuristics 
        
        ...

        Implementation Note(s)
            If there are no empty cells, board must necessarily be complete
        
        ...

        Returns
            True    Board solution is found and bo is updated
            False   Board solution is NOT found
        '''
        self.solveCount += 1
        emptyCell = self.findEmpty()

        # if there are no empty cells, board must be complete
        if not emptyCell: return True
        # otherwise, set row and col
        row, col = emptyCell

        for n in self.remVals[row][col]:
            # update Board
            self.bo[row][col] = n
            # save and update numCount
            prevNumCount = self.numCount[row][col]
            self.numCount[row][col] = inf
            # update valueCount
            self.valueCount[n] += 1
            # update remVals
            updatedCells = self.updateRemVals(n, row, col)

            if self.solveBoard(): return True

            # reset Board
            self.bo[row][col] = 0
            # reset numCount
            self.numCount[row][col] = prevNumCount
            # reset valueCount
            self.valueCount[n] -= 1
            # reset remVals that were changed
            self.returnRemVals(updatedCells, n)
        
        return False

    def updateRemVals(self, num : int, row : int, col : int) -> set:
        ''' 
        Updates remaining values for all cells in row, col, and box

        ...

        Implementation Note(s)
            Boxes are numbered where each number is a 3x3 grid
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8

        ...

        Parameters
            num : int
                Number to be removed from each relevant cell
            row : int
            col : int

        ...

        Returns
            updatedCells    set of cells that were updated with the values
        '''
        updatedCells = set()

        # row update
        for c in range(9):
            if c != col and num in self.remVals[row][c]:
                updatedCells.add((row, c))
                self.numCount[row][c] -= 1
                self.remVals[row][c].discard(num)

        # col update
        for r in range(9):
            if r != row and (r, col) not in updatedCells and num in self.remVals[r][col]:
                updatedCells.add((r, col))
                self.numCount[r][col] -= 1
                self.remVals[r][col].discard(num)
        
        # box update
        boxRow, boxCol = row // 3, col // 3
        for r in range(boxRow * 3, boxRow * 3 + 3):
            for c in range(boxCol * 3, boxCol * 3 + 3):
                if (r, c) != (row, col) and (r, c) not in updatedCells and num in self.remVals[r][c]:
                    updatedCells.add((r, c))
                    self.numCount[r][c] -= 1
                    self.remVals[r][c].discard(num)

        return updatedCells

    def returnRemVals(self, updatedCells : set, num : int) -> None:
        '''
        Returns the num to each cell listed in updatedCells
        Updates numCount as well

        ...

        Parameters
            updatedCells
                set containing all cells to return num into
            num
        ''' 
        for cell in updatedCells:
            row, col = cell
            self.remVals[row][col].add(num)
            self.numCount[row][col] += 1

    def findEmpty(self) -> typing.Tuple[int, int]:
        '''
        Finds empty cell to test, will prioritize lowest value
        
        ...
        
        Returns
            Tuple[row, col]     If empty cell found
            None                Otherwise
        '''
        arr = np.array(self.numCount)
        smallestInd = np.unravel_index(arr.argmin(), arr.shape)

        if self.numCount[smallestInd[0]][smallestInd[1]] == inf: return None

        return smallestInd

    def printBoard(self) -> None:
        ''' Prints the current state of the board with proper spacing '''
        for r in range(9):
            if r % 3 == 0 and r != 0: print("- - - - - - - - - - - - ")

            for c in range(9):
                if c % 3 == 0 and c != 0: print(" | ", end="")

                if c == 8: print(self.bo[r][c])
                else: print(str(self.bo[r][c]) + " ", end="")
        
        print()

    def printSolveCount(self) -> None:
        ''' Prints the number of times Solve is called '''
        return self.solveCount 

    def getBoard(self) -> list:
        ''' Returns board list ''' 
        return self.bo  