import pandas as pd
df=pd.DataFrame({'Id':[1,2,3],'Name':['阿土仔','孙小美','钱夫人']})
df=df.set_index('Id')
df.to_excel('pandas创建的表格.xlsx')
print('Done!')