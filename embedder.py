import cv2
import os
from headermanager import *
from ByteProcessor import *

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

class embedder:
	
	def __init__(self,toembedd,vessel):
		self.toembedd=toembedd
		self.vessel=vessel
	
	def embedd(self):
		src=cv2.imread(self.toembedd)
		des=cv2.imread(self.vessel)

		se=os.path.getsize(self.toembedd)
		h=headermanager()
		bp=ByteProcessor()
		hdr=h.formheader(self.toembedd,se)

		cols=des.shape[1]
		rows=des.shape[0]
		tp=rows*cols
		cnt= 0
		file=open(self.toembedd,'rb')
		cont=True
		flag=1
		for i in range(0,rows):
			for j in range(0,cols):
				b=des[i,j,0]
				g=des[i,j,1]
				r=des[i,j,2]
				if tp<(len(hdr)+se):
					print("Not Possible")
					return 0
				else:
					if cnt<len(hdr):
						data=ord(hdr[cnt])
					else:
						data=file.read(1)
						data=bytes_to_int(data)
						#print(type(data))
						if cnt==len(hdr)+se+1:
							cont=False
							break
					ar=bp.slice(data,flag)
					result=bp.merge(r,g,b,ar,flag)
					des[i,j,0]=result[2]
					des[i,j,1]=result[1]
					des[i,j,2]=result[0]
					

					flag=(flag+1)%3+1
				cnt=cnt+1
			if cont==False:
				break

		cv2.imwrite('test.png',des)

a='b.jpg'
b='image.png'
e=embedder(a,b)
e.embedd()
		
