from values import Inserted
from BoardExtractor import readImg, extractCells
import copy, random

# declaration of constants
POSS_VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
EMPTY_BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] ]


class Board:
    insertList = Inserted()

    # Creates an empty board
    def __init__(self):
        self.bo = copy.deepcopy(EMPTY_BOARD)
        """
        num_fill = random.randint(16, 50)       # spaces on board to fill
        count = 0                               # counts the times num was randomized

        for i in num_fill:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)

            while not insertList.insert(num, row, col):
                num = random.randint(1, 9)
        """

    def __init__(self, image_url):
        boardImg = readImg('board2.png')
        preprocessed = preprocessImg(boardImg)
        cropAndWarp(preprocessed)
    
    # Prints board
    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.bo[i][j])
                else:
                    print(str(self.bo[i][j]) + " ", end="")
"""
    # Randomly fills the board
    def create_board(self):
        for i in range(0, 50):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)

            while self.bo[row][col] != 0:
                col = random.randint(0, 8)
                row = random.randint(0, 8)
            
            while not valid_pos(self, num, (row, col)):
                num = (num + 1) % 9 + 1
"""         





