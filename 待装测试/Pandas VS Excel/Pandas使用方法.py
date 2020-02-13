import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''--创建pandas的series
# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# data：数组类，可迭代对象，字典或者标量(array-like, Iterable, dict, or scalar value)。创建系列的数据。
# index：数组类或者一维的索引序列(array-like or Index (1d))。系列的索引。index必须是跟数据长度一样的离散值，可以不唯一，如果未设置则会默认为(0, 1, 2, …, n)。如果字典和索引序列同时使用，索引序列会覆盖字典的键。
# dtype：字符串，numpy.dtype或拓展的类型，可选参数。Series的数据类型。
# copy：布尔值，默认值为False。是否建立副本'''
# x = pd.Series(data=[1, 2, 3], index=list('abc'), dtype=float, name='Magic')
# print(x)
# print('the Series\'s name is:', x.name)
# print(list(x))  #直接打印数值
# print(dict(x))  #输出字典，index为键名，data为键值
# #构造字典进行输入
# d=dict(zip('abcde',range(5)))  
# y=pd.Series(d)
# print(y)

# 用Ndarray创建Series
# nd=np.array([1,2,3])
# s_nd=pd.Series(nd)
# print(s_nd)

# 用标量创建Series
# s_bx = pd.Series(2)                   #输入一个值
# s_by= pd.Series(6, index=list('abc')) # 匹配索引长度,自动填充
# print(s_bx)
# print(s_by)

'''-----选择元素-----'''
# 1. 使用下标
# x = pd.Series(range(1, 6), index=list('abcde'))
# print(x)
# print('下标2：\n', x[2],x[3])    #单独下标，输出值，无index
# print('切片[:2]：\n', x[:2])     #切片输出index和值

# 2. 使用索引
# x = pd.Series(range(1, 6), index=list('abcde'))
# print(x)
# print('索引b：\n', x['b'])                  #取单一值，可不把index框起来
# print(x[['b']])                             #index框起来就输出index和值
# print('索引a,c,d：\n', x[['a', 'c', 'd']])  #index是单独一个列表，有嵌套



'''-----基本属性-----
1. axes：返回行轴标签列表。
2. dtype：返回数据类型。
3. empty：返回系列是否为空。
4. ndim：返回数据维数。
5. size：返回元素个数。
6. values：将系列作为 ndarray 返回。
7. head()：返回前 n 行。n默认为5。
8. tail()：返回后 n 行。n默认为5。
————————————————'''
# s = pd.Series([1, 3, 4, 7,8,9,10,11,12,13,14], index=list('abcdefghijk'))
# print('axes:\n', s.axes)
# print('dtype:', s.dtype)
# print('empty:', s.empty)
# print('ndim:', s.ndim)
# print('size:', s.size)
# print('values:\n', s.values)
# print('head:\n', s.head(2))
# print('tail:\n', s.tail(2))

'''-----DataFrame（数据帧）-----
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
data：ndarray, Iterable, dict, or DataFrame。创建数据帧的数据。字典可以包括Series，数组，常数，列表对象。
index：Index or array-like。数据帧的行索引。index必须是跟数据行数一样，如果未设置则会默认为(0, 1, 2, …, n)。
columns：Index or array-like。数据帧的列标签。columns必须是跟数据列数一样，如果未设置则会默认为(0, 1, 2, …, n)。
dtype：dtype，默认值为None。数据类型。
copy：布尔值，默认值为False。是否建立副本。
————————————————
'''
# 1. 用List创建DataFrame
# x = pd.DataFrame([11, 22, 33])
# y = pd.DataFrame([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]], index=list(range(3)), columns=list('abc'))
# print(x)
# print(y)

# 2. 用字典创建DataFrame
# 字典数据要放在[]内，一个字典，一行数据，字典长度、键名可以不一致，列名是键名。
# 从左到右进行连接，不一致的键名的值用NaN填充
# a = pd.DataFrame({'a': 1, 'b': 2}, index=['A'])  # 全使用标量时必须传入index
# b = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# c = pd.DataFrame([{'a': 1, 'e': 2}, {'a': 11, 'd': 22, 'c': 33}],index=list('AB')) # 字典列表
# print('a:\n', a)
# print('b:\n', b)
# print('c:\n', c)

