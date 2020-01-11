import pandas as pd
import datetime
import random

def addMonth(date,am):
    y=am//12
    m=date.month+am%12
    if m>12:
        y=y+m//12
        m=m%12
    return datetime.date(date.year+y,m,date.day)
'''如果在读取时设置了index,那么不能对这一列进行修改，写入时也不会自动增加一列索引'''
stu=pd.read_excel('output1.xlsx',skiprows=3,usecols='d:h',index_col='Id',
                  dtype={'Id':str,'学号':str,'成绩':str,'等级':str,'日期':str})
startdate=datetime.date(2020,1,1)
for i in stu.index:
    # stu['Id'].at[i]=i+1
    stu['成绩'].at[i]=random.randrange(70,100)
    stu['等级'].at[i]='Good' if stu['成绩'].at[i]>85 else 'Bad'
    # stu['日期'].at[i]=datetime.timedelta(days=i)+startdate   #按日增加
    # stu['日期'].at[i] =datetime.date(startdate.year+1,startdate.month,startdate.day) #按年增加
    stu['日期'].at[i] = addMonth(startdate,i) #按月增加
print(stu)
# stu=stu.set_index('Id')

stu.to_excel('output2.xlsx')
# df=pd.DataFrame({'Id':[1,2,3],'Name':['阿土仔','孙小美','钱夫人']})
# df=df.set_index('Id')
# df.to_excel('pandas创建的表格.xlsx')

# dz=pd.read_excel("test.xlsx",index_col='Id')
# dz.to_excel('output.xlsx')
# print(dz.shape)
# print(dz.columns)
# print(dz.head())
# print('-'*50)
# print(dz.tail(20))

# s1=pd.Series([1,2,3],index=[1,2,3],name='A')
# s2=pd.Series([10,20,30],index=[1,2,3],name='B')
# s3=pd.Series([100,200,300],index=[1,2,3],name='C')
# df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
# df=df.set_index('A')
# df=pd.DataFrame()
# # df.to_excel('output1.xlsx')



print('Done!')