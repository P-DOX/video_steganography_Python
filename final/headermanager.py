class headermanager:

	def __init__(self):
		self.hearderlength=25
		self.forsize=8
		self.forseperator=1
		self.seperator='~'
		self.forname=self.hearderlength-self.forsize-self.forseperator

		
	def formheader(self,fname,fsize):

		fs=str(fsize)
		while len(fs)<self.forsize:
			fs='#'+fs

		lt=fname.split('\\')
		if len(lt)!=1:
			fn=lt[-1]
		else:
			lt=fname.split('/')
			fn=lt[-1]

		if len(fn)>self.forname:
			fn=fn[len(fn)-self.forname:len(fn)]
		else:
			while len(fn)<self.forname:
				fn='#'+fn

		return fn+self.seperator+fs

	def getfilename(self,hdr):
		fname=hdr[0:self.forname]

		for i in range(0,len(fname)):
			if fname[i]!='#':
				break

		fname=fname[i:len(fname)]
		return fname

	def getfilesize(self,hdr):
		start=self.forname+self.forseperator
		fsize=hdr[start:self.hearderlength]
		#print(fsize)

		for i in range(0,len(fsize)):
			if fsize[i]!='#':
				break

		fsize=int(fsize[i:self.forsize])
		return fsize


				


'''
h=headermanager()
f='E/Project/a.png'
r=h.formheader(f,909647)
print(r)
p='###########2.mp4~43567234'
s=h.getfilesize(p)
print(s)
'''
