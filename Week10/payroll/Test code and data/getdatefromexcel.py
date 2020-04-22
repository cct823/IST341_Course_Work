import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('108.02二店帳務.xlsx', sheetname='總表')

# print("Column headings:")
# print(df.columns)

#for i in df.index:
#    print(df['營收總和'][i])


dailyincome = list(df['營收總和'][1:32])
# print(dailyincome)
# newlist= []
# for item in dailyincome:
#     item = str(item)
#     newlist.append(item)




weekday=[]
weekend=[]

'''separate the revenue to weekday and weekend'''

for item in range(31):
    if item % 7 ==5 or item%7 ==6:
        weekend.append(dailyincome[item])
    else:
        weekday.append(dailyincome[item])


print(weekend)



# totalincome = df['當月營收'][0]
# print(totalincome)