# 3. 用Series创建DataFrame
# 需用Series构建字典，键名是列名，值是Series
#从左往右进行连接，根据index名称分行，缺少的行值用NaN填充
# index可以不填
# d = {'Name': pd.Series(['Jhon', 'Todd'], index=['a', 'b']),
#      'Age': pd.Series(['10', '20', '30'],index=['a', 'b', 'c'])}
# df = pd.DataFrame(d)
# print(df)

# 4. 用Ndarray创建DataFrame
# 注意数组有嵌套，类似列表输入
# d = np.array([[1, 2, 3], [4, 5, 6]])
# df = pd.DataFrame(d,index=list('ab'),columns=list('ABC'))
# print(df)
# print(d)

# 5. 用DataFrame创建DataFrame
# 数值相加或者字符连接
# a = pd.DataFrame([1, 2, 3])
# b = pd.DataFrame([11, 22, 33])
# c=pd.DataFrame([55,66,77])
# df = pd.DataFrame(a + b*c)
# print(df)
# d=pd.DataFrame(list('abc'))
# e=d
# f=pd.DataFrame(d+e)
# print(f)

'''-----pd.DataFrame元素与行、列操作-----'''
'''# 选择元素--- .loc()根据标签选择元素
# 只能按行选择，不能按列选择，布尔函数选择列时，长度要与列数一致
# ['r2':'r3', 'c3':]先列后行选择数据
# [df['c3'] > 2] 只能按列取条件，C3>3的行所有元素显示出来。
# df[['b','c']][df['a']>30]筛选a列的取值大于30的记录,但是之显示满足条件的b，c列的值
# 筛选a值等于30或者54的记录df[df.a.isin([30, 54])]
# df[(df['a'] > 30) & (df['b'] > 40)]筛选a列的取值大于30，b列的取值大于40的记录
#'''
# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df.loc['r1':'r3',['c1','c4']])
# print(df.iloc[0:3,[0,3]])
# print(df)
# print('使用单个标签，返回Series：\n', df.loc['r3'])
# print('使用标签列表，返回DataFrame：\n', df.loc[['r3', 'r2']])
# print('使用布尔值列表，返回DataFrame：\n', df.loc[[False, True, False,True]])  # 注意布尔值列表长度和行数必须一样
# print('使用单个标签，返回某一行某一列交叉处的数字：\n', df.loc['r4', 'c1'])
# print('使用切片，返回DataFrame：\n', df.loc['r2':'r3', 'c3':])  # 注意首尾都包括在内
# print('使用条件选择，返回DataFrame：\n', df.loc[df['c3'] > 2])  # 注意条件这里只能用列
# print('使用条件选择，返回DataFrame：\n', df.loc[df['c1'] > 5, ['c1', 'c2']])

'''# .iloc()根据数字下标选择元素。
# 用数字代替行、列名称
# 不能进行列比较
# 两者区别：df.iloc[[0,2],[0,3]] ,df.loc[['r1','r3'],['c1','c4']]
'''

# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df)
# print('使用单个标签，返回Series：\n', df.iloc[1])
# print('使用标签列表，返回DataFrame：\n', df.iloc[[0, 2]])
# print('使用切片，返回DataFrame：\n', df.iloc[1:3, 0:2])
# print('使用单个标签，返回某一行某一列交叉处的数字：\n', df.iloc[1, 1])
# print('使用布尔值列表，返回DataFrame：\n', df.iloc[[False, True, True,False]])
# print(df.iloc[[0,2],[0,3]])
# print(df.loc[['r1','r3'],['c1','c4']])


'''# 属性选择--直接使用标签选择列。
# 直接用列名选择列，用列表或者直接用列名
# 比较结果是逻辑值'''
# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df)
# print('使用[标签]：\n', df['c2'])
# print('使用.标签：\n', df.c3)
# print(df.c3>2)

