import cv2
import os
import numpy as np
path = ("/Users/muhammadtaqiriaz/Documents/opencv/Face_detection/haarcascade_frontalface_default.xml")
image_set = ("/Users/muhammadtaqiriaz/Documents/opencv/Face_detection/image_set")
images = []
labels = []
names = {}
id = 0
for subdirs,dirs,files in os.walk(image_set):
    for subdirs in dirs:
        names[id] = subdirs
        fpath = os.path.join(image_set,subdirs)
        for i in os.listdir(fpath):
            ipath = (fpath) + "/" + i
            label = id 
            images.append(cv2.imread(ipath,0))
            labels.append(label)
        id = id + 1
print(labels)
print(names)
images = np.array(images)
labels = np.array(labels)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
face_detection = cv2.CascadeClassifier(path)
webcam = cv2.VideoCapture(0)
while True:
    value,image = webcam.read()
    img_grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face = face_detection.detectMultiScale(img_grey,1.3,4)
    for x,y,w,h in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        faces =  img_grey[y:y+h,x:x+w]
        faces2 = cv2.resize(faces,(130,100))
        result = model.predict(faces2)
        print(result)
    cv2.imshow("image",image)
    key = cv2.waitKey(10)
    if key == 27:
         break