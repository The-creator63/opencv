import cv2
import numpy as np
import random
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/img_1.jfif",1)
cv2.imshow("Image 1",img)
img_big = cv2.resize(img,(500,350))
cv2.imshow("Image 1 resize",img_big)
img_2 = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/img_2.jfif",1)
cv2.imshow("Image 2",img_2)
img2_big = cv2.resize(img_2,(500,350))
cv2.imshow("Image 2 resize",img2_big)
img_weighted = cv2.addWeighted(img_big,0.5,img2_big,0.5,-25)
cv2.imshow("Image weighted",img_weighted)
img_subtract = cv2.subtract(img_big,img2_big)
cv2.imshow("Image subrtact",img_subtract)
kernel = np.ones((5,5),np.uint8)
img_erosion = cv2.erode(img,kernel)
cv2.imshow("Image 1 erosion",img_erosion)
img_blur = cv2.GaussianBlur(img,(15,15),0)
cv2.imshow("Image 1 gaussian blur",img_blur)
img_medianblur = cv2.medianBlur(img,(15))
cv2.imshow("Image 1 median blur",img_medianblur)
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)
img_border = cv2.copyMakeBorder(img,9,9,9,9,cv2.BORDER_CONSTANT,value = (r,b,b))
cv2.imshow("Image 1 border constant",img_border)
img_border2 = cv2.copyMakeBorder(img,9,9,9,9,cv2.BORDER_REFLECT)
cv2.imshow("Image 1 border reflect",img_border2)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image 1 greyscale",img_grey)
rows,columns = img.shape[0:2]
for i in range(rows):
    for j in range(columns):
        img[i,j] = sum(img[i,j]) * 0.3
cv2.imshow("Image 1 greyscale 2",img)
img = cv2.imread("/Users/muhammadtaqiriaz/Documents/opencv/img_1.jfif",1)
rows,columns = img.shape[0:2]
rotate_m = cv2.getRotationMatrix2D((rows/2,columns/2),90,1)
img_rotate = cv2.warpAffine(img,rotate_m,(rows,columns))
cv2.imshow("Image 1 rotation",img_rotate)
img_edge = cv2.Canny(img,100,200)
cv2.imshow("Image 1 edges",img_edge)
cv2.waitKey(0)