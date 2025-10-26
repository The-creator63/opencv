import cv2
import os
from PIL import Image
os.chdir("/Users/muhammadtaqiriaz/Documents/opencv/images_videohw")
path = "/Users/muhammadtaqiriaz/Documents/opencv/images_videohw"
mwidth = 0
mheight = 0
list = []
for i in os.listdir("."):
    if i.endswith((".jpg",".jpeg")):
        list.append(i)
for j in list:
    img_store = Image.open(os.path.join(path,j))
    width,height = img_store.size
    mwidth = mwidth + width
    mheight = mheight + height
length = len(list)
mwidth = mwidth//length
mheight = mheight//length
for n in list:
    if n.endswith((".jpg",".jpeg")):
        img_store2 = Image.open(os.path.join(path,n))
        img_resize = img_store2.resize((mwidth,mheight),Image.Resampling.LANCZOS)
        img_resize.save(n,"JPEG",quality = 95)
video_name = "videohw.avi"
os.chdir("/Users/muhammadtaqiriaz/Documents/opencv/images_videohw")
images =  []
for l in list:
    if l.endswith((".jpg",".jpeg")):
        images.append(l)
frame = cv2.imread(os.path.join(".",images[0]))
print(frame.shape)
width2,height2,colour = frame.shape
video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*"XVID"),1,(width2,height2))
for g in images:
    video.write(cv2.imread(os.path.join(".",g)))
video.release()
cv2.waitKey(0)