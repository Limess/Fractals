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
z=[0 for i in range(maxit+2)]
solutions=[] # creates an array of solutions to the desired equation
start_time = time.time()

def f(z):
    return z**6+z**3-1
def df(z):
    return 6*z**5+3*z**2
def P(z):
    return z - f(z)/df(z)

for x in xrange(size):
    for y in xrange(size):
        z[0] = x * (4.0 / size) - 2 + (y * (4.0 / size) - 2) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
        i = 0
        n = -1
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
                #print n
                break
        if n < 0:
            solutions.append(z[i+1])
            n = solutions.index(z[i+1])
            #print n
        if i>=1:
            (r,g,b) = colorsys.hsv_to_rgb(20*n/360.0, 1, 0.4+0.6*(log(maxit/i)/log(maxit)))
            pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
            #print x, " + ", y , "*j has root ", solutions[n]
        else:
            pix[x, size-y-1] = (0,0,0)
            print x, " + ", y , "*j has no root"
        # print at every 10% of points calculated with time value.
        if y == 0 and x % (size/20) == 0 and x > 0:
            print str(20*x/(size/5)) + "% complete. Time: ", round(time.time() - start_time,1), "seconds"

print solutions
image.save("newtonjuliafilled.png")
print "Done"
