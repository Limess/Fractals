# Mandelbrot Set plot
#import os

from PIL import Image
from math import sqrt
from math import pow
from math import floor
from math import log
import colorsys
import time

# settings
centre = 0 + 0 * 1j # center of iteration.
size = 19200         # resolution size x size.
maxit = 1000.0      # maximum iteration.
outercolour = 3.0   # colour of quickly escaping values
innercolour = 60.0  # colour of slowly escaping values
saturation = 1.0    # level of saturation. 0 gives a black and white image.

# load canvas
image = Image.new("RGB", (size, size))
pix = image.load()  # loads pixels for editing.

# store maximum horizontal, vertical values, time.
xmax = size/2
xmin = size/2
ymin = size/2
start_time = time.time()

for x in xrange(size):
    for y in xrange(size/2):
        # converts canvas coordinates to values in the complex plane, -2<x<1, -2<y<2.
        a = x*(4.0)/size -3
        b = y*(4.0)/size -2
        c = a + b*1j
        i = 0
        z = centre
        p = pow(a-(1.0/4),2) + pow(b,2)
        
        # checks to see if a+b*j is in the 2-bulb.
        if (pow((a+1),2) + pow(b,2)) < (1/16):
            pix[x, y]           = (0,0,0)
            pix[x, size- y - 1] = (0,0,0)
        # checks to see if a+b*j is in the main cardenoid.
        elif pow(b,2) > 4*p*(p+a-1.0/4):
            pix[x, size-y-1]    = (0,0,0)
            pix[x, y+1]         = (0,0,0)
            
        else:
            while abs(z) < max(abs(c),2) and i < maxit:  
                z = z ** 2 + c
                i += 1
                
        # if abs(z) < max(abs(c),2) for maxit iterations, colour black.
            if i == maxit:
                (r,g,b) = (0,0,0)
        # else colour saturation based on smallest k s.t abs(f^k(z)) > maxval.
            else:
                hue = outercolour
                value = 1-log(maxit/i)/log(maxit)
                (r,g,b) = colorsys.hsv_to_rgb(log(maxit/i)/log(maxit), saturation, value)
                
            pix[x, y]               = (int(255*r),int(255*g),int(255*b)) 
            pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
            
        # check maximum horiztonal, vertical values.
        if i >= 2:
            if y<ymin:
                ymin=y
            if x>xmax:
                xmax=x
            if x<xmin:
                xmin=x
        # print at every 10% of points calculated with time value.
        if y == 0 and x % (size/10) == 0 and x > 0:
            print str(10*x/(size/10)) + "% complete. Time: ", round(time.time() - start_time,1), "seconds"
        
print "100% complete. Time: ", round(time.time() - start_time,1) , "seconds."

#print "ymax: ", ymax, " ymin: ", ymin, " xmax: ", xmax, " xmin: ", xmin, "."
#box = (xmin-size/40,ymin-size/40,xmax+size/40,size-ymin+size/40)
box = (xmin,ymin,xmax,size-ymin)
croppedimage = image.crop(box)
(width, height) = croppedimage.size
croppedimage.save("mandelbrot[" + str(width) + "x" + str(height) + "].png")
#os.system("shutdown /s /t 0")
