class ByteProcessor:
	
	def slice(self,x,flag):
		if flag==1:
			arr = [(x&224)>>5 , (x&28)>>2 , (x&3)]
		elif flag==2:
			arr = [(x&224)>>5 , (x&24)>>3 , (x&7)]
		else:
			arr = [(x&192)>>6 , (x&56)>>3 , (x&7)]

		return arr

	def merge(self,r,g,b,arr,flag):
		if flag==1:
			result = [ (r&(~7))|arr[0] , (g&(~7))|arr[1] , (b&(~3))|arr[2] ]
		elif flag==2:
			result = [ (r&(~7))|arr[0] , (g&(~3))|arr[1] , (b&(~7))|arr[2] ]
		else:
			result = [ (r&(~3))|arr[0] , (g&(~7))|arr[1] , (b&(~7))|arr[2] ]

		return result

	def extract(self,r,g,b,flag):
		if flag==1:
			result = [ r&7 , g&7 , b&3 ]
		elif flag==2:
			result = [ r&7 , g&3 , b&7 ]
		else:
			result = [ r&3 , g&7 , b&7 ]
		return result

	def combine(self,arr,flag):
		if flag==1:
			return arr[0] <<5 | (arr[1]<<2) |arr[2]
		elif flag==2:
			return arr[0] <<5 | (arr[1]<<3) |arr[2]
		else:
			return arr[0] <<6 | (arr[1]<<3) |arr[2]



'''
b = ByteProcessor()

ar=[35,35,35,35,35,35,35,35,35,35,35,98,46,106,112,103,126,35,35,51,53,51,48,53,51]
flag=1
for n in ar:
	temp=b.slice(n,flag)
	print(temp)
	flag=(flag+1)%3+1
'''