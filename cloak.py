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