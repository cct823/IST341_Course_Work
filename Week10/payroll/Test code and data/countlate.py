import pandas as pd
import numpy as np
import datetime
import math
from datetime import datetime, timedelta


now = datetime.now()
Month = now.month - 1
Year = now.year

#
##  remove the float data when read from Pandas
#

def correct_month(Month):
    # file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'
    if 1 <=  Month <= 9:
        return '0'+str(Month)
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
    check_in_sheet=  check_in_sheet.drop('部門', axis=1) #部門==刷卡地點 so drop one

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

        NewYanji = Yanji.drop_duplicates(subset= ['員工姓名','日期','燈號狀態'],keep='first')

        for i in range(len(NewYanji['刷卡時間'])):
            if NewYanji['刷卡時間'].iloc[i][:2] == '00':
                NewYanji['燈號狀態'].iloc[i] = '下班'

        return NewYanji

    elif x=='shifu':

        check_in_sheet = readfile()
        Shifu_1 = check_in_sheet.loc[check_in_sheet['刷卡地點'] == 2]
        # Shifu = Shifu_1.loc[Shifu_1['燈號狀態'] == '上班']  #filter check in/out, only need check in

        # reason for loop, check doc string above.
        for i in range(len(Shifu_1['刷卡時間'])):
            if Shifu_1['刷卡時間'].iloc[i][:2] == '00':
                Shifu_1['燈號狀態'].iloc[i] = '隔夜下班'

        NewShifu = Shifu_1.drop_duplicates(subset= ['員工姓名','日期','燈號狀態'],keep='first')

        for i in range(len(NewShifu['刷卡時間'])):
            if NewShifu['刷卡時間'].iloc[i][:2] == '00':
                NewShifu['燈號狀態'].iloc[i] = '下班'

        ''' change the data back to normal so some of the data will have 2 check outs.'''

        return NewShifu


'''def find_Yanji():

    check_in_sheet = readfile()
    Yanji_1 =  check_in_sheet.loc[check_in_sheet['刷卡地點'] == 1]
    # Yanji = Yanji_1.loc[Yanji_1['燈號狀態'] == '上班']  # filter check in/out, only need check in
    # remove multiplce check in/out on same day
    # NewYanji = Yanji.drop_duplicates(subset= ['員工姓名','日期','燈號狀態'],keep='first')

    return Yanji_1


def find_Shifu():

    check_in_sheet = readfile()
    Shifu_1 = check_in_sheet.loc[check_in_sheet['刷卡地點'] == 2]
    # Shifu = Shifu_1.loc[Shifu_1['燈號狀態'] == '上班']  #filter check in/out, only need check in
    # remove multiplce check in/out on same day
    # NewShifu = Shifu.drop_duplicates(subset= ['員工姓名','日期','燈號狀態'],keep='first')
    return Shifu_1'''


#
#  distribute the Part time or Full time employees
#


def find_FTPT(x,y):

    '''find the PT or FT employees'''

    file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'

    if x =='yanji':
        file = pd.read_excel(file, sheet_name='延吉')
    elif x =='shifu':
        file = pd.read_excel(file, sheet_name='市府')
    else:
        print('you have the wrong input')

    FT = []
    PT = []
    name = list(file.loc[:, '姓名'])
    type = list(file.loc[:, 'PT/FT'])

    if y == 'FT':
        for i in range(len(type)):
            if type[i] =='FT':
                FT.append(name[i])
        return FT

    elif y=='PT':
        for i in range(len(type)):
            if type[i] == 'PT':
                PT.append(name[i])
        return PT
    else:
        print('you have the wrong input')


