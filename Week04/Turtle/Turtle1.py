#
# hw3pr1.py
#
# Name:
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *


def tri(n):
    shape('turtle') 
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        clr = choice(['darkgreen', 'red', 'blue'])
        #random.color(clr) 
        width(2*n+1)
        forward(100)
        left(120)
        tri(n-1)    # Recur to draw the rest of the sides!
        
def spiral(initialLength, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
  
    shape('turtle')
    if initialLength <= 1:
        return      # No more to draw, so stop this call to spiral
    else:
        forward(initialLength)# You will want a call to forward here...
        left(angle)# You will want a turn here...
        # You will want to recur here! That is, make a new call to spiral...
        spiral(initialLength*multiplier, angle, multiplier) 
        
                      
def chai(size):
    """Our chai function!"""
    if (size < 5): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        forward(trunklength)
        pos = position()
        hdg = heading()
        left(35)
        svtree(trunklength/2, levels-1)
        setposition(pos)
        setheading(hdg)
        right(35)
        svtree(trunklength/2, levels-1)
        setposition(pos)
        setheading(hdg)
        backward(trunklength)


    

def flakeside(sidelength, levels):
    shape('turtle')
    if levels > 0:
        for t in [-60, 120, -60, 0]:
            flakeside(sidelength/2,levels-1)
            left(t)
    else:
        forward(sidelength)

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)






        
