# CS5 Gold, Lab1 part 2
# Filename: hw1pr2.py
# Name:
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x


def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x


def sq(x):
    # square the number
    return x**2


def interp(low, hi, fraction):
    # return the fraction between low and hi
    return (hi-low)*fraction+low

def checkends(s):
    #check if the first letter match the last letter
    if s[0] == s[len(s)-1] or s[0] == ' ':
        return True
    else:
        return False

def flipside(s):
    """put your docstring here
        """
    #flip the word
    x = len(s) // 2
    return s[x:]+s[:x]


def convertFromSeconds(s):
    #input the second and output the day/hour/min/sec
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    s = s % 60
    seconds = s
    return [days, hours, minutes, seconds]