import pandas as pd
pd.options.display.max_columns=999
zb=pd.read_excel('联合查询表.xlsx',sheet_name='总表',index_col='ID')
fb=pd.read_excel('联合查询表.xlsx',sheet_name='分表',index_col='ID')
# result=fb.merge(zb,how='left').fillna('找不到')
result=pd.merge(fb,zb,on='ID',how='left').fillna('找不到')
# result=fb.join(zb,on='接入号') #两个表除了index,不能有重复项
print(result)