'''# 添加和删除行、列
# 行操作：df.loc['r5']直接添加，df.apend Series,删除用drop
# 列操作：df['c5']或者df.loc[:,'c5']直接添加，列可以相加，删除用del或Pop'''
# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df)
# df.loc['r5'] = [11, 22, 33, 44]  #直接添加
# print('添加第五行后:\n',df)
# df = df.append(pd.Series([55, 66, 77, 88], index=['c1', 'c2', 'c3', 'c4'], name='r6'))
# print('行添加：\n', df)
# df = df.drop('r3')  # 使用drop删除
# print('行删除：\n', df)

# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df)
# df['c11'] = pd.Series([11, 22, 33, 44], index=['r2', 'r1', 'r3', 'r4'])  # 直接添加一列
# df.iloc[:,'c5'] = df['c1'] + df['c3']  # 用另外两列相加新添一列
# print('列添加：\n', df)
# del df['c2']  # 使用del删除
# df.pop('c11')  # 使用pop删除
# print('列删除：\n', df)

'''基本属性
1. T：转置。
2. axes：返回行、列标签列表。
3. dtypes：返回数据类型。
4. empty：返回系列是否为空。
5. ndim：返回数据维数。
6. shape：返回表示DataFrame的维度的元组。
7. size：返回元素个数。
8. values：将数据帧作为 ndarray 返回。
9. head()：返回前 n 行。n默认为5。
10. tail()：返回后 n 行。n默认为5。
————————————————'''
# df = pd.DataFrame([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print('转置:\n', df.T)
# print('axes:\n', df.axes)
# print('dtype:\n', df.dtypes)
# print('empty:', df.empty)
# print('ndim:', df.ndim)
# print('shape:', df.shape)
# print('size:', df.size)
# print('values:\n', df.values)
# print('head:\n', df.head(2))
# print('tail:\n', df.tail(2))
# print('-'*50)
# print(df)
# print('-'*50)
# print(df.iloc[[0,2],[0,3]])
# print(df.loc[['r1','r3'],['c1','c4']])
# print('-'*50)
# # print(df.iloc[[0:,1:3])
# print(df[['c1','c3']])

'''-----函数-----
# count(), 非空值计数 
# DataFrame.count(self, axis=0, level=None, numeric_only=False)
# axis：0 for index, 1 for columns
# level：整数或字符串，可选参数。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为False。如果为True，只将浮点数、整数或布尔值计数。
————————————————
'''
# df = pd.DataFrame([[1, np.NaN, 'hehe', True],
#                    [5, 6, 'haha', False],
#                    [9, 10, 'enhen', True],
#                    [13, 14, 'oule', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.count(numeric_only=True))

'''sum(), 求和
# DataFrame.sum(self, axis=None, skipna=True, level=None, numeric_only=None, min_count=0, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
# level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据相加。
# min_count：整数，默认值为0。执行求和操作的最少非空值数目，如果非空值的数目小于min_count，则返回结果为空值。
# **kwargs：其他附加的关键字参数
# ————————————————
'''
# df = pd.DataFrame([[1, np.NaN, 'a', True],
#                    [5, 6, 'b', False],
#                    [9, 10, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.sum(numeric_only=True))
# print(df.sum(min_count=4))

''' mean(), 平均值
# DataFrame.mean(self, axis=None, skipna=True, level=None, numeric_only=None, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
# level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据相加。
# **kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 'a', True],
#                    [5, 6, 'b', False],
#                    [9, 10, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.mean(skipna=True))
# print(df.mean(skipna=False))

'''median(), 中位数
# DataFrame.median(self, axis=None, skipna=True, level=None, numeric_only=None, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
# level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据纳入计算。
# **kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 'a', True],
#                    [5, 6, 'b', False],
#                    [9, 10, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.median(skipna=True))
# print(df.median(skipna=False))

