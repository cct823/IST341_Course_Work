import pandas as pd
import numpy as np
import datetime
import math
from datetime import datetime, timedelta
from calendar import monthrange
from datetime import date,datetime



now = datetime.now()
Year = now.year
Month = now.month - 1  # counting previous month
Days = monthrange(now.year,now.month)[1]



# countbonus file
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
            if len(work_dic[name][i]) == 2:  #get M0
                bonus += bonuslist[i]
            bonus_dic[name] = bonus
    return bonus_dic

# countlate file
#
## remove the float data when read from Pandas
#

def correct_month(Month):
    # file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'
    if 1 <= Month <= 9:
        return '0' + str(Month)
    return str(Month)


def correct_year(Year):
    return str(Year - 1911)


def isnan(x):
    '''if it's nan -> False, will be removed'''

    if type(x) != type(1.42):
        return True
    if math.isnan(x) == True:
        return False
    return True


def isfloat64(x):
    '''remove the nan in numpy array'''

    if isinstance(x, np.float64) == True:
        return False
    return True


#
#  separate the sheet to different files
#


def readfile():
    '''read the check in/out data downloaded from POS machine'''

    check_in_sheet = pd.read_excel('RPA020.xls', sheet_name='刷卡資料查詢')
    check_in_sheet = check_in_sheet.drop('部門', axis=1)  # 部門==刷卡地點 so drop one

    return check_in_sheet


'''could join two function by providing a enter (x) which x = Yanji or Shifu then return different values'''


def find_branches(x):
    '''find the correct work time for each branch'''

    pd.options.mode.chained_assignment = None  # turn off the warning for replace the data in part of the DF.

    '''
        The reason for the for loop below because the check out date is not the same day as the check in date.
        But, that is still the same shift. If the program just remove the duplicated based on [Name][Date][In/Out],
        the second row will be remove but that's not the one should be removed. 
        Hence, the for loop change the check out time if the first two digit is '00' -> set the [In/Out] to '隔夜下班',
        then remove the duplicates as usual. After removing the duplicates, change '隔夜下班' back to '下班'.
        That's the reason for the for loop existing. 

        0   002 鄭功宏	2019/03/18	002	21:28:38	上班
        1   002	鄭功宏	2019/03/19	002	00:01:59	下班
        2   002	鄭功宏	2019/03/19	002	21:32:16	上班
        3   002	鄭功宏	2019/03/19	002	22:38:46	下班

        However, changing the context in DataFrame will raise : 'SettingWithCopyWarning'
        pd.options.mode.chained_assignment = None this is the line to close it.
        If change to the original setting, Nono = Warn.
    '''

    if x == 'yanji':

        check_in_sheet = readfile()
        Yanji = check_in_sheet.loc[check_in_sheet['刷卡地點'] == 1]
        # Yanji = Yanji_1.loc[Yanji_1['燈號狀態'] == '上班']  # filter check in/out, only need check in

        # reason for loop, check doc string above.
        for i in range(len(Yanji['刷卡時間'])):
            if Yanji['刷卡時間'].iloc[i][:2] == '00':
                Yanji['燈號狀態'].iloc[i] = '隔夜下班'

        NewYanji = Yanji.drop_duplicates(subset=['員工姓名', '日期', '燈號狀態'], keep='first')

        for i in range(len(NewYanji['刷卡時間'])):
            if NewYanji['刷卡時間'].iloc[i][:2] == '00':
                NewYanji['燈號狀態'].iloc[i] = '下班'

        return NewYanji

    elif x == 'shifu':

        check_in_sheet = readfile()
        Shifu_1 = check_in_sheet.loc[check_in_sheet['刷卡地點'] == 2]
        # Shifu = Shifu_1.loc[Shifu_1['燈號狀態'] == '上班']  #filter check in/out, only need check in

        # reason for loop, check doc string above.
        for i in range(len(Shifu_1['刷卡時間'])):
            if Shifu_1['刷卡時間'].iloc[i][:2] == '00':
                Shifu_1['燈號狀態'].iloc[i] = '隔夜下班'

        NewShifu = Shifu_1.drop_duplicates(subset=['員工姓名', '日期', '燈號狀態'], keep='first')

        for i in range(len(NewShifu['刷卡時間'])):
            if NewShifu['刷卡時間'].iloc[i][:2] == '00':
                NewShifu['燈號狀態'].iloc[i] = '下班'

        ''' change the data back to normal so some of the data will have 2 check outs.'''

        return NewShifu

