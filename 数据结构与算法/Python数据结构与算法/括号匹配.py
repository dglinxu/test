#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/5 
#开发工具：PyCharm   文件名称：括号匹配.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def bracketCheck(symbolString):
    #此程序既可以比较全部是括号的字符串，也可比较中间有其他符号的式子

    #定义开、闭括号，注意顺序
    open='{[('
    close='}])'

    flag=True
    stack=[]
    index=0
    while index<len(symbolString) and flag:
        c=symbolString[index]
        if c in open:              #字符是开括号，压人栈
            stack.append(c)
        elif c in close:           #字符是闭括号，比较栈顶字符，相符就删除栈顶符号
            if stack[-1] == open[close.index(c)]:   #根据闭括号索引找开括号
                stack.pop()
            else:
                flag=False          #不相符，退出循环，避免break
        index+=1
    return flag and stack==[]       #要注意stack不为空，不是全匹配

if __name__ == '__main__':
    s='{1{(5[][a])}(c)}'
    print(bracketCheck(s))


