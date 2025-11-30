import cv2
video = cv2.VideoCapture("/Users/muhammadtaqiriaz/Documents/opencv/Car_detection/Cars.mp4")
path = cv2.CascadeClassifier("/Users/muhammadtaqiriaz/Documents/opencv/Car_detection/cars.xml")
while True:
    value,image = video.read()
    img_grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    car = path.detectMultiScale(img_grey,1.3,4)
    for x,y,w,h in car:
        cv2.rectangle(img_grey,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("image",img_grey)
    cv2.waitKey(0)