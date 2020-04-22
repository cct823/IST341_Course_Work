# coding: utf-8
#
# hw1pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon (rock/paper/scissor):")
    comp = random.choice(['rock','paper','scissor'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user =='rock':
        if comp=='rock':
            print('Hey it\'s a Tie')
        elif comp=='scissor':
            print('w0w! You Win')
        else:
            print('>________<  You Lose')
    elif user =='scissor':
        if comp=='rock':
            print('>________<  You Lose')
        elif comp=='scissor':
            print('Hey it\'s a Tie')
        else:
            print('w0w! You Win')
    else:
        if comp=='paper':
            print('Hey it\'s a Tie')
        elif comp=='rock':
            print('w0w! You Win')
        else:
            print('>________<  You Lose')





    #print("Better luck next time...")
