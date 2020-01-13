import pandas as pd

student=pd.read_excel('学生成绩.xlsx')
# student.drop_duplicates(subset='学号',inplace=True,keep='first')
# student=student.append(student[['科目1','科目2','科目3']])
dupe=student.duplicated(subset='学号')
# dupe=dupe[dupe==True]
dupe=dupe[dupe]                 #两种筛选方法
print(student.iloc[dupe.index]) #不能设置ID为索引