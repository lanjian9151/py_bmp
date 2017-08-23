import struct
fp=open("1.bmp", "rb", 1)
a=fp.read(14)
fp.close()
tp,fs,r1,r2,ofst=struct.unpack("<HIHHI",a)
print("%x"%ofst)
