import cv2
import numpy as np
video = cv2.VideoCapture("/Users/muhammadtaqiriaz/Documents/opencv/IMG_1122.MOV")
background = None
for i in range(50):
    valid,frame = video.read()
    if valid is False:
        print("frame is invalid")
        continue
    background = frame 
background = np.flip(background,axis = 1)
while video.isOpened():
    valid2,frame2 = video.read()
    if valid2 is False:
        print("no more frames")
        break
    frame2 = np.flip(frame2,axis = 1)
    hsvf = cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
    lower_green = np.array([25,40,40])
    upper_green = np.array([100,255,255])
    mask1 = cv2.inRange(hsvf,lower_green,upper_green)
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations = 1)
    mask3 = cv2.bitwise_not(mask1)
    rframe = cv2.bitwise_and(background,background,mask = mask1)
    rframe2 = cv2.bitwise_and(frame2,frame2,mask = mask3)
    result = cv2.addWeighted(rframe,1,rframe2,1,0)
    cv2.imshow("invisible man green cloak",result)
    key = cv2.waitKey(10)
    if key == 27:
        break