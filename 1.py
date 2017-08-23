# define the class of bitmap-file header and bitmap-information header
class Bmheader:
    
    bfType = 0
    bfSize = 0
    bfReserved1 = 0
    bfReserved2 = 0
    bfOffBits = 0
    biSize = 0
    biWidth = 0
    biHeight = 0
    biPlanes = 0
    biBitCount = 0
    biCompression = 0
    biSizeImage = 0
    biXPelsPerMeter = 0
    biYPelsPerMeter = 0
    biClrUsed = 0
    biClrImportant = 0

    def __init__(self,bfType,bfSize,bfReserved1,bfReserved2,bfOffBits,biSize,
                 biWidth,biHeight,biPlanes,biBitCount,biCompression,biSizeImage,
                 biXPelsPerMeter,biYPelsPerMeter,biClrUsed,biClrImportant):
        self.bfType = bfType
        self.bfSize = bfSize
        self.bfReserved1 = bfReserved1
        self.bfReserved2 = bfReserved2
        self.bfOffBits = bfOffBits
        self.biSize = biSize
        self.biWidth = biWidth
        self.biHeight = biHeight
        self.biPlanes = biPlanes
        self.biBitCount = biBitCount
        self.biCompression = biCompression
        self.biSizeImage = biSizeImage
        self.biXPelsPerMeter = biXPelsPerMeter
        self.biYPelsPerMeter = biYPelsPerMeter
        self.biClrUsed = biClrUsed
        self.biClrImportant = biClrImportant



import struct

bmpfile = input("Input File Name: ")
fp = open(bmpfile,"rb",1)

header = Bmheader(*(struct.unpack("<HIHHIIIIHHIIIIII",fp.read(54))))
new_header = [ header.bfType,header.bfSize,header.bfReserved1,header.bfReserved2,
               header.bfOffBits,header.biSize,header.biWidth,header.biHeight,header.biPlanes,
               header.biBitCount,header.biCompression,header.biSizeImage,header.biXPelsPerMeter,
               header.biYPelsPerMeter,header.biClrUsed,header.biClrImportant ]

fp1 = open("%s_convert.bmp"%bmpfile,"wb",1)
fp1.write(struct.pack("<HIHHIIIIHHIIIIII",*new_header))

buffer = list(struct.unpack("<%dB"%header.biSizeImage,fp.read(header.biSizeImage)))
fp.close()

for i in range(0,header.biSizeImage,3):
    avr=int((buffer[i]+buffer[i+1]+buffer[i+2])/3)
    buffer[i]=avr
    buffer[i+1]=avr
    buffer[i+2]=avr
    
fp1.write(struct.pack("<%dB"%header.biSizeImage,*buffer))    
fp1.flush()
fp1.close()

         
print(header.biSizeImage)
