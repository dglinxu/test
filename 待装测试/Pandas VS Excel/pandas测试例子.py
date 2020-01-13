import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=16)

pict=pd.read_excel('picture.xlsx')
pict.sort_values(by='价格',inplace=True)
pict.plot.bar(x='商品',y='价格',title='6month price')
# plt.bar(pict.商品,pict.价格,color='green')
plt.xticks(pict.商品,rotation='45')
plt.xlabel('spmc',fontsize=15,color='red')
plt.ylabel('价  格',fontproperties=font_set,color='blue')
plt.title('title',fontsize=20,color='red')
plt.tight_layout()
plt.show()


'''筛选'''
# price=pd.read_excel('output2.xlsx',index_col='Id')
# price=price.loc[price['价格'].apply(lambda x:110<x<120)].loc[price.喜好.apply(lambda x:x=='Y')]
# # price=price.loc[price.价格.apply(lambda x:110<x)]
# print(price)

''' 排序  '''
# price=pd.read_excel('output2.xlsx',index_col='Id')
# price.sort_values(by=['喜好','价格'],inplace=True,ascending=[True,False])
# print(price)
''' 运算  '''
# price=pd.read_excel('output2.xlsx',index_col='Id')
# price['价格']=price['价格'].apply(lambda x:x+10)
# price['售价']=price['价格']*price['折扣']
# price['商品']=price['商品']+'--折扣商品'
# price.to_excel('output2.xlsx')

''' 填充  '''
# def addMonth(date,am):
#     y=am//12
#     m=date.month+am%12
#     if m>12:
#         y=y+m//12
#         m=m%12
#     return datetime.date(date.year+y,m,date.day)
# """如果在读取时设置了index,那么不能对这一列进行修改，写入时也不会自动增加一列索引"""
# stu=pd.read_excel('output1.xlsx',skiprows=3,usecols='d:h',index_col='Id',
#                   dtype={'Id':str,'学号':str,'成绩':str,'等级':str,'日期':str})
# startdate=datetime.date(2020,1,1)
# for i in stu.index:
#     # stu['Id'].at[i]=i+1
#     stu.at[i,'成绩']=random.randrange(70,100) #有两种赋值形式，注意顺序
#     stu['等级'].at[i]='Good' if stu['成绩'].at[i]>85 else 'Bad'
#     # stu['日期'].at[i]=datetime.timedelta(days=i)+startdate   #按日增加
#     # stu['日期'].at[i] =datetime.date(startdate.year+1,startdate.month,startdate.day) #按年增加
#     stu['日期'].at[i] = addMonth(startdate,i) #按月增加
# print(stu)
# # stu=stu.set_index('Id')
#

''' 创建表格  '''
# stu.to_excel('output2.xlsx')
# df=pd.DataFrame({'Id':[1,2,3],'Name':['阿土仔','孙小美','钱夫人']})
# df=df.set_index('Id')
# df.to_excel('pandas创建的表格.xlsx')
''' 读取表格  '''
# pd.options.display.max_columns=999
# dz=pd.read_excel("test.xlsx",index_col='Id')
# dz.to_excel('output.xlsx')
# print(dz.shape)
# print(dz.columns)
# print(dz.head())
# print('-'*50)
# print(dz.tail(20))
''' 由序列生成表格  '''
# s1=pd.Series([1,2,3],index=[1,2,3],name='A')
# s2=pd.Series([10,20,30],index=[1,2,3],name='B')
# s3=pd.Series([100,200,300],index=[1,2,3],name='C')
# df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
# df=df.set_index('A')
# df=pd.DataFrame()
# # df.to_excel('output1.xlsx')



print('Done!')