# CS5 Gold, hw1pr3
# Filename: hw1pr3.py
# Name:
# Problem description: Function Frenzy!

#
# leng example from class
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n,m):
    '''input two numbers and return the multiply of two numbers'''
    if m==0:
        return 0
    elif m<0:
        return -n+mult(n,m+1)
    else:
        return n+mult(n,m-1)

#
# Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0

def dot(L,K):
    '''calculate the result by list*list and sum it'''
    if len(L) != len(K):
        return 0
    elif len(L) == 0:
        return 0
    else:
        return L[0]*K[0]+dot(L[1:], K[1:]) #after remove the first object in the list, input start from 1: to the end


def ind(e,L):
    '''find the input number and return the index, assisted by professor, comments below.'''
    if e in L:
        if e == L[0]:
            return 0  #original I put e, but it should return index 0
        else:
            return 1 + ind(e,L[1:]) # because I remove index 0, so it should return 1+ function, which will go
                                    # recursively to add the index.
    else:
        return(len(L))

assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5


def letterScore(let):
    '''each letter represent a number, input a letter and return a number'''
    if let in 'aeilnorstu':
        return 1
    elif let in 'dg':
        return 2
    elif let in 'bcp':
        return 3
    elif let in 'fhvwy':
        return 4
    elif let in 'k':
        return 5
    elif let in 'jx':
        return 8
    elif let in 'qz':
        return 10
    else:
        return 0


assert letterScore('a') == 1
assert letterScore('z') == 10
assert letterScore('h') == 4
assert letterScore('*') == 0


def scrabbleScore(S):
    '''input a string and calculate the total number'''
    if len(S) == 0:
        return 0
    else:
        if S[0] in 'aeilnorstu':
            return 1 + scrabbleScore(S[1:])
        elif S[0] in 'dg':
            return 2 + scrabbleScore(S[1:])
        elif S[0] in 'bcpm':
            return 3 + scrabbleScore(S[1:])
        elif S[0] in 'fhvwy':
            return 4 + scrabbleScore(S[1:])
        elif S[0] in 'k':
            return 5 + scrabbleScore(S[1:])
        elif S[0] in 'jx':
            return 8 + scrabbleScore(S[1:])
        elif S[0] in 'qz':
            return 10 + scrabbleScore(S[1:])
        else:
            return 0 + scrabbleScore(S[1:])

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0


def one_dna_to_rna(c):
    '''set the rule for the next function.'''
    """Converts a single-character c from DNA
       nucleotide to complementary RNA nucleotide """
    if c == 'A':
        return 'U'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    elif c == 'T':
        return 'A'
    else:
        return ''

def transcribe(S):
    '''  input a string, enter first letter to upper function and the return the rest until nothing
     when nothing, return '' (no space)'''
    if len(S)==0:
        return ''
    return one_dna_to_rna(S[0]) + transcribe(S[1:])

#
# I finished all of the CodingBat STRING problems.
#
#
# I finished all of the CodingBat LIST problems.
#

def pigletLatin(s):
    '''check if the first letter is vowel, and return different result based on the string.'''
    if s[0] in 'aeiou':
        return s+'way'
    return s[1]+s[0]+'ay'


def pigLatin(s):
    ''' check first letter if it's vowel or 'y'''
    if s[0] in 'aeiou':
        return pigletLatin(s)
    elif s[0]=='y' and s[1] in 'aeiou':
        return s[1:]+s[0]+'ay'
    elif s[0] == 'y' and s[1] not in 'aeiou':
        return s+'way'
    return initial_consonants(s) # go to next function if none of above

def initial_consonants(s):
    '''find the vowel and slice the string, and return the organized string'''
    for i in range(len(s)):
        if s[i] not in 'aeiou':
            continue #skip until find vowel
        return s[i:]+s[:i]+'ay' #print reverse +'ay



