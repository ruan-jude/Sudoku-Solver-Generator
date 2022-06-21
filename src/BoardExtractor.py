import cv2
import numpy as np
from src.NumberExtractor import processData, evaluateModel, predict
# Reads in what board to solve
def readImg(image_url):
    img = cv2.imread(image_url, 0)
    return img


# Extracts snippets of each cell into a numpy array
def extractCellImgs(img):
    # Edits image to reduce noise and crop
    img = processImg(img)
    img = cropAndWarp(img)

    # adaptive thresholding the cropped grid and inverting it
    threshImg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 1)
    grid = cv2.bitwise_not(threshImg)

    # Dimensions of board/cells
    edgeH = np.shape(grid)[0]
    edgeW = np.shape(grid)[1]
    cellEdgeH = edgeH // 9
    cellEdgeW = edgeW // 9

    # iterate through the length and width of the grid, extract the cell images and store them in temporary grid
    tempGrid = []
    for i in range(cellEdgeH, edgeH+1, cellEdgeH):
        for j in range(cellEdgeW, edgeW + 1, cellEdgeW):
            rows = grid[i - cellEdgeH:i]
            tempGrid.append([ rows[k][j-cellEdgeW : j] for k in range(len(rows)) ])

    # creating the 9X9 grid of images and converting to numpy array
    finalGrid = []
    for i in range(0, len(tempGrid) - 8, 9):
        finalGrid.append(tempGrid[i : i+9])

    # Converting all the cell images to np.array
    for i in range(9):
        for j in range(9):
            finalGrid[i][j] = np.array(finalGrid[i][j])
    
    # saves each cell in the current working directory
    try:
        for i in range(9):
            for j in range(9):
                os.remove("BoardCells/cell" + str(i) + str(j) + ".jpg")
    except: pass

    for i in range(9):
        for j in range(9):
            cv2.imwrite(str("BoardCells/cell" + str(i) + str(j) + ".jpg"), finalGrid[i][j])
    
    return finalGrid


def extractCellNums(imgArr):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    trS, trL, teS, teL = processData()
    model = evaluateModel(trS, trL, teS, teL)

    thresh = 128
    
    for i in range(9):
        for j in range(9):
            gray = cv2.threshold(imgArr[i][j], thresh, 255, cv2.THRESH_BINARY)[1]

            # Find contours
            cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)

                if (x < 3 or y < 3 or h < 3 or w < 3):
                    # Note the number is always placed in the center
                    # Since image is 28x28
                    # the number will be in the center thus x >3 and y>3
                    # Additionally any of the external lines of the sudoku will not be thicker than 3
                    continue
                ROI = gray[y:y + h, x:x + w]
                # increasing the size of the number allws for better interpreation,
                # try adjusting the number and you will see the differnce
                # ROI = scale_and_centre(ROI, 120)
            
                board[i][j] = predict(model, ROI)  

    print(board)



# ======================= IMG PROCESSING ======================= 

# Removes noise from original img
def processImg(img):
    # reduce noise from original image
    blurImg = cv2.GaussianBlur(img, (9, 9), 0)

    # separates the image into multiple segments/regions
    # adaptive thresholding: threshold is not a constant scalar, but a distribution applied over a small window of pixels
    threshImg = cv2.adaptiveThreshold(blurImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # inverts the color of the thresholded image
    invertedImg = cv2.bitwise_not(threshImg)

    # dilates the image based on the given convolution kernel
    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
    processedImg = cv2.dilate(invertedImg, kernel)
    
    return processedImg


# Edits image to contain only the board found
def cropAndWarp(img):
    topL, botL, botR, topR = findCorners(img)

    width = calcWidth(topL, botL, botR, topR)
    height = calcHeight(topL, botL, botR, topR)
    dimensions = np.array([[0, 0], [0, height - 1], [width - 1, height - 1], [width - 1, 0]], dtype="float32")

    # convert to Numpy format
    ordered_corners = np.array([topL, botL, botR, topR], dtype="float32")

    # calc the perspective trandorm matrix and warp
    grid = cv2.getPerspectiveTransform(ordered_corners, dimensions)
    return cv2.warpPerspective(img, grid, (width, height))


# ======================= HELPER METHODS =========================

# Finds external contours from processed image and returns board corner points 
def findCorners(img):
    contour = None

    # creates a binary thresholded image
    ret, thresh = cv2.threshold(img, 127, 255, 0)

    '''
    finds the boundaries of shapes having the same intensity
        CHAIN_APPROX_SIMPLE : stores only minimal information of points to describe the contour
        RET_EXTERNAL: gives "outer" contours
    '''
    extContours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # finds the largest 4 sided contour
    for c in extContours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        if len(approx) == 4:
            contour = approx
    
    # if no img contour is valid
    if contour is None: 
        print("No board found")
        exit(1)

    # extracts corners from the contour found
    corners = [(corner[0][0], corner[0][1]) for corner in contour]
    
    # 0 - top left      1 - bottom left     2 - bottom right          3 - top right
    return corners[0], corners[1], corners[2], corners[3]


# Calculates the width of the board
def calcWidth(topL, botL, botR, topR):
    width1 = np.sqrt(((botR[0] - botL[0]) ** 2) + ((botR[1] - botL[1]) ** 2))
    width2 = np.sqrt(((topR[0] - topL[0]) ** 2) + ((topR[1] - topL[1]) ** 2))

    return max(int(width1), int(width2))


# Calculates the height of the board
def calcHeight(topL, botL, botR, topR):
    height1= np.sqrt(((topR[0] - botR[0]) ** 2) + ((topR[1] - botR[1]) ** 2))
    height2 = np.sqrt(((topL[0] - botL[0]) ** 2) + ((topL[1] - botL[1]) ** 2))

    return max(int(height1), int(height2))


boardImg = readImg('board2.png')
cellImgArr = extractCellImgs(boardImg)
extractCellNums(cellImgArr)