'''mode(), 众数
# DataFrame.mode(self, axis=0, numeric_only=False, dropna=True)
# axis：0 for index, 1 for columns
# numeric_only：布尔值，默认为False。如果为True，只将浮点数、整数或布尔值纳入计算。
# dropna：布尔值，默认为True。如果为True，则不考虑空值。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 'a', False],
#                    [1, np.NaN, 'a', False],
#                    [1, 6, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.mode(dropna=True))
# print(df.mode(dropna=False))

'''std(), 标准差(数值与均值的差的平方求和，取平方)
DataFrame.std(self, axis=None, skipna=True, level=None, ddof=1, numeric_only=None, **kwargs)
axis：0 for index, 1 for columns
skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
ddof：整数，默认值为1。自由度，除数使用的是N-ddof。（下列公式中样本个数N替换成N-ddof，r表示均值）
numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据纳入计算。
**kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 'a', False],
#                    [1, np.NaN, 'a', False],
#                    [1, 6, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.std())

'''min(), 最小值 max(), 最大值
# DataFrame.min(self, axis=None, skipna=True, level=None, numeric_only=None, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
# level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据纳入计算。
# **kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 'a', False],
#                    [1, np.NaN, 'a', False],
#                    [1, 6, 'c', True],
#                    [13, 14, 'D', False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.min())

''' abs(), 绝对值
# 求绝对值。本函数仅对数值型元素有效。如果是复数，则返回的是实部2+虚部2−−−−−−−−−√\sqrt{实部^2+虚部^2} 
# 实部 2 +虚部 2 的平方根 
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 3 + 4j, False],
#                    [-1, np.NaN, -4 + 3j, False],
#                    [1, -6, 3, True],
#                    [13, 14, 3 - 4j, False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.abs())

'''prod(), 乘积 计算各元素的乘积。
# DataFrame.prod(self, axis=None, skipna=True, level=None, numeric_only=None, min_count=0, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。
# level：整数或字符串，默认值为None。如果轴是多重索引，则沿指定层次的轴进行计数。
# numeric_only：布尔值，默认为None。如果为True，只将浮点数、整数或布尔值纳入计算。如果为None，则会尽力尝试将所有类型的数据纳入计算。
# min_count：整数，默认值为0。执行计算的最少非空值数目，如果非空值的数目小于min_count，则返回结果为空值。
# **kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 1 + 1j, False],
#                    [-1, np.NaN, -1 + 1j, False],
#                    [2, -6, 3, True],
#                    [13, 14, 1 - 1j, False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.prod())
# print('如果是空的Series，则返回结果为1\n', pd.Series().prod())

'''cumsum(), 累计和 cumprod(), 累计乘积
# DataFrame.cumsum(self, axis=None, skipna=True, *args, **kwargs)
# axis：0 for index, 1 for columns
# skipna：布尔值，默认为True。计算时是否将 NA/null 纳入计算。如果整列或者整行都是NA，则返回的结果为NA
# *args, **kwargs：其他附加的关键字参数。附加关键字参数没有实际效果，但是可能与NumPy兼容。
————————————————'''
# df = pd.DataFrame([[1, np.NaN, 1 + 1j, False],
#                    [-1, np.NaN, -1 + 1j, False],
#                    [2, -6, 3, True],
#                    [13, 14, 1 - 1j, False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.cumsum())
# print(df.cumsum(skipna=False))

'''cov(), 协方差  计算协方差。NA/null 不纳入计算。
# DataFrame.cov(self, min_periods=None)
# min_periods：整数，可选参数。参与计算的最小有效值数目。'''
# df = pd.DataFrame([[1, np.NaN, 1, False],
#                    [-1, np.NaN, 1, False],
#                    [2, -6, 1, True],
#                    [13, 14, 1, False]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df['c1'].cov(df['c2']))
# print(df.cov())
# print(df.cov(min_periods=3))

