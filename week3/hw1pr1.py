# CS5 Gold, hw1pr1
# Filename: hw1pr1.py
# Name:
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]
print('Answer0:',answer0)
answer1= e[1:]
print('Answer1:',answer1)
answer2=pi[-1::-2]
print('Answer2:',answer2)
answer3=pi[1:]
print('Answer3:',answer3)
answer4=e[-1::-2]+pi[0:5:2]
print('Answer4:',answer4)

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

answer5 = h[0]+h[4:]
print('Answer5:',answer5)
answer6= c[:4]+m[1:3]+c[6]
print('Answer6:',answer6)
answer7=h[1:]+m[1:]
print('Answer7:',answer7)
answer8=h[0:3]+m[3]+c[6]+h[0:3]*3
print('Answer8:',answer8)
answer9=c[3:5]+c[-2::-4]+m[0]+h[-1:-3:-1]+c[-2::-4]
print('Answer9:',answer9)
answer10=c[0]+c[3:5]+h[1:3]+c[0]+h[1]+c[2:4]
print('Answer10:',answer10)
