# import random
# alist=[random.randint(0,100) for i in range(20)]
# for i in alist:
#     print(i,alist.count(i))

# adic={'1':'a','2':'b','3':'c','4':'d','5':'e'}
# k=input('请输入键值：')
# # if k in adic.keys():
# #     print(adic[k])
# # else:
# #     print('输入的键值不在字典内。')
# print(adic.get(k,'输入的键值不在字典！'))

import random
alist=[random.randint(0,100) for i in range(20)]
print(alist)
print(sorted(alist[:10])+sorted(alist[10:],reverse=True))