import cv2
import time
import HandTrackingModule as htm
import math
import numpy as np
# import volume packages Pycaw, ctypes,comtypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



# setup webcam

# detect hands
detector = htm.handDetector()
cap = cv2.VideoCapture(0)
x4, y4 = 0,0
x8, y8 = 0,0
distance = 0
# colors constants   rgb   bgr
red = (0,0,255)
green  = (0,255,0)
blue = (255,0,0)
def findDistance(A,B):
    AB =math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    return AB

# initialize the volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol = volume.GetVolumeRange()

print(vol)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lm = detector.findPosition(img, draw =False)
    if len(lm) != 0:
        x4 = int(lm[4][1])
        y4 = int(lm[4][2])
        x8 = int(lm[8][1])
        y8 = int(lm[8][2])
    A=(x4,y4)
    B = (x8,y8)
    cx, cy = (x4+x8) //2, (y4+y8) //2
    C = (cx, cy)
    cv2.line(img,A,B,(0,0,255), 4, )
    # Draw a circle on A and B
    cv2.circle(img, A, 15, red, cv2.FILLED)
    cv2.circle(img, B, 15, red, cv2.FILLED)

    # draw circle on the center
    cv2.circle(img, C, 15, red, cv2.FILLED )
    cv2.imshow("HAND GESTURE VOLUME CONTROL", img)
    # Distance
    distance = findDistance(A,B)
    # convert the distance to the volume range | hand range 20 - 290 | volume range -63,5  0
    handRange =[20, 290]
    volRange = [vol[0],vol[1]]
    volu = np.interp(distance,handRange,volRange )
    # Change the volume level
    print(findDistance(A, B), volu)
    volume.SetMasterVolumeLevel(volu, None)
    cv2.waitKey(1)

