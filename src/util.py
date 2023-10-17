import numpy as np
import cv2

WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 255]
BLUE = [0, 0, 255]
YELLOW = [0, 255, 255]
BLACK = [0, 0, 0]

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    return lowerLimit, upperLimit

if __name__ == '__main__':
    pass
