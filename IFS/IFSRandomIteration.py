# Levy Dragon Random Iteration Algorithm
import math
import random
from PIL import Image
from PIL import ImageDraw

## Image Properties
imgx = 4000; imgy = 4000 # dimensions of canvas
image = Image.new("RGB", (imgx, imgy), (255,255,255)) # greyscale image white canvas
pix = image.load()
draw = ImageDraw.Draw(image)

maxIteration = 10000000 # number of iterations

## IFS definition of Levy Dragon
#fracname = "LevyCDragon"
#mat =   [[0.5,  -0.5,   0.5,    0.5,    0.0,    0.0,    0.5], # S1
#         [0.5,  0.5,    -0.5,   0.5,    0.5,    0.5,    0.5]] #S2

## IFS definition of Sierpinski Gasket
#fracname = "SierpinskiGasket"
#mat=[[0.5, 0.0,    0.0,    0.5,    0.0,    0.0,    1/3], # S1
#     [0.5, 0.0,    0.0,    0.5,    0.25,   0.5,    1/3], #S2
#     [0.5, 0.0,    0.0,    0.5,    0.5,    0.0,    1/3]] #S3

## IFS definition of Dragon Curve
fracname = "LevyDragon"
mat=[[0.5, -0.5,    0.5,    0.5,    0.0,    0.0,    0.5], # S1
     [-0.5, -0.5,    0.5,    -0.5,    1.0,   0.0,    0.5]] #S2

# calculates the number of similarities in the IFS
m = len(mat)
#print "m is: ", m

# fills lists of appropriate length with 0s
x = [0] * (maxIteration + 1)
y = [0] * (maxIteration + 1)

# picks a random point to begin
dx = random.randint(0, imgx)
dy = random.randint(0, imgy)
x[0] = dx*4.0/imgx -2
y[0] = dy*4.0/imgy -2
ymin = imgy/2
ymax = imgy/2
xmax = imgx/2
xmin = imgx/2
pix[((x[0]+2)*imgx)/4,imgy -((y[0]+2)*imgy)/4] = (0,0,0)
print "x[0],y[0] is: [", x[0], y[0], "]"

for i in range(1, maxIteration):
    # picks a similarity at random
    r=random.randint(0,m-1)
    #print "r is: ", r
    x[i] = x[i-1] * mat[r][0] + y[i-1] * mat[r][1] + mat[r][4]#*imgx
    #print "x[i] is: ", x[i]
    y[i] = x[i-1] * mat[r][2] + y[i-1] * mat[r][3] + mat[r][5]#*imgy
    #print "y[i] is: ", y[i]
    # fills the corresponding pixel black
    #print "x[",i,"]", "final ","y[",i,"] is: ", x[i], y[i]
    #print "adjusted x[i], y[i] is: ", ((x[i]+2)*imgx)/4, imgy -((y[i]+2)*imgy)/4
    if ((x[i]+2)*imgx)/4 <= imgx and ((x[i]+2)*imgx)/4 >=0 and imgy -((y[i]+2)*imgy)/4<=imgy and imgy -((y[i]+2)*imgy)/4 >=0:
        if imgy -((y[i]+2)*imgy)/4 < ymin:
            ymin = int(imgy -((y[i]+2)*imgy)/4)
        if imgy -((y[i]+2)*imgy)/4 > ymax:
            ymax = int(imgy -((y[i]+2)*imgy)/4)
        if ((x[i]+2)*imgx)/4 > xmax:
            xmax = int(((x[i]+2)*imgx)/4)
        if ((x[i]+2)*imgx)/4 < xmin:
            xmin = int(((x[i]+2)*imgx)/4)
        if r == 0:
            pix[((x[i]+2)*imgx)/4, imgy -((y[i]+2)*imgy)/4] = (255,0,0)
        elif r == 1:
            pix[((x[i]+2)*imgx)/4, imgy -((y[i]+2)*imgy)/4] = (0,0,255)
        elif r == 2:
            pix[((x[i]+2)*imgx)/4, imgy -((y[i]+2)*imgy)/4] = (0,255,0)
        
        #print x[i], y[i]
    #image.save(fracname + str(maxIteration) + "iterations.png", "PNG")

    # draws lines between points at each iteration
    #if i >=1:
       #draw.line([(dx[i-1], dy[i-1]), (dx[i], dy[i])], 0)
box = (xmin,ymin,xmax,ymax)
croppedimage = image.crop(box)
croppedimage.save(fracname + str(maxIteration) + "iterations.png", "PNG")
