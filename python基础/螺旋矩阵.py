#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：螺旋矩阵.py   
#E-mail: humen@189.cn
'''说明： 程序2比程序1稍快
----------------------------'''

import itertools
import time

def timing(func):
    def warpper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print('{}运行时间是：{}'.format(func.__name__,round(end-start,2)))
        return result
    return warpper
@timing
def circle(n):
    ans=[[None]*n for i in range(n)]
    i,j,k=1,0,-1
    for item in itertools.cycle(([0,1],[1,0],[0,-1],[-1,0])):
            j+=item[0]
            k+=item[1]
            while i<=n**2:
                if j<n and j>-1 and k<n and ans[j][k]==None:
                    ans[j][k]=i
                    i+=1
                    j+=item[0]
                    k+=item[1]
                    # print(j,k,'----')
                    # print(ans)
                else:
                    j-=item[0]
                    k-=item[1]
                    # print(j,k,'+++++++')
                    break
            if i>n**2:
                break
    return ans
@timing
def circle2(n):
    ans=[[None]*n for i in range(n)]
    flag=[[0,1],[1,0],[0,-1],[-1,0]]
    f=0
    j,k=0,0
    m=f%4
    for i in range(1,n**2+1):
        if j<n and j>=0 and k<n and ans[j][k]==None:
            ans[j][k]=i
        else:
            j-=flag[m][0]
            k-=flag[m][1]
            f+=1
            m=f%4
            j+=flag[m][0]
            k+=flag[m][1]
            ans[j][k]=i
        j+=flag[m][0]
        k+=flag[m][1]

    return ans

circle(10000)
circle2(10000)

# for i in circle2(6):
#     for k in i:
#         print("%d\t"%k,end='')
#     print()
