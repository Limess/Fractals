# Filled in Julia sets algorithm
from PIL import Image
from math import *
from images2gif import *
from numpy import *
size = 1000 # resolution size x size
maxit = 100
images = []
start = -100
end = 100
t = 0

print "Start"

for k in range (start , end+1, 1):
    s = 0.01 * k
    c = complex(s,0.5) # j is i in python#
    #print c
##    imagek = Image.open("juliafilled" + str(c) + ".png")
##    pixk = imagek.load() # loads pixels for editing
    maxval = max(abs(c),2) # sets the bound based on Devaney's escape time algorithm

    imagek = Image.new("RGB", (size, size))
    pixk = imagek.load() # loads pixels for editing

    for x in xrange(size):
        for y in xrange(size):
            z = x * (4.0 / size) - 2 + (y * (4.0 / size) - 2) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
            i = 0
            while abs(z) < maxval and i < maxit:  
                z = z ** 2 + c
                i += 1
            pixk[x, size-y-1] = (int(255-floor(i/(maxit/255.0))),int(255-floor(i/(maxit/255.0))),int(255-floor(i/(maxit/255.0)))) # if abs(z) < 4 for 256 iterations, colour black, else colour greyscale based on smallest k s.t abs(f^k(z))>maxval
            #if 255-i/4 != 255:
                #print x,y, " is ", "(",225-i/4,225-i/4,225-i/4,')'
            
    images.append(imagek)
    #image.save("juliafilled" + str(c) + ".png")
    if abs(k) % ((start-end)/20) == 0:
        if t > 0 :
            print str(5*t) + "% Completed."
        t += 1
writeGif("gifjuliafilled.gif", images, duration=0.05, repeat=True, dither=False, 
                nq=0, subRectangles=True, dispose=None)
