import os

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

''''
f="a.png"
fu="temp.png"
file=open(f,'rb')
file2=open(fu,'ab')
size=os.path.getsize(f)
print(size)

for b in range(size):
	#print("----------------------")
	print(b)
	f=file.read(1)
	#print(f,"	->	",type(f))
	p=bytes_to_int(f)
	#print(p,"	->	",type(p))
	a=bytes([p])
	#print(a,"	->	",type(a))
	file2.write(a)
	#print("----------------------")
'''
a=ord('#')
print(chr(35))