def find_basepay(x):

    '''get the base pay for all employees'''

    file = '紅九九員工基本資料.xlsx'
    if x =='yanji':
        file = pd.read_excel(file, sheet_name='延吉')
    elif x =='shifu':
        file = pd.read_excel(file, sheet_name='市府')
    else:
        print('you have the wrong input')

    names = list(file.columns.values)

    '''late time is calculate base on base and two other bonus'''
    base = list(file.iloc[0, :])  #底薪
    base_1 = list(file.iloc[1, :]) #職務加給
    base_2 = list(file.iloc[2, :]) #其他津貼（試用期滿）
    base_3 = list(file.iloc[3, :]) #外語加給

    base_all = []

    for i in range(len(base)):
        sum_all = base[i]+base_1[i]+base_2[i]+base_3[i]
        base_all.append(sum_all)

    # print(base_all)


    # base_all

    base_dic = {}
    for name in range(len(names)):
        base_dic[names[name]] = base_all[name]

    # print(base_dic)

    return base_dic


'''def Shifu_FTPT(x):

    FT = []
    PT = []

    file = pd.read_excel('紅九九班表3月(加上PT).xlsx',sheet_name='市府')
    name = list(file.loc[ :,'姓名'])
    type = list(file.loc[:,'PT/FT'])

    if x == 'FT':
        for i in range(len(type)):
            if type[i] =='FT':
                FT.append(name[i])
        return FT

    else:
        for i in range(len(type)):
            if type[i] == 'PT':
                PT.append(name[i])
        return PT

def Yanji_FTPT():
    FT = []
    PT = []

    file = pd.read_excel('紅九九班表3月(加上PT).xlsx', sheet_name='延吉')
    name = list(file.loc[:, '姓名'])
    type = list(file.loc[:, 'PT/FT'])

    if x == 'FT':
        for i in range(len(type)):
            if type[i] == 'FT':
                FT.append(name[i])
        return FT

    else:
        for i in range(len(type)):
            if type[i] == 'PT':
                PT.append(name[i])
        return PT'''
#
## getting the work shift categories
#


def get_shift():

    '''there are sharing same time shift, so dont need to distribute the branches'''

    file = correct_year(Year) + '.' + correct_month(Month) + '班表.xlsx'

    shift = pd.read_excel(file)
    name = list(shift['班別'])#.remove(float('nan'))
    time = list(shift['時段'])#.remove(float('nan'))
    shift_name = [ x for x in name if isnan(x)] #if isok(x) == True
    shift_time = [ x for x in time if isnan(x)]
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
        shift = pd.read_excel(file,sheet_name='延吉' )
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
        workshift = work_dic[name][day-1]
        shifttime = shift_dic[workshift]
        inouttime = shifttime[status]
        newrow = np.append(row, inouttime)

        # compare the check in/out with actual check in out time
        check_in_actual = datetime.strptime(newrow[-3],'%H:%M:%S')  # actual check in/out time
        suppose_to_check = datetime.strptime(newrow[-1],'%H:%M')    # suppose to check in/out before ....

        # on duty
        if newrow[-2] == '上班':
            if check_in_actual < suppose_to_check:
                latetime=0
                newrow = np.append(newrow,latetime)
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
                    latemins = latetime.seconds//60
                    newrow = np.append(newrow,latemins)
                    newrowlist.append(newrow)
        else:
            # off duty, not necessary now, so set the early leave time to 0
            '''check out but still need to append an element, so append 0'''
            latetime = 0
            newrow = np.append(newrow, latetime)
            newrowlist.append(newrow)

            # else:
            #     if check_in_actual > suppose_to_check:
            #         earlymins=0
            #         newrow = np.append(newrow,earlymins)
            #         newrowlist.append(newrow)
            #         # print(newrow)
            #     else:
            #         earlytime = suppose_to_check - check_in_actual
            #         if earlytime < timedelta(minutes=1):
            #             earlymins = 0
            #             newrow = np.append(newrow, earlymins)
            #             newrowlist.append(newrow)
            #
            #             # continue
            #         else:
            #             earlymins = earlytime.seconds//60*-1
            #             newrow = np.append(newrow,earlymins)
            #             newrowlist.append(newrow)

    # sum the late time for each person.
    newrowlist = np.array(newrowlist)
    # print(newrowlist[i][-1]) # the min position.
    # df = pd.DataFrame(data=newrowlist,columns= ['name','date','position','check_time','status','actual_time','min'])
    # print(df)
    # df.to_excel(('test.xlsx'))

    latetime_dic={}

    for name in FT:
        sumtime = 0
        for rows in range(len(newrowlist)):
            if newrowlist[rows][0] == name:
                if newrowlist[rows][-1] >300:
                    sumtime +=0
                else:
                    sumtime += newrowlist[rows][-1]
                latetime_dic[name] = sumtime
    # print(latetime_dic)
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
            bonus= (latetime - 60) * (base_all / 30 / 8 / 60)*-1
            bonus_up=math.floor(bonus)
            bonus_dic[name] = bonus_up
            # break

    return bonus_dic



