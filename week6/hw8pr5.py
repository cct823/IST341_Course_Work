

def printRect(width,height,symbol):

    for i in range(height):
        for j in range(width):
            print(symbol+' ', end = '')
        print()



def printTriangle(width,symbol,rightsideup):

    if rightsideup == True:
        for i in range(1,width+1):
            print((symbol+ ' ')*i)
    if rightsideup == False:
        for j in range(width,0,-1):
            print((symbol + ' ') * j)


def printBumps(num, symbol1, symbol2):

    for i in range(1,num+1):
        printTriangle(i,symbol1,True)
        printTriangle(i,symbol2, False)


def printDiamond(width, symbol) :

    for i in range (1,width+1):
        print(' '*(width-i)+(symbol+' ')*i)
    for j in range (width-1,0,-1):
        print(' ' * (width - j) + (symbol + ' ') * j)


def printStripedDiamond(width, sym1, sym2):

    s = (' ' +sym1 + ' ' + sym2)*100

    for i in range(1,width*2,2):
        print(' '*(width-i//2), end = '')
        print(s[:i+1])

    for j in range ((width-1)*2,0,-2):
        print(' ' * (width - j // 2+2), end='')
        p = (s[:j])
        print(p[::-1])



def printCrazyStripedDiamond(width, sym1, sym2, sym1Width, sym2Width):

    s = ((sym1+' ')*sym1Width + (sym2+' ')*sym2Width)*100

    for i in range(1, width * 2, 2):
        print(' ' * (width - i // 2), end='')
        print(s[:i + 1])

    for j in range((width - 1) * 2, 0, -2):
        print(' ' * (width - j // 2), end='')
        p = (s[2:j+2])
        print(p[::-1])
