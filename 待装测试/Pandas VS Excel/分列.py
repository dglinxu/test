import pandas as pd
data=pd.read_excel('output2.xlsx',index_col='ID')
df=data.商品.str.split('--',expand=True)
data['商品名']=df[0].str.capitalize()
data['是否折扣']=df[1]
print(data)