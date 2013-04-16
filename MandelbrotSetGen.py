# Mandelbrot Set plot
from PIL import Image
import time
size = 4000 # resolution size x size
image = Image.new("RGB", (size, size))
pix = image.load() # loads pixels for editing
xmax = size/2
xmin = size/2
ymax = size/2
ymin = size/2
start_time = time.time()


for x in xrange(size):
    for y in xrange(size):
        #z = x * (4.0 / size) - 3 + (y * (4.0 / size) - 2) * 1j # changes grid to complex plane -2<=x<=2, -2i<=y<=2
        a = x*(4.0)/size -3
        b = y*(4.0)/size -2
        c = a + b*1j
        i = 0
        z=0
        while abs(z) < max(abs(x+y*1j),2) and i < 256:  
            z = z ** 2 + c
            i += 1
        if i > 1:
            pix[x, size-y-1] = (255-i,255-i,255-i) # if abs(z) < 4 for 256 iterations, colour black, else colour greyscale based on smallest k s.t abs(f^k(z))>maxval
        else:
            pix[x, size-y-1] = (255,255,255)
        #if 255-i/4 != 255:
            #print x,y, " is ", "(",225-i,225-i,225-i,')'
        if 255-i < 100:
            if y>ymax:
                ymax=y
            if y<ymin:
                ymin=y
            if x>xmax:
                xmax=x
            if x<xmin:
                xmin=x
        if y == 0 and x % (size/20) == 0 and x > 0:
            print 5*x/(size/20), "% complete. Time: ", round(time.time() - start_time,1), "seconds"
        
print "100 % complete. Time: ", round(time.time() - start_time,1) , "seconds."

#print "ymax: ", ymax, " ymin: ", ymin, " xmax: ", xmax, " xmin: ", xmin, "."
box = (xmin-size/40,ymin-size/40,xmax+size/40,ymax+size/40)
croppedimage = image.crop(box)
croppedimage.save("mandelbrot[" + str(size) + "x" + str(size) + "].png")
