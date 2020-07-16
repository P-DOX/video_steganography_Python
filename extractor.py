import cv2
import os
from headermanager import *
from ByteProcessor import *

class extractor:
	def __init__(self,vessel,target):
		self.vessel=vessel
		self.target=target

	def extract(self):
		ves=cv2.imread(self.vessel)
		cols=ves.shape[1]
		rows=ves.shape[0]
		flag=1
		h=headermanager()
		bp=ByteProcessor()
		cnt=0
		cont=True

		hdr=""

		f=open(self.target,'ab')	

		for i in range(0,rows):
			for j in range(0,cols):
				b=ves[i,j,0]
				g=ves[i,j,1]
				r=ves[i,j,2]

				#print(r,g,b)

				ar=bp.extract(r,g,b,flag)
				data=bp.combine(ar,flag)

				if cnt<h.hearderlength:
					hdr=hdr+chr(data)
					if cnt==h.hearderlength-1:
						fname=h.getfilename(hdr)
						fsize=h.getfilesize(hdr)
						print(fname,fsize)
						f.seek(0,0)
				else:
					data=bytes([data])
					f.write(data)
					#print("--")
					if cnt==fsize+h.hearderlength-1:
						cont=False
						break

				cnt=cnt+1
				flag=(flag+1)%3+1
			if cont==False:
				#print(cnt)
				break

a='test.png'
b='t.png'
ex=extractor(a,b)
ex.extract()