#
#  distribute the Part time or Full time employees
#


def find_FTPT(x, y):
    '''find the PT or FT employees'''

    file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'

    if x == 'yanji':
        file = pd.read_excel(file, sheet_name='延吉')
    elif x == 'shifu':
        file = pd.read_excel(file, sheet_name='市府')
    else:
        print('you have the wrong input')

    FT = []
    PT = []
    name = list(file.loc[:, '姓名'])
    type = list(file.loc[:, 'PT/FT'])

    if y == 'FT':
        for i in range(len(type)):
            if type[i] == 'FT':
                FT.append(name[i])
        return FT

    elif y == 'PT':
        for i in range(len(type)):
            if type[i] == 'PT':
                PT.append(name[i])
        return PT
    else:
        print('you have the wrong input')


def find_basepay(x):
    '''get the base pay for all employees'''

    file = '紅九九員工基本資料.xlsx'
    if x == 'yanji':
        file = pd.read_excel(file, sheet_name='延吉')
    elif x == 'shifu':
        file = pd.read_excel(file, sheet_name='市府')
    else:
        print('you have the wrong input')

    names = list(file.columns.values)

    '''late time is calculate base on base and two other bonus'''
    base = list(file.iloc[0, :])  # 底薪
    base_1 = list(file.iloc[1, :])  # 職務加給
    base_2 = list(file.iloc[2, :])  # 其他津貼（試用期滿）
    base_3 = list(file.iloc[3, :])  # 外語加給

    base_all = []

    for i in range(len(base)):
        sum_all = base[i] + base_1[i] + base_2[i] + base_3[i]
        base_all.append(sum_all)

    # print(base_all)

    # base_all

    base_dic = {}
    for name in range(len(names)):
        base_dic[names[name]] = base_all[name]

    # print(base_dic)

    return base_dic

#
## getting the work shift categories
#


def get_shift():
    '''there are sharing same time shift, so dont need to distribute the branches'''

    file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'

    shift = pd.read_excel(file)
    name = list(shift['班別'])  # .remove(float('nan'))
    time = list(shift['時段'])  # .remove(float('nan'))
    shift_name = [x for x in name if isnan(x)]  # if isok(x) == True
    shift_time = [x for x in time if isnan(x)]
    # print(shift_time)
    # print(shift_name)

    # shift_list = []
    shift_dic = {}
    for i in range(len(shift_name)):
        time = shift_time[i].split('-')
        shift_dic[shift_name[i]] = {'上班': time[0], '下班': time[1]}
        # shift_list.append(shift_dic)
    return shift_dic


#
## get the working time everyday.
#


def work_time(x):
    '''create the name and work time'''

    shift = ''
    file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'
    if x == 'yanji':
        shift = pd.read_excel(file, sheet_name='延吉')
    elif x == 'shifu':
        shift = pd.read_excel(file, sheet_name='市府')

    newshift = shift[shift.columns[:33]]
    name = newshift.iloc[:, 0]
    # print(name)
    work_dic = {}

    for i in range(len(name)):
        work_dic[name[i]] = list(newshift.iloc[i, 1:])

    for i in range(len(work_dic)):
        work_dic[name[i]] = [x for x in work_dic[name[i]] if isfloat64(x)]

    return work_dic


#
## count the late mins for check in
#


