#
# hw9pr1.py - Game of Life lab
#
# Name:
#

import random

def createOneRow(w):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(w):
        row += [0]
    return row


def createBoard(w, h):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(h):
        A += [createOneRow(w)]       # use the above function so that SOMETHING is one row!!
    return A


def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:               # row is the whole row
        for col in row:         # col is the individual element
            print(col, end='')  # print that element
        print()


def diagonalize(w, h):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A


def innerCells(w, h):
    '''create a board that has all live cells'''
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if  0 < row < h-1 and 0 < col < w-1:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def randomCells(w, h):
    '''generate live cells randomly in the board.'''
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0,1])

    return A

def copy(A):
    '''copy the board to another '''
    w = len(A)
    h = len(A[0])

    B = createBoard(w,h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            B[row][col] = A[row][col]

    return B


def innerReverse(A):
    ''' swap the inner cells
    if the inner cell is 0 -> 1 , if it is 1 -> 0
    '''

    w = len(A)
    h = len(A[0])

    B = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if A[row][col] ==0:
                B[row][col] = 1
            else:
                B[row][col] = 0
    return B


def countNeighbors(row, col, A):
    '''count how many live neighbors are there around the cells.'''

    count = 0
    '''start from [row,col], count the 8 digit around and sum '''

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            count += A[r][c]

    return count-A[row][col]  # so need to deduct here




# if A[row-1][col-1] == 1:
#     count +=1
# if A[row-1][col] == 1
#     count += 1
# if A[row-1][col+1] == 1:
#     count += 1
# if A[row][col-1] == 1:
#     count += 1
# if A[row][col+1] == 1:
#     count += 1
# if A[row+1][col-1] == 1:
#     count += 1
# if A[row+1][col] == 1:
#     count += 1
# if A[row+1][col+1] == 1:
#     count += 1

    #return count



def next_life_generation(A):
    ''' this program will run through all the cells and find out if it should generate a new live. '''

    w = len(A)
    h = len(A[0])

    B = copy(A)



    for row in range(1, h - 1):
        for col in range(1, w - 1):
            #if 0 < row < h - 1 and 0 < col < w - 1:
            countlive = countNeighbors(row, col, A)

            if countlive < 2 or countlive > 3:
                B[row][col] = 0
            elif countlive == 3:
                B[row][col] = 1
            else:
                B[row][col] = A[row][col]

    return B


#A = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]  # vertical bar






