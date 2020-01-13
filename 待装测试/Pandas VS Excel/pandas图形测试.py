import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
pic=pd.read_excel('picture.xlsx')
pic.plot.bar(x='商品',y='价格',color='pink')
plt.xlabel('商   品',fontsize=15,fontweight='bold',color='orange')
plt.ylabel('价   格',fontsize=15,fontweight='bold',color='green')
plt.title('阿土仔网店12月销售情况',fontsize=16,fontweight='bold',color='red')
plt.xticks(rotation='45',color='blue')
plt.yticks(rotation='45',color='blue')
plt.show()