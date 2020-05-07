#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/5 
#开发工具：PyCharm   文件名称：约瑟夫环.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def josephQue(numlist,n):
    while len(numlist)>1:
        for i in range(n-1):
            numlist.insert(0,numlist.pop())
        numlist.pop()
    return numlist[0]

def joseph(numlist,n):
    numlist_l=len(numlist)
    index=n-1
    while numlist_l>1:
        if index>numlist_l:
            index=index%numlist_l
        numlist.pop(index)
        index+=n-1
        numlist_l=len(numlist)
    return numlist[0]


if __name__ == '__main__':
    alist=list(range(99))
    print(josephQue(alist,7))
    print(joseph(alist,7))



