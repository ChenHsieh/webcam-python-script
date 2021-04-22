import cv2
import numpy as np

cap = cv2.VideoCapture(0)
import time

nframes = 60*15
interval = 1
img_list = []

for i in range(nframes):
	print(f'taking the picture number {i}') 
	ret, img = cap.read()
	file_name = './img_'+str(i).zfill(4)+'.png'
	img_list.append(file_name)
	cv2.imwrite(file_name, img)
	time.sleep(interval)
	
ww = 640
hh = 480
size = (ww, hh)
#fourcc mp4v or avc1 for mac
video = cv2.VideoWriter('image_sequence.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, size)
print("starting to write video")
for img in img_list:
	img = cv2.imread(img)
	video.write(img)
video.release()