def PT_workhours(x):

    '''later has to add the PT shift dic, then replace the check in time to office work hour time.'''

    PT = find_FTPT(x, 'PT')
    # print(PT)
    check_in_record = find_branches(x)
    # shift_dic = get_shift()  #EX: 'PT': {'上班': '00:00', '下班': '00:00'}}
    # print(shift_dic)
    PT_record = check_in_record[check_in_record.員工姓名.isin(PT)].values
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
        if row[-1] == '下班' and row2[-1] =='上班' :
            row[3] = row[1] + ' '+ row[3]
            check_in = row[3]
            row = np.insert(row, 3, check_in)
            row2 = np.insert(row, 4, '上班')
            combinerow = row2
            combinerow = np.delete(combinerow, 1)  # delete the original date
            i = i + 1

        # if check out is missing, set check out time = check in time
        elif row[-1] == '上班' and row2[-1] =='上班':
            # print('1',row)
            # print('2',row2)
            row[3] = row[1] + ' '+ row[3]
            check_in = row[-2]
            row = np.insert(row, 5, check_in)
            row2 = np.insert(row, 6, '下班')
            combinerow = row2
            combinerow = np.delete(combinerow, 1) # delete the original date
            i = i + 1

        else:
            row[3] = row[1] + ' ' + row[3]
            row2[3] = row2[1] + ' ' + row2[3]
            combinerow = np.append(row,row2[-2:])
            combinerow = np.delete(combinerow,1)  # delete the original date
            i = i + 2

        c_in = datetime.strptime(combinerow[2], '%Y/%m/%d %H:%M:%S')  # actual check in
        c_out = datetime.strptime(combinerow[4], '%Y/%m/%d %H:%M:%S')  # actual check out
        hour, min, sec = str(c_out - c_in).split(':')  # just need the hours

        hour = int(hour)
        min = int(min)

        if min > 30:
            final_hour = hour +0.5  # if
        else:
            final_hour = hour

        newrow = np.append(combinerow,final_hour)
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


'''
        for i in range(len(PT_record)):

    row = PT_record[i]

    if row[-1] =='上班':
        check_in = row[-2]
        y,m,day_in = row[1].split('/')
        day_in = int(day_in)

    elif row[-1] == '下班':
        check_out = row[-2]
        y, m, day_out = row[1].split('/')
        day_out = int(day_out)

    if day_in == day_out:
        if row[-1] =='上班':
            continue
        else:
            # row = np.append(row, '上班')
            # row = np.append(row,check_in)

            row = np.insert(row, 3, check_in)
            row = np.insert(row, 4, '上班')

            c_in  = datetime.strptime(row[3], '%H:%M:%S')   # actual check in
            c_out = datetime.strptime(row[5], '%H:%M:%S')   # actual check out

            hour,min,sec  = str(c_out-c_in).split(':')  # just need the hours
            newrow = np.append(row,hour)    # append hours to the data.
            newrowlist.append(newrow)

newrowlist = np.array(newrowlist)
'''



# d = FT_latemin('shifu')
# d1 = find_basepay('shifu')
d2 = ontime_bonus('yanji')
# c = FT_latemin('yanji')
# p1 = PT_workhours('yanji')

# p1 = PT_workhours('yanji')
# p2 = PT_workhours('shifu')
# # print(p1)
# print(p2)

# q= find_branches('shifu')