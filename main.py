import cv2
import os
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/cherry_img.png",1)
cv2.imshow("cherry image",img)
img2 = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/cherry_img.png",0)
cv2.imshow("cherry image grey",img2)
b,g,r = cv2.split(img)
cv2.imshow("blue saturation",b)
cv2.imshow("green saturation",g)
cv2.imshow("red saturation",r)
folder = "/Users/muhammadtaqiriaz/Documents/opencv/img_save"
os.chdir(folder)
cv2.imwrite("greyscale.png",img2)
cv2.imwrite("blue_saturation.png",b)
cv2.imwrite("green_saturation.png",g)
cv2.imwrite("red_saturation.png",r)
cv2.waitKey(0)
#cv2.destroyAllWindows()