'''Personal paint'''

import time
from turtle import *
from random import *

def flakeside(sidelength, levels):
    if levels > 0:
        for t in [60, 120, 60, 0]:
            flakeside(sidelength/2,levels-1)
            left(t)
    else:
        forward(sidelength)