def FT_latemin(x):
    ''' count late for the Full time employee '''

    # select the data
    ''' 
        work_dic  : get the check in /out time 
        shift_dic : EX: {'M0': {'上班': '10:00', '下班': '20:00'}
        FT : get the Full Time employee names 
        check_in_record: get the check-in record for specific branch
    '''
    work_dic = work_time(x)
    shift_dic = get_shift()
    FT = find_FTPT(x, 'FT')
    check_in_record = find_branches(x)

    '''
        removing the checking record if the people is not Full time employee
        .values make it transfer to numpy array so i can get the each element
    '''
    FT_record = check_in_record[check_in_record.員工姓名.isin(FT)].values

    # start counting late time

    newrowlist = []

    for row in FT_record:
        # print(row)
        name = row[0]
        date = row[1]
        status = row[4]
        yr, month, day = date.split("/")

        '''
            day = int(day)  #make 01...09 to 1...9
            workshift : P0,M1 ...
            shifttime : get the exact hours for different time shift. ex: 10:00-18:00
            inouttime : get the check in/out time from dic {'上班':time,'下班':time}
            newrow    : add it to each row
        '''
        day = int(day)
        workshift = work_dic[name][day - 1]
        shifttime = shift_dic[workshift]
        inouttime = shifttime[status]
        newrow = np.append(row, inouttime)

        # compare the check in/out with actual check in out time
        check_in_actual = datetime.strptime(newrow[-3], '%H:%M:%S')  # actual check in/out time
        suppose_to_check = datetime.strptime(newrow[-1], '%H:%M')  # suppose to check in/out before ....

        # on duty
        if newrow[-2] == '上班':
            if check_in_actual < suppose_to_check:
                latetime = 0
                newrow = np.append(newrow, latetime)
                newrowlist.append(newrow)
                # print(newrow)
            else:
                latetime = check_in_actual - suppose_to_check
                if latetime < timedelta(minutes=1):
                    latemins = 0
                    newrow = np.append(newrow, latemins)
                    newrowlist.append(newrow)
                    # continue
                else:
                    latemins = latetime.seconds // 60
                    newrow = np.append(newrow, latemins)
                    newrowlist.append(newrow)
        else:
            # off duty, not necessary now, so set the early leave time to 0
            '''check out but still need to append an element, so append 0'''
            latetime = 0
            newrow = np.append(newrow, latetime)
            newrowlist.append(newrow)


    # sum the late time for each person.
    newrowlist = np.array(newrowlist)
    latetime_dic = {}

    for name in FT:
        sumtime = 0
        for rows in range(len(newrowlist)):
            if newrowlist[rows][0] == name:
                if newrowlist[rows][-1] > 300:
                    sumtime += 0
                else:
                    sumtime += newrowlist[rows][-1]
                latetime_dic[name] = sumtime
    return latetime_dic


def ontime_bonus(x):
    latemin_dic = FT_latemin(x)
    base_dic = find_basepay(x)
    FT = find_FTPT(x, 'FT')

    bonus_dic = {}

    for name in FT:
        latetime = latemin_dic[name]
        # print(latetime)
        base_all = base_dic[name]
        # print(base)

        if latetime <= 40:
            bonus = 2000
            bonus_dic[name] = bonus
        elif latetime >= 40 and latetime < 60:
            bonus = 0
            bonus_dic[name] = bonus
        elif latetime >= 60:
            bonus = (latetime - 60) * (base_all / 30 / 8 / 60) * -1
            bonus_up = math.floor(bonus)
            bonus_dic[name] = bonus_up
    return bonus_dic

def roundtime(dt, delta):
    return dt + (datetime.min - dt) % delta


import time

def PT_workhours(x):
    '''later has to add the PT shift dic, then replace the check in time to office work hour time.'''

    PT = find_FTPT(x, 'PT')
    # print(PT)
    check_in_record = find_branches(x)
    # shift_dic = get_shift()  #EX: 'PT': {'上班': '00:00', '下班': '00:00'}}
    # print(shift_dic)
    PT_record = check_in_record[check_in_record.員工姓名.isin(PT)].values
    # print(PT_record)
    # print(len(PT_record))

    # code to round to 30 min
    for rows in PT_record:
        # print(rows)
        time.sleep(0.1)
        if rows[-1] == '上班':
            '''Maybe need to filter out check in around 18:07, 18:37 send 7 minutes for free now'''
            # minus 15 to make sure 18:02:35 -> 18:00:00 not 18:30:00
            rows[-2] = datetime.strptime(rows[-2],'%H:%M:%S') - timedelta(minutes = 15)
            a = str(roundtime(rows[-2],timedelta(minutes=30)))
            b,c = a.split(' ')
            rows[-2] = c
    #     time.sleep(0.1)
    #     print(rows[-2])
    # time.sleep(0.1)
    # print(PT_record)


    newrowlist = []
    i = 0

    while i < len(PT_record):
        row = PT_record[i]
        row2 = PT_record[i + 1]
        '''
            1. if employee miss check in or check out, there will be a issue
            so missing any of check in or out, use the same time as check in/out
            2. PT just time (check out - check it) so add the date to the time string  
        '''

        # if check in is missing, set the check in time = check out time
        if row[-1] == '下班' and row2[-1] == '上班':
            # change the time
            row[3] = row[1] + ' ' + row[3] # date + time
            check_in = row[3]
            row = np.insert(row, 3, check_in)
            row2 = np.insert(row, 4, '上班')
            combinerow = row2
            combinerow = np.delete(combinerow, 1)  # delete the original date
            i = i + 1

        # if check out is missing, set check out time = check in time
        elif row[-1] == '上班' and row2[-1] == '上班':
            # print('1',row)
            # print('2',row2)
            row[3] = row[1] + ' ' + row[3]
            check_in = row[-2]
            row = np.insert(row, 5, check_in)
            row2 = np.insert(row, 6, '下班')
            combinerow = row2
            combinerow = np.delete(combinerow, 1)  # delete the original date
            i = i + 1

        else:
            row[3] = row[1] + ' ' + row[3]
            row2[3] = row2[1] + ' ' + row2[3]
            combinerow = np.append(row, row2[-2:])
            combinerow = np.delete(combinerow, 1)  # delete the original date
            i = i + 2

        c_in = datetime.strptime(combinerow[2], '%Y/%m/%d %H:%M:%S')  # actual check in
        c_out = datetime.strptime(combinerow[4], '%Y/%m/%d %H:%M:%S')  # actual check out
        hour, min, sec = str(c_out - c_in).split(':')  # just need the hours

        hour = int(hour)
        min = int(min)

        # make here 40 because some people will check in earlier so the time deduction will add 0.5 hours
        if min > 30:
            final_hour = hour + 0.5  # if
        else:
            final_hour = hour

        newrow = np.append(combinerow, final_hour)
        newrowlist.append(newrow)

    newrowlist = np.array(newrowlist)
    # print(newrowlist)

    PT_worktime = {}
    for name in PT:
        workhour = 0
        for rows in range(len(newrowlist)):
            if newrowlist[rows][0] == name:
                workhour += newrowlist[rows][-1]
        PT_worktime[name] = workhour

    return PT_worktime


