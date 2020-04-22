
def rot (c, n):
    if 'a' <= c <= 'z':
        c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    if 'A' <= c <= 'Z':
        c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    return c

def list_to_str(L):
    """L must be a list of characters;
       this function returns a single string made from them.
    """
    if len(L) == 0:
        return ''
    return L[0] + list_to_str(L[1:])


# assert list_to_str(['c', 's', '5', '!']) == 'cs5!'

def encipher (S, n):

    return list_to_str([rot(c, n) for c in S])

#print(encipher('xyza', 1))

def letProb( c ):
    """ if c is the space character or an alphabetic character,
        we return its monogram probability (for english),
        otherwise we return 1.0 We ignore capitalization.
        Adapted from
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

def toString(S):
    """
    Converts to String
    """
    if len(S) == 0:
        return ""
    return S[0] + toString(S[1:])


def decipher(S):
    if (len(S) == 0):
        return ""
    LoL = [x for x in [encipher(S, y) for y in range(26)]]  # list of lists
    minDiff = 1 << 30
    index = 0
    for x in range(len(LoL)):
        freq = [0] * 26
        for y in LoL[x]:
            if 'a' <= y <= 'z':
                freq[ord(y) - ord('a')] += 1.0
            elif 'A' <= y <= 'Z':
                freq[ord(y) - ord('A')] += 1.0
        currDiff = 0
        for y in range(26):
            currDiff += abs(freq[y] / len(LoL[x]) - letProb(chr(y + ord('a')))) ** 3
        # print currDiff, " ", toString(LoL[x])
        if currDiff < minDiff:
            minDiff = currDiff
            index = x
        # print(LoL[x])
    return toString(LoL[index])

def blsort(L):
    '''
    Design and write a function named blsort(L),
    which will accept a list L and should return a list with the same elements as L,
    but in ascending order.
    '''
    count = 0
    for i in L:
        if i == 0:
            count +=1
    print(count)
    LC = [0 if count >j else 1 for j in range(len(L))]
    return LC


def gensort(L):
    '''
    Use recursion to write a general-purpose sorting function gensort(L),
    which accepts a list L and returns a list with the same elements as L, but in ascending order
    '''
    for i in range(len(L)):
        for j in range(i+1,(len(L))):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    return L


def jscore(S,T):

    '''count how many letter are share in T'''
    count = 0
    listmax = []
    if len(T) == 0: #    if len(T) == 0: #
        return 0
    else:
        for i in S:
            if i in T:
               count+=1
    '''count the maximum letter appear in T
     if count > max letter means the letter count in S has appear more than T has
     so count = max letter in (T), else just return count'''
    for j in T:
        maxcount = T.count(j)
        listmax.append(maxcount)
    if count > max(listmax):
        count = max(listmax)

    return count


assert jscore('diner', 'syrup') == 1
assert jscore('geese', 'elate') == 2
assert jscore('gattaca', 'aggtccaggcgc') == 5
assert jscore('gattaca', '') == 0

'''three more questions to complete'''

def exact_change(target_amount, L):

    if target_amount < 0 :
        return False

    if target_amount == 0:
        return True

    if L == []:
        return False

    loseit = exact_change(target_amount, L[1:])

    useit = exact_change(target_amount-L[0], L[1:])

    if useit == True or loseit ==True:
        return True
    else:
        return False





def exact_changeorig(target_amount, L):
    '''provide a number and a string, then find out if the number is the conbination of the string.
        Each number can only use onece'''
    for i in range(len(L)):
        if target_amount >= L[0]:
            return exact_change(target_amount - L[0], L[1:])
        return exact_change(target_amount, L[1:])

    if target_amount == 0:
        return True
    else:
        return False
#exact_change(42, [25, 16, 2, 15]) this isn't working, can't skip 16


def LCS(S, T):
    '''this function accept two strings, S and T.
    LCS should return the longest common subsequence (LCS) that S and T share'''
    if len(S) ==0:
        return ''
    elif len(T) == 0:
        return ''
    elif S[0]==T[0]:
        return S[0] + LCS(S[1:],T[1:])

    else:
        r1 = LCS(S, T[1:])
        r2 = LCS(S[1:], T)
        if len(r1)>len(r2):
            return r1
        else:
            return r2


        # if len(T)>0:
        #     if S[0] in T:
        #         if S[0] == T[0]:
        #             return S[0] + LCS(S[1:],T[1:])
        #         else:
        #             return LCS(S,T[1:])
        #     else:
        #         return LCS(S[1:],T)
        # else:
        #     return ''

#LCS('gattaca', 'tacgaacta') this one is wrong
    #return

'''def make_change( target_amount, L ):
    for i in range(len(L)):
        if target_amount >= L[0]:
            return savelist(L[0]),exact_change(target_amount - L[0], L[1:])
        return exact_change(target_amount, L[1:])

    if target_amount == 0:
        return savelist()
    else:
        return False

def savelist(x):
    k = []
    k.append(x)
    return k

'''



