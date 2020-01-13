import pandas as pd

student=pd.read_excel('学生成绩.xlsx',index_col='学号')
data=student[['科目1','科目2','科目3']]
row_sum=data.sum(axis=1)
row_mean=data.mean(axis=1)
student['总分']=row_sum
student['平均分']=row_mean
col_mean=student[['科目1','科目2','科目3','总分','平均分']].mean(axis=0)
col_mean['学号']='各科平均'
student=student.append(col_mean,ignore_index=True)
student['科目1']=student['科目1'].astype(int)
temp=student.transpose()
print(student)
print(temp)