''' pct_change(), 环比，即每一个元素与上一元素的变化百分比。
# DataFrame.pct_change(self, periods=1, fill_method=‘pad’, limit=None, freq=None, **kwargs)
# periods：整数，默认值为1。即返回每一个元素与前periods个元素的变化百分比，默认值为1，即每一个元素与上一个元素的变化百分比。
# fill_method：字符串，默认值为’pad’。如何填充NA值。
# limit：整数，默认值为None。停止前要填充的NA数量。
# **kwargs：其他附加的关键字参数。
————————————————'''
# df = pd.DataFrame([[1, np.NAN, 1, 2],
#                    [2, 1, 2, 6],
#                    [3, np.NAN, 3, 5],
#                    [4, 5, 6, 3],
#                    [5, 2, 7, 9]], index=['r1', 'r2', 'r3', 'r4', 'r5'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.pct_change())
# print(df.pct_change(periods=2))

'''pct_corr(), 相关系数  计算两个数列之间的相关系数。
# DataFrame.corr(self, method=‘pearson’, min_periods=1)
# method：计算相关系数的方法。可选 ‘pearson’、‘kendall’、‘spearman’、callable
# min_periods：整数，可选参数。得到结果所需的最小的列数，仅Pearson和Spearman有用。
————————————————'''
# df = pd.DataFrame([[1, 5, 1, 2],
#                    [2, 6, 2, 6],
#                    [3, 7, 3, 5],
#                    [4, 8, 6, 3]], index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print('pearson:\n', df.corr())
# print('kendall:\n', df.corr(method='kendall'))
# print('spearman:\n', df.corr(method='spearman'))

'''sort_index(), 对标签(index)排序。
# DataFrame.sort_index(self, axis=0, level=None, ascending=True, inplace=False, kind=‘quicksort’, na_position=‘last’, sort_remaining=True)
# axis：0 for index, 1 for columns
# level：指定排序的轴level。（多重索引）
# ascending：布尔值，默认值True。True为升序，False为降序(descending)
# inplace：布尔值，默认值False。是否替代原DataFrame
# kind：{‘quicksort’, ‘mergesort’, ‘heapsort’}, 默认值 ‘quicksort’。排序算法。‘mergesort’ 是唯一的稳定算法。对于DataFrame，仅在针对单个列排序时本参数有效。
# na_position：{‘first’, ‘last’}, 默认值 ‘last’。将NA值放在前面还是后面，对多重索引无效。
# sort_remaining：布尔值，默认值True。多重索引时，在对指定Level排序后，对其他Level进行排序。
————————————————'''
# df = pd.DataFrame([[1, 5, 1, 2],
#                    [2, 9, 3, 5],
#                    [5, 7, 2, 5],
#                    [4, 8, 6, 3]], index=['d', 'a', 'b', 'c'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# df.sort_index(axis=1, ascending=False, inplace=True)
# print(df)

'''sort_values(), 按值排序
# DataFrame.sort_values(self, by, axis=0, ascending=True, inplace=False, kind=‘quicksort’, na_position=‘last’)
# by：字符串，或者字符串列表。筛选的行或列。
# axis：0 for index, 1 for columns
# ascending：布尔值或者布尔值列表，默认值True。True为升序，False为降序(descending)。如果是布尔值列表，则与by参数要一一对应。
# inplace：布尔值，默认值False。是否替代原DataFrame
# kind：{‘quicksort’, ‘mergesort’, ‘heapsort’}, 默认值 ‘quicksort’。排序算法。‘mergesort’ 是唯一的稳定算法。对于DataFrame，仅在针对单个列排序时本参数有效。
# na_position：{‘first’, ‘last’}, 默认值 ‘last’。将NA值放在前面还是后面，对多重索引无效。
————————————————'''
# df = pd.DataFrame([[1, 5, 1, 2],
#                    [2, 9, 3, 5],
#                    [5, 7, 2, 5],
#                    [4, 7, 6, 3]], index=['d', 'a', 'b', 'c'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# df.sort_values(by=['c2', 'c3'], ascending=False, inplace=True)
# print(df)

