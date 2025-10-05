import cv2
import numpy as np
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/istockphoto-1368965646-612x612.jpg",1)
cv2.imshow("Circle image",img)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(img_grey,(3,3))
detector = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,80,param1 = 50,param2 = 33,minRadius = 20,maxRadius = 45)
if detector is not None:
    detector = np.uint16(np.around(detector))
    for i in detector[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(img,(x,y),r,(0,0,0),3)
        cv2.imshow("Image circle",img)
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/istockphoto-1368965646-612x612.jpg",1)
blobdetect = cv2.SimpleBlobDetector_Params()
blobdetect.filterByArea = True
blobdetect.minArea = 800
blobdetect.filterByCircularity = False
blobdetect.minCircularity = 0.25
blobdetect.filterByConvexity = False
blobdetect.minConvexity = 0.1
detector1 = cv2.SimpleBlobDetector_create(blobdetect)
point = detector1.detect(img)
elements = len(point)
font = cv2.FONT_HERSHEY_COMPLEX
position = (0,75)
size = (1.5)
text = (str(elements))
imgtext = cv2.putText(img,text,position,font,size,(0,0,0),3,cv2.LINE_AA)
cv2.imshow("blobs",imgtext)
img_blobs = cv2.drawKeypoints(img,point,img,(0,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Blob detectiom",img_blobs)
cv2.waitKey(0)