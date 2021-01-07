# mandelbrot.py
# Lab 9
#
# Name: Avaneesh Kolluri

# keep this import line...
from cs5png import PNGImage
from cs5png import *

# start your Lab 9 functions here:

def mult(c,n):
    a = 0
    result = 0
    for a in range(n):
        result = c + result
    return result

def update(c,n):
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z)>2:
            return False
    return True

def weWantThisPixel(col, row):
    if col%10 == 0 and row%10 == 0:
        return True
    return False

"""The and gate allows it to be spaced out 10px both vertically/
    and horizontally, while or will only guarantee one of them."""

def test():
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    image.saveFile()    

def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in pix, the CURRENT pixel column (or row)/
        pixMax, the total # of pixel columns floatMin, the min floating-point value/
        floatMax, the max floating-point value scale returns the floating-point value that/
        corresponds to pix"""
    x = pix/pixMax
    return floatMin + x*(floatMax - floatMin)

def mset():
    """creates a 300x200 image of the madlebrot set"""
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            x = scale(col,width,-2.0,1.0)
            y = scale(row,height,-1.0,1.0)
            c = x+y*1j
            n=25
            if inMSet( c, n ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()


    





    
            
        
