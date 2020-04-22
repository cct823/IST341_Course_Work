# CS 5 Gold, hw3pr3
# filename: hw3pr3.py
# Name:
# problem description: List comprehensions



# this gives us functions like sin and cos...




# two more functions (not in the math library above)

from math import *
import math

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    #return [x//2 for x in range(N)]
    return [float(x//2) for x in range(N)]


def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    '''input a number and divided into N elements'''
    return [x/N for x in range(N)]

def scaledfracs(low,high,N):
    '''from the distance between low to high, divide into unitfracs and add to the low.
        N is how many elements in the loop.
    '''

    return [(high-low)*x + low for x in unitfracs(N)]

def sqfracs(low,high,N):
    '''from low to high, get the square of each number. N is how many elements in the loop.'''

    return [ x**2 for x in scaledfracs(low,high,N)]

def f_of_fracs (f, low, high, N):
    """ Returns a list of N left endpoints uniformly through
        the interval of [lo, hi) that has function f applied
        to it
    """
    return [f(x) for x in scaledfracs(low, high, N)];


def integrate(f, low, high, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """
    return sum(f_of_fracs(f,low,high,N))*(high-low)/N

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

'''
Responses:

Q1. 
For the function we use here is providing infinity rectangles to fit it. 
However, y=2x can never fit with many rectangles perfectly 
because it is not rectangle. That's why the result is close to 100 but not 100.

Q2:
The function is a quarter circle, so the area is PI (2*2*PI/4 = PI) 
So, now the function use rectangle to fulfill the quarter circle. 
When N goes to infinity, it converge to pi.
It's cut the circular into small pieces.
Just what the function do above, when it get more close to infinity, it will close to 
3.1415936531737585 (N=2000000) which is the number of pi.
'''



