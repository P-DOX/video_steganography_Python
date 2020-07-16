import cv2
import numpy as np

cap = cv2.VideoCapture('as.mp4')
 
#Check if camera opened successfully
if (cap.isOpened()== False): 
   print("Error opening video stream or file")
#length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


frame = cap.read()

ret,frame=cap.read()
row=frame.shape[0]
col=frame.shape[1]
print(row,col)
#cv2.imwrite('temp.png',frame) 

# Read until video is completed
cnt=0
while(cap.isOpened()):
  #cnt=cnt+1
  # Capture frame-by-frame
  ret, frame = cap.read()  
  cv2.imshow('Frame',frame)
  #hdr="frame"+str(cnt)
  #print(hdr)
'''
  for i in range(row):
  	for j in range(col):
      
      
  		if i==j:
  			frame[i,j,0]=0
  			frame[i,j,1]=0
  			frame[i,j,2]=0
                  

'''
  #cv2.imshow('Frame',frame) 
  # Press Q on keyboard to  exit
  #if cv2.waitKey(25) & 0xFF == ord('q'):
   #break
 
  # Break the loop
  #else: 
   # break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

