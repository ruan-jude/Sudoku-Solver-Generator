# **Sudoku-Solver-Generator**

Sudoku-Solver-Generator is a three part project:

1. Analyze the difference between Sudoku solving algorithms in terms of runtime and solve call efficiency. The first is a simple backtracking algorithm. The second expands on backtracking with the use of mental [heuristics](https://sandiway.arizona.edu/sudoku/index.html).
2. Generate, store, and rank Sudoku boards using backtracking and techniques mentioned by [Daniel Beer](https://dlbeer.co.nz/articles/sudoku.html).
3. Implement computer vision which accepts pictures of Sudoku boards and, through the use of TensorFlow and Keras, deciphers/solves the given board with number inputted back on original board.

# **Running the Project**
```bash
make run
```

# **Table of Contents**
1. [To Do](#to-do)
2. [Heuristics Implemented](#heuristics-implemented)
3. [Sudoku Boards](#sudoku-boards-used)
4. [Algorithm Analysis](#algorithm-analysis)
5. [Sources/References](#sources)

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
1. Area inconsistency and insufficiency: Two cells cannot share the same value, and each cell must have a valid value to set
    - Extension, factoring two uniqueness heuristics: 
2. Area set cover elimination
3. Unique row/column elimination
4. Unique mention in area

## **Sudoku Boards and Heuristic Utilization**
Boards and rankings are obtained from [Sudoku Sandiway](https://sandiway.arizona.edu/sudoku/examples.html).
- Board 1
    - Beginner
    - Only Heuristic 1
- Board 2
    - Beginner
    - Only Heuristic 1
- Board 3
    - Intermediate
    - Heuristic 1 & 2
- Board 4
    - Difficult
    - Extended Heuristic 1 & 4
- Board 5
    - Difficult
    - Extended Heuristic 1
- Board 6
    - Extreme Difficulty
    - ...


## **Algorithm Analysis**
Both algorithms utilize similar algorithm structures in order to solve each Sudoku board. 
1. An empty cell in the board is selected.
2. Digits, 1-9, are placed in the selected cell.
3. Each digit is checked for validity, and placed if valid. 
4. The board is then filled recursively until a complete board, or until a cell has no valid digits.
We will consider each recursive call to the solve method as an iteration. 

For simple backtracking, an empty cell is selected (step 1) by iterating through each cell until an empty one is found. Each digit from 1-9 is checked to be valid in the given cell, and if the digit is valid it is placed (step 2). These two steps choose cells and select digits arbitrarily and can lead to very long runtimes if unlucky.

For backtracking using heuristics we will be implementing logical tricks used by humans to help reduce possible cell values. The heurstics used can be found in the [Heuristics](#heuristics-implemented) section. 



## **Sources**
- [Simple backtracking algorithm](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) - TechWithTim
    * Computer Vision Pt 1:     https://becominghuman.ai/image-processing-sudokuai-opencv-45380715a629
    * Computer Vision Pt 2:     https://becominghuman.ai/sudoku-and-cell-extraction-sudokuai-opencv-38b603066066
    * Computer Vision Pt 3:     https://becominghuman.ai/part-3-solving-the-sudoku-ai-solver-13f64a090922
    * Image blurring:           https://datacarpentry.org/image-processing/06-blurring/
    * Thresholding:             https://www.quora.com/Why-is-thresholding-used-in-image-processing
    * More Computer Vision:     https://towardsdatascience.com/computer-vision-for-beginners-part-2-29b3f9151874
