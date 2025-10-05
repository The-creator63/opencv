import cv2
import os
from PIL import Image
os.chdir("/Users/muhammadtaqiriaz/Documents/opencv/images_video")
path = "/Users/muhammadtaqiriaz/Documents/opencv/images_video"
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
for k in list:
    if k.endswith((".jpg",".jpeg")):
        img_store2 = Image.open(os.path.join(path,k))
        img_resize = img_store2.resize((mwidth,mheight),Image.Resampling.LANCZOS)
        img_resize.save(k,"JPEG",quality = 95)
cv2.waitKey(0)