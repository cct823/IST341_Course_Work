
from calendar import monthrange
import datetime
import pandas as pd

now = datetime.datetime.now()
Month = now.month
Days = monthrange(now.year,now.month)[1]


def daily_revenue():
    return

def findseason():
    '''Light season: March - September '''
    if Month >=4 and Month <=9:
        return 'lightseason'
    return 'busyseason'

def shiftdays():
    '''if the first day of the month is not start from Monday, shift the index'''
    weekdaystart = int(input('Please input weekday start from: '))
    shiftday = 0

    if weekdaystart == 2:
        shiftday = 1
    elif weekdaystart == 3:
        shiftday = 2
    elif weekdaystart == 4:
        shiftday = 3
    elif weekdaystart == 5:
        shiftday = 4
    elif weekdaystart == 6:
        shiftday = 5
    elif weekdaystart == 7:
        shiftday = 6

    return shiftday

def season_daily_bonus():


    shiftday = shiftdays()
    season = findseason()

    df = pd.read_excel('108.03二店帳務.xlsx', sheetname='總表')
    dailyincome = list(df['營收總和'][1:32])
    print(dailyincome)
    bonus = 0
    weekday = []
    weekend = []

    '''distribute the weekday and weekend revenue'''
    for item in range(1,len(dailyincome)+1):
        if item % 7 == 6-shiftday or item % 7 == 7-shiftday:
            weekend.append(dailyincome[item-1])
        else:
            weekday.append(dailyincome[item-1])
    print('weekday: ',weekday)
    print('weekend:' ,weekend)
    print(season)
    '''the item has to be the range:'''
    if season == 'lightseason':
        for itema in weekday:
            if 55000 <= itema < 60000:
                bonus += 100
            elif 60000 <= itema < 65000:
                bonus += 150
            elif 65000 <= itema < 70000:
                bonus += 200
            elif 70000 <= itema < 75000:
                bonus += 250
            elif 75000 <= itema < 80000:
                bonus += 300
            elif 80000 <= itema < 85000:
                bonus += 350
            elif 85000 <= itema < 90000:
                bonus += 400
            elif itema >= 90000:
                bonus += 450

        for itemb in weekend:
            if 60000 <= itemb < 65000:
                bonus += 100
            elif 65000 <= itemb < 70000:
                bonus += 150
            elif 70000 <=itemb < 75000:
                bonus += 200
            elif 75000 <= itemb < 80000:
                bonus += 250
            elif 80000 <= itemb < 85000:
                bonus += 300
            elif 85000 <=  itemb < 90000:
                bonus += 350
            elif itemb >= 90000:
                bonus += 400

        return bonus

    elif season == 'busyseason':
        for itemc in weekday:
            if 60000 <= itemc < 65000:
                bonus += 100
            elif 65000 <= itemc < 70000:
                bonus += 150
            elif 70000 <= itemc < 75000:
                bonus += 200
            elif 75000 <= itemc < 80000:
                bonus += 250
            elif 80000 <= itemc < 85000:
                bonus += 300
            elif 85000 <= itemc < 90000:
                bonus += 350
            elif itemc >= 90000:
                bonus += 400

        for itemd in weekend:
            if 65000 <= itemd < 70000:
                bonus += 100
            elif 70000 <= itemd < 75000:
                bonus += 150
            elif 75000 <= itemd < 80000:
                bonus += 200
            elif 80000 <= itemd < 85000:
                bonus += 250
            elif 85000 <= itemd < 90000:
                bonus += 300
            elif itemd >= 90000:
                bonus += 350
        return bonus


bonus = season_daily_bonus()
print(bonus)


def FT_EmployeeInfo():
    id = int(input('please input employee id:'))
    #name = input('Please enter employee name: ')
    base = int(input('Please input employee base pay: '))
    Latetime = int(input('Please input late minutes: '))
    SickLeave = int(input('Please input sick leave day(s): '))
    Leave = float(input('Please input personal leave day(s):'))
    d = FullTime(id,base,Latetime,SickLeave,Leave)
    return d


def FullTime(id,base,Latetime,SickLeave,Leave):

    if SickLeave >= 1 :
        SickLeave = (base/Days)*SickLeave
    if Leave >= 0.5:
        Leave = (base/Days)/2 * Leave
    if Latetime <= 40:
        Latetime = 2000
    elif Latetime >= 40 and Latetime<60:
        Latetime = 0
    elif Latetime >=60:
        Latetime = -2000 + (Latetime-60)//5*(base/30/8/12)


    TotalSalary = base+Latetime-SickLeave-Leave
    Leave = SickLeave+Leave

    d = DataPrint(id,base,TotalSalary,Latetime,Leave)
    return d



def DataPrint(id,base,TotalSalary,Latetime,Leave):
    # global d
    d={}
    d[id] = {'EmployeeID': "%02d"%id, 'BasePay':base,'OnTimeBonus': Latetime,'LeavePenalty': -Leave,'Salary': TotalSalary}
    # print(d)
    # df = pd.DataFrame(data=d)
    # print(df)
    return d

def parttime():
    return p


L = []
while True:
    n = input('Please input: [FT/PT/exit]:')
    if n == 'FT':
        d = FT_EmployeeInfo()
        L += [d]
    elif n =='PT':
        p = parttime()
    elif n == 'exit':
        break
    else:
        continue

for i in range(len(L)):
   L[i] = L[i][i+1]

df = pd.DataFrame(data=L,columns=['EmployeeID','BasePay','LeavePenalty','OnTimeBonus','Salary'])

print(df)




