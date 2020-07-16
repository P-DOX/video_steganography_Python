''''
def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result
'''
#a=b'\xF1\x10'
'''
c=bytes_to_int(a)


p='~'
print(type(ord(p)))

#int.form_bytes(a,byteorder='big')
#c=int(a)
'''
import cv2
src=cv2.imread('test.png')
des=cv2.imread('asd.png')

print(src[103,101],des[103,101])


