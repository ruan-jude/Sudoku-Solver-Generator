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
2. [Algorithm Analysis](#algorithm-analysis)
3. [Sources/References](#sources)

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

## **Algorithm Analysis**
For 

For backtracking using heuristics we will be implementing logical tricks used by humans to help reduce possible cell values. The heuristics are as follows:

1. Area inconsistency and insufficiency: Two cells cannot share the same value, and each cell must have a valid value to set

## **Sources**
- [Simple backtracking algorithm](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) - TechWithTim
    * Computer Vision Pt 1:     https://becominghuman.ai/image-processing-sudokuai-opencv-45380715a629
    * Computer Vision Pt 2:     https://becominghuman.ai/sudoku-and-cell-extraction-sudokuai-opencv-38b603066066
    * Computer Vision Pt 3:     https://becominghuman.ai/part-3-solving-the-sudoku-ai-solver-13f64a090922
    * Image blurring:           https://datacarpentry.org/image-processing/06-blurring/
    * Thresholding:             https://www.quora.com/Why-is-thresholding-used-in-image-processing
    * More Computer Vision:     https://towardsdatascience.com/computer-vision-for-beginners-part-2-29b3f9151874
