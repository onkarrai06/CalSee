import cv2
import math
import sys
import numpy as np

def getColorFeature(img):
    '''
    Computes the color feature vector of the image
    based on HSV histogram
    '''
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)

    hsvHist = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(6)]

    featurevec = []
    hist = cv2.calcHist([img_hsv], [0, 1, 2], None, [6, 2, 2], [0, 180, 0, 256, 0, 256])
    for i in range(6):
        for j in range(2):
            for k in range(2):
                featurevec.append(hist[i][j][k])
    feature = featurevec[1:]
    M = max(feature)
    m = min(feature)
    feature = list(map(lambda x: x * 2, feature))
    feature = [(x - M - m) / (M - m) for x in feature]
    mean = np.mean(feature)
    dev = np.std(feature)
    feature = [(x - mean) / dev for x in feature]

    return feature

if __name__ == '__main__':
    img = cv2.imread(sys.argv[1])
    featureVector = getColorFeature(img)
    print(featureVector)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