'''rank(), 排名
# 为元素数组中的每个元素生成排名。如果相同，则分配平均等级。
# DataFrame.rank(self, axis=0, method=‘average’, numeric_only=None, na_option=‘keep’, ascending=True, pct=False)
# axis：0 for index, 1 for columns
# method：{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}, 默认值 ‘average’。值相同时如何排名。average按排名的平均值；min按最小的排名；max按最大的排名；first按出现顺序排名；dense和min差不多，但是排名通常只增加1，即相同值只占一个排名位置
# numeric_only：布尔值，可选参数。是否只对数值列排名。
# na_position：{‘keep’, ‘top’, ‘bottom’}, 默认值 ‘keep’。NA值如何排名。keep对NA排名为NA；top对NA排名为最高；bottom对NA排名为最低
# ascending：布尔值，默认值True。True为升序，False为降序(descending)
# pct：布尔值，默认值False。是否以百分比形式返回排名
————————————————'''
# df = pd.DataFrame([[1, 5, 1, 2],
#                    [2, 9, 3, 5],
#                    [5, 7, 2, 5],
#                    [4, 7, 6, 3]], index=['d', 'a', 'b', 'c'], columns=['c1', 'c2', 'c3', 'c4'])
# print(df, '\n')
# print(df.rank())
# print(df.rank(method='min'))
# print(df.rank(method='first'))
# print(df.rank(method='dense'))
# print(df.rank(pct=True))

'''文本函数
1. lower(), 转小写
  Series.str.lower(self)
2. upper(), 转大写
  Series.str.upper(self)
3. len(), 字符长度
  Series.str.len(self)
4. strip(), 删除首尾指定字符
  Series.str.strip(self, to_strip=None)
to_strip：字符串或者None，默认为None。要删除的字符系列，如果是None，则默认删除空格。
————————————————'''
# s = pd.Series(['a.', '1bb', '2 cccc '])
# print(s.str.strip())
# print(s.str.strip('12.'))

'''split(), 拆分   按指定分隔符拆分。
# Series.str.split(self, pat=None, n=-1, expand=False)
# pat：字符串，可选参数。指定的分隔符，字符串或者正则表达式，如果没有指定，则默认分隔符为空格
# n：整数，默认值-1。限定拆分的次数，None、0、-1表示不限制次数，完全拆分
# expand：布尔值，默认值False。是否将结果拓展为多列。值为True时，返回结果是一个DataFrame；值为False时，返回结果是一个Series
————————————————'''
# s = pd.Series(['a.b.c.d', 'b bb', '2 c.c.cc'])
# print(s.str.split())
# print(s.str.split('.', n=1))
# print(s.str.split('.', n=2, expand=True))

'''cat(), 连结   按指定分隔符连结。
# Series.str.cat(self, others=None, sep=’’, na_rep=None, join=None)
# others：Series, Index, DataFrame, np.ndarray or list-like。必须跟原Series长度相同。
# sep：字符串，默认值为 ‘’ 。连结后，使用的分隔符。
# na_rep：字符串或None，默认值为None。缺失值如何填充。如果na_rep为None，others也为None，则缺失值就会被省略；如果na_rep为None，而others不为None，则这一行为NA值。
# join：{‘left’, ‘right’, ‘outer’, ‘inner’}, 默认值为None。指定连结的方式。others的index和原Series不一样时有效果。
————————————————'''
# s = pd.Series(['1', '2', '3', '5'])
# print(s.str.cat())
# print(s.str.cat(list('abcd')))
# print(s.str.cat(list('abcd'), sep='@'))
# print(s.str.cat(['a', np.NaN, 'c', 'd']))
# print(s.str.cat(['a', np.NaN, 'c', 'd'], na_rep='#'))
# t = pd.Series(['a', np.NaN, 'c', 'd'], index=[3, 0, 4, 2])
# print('left:\n',s.str.cat(t, na_rep='#', join='left'))
# print('right:\n',s.str.cat(t, na_rep='#', join='right'))
# print('inner:\n',s.str.cat(t, na_rep='#', join='inner'))
# print('outer:\n',s.str.cat(t, na_rep='#', join='outer'))

