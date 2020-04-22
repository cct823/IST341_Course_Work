#
# hw6pr5.py - Intro to loops!
#
# Name:
#
import random


def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
assert fac(0) == 1
assert fac(5) == 120


def power(b,p):

    result = 1
    if p ==0:
        return 1
    else:
        for i in range(p):
            result = result*b
    return result

def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42


def summedOdds(L):

    result = 0
    for i in L:
        if i%2==1:
            result = result +i
    return result

def untilARepeat(high):
    L = []
    guess = random.choice(range(0, high + 1))
    L.append(guess)
    count = 1
    while True:
        guess = random.choice (range(0,high+1))
        if guess in L:
            L.append(guess)
            count+=1
            #print(L)
            #print('repeated number = ', guess)
            break
        else:
            L.append(guess)
            count +=1
    return count


'''
def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses

def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!
'''








