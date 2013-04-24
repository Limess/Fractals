# Filled in Julia sets algorithm
from PIL import Image
from math import *
import colorsys
import time
size = 5000 # resolution size x size
maxit = 350
error = 10**(-12)
image = Image.new("RGB", (size, size))
pix = image.load() # loads pixels for editing
solutions=[] # creates an array of solutions to the desired equation
start_time = time.time()

def f(a,b):
    return cosh(a)*cos(b)+1j*sinh(a)*sin(b)
def df(a,b):
    return sinh(a)*cos(b)+1j*cosh(a)*sin(b)
def P(a,b):
    return a+b*1j - f(a,b)/df(a,b)

def Black():
    pix[x, size-y - 1] = (0,0,0)
    #print x, " + ", y , "*j has no root"

def Red():
    pix[x, size-y - 1] = (255,0,0)
    
for x in xrange(size):
    for y in xrange(size):
        z=[None for i in range(maxit+2)]
        z[0] = x * (1.0 / size)-0.5 + (y * (1.0 / size)-0.5) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
        i = 0
        n = -1
        while i < maxit:
            i += 1
            try:
                z[i] = P(z[i-1].real, z[i-1].imag)
            except ZeroDivisionError:
                print "WARNING! ZERO!"
                n=-5
                break
            try:
                if abs(f(z[i].real,z[i].imag)) < error:
                    break
            except OverflowError:
                #print "OverflowError"
                break
        if n == -5:
            Black()
        else:
            if z[i] == z[i-2]:
                #print abs(f(z[i].real,z[i].imag))
                print i, z[i], z[i-2]
                Red()
            elif z[i] != z[i-2]:
                for sol in solutions:
                    #print z[0],z[i-1],z[i],x,y,i
                    rootcheck=abs(z[i]-sol)
                    if rootcheck < error:
                        n = solutions.index(sol)
                        break
            if n < 0 and n!=-5:
                solutions.append(z[i])
                n = solutions.index(z[i])
            if i>=1 and n!=-5:
                (r,g,b) = colorsys.hsv_to_rgb(((137+60)%360.0)/360, 1, 0.4+0.5*(log(maxit/i)/log(maxit)))
                pix[x, size - y - 1]    = (int(255*r),int(255*g),int(255*b))
                #print x, " + ", y , "*j has root ", solutions[n]
                
        # print at every 10% of points calculated with time value.
        if y == 0 and x % (size/20) == 0 and x > 0:
            print str(20*x/(size/5)) + "% complete. Time: ", round(time.time() - start_time,1), "seconds"

print solutions
print "There were ",len(solutions), "solutions."
image.save("newtonjuliafilled.png")
