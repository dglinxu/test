
# for i in range(100,1000):
#     la=list(map(int,str(i)))
#     num=sum([i**3 for i in la])
#     if num==i:
#         print(i)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(np.exp(obj2))
np.exp(obj2,obj2)
print(obj2)