# main.py

def combine_shifu():

    df_shifu = pd.read_excel('紅九九員工基本資料.xlsx',sheet_name = '市府' , index_col=0)
    # print(df_shifu)
    name_order = list(df_shifu.columns.values[0:])

    ontime_bonuslist = []
    bonus_dic= ontime_bonus('shifu')

    for name in name_order:
        try:
            bonus =  bonus_dic[name]
        except:
            bonus = 0
        ontime_bonuslist.append(bonus)
    # print(ontime_bonuslist)
    # print(len(ontime_bonuslist))

    revenue_bonuslist = []
    revenue_dic = employee_bonus('shifu')

    for name in name_order:
        try:
            revenuebonus = revenue_dic[name]
        except:
            revenuebonus = 0
        revenue_bonuslist.append(revenuebonus)
    # print(revenue_bonuslist)


    # add ontime_bonus and revenue bonus
    df_shifu = df_shifu.append(pd.Series(ontime_bonuslist,index=df_shifu.columns),ignore_index=True)
    final = df_shifu.append(pd.Series(revenue_bonuslist, index=df_shifu.columns), ignore_index=True)
    # sum the salary for each employee
    salary = list(final.sum())
    # join everything to a dataframe
    shifu_salary = final.append(pd.Series(salary,index=df_shifu.columns), ignore_index=True)
    shifu_salary = shifu_salary.assign(index_name = ['底薪', '職務加給', '其他津貼', '外語/證照加給', '勞健保','全勤獎金',
                                                     '業績獎金','實際薪水'])
    shifu_salary = shifu_salary.set_index('index_name')

    return shifu_salary


def combine_yanji():
    df_yanji = pd.read_excel('紅九九員工基本資料.xlsx',sheet_name = '延吉', index_col=0)
    # print(df_yanji)
    name_order = list(df_yanji.columns.values[0:])

    ontime_bonuslist = []
    bonus_dic = ontime_bonus('yanji')

    for name in name_order:
        try:
            bonus = bonus_dic[name]
        except:
            bonus = 0
        ontime_bonuslist.append(bonus)
    # print(ontime_bonuslist)

    revenue_bonuslist = []
    revenue_dic = employee_bonus('yanji')

    for name in name_order:
        try:
            revenuebonus = revenue_dic[name]
        except:
            revenuebonus = 0
        revenue_bonuslist.append(revenuebonus)

    # add ontime_bonus and revenue bonus
    df_yanji = df_yanji.append(pd.Series(ontime_bonuslist, index=df_yanji.columns), ignore_index=True)
    final = df_yanji.append(pd.Series(revenue_bonuslist, index=df_yanji.columns), ignore_index=True)
    # sum the salary for each employee
    salary = list(final.sum())
    # join everything to a dataframe
    yanji_salary = final.append(pd.Series(salary, index=df_yanji.columns), ignore_index=True)
    yanji_salary = yanji_salary.assign(index_name=['底薪', '職務加給', '其他津貼', '外語/證照加給', '勞健保', '全勤獎金',
                                                   '業績獎金', '實際薪水'])
    yanji_salary = yanji_salary.set_index('index_name')

    return yanji_salary


