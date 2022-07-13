# **Sudoku-Solver-Generator**

Sudoku-Solver-Generator is comprised of three individual parts:

1. Analyze the difference between Sudoku solving algorithms in terms of runtime and solve call efficiency. The first is a simple backtracking algorithm. The second expands on backtracking with the use of mental [heuristics](https://sandiway.arizona.edu/sudoku/index.html).
2. Implement computer vision which accepts pictures of Sudoku boards and, through the use of TensorFlow and Keras, deciphers/solves the given board with number inputted back on original board.
3. Generate, store, and rank Sudoku boards using backtracking and techniques mentioned by [Daniel Beer](https://dlbeer.co.nz/articles/sudoku.html).

# **Running the Project**
```bash
make run
```

# **Table of Contents**
1. [To Do](#to-do)
2. [Heuristics Implemented](#heuristics-implemented)
3. [Sudoku Boards](#sudoku-boards-used)
4. [Algorithm Structure/Overview](#algorithm-structureoverview)
5. [Heuristic Implementations](#heuristic-implementation)
6. [Sources/References](#sources)

- - - -

## **To Do**
- [x] Restructure project
- [x] Simple backtracking
- [x] Upload example boards
- [x] Create Makefile
- [x] Create test file
- [ ] Backtracking with heuristics
    - [x] Simple area inconsistency
    - [x] Area insufficiency
    - [ ] Area set cover elimination
    - [ ] Unique number area
    - [ ] Unique number mention
- [ ] Board generation
- [ ] Computer vision implementation

## **Heuristics Implemented**
1. <u>Area inconsistency and insufficiency</u>: Two cells cannot share the same value, and each cell must have a valid value to set
    - <u>Extension by factoring two uniqueness heuristics</u>: Utilizes a chain of reasoning to select a cell value
2. <u>Area set cover elimination</u>: A subset of cells may share a subset of possible values which can't be found outside of the given cell subset
3. <u>Unique row/column combination</u>: A cell must hold a certain value because it already exists in every other row & column
4. <u>Unique mention in area</u>: A value has only one cell mention in a given row, column, or 3x3 box, meaning that it must be placed in that cell

## **Sudoku Boards and Heuristic Utilization**
Boards and rankings are obtained from [Sudoku Sandiway](https://sandiway.arizona.edu/sudoku/examples.html).

|   Board Number    |   Ranking         |   Heuristics Needed
|   :---:           |   :---:           |   :--:
|   1               |   Beginner        |   1
|   2               |   Beginner        |   1
|   3               |   Intermediate    |   1 & 2
|   4               |   Difficult       |   1 & 4
|   5               |   Difficult       |   Extended 1, with chaining requiring no more than 2 pivots
|   6               |   Extreme         |   Extended 1, with chaining requiring 2+ pivots

## **Algorithm Structure/Overview**
Both algorithms utilize similar algorithm structures in order to solve each Sudoku board. 
1. An empty cell in the board is selected.
2. Digits, 1-9, are placed in the selected cell.
3. Each digit is checked for validity, and placed if valid. 
4. The board is then filled recursively until a complete board, or until a cell has no valid digits.
We will consider each recursive call to the solve method as an iteration. 

For simple backtracking, an empty cell is selected (step 1) by iterating through each cell until an empty one is found. Each digit from 1-9 is checked to be valid in the given cell, and if the digit is valid it is placed (step 2). These two steps choose cells and select digits arbitrarily and can lead to very long runtimes if unlucky.

For backtracking using heuristics we will be implementing logical tricks used by humans to help reduce possible cell values (described in the [Heuristics](#heuristics-implemented) section). The overall structure of the program does not change. We first select an empty cell (step 1), but now we select the cell with the minimum amount of remaining values maintained by the ```numCount``` structure. Each possible cell value, maintained by the ```remVals``` structure, is placed and tested (step 2). Throughout the code we implement the different heuristics, which we will now go over. 

## **Heuristic Implementation**

The easiest of the heuristics to implement was number 1. To avoid inconsistency errors, the ```remVals``` structure was used to hold each cells' possible, remaining values. Every time a cell is set, every cell in the same row, column, and 3x3 box were updated accordingly in the structure. To avoid insufficiency errors, the ```numCount``` structure was used to hold the number of possible values a cell may have. If a cell has no possible values remaining it's count would be set to 0. An easy check is implemented to avoid this. It's extension requiring chaining is naturally implemented through backtracking. 



## **Sources**
- [Simple backtracking algorithm](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) - TechWithTim
- [Sudoku with heuristics](https://sandiway.arizona.edu/sudoku/examples.html) - Sandiway
    * Computer Vision Pt 1:     https://becominghuman.ai/image-processing-sudokuai-opencv-45380715a629
    * Computer Vision Pt 2:     https://becominghuman.ai/sudoku-and-cell-extraction-sudokuai-opencv-38b603066066
    * Computer Vision Pt 3:     https://becominghuman.ai/part-3-solving-the-sudoku-ai-solver-13f64a090922
    * Image blurring:           https://datacarpentry.org/image-processing/06-blurring/
    * Thresholding:             https://www.quora.com/Why-is-thresholding-used-in-image-processing
    * More Computer Vision:     https://towardsdatascience.com/computer-vision-for-beginners-part-2-29b3f9151874
