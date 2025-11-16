import cv2
import os
path = ("/Users/muhammadtaqiriaz/Documents/opencv/Face_detection/haarcascade_frontalface_default.xml")
image_set = ("/Users/muhammadtaqiriaz/Documents/opencv/Face_detection/image_set")
folder = ("/Users/muhammadtaqiriaz/Documents/opencv/Face_detection/image_set/Eshan")
path_save = os.path.join(image_set,folder)
width = 130
height = 100
face_detection = cv2.CascadeClassifier(path)
webcam = cv2.VideoCapture(0)
for i in range(1,30):
    value,image = webcam.read()
    cv2.imshow("image",image)
    img_grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face = face_detection.detectMultiScale(img_grey,1.3,4)
    for x,y,w,h in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        faces =  img_grey[y:y+h,x:x+w]
        faces2 = cv2.resize(faces,(width,height))
        cv2.imwrite("%s/%s.png"%(path_save,i),faces2)
    image2 = cv2.imshow("image",image)
    key = cv2.waitKey(10)
    if key == 27:
        break
    