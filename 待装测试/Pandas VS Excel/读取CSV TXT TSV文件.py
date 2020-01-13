import pandas as pd

csv=pd.read_csv('学生成绩.csv',index_col='ID',encoding='gbk')
print(csv)
tsv=pd.read_csv('学生成绩.tsv',sep='\t',index_col='ID',encoding='gbk')
print(tsv)
# csv=pd.read_csv('学生成绩.txt',index_col='ID',encoding='gbk')
# print(csv)