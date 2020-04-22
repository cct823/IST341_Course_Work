from countbonus import *
from countlate import *
import pandas as pd

# p1 = PT_workhours('yanji')
# p2 = PT_workhours('shifu')
# # print(p1)
# print(p2)

# bonus_dic= ontime_bonus('shifu')
# b = employee_bonus('shifu')
# print(d3)
# print(b)

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