'''get_dummies(), 哑变量
# Series.str.get_dummies(self, sep=’|’)
# sep：字符串，默认为 ‘|’。分隔符'''
# s = pd.Series(['a|c', 'b', 'c', 'a|b'])
# print(s.str.get_dummies())

'''contains(), 检查Series中是否包含指定正则表达式的内容。
# Series.str.contains(self, pat, case=True, flags=0, na=nan, regex=True)
# pat：字符串。字符序列或者正则表达式。
# case：布尔值，默认值为True。是否大小写敏感。
# flags：整数，默认值为0。正则表达式的flags，例如re.IGNORECASE。
# na：默认值NaN。缺失值用什么填充。
# regex：布尔值，默认为True。值为True时，确保pat是一个正则表达式；值为False，将pat视为字符串。
————————————————'''
# s = pd.Series(['aBd', 'aC', 'bbb', 'bc'])
# print(s.str.contains('c'))
# print(s.str.contains('c', case=False))

''' replace(), 按指定正则表达式进行替换。
# Series.str.replace(self, pat, repl, n=-1, case=None, flags=0, regex=True)
# pat：字符串。字符序列或者正则表达式。
# repl：字符串或callable。将目标替换成repl。
# n：整数，默认值为-1（全部替换）。替换的个数。
# case：布尔值，默认值为True。是否大小写敏感。
# flags：整数，默认值为0。正则表达式的flags，例如re.IGNORECASE。
# regex：布尔值，默认为True。值为True时，确保pat是一个正则表达式；值为False，将pat视为字符串。
————————————————'''
# s = pd.Series(['aBd', 'aC', 'bbb', 'bc'])
# print(s.str.replace('c', '1'))
# print(s.str.replace('c', '2', case=False))

'''repeat(), 重复
# Series.str.repeat(self, repeats)
# repeats：整数或整数列表。重复次数。'''
# s = pd.Series(['a', 'b', 'c', 'd'])
# print(s.str.repeat(repeats=2))
# print(s.str.repeat(repeats=[1, 2, 3, 4]))

'''count(), 指定模式出现的次数。
# Series.str.count(self, pat, flags=0, **kwargs)
# pat：字符串。正则表达式。
# flags：整数，默认值为0。正则表达式的flags，例如re.IGNORECASE。'''
# s = pd.Series(['ab1', 'bb', 'bc3', 'd'])
# print(s.str.count('b'))
# print(s.str.count('\d'))

'''find(), 返回指定模式第一次出现的位置。
# Series.str.find(self, sub, start=0, end=None)
# sub：字符串。需要搜索的子字符串。
# start：整数。开始搜索的位置。
# end：整数。结束搜索的位置。'''
# s = pd.Series(['ab1', 'bb', 'c3b', 'd'])
# print(s.str.find('b'))
# print(s.str.find('b', start=1, end=2))

''' findall(), 查找所有符合模式的字符串，形成列表。
Series.str.findall(self, pat, flags=0, **kwargs)
pat：字符串。正则表达式。
flags：整数，默认值为0。正则表达式的flags，例如re.IGNORECASE。
————————————————'''
# s = pd.Series(['ab1', 'bb', 'c3b', 'd'])
# print(s.str.findall('b'))

'''line(), 折线图
# DataFrame.plot.line(self, x=None, y=None, **kwargs)
# x：可选参数。x轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的index序列。
# y：可选参数。y轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的所有数值列。
————————————————'''
# df = pd.DataFrame([[1, 3],
#                    [3, 8],
#                    [4, 6],
#                    [10, 12]], index=['a', 'b', 'c', 'd'], columns=['X', 'Y'])
# print(df)
# df.plot.line()
# df.plot.line(x='X', y='Y')
# plt.show()  # PyCharm中，必须加上这一项才会显示图片

