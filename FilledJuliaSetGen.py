# Filled in Julia sets algorithm
from PIL import Image
size = 500 # resolution size x size
image = Image.new("RGB", (size, size))
pix = image.load() # loads pixels for editing
c = -0.33+0.92j # j is i in python#
maxval = max(abs(c),2) # sets the bound based on Devaney's escape time algorithm

for x in xrange(size):
    for y in xrange(size):
        z = x * (4.0 / size) - 2 + (y * (4.0 / size) - 2) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
        i = 0
        while abs(z) < maxval and i < 1024:  
            z = z ** 2 + c
            i += 1
        pix[x, size-y-1] = (255-i/4,255-i/4,255-i/4) # if abs(z) < 4 for 256 iterations, colour black, else colour greyscale based on smallest k s.t abs(f^k(z))>maxval
        #if 255-i/4 != 255:
            #print x,y, " is ", "(",225-i/4,225-i/4,225-i/4,')'
        
image.save("juliafilled.png")
