# Sierpinski Gasket Deterministic Algorithm
import math
from PIL import Image

## Image Properties
imgx = 600; imgy = 600 # dimensions of canvas
picture = Image.open("image.png") # loads the chosen image file
image1 = picture.resize((imgx,imgy)) # resizes the image to the canvas dimensions
image1 = image1.convert("1") # converts the image to black and white
image2 = Image.new("L", (imgx, imgy), 255) # creates blank canvas
pix2 = image2.load() # loads pixels of blank canvas for editing

maxIteration = 2 # number of iterations

## IFS definition of Sierpinski Gasket
mat=[[0.5,0.0,0.0,0.5,0,0,1/3],         # S1
     [0.5,0.0,0.0,0.5,0.25,0.5,1/3],    # S2
     [0.5,0.0,0.0,0.5,0.5,0.0,1/3]]     # S3

# calculates the number of similarities in the IFS
m = len(mat)

# fills a list with 2 elements
S = [255,255]
# sets counter and values
i=0
    
for i in range(maxIteration):
    for j in range(imgx):
        for k in range(imgy):
            if image1.getpixel((j,k)) != 255: # scans image file to find filled pixels
                # applys all similarities to the filled pixel
                for l in range(m):
                    S[0] = j * mat[l][0] + k * mat[l][1] + mat[l][4]*imgx
                    S[1] = j * mat[l][2] + k * mat[l][3] + mat[l][5]*imgy
                    pix2[S[0], S[1]] = 0 # draws result of similarities on new canvas
    image1 = image2 # replaces previous image file with new iterated image
    image2 = Image.new("L", (imgx, imgy), 255) # loads new blank canvas
    pix2=image2.load() # loads pixels for editing from new canvas
    i += 1

image1 = image1.rotate(180)
image1.save("SierpinskiGasketImg.png", "PNG") # saves image file
