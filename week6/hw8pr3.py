import math
import random


def throwDart():

    '''x*y is a square
    throw in square but outside of circle return False.
    throw in square and inside of the circle return True'''
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2+ y**2 <=1:
        return True
    return False

def forPi(n):

    ''' The number of darts thrown so far.
        The number of darts thrown so far that have hit the circle.
        The resulting estimate of π.'''

    count = 0

    for i in range(1,n+1):
        if throwDart() == True:
            count+=1
        print(count,'hits out of', i, 'throws so that pi is', (count/i)*4.0)

    return (count/n)*4.0


def whilePi(error):
    '''The number of darts thrown so far.
        The number of darts thrown so far that have hit the circle.
        stop the function when the error is within the π+error or π-error '''

    m=math.pi
    n=-99976
    throws = 0
    hits = 0

    while True:

        if  m-error < n < m+(error):
            break
        else:
            throws += 1
            if throwDart() == True:
                hits += 1
            n = hits*4/throws
            print(hits, 'hits out of', throws, 'throws so that pi is', n)