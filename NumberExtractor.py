import keras
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

import cv2

# the data, split between train and test sets
import tensorflow
from tensorflow import keras
from tensorflow.python.keras import Sequential
# from tensorflow.python.keras.optimizers import SGD

trainSamples = trainLabels = testSamples = testLabels = None


# Reshapes the data
def processData():
    '''
    MNIST data is split between train and test sets
        data set of 60,000 28x28 grayscale images of the 10 digits; (trainSamples, trainLabels)
        test set of 10,000 images; (testSamples, testLabels)
    '''
    (trainSamples, trainLabels), (testSamples, testLabels) = mnist.load_data()
    print(trainSamples)
    print(trainLabels)
    print("break")
    print(testSamples)
    print(testLabels)
    # Flattens 2D arrays of image/label data to 1D arrays
    trainSamples = trainSamples.reshape(trainSamples.shape[0], 28, 28, 1).astype('float32')
    testSamples = testSamples.reshape(testSamples.shape[0], 28, 28, 1).astype('float32')

    # One-Hot Code technique == representation of categorical data in a more expressive way
    trainLabels = np_utils.to_categorical(trainLabels)
    testLabels = np_utils.to_categorical(testLabels)

    # convert from integers to floats
    trainSamples = trainSamples.astype('float32')
    testSamples = testSamples.astype('float32')
    # normalize to range [0, 1]
    trainSamples = (trainSamples / 255.0)
    testSamples = (testSamples / 255.0)

    return trainSamples, trainLabels, testSamples, testLabels


# Defines a baseline Convolutional Neural Network (CNN) model
def createModel():
    # Create model/building CNN
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model


# Runs training and test data through the model, and saves the model
def evaluateModel(trainSamples, trainLabels, testSamples, testLabels):
    # create model
    model = createModel()

    # compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit model - runs input data through CNN
    dataFit = model.fit(trainSamples, trainLabels, epochs=1, batch_size=32, verbose=2, validation_data=(testSamples, testLabels))

    # save model and architecture to single file
    # model.save("cnn.hdf5")
    return model



def predict(model,img):
    '''cv2.imshow('croppedAndWarped', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

    img = cv2.resize(img, (28, 28))
    img = img.astype('float32')
    img = img.reshape(1, 28, 28, 1)
    img /= 255

    # model = load_model('cnn.hdf5')
    pred = model.predict(img.reshape(1, 28, 28, 1), batch_size=1)

    print("Predicted Number: ", pred.argmax())
    return pred.argmax()



'''
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# save model and architecture to single file
model.save("model.h5")
print("Saved model to disk")

thresh = 128  # define a threshold, 128 is the middle of black and white in grey scale
# threshold the img
gray = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

# Find contours
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)

    if (x < 3 or y < 3 or h < 3 or w < 3):
        # Note the number is always placed in the center
        # Since img is 28x28
        # the number will be in the center thus x >3 and y>3
        # Additionally any of the external lines of the sudoku will not be thicker than 3
        continue
    ROI = gray[y:y + h, x:x + w]
    # increasing the size of the number allws for better interpreation,
    # try adjusting the number and you will see the differnce
    ROI = scale_and_centre(ROI, 120)
  
    tmp_sudoku[i][j] = predict(ROI)'''