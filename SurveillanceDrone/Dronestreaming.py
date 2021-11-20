import cv2
from djitellopy import *
from tkinter import *
import tkinter
counter = 0

# Initialize the drone
# create an instance of tello drone
my = Tello()
my.connect()
my.streamon()

# build interface
w = Tk()
w.geometry("400x300")
# definition of take image function
def takeImage():
    global counter = counter+1
    img = my.get_frame_read().frame
    cv2.imwrite(f'images/image-{counter}.png',img)

# -----button----------
btn = Button(text="Take Photo", command=takeImage)
btn.pack()
# Streaming
while True:
    img = my.get_frame_read().frame
    img = cv2.resize(img, (400,360))
    cv2.imshow("Drone Streaming ",img)
    if cv2.waitKey(25) and 0xFF==ord('q'):
        break
    w.mainloop()







