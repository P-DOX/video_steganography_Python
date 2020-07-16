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
		#print(se)
		h=headermanager()
		bp=ByteProcessor()
		hdr=h.formheader(self.toembedd,se)

		cols=des.shape[1]
		rows=des.shape[0]
		tp=rows*cols
		#print(tp)
		cnt= 0
		file=open(self.toembedd,'rb')
		f2=open("asdf.png",'ab')
		cont=True
		flag=1
		hg=" "
		for i in range(0,rows):
			for j in range(0,cols):
				b=des[i,j,0]
				g=des[i,j,1]
				r=des[i,j,2]
				print("->",r,g,b)
				if tp<(len(hdr)+se):
					print("Not Possible")
					return 0
				else:
					if cnt<len(hdr):
						data=ord(hdr[cnt])
						#print(data)
					else:
						data=file.read(1)
						data=bytes_to_int(data)
		
						if cnt==len(hdr)+se+1:
							cont=False
							break
					#print(type(data))
					ar=bp.slice(data,flag)
					#print(data,flag)
					#print(ar)
					result=bp.merge(r,g,b,ar,flag)
					des[i,j,0]=result[2]
					des[i,j,1]=result[1]
					des[i,j,2]=result[0]

					if cnt<len(hdr):
						print(des[i,j,2],des[i,j,1],des[i,j,0])
						ar=bp.extract(result[0],result[1],result[2],flag)
						da=bp.combine(ar,flag)
						hg=hg+chr(da)
						print(hg)
						#print(chr(da),type(chr(da)))
						da=bytes([da])

						#print(da,type(da))

					
					flag=(flag+1)%3+1
				cnt=cnt+1
			if cont==False:
				break
		#print(cont)
		#print(len(hdr))
		cv2.imwrite('test.png',des)
			

		

a='a.png'
b='c.jpg'
e=embedder(a,b)
e.embedd()
		