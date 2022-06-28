import typing

class BacktrackingSudoku:
    """

    A class used to represent a Sudoku Board with simple backtracking implementation
    
    ...
    
    Attributes
        bo : list
            2D array which holds current state of Sudoku board 
        solveCount : int
            Counts how many time solve is called

    ...

    Methods
        solveBoard(self) -> bool
            Solves instantiated board through simple backtracking 
        findEmpty(self) -> typing.Tuple[int, int]
            Finds first empty cell to test
        validPosition(self, num : int, row : int, col : int) -> bool
            Checks if num can go into the given cell (row, col)
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

    def solveBoard(self) -> bool:
        ''' 
        Solves instantiated board through simple backtracking 
        
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

        if not emptyCell: return True
        row, col = emptyCell

        for n in range(1, 10):
            if self.validPosition(n, row, col):
                self.bo[row][col] = n

                if self.solveBoard(): return True

                self.bo[row][col] = 0
        
        return False

    def findEmpty(self) -> typing.Tuple[int, int]:
        '''
        Finds first empty cell to test
        
        ...
        
        Returns
            Tuple[row, col]     If empty cell found
            None                Otherwise
        '''
        for r in range(9):
            for c in range(9):
                if self.bo[r][c] == 0: 
                    return (r, c)
        
        return None
    
    def validPosition(self, num : int, row : int, col : int) -> bool:
        ''' 
        Checks if num can go into the given cell (row, col)

        ...

        Implementation Note(s)
            Boxes are numbered where each number is a 3x3 grid
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8

        ...

        Parameters
            num : int
                Number to be tested in given cell
            row : int
            col : int

        ...

        Returns
        -------
            True    num can go into position
            False   num can NOT go into position
        '''
        # row check
        for c in range(9):
            if c != col and self.bo[row][c] == num: 
                return False

        # col check
        for r in range(9):
            if r != row and self.bo[r][col] == num: 
                return False

        # box check
        boxRow, boxCol = row // 3, col // 3
        for r in range(boxRow * 3, boxRow * 3 + 3):
            for c in range(boxCol * 3, boxCol * 3 + 3):
                if r != row and c != col and self.bo[r][c] == num: 
                    return False
        
        return True

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
