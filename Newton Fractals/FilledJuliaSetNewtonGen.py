# Filled in Julia sets algorithm
from PIL import Image
from math import *
import colorsys
import time
size = 1000 # resolution size x size
maxit = 50
error = 10**(-10)
order = 3
image = Image.new("RGB", (size, size))
pix = image.load() # loads pixels for editing
n=4
z=[0 for i in range(maxit+2)]
solutions=[cos((pi*2.0*(k+1.0))/3.0)+sin((pi*2.0*(k+1.0))/3.0)*1j for k in range(3)] # creates an array of solutions to the desired equation
start_time = time.time()

def f(z):
    return z**order -1
def P(z):
    return (2*(z**3) + 1)/(3*(z**2))

for x in xrange(size):
    for y in xrange(size):
        z[0] = x * (4.0 / size) - 2 + (y * (4.0 / size) - 2) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
        i = 0
        while i < maxit:  
            try:
                z[i+1] = P(z[i])
            except ZeroDivisionError:
                #print "WARNING! ZERO!", x ,y
                break
            if abs(f(z[i+1])) < error:
                break
            i += 1
        for sol in solutions:
            rootcheck=abs(z[i+1]-sol)
            if rootcheck < error:
                n = solutions.index(sol)
                break
            else:
                n = 4
        if n == 0 and i>=1:
            (r,g,b) = colorsys.hsv_to_rgb(210/360.0, 1, 0.4+0.6*(log(maxit/i)/log(maxit)))
            pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
            #print x, " + ", y , "*j has root ", solutions[n]
        elif n == 1 and i>=1:
            (r,g,b) = colorsys.hsv_to_rgb(180/360.0, 1, 0.4+0.6*(log(maxit/i)/log(maxit)))
            pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
            
            #print x, " + ", y , "*j has root ", solutions[n]
        elif n == 2 and i>=1:
            (r,g,b) = colorsys.hsv_to_rgb(150/360.0, 1, 0.4+0.6*(log(maxit/i)/log(maxit)))
            pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
            
            #print x, " + ", y , "*j has root ", solutions[n]
        else:
            pix[x, size-y-1] = (0,0,0)
            print x, " + ", y , "*j has no root"
        # print at every 10% of points calculated with time value.
        if y == 0 and x % (size/20) == 0 and x > 0:
            print str(20*x/(size/5)) + "% complete. Time: ", round(time.time() - start_time,1), "seconds"
    
image.save("newtonjuliafilled.png")
print "Done"
