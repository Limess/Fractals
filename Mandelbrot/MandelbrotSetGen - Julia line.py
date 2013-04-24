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
size = 600         # resolution size x size.
maxit = 1000.0      # maximum iteration.
innercolour = 340.0  # colour of slowly escaping values, 0-360
saturation = 0.0    # level of saturation. 0 gives a black and white image.
d = 0.0 + 0.66j

# load canvas
image = Image.new("RGB", (size, size))
pix = image.load()  # loads pixels for editing.

# store maximum horizontal, vertical values, time.
xmax = size/2
xmin = size/2
ymin = size/2
start_time = time.time()

for x in xrange(size):
    for y in xrange(size):
        # converts canvas coordinates to values in the complex plane, -2<=x<=1, -1.5<=y<=1.5.
        a = x*(3.0)/size -2
        b = y*(3.0)/size -1.5
        c = a + b*1j
        i = 0
        z = centre
        p = pow(a-(1.0/4),2) + pow(b,2)
        # checks to see if a+b*j is in the 2-bulb.
        if (pow((a+1),2) + pow(b,2)) < (1/16):
            #pix[x, y]           = (0,0,0)
            pix[x, size- y - 1] = (0,0,0)
        # checks to see if a+b*j is in the main cardenoid.
        elif pow(b,2) > 4*p*(p+a-1.0/4):
            pix[x, size-y-1]    = (0,0,0)
            #pix[x, y]           = (0,0,0)
            
        else:
            while abs(z) < max(abs(c),2) and i < maxit:  
                z = z ** 2 + c
                i += 1
                
        # if abs(z) < max(abs(c),2) for maxit iterations, colour black.
            if i == maxit:
                (r0,g0,b0) = (0,0,0)
        # else colour saturation based on smallest k s.t abs(f^k(z)) > maxval.
            else:
                value = log(maxit/i)/log(maxit)
                (r0,g0,b0) = colorsys.hsv_to_rgb(0, saturation, value)
                
            #pix[x, y]               = (int(255*r0),int(255*g0),int(255*b0)) 
            pix[x, size - y - 1]    = (int(255*r0),int(255*g0),int(255*b0))
            
        # check maximum horiztonal, vertical values.
        if i >= 2:
            if y<ymin:
                ymin=y
            if x>xmax:
                xmax=x
            if x<xmin:
                xmin=x
        if abs(d.real - a) < 10**(-3):
            #print x, y
            #pix[x, y]         = (255,0,0)
            pix[x, size- y - 1] = (255,0,0)
        #print abs(b-d.imag)
        if abs(d.imag- b) < 10**(-3):
            #pix[x, y]         = (255,0,0)
            pix[x, size- y - 1] = (255,0,0)
        # print at every 10% of points calculated with time value.
        if y == 0 and x % (size/10) == 0 and x > 0:
            print str(10*x/(size/10)) + "% complete. Time: ", round(time.time() - start_time,1), "seconds"
        
print "100% complete. Time: ", round(time.time() - start_time,1) , "seconds."

#print "ymax: ", ymax, " ymin: ", ymin, " xmax: ", xmax, " xmin: ", xmin, "."
#box = (xmin-size/40,ymin-size/40,xmax+size/40,size-ymin+size/40)
box = (xmin,ymin,xmax,size-ymin)
croppedimage = image.crop(box)
(width, height) = croppedimage.size
croppedimage.save("mandelbrot[" + str(width) + "x" + str(height) + "]withc=" + str(d) + ".png")
#os.system("shutdown /s /t 0")
