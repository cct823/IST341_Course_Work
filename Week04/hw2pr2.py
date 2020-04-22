# CS5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name:
# Problem description: Sleepwalking student

import random
import sys
import time
sys.setrecursionlimit(50000)
#count = 0
sdelay= 0.1

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    '''give a start point and how many steps need to move
        return the final position after the program finished.
    '''

    '''print the start position'''
    print('start is:', start)
    '''if finish the step, return the start position, else + the random step and nstep-1'''
    if nsteps == 0:
        #print('start is2:', start)
        return start
    else:
        #print('start is:', start)
        #nsteps = nsteps - 1
        #start = start + rs()
        return rwpos(start+rs(), nsteps-1)
        #return start


def rwsteps(start, low, high):
    '''print the start position with the walls, when hits the wall, stop return 0
    else, return the recursive function and +1 step for counting how many steps later.'''
    print('Class|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Dorm')
    time.sleep((sdelay))
    if start == low or start == high:
        return 0
    else:
        return 1 + rwsteps(start + rs(), low, high)

a = rwsteps(20,5,40)
print(a)
'''
original code written before using fucntion

global count
    if start == low+1:
        print('|' + 'S' + ' ' * (high - start) + ' |')
        #print(start, low, high)
        #print('the student hits the low wall')
        print(count)
    elif start == high-1:
        print('|' + ' ' * (start - low) + 'S'+' |')
        #print(start, low, high)
        #print('the student hits the high wall')
        print(count)
    else:
        print('|'+' '*(start-low)+'S'+' '*(high-start)+'|')
        start = start + rs()
        count = count +1
        #print(start, low, high)
        # rwsteps(start, low, high)

    '''