'''bar(), 条形图
# DataFrame.plot.bar(self, x=None, y=None, **kwargs)
# x：可选参数。x轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的index序列。
# y：可选参数。y轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的所有数值列。
————————————————'''
# df = pd.DataFrame([[1, 3],
#                    [3, 8],
#                    [4, 6],
#                    [10, 12]], index=['a', 'b', 'c', 'd'], columns=['X', 'Y'])
# print(df)
# df.plot.bar(rot=0)  # 实测要有rot=0，横坐标才不会倒着
# df.plot.bar(rot=0, subplots=True)  # 拆分显示
# df.plot.bar(rot=0, stacked=True)  # 堆积
# df.plot.bar(x='X', y='Y')  # 没有rot=0，横坐标会倒着
# plt.show()

'''barh(), 水平条形图
# DataFrame.plot.barh(self, x=None, y=None, **kwargs)
# x：可选参数。x轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的index序列。
# y：可选参数。y轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的所有数值列。
————————————————'''
# df = pd.DataFrame([[1, 3],
#                    [3, 8],
#                    [4, 6],
#                    [10, 12]], index=['a', 'b', 'c', 'd'], columns=['X', 'Y'])
# print(df)
# df.plot.barh()
# plt.show()

'''hist(), 直方图
# DataFrame.plot.hist(self, by=None, bins=10, **kwargs)
# by：字符串，可选参数。分组的列。（这个参数没有弄懂）
# bins：整数，默认值为10。直方图的箱数。'''
# df = pd.DataFrame(np.random.randint(1, 7, 10000), columns=['a'])
# df['b'] = df['a'] + np.random.randint(1, 7, 10000)
# df.plot.hist(bins=12, alpha=0.5)  # 透明度0.5
# plt.show()

'''box(), 箱型图'''
# df = pd.DataFrame([[1, 3, 4, 7],
#                    [3, 7, 4, 9],
#                    [4, 5, 9, 2],
#                    [7, 9, 2, 1]], columns=['A', 'B', 'C', 'D'])
# print(df)
# df.plot.box()
# plt.show()

'''area(), 面积图
# DataFrame.plot.area(self, x=None, y=None, stacked=True, **kwargs)
# x：可选参数。x轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的index序列。
# y：可选参数。y轴所使用的列，既可使用位置下标，也可使用标签。缺省时，使用的是DataFrame的所有列。
stacked：布尔值，默认为True。是否累计。
————————————————'''
# df = pd.DataFrame([[1, 3, 4, 7],
#                    [3, 7, 4, 9],
#                    [4, 5, 9, 2],
#                    [7, 9, 2, 1]], columns=['A', 'B', 'C', 'D'])
# print(df)
# df.plot.area()
# df.plot.area(y=['A'])
# df.plot.area(stacked=False)
# plt.show()

'''scatter(), 散点图
# DataFrame.plot.scatter(self, x, y, s=None, c=None, **kwargs)
# x：整数或字符串。横轴使用的列。
# y：整数或字符串。纵轴使用的列。
# s：数字或数字列表，可选参数。每个点的大小。如果是一个数字，则是设置所有点的大小；如果是一个列表，则是设置对应每个点的大小。
# c：字符串、整数或列表，可选参数。每个点的颜色。与s参数的设置方法类似，可以使用颜色名字例如’red’，也可以使用RGB编码例如’#a98d19’。
————————————————'''
# df = pd.DataFrame([[1, 3, 4, 7],
#                    [3, 6, 4, 9],
#                    [4, 8, 9, 2],
#                    [7, 13, 2, 1]], columns=['A', 'B', 'C', 'D'])
# df.plot.scatter(x='A', y='B', s=[10, 30, 50, 100], c='green')
# plt.show()

'''pie(), 饼状图
# DataFrame.plot.pie(self, y=None, subplots=None, **kwargs)
# y：整数或标签，可选参数。用于绘图的列，如果本参数没有设置，则subplots=True必须传递。'''
# df = pd.DataFrame([[1, 3, 4, 7],
#                    [3, 6, 4, 9],
#                    [4, 8, 9, 2],
#                    [7, 13, 2, 1]], index=['r1', 'r2', 'r3', 'r4'], columns=['A', 'B', 'C', 'D'])
# df.plot.pie(y='A')
# df.plot.pie(subplots=True)
# plt.show()


