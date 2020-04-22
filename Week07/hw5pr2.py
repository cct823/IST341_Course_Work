import csv
import pandas as pd


def open_csv( filename="rps.csv" ):
   """ opens the file with name filename
         by default:  it looks for "rps.csv"
       reads all of the csv data and assembles it into
       a list-of-lists and then returns that...
       (Here, it uses the variable name LoL.
        Remember you can use any variable name!)
   """
   f = open(filename, newline='')
   reader = csv.reader(f)

   LoL = []
   for row in reader:
       LoL.append( row )
   # print("LoL is", LoL)
   f.close()

   return LoL


if True:
    """ run functions/code here... """
    LoL = open_csv()  # uses the default filename
    human = 0

    '''I assume program generate string will have rr, pp, ss each over 20 times, 
    so the overall will go over 60'''


    for i in range(len(LoL)):
        count = LoL[i][2].count('rr') + LoL[i][2].count('pp') + LoL[i][2].count('ss')

        if count >=69:
            LoL[i] = LoL[i][:2] + ['machine-generated'] + LoL[i][2:]
            #print("Label", i, 'is create by program')
        else:
            LoL[i] = LoL[i][:2] + ['human-generated'] + LoL[i][2:]
            #print("Label", i, 'is create by human')
            human += 1


df = pd.DataFrame(data=LoL)
print(df)
# print(human)
df.to_csv('result.csv')


def batch_rps(user,comp):

    if len(user) == 0:
        return ''

    for k in range(len(user)):
        if user[0] == 'r':
            if comp[0] == 'r':
                return 'ties,' + batch_rps(user[1:],comp[1:])
            elif comp[0] == 's':
                return 'rps1 wins,' + batch_rps(user[1:],comp[1:])
            else:
                return 'rps2 wins,' +batch_rps(user[1:],comp[1:])
        elif user[0] == 'p':
            if comp[0] == 'r':
                return'rps1 wins,'+ batch_rps(user[1:],comp[1:])
            elif comp[0] == 's':
                return 'rps2 wins,' +batch_rps(user[1:],comp[1:])
            else:
                return 'ties,' + batch_rps(user[1:],comp[1:])
        elif user[0] == 's':
            if comp[0] == 'r':
                return 'rps2 wins,'+  batch_rps(user[1:],comp[1:])
            elif comp[0] == 's':
                return 'ties,' + batch_rps(user[1:],comp[1:])
            else:
                return 'rps1 wins,' + batch_rps(user[1:],comp[1:])

batchlist = []
for j in range(len(LoL)):
    batchlist.append(LoL[j][3])

L = []
user = []
comp = []
while True:
    a = input('Do you want to see the result of any two string? Please enter [yes/no]: ')
    if a == 'yes':
        rps1 = int(input('Please choose first batch, from number 1~64: '))
        rps2 = int(input('Please choose second batch, from number 1~64: '))
        user = batchlist[rps1 - 1]
        comp = batchlist[rps2 - 1]
        result = batch_rps(user, comp)
        L += [result]

        '''if i type no at first, the program will generate error message, how do i prevent that?'''
        '''Except using try/except, how should i prevent it?, right now it will only show the second result'''

        L = L[0].split(',')
        L = L[0:300]
        user = list(user)
        comp = list(comp)
        match = []
        for i in range(1, len(user) + 1):
            match.append('Game' + str(i))

        game = {'Match': match, 'rps1': user, 'rps2': comp, 'result': L}

        g = pd.DataFrame(data=game)
        print(g)
    else:
        break










