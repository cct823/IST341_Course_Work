import pandas as pd
from calendar import monthrange
from datetime import date,datetime
from countlate import *

now = datetime.now()
Year = now.year
Month = now.month - 1  # counting previous month
Days = monthrange(now.year,now.month)[1]


def findseason():
    '''Light season: March - September '''
    if Month >=4 and Month <=9:
        return 'lightseason'
    return 'busyseason'


def bonus_dict(day,revenue):

    revenue = int(revenue)
    season = findseason()
    weekday = [1,2,3,4,5]
    weekend = [6,7]

    if season == 'lightseason':
        if day in weekday:
            if 55000 <= revenue < 60000:
                return 100
            elif 60000 <= revenue < 65000:
                return 150
            elif 65000 <= revenue < 70000:
                return 200
            elif 70000 <= revenue < 75000:
                return 250
            elif 75000 <= revenue < 80000:
                return 300
            elif 80000 <= revenue < 85000:
                return 350
            elif 85000 <= revenue < 90000:
                return 400
            elif revenue >= 90000:
                return 450
            else:
                return 0

        elif day in weekend:
            if 60000 <= revenue < 65000:
                return 100
            elif 65000 <= revenue < 70000:
                return 150
            elif 70000 <=revenue < 75000:
                return 200
            elif 75000 <= revenue < 80000:
                return 250
            elif 80000 <= revenue < 85000:
                return 300
            elif 85000 <=  revenue < 90000:
                return 350
            elif revenue >= 90000:
                return 400
            else:
                return 0

    elif season == 'busyseason':
        if day in weekday:
            if 60000 <= revenue < 65000:
                return 100
            elif 65000 <= revenue < 70000:
                return 150
            elif 70000 <= revenue < 75000:
                return 200
            elif 75000 <= revenue < 80000:
                return 250
            elif 80000 <= revenue < 85000:
                return 300
            elif 85000 <= revenue < 90000:
                return 350
            elif revenue >= 90000:
                return 400
            else:
                return 0

        elif day in weekend:
            if 65000 <= revenue < 70000:
                return 100
            elif 70000 <= revenue < 75000:
                return 150
            elif 75000 <= revenue < 80000:
                return 200
            elif 80000 <= revenue < 85000:
                return 250
            elif 85000 <= revenue < 90000:
                return 300
            elif revenue >= 90000:
                return 350
            else:
                return 0


def count_daily_bonus(x):

    '''use daily revenue and weekday to find out if that day has the bonus.'''

    # get the daily revenue

    file = correct_year(Year) + '.' + correct_month(Month) # 108.03

    if x == 'shifu':
        df = pd.read_excel(file + '二店帳務.xlsx', sheet_name='總表')
    elif x =='yanji':
        df = pd.read_excel(file + '一店帳務.xlsx', sheet_name='總表')

    dailyincome = list(df['營收總和'][1:32])
    weekdaylist = []

    # generate a weekday list on that month
    weekdaystart = date(Year, Month, 1).isoweekday
    daystart = weekdaystart()
    newdaystart = int(daystart)

    for i in range(newdaystart,len(dailyincome)+newdaystart):
        weekday = i%7
        if weekday == 0:
            weekdaylist.append(7)
        else:
            weekdaylist.append(weekday)

    # get the bonus list
    bonuslist = []
    for i in range(len(dailyincome)):
        bonus = bonus_dict(weekdaylist[i],dailyincome[i])
        bonuslist.append(bonus)

    return bonuslist


def employee_bonus(x):

    work_dic = work_time(x)
    FT = find_FTPT(x, 'FT')
    bonuslist =count_daily_bonus(x)

    bonus_dic = {}
    # loop through the employee name in branch, if he is working, add the bonus.
    for name in FT:
        bonus = 0

        for i in range(len(bonuslist)):
            if len(work_dic[name][i]) == 2:
                bonus += bonuslist[i]
            bonus_dic[name] = bonus
    return bonus_dic


b = employee_bonus('shifu')
a = employee_bonus('yanji')
# b = count_daily_bonus()
# c = work_dic = work_time('shifu')
'''from countbonus import *
from countlate import *

# p1 = PT_workhours('yanji')
# p2 = PT_workhours('shifu')
# # print(p1)
# print(p2)

d3= ontime_bonus('shifu')
b = employee_bonus('shifu')
print(d3)
print(b)'''