def combine_PT_Shifu():

    PT_shifu = pd.read_excel('紅九九員工基本資料.xlsx',sheet_name = '市府_PT', index_col=0)
    name_order = list(PT_shifu.columns.values[0:])
    workhour_dic = PT_workhours('shifu')

    workhourslist = []
    workhourbonus = []

    for name in name_order:
        try:
            workhour = workhour_dic[name]
        except:
            workhour = 0

        if workhour > 100:
            bonus = 500
        else:
            bonus =0

        workhourslist.append(workhour)
        workhourbonus.append(bonus)

    PT_shifu = PT_shifu.append(pd.Series(workhourslist, index=PT_shifu.columns), ignore_index=True)
    salary = list(PT_shifu.cumprod().iloc[1]) # get the multiply of hours * base pay
    final = PT_shifu.append(pd.Series(salary, index=PT_shifu.columns), ignore_index=True)
    PT_shifu_salary = final.append(pd.Series(workhourbonus, index=PT_shifu.columns), ignore_index=True)

    #is there easier way for only sum row 2 and row 3?

    salary_1 = list(PT_shifu_salary.iloc[2])
    salary_2 = list(PT_shifu_salary.iloc[3])
    salar_total=[]
    for i in range(len(salary_1)):
        salary_all = salary_1[i]+salary_2[i]
        salar_total.append(salary_all)

    PT_shifu_salary= final.append(pd.Series(workhourbonus, index=PT_shifu.columns), ignore_index=True)
    PT_shifu_final = PT_shifu_salary.append(pd.Series(salar_total, index=PT_shifu.columns), ignore_index=True)
    PT_shifu_final = PT_shifu_final.assign(index_name=['時薪', '時數', '基本薪水', '時數加給','實際薪水'])
    PT_shifu_final = PT_shifu_final.set_index('index_name')

    return PT_shifu_final


def combine_PT_Yanji():

    PT_Yanji = pd.read_excel('紅九九員工基本資料.xlsx',sheet_name = '延吉_PT', index_col=0)
    name_order = list(PT_Yanji.columns.values[0:])
    workhour_dic = PT_workhours('yanji')

    workhourslist = []
    workhourbonus = []

    for name in name_order:
        try:
            workhour = workhour_dic[name]
        except:
            workhour = 0

        if workhour > 100:
            bonus = 500
        else:
            bonus = 0

        workhourslist.append(workhour)
        workhourbonus.append(bonus)

    PT_Yanji = PT_Yanji.append(pd.Series(workhourslist, index=PT_Yanji.columns), ignore_index=True)
    salary = list(PT_Yanji.cumprod().iloc[1]) # get the multiply of hours * base pay
    final = PT_Yanji.append(pd.Series(salary, index=PT_Yanji.columns), ignore_index=True)
    PT_yanji_salary = final.append(pd.Series(workhourbonus, index=PT_Yanji.columns), ignore_index=True)

    #is there easier way for only sum row 2 and row 3?

    salary_1 = list(PT_yanji_salary.iloc[2])
    salary_2 = list(PT_yanji_salary.iloc[3])
    salar_total=[]
    for i in range(len(salary_1)):
        salary_all = salary_1[i]+salary_2[i]
        salar_total.append(salary_all)

    PT_yanji_salary= final.append(pd.Series(workhourbonus, index=PT_Yanji.columns), ignore_index=True)
    PT_yanji_final = PT_yanji_salary.append(pd.Series(salar_total, index=PT_Yanji.columns), ignore_index=True)
    PT_yanji_final = PT_yanji_final.assign(index_name=['時薪', '時數', '基本薪水', '時數加給','實際薪水'])
    PT_yanji_final = PT_yanji_final.set_index('index_name')

    return PT_yanji_final

a = combine_shifu()
b = combine_yanji()
c = combine_PT_Shifu()
d = combine_PT_Yanji()


with pd.ExcelWriter(str(Month) +'月薪資表.xlsx') as writer:  # doctest: +SKIP
    a.to_excel(writer, sheet_name='市府正職')
    b.to_excel(writer, sheet_name='延吉正職')
    c.to_excel(writer, sheet_name='市府_PT')
    d.to_excel(writer, sheet_name='延吉_PT')