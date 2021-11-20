
import cv2
from djitellopy import *

# create an instance of tello drone
my = Tello()
my.connect()
my.streamon()

while True:
    img = my.get_frame_read().frame
    img = cv2.resize(img, (400,360))
    cv2.imshow("Drone Streaming ",img)
    if cv2.waitKey(25) and 0xFF==ord('q'):
        break






