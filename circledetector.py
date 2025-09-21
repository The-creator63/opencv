import cv2
import numpy as np
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/image3.jfif",1)
cv2.imshow("Circle image",img)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(img_grey,(3,3))
detector = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2 = 30,minRadius = 3,maxRadius = 40)
if detector is not None:
    detector = np.uint16(np.around(detector))
    for i in detector[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(img,(x,y),r,(0,0,0),3)
        cv2.imshow("Image circle",img)
cv2.waitKey(0)