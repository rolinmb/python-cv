from util import get_limits, YELLOW
import cv2
cam = cv2.VideoCapture(0)
from PIL import Image

if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Simple (colored) light detection mask
        lowerLimit, upperLimit = get_limits(color=YELLOW)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        print(bbox)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
