# Sierpinski Gasket Random Iteration Algorithm
import math
import random
from PIL import Image
from PIL import ImageDraw

## Image Properties
imgx = 600; imgy = 600 # dimensions of canvas
image = Image.new("RGB", (imgx, imgy), (255,255,255)) # greyscale image white canvas
pix = image.load()
draw = ImageDraw.Draw(image)

maxIteration = 2500 # number of iterations

## IFS definition of Sierpinski Gasket
mat=[[0.5,0.0,0.0,0.5,0,0,1/3], # S1
     [0.5,0.0,0.0,0.5,0.25,0.5,1/3], #S2
     [0.5,0.0,0.0,0.5,0.5,0.0,1/3]] #S3

# calculates the number of similarities in the IFS
m = len(mat)

# picks a random point to begin
x0=random.randint(0, imgx)
y0=random.randint(0, imgy)
##print x0
##print y0

# fills lists of appropriate length with 0s
x = [0] * (maxIteration + 1)
y = [0] * (maxIteration + 1)
dx = [0] * (maxIteration + 1)
dy = [0] * (maxIteration + 1)
# sets counter
i=0
    
for i in range(maxIteration):
    # picks a similarity at random
    r=random.randint(0,m-1)
    # first iteration on a random point
    if i == 0:
        x[i] = x0 * mat[r][0] + y0 * mat[r][1] + mat[r][4]*imgx
        y[i] = x0 * mat[r][2] + y0 * mat[r][3] + mat[r][5]*imgy
    # subsequent iterations
    else:
        x[i] = x[i-1] * mat[r][0] + y[i-1] * mat[r][1] + mat[r][4]*imgx
        y[i] = x[i-1] * mat[r][2] + y[i-1] * mat[r][3] + mat[r][5]*imgy
    # flips the image horizontally and vertically
    dx[i] = imgx-x[i] 
    dy[i] = imgx-y[i]
    # fills the corresponding pixel black
    pix[dx[i], dy[i]] = (255,0,0)

    # draws lines between points at each iteration
    #if i >=1:
       #draw.line([(dx[i-1], dy[i-1]), (dx[i], dy[i])], 0)

image.save("SierpinskiGasket" + str(maxIteration) + "iterations.png", "PNG")
