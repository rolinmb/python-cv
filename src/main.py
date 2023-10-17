from util import get_limits, YELLOW
import cv2
cam = cv2.VideoCapture(0)

if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Simple (colored) light detection mask
        lowerLimit, upperLimit = get_limits(color=YELLOW)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        cv2.imshow('frame', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
