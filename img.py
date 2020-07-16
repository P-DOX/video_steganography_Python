'''
import numpy as np 
import cv2

#img = cv2.imread('asd.jpg')
#cv2.imshow('Image',img)
#cols = img.shape[1]
#print(cols)

cap = cv2.VideoCapture('2.mp4')

while(cap.isOpened()):
	ret,frame = cap.read()
	if ret==True:
		cv2.imshow('Frame',frame)
	else:
		break



pixel = img[500,500,1]
print (pixel)


for i in pixel:
	print(i, end=' ')
k = cv2.waitKey(0)
if k==27:
	cap.release()
	cv2.destroyAllWindows()
'''
import cv2
src=cv2.imread('b.jpg')
des=cv2.imread('t.png')

# print(des.shape[0],des.shape[1])
for i in range(des.shape[0]):
	for j in range(des.shape[1]):
		print(src[i,j],des[i,j])
