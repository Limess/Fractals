# Julia sets algorithm
from PIL import Image
from math import *
size = 300 # resolution size x size
maxit = 1000
step = 1

c = complex(0.0,0.66) # j is i in python#
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


imagek.save("juliafilled(" + str(c.real) + "+" + str(c.imag) + "i).png")
print "Filled-in Julia set saved, output name: juliafilled(" + str(c.real) + "+" + str(c.imag) + "i).png"

images = Image.new("RGB", (size, size))
pixs = images.load()

for x in range(0, size-step, step):
    for y in range(0, size-step, step):
        k = 0
        if pixk[x,y] == (0,0,0):
            k += 1
        if pixk[x,y+step] == (0,0,0):
            k += 1
        if pixk[x+step,y] == (0,0,0):
            k += 1
        if pixk[x+step,y+step] == (0,0,0):
            k += 1
        if k <= 1:
            for p in range (x, x + step + 1):
                for q in range (y, y + step + 1):
                    pixs[p,q] = (255,255,255)
        if k >=2 and k <=3:
            for p in range (x, x + step + 1):
                for q in range (y, y + step + 1):
                    pixs[p,q] = (0,0,0)
        else:
            for p in range (x, x + step + 1):
                for q in range (y, y + step + 1):
                    pixs[p,q] = (255,255,255)

images.save("julia(" + str(c.real) + "+" + str(c.imag) + "i).png")
print "Julia set saved, output name: julia(" + str(c.real) + "+" + str(c.imag) + "i).png"
